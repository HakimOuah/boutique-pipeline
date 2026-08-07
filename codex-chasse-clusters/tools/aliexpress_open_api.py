#!/usr/bin/env python3
"""Client en lecture seule pour les API officielles AliExpress actuelles.

Deux niveaux sont pris en charge :

* AE-Affiliate : variantes, prix TTC et livraison, sans jeton acheteur ;
* AE-Dropshipper : stock par SKU et informations vendeur, avec jeton acheteur.

Les secrets sont lus uniquement depuis l'environnement :
  ALIEXPRESS_APP_KEY
  ALIEXPRESS_APP_SECRET
  ALIEXPRESS_ACCESS_TOKEN  # requis uniquement pour AE-Dropshipper
  ALIEXPRESS_REFRESH_TOKEN # requis uniquement pour renouveler le jeton
  ALIEXPRESS_CALLBACK_URL  # URL déclarée dans l'application Open Platform

Le client ne contient volontairement aucune fonction de panier, commande,
paiement, message fournisseur ou mutation de catalogue.
"""

from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import os
import secrets
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any, Iterable, Mapping


DEFAULT_ENDPOINT = "https://api-sg.aliexpress.com/sync"
DEFAULT_REST_ENDPOINT = "https://api-sg.aliexpress.com/rest"
AUTHORIZATION_ENDPOINT = "https://api-sg.aliexpress.com/oauth/authorize"
TOKEN_CREATE_PATH = "/auth/token/create"
TOKEN_REFRESH_PATH = "/auth/token/refresh"
AFFILIATE_SKU_METHOD = "aliexpress.affiliate.product.sku.detail.get"
AFFILIATE_SHIPPING_METHOD = "aliexpress.affiliate.product.shipping.get"
DS_PRODUCT_METHOD = "aliexpress.ds.product.get"
DS_FREIGHT_METHOD = "aliexpress.ds.freight.query"
SIGN_METHOD = "sha256"
SYSTEM_PARAMETERS = {
    "method",
    "app_key",
    "timestamp",
    "access_token",
    "session",
    "sign_method",
    "sign",
    "v",
    "format",
    "simplify",
}
IOP_SYSTEM_PARAMETERS = {
    "app_key",
    "timestamp",
    "access_token",
    "sign_method",
    "sign",
    "simplify",
}


class ConfigurationError(RuntimeError):
    """Raised when required credentials are absent."""


@dataclass(frozen=True)
class Credentials:
    app_key: str
    app_secret: str
    access_token: str = ""
    refresh_token: str = ""

    @classmethod
    def from_environment(
        cls,
        require_access_token: bool = False,
        require_refresh_token: bool = False,
    ) -> "Credentials":
        values = {
            "app_key": os.environ.get("ALIEXPRESS_APP_KEY", "").strip(),
            "app_secret": os.environ.get("ALIEXPRESS_APP_SECRET", "").strip(),
            "access_token": os.environ.get("ALIEXPRESS_ACCESS_TOKEN", "").strip(),
            "refresh_token": os.environ.get("ALIEXPRESS_REFRESH_TOKEN", "").strip(),
        }
        missing = []
        if not values["app_key"]:
            missing.append("ALIEXPRESS_APP_KEY")
        if not values["app_secret"]:
            missing.append("ALIEXPRESS_APP_SECRET")
        if require_access_token and not values["access_token"]:
            missing.append("ALIEXPRESS_ACCESS_TOKEN")
        if require_refresh_token and not values["refresh_token"]:
            missing.append("ALIEXPRESS_REFRESH_TOKEN")
        if missing:
            raise ConfigurationError("Variables manquantes : " + ", ".join(missing))
        return cls(**values)


def _required_environment(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise ConfigurationError(f"Variable manquante : {name}")
    return value


def _timestamp_ms() -> str:
    """Return the millisecond timestamp used by the current IOP SDK."""
    return str(int(time.time() * 1000))


def signature_payload(params: Mapping[str, Any], api_name: str = "") -> bytes:
    """Build the ASCII-sorted payload used by AliExpress IOP/TOP.

    The current official SDK signs the API path as a prefix for GOP calls. For
    TOP calls (used here), the method is itself a signed parameter and
    ``api_name`` stays empty.
    """
    chunks: list[str] = [api_name]
    for key in sorted(params):
        value = params[key]
        if key == "sign" or value is None or value == "":
            continue
        chunks.extend((str(key), str(value)))
    return "".join(chunks).encode("utf-8")


def sign_params(
    params: Mapping[str, Any], app_secret: str, sign_method: str = SIGN_METHOD,
    api_name: str = "",
) -> str:
    """Sign a request exactly like the current official Java IOP SDK.

    Despite the wire value ``sign_method=sha256``, the SDK applies
    HMAC-SHA256 with the App Secret as key.
    """
    if sign_method not in ("sha256", "HmacSHA256", "hmac-sha256"):
        raise ValueError(f"Méthode de signature non prise en charge : {sign_method}")
    payload = signature_payload(params, api_name)
    return hmac.new(app_secret.encode("utf-8"), payload, hashlib.sha256).hexdigest().upper()


def build_authorization_url(
    app_key: str,
    callback_url: str,
    state: str,
    force_auth: bool = True,
    authorization_endpoint: str = AUTHORIZATION_ENDPOINT,
) -> str:
    """Build the official OAuth URL without transmitting any secret."""
    parsed_callback = urllib.parse.urlsplit(callback_url)
    if parsed_callback.scheme not in ("http", "https") or not parsed_callback.netloc:
        raise ValueError("ALIEXPRESS_CALLBACK_URL doit être une URL HTTP(S) absolue")
    if not app_key.strip():
        raise ConfigurationError("Variable manquante : ALIEXPRESS_APP_KEY")
    if not state.strip():
        raise ValueError("État OAuth vide")
    params = {
        "response_type": "code",
        "force_auth": "true" if force_auth else "false",
        "redirect_uri": callback_url,
        "client_id": app_key,
        "state": state,
    }
    return authorization_endpoint + "?" + urllib.parse.urlencode(params)


def _build_iop_request(
    credentials: Credentials,
    api_path: str,
    business_params: Mapping[str, Any],
    timestamp: str | None = None,
) -> dict[str, str]:
    params = {
        "app_key": credentials.app_key,
        "timestamp": timestamp or _timestamp_ms(),
        "sign_method": SIGN_METHOD,
        "simplify": "true",
    }
    for key, value in business_params.items():
        if value is not None and str(value) != "":
            params[str(key)] = str(value)
    params["sign"] = sign_params(
        params, credentials.app_secret, api_name=api_path
    )
    return params


def build_token_create_request(
    credentials: Credentials,
    code: str,
    timestamp: str | None = None,
) -> dict[str, str]:
    if not code.strip():
        raise ValueError("Code OAuth vide")
    return _build_iop_request(
        credentials, TOKEN_CREATE_PATH, {"code": code}, timestamp
    )


def build_token_refresh_request(
    credentials: Credentials,
    refresh_token: str | None = None,
    timestamp: str | None = None,
) -> dict[str, str]:
    token = (refresh_token or credentials.refresh_token).strip()
    if not token:
        raise ConfigurationError("Variable manquante : ALIEXPRESS_REFRESH_TOKEN")
    return _build_iop_request(
        credentials, TOKEN_REFRESH_PATH, {"refresh_token": token}, timestamp
    )


def _common_params(
    credentials: Credentials,
    method: str,
    require_access_token: bool,
    timestamp: str | None = None,
) -> dict[str, str]:
    if require_access_token and not credentials.access_token:
        raise ConfigurationError("Variable manquante : ALIEXPRESS_ACCESS_TOKEN")
    params = {
        "method": method,
        "app_key": credentials.app_key,
        "timestamp": timestamp or _timestamp_ms(),
        "v": "2.0",
        "format": "json",
        "simplify": "true",
        "sign_method": SIGN_METHOD,
    }
    if credentials.access_token:
        # The live-validated Drop Shipping gateway expects the OAuth token
        # under the historical TOP name ``session``.
        params["session"] = credentials.access_token
    return params


def _finish_request(params: dict[str, str], app_secret: str) -> dict[str, str]:
    params["sign"] = sign_params(params, app_secret)
    return params


def build_affiliate_skus_request(
    credentials: Credentials,
    item_id: str,
    ship_to: str = "FR",
    currency: str = "EUR",
    language: str = "FR",
    include_delivery: bool = True,
    sku_ids: Iterable[str] | None = None,
    timestamp: str | None = None,
) -> dict[str, str]:
    params = _common_params(credentials, AFFILIATE_SKU_METHOD, False, timestamp)
    params.update(
        {
            "ship_to_country": ship_to.upper(),
            "product_id": str(item_id),
            "target_currency": currency.upper(),
            "target_language": language.upper(),
            "need_deliver_info": "Yes" if include_delivery else "No",
        }
    )
    if sku_ids:
        params["sku_ids"] = ",".join(str(sku_id) for sku_id in sku_ids)
    return _finish_request(params, credentials.app_secret)


def build_affiliate_shipping_request(
    credentials: Credentials,
    item_id: str,
    sku_id: str,
    target_sale_price: str,
    tax_rate: str,
    ship_to: str = "FR",
    currency: str = "EUR",
    language: str = "FR",
    timestamp: str | None = None,
) -> dict[str, str]:
    params = _common_params(credentials, AFFILIATE_SHIPPING_METHOD, False, timestamp)
    params.update(
        {
            "product_id": str(item_id),
            "sku_id": str(sku_id),
            "ship_to_country": ship_to.upper(),
            "target_currency": currency.upper(),
            "target_sale_price": str(target_sale_price),
            "target_language": language.upper(),
            "tax_rate": str(tax_rate),
        }
    )
    return _finish_request(params, credentials.app_secret)


def build_ds_product_request(
    credentials: Credentials,
    item_id: str,
    ship_to: str = "FR",
    currency: str = "EUR",
    language: str = "fr",
    timestamp: str | None = None,
) -> dict[str, str]:
    params = _common_params(credentials, DS_PRODUCT_METHOD, True, timestamp)
    params.update(
        {
            "ship_to_country": ship_to.upper(),
            "product_id": str(item_id),
            "target_currency": currency.upper(),
            "target_language": language.lower(),
            "remove_personal_benefit": "true",
        }
    )
    return _finish_request(params, credentials.app_secret)


# Backward-compatible name used by the first prototype and its tests.
build_product_request = build_ds_product_request


def build_freight_request(
    credentials: Credentials,
    item_id: str,
    ship_to: str = "FR",
    quantity: int = 1,
    currency: str = "EUR",
    sku_id: str | None = None,
    language: str = "fr_FR",
    timestamp: str | None = None,
) -> dict[str, str]:
    if not sku_id:
        raise ValueError("sku_id numérique requis pour le fret")
    query: dict[str, Any] = {
        "quantity": str(int(quantity)),
        "shipToCountry": ship_to.upper(),
        "productId": str(item_id),
        "provinceCode": "",
        "cityCode": "",
        "selectedSkuId": str(sku_id),
        "language": language,
        "currency": currency.upper(),
        "locale": language,
    }

    params = _common_params(credentials, DS_FREIGHT_METHOD, True, timestamp)
    params["queryDeliveryReq"] = json.dumps(
        query, ensure_ascii=False, separators=(",", ":")
    )
    return _finish_request(params, credentials.app_secret)


def _request_url(endpoint: str, system_params: Mapping[str, Any]) -> str:
    query = urllib.parse.urlencode(system_params)
    separator = "&" if "?" in endpoint else "?"
    return endpoint + separator + query


def post_top_request(
    endpoint: str, params: Mapping[str, Any], timeout: int = 30
) -> dict[str, Any]:
    """Send one TOP request: common parameters in URL, business data in body."""
    system = {key: value for key, value in params.items() if key in SYSTEM_PARAMETERS}
    business = {key: value for key, value in params.items() if key not in SYSTEM_PARAMETERS}
    encoded = urllib.parse.urlencode(business).encode("utf-8")
    request = urllib.request.Request(
        _request_url(endpoint, system),
        data=encoded,
        headers={"Content-Type": "application/x-www-form-urlencoded;charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        if not body:
            raise RuntimeError(f"Passerelle AliExpress : HTTP {exc.code}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Passerelle AliExpress inaccessible : {exc.reason}") from exc

    try:
        return json.loads(body)
    except json.JSONDecodeError as exc:
        raise RuntimeError("Réponse AliExpress non JSON") from exc


def post_iop_request(
    rest_endpoint: str,
    api_path: str,
    params: Mapping[str, Any],
    timeout: int = 30,
) -> dict[str, Any]:
    """Send an IOP path request such as /auth/token/create or refresh."""
    system = {
        key: value for key, value in params.items() if key in IOP_SYSTEM_PARAMETERS
    }
    business = {
        key: value for key, value in params.items() if key not in IOP_SYSTEM_PARAMETERS
    }
    request_url = rest_endpoint.rstrip("/") + "/" + api_path.lstrip("/")
    encoded = urllib.parse.urlencode(business).encode("utf-8")
    request = urllib.request.Request(
        _request_url(request_url, system),
        data=encoded,
        headers={"Content-Type": "application/x-www-form-urlencoded;charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        if not body:
            raise RuntimeError(f"Passerelle OAuth AliExpress : HTTP {exc.code}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(
            f"Passerelle OAuth AliExpress inaccessible : {exc.reason}"
        ) from exc

    try:
        return json.loads(body)
    except json.JSONDecodeError as exc:
        raise RuntimeError("Réponse OAuth AliExpress non JSON") from exc


def probe_gateway(endpoint: str, item_id: str, timeout: int = 20) -> dict[str, Any]:
    """Network-only probe; intentionally credential-free and read-only."""
    return post_top_request(
        endpoint,
        {
            "method": AFFILIATE_SKU_METHOD,
            "product_id": str(item_id),
            "ship_to_country": "FR",
            "target_currency": "EUR",
            "target_language": "FR",
            "need_deliver_info": "Yes",
        },
        timeout=timeout,
    )


def redact_request(params: Mapping[str, Any]) -> dict[str, Any]:
    redacted = dict(params)
    for key in ("access_token", "refresh_token", "session", "sign", "code"):
        if key in redacted:
            redacted[key] = "***"
    return redacted


def redact_token_response(value: Any) -> Any:
    """Recursively mask OAuth material while preserving diagnostics/expiry."""
    if isinstance(value, Mapping):
        return {
            key: "***"
            if key in {"access_token", "refresh_token"}
            else redact_token_response(item)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [redact_token_response(item) for item in value]
    return value


def _dig_result(response: Mapping[str, Any]) -> Mapping[str, Any]:
    """Find the DS product result across simplified and wrapped responses."""
    candidates: list[Any] = [response]
    while candidates:
        candidate = candidates.pop(0)
        if not isinstance(candidate, Mapping):
            continue
        if "ae_item_sku_info_dtos" in candidate:
            return candidate
        for key in ("aliexpress_ds_product_get_response", "resp_result", "result"):
            value = candidate.get(key)
            if isinstance(value, Mapping):
                candidates.append(value)
    raise ValueError("Réponse DS sans bloc produit exploitable")


def _list_from_container(value: Any, *keys: str) -> list[Mapping[str, Any]]:
    """Accept both simplified lists and the wrappers used by older TOP replies."""
    if isinstance(value, list):
        return [item for item in value if isinstance(item, Mapping)]
    if isinstance(value, Mapping):
        for key in keys:
            nested = value.get(key)
            if isinstance(nested, list):
                return [item for item in nested if isinstance(item, Mapping)]
            if isinstance(nested, Mapping):
                return [nested]
    return []


def _first_present(mapping: Mapping[str, Any], *keys: str) -> Any:
    """Return the first present value, preserving meaningful zeroes and false."""
    for key in keys:
        if key in mapping and mapping[key] is not None:
            return mapping[key]
    return None


def normalize_ds_product(response: Mapping[str, Any]) -> dict[str, Any]:
    """Normalize exact SKU truth needed by the sourcing workflow."""
    result = _dig_result(response)
    base = result.get("ae_item_base_info_dto") or {}
    store = result.get("ae_store_info") or {}
    normalized_skus = []
    raw_skus = _list_from_container(
        result.get("ae_item_sku_info_dtos") or [],
        "ae_item_sku_info_d_t_o",
        "aeop_ae_product_sku",
    )
    for sku in raw_skus:
        properties = []
        raw_properties = _list_from_container(
            sku.get("ae_sku_property_dtos")
            or sku.get("aeop_s_k_u_propertys")
            or sku.get("aeop_s_k_u_property_list")
            or [],
            "ae_sku_property_d_t_o",
            "aeop_sku_property",
        )
        for prop in raw_properties:
            properties.append(
                {
                    "name": prop.get("sku_property_name"),
                    "value": prop.get("property_value_definition_name")
                    or prop.get("sku_property_value"),
                    "image": prop.get("sku_image"),
                }
            )
        normalized_skus.append(
            {
                "sku_id": _first_present(sku, "sku_id", "id"),
                "sku_attr": _first_present(sku, "sku_attr", "id"),
                "properties": properties,
                "stock": _first_present(
                    sku,
                    "sku_available_stock",
                    "s_k_u_available_stock",
                    "ipm_sku_stock",
                ),
                "price": _first_present(sku, "offer_sale_price", "sku_price"),
                "currency": sku.get("currency_code"),
                "tax_included": sku.get("price_include_tax"),
                "image": next((p.get("image") for p in properties if p.get("image")), None),
            }
        )
    return {
        "product_id": base.get("product_id"),
        "title": base.get("subject"),
        "status": base.get("product_status_type"),
        "rating": base.get("avg_evaluation_rating"),
        "evaluation_count": base.get("evaluation_count"),
        "store": {
            "id": store.get("store_id"),
            "name": store.get("store_name"),
            "item_as_described_rating": _first_present(
                store, "item_as_described_rating", "item_as_descriped_rating"
            ),
            "communication_rating": store.get("communication_rating"),
            "shipping_speed_rating": store.get("shipping_speed_rating"),
            "country": store.get("store_country_code"),
        },
        "skus": normalized_skus,
    }


def _normalized_selector(value: Any) -> str:
    return " ".join(str(value or "").casefold().replace("_", " ").split())


def _compact_property(value: Any) -> str:
    """Ignore supplier punctuation/spacing without translating property words."""
    return "".join(char for char in _normalized_selector(value) if char.isalnum())


def _property_matches(selector: str, prop: Mapping[str, Any]) -> bool:
    """Match a selector inside one property value, never across all labels.

    Keeping each property isolated avoids false positives such as ``cat``
    matching the property name ``Spécification``. A supplier may add harmless
    words around a value, so a compact selector can be contained in the value
    or in the explicit ``name + value`` pair.
    """
    value = _compact_property(prop.get("value"))
    name = _compact_property(prop.get("name"))
    if not selector:
        return False
    if selector in value:
        return True
    return bool(name) and selector.startswith(name) and selector[len(name):] in value


def select_exact_sku(
    product: Mapping[str, Any],
    sku_id: str | None = None,
    required_properties: Iterable[str] | None = None,
) -> dict[str, Any]:
    """Select one SKU and fail closed when the requested variant is ambiguous."""
    wanted_id = _normalized_selector(sku_id)
    wanted_properties = [
        _compact_property(value)
        for value in (required_properties or [])
        if _compact_property(value)
    ]
    if not wanted_id and not wanted_properties:
        raise ValueError(
            "Sélecteur de variante requis : --sku-id ou au moins un --property"
        )

    matches = []
    for sku in product.get("skus") or []:
        candidate_ids = {
            _normalized_selector(sku.get("sku_id")),
            _normalized_selector(sku.get("sku_attr")),
        }
        if wanted_id and wanted_id not in candidate_ids:
            continue
        properties = sku.get("properties") or []
        if not all(
            any(_property_matches(value, prop) for prop in properties)
            for value in wanted_properties
        ):
            continue
        matches.append(dict(sku))

    if not matches:
        selector = sku_id or " + ".join(required_properties or [])
        raise ValueError(f"Aucun SKU ne correspond exactement à : {selector}")
    if len(matches) != 1:
        raise ValueError(
            f"Variante ambiguë : {len(matches)} SKU correspondent ; ajouter un critère"
        )
    return matches[0]


def build_qualification_record(
    product: Mapping[str, Any],
    sku: Mapping[str, Any],
    freight_response: Mapping[str, Any],
    ship_to: str,
) -> dict[str, Any]:
    """Create a dated, evidence-bounded record for downstream review."""
    stock = sku.get("stock")
    try:
        numeric_stock = int(stock)
    except (TypeError, ValueError) as exc:
        raise ValueError("Stock numérique du SKU manquant") from exc
    if numeric_stock <= 0:
        raise ValueError("SKU hors stock")
    return {
        "checked_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source": "AliExpress Open Platform / AE-Dropshipper",
        "destination": ship_to.upper(),
        "product": {
            "product_id": product.get("product_id"),
            "title": product.get("title"),
            "status": product.get("status"),
            "rating": product.get("rating"),
            "evaluation_count": product.get("evaluation_count"),
            "store": product.get("store"),
        },
        "exact_sku": dict(sku),
        "freight": dict(freight_response),
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Sourcing officiel AliExpress en lecture seule (aucune commande)."
    )
    parser.add_argument("--endpoint", default=DEFAULT_ENDPOINT)
    parser.add_argument("--rest-endpoint", default=DEFAULT_REST_ENDPOINT)
    parser.add_argument("--timeout", type=int, default=30)
    sub = parser.add_subparsers(dest="command", required=True)

    auth_url = sub.add_parser(
        "auth-url", help="Générer l'URL OAuth officielle (aucun secret transmis)"
    )
    auth_url.add_argument(
        "--callback-url",
        help="Doit correspondre exactement à l'URL déclarée dans Open Platform",
    )
    auth_url.add_argument("--state")
    auth_url.add_argument("--reuse-login", action="store_true")

    token_create = sub.add_parser(
        "token-create", help="Échanger un code OAuth contre les jetons"
    )
    token_create.add_argument("--code", required=True)
    token_create.add_argument("--dry-run", action="store_true")
    token_create.add_argument(
        "--show-tokens",
        action="store_true",
        help="Afficher explicitement les jetons dans le terminal local",
    )

    token_refresh = sub.add_parser(
        "token-refresh", help="Renouveler les jetons via le refresh token"
    )
    token_refresh.add_argument("--refresh-token")
    token_refresh.add_argument("--dry-run", action="store_true")
    token_refresh.add_argument(
        "--show-tokens",
        action="store_true",
        help="Afficher explicitement les nouveaux jetons dans le terminal local",
    )

    probe = sub.add_parser("probe", help="Tester l'accès à la passerelle officielle")
    probe.add_argument("--item-id", default="1005010249362754")

    affiliate = sub.add_parser(
        "affiliate-skus", help="Lire variantes, prix TTC et livraison (App Key seulement)"
    )
    affiliate.add_argument("--item-id", required=True)
    affiliate.add_argument("--ship-to", default="FR")
    affiliate.add_argument("--currency", default="EUR")
    affiliate.add_argument("--language", default="FR")
    affiliate.add_argument("--sku-id", action="append", dest="sku_ids")
    affiliate.add_argument("--no-delivery", action="store_true")
    affiliate.add_argument("--dry-run", action="store_true")

    affiliate_shipping = sub.add_parser(
        "affiliate-shipping", help="Vérifier la livraison d'un SKU Affiliate exact"
    )
    affiliate_shipping.add_argument("--item-id", required=True)
    affiliate_shipping.add_argument("--sku-id", required=True)
    affiliate_shipping.add_argument("--target-sale-price", required=True)
    affiliate_shipping.add_argument("--tax-rate", required=True)
    affiliate_shipping.add_argument("--ship-to", default="FR")
    affiliate_shipping.add_argument("--currency", default="EUR")
    affiliate_shipping.add_argument("--language", default="FR")
    affiliate_shipping.add_argument("--dry-run", action="store_true")

    product = sub.add_parser(
        "ds-product", aliases=["product"],
        help="Lire produit, SKU, stock, prix et vendeur (jeton DS requis)",
    )
    product.add_argument("--item-id", required=True)
    product.add_argument("--ship-to", default="FR")
    product.add_argument("--currency", default="EUR")
    product.add_argument("--language", default="fr")
    product.add_argument("--raw", action="store_true")
    product.add_argument("--dry-run", action="store_true")

    freight = sub.add_parser(
        "ds-freight", aliases=["freight"],
        help="Calculer le fret vers la France pour un SKU exact",
    )
    freight.add_argument("--item-id", required=True)
    freight.add_argument("--sku-id", required=True)
    freight.add_argument("--ship-to", default="FR")
    freight.add_argument("--quantity", type=int, default=1)
    freight.add_argument("--currency", default="EUR")
    freight.add_argument("--language", default="fr_FR")
    freight.add_argument("--dry-run", action="store_true")

    qualify = sub.add_parser(
        "qualify",
        help="Qualifier une variante exacte puis calculer son fret France",
    )
    qualify.add_argument("--item-id", required=True)
    qualify.add_argument("--sku-id")
    qualify.add_argument(
        "--property",
        action="append",
        dest="properties",
        help="Libellé de propriété requis ; option répétable",
    )
    qualify.add_argument("--ship-to", default="FR")
    qualify.add_argument("--quantity", type=int, default=1)
    qualify.add_argument("--currency", default="EUR")
    qualify.add_argument("--language", default="en")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.command == "auth-url":
            app_key = _required_environment("ALIEXPRESS_APP_KEY")
            callback_url = args.callback_url or _required_environment(
                "ALIEXPRESS_CALLBACK_URL"
            )
            oauth_state = args.state or secrets.token_urlsafe(24)
            result = {
                "authorization_url": build_authorization_url(
                    app_key,
                    callback_url,
                    oauth_state,
                    force_auth=not args.reuse_login,
                ),
                "callback_url": callback_url,
                "state": oauth_state,
                "instruction": (
                    "Vérifier que le state retourné est identique, puis utiliser "
                    "le code dans les 30 minutes avec token-create."
                ),
            }
        elif args.command == "token-create":
            credentials = Credentials.from_environment()
            params = build_token_create_request(credentials, args.code)
            if args.dry_run:
                result = redact_request(params)
            else:
                token_response = post_iop_request(
                    args.rest_endpoint,
                    TOKEN_CREATE_PATH,
                    params,
                    args.timeout,
                )
                result = (
                    token_response
                    if args.show_tokens
                    else redact_token_response(token_response)
                )
        elif args.command == "token-refresh":
            credentials = Credentials.from_environment()
            params = build_token_refresh_request(
                credentials, args.refresh_token
            )
            if args.dry_run:
                result = redact_request(params)
            else:
                token_response = post_iop_request(
                    args.rest_endpoint,
                    TOKEN_REFRESH_PATH,
                    params,
                    args.timeout,
                )
                result = (
                    token_response
                    if args.show_tokens
                    else redact_token_response(token_response)
                )
        elif args.command == "probe":
            result = probe_gateway(args.endpoint, args.item_id, args.timeout)
        elif args.command == "affiliate-skus":
            credentials = Credentials.from_environment()
            params = build_affiliate_skus_request(
                credentials,
                args.item_id,
                args.ship_to,
                args.currency,
                args.language,
                not args.no_delivery,
                args.sku_ids,
            )
            result = redact_request(params) if args.dry_run else post_top_request(
                args.endpoint, params, args.timeout
            )
        elif args.command == "affiliate-shipping":
            credentials = Credentials.from_environment()
            params = build_affiliate_shipping_request(
                credentials,
                args.item_id,
                args.sku_id,
                args.target_sale_price,
                args.tax_rate,
                args.ship_to,
                args.currency,
                args.language,
            )
            result = redact_request(params) if args.dry_run else post_top_request(
                args.endpoint, params, args.timeout
            )
        elif args.command in ("ds-product", "product"):
            credentials = Credentials.from_environment(require_access_token=True)
            params = build_ds_product_request(
                credentials,
                args.item_id,
                args.ship_to,
                args.currency,
                args.language,
            )
            if args.dry_run:
                result = redact_request(params)
            else:
                raw = post_top_request(args.endpoint, params, args.timeout)
                result = raw if args.raw else normalize_ds_product(raw)
        elif args.command in ("ds-freight", "freight"):
            credentials = Credentials.from_environment(require_access_token=True)
            params = build_freight_request(
                credentials,
                args.item_id,
                ship_to=args.ship_to,
                quantity=args.quantity,
                currency=args.currency,
                sku_id=args.sku_id,
                language=args.language,
            )
            result = redact_request(params) if args.dry_run else post_top_request(
                args.endpoint, params, args.timeout
            )
        else:
            credentials = Credentials.from_environment(require_access_token=True)
            product_params = build_ds_product_request(
                credentials,
                args.item_id,
                args.ship_to,
                args.currency,
                args.language,
            )
            normalized_product = normalize_ds_product(
                post_top_request(args.endpoint, product_params, args.timeout)
            )
            exact_sku = select_exact_sku(
                normalized_product, args.sku_id, args.properties
            )
            freight_params = build_freight_request(
                credentials,
                args.item_id,
                ship_to=args.ship_to,
                quantity=args.quantity,
                currency=args.currency,
                sku_id=exact_sku.get("sku_id"),
            )
            freight_response = post_top_request(
                args.endpoint, freight_params, args.timeout
            )
            result = build_qualification_record(
                normalized_product, exact_sku, freight_response, args.ship_to
            )
    except (ConfigurationError, RuntimeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

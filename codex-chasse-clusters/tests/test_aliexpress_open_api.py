import json
import sys
import unittest
from pathlib import Path
from urllib.parse import parse_qs, urlsplit


TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))

from aliexpress_open_api import (  # noqa: E402
    AFFILIATE_SKU_METHOD,
    TOKEN_CREATE_PATH,
    TOKEN_REFRESH_PATH,
    Credentials,
    build_authorization_url,
    build_affiliate_shipping_request,
    build_affiliate_skus_request,
    build_freight_request,
    build_product_request,
    build_qualification_record,
    build_token_create_request,
    build_token_refresh_request,
    normalize_ds_product,
    redact_request,
    redact_token_response,
    select_exact_sku,
    sign_params,
    signature_payload,
)


class AliExpressOpenApiTests(unittest.TestCase):
    def setUp(self):
        self.credentials = Credentials("12345678", "helloworld", "session-token")
        self.timestamp = "1785683205000"

    def test_signature_payload_is_ascii_sorted(self):
        params = {"foo": "1", "bar": "2", "foobar": "4", "foo_bar": "3", "sign": "ignored"}
        self.assertEqual(signature_payload(params), b"bar2foo1foo_bar3foobar4")

    def test_sha256_means_hmac_sha256_like_current_official_sdk(self):
        params = {"foo": "1", "bar": "2", "foobar": "4", "foo_bar": "3"}
        self.assertEqual(
            sign_params(params, "helloworld", "sha256"),
            "339676BF36C50A8BD3D8F6B4A81B2F9AA614B05BFCFEBEFC169CB830D6B77D3B",
        )

    def test_authorization_url_keeps_exact_callback_and_state(self):
        url = build_authorization_url(
            "12345678",
            "https://example.test/oauth/callback",
            "state-123",
        )
        parsed = urlsplit(url)
        query = parse_qs(parsed.query)
        self.assertEqual(parsed.scheme, "https")
        self.assertEqual(parsed.netloc, "api-sg.aliexpress.com")
        self.assertEqual(query["response_type"], ["code"])
        self.assertEqual(query["client_id"], ["12345678"])
        self.assertEqual(
            query["redirect_uri"], ["https://example.test/oauth/callback"]
        )
        self.assertEqual(query["state"], ["state-123"])
        self.assertEqual(query["force_auth"], ["true"])

    def test_token_create_request_uses_iop_path_signature(self):
        request = build_token_create_request(
            self.credentials,
            "oauth-code",
            timestamp=self.timestamp,
        )
        self.assertEqual(request["code"], "oauth-code")
        self.assertEqual(request["simplify"], "true")
        self.assertNotIn("method", request)
        self.assertEqual(
            request["sign"],
            sign_params(
                {key: value for key, value in request.items() if key != "sign"},
                self.credentials.app_secret,
                api_name=TOKEN_CREATE_PATH,
            ),
        )

    def test_token_refresh_uses_refresh_token_not_access_token(self):
        credentials = Credentials(
            "12345678", "helloworld", "access-token", "refresh-token"
        )
        request = build_token_refresh_request(
            credentials, timestamp=self.timestamp
        )
        self.assertEqual(request["refresh_token"], "refresh-token")
        self.assertNotIn("access_token", request)
        self.assertEqual(
            request["sign"],
            sign_params(
                {key: value for key, value in request.items() if key != "sign"},
                credentials.app_secret,
                api_name=TOKEN_REFRESH_PATH,
            ),
        )

    def test_affiliate_sku_request_targets_exact_item_and_france(self):
        request = build_affiliate_skus_request(
            Credentials("12345678", "helloworld"),
            "1005010249362754",
            timestamp=self.timestamp,
        )
        self.assertEqual(request["method"], AFFILIATE_SKU_METHOD)
        self.assertEqual(request["product_id"], "1005010249362754")
        self.assertEqual(request["ship_to_country"], "FR")
        self.assertEqual(request["target_currency"], "EUR")
        self.assertEqual(request["target_language"], "FR")
        self.assertEqual(request["need_deliver_info"], "Yes")
        self.assertNotIn("access_token", request)
        self.assertEqual(len(request["sign"]), 64)

    def test_affiliate_shipping_is_exact_sku(self):
        request = build_affiliate_shipping_request(
            Credentials("12345678", "helloworld"),
            "1005010249362754",
            "120000123",
            "101.99",
            "0.2",
            timestamp=self.timestamp,
        )
        self.assertEqual(request["sku_id"], "120000123")
        self.assertEqual(request["ship_to_country"], "FR")
        self.assertEqual(request["target_sale_price"], "101.99")
        self.assertEqual(request["tax_rate"], "0.2")

    def test_ds_product_request_targets_france_and_has_token(self):
        request = build_product_request(
            self.credentials,
            "1005010249362754",
            timestamp=self.timestamp,
        )
        self.assertEqual(request["method"], "aliexpress.ds.product.get")
        self.assertEqual(request["product_id"], "1005010249362754")
        self.assertEqual(request["ship_to_country"], "FR")
        self.assertEqual(request["target_currency"], "EUR")
        self.assertEqual(request["target_language"], "fr")
        self.assertEqual(request["session"], "session-token")
        self.assertNotIn("access_token", request)
        self.assertEqual(request["remove_personal_benefit"], "true")

    def test_freight_request_includes_exact_sku(self):
        request = build_freight_request(
            self.credentials,
            "1005010249362754",
            sku_id="120000123",
            timestamp=self.timestamp,
        )
        query = json.loads(request["queryDeliveryReq"])
        self.assertEqual(request["method"], "aliexpress.ds.freight.query")
        self.assertEqual(query["productId"], "1005010249362754")
        self.assertEqual(query["selectedSkuId"], "120000123")
        self.assertEqual(query["shipToCountry"], "FR")
        self.assertEqual(query["quantity"], "1")
        self.assertEqual(query["currency"], "EUR")
        self.assertEqual(query["language"], "fr_FR")

    def test_normalize_ds_product_preserves_variant_truth(self):
        response = {
            "aliexpress_ds_product_get_response": {
                "resp_result": {
                    "result": {
                        "ae_item_base_info_dto": {
                            "product_id": 1005010249362754,
                            "subject": "Test watch",
                            "avg_evaluation_rating": "4.8",
                            "evaluation_count": "92",
                        },
                        "ae_store_info": {
                            "store_id": 42,
                            "store_name": "Test Store",
                            "shipping_speed_rating": "4.7",
                        },
                        "ae_item_sku_info_dtos": [
                            {
                                "sku_id": "120000123",
                                "sku_attr": "14:193",
                                "sku_available_stock": 17,
                                "offer_sale_price": "101.99",
                                "currency_code": "EUR",
                                "ae_sku_property_dtos": [
                                    {
                                        "sku_property_name": "Color",
                                        "property_value_definition_name": "White Arabic dial",
                                        "sku_image": "https://example.invalid/white.jpg",
                                    }
                                ],
                            }
                        ],
                    }
                }
            }
        }
        normalized = normalize_ds_product(response)
        self.assertEqual(normalized["product_id"], 1005010249362754)
        self.assertEqual(normalized["store"]["name"], "Test Store")
        self.assertEqual(normalized["skus"][0]["sku_id"], "120000123")
        self.assertEqual(normalized["skus"][0]["stock"], 17)
        self.assertEqual(
            normalized["skus"][0]["properties"][0]["value"], "White Arabic dial"
        )

    def test_normalize_supports_legacy_top_wrappers_and_zero_stock(self):
        response = {
            "result": {
                "ae_item_base_info_dto": {"product_id": 7, "subject": "Watch"},
                "ae_item_sku_info_dtos": {
                    "ae_item_sku_info_d_t_o": [
                        {
                            "id": "14:193;5:36",
                            "s_k_u_available_stock": 0,
                            "sku_price": "99.00",
                            "aeop_s_k_u_propertys": {
                                "aeop_sku_property": [
                                    {
                                        "sku_property_name": "Color",
                                        "property_value_definition_name": "white sterile",
                                    }
                                ]
                            },
                        }
                    ]
                },
            }
        }
        normalized = normalize_ds_product(response)
        self.assertEqual(normalized["skus"][0]["sku_id"], "14:193;5:36")
        self.assertEqual(normalized["skus"][0]["stock"], 0)

    def test_exact_sku_selection_requires_all_properties(self):
        product = {
            "skus": [
                {
                    "sku_id": "white-36",
                    "properties": [
                        {"name": "Color", "value": "white sterile"},
                        {"name": "Size", "value": "36mm - glassback"},
                    ],
                    "stock": 12,
                },
                {
                    "sku_id": "white-39",
                    "properties": [
                        {"name": "Color", "value": "white sterile"},
                        {"name": "Size", "value": "39mm-glass back"},
                    ],
                    "stock": 9,
                },
            ]
        }
        selected = select_exact_sku(
            product, required_properties=["white sterile", "36mm-glass back"]
        )
        self.assertEqual(selected["sku_id"], "white-36")
        with self.assertRaisesRegex(ValueError, "Variante ambiguë"):
            select_exact_sku(product, required_properties=["white sterile"])

    def test_property_selector_does_not_match_across_property_names(self):
        product = {
            "skus": [
                {
                    "sku_id": "bear-400",
                    "properties": [
                        {"name": "Color", "value": "Bear"},
                        {"name": "Spécification", "value": "400MMx600MM"},
                    ],
                },
                {
                    "sku_id": "cat-400",
                    "properties": [
                        {"name": "Color", "value": "Cat"},
                        {"name": "Spécification", "value": "400MMx600MM"},
                    ],
                },
            ]
        }

        selected = select_exact_sku(
            product, required_properties=["Cat", "400MMx600MM"]
        )

        self.assertEqual(selected["sku_id"], "cat-400")

    def test_qualification_rejects_zero_stock(self):
        product = {"product_id": 7, "title": "Watch", "store": {}}
        with self.assertRaisesRegex(ValueError, "hors stock"):
            build_qualification_record(
                product,
                {"sku_id": "x", "stock": 0, "price": "1.00"},
                {"shipping": "free"},
                "FR",
            )

    def test_redaction_never_prints_token_or_signature(self):
        redacted = redact_request(
            {
                "access_token": "secret",
                "refresh_token": "refresh",
                "code": "oauth-code",
                "sign": "signature",
                "product_id": "1",
            }
        )
        self.assertEqual(redacted["access_token"], "***")
        self.assertEqual(redacted["refresh_token"], "***")
        self.assertEqual(redacted["code"], "***")
        self.assertEqual(redacted["sign"], "***")
        self.assertEqual(redacted["product_id"], "1")

    def test_token_response_redaction_is_recursive(self):
        redacted = redact_token_response(
            {
                "access_token": "access",
                "nested": {"refresh_token": "refresh", "expires_in": 3600},
            }
        )
        self.assertEqual(redacted["access_token"], "***")
        self.assertEqual(redacted["nested"]["refresh_token"], "***")
        self.assertEqual(redacted["nested"]["expires_in"], 3600)


if __name__ == "__main__":
    unittest.main()

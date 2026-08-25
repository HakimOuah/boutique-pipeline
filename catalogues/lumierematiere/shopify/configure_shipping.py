#!/usr/bin/env python3
"""France métropolitaine only, livraison offerte (0 €), sans autre zone."""
from __future__ import annotations

import json

from client import gql

LOCATION_GROUP = "gid://shopify/DeliveryLocationGroup/135450624336"
ZONE_FR = "gid://shopify/DeliveryZone/616578646352"
METHOD_NAME = "Livraison offerte"

ZONES = """
query DeliverySnapshot {
  deliveryProfiles(first: 10) {
    nodes {
      id
      name
      default
      profileLocationGroups {
        locationGroup { id }
        locationGroupZones(first: 20) {
          nodes {
            zone { id name countries { code { countryCode restOfWorld } } }
            methodDefinitions(first: 20) {
              nodes {
                id
                name
                active
                rateProvider {
                  __typename
                  ... on DeliveryRateDefinition {
                    id
                    price { amount currencyCode }
                  }
                }
                methodConditions { id field operator }
              }
            }
          }
        }
      }
    }
  }
}
"""

MUTATION = """
mutation ConfigureFrFree($id: ID!, $profile: DeliveryProfileInput!) {
  deliveryProfileUpdate(id: $id, profile: $profile) {
    profile { id name }
    userErrors { field message }
  }
}
"""


def _base_gid(gid: str) -> str:
    return gid.split("?", 1)[0]


def _price(method: dict) -> float | None:
    rp = method.get("rateProvider") or {}
    amount = (rp.get("price") or {}).get("amount")
    try:
        return float(amount) if amount is not None else None
    except (TypeError, ValueError):
        return None


def _dump(profile: dict) -> None:
    for zg in profile["profileLocationGroups"]:
        for z in zg["locationGroupZones"]["nodes"]:
            zone = z["zone"]
            pays = [
                (c.get("code") or {}).get("countryCode")
                for c in zone["countries"]
            ]
            print(f"Zone {zone['name']} ({zone['id']}) pays={pays}")
            for m in z["methodDefinitions"]["nodes"]:
                print(
                    f"  {m['name']} id={_base_gid(m['id'])} active={m['active']} "
                    f"{_price(m)} EUR "
                    f"conditions={len(m.get('methodConditions') or [])}"
                )


def _is_target(profile: dict) -> bool:
    groups = profile.get("profileLocationGroups") or []
    if len(groups) != 1:
        return False
    zones = groups[0]["locationGroupZones"]["nodes"]
    if len(zones) != 1:
        return False
    z = zones[0]
    pays = [
        (c.get("code") or {}).get("countryCode")
        for c in z["zone"]["countries"]
    ]
    if pays != ["FR"] or (z["zone"].get("name") != "France"):
        return False
    seen: set[str] = set()
    unique = []
    for m in z["methodDefinitions"]["nodes"]:
        bid = _base_gid(m["id"])
        if bid in seen:
            continue
        seen.add(bid)
        unique.append(m)
    if len(unique) != 1:
        return False
    m = unique[0]
    return (
        m["name"] == METHOD_NAME
        and m.get("active") is True
        and _price(m) == 0.0
        and not (m.get("methodConditions") or [])
    )


def snapshot() -> dict:
    data = gql(ZONES)
    nodes = (data.get("deliveryProfiles") or {}).get("nodes") or []
    if not nodes:
        raise SystemExit("Aucun profil de livraison")
    default = next((p for p in nodes if p.get("default")), nodes[0])
    return default


def main() -> None:
    profile = snapshot()
    if _is_target(profile):
        print("Déjà conforme — France only, 0 €, sans condition")
        _dump(profile)
        return

    groups = profile["profileLocationGroups"]
    loc_id = groups[0]["locationGroup"]["id"] if groups else LOCATION_GROUP
    zones = []
    for zg in groups:
        zones.extend(zg["locationGroupZones"]["nodes"])

    extra_zones = [
        z["zone"]["id"] for z in zones if z["zone"]["id"] != ZONE_FR
    ]
    fr = next((z for z in zones if z["zone"]["id"] == ZONE_FR), None)
    if fr is None:
        raise SystemExit(f"Zone France {ZONE_FR} introuvable")

    to_delete_methods = []
    has_free = False
    seen_methods: set[str] = set()
    for m in fr["methodDefinitions"]["nodes"]:
        bid = _base_gid(m["id"])
        if bid in seen_methods:
            continue
        seen_methods.add(bid)
        if (
            m["name"] == METHOD_NAME
            and _price(m) == 0.0
            and not (m.get("methodConditions") or [])
        ):
            has_free = True
            continue
        to_delete_methods.append(bid)

    profile_input: dict = {}
    if extra_zones:
        profile_input["zonesToDelete"] = extra_zones
    if to_delete_methods:
        profile_input["methodDefinitionsToDelete"] = to_delete_methods
    if not has_free:
        profile_input["locationGroupsToUpdate"] = [
            {
                "id": loc_id,
                "zonesToUpdate": [
                    {
                        "id": ZONE_FR,
                        "methodDefinitionsToCreate": [
                            {
                                "name": METHOD_NAME,
                                "active": True,
                                "rateDefinition": {
                                    "price": {
                                        "amount": "0.00",
                                        "currencyCode": "EUR",
                                    }
                                },
                            }
                        ],
                    }
                ],
            }
        ]

    if not profile_input:
        print("Rien à changer")
        _dump(profile)
        return

    payload = gql(
        MUTATION,
        {"id": profile["id"], "profile": profile_input},
    )["deliveryProfileUpdate"]
    errors = payload.get("userErrors") or []
    if errors:
        print(json.dumps(errors, indent=2, ensure_ascii=False))
        raise SystemExit(1)

    after = snapshot()
    if not _is_target(after):
        print("Mutation OK mais profil encore non conforme :")
        _dump(after)
        raise SystemExit(1)
    print("OK — France only, livraison offerte 0 €")
    _dump(after)


if __name__ == "__main__":
    main()

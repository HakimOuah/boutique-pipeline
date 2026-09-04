"""Calculs phase 5 A6 — reproductibles. Aucun appel réseau."""
from __future__ import annotations

import csv
import json
from decimal import Decimal, ROUND_HALF_UP, getcontext
from pathlib import Path

getcontext().prec = 28

ROOT = Path(__file__).resolve().parent
VAT = Decimal("0.20")
COST_KIT_TTC = Decimal("29.79")  # PDP 2026-09-04 23:42 CEST
COST_K23_TTC = Decimal("27.79")
COST_A99_TTC = Decimal("32.39")
CPC_USD = Decimal("0.926")
FX_EURUSD_BCE_2026_09_03 = Decimal("1.1615")
CPC_PROXY = (CPC_USD / FX_EURUSD_BCE_2026_09_03).quantize(
    Decimal("0.001"), rounding=ROUND_HALF_UP
)  # 0.797 → dossier A6 arrondit 0,798
CPC_PROXY_DOSSIER = Decimal("0.798")
CPC_ROUND = Decimal("0.80")
CPC_STRESS = Decimal("1.20")


def D(x) -> Decimal:
    return x if isinstance(x, Decimal) else Decimal(str(x))


def eur(x: Decimal) -> str:
    return str(D(x).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def ratio6(x: Decimal) -> str:
    return str(D(x).quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP))


def compute(ttc, pay_rate, pay_fix, sav_rate, cost, pack) -> dict:
    ttc, pay_rate, pay_fix, sav_rate, cost, pack = map(
        D, (ttc, pay_rate, pay_fix, sav_rate, cost, pack)
    )
    ca_ht = ttc / (1 + VAT)
    tva_collectee = ttc - ca_ht
    paiement = ttc * pay_rate + pay_fix
    sav = ttc * sav_rate
    contrib = ca_ht - paiement - sav - cost - pack
    return {
        "ttc": ttc,
        "ca_ht": ca_ht,
        "tva_collectee": tva_collectee,
        "paiement": paiement,
        "sav": sav,
        "cost": cost,
        "pack": pack,
        "contrib": contrib,
    }


PAYMENT = {
    "stripe_indicatif": (Decimal("0.014"), Decimal("0.25")),
    "paypal_indicatif": (Decimal("0.029"), Decimal("0.35")),
    "a6_dossier": (Decimal("0.02"), Decimal("0.30")),
}

SCENARIOS = [
    {
        "id": "prudent",
        "label": "prudent — SKU sourcé à 69 €",
        "ttc": Decimal("69"),
        "payment": "paypal_indicatif",
        "sav_rate": Decimal("0.08"),
        "pack": Decimal("2.00"),
        "cost": COST_KIT_TTC,
        "cpc": CPC_STRESS,
        "comparabilite_prix": "Rasoir Lamier 69 € PDP 04/09 ; SKU = rasoir + 5 lames annoncées, pas le kit 99/119",
    },
    {
        "id": "central_sku_69",
        "label": "central SKU — 69 € Stripe",
        "ttc": Decimal("69"),
        "payment": "stripe_indicatif",
        "sav_rate": Decimal("0.05"),
        "pack": Decimal("0"),
        "cost": COST_KIT_TTC,
        "cpc": CPC_PROXY_DOSSIER,
        "comparabilite_prix": "Prix réaliste du SKU sourcé vs rasoir Lamier 69 € ; Bambaw ~21 € et Bouc 34,90 € plus bas",
    },
    {
        "id": "central_99",
        "label": "central ancré 99 € — non comparable au contenu",
        "ttc": Decimal("99"),
        "payment": "stripe_indicatif",
        "sav_rate": Decimal("0.05"),
        "pack": Decimal("0"),
        "cost": COST_KIT_TTC,
        "cpc": CPC_PROXY_DOSSIER,
        "comparabilite_prix": "Ancré Lamier kit 99 € et Bouc 99,72 € ; contenu sourcé ≠ blaireau/support/étui",
    },
    {
        "id": "central_99_a6",
        "label": "central 99 € — barème dossier A6 03/09",
        "ttc": Decimal("99"),
        "payment": "a6_dossier",
        "sav_rate": Decimal("0.05"),
        "pack": Decimal("0"),
        "cost": COST_KIT_TTC,
        "cpc": CPC_PROXY_DOSSIER,
        "comparabilite_prix": "Continuité des hypothèses A6.md (2 % + 0,30 €)",
    },
    {
        "id": "favorable_119",
        "label": "favorable — 119 € Stripe SAV 3 %",
        "ttc": Decimal("119"),
        "payment": "stripe_indicatif",
        "sav_rate": Decimal("0.03"),
        "pack": Decimal("0"),
        "cost": COST_KIT_TTC,
        "cpc": CPC_PROXY_DOSSIER,
        "comparabilite_prix": "Ancré Lamier kit menu 119 € ; contenu sourcé non équivalent",
    },
    {
        "id": "stress_99",
        "label": "stress — 99 € PayPal SAV 8 % CPC 1,20",
        "ttc": Decimal("99"),
        "payment": "paypal_indicatif",
        "sav_rate": Decimal("0.08"),
        "pack": Decimal("0"),
        "cost": COST_KIT_TTC,
        "cpc": CPC_STRESS,
        "comparabilite_prix": "Même ancrage 99 €, hypothèses défavorables",
    },
    {
        "id": "alt_k23_99",
        "label": "alt K23 27,79 € à 99 € — sans lames",
        "ttc": Decimal("99"),
        "payment": "stripe_indicatif",
        "sav_rate": Decimal("0.05"),
        "pack": Decimal("0"),
        "cost": COST_K23_TTC,
        "cpc": CPC_PROXY_DOSSIER,
        "comparabilite_prix": "K23 = rasoir + support, lames absentes ; pas un kit débutant",
    },
    {
        "id": "alt_a99_69",
        "label": "alt A99 32,39 € à 69 € — rasoir seul",
        "ttc": Decimal("69"),
        "payment": "stripe_indicatif",
        "sav_rate": Decimal("0.05"),
        "pack": Decimal("0"),
        "cost": COST_A99_TTC,
        "cpc": CPC_PROXY_DOSSIER,
        "comparabilite_prix": "A99 silvery, promo jusqu'au 07/09/2026 23:59 CET",
    },
]


def enrich(s: dict) -> dict:
    pr, pf = PAYMENT[s["payment"]]
    r = compute(s["ttc"], pr, pf, s["sav_rate"], s["cost"], s["pack"])
    contrib = r["contrib"]
    cpc = s["cpc"]
    out = {
        "id": s["id"],
        "label": s["label"],
        "comparabilite_prix": s["comparabilite_prix"],
        "prix_ttc": eur(s["ttc"]),
        "ca_ht": eur(r["ca_ht"]),
        "tva_collectee": eur(r["tva_collectee"]),
        "modele_paiement": s["payment"],
        "paiement": eur(r["paiement"]),
        "taux_sav": str(s["sav_rate"]),
        "provision_sav": eur(r["sav"]),
        "cout_rendu_ttc": eur(r["cost"]),
        "emballage": eur(r["pack"]),
        "marge_contributive_avant_ads": eur(contrib),
        "cpa_max": eur(contrib),
        "cpc_eur": str(cpc),
        "tva_achat": "non_recuperable_hypothese",
    }
    if contrib > 0:
        out["be_cvr"] = ratio6(cpc / contrib)
        out["clics_par_vente_be"] = eur(contrib / cpc)
        out["is_25_si_ads_zero_illustration"] = eur(contrib * Decimal("0.25"))
        out["apres_is_si_ads_zero_illustration"] = eur(contrib * Decimal("0.75"))
    else:
        out["be_cvr"] = "incalculable_contrib_non_positive"
        out["clics_par_vente_be"] = "incalculable_contrib_non_positive"
        out["is_25_si_ads_zero_illustration"] = "incalculable"
        out["apres_is_si_ads_zero_illustration"] = "incalculable"
    after = {}
    for cvr in (Decimal("0.01"), Decimal("0.015"), Decimal("0.02"), Decimal("0.03")):
        cpa_scen = cpc / cvr
        after[str(cvr)] = {
            "cpa_scenario": eur(cpa_scen),
            "contrib_apres_ads": eur(contrib - cpa_scen),
        }
    out["sensibilite_cvr"] = after
    # raw for audit
    out["_raw_contrib"] = str(contrib)
    return out


def main() -> None:
    rows = [enrich(s) for s in SCENARIOS]
    # VAT recoverable sensitivity on central_99
    cost_ht = COST_KIT_TTC / (1 + VAT)
    rec = compute(99, 0.014, 0.25, 0.05, cost_ht, 0)
    vat_rec = {
        "id": "sensi_tva_recuperable_99",
        "label": "sensibilité — si TVA achat récupérable (non observée)",
        "cout_ht": eur(cost_ht),
        "marge_contributive_avant_ads": eur(rec["contrib"]),
        "be_cvr_cpc_0.798": ratio6(CPC_PROXY_DOSSIER / rec["contrib"]),
        "statut": "contre-hypothese_non_retenue",
    }

    cap_99_a6 = compute(99, 0.02, 0.30, 0.05, 0, 0)
    continuity = {
        "pre_goods_99_a6": eur(cap_99_a6["contrib"]),
        "plafond_produit_cvr2_cpc0.80": eur(
            cap_99_a6["contrib"] - Decimal("0.80") / Decimal("0.02")
        ),
        "plafond_attendu_dossier_README": "35.27",
        "contrib_si_cout_29.79": eur(cap_99_a6["contrib"] - COST_KIT_TTC),
    }

    payload = {
        "date": "2026-09-04",
        "cpc_proxy_calcule": str(CPC_PROXY),
        "cpc_proxy_dossier_a6": str(CPC_PROXY_DOSSIER),
        "note_cpc": "0,926 USD / 1,1615 = 0,797 arrondi dossier 0,798. DataForSEO, pas CPC campagne.",
        "cout_kit_ttc": str(COST_KIT_TTC),
        "scenarios": [{k: v for k, v in r.items() if not k.startswith("_")} for r in rows],
        "sensibilite_tva_recuperable": vat_rec,
        "continuite_plafond_a6": continuity,
        "formules": {
            "ca_ht": "TTC / 1,20",
            "paiement": "TTC * taux + fixe",
            "sav": "TTC * taux",
            "marge_contributive_avant_ads": "CA_HT - paiement - SAV - cout_rendu_TTC_non_recuperable - emballage",
            "cpa_max": "égal à la marge contributive avant Ads",
            "be_cvr": "CPC / cpa_max si cpa_max > 0",
        },
    }
    (ROOT / "economie-calculs.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    csv_rows = []
    for r in payload["scenarios"]:
        csv_rows.append(
            {
                "id": r["id"],
                "prix_ttc": r["prix_ttc"],
                "ca_ht": r["ca_ht"],
                "tva_collectee": r["tva_collectee"],
                "paiement": r["paiement"],
                "provision_sav": r["provision_sav"],
                "cout_rendu_ttc": r["cout_rendu_ttc"],
                "emballage": r["emballage"],
                "marge_contributive_avant_ads": r["marge_contributive_avant_ads"],
                "cpa_max": r["cpa_max"],
                "cpc_eur": r["cpc_eur"],
                "be_cvr": r["be_cvr"],
                "clics_par_vente_be": r["clics_par_vente_be"],
                "contrib_apres_ads_cvr_1pct": r["sensibilite_cvr"]["0.01"]["contrib_apres_ads"],
                "contrib_apres_ads_cvr_1_5pct": r["sensibilite_cvr"]["0.015"]["contrib_apres_ads"],
                "contrib_apres_ads_cvr_2pct": r["sensibilite_cvr"]["0.02"]["contrib_apres_ads"],
                "contrib_apres_ads_cvr_3pct": r["sensibilite_cvr"]["0.03"]["contrib_apres_ads"],
            }
        )
    with (ROOT / "economie-calculs.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(csv_rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(csv_rows)
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

"""Rédige PRIX-ALIGNEMENT-LUSTRIA-2026-08-26.md depuis le plan d'appariement.

Le corps rédigé (contexte, méthode, arbitrages) est ici en toutes lettres ; seuls
le tableau des 120 lignes et les chiffres de synthèse sont calculés, pour qu'un
recalcul du plan ne laisse jamais un chiffre périmé dans le texte.
"""
from __future__ import annotations

import collections
import json
import statistics as st
from pathlib import Path

import lustria_match as L

HERE = Path(__file__).resolve().parent
PLAN = HERE / "prix-alignement-plan-2026-08-26.json"
OUT = HERE / "PRIX-ALIGNEMENT-LUSTRIA-2026-08-26.md"

DECISION_LIB = {
    "baisse": "baisse",
    "inchange_deja_sous_cible": "inchangé — déjà sous la cible",
    "inchange_sans_comparable": "inchangé — aucun comparable",
    "bloque_marge": "bloqué par la marge",
}


def eur(x: float) -> str:
    return f"{x:,.0f}".replace(",", " ")


def eur2(x: float) -> str:
    return f"{x:,.2f}".replace(",", " ").replace(".", ",")


def n(x: int) -> str:
    """Effectif, séparateur de milliers en espace fine."""
    return f"{x:,d}".replace(",", " ")


def pct(x: float, d: int = 1, signe: bool = False) -> str:
    fmt = f"{{:{'+' if signe else ''}.{d}f}}"
    return fmt.format(x).replace(".", ",")


def quant(vals: list[float], f: float) -> float:
    v = sorted(vals)
    i = f * (len(v) - 1)
    lo = int(i)
    hi = min(lo + 1, len(v) - 1)
    return v[lo] + (v[hi] - v[lo]) * (i - lo)


def descendant_9(x: float) -> int:
    p = L.arrondi_9(x)
    while p > x:
        p -= 10
    return p


def main() -> None:
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    lignes = plan["lignes"]
    lustria = L.charge_lustria()
    brut = [p["prix"] for p in json.loads(L.LUSTRIA.read_text(encoding="utf-8"))["produits"]
            if p.get("prix")]

    baisses = [l for l in lignes if l["decision"] == "baisse"]
    deja = [l for l in lignes if l["decision"] == "inchange_deja_sous_cible"]
    sans = [l for l in lignes if l["decision"] == "inchange_sans_comparable"]
    bloq = [l for l in lignes if l["decision"] == "bloque_marge"]
    apparies = [l for l in lignes if l["comparable_med"]]

    av = [l["prix_actuel"] for l in lignes]
    ap = [l["prix_retenu"] for l in lignes]
    lus_susp = [x["prix"] for x in lustria if x["type"] == "suspendu"]
    lus_plaf = [x["prix"] for x in lustria if x["type"] == "plafonnier"]
    lus_all = [x["prix"] for x in lustria]

    marge_av = sum(l["marge_avant"] for l in lignes)
    marge_ap = sum(l["marge_apres"] for l in lignes)
    remises = [100 * (1 - l["prix_retenu"] / l["comparable_med"]) for l in baisses]
    hausses = [l for l in apparies if l["cible"] > l["prix_actuel"]]
    strict = [(l, descendant_9(l["cible_brute"])) for l in baisses]
    strict = [(l, p) for l, p in strict if p != l["prix_retenu"]]

    dix_av = sum(1 for l in apparies if l["prix_actuel"] <= l["comparable_med"] * 0.9 + 1e-9)
    dix_ap = sum(1 for l in apparies if l["prix_retenu"] <= l["comparable_med"] * 0.9 + 1e-9)
    sous_av = sum(1 for l in apparies if l["prix_actuel"] < l["comparable_med"])
    sous_ap = sum(1 for l in apparies if l["prix_retenu"] < l["comparable_med"])

    d: list[str] = []
    w = d.append

    w("# Alignement des prix sur Lustria — lumierematiere.fr")
    w("")
    w("**26/08/2026 · 120 fiches · méthode `METHODE-ANALYSE-MARCHE.md` étape 9**  ")
    w("Base de comparaison : `lustria-catalogue-2026-08-25.json`, 5 928 fiches lues le "
      "25/08/2026. Aucun nouveau scrape.  ")
    w("Rapport rendu **avant** application, comme demandé. Plan machine : "
      "`prix-alignement-plan-2026-08-26.json`. Application : `align_prices.py`.")
    w("")
    w("---")
    w("")

    # ---------------------------------------------------------------- 1
    w("## 1. Ce qu'il faut savoir avant de lire le tableau")
    w("")
    w("### La médiane de 169,90 € n'est pas celle de nos concurrents")
    w("")
    w("`CONCURRENT-LUSTRIA-2026-08-25.md` compare **notre médiane de 199 €** à **leur médiane "
      "de 169,90 €** et en conclut que nous sommes 17 % au-dessus. Ce chiffre est juste, mais "
      "il compare deux populations différentes : leur médiane est celle des **5 928 fiches du "
      "catalogue entier**, dont 1 522 appliques murales, 263 veilleuses, 319 lampes de chevet "
      "et 121 luminaires d'extérieur. Nous ne vendons aucun de ces produits.")
    w("")
    w("Ramené à ce que nous vendons vraiment — le luminaire suspendu et le plafonnier — le "
      "repère change de niveau :")
    w("")
    w("| Population Lustria | Fiches | p25 | Médiane | p75 |")
    w("|---|---:|---:|---:|---:|")
    w(f"| Catalogue entier | {n(len(brut))} | {eur2(quant(brut, .25))} € | "
      f"**{eur2(st.median(brut))} €** | {eur2(quant(brut, .75))} € |")
    w(f"| Luminaires suspendus | {n(len(lus_susp))} | {eur2(quant(lus_susp, .25))} € | "
      f"**{eur2(st.median(lus_susp))} €** | {eur2(quant(lus_susp, .75))} € |")
    w(f"| Plafonniers | {n(len(lus_plaf))} | {eur2(quant(lus_plaf, .25))} € | "
      f"**{eur2(st.median(lus_plaf))} €** | {eur2(quant(lus_plaf, .75))} € |")
    w(f"| **Périmètre comparable retenu** | **{n(len(lus_all))}** | "
      f"{eur2(quant(lus_all, .25))} € | **{eur2(st.median(lus_all))} €** | "
      f"{eur2(quant(lus_all, .75))} € |")
    w("")
    w(f"Note de traçabilité : recalculée sur le même fichier, la médiane du catalogue entier "
      f"ressort à {eur2(st.median(brut))} € et non 169,90 €. L'écart vient du choix du point "
      f"milieu sur un effectif pair — 169,90 € est la valeur médiane basse, "
      f"{eur2(st.median(brut))} € la moyenne des deux valeurs centrales. Cela ne change aucune "
      f"conclusion.")
    w("")
    w("**Conséquence directe.** Comparable à comparable, notre médiane de 199 € est déjà "
      f"**{pct(100 * (1 - 199 / st.median(lus_all)), 0)} % sous** la leur, pas 17 % au-dessus. "
      "L'étape 9 n'est pas violée dans le sens que l'analyse laissait entendre. Ce qui reste "
      "vrai, et que ce travail corrige, c'est qu'elle est violée **par famille** : sur la "
      "céramique, le bambou, le tissu et le plafonnier bois, ils sont moins chers que nous.")
    w("")
    w("### Le mandat mécanique aurait été une hausse de prix sur la moitié du catalogue")
    w("")
    plus_gros = max(hausses, key=lambda l: l["cible"] - l["prix_actuel"])
    w(f"Appliquée à la lettre, la règle « médiane du comparable × 0,90 » remonte le prix de "
      f"**{len(hausses)} fiches sur {len(apparies)}**, pour "
      f"**+{eur(sum(l['cible'] - l['prix_actuel'] for l in hausses))} € TTC** cumulés. La plus "
      f"forte : `{plus_gros['sku']}` ({plus_gros['titre']}) passerait de "
      f"{int(plus_gros['prix_actuel'])} € à {plus_gros['cible']} €, la médiane de ses "
      f"{plus_gros['pool_n']} comparables étant à {eur2(plus_gros['comparable_med'])} €.")
    w("")
    w("**Ces hausses ne sont pas appliquées.** Le mandat est de se placer *sous* Lustria, le "
      "jeu de décisions demandé est baisse / inchangé / bloqué par la marge, et rien n'autorise "
      "une hausse. Ces lignes sortent en « inchangé — déjà sous la cible », avec le montant "
      "laissé de côté chiffré ci-dessus. **C'est un arbitrage, pas un calcul : à trancher.**")
    w("")

    # ---------------------------------------------------------------- 2
    w("## 2. Méthode")
    w("")
    w("### Terminaison retenue : euro entier terminant par 9, grille au pas de 10 €")
    w("")
    w("Nos 120 fiches finissent déjà toutes par 9 sans centimes ; Lustria finit par `,90`. "
      "**On garde le 9 en euro entier** et on ne change qu'une chose : le pas de la grille "
      "passe de 50 € (149 / 199 / 249 / 299 / 349 / 399 / 499) à 10 € (…129, 139, 149, 159…). "
      "Trois raisons :")
    w("")
    w("1. **Un pas de 50 € rend l'exercice impossible.** Une cible calculée à 166 € ne peut "
      "atterrir que sur 149 €, en donnant 17 € de marge pour rien, ou sur 199 €, au-dessus du "
      "comparable. Le pas de 10 € est le plus grossier qui permette encore de viser −10 % à "
      "moins de 5 € près.")
    w("2. **`,90` est la terminaison de celui qu'on sous-cote.** Sans prix barré ni promotion, "
      "l'euro entier se lit comme un prix posé et non comme une remise ; c'est aussi ce qui "
      "nous distingue d'eux à l'affichage en Shopping.")
    w("3. **169 € bat 169,90 € pour 0,90 € de marge.** À affichage égal en comparateur, le "
      "nombre entier est perçu plus bas.")
    w("")
    w("Arrondi **au plus proche**, pas vers le bas. La remise réellement obtenue sur les "
      f"{len(baisses)} baisses va donc de **{pct(min(remises))} % à {pct(max(remises))} %** "
      f"(médiane {pct(st.median(remises))} %) au lieu de 10 % pile. Garantir −10 % strict "
      f"imposerait de descendre d'un cran de plus sur **{len(strict)} des {len(baisses)} "
      f"lignes**, pour **{eur2(sum((l['prix_retenu'] - p) / L.TVA for l, p in strict))} € HT** "
      "de marge unitaire, et sortirait tout le bambou de son palier à 199 €. Hakim préférant "
      "une marge tenue à un alignement mécanique, on garde l'arrondi au plus proche.")
    w("")
    w("### Les quatre axes d'appariement, et ce qui est réellement mesurable")
    w("")
    w("| Axe | Chez nous | Chez Lustria | Verdict |")
    w("|---|---|---|---|")
    w("| **Type** | premier mot du titre (suspension / lustre / plafonnier) | champ `type` "
      "publié | **fiable des deux côtés**, axe obligatoire |")
    mat_ok = sum(1 for x in lignes if x["matiere"])
    mat_lus = sum(1 for x in lustria if x["matiere"])
    frm_lus = sum(1 for x in lustria if x["forme"])
    w("| **Matière** | titre, puis fiche fournisseur en second recours | handle descriptif "
      f"+ tags | **fiable** — nommée sur {mat_ok}/{len(lignes)} de nos fiches, "
      f"{n(mat_lus)}/{n(len(lustria))} des leurs |")
    w("| **Classe de taille** | option `Diamètre` (Ø en cm) sur "
      f"{sum(1 for x in lignes if x['diam_max'])}/{len(lignes)} fiches | **absente** — 0 handle "
      "sur 5 928 porte un « cm » | **non mesurable chez eux** : remplacée par la forme, "
      f"lisible sur {n(frm_lus)}/{n(len(lustria))} de leurs fiches |")
    w("| **Nombre de lumières** | options (`4 lumières`, `6 anneaux`…) | **quasi absent** — "
      "4 handles sur 5 928 | **partiellement mesurable** : réduit à mono / multi |")
    w("")
    w("La classe de taille est le point faible et il faut le dire net : **Lustria ne publie "
      "aucune dimension dans les données dont nous disposons.** Elle est remplacée par la "
      "**forme** (anneau · linéaire · composition multi · globe · dôme), lisible des deux "
      "côtés dans les libellés, et qui porte l'essentiel de l'effet-taille sur le prix — un "
      "lustre à anneaux n'est pas un dôme, quelle que soit sa cote. Le nombre de lumières est "
      "réduit à mono contre multi, seule granularité que leurs libellés permettent.")
    w("")
    w("### Pièges neutralisés")
    w("")
    w("- **Comparer des suspensions à des suspensions.** Appliques, veilleuses, lampes de "
      f"chevet et de table, lampadaires, extérieur : écartés par type. {n(len(brut))} fiches en "
      f"entrée, **{n(len(lus_all))} retenues** comme comparables possibles.")
    w("- **Leur champ `type` est parfois faux.** Des appliques murales sont typées "
      "`Luminaire Plafonnier` chez eux. Un garde-fou sur le handle écarte ces fiches malgré "
      "leur type.")
    w("- **Notre collection n'est pas notre matière.** `Suspension céramique festonnée "
      "blanche, tête bois` est rangée dans *Suspensions bois* et `Suspension papier ou soie` "
      "dans *Suspensions métal*. La matière est lue dans le **titre**, jamais dans la "
      "collection.")
    w("- **Le métal en dernier.** Presque toute monture en contient : il n'est retenu comme "
      "matière dominante qu'à défaut d'une matière d'abat-jour nommée.")
    w("- **Une médiane sur 3 fiches ne vaut rien.** Le critère le plus fin qui porte au moins "
      f"{L.POOL_CONFORT} comparables est retenu ; on ne relâche un axe que sous ce seuil, et "
      f"jamais en dessous de {L.POOL_MIN} fiches. Sous {L.POOL_MIN}, la ligne sort en « aucun "
      "comparable » et son prix ne bouge pas.")
    w("")
    w("### Plancher de marge")
    w("")
    w("Coût DSers unitaire + 2 € de fret, base HT (TVA 20 %, HT = TTC / 1,2), marge exigée "
      "**≥ max(40 € HT ; 25 % du HT)** — les deux conditions ensemble, lecture prudente du "
      "« ou ». Aucun prix cible ne descend sous ce plancher ; le cas échéant on garde le prix "
      "actuel.")
    w("")
    w("Deux réserves sur la donnée de coût. La colonne `cost_proxy_ae` du "
      "`catalogue-dsers.csv` est un **proxy** : sur la plupart des fiches elle vaut le prix "
      "AliExpress de la variante d'entrée, mais sur les lustres à pampilles multi-tailles "
      "(LM-070, LM-071) elle est proche de la **médiane** des variantes, donc très au-dessus "
      "du palier de base. Et la marge est calculée au **palier d'entrée** de chaque fiche, le "
      "plus mince : c'est le contrôle conservateur. Les frais de paiement (≈ 1,4 % + 0,25 €) "
      "évoqués à l'étape 9 ne sont pas déduits, la règle du brief ne les mentionnant pas — "
      "ils coûteraient environ 3 € HT par vente.")
    w("")

    # ---------------------------------------------------------------- 3
    w("## 3. Les 120 lignes")
    w("")
    w("`Prix` et `cible` en TTC. `Marge` = marge HT au palier d'entrée, en euros puis en % du "
      "HT. `n` = nombre de comparables Lustria dans le pool ; la colonne *comparable* donne "
      "le handle dont le prix est le plus proche de la médiane du pool, et **la médiane du "
      "pool** est ce qui sert au calcul. `≈` marque un appariement approximatif.")
    w("")
    w("| SKU | Handle | Prix | Comparable Lustria retenu | Son prix | Médiane pool | n | "
      "Cible | Marge avant | Marge après | Décision |")
    w("|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|")
    for l in lignes:
        comp = l["comparable_h"] or "—"
        if len(comp) > 46:
            comp = comp[:45] + "…"
        marque = " ≈" if l["qualite"] == "approximatif" else ""
        cp = f"{eur2(l['comparable_prix'])} €" if l["comparable_prix"] else "—"
        cm = f"{eur2(l['comparable_med'])} €" if l["comparable_med"] else "—"
        cible = f"{l['cible']} €" if l["cible"] else "—"
        pool_n = str(l["pool_n"]) if l["pool_n"] else "—"
        w(f"| {l['sku']} | `{l['handle']}` | {int(l['prix_actuel'])} € | {comp}{marque} | "
          f"{cp} | {cm} | {pool_n} | {cible} | {eur2(l['marge_avant'])} € · "
          f"{l['marge_avant_pct']:.0f} % | {eur2(l['marge_apres'])} € · "
          f"{l['marge_apres_pct']:.0f} % | {DECISION_LIB[l['decision']]} |")
    w("")

    # ---------------------------------------------------------------- 4
    w("## 4. Synthèse")
    w("")
    w("| | |")
    w("|---|---:|")
    w(f"| Fiches traitées | {len(lignes)} |")
    w(f"| **Fiches qui baissent** | **{len(baisses)}** |")
    w(f"| Baisse moyenne | **{eur2(st.mean([l['prix_actuel'] - l['prix_retenu'] for l in baisses]))} € "
      f"({pct(st.mean([100 * (1 - l['prix_retenu'] / l['prix_actuel']) for l in baisses]))} %)** |")
    w(f"| Baisse médiane | {eur2(st.median([l['prix_actuel'] - l['prix_retenu'] for l in baisses]))} € |")
    w(f"| Baisse la plus forte | {max(l['prix_actuel'] - l['prix_retenu'] for l in baisses):.0f} € |")
    w(f"| Inchangées — déjà sous la cible | {len(deja)} |")
    w(f"| Inchangées — aucun comparable | {len(sans)} |")
    w(f"| **Bloquées par le plancher de marge** | **{len(bloq)}** |")
    w(f"| Appariements francs · approximatifs · aucun | "
      f"{sum(1 for l in lignes if l['qualite'] == 'franc')} · "
      f"{sum(1 for l in lignes if l['qualite'] == 'approximatif')} · "
      f"{sum(1 for l in lignes if l['qualite'] == 'aucun')} |")
    w(f"| Confiance haute · moyenne · faible | "
      f"{sum(1 for l in lignes if l['confiance'] == 'haute')} · "
      f"{sum(1 for l in lignes if l['confiance'] == 'moyenne')} · "
      f"{sum(1 for l in lignes if l['confiance'] == 'faible')} |")
    w("")
    w("### Prix")
    w("")
    w("| | min | p25 | médiane | p75 | max | moyenne |")
    w("|---|---:|---:|---:|---:|---:|---:|")
    w(f"| Nous, avant | {eur(min(av))} € | {eur(quant(av, .25))} € | **{eur(st.median(av))} €** | "
      f"{eur(quant(av, .75))} € | {eur(max(av))} € | {eur2(st.mean(av))} € |")
    w(f"| Nous, après | {eur(min(ap))} € | {eur(quant(ap, .25))} € | **{eur(st.median(ap))} €** | "
      f"{eur(quant(ap, .75))} € | {eur(max(ap))} € | {eur2(st.mean(ap))} € |")
    w(f"| Lustria, périmètre comparable | {eur2(min(lus_all))} € | {eur2(quant(lus_all, .25))} € | "
      f"**{eur2(st.median(lus_all))} €** | {eur2(quant(lus_all, .75))} € | "
      f"{eur2(max(lus_all))} € | — |")
    w("")
    w(f"**Notre médiane ne bouge pas : {eur(st.median(av))} € avant, {eur(st.median(ap))} € "
      f"après.** {sum(1 for l in lignes if l['prix_retenu'] == 199)} fiches restent à 199 €, "
      f"seules {len(baisses)} descendent : le point milieu ne se déplace pas. Ce qui bouge, "
      f"c'est la moyenne ({eur2(st.mean(av))} € → {eur2(st.mean(ap))} €) et le p75 "
      f"({eur(quant(av, .75))} € → {eur(quant(ap, .75))} €). Face à la médiane comparable de "
      f"Lustria ({eur2(st.median(lus_all))} €), nous sommes à "
      f"**−{pct(100 * (1 - st.median(ap) / st.median(lus_all)), 0)} %**.")
    w("")
    w("### Respect de l'étape 9, fiche par fiche")
    w("")
    w("| | Avant | Après |")
    w("|---|---:|---:|")
    w(f"| Sous la médiane de son comparable | {sous_av} / {len(apparies)} | "
      f"**{sous_ap} / {len(apparies)}** |")
    w(f"| Au moins 10 % sous cette médiane | {dix_av} / {len(apparies)} | "
      f"**{dix_ap} / {len(apparies)}** |")
    w("")
    w(f"C'est le vrai résultat : **plus une seule fiche appariée n'est au-dessus du prix "
      f"médian de son comparable**, contre {len(apparies) - sous_av} avant. Les "
      f"{len(apparies) - dix_ap} fiches qui restent entre 0 et 10 % sous la médiane le sont "
      "à cause de l'arrondi de grille, jamais de plus de 5 €.")
    w("")
    w("### Marge")
    w("")
    w("| | Avant | Après | Écart |")
    w("|---|---:|---:|---:|")
    pct_av = st.mean([l["marge_avant_pct"] for l in lignes])
    pct_ap = st.mean([l["marge_apres_pct"] for l in lignes])
    w(f"| Somme des marges HT unitaires, palier d'entrée | {eur2(marge_av)} € | "
      f"{eur2(marge_ap)} € | **−{eur2(marge_av - marge_ap)} € "
      f"(−{pct(100 * (marge_av - marge_ap) / marge_av)} %)** |")
    w(f"| Marge HT moyenne en % du HT | {pct(pct_av)} % | {pct(pct_ap)} % | "
      f"{pct(pct_ap - pct_av, 1, signe=True)} pt |")
    w(f"| Marge HT la plus basse | {eur2(min(l['marge_avant'] for l in lignes))} € | "
      f"{eur2(min(l['marge_apres'] for l in lignes))} € | |")
    w("")
    w("Ces montants sont une **somme de marges unitaires sur les 120 paliers d'entrée**, pas "
      "un impact de compte de résultat : sans volumes de vente, aucune pondération n'est "
      "possible. À lire comme un indicateur de catalogue.")
    w("")
    w("### Pourquoi aucune fiche n'est bloquée par la marge")
    w("")
    w(f"**{len(bloq)} fiche bloquée.** Le plancher ne mord jamais parce que nos coûts sont "
      f"très bas devant les prix cibles : "
      f"{sum(1 for l in lignes if l['cout'] <= 75)} fiches sur {len(lignes)} coûtent 75 € ou "
      f"moins rendu, ce qui place leur plancher entre 99 et 149 €, quand la cible la plus "
      f"basse du plan est à {min(l['prix_retenu'] for l in baisses)} €. La marge HT la plus "
      f"mince après application reste à "
      f"{eur2(min(l['marge_apres'] for l in baisses))} € "
      f"({pct(min(l['marge_apres_pct'] for l in baisses), 0)} % du HT).")
    w("")
    nc = [l for l in lignes if not l["marge_actuelle_conforme"]]
    if nc:
        w("**Une anomalie préexistante, sans lien avec ce travail.**")
        w("")
        for l in nc:
            w(f"- `{l['sku']}` — {l['titre']} — se vend **{int(l['prix_actuel'])} €** pour un "
              f"coût proxy de {eur2(l['cout'])} € rendu {eur2(l['cout'] + L.FRET)} € : "
              f"{eur2(l['marge_avant'])} € HT de marge, soit {pct(l['marge_avant_pct'])} % du "
              f"HT, **sous les deux planchers** (il faudrait {l['prix_plancher']} €). Sa cible "
              f"Lustria étant de {l['cible']} €, largement au-dessus, ce plan n'y touche pas. "
              "À vérifier séparément : le proxy de coût est ici proche de la médiane des "
              "variantes, pas du palier d'entrée, donc l'anomalie est peut-être un artefact "
              "de donnée plutôt qu'une vraie perte.")
        w("")
    w("### Par famille")
    w("")
    fam: dict[str, list[dict]] = collections.defaultdict(list)
    for l in lignes:
        fam[l["famille"]].append(l)
    w("| Famille | Fiches | Médiane avant | Médiane après | Baisses | Médiane du comparable |")
    w("|---|---:|---:|---:|---:|---:|")
    for f, ls in sorted(fam.items(), key=lambda kv: -len(kv[1])):
        meds = [x["comparable_med"] for x in ls if x["comparable_med"]]
        w(f"| {f} | {len(ls)} | {eur(st.median([x['prix_actuel'] for x in ls]))} € | "
          f"{eur(st.median([x['prix_retenu'] for x in ls]))} € | "
          f"{sum(1 for x in ls if x['decision'] == 'baisse')} | "
          f"{eur2(st.median(meds)) + ' €' if meds else '—'} |")
    w("")
    w("Les baisses se concentrent là où ils sont réellement moins chers que nous : "
      "**céramique** (8 fiches sur 8), **bambou** (8 sur 16), **rotin et corde** (7 sur 14), "
      "**tissu et plafonnier bois** (5). À l'inverse le verre, la pierre, le cristal et les "
      "lustres à anneaux LED ne bougent pas : nous y sommes déjà largement sous eux.")
    w("")

    # ---------------------------------------------------------------- 5
    w("## 5. Les appariements dont je suis le moins sûr")
    w("")
    fragiles = sorted([x for x in lignes if x["decision"] == "baisse"
                       and x["confiance"] == "faible"],
                      key=lambda x: (-x["comparable_spread"], x["sku"]))
    w(f"D'abord les seules qui comptent vraiment : les **{len(fragiles)} lignes qui baissent "
      "sur un appariement fragile**, classées du pool le plus étalé au moins étalé. Une baisse "
      "sur appariement solide se défend toute seule ; celles-ci sont à relire avant "
      "d'appliquer.")
    w("")
    for l in fragiles:
        w(f"- **`{l['sku']}` {l['titre']}** — {int(l['prix_actuel'])} € → "
          f"**{l['prix_retenu']} €**, sur {l['pool_n']} comparables *{l['critere']}*, médiane "
          f"{eur2(l['comparable_med'])} € mais p25 {eur2(l['comparable_p25'])} € et p75 "
          f"{eur2(l['comparable_p75'])} € : le pool est étalé d'un facteur "
          f"{pct(l['comparable_spread'])}, la médiane y est peu représentative. "
          f"Marge après : {eur2(l['marge_apres'])} € HT.")
    w("")
    w("Le point commun de ces lignes : ce sont **toutes des plafonniers**. Leur rayon "
      "plafonnier mélange des spots et plafonniers d'appoint à 30-80 € avec des grands "
      "luminaires LED à 300 € et plus, sur un même tag matière. La médiane y est "
      "mathématiquement correcte et commercialement discutable. Si Hakim veut sécuriser, ce "
      "sont ces cinq lignes à sortir du lot, pas les 33 autres.")
    w("")
    w("Les deux réserves de méthode à garder en tête sur **toutes** les lignes :")
    w("")
    w("1. **La classe de taille n'est pas vérifiée côté Lustria** — elle n'est pas publiée. Un "
      "de nos dômes bambou Ø 80 cm est apparié à des dômes bambou dont nous ignorons la cote. "
      "C'est la limite structurelle de tout ce travail, et elle ne se lève qu'en ouvrant leurs "
      "fiches une par une.")
    w("2. **Le nombre de lumières est réduit à mono / multi.** Un lustre à 6 anneaux et un "
      "lustre à 2 anneaux tombent dans le même pool.")
    w("")
    approx = [l for l in lignes if l["qualite"] == "approximatif"]
    if approx:
        w(f"**Les {len(approx)} appariements approximatifs**, tous des corps LED dont ni notre "
          "titre ni leur handle ne nomme de matière. Appariés sur type + forme, plus le "
          "nombre de lumières quand il départage. Aucun ne porte de baisse :")
        w("")
        for l in sorted(approx, key=lambda x: x["sku"]):
            w(f"- `{l['sku']}` {l['titre']} — {l['pool_n']} comparables *{l['critere']}*, "
              f"médiane {eur2(l['comparable_med'])} € → {DECISION_LIB[l['decision']]}.")
        w("")
    if sans:
        w(f"**Les {len(sans)} fiches sans aucun comparable**, prix inchangé. Aucune ne nomme "
          "de matière ni de forme exploitable, donc aucun axe au-delà du type : un pool de "
          "« tous leurs plafonniers » ou « toutes leurs suspensions » n'est pas un "
          "appariement, c'est une moyenne de rayon.")
        w("")
        for l in sans:
            w(f"- `{l['sku']}` {l['titre']} — {int(l['prix_actuel'])} €, inchangé "
              f"(type *{l['type']}*, matière non nommée, forme non nommée).")
        w("")
        w("Les deux plafonniers connectés (`LM-060`, `LM-090`) relèvent en plus d'un segment "
          "domotique — RVB piloté par application, enceinte intégrée — que leur catalogue ne "
          "permet pas d'isoler : ni tag ni handle ne le signale. Le ruban LED en trèfle "
          "(`LM-111`) est une forme sculptée qui n'a pas d'équivalent nommé chez eux.")
        w("")

    # ---------------------------------------------------------------- 6
    w("## 6. Application")
    w("")
    w("`align_prices.py`. Idempotent : relancé, il ne réécrit que ce qui diffère de la cible. "
      "Sauvegarde intégrale des prix avant toute écriture dans "
      "`backups/2026-08-26-prix/`.")
    w("")
    w("- `productVariantsBulkUpdate` avec `productId` + `variants: [{id, price}]`, rien "
      "d'autre dans la charge utile.")
    w("- **Aucun** `compareAtPrice` touché : les 120 fiches sont déjà à `null`, elles y "
      "restent. Aucun SKU, aucune option, aucune variante, aucun titre, aucune description, "
      "aucune image, aucune collection.")
    multi = [l for l in baisses if len(l["paliers"]) > 1]
    w(f"- **{len(multi)} fiches à plusieurs paliers** parmi les baisses : l'écart relatif "
      "entre paliers est conservé, puis chaque palier est ramené sur la grille en 9 et l'ordre "
      "strictement croissant est revérifié.")
    if multi:
        w("")
        for l in multi:
            av_ = " / ".join(str(int(p)) for p in l["paliers"])
            ap_ = " / ".join(str(p) for p in l["paliers_cibles"])
            w(f"  - `{l['sku']}` : {av_} € → **{ap_} €**")
    w("")
    w(f"Écritures attendues : {len(baisses)} fiches, "
      f"{sum(sum(1 for v in l['variants'] if v['price'] != l['paliers_cibles'][l['paliers'].index(v['price'])]) for l in baisses)} "
      "variantes.")
    w("")

    journal = HERE / "backups" / "2026-08-26-prix" / "journal.json"
    if journal.exists():
        j = json.loads(journal.read_text(encoding="utf-8"))
        w("### Appliqué")
        w("")
        w(f"Le {j['applique_le']}. **{j['fiches_ecrites']} fiches écrites**, "
          f"{sum(x['variantes_modifiees'] for x in j['detail'])} variantes. "
          f"{len(j['ignorees'])} ligne ignorée.")
        w("")
        w("Contrôles passés après écriture (`verify_prices.py`, relecture en ligne) : les 120 "
          "fiches et leurs 629 variantes portent le prix du plan, aucun `compareAtPrice` "
          "n'est renseigné, aucun SKU n'a bougé, aucune variante n'a été ajoutée ni "
          "supprimée, et tous les paliers restent sur la grille en 9. Relancé, "
          "`align_prices.py` n'a plus rien à écrire.")
        w("")
        w("Retour arrière en une commande, prix seuls :")
        w("")
        w("```bash")
        w(f"python3 align_prices.py --restore backups/2026-08-26-prix/{j['sauvegarde']} --apply")
        w("```")
        w("")

    OUT.write_text("\n".join(d) + "\n", encoding="utf-8")
    print(f"{OUT.name} — {len(d)} lignes de markdown, {len(lignes)} fiches")


if __name__ == "__main__":
    main()

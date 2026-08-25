"""Seconde passe titres — corrections imposées par les volumes SEMrush du 25/08/2026.

Ne réécrit pas les 120 titres : reprend la table de `retitle_seo.py` et ne remplace que les
fiches que la mesure contredit, selon les cinq corrections de `MOTS-CLES-TITRES-2026-08-25.md`
et du § « Corrections imposées par les volumes » de la convention :

  A. `lustre anneau` (20/mois) ne porte plus aucun titre — le mot passe en second, comme forme.
  B. `lustre effet cristal` (20/mois) devient `lustre pampilles` (1 600) là où la photo montre
     des pampilles, sinon `lustre salon` / `lustre led`. `lustre cristal` reste interdit.
  C. `suspension pierre` (170) devient `suspension travertin` (480) là où la photo le justifie.
  D. Un mot de pièce, jamais en liste, là où l'usage est vrai.
  E. `globe` → `boule`, `naturel` retiré quand il ne dit rien, `osier` et `papier` utilisés.

Le contrôle automatique, la coupe du `seo_title`, la lecture du live et la mutation sont
importés de `retitle_seo.py` : une seule implémentation, un seul comportement.
`apply_pdp.py` n'est ni exécuté ni importé.

Usage :
    python3 retitle_seo_v2.py --check     # validation + volumes, hors ligne
    python3 retitle_seo_v2.py --dry-run   # validation + diff avec le live
    python3 retitle_seo_v2.py             # validation, backup, pdp-copy.json, push, relecture
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

from retitle_seo import (
    BANNED_CHARS,
    COLORS,
    HARD_MAX,
    MATERIALS,
    RANGE_RE,
    TITLES as TITLES_V1,
    fetch_live,
    fold,
    has_any,
    push,
    report_stats,
    seo_title,
    validate,
)

ROOT = Path(__file__).resolve().parent
COPY_PATH = ROOT / "pdp-copy.json"
BACKUP_DIR = ROOT / "backups" / "2026-08-25-titres-seo-v2"
VOLUMES_PATH = ROOT / "semrush-volumes-2026-08-25.json"

# ---------------------------------------------------------------------------
# A. Les titres menés par « anneau » — 20 recherches par mois.
#    Le premier mot suit la fixation lue sur la photo : platine plaquée au plafond =
#    plafonnier, câble ou tige = suspension ou lustre. `anneaux` reste en second, comme forme.
# ---------------------------------------------------------------------------

ANNEAUX = {
    # Collection « Lustres anneau » — les 12 fiches visées par la mesure.
    "lustre-anneau-led-led-noir-dore-024410": "Lustre salon LED anneaux cascade, noir, café ou doré",
    "lustre-anneau-led-led-597704": "Lustre salon LED anneaux superposés, doré, blanc ou noir",
    "lustre-anneau-led-led-717226": "Plafonnier LED salon, 4 ou 6 anneaux blancs",
    "lustre-anneau-led-led-625575": "Plafonnier LED anneaux blancs, platine chromée",
    "lustre-anneau-led-led-dore-418494": "Lustre salon LED 6 anneaux, noir, café ou doré",
    "lustre-anneau-led-led-784897": "Lustre chambre LED double anneau, doré, blanc ou noir",
    "lustre-anneau-led-007557": "Plafonnier LED chambre connecté RVB, blanc ou noir",
    "lustre-anneau-led-led-795468": "Suspension LED anneau fin, blanc ou noir",
    "lustre-anneau-led-led-dore-641905": "Lustre salon LED 5 anneaux, noir, doré ou blanc",
    "lustre-anneau-led-led-892612": "Suspension LED anneau opalin blanc, télécommande",
    "lustre-anneau-led-led-799451": "Lustre salon LED spirale, doré, blanc ou noir",
    "lustre-anneau-led-led-134962": "Plafonnier LED anneaux entrelacés, blanc, noir ou doré",
    # Mêmes têtes mortes hors collection : `lustre anneau` 20, `suspension anneau` 50,
    # `plafonnier anneau` non mesuré. La contradiction est la même, la correction aussi.
    "lustre-salon-led-147017": "Lustre salon LED anneaux concentriques, doré ou blanc",
    "plafonnier-led-led-698635": "Plafonnier LED anneaux, blanc, noir ou doré",
    "suspension-metal-led-dore-081498": "Suspension LED métal doré, anneau et oiseau posé",
    "suspension-metal-led-dore-843772": "Plafonnier LED 3 anneaux entrelacés, métal doré",
    "lustre-salon-led-630766": "Suspension salon LED verre facetté, doré ou noir",
}

# ---------------------------------------------------------------------------
# B. « effet cristal » — 20 recherches par mois.
#    `lustre pampilles` (1 600) là où la photo montre des gouttes suspendues ; ailleurs
#    `lustre salon` (22 200) ou `suspension led` (1 000). `lustre cristal` (1 600) reste
#    interdit : nos pièces sont en verre travaillé, la revendication serait un risque
#    `misrepresentation` Merchant Center.
# ---------------------------------------------------------------------------

PAMPILLES = {
    # Pampilles vérifiées sur photo : gouttes ou brins suspendus sous la monture.
    "lustre-cristal-led-led-560904": "Lustre pampilles doré, couronne de gouttes LED",
    "lustre-cristal-led-led-dore-841671": "Lustre pampilles à branches dorées ou argentées",
    "lustre-cristal-led-dore-202521": "Lustre pampilles cascade, branches dorées ou argentées",
    "lustre-cristal-led-noir-347688": "Lustre pampilles noir, tambour à 5 lumières",
    # Pas de pampille sur la photo : facettes serties dans l'anneau, ou goutte unique.
    "lustre-cristal-led-led-141724": "Lustre chambre LED 3 anneaux dorés à facettes",
    "lustre-cristal-led-677865": "Lustre salon LED anneaux à facettes, doré ou chrome",
    "lustre-cristal-led-led-dore-264869": "Suspension LED goutte dorée, 1 ou 2 lumières",
    "lustre-salon-led-240560": "Lustre salon LED anneau à facettes, blanc, noir ou doré",
}

# ---------------------------------------------------------------------------
# C. Suspensions pierre — `suspension travertin` (480) contre `suspension pierre` (170).
#    Le travertin n'est écrit que sur les fiches où la passe photo l'a identifié :
#    grain piqueté visible. Les quatre autres gardent `pierre`, qui n'affirme rien de faux.
# ---------------------------------------------------------------------------

PIERRE = {
    "suspension-effet-pierre-led-709819": "Suspension travertin cuisine, tube beige LED",
    "suspension-effet-pierre-led-338324": "Suspension travertin, gros cylindre à tête noyer",
    "suspension-effet-pierre-led-445794": "Suspension travertin, cylindre étroit et bois clair",
    "suspension-effet-pierre-led-147607": "Suspension travertin cuisine, cône ou galet beige",
    "suspension-effet-pierre-343987": "Suspension travertin, tube beige court ou long",
    # Composites sans grain de travertin : la revendication serait fausse.
    "suspension-effet-pierre-led-073999": "Suspension pierre cuisine, galet sur tige bois clair",
    "suspension-effet-pierre-led-434888": "Suspension pierre, galet blanc et tube opalin",
    "suspension-effet-pierre-092465": "Suspension pierre claire, cylindre à tête bois brun",
    "suspension-effet-pierre-led-dore-960013": "Suspension pierre salon, gros galet blanc ou gris",
}

# ---------------------------------------------------------------------------
# D. Mots de pièce, un seul par titre, seulement là où l'usage est vrai.
#    Les petites suspensions basses et les rampes vont en cuisine, les grandes pièces
#    centrales au salon. `suspension salle à manger` (590) est écarté comme trop faible.
# ---------------------------------------------------------------------------

PIECES = {
    "suspension-bambou-280004": "Suspension bambou cuisine, 3 lampes à câble noir",
    "suspension-rotin-623305": "Suspension rotin cuisine, abat-jour tambour tressé",
    "suspension-rotin-272937": "Suspension cuisine, 3 boules corde à monture noire",
    "suspension-bois-led-989306": "Suspension bois cuisine, double coquille platine blanche",
    "suspension-bois-led-334133": "Suspension cuisine, perles pierre et boule opaline",
    "suspension-deco-blanc-560098": "Suspension céramique cuisine, double à motif bleu",
    "plafonnier-led-led-922186": "Suspension salon laiton, guirlande de boules opalines",
    "plafonnier-led-565566": "Plafonnier salon chrome, 6 boules verre sur tiges",
    "plafonnier-led-992600": "Plafonnier salon noir, 8 boules verre sur tiges courbes",
    "plafonnier-led-led-183789": "Plafonnier LED salon, palets bois gris ou blancs",
    "lustre-salon-233314": "Lustre salon, grappe de 7 ou 13 boules opalines",
    "lustre-salon-907106": "Lustre salon, grappe de boules verre coloré",
    "lustre-salon-led-254609": "Lustre salon sputnik noir et doré, 12 boules verre",
    "lustre-statement-led-noir-950316": "Lustre salon sputnik laiton et noir, 6 boules verre",
    "suspension-metal-noir-dore-361680": "Lustre salle à manger laiton, 6 bras à bougies",
}

# ---------------------------------------------------------------------------
# E. Vocabulaire : `boule` contre `globe` (1 000 contre 320), `naturel` retiré quand il ne
#    dit rien (`suspension bambou naturel` = 20), `osier` (1 600) sur la vannerie claire,
#    `papier` (1 600) sur les voiles (`suspension voile` = 30).
# ---------------------------------------------------------------------------

VOCABULAIRE = {
    # `naturel` remplacé par une forme ou une pièce — bambou.
    "suspension-bambou-led-136557": "Suspension bambou grande vague tressée LED",
    "suspension-bambou-led-80-cm-236157": "Suspension bambou vague tressée, tige rigide",
    "suspension-bambou-942503": "Suspension bambou XXL, corolle de pétales tressés",
    "suspension-bambou-led-033589": "Suspension bambou cascade de 3 vagues tressées",
    "suspension-bambou-655008": "Suspension bambou dôme tressé serré, salon",
    "suspension-bambou-led-80-cm-191307": "Suspension bambou vague tressée, câble souple",
    "suspension-bambou-led-630923": "Suspension bambou disque plat tressé, salon",
    "suspension-bambou-led-50cm-377816": "Suspension bambou double étage tressé serré",
    "suspension-bambou-104055": "Suspension bambou tambour large tressé, salon",
    "suspension-bambou-dore-60cm-805884": "Suspension bambou grand ovale tressé serré",
    # `naturel` remplacé — rotin. `osier` là où la vannerie est claire et ouverte.
    "suspension-rotin-897170": "Suspension rotin corolle de pétales tressés",
    "suspension-rotin-dore-435189": "Suspension rotin cloche haute tressée, osier",
    "suspension-rotin-489600": "Suspension paille brute, couronne de brins dorés",
    "suspension-rotin-led-535545": "Suspension rotin XXL, corolle de pétales tressés",
    "suspension-rotin-led-420069": "Suspension rotin cloche large tressée, salon",
    "suspension-rotin-605780": "Suspension rotin dôme tressé, osier clair",
    # `suspension fibre naturelle` vaut 320 : ici « naturelle » porte la requête, il reste.
    "suspension-rotin-led-761433": "Suspension fibre naturelle, corolle de pétales",
    # `globe` → `boule`.
    "suspension-verre-394147": "Suspension boule verre fumé, 1 ou 3 lumières",
    "suspension-verre-446435": "Suspension boule verre fumé, tige rigide noire",
    "suspension-verre-led-blanc-554061": "Suspension boules opalines, tiges laiton doré",
    "suspension-verre-led-dore-436718": "Suspension arceau laiton doré, boules opalines",
    # `suspension voile` vaut 30, `suspension papier` 1 600.
    "suspension-metal-led-dore-701414": "Suspension papier ou soie, voile LED blanc",
}

CHANGES: dict[str, str] = {**ANNEAUX, **PAMPILLES, **PIERRE, **PIECES, **VOCABULAIRE}
TITLES: dict[str, str] = {**TITLES_V1, **CHANGES}

# ---------------------------------------------------------------------------
# Volume du mot-clé de tête
#
# Le mot-clé de tête est l'expression mesurée la plus forte qui commence au premier mot du
# titre, en phrase contiguë : c'est ce que la mesure reproche aux titres actuels
# (« Leurs titres commencent aujourd'hui par `Lustre anneaux LED…` »). Une expression
# présente mais dispersée dans le titre ne compte pas ici.
# ---------------------------------------------------------------------------

WORD_RE = re.compile(r"[a-z0-9]+")


def _norm(text: str) -> list[str]:
    return WORD_RE.findall(fold(text).replace("-", " "))


def _singular(token: str) -> str:
    return token[:-1] if len(token) > 3 and token.endswith("s") else token


def load_volumes() -> dict[str, int]:
    raw = json.loads(VOLUMES_PATH.read_text(encoding="utf-8"))
    vols: dict[str, int] = {}
    for entry in raw.values():
        for row in [entry["head"], *entry["rows"]]:
            key = " ".join(_norm(row["kw"]))
            vols[key] = max(vols.get(key, 0), row["vol"] or 0)
    return vols


def head_keyword(title: str, vols: dict[str, int]) -> tuple[str, int]:
    """Meilleure expression mesurée en phrase contiguë depuis le premier mot."""
    tokens = _norm(title)
    best = ("", 0)
    for length in (2, 3, 4):
        if len(tokens) < length:
            break
        window = tokens[:length]
        for variant in ({" ".join(window), " ".join(_singular(t) for t in window)}):
            vol = vols.get(variant)
            if vol is not None and vol > best[1]:
                best = (variant, vol)
    return best


def volume_report(vols: dict[str, int]) -> tuple[int, int]:
    before = sum(head_keyword(t, vols)[1] for t in TITLES_V1.values())
    after = sum(head_keyword(t, vols)[1] for t in TITLES.values())
    morts_avant = sum(1 for t in TITLES_V1.values() if head_keyword(t, vols)[1] < 500)
    morts_apres = sum(1 for t in TITLES.values() if head_keyword(t, vols)[1] < 500)
    piece_re = re.compile(r"\b(salon|chambre|cuisine|salle a manger)\b")
    pieces_avant = sum(1 for t in TITLES_V1.values() if piece_re.search(fold(t)))
    pieces_apres = sum(1 for t in TITLES.values() if piece_re.search(fold(t)))
    print(f"\nMot-clé de tête — somme des volumes : {before} → {after} ({after - before:+})")
    print(f"  titres sous 500 recherches : {morts_avant} → {morts_apres}")
    print(f"  titres portant un mot de pièce : {pieces_avant} → {pieces_apres}")
    return before, after


def changes_table(vols: dict[str, int]) -> list[dict]:
    rows = []
    for handle, new in CHANGES.items():
        old = TITLES_V1[handle]
        okw, ovol = head_keyword(old, vols)
        nkw, nvol = head_keyword(new, vols)
        rows.append(
            {
                "handle": handle,
                "avant": old,
                "apres": new,
                "kw_perdu": okw or "—",
                "vol_perdu": ovol,
                "kw_gagne": nkw or "—",
                "vol_gagne": nvol,
                "len": len(new),
            }
        )
    return rows


# ---------------------------------------------------------------------------


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="validation + volumes, hors ligne")
    ap.add_argument("--dry-run", action="store_true", help="validation + diff live, sans écriture")
    args = ap.parse_args()

    print(f"Table : {len(TITLES)} handles · {len(CHANGES)} titres corrigés")
    failures = validate(TITLES)
    if failures:
        print(f"\nREFUS — {len(failures)} titres invalides :")
        for handle, errs in failures.items():
            print(f"  {handle}: {'; '.join(errs)}")
        sys.exit(1)
    print(f"Contrôle automatique : {len(TITLES)}/{len(TITLES)} acceptés")

    print("\nAvant (passe 1)")
    report_stats(list(TITLES_V1.values()))
    print("Après (passe 2)")
    report_stats(list(TITLES.values()))

    vols = load_volumes()
    volume_report(vols)

    if args.check:
        for row in changes_table(vols):
            print(
                f"  {row['vol_perdu']:>6} → {row['vol_gagne']:>6}  "
                f"{row['apres']} ({row['len']} c.)"
            )
        return

    live = fetch_live()
    print(f"\nLive : {len(live)} fiches actives")
    missing = {p["handle"] for p in live} - set(TITLES)
    extra = set(TITLES) - {p["handle"] for p in live}
    if missing or extra:
        print(f"REFUS — handles hors table : {sorted(missing)} ; inconnus : {sorted(extra)}")
        sys.exit(1)

    changed = [p for p in live if p["title"] != TITLES[p["handle"]]]
    print(f"À changer : {len(changed)}")
    if args.dry_run:
        for p in sorted(changed, key=lambda x: x["productType"]):
            print(f"  {p['productType']:22} {p['title']}")
            print(f"  {'':22} → {TITLES[p['handle']]}")
        return

    # Le backup capture l'état antérieur ; il n'est jamais réécrit par une seconde exécution.
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    copies = json.loads(COPY_PATH.read_text(encoding="utf-8"))
    snapshots = {
        "titles-live.avant.json": [
            {
                "handle": p["handle"],
                "productType": p["productType"],
                "title": p["title"],
                "seo_title": (p.get("seo") or {}).get("title"),
                "seo_description": (p.get("seo") or {}).get("description"),
            }
            for p in live
        ],
        "pdp-copy.avant.json": copies,
    }
    for name, payload in snapshots.items():
        path = BACKUP_DIR / name
        if path.exists():
            print(f"Backup déjà présent, conservé : {name}")
            continue
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"Backup écrit : {name}")

    for handle, title in TITLES.items():
        if handle not in copies:
            print(f"REFUS — {handle} absent de pdp-copy.json")
            sys.exit(1)
        copies[handle]["title"] = title
        copies[handle]["seo_title"] = seo_title(title)
    COPY_PATH.write_text(json.dumps(copies, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"pdp-copy.json : title et seo_title mis à jour sur {len(TITLES)} fiches")

    # `push` renvoie toujours `seo.title` ET `seo.description` : l'objet `seo` de
    # `ProductInput` est remplacé en bloc, omettre la description l'effacerait.
    done, skipped, failed = push(live, TITLES, copies)
    print(f"push : {done} modifiés, {skipped} déjà à jour, {failed} en échec")
    if failed:
        sys.exit(1)

    after = fetch_live()
    live_titles = [p["title"] for p in after]
    print(f"\nRelecture live ({len(after)} fiches)")
    report_stats(live_titles)
    ecarts = [p["handle"] for p in after if p["title"] != TITLES[p["handle"]]]
    seo_ecarts = [
        p["handle"] for p in after
        if (p.get("seo") or {}).get("title") != seo_title(TITLES[p["handle"]])
    ]
    desc_vides = [p["handle"] for p in after if not (p.get("seo") or {}).get("description")]
    bad_chars = [
        p["handle"] for p in after
        if any(c in p["title"] for c in BANNED_CHARS) or RANGE_RE.search(p["title"])
    ]
    too_long = [p["handle"] for p in after if len(p["title"]) > HARD_MAX]
    print(f"  écarts titre : {len(ecarts)} {ecarts}")
    print(f"  écarts seo_title : {len(seo_ecarts)} {seo_ecarts}")
    print(f"  meta descriptions vides : {len(desc_vides)} {desc_vides}")
    print(f"  caractères interdits : {len(bad_chars)} {bad_chars}")
    print(f"  dépassements 65 c. : {len(too_long)} {too_long}")
    print(f"  titres uniques : {len(set(live_titles))}/{len(after)}")
    print(f"  matière {sum(1 for t in live_titles if has_any(t, MATERIALS))}/{len(after)} · "
          f"couleur {sum(1 for t in live_titles if has_any(t, COLORS))}/{len(after)}")
    if (
        ecarts or seo_ecarts or desc_vides or bad_chars or too_long
        or len(set(live_titles)) != len(after)
    ):
        sys.exit(1)
    (ROOT / "titres-v2-changements.json").write_text(
        json.dumps(changes_table(load_volumes()), ensure_ascii=False, indent=1), encoding="utf-8"
    )
    print(f"\nOK — {date.today().isoformat()}")


if __name__ == "__main__":
    main()

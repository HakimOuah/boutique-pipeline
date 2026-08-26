#!/usr/bin/env python3
"""Réécrit pdp-copy.json en copy humanisée : titres uniques, zéro tiret cadratin, rythme varié.

Ne touche ni aux variantes ni aux SKU. Écrit uniquement pdp-copy.json ;
le push se fait ensuite via apply_pdp.push_copy.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from build_pdp_copy import appearance_of, detect_source, diameters_cm, et_join, is_blind_code, ou_join  # noqa: E402

COPY_PATH = ROOT / "pdp-copy.json"
LIVE_PATH = ROOT / "titles-live-2026-08-25.json"
ROWS_PATH = ROOT / "pdp-options-live.json"

# ── Titres différenciés : 13 groupes de doublons, lus sur la photo featured ──────
TITLE_OVERRIDES: dict[str, str] = {
    # « Suspension effet pierre, LED » ×4
    "suspension-effet-pierre-led-073999": "Suspension effet pierre, galet plat sur tige de bois clair",
    "suspension-effet-pierre-led-338324": "Suspension effet pierre, large cylindre à capot noyer",
    "suspension-effet-pierre-led-445794": "Suspension effet pierre, cylindre étroit, bois clair ou foncé",
    "suspension-effet-pierre-led-147607": "Suspension effet pierre, trois formes au choix",
    # « Suspension déco en céramique, LED » ×4
    "suspension-deco-led-837156": "Suspension céramique festonnée, vert céladon ou bleu poudré",
    "suspension-deco-led-077631": "Suspension céramique à fleurs bleues, douille laiton",
    "suspension-deco-led-889929": "Suspension grappe de cônes en céramique, deux modèles",
    "suspension-deco-led-689455": "Suspension 3 lumières, céramique nervurée et laiton",
    # « Suspension bois, LED » ×3
    "suspension-bois-led-830581": "Suspension bois tourné, ampoule globe apparente",
    "suspension-bois-led-453740": "Suspension bois en forme de guitare, 6 lanternes de verre",
    "suspension-bois-led-934110": "Suspension tube vertical effet travertin, rosace bois foncé",
    # « Suspension rotin tressée » ×3
    "suspension-rotin-469688": "Suspension rotin tressé, 3 lanternes sur platine noire",
    "suspension-rotin-623305": "Suspension rotin tressé, abat-jour tambour, une lumière",
    "suspension-rotin-272937": "Suspension corde de chanvre tressée, 1 ou 3 lumières",
    # « Lustre anneau LED, Ø 40–100 cm, noir, café ou doré » ×2
    "lustre-anneau-led-led-noir-dore-024410": "Lustre anneaux LED en cascade, 1 à 4 anneaux, noir, café ou doré",
    "lustre-anneau-led-led-dore-418494": "Lustre 6 anneaux LED superposés, noir, café ou doré",
    # « Lustre anneau LED, 4 lumières et 6 lumières » ×2
    "lustre-anneau-led-led-717226": "Lustre anneaux LED blancs, 4 ou 6 lumières, tige de suspension",
    "lustre-anneau-led-led-625575": "Plafonnier anneaux LED blancs, 4 ou 6 lumières, platine chromée",
    # « Suspension déco en céramique, blanc » ×2
    "suspension-deco-348096": "Suspension dôme en céramique blanche ajourée",
    "suspension-deco-blanc-560098": "Suspension double en céramique à motifs bleus, laiton",
    # « Suspension métal, LED, doré » ×2
    "suspension-metal-led-dore-952116": "Suspension céramique bleu et blanc, monture laiton",
    "suspension-metal-led-dore-975417": "Suspension corolle plissée blanche, cordon doré",
    # « Plafonnier LED, intérieur » ×2
    "plafonnier-led-led-637673": "Plafonnier LED rond, lumière colorée et enceinte intégrée",
    "plafonnier-led-led-922186": "Suspension guirlande de globes opalins, 5 à 20 globes",
    # « Suspension bois, LED, Ø 40–80 cm » ×2
    "suspension-bois-led-989306": "Suspension double coquille en bois tressé, platine linéaire blanche",
    "suspension-bois-led-582321": "Suspension double coquille en bois tressé, rosace ronde dorée",
    # « Suspension bambou tissée, LED, Ø 40–80 cm » ×2
    "suspension-bambou-led-80-cm-236157": "Suspension bambou tressé en vague, tige rigide, Ø 40 à 80 cm",
    "suspension-bambou-led-80-cm-191307": "Suspension bambou tressé en vague, câble souple, Ø 40 à 80 cm",
    # « Suspension bambou tissée, LED, Ø 40–100 cm, câble blanc, noir ou doré » ×2
    "suspension-bambou-led-583180": "Suspension bambou tressé, une vague, Ø 40 à 100 cm",
    "suspension-bambou-led-033589": "Suspension bambou tressé, 3 vagues en cascade, Ø 40 à 100 cm",
    # « Suspension bambou tissée, Ø 30–45 cm » ×2
    "suspension-bambou-655008": "Suspension dôme en bambou tressé serré, tige de bois",
    "suspension-bambou-655463": "Suspension coupole en bambou tressé, câble noir",
    # Valeur d’option « Blanc chaud » renommée « Pierre claire » (photo : teinte du corps)
    "suspension-effet-pierre-092465": "Suspension pierre translucide, pierre claire ou brun",
    # ── Fiches hors doublons dont la photo contredisait le titre repris du catalogue ──
    "lustre-anneau-led-007557": "Plafonnier LED connecté, lumière RVB, blanc ou noir",
    "lustre-salon-233314": "Lustre grappe de globes effet lune, 7 ou 13 lumières",
    "lustre-salon-907106": "Lustre grappe de globes en verre coloré, 1 à 8 lumières",
    "lustre-salon-led-254609": "Lustre sputnik, 4, 8 ou 12 globes, doré, noir ou bicolore",
    "lustre-statement-led-noir-950316": "Lustre sputnik noir et laiton, 4, 6 ou 8 globes",
    "plafonnier-led-565566": "Plafonnier tiges croisées, 6 globes, cuivre ou chrome",
    "plafonnier-led-992600": "Plafonnier tiges courbes, 4, 6 ou 8 globes, noir, blanc ou doré",
    "plafonnier-led-led-442025": "Suspension boule d’épines dorées, Ø 65 cm",
    "plafonnier-led-led-728204": "Réglette LED au plafond, 60 à 200 cm, blanc ou noyer",
    "suspension-bois-059364": "Suspension tonneau en bois, chaîne et rosace métal",
    "suspension-bois-193329": "Suspension travertin à capot noyer, bois clair ou foncé",
    "suspension-bois-832012": "Suspension 3 gouttes de verre, tête bois, fumé, ambre ou clair",
    "suspension-bois-led-121862": "Suspension abat-jour festonné en céramique, tête bois",
    "suspension-bois-led-245113": "Suspension cylindre travertin et bois foncé, Ø 17 cm",
    "suspension-bois-led-334133": "Suspension perles de pierre et bois, globe opalin",
    "suspension-bois-led-30cm-886635": "Suspension abat-jour plissé en céramique, Ø 30 cm",
    "suspension-deco-253182": "Suspension céramique émaillée, trois modèles, monture laiton",
    "suspension-deco-led-blanc-805304": "Suspension coupelle en céramique à motifs, cordon laiton",
    "suspension-effet-pierre-343987": "Suspension effet pierre, tube court ou long",
    "suspension-effet-pierre-led-dore-960013": "Suspension galet effet pierre, Ø 40 à 70 cm",
    "suspension-metal-dore-037279": "Suspension dôme en céramique gaufrée, monture laiton",
    "suspension-metal-dore-502141": "Suspension abat-jour tissu sur armature laiton, Ø 35 à 55 cm",
    "suspension-metal-led-dore-081498": "Suspension anneau LED et oiseau doré",
    "suspension-metal-led-dore-701414": "Suspension voile LED, Ø 40 à 100 cm, papier ou soie",
    "suspension-metal-led-dore-843772": "Plafonnier 3 anneaux LED dorés, Ø 40 à 80 cm",
    "suspension-metal-noir-dore-361680": "Lustre laiton à bougies, 4, 6 ou 8 bras",
    "suspension-rotin-443915": "Suspension corde tressée en cloche, Ø 30 à 60 cm",
    "suspension-rotin-477244": "Suspension corolle en corde tressée, Ø 40 à 60 cm",
    "suspension-rotin-489600": "Suspension paille brute, Ø 40 à 80 cm",
    "suspension-rotin-dore-865596": "Suspension bois deux pétales, Ø 39 à 85 cm, monture dorée",
    "suspension-rotin-led-761433": "Suspension corolle en fibre tressée, Ø 30 à 60 cm",
    "suspension-verre-091815": "Suspension nuages en verre soufflé, Ø 20 à 40 cm",
    "suspension-verre-394147": "Suspension globe en verre double paroi, 1 ou 3 lumières",
    "suspension-verre-led-489156": "Suspension nuages en verre soufflé LED, Ø 20 à 40 cm",
    # ── Titres encore génériques après le premier passage : relus sur la photo ──
    "lustre-salon-957153": "Suspension ruban LED en trèfle, Ø 50 cm, doré",
    "lustre-salon-blanc-246282": "Suspension soucoupe en soie tendue, Ø 30 à 60 cm, blanc",
    "lustre-salon-blanc-575463": "Suspension rose en pétales acryliques, Ø 33 à 43 cm",
    "lustre-salon-led-147017": "Lustre anneaux LED concentriques, Ø 40 à 80 cm",
    "lustre-salon-led-240560": "Lustre anneau LED à couronne effet cristal, noir, blanc ou doré",
    "lustre-salon-led-341706": "Suspension coupole galet LED, Ø 40 à 60 cm, cinq modèles",
    "lustre-salon-led-366435": "Suspension ruban LED double boucle, 70 à 92 cm, doré",
    "lustre-salon-led-630766": "Suspension anneau LED à verre facetté, doré, blanc ou noir",
    "lustre-salon-led-784326": "Plafonnier palets LED et bois, 4 à 7 lumières",
    "plafonnier-led-led-183789": "Plafonnier palets LED et bois, 5 ou 6 lumières, gris ou blanc",
    "plafonnier-led-led-465027": "Plafonnier boucles LED entrelacées, blanc ou noir",
    "plafonnier-led-led-698635": "Plafonnier anneaux LED, 1 à 6 anneaux, blanc, noir ou doré",
    "plafonnier-led-led-dore-blanc-354637": "Plafonnier coupole plissée en acrylique, Ø 30 à 55 cm",
    "suspension-moderne-led-noir-330664": "Suspension deux barres LED croisées, 100 à 150 cm, noir",
    "suspension-verre-446435": "Suspension globe en verre fumé sur tige rigide, Ø 20 cm",
    "suspension-verre-651675": "Suspension boule en verre fumé miroir, Ø 20 à 30 cm",
    "suspension-verre-814554": "Suspension disque plat en verre coloré, ampoule apparente",
    "suspension-verre-928640": "Suspension galet en verre fumé à micro-LED, monture laiton",
    "suspension-verre-led-blanc-554061": "Suspension globes opale sur câbles laiton, quatre modèles",
    "suspension-verre-led-dore-436718": "Suspension arceau laiton et globes opale, doré ou noir",
    "suspension-verre-noir-201424": "Suspension grappe de verres fumés miroir, rosace noire",
}

# Fiches dont la photo contredit le type de produit : on écrit ce que montre l’image.
FAMILY_OVERRIDES: dict[str, str] = {
    "suspension-bois-led-934110": "Suspensions pierre",
    "suspension-metal-led-dore-952116": "Suspensions déco",
    "suspension-metal-led-dore-975417": "Suspensions déco",
    "plafonnier-led-led-922186": "Suspensions verre",
    # audit photo du 25/08 : la famille du catalogue ne correspondait pas à l’image
    "lustre-anneau-led-007557": "Plafonniers",
    "plafonnier-led-led-442025": "Suspensions métal",
    "suspension-bois-193329": "Suspensions pierre",
    "suspension-bois-832012": "Suspensions verre",
    "suspension-bois-led-121862": "Suspensions déco",
    "suspension-bois-led-245113": "Suspensions pierre",
    "suspension-bois-led-334133": "Suspensions pierre",
    "suspension-bois-led-30cm-886635": "Suspensions déco",
    "suspension-metal-dore-037279": "Suspensions déco",
    "suspension-rotin-dore-865596": "Suspensions bois",
    # relecture des titres génériques : la photo montre un anneau LED ou un plafonnier
    "lustre-salon-led-147017": "Lustres anneau",
    "lustre-salon-led-240560": "Lustres anneau",
    "lustre-salon-led-630766": "Lustres anneau",
    "lustre-salon-led-784326": "Plafonniers",
}

# Textes partagés par les fiches en corde, chanvre ou paille : la famille « rotin »
# leur donnerait des affirmations fausses sur la fibre.
FIBRE_TEXTS: dict[str, list] = {
    "intros": [
        "La fibre est enroulée serré autour de l’abat-jour : la lumière ne traverse presque pas, elle ressort par le haut et par le bas. Cette <strong>suspension en fibre tressée</strong> pose une lumière basse, au-dessus d’une table ou d’un chevet.",
        "Cette <strong>suspension en fibre tressée</strong> a le grain d’un objet de vannerie et le poids d’un rien. Elle réchauffe une pièce claire sans y ajouter de couleur.",
        "Un abat-jour en fibre tressée, une lumière qui sort par les vides du tressage : cette <strong>suspension en fibre tressée</strong> convient à une chambre comme à une cuisine.",
    ],
    "angles": [
        [
            ("Ce que la fibre fait au faisceau", "La corde absorbe une partie de la lumière au lieu de la renvoyer. On obtient une lumière chaude, sans reflet dur, même avec une ampoule assez forte."),
            ("Choisir la bonne envergure", "{size} Au-dessus d’une table, prenez nettement plus étroit que le plateau ; dans une chambre, restez modeste."),
            ("Une matière qui se patine", "La teinte de la fibre bouge légèrement d’un exemplaire à l’autre, c’est le propre du tressage à la main. {care_lead}{care}. {aspect}"),
        ],
    ],
}

MATTER_OVERRIDES: dict[str, dict] = {
    "suspension-deco-led-889929": {
        "matter": "céramique",
        "usp": "Céramique",
        "matter_faq": "De la céramique, en cônes texturés façon cornet, écrus, miel ou bruns selon le cône, avec une petite source globe en pointe. La texture est prise dans la pièce, pas peinte dessus.",
        "care": "un chiffon doux sur la céramique",
    },
    "suspension-bois-led-453740": {
        "matter": "bois et lanternes en verre",
        "usp": "Bois et verre",
        "matter_faq": "Un corps en bois vieilli, six lanternes en verre suspendues par des chaînes en métal noir. Le bois porte ses nœuds et ses marques, c’est ce qui fait la pièce.",
        "care": "un chiffon sec sur le bois, un chiffon microfibre sur les verres",
    },
    "suspension-metal-led-dore-952116": {
        "matter": "céramique peinte et laiton",
        "usp": "Céramique peinte",
        "matter_faq": "Un abat-jour en céramique peinte de motifs bleus, monté sur une douille et une rosace en laiton, avec un câble textile torsadé. Le motif est appliqué avant cuisson.",
        "care": "un chiffon doux sur la céramique, sans abrasif",
    },
    "suspension-metal-led-dore-975417": {
        "matter": "céramique plissée et laiton",
        "usp": "Céramique plissée",
        "matter_faq": "De la céramique blanche plissée en corolle, sur une douille en laiton et un cordon doré. L’ampoule reste visible sous l’abat-jour.",
        "care": "un chiffon doux sur l’émail",
    },
    "plafonnier-led-led-922186": {
        "base": "Suspension guirlande de globes",
        "matter": "globes opalins en acrylique et métal doré",
        "usp": "Globes opalins",
        "matter_faq": "Des globes opalins en acrylique enfilés sur un câble doré, comme un collier tendu au plafond. L’acrylique diffuse comme un verre dépoli et ne casse pas à la pose.",
        "care": "un chiffon microfibre globe par globe, sans solvant",
        "intros": [
            "Une guirlande de globes tendue d’un point à l’autre du plafond, et la lumière qui court avec elle : cette suspension s’installe au-dessus d’un lit, d’une table ou le long d’un couloir.",
        ],
        "angles": [
            [
                ("Une ligne de lumière, pas un point", "Chaque globe éclaire pour lui : la lumière arrive par petites nappes réparties au lieu de tomber d’un seul endroit. C’est ce qui rend la pièce homogène."),
                ("Le nombre de globes fait la longueur", "{size} Comptez la portée à installer avant de choisir : c’est le nombre de globes qui décide de la longueur tendue, pas un diamètre."),
                ("Léger à poser", "L’acrylique pèse une fraction du verre, ce qui rend la guirlande plus facile à tendre. {care_lead}{care}. {aspect}"),
            ],
        ],
    },
    "plafonnier-led-led-637673": {
        "matter": "diffuseur LED avec enceinte intégrée",
        "usp": "Enceinte intégrée",
        "matter_faq": "Un plafonnier rond à diffuseur LED, avec une enceinte au centre et une lumière qui change de couleur. La partie éclairage fonctionne indépendamment du son.",
        "care": "un chiffon sec sur le diffuseur",
    },
    # ── Corrections issues de l’audit photo du 25/08 ────────────────────────────
    "lustre-anneau-led-007557": {
        "base": "Plafonnier LED connecté",
        "matter": "diffuseur LED pilotable",
        "usp": "Lumière RVB",
        "matter_faq": "Un diffuseur rond sur platine laquée, avec une LED couleur pilotable depuis une application ou par la commande murale. Le blanc chaud reste disponible pour l’usage courant.",
        "care": "un chiffon sec sur le diffuseur",
    },
    "plafonnier-led-led-442025": {
        "base": "Suspension boule d’épines",
        "matter": "tiges d’aluminium doré",
        "usp": "Boule d’épines",
        "matter_faq": "Des dizaines de tiges d’aluminium anodisé doré plantées sur une sphère centrale. La lumière part des sources logées au cœur de la boule et se répartit le long des tiges.",
        "care": "un plumeau ou un chiffon sec entre les tiges",
        "intros": [
            "Une sphère hérissée de tiges dorées, une lumière qui sort du cœur et court le long du métal : cette suspension se choisit comme un objet, au-dessus d’une table ou dans une entrée à double hauteur.",
        ],
        "angles": [
            [
                ("Une lumière éclatée", "Les tiges renvoient chacune un petit reflet. Au lieu d’un rond de lumière net, on obtient une source scintillante qui accroche l’œil de loin."),
                ("Prévoir le volume autour", "{size} Une boule d’épines a besoin de vide pour se lire : gardez de la marge sur les côtés, sinon la pièce paraît encombrée."),
                ("Le doré se garde mat", "L’anodisation ne marque pas comme une laque. {care_lead}{care}. {aspect}"),
            ],
        ],
    },
    "suspension-metal-dore-502141": {
        "matter": "abat-jour en tissu sur armature laiton",
        "usp": "Abat-jour tissu",
        "matter_faq": "Un abat-jour en tissu tendu, monté à l’intérieur d’une armature en laiton apparente. La lumière traverse le tissu par les côtés et sort franchement par le bas.",
        "care": "un plumeau ou une brosse douce sur le tissu",
        "intros": [
            "Le tissu tendu adoucit tout ce qui le traverse : cette suspension éclaire une table sans le rond de lumière dur d’un abat-jour métal. L’armature en laiton reste visible autour.",
        ],
        "angles": [
            [
                ("Le tissu diffuse, l’armature dessine", "Une partie de la lumière passe à travers le tissu et éclaire la pièce, le reste tombe sur la table. C’est un éclairage plus enveloppant qu’un abat-jour opaque."),
                ("Choisir le diamètre", "{size} Au-dessus d’une table, un abat-jour large adoucit encore le faisceau ; un petit concentre davantage."),
                ("Un textile, donc de la poussière", "Le tissu prend la poussière plus vite qu’un métal. {care_lead}{care}. {aspect}"),
            ],
        ],
    },
    "suspension-metal-led-dore-701414": {
        "base": "Suspension voile LED",
        "matter": "voile de papier ou de soie sur tige métal",
        "usp": "Voile lumineux",
        "matter_faq": "Un voile tendu, en papier technique ou en soie selon la variante, monté sur une tige en métal. La lumière est renvoyée par la face intérieure du voile plutôt que projetée vers le bas.",
        "care": "un chiffon sec, très légèrement, le voile ne se lave pas",
        "intros": [
            "Un voile tendu en biais, une lumière qui rebondit dessus au lieu de tomber droit : cette suspension éclaire par réflexion, ce qui donne une lumière très douce au-dessus d’une table.",
        ],
        "angles": [
            [
                ("Une lumière réfléchie, pas projetée", "La source est cachée derrière le voile et vient frapper sa face intérieure. Il n’y a pas de point lumineux visible, donc pas d’éblouissement quand on est assis dessous."),
                ("L’envergure compte plus que la hauteur", "{size} Ce type de voile se lit de loin : donnez-lui de la longueur de table plutôt que de la hauteur."),
                ("Un matériau à ménager", "Le voile est tendu, il ne se frotte pas. {care_lead}{care}. {aspect}"),
            ],
        ],
    },
    "suspension-metal-noir-dore-361680": {
        "base": "Lustre laiton à bougies",
        "matter": "laiton",
        "usp": "Laiton",
        "matter_faq": "Du laiton, sur des bras courbés terminés par des fausses bougies. Il n’y a pas d’abat-jour : les ampoules restent nues, ce qui suppose de les choisir décoratives.",
        "care": "un chiffon doux sur le laiton",
        "intros": [
            "Des bras de laiton courbés, des bougies au bout, rien pour cacher la source : ce lustre éclaire une salle à manger comme un candélabre le ferait, par petits points chauds plutôt que par nappe.",
        ],
        "angles": [
            [
                ("Des points de lumière, pas une nappe", "Chaque bougie est un point chaud. L’ensemble éclaire moins fort qu’un plafonnier mais donne une lumière de repas immédiatement plus douce."),
                ("Compter l’envergure des bras", "{size} Les bras s’étalent largement : mesurez le débattement autour du point de fixation avant de percer."),
                ("Choisir les ampoules avec soin", "Comme rien ne les cache, les ampoules font partie du dessin : des flammes ou des filaments valent mieux qu’une LED banche. {care_lead}{care}. {aspect}"),
            ],
        ],
    },
    "suspension-rotin-272937": {
        "base": "Suspension corde de chanvre tressée",
        "matter": "corde de chanvre tressée",
        "usp": "Corde de chanvre",
        "matter_faq": "De la corde de chanvre tressée à la main sur une armature métal noire. La teinte de la corde bouge un peu d’un abat-jour à l’autre, c’est le propre de la fibre.",
        "care": "un chiffon sec, jamais d’eau sur la corde",
        "intros": FIBRE_TEXTS["intros"],
        "angles": FIBRE_TEXTS["angles"],
    },
    "suspension-rotin-443915": {
        "base": "Suspension corde tressée",
        "matter": "corde tressée",
        "usp": "Corde tressée",
        "matter_faq": "De la corde enroulée serré sur une forme en cloche. La lumière ne traverse quasiment pas la fibre : elle ressort par le haut et par le bas de l’abat-jour.",
        "care": "un chiffon sec, la corde ne se lave pas",
        "intros": FIBRE_TEXTS["intros"],
        "angles": FIBRE_TEXTS["angles"],
    },
    "suspension-rotin-477244": {
        "base": "Suspension corolle en corde tressée",
        "matter": "corde tressée",
        "usp": "Corde tressée",
        "matter_faq": "De la corde tressée montée en pétales sur une armature. Les bords ondulent, aucun exemplaire ne retombe exactement comme l’autre.",
        "care": "un chiffon sec, la corde ne se lave pas",
        "intros": FIBRE_TEXTS["intros"],
        "angles": FIBRE_TEXTS["angles"],
    },
    "suspension-rotin-led-761433": {
        "base": "Suspension corolle en fibre tressée",
        "matter": "fibre naturelle tressée",
        "usp": "Fibre tressée",
        "matter_faq": "De la fibre naturelle tressée, montée en pétales autour d’un diffuseur central. La maille est fine : la lumière passe surtout par le centre et par les bords.",
        "care": "un chiffon sec, sans eau sur la fibre",
        "intros": FIBRE_TEXTS["intros"],
        "angles": FIBRE_TEXTS["angles"],
    },
    "suspension-rotin-489600": {
        "base": "Suspension paille brute",
        "matter": "paille brute",
        "usp": "Paille brute",
        "matter_faq": "De la paille laissée brute, en touffe, sans finition lisse. Les brins dépassent volontairement : c’est ce qui donne l’ombre irrégulière au plafond.",
        "care": "un plumeau, rien d’humide",
        "intros": FIBRE_TEXTS["intros"],
        "angles": FIBRE_TEXTS["angles"],
    },
    "suspension-rotin-dore-865596": {
        "base": "Suspension bois deux pétales",
        "matter": "bois cintré et monture dorée",
        "usp": "Bois cintré",
        "matter_faq": "Deux pétales de bois cintré posés en aile, sur une monture et une rosace dorées. Le veinage court dans le sens du cintrage, il n’est pas deux fois le même.",
        "care": "un chiffon sec sur le bois, sans cire",
        "intros": [
            "Deux pétales de bois cintré ouverts en aile, l’ampoule au milieu : cette suspension travaille l’horizontale, au-dessus d’une table longue ou d’un îlot.",
        ],
        "angles": [
            [
                ("Une lumière rasante", "Les pétales renvoient la lumière vers le bas et vers les côtés. On obtient une nappe large et basse plutôt qu’un rond franc sous le luminaire."),
                ("Mesurer l’envergure, pas le diamètre", "{size} Cette forme s’étale plus qu’elle ne descend : c’est la longueur de table qui commande, pas la hauteur sous plafond."),
                ("Le veinage fait l’objet", "Chaque pétale a son dessin. {care_lead}{care}. {aspect}"),
            ],
        ],
    },
    "suspension-bois-193329": {
        "matter": "travertin et bois",
        "usp": "Travertin et bois",
        "matter_faq": "Un cylindre en travertin coiffé d’un capot en bois, clair ou noyer selon la variante. Les creux du travertin sont ceux de la pierre, ils diffèrent d’une pièce à l’autre.",
        "care": "un chiffon doux sur la pierre, un chiffon sec sur le bois",
    },
    "suspension-bois-led-245113": {
        "matter": "travertin et bois foncé",
        "usp": "Travertin et bois",
        "matter_faq": "Un cylindre en travertin ceinturé d’une bande de bois foncé. La pierre porte ses creux et ses veines, le bois son veinage : les deux varient d’un exemplaire à l’autre.",
        "care": "un chiffon doux sur la pierre, un chiffon sec sur le bois",
    },
    "suspension-bois-led-334133": {
        "matter": "perles de pierre et bois",
        "usp": "Pierre et bois",
        "matter_faq": "Deux perles de pierre claire enfilées sous une bille de bois, avec un globe opalin en pointe. Le veinage de la pierre change d’une perle à l’autre.",
        "care": "un chiffon doux sur la pierre, un chiffon microfibre sur le globe",
    },
    "suspension-effet-pierre-092465": {
        "base": "Suspension pierre translucide",
        "matter": "pierre claire translucide et tige brune",
        "usp": "Pierre translucide",
        "matter_faq": "Un cylindre de pierre claire assez fine pour que la lumière la traverse, monté sous une tige brune. Allumée, la pierre devient laiteuse et laisse voir ses nuances.",
        "care": "un chiffon doux, rien d’abrasif",
        "intros": [
            "La pierre est taillée assez fine pour que la lumière passe au travers : allumée, elle devient laiteuse et ses nuances se lisent. Cette suspension éclaire de près, au-dessus d’un chevet ou d’une console.",
        ],
        "angles": [
            [
                ("La lumière passe dans la pierre", "Ce n’est pas un abat-jour qu’on éclaire de l’intérieur, c’est la matière elle-même qui s’allume. Le rendu change selon l’épaisseur, veine par veine."),
                ("Un petit volume, à voir de près", "{size} Ce format se joue en lumière d’appoint : posez-le là où on passe à côté, pas au centre d’un grand séjour."),
                ("Chaque pièce est différente", "Les nuances de la pierre ne se répètent pas d’un exemplaire à l’autre. {care_lead}{care}. {aspect}"),
            ],
        ],
    },
    "suspension-bois-led-121862": {
        "matter": "céramique émaillée et bois",
        "usp": "Céramique et bois",
        "matter_faq": "Un abat-jour en céramique émaillée blanche à bord festonné, avec un liseré peint et une tête en bois. L’émail est appliqué à la main, le liseré n’est jamais parfaitement régulier.",
        "care": "un chiffon doux sur l’émail",
    },
    "suspension-bois-led-30cm-886635": {
        "matter": "céramique plissée et bois",
        "usp": "Céramique plissée",
        "matter_faq": "De la céramique blanche plissée en parasol, sur une poignée tournée en bois clair et une douille en laiton. L’ampoule reste visible sous l’abat-jour.",
        "care": "un chiffon doux sur l’émail",
    },
    "suspension-metal-dore-037279": {
        "matter": "céramique gaufrée et laiton",
        "usp": "Céramique gaufrée",
        "matter_faq": "Un dôme en céramique blanche au motif gaufré dans la masse, sur une monture en laiton avec une perle de céramique sur le câble. Le relief se lit surtout quand la lumière rase la surface.",
        "care": "un chiffon doux sur l’émail",
    },
    "suspension-bois-832012": {
        "matter": "verre soufflé et bois",
        "usp": "Verre et bois",
        "matter_faq": "Trois gouttes en verre soufflé, teinté gris fumé, ambre ou laissé clair, coiffées chacune d’une tête en bois. Le soufflage laisse des irrégularités dans l’épaisseur, visibles quand c’est allumé.",
        "care": "un chiffon microfibre sur le verre, un chiffon sec sur le bois",
    },
    "suspension-verre-091815": {
        "base": "Suspension nuages en verre soufflé",
        "matter": "verre soufflé",
        "usp": "Verre soufflé",
        "matter_faq": "Du verre soufflé, plissé en forme de nuage. Chaque pièce est soufflée séparément : deux nuages ne se replient jamais exactement pareil.",
        "care": "un chiffon microfibre sur chaque nuage",
    },
    "suspension-verre-led-489156": {
        "base": "Suspension nuages en verre soufflé",
        "matter": "verre soufflé",
        "usp": "Verre soufflé",
        "matter_faq": "Du verre soufflé, plissé en forme de nuage. Chaque pièce est soufflée séparément : deux nuages ne se replient jamais exactement pareil.",
        "care": "un chiffon microfibre sur chaque nuage",
    },
    "suspension-bois-059364": {
        "base": "Suspension tonneau en bois",
        "matter": "bois cerclé de métal",
        "usp": "Bois cerclé",
        "matter_faq": "Un fût en douves de bois, cerclé de feuillards métalliques, suspendu à une chaîne. Le bois est traité pour rester foncé, chaque douve garde son veinage.",
        "care": "un chiffon sec, sans cire ni détergent",
    },
    "lustre-salon-233314": {
        "matter": "globes effet lune et métal",
        "usp": "Globes effet lune",
        "matter_faq": "Des globes au relief imprimé façon surface lunaire, montés en grappe sur une platine métal. Allumés, les creux du relief se dessinent en ombres légères.",
        "care": "un chiffon microfibre globe par globe",
    },
    "lustre-salon-907106": {
        "matter": "globes en verre coloré et métal",
        "usp": "Verre coloré",
        "matter_faq": "Des globes en verre coloré, ambre, rose, fumé, vert d’eau, martelés en surface. Chaque globe est teinté dans la masse, la couleur ne s’efface pas.",
        "care": "un chiffon microfibre globe par globe",
    },
    "lustre-salon-led-254609": {
        "base": "Lustre sputnik",
        "matter": "métal et laiton",
        "usp": "Sputnik",
        "matter_faq": "Des bras métalliques rayonnants et des douilles en laiton, sans abat-jour. Les ampoules restent nues : elles font partie du dessin du luminaire.",
        "care": "un chiffon doux sur le métal",
    },
    "lustre-statement-led-noir-950316": {
        "base": "Lustre sputnik",
        "matter": "métal noir et laiton",
        "usp": "Sputnik",
        "matter_faq": "Un axe et des bras en métal noir, des douilles en laiton, aucun abat-jour. Ce sont les ampoules choisies qui donnent le caractère de la pièce.",
        "care": "un chiffon doux sur le métal",
    },
    "plafonnier-led-565566": {
        "base": "Plafonnier tiges croisées",
        "matter": "métal chromé",
        "usp": "Tiges croisées",
        "matter_faq": "Des tiges métalliques croisées sur une platine, finition cuivre ou chrome selon la variante, avec des douilles nues au bout de chaque branche.",
        "care": "un chiffon doux sur le métal",
    },
    "plafonnier-led-992600": {
        "base": "Plafonnier tiges courbes",
        "matter": "métal laqué",
        "usp": "Tiges courbes",
        "matter_faq": "Des tiges courbées en spirale sur une platine laquée, noir, blanc ou doré selon la variante, avec des douilles nues au bout de chaque branche.",
        "care": "un chiffon doux sur la laque",
    },
    "plafonnier-led-led-728204": {
        "base": "Réglette LED",
        "matter": "profilé aluminium et diffuseur",
        "usp": "Réglette LED",
        "matter_faq": "Un profilé en aluminium fermé par un diffuseur continu, finition blanche ou noyer. La LED court sur toute la longueur, il n’y a pas de point chaud visible.",
        "care": "un chiffon sec sur le diffuseur",
    },
    # ── Fiches dont le titre générique cachait la matière réelle (audit du 25/08) ──
    "lustre-salon-957153": {
        "base": "Suspension ruban LED",
        "matter": "profilé aluminium doré",
        "usp": "Ruban LED",
        "matter_faq": "Un profilé d’aluminium plié en trèfle, finition dorée, avec la LED logée derrière un diffuseur sur toute la boucle. Aucune ampoule à visser.",
        "care": "un chiffon sec sur le profilé",
    },
    "lustre-salon-led-366435": {
        "base": "Suspension ruban LED",
        "matter": "profilé aluminium doré",
        "usp": "Ruban LED",
        "matter_faq": "Un profilé d’aluminium doré replié en deux boucles, la LED derrière un diffuseur continu. C’est une pièce large, pensée pour une table en longueur.",
        "care": "un chiffon sec sur le profilé",
    },
    "lustre-salon-blanc-246282": {
        "base": "Suspension soucoupe",
        "matter": "soie tendue sur armature",
        "usp": "Soie tendue",
        "matter_faq": "De la soie tendue sur une armature légère, nervure après nervure, comme un cocon aplati. La lumière traverse la soie et sort adoucie de toute la surface.",
        "care": "un plumeau ou un chiffon sec, jamais d’eau sur la soie",
    },
    "lustre-salon-blanc-575463": {
        "base": "Suspension rose",
        "matter": "pétales en acrylique",
        "usp": "Pétales acryliques",
        "matter_faq": "Des pétales en acrylique blanc emboîtés en corolle. L’acrylique diffuse comme un verre dépoli, en beaucoup plus léger, et ne casse pas à la pose.",
        "care": "un chiffon microfibre, pétale après pétale, sans solvant",
    },
    "lustre-salon-led-240560": {
        "base": "Lustre anneau LED",
        "matter": "profilé laqué et verre facetté",
        "usp": "Effet cristal",
        "matter_faq": "Un anneau en profilé laqué garni de verre facetté sur son pourtour intérieur, avec la LED derrière. Ce n’est pas du cristal taillé, c’est du verre moulé à facettes.",
        "care": "un chiffon microfibre sur les facettes, sans produit",
    },
    "lustre-salon-led-630766": {
        "base": "Suspension anneau LED",
        "matter": "profilé laqué et verre facetté",
        "usp": "Verre facetté",
        "matter_faq": "Un anneau laqué dont la tranche intérieure est garnie de verre à facettes, éclairé de l’intérieur. Le rendu scintille sans le poids ni le prix du cristal taillé.",
        "care": "un chiffon microfibre sur les facettes, sans produit",
    },
    "lustre-salon-led-341706": {
        "base": "Suspension coupole galet",
        "matter": "métal laqué blanc",
        "usp": "Coupole galet",
        "matter_faq": "Une coupole en métal laqué blanc, découpée en galet, dont la LED éclaire à la fois vers le plafond et vers le bas par la fente centrale.",
        "care": "un chiffon doux sur la laque",
    },
    "lustre-salon-led-784326": {
        "base": "Plafonnier palets LED",
        "matter": "palets laqués et bois clair",
        "usp": "Palets et bois",
        "matter_faq": "Des palets LED laqués posés au bout de bras métalliques, ponctués de disques en bois clair. Chaque palet a son diffuseur, il n’y a pas d’ampoule à ajouter.",
        "care": "un chiffon sec sur les diffuseurs et sur le bois",
    },
    "plafonnier-led-led-183789": {
        "base": "Plafonnier palets LED",
        "matter": "palets laqués et bois clair",
        "usp": "Palets et bois",
        "matter_faq": "Des palets LED gris ou blancs répartis en étoile sur une platine noire, avec des disques de bois clair entre les bras. Source intégrée, rien à visser.",
        "care": "un chiffon sec sur les diffuseurs et sur le bois",
    },
    "plafonnier-led-led-465027": {
        "base": "Plafonnier boucles LED",
        "matter": "boucles laquées à diffuseur",
        "usp": "Boucles LED",
        "matter_faq": "Des boucles de profilé laqué entrelacées à plat contre le plafond, la LED derrière un diffuseur sur toute la longueur de chaque boucle.",
        "care": "un chiffon sec sur les diffuseurs",
    },
    "plafonnier-led-led-698635": {
        "base": "Plafonnier anneaux LED",
        "matter": "anneaux en profilé doré",
        "usp": "Anneaux LED",
        "matter_faq": "Des anneaux en profilé métallique imbriqués, chacun éclairé sur sa face intérieure. Le nombre d’anneaux se choisit à la commande.",
        "care": "un chiffon sec sur les profilés",
    },
    "plafonnier-led-led-dore-blanc-354637": {
        "base": "Plafonnier coupole plissée",
        "matter": "acrylique plissé",
        "usp": "Coupole plissée",
        "matter_faq": "Une coupole en acrylique plissé, nervurée du centre vers le bord, plaquée au plafond. L’acrylique diffuse la LED sans laisser voir de point chaud.",
        "care": "un chiffon microfibre dans le sens des plis",
    },
    "suspension-moderne-led-noir-330664": {
        "base": "Suspension barres LED",
        "matter": "profilés noirs croisés",
        "usp": "Barres croisées",
        "matter_faq": "Deux profilés noirs suspendus en croix décalée, chacun éclairé sur toute sa longueur par une LED derrière diffuseur. Aucune ampoule visible.",
        "care": "un chiffon sec le long des profilés",
    },
    "suspension-verre-928640": {
        "base": "Suspension galet en verre",
        "matter": "verre fumé et micro-LED sur fils cuivre",
        "usp": "Micro-LED",
        "matter_faq": "Un galet de verre fumé aplati, monté sur une tige laiton, dans lequel courent des fils de cuivre semés de micro-LED. Allumé, on lit chaque point à travers le verre.",
        "care": "un chiffon microfibre sur le verre, sans produit",
        "intros": [
            "Un galet de verre fumé posé au bout d’une tige laiton, et dedans une constellation de points lumineux : cette suspension se regarde autant qu’elle éclaire. Au-dessus d’une table basse ou d’un lit, elle fait office de veilleuse décorative.",
        ],
        "angles": [
            [
                ("Une lumière en semis, pas en nappe", "Les micro-LED sont réparties sur des fils de cuivre : allumée, la pièce reçoit une multitude de petits points au lieu d’un faisceau. C’est une lumière d’ambiance, pas une lumière de travail."),
                ("Prévoir un fond calme derrière", "{size} Le verre fumé se lit mieux devant un mur uni. Devant une fenêtre, les points se noient dans le contre-jour."),
                ("Le verre garde les traces", "La finition fumée marque les doigts plus qu’un verre clair. {care_lead}{care}. {aspect}"),
            ],
        ],
    },
    "suspension-verre-led-blanc-554061": {
        "base": "Suspension globes opale",
        "matter": "verre opale et laiton",
        "usp": "Globes opale",
        "matter_faq": "Des globes en verre opale suspendus à des câbles laiton, à des hauteurs décalées. Le verre opale rend la source diffuse au lieu de la laisser ponctuelle.",
        "care": "un chiffon microfibre sur les globes",
    },
    "suspension-verre-led-dore-436718": {
        "base": "Suspension arceau",
        "matter": "arceau métal et globes en verre opale",
        "usp": "Arceau et globes",
        "matter_faq": "Un arceau métallique en U, doré ou noir, avec un petit globe en verre opale à chaque extrémité. Le dessin tient en deux traits, c’est tout l’intérêt.",
        "care": "un chiffon doux sur l’arceau, microfibre sur les globes",
        "intros": [
            "Un trait de métal replié en U, un globe opale à chaque bout, rien de plus : cette suspension joue la ligne plutôt que le volume. Elle tient bien à côté d’un lit ou dans un couloir étroit.",
        ],
        "angles": [
            [
                ("Deux points de lumière décalés", "Les globes ne sont pas à la même hauteur : la lumière arrive sur deux plans, ce qui évite l’effet de spot unique. Le verre opale adoucit chaque source."),
                ("Un encombrement de rien", "{size} Cette pièce se choisit pour un endroit contraint, là où un abat-jour large ne passerait pas."),
                ("Le métal reste net", "Peu de surface, donc peu de poussière à reprendre. {care_lead}{care}. {aspect}"),
            ],
        ],
    },
    "suspension-verre-noir-201424": {
        "base": "Suspension grappe de verres",
        "matter": "verre fumé électroplaqué",
        "usp": "Verre miroir",
        "matter_faq": "Des verres soufflés de formes différentes, traités par électroplacage pour un rendu fumé miroir. Chacun garde ses petites irrégularités de soufflage.",
        "care": "un chiffon microfibre, la finition miroir garde les traces de doigts",
    },
    "suspension-verre-814554": {
        "base": "Suspension disque plat",
        "matter": "verre coloré et douille laquée",
        "usp": "Disque coloré",
        "matter_faq": "Un disque plat en verre coloré, monté sous une douille laquée assortie. L’ampoule reste apparente sous le disque, elle fait partie du dessin.",
        "care": "un chiffon microfibre sur le verre",
    },
}

# Valeurs d’option renommées (aucun SKU touché, productOptionUpdate seulement).
OPTION_VALUE_RENAMES: dict[str, list[tuple[str, str, str]]] = {
    "suspension-effet-pierre-092465": [("Couleur", "Blanc chaud", "Pierre claire")],
}

# Source lumineuse corrigée : le handle contient « led » mais la fiche fournisseur
# annonce une douille, ou la photo montre une ampoule à visser.
SOURCE_OVERRIDES: dict[str, str] = {
    "lustre-salon-led-254609": "e27",
    "lustre-statement-led-noir-950316": "e27",
    "plafonnier-led-565566": "e27",
    "plafonnier-led-992600": "e27",
    "suspension-bois-led-30cm-886635": "e27",
    "suspension-bois-led-830581": "e27",
    "suspension-bois-led-934110": "g9",
    "suspension-effet-pierre-led-147607": "e27",
    "suspension-effet-pierre-led-dore-960013": "e27",
    "suspension-metal-led-dore-975417": "e27",
    "suspension-metal-noir-dore-361680": "e14",
    # `detect_source` retombait sur « mixte » alors qu’aucun axe ne laisse ce choix :
    # la photo montre une douille à visser, ou au contraire une source close.
    "lustre-salon-blanc-575463": "e27",
    "suspension-bambou-104055": "e27",
    "suspension-bois-059364": "e27",
    "suspension-bois-193329": "e27",
    "suspension-deco-253182": "e27",
    "suspension-deco-348096": "e27",
    "suspension-deco-blanc-560098": "e27",
    "suspension-effet-pierre-092465": "e27",
    "suspension-metal-dore-037279": "e27",
    "suspension-rotin-272937": "e27",
    "suspension-rotin-897170": "e27",
    "suspension-rotin-dore-865596": "e27",
    "suspension-verre-446435": "e27",
    "suspension-verre-651675": "e27",
    "suspension-verre-091815": "g9",
    # axe « Température » seul : la source est fournie, elle ne se remplace pas
    "suspension-effet-pierre-343987": "led",
    "suspension-verre-928640": "led",
    # axe « Température » seul, mais l’ampoule à visser est visible sur la photo
    "lustre-salon-907106": "e27",
    "suspension-bambou-942503": "e27",
    "suspension-metal-dore-502141": "e27",
    "suspension-rotin-443915": "e27",
    "suspension-rotin-469688": "e27",
    "suspension-rotin-489600": "e27",
    "suspension-rotin-605780": "e27",
    "suspension-verre-814554": "e27",
    "suspension-verre-noir-201424": "e27",
    # axe « Ampoule » à valeur unique « ampoule non fournie » : pas de choix, c’est une douille
    "suspension-bambou-280004": "e27",
    "suspension-bambou-led-630923": "e27",
    "suspension-bambou-led-50cm-377816": "e27",
    "suspension-rotin-607504": "e27",
}

# Fiches dont l’axe de taille est une longueur, pas un diamètre.
LENGTH_HANDLES = {
    "plafonnier-led-led-728204",
    "lustre-salon-led-366435",
    "suspension-moderne-led-noir-330664",
}

# ── Briques rotatives ───────────────────────────────────────────────────────────
SOURCE_SENTENCES = {
    "led": [
        "La LED est intégrée : vous branchez, ça éclaire, il n’y a pas d’ampoule à acheter.",
        "Pas d’ampoule à prévoir, la source est déjà dans le luminaire.",
        "La LED est logée dans la pièce : rien à visser au moment de la pose.",
    ],
    "e27": [
        "Douille E27, ampoule non fournie : une LED blanc chaud fait le travail.",
        "Il vous faudra une ampoule E27. Comptez une LED entre 2700 et 3000 K pour une lumière douce.",
        "L’ampoule n’est pas dans le colis. La douille est une E27, la plus courante.",
    ],
    "mixte": [
        "Regardez la variante avant de valider : certaines ont la LED intégrée, d’autres une douille E27 à équiper.",
        "Selon la variante, la LED est intégrée ou la douille E27 reste à garnir.",
        "Deux cas de figure selon la variante : source intégrée, ou ampoule E27 à ajouter.",
    ],
    "e14": [
        "Douille E14, ampoule non fournie : ce sont les petites flammes ou les filaments qui vont bien ici.",
        "Il vous faudra des ampoules E14, le petit culot à vis. Elles ne sont pas dans le colis.",
        "Ampoules E14 à prévoir, non fournies. Comme elles restent visibles, choisissez-les décoratives.",
    ],
    "g9": [
        "L’ampoule est une G9, remplaçable, et elle n’est pas fournie : comptez une LED G9 blanc chaud.",
        "Douille G9, ampoule non fournie. C’est un culot à broches, courant en petites LED.",
        "Prévoyez une ampoule G9. Elle se change sans démonter le luminaire.",
    ],
}

SIZE_SENTENCES = [
    "Diamètres proposés : {list}.",
    "Vous choisissez entre {list}.",
    "Cette fiche va de {mini} cm à {maxi} cm ({list}).",
]

CARE_LEAD = ["Entretien : ", "Côté entretien, ", "Pour la garder nette, "]


def dash_free(text: str) -> str:
    """Aucun tiret cadratin ni demi-cadratin ne doit sortir vers le client."""
    text = re.sub(r"(\d)\s*[–—]\s*(\d)", r"\1 à \2", text)
    text = re.sub(r"\s*[–—]\s*", ", ", text)
    return re.sub(r"\s{2,}", " ", text).strip()


# Libellés de variante repris tels quels de l’import : illisibles côté client.
VALUE_DISPLAY: dict[str, str] = {
    "Plum Vert Celadon": "Vert céladon",
    "Powder Bleu Celadon": "Bleu céladon poudré",
    "Papier DuPont": "Papier",
    "Soie unie": "Soie",
}

CODE_VALUE = re.compile(r"^(?:Modèle |Forme )?[A-Z]\d?$")


def display_values(name: str, values: list[str]) -> list[str]:
    """Nettoie les valeurs d’option pour l’affichage seul : Shopify n’est pas touché.

    Retire les suffixes de dédoublonnage (« Blanc chaud · 2 », « Vert 1 »), les échos
    entre parenthèses, traduit les libellés fournisseur et remet les codes dans l’ordre.
    """
    stripped = [re.sub(r"\s*\(.+\)$", "", v) for v in values]
    if name in {"Modèle", "Forme"}:
        # « Modèle : Modèle A, Modèle B » se lit « Modèle : A, B »
        stripped = [re.sub(rf"^{name} (?=\S)", "", v) for v in stripped]
    known = set(stripped)
    cleaned: list[str] = []
    for value in stripped:
        base = re.sub(r"(?:\s*·\s*\d+|\s+\d+)$", "", value)
        # on ne coupe le suffixe que s’il ne servait qu’à dédoublonner un libellé existant
        keep = base if base != value and base in known else value
        keep = VALUE_DISPLAY.get(keep, keep)
        if keep and keep not in cleaned:
            cleaned.append(keep)
    if name in {"Modèle", "Forme"} and all(CODE_VALUE.match(v) for v in cleaned):
        cleaned.sort()
    return cleaned


def renamed_values(handle: str, name: str, values: list[str]) -> list[str]:
    """Aligne la copy sur les valeurs d’option renommées côté Shopify."""
    renames = {(axis, old): new for axis, old, new in OPTION_VALUE_RENAMES.get(handle, [])}
    return [renames.get((name, v), v) for v in values]


def tidy_lights(title: str) -> str:
    """« 4 lumières, 6 lumières et 8 lumières » se lit « 4, 6 ou 8 lumières »."""

    def repl(match: re.Match) -> str:
        counts = re.findall(r"(\d+)\s+lumières?", match.group(0))
        return f"{', '.join(counts[:-1])} ou {counts[-1]} lumières"

    title = re.sub(r"\d+\s+lumières?(?:(?:,|\set)\s+\d+\s+lumières?)+", repl, title)
    return re.sub(r"\b1 lumières\b", "1 lumière", title)


def diam_phrase(cms: list[int]) -> str:
    if not cms:
        return ""
    if len(cms) == 1:
        return f"Ø {cms[0]} cm"
    return f"Ø {cms[0]} à {cms[-1]} cm"


def size_sentence(cms: list[int], rot: int) -> str:
    if not cms:
        return "Les dimensions sont portées sur chaque variante."
    listing = et_join([f"{c} cm" for c in cms])
    if len(cms) == 1:
        return f"Un seul diamètre ici, {diam_phrase(cms)}."
    tpl = SIZE_SENTENCES[rot % len(SIZE_SENTENCES)]
    return tpl.format(list=listing, mini=cms[0], maxi=cms[-1])


def aspect_sentence(axis: str | None, values: list[str], rot: int) -> str:
    if not axis or not values or all(is_blind_code(v) for v in values):
        return ""
    low = ou_join([v.lower() for v in values[:4]])
    if axis == "Câble":
        variants = [
            f"Le choix {low} porte sur le câble et sa rosace ; l’abat-jour ne change pas de matière.",
            f"Câble et rosace se prennent en {low}. C’est bien le fil qui change de couleur, pas l’abat-jour.",
            f"Vous réglez la couleur du câble et de la rosace : {low}. L’abat-jour reste celui des photos.",
        ]
        return variants[rot % len(variants)]
    if axis == "Verre":
        return f"Le verre existe en {low}."
    if axis == "Abat-jour":
        return f"L’abat-jour se prend en {low}."
    if axis == "Émail":
        return f"Émail proposé en {ou_join(values[:4])}."
    return f"Finitions au choix : {low}."


# ── Familles ────────────────────────────────────────────────────────────────────
# Chaque famille : 3 intros et 3 jeux de 3 bénéfices. Tokens : {size}, {care}, {aspect}.
FAMILIES: dict[str, dict] = {
    "Suspensions bambou": {
        "kind": "suspension",
        "base": "Suspension bambou tressée",
        "kw": "suspension en bambou tressé",
        "matter": "bambou tressé",
        "usp": "Bambou tressé",
        "care": "un chiffon sec suffit, les fibres n’aiment pas l’eau",
        "matter_faq": "Du bambou tressé, celui des photos. La teinte des lattes bouge légèrement d’une pièce à l’autre, c’est le propre de la fibre.",
        "intros": [
            "Cette <strong>suspension en bambou tressé</strong> fait ce qu’on attend d’une vannerie au plafond : elle adoucit la lumière et pose un volume chaud dans la pièce. Au-dessus d’une table ou dans une entrée, elle tient les deux rôles.",
            "Le bambou tressé n’est pas ici un décor rapporté : c’est l’abat-jour lui-même. Allumée, cette <strong>suspension en bambou tressé</strong> renvoie le dessin du tressage sur le plafond et sur les murs proches.",
            "On accroche cette <strong>suspension en bambou tressé</strong> pour la fibre le jour et pour la lumière filtrée le soir. Elle marche au-dessus d’un plan de travail comme dans une chambre.",
        ],
        "angles": [
            [
                ("Le tressage découpe la lumière", "Une ampoule nue tape dans les yeux. Là, la fibre s’interpose : le soir, le dessin du tressage se dépose sur le plafond et la lumière arrive sans arête dure."),
                ("Le diamètre décide de tout", "{size} Au-dessus d’une table, prenez nettement plus étroit que le plateau. Un dôme trop large écrase le repas ; trop petit, on ne le voit plus."),
                ("Chaude même éteinte", "En plein jour, il reste un volume clair et un peu doré accroché au plafond. {care_lead}{care}. {aspect}"),
            ],
            [
                ("Ce qu’on voit quand on allume", "La lumière ne sort pas d’un bloc, elle passe entre les lattes et arrive par petites raies. C’est ce qui rend la vannerie lisible, nervure après nervure."),
                ("Prendre la mesure avant de percer", "{size} Pensez aussi à la hauteur libre : on doit pouvoir passer dessous sans y penser."),
                ("Un objet, pas seulement une lampe", "Éteinte, elle continue de meubler le plafond, ce qu’un globe blanc ne fait pas. {care_lead}{care}. {aspect}"),
            ],
            [
                ("Une lumière qui ne fatigue pas", "Le bambou retient une partie du faisceau et laisse filer le reste. On peut dîner dessous sans plisser les yeux, même avec une ampoule assez forte."),
                ("Le bon diamètre au-dessus d’une table", "{size} Gardez une bonne marge entre le bord de l’abat-jour et le bord du plateau, sinon la pièce paraît encombrée."),
                ("La fibre travaille avec le reste", "Du bois, du lin, un mur clair : le bambou s’y pose sans effort. {care_lead}{care}. {aspect}"),
            ],
        ],
    },
    "Suspensions rotin": {
        "kind": "suspension",
        "base": "Suspension rotin tressé",
        "kw": "suspension en rotin tressé",
        "matter": "rotin tressé",
        "usp": "Rotin tressé",
        "care": "un chiffon sec, le rotin ne se lave pas à l’eau",
        "matter_faq": "Du rotin tressé, plus souple et plus miel que le bambou. Les brins ne prennent pas la teinte de façon parfaitement homogène, et c’est visible de près.",
        "intros": [
            "Le rotin tressé donne une lumière rayée plutôt qu’une nappe uniforme. Cette <strong>suspension en rotin tressé</strong> se pose au-dessus d’un coin repas ou dans un salon qui manque de matière.",
            "Cette <strong>suspension en rotin tressé</strong> ressemble à un panier retourné, et c’est exactement l’effet cherché. Elle réchauffe une pièce claire sans y ajouter de couleur.",
            "Un abat-jour en rotin tressé, du miel dans la fibre, une lumière qui sort par les vides du tressage : cette <strong>suspension en rotin tressé</strong> convient à une chambre comme à une table.",
        ],
        "angles": [
            [
                ("Le tressage strie la lumière", "Les brins laissent passer la lumière par intervalles. Sur les murs proches, ça donne un jeu de raies fines qui bouge dès qu’on change d’ampoule."),
                ("Un volume léger au-dessus de la pièce", "{size} Le rotin pèse peu pour son encombrement : on peut viser large sans alourdir le plafond."),
                ("Le miel du rotin, allumé ou éteint", "La fibre garde sa couleur chaude en pleine journée. {care_lead}{care}. {aspect}"),
            ],
            [
                ("Une lumière moins frontale", "Le faisceau se casse dans le tressage avant d’arriver sur la table. Utile quand on mange sous le luminaire tous les soirs."),
                ("Choisir la bonne envergure", "{size} Au-dessus d’un îlot, un abat-jour large centre la pièce ; dans une chambre, restez modeste."),
                ("Ça reste un objet de vannerie", "De près, on voit le sens du tressage et les reprises de brin. {care_lead}{care}. {aspect}"),
            ],
            [
                ("Ce que la fibre fait au faisceau", "Le rotin est plus souple que le bambou, la maille est souvent plus ouverte : la lumière passe davantage, les raies sont plus larges."),
                ("Mesurez la table, pas le mur", "{size} La largeur du plateau donne la limite haute ; la hauteur sous plafond décide de la longueur du câble."),
                ("Facile à vivre", "{care_lead}{care}. Le rotin se patine un peu avec les années, sans se dégrader. {aspect}"),
            ],
        ],
    },
    "Suspensions bois": {
        "kind": "suspension",
        "base": "Suspension bois",
        "kw": "suspension en bois",
        "matter": "bois",
        "usp": "Bois",
        "care": "un chiffon sec, sans cire ni détergent",
        "matter_faq": "Du bois : lamelles, placage ou abat-jour tourné selon le modèle. Le veinage n’est jamais deux fois le même, celui des photos est un exemple.",
        "intros": [
            "Le bois absorbe la lumière au lieu de la renvoyer. Cette <strong>suspension en bois</strong> réchauffe la pièce sans créer d’éclat, ce qui la rend facile à vivre au-dessus d’une table.",
            "Cette <strong>suspension en bois</strong> se remarque d’abord par sa matière, avant d’être une source de lumière. Salle à manger ou chambre : c’est la même logique, un objet chaud au point haut de la pièce.",
            "Du bois au plafond change la température d’une pièce plus vite qu’un mur repeint. Cette <strong>suspension en bois</strong> joue là-dessus, avec une lumière qui reste douce.",
        ],
        "angles": [
            [
                ("Une lumière que le bois adoucit", "Le bois ne renvoie pas comme le métal : il boit une partie du faisceau. La pièce se réchauffe sans que la source devienne agressive."),
                ("Chaude au-dessus de la table", "{size} Au-dessus d’un repas, la matière compte plus que les watts : un bois clair suffit à rendre la lumière accueillante."),
                ("Le veinage fait l’objet", "Chaque pièce a son dessin, ses nœuds, sa teinte. {care_lead}{care}. {aspect}"),
            ],
            [
                ("Ce que ça change le soir", "Une fois la lumière du jour tombée, le bois renvoie une couleur légèrement ambrée. C’est ce qui distingue cette suspension d’un abat-jour blanc."),
                ("La bonne taille pour la pièce", "{size} Trop petite, une suspension en bois disparaît dans le plafond ; laissez-lui de la place."),
                ("Vivre avec, sans entretien", "{care_lead}{care}. Le bois se patine, il ne s’abîme pas. {aspect}"),
            ],
            [
                ("La matière avant la performance", "On ne choisit pas ce luminaire pour ses lumens. On le choisit parce que le bois casse la froideur d’un plafond blanc."),
                ("Mesurer, puis percer", "{size} Vérifiez aussi la hauteur : au-dessus d’une table, le bas de l’abat-jour doit rester au-dessus du champ de vision."),
                ("Un bois qui reste sobre", "Pas de vernis brillant, pas de reflet parasite. {care_lead}{care}. {aspect}"),
            ],
        ],
    },
    "Suspensions pierre": {
        "kind": "suspension",
        "base": "Suspension effet pierre",
        "kw": "suspension effet pierre",
        "matter": "composite à grain minéral",
        "usp": "Effet pierre",
        "care": "un chiffon doux, rien d’abrasif qui rayerait le grain",
        "matter_faq": "Un composite à grain minéral, beaucoup plus léger qu’un bloc de pierre taillé. L’aspect travertin ou albâtre vient de ce grain de surface.",
        "intros": [
            "Cette <strong>suspension effet pierre</strong> travaille une matière à grain minéral : mate, un peu poreuse à l’œil, laiteuse dès qu’on allume. Elle tient au-dessus d’une table comme au-dessus d’un lit.",
            "Le grain minéral fait le travail ici : il retient le faisceau et le rend crémeux. Cette <strong>suspension effet pierre</strong> apporte du poids visuel sans le poids réel d’une pierre.",
            "Une matière minérale claire au plafond, une lumière qui semble venir de l’intérieur du volume : voilà ce que fait cette <strong>suspension effet pierre</strong>, en chambre comme en salle à manger.",
        ],
        "angles": [
            [
                ("Une clarté laiteuse", "Le grain retient le faisceau et le restitue en lumière crémeuse. On perd le côté ponctuel de l’ampoule, on gagne une source qui semble large."),
                ("Le format compte", "{size} Ces volumes minéraux paraissent toujours plus petits en photo qu’en vrai : mesurez avant de choisir."),
                ("Le grain se lit de près", "Allumée, la surface se réveille et les creux apparaissent. {care_lead}{care}. {aspect}"),
            ],
            [
                ("Plus léger qu’un bloc de pierre", "Le composite reprend le grain et la couleur du travertin en restant manipulable. Une fixation plafond standard suffit."),
                ("Bien la dimensionner", "{size} Au-dessus d’une table, un volume trop petit se perd ; au-dessus d’un lit, l’inverse."),
                ("Une matière qui vieillit bien", "Le mat ne prend pas les traces de doigts comme un verre. {care_lead}{care}. {aspect}"),
            ],
            [
                ("Ce que la pierre fait à la lumière", "Une surface minérale ne réfléchit pas, elle diffuse. La pièce s’éclaire par nappes plutôt que par points."),
                ("Choisir le bon volume", "{size} Regardez aussi la hauteur libre : ces formes pleines se remarquent tout de suite quand elles descendent trop."),
                ("Presque rien à faire", "{care_lead}{care}. Pas de produit, pas d’eau stagnante dans les creux. {aspect}"),
            ],
        ],
    },
    "Suspensions verre": {
        "kind": "suspension",
        "base": "Suspension verre",
        "kw": "suspension en verre",
        "matter": "verre",
        "usp": "Verre",
        "care": "un chiffon microfibre, la poussière se voit vite sur le verre",
        "matter_faq": "Du verre : fumé, opalin, ambré ou transparent selon la variante. Le verre soufflé garde de petites irrégularités visibles en transparence.",
        "intros": [
            "Cette <strong>suspension en verre</strong> laisse voir la source à travers la matière. Selon la teinte du verre, la lumière ressort franche ou tamisée, et l’effet dans la pièce n’a rien à voir.",
            "Un globe, une cloche, une grappe : cette <strong>suspension en verre</strong> se place au-dessus d’un îlot ou d’une table, là où on veut de la lumière sans masse au plafond.",
            "Le verre est la seule matière qui laisse la lumière traverser entièrement. Cette <strong>suspension en verre</strong> en tire une lumière large, avec des reflets sur les surfaces proches.",
        ],
        "angles": [
            [
                ("La lumière traverse et se teinte", "Un verre fumé assombrit et calme la pièce, un opalin l’élargit. Le même luminaire ne donne pas du tout la même soirée selon la teinte choisie."),
                ("Globe seul ou ligne de globes", "{size} Une ligne tient un îlot de cuisine ; une pièce unique suffit au-dessus d’une petite table."),
                ("Un verre se garde propre", "{care_lead}{care}. C’est la contrepartie du verre : ça se voit vite, ça se nettoie vite. {aspect}"),
            ],
            [
                ("Voir la source, c’est le point", "Ici, on ne cache pas l’ampoule, on l’habille. C’est ce qui rend le verre intéressant quand il est allumé bas, le soir."),
                ("Choisir la bonne échelle", "{size} Au-dessus d’un plan de travail, plusieurs petits globes éclairent mieux qu’un seul gros."),
                ("Les reflets font partie du décor", "Le verre renvoie des points de lumière sur les murs et les plans autour. {care_lead}{care}. {aspect}"),
            ],
            [
                ("Une lumière franche ou tamisée", "Tout dépend de la teinte : le transparent ne filtre presque rien, l’ambré réchauffe, le fumé retient. La forme, elle, décide de la direction."),
                ("La taille avant l’achat", "{size} Le verre trompe l’œil sur les photos ; les cotes de la variante sont plus fiables que l’impression."),
                ("Fragile mais pas capricieux", "Manipulez à la pose, ensuite il ne demande rien. {care_lead}{care}. {aspect}"),
            ],
        ],
    },
    "Lustres cristal": {
        "kind": "lustre",
        "base": "Lustre effet cristal",
        "kw": "lustre effet cristal",
        "matter": "verre travaillé",
        "usp": "Effet cristal",
        "care": "un plumeau ou un chiffon microfibre sur les facettes",
        "matter_faq": "Du verre travaillé : facetté, strié ou taillé en gouttes selon le modèle. L’expression « effet cristal » décrit ce jeu d’arêtes dans le verre.",
        "intros": [
            "Ce <strong>lustre effet cristal</strong> éclate la lumière en petits points brillants au lieu de la diffuser. Il lui faut un peu de hauteur sous plafond pour que l’effet fonctionne.",
            "Les arêtes du verre découpent le faisceau et le renvoient par éclats. Ce <strong>lustre effet cristal</strong> prend tout son sens le soir, allumé bas, dans un salon ou une cage d’escalier.",
            "Ce <strong>lustre effet cristal</strong> joue sur le verre taillé et sur la façon dont il fragmente la lumière. Le dessin reste contemporain, pas celui d’un lustre d’époque.",
        ],
        "angles": [
            [
                ("Le verre fragmente la lumière", "Chaque facette renvoie un point brillant. Sur un plafond clair, ça pique de petites taches lumineuses tout autour du lustre."),
                ("Il lui faut de la hauteur", "{size} Sous un plafond bas, l’effet se perd et le lustre gêne le passage. Vérifiez la hauteur libre avant de commander."),
                ("Baissée, la lumière scintille", "Sur un variateur, on passe d’un éclairage général à un scintillement. {care_lead}{care}. {aspect}"),
            ],
            [
                ("Ce que les facettes changent", "Un abat-jour lisse donne une nappe ; le verre taillé donne des points. C’est plus vivant, et plus contrasté sur les murs."),
                ("Dimensionner l’envergure", "{size} Comptez large dans un séjour : un lustre à facettes trop petit passe pour un accessoire."),
                ("Un entretien régulier", "La poussière se voit sur les arêtes plus que sur une surface mate. {care_lead}{care}. {aspect}"),
            ],
            [
                ("Un éclat maîtrisé", "Le verre travaillé donne du brillant sans virer au clinquant, à condition de garder une ampoule chaude plutôt que blanche froide."),
                ("Mesurez avant d’accrocher", "{size} Regardez la hauteur sous le lustre autant que son diamètre : c’est elle qui décide du confort."),
                ("Vivre avec les reflets", "Les points de lumière se déplacent quand on bouge dans la pièce. {care_lead}{care}. {aspect}"),
            ],
        ],
    },
    "Lustres anneau": {
        "kind": "lustre",
        "base": "Lustre anneau LED",
        "kw": "lustre à anneaux LED",
        "matter": "profilé LED",
        "usp": "Anneau LED",
        "care": "un chiffon sec sur le profilé",
        "matter_faq": "Un ou plusieurs cercles en profilé aluminium, avec la LED logée à l’intérieur derrière un diffuseur. Aucune ampoule visible, aucune ampoule à ajouter.",
        "intros": [
            "Ce <strong>lustre à anneaux LED</strong> pose un cercle de lumière au plafond, sans ampoule apparente. C’est le geste le plus simple pour éclairer une table ronde ou un séjour.",
            "La LED est cachée dans le profilé : ce <strong>lustre à anneaux LED</strong> montre une ligne lumineuse continue, pas une source ponctuelle. Rien ne dépasse, rien ne se change.",
            "Ce <strong>lustre à anneaux LED</strong> tient dans un séjour contemporain sans surcharger le plafond. Un anneau au-dessus d’une table ronde, plusieurs dans une pièce haute.",
        ],
        "angles": [
            [
                ("Un cercle de lumière, rien d’autre", "La LED est dans le profilé : on voit une ligne continue, jamais l’ampoule. C’est ce qui donne cet aspect net, presque graphique, une fois allumé."),
                ("Un anneau ou plusieurs", "{size} Un cercle suffit au-dessus d’une table ronde. Les compositions à plusieurs anneaux sont faites pour les pièces hautes."),
                ("L’envergure compte plus que le nombre", "Deux anneaux serrés se voient moins qu’un seul très large. {care_lead}{care}. {aspect}"),
            ],
            [
                ("Rien à changer pendant des années", "Pas de douille, pas d’ampoule à dévisser au-dessus d’une table : la LED est intégrée pour la durée de vie du luminaire."),
                ("Le diamètre décide de l’effet", "{size} Mesurez la table, puis la pièce. Un anneau doit se lire comme un cercle, pas comme un trait au loin."),
                ("Une lumière régulière", "La ligne lumineuse éclaire de façon égale, sans point chaud. {care_lead}{care}. {aspect}"),
            ],
            [
                ("Le dessin plutôt que la masse", "Un anneau occupe l’espace sans le boucher : on voit le plafond au travers. Utile dans une pièce déjà chargée."),
                ("Bien choisir la taille", "{size} Dans un séjour, additionnez longueur et largeur en mètres : le chiffre obtenu, lu en centimètres, donne un diamètre de départ."),
                ("Simple à garder propre", "{care_lead}{care}. Le diffuseur prend peu la poussière. {aspect}"),
            ],
        ],
    },
    "Lustres salon": {
        "kind": "lustre",
        "base": "Lustre salon",
        "kw": "lustre de salon",
        "matter": "métal et lumière",
        "usp": "Lustre de salon",
        "care": "un chiffon doux sur la structure",
        "matter_faq": "Une structure métal, parfois complétée de verre selon le modèle. Les photos de la fiche montrent la pièce exacte, finition comprise.",
        "intros": [
            "Ce <strong>lustre de salon</strong> occupe le point haut de la pièce à vivre. C’est de lui que part la lumière du soir, donc autant qu’il soit à l’échelle du séjour.",
            "Un séjour sans luminaire central se contente d’une lumière de bord. Ce <strong>lustre de salon</strong> corrige ça : il éclaire depuis le centre et donne un repère au plafond.",
            "Ce <strong>lustre de salon</strong> se choisit d’abord pour son envergure, ensuite pour sa finition. Il faut pouvoir traverser la pièce sans baisser la tête.",
        ],
        "angles": [
            [
                ("Le point haut de la pièce à vivre", "Un lustre trop discret dans un grand séjour ne fait ni lumière ni décor. Celui-ci est fait pour être vu depuis le canapé."),
                ("Le dimensionner à la pièce", "{size} Repère utile : additionnez la longueur et la largeur du séjour en mètres, lisez le résultat en centimètres, vous avez un diamètre de départ."),
                ("La lumière du soir part de là", "En complément de deux lampes basses, il suffit à toute la soirée. {care_lead}{care}. {aspect}"),
            ],
            [
                ("Ce qu’un lustre central change", "La lumière vient d’en haut et du milieu : les angles de la pièce restent plus sombres, ce qui est exactement ce qu’on veut le soir."),
                ("Hauteur avant diamètre", "{size} Sous 2,50 m de plafond, préférez un modèle plat. Au-delà, vous pouvez laisser descendre."),
                ("Une finition qui doit tenir", "Elle sera vue de loin et tous les jours. {care_lead}{care}. {aspect}"),
            ],
            [
                ("Le repère visuel du séjour", "Comme une table basse ou un tapis, un lustre structure la pièce même éteint. C’est ce qui justifie d’y mettre de l’envergure."),
                ("Mesurez la circulation", "{size} On doit passer dessous librement, y compris quand on traverse sans regarder."),
                ("Peu d’entretien", "{care_lead}{care}. Une fois par saison suffit largement. {aspect}"),
            ],
        ],
    },
    "Plafonniers": {
        "kind": "plafonnier",
        "base": "Plafonnier LED",
        "kw": "plafonnier LED",
        "matter": "diffuseur LED",
        "usp": "Plafonnier LED",
        "care": "un chiffon sec sur le diffuseur",
        "matter_faq": "Un plafonnier d’intérieur, plaqué au plafond, à installer hors volumes d’eau. Le diffuseur est en acrylique ou en verre selon le modèle.",
        "intros": [
            "Ce <strong>plafonnier LED</strong> se plaque au plafond : rien ne descend, rien ne gêne. C’est la solution quand une suspension serait dans le passage.",
            "Couloir, chambre, pièce basse : ce <strong>plafonnier LED</strong> éclaire sans occuper de volume. La lumière arrive en nappe régulière plutôt qu’en faisceau.",
            "Ce <strong>plafonnier LED</strong> est fait pour les endroits où la hauteur manque. On le pose, il éclaire large, et on l’oublie.",
        ],
        "angles": [
            [
                ("Collé au plafond, rien ne descend", "Aucune tige, aucun câble : on passe dessous sans y penser. C’est le seul choix raisonnable dans un couloir étroit ou sous une poutre."),
                ("La pièce basse trouve sa lumière", "{size} Dès que le plafond descend sous 2,50 m, ou juste au-dessus d’un lit, le plafonnier prend l’avantage sur la suspension."),
                ("Une nappe, pas un spot", "La lumière se répartit au lieu de tomber en cône. {care_lead}{care}. {aspect}"),
            ],
            [
                ("Discret par construction", "Éteint, il se confond presque avec le plafond. C’est utile dans une pièce déjà occupée par des meubles ou des poutres."),
                ("Choisir la bonne surface", "{size} Un diffuseur large éclaire plus uniformément qu’un petit modèle très lumineux."),
                ("Intérieur, hors volumes d’eau", "À réserver aux pièces sèches, pas à une douche. {care_lead}{care}. {aspect}"),
            ],
            [
                ("La lumière utile, sans mise en scène", "Ce n’est pas la pièce qu’on montre aux invités, c’est celle qui rend un couloir praticable la nuit."),
                ("Une taille pour chaque pièce", "{size} Pour une chambre, visez la couverture ; pour un couloir, la régularité compte plus que la puissance."),
                ("Rien à entretenir", "{care_lead}{care}. Pas d’ampoule à changer, pas de démontage. {aspect}"),
            ],
        ],
    },
    "Suspensions métal": {
        "kind": "suspension",
        "base": "Suspension métal",
        "kw": "suspension en métal",
        "matter": "métal laqué",
        "usp": "Métal",
        "care": "un chiffon sec, sans abrasif qui marquerait la laque",
        "matter_faq": "Un abat-jour en métal laqué, noir, doré ou aspect laiton selon la variante. Le métal étant opaque, la lumière ne sort que par le bas.",
        "intros": [
            "Cette <strong>suspension en métal</strong> dirige la lumière vers le bas : le halo tombe sur le plan de travail ou sur la table, sans se répandre au plafond.",
            "Un abat-jour métal, un faisceau net, rien qui traverse : cette <strong>suspension en métal</strong> est faite pour éclairer un endroit précis, en cuisine notamment.",
            "Cette <strong>suspension en métal</strong> se remarque par sa forme et sa finition plus que par sa matière. Deux ou trois exemplaires alignés tiennent un îlot.",
        ],
        "angles": [
            [
                ("Un faisceau net, dirigé vers le bas", "Le métal est opaque : toute la lumière sort par l’ouverture. On obtient un rond de lumière franc sous le luminaire, sans halo autour."),
                ("Une, deux ou trois sur un îlot", "{size} En cuisine, l’alignement compte autant que le diamètre : espacez régulièrement le long du plan de travail."),
                ("La finition fait le style", "Noir graphique ou doré chaud, ce n’est pas le même objet. {care_lead}{care}. {aspect}"),
            ],
            [
                ("Éclairer un endroit, pas une pièce", "C’est un éclairage de tâche : très efficace au-dessus d’un plan de travail, insuffisant seul dans un grand salon."),
                ("Choisir le diamètre", "{size} Un abat-jour large donne un rond de lumière plus doux ; un petit concentre davantage."),
                ("Un métal qui se garde", "{care_lead}{care}. La laque marque si on frotte trop. {aspect}"),
            ],
            [
                ("La forme dessine le halo", "Un dôme évasé étale la lumière, un cylindre la resserre. C’est la géométrie de l’abat-jour qui décide, pas la puissance de l’ampoule."),
                ("Bien placer la hauteur", "{size} Au-dessus d’un îlot, laissez le bas de l’abat-jour au-dessus du regard, sinon on voit la source en s’asseyant."),
                ("Simple à vivre", "{care_lead}{care}. Rien d’autre à prévoir. {aspect}"),
            ],
        ],
    },
    "Suspensions déco": {
        "kind": "suspension",
        "base": "Suspension déco en céramique",
        "kw": "suspension en céramique",
        "matter": "céramique émaillée",
        "usp": "Céramique émaillée",
        "care": "un chiffon doux sur l’émail",
        "matter_faq": "De la céramique émaillée, cuite pièce à pièce. L’émail présente de légères variations de teinte et parfois un fin réseau de craquelures, liés à la cuisson.",
        "intros": [
            "Cette <strong>suspension en céramique</strong> se choisit d’abord pour sa forme. Elle éclaire un comptoir, un couloir ou un chevet, sans prétendre remplacer un lustre de salon.",
            "De la céramique émaillée au plafond, c’est un objet autant qu’une lampe. Cette <strong>suspension en céramique</strong> se pose là où on regarde de près : entrée, coin repas, table de nuit.",
            "Cette <strong>suspension en céramique</strong> apporte un satiné que ni le bois ni le métal ne donnent. Un accent, dans une pièce qui a déjà sa lumière principale.",
        ],
        "angles": [
            [
                ("La forme d’abord, la lumière ensuite", "On l’achète pour son volume et son émail. L’éclairage suit, plus doux qu’un spot, plus décoratif qu’un plafonnier."),
                ("Un accent, pas un lustre", "{size} Un comptoir, un couloir, un chevet : ces formats sont pensés pour compléter, pas pour éclairer seuls un séjour."),
                ("L’émail renvoie un satiné", "La cuisson laisse des variations de teinte d’une pièce à l’autre. {care_lead}{care}. {aspect}"),
            ],
            [
                ("Un objet qu’on regarde de près", "La céramique se juge à un mètre : l’épaisseur de l’émail, le bord, la petite irrégularité. C’est pour ça qu’on la met là où on passe."),
                ("Le bon endroit", "{size} Au-dessus d’un îlot ou d’un meuble d’entrée, elle a la bonne échelle. Au centre d’un grand salon, elle se perd."),
                ("Vivre avec l’émail", "{care_lead}{care}. Ni abrasif ni détergent, l’émail se rayerait. {aspect}"),
            ],
            [
                ("Une lumière chaude, contenue", "La céramique est opaque : la lumière sort par le bas et reste concentrée sous l’abat-jour. Bon pour un coin, moins pour une pièce entière."),
                ("Choisir l’échelle", "{size} Deux petites pièces côte à côte fonctionnent souvent mieux qu’une seule moyenne."),
                ("Fait pièce à pièce", "Aucune pièce n’est parfaitement identique à la suivante. {care_lead}{care}. {aspect}"),
            ],
        ],
    },
    "Lustres statement": {
        "kind": "lustre",
        "base": "Lustre statement",
        "kw": "grand lustre",
        "matter": "structure rayonnante",
        "usp": "Grand lustre",
        "care": "un chiffon sec sur les branches",
        "matter_faq": "Une structure métal rayonnante, avec LED intégrée. La pièce est volumineuse : mesurez la hauteur libre avant de commander.",
        "intros": [
            "Ce <strong>grand lustre</strong> est fait pour occuper un vide : un séjour à double hauteur, une cage d’escalier. Dans une pièce standard, il serait de trop.",
            "On ne met pas ce <strong>grand lustre</strong> partout. Il lui faut de la hauteur et du recul, et il devient alors le seul objet nécessaire au plafond.",
            "Ce <strong>grand lustre</strong> se choisit pour son envergure. Toute la lumière du soir peut partir de là, à condition que la pièce le supporte.",
        ],
        "angles": [
            [
                ("Un geste qui occupe le vide", "Dans une cage d’escalier ou un séjour haut, un luminaire discret disparaît. Celui-ci remplit l’espace vertical au lieu de le subir."),
                ("Mesurez avant d’accrocher", "{size} Relevez la hauteur libre sous le point de fixation et comparez-la à l’encombrement de la pièce."),
                ("Toute la lumière du soir", "Il éclaire assez pour se passer d’un plafonnier d’appoint. {care_lead}{care}. {aspect}"),
            ],
            [
                ("Fait pour la hauteur", "Sous un plafond bas, préférez un anneau plat ou un plafonnier. Ici, la pièce doit offrir du volume."),
                ("Vérifier les cotes", "{size} L’envergure et la longueur totale sont les deux chiffres à confronter à votre pièce."),
                ("Le seul objet nécessaire", "Une fois installé, il n’a pas besoin d’accompagnement. {care_lead}{care}. {aspect}"),
            ],
            [
                ("Une pièce qui se voit de loin", "C’est un point de repère dans un volume ouvert : depuis l’étage, depuis l’entrée, depuis le canapé."),
                ("La hauteur libre décide", "{size} Comptez le passage sous le luminaire avant tout le reste."),
                ("Peu de contraintes ensuite", "{care_lead}{care}. Pas d’ampoule à changer. {aspect}"),
            ],
        ],
    },
    "Suspensions modernes": {
        "kind": "suspension",
        "base": "Suspension design",
        "kw": "suspension design",
        "matter": "structure épurée",
        "usp": "Dessin épuré",
        "care": "un chiffon sec",
        "matter_faq": "Une structure métal noir avec LED intégrée. Peu d’éléments, aucune ampoule visible.",
        "intros": [
            "Cette <strong>suspension design</strong> tient sur peu de choses : une géométrie simple, une source invisible, rien autour. Elle convient au-dessus d’une table comme au centre d’un séjour.",
            "Pas d’ampoule apparente, pas d’ornement : cette <strong>suspension design</strong> mise sur la ligne. C’est ce qui la rend facile à poser dans un intérieur déjà chargé.",
            "Cette <strong>suspension design</strong> fait le contraire d’un lustre : elle disparaît quand elle est éteinte et n’éclaire que ce qu’il faut quand elle est allumée.",
        ],
        "angles": [
            [
                ("Peu de choses, bien tenues", "Une ligne, une source cachée, une finition mate. Il n’y a rien à regarder de trop, et c’est le but."),
                ("Calme au-dessus de la table", "{size} Elle tient au-dessus d’un plateau comme au centre d’une pièce, sans imposer de style."),
                ("La source ne se voit pas", "La LED est intégrée, on ne voit que l’effet. {care_lead}{care}. {aspect}"),
            ],
        ],
    },
}


def rows_live() -> list[dict]:
    nodes = json.loads(LIVE_PATH.read_text(encoding="utf-8"))
    types = {r["handle"]: r.get("type") for r in json.loads(ROWS_PATH.read_text(encoding="utf-8"))}
    prices = {r["handle"]: r.get("price") for r in json.loads(ROWS_PATH.read_text(encoding="utf-8"))}
    rows = []
    for n in nodes:
        rows.append(
            {
                "handle": n["handle"],
                "title": n["title"],
                "type": types.get(n["handle"]) or "Suspensions bambou",
                "price": prices.get(n["handle"]),
                "options": [
                    {
                        "name": o["name"],
                        "values": renamed_values(
                            n["handle"],
                            o["name"],
                            display_values(o["name"], [v["name"] for v in o["optionValues"]]),
                        ),
                    }
                    for o in n["options"]
                ],
            }
        )
    return rows


def family_for(row: dict) -> dict:
    key = FAMILY_OVERRIDES.get(row["handle"]) or row["type"]
    fam = dict(FAMILIES.get(key) or FAMILIES["Suspensions bambou"])
    fam["_key"] = key
    fam.update({k: v for k, v in MATTER_OVERRIDES.get(row["handle"], {}).items()})
    return fam


def new_title(row: dict, options: list[dict]) -> str:
    override = TITLE_OVERRIDES.get(row["handle"])
    if override:
        return tidy_lights(dash_free(override))
    return tidy_lights(dash_free(row["title"]))


def seo_title_of(title: str) -> str:
    suffix = " | Lumière Matière"
    if len(title) + len(suffix) <= 70:
        return title + suffix
    chunk = title[: 70 - len(suffix)]
    # on coupe sur un segment entier plutôt qu’au milieu d’une cote
    chunk = chunk.rsplit(",", 1)[0] if "," in chunk else chunk.rsplit(" ", 1)[0]
    return chunk.rstrip(" ,;:·") + suffix


def seo_description_of(title: str, fam: dict, source: str, cms: list[int], aspect: str) -> str:
    src = {
        "led": "LED intégrée, aucune ampoule à prévoir.",
        "e27": "Douille E27, ampoule non fournie.",
        "e14": "Douille E14, ampoule non fournie.",
        "g9": "Douille G9, ampoule non fournie.",
        "mixte": "LED intégrée ou douille E27 selon la variante.",
    }[source]
    dp = diam_phrase(cms)
    low = title.lower()
    # ne pas répéter la matière ni la cote déjà présentes dans le titre
    liaisons = {"en", "et", "à", "de", "du", "des", "avec", "sur", "ou", "selon", "la", "le"}
    matter_known = any(
        word in low
        for word in re.findall(r"[\wéèêàôûîç]+", fam["matter"].lower())
        if len(word) >= 3 and word not in liaisons
    )
    bits = [f"{title}." if matter_known else f"{title} en {fam['matter']}.", src]
    if dp and dp.lower() not in low and dp.replace("Ø ", "").lower() not in low:
        bits.append(f"{dp}.")
    if aspect:
        bits.append(aspect)
    bits.append("Livraison offerte en France métropolitaine.")
    text = " ".join(bits)
    if len(text) > 320:
        text = text[:317].rsplit(" ", 1)[0] + "."
    return dash_free(text)


def usps_of(fam: dict, source: str, cms: list[int], axis: str | None, values: list[str], options: list[dict]) -> list[str]:
    pills = [
        fam["usp"],
        {
            "led": "LED intégrée",
            "e27": "Douille E27",
            "e14": "Douille E14",
            "g9": "Douille G9",
            "mixte": "LED ou douille E27",
        }[source],
    ]
    dp = diam_phrase(cms)
    if dp:
        pills.append(dp)
    blob = " ".join(v for o in options for v in o["values"]).lower()
    if "télécommande" in blob or "variable" in blob:
        pills.append("Intensité variable")
    elif "3 teintes" in blob:
        pills.append("3 teintes")
    if fam["kind"] == "plafonnier":
        pills.append("Plafond bas")
    if len(pills) < 4 and axis and values and not all(is_blind_code(v) for v in values):
        label = {
            "Câble": "Câble au choix",
            "Verre": "Verre au choix",
            "Abat-jour": "Abat-jour au choix",
            "Émail": "Émail au choix",
            "Finition": "Finition au choix",
            "Couleur": "Teinte au choix",
        }.get(axis)
        if label and len(values) > 1:
            pills.append(label)
        elif values:
            pills.append(values[0])
    out: list[str] = []
    for p in pills:
        p = dash_free(p)
        if p not in out:
            out.append(p)
    return out[:4]


def description_of(fam: dict, rot: int, source: str, cms: list[int], aspect: str, size_txt: str) -> str:
    intro = fam["intros"][rot % len(fam["intros"])]
    src = SOURCE_SENTENCES[source][rot % 3]
    tail = " ".join(x for x in [src, aspect] if x)
    if not cms:
        tail = " ".join(x for x in [tail, "Les cotes exactes sont sur chaque variante."] if x)
    return dash_free(f"<p>{intro}</p>") + dash_free(f"<p>{tail}</p>")


SPEC_LABELS = {
    "Câble": "Câble et rosace",
    "Verre": "Verre",
    "Abat-jour": "Abat-jour",
    "Émail": "Émail",
    "Finition": "Finition",
    "Couleur": "Teinte",
    "Modèle": "Modèle",
    "Forme": "Forme",
    "Puissance": "Puissance",
    "Lumières": "Nombre de lumières",
    "Ampoule": "Ampoule",
    "Taille": "Taille",
    "Diamètre": "Diamètre",
}


def specs_of(fam: dict, source: str, cms: list[int], options: list[dict], price: str | None) -> str:
    source_row = {
        "led": "LED intégrée",
        "e27": "douille E27, ampoule non fournie",
        "e14": "douille E14, ampoule non fournie",
        "g9": "douille G9, ampoule non fournie",
        "mixte": "LED intégrée ou douille E27 selon la variante",
    }[source]
    rows = [
        f"<li><strong>Type :</strong> {fam['base']}</li>",
        f"<li><strong>Matière :</strong> {fam['matter']}</li>",
        "<li><strong>Usage :</strong> intérieur, hors volumes d’eau</li>",
        f"<li><strong>Source :</strong> {source_row}</li>",
    ]
    listed: set[str] = set()
    if cms:
        rows.append(f"<li><strong>Diamètre :</strong> {et_join([f'{c} cm' for c in cms])}</li>")
        listed.update({"Diamètre", "Taille"})
    for opt in options:
        name = opt["name"]
        vals = [v for v in opt["values"] if "entrepôt" not in v.lower() and "chine" not in v.lower()]
        if not vals or name in listed:
            continue
        if name in {"Température", "Éclairage"}:
            rows.append(f"<li><strong>Lumière :</strong> {et_join(vals[:6])}</li>")
            listed.add(name)
            continue
        label = SPEC_LABELS.get(name)
        if not label:
            continue
        rows.append(f"<li><strong>{label} :</strong> {et_join(vals[:8])}</li>")
        listed.add(name)
    if price:
        rows.append(f"<li><strong>Prix :</strong> à partir de {price.replace('.00', '')} € TTC selon la variante</li>")
    rows.append("<li><strong>Installation :</strong> au plafond, courant coupé, hors salle de bain</li>")
    return dash_free("<ul>" + "".join(rows) + "</ul>")


def installation_of(fam: dict, source: str, rot: int) -> str:
    if fam["kind"] == "plafonnier":
        pose = [
            "Le plafonnier se plaque au plafond : il n’y a pas de hauteur à régler. La platine se visse, le diffuseur se clipse ensuite.",
            "Pose directe au plafond, sans câble à ajuster. Vérifiez juste que la boîte de dérivation est bien centrée sur la platine.",
            "Rien à régler à la pose : la platine se fixe au plafond et le diffuseur vient par-dessus.",
        ][rot % 3]
    else:
        pose = [
            "Fixation au plafond. Le câble se raccourcit ou s’enroule dans la rosace pour trouver la bonne hauteur : on doit circuler dessous sans y penser.",
            "Le luminaire se fixe au plafond et la hauteur se règle au câble, à la rosace. Au-dessus d’une table, comptez de quoi passer sans heurter l’abat-jour.",
            "Pose au plafond, hauteur ajustable au câble. Faites l’essai avant de couper : on se trompe plus souvent en trop court qu’en trop long.",
        ][rot % 3]
    src = {
        "led": "La LED est intégrée : vous raccordez phase, neutre et terre, il n’y a pas de douille à équiper.",
        "e27": "Vissez l’ampoule E27 après la pose. Elle n’est pas fournie.",
        "e14": "Vissez les ampoules E14 après la pose. Elles ne sont pas fournies.",
        "g9": "Enfichez l’ampoule G9 après la pose. Elle n’est pas fournie.",
        "mixte": "Selon la variante : raccordement direct sur la LED intégrée, ou douille E27 à équiper d’une ampoule.",
    }[source]
    sav = [
        "Coupez le courant au disjoncteur avant de commencer. Si le raccordement électrique n’est pas quelque chose que vous faites d’habitude, faites-le poser par un électricien. La notice est dans le colis.",
        "Courant coupé au disjoncteur, toujours. En cas de doute sur le raccordement, passez par un électricien. Notice fournie avec le luminaire.",
        "Commencez par couper le courant. Le raccordement reste simple, mais il n’y a aucune honte à le confier à un électricien. La notice accompagne le colis.",
    ][rot % 3]
    return dash_free(f"<p>{pose}</p>") + dash_free(f"<p>{src}</p>") + dash_free(f"<p>{sav}</p>")


def benefits_of(fam: dict, rot: int, size_txt: str, aspect: str) -> list[dict]:
    angles = fam["angles"]
    angle = angles[rot % len(angles)]
    care_lead = CARE_LEAD[rot % len(CARE_LEAD)]
    out = []
    for title, body in angle:
        text = body.format(size=size_txt, care=fam["care"], care_lead=care_lead, aspect=aspect)
        out.append({"title": dash_free(title), "body": dash_free(text)})
    return out


def faq_of(fam: dict, source: str, cms: list[int], options: list[dict], rot: int) -> list[dict]:
    items: list[dict] = []
    if fam["kind"] == "plafonnier":
        q1 = "Plafonnier ou suspension, comment choisir ?"
        a1 = (
            "Le plafonnier reste collé au plafond : c’est le bon choix dans un couloir, une chambre ou une pièce basse. "
            "La suspension garde l’avantage au-dessus d’une table, où la descente crée l’intimité."
        )
        if cms:
            a1 += f" Diamètres proposés ici : {et_join([f'{c} cm' for c in cms])}."
    elif cms:
        q1 = f"Quelle taille prendre ({diam_phrase(cms)}) ?"
        a1 = (
            f"Les diamètres de cette fiche : {et_join([f'{c} cm' for c in cms])}. "
            "Au-dessus d’une table, visez nettement moins large que le plateau, et gardez de quoi passer dessous sans heurter l’abat-jour."
        )
    else:
        q1 = "Comment choisir la taille ?"
        a1 = (
            "Les cotes sont indiquées sur chaque variante. Mesurez votre pièce avant de commander : "
            "sur une photo, un luminaire paraît toujours plus petit qu’en vrai."
        )
    items.append({"q": q1, "a": a1})

    a2 = {
        "led": "Non, il n’y en a pas besoin : la LED est intégrée au luminaire. Rien à visser à la pose, rien à remplacer ensuite.",
        "e27": "Non. La douille est une E27 et l’ampoule n’est pas fournie. Une LED blanc chaud, entre 2700 et 3000 K, convient dans une pièce à vivre.",
        "e14": "Non. Les douilles sont des E14, le petit culot à vis, et les ampoules ne sont pas fournies. Des flammes ou des filaments valent mieux ici, puisqu’elles restent visibles.",
        "g9": "Non. Le luminaire prend une ampoule G9, à broches, non fournie. Une LED G9 blanc chaud, entre 2700 et 3000 K, fait le travail.",
        "mixte": "Ça dépend de la variante. Avec la LED intégrée, il n’y a rien à ajouter. Avec la douille E27, l’ampoule reste à votre charge.",
    }[source]
    items.append({"q": "L’ampoule est-elle fournie ?", "a": a2})
    items.append({"q": "C’est quoi exactement, comme matière ?", "a": fam["matter_faq"]})

    cable = next((o for o in options if o["name"] == "Câble"), None)
    if cable and cable.get("values"):
        items.append(
            {
                "q": f"{ou_join(cable['values'])} : c’est la couleur de quoi ?",
                "a": (
                    "Du câble et de la rosace, pas de l’abat-jour. L’abat-jour garde la matière décrite sur la fiche, "
                    "quelle que soit la couleur de fil choisie."
                ),
            }
        )

    items.append(
        {
            "q": "Quel délai de livraison ?",
            "a": (
                "Livraison offerte en France métropolitaine, Corse incluse. On prépare le colis en 1 à 2 jours "
                "ouvrés, l’acheminement prend 6 à 16 jours ouvrés, soit 7 à 18 jours ouvrés au total. "
                "Les commandes validées avant 16h00, heure de Paris, partent le jour même en préparation."
            ),
        }
    )
    items.append(
        {
            "q": "Et si le luminaire ne me convient pas ?",
            "a": (
                "Vous avez 14 jours de rétractation légale, que nous étendons à 30 jours à compter de la réception. "
                "S’il s’agit d’un simple changement d’avis, les frais de retour sont à votre charge, sans frais de "
                "réapprovisionnement. Le service client répond du lundi au vendredi, de 10h00 à 18h00, "
                "sous 24 h ouvrées."
            ),
        }
    )
    return [{"q": dash_free(i["q"]), "a": dash_free(i["a"])} for i in items]


LENGTH_SWAPS = [
    (r"Ø (\d+) à (\d+) cm", r"\1 à \2 cm"),
    (r"Ø (\d+) cm", r"\1 cm"),
    (r"\bDiamètres proposés\b", "Longueurs proposées"),
    (r"\bdiamètres de cette fiche\b", "longueurs de cette fiche"),
    (r"\bDiamètres? :", "Longueur :"),
    (r"\bdiamètre\b", "longueur"),
    (r"\bDiamètre\b", "Longueur"),
]


def as_length(copy: dict) -> dict:
    """Réécrit une fiche dont l’axe de taille est une longueur, pas un diamètre."""

    def fix(text: str) -> str:
        for pattern, repl in LENGTH_SWAPS:
            text = re.sub(pattern, repl, text)
        return text

    def walk(value):
        if isinstance(value, str):
            return fix(value)
        if isinstance(value, list):
            return [walk(v) for v in value]
        if isinstance(value, dict):
            return {k: walk(v) for k, v in value.items()}
        return value

    return walk(copy)


# Sur une fiche à LED intégrée, les textes de famille qui parlent d’ampoule à choisir
# promettent un geste qui n’existe pas.
LED_SWAPS: list[tuple[str, str]] = [
    (r"même avec une ampoule assez forte", "même à pleine puissance"),
    (r"Une ampoule nue tape dans les yeux\.", "Une source nue tape dans les yeux."),
    (r"Ici, on ne cache pas l’ampoule, on l’habille\.", "Ici, la source n’est pas cachée, elle est habillée par le verre."),
    (r"dès qu’on change d’ampoule", "selon la teinte choisie"),
    (r"Ce sont les ampoules choisies qui donnent", "C’est la finition choisie qui donne"),
]


def as_led(copy: dict) -> dict:
    """Retire des textes de famille les gestes réservés aux fiches à douille."""

    def fix(text: str) -> str:
        for pattern, repl in LED_SWAPS:
            text = re.sub(pattern, repl, text)
        return text

    def walk(value):
        if isinstance(value, str):
            return fix(value)
        if isinstance(value, list):
            return [walk(v) for v in value]
        if isinstance(value, dict):
            return {k: walk(v) for k, v in value.items()}
        return value

    return walk(copy)


def build(rows: list[dict]) -> dict[str, dict]:
    # rotation stable par famille : les fiches voisines n’ont pas le même texte
    by_family: dict[str, list[str]] = {}
    for row in sorted(rows, key=lambda r: r["handle"]):
        key = FAMILY_OVERRIDES.get(row["handle"]) or row["type"]
        by_family.setdefault(key, []).append(row["handle"])
    rot_of = {h: i for handles in by_family.values() for i, h in enumerate(handles)}

    copies: dict[str, dict] = {}
    for row in rows:
        handle = row["handle"]
        fam = family_for(row)
        options = row["options"]
        cms = diameters_cm(options)
        axis, values = appearance_of(options)
        source = SOURCE_OVERRIDES.get(handle) or detect_source(handle, row["title"], options)
        rot = rot_of[handle]
        size_txt = size_sentence(cms, rot)
        aspect = aspect_sentence(axis, values, rot)
        title = new_title(row, options)
        copies[handle] = {
            "title": title,
            "seo_title": seo_title_of(title),
            "seo_description": seo_description_of(title, fam, source, cms, aspect),
            "usps": usps_of(fam, source, cms, axis, values, options),
            "description_html": description_of(fam, rot, source, cms, aspect, size_txt),
            "specs_html": specs_of(fam, source, cms, options, row.get("price")),
            "installation_html": installation_of(fam, source, rot),
            "benefits": benefits_of(fam, rot, size_txt, aspect),
            "faq": faq_of(fam, source, cms, options, rot),
        }
        if source == "led":
            copies[handle] = as_led(copies[handle])
        if handle in LENGTH_HANDLES:
            copies[handle] = as_length(copies[handle])
    return copies


def audit(copies: dict[str, dict]) -> None:
    blob = json.dumps(copies, ensure_ascii=False)
    print(f"tirets cadratins restants : {blob.count('—')} · demi-cadratins : {blob.count('–')}")
    titles = Counter(c["title"] for c in copies.values())
    dupes = {t: n for t, n in titles.items() if n > 1}
    print(f"titres uniques : {len(titles)}/{len(copies)}")
    if dupes:
        print("DOUBLONS RESTANTS :", dupes)
    for bad in ("pas une usine", "honnêteté", "galerie de matières", "pièce par pièce", "Baccarat", "ventilateur", "cristal de marque"):
        n = blob.count(bad)
        if n:
            print(f"  reste « {bad} » ×{n}")


def main() -> None:
    rows = rows_live()
    copies = build(rows)
    audit(copies)
    COPY_PATH.write_text(json.dumps(copies, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"pdp-copy.json réécrit : {len(copies)} fiches")


if __name__ == "__main__":
    main()

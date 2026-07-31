# Broyeur DropPilot

Moteur de scoring produit. Reçoit des candidats (issus des 9 sources de sourcing),
applique les hard filters + le scoring pondéré, et sort une décision par produit :
`shortlist` (→ funnel Semrush), `review` (à creuser), `reject`.

La logique de tri est celle du formateur (analyse des 9 vidéos), fusionnée avec
les critères DropPilot (marchés FR/BE/CH/LU, sweet spot 600-900€, marge nette ≥20%).

## Structure

```
broyeur_package/
├── broyeur/
│   ├── scoring_config.yaml   # SOURCE DE VÉRITÉ : tous les seuils/pondérations. Édite ici.
│   ├── broyeur.py            # moteur (hard filters + scoring). Ne code aucune règle en dur.
│   ├── adapter.py            # markdown -> Product (garde tes livrables lisibles)
│   ├── run.py                # CLI
│   └── tests/
│       └── test_broyeur.py   # 16 tests sur les produits réels des vidéos
└── README.md
```

## Installation

```bash
pip install pyyaml pytest
```

## Usage

Depuis un JSON (une liste d'objets produit) :
```bash
python -m broyeur.run --input produits.json
```

Depuis un livrable markdown d'agent :
```bash
python -m broyeur.run --input livrable.md --format md
```

Ne sortir que la shortlist :
```bash
python -m broyeur.run --input produits.json --shortlist-only
```

## Format d'entrée JSON (un produit)

```json
{
  "product_name": "Fauteuil suspendu",
  "source": "europages",
  "category": "garden",
  "price_sell": 400,
  "price_source_ali": 90,
  "net_margin_pct": 28,
  "competitors_type": "dropshippers_weak_sites",
  "sells_in_search": true,
  "sells_in_shopping": true,
  "big_retailer_same_product": false,
  "legal_eu": true,
  "not_available_on_generic_channels": "partial"
}
```

### Valeurs des champs à énumération
- `source` : flippa, dotmarket, amazon_movers, pinterest_trends, bigbuy, europages, vevor, cdiscount, temu
- `competitors_type` : dropshippers_weak_sites | dropshippers_mixed | few_or_none | semi_brands | institutional
- `not_available_on_generic_channels` : yes | partial | commodity
- `category` : libre, mais les exclusions dures portent sur : beauty, clothing, jewelry, food, computing, workwear, car_motorbike_generic, adult, weapons. baby/toys ont un override (gardés si ≥400€ ET marge ≥4x).

`price_source_ali` sert à calculer `margin_ratio` (= price_sell / price_source_ali).
Champs manquants → None → peut forcer un `review` plutôt qu'un score faussement confiant.

## Tests

```bash
pytest -v
```

Les 16 tests encodent ce que le formateur dit de chaque produit réel (biker jewelry,
cabane enfant, boîte à montre, dashcam, cave à vin, banc muscu, pergola…) et vérifient
que le broyeur tranche comme lui. Si tu changes une pondération dans le YAML, relance
les tests : ils te disent immédiatement si un arbitrage a basculé.

## Règles clés (résumé)

Hard filters (rejet binaire) : ticket <150€ (sauf marge ≥10x → floor 80€), ticket >2000€,
catégories exclues, illégal EU, dominance d'une grande enseigne sur le même produit.

Scoring /100 : marge (25) > concurrence (20) = ticket (20) > canal/GMC (15) >
signal source (12) > défendabilité niche (8). Malus : saisonnier (-10), barrière faible
+ grosses marques (-8), dur à sourcer (-6).

Décision : ≥70 shortlist · 55-69 review · <55 reject. Un flag critique manquant
(légalité EU non vérifiée, marge non calculée) force un review.

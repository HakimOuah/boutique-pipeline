# 06 — Sourcing + parcours personnalisation

Copie du phase 4 (`reports/` est gitignoré dans boutique-pipeline). Date : 2026-08-31 16:45.

Instruction Hakim : due diligence AliExpress **malgré le CAS LIMITE volume**, catalogue large, **personnalisation réelle**, parcours photo client → fournisseur.

Entrée : `CAS LIMITE` (37 270). Pas un `PASS_PREQUALIFICATION`. Sourcing ouvert uniquement sur sa demande. Aucun `GO_FINAL`, aucun `GO fournisseur`.

Preuve : SERP `fr.aliexpress.com` + passerelle VPS `variants` + API avis. **Confiance B+.** PDP = anti-bot. `exact` France refusé (SKU ambigus).

## Le constat ops

**La photo n’est pas une variante couleur.** YILI : SKU = métal + longueur ; perso **après commande** (chat). Avis FR janv. 2026 + « Ils ont ajouté la photo que je souhaitais ».

Magasins qui **encodent** la perso dans un faux attribut — à mapper DSers :

| Magasin | SKU perso | Prix promo 31/08 | Lecture |
|---|---|---:|---|
| [HAOHUPO](https://fr.aliexpress.com/item/1005008779366284.html) | Longueur = **`Send me your picture`** | **9,49 €** | Fichier attendu |
| [Letdiffery](https://fr.aliexpress.com/item/1005007259640988.html) | Longueur = **`Engrave word`** | **2,86 €** | Texte / laser, pas nano |
| [Tiffmet](https://fr.aliexpress.com/item/1005007741321294.html) | **`Type personnalisé`** | **3,29 €** | Projection couleur |

Sans ce SKU, DSers commande « or 16,5 cm » et le client reçoit une **démo**.

## Parcours photo

```
PDP Shopify (Ymq / Uploadery)
  → JPG/PNG sur CDN Files (URL HTTPS publique, pas un lien admin)
  → line item : photo_url
  → recadrage 800×800, contraste, N&B (nano)
  → DSers : SKU « Send me your picture » + remark = URL + Add pictures to remarks
  → vendeur télécharge, fabrique, expédie
```

Pièges : URL signée qui expire · photo de groupe · chat YILI non scalable · listings « 100 langues » **sans** badge Personnalisable = pas de photo client.

Avis YILI : projection « impressionniste », parfois lampe torche. Le dire sur la PDP.

## Fiches

- **YILI** `1005005478713234` — 7,49 €, 4,6, +2 000 SERP, 800+ `variants`, store 4,6. Preuve sociale max, perso au chat. `FOURNISSEUR À TESTER`
- **HAOHUPO** `1005008779366284` — 9,49 €, store 4,9, SKU photo. `FOURNISSEUR À TESTER` (meilleur mapping)
- **Letdiffery** `1005007259640988` — 2,86 €, `Engrave word`. `FOURNISSEUR À TESTER` (F3/F5)
- F2 colliers : SERP Personnalisable (DHQH homme 3,59 €, pendentif 7,59 €…) — `OFFRE TROUVÉE`, variants manquants
- F3–F8 : mêmes 3–4 magasins, pas 466 usines

Délais : avis 2–3 semaines CN, pas 5–9 j. Format fichier officiel : à lire en DSers (classe A).

Brut : dossier [`sourcing/`](sourcing/).

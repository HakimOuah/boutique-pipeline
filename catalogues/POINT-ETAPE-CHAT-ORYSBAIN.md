# Prompt à coller — nouveau chat Orysbain

> Copier tout le bloc ci-dessous dans un nouveau chat Cursor.

---

```
Tu travailles sur ORYSBAIN uniquement (pas Lumière Matière).

## Contexte

Boutique France dropshipping OH Ventures — mode **PRODUIT PUR** : sèche-serviettes électriques.
Domaines prévus : orysbain.fr / orysbain.com (pas encore achetés / Shopify pas encore créé au 21/08/2026).
Repo de vérité : `/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/` (commit + push sur ce repo).
Hub parent : `/Users/Hakim/Documents/Boutiques drop/` (règles dans CLAUDE.md).

Référence concurrente / univers ≠ ce mode : Mille et une Nuisette est une ref UNIVERS pour LM, pas pour Orysbain. Orysbain reste gamme courte, hero product, arborescence simple.

## Identité légale (figée)

- Éditeur : OH Ventures SASU, capital 1 000 €
- Siège : 47 rue Vivienne, 75002 Paris
- SIRET : 10315725100010 | TVA : FR55103157251
- Email : contact@orysbain.fr | Tél : +33 7 56 82 80 94
- Médiateur : CM2C, 14 rue Saint Jean 75017 Paris, 01 89 47 00 14, https://www.cm2c.net/ (vérifier couverture orysbain.fr)

## Chiffres opérationnels (ne pas contredire)

| Élément | Valeur |
|---|---|
| Prix héros | ~199 € | smart ~249 € |
| Cut-off | 14h00 Paris |
| Traitement | 1–2 j ouvrés |
| Transit | 4–10 j ouvrés (entrepôt DE / DPD) |
| Total | 5–12 j ouvrés |
| Livraison | Gratuite FR métro |
| Retours | 30 j (+ rétractation 14 j) |
| SAV | lun–ven 9h–17h Paris |

## DA / branding

- Positionnement : « chaleur minérale » — SDB française soignée
- Couleurs : fond `#F6F4F1` · accent cuivre `#B25A28` · ardoise `#26343C`
- Doc : `catalogues/2026-08-20-branding-audit-orysbain-lumiere-matiere.md` (section Orysbain)
- VOC / personas Léa & Marc + objections : `catalogues/2026-08-20-voc-personas-objections-orysbain-lm.md`

## Fichiers catalogue (prêts)

Racine marque : `boutique-pipeline/catalogues/orysbain/`

| Fichier / dossier | Contenu |
|---|---|
| `catalogue-dsers.csv` | 32 SKU (import DSers) |
| `CATALOGUE-DSERS.md` | Doc catalogue |
| `descriptions/*.html` | 32 fiches HTML (VOC, purgées AE/DSers/GMC leaks) |
| `pages/` | notre-histoire, faq, retours, livraison, confidentialité, CGV, conditions-paiement + INDEX.md |
| `sources-fournisseur/<supplier_id>/` | Galeries AE brutes (gitignoré) — 32/32, 195 images |
| `sources-par-handle/<handle>/` | Symlinks vers sources (gitignoré) — utiliser ça pour lire |
| `sources-fournisseur/MANIFESTE.json` | Manifeste téléchargement |

## Visuels Codex (EN COURS)

Brief mission : `catalogues/BRIEF-VISUELS-CODEX-ORYSBAIN.md`

Sortie attendue (gitignorée) :
```
catalogues/orysbain/livraisons-visuels-codex/
  brand/          # logos, home, collection
  produits/<handle>/<handle>-g1.jpg … -g5.jpg + manifeste.json
  INDEX-LIVRAISON.md
```

Slots PDP : g1 hero packshot · g2 3/4 · g3 détail commande · g4 lifestyle SDB · g5 usage serviettes.
Format : JPEG sRGB 2048×2048 (sauf logos PNG).

Déjà présents au 21/08 (brand partiel, PDP pas finis) :
- `livraisons-visuels-codex/brand/orysbain-logo-primary-ardoise.png`
- `…/orysbain-logo-inverse-blanc.png`
- `…/orysbain-logo-mono-cuivre.png`
- `…/orysbain-favicon-512.png`
- `…/orysbain-home-hero.jpg`
(encore manquants brand : home-benefit, home-detail, collection — + les 32×5 PDP)

Ne pas relancer une génération en doublon : d’abord inventaire `livraisons-visuels-codex/`, croiser avec le BRIEF.

## État d’avancement

FAIT :
- Catalogue 32 SKU + URLs AE uniques + HTML VOC
- Pages légales / FAQ / histoire
- Branding + VOC
- Sources AE locales 32/32
- Brief Codex + début livraisons brand

PAS FAIT :
- Achat domaines
- Création Shopify + thème
- Coller pages policies
- Import DSers / mapping variantes
- Upload images générées (quand Codex termine)
- GMC / Google Ads
- Vérifier adhésion CM2C pour orysbain.fr

## Ta mission dans ce chat

1. Faire un inventaire à jour de `orysbain/livraisons-visuels-codex/` (ce que Codex a déjà livré vs BRIEF).
2. Ne travailler QUE Orysbain.
3. Demande-moi la priorité si ambigu (thème Shopify, QA visuels, import, GMC…).
4. Toute modif durable → commit + push dans `boutique-pipeline` (jamais committer les JPEG sources/livraisons gitignorés, sauf si on change explicitement la politique).

Réponds d’abord par un point d’étape court : prêt / en cours / bloqué, puis propose la prochaine action concrète.
```

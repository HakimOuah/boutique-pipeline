# Prompt à coller — nouveau chat Lumière Matière

> Copier tout le bloc ci-dessous dans un nouveau chat Cursor.

---

```
Tu travailles sur LUMIÈRE MATIÈRE uniquement (pas Orysbain).

## Contexte

Boutique France dropshipping OH Ventures — mode **UNIVERS** : lustres & suspensions, organisée par **matière**.
Domaines prévus : lumierematiere.fr / lumierematiere.com (pas encore achetés / Shopify pas encore créé au 21/08/2026).
Repo de vérité : `/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/` (commit + push sur ce repo).
Hub parent : `/Users/Hakim/Documents/Boutiques drop/` (règles dans CLAUDE.md).

Référence UNIVERS qui fonctionne + acceptée GMC : https://www.mille-et-une-nuisette.com
→ Profondeur catalogue (~777 SKU chez eux), homepage en blocs de catégories, sous-collections d’intention, aspect boutique thématique tenue — pas landing one-product.
Notre catalogue actuel = **121 SKU** (plus léger) : même logique d’univers (collections matières fortes + homepage en blocs), profondeur à élargir plus tard.

## Identité légale (figée)

- Éditeur : OH Ventures SASU, capital 1 000 € (même entité qu’Orysbain)
- Siège : 47 rue Vivienne, 75002 Paris
- SIRET : 10315725100010 | TVA : FR55103157251
- Email : contact@lumierematiere.fr | Tél : +33 7 56 82 80 94
- Médiateur : CM2C, 14 rue Saint Jean 75017 Paris, 01 89 47 00 14, https://www.cm2c.net/ (vérifier couverture lumierematiere.fr)
- **Formulation** des pages légales = distincte d’Orysbain (faits légaux communs, texte différent — règle GMC)

## Chiffres opérationnels (ne pas contredire)

| Élément | Valeur |
|---|---|
| Prix typiques | ~149–299 € (ads souvent ~199 €) |
| Cut-off | 16h00 Paris |
| Traitement | 1–2 j ouvrés |
| Transit | 6–15 j ouvrés (mix CN/UE) |
| Total | 7–17 j ouvrés |
| Livraison | Gratuite FR métro, sans seuil |
| Retours | 30 j (+ rétractation 14 j) |
| SAV | lun–ven 10h–18h Paris |

Préférer variantes entrepôt UE au mapping DSers quand dispo.

## DA / branding

- Positionnement : « galerie de matières » — matière → qualité de lumière
- Couleurs : fond papier `#F6F3EC` · ambre `#C08A2D` · charbon `#24211B`
- Lumière produit : blanc chaud
- Doc : `catalogues/2026-08-20-branding-audit-orysbain-lumiere-matiere.md` (section Lumière Matière)
- VOC / personas Camille & Nina + objections : `catalogues/2026-08-20-voc-personas-objections-orysbain-lm.md`

## Collections (CSV)

Lustres cristal · Lustres anneau · Lustres salon · Lustres statement · Suspensions rotin · Suspensions bambou · Suspensions bois · Suspensions pierre · Suspensions verre · Suspensions métal · Suspensions déco · Plafonniers

## Fichiers catalogue (prêts)

Racine marque : `boutique-pipeline/catalogues/lumierematiere/`

| Fichier / dossier | Contenu |
|---|---|
| `catalogue-dsers.csv` | 121 SKU (import DSers) |
| `CATALOGUE-DSERS.md` | Doc catalogue |
| `descriptions/*.html` | 121 fiches HTML (matière-first, VOC, purgées AE/DSers) |
| `pages/` | notre-histoire, faq, retours, livraison, confidentialité, CGV, conditions-paiement + INDEX.md |
| `sources-fournisseur/<supplier_id>/` | Galeries AE brutes (gitignoré) — 121/121, ~722 images |
| `sources-par-handle/<handle>/` | Symlinks vers sources (gitignoré) — utiliser ça pour lire |
| `sources-fournisseur/MANIFESTE.json` | Manifeste téléchargement |

## Visuels Codex (EN COURS)

Brief mission : `catalogues/BRIEF-VISUELS-CODEX-LUMIERE-MATIERE.md`

Sortie attendue (gitignorée) :
```
catalogues/lumierematiere/livraisons-visuels-codex/
  brand/          # logos, home, 12 covers collections
  produits/<handle>/<handle>-g1.jpg … -g5.jpg + manifeste.json
  INDEX-LIVRAISON.md
```

Slots PDP : g1 hero allumé · g2 silhouette matière · g3 macro · g4 lifestyle · g5 qualité de lumière.
Format : JPEG sRGB 2048×2048 (sauf logos PNG). Volume ordre de grandeur ~624 fichiers.

Déjà présents au 21/08 (brand partiel, PDP / covers pas finis) :
- `livraisons-visuels-codex/brand/lumierematiere-logo-primary-charbon.png`
- `…/lumierematiere-logo-inverse-blanc.png`
- `…/lumierematiere-logo-mono-ambre.png`
- `…/lumierematiere-favicon-512.png`
- `…/lumierematiere-home-hero.jpg`
(encore manquants brand : home-matiere, home-table, 12 collection covers — + les 121×5 PDP)

Ne pas relancer une génération en doublon : d’abord inventaire `livraisons-visuels-codex/`, croiser avec le BRIEF.

## État d’avancement

FAIT :
- Catalogue 121 SKU + URLs AE uniques + HTML VOC matière-first
- Pages légales / FAQ / histoire (texte distinct Orysbain)
- Branding + VOC
- Sources AE locales 121/121
- Brief Codex + début livraisons brand
- Ref UNIVERS Mille et une Nuisette notée pour structure homepage / profondeur

PAS FAIT :
- Achat domaines
- Création Shopify + thème UNIVERS (blocs catégories / matières, pas one-product)
- Coller pages policies
- Import DSers / mapping variantes (privilégier UE)
- Upload images (quand Codex termine)
- GMC / Google Ads
- Vérifier adhésion CM2C pour lumierematiere.fr
- Élargissement catalogue type ref (~profondeur) — plus tard

## Ta mission dans ce chat

1. Faire un inventaire à jour de `lumierematiere/livraisons-visuels-codex/` (Codex déjà livré vs BRIEF).
2. Ne travailler QUE Lumière Matière.
3. Garder l’esprit UNIVERS (collections matières, homepage en blocs) — inspiré Mille et une Nuisette, DA propre LM.
4. Demande-moi la priorité si ambigu (thème, QA visuels, import, GMC…).
5. Toute modif durable → commit + push dans `boutique-pipeline` (ne pas committer les JPEG sources/livraisons gitignorés sauf changement explicite de politique).

Réponds d’abord par un point d’étape court : prêt / en cours / bloqué, puis propose la prochaine action concrète.
```

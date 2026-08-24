# Prompt à coller — nouveau chat Lumière Matière

> Copier tout le bloc ci-dessous dans un nouveau chat Cursor.

---

```
Tu travailles sur LUMIÈRE MATIÈRE uniquement (pas Orysbain).

## Contexte

Boutique France dropshipping OH Ventures — mode **UNIVERS** : lustres & suspensions, organisée par **matière**.
Domaine retenu (24/08) : **lumierematiere.fr** (racheté, Workspace en cours). Le `.com` existe aussi, identité boutique = `.fr`. Shopify pas encore créé.
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

## Collections (CSV — 13, pas 12)

Lustres cristal (7) · Lustres anneau (12) · Lustres salon (12) · Lustres statement (**1**) · Suspensions rotin (14) · Suspensions bambou (16) · Suspensions bois (12) · Suspensions pierre (10) · Suspensions verre (10) · Suspensions métal (8) · Suspensions déco (8) · Plafonniers (10) · **Suspensions modernes (1)** — hors tableau du brief visuels, présente dans le CSV + cover Codex.

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

## Visuels Codex (COMPLET le 21/08/2026)

Brief : `catalogues/BRIEF-VISUELS-CODEX-LUMIERE-MATIERE.md`  
Inventaire versionné : `catalogues/2026-08-21-inventaire-visuels-lumiere-matiere.md`  
Livraison (gitignorée) : `catalogues/lumierematiere/livraisons-visuels-codex/`

| Bloc | Disque |
|---|---|
| Logos / favicon | 4 PNG |
| Homepage | 3 JPEG (hero, matière, table) |
| Covers | **13** (12 slugs brief + `suspensions-modernes`) |
| PDP | **121/121** handles, **605/605** JPEG g1–g5, 2048×2048 RGB |
| Manifestes | 121 `manifeste.json` + `manifeste-brand.json` |

**Ne pas relancer de génération en doublon.** QA 21/08 : `catalogues/2026-08-21-qa-visuels-lumiere-matiere.md` (53 KEEP / 9 RETOUCH / 5 REJECT = LM-086 entier). Spec homepage UNIVERS : `catalogues/2026-08-21-spec-homepage-univers-lumiere-matiere.md`.

## État d’avancement

FAIT :
- Catalogue 121 SKU + URLs AE uniques + HTML VOC matière-first
- Pages légales / FAQ / histoire / contact (texte distinct Orysbain)
- Branding + VOC
- Sources AE locales 121/121
- Brief Codex + **livraison visuels complète** (brand + 13 covers + 605 PDP)
- Inventaire visuels 21/08 + **QA échantillon** (covers, homepage, 21 SKU)
- **Spec homepage UNIVERS** Horizon (6 tuiles matières + 3 pièce/forme, copy collable)
- Ref UNIVERS Mille et une Nuisette notée pour structure homepage / profondeur

PAS FAIT :
- Domaine `.fr` + Workspace : en cours. Création Shopify (Hakim)
- Coller pages policies + monter le thème selon la spec
- Import DSers / mapping variantes (privilégier UE) — **exclure les 5 JPEG LM-086**
- Upload images KEEP (+ RETOUCH day one)
- Retouches visuelles ciblées (covers salon/plafonniers/bois/verre/métal, home-table, LM-034) — pas de regen 605
- GMC / Google Ads
- Vérifier adhésion CM2C pour lumierematiere.fr
- Élargissement catalogue type ref (~profondeur) — plus tard

## Ta mission dans ce chat

1. Ne travailler QUE Lumière Matière.
2. Visuels Codex = livrés ; QA faite. Ne pas régénérer en masse. Retouches ciblées seulement si Hakim le demande (voir QA : LM-086 REJECT, 9 RETOUCH).
3. Spec homepage UNIVERS écrite : coller sur Horizon **après** création boutique. Ne pas improviser une landing one-product.
4. Prochaine balle dans le camp Hakim : domaines + boutique Shopify. Ensuite : import DSers (hors LM-086 images) + montage spec.
5. Toute modif durable → commit + push dans `boutique-pipeline` (ne pas committer les JPEG sources/livraisons gitignorés sauf changement explicite de politique).

Réponds d’abord par un point d’étape court : prêt / en cours / bloqué, puis propose la prochaine action concrète.
```

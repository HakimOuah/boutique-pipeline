# Inventaire visuels Codex — Lumière Matière

**Date :** 21/08/2026  
**Périmètre :** `catalogues/lumierematiere/livraisons-visuels-codex/` croisé avec `BRIEF-VISUELS-CODEX-LUMIERE-MATIERE.md` et `catalogue-dsers.csv`.  
**Dossier livraisons :** gitignoré (JPEG + INDEX locaux). Ce fichier est la copie versionnée du constat.

**Verdict fichiers :** **complet vs brief.** Ne pas relancer de génération en doublon.

---

## Totaux

| Bloc | Brief | Disque | Écart |
|---|---:|---:|---|
| Logos / favicon PNG | 4 | 4 | — |
| Homepage JPEG | 3 | 3 | — |
| Covers collections | 12 (tableau brief) | **13** | +1 volontaire (13e collection CSV) |
| Handles PDP | 121 | 121 | handles CSV = dossiers, 0 orphelin |
| JPEG produit g1–g5 | 605 | 605 | 121 × 5, aucun slot manquant |
| `manifeste.json` produit | 121 | 121 | — |
| `compte-rendu.md` produit | — | 121 | hors brief, utile |
| `rejected/` | — | 0 | — |
| **Total images** | ~624 | **625** (4 PNG + 16 JPEG brand + 605 PDP) | — |

Tech PDP (605 JPEG) : RGB, **2048 × 2048**, JPEG, poids 300 853–1 158 146 o (bande brief 300 Ko–1,2 Mo).  
Homepage : 2048 × 2048 (brief autorisait 2400 × 1600 pour le hero ; 1:1 livré).  
Logos PNG : primary 2000 × 620.

`INDEX-LIVRAISON.md` local (gitignoré) date du 21/08 : « livraison catalogue complète », 0 blocage.

---

## Brand présent

- `lumierematiere-logo-primary-charbon.png`
- `lumierematiere-logo-inverse-blanc.png`
- `lumierematiere-logo-mono-ambre.png`
- `lumierematiere-favicon-512.png`
- `lumierematiere-home-hero.jpg`
- `lumierematiere-home-matiere.jpg`
- `lumierematiere-home-table.jpg`
- `manifeste-brand.json` (`status: brand-complet`)

### Covers (13)

Les 12 slugs du brief **plus** `lumierematiere-collection-suspensions-modernes.jpg`.

Le CSV a **13 collections**, pas 12 : Codex a suivi « 1 cover par collection CSV ».

| Collection CSV | SKU | Cover |
|---|---:|---|
| Suspensions bambou | 16 | oui |
| Suspensions rotin | 14 | oui |
| Suspensions bois | 12 | oui |
| Lustres anneau | 12 | oui |
| Lustres salon | 12 | oui |
| Suspensions pierre | 10 | oui |
| Suspensions verre | 10 | oui |
| Plafonniers | 10 | oui |
| Suspensions métal | 8 | oui |
| Suspensions déco | 8 | oui |
| Lustres cristal | 7 | oui |
| Lustres statement | **1** | oui |
| Suspensions modernes | **1** | oui (hors tableau brief) |

Prix catalogue : 64 SKU à 199 € · 50 à 249 € · 6 à 299 € · 1 à 149 €.

---

## Échantillon visuel (pas une QA 605/605)

Vu le 21/08 : logos primary, 3 homepage, covers cristal / métal / modernes, g1 anneau `lustre-anneau-led-led-noir-dore-024410`, g1 rotin `suspension-rotin-469688`.

- DA papier / ambre / charbon et lumière blanc chaud : **tenue** sur l’échantillon.
- g1 packshot allumé fond papier : **conforme** au slot.
- Homepage : les 3 JPEG partent de la **même** source bambou `1005010089191307` (LM-009). Hero / matière / table racontent le même objet — trop étroit pour une homepage UNIVERS en blocs matières.
- Cover « métal » : silhouette organique translucide, lecture **matière métal** douteuse.
- Cover « modernes » : 1 SKU, look linéaire charbon — OK en visuel, collection trop mince pour un bloc homepage du même poids que bambou (16) ou rotin (14).

Méthode Codex (INDEX local) : g1 depuis source fournisseur ; **g2–g5 dérivés du g1**, pas des autres angles AE. Risque de galerie PDP trop homogène — à juger sur un lot ads 199 €, pas en relançant tout le catalogue.

---

## Ce que ça débloque / ne débloque pas

Débloqué : plus d’attente génération visuels pour uploader (quand Shopify existe).

Toujours bloqué côté boutique :

1. Achat domaines `lumierematiere.fr` / `.com` (Hakim).
2. Création Shopify + thème UNIVERS (blocs collections matières, pas one-product).
3. Coller pages `catalogues/lumierematiere/pages/`.
4. Import DSers + mapping variantes (privilégier UE).
5. Upload images (script ou glisser g1→g5).
6. GMC / Ads.
7. Vérifier adhésion CM2C pour `lumierematiere.fr`.

Élargissement catalogue type Mille et une Nuisette (~profondeur) : plus tard, pas maintenant.

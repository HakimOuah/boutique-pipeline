# Production des visuels — Lumière Matière (lustres & suspensions)

**Document de mission complet pour Codex.** Tout ce dont tu as besoin est ici.

Date : 20/08/2026  
Répertoire de travail : `/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/catalogues/`

---

## 0. Mission en trois phrases

Lumière Matière est une boutique française de **lustres et suspensions** (marque d’OH Ventures), organisée par **matière**. Le catalogue compte **121 fiches** ; les galeries AliExpress sont déjà téléchargées en local.

Ton travail : **produire des fichiers image sur le disque** (logo, homepage, covers de collections, **5 slots par fiche**), depuis les photos fournisseur, selon la DA et le nommage ci-dessous.

**Tu ne touches jamais à Shopify / DSers / Ads.** Fichiers + manifestes uniquement.

---

## 1. Sources fournisseur

```
catalogues/lumierematiere/sources-fournisseur/<supplier_id>/01.jpg …
catalogues/lumierematiere/sources-par-handle/<handle>  →  symlink
catalogues/lumierematiere/sources-fournisseur/MANIFESTE.json
catalogues/lumierematiere/catalogue-dsers.csv
```

- **121 / 121** produits OK (20/08/2026) — ouvrir via `sources-par-handle/<handle>/`.
- **Aucune génération sans source locale.** Si un dossier manque : signaler dans `INDEX-LIVRAISON.md`, ne pas inventer.

---

## 2. Cinq règles non négociables

1. **Partir de la photo fournisseur** — forme, Ø apparent, matière, couleur, type (anneau / rotin / verre…). Pas d’invention de produit.
2. **Jamais livrer une brute AE** (fond blanc marketplace, watermark, main, décor vendeur).
3. **Aucun texte / badge / étoile / promo / cote incrustés.** Pas de faux « cristal » étincelant Disney si la source est verre / acrylique.
4. **Aucun visage.** Lifestyle table / salon OK sans personne.
5. **JPEG sRGB 2048×2048**, 1:1, ~300 Ko–1,2 Mo (hero homepage peut être 2400×1600).

---

## 3. DA — « galerie de matières »

| Élément | Valeur |
|---|---|
| Fond studio | papier `#F6F3EC` |
| Accent | ambre `#C08A2D` (halo / lumière, pas flashy) |
| Texte | charbon `#24211B` |
| Lumière produit | **blanc chaud** (ambiance accueillante) |
| Interdit | purple IA, cream+terracotta cliché, ampoule cartoon, dark neon |

Promesse visuelle : **matière → qualité de lumière**.

---

## 4. Livrables brand

Dossier : `lumierematiere/livraisons-visuels-codex/brand/`

| Fichier | Contenu |
|---|---|
| `lumierematiere-logo-primary-charbon.png` | Câble vertical + cercle (globe) + halo ambre + wordmark |
| `lumierematiere-logo-inverse-blanc.png` | Version claire |
| `lumierematiere-logo-mono-ambre.png` | 1 couleur |
| `lumierematiere-favicon-512.png` | Monogramme seul |
| `lumierematiere-home-hero.jpg` | Full-bleed lustre / suspension **allumé**, matière lisible |
| `lumierematiere-home-matiere.jpg` | Macro matière (rotin ou verre) |
| `lumierematiere-home-table.jpg` | Suspension au-dessus d’une table (échelle crédible) |

### Covers collections (1 par collection CSV)

Préfixe : `lumierematiere-collection-<slug>.jpg`

| Collection CSV | slug fichier |
|---|---|
| Lustres cristal | `lustres-cristal` |
| Lustres anneau | `lustres-anneau` |
| Lustres salon | `lustres-salon` |
| Lustres statement | `lustres-statement` |
| Suspensions rotin | `suspensions-rotin` |
| Suspensions bambou | `suspensions-bambou` |
| Suspensions bois | `suspensions-bois` |
| Suspensions pierre | `suspensions-pierre` |
| Suspensions verre | `suspensions-verre` |
| Suspensions métal | `suspensions-metal` |
| Suspensions déco | `suspensions-deco` |
| Plafonniers | `plafonniers` |

Exemple : `lumierematiere-collection-suspensions-rotin.jpg`

---

## 5. Fiches produit — 5 slots / handle (121)

| Slot | Fichier | Intention |
|---|---|---|
| g1 | `<handle>-g1.jpg` | **Hero packshot allumé**, fond `#F6F3EC` |
| g2 | `<handle>-g2.jpg` | **Silhouette / angle matière** |
| g3 | `<handle>-g3.jpg` | **Macro matière** (tressage, facettes, grain) |
| g4 | `<handle>-g4.jpg` | **Lifestyle** table ou salon, Ø crédible |
| g5 | `<handle>-g5.jpg` | **Qualité de lumière** — halo / ombres sur surface |

Source : `sources-par-handle/<handle>/01.jpg` (meilleure face) ; autres files pour angles.

---

## 6. Nommage et rangement FIGÉS

```
catalogues/lumierematiere/livraisons-visuels-codex/
  brand/
    lumierematiere-logo-*.png
    lumierematiere-favicon-512.png
    lumierematiere-home-*.jpg
    lumierematiere-collection-*.jpg
    manifeste-brand.json
  produits/
    <handle>/
      <handle>-g1.jpg … <handle>-g5.jpg
      manifeste.json
      compte-rendu.md
      rejected/
  INDEX-LIVRAISON.md
```

### Manifeste produit (exemple)

```json
{
  "brand": "lumierematiere",
  "sku": "LM-…",
  "handle": "suspension-rotin-469688",
  "collection": "Suspensions rotin",
  "supplier_id": "1005009535104055",
  "images": [
    {
      "fichier": "suspension-rotin-469688-g1.jpg",
      "slot": "g1-hero-allume",
      "source": "catalogues/lumierematiere/sources-fournisseur/1005009535104055/01.jpg"
    }
  ],
  "ecartes": []
}
```

### Règles de nom (strict)

- `handle` = **exactement** la colonne `Handle` du CSV (minuscules, tirets).
- Galerie : **uniquement** `-g1` … `-g5` (jamais `-6` / variante fantôme).
- Pas d’espaces, pas d’accents, pas de majuscules dans les noms de fichiers.
- Préfixe brand : toujours `lumierematiere-` ; collections : `lumierematiere-collection-<slug>.jpg`.

### Pourquoi cette arborescence (upload)

- **PDP Shopify** : 1 dossier `produits/<handle>/` = 1 fiche → glisser les 5 `-gN.jpg` **dans l’ordre g1→g5**.
- **Script futur** : glob `produits/*/*-g*.jpg` + `manifeste.json` → `productCreateMedia` par handle.
- **Collections** : `brand/lumierematiere-collection-*.jpg` → image de collection Shopify.
- **Thème** : logos + home uniquement dans `brand/` (jamais mélangés aux PDP).

---

## 7. Volume

| Bloc | Quantité |
|---|---:|
| Produits × 5 | **605** |
| Logos / favicon | 4 |
| Homepage | 3 |
| Collections | 12 |
| **Total ordre de grandeur** | **~624** |

Priorité si tu dois découper en lots : (1) brand + 20 SKU ads 199 €, (2) collections covers, (3) reste catalogue.

---

## 8. Checklist `done`

1. Sources locales présentes pour chaque handle traité.  
2. 5× JPEG + manifeste par handle.  
3. Fidélité matière / silhouette à la source.  
4. Brand + covers collection + `INDEX-LIVRAISON.md`.  
5. Aucune brute AE, aucun texte incrusté, aucun visage.

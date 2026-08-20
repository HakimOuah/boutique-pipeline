# Production des visuels — Orysbain (sèche-serviettes électriques)

**Document de mission complet pour Codex.** Tout ce dont tu as besoin est ici.

Date : 20/08/2026  
Répertoire de travail : `/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/catalogues/`

---

## 0. Mission en trois phrases

Orysbain est une boutique française de **sèche-serviettes électriques** (marque d’OH Ventures). Le catalogue compte **32 fiches** ; les galeries fournisseur AliExpress sont déjà téléchargées en local.

Ton travail : **produire des fichiers image sur le disque** (logo, homepage, collections, **5 slots par fiche produit**), à partir des photos fournisseur, selon la DA et la convention de nommage ci-dessous.

**Tu ne touches jamais à Shopify / DSers / Ads.** Tu livres des fichiers + manifestes. Le branchement est fait ensuite.

---

## 1. Où sont les sources (déjà téléchargées)

```
catalogues/orysbain/sources-fournisseur/<supplier_id>/01.jpg … 06.jpg (parfois plus)
catalogues/orysbain/sources-par-handle/<handle>  →  symlink vers le dossier supplier_id
catalogues/orysbain/sources-fournisseur/MANIFESTE.json
```

- **32 / 32** produits OK, **195** images sources (20/08/2026).
- Catalogue : `orysbain/catalogue-dsers.csv` (sku, handle, supplier_id, title, color, tech, price).
- Pages / DA : `orysbain/pages/` + `catalogues/2026-08-20-branding-audit-orysbain-lumiere-matiere.md`.

**Résolution sources** : typiquement 800–1200 px. Sortie imposée **2048 × 2048**. Agrandissement OK ; si une macro est illisible, écarte le slot avec motif.

---

## 2. Cinq règles non négociables

1. **Toujours partir de la photo fournisseur** (image-to-image / composition). Jamais inventer la géométrie, le nombre de barres, la finition, la couleur, le type de commande (classique / tactile / smart).
2. **Jamais livrer une photo AE brute** (fond marketplace, watermark, main du vendeur, nappe grise caractéristique). Fond / scène / lumière = maison Orysbain.
3. **Aucun logo, texte, badge, étoile, promo, cote cm incrustés** dans les pixels. Pas de logo « Orysbain » sur le produit non plus (sauf livrables logo dédiés §4).
4. **Aucun visage, doigt, corps** en lifestyle. Salle de bain réelle OK sans personne.
5. **Format** : JPEG sRGB, **2048 × 2048**, 1:1, ~300 Ko–1,2 Mo.

---

## 3. Direction artistique Orysbain — « chaleur minérale »

| Élément | Valeur |
|---|---|
| Fond studio | vapeur `#F6F4F1` |
| Accent | cuivre `#B25A28` (discret, pas saturé) |
| Texte / ombre | ardoise `#26343C` |
| Ambiance | SDB française soignée, lumière douce du matin, carrelage / pierre / bois clair — **pas** purple IA, pas cream+terracotta cliché, pas dark mode |

Le produit reste fidèle à la source ; seuls fond, lumière, cadrage et scène changent.

---

## 4. Livrables hors fiches produit

### 4.1 Logo (dossier `livraisons-visuels-codex/brand/`)

| Fichier | Contenu |
|---|---|
| `orysbain-logo-primary-ardoise.png` | Monogramme **O** + **3 barres** horizontales (échelle sèche) + wordmark `ORYSBAIN` — ardoise sur fond transparent |
| `orysbain-logo-inverse-blanc.png` | Même, blanc |
| `orysbain-logo-mono-cuivre.png` | 1 couleur cuivre |
| `orysbain-favicon-512.png` | Monogramme seul, 512×512 |

Pas de flamme, pas de serviette cartoon, pas de serif fantaisie.

### 4.2 Homepage

| Fichier | Contenu |
|---|---|
| `orysbain-home-hero.jpg` | Full-bleed SDB réelle + sèche-serviettes mural (noir mat préféré), 2400×1600 ou 2048×2048 cropable |
| `orysbain-home-benefit-serviettes.jpg` | Bénéfice : serviettes sur échelle chaude |
| `orysbain-home-detail-finition.jpg` | Gros plan finition (chrome ou noir) |

### 4.3 Collection

| Fichier | Contenu |
|---|---|
| `orysbain-collection-seche-serviettes.jpg` | Planche / ambiance gamme (plusieurs finitions possibles, ou un héros noir mat) |

---

## 5. Fiches produit — 5 slots obligatoires par handle

Pour **chaque** ligne de `catalogue-dsers.csv` (32) :

| Slot | Fichier | Intention |
|---|---|---|
| g1 | `<handle>-g1.jpg` | **Hero packshot** fond `#F6F4F1`, face avant, produit net, ombre douce |
| g2 | `<handle>-g2.jpg` | **3/4 structure** — barres / échelle lisibles |
| g3 | `<handle>-g3.jpg` | **Détail** commande (tactile / bouton) + texture finition |
| g4 | `<handle>-g4.jpg` | **Lifestyle SDB** mural, sans personne, géométrie = source |
| g5 | `<handle>-g5.jpg` | **Usage** — 1–2 serviettes sur l’échelle (bénéfice chaleur / séchage) |

Pas de slot variante séparé (1 couleur dominante déjà dans le handle). Si plusieurs coloris sur la même fiche Shopify un jour : alors `<handle>-v-<code>.jpg`.

**Source à privilégier :** `sources-par-handle/<handle>/01.jpg` pour g1 ; autres `02…` pour angles. Si `01` est mauvaise (schéma, texte), prendre la meilleure face `ok` du dossier.

---

## 6. Nommage et rangement — convention FIGÉE (pour upload facile)

### Arborescence

```
catalogues/orysbain/livraisons-visuels-codex/
  brand/
    orysbain-logo-*.png
    orysbain-favicon-512.png
    orysbain-home-*.jpg
    orysbain-collection-*.jpg
    manifeste-brand.json
  produits/
    <handle>/
      <handle>-g1.jpg
      <handle>-g2.jpg
      <handle>-g3.jpg
      <handle>-g4.jpg
      <handle>-g5.jpg
      manifeste.json
      compte-rendu.md
      rejected/          # optionnel
  INDEX-LIVRAISON.md     # totaux + checklist
```

### Règles de nom

- `handle` = **exactement** la colonne `handle` du CSV (minuscules, tirets).
- Galerie : **uniquement** `-g1` … `-g5` (jamais `-6` / `-7`).
- Pas d’espaces, pas d’accents, pas de majuscules dans les noms de fichiers.
- Prefixe brand : toujours `orysbain-`.

### `manifeste.json` (par produit)

```json
{
  "brand": "orysbain",
  "sku": "ORYS-021-TAC-NOI",
  "handle": "seche-serviette-tactile-noir-standard-174351",
  "supplier_id": "1005005855174351",
  "images": [
    {
      "fichier": "seche-serviette-tactile-noir-standard-174351-g1.jpg",
      "slot": "g1-hero-packshot",
      "source": "catalogues/orysbain/sources-fournisseur/1005005855174351/01.jpg"
    }
  ],
  "ecartes": []
}
```

Champs : `fichier`, `slot`, `source` (chemin relatif depuis `boutique-pipeline/`). Pas d’ID Shopify.

### Pourquoi cette arborescence

- Upload Shopify : un dossier = une fiche → glisser les 5 `-gN.jpg` dans l’ordre.
- Script futur : `produits/*/*-g*.jpg` + manifeste → `productCreateMedia` par handle.
- Brand séparé : assets thème / homepage sans mélanger aux PDP.

---

## 7. Liste des 32 handles

Lis `orysbain/catalogue-dsers.csv`. Une fiche sans source exploitable → **ne rien inventer** ; noter dans `ecartes` / `INDEX-LIVRAISON.md`.

---

## 8. Checklist avant `done`

1. 5 JPEG 2048×2048 par handle + manifeste.  
2. Produit fidèle à la source (barres, couleur, commande).  
3. Aucun texte / watermark / visage.  
4. Brand : logos + hero + 2 home + 1 collection + `manifeste-brand.json`.  
5. `INDEX-LIVRAISON.md` : totaux (attendu 32×5 = 160 produit + brand).

**Volume attendu produit :** 160 images. **Brand :** ~8 fichiers.

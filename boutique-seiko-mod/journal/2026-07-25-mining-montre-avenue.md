# Minage montre-avenue — ce qui est portable sur NOIRMONT

> **25/07/2026** — recherche seule, aucune modification faite ni chez eux ni chez nous.
> Complète `2026-07-25-plan-lisibilite-variantes.md` (§3, ligne « Minage montre-avenue »).

## 0. Correction préalable — le domaine

Le brief indiquait `montre-avenue.fr`. **Ce domaine n'existe pas** (NXDOMAIN sur DNS public, y compris `www`). Le site réel est :

**`https://montre-avenue.com`**

Vérifié : HTTP 200, `products.json` accessible, thème déclaré
`Shopify.theme = {"name":"FullStack 2.2 - Montre Avenue","schema_name":"FullStack","schema_version":"2.2.0","theme_store_id":null,"role":"main"}`

→ **Même thème que nous, même version majeure (FullStack 2.2).** L'hypothèse de portabilité est confirmée : tout ce qui suit est du réglage, pas du portage de code.

Un détail à corriger partout où le domaine est noté (plan, Notion, briefs d'agents).

---

## 1. Le sélecteur de variantes — priorité absolue

### 1.1 Ce qu'ils font

Trois rendus coexistent, et **le thème choisit tout seul** :

| Rendu | Quand | Exemple |
|---|---|---|
| **Pastilles image** (cercles, souvent bicolores) | la valeur d'option porte un *swatch image* | `montre-sport-homme-style-racing-cadran-sport-et-style-agressif` — 8 coloris |
| **Pastilles couleur** (aplat uni) | la valeur porte un *swatch couleur* | `etui-montre-daim-voyage` — 5 coloris, `rgb(154 86 48)`, `rgb(234 216 171)`… |
| **Boutons texte** (repli) | la valeur n'a **aucun** swatch | `montre-vintage-femme-jonc-ajoure-cadran-rectangulaire` — « Argenté · Cadran Blanc »… |

Produit mono-variante (`etui-montre-voyage-cuir-vintage`) : **le bloc `<variant-picker>` n'est pas rendu du tout**. Pas de « Default Title » affiché. Comportement natif.

**Le point capital** : le rendu pastille **n'est pas un réglage de thème**. C'est une conséquence automatique de la donnée Shopify. Le thème regarde si la valeur d'option a un swatch ; si oui → pastille, si non → bouton texte. C'est exactement notre situation actuelle : nos `M14` / `WB33` s'affichent en boutons texte **parce que nos valeurs d'option n'ont pas de swatch**, pas parce qu'un réglage serait désactivé.

Noter aussi : **eux non plus n'ont pas tout fait**. Leur produit le plus récent (`montre-vintage-femme-jonc-ajoure…`, id produit 8510051451074) est encore en boutons texte — et il utilise le **même séparateur `·` que nous** (« Argenté · Cadran Blanc »). Le `·` n'est donc pas le problème : c'est la pastille manquante. Un libellé `Rouge · 4 montres` est parfaitement lisible ; c'est le suffixe `· C` qui pollue, et l'absence de visuel qui tue.

### 1.2 Comment c'est fait techniquement

**Le DOM du picker :**

```html
<variant-picker data-product-url="/products/…">
  <input type="hidden" name="id" value="45219543122114">
  <div class="variant-picker__options">
    <fieldset class="variant-picker__option">
      <div class="variant-picker__option-name variant_label"><span>Couleur :</span></div>
      <div class="variant-picker__option-values">
        <div class="swatches">
          <input class="swatch-input" type="radio" name="option-Couleur"
                 id="option-Couleur-Noir et Rouge" value="Noir et Rouge"
                 data-option-value-id="2402628960450"      <!-- ← clé de tout -->
                 data-variant-id="45219543122114" checked>
          <label class="swatch" for="option-Couleur-Noir et Rouge">
            <span style="--swatch-background: url(//…/cdn/shop/files/noir-rouge.jpg?width=100);;"></span>
          </label>
          …
```

Le repli texte, lui, produit `<div class="variant-picker__option-value">` + `<label>` portant le libellé brut. Même `data-option-value-id`, même JS — seule la présentation diffère.

- `data-option-value-id` = l'ID de **valeur d'option Shopify** (pas la variante). C'est la fonctionnalité native Shopify « swatches de valeurs d'option ».
- `--swatch-background` reçoit soit `url(…)` (image), soit `rgb(…)` (couleur). Le `;;` en fin est un artefact de concaténation Liquid, sans importance.
- Les images de pastille sont des **fichiers uploadés dans Shopify Files** : `/cdn/shop/files/noir-rouge.jpg`, `/cdn/shop/files/pastille-noir.jpg` (le nom « pastille » est explicite). Format constaté : **JPG 156 × 156 px, 0,6 à 1,7 Ko**. Une image par combinaison de couleurs, réutilisée entre produits.

**Le changement d'image au clic — mécanisme exact** (`assets/variant-picker.js` + `assets/product-media-gallery.js`) :

1. `<variant-picker>` écoute `change`.
2. Il construit `"/products/<handle>?option_values=<id1>,<id2>"` et **refetch la page entière** (`fetch`, avec `AbortController` pour annuler un clic précédent).
3. Il remplace son propre `innerHTML` par le `<variant-picker>` de la réponse, puis émet `VariantUpdatedEvent` en y joignant le **DOM complet** de la réponse.
4. `<product-media-gallery>` écoute `variantUpdated` sur sa `.shopify-section`, extrait `product-media-gallery slider-component` du DOM reçu et fait un **`replaceWith()` de toute la galerie**.
5. `history.replaceState` pose `?variant=<id>` dans l'URL.

**Ce n'est donc ni un scroll ni un saut vers une image.** La galerie est **re-rendue côté serveur** : l'image de la variante devient la position 1 et le reste suit dans l'ordre d'origine. Vérifié en direct sur le produit racing :

| | galerie |
|---|---|
| avant (Noir et Rouge) | `…Sport.webp`, `…Sport_23.webp`, `…Sport_8.webp`, `…Sport_9.webp` |
| après clic « Noir et Vert » | **`…Sport_6.webp`**, `…Sport.webp`, `…Sport_23.webp`, `…Sport_8.webp` |

Le prix, l'`<input name="id">` caché, le sticky ATC et l'URL se mettent à jour dans le même cycle.

**Conséquence pour nous, à ne pas rater** : ce comportement suppose que **chaque variante ait une image assignée** (`featured_media`). Sans ça, le refetch renvoie la même galerie et le clic ne produit rien de visible — même avec de belles pastilles.

### 1.3 Les pastilles sur les cartes de collection

Même dispositif, décliné en `<product-card-swatches>` (`assets/product-card-swatches.js`), classes `swatches swatches--small swatches--rounded`. Chaque pastille est un `<span role="button" data-href="/products/…?variant=…">` — donc un lien vers la variante, pas un changement in-place.

Sur `/collections/montre-homme` : **24 cartes sur 24 portent des pastilles**, 4 à 7 chacune. Alimenté par la même donnée que la fiche — le travail est fait une fois, il sert aux deux endroits.

### 1.4 Taux de couverture chez eux

Échantillon aléatoire de 16 produits multi-variantes :

- **10** pastilles image
- **5** pastilles couleur
- **1** repli texte (`remontoir-pour-montre-automatique` — valeurs non chromatiques)

→ **94 % de couverture.** C'est un chantier qu'ils ont mené systématiquement, pas un cas isolé.

### 1.5 Ce qu'on porte chez nous

**Verdict : donnée Shopify, pas de développement, pas de réglage de thème.** Notre thème sait déjà tout faire.

Trois gestes, dans cet ordre :

1. **Renommer les valeurs d'option** en libellés clients (déjà cadré §2 du plan, agent de renommage). Sans ça les pastilles seront jolies mais l'infobulle et le panier resteront illisibles.
2. **Attacher un swatch à chaque valeur** — couleur unie quand la couleur suffit, image 156 × 156 quand le choix est visuel (cadran, matière, bicolore). Via l'API Admin `productOptionUpdate`, en passant `optionValues: [{ id, swatch: { color } | { mediaId } }]`. Notre MCP Shopify le permet.
3. **Assigner une image de produit à chaque variante** — sinon le clic ne change rien.

Règle de choix reprise d'eux, cohérente avec §2 du plan : image quand le choix est visuel, couleur quand c'est une couleur, **rien** quand c'est une dimension (nos loupes `4,0 mm` / `5,5 mm` doivent rester en boutons texte — le repli est le bon rendu, pas un défaut).

Piège à éviter : nos SKU portent le mapping DSers. On ne touche qu'aux **valeurs d'option**, jamais aux SKU (§4 du plan).

---

## 2. Le bloc de vente croisée « Obtenez 30 % de réduction sur un étui »

### 2.1 Ce qu'ils font

Encart placé **entre le sélecteur de variantes et le bouton Ajouter au panier** — donc à l'endroit de la décision, pas en bas de page. Une phrase d'accroche, puis 1 à N accessoires, chacun avec vignette, titre cliquable, prix, un `<select>` de coloris et une **case à cocher**. Ce qui est coché part au panier **avec le même clic « Ajouter au panier »** que la montre.

Sur le produit racing : « Étui pour montre Daim de Voyage » 30,90 € (5 coloris) + « Étui pour montre de voyage Cuir 2 Compartiments » 39,90 € (4 coloris).

### 2.2 Comment c'est fait techniquement

**Bloc natif FullStack — aucune application tierce.** Éléments `<toggle-cross-sell-list>` / `<toggle-cross-sell>`, script `assets/toggle-cross-sell.js` servi par le CDN du thème.

Preuve par les scripts : sur toute la fiche produit, **le seul script tiers est Klaviyo** (`static.klaviyo.com/onsite/js/U7nLmL/klaviyo.js`). Tout le reste est `montre-avenue.com/cdn/shop/t/9/assets/*` ou Shopify. Liste complète des assets du thème sur une PDP : `utilities, events, header, splide, slider, toast-notification, accordion, quantity-selector, dropdown, popup, loader, localization-form, predictive-search, cart-icon, cart-drawer, cross-sell, cart-discount, product-media-gallery, product-price, product-form, variant-picker, toggle-cross-sell, sticky-add-to-cart, product-card, quick-add, product-recommendations`.

Logique du JS :
- Deux modes de sélection au choix (réglage du bloc) : **case à cocher** (`toggle-cross-sell-checkbox`) ou **bouton « Ajouter »** qui bascule en `.button--active`. Ils ont retenu la case à cocher.
- Changer le `<select>` déclenche `variantChanged()` → met à jour prix, vignette (`data-variant-image`), `data-variant-id`, **et coche automatiquement la case**. Bonne micro-décision : choisir une couleur vaut acceptation.
- `getSelectedItems()` renvoie `[{id, quantity: 1}]` agrégé, consommé par `<product-form>` à la soumission.

**Point de vigilance** : le bloc **n'applique aucune remise**. Le prix affiché est le prix plein (30,90 € = exactement le prix catalogue de l'étui, aucun `compare_at_price`). Les « 30 % » ne sont qu'un texte libre. Pour que la promesse soit tenue il faut une **remise automatique Shopify** (type « achetez X, obtenez Y à −30 % ») configurée à côté. Non vérifiable de l'extérieur sans passer commande — je ne l'ai pas fait.

### 2.3 Ce qu'on porte

**Bloc à ajouter dans le thème (theme editor), zéro développement.** Notre FullStack 2.2 embarque le même `toggle-cross-sell`.

À faire : ajouter le bloc dans le template produit sous le variant picker, y accrocher nos accessoires (rouleau de voyage, remontoir, bracelets), et — si on annonce une remise — **créer la remise automatique correspondante**. Sinon on écrit une accroche sans chiffre. Cohérent avec la règle « promesses vérifiables » : ne pas annoncer −30 % si la remise n'existe pas dans Shopify.

---

## 3. Les badges d'attributs sous le titre

### 3.1 Ce qu'ils font

Juste sous le H1, une rangée de pastilles grises arrondies. Sur le produit racing : « Grand cadran de 46 mm », « Mouvement à quartz », « Aiguilles lumineuses », « Étanchéité 3 ATM ». Quatre faits techniques, courts, vérifiables, avant même le prix.

### 3.2 Comment c'est fait

**Un métachamp de type `list.single_line_text_field`**, affiché par un simple **bloc Texte** du thème dont le contenu est branché sur ce métachamp via la source dynamique de l'éditeur. Shopify rend nativement une liste en :

```html
<ul class="metafield-single_line_text_field-array">
  <li class="metafield-single_line_text_field">Grand cadran de 46 mm</li>
  …
</ul>
```

Le look « pastille » vient ensuite de **~11 lignes de CSS personnalisé**, injectées dans le champ *Custom CSS* de la section (portée automatique `#shopify-section-template--…__main`) :

```css
.metafield-single_line_text_field-array { list-style: none; padding: 0; display: flex; gap: .5rem; flex-wrap: wrap; }
.metafield-single_line_text_field-array li {
  background-color: rgb(243,243,243);
  padding: 0 10px 1px;
  border-radius: 25px;
  font-size: .9rem;
  line-height: 1.6rem;
  font-weight: 300;
  white-space: nowrap;
  color: rgb(105,105,105) !important;
}
```

Ni tags, ni saisie manuelle, ni application.

### 3.3 Ce qu'on porte

**Métachamp + bloc de thème + CSS de section.** Effort quasi nul côté thème ; le vrai coût est le remplissage éditorial (3–4 attributs × nos fiches).

C'est aussi un excellent véhicule pour notre positionnement « explicable au particulier » : mettre des faits qu'un non-initié comprend (« Verre saphir », « Mouvement automatique », « Étanche 10 ATM ») plutôt que du jargon d'horloger.

---

## 4. Structure et navigation

**Bandeau promo** : section `announcement_bar` dans le `header-group`, texte simple « - 10 % avec le code MONTRE10 », `color-scheme-3`, carrousel Splide (un seul message ici). **Le même message est répété en tête de fiche produit**, avec une icône réveil, juste au-dessus du H1 — piqûre de rappel au moment du choix. Malin et gratuit.

**Fil d'Ariane** : section dédiée dans son propre groupe (`sections--…__breadcrumbs`), rendue **entre le header et le contenu, sur toutes les pages**. Format PDP : `Accueil / Toutes nos montres / Montre Chronographe / <titre>`. Format collection : `Accueil / Homme / Montre Homme`.

**Méga-menu** : cinq entrées — *Toutes nos montres · Homme · Femme · Enfant · Accessoires*. Derrière, **une architecture SEO pure : ~57 collections**, chacune calquée sur une requête exacte.

- *Toutes nos montres* (15) : par type — automatique, en bois, chronographe, connectée, de luxe, de sport, digitale, militaire, solaire, squelette, vintage, à gousset, à quartz, mécanique, en cuir.
- *Homme* (14) / *Femme* (13) : le **produit cartésien type × genre** — « Montre automatique homme », « Montre Chronographe Femme »…
- *Enfant* (8) : bascule sur l'intention et l'âge — « Montre enfant 3 ans », « Montre enfant 5 ans », « Montre gps enfant », « Montre enfant garcon/fille ».
- *Accessoires* (5) : boîtes, étuis, remontoirs, bracelets.

**Sélecteur de devise** : `<localization-form-component>` avec drapeau français, mais **une seule devise proposée (EUR)**. C'est donc un signal de confiance décoratif, pas une vraie fonction multi-devise.

**Page collection** : titre + **texte SEO tronqué avec un « Voir plus »** (le texte est là pour Google, replié pour l'humain), puis une **rangée de liens-pastilles vers les collections sœurs, avec vignette** (Tous les produits / Montres homme / Montres femme / Montres enfant / Accessoires), puis grille + filtres latéraux (Trier par, Prix).

**Ce qu'on porte** : le rappel du code promo en tête de fiche (5 min), le fil d'Ariane global (réglage), les liens-pastilles inter-collections (bloc + vignettes). L'architecture à 57 collections est un chantier SEO à part entière — à instruire séparément, mais le modèle « type × genre » est directement transposable à « type × usage » chez nous.

---

## 5. Anatomie de la fiche produit

Ordre exact, de haut en bas :

1. Bandeau promo (`announcement_bar`)
2. Header collant (`--header-height: 65px`)
3. **Fil d'Ariane**
4. Section principale — colonne gauche : galerie `<product-media-gallery>` (slider Splide) ; colonne droite :
   1. rappel promo avec icône réveil — « - 10 % avec le code MONTRE10 »
   2. **H1** (Merriweather serif)
   3. **badges d'attributs** (§3)
   4. **prix** `<product-price>`
   5. **sélecteur de variantes** — « Couleur : » + pastilles (§1)
   6. **vente croisée** (§2)
   7. sélecteur de quantité + **Ajouter au panier** (avec rappel du prix)
   8. **accordéons** : *Description* · *Caractéristiques* · *Livraison et retour* · *Boite Premium (Offerte)* (avec icône cadeau)
5. Sections narratives libres (5 blocs) : « Puissance Sportive & Confort Haute Performance », « Un Cadran Taillé pour l'Action », « Prête pour le Quotidien », « Coffret cadeau offert », « Besoin d'aide ? »
6. **FAQ** en accordéon, **spécifique au produit** (« Cette montre est-elle adaptée au sport ? », « Puis-je la porter sous la pluie ? »…)
7. **Avis clients** — **Judge.me** (`jdgm`, 168 occurrences). Ici : *« Soyez le premier à écrire un avis »* → **zéro avis affiché**
8. `<product-recommendations>`
9. Capture email — « Économisez 10 % sur votre première commande »
10. Footer

**Sticky add-to-cart** (`<sticky-add-to-cart data-active="false">`) présent, réplique l'`input name="id"` et le prix.

**Réassurance** : coffret offert (accordéon dédié + section illustrée), horaires du support en clair (« Lundi au Vendredi 8h30–19h, Samedi 10h–17h »), téléphone et email en pied de page, FAQ par produit, mentions légales complètes.

**Preuve sociale** : faible. Judge.me installé mais vide sur les fiches vues, baseline « Passionné depuis 2022 » sous le logo. C'est leur point faible — et un endroit où nous pouvons faire mieux (cf. la recette d'import d'avis Trustoo déjà en mémoire).

**Urgence** : **aucune.** Pas de compte à rebours, pas de stock résiduel, pas de « X personnes regardent ». Le seul levier est le code promo permanent. À noter : c'est un concurrent direct qui vend sans artifice d'urgence.

**Typographie** : `--font-heading--family: Merriweather, serif` · `--font-body--family: "Instrument Sans", sans-serif`.

---

## 6. Le catalogue en un coup d'œil

`https://montre-avenue.com/products.json?limit=250` puis `&page=2`.

- **364 produits publiés**, vendor unique « Montre Avenue ».
- **Prix : 14,90 € à 354,90 €**, **médiane 59,90 €**, quartiles 39,90 € / 69,90 €. Fourchette et médiane très proches des nôtres → concurrent direct confirmé.
- Familles principales : chronographe homme (20), montre à gousset (19), vintage femme (16), quartz femme (15), bracelets (13), quartz homme (13), connectées (12), squelette homme (12), luxe femme (10), cuir homme (10), étuis (10)… plus boîtes à montre et remontoirs.
- **Noms d'options**, sur 364 produits : `Couleur` (229), `Title` (80, mono-variante), `Couleur du bracelet` (37), `Couleur du cadran` (9), `Couleur du boîtier` (6). Résidus non nettoyés : `Color` (1, anglais), `Couleur du bracelet ` (1, espace final), `Couleurs` (1). **Ils vivent très bien avec ~1 % de scories** — utile à savoir avant de viser la perfection sur notre propre passe.
- **Valeurs d'options** : français client systématique — « Noir et Rouge », « Or Rose et Bleu », « Argenté · Cadran Blanc », « Marron », « Beige ». Zéro code fournisseur visible. Les codes existent bien, mais **restent dans le SKU** (`"sku": "14:201447598#912 Black Red"`) — exactement la discipline que le §4 de notre plan impose.

---

## 7. Liste priorisée — les 5 chantiers à porter en premier

| # | Chantier | Nature | Effort | Pourquoi en premier |
|---|---|---|---|---|
| **1** | **Swatches sur les valeurs d'option** — couleur unie ou image 156×156, via `productOptionUpdate` | **Donnée Shopify** (API/MCP), 0 dev, 0 réglage de thème | **M** — 2–3 h d'API une fois les libellés arrêtés ; le coût réel est la production des pastilles image | C'est *tout* le sujet des pastilles. Le thème est déjà prêt : il attend la donnée. Enchaîne directement derrière l'agent de renommage |
| **2** | **Image assignée à chaque variante** | **Donnée Shopify** | **M** — dépend du budget Higgsfield (§5 du plan, ~43 visuels ≈ 230 crédits) | Sans ça le clic sur une pastille ne change **rien** à l'écran. Inutile de faire 1 sans 2 |
| **3** | **Badges d'attributs sous le titre** — métachamp `list.single_line_text_field` + bloc Texte + 11 lignes de CSS | **Réglage de thème** + saisie éditoriale | **S** — 30 min de mise en place, puis 3–4 attributs par fiche | Meilleur rapport effet/effort du document. Sert directement le positionnement « explicable au particulier » |
| **4** | **Bloc de vente croisée sous le picker** | **Bloc natif FullStack** à ajouter | **S** — 1 h. **+1 h** si on annonce une remise (créer la remise automatique Shopify) | Panier moyen, au point de décision. Nos accessoires sont déjà sourcés |
| **5** | **Rappel du code promo en tête de fiche + fil d'Ariane global** | **Réglage de thème** | **XS** — < 30 min les deux | Gratuit, immédiat, aucun risque |

**Hors top 5, à instruire séparément** : l'architecture à ~57 collections SEO (chantier lourd mais c'est visiblement leur moteur d'acquisition organique), et le remplissage des avis Judge.me/Trustoo — où ils sont à zéro et où nous pouvons prendre un avantage net.

---

## 8. Références vérifiables

| Objet | URL |
|---|---|
| Pastilles image, 8 coloris, cross-sell 2 produits | `/products/montre-sport-homme-style-racing-cadran-sport-et-style-agressif` |
| Pastilles couleur unie, 5 coloris | `/products/etui-montre-daim-voyage` |
| Mono-variante — picker absent | `/products/etui-montre-voyage-cuir-vintage` |
| Repli boutons texte (pas de swatch) | `/products/montre-vintage-femme-jonc-ajoure-cadran-rectangulaire` |
| Pastilles sur cartes, intro SEO repliée, liens-pastilles sœurs | `/collections/montre-homme` |
| Catalogue complet | `/products.json?limit=250` puis `&page=2` |
| JS du picker / galerie / cross-sell | `/cdn/shop/t/9/assets/{variant-picker,product-media-gallery,toggle-cross-sell}.js` |
| Exemples de pastilles | `/cdn/shop/files/noir-rouge.jpg` · `/cdn/shop/files/pastille-noir.jpg` |

Copies locales des pages et des JS analysés :
`/private/tmp/claude-502/-Users-Hakim-Documents-Boutiques-drop/455c6a31-511d-4d11-a937-711aeb4be1b5/scratchpad/` (`pdp-*.html`, `coll.html`, `js-*.js`, `ma-products.json`, `ma-p2.json`, `sample/`).

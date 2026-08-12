# Audit UI/UX — Panier (page + tiroir) — Maison Noirmont

Boutique `v42pzp-h4` / maisonnoirmont.fr — thème `204248088914` « Maison Noirmont » (MAIN).
Lecture seule. Aucune écriture de thème, aucune mutation, aucune commande.
Référentiels : Web Interface Guidelines (vercel-labs) + ui-ux-pro-max (`--domain ux`, quick-reference §2 Touch, §8 Formulaires, §9 Navigation).
Rendu live vérifié sur navigateur intégré, viewport 375×812. Pas de mot de passe boutique.

## Appariement nom ↔ contenu (`checksumMd5`)

| Fichier | checksumMd5 API | md5 recalculé | Verdict |
|---|---|---|---|
| `templates/cart.json` | d1b4bd3d77588e813adc440bd09e468a | idem | OK |
| `sections/cart-drawer-group.json` | f22a877d4cb3376a3995c589f0a70114 | a993bf3ce276cdfd8066ccf75162b9b5 | **écart** — fichier de groupe auto-généré, normalisé par l'API au retour ; contenu apparié par inspection (`"type": "custom.cart_drawer"`, blocs `nm_banner_livraison` / `nm_upsell` / `discount_code_GBacFY` / `payment_methods_WRBbVe`) |
| `sections/cart-drawer.liquid` | 5339b383c962343007d73c74b34ed914 | idem | OK |
| `sections/cart.liquid` | 3143ed9377267abadf4b7964b344cf55 | idem | OK |
| `snippets/quantity-selector.liquid` | 4b12b6f533ec5799c3ca8607aa1c3810 | idem | OK |
| `blocks/_discount-code.liquid` | 7d6bb839fddf5019f693e679c7da46dd | idem | OK |
| `blocks/_cart-footer-resume-blocks.liquid` | 969cccbd659e9e95c31d35abd9f72a97 | idem | OK |
| `blocks/payment-methods.liquid` | 7c95956871ebb6064601f501bf12b47d | idem | OK |
| `assets/cart.js` | 13577feb6115a0fb2dc9d5f64169239c | idem | OK |
| `assets/cart-drawer.js` | f67075a055a55ae2da2ebdcc1f122afc | idem | OK |
| `assets/cart-discount.js` | 90a5e34889100851ebbe9caf8dd7e13a | idem | OK |
| `assets/toast-notification.js` | 30394fff73590fd2f907b7ec96154098 | idem | OK |
| `assets/base.css` | c037249b45dfb3f9b723e11debee3349 | idem | OK |
| `snippets/textfield.liquid` | f79653fd4f885eb03b55fe794a724ead | idem | OK |
| `snippets/button.liquid` | 5955bff487e064c74feb71ae07d4aaa0 | idem | OK |
| `snippets/icon.liquid` | 33914247d4fd573514d778ca74c3a40c | idem | OK |

Constantes lues dans `snippets/css-variables.liquid` et confirmées en live : `--small-multiplier: 0.7`, `--inputs-min-height: 50px`, `--inputs-font-size: 0.875rem` (14 px), `--animation-speed: 0.25s`, `--gap-sm: 0.5rem`.

---

## Constats

### templates/cart.json

- `templates/cart.json:29` - bandeau en `linear-gradient(90deg,#1E3A2F,#A98E5F)` : vert forêt + laiton, hors direction A+B (encre/craie + citron `#D6FF3F` unique). `#D6FF3F` n'apparaît nulle part dans le panier ni dans `settings_data.json`.
- `templates/cart.json:29` - texte `#FAFAF7` à 0.85rem/500 sur l'extrémité `#A98E5F` du dégradé : contraste 3,0:1, sous le seuil 4,5:1 (texte non large).
- `templates/cart.json:56` - **vente croisée : aucun pourcentage de remise annoncé** (titre « Complétez votre collection », prix unitaire, bouton « Ajouter »). Vérifié côté Admin : `automaticDiscountNodes` = 0 remise automatique. Aucune promesse fausse au panier. Point critique levé.
- `templates/cart.json:56` - `.nm-upsell-add` : `padding:.4rem .85rem` + `font-size:.78rem` → hauteur effective ≈ 28 px, sous 44×44 (WIG touch / ux `touch-target-size`).
- `templates/cart.json:56` - après ajout, rechargement complet de la page (`location.reload()`) : perte de la position de scroll, aucune confirmation ciblée de l'article ajouté.
- `templates/cart.json:56` - deux boutons `<button type="submit">Ajouter</button>` sans `aria-label` : indiscernables l'un de l'autre au lecteur d'écran.
- `templates/cart.json:56` - le `<style>` du bloc réintroduit `#1E3A2F` sur le titre, le prix et le survol du bouton : accent hors charte à trois endroits.
- `templates/cart.json:68` vs `sections/cart-drawer-group.json:70` - code promo en `style: "normal"` sur la page, `"in_accordion"` dans le tiroir : deux comportements et deux niveaux de visibilité pour le même champ.
- `templates/cart.json:181` - « Comptez généralement 2 à 3 semaines après la commande » = **J+14/J+21, cohérent** avec le bandeau, la section confiance et la fiche produit. Aucune contradiction relevée.
- `templates/cart.json:255` - `nm_reco_title` « Complétez votre collection » reprend mot pour mot le titre du bloc upsell L56 : **titre dupliqué sur la même page** (confirmé en live).
- `templates/cart.json:94` - paiement express (`_cart-accelerated-checkout`) présent sur la page panier, **absent du tiroir**.

### sections/cart-drawer-group.json

- `sections/cart-drawer-group.json:100` - `payment_methods` en `show_on_display: "desktop_only"` → `.mobile-hide` (`base.css:59`) : **aucun logo de paiement dans le tiroir sur mobile**.
- `sections/cart-drawer-group.json:111` - `block_order` du footer ne contient aucun `_cart-accelerated-checkout` : pas de Shop Pay / PayPal / Apple Pay express dans le tiroir, alors que `settings_data.json` fixe `cart_type: "drawer"` et `add_to_cart_behavior: "open_cart"` — le tiroir est le panier principal.
- `sections/cart-drawer-group.json:131` - `full_width_on_mobile: false` : combiné à `max-width: calc(100vw - 30px)` (`cart-drawer.liquid:258`), le tiroir fait 345 px sur un iPhone de 375, avec une bande morte de 30 px comme seule zone de fermeture au doigt.
- `sections/cart-drawer-group.json:31` - même bandeau, même écart de charte, même contraste 3,0:1 que sur la page.

### sections/cart-drawer.liquid

- `sections/cart-drawer.liquid:3` - `<cart-drawer>` sans `role="dialog"`, sans `aria-modal="true"`, sans `aria-label` (confirmé en live : `role=null`, `aria-modal=null`, `aria-label=null`). Ce n'est pas une boîte de dialogue pour les technologies d'assistance.
- `sections/cart-drawer.liquid:3` - **aucun piège de focus et aucune fermeture au clavier** : `cart-drawer.js` n'installe aucun écouteur `keydown`, `Escape` ne ferme pas le tiroir (ux `escape-routes`, `modal-escape`).
- `sections/cart-drawer.liquid:19` - bouton de fermeture sans `aria-label`, nom accessible = la ligature Material « close » (`snippets/icon.liquid:19`) ; `onclick` en attribut inline.
- `sections/cart-drawer.liquid:372` - `.cart-drawer__close { padding: 0; height: 24px }` → **24×24 px mesuré en live**, sous 44×44.
- `sections/cart-drawer.liquid:155` - bouton de suppression rendu par `render 'button'` sans `label` → `.button--icon-only` ; `snippets/button.liquid` n'expose aucun paramètre `aria-label`/`title` : nom accessible = « delete », en anglais, dans une boutique FR.
- `sections/cart-drawer.liquid:155` → `assets/base.css:428` - `.button--small.button--icon-only` : `min/max-width` et `min/max-height` = `0.7 × 50px` = **35×35 px verrouillés** (les `max-*` empêchent tout agrandissement).
- `sections/cart-drawer.liquid:170` - **`min: -1`** transmis au sélecteur de quantité : `quantity-selector.js` calcule `min = parseInt("-1") = -1`, le bouton « − » reste donc actif à quantité 1 ; un appui fait `stepDown()` → 0 → `change` → `#updateLineItemQuantity(line, 0)` → **article supprimé**. Le « − » est un bouton de suppression déguisé, sans confirmation.
- `sections/cart-drawer.liquid:166` → `snippets/quantity-selector.liquid:114` - variante `--small` : boutons `−` / `+` à `calc(0.7 × 50px − 2px)` = **33×33 px**.
- `sections/cart-drawer.liquid:656` - `.cart-drawer__item-actions-wrapper { gap: 5px }` : **5 px** entre le bouton supprimer (35 px) et le sélecteur de quantité (35 px), sous le minimum de 8 px (ux `touch-spacing`).
- `sections/cart-drawer.liquid:461` - `.cart-drawer__body { overflow-y: auto }` **sans `overscroll-behavior: contain`** (computed live = `auto`) : arrivé en bout de liste, le scroll fuit vers la page derrière le tiroir. Violation directe WIG « use `overscroll-behavior: contain` in modals, drawers, sheets ». Zéro règle `overscroll-behavior` dans l'ensemble des feuilles chargées.
- `sections/cart-drawer.liquid:461` - aucun `touch-action: manipulation` et aucun `-webkit-tap-highlight-color` sur le tiroir ni sur le sélecteur de quantité : délai de 300 ms au double-tap conservé sur les `+`/`−`, surlignage système non maîtrisé. Zéro règle `touch-action` sur tout le site.
- `sections/cart-drawer.liquid:395` - `.cart-drawer__footer { position: sticky; bottom: 0; padding: var(--padding-md) }` **sans `env(safe-area-inset-bottom)`** : le bouton « Commander » se glisse sous la barre gestuelle iOS. Zéro `safe-area-inset` sur tout le site.
- `sections/cart-drawer.liquid:247` - `modalSlideInRight` / `modalSlideOutRight` inconditionnels ; aucun `@media (prefers-reduced-motion: reduce)` ne couvre le tiroir (les deux seuls blocs `reduce` du thème visent les cartes produit et le méga-menu).
- `sections/cart-drawer.liquid:419` - `.cart-drawer__totals`, `.cart-drawer__reductions`, `.cart-drawer__totals-value` : **CSS mort**, le bloc `_cart-footer-resume-blocks` émet `cart__totals*`. Le tiroir n'est stylé que par ricochet des règles de `sections/cart.liquid`.
- `sections/cart-drawer.liquid:703` - `.cart-drawer__item-discount span { max-width: 70px; text-overflow: ellipsis }` : nom de la remise coupé à 70 px, sans infobulle ni texte complet (ux `truncation-strategy`).
- `sections/cart-drawer.liquid:711` - `.cart-drawer__discounts { overflow: scroll }` sur mobile : zone de défilement horizontal sans affordance, et `scroll` (au lieu de `auto`) réserve une gouttière permanente.
- `sections/cart-drawer.liquid:510` - `background-color: white` codé en dur sur les vignettes d'article : la craie de la charte est `#FAFAF7`, pas `#FFF`.
- `sections/cart-drawer.liquid:26` - titre du tiroir en `<p class="h6">` : aucun élément de titre réel dans la boîte de dialogue. `sections/cart-drawer.liquid:364` cible un `h2` qui n'existe pas — sélecteur mort.
- `sections/cart-drawer.liquid:52` - `width="85"` alors que `--cart-item-image-width: 80px` (L218) : ratio réservé faux, léger décalage de mise en page au chargement.
- `sections/cart-drawer.liquid:226` - `width: 100vw` sur l'overlay fixe : débordement horizontal possible sur desktop à barre de défilement visible.

### assets/cart-drawer.js

- `assets/cart-drawer.js:145` - `#handleItemRemove` → `#updateLineItemQuantity(index, 0)` : **action destructive exécutée immédiatement, ni fenêtre de confirmation ni annulation**. Violation frontale WIG « Destructive actions require confirmation modal or undo window — never execute immediately » et ux `confirmation-dialogs` / `undo-support`.
- `assets/cart-drawer.js:177` - `message: message` : variable **non définie** dans cette portée → `ReferenceError`, capturée par le `.catch` L192. **Le toast d'erreur du tiroir ne s'affiche jamais.** Dépassement de stock, article épuisé : la quantité ne bouge pas et rien ne l'explique.
- `assets/cart-drawer.js:69` - `#onBackdropClick` fait un test géométrique sur `event.clientX/clientY`. Une activation clavier (Entrée/Espace sur un bouton) synthétise un clic à `0,0` → jugé « hors dialogue » → **le tiroir se ferme** dès qu'on manipule la quantité au clavier.
- `assets/cart-drawer.js:78` - `open()` n'envoie pas le focus dans le tiroir ; `close()` ne le restitue pas à l'élément déclencheur.
- `assets/cart-drawer.js:100` - `renderCartContents` remplace tout le contenu HTML du tiroir à chaque mise à jour : focus détruit, aucune région `aria-live`, aucune annonce du nouveau total.
- `assets/cart-drawer.js:90` - `setTimeout(..., 125)` alors que `--animation-speed = 0.25s` : l'animation de sortie est tronquée de moitié, le tiroir disparaît d'un coup.
- `assets/cart-drawer.js:62` - `is-loading` ajouté au clic sur « Commander », jamais retiré et bouton non désactivé : au retour arrière navigateur, le bouton reste en état de chargement.

### assets/cart.js

- `assets/cart.js:49` - suppression immédiate, ni confirmation ni annulation (même défaut que le tiroir).
- `assets/cart.js:87` - `.finally(() => window.location.reload())` : **rechargement complet de la page à chaque changement de quantité**, y compris en cas d'erreur. Le toast d'erreur envoyé L80 est détruit avant d'être lu — l'acheteur voit sa quantité revenir en place sans explication.
- `assets/cart.js:14` et `:45` - `removeEventListener` avec de nouvelles fonctions fléchées : écouteurs jamais retirés, doublons à chaque re-rendu de section.

### snippets/quantity-selector.liquid

- `snippets/quantity-selector.liquid:35` et `:60` - boutons `−` / `+` sans `aria-label` et sans `type="button"` : dans un formulaire ils valent `submit`, et leur nom accessible est la ligature « remove » / « add ».
- `snippets/quantity-selector.liquid:44` - `<input type="number">` sans `<label>` ni `aria-label` : le champ de quantité n'a aucun nom accessible (ux `input-labels`, `form-labels`).
- `snippets/quantity-selector.liquid:141` - `input:focus-visible { outline: none; box-shadow: none }` **sans indicateur de remplacement**. Violation WIG « never apply `outline: none` without providing focus replacement ».
- `snippets/quantity-selector.liquid:125` - retour visuel réservé au survol (`:hover svg { scale(1.1) }`) : aucun état pressé, inopérant au doigt (ux `hover-vs-tap`, `press-feedback`).
- `snippets/quantity-selector.liquid:94` - `appearance: textfield` appliqué aussi aux `<button>`.

### blocks/_discount-code.liquid — champ code promo

- `blocks/_discount-code.liquid:43` - `render 'textfield'` **sans `autocomplete`, sans `spellcheck`, sans `autocapitalize`, sans `autocorrect`** (confirmé en live : les quatre attributs absents, correction orthographique active par défaut). Sur iOS le clavier met une majuscule initiale et autocorrige la saisie : un code sensible à la casse devient inapplicable, et le correcteur souligne le code en rouge. `snippets/textfield.liquid` accepte pourtant `autocorrect`, `autocapitalize`, `autocomplete` en paramètres — aucun n'est transmis. Violation WIG formulaires (`autocomplete` requis, désactivation du correcteur sur les codes).
- `blocks/_discount-code.liquid:43` → `snippets/textfield.liquid:104` - `font-size: var(--inputs-font-size)` = **14 px** (mesuré live) : sous 16 px, **Safari iOS zoome la page au focus** du champ promo, dernière étape avant paiement (ux `readable-font-size`).
- `blocks/_discount-code.liquid:52` - `<button class="button ..." data-ref="apply-discount">` **sans `type="button"`** : sur la page panier il devient le bouton de soumission implicite du `<form id="cart_form">` ; dans le tiroir le bloc est hors du `<form id="cart_drawer_form">` (fermé `cart-drawer.liquid:181`, footer ouvert L184) donc **la touche Entrée dans le champ promo ne fait rien**. Comportement clavier différent entre les deux contextes.
- `blocks/_discount-code.liquid:70` - `<span class="cart-discount__remove-discount" data-ref="remove-discount">` : retrait d'une remise appliquée — action destructive — sur un `<span>` **non focusable, sans `role`, sans `aria-label`, inaccessible au clavier**.
- `blocks/_discount-code.liquid:151` - `.cart-discount__remove-discount { height: 14px }` : cible tactile de 14 px.
- `blocks/_discount-code.liquid:85` - en `in_accordion` (réglage du tiroir), le champ est replié par défaut : un acheteur détenteur d'un code doit le découvrir derrière un accordéon.
- `blocks/_discount-code.liquid:43` - libellé : `<label for="cart-discount">` bien présent et associé (vérifié live) — conforme. Le libellé et le placeholder partagent la même chaîne « Code de réduction », le libellé flottant remonte au focus.

### assets/cart-discount.js

- `assets/cart-discount.js:175` - `setErrorMode` n'affiche l'erreur qu'en **toast global centré en bas d'écran**, jamais sous le champ. Violation WIG « display errors inline adjacent to fields » et ux `error-placement` / `error-feedback`.
- `assets/cart-discount.js:181` - `this.inputDiscount.value = ''` : **la saisie de l'utilisateur est effacée à chaque erreur**. Une faute de frappe impose de retaper le code entier.
- `assets/cart-discount.js:183` - la classe `textfield--error` est retirée au bout de 2 s : le seul repère visuel sur le champ disparaît de lui-même.
- `assets/cart-discount.js:130` - après échec, le focus n'est pas rendu au champ (WIG « focus first error on form submission »).
- `assets/cart-discount.js:143` - **aucun retour de succès** quand un code est accepté : ni toast, ni message. Le seul signal est un badge qui apparaît après rechargement (ux `success-feedback`).
- `assets/cart-discount.js:148` - `window.location.reload()` dès que l'URL contient `/cart` : rechargement complet pour appliquer un code.
- `assets/cart-discount.js:21` - `removeEventListener` avec de nouvelles fonctions fléchées : sans effet.

### blocks/_cart-footer-resume-blocks.liquid — totaux

- `blocks/_cart-footer-resume-blocks.liquid:28` - `.cart__totals-value` **sans `font-variant-numeric: tabular-nums`** (computed live = `normal`). **Zéro règle `font-variant-numeric` / `tabular-nums` dans l'ensemble des feuilles chargées.** Exigence explicite de la direction A+B sur totaux et sous-totaux ; aggravé par `show_trailing_zeros: false` qui fait varier le nombre de chiffres (`€0`, `€12,90`, `€329`).
- `blocks/_cart-footer-resume-blocks.liquid:5` - `content_for 'blocks'` est rendu **avant** remises et total : dans l'ordre visuel, l'upsell et le champ promo s'intercalent entre les articles et le montant à payer.
- `blocks/_cart-footer-resume-blocks.liquid:28` - le récapitulatif ne comporte **aucune ligne « Livraison : offerte »** alors que le bandeau et deux autres blocs la promettent : l'engagement n'est jamais confirmé sur la ligne de compte.
- `blocks/_cart-footer-resume-blocks.liquid:33` - le total barré est reconstruit depuis `compare_at_price × quantité`, pas depuis une remise réelle : ancre de prix dérivée du prix barré catalogue, à surveiller côté véracité.
- `blocks/_cart-footer-resume-blocks.liquid:7` - `.cart__discounts` passe en `overflow: scroll` sous 750 px : la ligne de remise défile horizontalement sur mobile.

### sections/cart.liquid — page panier

- `sections/cart.liquid:191` - `.cart__footer` est rendu **hors du `{% if cart.empty? %}`** : sur un panier vide, la page affiche l'upsell, le champ code promo, « Total estimé **€0** » et un bouton « Commander » (désactivé mais visible). Confirmé en live sur `/cart`.
- `sections/cart.liquid:123` - le prix affiché par ligne est `item.final_price`, soit le **prix unitaire** ; le total de la ligne n'apparaît nulle part. À quantité 2, l'acheteur lit « €299 » sur une ligne qui en vaut 598. Le code de la version précédente, qui affichait `final_line_price`, est conservé en commentaire L128-140.
- `sections/cart.liquid:178` - `min: -1` : même piège de suppression au « − » que dans le tiroir.
- `sections/cart.liquid:163` - même bouton supprimer icon-only, 35×35 px, nom accessible « delete ».
- `sections/cart.liquid:491` - `.cart__item-actions-wrapper { gap: 5px }` : même espacement sous 8 px.
- `sections/cart.liquid:249` - `.cart__form { grid-template-columns: 100% }` sous 750 px et `.cart__footer` sans `position: sticky` : **aucun CTA collant sur mobile**. Le bouton « Commander » arrive après les articles, l'upsell, le code promo, les logos de paiement et deux accordéons — hors écran sur tout panier réel.
- `sections/cart.liquid:352` - `background-color: white` codé en dur.
- `sections/cart.liquid:545` - la règle de troncature à 70 px des noms de remise est **commentée ici** mais **active dans le tiroir** (`cart-drawer.liquid:703`) : même donnée, deux rendus.

### assets/base.css — socle

- `assets/base.css:347` - `.button { outline: 1px solid transparent }` et **aucune règle `:focus-visible` positive** pour les boutons, champs et liens du panier. Les seules règles `:focus-visible` du site posant un anneau visible appartiennent à Splide (hors périmètre) ; toutes celles qui touchent le panier le **suppriment** : `base.css:475` (`.select`), `base.css:727` (`.dialog-modal`), `quantity-selector.liquid:141`, `textfield.liquid:96`. **Le focus clavier est invisible sur l'intégralité du panier.** Violation WIG focus et ux `focus-states`.
- `assets/base.css:348` - `transition: all var(--animation-speed-medium)` sur `.button` : violation WIG « never use `transition: all` — explicitly list properties ». Concerne « Commander » et le bouton supprimer.
- `assets/base.css` - **aucun `@media (prefers-reduced-motion: reduce)`** couvrant le tiroir, son fond `backdrop-filter` ou les transitions de boutons. Violation WIG motion.
- `assets/base.css:836` - `.toast-notification { top: 100% }` + `translateY(calc(-100% - 20px))` : 20 px fixes du bas, **sans `env(safe-area-inset-bottom)`**, et `z-index: 10001` contre `10000` du tiroir → le toast se superpose au bouton « Commander » collant.
- `assets/base.css:282` - `::-webkit-scrollbar-thumb { border: 3px solid white }` : blanc codé en dur, visible sur la barre de défilement du tiroir.

### assets/toast-notification.js

- `assets/toast-notification.js:21` - le toast n'a **ni `role="alert"` ni `aria-live`** (confirmé live : `role=null`, `aria-live=null`). Seul canal d'erreur du panier, jamais annoncé aux lecteurs d'écran. Violation ux `aria-live-errors` / `toast-accessibility`.
- `assets/toast-notification.js:41` - auto-fermeture à 3 s, **aucun bouton de fermeture**, aucune pause au survol ou au focus : un message d'erreur long peut disparaître avant d'être lu.
- `assets/toast-notification.js:54` - le message est injecté en HTML brut (propriété `.innerHTML`) là où `textContent` suffirait.
- `assets/toast-notification.js:21` - écouteur `toast:open` posé dans `connectedCallback`, jamais retiré : doublons possibles.

### snippets/button.liquid — snippets/icon.liquid

- `snippets/button.liquid:60` - le snippet n'expose **aucun paramètre `aria-label` ni `title`** : tout bouton `--icon-only` du thème naît sans nom accessible. Cause racine des boutons supprimer et fermer du panier.
- `snippets/icon.liquid:11` - l'icône est un `<span>` contenant une **ligature Material lisible** (`delete`, `close`, `remove`, `add`), sans `aria-hidden="true"` : les noms accessibles du panier sont des mots anglais dans une boutique française.

### Vérifications live complémentaires

- Format monétaire `€12,90` / `€329` / `€0` : symbole avant le nombre, non conforme à l'usage français (`12,90 €`). Visible sur tous les prix et sur le total du panier.
- « Complétez votre collection » apparaît deux fois sur `/cart` (bloc upsell puis section `nm_reco`).
- « Livraison offerte » apparaît quatre fois sur `/cart` (bandeau d'annonce, bandeau panier, accordéon, section confiance) : redondance qui dilue le message.
- Délai affiché : **J+14/J+21 partout**, conforme et non contradictoire.
- Absence de mention de délai dans le tiroir : conforme au choix retenu, non signalé.

---

## Classement par impact conversion

### BLOQUANT — 4

1. **Suppression d'article sans filet, et « − » transformé en bouton de suppression** (`cart.js:49`, `cart-drawer.js:145`, `cart-drawer.liquid:170`, `cart.liquid:178`) — un seul appui à 33×33 px, souvent involontaire, vide la ligne sans confirmation ni annulation : c'est le geste qui fait perdre un panier de 299 € en un doigt mal placé.
2. **Erreurs de quantité invisibles** (`cart-drawer.js:177` variable non définie → toast jamais émis ; `cart.js:87` rechargement qui détruit le toast) — l'acheteur qui dépasse le stock voit sa quantité revenir en arrière sans un mot d'explication et conclut que le site est cassé.
3. **Champ code promo inutilisable sur mobile** (`_discount-code.liquid:43` sans correcteur désactivé ni `autocapitalize`/`autocorrect`/`autocomplete`, 14 px donc zoom iOS ; `cart-discount.js:181` efface la saisie, `:175` erreur en toast lointain) — le code est autocapitalisé puis refusé puis effacé, à l'étape précise où l'acheteur cherche à réduire son panier avant de payer.
4. **Tiroir mobile non contenu** (`cart-drawer.liquid:461` sans `overscroll-behavior: contain`, aucune fermeture par `Escape`, `:395` footer collant sans safe-area) — le scroll fuit vers la page derrière, on ne sort pas du tiroir au clavier, et « Commander » tombe sous la barre gestuelle iOS : le tiroir est pourtant le panier principal (`cart_type: drawer`).

### FORT — 6

5. **Cibles tactiles hors normes et trop rapprochées** (supprimer 35×35 verrouillé par `base.css:428`, quantité 33×33, fermer 24×24, écart de 5 px `cart-drawer.liquid:656`) — supprimer et décrémenter se touchent à 5 px : la mauvaise action part une fois sur plusieurs.
6. **Aucun paiement express ni logo de paiement dans le tiroir sur mobile** (`cart-drawer-group.json:100` et `:111`) — le canal de conversion principal est privé de Shop Pay/Apple Pay et de tout signal de sécurité de paiement.
7. **Aucun CTA collant sur la page panier mobile** (`cart.liquid:249`) — « Commander » est enterré sous l'upsell, le promo, les logos et deux accordéons ; il faut scroller pour trouver la sortie.
8. **Focus clavier invisible sur tout le panier** (`base.css:347`, `:475`, `:727`, `quantity-selector.liquid:141`, `textfield.liquid:96`) plus boutons icon-only sans nom accessible (« delete », « close ») — panier inutilisable au clavier et opaque au lecteur d'écran.
9. **Montants illisibles et incomplets** (`_cart-footer-resume-blocks.liquid:28` sans chiffres tabulaires, `cart.liquid:123` prix unitaire sans total de ligne) — l'acheteur ne peut pas vérifier son propre calcul avant de payer, ce qui est le seul travail d'un panier.
10. **Bandeau de réassurance hors charte et sous le seuil de contraste** (`cart.json:29`, `cart-drawer-group.json:31` : dégradé `#1E3A2F`→`#A98E5F`, 3,0:1) — la promesse la plus importante du panier est celle qu'on lit le moins bien, dans des couleurs qui ne sont pas celles de la maison.

### MOYEN — 8

11. **Titre « Complétez votre collection » dupliqué** (`cart.json:56` et `:255`) — deux blocs de vente croisée successifs portant le même titre donnent l'impression d'un bug de template.
12. **Footer complet affiché sur panier vide** (`cart.liquid:191`) — champ promo, « Total estimé €0 » et bouton Commander sur une page qui vient d'annoncer que le panier est vide.
13. **Toast sans `aria-live`, sans fermeture, coupé à 3 s** (`toast-notification.js:21`, `:41`) — seul canal de feedback du panier, et il est à la fois muet pour les lecteurs d'écran et trop fugace.
14. **Retrait de remise inaccessible** (`_discount-code.liquid:70` `<span>` non focusable, 14 px) — action destructive impossible à déclencher au clavier et difficile au doigt.
15. **Noms de remise tronqués à 70 px et remises en scroll horizontal** (`cart-drawer.liquid:703`, `:711`, `cart.liquid:545` commenté) — l'acheteur ne sait pas quelle remise s'applique, et le rendu diffère entre page et tiroir.
16. **Format monétaire `€12,90`** — symbole devant le nombre : détail qui signale à un acheteur français un site non localisé, juste avant le paiement.
17. **Animation de sortie tronquée et aucun `prefers-reduced-motion`** (`cart-drawer.js:90` 125 ms contre 250 ms, `base.css` sans bloc `reduce`) — fermeture qui saute, et mouvement imposé aux utilisateurs qui l'ont désactivé.
18. **Comportement clavier divergent du bouton « Appliquer »** (`_discount-code.liquid:52` sans `type="button"`) — Entrée fonctionne sur la page, ne fait rien dans le tiroir.

### FAIBLE — 6

19. **Fermeture parasite du tiroir à l'activation clavier** (`cart-drawer.js:69` test sur `clientX/Y`, nul en clavier) — gêne réelle mais population très restreinte au vu des autres blocages clavier déjà présents.
20. **Focus perdu à chaque mise à jour du tiroir** (`cart-drawer.js:100` remplacement complet du contenu, aucune annonce du nouveau total) — sans anneau de focus visible, la perte passe inaperçue de la plupart des visiteurs.
21. **`transition: all` sur `.button`** (`base.css:348`) — coût de rendu et transitions involontaires, sans effet perçu à ce stade.
22. **Blanc pur codé en dur** (`cart-drawer.liquid:510`, `cart.liquid:352`, `base.css:282`) — écart de charte de faible amplitude sur des surfaces réduites.
23. **CSS et sélecteurs morts** (`cart-drawer.liquid:419` totaux jamais appliqués, `:364` `h2` inexistant) — dette qui rendra la prochaine retouche du tiroir imprévisible.
24. **Écouteurs jamais retirés** (`cart.js:14`/`:45`, `cart-discount.js:21`, `toast-notification.js:21`) et `width="85"` contre `80px` (`cart-drawer.liquid:52`) — fuites et micro-décalage sans effet mesurable sur la conversion.

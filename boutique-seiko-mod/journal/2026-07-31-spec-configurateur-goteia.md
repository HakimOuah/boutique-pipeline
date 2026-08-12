# Spécification — configurateur goteia.fr, décorticage et transposition NOIRMONT

Relevé du **27/07/2026**, navigateur intégré (Chrome laissé libre). **Étude en lecture seule** : aucun
identifiant saisi, aucune commande, aucun ajout au panier validé, aucune modification du thème NOIRMONT.
Bandeau cookies refusé (option la plus protectrice).

Cibles observées : `goteia.fr/configurateur/seikoak` (5 étapes, 29 règles) et
`goteia.fr/configurateur/seikojust` (8 groupes, 19 règles) en **desktop 1280×720 et 1600×900** puis en
**mobile 375×812**. Comparaison secondaire : `watchmodcustom.com/en/configurator/32-basic-watch.html`.

Les valeurs chiffrées ci-dessous ne sont pas déduites de l'apparence : elles viennent du DOM, des styles
inline, du chunk client `_next/static/chunks/0djodmx8fwfh2.js` (28,6 ko, le composant `ConfiguratorClient`),
du dataset Sanity public `uihp5v6f/production` et de `PerformanceResourceTiming`.

---

## 0. Réponse courte à la question qui commande tout

**Leur image est un empilement de calques PNG transparents (un calque par pièce), pas une photo finie.**
Le mécanisme de composition n'est **pas** transposable à nos visuels. **En revanche leur mise en scène l'est
intégralement**, et même mieux avec des photos entières — voir §8. Ce qu'il faut copier, ce n'est pas le
compositeur, c'est le **carrousel dont la vignette sélectionnée *est* le produit fini**.

---

## 1. Structure de l'entonnoir

### 1.1 Architecture générale

Cinq configurateurs séparés (`seikoak`, `seikojust`, `seikolus`, `seikona`, `seikoriner`), un par plateforme
horlogère, chacun à **349,00 €** de prix de base. Le choix de plateforme se fait **avant** le configurateur,
sur `/configurateur` (grille de 5 cartes « CONFIGURER »). C'est ce qui leur permet de n'avoir aucune règle
dimensionnelle à l'intérieur d'un configurateur.

Page `/configurateur/{slug}` = une seule vue, pas de navigation d'URL entre les étapes. L'URL ne change
**jamais** pendant la configuration ; le paramètre `?c=<base64>` n'est produit que par le bouton Partager.
Conséquences : pas de retour arrière navigateur, pas d'étape indexable, pas de reprise après rechargement.

### 1.2 Les étapes, réellement

| # | Question affichée | Groupe | Options (SEIKOAK) | Rendu |
|---|---|---|---:|---|
| 1 | « Choisissez votre boîtier » | `boitier` | 8 | carrousel |
| 2 | « Choisissez votre bracelet » | `bracelet` | 11 | carrousel |
| 3 | « Choisissez votre cadran » | `cadran` | 18 | carrousel |
| 4 | « Choisissez votre aiguilles » | `aiguilles` | 8 | carrousel |
| 5 | « Choisissez votre fond de boîtier » | `fond-boitier` | 2 | *split layout* (grille 2 colonnes) |

Le libellé est généré par `« Choisissez votre » + label.toLowerCase()` — d'où le **« Choisissez votre
aiguilles »** fautif, visible en production. Titre `<h1>` réel en `sr-only` ; ce qui est affiché est un `<p>`.

Les autres modèles montent plus haut : **SEIKOJUST = 8 groupes** (`boitier` 12, `bracelet` 25, `cadran` 34,
`aiguilles` 9, `trotteuse` 13, `date` 2, `size` 2, `fond-de-boitier` 2) ; SEIKORINER = 8 groupes ;
SEIKONA = 5 ; SEIKOLUS = 4. **Le nombre d'étapes n'est pas constant d'un modèle à l'autre.**

### 1.3 Récapitulatif

**Il n'y a pas d'écran de récapitulatif.** Le récapitulatif est une **barre permanente** sous l'aperçu,
présente dès l'étape 1 : nom du modèle, ligne en capitales
`BOÎTIER ARGENT — BRACELET ARGENT — CADRAN NOIR ET ARGENT — AIGUILLES ARGENT — FOND DE BOÎTIER TRANSPARENT`
(séparateur `"  —  "`), prix, puis « ENREGISTRER LA CONFIGURATION » et « AJOUTER AU PANIER ».
À la dernière étape, le bouton « Étape suivante » de l'en-tête **se transforme en « Ajouter au panier »**
(avec icône panier) : c'est le seul signal de fin de parcours.

### 1.4 Retour arrière — et ce qu'il détruit

On peut revenir (bouton « Étape précédente », désactivé à l'étape 1). **Mais revenir et changer le boîtier
écrase silencieusement les choix suivants.** Le code fait deux passes :

```js
// passe 1 — dès que la valeur "when" change, le groupe "then" est remis à la PREMIÈRE valeur autorisée
if (G[r.whenGroupKey] === r.whenChoiceValue && prev[r.whenGroupKey] !== G[r.whenGroupKey]) {
  const a = r.thenAllowedValues.find(v => group.choices.some(c => c.value === v));
  if (a) fix[r.thenGroupKey] = a;
}
// passe 2 — tout groupe dont la valeur courante n'est plus autorisée est ramené à la première autorisée
```

Vérifié en direct : bracelet = *Caoutchouc Noir*, on revient changer le boîtier `argent → argent-chrono`
(règle qui **autorise toujours** `caoutchouc-noir`) → le bracelet repasse quand même à **Argent**.
La passe 1 ne cherche pas à préserver un choix encore valide. **C'est un bug de conception, pas une
contrainte** : à ne pas reproduire.

Effet de bord observé : le compteur passe de **« Étape 1 / 5 » à « Étape 1 / 4 »**, car les étapes dont il ne
reste qu'une option (ici `fond-boitier` forcé à `plein`) **disparaissent du parcours** :

```js
eW = optionGroups.map((g,i)=>i).filter(i => nbOptionsAutorisées(i) >= 2)   // étapes visibles
// « Étape {index dans eW + 1} / {eW.length} »
```

C'est bien géré (le dénominateur suit), mais le choix escamoté **reste listé dans le récapitulatif**
(« FOND DE BOÎTIER PLEIN ») sans que le client l'ait vu ni choisi.

---

## 2. Comment l'image se met à jour — le mécanisme réel

### 2.1 Verdict : calques superposés

Ce sont **des calques PNG transparents empilés**, un par pièce, tous carrés et de même cadrage,
`position: absolute; inset: 0; object-contain`, avec un `z-index` par groupe fourni par le CMS.
Ni sprite, ni vidéo, ni 3D, ni image par combinaison (impossible : 8×11×18×8×2 = **25 344** combinaisons pour
SEIKOAK, ≈ 5 M pour SEIKOJUST).

Schéma CMS par groupe : `key, label, displayType, zIndex, layerScale, layerOffsetX, layerOffsetY, required,
splitLayout, tooltipOffsetY, choices[]`. Chaque `choice` porte **deux images distinctes** :
`image` (la vignette de choix) et `previewLayer` (le calque de composition) — souvent le même asset, mais le
modèle les sépare, ce qui est le bon découpage.

Ordre d'empilement SEIKOAK (`zIndex`) : `fond-boitier 0 < cadran 10 < bracelet 20 < boitier 30 < aiguilles 50`.
SEIKOJUST : `bracelet 10 < boitier 20 < cadran 30 < date 40 < aiguilles 50 < trotteuse 60`.
Chaque calque reçoit une correction de calage par groupe : `transform: translate(offsetX%, offsetY%)
scale(layerScale)` — pour SEIKOAK, `layerScale = 1.02` sur les quatre groupes visuels. **Ce recalage à la main
est le coût caché du modèle en calques.**

Les options non visuelles n'ont **aucun calque** : `fond-boitier` et `size` ont `nLayer = 0`. Elles ne
modifient pas l'image du tout. C'est le motif directement réutilisable — voir §8.4.

### 2.2 La trouvaille de mise en scène (le vrai sujet)

Le carrousel d'options **n'est pas à côté** de l'aperçu : il est **dans** l'empilement, à sa profondeur.
Le code découpe les calques en deux paquets autour du groupe courant :

```js
eG = groupes dont zIndex < zIndex(groupe courant)   // rendus SOUS le carrousel
eO = groupes dont zIndex > zIndex(groupe courant)   // rendus AU-DESSUS du carrousel
```

et l'emplacement central du carrousel porte le calque du groupe en cours d'édition. Résultat :

- l'option **sélectionnée** apparaît **habillée du reste de la montre** (elle est la montre finie) ;
- les options **voisines** apparaissent en **pièces nues** (boîtiers vides, jeux d'aiguilles isolés) ;
- la vignette de l'option sélectionnée est mise à `opacity: 0` — l'aperçu composé prend exactement sa place
  (mesuré : pile `x = 324, 241×241` / vignette `x = 326, 238×238`, elles se superposent au pixel près).

Quand on choisit un voisin, on a la sensation que la pièce **glisse dans la montre**. C'est l'effet que Hakim
a vu et qu'il veut. **Il ne dépend pas des calques** : il dépend de la géométrie du carrousel (§8.2).

### 2.3 URL, dimensions, poids

CDN Sanity, sources **800×800** et **1080×1080 PNG**, servies via des paramètres de transformation :

```
https://cdn.sanity.io/images/uihp5v6f/production/<hash>-1080x1080.png?w=1000&q=80&auto=format
```

| Variante | Usage | Poids mesuré (AVIF, `Accept` navigateur) | Poids si PNG |
|---|---|---:|---:|
| `w=600` | préchargement « mobile » | **15 ko** | 110 ko |
| `w=1000` | **rendu réel, toutes tailles d'écran** | **35 ko** | 290 ko |
| `w=1600` | vue zoomée | **55 ko** | 717 ko |

`Cache-Control: public, max-age=31536000, s-maxage=2592000` — un an de cache navigateur : le deuxième passage
sur une option est gratuit. **C'est ce qui rend le swap instantané, pas une astuce d'animation.**

Surdimensionnement à noter : l'emplacement mesure **238 px** en desktop 1280 et **262 px** en mobile 375, et
on télécharge du **1000 px** dans les deux cas. Aucun `srcset`, aucun `sizes` : 4× le nécessaire en desktop DPR 1.

### 2.4 Préchargement — trois couches empilées

1. **`<link rel="preload" as="image">` du HTML** : les options du groupe courant + les calques actifs, en
   **`w=1600` avec `fetchpriority="high"`** *et* en `w=1000` *et* en `w=600`. **58 balises `preload`** sur la
   page SEIKOAK, dont 22 doublons exacts, **aucune n'ayant d'attribut `media` ni `imagesrcset`** → tous les
   écrans téléchargent les trois tailles.
2. **Préchargement JS exhaustif au montage** — le cœur du dispositif :
   ```js
   const all = useMemo(() => optionGroups.flatMap(g =>
     g.choices.filter(c => c.previewLayer)
              .map(c => urlFor(c.previewLayer).width(1000).auto('format').quality(80).url())), [conf]);
   useEffect(() => { for (const src of all) new window.Image().src = src; }, [all]);
   ```
   **Tous les calques de toutes les options de toutes les étapes**, en `w=1000`, dès l'ouverture.
3. Placeholder **LQIP** base64 20×20 par option (`filter: blur(12px)`), fondu à `opacity 0` sur `onLoad`.

Coût mesuré sur **SEIKOJUST** (première visite, cache froid) : **110 requêtes `cdn.sanity.io`**
(78 en `w=1000`, 32 en `w=1000/1600` via `preload`), **toutes terminées à 1 162 ms**, `load` à 1 195 ms.
Estimation du volume : **≈ 3,6 Mo d'images sur un seul chargement de page**. Sur un mobile 4G réel c'est
2 à 3 s d'occupation du réseau ; en 3G, une page inutilisable pendant plusieurs secondes.

**Le principe est juste (rien ne scintille), la dose est excessive.** §8.5 propose la version dosée.

### 2.5 Séquence exacte au clic sur une option

Mesuré par `MutationObserver` horodaté, trois fois :

| t | Événement |
|---|---|
| **0 ms** | `transform: translate(calc(var(--carousel-step) * -N - var(--slot-size)/2), -50%)` sur la rangée → glissement du carrousel |
| 0 ms | ancienne vignette → `opacity-100`, nouvelle vignette → `opacity-0` (transition 500 ms) |
| **~250 ms** *(code)* | `useState` retardé `setTimeout(() => setDeferred(selections), 250)` : les calques environnants adoptent la nouvelle sélection |
| ~250→750 ms | fondu croisé du calque changé (`AnimatePresence`, ancien et nouveau coexistent) |
| **0 requête réseau** | l'image était déjà en cache (vérifié : aucune entrée `resource` nouvelle) |

En pratique j'ai mesuré le remplacement du `src` du calque à **438 ms, 1 045 ms et 1 057 ms** après le clic
selon la charge : le `setTimeout(250)` est repoussé par React (`useTransition`) et par le travail de rendu.
**C'est visible** : la pièce reste « en transit » jusqu'à une seconde. Faiblesse à corriger chez nous.

---

## 3. Le mouvement — toutes les valeurs

| Élément | Propriété animée | Durée | Fonction | Source |
|---|---|---:|---|---|
| Rangée du carrousel | `transform: translateX` | **250 ms** | `ease-out` = `cubic-bezier(0,0,.2,1)` | classe `transition-transform duration-[250ms] ease-out` |
| Vignette sélectionnée / désélectionnée | `opacity` | **500 ms** | défaut Tailwind | `transition-opacity duration-500` |
| Échange d'un calque | `opacity` (fondu croisé) | **500 ms** | `easeOut` | `AnimatePresence mode="popLayout"`, `transition:{duration:.5}` |
| Respiration permanente de l'aperçu | `scale: [1 → 1.012]` | **2 500 ms**, `repeat: Infinity, repeatType: 'reverse'` | `easeInOut` | `em` (Framer Motion) |
| Passage en vue zoomée | **`width` et `height`** | **600 ms** | `ease-out` | `transition:"width 0.6s ease-out, height 0.6s ease-out"` |
| Ouverture du panneau *split* | **`width` 0 → 400 px** | **450 ms** | `cubic-bezier(.22,1,.36,1)` | `motion.div animate={{width:400*open}}` |
| Contenu du panneau *split* | `opacity` + `x: -12 → 0` | **350 ms**, `delay: 200 ms` | `easeOut` | idem |
| Apparition du carrousel au changement d'étape | `opacity` 0 → 1 | **350 ms** | `easeOut` | wrapper `motion.div` |
| Panneau *split* en mobile | `opacity` + `y: 8 → 0` | **300 ms** | `easeOut` | bloc `lg:hidden` |
| Fondu du LQIP flou | `opacity` | **300 ms** | défaut | `transition-opacity duration-300` |
| Étiquette au survol | `opacity` | **200 ms**, `delay: 600 ms` | défaut | `group-hover:delay-[600ms]` |
| Fond de la barre récap en vue zoomée | `opacity` 1 → 0,7 | **300 ms** | défaut | `transition-opacity duration-300` |
| Boutons de zoom | **`transition-all`** | 150 ms | défaut | classe `transition-all` |

Donc : **fondu** (calques, vignettes, étapes), **glissement** (carrousel en `translateX`, panneau en `x`),
**zoom** (respiration continue + agrandissement de l'emplacement). Pas de rotation, pas de parallaxe.

### 3.1 `prefers-reduced-motion` : **non respecté**

Trois preuves convergentes :

1. La feuille de style de production ne contient **qu'une seule** règle `@media (prefers-reduced-motion: reduce)`,
   et elle ne concerne pas le configurateur :
   ```css
   @media (prefers-reduced-motion:reduce){
     .goteia-faq-content,.goteia-faq-content[data-open=true]{transition:none!important}
   }
   ```
2. Le chunk du configurateur (`0djodmx8fwfh2.js`) ne contient **ni `matchMedia`, ni `prefers-reduced-motion`,
   ni `MotionConfig`** (0 occurrence de chacun).
3. Framer Motion est donc laissé sur son défaut, présent en clair dans son bundle :
   `reducedMotion:"never"` — la préférence système est **ignorée par construction**.

Conséquence concrète : la **respiration infinie `scale 1 → 1.012` toutes les 2,5 s ne s'arrête jamais**, même
pour un utilisateur qui a demandé de réduire les animations. C'est le point le plus net à ne pas reproduire.

### 3.2 Propriétés animées : deux fautes de performance

- `transition: "width 0.6s, height 0.6s"` sur la pile de calques et `animate={{width:400}}` sur le panneau
  *split* : ce sont des **propriétés de mise en page**, elles déclenchent *layout* + *paint* à chaque frame,
  sur un conteneur qui porte 3 à 6 images de 1000 px.
- `transition-all` sur les boutons de zoom.

Les animations qui portent l'effet (carrousel, fondus, respiration) sont, elles, correctement en `transform`
et `opacity`.

---

## 4. Traitement des options impossibles

### 4.1 Le moteur

`rules[] = { label, whenGroupKey, whenChoiceValue, thenGroupKey, thenAllowedValues[] }` — une **liste blanche**,
jamais une liste noire. Résolution par **intersection** de toutes les règles déclenchées :

```js
const allowed = (groupKey) => {
  const hits = rules.filter(r => r.thenGroupKey === groupKey && selections[r.whenGroupKey] === r.whenChoiceValue);
  return hits.length === 0 ? null                        // null = aucune restriction
    : hits.reduce((acc, r) => acc.filter(v => r.thenAllowedValues.includes(v)), hits[0].thenAllowedValues);
};
```

Volumétrie réelle : **SEIKOAK 29 règles**, **SEIKOJUST 19**, SEIKONA 8, SEIKORINER 4, SEIKOLUS 0.
*(La note du 24/07 attribuait les 19 règles au configurateur observé : elles sont bien celles de SEIKOJUST.)*
Pour SEIKOAK, **les 29 règles sont toutes déclenchées par `boitier`** — le premier choix pilote tout, aucun
autre groupe n'est déclencheur. Une règle est un **doublon exact** (`or-jaune-chrono → bracelet` deux fois).

Familles de règles SEIKOAK : accord de métal boîtier↔bracelet (8), boîtier chrono ↔ cadran chrono (8),
boîtier chrono ↔ aiguilles chrono (8), boîtier chrono → fond plein obligatoire (4).

### 4.2 Dans l'interface : **deux traitements différents selon le rendu**

**a) Étapes en carrousel (`displayType: "tiles"`) → l'option incompatible est ABSENTE.**
Elle est retirée de la liste avant rendu, elle n'existe pas dans le DOM :

```js
const visible = allowed ? allowed.map(v => choices.find(c => c.value === v)).filter(Boolean) : choices;
```

Vérifié : `bracelet` a **11** options au CMS ; avec `boitier = argent`, le DOM n'en contient que **8**
(or jaune, or rose, noir disparus). Le `cadran` passe de 18 à 9 avec un boîtier chrono, les `aiguilles` de
8 à 4. Aucun indice visuel, aucun message : le client ne sait pas que des options existent ailleurs.

**b) Étapes *split layout* (`displayType: "radio"`, ou clés `date` / `taille` / `size`) → GRISÉE + libellée.**
Là, l'option est rendue, `disabled`, `opacity-40 cursor-not-allowed`, et surmontée d'un bandeau :

```jsx
<span className="absolute inset-x-0 bottom-0 bg-noir/70 py-1 text-center
                 text-[10px] font-semibold uppercase tracking-wider text-cream">Indisponible</span>
```

**Leur choix n'est donc pas un choix : c'est une incohérence.** Filtrage silencieux sur 4 étapes sur 5,
grisage explicite sur la 5ᵉ. Le grisage explicite est le meilleur des deux (et c'est aussi le seul rendu qui
porte `aria-pressed`) — voir §8.6.

---

## 5. Présentation des options — mesures

### 5.1 Desktop (relevé à 1280×720)

```css
--preview-h:  max(290px, calc(100svh - 520px))                                    /* = 290px ici */
--slot-size:  min(400px, 32vw, calc(var(--preview-h) - 52px), 36svh)              /* = 238px ici */
--carousel-step: var(--slot-size)                                                 /* = 238px, sans chevauchement */
/* vue zoomée */ --slot-size: min(650px, 60vw, 80svh)
```

| Élément | Taille mesurée | Forme | Verdict 44 px |
|---|---|---|---|
| Vignette d'option | **238 × 238 px** | carré sans cadre ni fond, image détourée sur crème | ✅ |
| Flèches de choix (‹ ›) | **48 × 48 px**, `left-4` / `right-4`, `hidden lg:grid` | carré bordé | ✅ desktop, **absentes en mobile** |
| Étape précédente / suivante | h **42 px** | rectangle bordé, texte 10 px | ❌ 42 < 44 |
| Partager | **42 × 42 px** | carré bordé | ❌ |
| Vue standard / Vue zoomée | **40 × 40 px**, empilés avec 8 px d'écart | carré bordé | ❌ 40 < 44 |
| Enregistrer / Ajouter au panier | h **49 px** | rectangle | ✅ |
| Pastille de libellé (*split*) | h **44 px**, min-w 96 px | rectangle, noir plein si sélectionné | ✅ (exactement 44) |

**Indication de la sélection — le point faible.** Dans le carrousel, la sélection n'est signalée que par
`opacity: 0` sur la vignette (remplacée visuellement par la montre composée). Aucun `aria-pressed`, aucun
`role="radio"`, aucun `aria-checked`, pas de cadre, pas de puce. Dans le *split layout* en revanche :
`aria-pressed`, bordure `border-noir` sur la vignette, pastille inversée en noir.

**Libellés.** Dans le carrousel, le nom de l'option n'apparaît **qu'au survol** : `<span>` 11 px, `600`,
`letter-spacing 0.55px`, `translate(-50%, -38px)` sous la vignette, `opacity 0 → 1` en 200 ms avec
**600 ms de délai de survol**, offset vertical piloté par `tooltipOffsetY` (−50 boîtier, −90 cadran,
−100 aiguilles). En dehors du survol, le seul endroit où lire le nom des pièces est la ligne de récapitulatif.

**Focus clavier — mesuré.** Aucune classe `focus-visible:*` sur les boutons du configurateur (les utilitaires
shadcn existent dans la feuille mais ne sont pas appliqués ici) : on retombe sur l'anneau UA de Chrome,
`outline: auto 1px`. Pire, en tabulant on atterrit sur l'option **sélectionnée**, dont le bouton est à
`opacity: 0` → **l'anneau de focus est invisible** (vérifié : `matches(':focus-visible') === true`,
`opacity === '0'`). Le carrousel a 8 arrêts de tabulation sans `tabindex` glissant, sans `role="radiogroup"`,
et **aucun `keydown`** dans le composant → **les flèches du clavier ne font rien**.

**Contrastes calculés sur le rendu** (crème `#FEFAF1`, encre `#202020`, barre `#E8E2D4`) :
encre/crème **15,6:1** ✅ ; encre/barre **12,6:1** ✅ ; **bouton désactivé à `opacity: .3` → 1,9:1** ❌
(couleur effective ≈ `#BBB9B2`) — « Étape précédente » à l'étape 1 et les flèches en bout de course sont
quasi illisibles.

### 5.2 Mobile 375 × 812

```css
@media (max-width:1023px){
  [data-conf-preview][data-zoom=normal]{
    --slot-size: min(350px, 70vw, 52svh)!important;        /* = 262,5px */
    --preview-h: max(300px, calc(100svh - 460px))!important; /* = 352px */
    --carousel-step: calc(var(--slot-size) * .73)!important;  /* = 192px → chevauchement de 71px */
  }
  [data-conf-preview][data-zoom=zoomed]{ --slot-size: min(560px, 92vw, 85svh)!important }
}
```

Mesures relevées :

- Vignettes **263 × 263 px**, positions x = 56, 248, 440, 631… → **pas de 192 px, chevauchement de 71 px**.
  Zone de frappe utile ≈ **192 × 263 px** (le voisin suivant peint par-dessus). Très au-delà de 44 px. ✅
- **Aucun débordement horizontal** : `document.scrollWidth === innerWidth === 375` grâce à `overflow-x-clip`
  sur la section, alors que la dernière vignette est à `x = 1398`. ✅
- **Flèches supprimées** (`hidden lg:grid`) : la navigation ne se fait plus qu'au **swipe**, et le swipe est
  proprement implémenté — `touchstart` mémorise x/y, verrouillage d'axe à **8 px**, `preventDefault()`
  uniquement sur l'axe horizontal via un `touchmove` en `{passive:false}`, déclenchement à **40 px** de
  déplacement, désactivé en vue zoomée. Mais **aucune affordance** : ni points, ni compteur « 3 / 8 »,
  ni flèche. Une seule option voisine dépasse à droite, coupée par le bord ; rien à gauche.
- Boutons de zoom **40 × 40 px** posés **par-dessus** la vignette voisine, dans le couloir du pouce.
- Prix et « Ajouter au panier » relevés à **y = 1 086 et 1 147 px** pour un viewport de 812 : **le prix et le
  CTA sont sous la ligne de flottaison à chaque étape** ; la barre récap n'est pas *sticky*.
- **Le libellé de l'option n'est jamais lisible au doigt** (il est en `group-hover`) : sur mobile on choisit
  une pièce dont on ne connaît pas le nom avant de l'avoir sélectionnée.
- En-tête : les trois boutons passent sur deux lignes, « Partager » se retrouve seul, aligné à droite.

---

## 6. L'aboutissement

Dernière étape = dernier groupe d'options, **pas d'écran final**. Ce qui la signale : le bouton d'en-tête
devient « AJOUTER AU PANIER ». La barre permanente porte :

- `<h2>` nom du modèle ; ligne récap en capitales ; prix `tabular-nums` ;
- **prix = `basePrice + Σ priceModifier`**. Contrairement à ce que supposait la note du 24/07, **il y a des
  suppléments** : sur SEIKOAK les trois bracelets cuir portent `priceModifier: 1500` → **+15,00 €**
  (349 € → 364 €). Les 44 autres options de SEIKOAK sont à 0.
- promotion prévue mais **inactive** (`{active:false, discountPercent:15, label:"SOLDES"}`) : si activée,
  prix barré + badge noir « SOLDES » + prix remisé ;
- « ENREGISTRER LA CONFIGURATION » (h 49 px) → si non connecté, **toast** « Connectez-vous pour sauvegarder
  votre configuration. » avec action vers `/connexion?redirectTo=/configurateur/{slug}` ; si connecté,
  *server action* `saveConfiguration` ;
- « AJOUTER AU PANIER » (h 49 px).

**Partage** : modale (Radix Dialog) avec un `<input readOnly>` contenant
`https://goteia.fr/configurateur/seikoak?c=<base64(JSON des sélections)>`, un bouton copier 42 px, et des
liens WhatsApp / réseaux en h 42 px. Le payload décodé est exactement
`{"aiguilles":"argent","boitier":"argent","bracelet":"argent","cadran":"noir-et-argent","fond-boitier":"transparent"}`.
À l'ouverture, `?c=` est décodé et **chaque valeur est vérifiée contre le catalogue** avant d'être appliquée
(sinon défaut) — bonne hygiène.

### 6.1 Transmission au panier — ni variante, ni produit dédié

Pas de Shopify du tout : Next.js + Sanity + panier maison (store client). Le payload est un **produit
synthétique** :

```js
addItem({
  productId: `configurator:${slug}:${Object.values(selections).join('-')}`,
  slug, name, unitPrice: finalPrice,
  imageUrl: urlFor(conf.defaultImage).width(800).height(800).fit('crop').url(),  // image GÉNÉRIQUE du modèle
  variant: "Boîtier: Argent · Bracelet: Argent · Cadran: … · Fond de Boîtier: Transparent",
  configuratorSlug: slug,
  configuration: [{groupKey, groupLabel, choiceLabel, choiceValue}, …],
  layers: [{src /* w=600 */, scale, offsetX, offsetY, zIndex}, …]   // trié par zIndex
})
```

Deux points remarquables :
- la **liste des calques est embarquée dans la ligne de panier**, en `w=600` : le panier et la commande peuvent
  **recomposer la montre** sans rejouer le configurateur ;
- mais l'`imageUrl` de la vignette de panier est l'**image générique du modèle**, pas la configuration
  choisie. Le client voit dans son panier une montre qui n'est pas la sienne.

Télémétrie PostHog : `configurator_opened`, `configurator_step_changed`, `configurator_completed`
(avec `durationSec`), `add_to_cart`, `configuration_shared`. Modèle d'instrumentation à reprendre tel quel.

---

## 7. Ce qui est perfectible chez eux

Classé par gravité pour nous.

1. **`prefers-reduced-motion` ignoré, y compris une animation infinie.** §3.1. Disqualifiant.
2. **Latence visible de l'aperçu : 0,44 à 1,05 s** entre le clic et la mise à jour des calques (§2.5). La
   pièce reste « en vol ». Le retard est *voulu* (250 ms) mais dérive sous charge.
3. **≈ 3,6 Mo d'images en 1,2 s au chargement** (110 requêtes CDN sur SEIKOJUST), sans `srcset`, sans `media`
   sur les `preload`, avec 22 balises `preload` en doublon et une taille `w=600` téléchargée puis jamais
   utilisée en desktop. Le principe est bon, la dose ne l'est pas.
4. **Images 4× surdimensionnées** : `w=1000` pour un emplacement de 238 px (desktop) ou 262 px (mobile).
5. **Retour arrière destructeur** : changer le boîtier réinitialise un bracelet **encore valide** (§1.4).
6. **Deux traitements contradictoires de l'incompatible** : absence silencieuse dans 4 étapes sur 5, grisage
   + « Indisponible » dans la 5ᵉ (§4.2).
7. **Sélection non exposée** : ni `aria-pressed`, ni `role="radio"`, ni cadre. La sélection est un
   `opacity: 0`.
8. **Anneau de focus invisible** sur l'élément sélectionné (bouton à `opacity: 0`) ; aucun style
   `focus-visible` propre ; **pas de navigation aux flèches** (aucun `keydown`).
9. **Contraste 1,9:1** sur tous les contrôles désactivés (`opacity: .3`).
10. **Mobile — libellés inaccessibles au doigt** : le nom de l'option n'existe qu'en `group-hover`.
11. **Mobile — pas d'affordance de swipe** : ni points, ni compteur, ni flèches ; une seule option voisine
    visible, coupée.
12. **Mobile — prix et CTA sous la ligne de flottaison** à chaque étape (barre non *sticky*).
13. **Mobile — les boutons de zoom (40 px, 8 px d'écart) recouvrent la vignette voisine** dans la zone de swipe.
14. **Animation de `width`/`height`** sur la pile d'images et le panneau *split*, plus un `transition-all`.
15. **Scintillement de transition d'étape** : entre deux étapes, l'ancienne grille *split* reste visible en
    fondu pendant ~500 ms par-dessus le nouveau carrousel (capturé à l'écran). État transitoire mal fermé.
16. **Étape escamotée mais choix conservé** : `FOND DE BOÎTIER PLEIN` figure au récapitulatif sans avoir
    jamais été proposé (§1.4).
17. **Vignette de panier générique** : la ligne de panier n'affiche pas la montre configurée (§6.1).
18. **Aucun état d'URL par étape** : ni retour navigateur, ni reprise après rechargement, ni étape partageable.
19. **Fautes de langue générées** : « Choisissez votre aiguilles », « Noir et Argent Chronoraph »,
    « Boitier chrono … » dans les libellés de règles.
20. **Le fond de boîtier est choisi devant une image de face** : l'aperçu ne montre jamais ce que l'option
    modifie.

### 7.1 Comparaison watchmodcustom.com (secondaire)

PrestaShop + module de personnalisation (`composition_element`, `visual-effect`, `ndk-lazy`). **Même famille
technique : 6 calques empilés à 1000 px**, `transition: all`, 316 images `.visual-effect` dans le DOM en
chargement paresseux. Mais l'expérience est nettement en dessous :

- **pas d'étapes** : tous les groupes empilés verticalement sur une page, aperçu *sticky* à gauche ;
- options en **boutons de texte pur** dans une grille 4 colonnes (« DJ Silver Full Rose Gold 39mm ») avec une
  icône « ? » pour voir l'image → l'image est cachée derrière une infobulle, exactement l'inverse de Goteia ;
- sélection = **remplissage ambre**, lisible mais hors charte ;
- **« The price will be calculated at the end of your configuration »** : prix masqué pendant tout le
  parcours. Anti-conversion.

**Ce que ça confirme** : la valeur de Goteia n'est pas dans le compositeur (que les deux ont), elle est dans
la **présentation visuelle des options et la mise à jour du prix en continu**.

---

## 8. Spécification d'implémentation NOIRMONT — adaptée à nos photos par coloris

### 8.1 La décision de fond : ne pas copier le compositeur

Nos visuels sont **une photo finie par coloris** (67 coloris produits en `nano_banana_pro` 4K,
cf. `2026-07-25-images-modeles-et-coloris.md`). Un empilement de calques exigerait :
une production **par pièce** en PNG détouré, un **calage sub-pixel commun** entre toutes les pièces, et un
recalage manuel `layerScale/offsetX/offsetY` par groupe (Goteia est à `1.02` partout — ce n'est pas un hasard,
c'est une correction). Ce n'est ni le pipeline ni le budget de production actuel, et un modèle génératif ne
produit pas des calques recalés.

**Donc : mécanisme = une photo par combinaison, servie depuis une table de correspondance.** Et cela n'oblige
à renoncer à rien de ce que Hakim a vu : §8.2 montre que leur mise en scène fonctionne *mieux* avec des
photos entières.

**La contrainte que ça impose, énoncée franchement.** Le nombre de photos = le nombre de combinaisons
atteignables. Le sourcing établit **528 combinaisons plateforme A + 900 plateforme B**
(`2026-07-31-sourcing-configurateur.md` §5). **On ne photographiera pas 1 428 montres.** L'architecture doit donc
séparer deux natures d'axes :

- **axes visuels** (ils changent la photo) : leur **produit cartésien doit rester ≤ au nombre de photos
  produites**. Cible de conception : **1 axe visuel principal (le coloris/la face) × 1 axe secondaire au plus**,
  soit un ordre de grandeur de 20 à 60 photos par plateforme ;
- **axes non visuels** (ils ne changent pas la photo) : taille 36/39, fond de boîtier, loupe cyclope.
  Traités comme Goteia traite `fond-boitier` : `previewLayer = null`, rendu *split*, **l'aperçu ne bouge pas**.
  Zéro coût de production, et c'est déjà validé en production chez eux.

Tout axe visuel supplémentaire multiplie le budget images : c'est l'arbitrage à poser à Hakim **avant** de
coder, pas après.

### 8.2 Le mécanisme visuel retenu — carrousel de photos entières

Reprise de leur géométrie, sans les calques :

- une rangée horizontale d'emplacements carrés de côté `--slot-size`, translatée en `transform: translateX`
  de `--carousel-step × index` ;
- chaque emplacement porte la **photo finie de la combinaison qui résulterait de ce choix** (et non la pièce
  isolée) : `photo(sélection courante avec cet axe remplacé par cette option)` ;
- l'emplacement **sélectionné est au centre** et affiche donc la montre actuelle ;
- **on supprime la double pile `eG`/`eO` et le `opacity: 0` sur la vignette sélectionnée** : ils n'existent
  que pour recomposer une pièce nue. Chez nous, la vignette sélectionnée **est déjà** l'aperçu.

Gains directs sur eux : plus de calage, plus de fondu croisé à orchestrer, plus de retard de 250 ms, chaque
image du carrousel est une **vraie photographie** (aucune pièce nue, aucune combinaison jamais montée à
l'écran), et le voisin qui dépasse montre déjà **le résultat** du prochain choix — ce que leur carrousel de
pièces nues ne montre pas.

Coût : les voisins pèsent plein tarif (une photo complète, pas une pièce). D'où §8.5.

### 8.3 Structure de l'entonnoir

- **Une page par plateforme** (`/pages/configurateur-<plateforme>`), le choix de plateforme en amont. Motif
  Goteia, il neutralise toute règle dimensionnelle.
- **Ordre des étapes : l'axe visuel principal d'abord.** Chez Goteia, `boitier` est premier parce qu'il
  déclenche les 29 règles. Chez nous, le premier choix doit être celui qui **détermine la photo**.
- **État d'étape dans l'URL** (`?e=2&c=<base64>`, `history.replaceState`) — corrige leur faiblesse nº 18 :
  retour navigateur, reprise après rechargement, étape partageable.
- **Compteur « Étape n / N » avec N = nombre d'étapes réellement atteignables** (leur `eW`, à reprendre), et
  **une étape escamotée ne figure pas au récapitulatif** (corrige nº 16).
- **Barre de récapitulatif permanente** dès l'étape 1 : nom, ligne des choix, prix, CTA. **Sticky en mobile**
  (`position: sticky; bottom: 0` + `padding-bottom: env(safe-area-inset-bottom)`) — corrige nº 12.
- **Pas d'écran final** : à la dernière étape le bouton « Étape suivante » devient « Ajouter au panier ».
  Leur choix est bon, on le garde.
- **Retour arrière non destructeur** — corrige nº 5 :
  ```
  à chaque changement d'un axe amont :
    pour chaque axe aval :
      si la valeur actuelle est encore autorisée → LA GARDER
      sinon → prendre la plus proche autorisée, et le signaler :
              toast « Bracelet Or Jaune n'existe pas avec ce boîtier — passé à Argent. »
  ```
  Ne jamais réinitialiser en silence un choix encore valide.

### 8.4 Moteur de règles

Reprendre leur schéma tel quel, il est bon :
`{ label, whenAxis, whenValue, thenAxis, thenAllowedValues[] }`, liste blanche, résolution par
**intersection** des règles déclenchées, `null` = pas de restriction. Stocké en **metafield JSON du produit**
(pas dans le Liquid), pour être éditable sans déploiement.

Deux ajouts à leur modèle :
- **déduplication au chargement** (ils ont une règle en double) ;
- **un booléen `visuel` par axe** : `visuel: false` ⇒ pas de photo associée, rendu *split*, aperçu figé.
  C'est leur `previewLayer: null` rendu explicite.

Et une **garde de cohérence au build** : tout couple (axe visuel, valeur) atteignable après règles **doit**
avoir une photo. Un script de vérification dans le pipeline de visuels, pas une découverte en production.

### 8.5 Stratégie de préchargement — sans défaire le chargement différé

Le point de tension : nous venons de passer les images en `loading="lazy"`. Un configurateur a besoin
d'images **immédiatement disponibles**, sinon l'aperçu scintille. Leur solution (`new Image()` sur *tout*,
≈ 3,6 Mo) marche mais coûte trop cher. Version dosée, **quatre règles** :

1. **Le différé reste la règle du site ; le configurateur est une exception locale, jamais globale.**
   `loading="lazy"` demeure partout ailleurs. À l'intérieur du configurateur :
   - photo courante de l'aperçu : `loading="eager"` + `fetchpriority="high"` + un seul
     `<link rel="preload" as="image" imagesrcset sizes>` (**une seule taille par écran**, pas trois) ;
   - **les deux voisins immédiats** du carrousel : `loading="eager"`, `fetchpriority="low"` ;
   - tout le reste : `loading="lazy"` + `decoding="async"`.
2. **Préchargement en anneau glissant, pas exhaustif.** À chaque changement de sélection, précharger la
   fenêtre `[index−2 … index+2]` de l'axe courant, plus **la seule photo par défaut de l'étape suivante**.
   Budget : **≤ 5 images en vol**, contre 94 chez eux.
   ```js
   const warm = (urls) => urls.forEach(u => {
     if (warmed.has(u)) return; warmed.add(u);
     const img = new Image(); img.decoding = 'async'; img.fetchPriority = 'low'; img.src = u;
   });
   ```
3. **Fenêtre de préchauffage différée et annulable.** Une fois l'aperçu peint et le réseau calme, tiédir le
   reste de l'axe courant — **jamais avant** :
   ```js
   if ('requestIdleCallback' in window
       && !matchMedia('(prefers-reduced-data: reduce)').matches
       && !(navigator.connection?.saveData)
       && !/(^|-)2g$/.test(navigator.connection?.effectiveType || '')) {
     requestIdleCallback(() => warm(resteDeLAxe), { timeout: 3000 });
   }
   ```
   Sur 2G / `saveData` / `prefers-reduced-data` : **aucun préchauffage**, seulement le différé natif.
4. **Interdiction de scintiller, garantie autrement que par le préchargement.** Le remplacement de la photo
   ne s'engage qu'une fois l'image décodée, et l'ancienne reste affichée jusque-là :
   ```js
   const img = new Image(); img.src = next;
   try { await img.decode(); } catch {}
   setPhoto(next);              // l'ancienne photo n'a jamais disparu entre-temps
   ```
   C'est ce que Goteia obtient par accident (cache d'un an + préchargement massif) et perd sous charge
   (§2.5). On l'obtient par construction, **sans les 3,6 Mo** — et le pire cas dégrade en attente courte,
   jamais en trou blanc.

Compléments : `<link rel="preconnect">` vers le CDN d'images ; **un seul format servi** (WebP/AVIF via
`srcset`) ; taille demandée **calée sur `--slot-size` × DPR** et non fixée à 1000 px (corrige nº 4) ;
`aspect-ratio` figé sur le conteneur pour un CLS nul ; réserve d'une **image de repli** par plateforme si une
combinaison n'a pas encore sa photo (avec libellé honnête, jamais une photo approchante silencieuse).

### 8.6 Options impossibles : **grisées et libellées, jamais absentes**

Décision : **on retient leur traitement *split* et on l'applique partout**, pas le filtrage silencieux.
Raisons : le client comprend qu'une option existe et pourquoi elle est fermée (argument de crédibilité
« chaque combinaison que nous proposons a été montée ») ; le nombre d'options reste stable d'un pas à l'autre,
donc le carrousel ne se réorganise pas sous le doigt ; et c'est le seul des deux rendus qui expose un état
accessible.

Mise en œuvre :
- `<button disabled aria-disabled="true">`, opacité **0,45 minimum** (leur `0,40` combiné à un texte gris
  descend sous 3:1 — **contraste à mesurer sur le rendu**, pas à supposer) ;
- bandeau court en bas de vignette : **« Indisponible »** (10–11 px, capitales, fond `noir-encre` à 70 %,
  texte `craie` — contraste à vérifier sur le rendu réel) ;
- **la raison au survol et au focus** — ce qu'ils n'ont pas : « Indisponible avec le boîtier Or Jaune » ;
- si un axe se retrouve à **une seule** option autorisée : l'étape est **escamotée** (leur `eW`) **et** le
  choix forcé est annoncé dans la ligne de récapitulatif comme imposé, pas comme choisi.

### 8.7 Mouvement — valeurs retenues

Uniquement `transform` et `opacity`. **Jamais `transition: all`, jamais `width`/`height` animées**
(corrige nº 14 ; le zoom se fait en `transform: scale()` sur un conteneur à taille fixe).

| Élément | Propriété | Durée | Fonction |
|---|---|---:|---|
| Rangée du carrousel | `transform: translate3d(x,0,0)` | **240 ms** | `cubic-bezier(0.2, 0, 0, 1)` |
| Photo de l'aperçu (changement de coloris) | `opacity` en fondu croisé | **200 ms** | `ease-out` |
| Vignette au survol / focus | `transform: scale(1.03)` + `opacity` | **160 ms** | `ease-out` |
| Apparition du carrousel au changement d'étape | `opacity` + `translateY(6px → 0)` | **240 ms** | `ease-out` |
| Panneau *split* | `opacity` + `transform: translateX(-8px → 0)` | **240 ms** | `ease-out` |
| Vue zoomée | `transform: scale()` | **320 ms** | `ease-out` |

**Pas de respiration infinie.** Leur `scale 1 → 1.012` toutes les 2,5 s est joli une fois et fatigant
ensuite, et c'est précisément l'animation qui ignore `prefers-reduced-motion`. Si Hakim la veut : **une seule
passe à l'arrivée sur la page**, jamais en boucle.

**`prefers-reduced-motion` respecté — non négociable** (corrige nº 1) :

```css
@media (prefers-reduced-motion: reduce) {
  .cfg-track, .cfg-photo, .cfg-slot, .cfg-panel { transition: none !important; animation: none !important; }
}
```
Et si un moteur d'animation JS est utilisé, il doit être branché sur la préférence (l'équivalent du
`MotionConfig reducedMotion="user"` que Goteia n'a pas posé). Le carrousel **saute** alors à sa position :
le résultat reste correct, la mise à jour de la photo reste instantanée.

### 8.8 Présentation des options — valeurs retenues

| Élément | Cible | Note |
|---|---|---|
| Vignette d'option | carré, `--slot-size` : desktop `min(360px, 30vw, calc(var(--preview-h) - 56px))` ; mobile `min(300px, 72vw, 46svh)` | forme **carrée**, cohérente avec les *swatches* NOIRMONT existants |
| Chevauchement mobile | `--carousel-step: calc(var(--slot-size) * .78)` | laisse **deux** voisins perceptibles, pas un seul coupé |
| **Toute cible tactile** | **≥ 44 × 44 px** | corrige leurs 40 et 42 px : navigation d'étape, partage, zoom, copier |
| Boutons de zoom | **44 × 44 px**, écart **8 px minimum**, **hors du couloir de swipe** (en en-tête, pas en surimpression) | corrige nº 13 |
| Libellé de l'option | **toujours visible sous la vignette** sur mobile ; au survol/focus en desktop, **sans délai de 600 ms** | corrige nº 10 |
| Sélection | **`aria-pressed` (ou `role="radio"` + `aria-checked`) + bordure `noir-encre` 2 px + pastille de libellé inversée** | jamais un simple `opacity: 0` (corrige nº 7) |
| Anneau de focus | **visible, `outline: 2px solid vert-jura; outline-offset: 2px`**, jamais sur un élément à `opacity: 0` | corrige nº 8 |
| Clavier | `role="radiogroup"`, **`tabindex` glissant** (un seul arrêt pour tout le groupe), **flèches ← → pour changer d'option**, `Home`/`End` | corrige nº 8 |
| Affordance mobile | **compteur « 3 / 8 »** sous le carrousel + points, et **flèches ≥ 44 px conservées en mobile** | corrige nº 11 |
| État désactivé | opacité **≥ 0,45**, contraste **mesuré sur le rendu** | corrige nº 9 (leur 1,9:1) |
| Débordement | `overflow-x: clip` sur le conteneur, `scrollWidth === innerWidth` vérifié à 320, 375 et 430 px | leur point fort, à conserver |

Palette : `craie #FAFAF7` en fond d'aperçu, `noir-encre #0B0B0C` pour texte et bordures, `vert-jura #1E3A2F`
réservé aux points de décision (CTA, sélection, anneau de focus), `laiton #A98E5F` en filet seulement —
conforme à `brand-tokens-noirmont.json`. **Tous les contrastes à mesurer sur le rendu final**, y compris
l'état désactivé, le bandeau « Indisponible » et le libellé 11 px.

### 8.9 Aboutissement et panier

- **Prix visible en continu** (leur point fort face à watchmodcustom) : `prix de base + Σ suppléments`,
  `tabular-nums`, mis à jour à chaque choix.
- **Supplément par option assumé** : leur `priceModifier` (+15 € sur le cuir) est un bon motif, à garder pour
  les pièces réellement plus chères.
- **Transmission au panier — nous sommes sur Shopify, donc dans l'ordre de préférence** :
  1. **variante Shopify réelle** quand la combinaison correspond à une variante existante (cas des axes
     visuels bornés du §8.1) : stock, prix, image de variante et analytics natifs — nettement supérieur à leur
     produit synthétique ;
  2. sinon **produit « configuré » unique + `line item properties`** portant chaque axe en clair
     (`_Boîtier`, `_Cadran`, …) plus un `_config` compact pour reconstruire l'état, et un
     `Selling plan`/supplément via un produit d'appoint si le prix diffère.
- **Vignette de panier = la photo de la combinaison choisie** (corrige nº 17). C'est immédiat chez nous, la
  photo existe déjà : c'est un avantage direct du modèle photo-par-combinaison sur leur modèle en calques.
- **Lien de partage** `?c=<base64>` avec **validation de chaque valeur contre le catalogue** à l'ouverture
  (leur hygiène, à copier), plus repli sur le défaut si une valeur a disparu.
- **Télémétrie** : `configurateur_ouvert`, `etape_changee`, `option_choisie`, `configurateur_termine`
  (avec durée), `partage`, `ajout_panier`. Leur jeu d'événements est le bon.

### 8.10 Recette de vérification avant livraison

1. **375 px** : `document.scrollWidth === 375` sur chaque étape ; prix et CTA visibles sans défilement ;
   toutes les cibles mesurées **≥ 44 px** (mesure au `getBoundingClientRect`, pas à l'œil).
2. **`prefers-reduced-motion: reduce` activé** : aucune transition, aucune animation, aucune boucle ; le
   parcours reste entièrement utilisable.
3. **Clavier seul** : parcourir les 5 étapes, changer d'option aux flèches, atteindre « Ajouter au panier ».
   **Anneau de focus visible à chaque arrêt.**
4. **Réseau bridé « Slow 4G », cache vide** : changer 10 fois d'option — **zéro image blanche, zéro
   scintillement**, le remplacement attend `decode()`.
5. **Budget images** : ≤ 5 images en vol à tout instant, **≤ 600 ko** transférés au premier rendu de l'étape 1
   (référence adverse : ≈ 3,6 Mo).
6. **Contrastes mesurés sur le rendu** : texte courant, libellé 11 px, état désactivé, bandeau
   « Indisponible », pastille sélectionnée.
7. **Cohérence des données** : chaque combinaison atteignable après règles possède une photo ; aucune règle en
   double ; aucun axe visuel sans photo.
8. **Retour arrière** : revenir sur l'axe amont **ne perd aucun choix aval encore valide** ; toute correction
   forcée est annoncée.

---

## Annexe — d'où viennent les chiffres

- Données de configuration et règles : dataset Sanity public,
  `https://uihp5v6f.apicdn.sanity.io/v2023-05-03/data/query/production?query=*[_type=="configurator"]` —
  lecture seule.
- Logique, durées, fonctions d'accélération, préchargement, payload panier : chunk client
  `https://goteia.fr/_next/static/chunks/0djodmx8fwfh2.js` (composant `ConfiguratorClient`).
- Géométrie, tailles, contrastes : `getBoundingClientRect` / `getComputedStyle` sur la page rendue en
  1280×720, 1600×900 et 375×812.
- Séquence d'animation : `MutationObserver` horodaté sur `[data-conf-preview]`, trois mesures.
- Poids et cache des images : `fetch` avec l'en-tête `Accept` du navigateur sur
  `cdn.sanity.io/.../<hash>.png?w=600|1000|1600&q=80&auto=format`.
- Volumétrie réseau : `performance.getEntriesByType('resource')` et l'entrée `navigation`.

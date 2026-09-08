# Production des visuels — Cosy Cat House (UK), lot 1

**Document de mission autoportant.** Il complète, pour cette boutique, la spécification permanente
`docs/codex-handoff/15-CODEX-EXECUTANT-IMAGES.md` (DA §3, contraintes §4, QA §5, livraison §6). La spec
prévoit des **surcharges de DA** par l'ordre (§3 « sauf surcharge explicite ») : ce brief en fournit
(fond, scènes, formats). Il **ne suspend aucune contrainte permanente** : il les complète par des
contraintes propres à ce produit (§2 bis). Le produit n'est pas une montre ; les règles écrites pour les
cadrans (stérilité, orientation cadran lisible) se lisent ici sur l'objet réel : aucun lettrage sur le
tissu, abri posé sur ses pieds, toit en haut, porte lisible.

Date : 08/09/2026. Répertoire : `boutique-pipeline/boutique-cosycathouse/`.

---

## 0. La mission en trois phrases

Cosy Cat House vend au Royaume-Uni **un abri extérieur isolé pour chat** : un seul produit, une seule
variante (Large, gris). La boutique est montée, mais **tous les emplacements image sont vides** (hero,
galerie produit, 4 blocs bénéfices, carte collection). Ton travail : produire ces images **sur le disque**,
à partir de la photo fournisseur, avec une mise en scène maison. Tu ne touches jamais à la boutique.

## 1. Le produit, tel qu'il est (vérité produit)

Source unique : `boutique-cosycathouse/assets/source/1005010759559289/sku-gris.jpg` (800 × 800).
Les deux autres fichiers du dossier (`sku-noir.jpg`, `sku-vert.jpg`) sont des coloris **non vendus** :
ne les utilise pas. Le dossier `assets/source/1005009960200806/` est un **autre modèle** (blanc, porte en
arche) : ne l'utilise pas.

Ce que la photo montre, et qui doit rester **identique** sur chaque image :
- Corps cubique en **tissu Oxford gris anthracite**, texture tissée visible.
- **Toit à deux pans** débordant, dont le dessous est doublé d'un **film réfléchissant argenté** (visible
  sous les débords du toit).
- **Porte carrée à rabat** sur la face avant, rabat en tissu gris avec le même film argenté au dos ; la
  porte est décalée vers la gauche de la face.
- **Fenêtre** rectangulaire sur le côté droit, doublée du même film argenté.
- **Quatre pieds tubulaires noirs** (structure tube, pieds surélevés d'environ 10–12 cm), embouts noirs.
- Une **cordelette noire** pend sur la face avant (elle peut disparaître dans une mise en scène).
- Dimensions extérieures : 55 × 45 × 40 cm — à respecter en proportion avec un chat adulte
  (un chat domestique moyen fait ~45 cm du museau à la base de la queue : l'abri est un peu plus large
  que long qu'un chat).

Interdits produit : pas de toit d'une autre forme, pas de porte en arche, pas de couleur autre que gris,
pas de pieds en bois, pas de chauffage ni de câble, pas de coussin visible à l'intérieur (non fourni),
pas d'accessoire inventé.

## 2. Direction artistique (surcharge de la spec §3)

- **Fond studio** : crème uni `#FFF7ED` (couleur de fond du site), lumière douce latérale haute-gauche,
  une seule ombre portée diffuse. Pas de dégradé pierre/craie ici.
- **Scènes** : jardin britannique réaliste en automne ou début d'hiver — pelouse humide, patio en dalles,
  terrasse en bois, sous un abri ou contre un mur de brique, un peu de buée ou de rosée, lumière de fin
  de journée ou d'aube grise. **Rien d'exagéré** : pas de blizzard, pas de neige épaisse, pas de
  cheminée de Noël, pas d'ambiance catalogue de luxe. Un vrai jardin de banlieue anglaise.
- **Chats** : autorisés et souhaités sur certains slots. Chat domestique adulte ordinaire (tigré gris,
  roux, noir et blanc), jamais de race « de prestige », jamais de chaton. Le chat est **à côté**, **à
  l'entrée** (tête sortant du rabat) ou **entrant** ; jamais deux chats dans l'abri. Anatomie contrôlée
  (yeux, pattes, queue, proportions).
- **Aucun texte, aucun logo, aucun badge, aucune note ou étoile** dans l'image. Pas d'étiquette, pas de
  filigrane, pas de mention de marque sur le tissu.
- **Aucune promesse visuelle non tenue** : pas de renard repoussé, pas de neige sur le toit qui « glisse »,
  pas de thermomètre, pas de radiateur, pas d'effet de chaleur rouge. Le confort se suggère par un chat
  au sec et un sol humide autour.
- Rendu : photo réaliste de type éditorial e-commerce, ni illustration, ni 3D lisse.

## 2 bis. Bloc d'orientation propre à ce produit (à inclure dans chaque prompt)

```
MANDATORY ORIENTATION — the shelter stands on its four black tubular legs, roof at the TOP,
gable ridge horizontal, square door flap on the front face, side window on the right face.
Never upside down, never on its side, never floating. Keep the reference three-quarter framing
unless the slot says otherwise; if in doubt, keep the reference framing and move the camera.
```

## 3. Le manifeste (ce que tu livres)

Handle `insulated-outdoor-cat-house`, SKU `CCH-L-GREY`. Un fichier par slot, nommé exactement comme
le champ `fichier` de l'ordre. Formats : `galerie` = carré 2048 × 2048 ; `hero` = 2048 × 1152 (16:9) ;
`benefice` = 2048 × 1536 (4:3) ; `carte` = carré 2048 × 2048. JPEG qualité ~90.

| Slot | Fichier | Contenu attendu |
|---|---|---|
| `face` | `…-face.jpg` | Produit seul, trois-quarts avant comme la source, fond crème uni. Image principale de la fiche. |
| `situation-jardin` | `…-situation-jardin.jpg` | L'abri posé sur un patio ou contre un mur de brique, pelouse humide, fin de journée grise ; sans chat. |
| `chat-entree` | `…-chat-entree.jpg` | Un chat tigré passant la tête par le rabat, ou assis juste devant l'entrée, même décor jardin. |
| `macro-doublure` | `…-macro-doublure.jpg` | Détail rapproché du dessous du toit et du rabat : film argenté et tissu Oxford, très net. |
| `pieds-sureleves` | `…-pieds-sureleves.jpg` | Angle bas montrant les quatre pieds noirs et l'espace sous l'abri, sur dalles mouillées. |
| `hero` | `…-hero.jpg` | 16:9, sujet **décalé à droite**, tiers gauche calme (fond de pelouse/mur flou) pour recevoir le titre en HTML ; abri dans un jardin au crépuscule, chat assis à l'entrée. Mobile-safe : le produit doit rester visible dans un recadrage central 9:16. |
| `benefice-chaleur` | `…-benefice-chaleur.jpg` | 4:3, l'abri au petit matin avec buée/rosée autour, chat couché à l'intérieur vu par la porte (tête visible, au sec). |
| `benefice-sec` | `…-benefice-sec.jpg` | 4:3, sol trempé, flaques, l'abri surélevé au sec sur ses pieds. |
| `benefice-installation` | `…-benefice-installation.jpg` | 4:3, l'abri **monté**, posé par deux mains adultes dans un coin abrité de terrasse (mains sur le toit ou les côtés, sans visage). Aucun état plié ni en cours de dépliage : la source ne le documente pas. |
| `benefice-refuge` | `…-benefice-refuge.jpg` | 4:3, l'abri dans un coin abrité (sous un banc, contre une haie), chat assis dedans, regard vers l'extérieur ; ambiance calme, aucune menace figurée. |
| `carte` | `…-carte.jpg` | Carré, produit seul sur fond crème, cadrage un peu plus large que `face`. |

## 4. QA avant livraison (en plus de la spec §5)

1. **Fidélité** : toit à deux pans + film argenté, porte carrée à rabat, fenêtre latérale, quatre pieds
   noirs, tissu gris — contrôle image par image contre la source.
2. **Chats** : compte les pattes, vérifie yeux et queue, une seule tête par chat. Au moindre défaut :
   régénère (jamais d'inpainting).
3. **Mains** (slot `benefice-installation`) : compte les doigts.
4. **Aucun texte/logo/badge** au zoom, y compris sur le tissu et les embouts.
5. **Planche de contrôle** ≥ 740 px par vignette, toutes images côte à côte : homogénéité de la couleur
   du tissu et de la lumière.
6. **Hero** : vérifier qu'un recadrage central 9:16 garde le produit et le chat.

## 5. Livraison

Dossier : `boutique-cosycathouse/livraisons/visuels-lot1-2026-09-08/` ; manifeste `manifeste-realise.json`
indexé `handle` + `sku` + `slot` ; rejets dans `rejected/` avec motif ; enveloppe de résultat dans
`ordres/pour-codex/resultats/`. Le branchement Shopify est fait ensuite côté Claude Code, après QA.

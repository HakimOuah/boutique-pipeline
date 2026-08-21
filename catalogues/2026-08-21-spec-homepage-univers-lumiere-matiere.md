# Spec homepage UNIVERS — Lumière Matière

**Date :** 21/08/2026  
**Auteur :** Claude Fable 5 (skill `webdesign-boutiques` exécuté : persona → moteur ui-ux-pro-max → DA figée → overlay Horizon)  
**Statut :** spec opérationnelle, prête à coller sur Horizon dès que la boutique Shopify existe. **Aucun thème implémenté, rien committé.**  
**Périmètre :** homepage + nav + tokens + mapping images + checklist admin. PDP = rappel d'ordre seulement.  
**Sources :** charte LM §5 (`2026-08-20-branding-audit-orysbain-lumiere-matiere.md`), VOC (`2026-08-20-voc-personas-objections-orysbain-lm.md`), inventaire visuels (`2026-08-21-inventaire-visuels-lumiere-matiere.md`), QA visuels (`2026-08-21-qa-visuels-lumiere-matiere.md`), pages légales (`catalogues/lumierematiere/pages/`), ossature Horizon (`docs/horizon-product-page-reference/homepage/HORIZON-HOMEPAGE-NOTION.md` + `templates/index.json`), structure mille-et-une-nuisette.com (fetch 21/08).

---

## 0. Décisions tranchées (résumé)

1. **9 tuiles collections sur la homepage, en deux bandes** : grille « matières » de **6 tuiles** (bambou, rotin, bois, pierre, verre, effet cristal) + bande « pièce & forme » de **3 tuiles** (lustres anneau, lustres salon, plafonniers). Métal (8) et déco (8) restent accessibles par la nav et `/collections/all` — la cover métal est illisible comme « métal » (voile translucide), elle ne porte pas une tuile.
   *Alternative envisagée puis écartée : une seule grille de 8 tuiles matières (ajouter métal + déco). Écartée car la cover métal trahit son titre, et 8 tuiles diluent la lecture « galerie de matières » ; 6 + 3 raconte mieux : d'abord la matière, ensuite la pièce.*
2. **Collections à 1 SKU** : **aucun bloc homepage, aucune entrée de menu.**
   - `Lustres statement` (1 SKU, sputnik noir/doré) → le produit est **ajouté aussi à la collection Lustres salon**.
   - `Suspensions modernes` (1 SKU, barre LED métal noir) → le produit est **ajouté aussi à la collection Suspensions métal**.
   - Les deux collections d'origine **restent publiées** (SEO / filtres / URLs du feed), simplement invisibles dans les menus.
3. **Hero conservé sur `lumierematiere-home-hero.jpg`** (bambou LM-009 au-dessus d'une table — la meilleure scène du lot, et elle parle aux deux personas). Le problème « trio mono-bambou » est traité par la ventilation : macro `home-matiere.jpg` réservée au bloc éditorial mi-page, `home-table.jpg` déplacé en teaser « Notre histoire » en bas de page (option : le sortir de la homepage). Substituts hero prêts si Hakim trouve ça trop bambou : cover **rotin** ou cover **pierre** (chemins en §7).
4. **« Cristal » → « Effet cristal » partout dans l'UI** (tuile, mega, titre de collection) tant qu'aucune preuve de cristal véritable n'existe — aligné FAQ déjà écrite (« Effet cristal … ce que montrent les photos »).
5. **Newsletter sans remise au lancement.** Un « -10 % » ne s'affiche que si Hakim crée réellement le code + l'automatisation (étape optionnelle en checklist §10). Aucune promesse non branchée.
6. **Échange de deux covers entre elles** (assignation seulement, zéro régénération) : l'image livrée « plafonniers » montre un sputnik **suspendu**, l'image « lustres salon » montre un plafonnier **plaqué au plafond**. On croise les deux — chaque tuile redevient exacte (§7).
7. **13 sections Horizon** de l'annonce au footer, ordre en §5. Une seule liste produits au lancement (« Autour de 199 € », collection manuelle à créer) ; des rangées produits par matière viendront plus tard, quand il y aura des ventes pour les trier.
8. **Croisement QA 21/08** : ne pas uploader LM-086 (`plafonnier-led-led-728204`, 5 JPEG REJECT — montage inventé). Cover bois = RETOUCH (lumière trop orange) : tuile homepage day one quand même, à remplacer dès qu'un g4 KEEP (ex. LM-037) est promu en image de collection. Cover verre = RETOUCH lisible « laiton d'abord » : acceptable en tuile, pas prioritaire ads.

---

## 1. DA appliquée — moteur ui-ux-pro-max, retenu / écarté

Requêtes lancées le 21/08 : `--domain product "lighting pendant chandelier gallery materials luxury"`, `--domain style "Minimalism"`, `--domain color "warm neutral gallery editorial luxury"`, `--domain ux "checkout conversion trust"` (et variantes).

**Retenu :**
- Fiche **Museum/Gallery** : « Minimalism + Motion-Driven », landing « Storytelling-Driven + Feature-Rich », neutres + accents d'exposition. C'est exactement le positionnement « galerie de matières » : fonds neutres qui laissent les photos chaudes porter la couleur, motion discret.
- Palette **Museum/Gallery** (fond neutre clair, texte quasi-noir, **un seul accent**) : valide la charte LM telle quelle — papier `#F6F3EC`, charbon `#24211B`, ambre `#C08A2D` en accent unique. **On ne touche pas aux hex.**
- Landing « Feature-Rich Showcase » (fiche E-commerce Luxury) : homepage en blocs riches plutôt qu'un hero unique — cohérent avec la référence mille-et-une-nuisette.
- Guidelines maison du skill (la recherche `--domain ux` n'a **pas trouvé de correspondance en base**, fallback assumé sur les règles du skill) : cibles tactiles ≥ 44 px, contraste 4,5:1, CLS < 0,1, coins 4–8 px max, icônes SVG jamais d'emoji, QA mobile 375 px d'abord.

**Écarté (et pourquoi) :**
- **Liquid Glass / Glassmorphism / Aurora UI** (recommandation n°1 des fiches Luxury) : effets de verre décoratifs qui concurrenceraient les photos de luminaires allumés — la lumière doit venir des produits, pas de l'UI.
- **Black + Gold #FFD700** : trop bijouterie ; l'ambre `#C08A2D` est plus mat, plus « matière ».
- **Exaggerated Minimalism** (typo 12rem) : registre agence/portfolio, pas une boutique 149–299 € qui doit rassurer Camille et Nina.
- **Vibrant & Block-based / pop stickers** : la règle maison le réserve aux niches créatives/DIY. LM est une galerie 149–299 €, pas un univers créatif — luxury/gallery sobre, oui ; stickers, non.

---

## 2. Ce qu'on transpose de mille-et-une-nuisette (structure seulement)

Constaté au fetch du 21/08 (~777 SKU chez eux) :

| Leur bloc | Ce qu'on en garde pour LM (121 SKU) |
|---|---|
| Bandeau 3 messages (paiement, livraison, discrétion) | Bandeau 2 messages vérifiables (livraison offerte, retours 30 j) |
| H1 court + tagline de catégorie (« Lingerie de nuit · Cocooning · Séduction ») | Sur-titre « galerie de matières » + H1 promesse |
| « Nos catégories » = grille de tuiles | Grille matières 6 tuiles + bande pièce/forme 3 tuiles |
| « Meilleures ventes » (rangée produits) | « Autour de 199 € » (pas de bestsellers day one : la sélection prix remplace) |
| 4 gros blocs catégorie : titre + **paragraphe sensoriel** + 3 produits + « Voir tous les… » | Le paragraphe sensoriel vit dans le bloc éditorial « La matière fait la lumière » ; les rangées produits par matière = phase 2, après premières ventes |
| Journal / blog | **Pas au lancement** (rien à publier — ne pas simuler la profondeur) |
| Newsletter « club -10 % » | Newsletter **sans remise** tant que le code n'existe pas |
| 5 items de réassurance footer | 3 colonnes réassurance + footer confiance (SIRET, policies, paiement) |

Leur DA lingerie (roses, promos barrées partout) n'est **pas** transposée. Pas de compteurs, pas de fausses promos au lancement.

---

## 3. Collections & blocs homepage

Rappel catalogue : 121 SKU, 13 collections CSV. Prix : 64 × 199 € · 50 × 249 € · 6 × 299 € · 1 × 149 €.

| Collection CSV | SKU | Homepage | Nav | Notes |
|---|---:|---|---|---|
| Suspensions bambou | 16 | Tuile grille matières #1 | Mega « Par matière » | |
| Suspensions rotin | 14 | Tuile #2 | Mega | Cover la plus forte du lot — substitut hero n°1 |
| Suspensions bois | 12 | Tuile #3 | Mega | |
| Suspensions pierre | 10 | Tuile #4 | Mega | Cover travertin très « galerie » — substitut hero n°2 |
| Suspensions verre | 10 | Tuile #5 | Mega | Cover = laiton + globes opale : acceptable (verre opalin), à surveiller |
| Lustres cristal | 7 | Tuile #6, label **« Effet cristal »** | Mega, label « Effet cristal » | Renommer le titre de collection (checklist) |
| Lustres anneau | 12 | Tuile bande pièce/forme #1 | Mega « Lustres » | |
| Lustres salon | 12 | Tuile bande #2 | Mega « Lustres » | Reçoit en plus le SKU statement |
| Plafonniers | 10 | Tuile bande #3 | Entrée directe nav | |
| Suspensions métal | 8 | — (nav seulement) | Mega « Par matière » | Reçoit en plus le SKU modernes ; cover illisible → pas de tuile |
| Suspensions déco | 8 | — (nav seulement) | Mega « Par matière » | |
| Lustres statement | **1** | — | — | Publiée (SEO), hors menus ; produit dupliqué dans Lustres salon |
| Suspensions modernes | **1** | — | — | Publiée (SEO), hors menus ; produit dupliqué dans Suspensions métal |

**Sous-collections d'intention** : rien n'est inventé au lancement. « Salon » et « Plafonniers » couvrent déjà la pièce et le type de pose avec du stock réel. Une collection automatique « Au-dessus de la table » (tag `table` sur les suspensions Ø ≥ 40 cm à câble) est possible en phase 2 — elle demande un passage de tags sur les fiches, listée en option dans la checklist, **pas** un bloc homepage day one.

---

## 4. Navigation

### Menu principal (`main-menu`)

1. **Accueil** → `/`
2. **Par matière** → `/collections/all` — mega menu :
   - Bambou → collection bambou
   - Rotin → collection rotin
   - Bois → collection bois
   - Pierre → collection pierre
   - Verre → collection verre
   - Métal → collection métal
   - Déco colorée → collection déco
3. **Lustres** → collection lustres salon — sous-menu :
   - Lustres anneau
   - Lustres salon
   - Effet cristal → collection cristal
4. **Plafonniers** → collection plafonniers
5. **Notre histoire** → `/pages/notre-histoire`
6. **FAQ** → `/pages/faq`
7. **Contact** → `/pages/contact`

Réglages header Horizon (repris de la référence BV) : logo à gauche, menu à gauche, recherche à droite, header fixe, style mega « produits mis en avant » (Horizon affiche des vignettes produit dans le mega — brancher la collection bambou par défaut). **Masquer les sélecteurs pays/langue** : offre France uniquement.

*Handles définitifs = ceux générés à l'import CSV ; vérifier chaque lien de menu après création des collections (checklist §10).*

---

## 5. Homepage — sections Horizon dans l'ordre, copy collable

Toutes les images ci-dessous : chemins complets et alt en §7. Type Horizon = composant natif de la référence (`hero`, `collection-list`, `product-list`, `section` + blocs, `email-signup`).

### 5.1 Bandeau d'annonce — `header-announcements`

Deux messages en rotation (vitesse 5, comme BV) :

1. `Livraison offerte en France métropolitaine — sans minimum`
2. `Retours sous 30 jours · Paiement sécurisé`

Fond charbon `#24211B`, texte papier `#F6F3EC`. Les deux promesses sont couvertes par les policies déjà écrites.

### 5.2 Header — `header`

Logo `lumierematiere-logo-primary-charbon.png` (hauteur 36 px desktop / 28 px mobile), fond papier. Nav §4.

### 5.3 Hero — `hero` (seul H1 de la page)

| Élément | Contenu |
|---|---|
| Image | `lumierematiere-home-hero.jpg` (desktop **et** mobile — livrée en 1:1, régler le point focal sur la suspension ; si le recadrage desktop coupe mal, activer un média mobile dédié plus tard) |
| Sur-titre | `Lumière Matière — galerie de matières` |
| H1 | `Chaque matière a sa lumière` |
| Sous-titre | `Suspensions et lustres choisis pour leur matière : bambou, rotin, bois, pierre, verre. Le matériau change la lumière — choisissez d'abord l'ambiance.` |
| CTA | `Explorer les matières` → `/collections/all` |
| Overlay | Charbon `#24211B` à ~25 % (lisibilité du texte sur photo chaude) |
| Hauteur | Moyenne, padding 72 px haut/bas (réglage BV conservé) |

### 5.4 Grille matières — `collection-list` (6 tuiles)

- Sur-titre : `Par matière`
- Titre (H2) : `Choisissez la matière, vous choisissez la lumière`
- 6 tuiles, 3 colonnes desktop / 2 mobile, images carrées, titre superposé, overlay charbon léger :
  1. `Bambou` → collection bambou — cover bambou
  2. `Rotin` → collection rotin — cover rotin
  3. `Bois` → collection bois — cover bois
  4. `Pierre` → collection pierre — cover pierre
  5. `Verre` → collection verre — cover verre
  6. `Effet cristal` → collection cristal — cover cristal
- Lien bas de section : `Voir tout le catalogue` → `/collections/all`

### 5.5 Bien choisir (preuves VOC) — `section` + 3 groupes icône/titre/texte

Titre (H2) : `Bien choisir, sans mauvaise surprise` — icônes SVG 40 px charbon, jamais d'emoji.

| Icône (SVG) | Titre | Texte |
|---|---|---|
| Règle / Ø | `Le bon diamètre` | `Diamètre et hauteur sont sur chaque fiche. Au-dessus d'une table, restez nettement plus étroit que le plateau — les photos compressent l'échelle, mesurez avant de choisir.` |
| Ampoule | `Ampoule : c'est écrit` | `LED intégrée ou douille E27/E14 selon le modèle — la fiche le précise avant l'achat. Si douille, une LED blanc chaud donne l'ambiance des photos.` |
| Câble / plafond | `Câble et pose` | `Raccordement au circuit plafond, câble souvent réglable à la rosace : un câble long n'est pas un défaut, il s'ajuste à votre hauteur. Pas à l'aise avec l'électricité ? Faites appel à un professionnel.` |

*(Reprend mot pour mot l'esprit des réponses FAQ déjà validées — Ø, ampoule, câble = les 3 objections VOC n°1.)*

### 5.6 Autour de 199 € — `product-list`

- Titre (H2) : `Autour de 199 €`
- Sous-texte : `Une sélection du catalogue à 199 €, livraison offerte.`
- Collection : `selection-199` (**manuelle, à créer**) — 6 SKU KEEP à 199 €, 6 familles, **hors LM-034** (RETOUCH orange) et **hors LM-086** (REJECT) :
  1. `LM-003` suspension-bambou-942503 — bambou
  2. `LM-017` suspension-rotin-605780 — rotin
  3. `LM-037` suspension-bois-led-582321 — bois
  4. `LM-043` suspension-effet-pierre-led-338324 — pierre
  5. `LM-076` suspension-verre-446435 — verre
  6. `LM-053` lustre-anneau-led-led-noir-dore-024410 — anneau
- Bouton : `Tout voir` → `/collections/selection-199`
- Disposition : carrousel, 4 colonnes desktop / 2 mobile, carte = image (g1), titre, prix. Fond soft `#EFE8DC` pour détacher la bande.

### 5.7 Par pièce & par forme — `collection-list` (3 tuiles)

- Titre (H2) : `Par pièce et par forme`
- 3 tuiles, 3 colonnes desktop / rangée scrollable mobile :
  1. `Lustres anneau` → collection anneau — cover anneau
  2. `Lustres salon` → collection salon — **cover livrée « plafonniers »** (sputnik doré suspendu, voir échange §7)
  3. `Plafonniers` → collection plafonniers — **cover livrée « lustres salon »** (plafonnier organique plaqué)

### 5.8 Éditorial matière → lumière — `section` (texte + image 50/50)

- Image : `lumierematiere-home-matiere.jpg` (macro tissage bambou allumé)
- Sur-titre : `Notre parti pris`
- Titre (H2) : `La matière fait la lumière`
- Texte : `Un tissage de bambou raye la lumière, un globe de verre la diffuse, la pierre la rend dense et calme. C'est pour ça que nos collections portent des noms de matières, pas des noms de tendances. Et parce que le rendu dépend aussi de votre ampoule et de votre pièce, chaque fiche décrit la matière visible — sans sur-promettre.`
- CTA : `Voir les suspensions bambou` → collection bambou (l'image est un bambou du catalogue — le CTA reste honnête)

### 5.9 FAQ homepage — `section` + `accordion` (6 lignes)

Titre (H2) : `Vos questions avant d'acheter` — intro : `Les réponses complètes sont dans la FAQ et les pages Politiques ; en cas d'écart, ces pages prévalent.`

1. **Comment choisir le bon diamètre ?** — `Chaque fiche donne le diamètre et la hauteur. Au-dessus d'une table, restez nettement plus étroit que le plateau. Un doute ? Écrivez-nous : contact@lumierematiere.fr.`
2. **L'ampoule est-elle fournie ?** — `Selon le modèle : LED intégrée (rien à ajouter) ou douille E27/E14 — c'est précisé sur chaque fiche. Si douille, prévoyez une LED blanc chaud.`
3. **Le câble est très long, c'est normal ?** — `Souvent oui : beaucoup de suspensions se règlent à la rosace. On ajuste le câble à votre hauteur sous plafond à la pose.`
4. **Faut-il un électricien ?** — `Le raccordement se fait au circuit plafond. Si vous n'êtes pas à l'aise avec l'électricité, faites appel à un professionnel — courant coupé avant toute intervention.`
5. **Quels sont les délais et frais de livraison ?** — `Livraison offerte en France métropolitaine. Commande avant 16h (heure de Paris) : préparation sous 1 à 2 jours ouvrés, total estimé 7 à 17 jours ouvrés selon l'entrepôt de départ.`
6. **Et si le colis arrive abîmé, ou si je change d'avis ?** — `Ouvrez dès réception et photographiez tout dommage : la casse transport est prise en charge sans frais de retour. Et vous avez 30 jours pour retourner un article qui ne convient pas, au-delà des 14 jours légaux.`

*(Alignées mot pour mot sur `pages/faq.md` et les policies — ne pas reformuler les chiffres.)*

### 5.10 Réassurance — `section` + 3 colonnes icône/titre/texte

| Icône (SVG) | Titre | Texte |
|---|---|---|
| Camion | `Livraison offerte` | `France métropolitaine, sans minimum. Total estimé : 7 à 17 jours ouvrés, suivi envoyé à l'expédition.` |
| Flèche retour | `Retours 30 jours` | `30 jours pour retourner, en plus des 14 jours légaux. Remboursement sous 7 jours ouvrés après contrôle.` |
| Cadenas | `Paiement sécurisé, SAV en français` | `Transactions chiffrées. Une équipe joignable du lundi au vendredi, 10h–18h (Paris), réponse sous 1 à 2 jours ouvrés.` |

### 5.11 Notre histoire (teaser) — `section` (texte + image)

- Image : `lumierematiere-home-table.jpg` (scène table dressée) — *option si la page paraît trop bambou : passer ce bloc en texte seul sur fond soft `#EFE8DC` et garder l'image pour la page Notre histoire.*
- Titre (H2) : `Une galerie de matières, pas un bazar de styles`
- Texte : `Lumière Matière part d'une idée simple : ce n'est pas « une lampe de plus » qui compte, c'est la matière qui transforme la lumière. Nous sélectionnons chaque modèle pour ce qu'il fait à la lumière — et nous restons joignables après l'achat.`
- CTA : `Notre histoire` → `/pages/notre-histoire`

### 5.12 Newsletter — `section` + `email-signup`

- Titre : `La lumière, matière par matière`
- Texte : `Un e-mail de temps en temps : nouvelles pièces, conseils de diamètre et d'ampoule. Rien de plus.`
- Bouton : `Je m'inscris`
- Fond soft `#EFE8DC`.
- **Pas de « -10 % » tant que le code de réduction et l'e-mail de bienvenue n'existent pas.** Si Hakim les crée (checklist), le titre devient `-10 % sur votre première commande` — jamais avant.

### 5.13 Footer — `footer` + `footer-utilities`

Fond charbon `#24211B`, logo `lumierematiere-logo-inverse-blanc.png`, texte papier.

- **Colonne coordonnées** : `Lumière Matière — une marque OH Ventures` · contact@lumierematiere.fr · +33 7 56 82 80 94 · 47 rue Vivienne, 75002 Paris · `SAV : lun–ven, 10h–18h (Paris)`
- **Menu Informations** : Notre histoire · FAQ · Contact · Livraison · Retours & remboursements
- **Menu Légal** : CGV (sert de mentions légales : l'éditeur est au §1, pas de fichier `mentions-legales.md` séparé) · Politique de confidentialité · Conditions de paiement
- **Newsletter** : même formulaire/mécanique que §5.12 (mêmes règles, pas de remise fantôme)
- **Signaux confiance** : icônes des moyens de paiement réellement actifs (à cocher après activation Shopify Payments/PayPal — ne pas afficher un logo non actif) + ligne légale : `OH Ventures, SASU au capital de 1 000 € — SIRET 10315725100010 — TVA FR55103157251`
- Footer utilitaire : copyright auto, « Powered by Shopify » masqué, liens policies.

---

## 6. Tokens Horizon (réglages du thème)

### Couleurs (charte figée — ne pas modifier les hex)

| Rôle Horizon | Hex | Usage |
|---|---|---|
| Fond principal | `#F6F3EC` | Page (papier) |
| Texte principal | `#24211B` | Titres et body (charbon) |
| Accent | `#C08A2D` | Hover, focus, soulignés, prix mis en avant (ambre) |
| Ligne / bordures | `#DDD6C8` | Séparateurs, bordures cartes |
| Fond secondaire | `#EFE8DC` | Bandes 199 €, newsletter, fonds collection (soft) |

**Boutons** : primaire = fond charbon `#24211B`, texte `#F6F3EC`, hover fond ambre `#C08A2D` ; secondaire = contour charbon sur papier, hover ambre. Jamais de CTA ambre plein en primaire (sinon tout brille).

### Typographies

- Display / titres : **Young Serif** (marque, H1–H2, titres de tuiles)
- UI / texte : **Instrument Sans** (nav, body, prix, boutons — graisse 500 pour nav et boutons)
- Les deux sont des Google Fonts sous licence OFL. **Si absentes du sélecteur de polices Shopify**, les charger en polices personnalisées dans les assets du thème (woff2 + une règle CSS) — étape en checklist. Ne pas se rabattre sur un serif générique sans le noter.

### Forme & motion

- Coins 4–8 px max, pas de pills.
- Motion sobre : fade du hero, soft reveal des tuiles matières au scroll, hover glow ambre léger sur les tuiles, underline nav. Rien qui clignote.
- Largeur globale : `narrow` (réglage BV conservé).

---

## 7. Mapping images Codex → sections

Base : `boutique-pipeline/catalogues/lumierematiere/livraisons-visuels-codex/brand/` (dossier gitignoré, fichiers vérifiés à l'œil le 21/08).

| Fichier | Affectation | Alt suggéré | Note |
|---|---|---|---|
| `lumierematiere-logo-primary-charbon.png` | Header (§5.2) | `Lumière Matière` | 2000×620, fond papier |
| `lumierematiere-logo-inverse-blanc.png` | Footer (§5.13) | `Lumière Matière` | Sur fond charbon |
| `lumierematiere-logo-mono-ambre.png` | Réserve (favicon secondaire, e-mails) | — | Pas sur la homepage |
| `lumierematiere-favicon-512.png` | Favicon boutique | — | |
| `lumierematiere-home-hero.jpg` | Hero (§5.3) | `Suspension bambou allumée au-dessus d'une table à manger` | 1:1 — régler le point focal sur la suspension |
| `lumierematiere-home-matiere.jpg` | Éditorial (§5.8) | `Détail du tissage bambou d'une suspension allumée` | La macro « matière » la plus on-message du lot |
| `lumierematiere-home-table.jpg` | Teaser histoire (§5.11) | `Table dressée sous une suspension bambou` | Option : réserver à la page Notre histoire si la homepage paraît trop bambou |
| `lumierematiere-collection-suspensions-bambou.jpg` | Tuile Bambou (§5.4) | `Suspension bambou tressé` | |
| `lumierematiere-collection-suspensions-rotin.jpg` | Tuile Rotin (§5.4) | `Suspension cloche en rotin tressé` | **Substitut hero n°1** si le hero bambou est jugé trop mono |
| `lumierematiere-collection-suspensions-bois.jpg` | Tuile Bois (§5.4) | `Suspension tonneau en bois` | |
| `lumierematiere-collection-suspensions-pierre.jpg` | Tuile Pierre (§5.4) | `Suspensions en travertin` | **Substitut hero n°2** — la plus « galerie » du lot |
| `lumierematiere-collection-suspensions-verre.jpg` | Tuile Verre (§5.4) | `Suspension laiton à globes de verre opalin` | Lecture « verre » moyenne (le laiton domine) — acceptable, à surveiller en phase 2 |
| `lumierematiere-collection-lustres-cristal.jpg` | Tuile Effet cristal (§5.4) | `Lustre à anneaux effet cristal` | Label UI = « Effet cristal », jamais « cristal » seul |
| `lumierematiere-collection-lustres-anneau.jpg` | Tuile Lustres anneau (§5.7) | `Lustre à trois anneaux LED dorés` | |
| `lumierematiere-collection-plafonniers.jpg` | **Tuile Lustres salon** (§5.7) | `Lustre sputnik doré` | **Échangée** : l'image montre un luminaire suspendu, pas un plafonnier |
| `lumierematiere-collection-lustres-salon.jpg` | **Tuile Plafonniers** (§5.7) | `Plafonnier LED organique dans un salon` | **Échangée** : l'image montre un plafonnier plaqué au plafond |
| `lumierematiere-collection-suspensions-metal.jpg` | Non utilisée en homepage | — | Voile translucide, ne lit pas « métal » ; sert d'image de collection (page collection métal) faute de mieux — pas de régénération demandée |
| `lumierematiere-collection-suspensions-deco.jpg` | Non utilisée en homepage | — | Image de la page collection déco |
| `lumierematiere-collection-lustres-statement.jpg` | Non utilisée | — | Collection hors menus |
| `lumierematiere-collection-suspensions-modernes.jpg` | Non utilisée | — | Collection hors menus |
| `produits/<handle>/g1.jpg` (121 dossiers) | Cartes produit (§5.6 + mega) | Titre produit | Dynamique via les fiches |

---

## 8. PDP — rappel d'ordre (pas une spec complète)

Ordre des modules, aligné charte §5 et VOC : **1. Matière → lumière** (photo + une phrase : ce que la matière fait à la lumière) → **2. Dimensions** (Ø, hauteur, longueur de câble — tôt, avant le fold si possible) → **3. Ampoule & pose** (LED intégrée ou douille, raccord plafond, câble réglable) → **4. Confiance** (livraison offerte 7–17 j ouvrés, retours 30 j, SAV). Reprendre l'ossature PDP Horizon de la référence (`horizon-product-page-reference/`), ne pas la réinventer.

---

## 9. Ce que fait Hakim dans l'admin Shopify (une fois la boutique créée)

Dans l'ordre :

1. **Réglages généraux** : nom `Lumière Matière`, e-mail `contact@lumierematiere.fr`, adresse OH Ventures, devise EUR, fuseau Paris. Brancher le domaine `lumierematiere.fr` quand acheté.
2. **Thème Horizon** : installer, puis appliquer les tokens §6 (couleurs, boutons, largeur `narrow`). Typos : chercher Young Serif / Instrument Sans dans le sélecteur ; si absentes, uploader les woff2 en polices personnalisées.
3. **Logos** : header primary charbon, footer inverse blanc, favicon 512.
4. **Import catalogue** : CSV DSers (121 SKU), privilégier les variantes UE au mapping. Vérifier que les 13 collections se créent avec les bons handles. **Ne pas uploader** les 5 JPEG de `plafonnier-led-led-728204` (LM-086, REJECT QA). Les 120 autres handles : g1→g5 dans l'ordre.
5. **Collections** :
   - assigner les covers (avec l'**échange salon ↔ plafonniers** du §7) comme images de collection ;
   - renommer « Lustres cristal » → **« Lustres effet cristal »** (titre + éventuel H1 de page collection) ;
   - créer la collection manuelle **`selection-199`** avec les 6 SKU listés en §5.6 ;
   - ajouter le SKU statement à « Lustres salon » et le SKU modernes à « Suspensions métal » ; laisser les deux collections d'origine publiées mais hors menus.
6. **Menus** : `main-menu` (§4) + menus footer Informations / Légal. Vérifier chaque lien après création des collections (handles réels).
7. **Pages** : coller `catalogues/lumierematiere/pages/` (histoire, FAQ, contact, policies). La FAQ pointe déjà vers `/pages/contact` — coller `contact.md`. Pas de page Mentions légales dédiée : le menu Légal ouvre les CGV. Vérifier le domaine dans les URLs internes.
8. **Homepage** : monter les 13 sections §5 dans l'ordre, coller la copy telle quelle, brancher images et collections.
9. **Bandeau + footer confiance** : messages §5.1 ; ligne SIRET/TVA §5.13 ; n'afficher que les icônes des moyens de paiement réellement activés (Shopify Payments, PayPal…).
10. **Newsletter** : au choix — laisser la version sans remise (rien à faire), ou créer le code -10 % + automatisation e-mail de bienvenue **avant** de changer le titre.
11. **Divers conformité** : masquer sélecteurs pays/langue, vérifier l'adhésion CM2C pour `lumierematiere.fr` (contrat par site ?), « Powered by Shopify » masqué.
12. **Option phase 2** (pas bloquant) : tags `table` pour une collection automatique « Au-dessus de la table » ; rangées produits par matière quand les bestsellers existent.

*(GMC/Ads : rien ici volontairement, hors signaux de confiance footer déjà couverts — le skill `gmc-acceptance` prendra le relais.)*

## QA avant publication (mobile d'abord, 375 px)

- [ ] Un seul H1 (le hero) ; tous les titres de sections en H2.
- [ ] Hero lisible en 1:1 mobile, point focal sur la suspension, CLS < 0,1 (dimensions d'images réservées).
- [ ] Tuiles et boutons ≥ 44 px, contraste texte/fond ≥ 4,5:1 (charbon sur papier passe ; vérifier texte sur overlay photo).
- [ ] Tous les CTA mènent à une collection/page publiée ; zéro lien vers statement/modernes dans les menus.
- [ ] Aucun « cristal » sans « effet », aucun « artisanal », aucune remise ou urgence non branchée, aucun avis inventé.
- [ ] Chiffres ops partout identiques : 16h Paris · 1–2 j · 6–15 j · 7–17 j · 30 j · 14 j · 7 j ouvrés remboursement.
- [ ] Pas de scroll horizontal ; icônes SVG uniquement.

---

**Rappels d'hygiène** : dossier visuels gitignoré (ne pas forcer au commit) ; ne rien régénérer des 605 images PDP ; Orysbain non concerné par ce document.

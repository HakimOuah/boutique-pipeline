# Audit UX / UI — Lumière Matière — 04/09/2026

Demande Hakim : « le menu sur desktop est trop long, pas optimisé, sans logo » + l'aspect global.
Relevé sur le site live à 1440 × 900 (desktop) et 375 × 812 (mobile), home, collection
`suspensions-rotin`, fiche `suspension-rotin-623305`, méga-menu et menu mobile ouverts.
Lecture seule : rien n'a été modifié. Skills : `webdesign-boutiques` + grille d'interface.

## Verdict en une phrase

**La direction artistique est juste et la copie est excellente ; les défauts sont structurels
— navigation, hiérarchie et redondances — pas esthétiques.** Le menu et le logo ont **une seule
cause**, et elle se corrige sans toucher au CSS.

---

## 1. Le header desktop — une cause, deux symptômes

### Ce qu'on voit

À 1440 px, le menu **passe sur deux lignes** : neuf entrées sur la première, « Suivre votre
commande » orphelin sur la seconde. Et **aucun logo** : la barre commence par « Accueil ».

### Ce qui se passe réellement

Le logo **est dans le HTML** (`lumierematiere-logo-primary-charbon.png`, 348 × 108 natif,
`--logo-width: 116px`), il se charge (`display: block`, `opacity: 1`, `visibility: visible`)…
et il est rendu à **0 px de large**. Mesuré au navigateur : `img.box = [110, 15, 0, 36]`, et son
lien parent `.header__logo` fait aussi 0 px.

La cause est dans la grille du thème Fullstack :

```css
.header__layout--logo-left { display: grid; grid-template-columns: 1fr auto 1fr; gap: 1.5rem }
.header__menu-desktop-list  { display: flex; flex-wrap: wrap; }
```

Trois colonnes : logo (`1fr`) · menu (`auto`) · icônes (`1fr`). Avec **dix entrées de premier
niveau**, la colonne `auto` du menu réclame toute la largeur (mesurée : 1 108 px sur 1 440),
la colonne du logo est écrasée à 0, et comme la liste est en `flex-wrap: wrap`, le menu déborde
sur une deuxième ligne par-dessus le marché.

**Le logo n'est pas absent, il est écrasé par le menu.** Réduire le menu le fait réapparaître.

Sur mobile, tout va bien : le logo passe par `--logo-width-mobile: 90px` dans un layout centré.
C'est pour ça que le problème ne se voit que sur desktop.

### Correction — deux niveaux

**A. Structurel, à faire de toute façon : ramener le menu à 5 entrées.** Aujourd'hui le premier
niveau mélange trois natures — des facettes (Par pièce, Par matière), des types de produit
(Lustres, Plafonniers LED, Appliques murales) et des liens utilitaires (Accueil, Notre histoire,
FAQ, Contact, Suivre votre commande). Dix entrées, dont quatre n'ont rien à faire dans une
navigation d'achat.

| Aujourd'hui (10) | Cible (5) |
|---|---|
| Accueil | *(supprimé : c'est le rôle du logo)* |
| Par pièce ▾ | **Par pièce ▾** — reste en premier, décision du 26/08 (la pièce fait 38,8 % du trafic Lustria contre 13,8 % pour la matière) |
| Par matière ▾ | **Par matière ▾** — en méga-menu visuel (voir §2) |
| Lustres ▾ | **Lustres ▾** |
| Plafonniers LED ▾ | **Plafonniers & appliques ▾** — fusion avec Appliques murales |
| Appliques murales | *(fusionné ci-dessus)* |
| Notre histoire | → footer, colonne « La boutique » (déjà présent) |
| FAQ | → footer, colonne « Informations pratiques » (déjà présent) — ou **Conseils ▾** si on veut garder la pédagogie en tête |
| Contact | → footer (déjà présent) |
| Suivre votre commande | → **icône ou lien utilitaire** à droite, à côté de la recherche et du panier |

Cinq entrées tiennent sur une ligne à 1024 px, et la colonne `1fr` du logo retrouve sa largeur.

**B. Filet de sécurité, réglage de thème : passer le header en « logo à gauche, menu à gauche ».**
Le thème possède le layout `header__layout--logo-left-menu-left` avec
`grid-template-columns: auto auto 1fr` : le logo prend sa largeur naturelle **avant** que le menu
se serve. Classe présente dans le CSS compilé — à vérifier que le personnalisateur l'expose.
Ça garantit le logo même si le menu regrossit un jour ; ça ne règle pas les deux lignes.

Faire A. B est une ceinture en plus.

---

## 2. Le méga-menu « Par matière » est une liste texte

Ouvert, « Par matière » affiche une colonne étroite : Bambou · Rotin · Osier · Bois · Pierre ·
Verre · Métal · Déco colorée. Pas d'image, pas de texture.

Pour une boutique dont **l'axe est la matière** — le hero dit « c'est la matière qui décide de
l'ambiance » — c'est la promesse de marque qui manque à l'endroit où elle devrait être la plus
visible. Une vignette par matière (les visuels `brand/lumierematiere-collection-*.jpg` existent
déjà) transformerait ce menu en argument.

---

## 3. « Matière » : trois comptes différents sur le même site

C'est le défaut de cohérence le plus visible une fois qu'on l'a vu.

| Surface | Matières |
|---|---|
| Cartes de la section « Par matière » (home) | **5** : bambou, rotin, bois, pierre, verre |
| Texte de cette même section | « **Six** matières au catalogue : bambou, rotin, bois, pierre, verre et **effet cristal** » |
| Menu « Par matière » | **8** : + osier, métal, déco colorée |

« Effet cristal » n'existe plus : `lustres-pampilles` est à 0 produit et dépubliée depuis le
26/08. Le texte promet une sixième carte qui n'est pas là. À l'inverse, osier, métal et déco
colorée sont au menu mais pas en home.

**Décider une liste canonique et l'appliquer aux trois surfaces.** Proposition : les 8 du menu
sont trop (osier = 2 produits), les 5 cartes sont la bonne base ; ajouter métal (6 produits,
vraie collection) → **6 matières partout**, et retirer « effet cristal » du texte.

---

## 4. Hiérarchie de la home : elle contredit la stratégie « pièce d'abord »

Le 26/08, le menu a été réordonné « Par pièce **avant** Par matière » sur la base du trafic
Lustria. La home dit l'inverse :

| Position | Section | Hauteur |
|---|---|---:|
| 2 | « Par matière » — 5 cartes | **1 086 px** |
| 7 | « Par pièce et par forme » — 3 cartes | 599 px |

Et les 3 cartes de « Par pièce et par forme » sont… **Lustres anneau, Lustres salon, Plafonniers
LED** : des formes, aucune pièce. Salon, Chambre, Cuisine n'ont pas de carte sur la home alors
qu'elles ouvrent le menu.

Ce n'est pas forcément à changer — « matière » est l'identité, « pièce » est le trafic — mais
c'est un choix à faire consciemment. Au minimum : renommer la section 7 « Par forme », ou y mettre
de vraies cartes pièce.

---

## 5. Redondances qui allongent la home (5 960 px)

La réassurance apparaît **quatre fois** sur la même page :

1. bandeau d'annonce — livraison offerte, retours 30 j
2. puces du hero — paiement sécurisé, SAV
3. section « Ce qu'on regarde avant de mettre une pièce en ligne » (695 px)
4. bande de 4 blocs avant le footer — livraison, paiement, retours, SAV (351 px)

Et **deux formulaires newsletter** à la suite : la section « Un e-mail de temps en temps »
(319 px) puis « Recevoir nos e-mails » dans le footer, 300 px plus bas.

Garder 3 (c'est la mieux écrite) et le footer ; supprimer la bande 4 et la section newsletter.
Gain : ~700 px et un message qui ne se dilue plus.

---

## 6. Mobile

**Le hero.** Le titre « Chaque matière a sa lumière » en blanc chevauche l'abat-jour bambou
éclairé — « a sa » et « lumière » passent sur la partie la plus claire de l'image. Sur desktop le
texte est à gauche et la lampe à droite, ça ne se voit pas ; sur mobile ils se superposent.
Correction : un dégradé sombre derrière le texte, ou le texte sous l'image.

**Le bandeau d'annonce** passe sur deux lignes avec ses flèches : ~130 px de bandeau + ~130 px de
header = **260 px de chrome** avant le premier pixel de contenu sur un écran de 812. Raccourcir
la phrase pour tenir sur une ligne : « Livraison offerte en France · Retours 30 j ».

**Le logo** à 90 × 28 px est lisible mais timide. 120 × 37 tiendrait entre les icônes.

**Le menu mobile** est propre : tiroir plein écran, lignes de ~100 px, très bonnes cibles
tactiles. Il souffre seulement de la même longueur que le desktop — la cible à 5 entrées
l'allège d'elle-même, et les liens utilitaires peuvent y rester en bas, en plus petit.

---

## 7. Ce qui est bon — et à ne pas « corriger »

- **La DA.** Papier `#F6F3EC`, charbon `#24211B`, ambre `#C08A2D`, Young Serif pour les titres,
  Instrument Sans pour le texte à 16 px. Chaud, calme, cohérent d'une page à l'autre. La règle
  maison « pop et mouvement » vaut pour les niches DIY ; pour des luminaires à 150–250 €, ce
  registre est le bon. Ne pas le rendre plus « vibrant ».
- **La copie.** « Où voulez-vous de la lumière ? », « Bien choisir en trois étapes », les
  descriptions de collection (« comparé au bambou, le rotin tire vers le miel ») — c'est de la
  pédagogie au particulier, exactement ce que demande le pipeline. C'est la meilleure chose du site.
- **La page collection.** Bloc éditorial texte + image en tête, filtres et tri, grille propre.
- **La fiche produit.** Titre, prix, chips de variantes lisibles (surtout depuis le renommage
  P4/P5 du jour), bouton panier, Shop Pay, pictos de paiement, accordéons. Structure CRO saine.
- **Le footer.** Quatre colonnes, coordonnées complètes, logo présent, pictos cohérents.

---

## 8. Détails techniques relevés au passage

- **Icônes en police Material Symbols.** Le texte de la page contient littéralement `verified`,
  `priority`, `lightbulb`, `home`, `architecture`, `delivery_truck_speed`, `encrypted`,
  `volunteer_activism`, `forum`, `arrow_forward`… Ce sont les ligatures de la police d'icônes,
  chargée depuis `fonts.googleapis.com`. Deux conséquences : si la police tarde ou est bloquée,
  l'utilisateur voit les mots à la place des icônes ; et un lecteur d'écran lit ces mots. Règle
  maison : icônes SVG inline. Non urgent, mais à inscrire.
- **Prix `€199`** — symbole avant le nombre. Déjà relevé le 31/08 (`money_format`), toujours là.
  `199 €` est la convention française ; ça se règle dans Paramètres → Général.
- **Deux dépendances externes** dans le head : Google Fonts (icônes) et le CSS Shopify des
  wallets. Rien d'anormal.

---

## 9. Ordre de traitement proposé

| # | Action | Effet | Où |
|---|---|---|---|
| 1 | Menu à 5 entrées, utilitaires déplacés (§1-A) | Logo visible, une ligne, nav lisible | Navigation Shopify + réglage header |
| 2 | Layout « logo à gauche, menu à gauche » (§1-B) | Logo garanti | Personnalisateur de thème |
| 3 | Liste canonique des matières sur les 3 surfaces (§3) | Cohérence de l'axe de marque | Section home + texte + menu |
| 4 | Hero mobile : dégradé ou texte sous l'image (§6) | Lisibilité du titre | Section `image_banner` |
| 5 | Supprimer bande de réassurance n°4 + section newsletter (§5) | −700 px, message net | Sections home |
| 6 | Bandeau d'annonce sur une ligne (§6) | −65 px de chrome mobile | Section `announcement_bar` |
| 7 | Méga-menu visuel « Par matière » (§2) | La promesse de marque dans le menu | Réglage menu du thème |
| 8 | « Par pièce et par forme » → renommer ou vraies cartes pièce (§4) | Cohérence stratégie | Section home |
| 9 | Icônes SVG, `money_format` (§8) | Robustesse, convention FR | Thème / Paramètres |

Les actions 1 à 6 sont des réglages de contenu et de sections ; aucune ne demande de code.
7 et 9 touchent au thème : à faire sur une **copie non publiée**, publication par Hakim.

Aucune de ces corrections n'affecte les signaux GMC (identité, policies, délais, prix) — elles
peuvent se faire pendant la période de repos avant la review sans « changement brutal ».

## Limites de ce relevé

Le panneau navigateur était masqué pendant la session : les sections de la home sous la ligne de
flottaison n'ont pas pu être capturées en desktop (elles se révèlent au défilement). Leur
structure, hauteurs et textes ont été lus dans le DOM, pas vus. Le rendu du méga-menu, du menu
mobile, de la fiche et de la collection a bien été vu.

# Brief de rédaction — boutique rocking chair (France) — 14/09/2026

**À lire en entier avant d'écrire** :
1. Persona validé par Hakim le 14/09 : `personas/persona-rocking-chair-2026-09-14.md` (§1 douleurs, objections et langage ; §4 axe ; §5 implications et tableau objections → réponses).
2. Charte : `content/CHARTE-COPY-2026-09-14.md`.
3. Faits produit : `content/FAITS-FOURNISSEURS-2026-09-14.md`. C'est la **seule** source de chiffres et de caractéristiques.
4. Arborescence et wireframes : `sitemap.md`.

## Marque et société
- Nom de marque : Bercelou (décision Hakim du 14/09, `DECISIONS-2026-09-14.md`). Domaine : `bercelou.fr`.
- Société : OH Ventures (SASU), 47 rue Vivienne, 75002 Paris, SIREN 103 157 251, TVA FR55103157251, e-mail info@ohventures.fr, directeur de la publication Hakim Ouahabi. Médiateur : CM2C, 14 rue Saint Jean, 75017 Paris, https://www.cm2c.net/.
- Thèse (persona §4) : *le spécialiste qui choisit chaque fauteuil pour les vraies nuits avec un bébé (on s'y assoit, on berce en douceur, on se relève sans réveiller personne) et assez beau pour rester au salon ensuite.*
- Une seule action dominante par page.

## Règles absolues
1. **Aucun avis, note, compteur ou témoignage.** Les verbatims du persona servent à comprendre, jamais à afficher.
2. **Aucune caractéristique ni aucun chiffre absent des faits fournisseurs.** Si une donnée manque, la phrase ou la ligne disparaît (charte). Dans les brouillons, une donnée utile mais absente est signalée en commentaire de fin de fichier (`<!-- manque : hauteur d'assise -->`), jamais dans le texte.
3. **Promesses conditionnées** (persona §5) : « bascule silencieuse », « se relève facilement », « bouclette douce », « housse lavable » ne s'écrivent que si les faits le permettent.
4. **Guides offerts en ligne**, jamais « dans le colis ».
5. **Aucun vocabulaire médical**, pas de promesse de santé sur les relax.
6. **Mobile-first** : H1 ≤ 60 caractères, paragraphes ≤ 3 lignes, listes courtes. SEO : un mot-clé principal par page, meta title ≤ 60 caractères, meta description ≤ 155. Les mots-clés secondaires de la fiche se placent naturellement dans le sous-titre, les H3 et la FAQ.
7. **Format** : Markdown, un fichier par page, en français. Des scripts parsent les fichiers : garder exactement les titres de sections du gabarit.

## Gabarit fiche produit (`content/produits/<handle>.md`, ordre imposé)
```
**Mot-clé principal :** …
**Mots-clés secondaires :** …
**Meta title (≤60) :** … | Bercelou
**Meta description (≤155) :** …

## H1
## Sous-titre            (une phrase de transformation)
## Bloc d'achat          (4 bénéfices d'une ligne + micro-copy livraison · retours · garantie · paiement)
## Description
### <H3 douleur → réponse> ×4 à 5
## Dimensions            (tableau 2 colonnes : Mesure | Valeur ; uniquement les valeurs connues ; conseil de place)
## Caractéristiques      (tableau 2 colonnes : Caractéristique | Valeur)
## Entretien             (si la matière est connue)
## Livraison             (entrepôt, délai de la famille, colis, montage)
## FAQ                   (6 à 8 : **1. question** puis réponse)
## Images (ALT et rôle)  (6 : désir · usage · matière · dimensions cotées · situation · détail)
```

**H3 types à adapter à la famille** : « Pour les tétées de nuit » · « Vos bras et votre dos bien soutenus » · « Une bascule douce » · « Se relever en douceur » · « Une matière douce et facile à vivre » · « Il reste au salon après bébé » · « Un coin lecture en un instant » · « Sur la terrasse » · « Réglages et confort » (relax).

## Gabarit collection (`content/collections/<handle>.md`)
Mot-clé · meta title · meta description · H1 · intro de 60 à 100 mots (au-dessus de la grille) · texte d'aide au choix de 200 à 300 mots (sous la grille, en H2/H3, avec les critères du persona et les liens vers les guides) · FAQ de 3 questions.

## Pages (`content/pages/`)
- `accueil.md` (wireframe `sitemap.md`) ;
- `guide-bien-choisir-fauteuil-allaitement.md` ;
- `guide-rocking-chair-taille-place.md` ;
- `guide-entretien-bouclette-velours-lin.md` ;
- `faq.md` ;
- `livraison-retours.md` ;
- `garantie-sav.md` ;
- `qui-sommes-nous.md` ;
- `contact.md` ;
- `annonces.md` (barre d'annonce, 3 messages).

## Catalogue (44 fiches uniques, prix cible de l'onglet « Rocking chair »)

| Handle | ID AliExpress | Nom de travail | Prix | Coût DS | Collections | Mots-clés portés (volume) | Variantes éclatées |
|---|---|---|---|---|---|---|---|
| fauteuil-rocking-chair-teddy-dossier-haut | 1005012886082802 | fauteuil rocking chair teddy dossier haut | 199 € | 101.13 € | fauteuils à bascule | fauteuil rocking chair 1300 | 0 |
| fauteuil-a-bascule-allaitement-teddy | 1005010201578018 | fauteuil à bascule allaitement teddy | 179 € | 82.67 € | fauteuils à bascule, fauteuils d'allaitement, rocking chair design & scandinave | fauteuil à bascule confortable 320 · fauteuil à bascule allaitement 1900 · chaise d'allaitement 590 · rocking chair cocoon 170 | 0 |
| fauteuil-a-bascule-scandinave-velours-cotele | 1005012640407961 | fauteuil à bascule scandinave velours côtelé | 329 € | 184.52 € | fauteuils à bascule | fauteuil à bascule scandinave 210 | 0 |
| fauteuil-a-bascule-bois-massif | 1005012803890256 | fauteuil à bascule bois massif | 329 € | 183.93 € | fauteuils à bascule | fauteuil à bascule bois 210 | 1 |
| rocking-chair-vintage-velours | 1005011838576965 | rocking chair vintage velours | 229 € | 116.99 € | fauteuils à bascule, rocking chair design & scandinave | fauteuil à bascule salon 170 · rocking chair vintage 390 | 0 |
| fauteuil-qui-se-balance | 1005012620439685 | fauteuil qui se balance | 179 € | 104.96 € | fauteuils à bascule | fauteuil balance 170 | 0 |
| chaise-rocking-chair | 1005010240771968 | chaise rocking chair | 249 € | 133.95 € | chaises à bascule, rocking chair design & scandinave | chaise rocking chair 480 · rocking chair beige 170 | 2 |
| siege-a-bascule-rembourre | 1005011557882819 | siège à bascule rembourré | 249 € | 135.02 € | chaises à bascule | siège à bascule 480 | 0 |
| chaise-qui-se-balance | 1005012653961063 | chaise qui se balance | 179 € | 114.65 € | chaises à bascule | chaise qui se balance 320 | 2 |
| chaise-a-bascule-en-bois | 1005010263245255 | chaise à bascule en bois | 299 € | 162.05 € | chaises à bascule | chaise à bascule bois 170 | 0 |
| chaise-a-bascule-allaitement-velours | 1005013103645873 | chaise à bascule allaitement velours | 219 € | 149.83 € | fauteuils d'allaitement | chaise à bascule allaitement 590 | 0 |
| fauteuil-allaitement-chambre-bebe-avec-repose-pieds | 1005012822557916 | fauteuil allaitement chambre bébé avec repose-pieds | 299 € | 169.35 € | fauteuils d'allaitement | fauteuil allaitement chambre bebe 110 | 0 |
| fauteuil-allaitement-confortable-dossier-haut | 1005012399034232 | fauteuil allaitement confortable dossier haut | 299 € | 169.35 € | fauteuils d'allaitement | fauteuil confortable allaitement 110 | 0 |
| rocking-chair-blanc-teddy | 1005012929587244 | rocking chair blanc teddy | 199 € | 127.72 € | rocking chair design & scandinave | rocking chair blanc 390 | 0 |
| rocking-chair-moderne-inclinable | 1005012105192978 | rocking chair moderne inclinable | 269 € | 141.27 € | rocking chair design & scandinave | rocking chair moderne 170 | 0 |
| fauteuil-cocon-exterieur | 1005013011290288 | fauteuil cocon extérieur | 199 € | 94.73 € | fauteuils cocon | fauteuil cocon exterieur 140 | 0 |
| fauteuil-cocon-suspendu | 1005012269732576 | fauteuil cocon suspendu | 229 € | 118.41 € | fauteuils cocon | fauteuil cocon suspendu 110 | 1 |
| fauteuil-a-bascule-de-jardin | 1005011730563839 | fauteuil à bascule de jardin | 269 € | 165.39 € | fauteuils cocon, rocking chair extérieur | fauteuil à bascule jardin 590 | 0 |
| chaise-a-bascule-exterieur-coussin-impermeable | 1005012626302710 | chaise à bascule extérieur coussin imperméable | 249 € | 137.75 € | rocking chair extérieur | chaise à bascule extérieur 260 | 1 |
| rocking-chair-acacia | 1005012803904475 | rocking chair acacia | 279 € | 183.93 € | rocking chair extérieur |  | 1 |
| housse-de-protection-rocking-chair | 1005006353185058 | housse de protection rocking chair | 29 € | 10.68 € | rocking chair extérieur |  | 0 |
| rocking-chair-rotin | 1005012477518388 | rocking chair rotin | 249 € | 141.91 € | rocking chair bois & rotin | rocking chair rotin 1000 | 1 |
| fauteuil-a-bascule-rotin-et-coussin | 1005012627789726 | fauteuil à bascule rotin et coussin | 269 € | 148.58 € | rocking chair bois & rotin | fauteuil à bascule rotin 390 | 0 |
| rocking-chair-papasan-avec-pouf | 1005010552530016 | rocking chair papasan avec pouf | 259 € | 181.99 € | rocking chair bois & rotin |  | 2 |
| rocking-chair-bambou-pliable | 1005002888932994 | rocking chair bambou pliable | 269 € | 149.39 € | rocking chair bois & rotin |  | 0 |
| fauteuil-relax-electrique | 1005012054721103 | fauteuil relax électrique | 349 € | 162.99 € | fauteuils relax | fauteuil relax électrique 6600 · fauteuil relax confortable 480 | 0 |
| fauteuil-relax-moderne | 1005012454786223 | fauteuil relax moderne | 329 € | 160.55 € | fauteuils relax | fauteuil relax moderne 2400 | 0 |
| fauteuil-relax-manuel | 1005008598267746 | fauteuil relax manuel | 449 € | 290.46 € | fauteuils relax | fauteuil relax manuel 1900 | 0 |
| fauteuil-relax-cuir | 1005012780948146 | fauteuil relax cuir | 449 € | 242.84 € | fauteuils relax | fauteuil relax cuir 1600 | 0 |
| fauteuil-relax-design | 1005010018998756 | fauteuil relax design | 449 € | 289.87 € | fauteuils relax | fauteuil relax design 1600 | 4 |
| fauteuil-relax-de-salon | 1005012809448823 | fauteuil relax de salon | 399 € | 210.5 € | fauteuils relax | fauteuil relax salon 1000 | 0 |
| fauteuil-relax-pivotant | 1005012491845495 | fauteuil relax pivotant | 499 € | 387.99 € | fauteuils relax | fauteuil relax pivotant 720 | 0 |
| fauteuil-relax-scandinave | 1005012837772306 | fauteuil relax scandinave | 299 € | 155.57 € | fauteuils relax | fauteuil relax scandinave 720 | 0 |
| fauteuil-relax-exterieur-inclinable | 1005008174331532 | fauteuil relax extérieur inclinable | 129 € | 74.39 € | fauteuils relax de jardin |  | 0 |
| fauteuil-relax-a-bascule | 1005011808697791 | fauteuil relax à bascule | 249 € | 126.39 € | rocking chair relax & repose-pieds | fauteuil relax à bascule 210 | 1 |
| rocking-chair-avec-repose-pieds | 1005010240143897 | rocking chair avec repose-pieds | 139 € | 91.01 € | rocking chair relax & repose-pieds | rocking chair avec repose pied 210 | 0 |
| chaise-a-bascule-enfant | 1005008723043604 | chaise à bascule enfant | 149 € | 80.4 € | rocking chair enfant | chaise à bascule enfant 390 | 1 |
| rocking-chair-bebe | 1005010686364227 | rocking chair bébé | 149 € | 79.96 € | rocking chair enfant | rocking chair bébé 260 · siège à bascule bébé 140 | 0 |
| repose-pieds-assorti | 1005007185322385 | repose-pieds assorti | 39 € | 15.68 € | accessoires rocking chair |  | 0 |
| coussin-d-assise-rocking-chair | 1005011653752895 | coussin d'assise rocking chair | 69 € | 40.18 € | accessoires rocking chair |  | 0 |
| plaid-pour-fauteuil | 1005008932793372 | plaid pour fauteuil | 39 € | 14.38 € | accessoires rocking chair |  | 0 |

Notes :
- Le **nom de travail** vient de l'onglet (mot-clé). Le H1 doit rester descriptif et vendeur, et reprendre la couleur ou la matière réelle des faits (ex. « Fauteuil à bascule d'allaitement en bouclette, dossier haut »).
- Les fiches qui portent plusieurs mots-clés (ex. `fauteuil-a-bascule-allaitement-teddy`) prennent le plus fort en mot-clé principal et les autres en secondaires.
- La famille relax (11 fiches) garde le vocabulaire confort et déco.

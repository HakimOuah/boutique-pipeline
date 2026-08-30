# Tuftéo — règles non négociables et pièges déjà payés

Ce que cette boutique a appris à ses dépens. Chaque entrée a coûté quelque chose. À lire avant
d'intervenir, en même temps que [`TABLEAU.md`](TABLEAU.md).

---

## Les trois règles qui gouvernent tout le reste

**1. « FAIT » ne veut rien dire tant que ce n'est pas constaté sur la page réelle.**

C'est la boutique qui a produit le cas d'école du parc : **les six faux avis sont restés servis
publiquement du 30/07 au 16/08**, alors que le ticket était marqué FAIT. Les instructions avaient été
écrites, l'action n'avait jamais été appliquée. Dix-sept jours de misrepresentation en ligne, sur un
compte Merchant Center approuvé.

Un ticket ne passe en FAIT que sur preuve : URL rechargée en navigation privée, capture, citation.
Pas un rapport, pas un accusé de succès d'API.

**2. Le compte Merchant Center est APPROUVÉ. On protège, on ne conquiert pas.**

173 produits, 173 approuvés. Ça inverse la logique habituelle : le danger n'est plus le refus à
l'entrée, c'est la suspension d'un actif existant. La checklist est nette — la plupart des
suspensions arrivent **après** l'approbation.

Corollaire pratique : **on évite les changements brutaux et on publie en une seule fois, proprement,
puis on surveille 30 jours.** Le 16/08 a déjà cumulé 17 nouveaux produits, deux renommages, 215
variantes reprises, une refonte des policies et un changement d'e-mail. Le volume seul peut
déclencher une revue.

**3. L'identité est partagée avec trois autres boutiques. Chacune doit être irréprochable.**

Adresse et téléphone communs à Bien Brûlé, Bonum Vitae et Maison Noirmont. Linkage assumé par
décision de Hakim (16/08). Une misrepresentation sur une boutique sœur dégrade l'entité OH Ventures —
qui a **déjà été suspendue** le 15/06/2026 (compte 5806019978, misrepresentation, réintégrée après
correction).

Ce qui reste séparable doit l'être : **les policies ne doivent jamais être identiques mot pour mot**
entre deux boutiques du parc.

---

## Les pièges techniques déjà payés ici

**`templates/index.json` ne peut pas être réécrit par `themeFilesUpsert`.** 124 999 octets : deux
upserts ont retourné un succès **sans appliquer**. `product.json` à 109 ko passe. La limite dure
GraphQL est autour de 125 ko. **Le 17/08, `shopify theme push --nodelete` a écrit `index.json`
à 124 922 octets sur une copie** — relire le contenu, ne pas se fier à `size`. Au-delà, passer
par les fichiers Liquid (sections, blocs).

**Le champ `size` renvoyé par l'API ne prouve rien.** Il annonçait 74 268 pour `index.json` dont le
contenu réel fait 124 999 octets. Ne jamais vérifier une écriture avec : relire le contenu, puis
recharger la page.

**Le thème publié (MAIN) est interdit à l'écriture.** Le connecteur le refuse. On travaille sur une
copie, **et c'est Hakim qui publie**.

**Une fiche créée par API n'est publiée sur aucun canal.** `resourcePublicationsV2` est vide à la
création — il faut publier explicitement sur Boutique en ligne **et** Google & YouTube. Piège vécu
sur les 17 fiches de fil.

**Les `curl` répétés déclenchent un 503 de limitation de Shopify.** Trois policies ont d'abord semblé
en échec pour cette seule raison. Refaire les constats au navigateur avant de conclure.

**`preview_theme_id` ne se transmet pas en `curl`** : il faut une session de navigateur pour voir un
thème brouillon.

---

## Les règles de contenu propres à cette boutique

**Aucune preuve sociale fabriquée, jamais.** C'est le motif qui a suspendu l'entité en juin et le
défaut qui a vécu dix-sept jours ici. Concrètement : aucun avis inventé, aucune mention « Vérifié »
non étayée, aucun compteur d'avis qui ne corresponde pas au décompte réel (169 avis Trustoo au
catalogue), aucun badge imitant un organisme de confiance type Trustpilot.

**Retirer un avis de la page ne le retire pas du flux.** Purge Shopify faite le 30/08 sur ordre
de Hakim : 51 métafields supprimés (17 fiches × `reviews.rating` + `reviews.rating_count` +
`vstar.product_rating` non nul). Relu API : `reviews.*` = 0 partout, plus aucun `vstar` à compteur
> 0. Les 23 `vstar` déjà à 0/0 n'ont pas été touchés.

**Trustoo peut les réécrire.** `vstar.product_rating` est le miroir de l'app. Si les six avis
fictifs existent encore dans Trustoo, la prochaine synchro recréera les compteurs. Contrôle
Trustoo (admin de l'app) à faire une fois ; tant que ce n'est pas fait, revérifier `reviews.rating`
avant chaque lancement ads.

**Aucune allégation d'origine non vérifiée fiche par fiche.** « Expédié depuis nos entrepôts en
Europe » a été retiré du footer et des fiches le 16/08 — le possessif était faux, Tuftéo n'a aucun
entrepôt, le catalogue vient d'AliExpress par DSers. Mais la mention **« depuis l'Europe » reste une
allégation d'origine** : elle n'est écrivable que sur les fiches dont l'entrepôt est documenté.
Aujourd'hui seuls les toiles (Allemagne, Pologne) et les deux articles électriques (Allemagne) le
sont. **Le gun et le kit — les produits phares — ne le sont pas.**

L'issue sans risque, déjà validée : écrire le fait vérifiable et tenu, **« Livraison offerte en
France en 6 à 10 jours ouvrés, suivi par e-mail »**, sans mention d'origine.

**Les chiffres de délai doivent être identiques partout.** Google compare ligne à ligne.
Alignés le 17/08 à **6 à 10 jours ouvrés** (expédition, CGV, FAQ copie). Périmètre : **France
métropolitaine uniquement** (décision Hakim 17/08, CGV live). Voir [T-04](TABLEAU.md), [T-05](TABLEAU.md).

**Une seule entité doit apparaître.** Shopify porte « Tuftéo » comme nom et « OH Ventures » comme
adresse ; le footer dit « OH VENTURES ». C'est celle du registre qui fait foi, partout.

**Le garde-fou électrique du 21/07 est soldé.** Tondeuse 200 W, ciseaux électriques et kit tondeuse :
**conformité CE validée par Hakim le 30/08/2026**. C'est la trace écrite qui manquait depuis
quatre semaines ; leur statut ACTIVE est désormais une décision, plus une régression. La règle
elle-même reste en vigueur pour toute nouvelle référence électrique, et **se rouvre à chaque
changement de fournisseur** — un ressourcing AliExpress ne transporte pas la conformité de l'ancien.

**« Gun » dans les titres : on garde, on surveille.** Décision Hakim du 30/08 — tous les concurrents
FR emploient le terme, et le compte est approuvé avec ces titres depuis le 14/08. On ne renomme pas
par précaution. Si un refus tombe sur « Tufting gun 2-en-1 Cut & Loop » ou « Lames de remplacement
(lot de 12) », la politique Armes en est la cause la plus probable et le repli est « Machine à tufter ».

**Le swatch de variante n'est pas un visuel de fiche.** Règle du parc : l'image principale part dans
le flux Shopping, elle doit montrer le produit entier à 800 px minimum. Les 17 fiches de fil ont été
créées avec des swatches de 251 × 194 px comme image principale.

---

## Ce que Hakim seul décide

La direction artistique · les placeholders de démonstration (slider, avis de démo — sa chasse
gardée) · **la publication du thème** · tout budget publicitaire · tout arbitrage de conformité
(CE, allégations, origine d'expédition).

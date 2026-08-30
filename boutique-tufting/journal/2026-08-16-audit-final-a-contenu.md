---
type: journal
boutique: tufting
date: 2026-08-16
nature: analyse
leviers: [conformite]
titre: "Audit final GMC — Agent A — Contenu, promesses et cohérence textuelle"
---

# Audit final GMC — Agent A — Contenu, promesses et cohérence textuelle

**Boutique** : Tuftéo (tufteo.com). **Date** : 16/08/2026. **Périmètre** : thème brouillon `189410738561` (celui que Hakim publiera) + données Shopify Admin (policies, réglages boutique) qui sont indépendantes du thème.

**Méthode d'accès** : API Shopify (MCP + GraphQL Admin), `curl` espacé de ≥4s. Pas de navigateur — je ne vérifie donc pas le rendu réel des pages du thème brouillon (c'est le périmètre de l'agent C). Quand une donnée n'existe que dans le rendu Liquid du thème brouillon, je la marque NON VÉRIFIÉ et je le signale.

Rapport écrit au fil de l'eau. Chaque item : verdict PASS / FAIL / NON VÉRIFIÉ, preuve (URL, citation exacte, chiffre), correction proposée si FAIL.

---

## En cours

Audit démarré. Prochaine étape : récupérer les 6 policies (Shopify Admin `shop.shippingPolicy`, `refundPolicy`, etc. via GraphQL) pour A1, puis les réglages boutique pour A3.

## A1 — Les 6 (en réalité 7) policies, mot pour mot

**Source** : GraphQL Admin `shop.shopPolicies` (Basic Shopify policies, 16/08/2026 ~13h50). Il y a **7** policies enregistrées dans Shopify, pas 6 : Contact, Mentions légales, Politique de confidentialité, Politique de remboursement, Expédition, CGV, CGU.

| Policy | URL |
|---|---|
| Contact | https://checkout.shopify.com/95327748481/policies/51848413569.html?locale=fr |
| Mentions légales | https://checkout.shopify.com/95327748481/policies/51848577409.html?locale=fr |
| Politique de confidentialité | https://checkout.shopify.com/95327748481/policies/51835437441.html?locale=fr |
| Politique de remboursement | https://checkout.shopify.com/95327748481/policies/51848479105.html?locale=fr |
| Expédition | https://checkout.shopify.com/95327748481/policies/51848610177.html?locale=fr |
| CGV | https://checkout.shopify.com/95327748481/policies/51848642945.html?locale=fr |
| CGU | https://checkout.shopify.com/95327748481/policies/51848511873.html?locale=fr |

### FAIL — Contradiction chiffrée entre policy Expédition et CGV (délai de livraison total)

- **Policy Expédition** (citation exacte) : « Délai de livraison total estimé : 6 à 10 jours ouvrés ». Préparation « 24h à 48h » (hors week-ends/jours fériés), transit « comprises entre 5 et 9 jours ouvrés », heure limite « du lundi au vendredi : 15h (GMT+1, heure de Paris) ».
- **CGV, Article 8 — Livraisons** (citation exacte) : « Les produits sont livrés dans un délai moyen de 8 à 13 jours ouvrés à l'adresse indiquée par le Client ».
- **Verdict : FAIL.** 6-10 jours (policy Expédition) contre 8-13 jours (CGV) : deux fenêtres différentes pour la même promesse, dans deux documents que Google Merchant Center compare ligne à ligne (checklist §3 : « mêmes chiffres partout »).
- **Correction proposée** : aligner l'article 8 des CGV sur les chiffres réels de la policy Expédition (préparation 24-48h + transit 5-9 j ouvrés = 6-10 j ouvrés total), ou l'inverse si la fourchette CGV est celle qui reflète la réalité — **à trancher par Hakim**, je ne sais pas laquelle des deux fourchettes est correcte.

### FAIL — Contradiction sur le périmètre géographique de livraison

- **Policy Expédition** : « Tuftéo assure les livraisons dans les pays suivants : France. »
- **CGV, Article 8** : « Les Produits commandés par le Client seront livrés en France métropolitaine et à l'international. »
- **Verdict : FAIL.** La policy Expédition limite à la France, les CGV promettent l'international. Incohérence à trancher.

### PASS (confirmé) — Absence de chiffre sur les fiches produit

Le plan signale : « la politique d'expédition annonce 6-10 jours ouvrés, les fiches produit n'affichent aucun chiffre ». **Confirmé** : j'ai lu les 40 `descriptionHtml` en entier (via GraphQL Admin, voir A2 pour la méthode) — aucune ne mentionne de délai ou de date de livraison. Pas de contradiction chiffrée au niveau des fiches produit puisqu'elles ne chiffrent rien. Nuance : la page FAQ, elle, affirme que « la date de livraison estimée s'affiche directement sur chaque fiche produit » — ce qui est faux tel que je l'ai constaté (voir A2, FAIL « FAQ promet un affichage de date de livraison »).

### PASS partiel — Droit de rétractation (14 jours)

- **Policy Remboursement** : « vous disposez d'un délai de 14 jours à compter de la réception de votre colis pour exercer votre droit de rétractation ».
- **CGV, Article 10** : « Le remboursement sera effectué dans un délai de quatorze jours (au plus 14 jours) à compter de la notification au Vendeur de la décision de rétractation. »
- Ces deux mentions du chiffre 14 jours désignent des choses différentes (fenêtre de rétractation vs délai de remboursement après notification) mais restent cohérentes entre elles — pas de contradiction relevée ici.

### À surveiller — Délai de remboursement, wording différent mais pas contradictoire

- **Policy Remboursement** : « Le délai de traitement peut varier de 7 à 14 jours selon votre établissement bancaire. »
- **CGV, Article 10** : « remboursement... dans un délai de quatorze jours (au plus 14 jours) ».
- **Verdict : PASS avec réserve.** Les deux bornes hautes concordent (14 jours), la policy Remboursement ajoute une borne basse (7 jours) absente des CGV. Wording non strictement identique mais pas de chiffre contradictoire — la checklist demande une cohérence de fond, celle-ci est respectée. Signalé pour information, pas classé FAIL.

### PASS — Médiateur avec URL (CGV Article 18)

Citation exacte : « Médiateur du site tufteo.com : CM2C, 14 rue Saint Jean, 75017 Paris, Tél : 01 89 47 00 14, site internet : https://www.cm2c.net/ ». URL présente et fonctionnelle en apparence (non testée en navigateur — hors périmètre). Correspond à la correction du plan (bien qu'à l'article 18 des CGV, pas 15 comme indiqué dans le plan — écart de numérotation sans conséquence).

### FAIL — Un troisième chiffre de délai de livraison, dans les CGU

**Nouvelle découverte, absente du plan initial.** Les CGU (Conditions générales d'utilisation) contiennent elles aussi un délai de livraison chiffré, différent de la policy Expédition :

- Citation exacte, CGU, section « LIVRAISON » : « Nous livrons vos colis entre 8 et 13 jours ouvrés. Vous recevrez un numéro de tracking lorsque votre colis sera expédié. Si vous ne recevez pas ce numéro de tracking au bout de 72 heures, [...] »
- Ce chiffre (8-13 j) est **identique à celui des CGV** (voir plus haut) mais **différent de la policy Expédition dédiée** (6-10 j).

**Bilan des trois documents qui donnent un délai de livraison total :**

| Document | Délai annoncé |
|---|---|
| Policy Expédition (dédiée) | 6 à 10 jours ouvrés |
| CGV, Article 8 | 8 à 13 jours ouvrés |
| CGU, section Livraison | 8 à 13 jours ouvrés |

**Verdict : FAIL, aggravé.** Ce n'est pas un écart isolé entre deux documents : c'est la policy Expédition — normalement la source de référence — qui est l'**outlier** face à deux documents concordants (CGV et CGU). Cela suggère que la policy Expédition a été retouchée récemment (probablement lors des corrections du 16/08) sans que CGV et CGU ne soient mises à jour en miroir, ou l'inverse. À trancher par Hakim : quel est le délai réel, et faut-il aligner CGV+CGU sur Expédition (6-10 j) ou Expédition sur CGV+CGU (8-13 j) ?

---

## A2 — Allégations invérifiables

**Source** : les 40 fiches produit (`descriptionHtml` via GraphQL Admin, lu intégralement), les 7 policies, et 4 pages CMS (Contact, FAQ, Notre histoire, Apprendre — Tuftéo Academy). 16/08/2026.

### FAIL critique — « Expédition depuis nos entrepôts en Europe » sur deux pages publiées, contredisant la correction du jour

Le plan indique cette correction comme déjà faite aujourd'hui : *« Expédié depuis nos entrepôts » → Aucune occurrence de « nos entrepôts » sur tout le site*. **C'est faux : j'ai trouvé l'occurrence exacte, deux fois, sur des pages CMS publiées** (`isPublished: true`) :

- Page **FAQ** (`/pages/faq`), question « Vous livrez en combien de temps ? » — citation exacte : « **Expédition depuis nos entrepôts en Europe**, avec suivi par email. »
- Page **Notre histoire** (`/pages/notre-histoire`), section « Concrètement » — citation exacte : « 📦 **Expédition depuis nos entrepôts en Europe**, avec suivi »

**Pourquoi c'est un FAIL grave** : la règle maison dit qu'« expédié depuis l'Europe » n'est écrivable que sur les fiches à entrepôt vérifié (aujourd'hui : tondeuse et ciseaux, Allemagne, plus les toiles). Ces deux pages ne parlent pas d'un produit précis : elles affirment, au singulier généralisant (« nos entrepôts »), que **toute la boutique** expédie depuis l'Europe — alors que sur 40 fiches, seules 2 (tondeuse électrique, ciseaux électriques) portent une mention d'entrepôt vérifiée en Allemagne, et que le reste du catalogue (fils, toiles, gun, accessoires) n'a, à ma connaissance, aucune vérification d'entrepôt européen documentée dans les fichiers boutique locaux que j'ai consultés. C'est exactement le type de mention d'origine invérifiable, possiblement fausse, que Google sanctionne en misrepresentation.

**Correction proposée** : retirer ou reformuler ces deux occurrences. Ne garder « expédition depuis l'Europe » que pour les fiches où c'est vérifié, ou remplacer par une formule neutre non géographique si le reste du catalogue expédie d'ailleurs (ex. Chine via AliExpress/DSers).

**Ceci reproduit exactement le schéma d'incident du 30/07-16/08 décrit en tête du plan** : une correction notée comme faite sur une surface (probablement le thème/l'accueil) mais pas appliquée sur une autre (les pages CMS, gérées séparément dans Shopify Admin → Pages, hors du thème).

### FAIL — La FAQ promet un affichage de date de livraison sur chaque fiche produit, qui n'existe pas

Citation exacte, page FAQ : « La date de livraison estimée s'affiche directement sur chaque fiche produit ». **J'ai lu les 40 `descriptionHtml` en entier (voir A1) : aucune ne contient de date ni de délai de livraison.** Le thème brouillon contient bien un bloc réutilisable `blocks/delivery-estimation.liquid` dans sa bibliothèque de blocs — donc la fonctionnalité existe techniquement — mais je n'ai pas pu vérifier (accès API seul, pas de rendu de page) s'il est effectivement posé sur le template produit. Que le bloc soit posé ou non, la description texte (`descriptionHtml`, ce que je peux lire) n'affiche aucune date. **Verdict : FAIL si le bloc n'est pas posé, NON VÉRIFIÉ sur le rendu réel — à confirmer par l'agent C.** Dans les deux cas, la phrase de la FAQ est actuellement une promesse que je n'ai pas pu confirmer.

### FAIL probable — Promesse répétée de « vidéos » sans preuve de leur existence

Plusieurs fiches et la FAQ promettent des vidéos pas à pas :
- Tufting gun 2-en-1 : « nos tutoriels en français t'accompagnent du premier fil à la dernière tonte »
- Kit Tufting Complet : « notice française claire et vidéos pas à pas (enfiler le fil, régler la vitesse, tenir la machine dans le bon sens) » ; « tu passes de l'un à l'autre en suivant notre tutoriel dédié »
- FAQ : « expliqués pas à pas dans les guides **et vidéos** de la Tuftéo Academy » ; « notre tutoriel dédié te montre comment passer de l'un à l'autre »

**Vérification faite** : j'ai lu intégralement le contenu HTML de la page `/pages/apprendre` (Tuftéo Academy, 13 827 caractères de body) — c'est un guide texte détaillé et sérieux (montage du cadre, tension de la toile, technique du gun), avec un lien vers un **PDF réel** (`Guide-demarrage-Tufteo.pdf`, vérifié par `curl` : HTTP 200, 6,7 Mo, `content-type: application/pdf` — le PDF existe bel et bien). **Mais je n'ai trouvé aucune trace de vidéo** : zéro occurrence de « vidéo », « video », « youtube » ou `<iframe>` dans le HTML de la page. J'ai aussi vérifié les médias attachés aux deux fiches produit qui promettent le plus explicitement des vidéos (Tufting gun, Kit Tufting Complet) via `product.media` : **uniquement des IMAGE, aucune VIDEO** sur les deux.

**Verdict : la promesse de « vidéos » n'est étayée par aucun contenu vidéo que j'ai pu localiser via l'API.** Soit les vidéos existent ailleurs (page non répertoriée dans Shopify Pages, plateforme externe, réseaux sociaux) et je ne les ai pas trouvées — à vérifier par Hakim ou l'agent C —, soit la promesse est actuellement fausse et doit être retirée ou remplacée par « guide écrit » / « guide PDF ».

### NON PROUVABLE — « professionnel » attaché à la tondeuse sans support dans sa propre fiche

- Le **handle** de la fiche tondeuse est `tondeuse-professionnelle-tapis`, mais son **titre** public est « Tondeuse électrique pour tapis » (sans « professionnelle ») — décalage entre URL et titre affiché (chevauche le périmètre B2 de l'agent B, signalé ici parce qu'il porte une allégation).
- Trois autres fiches la qualifient de « la tondeuse professionnelle » dans leur bloc croisé « Va bien avec » : Brosse de finition, Guide de tondeuse, Lames de remplacement.
- La fiche de la tondeuse elle-même ne contient aucun élément factuel soutenant un usage « professionnel » (pas de certification, pas de spec de durabilité industrielle) — seulement « 240 W, prise EU (secteur) », vitesse réglable.
- **Verdict : non prouvable.** « Professionnel » est un qualificatif de gamme non étayé. Correction proposée : soit l'étayer (specs objectives justifiant l'usage intensif), soit le retirer du handle et des 3 renvois croisés.

### NON PROUVABLE — « Un dos de tapis propre et professionnel » (Tissu de finition, fiche DRAFT)

Citation exacte, bullet de la fiche « Tissu de finition » (handle `tissu-de-finition`, **statut DRAFT**, donc non публique actuellement) : « Un dos de tapis propre et professionnel ». Qualificatif subjectif non étayé — signalé pour correction avant publication de la fiche, pas bloquant tant qu'elle reste en brouillon.

### PASS — Garantie légale de conformité 2 ans

Citée sur « Tufting gun 2-en-1 » et « Kit Tufting Complet » : « Garantie légale de conformité 2 ans ». Il s'agit d'un droit légal français automatique (Code de la consommation, art. L217-3 et suivants), pas d'un avantage commercial inventé — **prouvable par la loi elle-même**, indépendamment de ce que le vendeur décide d'afficher. PASS.

### PASS — Déclaration fournisseur explicitement non vérifiée et non-affiliation à Makita (Ciseaux électriques)

Citation exacte : « Le fournisseur annonce une compatibilité avec les stations de charge 18V type Makita (**déclaration non vérifiée indépendamment de notre côté**) ; **ce n'est pas un produit de la marque Makita.** » — C'est la bonne pratique : la mention de marque tierce est faite avec un désaveu explicite d'affiliation et un hedge sur la source de l'information. Modèle à répliquer si d'autres fiches mentionnent une marque tierce (vérification exhaustive = périmètre B6, agent B).

### PASS — Caractéristiques techniques attribuées à la source

« Caractéristiques (données fournisseur) : 800 W, capacité de coupe **annoncée** jusqu'à 6 mm » (Ciseaux électriques) — le chiffre est présenté comme une donnée fournisseur non vérifiée indépendamment, pas comme un fait établi par Tuftéo. Bonne pratique de hedging.

### PASS — « CE » absent des fiches machines

Sur les 3 fiches électriques (Tondeuse, Ciseaux électriques, Kit tondeuse — ce dernier en DRAFT), aucune mention de marquage CE, aucun logo CE cité en texte. Confirme la correction listée dans le plan comme déjà faite. PASS.

### Faux positif écarté — « professionnel » dans la Politique de confidentialité

Une occurrence de « professionnel » dans la Politique de confidentialité renvoie au dispositif Bloctel (« toute personne de refuser d'être démarchée par un professionnel avec lequel elle n'a pas de relation contractuelle en cours ») — c'est une référence légale au démarchage téléphonique tiers, sans rapport avec une allégation sur Tuftéo. Pas un problème.

### Origine — restriction respectée

Sur les 40 fiches, seules 2 revendiquent une expédition depuis l'Europe (« Expédiée(s) depuis l'Europe (entrepôt en Allemagne) ») : la tondeuse électrique et les ciseaux électriques. Conforme à la règle maison (seuls ces deux produits ont un entrepôt vérifié). **PASS au niveau des fiches produit** — le problème se situe dans les pages CMS (voir FAIL ci-dessus « nos entrepôts »), pas dans le catalogue.

---

## A3 — Mentions légales françaises

**Source** : policy « Mentions légales » (GraphQL `shop.shopPolicies`, type `LEGAL_NOTICE`), policy « Contact », `shop.billingAddress`. 16/08/2026.

| Élément requis | Trouvé | Verdict |
|---|---|---|
| Raison sociale | « OH Ventures » (Contact, Mentions légales, `billingAddress.company`) | PASS |
| Forme juridique (SASU/SAS/SARL...) | **Absente.** Ni dans la policy Contact ni dans les Mentions légales. Seul « Capital social : 1000€ » laisse deviner une société à capital, sans préciser laquelle. | **FAIL** |
| Capital social | « Capital social : 1000€ » (Mentions légales) | PASS (chiffre présent, cohérence non vérifiable sans acte) |
| SIRET | « 10315725100010 » (Contact et Mentions légales, identique dans les deux) | PASS |
| RCS (numéro + ville) | **Absent** des deux documents. | **FAIL** |
| TVA intracommunautaire | « FR55103157251 » (Contact et Mentions légales, identique) — cohérente avec le SIREN 103157251 (9 premiers chiffres du SIRET) | PASS |
| Adresse | « 47 rue Vivienne, 75002 Paris » — identique dans Contact, Mentions légales, `billingAddress`, et adresse de retour de la policy Remboursement | PASS |
| Directeur / responsable de publication | « Responsable publication : Hakim Ouahabi – contact@tufteo.com **. Le responsable publication est une personne morale.** » | **FAIL — incohérence interne.** La phrase nomme une personne physique (Hakim Ouahabi) puis affirme dans la même respiration qu'il s'agit d'une personne morale. Artefact de template non complété. |
| Hébergeur | « Shopify Inc. — 151 O'Connor Street Ground Floor, Ottawa, Ontario, K2P... Canada » | PASS partiel — voir remarque ci-dessous |
| Médiateur avec URL | « CM2C, 14 rue Saint Jean, 75017 Paris, Tél : 01 89 47 00 14, site internet : https://www.cm2c.net/ » — présent dans les **CGV** (Article 18), pas dans les Mentions légales elles-mêmes | PASS (présent quelque part sur le site, comme l'exige la checklist) |

### FAIL — Absence de forme juridique et de RCS

Aucun document ne précise la forme juridique d'OH Ventures (SASU ? SAS ? autre ?) ni son numéro RCS et sa ville d'immatriculation. La loi n° 2004-575 du 21 juin 2004 (LCEN), citée par les Mentions légales elles-mêmes en en-tête, exige ces informations pour une personne morale. Correction proposée : ajouter la forme juridique exacte et « RCS Paris : [numéro]".

### FAIL — Contradiction « personne physique / personne morale » sur le responsable de publication

Citation exacte : « Responsable publication : Hakim Ouahabi – contact@tufteo.com . Le responsable publication est une personne morale. » C'est manifestement un reliquat de template (probablement une case à cocher « personne physique / personne morale » du générateur de mentions légales, restée sur la mauvaise option). Correction proposée : soit désigner explicitement OH Ventures comme responsable de publication (personne morale) avec Hakim Ouahabi comme représentant légal, soit supprimer la phrase « Le responsable publication est une personne morale » si c'est bien Hakim Ouahabi en tant que personne physique qui est responsable.

### À signaler — Hébergeur : seul Shopify Inc. (Canada) est cité, pas Shopify International Limited (Irlande)

**Comparaison faite avec les mentions légales de Maison Noirmont** (fichier local `boutique-pipeline/boutique-seiko-mod/livraisons/mentions-legales-a-coller-2026-08-15.html`, 15/08/2026) : celles-ci citent **les deux entités Shopify** — « Shopify International Limited » (Dublin, Irlande — le cocontractant pour les marchands établis en France) **et** « Shopify Inc. » (Ottawa, Canada — hébergement technique). Les Mentions légales de Tuftéo ne citent que Shopify Inc. (Canada). Ce n'est pas nécessairement une erreur bloquante (Shopify Inc. héberge techniquement les données), mais Maison Noirmont applique un standard plus complet sur le même point. **À harmoniser, décision Hakim.**

### Incohérence Tuftéo / OH Ventures — clarifiée, pas un problème en soi

Le plan signalait : « Shopify porte "Tuftéo" comme entité et "OH Ventures" comme adresse de boutique, le footer affiche "OH VENTURES" ». Ce que j'observe dans les données Shopify (policies + `billingAddress`) : **c'est cohérent, pas contradictoire** — « Tuftéo » est systématiquement présenté comme le nom commercial et « OH Ventures » comme la raison sociale qui l'édite (« Tuftéo édité par OH Ventures », répété à l'identique dans la policy Contact et dans les Mentions légales ; `billingAddress.company` = « OH Ventures »). C'est un schéma nom-commercial/raison-sociale standard et légal en France, à condition que la relation soit explicite — ce qui est le cas ici. **Je ne peux pas vérifier ce qu'affiche le récapitulatif de paiement au checkout** (souvent tiré de `billingAddress` ou d'un champ dédié « nom légal de l'entreprise » distinct, invisible depuis l'API que j'ai interrogée) — c'est un point NON VÉRIFIÉ, à confirmer par Hakim directement dans Shopify Admin → Réglages → Général, ou par l'agent C au rendu du checkout (sans aller jusqu'au paiement).


---

## A4 — Unicité des textes

### PASS avec réserve — Les 17 fiches de fil ne sont pas identiques mot pour mot, mais très templatées

Les 17 fiches couleur (`fil-acrylique-tufting-noir`, `-blanc`, `-gris`, `-rouge`, `-bordeaux`, `-rose`, `-rose-poudre`, `-orange`, `-jaune`, `-vert-fonce`, `-beige`, `-bleu-clair`, `-bleu-marine`, `-violet`, `-taupe`, `-indigo`, `-caramel`) suivent toutes la même structure : bullet 1 identique mot pour mot (« Pensé pour le gun : débit régulier, sans nœuds »), bullet 2 propre à chaque couleur (ex. « Le rouge, la couleur forte qui donne du caractère à ta pièce »), paragraphe avec la phrase « se déroule sans accroc dans ton gun, pour tufter zone par zone sans t'arrêter à démêler » répétée à l'identique sur les 17 fiches (+ la fiche générique « Fil acrylique en cône », soit 18 occurrences), et un « Va bien avec » quasi identique.

**Mesure faite** : comparaison caractère à caractère (Noir vs Rouge, `difflib.SequenceMatcher`) → **85 % du texte est identique** entre deux fiches couleur, le nom de couleur et un fragment de bullet étant les seuls éléments qui varient. **Verdict : PASS strict** (aucune fiche n'est un copier-coller intégral d'une autre — chaque fiche a un contenu propre à sa couleur), mais avec une réserve à signaler à Hakim : un taux de similarité aussi élevé sur 17 fiches consécutives est un facteur de risque pour la politique Google sur le contenu dupliqué/mince (« thin/duplicate content »), même si ce n'est pas un motif de refus automatique documenté dans la checklist gmc-acceptance. Une différenciation plus marquée (usage, association déco, exemple concret par couleur) réduirait le risque sans complexifier la maintenance.

### FAIL probable — CGV et CGU partagent un socle de texte quasi identique avec les CGV de Maison Noirmont

**Comparaison faite** entre les CGV de Tuftéo (policy `TERMS_OF_SALE`, lue en intégralité) et un corps de CGV pour Maison Noirmont trouvé en local : `boutique-pipeline/boutique-seiko-mod/backups/backup-retours-2026-08-08/a-appliquer-par-hakim/CGV-politique-boutique-CORPS-COMPLET.html`.

- L'Article 1 (« Champ d'application ») commence par une phrase **identique au mot près**, à l'exception du nom de domaine : « Les présentes Conditions Générales de Vente s'appliquent, sans restriction ni réserve[,] à l'ensemble des ventes conclues par OH Ventures (« le Vendeur ») auprès de consommateurs et d'acheteurs non professionnels (« Les Clients ou le Client »), désirant acquérir les produits proposés à la vente par le Vendeur (« Les Produits ») sur le site Internet [tufteo.com / maisonnoirmont.fr]. »
- **Mesure faite** : après normalisation des noms de domaine, comparaison caractère à caractère des deux textes complets (`difflib.SequenceMatcher`) → **ratio de similarité globale 0,56**, avec **46,7 % du texte de Tuftéo retrouvé mot pour mot dans le texte de Maison Noirmont** (10 062 caractères sur 21 531). Les articles numérotés (« ARTICLE 1 », « ARTICLE 2 »...) suivent la même trame dans les deux documents.
- **Verdict : FAIL au sens de la règle maison** — « des policies dupliquées entre domaines sont un motif de refus immédiat » (consigne de la tâche). Ce n'est pas une copie à l'identique intégrale (53 % du texte diffère : produits vendus, articles spécifiques), mais près de la moitié du texte est un socle juridique partagé mot pour mot entre deux domaines actifs de Hakim (tufteo.com et maisonnoirmont.fr). Je n'ai pas testé si Google Merchant Center applique cette règle aux clauses générales de droit commun (souvent similaires par nature juridique) aussi strictement qu'au contenu marketing — **je ne rends pas de verdict de conformité**, je documente le chiffre et la citation pour que Hakim tranche s'il faut réécrire l'un des deux jeux de CGV pour réduire l'overlap.

### NON VÉRIFIÉ — Comparaison avec les policies de Bien Brûlé

Je n'ai trouvé, dans les fichiers locaux du dossier `Bien Brulé/`, aucun corps de texte de policy (CGV, CGU, confidentialité, mentions légales) — seulement un fichier de bloc Liquid `_footer-policy-list.liquid` qui ne contient pas le texte des policies elles-mêmes. Je n'ai pas d'accès API à la boutique Bien Brûlé depuis cette session (le connecteur MCP Shopify est positionné sur Tuftéo ; changer de boutique en cours d'audit risquait de perdre le contexte). **Comparaison non faite — à faire séparément, soit en connectant le MCP sur Bien Brûlé, soit en demandant à Hakim un export.**

### PASS — Mentions légales Tuftéo vs Maison Noirmont : pas de duplication de texte, mais des faits partagés (attendu)

Contrairement aux CGV, les **Mentions légales** de Tuftéo et de Maison Noirmont ne partagent pas de texte rédactionnel — structures et formulations différentes (Tuftéo : format court « Propriétaire : ... » ; Maison Noirmont : format numéroté en 6 sections). Elles partagent en revanche les mêmes faits bruts (adresse, SIRET, téléphone) — **attendu et assumé par Hakim** selon le plan (« Adresse et téléphone partagés avec Bien Brûlé et Maison Noirmont : décision assumée »). Pas de FAIL ici.

---

## A5 — Fausse urgence

### PASS — Code de réduction BIENVENUE10 réel et actif

**Vérifié via GraphQL Admin** (`codeDiscountNodeByCode`), 16/08/2026 : le code `BIENVENUE10` existe, statut **ACTIVE**, réduction de **10 %** (`percentage: 0.1`), titre interne « Bienvenue -10 % (newsletter) », actif depuis le 22/07/2026, sans date de fin (`endsAt: null`). Le bandeau annonçant « -10 % avec BIENVENUE10 » correspond donc à une offre réelle et fonctionnelle, pas une fausse promotion. PASS.

### PASS — Aucune fausse urgence détectée dans les 40 fiches produit

Sur les 40 `descriptionHtml` lues intégralement : aucune mention de compte à rebours, aucun « plus que X en stock », aucune « offre limitée » sans date. PASS pour le texte des fiches produit.

### NON VÉRIFIÉ — Blocs de thème pouvant produire de la fausse urgence s'ils sont posés

Le thème brouillon (`189410738561`, rôle UNPUBLISHED, confirmé) contient dans sa bibliothèque de blocs disponibles : `blocks/countdown.liquid` (compte à rebours générique, date de fin par défaut 01/01/2028 — donc inoffensif par défaut, mais configurable), `blocks/product-inventory.liquid` (affichage de stock bas configurable, seuil par défaut 20 unités, avec option d'afficher le chiffre exact), `blocks/delivery-estimation.liquid` (le bloc qui pourrait justifier — ou pas — la promesse de la FAQ, voir A2). **Le fait que ces blocs existent dans la bibliothèque du thème ne prouve pas qu'ils sont posés sur une page réelle** : je n'ai pas les moyens, en API seule sans rendu, de confirmer leur présence sur les templates produits effectivement utilisés sans lire des fichiers JSON de template volumineux, hors du périmètre que je me suis fixé (contenu, pas rendu). **Remonté à l'agent C** : vérifier en navigateur si un compte à rebours, un indicateur de stock bas ou un encart de date de livraison estimée apparaît réellement sur les fiches produit et l'accueil du thème brouillon.


---

## Synthèse

**Comptage** (granularité : chaque constat titré ci-dessus) : **9 FAIL** (dont 3 sur les chiffres de livraison A1, 3 sur les allégations A2, 3 sur les mentions légales A3, 1 sur la duplication CGV/CGU A4 — voir le détail, un item peut recouper deux catégories), **13 PASS** (dont 2 « avec réserve »), **6 NON VÉRIFIÉ**.

### FAIL classés par gravité (le plus grave en premier)

1. **« Expédition depuis nos entrepôts en Europe » sur les pages FAQ et Notre histoire** (A2) — reproduit exactement l'incident du 30/07-16/08 décrit en tête du plan : une correction notée comme faite mais appliquée sur une seule surface (le thème) et pas sur une autre (les pages CMS Shopify). Allégation d'origine généralisée à tout le catalogue alors que seuls 2 produits sur 40 ont un entrepôt vérifié. **C'est le point le plus grave de mon audit.**
2. **Trois chiffres différents pour le même délai de livraison total** : policy Expédition (6-10 j), CGV (8-13 j), CGU (8-13 j) (A1). Contradiction frontale sur exactement le type de donnée que la checklist gmc-acceptance dit vérifiée « ligne à ligne » par Google.
3. **CGV et CGU de Tuftéo partagent ~47 % de texte identique avec les CGV de Maison Noirmont** (A4), mesuré par comparaison caractère à caractère. Risque documenté de refus pour policies dupliquées entre domaines.
4. **FAQ promet un affichage de date de livraison sur chaque fiche produit — inexistant** (A2) et **promesses répétées de « vidéos » pas à pas sans preuve trouvée de leur existence** (A2, PDF réel confirmé mais aucune vidéo localisée).
5. **Mentions légales incomplètes** : forme juridique absente, RCS absent, contradiction interne « responsable publication... est une personne morale » alors qu'une personne physique est nommée (A3).
6. **Contradiction sur le périmètre géographique de livraison** : policy Expédition dit France uniquement, CGV disent France + international (A1).
7. **« Professionnel » attaché à la tondeuse** (handle + 3 fiches croisées) sans support factuel dans sa propre fiche, et sur la fiche « Tissu de finition » (DRAFT) (A2) — gravité faible, facilement corrigible.

### Ce qui est solide (PASS)

Médiateur CM2C avec URL fonctionnelle en apparence ; droit de rétractation 14 jours cohérent partout où il apparaît ; aucun marquage CE sur les fiches machines ; origine « Europe » correctement restreinte aux 2 seules fiches vérifiées dans le catalogue produit ; garantie légale de conformité correctement qualifiée de légale ; code promo BIENVENUE10 réel, actif, -10 % ; aucune fausse urgence (compte à rebours, stock faible, offre limitée) dans les 40 fiches produit ; SIRET/TVA/adresse cohérents partout où je les ai trouvés ; les 17 fiches de fil ne sont pas des copies conformes malgré un fort gabarit commun (85 % de similarité mesurée, pas 100 %).

---

## Ce que je n'ai pas pu vérifier

- **Rendu réel des pages** (thème brouillon) : je n'ai lu que les données sources (policies via API, `descriptionHtml`, fichiers de thème bruts). Je n'ai pas vu si le contenu s'affiche correctement, sans erreur Liquid, sans placeholder — c'est le périmètre de l'agent C.
- **Si les blocs `countdown`, `product-inventory` (stock bas) et `delivery-estimation` du thème brouillon sont effectivement posés sur une page** (accueil, fiche produit) avec quelles valeurs. Je n'ai confirmé que leur existence dans la bibliothèque de blocs du thème, pas leur usage réel. À vérifier par l'agent C en navigateur.
- **Ce qu'affiche le récapitulatif de paiement / checkout comme nom légal du vendeur** (Tuftéo ou OH Ventures) — invisible depuis les champs `shop` que j'ai interrogés via l'API GraphQL Admin accessible depuis le connecteur MCP.
- **Comparaison des policies avec Bien Brûlé** : aucun corps de texte de policy trouvé en local pour cette boutique, et je n'ai pas basculé le connecteur MCP dessus (risque de perdre le contexte Tuftéo en cours d'audit). Seule la comparaison avec Maison Noirmont (via fichiers locaux du repo `boutique-seiko-mod/`) a pu être faite.
- **L'existence de vidéos tutoriel ailleurs que sur les pages et fiches produit que j'ai consultées** (réseaux sociaux, plateforme d'hébergement vidéo externe, page non répertoriée dans Shopify Admin → Pages). J'ai seulement confirmé leur absence dans les 4 pages CMS et les médias des 2 fiches produit les plus concernées.
- **Cohérence de l'heure limite de commande (15h, GMT+1) et du délai de préparation (24-48h) avec d'éventuelles mentions dans le thème** (bannière, section livraison de la fiche produit rendue) — je n'ai vérifié que les 7 policies et les 4 pages CMS ; un bandeau ou une section de thème avec un chiffre différent resterait invisible pour moi sans lecture exhaustive des templates JSON (hors périmètre pour rester dans « contenu via API », et risque de doublon avec l'agent C).
- **Validité juridique du capital social (1000 €) et de la forme de société sous-jacente** — je constate l'absence de la forme juridique, je ne peux pas la déduire ni la vérifier auprès d'un registre externe (hors périmètre, aucune recherche externe faite).
- **Fonctionnement réel de l'URL du médiateur CM2C** (`https://www.cm2c.net/`) — présence textuelle confirmée, accessibilité non testée (pas de navigateur dans mon périmètre).

---

*Rapport clos à ce stade — 16/08/2026. Prêt pour consolidation avec les rapports des agents B et C.*

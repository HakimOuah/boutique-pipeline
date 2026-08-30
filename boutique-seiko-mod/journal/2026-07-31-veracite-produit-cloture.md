---
type: journal
boutique: seiko-mod
date: 2026-07-31
nature: intervention
leviers: [conformite]
titre: "Clôture des points de véracité produit — Maison Noirmont"
---

# Clôture des points de véracité produit — Maison Noirmont

> **26/07/2026** — boutique `v42pzp-h4` / maisonnoirmont.fr.
> Clôt les points 3, 4 et 5 de « ce que je n'ai pas tranché » de `2026-07-31-audit-promesses.md`, et le trou de
> couverture du diamètre de `2026-07-31-metachamps-montres.md`.
> Périmètre : **textes de fiches + métachamp `custom.diametre`**. Aucun SKU, prix, variante, option, statut
> ni mapping DSers touché. Thème publié « Helio » **non ouvert**. Aucune commande, aucun achat.
> Sauvegardes intégrales avant/après : `boutique-seiko-mod/backups/backup-veracite-2026-07-26/`.

---

## La méthode, et pourquoi elle a changé en cours de route

DSers **n'expose l'URL AliExpress nulle part dans son interface** : ni lien, ni info-bulle, ni page de mapping.
L'identifiant du produit fournisseur ne vit que dans l'état React de l'application. Il a fallu le lire là, ce qui
a permis de sortir **les 98 mappings d'un coup** plutôt que d'ouvrir 98 fiches. Le relevé est dans
`boutique-seiko-mod/backups/backup-veracite-2026-07-26/mapping-dsers.txt`.

Sur chaque fiche AliExpress, la source retenue est **l'attribut vendeur structuré** (« Profondeur de Résistance
à L'eau », titre H1 du vendeur). L'« Aperçu IA de l'article » d'AliExpress a été **écarté** : c'est du texte
généré, pas une déclaration du vendeur. Les blocs de recommandations en bas de page ont été écartés aussi —
ils affichent les caractéristiques d'**autres** montres, et c'est un piège à contresens.

**Dix listings couvrent les quinze fiches concernées.** Les 7 Intégrale partagent une seule référence
fournisseur, les 3 Héritage une autre, etc. C'est ce qui rend le relevé court et vérifiable.

---

# Volet 1 — l'étanchéité

## Ce que dit réellement le fournisseur, référence par référence

| Listing AliExpress | Nos fiches | Attribut vendeur « Profondeur de résistance à l'eau » | Titre vendeur |
|---|---|---|---|
| `1005009697365359` (Corgeut) | Trente-Six ×5 + mère | **10 bars** | « …36mm/39mm, **10 barres**… » |
| `1005010776361944` (Corgeut) | Trente-Neuf ×6 + mère | **10 bars** | « …**étanche à 100 m**… » |
| `1005004626900765` (Tandorio) | Noirmont Un, Un Bronze | **20 bars** | « …**étanche à 200 m**… », caractéristique « PLONGEUR » |
| `1005008657937411` (PARNSRPE) | Héritage ×3 + mère | **5 bars** | « Montre Mécanique Vintage **42mm**… » |
| `1005009821439225` | Intégrale ×7 + mère | **3 bars** | « …Acier Inoxydable **3Bar** » |
| `1005005629655849` (BLIGER) | Noirmont Deux | 10 bars | « …Miyota **40mm**… » |

**Le résultat va à l'inverse de l'hypothèse de départ.** La mission partait du principe que les 11 fiches
« 10 bar » reposaient sur une spécification invérifiable. Elle est vérifiable, et **elle est exacte** : le
vendeur déclare 10 bars dans son attribut structuré *et* dans son titre, sur les deux références. Il n'y avait
donc pas de promesse à retirer — seulement une promesse à **calibrer**.

## Ce qui a été écrit

### Les 11 fiches à 10 bar — promesse conservée, absolu retiré

Règle appliquée : 10 ATM autorise la nage en surface, pas la plongée. La piscine et la baignade **restent
donc autorisées**. Ce qui a été retiré, c'est la garantie absolue et l'absence de réserve sur la source.

| Avant | Après |
|---|---|
| « Étanchéité 10 bar : douche, piscine et baignade **sans souci** ; la plongée reste déconseillée » | « Étanchéité **annoncée** 10 bar : douche, piscine et baignade **en surface** ; la plongée reste déconseillée » |

`sans souci` est la formulation qui finit en litige : elle promet un résultat, pas une caractéristique.
`annoncée` reprend le hedge déjà en place ailleurs sur la boutique (« saphir annoncé »), et dit honnêtement
que la source est le fournisseur.

Fiches : Trente-Six Rouge, Bleu, Rose, Doré, Or intégral · Trente-Neuf Rouge, Bleu mer, Rose, Vert, Bleu, Noir.

### Noirmont Un Bronze — 200 m confirmé, plongée bouteille explicitement exclue

| Avant | Après |
|---|---|
| « Étanchéité 200 m : baignade, nage et plongée libre **sans souci** » | « Étanchéité **annoncée** 200 m : baignade, nage et plongée libre ; **la plongée en bouteille reste déconseillée** » |

Le vendeur déclare 20 bars et classe la montre « PLONGEUR ». La plongée libre (apnée, sans bouteille) tient
dans cette valeur. La plongée en bouteille n'y tient pas, et n'était pas exclue jusqu'ici : elle l'est
maintenant.

### Les 3 Héritage — le mot « Plongeuse » requalifié en style

Le fournisseur confirme **5 bars**. Le corps de fiche était déjà juste (« n'est pas prévue pour nager ni
plonger »). **Le problème n'était pas le chiffre, c'était le titre** : « Plongeuse vintage 42 » se lit comme
une promesse d'usage.

Les titres de produit m'étaient interdits sauf pour un matériau non prouvé — ils sont **intacts**. La
contradiction a donc été levée dans le corps, par un paragraphe qui dit explicitement ce que le mot recouvre :

> « Plongeuse » décrit ici un style, pas un usage : on en reprend la lunette tournante, les index larges et la
> matière luminescente. L'étanchéité annoncée est de 5 ATM — elle couvre la pluie, les éclaboussures et le
> lavage des mains, mais ne permet ni la nage ni la plongée.

Ajouté aux 3 fiches ACTIVE **et** à la fiche mère DRAFT `heritage-plongeuse-vintage-42`, dont la ligne
« 42 mm · saphir annoncé · 5 ATM » ne disait rien de l'usage et devient « …**étanchéité annoncée 5 ATM — ni
nage ni plongée** ».

Bonne surprise : les **balises SEO des 3 Héritage disaient déjà « style plongeuse » / « d'inspiration
plongeuse »**. Elles étaient déjà correctes et n'ont pas été touchées.

### Les 7 Intégrale — le silence comblé : 3 bar désormais annoncé

Le fournisseur ne donne que **3 bars** — la valeur la plus basse du catalogue. **Aucune fiche Intégrale
n'annonçait d'étanchéité**, vérifié sur les 7 : il n'y avait donc aucune promesse *fausse* à retirer, mais
un silence, et un silence à 379 € que le client comble tout seul — en supposant qu'une montre à ce prix
supporte l'eau, puis en la mouillant.

Mention ajoutée aux **7 fiches ACTIVE**, à la place où l'étanchéité figure sur toutes les autres fiches de la
boutique (entre la ligne de boîtier et la ligne de livraison) :

> Étanchéité annoncée 3 bar : de quoi encaisser la pluie et les éclaboussures ; on la retire avant la douche,
> la piscine et la mer.

Rédigée comme une information d'usage, pas comme un avertissement : elle dit ce que la montre encaisse avant
de dire ce qu'elle ne fait pas, et elle nomme les trois situations réelles où on la retire. **3 bar
n'autorise ni la douche, ni la nage, ni aucune immersion** — c'est ce que dit la phrase, sans le mot
« attention » et sans dramatiser une caractéristique qui est normale sur une montre habillée.

Fiches : Intégrale Vert, Brun or rose, Turquoise, Noir, Bleu nuit, Bleu ciel, Blanc argenté.

**La fiche mère `integrale-sport-chic-acier` (DRAFT) n'a pas reçu la mention** — elle est invisible en
vitrine et n'annonce aucune étanchéité, donc elle ne contredit rien. À aligner si elle est un jour publiée.

---

# Volet 2 — les matériaux

## L'acier 904L : non prouvé sur l'un, contredit sur l'autre

| Fiche | Ce qui était annoncé | Ce que dit le fournisseur | Traitement |
|---|---|---|---|
| `bracelet-presidentiel-904l` (`10977445052754`) | « acier **904L** » (titre + corps) | **Deux fournisseurs mappés qui se contredisent** : `1005010705179185` titre « en acier **316L** », `1005006496083816` titre « en acier inoxydable **904L** ». Attribut structuré des deux : « acier inoxydable », sans nuance | **Retiré.** Titre → « Bracelet Présidentiel — **acier inoxydable** » |
| `bracelet-jubile-acier-904l-20mm` (`10980388471122`) | « acier **904L** » (titre, corps ×2, SEO ×2) | `1005009920675767` : attribut « acier inoxydable » sans nuance ; le seul alliage nommé sur la page est **316L** ; « 904 » n'apparaît que dans « Jubilee 904 », qui est un **nom de modèle**, pas une nuance | **Retiré.** Titre → « Bracelet Jubilé **acier** — 20 mm » |

Le cas du Présidentiel est le plus net : **le même bracelet est vendu comme 316L par un fournisseur et 904L
par l'autre**. C'est exactement le cas « fournisseur contradictoire » — la promesse tombe.

Deux phrases de vente reposaient entièrement sur l'alliage et ont dû être réécrites, sans rien inventer :

- « dans un acier 904L plus dense et plus résistant à la corrosion — celui qu'on retrouve sur les pièces de
  haute horlogerie et sur les montres qui vivent près de la mer » → « dans un **acier inoxydable massif, poli
  et satiné** ».
- « la différence se voit surtout au bout de quelques mois, quand un acier ordinaire commence à se ternir »
  → remplacée par un fait observable : « le contraste entre les rangs polis et les rangs brossés accroche la
  lumière sur toute la longueur du bracelet ».

Balises SEO du Jubilé réécrites **avec les deux champs** (`title` *et* `description`) dans le même appel —
c'est le piège des 47 titres perdus, il n'a pas été rejoué.

## Le cuir véritable : étayé chez le fournisseur, aligné quand même vers le bas

`rouleau-de-voyage-cuir` (DRAFT, `10977444823378`) annonçait « le rouleau en **cuir véritable** ».
Le fournisseur `1005008493748701` (Embers) **dit bien « cuir véritable » dans son titre** — mais son attribut
structuré ne dit que « Cuir », et **ses 4 variantes ACTIVE chez nous disaient déjà simplement « cuir »**.

Un titre de place de marché n'est pas un certificat de matière, et la fiche mère contredisait ses propres
filles. Aligné sur le moins-disant : « le rouleau **en cuir** qui protège vos montres ».

**C'est un arbitrage de ma part, pas un constat de fausseté** — à réviser si le fournisseur fournit un jour
une attestation.

---

# Volet 3 — les 10 diamètres manquants

## Un seul était établissable. Neuf ne le sont pas.

| Fiche | Source fournisseur | Résultat |
|---|---|---|
| `noirmont-deux-plongeuse-ceramique` | H1 vendeur BLIGER : « …Insert Noir Bleu Vert, **40mm**, Bleu Ciel » | **`["40 mm"]` écrit** |
| Les 7 **Intégrale** | Listing `1005009821439225` : **aucune cote de boîtier**. Pas dans le titre, pas dans le H1, pas dans la table d'attributs (qui ne donne que « Longueur du bracelet 17.5 cm »), et **la description vendeur est vide**. Aucune option de taille : la seule option est « Couleur » | **laissé vide** |
| `noirmont-un-plongeuse-acier`, `noirmont-un-bronze-plongeuse` | Listing Tandorio `1005004626900765` : la table donne « **Diamètre du cadran : 30 à 34 mm** » — c'est le **cadran**, pas le boîtier, et c'est une **tranche**, pas une cote. Les options sont « boîtier acier/bronze » et « calibre / fond », aucune taille | **laissé vide** |

**Le piège du cadran, rencontré et évité.** « Diamètre du cadran 30 à 34 mm » ressemble à une cote de boîtier
et n'en est pas une — un boîtier de plongeuse fait couramment 6 à 10 mm de plus que son cadran. Écrire
« 32 mm » aurait produit une valeur fausse sur une gamme entière, et une nouvelle entrée parasite dans la
facette. C'est le même piège que le « 38 ou 39 mm » du poignet client déjà relevé sur les Quarante-et-Un.

## Couverture finale

| | Avant | Après |
|---|---:|---:|
| Montres avec `custom.diametre` | 43 / 53 | **44 / 53** |
| Taux | 81 % | **83 %** |

**Forme canonique respectée** : liste de textes `"NN mm"`, espace comprise. Valeurs distinctes après écriture :
`36 mm`, `39 mm`, `40 mm`, `41 mm`, `42 mm` — **exactement les cinq d'avant**. `40 mm` existait déjà (les 6
Voyageur), donc **aucune entrée en double n'a été créée dans la facette**.

---

## Contrôle d'application

Catalogue relu intégralement après écriture et comparé au relevé d'avant (99 produits des deux côtés) :

| Contrôle | Résultat |
|---|---|
| Occurrences de « sans souci » restantes | **0** |
| Occurrences de « 904 » restantes (titres, corps, SEO) | **0** |
| Occurrences de « cuir véritable » restantes | **0** |
| Balises SEO `title` perdues | **0** |
| Balises SEO `description` perdues | **0** |
| Titres de produit modifiés | **2**, et uniquement pour matériau non prouvé |
| Titres Héritage | **4 / 4 intacts** — l'arbitrage reste à Hakim |
| Descriptions modifiées | **26** |
| Fiches portant la mention 3 bar | **7**, une seule formulation, aucune variante |
| Formulation 3 bar autorisant un usage aquatique | **0** |
| Valeurs de diamètre distinctes | **5**, inchangées |

**Contrôle fait en rendu, pas seulement en JSON.** La description produit est servie dans un **accordéon
replié** : elle est absente de `innerText` et présente dans le DOM. Un contrôle sur le texte visible aurait
donc conclu à tort que rien n'était appliqué. Vérifié sur `integrale-noir`, `integrale-brun-or-rose` et
`heritage-bleu` en chargeant la page publique : les nouvelles chaînes sont là, les anciennes ont disparu, et
la balise `<title>` de chaque page affiche toujours son titre SEO d'origine.

---

## ⛔ Ce qui reste indécidable, et pourquoi

1. **Le diamètre des 7 Intégrale.** Le fournisseur ne le publie pas, du tout — sa description est vide et sa
   table d'attributs ne contient aucune cote de boîtier. La facette « Diamètre » **ne fera donc toujours pas
   apparaître une gamme entière de Sport chic**. Deux issues, aucune gratuite : poser la question au vendeur
   via la messagerie AliExpress, ou mesurer sur un exemplaire à réception. **Ne pas estimer sur photo** : sans
   cote de référence dans l'image, l'erreur courante est de 2 à 3 mm, soit une valeur fausse.

2. **Le diamètre des 2 Noirmont Un.** Même situation, aggravée par la présence d'une cote de **cadran** qui
   invite à la confusion. Même issue.

3. ~~La valeur 3 bar des Intégrale n'est pas dite au client.~~ **Tranché et appliqué** le 26/07 : la mention
   figure désormais sur les 7 fiches ACTIVE (voir volet 1). Reste seulement la fiche mère DRAFT, à aligner
   si elle est publiée.

4. **Les handles gardent « 904l ».** `bracelet-presidentiel-904l` et `bracelet-jubile-acier-904l-20mm`
   contiennent encore l'alliage dans leur URL. Les changer casserait les liens et sortait du périmètre.
   À arbitrer : soit on les laisse, soit on les change **avec une redirection**.

5. **Le mot « Plongeuse » reste dans les 3 titres Héritage — réservé à Hakim, non touché.** La contradiction
   est levée dans le corps et les balises SEO disent « style plongeuse », mais **un titre reste un titre** :
   c'est ce qui s'affiche en collection, en panier et dans Google Shopping, là où le paragraphe explicatif
   n'apparaît pas. Si tu veux fermer le point pour de bon, le titre doit devenir « **Héritage Bleu — Vintage
   42, style plongeuse** » ou équivalent. **Les 4 titres sont intacts, contrôlé après coup** ; le paragraphe
   de requalification tient jusqu'à ta décision.

   Même statut pour le **« cuir véritable »** de la fiche mère `rouleau-de-voyage-cuir` : mon alignement sur
   « cuir » est une **perte d'argument commercial, pas une correction de fausseté** — le fournisseur, lui,
   annonce bien « cuir véritable ». Laissé en l'état, à toi de trancher si tu veux récupérer l'argument.

6. **Rappel non traité ici, mais toujours ouvert** : une montre **remontée** (boîtier rouvert pour changer le
   cadran ou les aiguilles) perd la garantie d'étanchéité d'origine du fabricant, quelle que soit la valeur
   annoncée. Aucune de nos fiches ne le dit. C'est le point qui rend une promesse d'étanchéité fragile même
   quand le chiffre du fournisseur est exact — et il concerne **les 15 fiches**, pas seulement celles
   corrigées ici.

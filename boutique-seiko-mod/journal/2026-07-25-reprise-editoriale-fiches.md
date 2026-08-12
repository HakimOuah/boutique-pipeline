# Reprise éditoriale des 60 fiches découpées — 2026-07-25

Boutique **NOIRMONT** / Maison Noirmont (`v42pzp-h4`, maisonnoirmont.fr)

**60 / 60 fiches retravaillées** — 19 du lot 1, 41 du lot 2.
Champs touchés : `descriptionHtml` et `seo` **uniquement**. Aucun SKU, aucune variante, aucun prix,
aucun titre, aucune image, aucune fiche mère. Aucune commande passée.

---

## ⚠️ Note de méthode — la règle de marque a deux volets, pas un

Une première passe a retiré **toutes** les mentions de marque, y compris les fabricants de mouvements.
C'était une sur-application : la règle « aucune marque tierce » vise les **marques de design** — celles
dont les montres reprennent le dessin — parce que les citer reviendrait à revendiquer une filiation
qu'on n'a pas. Elle ne vise **pas les fabricants de composants**.

Les calibres ont donc été **rétablis** sur les 47 fiches concernées, et c'est la version en ligne :

| | Statut |
|---|---|
| Nommer le calibre **et son fabricant** (`Seiko NH35`, `Miyota 8215`, `Seiko VK63`) | ✅ **Autorisé** — c'est vrai, vérifiable, et c'est l'argument technique central |
| Nommer l'origine (japonais pour Seiko et Miyota) | ✅ Autorisé — **jamais** pour le PT5000, le Mingzhu 2813 ni le DG3804 |
| Nommer une marque dont on reprend le **dessin** | ⛔ Interdit |
| Suggérer une filiation, une équivalence ou une compatibilité de prestige | ⛔ Interdit |

Un acheteur de montre modifiée choisit précisément son calibre : c'est ce qui justifie l'écart de prix
entre variantes. Les fiches l'affichent donc, et **chacune annonce les calibres réellement disponibles
sur elle** — ce qui corrige au passage l'une des erreurs factuelles trouvées (plusieurs fiches n'en
citaient qu'un là où l'option en propose deux ou trois).

Les 13 accessoires (remontoirs, rouleaux) n'ont pas de mouvement : 60 − 13 = **47 fiches concernées**.

Le fabricant figure aussi dans les **métadonnées SEO** des 47 fiches : « seiko nh35 » et « miyota 8215 »
sont des requêtes intentionnistes de ce segment — celui qui les tape compare des mouvements.

---

## ⚠️ Piège technique — `seo` est remplacé en bloc, pas fusionné

**Envoyer `seo: { description: "…" }` sans `title` met le `seo.title` existant à `null`.**

Shopify ne fusionne pas l'objet `SEOInput` avec la valeur en place : il le remplace. Une passe qui ne
visait que les descriptions a donc effacé les 47 `seo.title` des fiches montres — les 13 accessoires,
non touchés par cette passe, avaient gardé les leurs, ce qui a rendu l'incident visible par asymétrie.

```graphql
# ❌ efface le seo.title
seo: { description: "…" }

# ✅ conserve les deux
seo: { title: "…", description: "…" }
```

Les 47 titres ont été **restaurés**. Règle à retenir : **toujours réécrire `title` et `description`
ensemble**, même quand un seul des deux change.

---

## Contrôles finaux

Deux relectures indépendantes des fiches par requête après écriture.

| Contrôle | Résultat |
|---|---|
| Marques de **design** citées (Rolex, Tudor, Omega, Cartier, Patek…) | **0** sur 60 |
| Formulations de filiation (« façon », « type », « hommage à », « équivalent à ») | **0** sur 60 |
| Concordance calibres annoncés / calibres réellement en option | **47 / 47**, zéro écart |
| « japonais » rattaché à tort au PT5000, au Mingzhu 2813 ou au DG3804 | **0** |
| Promesses non vérifiables (`assemblée à la commande`, `annoncé`, `cuir véritable`…) | **0** sur 60 |
| Fabricant accolé au mauvais calibre dans le SEO | **0** — lecture univoque sur les 20 fiches multi-calibres |
| `seo.title` vide ou hérité | **0** — 60 titres, tous **uniques**, 42 à 67 caractères |
| `seo.description` vide ou héritée | **0** — 60 descriptions, toutes **uniques**, 134 à 162 caractères |
| Renvois à la gamme (chaînes fautives) | **0** sur 60 |

---

## Le défaut de fond, au-delà de celui signalé

Le brief pointait « plusieurs lunettes bicolores au choix » sur le GMT. Le travers était réel et
**bien plus large** : sur les 60 fiches, le bloc hérité de la mère promettait un choix inexistant,
ou **décrivait des variantes que la fiche fille ne porte plus**. Six formulations étaient carrément
**fausses**, pas seulement inadaptées.

### Les formulations fautives les plus fréquentes

| Formulation trouvée | Fiches touchées | Nature |
|---|---:|---|
| `Assemblée à la commande` / `Assemblé à la commande` | **41** | Promesse non tenable en dropshipping |
| `SAV en français` sans point de contact | 41 | Vague, remplacé par l'adresse e-mail réelle |
| `la gamme` / `la série` / `le lot` / `le trio` / `les quatre essences` / `les six versions` | **31** | Renvoi à des sœurs absentes de la page |
| Un seul calibre annoncé là où l'option en propose 2 ou 3 | **20** | **Faux** pour la moitié ou les deux tiers des variantes |
| `saphir annoncé` / `étanchéité annoncée` | 13 | Aveu d'incertitude affiché au client |
| `vingt cadrans au choix selon disponibilité` | **12** | Choix inexistant + « selon disponibilité » |
| `un cadran panda` sur des fiches non panda | **10** | **Faux** |
| `plusieurs lunettes bicolores au choix` | **6** | Le défaut signalé au brief |
| `36 ou 39 mm · 10 bar` sans explication | 12 | Exact mais illisible pour un particulier |

### Le socle a été refait, pas seulement purgé

Chaque famille a reçu un **paragraphe pédagogique** qui explique une caractéristique au lieu de
l'énoncer : ce qu'est un bracelet jubilé (cinq rangs), une lunette cannelée (les stries qui captent
la lumière), un bracelet intégré (pas de cornes apparentes), un méca-quartz (le geste mécanique,
la régularité du quartz), une aiguille GMT (un tour de cadran en 24 h), à quoi sert un remontoir
(la montre s'arrête en 1-2 jours, il évite de tout remettre à l'heure).

**Là où deux calibres cohabitent**, la différence est expliquée plutôt qu'affichée : le NH35 se
remonte à la main et permet d'arrêter la trotteuse pour régler l'heure à la seconde près, ce que le
Miyota 8215 ne fait pas. C'est exactement l'écart que paie l'acheteur.

L'étanchéité, jusque-là posée en `10 bar` ou `5 ATM` bruts, est **traduite en usages** :
« douche, piscine et baignade sans souci ; la plongée reste déconseillée ».

Le bloc de réassurance est uniforme et strictement vérifiable :
`Livraison offerte en France · 14 jours pour changer d'avis · garantie 12 mois` + `contact@maisonnoirmont.fr`.

---

## Détail par famille

### Contre-la-montre — Chronographe (12 fiches)

- Calibre affiché : **Seiko VK63** (japonais), méca-quartz. L'option ne porte pas sur le mouvement.
- Purgé : `vingt cadrans au choix selon disponibilité` ; `Assemblé à la commande`.
- **Erreur factuelle corrigée** : le socle affirmait « un cadran **panda** » sur les 12 fiches, alors que
  seules 2 en sont (Panda, Panda inversé). Les 10 autres — Blanc, Champagne, Noir, Turquoise, Vert,
  Rose poudré, Gris anthracite, Argent, Compteurs bleus, Bleu glacier — l'annonçaient à tort.
- Ajouté : l'échelle tachymétrique expliquée sur la fiche Noir, la seule qui l'offre en option.

### Voyageur — GMT (6 fiches)

- Calibres affichés : **Seiko NH34** (japonais) **ou DG3804**, conformes aux 4 valeurs d'option.
  L'origine japonaise est enfermée dans une parenthèse accolée au seul NH34 — le DG3804 n'est pas japonais.
- Purgé : `plusieurs lunettes bicolores au choix` (le défaut du brief) ; `Assemblée à la commande`.
- **Erreur factuelle corrigée** : le bullet n'annonçait qu'un calibre alors que l'option en propose deux.
- Jargon retiré : `lunette rootbeer` → « lunette bicolore, brun et noir » ; `cadran stérile` → « cadran sans logo ».

### Intégrale — Sport chic (7 fiches)

- Calibre affiché : **Seiko NH35** (japonais). Option `Cadran` mono-valeur, pas de choix de mouvement.
- Purgé : `Assemblée à la commande` ; et les comparaisons entre sœurs absentes : « la **seule référence
  de la série** à quitter l'acier intégral », « les **deux bleus de la gamme** », « la plus formelle **des
  deux déclinaisons bleues** », « la déclinaison la plus lumineuse **de la série** ».
- La fiche Brun or rose annonçait un « bracelet acier » hérité du socle alors que son boîtier est or rose :
  le bullet ne qualifie plus la matière du bracelet, faute de source fiable. **À confirmer** (voir plus bas).

### Héritage — Plongeuse vintage 42 (3 fiches)

- Calibre affiché : **Seiko NH35** (japonais).
- Purgé : `saphir annoncé` ; `lume généreux` et `la base la plus culte du mod horloger` (jargon de
  connaisseur, et « base de mod » suggère une montre à modifier, pas un produit fini) ; « la plus lisible
  **du trio** », « la version la plus discrète **des trois** », « plus affirmé que **les deux bleus** ».
- Ajouté : le 5 ATM traduit en usages, avec la restriction explicite (ni nage ni plongée).

### Trente-Six — Classique jubilé (5 fiches)

- Calibre affiché : **Seiko NH35** (japonais). Option `Taille & fond` seule.
- Purgé : `Assemblée à la commande` ; le socle « **cannelée, jubilé, cadrans colorés — à votre goût** »,
  qui annonçait deux familles de produits et un choix de cadran sur une fiche mono-coloris.
- Comparaisons purgées : « le coloris le plus affirmé **de la gamme** », « le choix le plus facile **de la
  gamme** », « le coloris le plus doux **du lot** », « la version la plus démonstrative **de la gamme** ».

### Trente-Neuf — Classique cannelée (6 fiches)

- Calibres affichés : **Miyota 8215 ou Seiko NH35**, tous deux japonais — conformes aux 8 valeurs d'option.
- **Erreur factuelle corrigée** : le bullet annonçait un seul calibre alors que l'option en propose **deux**.
  L'information était fausse pour la moitié des 8 variantes de chaque fiche.
- Purgé : `saphir annoncé`, `Assemblée à la commande`, `Le cœur de gamme NOIRMONT`.
- Comparaisons purgées : « le coloris le moins passe-partout **de la série** », « le compromis **de la
  série** », « le plus sobre **de la série** », « le contraste le plus net **de la gamme** ».

### Quarante-et-Un — Sport acier / Sport cuir (6 fiches)

- Calibres affichés : **Miyota 8215 ou Seiko NH35**, conformes à l'option `Mouvement`.
- Purgé : `verre saphir annoncé` ; `Assemblée à la commande`.
- **Incohérence corrigée** : le socle promettait « un **bracelet intégré** au poignet » sur les 6 fiches,
  y compris les **3 versions cuir à boucle ardillon**. Le bracelet est désormais décrit fiche par fiche.
- Purgé : « **Si vous hésitez entre les six versions** » (fiche Noir Acier) — renvoi explicite au catalogue.

### Noirmont Un Bronze — Plongeuse (1 fiche)

- Calibres affichés : **Miyota 8215 ou Seiko NH35, tous deux japonais, ou PT5000** — conformes aux 6 valeurs.
- **Erreur factuelle corrigée** : le socle annonçait un « **mouvement japonais** » pour toute la fiche alors
  que le **PT5000 ne l'est pas**. La formule isole désormais les deux calibres japonais avant de le nommer.
- Purgé : `verre saphir annoncé` ; `Assemblée à la commande, contrôlée avant expédition`.
- L'étanchéité 200 m est conservée et traduite en usages.

### Trente-Neuf Duo Doré — Classique bicolore (1 fiche)

- Calibres affichés : **Miyota 8215 ou Seiko NH35, tous deux japonais, ou Mingzhu 2813** — conformes aux
  3 valeurs. Le Mingzhu n'est pas présenté comme japonais.
- **Anomalie 3 du lot 1 résolue** : le socle annonçait des « **chiffres romains** » que le cadran ne porte
  pas. La mention est supprimée de la fiche fille. **Elle subsiste sur la mère `10977448722770`.**
- **Erreur factuelle corrigée** : le bullet n'annonçait qu'un calibre là où l'option en propose **trois**.
- Le bullet ne promet plus que le `fond verre`, seule valeur réellement offerte par l'option.

### Remontoir Bois (4 fiches)

- Aucun mouvement, aucun calibre à citer.
- Purgé : « la plus sombre **des quatre essences** », « la plus claire **des quatre essences** ».
- `moteur silencieux` → `moteur discret` (promesse acoustique invérifiable).
- Ajouté : l'explication de ce que fait un remontoir, totalement absente jusqu'ici.

### Rouleau de Voyage — cuir (4 fiches)

- **Erreur factuelle corrigée** : le socle disait « **Deux ou trois montres**, zéro rayure » alors que
  l'option `Capacité` propose **1, 2 ou 3 montres**. La capacité de 1 montre était invisible au client.
- `cuir véritable` → `cuir` (aligné sur le titre, sans qualification invérifiable).
- Purgé : « le coloris le moins courant **de la série** » (fiche Vert).

### Remontoir Collection (5 fiches)

- **Erreur factuelle corrigée** : le socle annonçait « **2 à 6 emplacements** » sur les 5 fiches, alors que
  Bois noir et Bois beige proposent aussi **1 montre**, et que les deux fiches LED **plafonnent à 4**.
  Chaque fiche énonce désormais ses capacités exactes : `1, 2, 4 ou 6` / `2 ou 4` / `2, 4 ou 6`.
- Purgé : « **Le même coffret** en finition bois clair » (Bois beige), qui renvoyait à la fiche voisine.
- `moteurs silencieux` → `moteurs discrets`.

---

## Incohérences titre / sous-titre / option relevées

### 1. Réglée sans intervention — les trois « Sport acier » à bracelet cuir

L'anomalie 4 du lot 1 signalait que les fiches 15-17 gardaient le sous-titre « Sport acier » sur des
versions cuir. **Elles ont déjà été renommées « — Sport cuir »** : titres relus, cohérents. En revanche
c'est leur *description* qui restait fautive (bracelet intégré promis) — corrigé ici.

### 2. ⚠️ À trancher — « Plongeuse » vs 5 ATM sur les 3 Héritage

Les titres annoncent `Héritage <Coloris> — Plongeuse vintage 42`, le corps précise désormais que
l'étanchéité 5 ATM **n'autorise ni la nage ni la plongée**. Titre et contenu se contredisent frontalement.

Deux issues possibles, **non tranchées** car l'erreur peut être dans l'un ou l'autre :
- soit la valeur **5 ATM est erronée** (héritée de la mère, jamais vérifiée fournisseur) ;
- soit elle est juste, et le mot « Plongeuse » doit disparaître des 3 titres.

Par prudence, `seo.title` et `seo.description` disent déjà « **style plongeuse** » / « **d'inspiration
plongeuse** », exact dans les deux cas. **Le titre produit, lui, reste à arbitrer.**

### 3. À noter — « Trente-Six » et « Trente-Neuf » désignent la même paire de diamètres

Les 5 fiches Trente-Six **et** les 7 fiches Trente-Neuf proposent toutes le même choix `36 ou 39 mm`.
Les deux noms de modèle n'ont donc aucune valeur discriminante, et un acheteur peut raisonnablement
croire qu'une « Trente-Six » fait 36 mm. Défaut hérité des mères, hors périmètre éditorial.

### 4. Mineur — libellé des calibres dans les options

Dans les **valeurs d'option**, le Miyota et le Mingzhu portent leur fabricant (`Miyota 8215`,
`Mingzhu 2813`) mais les Seiko sont nus (`NH35`, `NH34`). Les descriptions, elles, écrivent
systématiquement « Seiko NH35 ». Incohérence d'affichage seule — **non corrigée, les options sont hors
périmètre** (y toucher casserait le mapping DSers).

---

## Ce qui reste à trancher

1. **⚠️ Les 3 Héritage : « Plongeuse » ou 5 ATM ?** — le plus urgent, seule contradiction restante
   visible par un client. Demande une confirmation fournisseur de l'étanchéité réelle.
2. **Le verre saphir a été retiré de 13 fiches.** Le texte hérité disait « saphir *annoncé* », un aveu
   d'incertitude qu'on ne peut pas afficher. **Argument de vente perdu** : à confirmer auprès du
   fournisseur, puis à réintroduire en une passe. Fiches : 3 Héritage, 6 Trente-Neuf, 6 Quarante-et-Un
   (dont Noirmont Un Bronze).
3. **Bracelet de l'Intégrale Brun or rose** : acier ou or rose ? Le socle hérité disait « bracelet acier »
   pour toute la famille, douteux sur un boîtier or rose. La matière n'est plus affirmée sur cette fiche.
4. **Les 7 fiches mères portent encore les défauts purgés ici** — `Assemblée à la commande`, les renvois
   de gamme, et les `chiffres romains` du Duo. Non touchées, conformément au brief.
5. **Étanchéité des GMT, Intégrale et chronographes non documentée** — aucune valeur n'existait dans le
   texte hérité, rien n'a été inventé. Ces fiches n'annoncent donc aucune étanchéité, ce qui est une
   question fréquente en préachat.
6. **Les 41 fiches du lot 2 n'ont toujours pas de visuel propre** ni de mapping DSers — hors périmètre.

---

## Annulation

Aucun champ structurel n'a été touché : seuls `descriptionHtml` et `seo` de 60 produits ont changé.
Les descriptions d'origine sont reconstituables depuis les deux fiches de découpage
(`2026-07-25-decoupage-coloris-lot1.md`, `2026-07-31-decoupage-elagage-lot2.md`) et le bloc hérité des 7 mères,
qui n'a pas été modifié et reste lisible sur chacune d'elles.

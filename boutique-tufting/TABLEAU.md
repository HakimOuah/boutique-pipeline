# Tuftéo — TABLEAU

**LE point d'entrée de cette boutique.** Qui que tu sois — Claude, Codex, Grok ou Hakim — tu
commences ici. Le détail des décisions passées est dans [`journal/`](journal/) ; tu n'y vas jamais
pour savoir *quoi faire*. L'état chiffré est dans [`ETAT.md`](ETAT.md), les pièges dans
[`REGLES.md`](REGLES.md).

**Créé le 17/08/2026.** Tuftéo était la seule boutique du parc sans tableau : quinze rapports datés
et aucune porte d'entrée — exactement ce que la méthode du 11/08 devait empêcher. Les rapports sont
désormais dans `journal/`.

---

## Le cadre, en trois phrases

1. **Le Merchant Center est déjà approuvé** — 173 produits, 173 approuvés. On ne cherche pas une
   approbation, on protège un actif. Les suspensions arrivent après.
2. **Le site sert encore publiquement six faux avis.** La correction existe, sur un thème brouillon
   non publié. C'est T-01, et rien ne passe avant.
3. **L'identité est partagée avec trois boutiques sœurs.** Le crible de ces boutiques est un chantier
   séparé — [`../CHANTIER-CRIBLE-ENTITE.md`](../CHANTIER-CRIBLE-ENTITE.md) — mais il **bloque** la
   montée en budget, pas le travail sur Tuftéo.

**Pourquoi publier le thème est un gain net, malgré ses défauts.** L'audit du 16/08 a trouvé des
échecs sur le thème brouillon : bandeau cookies absent, liens sociaux placeholder, H1 dupliqué,
bandeau d'annonce superposé. Ces défauts existent **aussi sur le thème publié** — ils sont antérieurs
à la copie. Publier ne les aggrave donc pas, et retire la seule misrepresentation active. On publie
d'abord, on corrige ensuite.

---

## À FAIRE

### T-01 — Publier la copie de thème « purge faux avis 16-08 »
**État** : À FAIRE · **Pour** : Hakim · **Gravité** : P0
**Pourquoi** : le site sert publiquement six faux avis avec badge « Vérifié » et un compteur
« 4,8/5 — 789 avis » imitant Trustpilot, sur un compte Merchant Center approuvé. C'est le premier
motif de refus GMC, et c'est ce qui a suspendu l'entité en juin.
**Comment** :
1. Prévisualiser le thème `189410738561` (« Tuftéo — purge faux avis 16-08 »).
2. Contrôler l'accueil et la fiche `kit-tufting-complet` : aucun des six noms (Camille R., Léa M.,
   Sarah D., Manon T., Julie B., Chloé P.), aucun « 789 », le compteur de la fiche affiche « 20 avis ».
3. Publier.
4. **Recharger tufteo.com en navigation privée** et refaire le même contrôle sur le site public.
**Sortie attendue** : capture des deux pages publiques sans aucun des six noms ni « 789 ».
**Attention** : tant que ce n'est pas publié, tout le reste est cosmétique. Et « publié » ne se
constate que sur le site public, pas en preview.
**Réf.** : `journal/2026-08-16-audit-gmc.md` §1, `journal/2026-07-30-audit-avis-demo-publics.md`

### T-02 — Bandeau de consentement cookies absent, traceurs posés sans consentement
**État** : À FAIRE · **Pour** : Claude puis Hakim · **Gravité** : P0
**Pourquoi** : aucun bandeau ne s'affiche au premier chargement, y compris en simulant une première
visite, et des scripts et cookies tiers traçants se posent avant tout consentement. C'est une
infraction RGPD/CNIL directe, indépendamment de Google. Et le lien « Préférences en matière de
cookies » du footer **mène à une page 404** — la checklist sanctionne aussi les 404.
**Comment** :
1. Vérifier dans Shopify → Boutique en ligne → Préférences si la bannière de consentement est
   activée, et pour quelles régions.
2. L'activer pour la France/UE, en mode blocage avant consentement.
3. Réparer ou retirer le lien de rappel du footer.
4. Recontrôler en navigation privée : bandeau affiché, refus possible, aucun traceur avant choix.
**Sortie attendue** : bandeau visible au premier chargement, refus fonctionnel, 0 cookie tiers avant
consentement, lien de rappel en 200.
**Réf.** : `journal/2026-08-16-audit-final-c-technique.md` C6

### T-03 — Les liens réseaux sociaux du footer pointent vers le thème de démonstration
**État** : À FAIRE · **Pour** : Claude · **Gravité** : P0
**Pourquoi** : les trois liens (Facebook, YouTube, LinkedIn) pointent vers les comptes du thème
démo — `facebook.com/themefullstack` et équivalents. Ils sont dans le footer **et** dans le JSON-LD
`sameAs`, donc lus par Google comme l'identité déclarée de la marque. Un lien social qui mène hors
site vers un thème commercial est un signal de setup non légitime, et la checklist classe les
« trust assets » comme scorés.
**Comment** : retirer les trois liens des réglages du thème (ne rien lier de neuf ou de faible —
mieux vaut aucun réseau qu'un réseau emprunté), puis vérifier que `sameAs` disparaît du JSON-LD.
**Sortie attendue** : 0 occurrence de `themefullstack` sur le site, `sameAs` absent ou vide.
**Attention** : ne pas y mettre des comptes Tuftéo tout neufs — la checklist l'interdit explicitement.
**Réf.** : `journal/2026-08-16-audit-final-c-technique.md` C1 et C5

### T-04 — Trois délais de livraison contradictoires dans trois documents
**État** : À FAIRE · **Pour** : Hakim tranche, Claude applique · **Gravité** : P0
**Pourquoi** : la policy d'expédition dit **6-10 jours ouvrés**, les CGV disent **8-13**, les CGU
donnent une troisième valeur. Google compare les policies ligne à ligne et la cohérence des chiffres
est le contrôle central de la checklist. Aggravant : c'est la policy d'expédition, normalement la
source de référence, qui est l'exception face à deux documents concordants — signe qu'elle a été
retouchée le 16/08 sans mise à jour en miroir.
**Comment** : Hakim tranche le délai réel, puis on aligne les trois documents **mot pour mot**, plus
la FAQ et le bandeau. Vérifier au passage l'heure limite de commande et son fuseau, le délai de
préparation, la fenêtre de rétractation et le délai de remboursement.
**Sortie attendue** : un seul jeu de chiffres, cité identiquement dans les 3 documents + FAQ.
**Réf.** : `journal/2026-08-16-audit-final-a-contenu.md` A1

### T-05 — Périmètre géographique contradictoire : France ou international ?
**État** : À FAIRE · **Pour** : Hakim tranche · **Gravité** : P1
**Pourquoi** : la policy d'expédition limite la livraison à la France, les CGV promettent
l'international. Une promesse de livraison non tenable est une misrepresentation.
**Comment** : trancher, puis aligner. Rappel : Bien Brûlé avait résolu sa suspension en passant à
« France uniquement, une seule livraison, offerte ».
**Sortie attendue** : un périmètre unique dans les deux documents et dans les réglages d'expédition.
**Réf.** : `journal/2026-08-16-audit-final-a-contenu.md` A1

### T-06 — « Expédition depuis nos entrepôts en Europe » subsiste sur deux pages publiées
**État** : À FAIRE · **Pour** : Claude · **Gravité** : P0
**Pourquoi** : la correction du 16/08 a retiré le possessif du footer et des fiches, mais deux pages
publiées le portent encore. Tuftéo n'a aucun entrepôt : le catalogue vient d'AliExpress par DSers.
Et la mention « depuis l'Europe » elle-même n'est vraie que pour les toiles (Allemagne, Pologne) et
les deux articles électriques (Allemagne) — **pas pour le gun ni le kit**, qui sont les produits
phares.
**Comment** : remplacer partout par le fait vérifiable et déjà tenu — « Livraison offerte en France
en 6 à 10 jours ouvrés, suivi par e-mail » — sans mention d'origine. Option coûteuse écartée :
vérifier l'entrepôt fiche par fiche dans DSers.
**Sortie attendue** : 0 occurrence de « nos entrepôts », et aucune allégation d'origine sur une fiche
non documentée.
**Réf.** : `journal/2026-08-16-audit-final-a-contenu.md` A2, `REGLES.md`

### T-07 — Aligner l'e-mail de la boutique dans Shopify
**État** : À FAIRE · **Pour** : Hakim (action manuelle) · **Gravité** : P1
**Pourquoi** : `shop.email` et `shop.contactEmail` valent toujours `contact.tufteo@gmail.com`, alors
que le footer et les policies affichent `contact@tufteo.com`. **C'est le Gmail que Shopify transmet à
Google.** Une tentative a déjà été faite le 16/08 sans être enregistrée.
**Comment** : Réglages → Coordonnées de la boutique, **les deux champs**, puis revérifier par l'API
que la modification a bien été prise.
**Sortie attendue** : l'API renvoie `contact@tufteo.com` pour les deux champs.
**Réf.** : `journal/2026-08-16-audit-gmc.md`, section « État des corrections de Hakim »

### T-08 — La FAQ promet une date de livraison qui ne s'affiche nulle part
**État** : À FAIRE · **Pour** : Claude · **Gravité** : P1
**Pourquoi** : la FAQ affirme que « la date de livraison estimée s'affiche directement sur chaque
fiche produit ». Les 40 descriptions ont été lues : aucune ne contient de date ni de délai. Le bloc
`delivery-estimation.liquid` existe dans la bibliothèque du thème mais on ne sait pas s'il est posé.
**Comment** : soit poser le bloc sur le template produit et vérifier son rendu, soit retirer la
phrase de la FAQ. La seconde est plus sûre tant que T-04 n'est pas tranché.
**Sortie attendue** : la promesse et l'affichage concordent, constaté sur une fiche réelle.
**Réf.** : `journal/2026-08-16-audit-final-a-contenu.md` A2

### T-09 — Collections sous le seuil de 5 produits, et `frontpage` publiée sans SEO
**État** : À FAIRE · **Pour** : Claude, arbitrage Hakim · **Gravité** : P1
**Pourquoi** : « moins de 5 produits par collection = red flag qualité » dans la checklist. Machines
en compte 4, Toiles 4 dont un brouillon (donc 3 actifs). Et la collection technique `frontpage`, à
**1 produit, sans titre ni meta SEO**, est **publiée sur 4 canaux dont Google & YouTube**.
**Comment** :
1. Dépublier `frontpage` de Google & YouTube et de la Boutique en ligne — c'est une collection
   technique, elle n'a rien à faire dans un flux.
2. Pour Machines et Toiles : compléter le catalogue (le sourcing existe déjà,
   `journal/2026-07-21-sourcing-toile-primaire.md`) ou fusionner. Compléter est préférable avant le
   Q4 — 23 produits reste mince pour du Shopping.
3. Vérifier que chaque collection conservée a un H1 et une meta-description propres : une collection
   sans H1 ni meta ne rapporte rien, c'est le constat fait sur `maisondutemps.com`.
**Sortie attendue** : aucune collection publiée sous 5 produits, `frontpage` hors des canaux.
**Réf.** : `journal/2026-08-16-audit-final-b-catalogue.md` B5

### T-10 — Statut CE des trois articles électriques, et fiches ACTIVE à stock 0
**État** : À FAIRE · **Pour** : Hakim tranche · **Gravité** : P1
**Pourquoi** : tondeuse 200 W, ciseaux électriques et kit tondeuse avaient été passés en DRAFT le
21/07 **en attente de conformité CE**. Ils sont repassés ACTIVE sans aucune trace écrite de la
décision : soit la conformité a été obtenue et il faut l'écrire, soit c'est une régression. Le produit
`original-tufting-accessories` est resté ACTIVE alors que certaines de ses variantes sont des
composants électriques — arbitrage ouvert depuis le 21/07. Par ailleurs deux fiches ACTIVE sont à
stock 0, ce que la checklist demande d'archiver.
**Comment** : Hakim tranche le statut CE et l'écrit dans `REGLES.md` ; puis dépublier ou archiver ce
qui doit l'être. Rappel du parc : dépublier oui, supprimer jamais.
**Sortie attendue** : une ligne écrite par article électrique, et 0 fiche ACTIVE à stock 0.
**Réf.** : `journal/2026-08-16-audit-gmc.md` §11, `journal/2026-07-21-project-state-archive.md`

### T-11 — Deux fiches en brouillon encore liées depuis une collection publiée
**État** : À FAIRE · **Pour** : Claude · **Gravité** : P2
**Comment** : retirer les deux fiches DRAFT des collections publiées, ou les publier si elles sont
prêtes. Vérifier au passage qu'aucun menu ne pointe vers un brouillon.
**Réf.** : `journal/2026-08-16-audit-final-b-catalogue.md` B4

### T-12 — H1 dupliqué sur les six policies
**État** : À FAIRE · **Pour** : Claude · **Gravité** : P2
**Pourquoi** : titre en double confirmé sur 6/6 des policies, en lecture DOM. Défaut de gabarit, pas
de contenu.
**Réf.** : `journal/2026-08-16-audit-final-c-technique.md` C1

### T-13 — Bandeau d'annonce : deux messages superposés en permanence
**État** : À FAIRE · **Pour** : Claude · **Gravité** : P2
**Pourquoi** : pas de rotation propre, les deux messages se chevauchent — visible immédiatement, sur
toutes les pages, mobile et desktop. C'est la première chose que voit un reviewer.
**Réf.** : `journal/2026-08-16-audit-final-c-technique.md` C1

### T-14 — Deux vidéos de galerie produit se téléchargent entièrement sans interaction
**État** : À FAIRE · **Pour** : Claude · **Gravité** : P2
**Pourquoi** : poids inutile au chargement, dégrade la vitesse (cible > 65, non mesurée).
**Réf.** : `journal/2026-08-16-audit-final-c-technique.md`, `journal/2026-08-16-correctifs-theme.md`

### T-15 — Traces du renommage Kaki→Beige et Camel→Taupe dans les noms de fichiers image
**État** : À FAIRE · **Pour** : Claude · **Gravité** : P2
**Pourquoi** : un renommage partiel laisse des traces visibles dans les URL d'images ; la cohérence
titre ↔ URL ↔ option ↔ description ↔ texte alternatif est un item de la checklist.
**Réf.** : `journal/2026-08-16-audit-final-b-catalogue.md` B2

### T-16 — Écrire la consolidation de l'audit final
**État** : À FAIRE · **Pour** : Claude · **Gravité** : P2
**Pourquoi** : les trois agents A, B et C ont rendu leurs rapports le 16/08, mais la consolidation
prévue — tableau pass/fail complet, bloquants classés, **verdict unique soumissible ou non** — n'a
jamais été écrite. Sans elle, personne ne sait dire si la boutique est prête autrement qu'en relisant
trois rapports.
**Sortie attendue** : `journal/2026-08-XX-audit-final-consolide.md`, et ce tableau mis à jour.

### T-17 — Contrôles jamais faits, à faire avant toute montée de budget
**État** : À FAIRE · **Pour** : Claude · **Gravité** : P2
**Comment** : les images produit une par une (texte incrusté, collage, filigrane, doublon entre
fiches, résolution sous 800 px) · la vitesse · les icônes de paiement du footer contre les moyens
réellement proposés au checkout (PayPal et Klarna sont affichés, l'API ne confirme que Shopify Pay et
Apple Pay).
**Réf.** : `ETAT.md`, section « Ce qui n'a jamais été vérifié »

### T-18 — Surveiller le Merchant Center pendant 30 jours après publication
**État** : À FAIRE · **Pour** : Hakim + bot AUDIT PUBLIC · **Gravité** : P1
**Pourquoi** : le compte est approuvé et les suspensions arrivent **après** l'approbation. Le 16/08 a
cumulé 17 nouveaux produits, deux renommages, 215 variantes reprises, une refonte des policies et un
changement d'e-mail ; T-01 ajoutera une publication de thème. Le volume peut déclencher une revue.
**Comment** : relevé quotidien de l'état du compte, des produits désapprouvés ou limités, et des
avertissements. Aucune modification en réponse sans arbitrage.
**Sortie attendue** : un relevé daté par jour pendant 30 jours, et une alerte immédiate au moindre
changement de statut.

---

## FAIT

*(rien encore — les corrections du 16/08 sont sur un thème non publié, donc elles ne comptent pas)*

Ce que le 16/08 a produit et qui attend T-01 pour exister publiquement : purge des six faux avis et
du badge 789 · footer complété (adresse, téléphone cliquable, e-mail) · retrait du possessif « nos
entrepôts » · déduplication des policies avec six redirections 301 · URL du médiateur CM2C ajoutée
aux CGV · téléphone renseigné dans les réglages Shopify · collection Fils portée à 18 produits ·
purge des `compareAtPrice`. Détail : `journal/2026-08-16-execution.md`.

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

1. **Le Merchant Center est déjà approuvé** — 173 produits, 173 approuvés (Hakim, 16/08, non
   remesuré le 17/08 soir). On protège un actif. Les suspensions arrivent après.
2. **T-01 est soldé.** Le thème MAIN est `189429678465` « Tuftéo — correctifs thème 16-08 ».
   Les six faux avis ne sont plus sur l'accueil ni sur la fiche kit. Prochaine priorité :
   les chiffres et allégations encore publics (T-05, T-06, T-08, T-19, T-20).
3. **L'identité est partagée avec les boutiques sœurs.** Le crible
   [`../CHANTIER-CRIBLE-ENTITE.md`](../CHANTIER-CRIBLE-ENTITE.md) **bloque** la montée en budget.
   T-18 (surveillance 30 jours) **a commencé** le jour de la publication du thème.

Audit GMC relancé le 17/08 soir : [`journal/2026-08-17-audit-gmc.md`](journal/2026-08-17-audit-gmc.md).

---

## À FAIRE

### T-02 — Lien cookies en 404, et scripts tiers avant tout choix
**État** : À FAIRE · **Pour** : Claude puis Hakim · **Gravité** : P1
**Pourquoi** : le bandeau est maintenant affiché (Accepter / Refuser / Gérer). Restent : le lien
« Préférences en matière de cookies » → `https://tufteo.com/policies/#…` (**404**), et les scripts
Trustoo + pixel Shopify qui se chargent avant tout clic. `document.cookie` avant choix =
`localization` + `cart_currency` seulement.
**Comment** :
1. Pointer le lien de rappel vers une URL 200 (souvent `/` + ancre), pas `/policies/`.
2. Bloquer Trustoo / pixels avant consentement si Shopify le permet.
3. Recontrôler en navigation privée.
**Sortie attendue** : lien de rappel en 200, bandeau intact, 0 script avis/pub avant choix.
**Réf.** : `journal/2026-08-17-audit-gmc.md`

### T-19 — Réparer le JSON-LD Organization de l'accueil
**État** : À FAIRE · **Pour** : Claude · **Gravité** : P0
**Pourquoi** : virgule orpheline après `logo` — `JSON.parse` échoue, Google ignore adresse,
téléphone et e-mail structurés. C'est le même piège que Noirmont.
**Comment** : sur une copie de thème, fermer l'objet sans virgule finale (ou ajouter `legalName`
inconditionnel). Vérifier `JSON.parse` sur tufteo.com rechargé, pas sur la réponse API.
**Sortie attendue** : un seul bloc `Organization` valide, avec `legalName: OH Ventures` si Hakim
l'accepte.
**Réf.** : `journal/2026-08-17-audit-gmc.md`

### T-20 — Aligner le prix du kit : 229 € (accueil) vs 269 € (fiche)
**État** : À FAIRE · **Pour** : Hakim tranche, Claude applique · **Gravité** : P1
**Pourquoi** : le « Guide de choix » de l'accueil affiche le Kit complet 2-en-1 à **229 €** ;
la fiche et le JSON-LD Product sont à **269 €**. Deux prix publics pour le même objet.
**Comment** : trancher le prix réel, puis corriger le bloc d'accueil (ou la fiche), jamais les deux
dans des sens différents.
**Sortie attendue** : un seul prix, constaté accueil + fiche + schema.
**Réf.** : `journal/2026-08-17-audit-gmc.md`

### T-04 — Trois délais de livraison contradictoires dans trois documents
**État** : QUASI SOLDÉ · **Pour** : — · **Gravité** : P2
**Pourquoi** : relus le 17/08 soir. Expédition, CGV et CGU citent **6 à 10 jours ouvrés**
(CGU : « entre 6 et 10 »). Le 8-13 a disparu. Reste un écart de formulation, pas de chiffre.
**Comment** : rien d'urgent. Harmoniser « à » / « et » si on retouche les CGU pour T-05.
**Réf.** : `journal/2026-08-17-audit-gmc.md`

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
**État** : FAIT le 17/08 (constaté API) — voir section FAIT.

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
2. **Ne pas compléter le catalogue maintenant** — compte GMC approuvé, volume du 16/08 déjà
   encaissé. Fusionner ou attendre. Seul geste utile tout de suite : **dépublier `frontpage`**
   (1 produit, SEO null, URL publique 200).
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
**État** : FAIT le 17/08 — `journal/2026-08-17-audit-gmc.md` (checklist Terry, verdict de protection
d'actif, pas « soumissible / non »).

### T-17 — Contrôles jamais faits, à faire avant toute montée de budget
**État** : À FAIRE · **Pour** : Claude · **Gravité** : P2
**Comment** : les images produit une par une (texte incrusté, collage, filigrane, doublon entre
fiches, résolution sous 800 px) · la vitesse · les icônes de paiement du footer contre les moyens
réellement proposés au checkout (PayPal et Klarna sont affichés, l'API ne confirme que Shopify Pay et
Apple Pay).
**Réf.** : `ETAT.md`, section « Ce qui n'a jamais été vérifié »

### T-18 — Surveiller le Merchant Center pendant 30 jours après publication
**État** : EN COURS depuis le 16/08 18:39 UTC (publication du thème) · **Pour** : Hakim + bot AUDIT PUBLIC · **Gravité** : P1
**Pourquoi** : le compte est approuvé et les suspensions arrivent **après** l'approbation. Le 16/08 a
cumulé 17 nouveaux produits, deux renommages, 215 variantes reprises, une refonte des policies et un
changement d'e-mail ; T-01 ajoutera une publication de thème. Le volume peut déclencher une revue.
**Comment** : relevé quotidien de l'état du compte, des produits désapprouvés ou limités, et des
avertissements. Aucune modification en réponse sans arbitrage.
**Sortie attendue** : un relevé daté par jour pendant 30 jours, et une alerte immédiate au moindre
changement de statut.

---

## FAIT

### T-01 — Publier le thème de purge des faux avis
**FAIT** — constaté le 17/08 soir. MAIN = `189429678465` « Tuftéo — correctifs thème 16-08 ».
Accueil et fiche kit : 0 des six noms, pas de badge 789, fiche « 20 avis ».
**Réf.** : `journal/2026-08-17-audit-gmc.md`

### T-03 — Liens sociaux themefullstack
**FAIT** sur le site public (17/08) : 0 lien social dans le footer, pas de `sameAs` dans le JSON-LD
(le bloc Organization est d'ailleurs invalide — T-19). Résidu : une chaîne de traduction
`consoleLogFullstackUrl`, non cliquable.

### T-07 — E-mail boutique
**FAIT** le 17/08. API : `shop.email` = `shop.contactEmail` = `contact@tufteo.com`.

### T-16 — Consolidation audit
**FAIT** le 17/08 : `journal/2026-08-17-audit-gmc.md`.

Ce que le 16/08 a aussi rendu public avec T-01 : footer (adresse, téléphone, e-mail) · 301 des
anciennes `/pages/*` · Fils à 18 · 0 `compareAtPrice` · mentions légales complétées (SASU, RCS,
SIRET, TVA — lu sur `/policies/legal-notice` le 17/08).

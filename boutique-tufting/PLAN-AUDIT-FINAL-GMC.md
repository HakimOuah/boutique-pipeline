# Plan d'audit final avant soumission GMC — Tuftéo

**16/08/2026.** Audit exhaustif demandé par Hakim avant publication du thème et soumission à Merchant
Center. Référence : skill `gmc-acceptance` (checklist Terry Ecom, 500+ revues de boutiques réelles),
adaptation France, plus les règles maison et **tout ce que la journée du 16/08 a appris**.

**Principe directeur de la journée, à appliquer partout :** un ticket marqué « FAIT » ne prouve rien.
Les six faux avis sont restés en ligne du 30/07 au 16/08 parce que les instructions avaient été
écrites sans être appliquées. **Chaque item est vérifié sur la page réelle, pas dans un rapport.**

Périmètre : le **thème brouillon `189410738561`**, qui est celui que Hakim publiera. Auditer le thème
publié actuel n'aurait aucun intérêt : il est périmé.

---

## Ce qui a déjà été corrigé aujourd'hui — à re-vérifier, pas à croire sur parole

| Correction | Preuve attendue à l'audit |
|---|---|
| 6 faux avis + badge « 4,8/5 — 789 avis » | Aucune occurrence des 6 noms, aucun « 789 », sur accueil **et** fiche produit |
| Policies dupliquées `/pages/*` | 6 redirections 301 actives, 0 lien `/pages/politique-*` au footer, un seul jeu |
| Footer incomplet | `mailto:`, `tel:`, adresse et raison sociale présents et cliquables |
| E-mail incohérent | `contact@tufteo.com` partout : footer, policies, réglages Shopify |
| Médiateur sans URL | `https://www.cm2c.net/` présent à l'article 15 des CGV |
| « Expédié depuis nos entrepôts » | Aucune occurrence de « nos entrepôts » sur tout le site |
| Collection Fils à 1 produit | 18 produits, vignettes = cônes, pas des nuanciers |
| Prix barrés fabriqués | **0 `compareAtPrice` non nul** sur l'ensemble du catalogue |
| Vidéo hero 9,08 Mo | Aucune requête vidéo sur l'accueil |
| Fiches machines | Texte et image concordants, aucun logo, aucun marquage CE |

---

## Répartition en trois agents, sans recouvrement

Leçon du jour : trois agents sur un seul onglet de navigateur **se sont gênés**. D'où une répartition
**par méthode d'accès**, pas seulement par thème, pour qu'ils ne se disputent pas le navigateur.

### Agent A — Contenu, promesses et cohérence textuelle
*Accès : API Shopify + `curl` espacé. Pas de navigateur.*

**A1. Les six policies, mot pour mot.** Relever les chiffres de chacune et vérifier qu'ils sont
**identiques partout** — policy, FAQ, fiche produit, bandeau : heure limite de commande et fuseau,
délai de préparation, délai de transit, fenêtre de rétractation, délai de remboursement. La checklist
dit que Google compare ligne à ligne. Aujourd'hui la politique d'expédition dit 6-10 jours ouvrés et
les fiches n'affichent aucun chiffre : **cet écart doit être tranché**.

**A2. Chasse aux allégations invérifiables**, sur les 40 fiches, les 6 policies et les 5 pages CMS :
« professionnel », « certifié », « CE », « garanti », « n°1 », « qualité premium », toute promesse de
résultat, toute mention d'origine. Chaque occurrence : citation exacte, URL, et **prouvable ou non**.
Rappel : on ne peut écrire « expédié depuis l'Europe » que sur les fiches dont l'entrepôt est vérifié
(aujourd'hui : tondeuse et ciseaux, expédiés d'Allemagne, plus les toiles d'après le sourcing).

**A3. Mentions légales françaises** : raison sociale, forme juridique, capital, SIRET/RCS, adresse,
directeur de publication, hébergeur, médiateur avec son URL, TVA. Signaler les manques.
⚠️ **Incohérence déjà repérée** : Shopify porte « Tuftéo » comme entité et « OH Ventures » comme
adresse, le footer dit « OH VENTURES ». **Une seule entité doit apparaître, celle du registre.**

**A4. Unicité** : les descriptions produit ne doivent pas être copiées entre fiches (les 17 fiches de
fil sont nécessairement proches — vérifier qu'elles ne sont pas identiques mot pour mot), ni reprises
d'un autre domaine, ni des policies partagées avec Bien Brûlé ou Maison Noirmont.

**A5. Fausse urgence** : compte à rebours, « plus que X en stock », « offre limitée » sans date réelle.

### Agent B — Catalogue, données produit et images
*Accès : API Shopify uniquement. Pas de navigateur, pas de `curl`.*

**B1. Prix barrés** : recompter à **0**. C'est le contrôle de la purge, fait par un autre agent.

**B2. Cohérence produit** : titre ↔ URL ↔ valeur d'option ↔ description ↔ texte alternatif.
Le renommage Camel→Taupe et Kaki→Beige a déjà montré qu'un renommage partiel laisse des traces.

**B3. Images, une par une, sur les 40 fiches** : texte incrusté, collage, logo de marque, filigrane,
image dupliquée entre deux fiches, variante sans image propre, image ne correspondant pas à sa
variante, photo fournisseur brute non retravaillée, résolution insuffisante (< 800 px).
Un collage a déjà été trouvé sur « Pièces détachées » — la fiche est en brouillon, à confirmer.

**B4. Statuts et stocks** : produits ACTIVE à stock 0 ; produits ACTIVE non publiés sur le canal
Online Store (**piège maison connu** : les fiches créées par API ne sont publiées sur aucun canal) ;
brouillons encore liés depuis un menu ou une collection.

**B5. Collections** : nombre de produits par collection (seuil 5), collection vide, collection sans
description ni titre SEO propres — **une collection sans H1 ni meta ne rapporte rien**, c'est le
constat de `maisondutemps.com`.

**B6. Conformité produit** : les trois articles électriques (tondeuse, ciseaux, kit tondeuse) et leur
statut CE ; toute mention de marque tierce (Makita, ONEVAN, EASYCLIP) dans un titre, une description
ou un nom de fichier.

### Agent C — Technique et rendu, sur le thème brouillon
*Accès : navigateur, seul à l'utiliser.*

**C1. Rendu réel** sur accueil, fiche produit, collection, panier, et les 6 policies — en **mobile
(375 × 812)** et desktop. Aucune erreur Liquid, aucune erreur console nouvelle, aucun `translation
missing`, aucun placeholder résiduel (`[promo]`, lorem ipsum).

**C2. Liens** : parcourir menu principal, menu footer, menu légal, liens de la home et des fiches.
**Zéro 404**, zéro lien mort, zéro redirection en chaîne. Vérifier que les 6 anciennes URL `/pages/*`
redirigent bien en 301.

**C3. Parcours d'achat** : ajout au panier, mise à jour de quantité, accès au checkout (**sans aller
au paiement**), affichage des frais de port et du seuil de livraison offerte.

**C4. Icônes de paiement du footer contre les moyens réellement proposés au checkout.** Point ouvert :
PayPal et Klarna sont affichés, l'API ne confirme que Shopify Pay et Apple Pay, et Hakim a retiré
Google Pay. **À trancher visuellement.**

**C5. Données structurées** : JSON-LD `Organization` et `Product` valides, `legalName` cohérent avec
les mentions légales, prix et disponibilité corrects. (Le gabarit `organization-schema.liquid` avait
un défaut de virgule sur Noirmont — vérifier qu'il n'est pas partagé.)

**C6. Bandeau cookies** : consentement présent, refus non essentiels possible, pas de dépôt avant
consentement.

**C7. Vitesse** : mesurer ce qui est mesurable sur le brouillon (poids de page, requêtes, absence de
vidéo). **Ne pas annoncer de score PageSpeed** : l'outil ne sait pas tester un thème non publié.

---

## Ce qui reste hors de portée d'un agent — pour Hakim

- ✅ **Téléphone testé par Hakim le 16/08 : le +33 7 56 82 80 94 répond en vocal.** Item PASS,
  preuve = test direct de Hakim. La checklist l'exige explicitement (« numéro testé : accepte
  réellement les appels vocaux »).
- ✅ **E-mail testé par Hakim le 16/08 : `contact@tufteo.com` reçoit bien.** Item PASS, preuve = test
  direct de Hakim.
- Vérifier que le **Gmail dédié** au GMC est distinct et « réchauffé ».
- **Adresse et téléphone partagés avec Bien Brûlé et Maison Noirmont** : décision assumée (voir
  échange du 16/08). Le risque n'est pas la mutualisation en soi mais la **propagation** d'une
  suspension entre boutiques liées — d'où l'exigence que chacune soit irréprochable.
- Réseaux sociaux : ne rien lier de neuf ou de faible.

---

## Restitution

Chaque agent écrit son propre fichier — `AUDIT-FINAL-A-contenu.md`, `-B-catalogue.md`,
`-C-technique.md` — au fil de l'eau, avec pour **chaque item** : verdict **PASS / FAIL / NON VÉRIFIÉ**,
la preuve (URL, citation, chiffre, capture), et la correction proposée si FAIL.

Puis consolidation par Claude dans **`AUDIT-FINAL-GMC-2026-08-16.md`** : tableau pass/fail complet,
**bloquants classés par gravité**, et verdict unique — *soumissible* ou *non soumissible*, sans
demi-mesure. La règle de la checklist est nette : **un seul item en échec = ne pas soumettre.**

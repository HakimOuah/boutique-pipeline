---
type: journal
boutique: seiko-mod
date: 2026-09-01
nature: intervention
leviers: [conformite]
titre: "Passe de correction — Jubilé, options fournisseur, délai FAQ"
---

# Passe de correction — 01/09/2026

Suite de l'audit du même jour. Corrections appliquées sur la boutique live via l'API Admin.
« Jubilé » est remplacé partout par **« cinq rangs »**, la description réelle du bracelet
(deux rangs larges encadrant trois rangs centraux) — pas un autre nom emprunté.

## Jubilé — 20 fiches

| Surface | Volume |
|---|---|
| Titres | 8 (`Bracelet cinq rangs acier : 20 mm`, `Bracelet cinq rangs : embouts courbes`, `Trente-Six … : Classique cinq rangs` ×6) |
| Handles + **301** | 8 publics, vérifiés en 301 ; +1 brouillon (`boitier-plongee-40-200m-cinq-rangs`) |
| `seo.title` | 6 |
| `seo.description` | 15 |
| `descriptionHtml` | 16 |
| Valeurs d'option | 3 (`Cinq rangs`, `Cinq rangs · or rose (réf. 15)`, `Cinq rangs · acier & or`) |
| Alts + noms de fichiers CDN | 43 sur 53 — **10 restent bloqués**, voir plus bas |

Reformulations non mécaniques : « Un bracelet jubilé, ce sont cinq rangs de maillons » →
« Ce bracelet, ce sont cinq rangs de maillons » · « bracelet jubilé à cinq rangs » →
« bracelet à cinq rangs » · « les maillons centraux du jubilé » → « du bracelet ».

## Options fournisseur — 13 fiches actives

- **`Ships From : China Mainland` supprimée** de `doigtiers-d-horloger-latex` (`productOptionsDelete`,
  stratégie non destructive). C'était la contradiction la plus lisible du site : une option publique
  déclarant l'expédition depuis la Chine sous un bandeau « Livraison offerte en France métropolitaine ».
- Noms d'options traduits : `Band Color` → `Finition` / `Coloris & boucle` / `Épaisseur & finition`,
  `Band Width` → `Largeur`, `Color` → `Coloris` / `Capacité` / `Conditionnement` / `Grossissement` /
  `Coloris & capacité` / `Coloris & conditionnement`.
- **~150 valeurs traduites** : `steel-no logo` → `Acier`, `white 100pcs` → `Blanc · 100 pièces`,
  `1.0mm-rose gold` → `1,0 mm · or rose`, `Green-Silver Buckle` → `Vert · boucle acier`,
  `Black Brown 3 Slot` → `Noir & brun · 3 emplacements`, `15X-with circle` → `15× · avec anneau`,
  `13pc Kits` → `Kit 13 pièces`, `20mm` → `20 mm`…

Contrôle live : **0** `no logo`, `ships from`, `china mainland`, `band color`, `band width`, `pcs`,
`circle` sur les 96 fiches publiques.

## Autres

- **FAQ** : « Comptez généralement 2 à 3 semaines » → « Comptez **14 à 21 jours calendaires** après la
  commande ». Le site n'annonce plus qu'une seule fenêtre de livraison.
- **301** posé sur `/products/mouvement-miyota-8215-nh34-gmt` → `mouvement-calibre-8215-nh34-gmt`
  (renommé le 31/08 sans redirection).

## Reste à faire

**Bloqué par le connecteur MCP :**

- `/collections/frontpage` (publiée, dans le sitemap, 1 produit) — `publishableUnpublish` est refusé
  par la politique de sécurité du connecteur. **2 clics dans l'admin** : Collections → Page d'accueil
  → retirer « Boutique en ligne » et « Google & YouTube ».
- Les policies : scope `write_legal_policies` absent. Quatre corrections à faire à la main :
  1. **Coordonnées** : SIRET `10315725100010` → `103 157 251 00010`, TVA `FR55103157251` → `FR55 103157251` (le reste du site écrit la version espacée)
  2. **CGV, article 15** : `<meta charset="utf-8">` dans le corps, juste avant le bloc CM2C — c'est le défaut listé dans `audit-lecons-noirmont.md`, jamais retiré
  3. **CGU, §2** : lien vers `/pages/mentions-legales` (page CMS dépubliée, aujourd'hui en 301) → pointer `/policies/legal-notice`
  4. **Mentions légales, §4 et §5** : trois `<a>` sans `href` (« Politique de confidentialité »,
     « Politique de cookies », « Conditions générales de vente ») — liens morts

**Bloqué côté Shopify (file lock) :** 10 fichiers CDN portent encore `jubile` dans leur nom et
« Classique jubilé » dans leur `alt`. Le premier envoi groupé a échoué sur une erreur temporaire
Shopify puis a laissé ces fichiers en « opérations en attente » ; ils sont `READY` mais refusent
toute écriture depuis — six tentatives sur une quinzaine de minutes, toutes rejetées.

**Ce n'est pas cosmétique** : sur `/products/trente-six-dore-classique-cinq-rangs`, le HTML rendu
contient encore **66 occurrences** de `jubil` (URL d'images dans le JSON du thème + 8 attributs
`alt`). Tant que ces 10 fichiers ne sont pas renommés, le crawler voit le mot. À reprendre :

```
59693975437650 59693975470418 59693975503186 59893480620370 59893499003218
59935330632018 59935331025234 59935332925778 59935335317842 59935335809362
```

**En attente d'arbitrage de Hakim :** `montre-acier-chiffres-3-6-9-explorateur` (ACTIVE) —
titre et SEO title « **Explorateur** », cadran 3-6-9. Même registre que Jubilé et Président, mais
« explorateur » est un mot français courant et non le nom commercial de la marque. Cité aussi dans la
description de la collection `montre-cadran-a-chiffres`. Non touché.

**Optionnel :** 42 fichiers CDN nommés en anglais d'après les anciennes valeurs fournisseur
(`…-v-green-silver-buckle.jpg`, `…-v-black-purple-6-slot.jpg`). Aucune marque, aucune origine —
cosmétique, écarté de cette passe pour ne pas multiplier les renommages simultanés.

## Examen GMC

La passe est nouvelle et crawlable : recompter **7 à 10 jours à partir du 01/09**, soit une fenêtre
**8–11 septembre**, et seulement une fois `frontpage`, les policies et les 10 fichiers réglés.
Toujours 0 ads.

---

# GMC 5840460291 — relevé du 01/09/2026

Accès obtenu via le profil Chrome « Noirmont » (l'extension y a été installée en cours de session).
Compte **OH Ventures — 5840460291**. Lecture seule : rien n'a été cliqué qui soumette quoi que ce soit.

## État

| Indicateur | Valeur |
|---|---|
| Problème | **Déclarations trompeuses ou déceptives** — « Empêche l'affichage de tous les produits dans ces pays : France » |
| Détection | « Google a détecté ce problème grâce à des **vérifications automatisées** » |
| Articles dans le flux | **883** (les 96 fiches × variantes) |
| Approuvés | **0** |
| Refusés | **883** |
| En cours d'examen | **0** |
| Clics 28 j | 7 (fiches gratuites) · clics annonces 0 · coût 0,00 € |
| Qualité du magasin | « informations non disponibles pour le moment » |

Motif affiché : « D'après les informations disponibles sur votre établissement, nous avons des raisons
de croire que les clients sont trompés sur Google. » Suit la liste générique de bonnes pratiques
(transparence sur l'identité et le modèle économique, avis et badges, design + SSL, renseigner
« Informations sur l'entreprise », cohérence données produit / boutique). **Aucun élément spécifique
n'est cité** — le diagnostic ne dit pas ce qui a déclenché la détection.

## Deux faits opérationnels

1. **Il n'y a pas de bouton « Demander un examen » sur ce problème.** La seule action proposée est
   **« Je ne suis pas d'accord avec le problème »** — c'est par là que passe la demande de réexamen.
   Non cliqué : la boutique n'est pas prête (voir « Reste à faire »).
2. **Second problème ouvert : « Aucun compte Google Ads associé ».** Le lien Ads posé le 18/08 via
   l'app Google & YouTube n'existe plus côté GMC. À reconnecter avant toute campagne — mais pas
   maintenant : rien ne doit bouger brutalement avant le réexamen.

## Suite

Le compteur de 7–10 jours court désormais à partir du **01/09** (passe de correction du jour),
et ne se déclenche vraiment qu'une fois `frontpage`, les quatre policies et les 10 fichiers réglés.
Toujours 0 ads.

---
type: livraison
boutique: seiko-mod
date: 2026-09-01
titre: "Reste à faire après la passe de correction du 01/09 — brief exécutable"
destinataire: cursor
---

# Reste à faire — Maison Noirmont, 01/09/2026

**État 01/09 soir (Cursor) :** blocs 1 et 2 **faits**. Bloc 3 **toujours verrouillé**
(`FILE_LOCKED` sur les 10 IDs, admin inclus). Journal :
`journal/2026-09-01-reste-cursor-blocs.md`.

Boutique : **maisonnoirmont.fr** (`v42pzp-h4`). Thème MAIN : `205451100498`.
Contexte : ban GMC 5840460291 « Déclarations trompeuses ou déceptives », toujours actif au 01/09.
La passe de correction du jour (Jubilé → cinq rangs, options fournisseur, FAQ, 301) est faite.
Trois blocs restent, bloqués par des limites d'accès. **Ne rien faire d'autre que ce qui suit.**

## Interdits — à respecter strictement

- Ne pas demander l'examen GMC, ne pas cliquer « Je ne suis pas d'accord avec le problème ».
- Ne pas lancer d'ads, ne pas reconnecter le compte Google Ads.
- Ne pas toucher `montre-acier-chiffres-3-6-9-explorateur` ni le mot « Explorateur » dans la
  description de la collection `montre-cadran-a-chiffres` : arbitrage en attente de Hakim.
- Ne pas renommer les 42 fichiers CDN contenant `buckle` ou `slot` : écarté volontairement.
- Ne pas republier le thème, ne pas toucher aux 96 fiches actives au-delà des points ci-dessous.

---

# Bloc 1 — Dépublier la collection `frontpage`

Elle est publiée, présente dans `sitemap_collections_1.xml`, et ne contient **1 seul produit**.
Une collection quasi vide et crawlable est un signal négatif avant un réexamen GMC.

- Collection : titre « Page d'accueil », handle `frontpage`,
  id `gid://shopify/Collection/690653954386`
- Publications à retirer :
  - « Boutique en ligne » — `gid://shopify/Publication/358599295314`
  - « Google & YouTube » — `gid://shopify/Publication/362955342162`

**Voie admin (la plus simple)** : Produits → Collections → « Page d'accueil » → encadré
« Publication » → décocher *Boutique en ligne* et *Google & YouTube* → Enregistrer.

**Voie API** (`publishableUnpublish` est refusé par le connecteur MCP de Claude ; il passe depuis un
accès Admin API classique) :

```graphql
mutation {
  publishableUnpublish(
    id: "gid://shopify/Collection/690653954386"
    input: [
      { publicationId: "gid://shopify/Publication/358599295314" }
      { publicationId: "gid://shopify/Publication/362955342162" }
    ]
  ) { userErrors { field message } }
}
```

**Vérification** : `curl -s -o /dev/null -w "%{http_code}" https://maisonnoirmont.fr/collections/frontpage`
doit rendre **404**, et l'URL doit disparaître de
`https://maisonnoirmont.fr/sitemap_collections_1.xml?from=690653954386&to=691208290642`.

---

# Bloc 2 — Quatre corrections dans les policies

Le connecteur utilisé le 01/09 n'a pas le scope `write_legal_policies`. À faire soit dans l'admin
(**Paramètres → Politiques**), soit par API avec ce scope, via
`shopPolicyUpdate(shopPolicy: { type: <TYPE>, body: "<corps complet>" })`.

**Attention** : `shopPolicyUpdate` remplace le corps **entier**. Récupérer le corps actuel avec
`{ shop { shopPolicies { type body } } }`, appliquer le remplacement exact, renvoyer le tout.
Ne changer que les chaînes indiquées. **Ne pas modifier les dates de version** (« 15 août 2026 »)
sur les policies 2b / 2c / 2d : leur contenu juridique ne change pas, seuls des liens et un artefact
HTML sont corrigés.

## 2a — `CONTACT_INFORMATION` (« Coordonnées »)

Le SIRET et la TVA y sont écrits collés, alors que le footer, les mentions légales, les CGV et
les CGU les écrivent espacés. Une seule écriture doit survivre.

Remplacer exactement :

```html
<p>SIRET : 10315725100010<br>N° TVA intracommunautaire : FR55103157251<br>Capital social : 1000 €</p>
```

par :

```html
<p>SIRET : 103 157 251 00010<br>N° TVA intracommunautaire : FR55 103157251<br>Capital social : 1 000 €</p>
```

Puis, pour aligner les horaires SAV sur le footer, remplacer exactement :

```html
<p>Nous répondons aux demandes du lundi au vendredi. Pour toute question sur une commande, précisez votre numéro de commande.</p>
```

par :

```html
<p>Nous répondons aux demandes du lundi au vendredi, de 9h à 17h, sous 48 heures ouvrées. Pour toute question sur une commande, précisez votre numéro de commande.</p>
```

## 2b — `TERMS_OF_SALE` (CGV), article 15

Un `<meta charset="utf-8">` traîne dans le corps de la policy, juste avant le bloc CM2C. C'est un
défaut listé dans `.claude/skills/gmc-acceptance/references/audit-lecons-noirmont.md` depuis le
23/08 et jamais retiré. L'URL du médiateur doit aussi devenir un vrai lien (art. R. 616-1).

Remplacer exactement :

```html
<p>Si la réponse n'est pas satisfaisante ou en l'absence de réponse dans un délai raisonnable, le consommateur peut recourir gratuitement au médiateur dont relève OH Ventures : <meta charset="utf-8"><span>CM2C, 14 rue Saint Jean, 75017 Paris, Tél : 01 89 47 00 14, site internet : https://www.cm2c.net/</span></p>
```

par :

```html
<p>Si la réponse n'est pas satisfaisante ou en l'absence de réponse dans un délai raisonnable, le consommateur peut recourir gratuitement au médiateur dont relève OH Ventures : CM2C, 14 rue Saint Jean, 75017 Paris, tél. 01 89 47 00 14, site internet : <a href="https://www.cm2c.net/" rel="noopener noreferrer" target="_blank">https://www.cm2c.net/</a></p>
```

## 2c — `TERMS_OF_SERVICE` (CGU), §2

Le lien pointe vers `/pages/mentions-legales`, page CMS dépubliée qui répond aujourd'hui en 301.
Il doit pointer directement sur la policy.

Remplacer exactement :

```html
<a href="/pages/mentions-legales">Mentions légales</a>
```

par :

```html
<a href="/policies/legal-notice">Mentions légales</a>
```

## 2d — `LEGAL_NOTICE` (Mentions légales), §4 et §5

Trois balises `<a>` sans `href` : liens morts pour un examinateur qui clique.

| Remplacer exactement | par |
|---|---|
| `<a>Politique de confidentialité</a>` | `<a href="/policies/privacy-policy">Politique de confidentialité</a>` |
| `<a>Politique de cookies</a>` | `<a href="/pages/politique-de-cookies">Politique de cookies</a>` |
| `<a>Conditions générales de vente</a>` | `<a href="/policies/terms-of-sale">Conditions générales de vente</a>` |

**Vérification du bloc 2** : récupérer les six pages `/policies/*` en visiteur anonyme et contrôler
qu'il ne reste **0** occurrence de `meta charset`, **0** de `10315725100010`, **0** de
`FR55103157251`, **0** de `href="/pages/mentions-legales"`, et **0** balise `<a>` sans `href`.

---

# Bloc 3 — Dix fichiers CDN encore nommés `jubile`

## Pourquoi ça compte

Ce n'est pas cosmétique. Sur `https://maisonnoirmont.fr/products/trente-six-dore-classique-cinq-rangs`,
le HTML rendu contient encore **66 occurrences** de `jubil` : les URL d'images dans le JSON du thème,
plus 8 attributs `alt`. Le crawler voit donc toujours le mot, qui appartient à la nomenclature Rolex
(Oyster / Jubilee / President) — la même famille que « Président », purgé le 23/08 comme cause du ban.

## Le blocage rencontré

Le premier envoi groupé de `fileUpdate` a échoué sur une erreur temporaire Shopify, qui a laissé ces
dix fichiers en **« opérations en attente »**. Ils sont pourtant `fileStatus: READY`. Une dizaine de
tentatives sur ~45 minutes — groupées, unitaires, et en `alt` seul sans `filename` — ont toutes été
rejetées avec le même message.

**Ordre de préférence pour Cursor :**

1. Réessayer `fileUpdate` (la file d'attente Shopify se débloque parfois d'elle-même). Y aller
   **un fichier à la fois**, pas en lot de dix : c'est le lot qui a créé le blocage.
2. Si le message « opérations en attente » persiste, passer par l'admin :
   **Contenu → Fichiers**, rechercher `jubile`, et pour chacun des dix, éditer le nom et le texte
   alternatif. L'interface admin emprunte un autre chemin que l'API et n'est pas concernée par ce
   verrou.

## Les dix fichiers

| `MediaImage` id | Nouveau nom de fichier | Nouveau texte alternatif |
|---|---|---|
| 59693975437650 | `trente-six-dore-classique-cinq-rangs-02-situation.jpg` | Trente-Six Doré — Classique cinq rangs — en situation — Maison Noirmont |
| 59693975470418 | `trente-six-dore-classique-cinq-rangs-03-macro.jpg` | Trente-Six Doré — Classique cinq rangs — macro — Maison Noirmont |
| 59693975503186 | `trente-six-dore-classique-cinq-rangs-04-poignet.jpg` | Trente-Six Doré — Classique cinq rangs — au poignet — Maison Noirmont |
| 59893480620370 | `trente-six-dore-classique-cinq-rangs-g1.jpg` | Trente-Six Doré — macro frontale de la jonction boîtier-bracelet : cadran champagne soleillé à index acier en haut de cadre, boîtier et bracelet cinq rangs en acier — Maison Noirmont |
| 59893499003218 | `trente-six-or-integral-classique-cinq-rangs-g1.jpg` | Trente-Six Or intégral — macro de la jonction boîtier-bracelet : boîtier, bracelet cinq rangs et cadran dans la même teinte or jaune, relief donné par l'alternance satiné-poli des maillons — Maison Noirmont |
| 59935330632018 | `trente-six-or-integral-classique-cinq-rangs-situation.jpg` | Trente-Six Or intégral — Classique cinq rangs — en situation — Maison Noirmont |
| 59935331025234 | `trente-six-or-integral-classique-cinq-rangs-macro.jpg` | Trente-Six Or intégral — Classique cinq rangs — macro — Maison Noirmont |
| 59935332925778 | `trente-six-rose-classique-cinq-rangs-poignet.jpg` | Trente-Six Rose — Classique cinq rangs — au poignet — Maison Noirmont |
| 59935335317842 | `trente-six-rose-classique-cinq-rangs-macro.jpg` | Trente-Six Rose — Classique cinq rangs — macro — Maison Noirmont |
| 59935335809362 | `trente-six-rose-classique-cinq-rangs-situation.jpg` | Trente-Six Rose — Classique cinq rangs — en situation — Maison Noirmont |

Forme de la mutation, un fichier à la fois :

```graphql
mutation {
  fileUpdate(files: [
    { id: "gid://shopify/MediaImage/59693975437650",
      filename: "trente-six-dore-classique-cinq-rangs-02-situation.jpg",
      alt: "Trente-Six Doré — Classique cinq rangs — en situation — Maison Noirmont" }
  ]) { userErrors { field message } }
}
```

**Ne pas** utiliser `fileDelete` ni réimporter les images : les médias doivent garder leur id et leur
rattachement aux fiches. Seuls `filename` et `alt` changent.

**Vérification du bloc 3** :

```bash
curl -s https://maisonnoirmont.fr/products/trente-six-dore-classique-cinq-rangs | grep -oi jubil | wc -l
```

doit rendre **0**. Idem sur `trente-six-or-integral-classique-cinq-rangs` et
`trente-six-rose-classique-cinq-rangs`. Et le catalogue public entier :

```bash
curl -s "https://maisonnoirmont.fr/products.json?limit=250" | grep -oi jubil | wc -l
```

doit rendre **0** (il rend 10 aujourd'hui, uniquement des noms de fichiers).

---

# Vérification finale, une fois les trois blocs faits

```bash
curl -s "https://maisonnoirmont.fr/products.json?limit=250" \
  | grep -oiE "jubil|seiko|miyota|mingzhu|presiden|904l|skx|no logo|ships from|china mainland|band color|band width" \
  | sort | uniq -c
```

Attendu : **aucune sortie**.

Puis relire la checklist §6 de `.claude/skills/gmc-acceptance/references/checklist-pre-soumission.md`
et `references/audit-lecons-noirmont.md`.

# Après

Le compteur de 7 à 10 jours repart de la **date du dernier changement crawlable**, donc de la fin de
ces trois blocs. Toujours 0 ads. La demande de réexamen GMC reste une décision de Hakim : sur ce
problème, Merchant Center ne propose pas de bouton « Demander un examen » mais seulement
« Je ne suis pas d'accord avec le problème », et une demande consommée trop tôt se paie cher.

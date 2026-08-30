---
type: journal
boutique: seiko-mod
date: 2026-08-13
nature: intervention
leviers: [conformite, page]
titre: "Conformité et textes — 13/08/2026"
---

# Conformité et textes — 13/08/2026

Session sans génération d'image (quota de l'exécutant épuisé jusqu'au 18/08).
Trois tickets traités : **T-04** (2 fiches arabes), **T-08** (`alt` génériques), **T-11** (audit GMC repris point par point).

Méthode : export en masse du catalogue par `bulkOperationRunQuery` (201 produits, 2 080 médias,
3 009 variantes), lecture des sept politiques et du thème publié par l'API, requêtes anonymes sur
`maisonnoirmont.fr`, et **ouverture visuelle de chaque image** avant toute réécriture d'`alt`.

---

## T-04 — Les 2 fiches arabes du 11/08 sont conformes au standard

Les deux fiches portaient un handle AliExpress brut, aucun titre SEO, aucune description, aucun tag,
aucun `productType` et n'appartenaient à aucune collection.

| | Fiche A | Fiche B |
|---|---|---|
| Produit Shopify | `11017842360658` | `11017842458962` |
| Source AliExpress | `1005009751528666` (XinXin Watch Parts Store) | `1005007348127532` (Watch DlY Factory Store) |
| Ancien handle | `new-arabic-sky-blue-nh35-28-5mm-sunburst-watch-dial-…` | `28-5mm-dial-diy-arabic-alphabet-surface-no-date-…` |
| Nouveau handle | `cadran-arabe-oriental-soleille-28-5` | `cadran-arabe-oriental-radial-28-5` |
| Titre | Cadran chiffres arabes orientaux 28,5 mm soleillé avec date — 11 coloris, pour NH35 | Cadran chiffres arabes orientaux 28,5 mm rayonné sans date — 12 finitions, pour NH35 |
| Variantes | 11 | 12 |

Les deux handles étaient **libres** (vérifié avant écriture), les deux fiches restent en **DRAFT**,
aucun prix n'a été touché. Elles sont désormais dans la collection `cadran-arabe`, qui passe de 5 à
7 produits.

### D'où viennent les caractéristiques

Rien n'a été inventé. Chaque ligne de la description vient d'une source vérifiable :

- **diamètre 28,5 mm, compatibilité NH35 / NH36 / 4R** : titres fournisseur officiels relevés par
  l'API (`journal/2026-08-09-resourcing-cadran-arabe.md`, `journal/2026-08-10-resourcing-cadran-arabe-agent.md`).
  Le texte dit explicitement « compatibilité **annoncée par le fournisseur** » et « nous n'avons pas
  monté ce cadran nous-mêmes » — nous ne l'avons pas testée ;
- **guichet de date à 3 h sur la fiche A, absence de guichet sur la fiche B** : deux sources
  concordantes — le relevé API (`preuves/preuves-sourcing-api-2026-08-09/1005009751528666.json`,
  champ `visual_qa.notes`) et **l'ouverture des 23 visuels** ;
- **chiffres orientaux appliqués en relief, piste des minutes graduée 5→60 en chiffres occidentaux
  sur la fiche A, absence de piste sur la fiche B, absence de tout lettrage** : lus sur les images,
  planche par planche puis au zoom natif ;
- **liste des finitions** : titres exacts des variantes Shopify, traduits, et **recalés sur ce que
  montre l'image** — la variante fournisseur « Brown » de la fiche A est en réalité un cuivre orangé,
  elle est décrite comme telle.

Aucune promesse de délai n'a été écrite, conformément à `REGLES.md`.

**Reste sur ces deux fiches** : leurs 23 variantes portent encore un SKU AliExpress brut (voir T-28),
et leur prix est le coût fournisseur (T-H3).

---

## T-08 — 87 `alt` réécrits, le défaut était plus large que la fiche signalée

Balayage des 2 080 médias du catalogue. Trois défauts distincts ont été séparés :

| Défaut | Volume | Traitement |
|---|---:|---|
| `alt` vide | **1 220** | **Aucun** — ce sont, sans exception, des photos AliExpress brutes sur des brouillons (noms de fichiers CDN `S…` / `H…`). Elles seront remplacées par T-07 ; leur écrire un `alt` serait du travail jeté. **Zéro visuel maison sans `alt`.** |
| `alt` répété dans une même fiche | **0** | — |
| `alt` générique ou faux | **87** | Réécrits |

Les 87 se répartissent sur **8 fiches** :

- `cadran-sterile-lumineux-28-5` — 17 `alt` « variante 1 … variante 17 » (la fiche du ticket) ;
- `cadran-sterile-couronne-3h-28-5` — 7 `alt` « variante A1 … A7 » ;
- `cadran-vierge-sterile-28-5` et `cadran-sterile-sunburst-28-5` — 24 `alt` « variante <couleur> » ;
- `cadran-pilote-33-5-aiguilles-lumineuses` et `cadran-pilote-29-mod-nh35` — 4 `alt` portant un code
  fournisseur non traduit (« variante Black Dial 1 », « black dial 2 lume ») ;
- les 2 fiches arabes de T-04 — 23 `alt` enrichis au passage ;
- + les 12 `alt` de plan (« vue de face », « vue rapprochée », « mise en situation ») de ces fiches,
  qui décrivaient le cadrage mais pas le produit.

**Les 51 visuels concernés ont été ouverts.** C'était nécessaire : sur `cadran-vierge-sterile-28-5`
et `cadran-sterile-sunburst-28-5`, plusieurs `alt` **décrivaient mal l'image** — la variante « Brun »
est un orange cuivré franc, la « Violet » est un magenta, la « Orange » est un ambre doré. Ces `alt`
n'étaient pas génériques, ils étaient faux ; ils sont maintenant décrits tels qu'ils apparaissent,
en gardant le mot du fournisseur entre les deux (« brun orangé cuivré », « violet magenta ») pour ne
pas casser le lien avec le nom de variante.

Chaque `alt` dit désormais la couleur, la finition, le type d'index et **la présence ou l'absence de
guichet de date** — l'information qui décide de l'achat sur une pièce de mod.

Aucun média n'a été supprimé ni déplacé ; seul le champ `alt` a été modifié, par `fileUpdate`.

---

## T-11 — Audit GMC du 08/08 repris point par point

**Le thème MAIN a changé** : c'est aujourd'hui `TRAVAIL Noirmont — publier apres validation`
(`205089014098`) qui est publié. Les correctifs préparés en thème de travail sont donc bien en ligne.

### Les neuf P0

| # | Point | État réel au 13/08 | Preuve |
|---|---|---|---|
| 1 | 9 visuels de faux témoignages sur 37 fiches | ✅ **soldé** | Scan des 2 080 médias : aucun fichier suffixé `-6`/`-7`, aucun `alt` contenant « témoignage » |
| 2 | 910 SKU AliExpress | ❌ **régression, pire qu'avant** | **2 065 variantes sur 3 009** portent encore un SKU brut (`14:201447598#Black Silver Dial`), sur **84 brouillons et 9 archivés**, dont **95 contenant « no logo »**. Les 96 fiches actives sont propres (`NOIR-T39-017`…). La réécriture du 08/08 n'a touché que le catalogue d'alors ; **les 94 fiches importées le 09/08 sont arrivées avec les SKU bruts et n'ont jamais été renommées** → **T-28** |
| 3 | E-mail de la boutique | ⚠️ **partiel** | `shop.email` = `shop.contactEmail` = `contact.noirmont@gmail.com`. Mais la politique de confidentialité servie publie désormais `contact@maisonnoirmont.fr` **en dur** : la contradiction publique a disparu, il reste l'adresse expéditeur des e-mails de commande → **T-H4** |
| 4 | Consentement cookies | ❌ **non soldé — et le contraire de ce qu'on croyait** | Requête anonyme : pas de `#shopify-pc__banner`, pas de `Shopify.customerPrivacy`, pas de `_tracking_consent`. **Aggravant découvert aujourd'hui** : la page « Politique de cookies », publiée, **affirmait** qu'un bandeau accepter/refuser s'affiche et qu'un lien « Préférences en matière de cookies » figure en bas de chaque page. Les deux sont faux — le lien a même été retiré du menu depuis. Texte corrigé aujourd'hui (voir plus bas) ; le bandeau reste à installer → **T-29** |
| 5 | Mesure d'achat | ❌ non soldé | `gtag`, `dataLayer`, `googletagmanager`, `AW-`, `G-XXXXXX` : zéro occurrence. Seul `trekkie` (analytics interne Shopify) → **T-10** |
| 6 | Sections d'avis fabriqués + badge « 4,8/5 · 1340 avis » | ✅ **soldé sur le thème publié** | `reviews_rXFabc`, `reviews_8P6xW3`, `reviews_badge_noirmont`, `reviews_badge_efW9wU` et **tous** les blocs `rating-stars` : `disabled: true`. Les chaînes « 4,8/5 », « 1340 avis », « 2 000 clients satisfaits » et `review_count: 123` subsistent **dans les fichiers**, mais sous des parents désactivés : elles ne sont pas servies |
| 7 | Politique de remboursement ≡ CGV ≡ vitrine | ✅ **soldé** | Les 7 politiques sont datées du 10/08. Plus aucune clause « portés… ne sont pas repris » : la politique de remboursement dit « le client peut manipuler et examiner le produit comme il pourrait raisonnablement le faire en magasin », les blocs `product.json` et `cart.json` disent « 14 jours … montre portée à l'essai comprise ». Les trois versions concordent |
| 8 | Médiateur de la consommation | ❌ **non soldé — T-H2 était coché à tort** | CGV **article 15, servi en ligne** : `[[MEDIATEUR_NOM]]`, `[[MEDIATEUR_ADRESSE]]`, `[[MEDIATEUR_SITE]]`. Les marqueurs sont toujours là |
| 9 | Ne pas créer le GMC | ✅ respecté | Aucun compte |

### Les quinze P1

| # | Point | État | Note |
|---|---|---|---|
| 10 | Téléphone cliquable au pied de page | ❌ | Aucun `tel:` dans `sections/footer.liquid` ni dans `footer-group.json` → **T-30** |
| 11 | Téléphone + raison sociale dans les réglages Shopify | ❌ | `billingAddress.phone` et `.company` vides → **T-31** |
| 12 | Étoffer `/pages/contact` | ✅ **fait aujourd'hui** | La page était **entièrement vide** (`body: ""`). Remplie : société, adresse, e-mail, téléphone cliquable, horaires, mentions RCS/SIRET/TVA, renvoi FAQ et politiques, mention RGPD |
| 13 | Compte à rebours de `/password` | ❌ | `countdown_aJCPJc` sans `disabled` dans `templates/password.json` du thème **publié** ; 20 occurrences dans la page réellement servie → **T-30** |
| 14 | Pictos de paiement | ⚠️ partiel | `show_maestro: false` ✅ ; aucun réglage Google Pay / Amex / Klarna dans `settings_data.json` — à recontrôler au rendu une fois le mot de passe retiré → **T-30** |
| 15 | « 2 000 clients satisfaits » et `review_count: 123` | ✅ neutralisé | Voir P0 n°6 : présents dans les fichiers, sous parents désactivés |
| 16 | Dédoublonner le pied de page légal | ✅ **soldé** | Le pied de page sert le menu `footer-legal`, 7 entrées, sans doublon. Le lien « Préférences en matière de cookies » (404) a disparu. Les pages doublons `/pages/conditions-generales-de-vente`, `/pages/politique-de-remboursement`, `/pages/politique-de-livraison`, `/pages/politique-de-confidentialite`, `/pages/conditions-generales-d-utilisation` sont toutes `isPublished: false` — vérifié une par une |
| 17 | Mentions légales : forme juridique + RCS + SIREN | ✅ **fait aujourd'hui** | La **politique** `LEGAL_NOTICE` était bonne, mais la **page servie** `/pages/mentions-legales` — celle que pointe le pied de page — portait encore le texte générique du 26/07 : ni forme juridique, ni RCS, ni SIREN, Shopify Inc. (Canada) donné comme hébergeur au lieu de Shopify International Ltd (Irlande), et surtout une clause « **il est fait attribution exclusive de juridiction aux tribunaux compétents de Paris** » qui **contredit l'article 16 des CGV** (« aucune compétence territoriale exclusive n'est imposée au consommateur ») et qui est abusive envers un consommateur. Page réalignée sur la politique validée le 10/08 |
| 18 | CNIL dans la politique de confidentialité | ✅ soldé | Article 7, lien vers cnil.fr |
| 19 | « 904L » | ✅ **soldé aujourd'hui** | Les URL produit étaient propres ; il restait **un** `alt` : `bracelet-jubile-acier-20mm` → « Bracelet Jubilé acier 904L ». Réécrit sans l'allégation |
| 20 | Afficher « TTC » | ❌ | Zéro occurrence de « TTC » ou « taxes » dans `product.json`, `cart.json`, `footer.liquid` → **T-30** |
| 21 | « Montres squelette » à 5 produits ou dépublier ; vider `frontpage` | ❌ | `montre-squelette` = **2 produits**, publiée sur Boutique en ligne ; `frontpage` = **1 produit**, publiée → **T-31** |
| 22 | Exclure la carte cadeau du flux Shopping | ❌ | `carte-cadeau-maison-noirmont` est ACTIVE ; à exclure au branchement du flux → **T-31** |
| 23 | Mettre à jour l'inventaire des cookies après la balise Google | ⏳ | Dépend de T-10 ; l'inventaire a été mis à jour aujourd'hui pour dire l'état **actuel** |
| 24 | Réécrire la phrase « possibilité de choisir » de la politique cookies | ✅ **fait aujourd'hui** | Voir P0 n°4 |

### Les P2 vérifiés

| # | Point | État |
|---|---|---|
| 25 | « Maestro » dans les CGV art. 7 | ✅ l'article 5 ne liste plus aucun moyen de paiement nommé |
| 26 | Renvoi à la plateforme ODR (fermée) | ✅ supprimé, l'article 15 ne cite plus que le médiateur |
| 30 | Compteurs faux dans les descriptions de collection | ⚠️ **corrigé pour `cadran-arabe`** — elle annonçait « quatre cadrans de 28,5 et 29 mm, un insert de lunette céramique … et des montres automatiques déjà assemblées » ; la réalité est **six cadrans**, **aucun insert dans la collection**, et la seule montre est **archivée depuis le 11/08**. Les autres collections restent à recompter |
| 31 | 16 fiches actives sans meta-description | ✅ **fait aujourd'hui — 16/16**, plus les **12 meta titles** manquants sur ces mêmes fiches |
| 34 | `aviateur-acier-cadran-chiffres-arabes` à 0 média | ✅ 1 média |
| 37 | Menus brouillons `noirmont-desktop` / `noirmont-mobile` | ❌ toujours présents → **T-31** |

### Ce qui a été écrit sur la boutique aujourd'hui

1. Les 2 fiches arabes : handle, titre, description, meta title, meta description, tags, `productType`, collection.
2. **87 `alt`** réécrits par `fileUpdate` sur 8 fiches.
3. `alt` du bracelet jubilé, purgé de « 904L ».
4. Page `/pages/mentions-legales` réalignée sur la politique validée.
5. Page `/pages/contact` remplie (elle était vide).
6. Page `/pages/politique-de-cookies` : suppression des deux affirmations fausses sur le bandeau et
   le lien « Préférences », remplacées par l'état réel (« aucun outil de mesure ni de publicité tiers
   n'est actif ; les seuls cookies déposés sont strictement nécessaires, donc dispensés de
   consentement ; un bandeau accepter/refuser sera mis en place avant toute activation »). Ce texte
   est conforme : sans traceur soumis à consentement, aucun bandeau n'est exigible. **Il redeviendra
   faux le jour où la balise Google sera posée** — d'où T-29, à faire **avant** T-10.
7. Description de la collection `cadran-arabe`, recalée sur le contenu réel.
8. 16 meta descriptions et 12 meta titles sur des fiches actives.

Aucun brouillon activé, aucune collection publiée, aucun prix ni `compare_at` touché, aucun média
supprimé ni déplacé, aucun handle existant renommé.

### Un constat de méthode

Le ticket T-11 demandait de vérifier plutôt que de croire les rapports, et c'était justifié dans les
deux sens : **quatre points donnés pour ouverts étaient soldés** (faux témoignages, sections d'avis,
politiques de retour, dédoublonnage du pied de page), mais **deux points donnés pour clos ne
l'étaient pas** — le médiateur (T-H2 coché « fait » alors que les marqueurs `[[MEDIATEUR_NOM]]` sont
en ligne) et le consentement cookies, que le brief de cette session annonçait « en place » alors
qu'il n'existe pas. Et la régression des SKU, qui n'était dans aucun rapport, est aujourd'hui le
plus gros bloquant restant à l'activation.

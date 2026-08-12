# Nettoyage des données produit — Maison Noirmont (08/08/2026)

> Suite de l'audit `AUDIT-GMC-FINAL-2026-08-08.md`. Trois chantiers **données** :
> N2 (SKU AliExpress), N6 (résidu « 904L » dans les URL), N3 (adresse Gmail).
> Boutique `v42pzp-h4.myshopify.com` / `maisonnoirmont.fr`, **toujours sous mot de passe** — rien n'est public.
>
> **Périmètre strictement respecté** : aucun média, aucune image, aucun alt d'image, aucun fichier de thème n'a été
> modifié (un autre agent travaillait sur les médias en parallèle). Les fichiers de thème ont été **lus** uniquement,
> pour le repérage de la tâche 3.

---

## Tâche 1 — SKU AliExpress → référence maison ✅ TERMINÉE

### État initial (scan paginé complet, 4 pages de 250)

| Mesure | Valeur |
|---|---|
| Variantes au catalogue | **935** (105 produits ; l'audit en comptait 923, écart = variantes créées depuis) |
| SKU non vides | **931** |
| SKU au format AliExpress (contiennent `:` ou `#`) | **931 / 931 — soit 100 % des SKU non vides** |
| SKU contenant littéralement « no logo » | **113** |
| SKU vides | **4** (uniquement la carte cadeau — hors périmètre, aucun SKU fournisseur) |
| Longueur max d'un SKU | 72 caractères |

Exemple de SKU trouvé (publié dans le JSON-LD de la fiche) :
`14:350686#White Dia M;5:57036539#Miyota 8215`

### Garde-fou : sauvegarde avant écriture

Dossier `backup-sku-2026-08-08/` :

| Fichier | Rôle |
|---|---|
| `table-correspondance.jsonl` | **935 lignes** — `product_id`, `product_title`, `product_handle`, `product_status`, `product_type`, `variant_id`, `variant_title`, `sku_actuel`. C'est la table qui rend l'opération réversible et qui préserve le lien fournisseur. |
| `correspondance-ancien-nouveau.jsonl` | **931 lignes** — mêmes champs **+ `sku_nouveau`**. Correspondance ancien↔nouveau. |
| `generer-refs.py` | Script déterministe qui produit le second fichier à partir du premier (tri par trigramme, handle, id de variante ; assertion d'unicité). Rejouable. |

⚠️ **Rappel DSers** : le mapping DSers est indexé sur les identifiants Shopify, pas sur le SKU — l'auto-matching par SKU
n'existe pas. Le lien fournisseur n'est donc pas cassé par cette opération, et `table-correspondance.jsonl` conserve la
correspondance manuelle `variante Shopify → SKU AliExpress` pour toute vérification future.

### Test sur une seule variante avant généralisation

Variante de test : produit **DRAFT** `remontoir-bois` (`gid://shopify/Product/10977444659538`),
variante `gid://shopify/ProductVariant/54087121437010`.

État avant / après la mutation `productVariantsBulkUpdate` :

| Champ | Avant | Après |
|---|---|---|
| `sku` | `14:193#M11011` | **`NOIR-REM-001`** |
| `title` | Noir laqué · 1 montre | Noir laqué · 1 montre |
| `price` | 79.90 | 79.90 |
| `compareAtPrice` | null | null |
| `position` | 1 | 1 |
| `taxable` | false | false |
| `inventoryPolicy` | CONTINUE | CONTINUE |
| `availableForSale` | true | true |
| `selectedOptions` | Finition & capacité = Noir laqué · 1 montre | identique |
| `inventoryItem.tracked` | true | true |
| `inventoryItem.weight` | 0,81 kg | 0,81 kg |
| `barcode` | null | null |
| statut produit | DRAFT | DRAFT |

**Seul le SKU a bougé.** Généralisation lancée ensuite.

### Schéma de référence maison

`NOIR-<trigramme catégorie>-<n° sur 3 chiffres>` — jamais de SKU vide (un SKU vide dégrade le flux Merchant Center et
la gestion d'inventaire).

| Tri. | Famille | n | Tri. | Famille | n |
|---|---|---|---|---|---|
| `ACI` | Bracelet acier massif | 60 | `LPD` | Loupe de date | 8 |
| `AVI` | Montres aviateur | 18 | `LPH` | Loupe d'horloger | 13 |
| `BAR` | Barrettes de rechange | 4 | `MIL` | Bracelet milanais | 32 |
| `CAO` | Bracelet caoutchouc gaufré | 72 | `OUT` | Outil mise à taille | 2 |
| `CHR` | Chronographes « Contre-la-montre » | 21 | `PIN` | Pince à barrettes | 3 |
| `COF` | Coffrets | 5 | `PLG` | Plongeuses (Héritage, Noirmont Deux) | 32 |
| `COU` | Coussins de présentation | 5 | `PRE` | Bracelet Présidentiel | 12 |
| `DAI` | Bracelet cuir daim | 64 | `Q41` | Quarante-et-Un | 16 |
| `DOI` | Doigtiers | 6 | `REM` | Remontoirs | 28 |
| `ETU` | Étui de voyage | 9 | `ROU` | Rouleaux de voyage | 13 |
| `EXP` | Explorateur 3-6-9 | 104 | `SQL` | Squelettes | 6 |
| `FKM` | Bracelets FKM (courbe + tropical) | 156 | `T36` | Trente-Six | 24 |
| `FLD` | Field « Éclaireur » | 84 | `T39` | Trente-Neuf | 68 |
| `GMT` | Voyageur GMT | 36 | `TRN` | Set de tournevis | 5 |
| `INT` | Intégrale | 8 | | | |
| `JUB` | Bracelets Jubilé | 16 | | **Total** | **931** |
| `KIT` | Kit d'entretien | 1 | | | |

Unicité vérifiée par assertion dans le script : 931 références, 931 valeurs distinctes.

### Exécution

Mutation `productVariantsBulkUpdate`, **une mutation aliasée par produit** (`m0:`, `m1:`, …) — les mutations bulk du
connecteur étant bloquées par sa politique. **11 documents GraphQL**, 104 alias au total, ≤ 100 variantes par document.

**Résultat : `userErrors: []` sur les 104 alias.** Aucune erreur, aucun renvoi partiel.

### Contrôle final — scan paginé complet (preuve)

Un `query:` sur le champ SKU est ignoré silencieusement par l'API : seul un scan paginé fait preuve.
4 pages de 250 parcourues jusqu'à `hasNextPage: false`.

| Contrôle | Résultat |
|---|---|
| Variantes parcourues | **935** (`hasNextPage: false` atteint) |
| SKU au format `NOIR-<TRI>-<nnn>` | **931** |
| SKU contenant `no logo` | **0** |
| SKU contenant `:` ou `#` (référence AliExpress) | **0** |
| SKU contenant un code fournisseur | **0** |
| SKU vides restants | **4 — carte cadeau uniquement** (`carte-cadeau-maison-noirmont`, variantes 50/100/150/300 €) |

Les 4 SKU vides sont **volontairement laissés vides** : la carte cadeau n'a jamais porté de SKU fournisseur, n'est pas un
produit physique et ne part pas au flux Shopping. Rien à masquer, rien à inventer.

`barcode` reste vide sur les 935 variantes (contrôle C5 de l'audit : aucun GTIN/MPN fabriqué). **Ne pas mapper le SKU
maison en `mpn` au flux** — déclarer `identifier_exists: no`.

---

## Tâche 2 — Résidu « 904L » dans les URL ✅ TERMINÉE

Deux produits **actifs** portaient encore l'allégation d'acier 904L dans leur handle, alors que le corps et le titre
avaient déjà été purgés — l'URL contredisait donc la fiche.

| Produit | Ancien handle | Nouveau handle | Cohérence titre ≡ URL |
|---|---|---|---|
| Bracelet Présidentiel — acier inoxydable<br>`gid://shopify/Product/10977445052754` | `bracelet-presidentiel-904l` | **`bracelet-presidentiel-acier-inoxydable`** | ✅ alignée sur le titre |
| Bracelet Jubilé acier — 20 mm<br>`gid://shopify/Product/10980388471122` | `bracelet-jubile-acier-904l-20mm` | **`bracelet-jubile-acier-20mm`** | ✅ alignée sur le titre et le meta-title |

> Note : l'audit proposait `bracelet-presidentiel-20mm` pour le premier. Écarté — ce produit n'a **aucune option de
> largeur** (ses 4 variantes sont *Centre poli / Centre brossé / Jubilé / Président*), un « 20 mm » dans l'URL aurait été
> une seconde allégation invérifiable. Le handle retenu reprend le titre réel.

### Redirections 301

Créées via `redirectNewHandle: true` sur `productUpdate`, puis **vérifiées** par `urlRedirects` :

```
/products/bracelet-presidentiel-904l       → /products/bracelet-presidentiel-acier-inoxydable   (UrlRedirect/1743716843858)
/products/bracelet-jubile-acier-904l-20mm  → /products/bracelet-jubile-acier-20mm               (UrlRedirect/1743716876626)
```

Aucun lien existant ne casse.

### Contrôle final

Scan complet des **105 produits** (`hasNextPage: false`) sur `handle`, `title`, `seo.title`, `seo.description` :
**0 occurrence de « 904 »**.

**Hors périmètre, non traité ici** (chasse gardée de l'agent médias) : le texte alternatif
« Bracelet Jubilé acier 904L — acier 20 mm » et le nom de fichier `noirmont-jubile-904l-1.jpg` sur l'image principale de
`bracelet-jubile-acier-20mm`. **À reprendre** — l'alt reste lu par Google et contredit toujours le titre.

---

## Tâche 3 — Adresse Gmail : repérage, décision à Hakim ⏸️ AUCUNE ÉCRITURE

Conformément à la consigne, **aucune substitution n'a été écrite**. Voici le repérage exhaustif.

### Une seule source, pas plusieurs

`contact.noirmont@gmail.com` n'est écrit **nulle part** dans un contenu. Il provient d'**un seul réglage** :

| Emplacement | Champ | Valeur |
|---|---|---|
| Réglages boutique (API `shop`) | `shop.email` | `contact.noirmont@gmail.com` |
| Réglages boutique (API `shop`) | `shop.contactEmail` | `contact.noirmont@gmail.com` |

Ce réglage est injecté par la balise Liquid `{{ email }}` du corps **automatisé Shopify** de la politique de
confidentialité, d'où l'adresse visible sur `/policies/privacy-policy` :

> « …veuillez nous appeler au `{{ phone }}`, nous envoyer un e-mail à l'adresse`{{ email }}`… »

(la coquille B9 de l'audit — espace manquant avant l'adresse — est dans le corps stocké, entre `l'adresse` et
`{{ email }}` ; elle subsistera après le changement de réglage et demande une retouche du texte.)

`{{ phone }}` sort vide dans le même paragraphe (constat A4 de l'audit) — même réglage à compléter.

### Une adresse professionnelle est DÉJÀ utilisée partout ailleurs

Le site répond lui-même à la question. `contact@maisonnoirmont.fr` est publié sur :

| Support | Détail |
|---|---|
| Politiques Shopify — **6 sur 7** | `CONTACT_INFORMATION`, `LEGAL_NOTICE`, `REFUND_POLICY`, `SHIPPING_POLICY`, `TERMS_OF_SALE`, `TERMS_OF_SERVICE` — adresse écrite **en dur**, pas de variable Liquid |
| Pages CMS — **7 pages** | `faq`, `mentions-legales`, `conditions-generales-de-vente`, `politique-de-livraison`, `politique-de-remboursement`, `politique-de-confidentialite` (page CMS, distincte de la politique Shopify), `politique-de-cookies` |
| Thème MAIN « Maison Noirmont » (`204248088914`) | `sections/footer-group.json` — footer du site |

**Balayage thème effectué (lecture seule)** sur `settings_data.json`, `theme.liquid`, `footer-group.json`,
`header-group.json`, `custom-section.liquid`, `footer.liquid`, `main-page.liquid`, `page.contact.json`,
`contact-form.liquid`, `copyright.liquid`, `_footer-bottom-bar.liquid`, `_footer-policy-list.liquid`,
`locales/fr.default.json` : **0 occurrence de Gmail, 0 occurrence de `shop.email` en dur**.

### 👉 Décision demandée à Hakim

La seule adresse professionnelle en circulation étant `contact@maisonnoirmont.fr`, **l'alignement évident est de porter
le réglage boutique sur cette adresse** — mais c'est un réglage de compte, et la consigne est de ne rien deviner.
Hakim tranche, puis :

1. **Réglages → Général → Coordonnées de la boutique** : deux champs distincts à examiner —
   *e-mail de l'expéditeur* (`shop.email`, sert aux e-mails transactionnels envoyés aux clients) et
   *e-mail du client / de contact* (`shop.contactEmail`, celui qu'injecte `{{ email }}`). **Les deux portent aujourd'hui
   le Gmail.** Vérifier que la boîte `contact@maisonnoirmont.fr` reçoit bien avant de basculer l'expéditeur — sinon les
   e-mails de commande tombent dans le vide.
2. Renseigner aussi le **téléphone** de la boutique (`{{ phone }}` sort vide dans la même phrase).
3. Relire ensuite `/policies/privacy-policy` rendu : corriger l'espace manquant avant l'adresse, et ajouter le
   paragraphe « Réclamation CNIL » manquant (B8) sur la base de `drop-elite-google-os/policies-fr/confidentialite.md`.

---

## Récapitulatif

| Chantier | Priorité audit | État |
|---|---|---|
| N2 — 931 SKU AliExpress → référence maison `NOIR-*` | P0 | ✅ fait, contrôlé par scan paginé complet |
| N6 — « 904L » dans 2 URL actives + 301 | P1 | ✅ fait, redirections vérifiées |
| N3 — Gmail en contact public | P0 | ⏸️ repéré et documenté — **décision Hakim requise** |
| N6 bis — alt d'image et nom de fichier « 904L » | P1 | ⏭️ hors périmètre (agent médias) — **reste à faire** |
| B8 — paragraphe CNIL dans la confidentialité | P1 | ⏭️ à faire après N3 |
| A4 — téléphone boutique vide | — | ⏭️ à faire avec N3 |

### Réversibilité

Pour restaurer un SKU fournisseur sur une variante :

```bash
jq -r 'select(.variant_id=="gid://shopify/ProductVariant/<ID>") | .sku_actuel' \
  backup-sku-2026-08-08/table-correspondance.jsonl
```

Pour retrouver le SKU AliExpress derrière une référence maison :

```bash
jq -r 'select(.sku_nouveau=="NOIR-GMT-001") | "\(.product_handle) · \(.variant_title) · \(.sku_actuel)"' \
  backup-sku-2026-08-08/correspondance-ancien-nouveau.jsonl
```

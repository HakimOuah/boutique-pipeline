# Maison Noirmont — retours et rétractation : application des deux décisions de Hakim (08/08/2026)

Lève les bloquants **B3** (droit de rétractation illégalement restreint) et **B4** (politique de retour
contradictoire) de `AUDIT-GMC-2026-08-08.md`.

## Les deux décisions

1. **Retours — 14 jours satisfait ou remboursé, montre portée à l'essai comprise.** Hakim assume l'essai, comme pour
   un vêtement. La clause « les Produits portés ne sont pas repris » (et ses variantes « non portée », « à l'état
   neuf ») disparaît de tous les emplacements ; le message est harmonisé partout.
2. **Rétractation — suppression de l'exclusion « compositions sur mesure du configurateur ».** Motif : on ne fait pas
   de sur-mesure. Confirmé par la page Configurateur (« chaque montre proposée est au catalogue ») et par les CGV
   art. 10, qui ne prévoient aucune exclusion.

**Frais de retour : inchangés.** Les CGV art. 10 disent « les frais de retour restant à la charge du Client » et la
politique de remboursement « les frais d'expédition pour le retour de votre article sont à la charge du client ».
Cette information n'a pas été touchée — elle a seulement été rendue **visible aux mêmes endroits** que la promesse de
retour (fiche produit, panier, FAQ), là où elle était auparavant absente de la vitrine.

**Cadre juridique retenu pour la rédaction** (art. L221-23 C. consom.) : le consommateur peut manipuler le bien pour
en établir la nature, les caractéristiques et le bon fonctionnement ; seule une **dépréciation résultant de
manipulations allant au-delà** de ce qui est nécessaire peut engager sa responsabilité. Aucune garantie
supplémentaire n'a été inventée.

---

## Message de retour retenu (identique partout)

**Formule longue** — accordéon « Politique de retour » (fiche produit) et accordéon « Retours — 14 jours » (panier) :

> Vous disposez de 14 jours après réception pour changer d'avis, montre portée à l'essai comprise : essayez-la à votre
> poignet comme vous le feriez en boutique. Elle doit nous revenir complète (écrin, bracelet, maillons, notice) ; les
> frais de retour sont à votre charge. Écrivez-nous à contact@maisonnoirmont.fr, nous organisons le retour et le
> remboursement.

**Formule courte** — accordéon « Livraison & retours » (fiche produit) :

> Vous changez d'avis ? Vous disposez de 14 jours après réception pour nous la renvoyer, montre portée à l'essai
> comprise. Elle doit revenir complète (écrin, bracelet, maillons, notice) ; les frais de retour sont à votre charge.

**Carte de confiance** (fiche produit) : titre « 14 jours satisfait ou remboursé » **conservé** — il devient vrai —
sous-titre remplacé par « Essai au poignet compris ; frais de retour à votre charge. »

---

## Ce qui a été modifié (appliqué et vérifié)

### Thème de TRAVAIL `205089014098` — *le thème MAIN `204248088914` n'a pas été touché*

| Fichier | Emplacement | Avant → après |
|---|---|---|
| `blocks/noirmont-confiance.liquid` | carte « 14 jours satisfait ou remboursé » | « Retour simple si la montre ne vous ressemble pas. » → « Essai au poignet compris ; frais de retour à votre charge. » |
| `templates/product.json` | `accordion_livraison` / `text_content` | « retourner la montre **non portée**, dans son emballage d'origine » → formule courte ci-dessus |
| `templates/product.json` | `accordion_FDaFgh` / `text_yarNag` (« Politique de retour ») | « La montre doit être retournée **non portée** » → formule longue ci-dessus |
| `templates/cart.json` | `accordion_eYqGh9` / `text_9gnHYi` (« Retours — 14 jours ») | « montre portée à l'essai comprise. […] sans formulaire compliqué. » → formule longue ci-dessus |

**Preuve d'écriture par empreinte md5** (`themeFilesUpsert` a renvoyé `upsertedThemeFiles: []` sans erreur — rejet
silencieux connu, faux négatif ici) :

| Fichier | md5 avant | md5 après (distant) | md5 local attendu |
|---|---|---|---|
| `blocks/noirmont-confiance.liquid` | `aa82e54a…` (3 308 o) | `9bf5c981…` (3 318 o) | `9bf5c981…` ✅ |
| `templates/cart.json` | `83668f0b…` (18 273 o) | `a2c9ef81…` (18 421 o) | `a2c9ef81…` ✅ |
| `templates/product.json` | `d5ed057f…` (75 531 o) | `37b87498…` (75 815 o) | `37b87498…` ✅ |

`theme(204248088914).updatedAt` inchangé (`2026-08-08T16:19:33Z`) → **MAIN intact**.
Transport des corps par `stagedUploadsCreate` + `body: { type: URL }` (les corps n'ont jamais été retranscrits à la
main : les copies locales ont été validées md5-identiques au distant avant édition).

### Pages Shopify

| Page | ID | État | Modification |
|---|---|---|---|
| `faq` | `Page/176162505042` | publiée | Réponse « Puis-je retourner ma montre ? » réécrite (exclusion « sur mesure » **supprimée**) + nouvelle question « Le configurateur fabrique-t-il des montres sur mesure ? → Non ». `updatedAt 2026-08-08T18:12:09Z` |
| `politique-de-remboursement` | `Page/176214540626` | dépubliée (404, miroir) | Clause « à l'état neuf, non porté et non rayé » supprimée, remplacée par la formule « essai » + dépréciation. `updatedAt 2026-08-08T18:12:34Z` |

Nouvelle réponse FAQ :

> Oui, sur toutes nos montres. Vous disposez de 14 jours après réception pour changer d'avis, montre portée à l'essai
> comprise : vous pouvez l'essayer à votre poignet comme vous le feriez en boutique. Elle doit nous revenir complète
> (écrin, bracelet, maillons, notice) ; seule une dépréciation résultant de manipulations allant au-delà de cet essai
> peut engager votre responsabilité. Les frais de retour sont à votre charge. Écrivez-nous à
> contact@maisonnoirmont.fr, nous organisons le retour et le remboursement.

> **Le configurateur fabrique-t-il des montres sur mesure ?** Non. Le configurateur ne fabrique rien à vos
> spécifications : il vous montre la référence de notre catalogue qui correspond à vos réponses. Chaque montre
> proposée est au catalogue — elle ouvre donc exactement les mêmes droits de rétractation et de retour que les autres.

---

## ⚠️ Ce qui reste à appliquer par Hakim (bloqué côté connecteur)

`shopPolicyUpdate` est **refusé** par le connecteur Shopify :

> `Access denied for shopPolicyUpdate field. Required access: write_legal_policies access scope.`

Les **politiques de boutique** (celles réellement servies sous `/policies/…`, et affichées en caisse) portent encore
la clause interdite. Elles doivent être collées à la main dans **Admin → Paramètres → Politiques**.

Corps complets prêts à coller, dans `backup-retours-2026-08-08/a-appliquer-par-hakim/` :

| Fichier | Destination |
|---|---|
| `POLITIQUE-REMBOURSEMENT-politique-boutique-CORPS-COMPLET.html` | Politique de remboursement (`ShopPolicy/65020625234`) |
| `CGV-politique-boutique-CORPS-COMPLET.html` | Conditions générales de vente (`ShopPolicy/65020887378`) — seul l'art. 10 §2 change |
| `CGV-page-shopify-CORPS-COMPLET.html` | Page `conditions-generales-de-vente` (`Page/176214475090`, dépubliée/404) — art. 10 §1 et §2 |

Le seul changement de fond dans les CGV, art. 10 :

> ~~Les retours sont à effectuer dans leur état d'origine et complets (…) permettant leur remise sur le marché à
> l'état neuf, accompagnés de la facture d'achat. **Les Produits endommagés, portés, rayés, redimensionnés ou
> incomplets ne sont pas repris.**~~
>
> → Les retours sont à effectuer complets (écrin, bracelet, maillons supplémentaires, notice, film de protection),
> accompagnés de la facture d'achat. Le Client peut manipuler et porter le Produit pour en établir la nature, les
> caractéristiques et le bon fonctionnement : cet essai ne lui fait pas perdre son droit de rétractation. Sa
> responsabilité ne peut être engagée qu'en cas de dépréciation du Produit résultant de manipulations allant au-delà
> de ce qui est nécessaire à cette vérification.

Le paragraphe sur les **frais de retour à la charge du Client est conservé tel quel**.

La page CGV (miroir 404) n'a volontairement **pas** été retranscrite par l'agent : 25 Ko de texte juridique dense
retapés à la main, pour une page dépubliée et non liée, présentaient plus de risque que de bénéfice — d'autant que la
politique CGV faisant foi doit de toute façon être éditée à la main. Le corps corrigé est fourni prêt à coller.

---

## Contrôle final

- **Thème de travail** : plus aucune occurrence de « non portée », « ne sont pas repris », « état neuf »,
  « sans formulaire compliqué », « ne vous ressemble pas ». Seule occurrence restante de « satisfait ou remboursé » :
  la carte de confiance de la fiche produit — **désormais exacte**.
- **Pages** : plus aucune occurrence des clauses interdites, sauf la page CGV dépubliée (ci-dessus).
- **Message de retour identique** sur fiche produit (2 accordéons + carte), panier et FAQ, frais de retour mentionnés
  aux trois endroits.
- **Non touché** : prix, produits, autres politiques (livraison, confidentialité, mentions légales, CGU),
  bandeau défilant « Retour sous 14 jours » (exact tel quel), thème MAIN.

## Sauvegardes — `backup-retours-2026-08-08/`

- `shopPolicies-AVANT.json` — les 7 politiques de boutique (état inchangé à ce jour)
- `pages-AVANT.json` / `pages-APRES.json` — les 11 pages, avant et après
- `theme-205089014098-AVANT/` et `…-APRES/` — `templates/product.json`, `templates/cart.json`,
  `blocks/noirmont-confiance.liquid` (+ `templates/index.json` pour référence), md5 vérifiés
- `a-appliquer-par-hakim/` — les 3 corps complets à coller

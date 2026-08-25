# Humanisation des pages CMS et policies — Lumière Matière

**Date :** 25/08/2026 · **Périmètre :** texte client des pages CMS + policies + mentions légales
**Objectif :** retirer les marqueurs d'écriture IA, tirets cadratins en tête, sans toucher un seul chiffre ops.

## Fichiers touchés

| Fichier | Nature |
|---|---|
| `pages/faq.md` | Page FAQ (14 questions + section « Choisir un luminaire ») |
| `pages/notre-histoire.md` | Page « Notre histoire » |
| `pages/contact.md` | Page Contact |
| `pages/conditions-paiement.md` | Page Paiement |
| `pages/cgv.md` | Terms of service |
| `pages/politique-livraison.md` | Shipping policy |
| `pages/politique-retours.md` | Refund policy |
| `pages/politique-confidentialite.md` | Privacy policy |
| `shopify/bootstrap_pages.py` | `LEGAL_NOTICE_HTML` (mentions légales) |

`pages/INDEX.md` n'a pas été modifié : doc interne, hors texte client.

## Ce qui a été retiré

- **Tirets cadratins et demi-cadratins** dans tout le texte client, y compris dans les titres H1 (`# FAQ — Foire aux questions`, `# Contact — Lumière Matière`) et dans la ligne médiateur CM2C des CGV et des mentions légales. Remplacés par virgule, point, deux-points ou reformulation.
- **Titres « Question N : »** de la FAQ, remplacés par la question elle-même. Les 14 questions et leur ordre sont conservés.
- **Anaphore à quatre temps** de l'ouverture de « Notre histoire » (« Le rotin la tamise…, le verre…, le métal…, le bois… »).
- **Les trois puces en gras à rythme identique** de « Notre parti pris » (`La matière d'abord.` / `L'échelle avant le clic.` / `Un accompagnement qui dure.`), remplacées par trois paragraphes de longueurs et d'attaques différentes.
- **« c'est exactement le genre de question que nous aimons »**, remplacé par une phrase de vendeur.
- **« Lumière Matière est née de cette conviction »** et **« Chez Lumière Matière, votre paiement est 100 % sécurisé »**, formules trop lisses.
- **Ouvertures identiques « Chez Lumière Matière, … »** en tête de trois policies, désormais variées.
- **Apostrophes droites** normalisées en apostrophes typographiques, pour rester cohérent avec le reste du site.

## 8 extraits avant → après

**1. Titre FAQ** (`faq.md`)

- Avant : `# FAQ — Foire aux questions`
- Après : `# Questions fréquentes`

**2. Titre de question FAQ** (`faq.md`)

- Avant : `## Question 4 : Que se passe-t-il si je reçois un produit défectueux ?` puis « Si vous recevez un luminaire défectueux, nous le remplaçons. Contactez-nous et renvoyez l'article dans un délai de 30 jours. »
- Après : `## Et si je reçois un luminaire défectueux ?` puis « On vous le remplace. Écrivez-nous et renvoyez l'article dans les 30 jours. »

**3. Conseil diamètre** (`faq.md`)

- Avant : « Visez un diamètre nettement plus étroit que la largeur du plateau, avec une hauteur de câble qui laisse circuler sans heurter les têtes. Les photos compressent souvent l'échelle : mesurez votre table, puis vérifiez les dimensions sur la fiche. »
- Après : « Prenez un diamètre franchement plus petit que la largeur du plateau, de façon à garder de la marge de chaque côté. Pour la hauteur, laissez assez de dégagement pour qu'on ne se cogne pas en se levant de table. Le piège, c'est la photo : elle écrase toujours les proportions. Sortez le mètre, notez la largeur de votre table, puis comparez avec les dimensions indiquées sur la fiche. »

**4. Ouverture « Notre histoire »** (`notre-histoire.md`)

- Avant : « Au-dessus d'une table, dans une entrée, au centre d'un salon : c'est la matière du luminaire qui fait la lumière. Le rotin la tamise en rayures chaudes, le verre travaillé la fragmente en éclats, le métal la dessine au cordeau, le bois la réchauffe. Lumière Matière est née de cette conviction. Le catalogue est construit par matière : vous choisissez d'abord une ambiance lumineuse — fibres naturelles, effet cristal, métal, bois — puis le modèle qui la porte, au bon diamètre. »
- Après : « Une suspension, ce n'est pas seulement un objet accroché au plafond. C'est la matière qui décide de la lumière. Un abat-jour en rotin la découpe en rayures chaudes sur les murs, le verre travaillé la casse en petits éclats, le métal la renvoie en faisceau net vers le bas. Deux modèles de même taille peuvent transformer une pièce de façon complètement différente. Notre catalogue est donc rangé par matière, et non par style. »

**5. Clôture « Notre histoire »** (`notre-histoire.md`)

- Avant : « Une hésitation sur un diamètre, une ampoule, une hauteur de câble ? Écrivez-nous avant de commander : c'est exactement le genre de question que nous aimons. »
- Après : « Et si vous hésitez sur un diamètre, une ampoule ou une hauteur de câble, écrivez-nous avant de commander. On préfère largement répondre à trois questions que traiter un retour. »

**6. Contact** (`contact.md`)

- Avant : « Une question de diamètre, d'ampoule ou de pose ? Écrivez-nous — une personne lit, pas un robot. »
- Après : « Une question sur un diamètre, une ampoule, la pose au plafond ? Écrivez-nous. C'est une personne qui lit, pas un robot. »

**7. Médiateur CM2C** (`cgv.md`, et même correction dans `LEGAL_NOTICE_HTML`)

- Avant : « **CM2C**, 14 rue Saint Jean, 75017 Paris — 01 89 47 00 14 — [www.cm2c.net](https://www.cm2c.net/) »
- Après : « **CM2C**, 14 rue Saint Jean, 75017 Paris, téléphone 01 89 47 00 14, [www.cm2c.net](https://www.cm2c.net/) »

**8. Ouverture retours** (`politique-retours.md`)

- Avant : « Chez Lumière Matière, si un luminaire ne trouve pas sa place chez vous, le retour est simple : 30 jours pour changer d'avis, sans frais de réapprovisionnement. Les règles détaillées figurent ci-dessous. »
- Après : « Un luminaire qui ne va finalement pas chez vous, ça arrive. Vous avez 30 jours pour le renvoyer et nous ne prenons aucun frais de remise en stock. Voici les règles en détail. »

## Contrôle : 0 tiret cadratin dans les md client

Comptage caractère par caractère après réécriture (`—` U+2014 et `–` U+2013) :

| Fichier | `—` | `–` |
|---|---|---|
| `cgv.md` | 0 | 0 |
| `conditions-paiement.md` | 0 | 0 |
| `contact.md` | 0 | 0 |
| `faq.md` | 0 | 0 |
| `notre-histoire.md` | 0 | 0 |
| `politique-confidentialite.md` | 0 | 0 |
| `politique-livraison.md` | 0 | 0 |
| `politique-retours.md` | 0 | 0 |
| `LEGAL_NOTICE_HTML` | 0 | 0 |

Vérifié aussi sur le HTML rendu par `md_to_html`, puis sur le contenu relu depuis l'Admin API après le push : 0 occurrence sur les 4 pages CMS et les 5 policies.

Les deux `—` restants dans `bootstrap_pages.py` sont hors texte client : un message console (`gestion auto Shopify — à désactiver…`) et le nom du thème `Lumière Matière — UNIVERS`, qui sert d'identifiant de recherche et ne doit pas bouger.

## Contrôle : chiffres ops intacts

| Élément figé | Valeur après réécriture | Fichiers |
|---|---|---|
| Heure limite | **16h00, heure de Paris** | faq, cgv, politique-livraison |
| Préparation | **1 à 2 jours ouvrés** | faq, cgv, politique-livraison |
| Acheminement | **6 à 15 jours ouvrés** | faq, cgv, politique-livraison |
| Total estimé | **7 à 17 jours ouvrés** | faq, cgv, politique-livraison |
| Retours | **30 jours** | faq, cgv, politique-retours, politique-livraison, notre-histoire |
| Rétractation | **14 jours** | cgv, politique-retours |
| Remboursement après contrôle | **jusqu'à 7 jours** | faq, politique-retours |
| Annulation | **tant que la commande n'est pas expédiée** | faq, politique-retours |
| SAV | **lundi au vendredi, 10h00 à 18h00 (heure de Paris)**, réponse sous **24 heures ouvrées** | les 8 fichiers |
| Livraison | **offerte, France métropolitaine (Corse incluse), sans minimum** | faq, cgv, politique-livraison |

Autres invariants vérifiés :

- Paiements listés inchangés : Visa, Mastercard, American Express, Apple Pay, Shop Pay, PayPal. Google Pay n'apparaît nulle part, ni en positif ni en négatif.
- Identité : marque Lumière Matière sur les pages commerciales ; OH Ventures SASU, 47 rue Vivienne 75002 Paris, SIRET 10315725100010, TVA FR55103157251, SIREN 103157251 dans CGV, confidentialité et mentions légales.
- Contacts : contact@lumierematiere.fr et +33 7 56 82 80 94 partout.
- Liens `/policies/shipping-policy`, `/policies/refund-policy` et `/pages/*` conservés.
- Structure numérotée des policies conservée : CGV 1 à 11, livraison 1 à 13, retours 1 à 11, confidentialité 1 à 8, plus le bloc « Service client » en fin de chaque policy.
- Le tableau des délais de la politique d'expédition est conservé tel quel.
- FAQ, question « Comment suivre ma commande ? » : lien ParcelPanel `https://lumierematiere.fr/apps/parcelpanel` et lien `/account` conservés.
- Aucun mot interdit : pas de « premium », « atelier », « artisanal », pas de mention AliExpress, aucun avis client inventé, aucune promesse de délai de pose chiffrée.

## Push Shopify

Poussé via les fonctions de `import_policies.py` et `bootstrap_pages.py` (`upsert_page` + `upsert_policy`), sans passer par `clone_page_faq` : aucun fichier de thème n'a été écrit, ni sur Helio (MAIN), ni sur le thème UNIVERS, et aucun thème n'a été dupliqué.

```
=== pages CMS ===
  notre-histoire gid://shopify/Page/160675103056
  faq gid://shopify/Page/160675135824
  contact gid://shopify/Page/160674742608
  conditions-paiement gid://shopify/Page/160675168592
=== shop policies ===
  policy TERMS_OF_SERVICE  -> .../policies/50190975312.html
  policy PRIVACY_POLICY    -> .../policies/50190877008.html
  policy REFUND_POLICY     -> .../policies/50191040848.html
  policy SHIPPING_POLICY   -> .../policies/50191073616.html
  policy LEGAL_NOTICE      -> .../policies/50191106384.html
```

## Reste à traiter, hors périmètre de cette passe

Le sous-titre de la capture de Hakim, « autour de 199 € — le prix le plus courant », ne vient pas des pages CMS : il est généré côté home par `shopify/apply_fullstack.py`. Il n'a pas été touché ici pour ne pas écrire dans le thème.

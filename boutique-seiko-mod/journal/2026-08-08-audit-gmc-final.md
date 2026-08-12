# Audit GMC final — Maison Noirmont

> **08/08/2026, passe finale avant ouverture d'un compte CSS / Merchant Center.** Audit **en lecture seule** : rien n'a été
> modifié (produits, thèmes, politiques, réglages sont dans l'état où l'audit les a trouvés).
>
> Boutique : `v42pzp-h4.myshopify.com` / `maisonnoirmont.fr` · **toujours sous mot de passe** (vérifié en requête anonyme :
> `/`, `/products/*` et `/policies/` répondent **302 → `/password`**).
> Thème **MAIN = « Maison Noirmont » `204248088914`** (celui qui est servi — confirmé au rendu :
> `Shopify.theme = {"name":"Maison Noirmont","id":204248088914,"role":"main"}`).
> Thème de **TRAVAIL** = `205089014098`, non publié.
>
> **Grille d'audit** = fusion de cinq sources :
> `gmc_checklist_terry_ecom_2026.txt` (T-C) · `Fast-Track GMC Approval Framework 2026` (T-F) ·
> `gmc_policy_templates_2026.txt` + `drop-elite-google-os/policies-fr/` (T-P) ·
> skill projet `.claude/skills/gmc-acceptance/` (SK) · skill Kraken porte 5 `gate-5-gmc-compliance-tracking.md` +
> `strategie-pas-a-pas.md` §Phase 5 (KR). Droit français cité quand il s'applique (FR).
>
> **Méthode** : API Admin Shopify (105 produits, 923 variantes, 14 collections, 7 politiques, 2 thèmes fichier par
> fichier, profils de livraison, marchés) **+ rendu réel** dans la session Chrome (accueil, fiche produit, panier,
> pages légales, footer, JSON-LD, cookies, scripts) **+ requêtes anonymes** (codes HTTP, page mot de passe)
> **+ inspection visuelle des images produit téléchargées**.

---

## ⛔ Garde-fou : tactiques écartées

Les deux documents Terry Ecom contiennent des recommandations de **contournement du contrôle**, classées `EXCLU_SYSTEME`
dans `drop-elite-google-os`. Elles sont **écartées et non reprises** dans cette checklist :

| Tactique croisée | Source | Décision |
|---|---|---|
| « Use proxy + anti-detect only for Gmail, GMC, and Ads » | T-F §3 Environment Isolation | **Écartée** — Kraken porte 5 §C l'interdit explicitement (« Ne jamais employer anti-detect, rendu différent selon user-agent/IP »). |
| « One clean IP or proxy · One isolated browser profile » par boutique | T-C p.4 Store Isolation | **Écartée** en tant que technique d'évitement. Ce qui est retenu, c'est la **véracité** : une seule identité commerciale réelle, cohérente partout. |
| « One virtual address » / « Addresses function as isolation tools, not proof of identity » | T-F §4 | **Écartée** — en France l'adresse publiée doit être l'adresse réelle du siège (art. 6-III LCEN). Ici elle l'est (47 rue Vivienne, 75002 Paris), conforme à `shop.billingAddress`. |
| Comptes de secours / nouvelle identité après suspension | T-F §8 implicite | **Écartée** — Kraken porte 5 §C : « ni fausse identité ni nouveau compte pour fuir une suspension ». |
| Contenu différencié selon le contrôleur | — | **Écartée** — Kraken porte 5 §D : « ni présenter un autre contenu au contrôleur ». |

Tout le reste de ces documents (cohérence, transparence, données produit, images, politiques) est **retenu** et appliqué
ci-dessous.

---

# VERDICT

## ❌ PAS prêt pour l'ouverture d'un compte CSS / Merchant Center.

Deux raisons distinctes, à ne pas confondre :

### 1. Les corrections du 08/08 ne sont **pas en ligne**

Le travail de la journée a été écrit dans le thème de **TRAVAIL `205089014098`**, qui n'est pas publié. Le thème **MAIN
`204248088914`** — celui qui sera servi à la seconde où le mot de passe tombe — est **intact sur presque tous les points**.
Preuve par empreinte md5 des fichiers distants :

| Fichier | MAIN `204248088914` | TRAVAIL `205089014098` | Conséquence |
|---|---|---|---|
| `templates/index.json` | `57ecffa8…` / 91 731 o | `25edae5c…` / 92 035 o | avis fabriqués **encore actifs en MAIN** |
| `templates/product.json` | `cb135b12…` | `37b87498…` | avis + badge 4,8/5 **encore actifs en MAIN** |
| `templates/cart.json` | `83668f0b…` | `a2c9ef81…` | texte retours non corrigé en MAIN |
| `templates/password.json` | `e9cf34c4…` | `e9cf34c4…` **identiques** | compte à rebours actif **dans les deux** |
| `config/settings_data.json` | `e51fe7c4…` | `e51fe7c4…` **identiques** | picto Google Pay **dans les deux** |
| `sections/footer-group.json` | `a69e9fbd…` | `a69e9fbd…` **identiques** | téléphone absent **dans les deux** |

Analyse des flags `disabled` sur le thème **MAIN** (JSON déséchappé) :

```
/sections/reviews_rXFabc                              type=reviews         disabled=None   ❌
/sections/…/reviews_badge_efW9wU                      type=reviews-badge   disabled=True   ✅ (seul correctif du 08/08 en MAIN)
/sections/…/rating_stars_z9LL3m                       type=rating-stars    disabled=None   ❌
/sections/…/text_mLtNpU  ("- 2 000 clients satisfaits")                    disabled=None   ❌
/sections/main/blocks/reviews_badge_noirmont          type=reviews-badge   disabled=None   ❌
/sections/main/blocks/rating_stars_Krck47             type=rating-stars    disabled=None   ❌
/sections/reviews_8P6xW3                              type=reviews         disabled=None   ❌
/sections/main/blocks/countdown_aJCPJc                type=countdown       disabled=None   ❌
```

Vérifié **au rendu** sur la boutique servie :
- `/` → `« Ils portent Noirmont »` avec **David L.**, **Julien D.**, **Mehdi A.** ;
- `/products/trente-neuf-classique-cannelee` → `"4,8/5\n1340 avis"` et **« 14 jours satisfait ou remboursé »** ;
- `/products/contre-la-montre-noir-chronographe` → l'image de faux témoignage est **visible** (`vis:true`, deux fois : visuel principal + vignette).

> ⚠️ **Piège de publication.** `templates/collection.json` fait **9 080 o en MAIN** contre **16 088 o en TRAVAIL**, et
> `product.json` diverge sur bien plus que les avis. Publier TRAVAIL tel quel n'appliquera pas seulement les correctifs :
> il remplacera aussi le template de collection. À differ avant publication, ou à re-dupliquer MAIN puis ré-appliquer
> les correctifs dessus.

### 2. Six problèmes **que les passes précédentes n'avaient pas vus**

| # | Problème | Gravité |
|---|---|---|
| **N1** | **Faux témoignages clients incrustés dans les images produit** — 5 étoiles, prénom + ville inventés, sur **37 fiches** dont **32 actives** | **P0** |
| **N2** | **910 variantes sur 923 portent le SKU brut du fournisseur AliExpress**, publié dans le JSON-LD de chaque fiche, dont **113 contenant littéralement « no logo »** | **P0** |
| **N3** | **`contact.noirmont@gmail.com` est publié sur le site** dans la politique de confidentialité rendue, alors que tout le reste publie `contact@maisonnoirmont.fr` | **P0** |
| **N4** | **Aucun mécanisme de consentement cookies** : pas de bandeau, pas d'API `Shopify.customerPrivacy`, pas de cookie `_tracking_consent` — et le lien « Préférences en matière de cookies » du pied de page pointe vers un **404** | **P0 (FR/RGPD)** |
| **N5** | **Aucune mesure de conversion** : ni `gtag`, ni `dataLayer`, ni GA4, ni balise Google. La porte 5 §E de Kraken est en échec sec | **P0 (avant Ads)** |
| **N6** | **« 904L » subsiste dans deux URL produit actives et dans un texte alternatif d'image**, alors que le corps des fiches a été purgé de la mention | **P1** |

**Ordre de bataille** : traiter N1→N6 + les P0 hérités, appliquer le tout **sur le thème qui sera publié**, vérifier au
rendu, **puis seulement** créer le compte GMC (T-F §7 : « Never create GMC before the store is complete »).

Le reste du dossier reste **solide** : délais cohérents partout, prix cohérents page/panier, livraison réelle = livraison
annoncée, zéro prix barré, catalogue rédigé avec des réserves honnêtes sur l'étanchéité et les calibres.

---

# CHECKLIST FUSIONNÉE

## A — Identité, transparence, contact

| # | Point de contrôle | Source | Statut | Preuve citée | Correction exacte | Prio |
|---|---|---|---|---|---|---|
| A1 | E-mail cliquable `mailto:` visible | T-F §4 « Clickable email using mailto: » | ✅ conforme | Pied de page rendu : `mailto:contact@maisonnoirmont.fr` (2 occurrences par page) | — | — |
| A2 | **Un seul** e-mail de contact sur tout le site | T-F §2 « Consistency beats perfection » ; SK principe 2 | ❌ **BLOQUANT (N3)** | `/policies/privacy-policy` **rendu** : « veuillez nous appeler au , nous envoyer un e-mail à l'adresse**contact.noirmont@gmail.com** ». Le reste du site publie `contact@maisonnoirmont.fr`. API : `shop.email` = `shop.contactEmail` = `contact.noirmont@gmail.com` | Réglages → Général : passer l'e-mail de la boutique à `contact@maisonnoirmont.fr` (la politique Shopify injecte `{{ email }}` = cet e-mail). Vérifier ensuite le rendu de `/policies/privacy-policy` | **P0** |
| A3 | Téléphone joignable, affiché au pied de page et cliquable `tel:` | T-C p.5 ; T-F §4 « Voice-capable phone number » | ❌ à corriger | Pied de page rendu : **0 lien `tel:`**, **0 occurrence** de `+33` ou `07 56`. Le numéro `+33 7 56 82 80 94` n'existe que dans `/policies/contact-information` et `/policies/legal-notice` | Ajouter `<a href="tel:+33756828094">+33 7 56 82 80 94</a>` au pied de page (`sections/footer-group.json`, bloc `text_hzJHEn` du groupe `group_y4aNMX`) | **P1** |
| A4 | **Téléphone renseigné dans les réglages Shopify** | KR §A « identité légale, coordonnées » ; T-C p.7 « Shopify settings must match footer » | ❌ à corriger — **non relevé auparavant** | API : `shop.billingAddress.phone` = `""` (vide), `shop.billingAddress.company` = `""`. C'est pour cela que la politique de confidentialité rendue affiche « appelez-nous au  » suivi de **rien** | Réglages → Général → renseigner téléphone `+33 7 56 82 80 94` et raison sociale `OH Ventures` | **P1** |
| A5 | Page contact complète (pas seulement un formulaire) | T-C p.5 « Display contact information clearly in footer, contact page, and policy pages » | ❌ à corriger | API : `page(contact).body` = `""` (chaîne vide). Rendu de `/pages/contact` : « Contact · Prénom · Nom · Téléphone · Email · Envoyer » — **rien d'autre**. `get_page_text` renvoie même « No text content found » | Ajouter au-dessus du formulaire : raison sociale, adresse postale, e-mail cliquable, téléphone cliquable, horaires (« du lundi au vendredi », déjà écrit dans `/policies/contact-information`), délai de réponse (24 h ouvrées) | **P1** |
| A6 | Formulaire de contact fonctionnel | KR §A « contact fonctionnel » | ✅ conforme | `<form action="/contact#contact_form">`, champs `contact[first_name] / last_name / phone / email / body` → formulaire natif Shopify, opérationnel | — | — |
| A7 | Formulaire : mention RGPD / finalité | FR (RGPD art. 13) | ⚠️ à corriger | Aucune mention d'information ni de finalité sous le formulaire (rendu) | Ajouter sous le bouton : « Vos coordonnées servent uniquement à traiter votre demande. Détails dans notre politique de confidentialité. » | P2 |
| A8 | Adresse réelle et cartographiable | T-F §4 « Real, mappable address » | ✅ conforme | Mentions légales rendues : « 47 rue Vivienne, 75002 Paris » — concorde avec `shop.billingAddress` | — | — |
| A9 | Page « À propos » humaine, sans historique inventé | T-F §4 « Short, simple, human-written · No exaggerated history » | ✅ conforme | `/pages/la-maison` rendu : « NOIRMONT est née d'une conviction simple : une montre n'a pas besoin d'un grand nom pour avoir de l'allure […] Nous annonçons le calibre de chaque référence ». **Aucune date de fondation, aucun atelier, aucun effectif inventés.** | — | — |
| A10 | Pas de réseaux sociaux vides liés trop tôt | T-F §4 « No social links > weak or new social pages » | ✅ conforme | Bloc `social_icons_hQdtRf` = `disabled: true` ; 0 lien externe au pied de page | — | — |
| A11 | Trustpilot ≥ 3,0 ou absent | T-F §4 ; APPENDIX B | ✅ conforme | Aucun compte Trustpilot. **Mais** le badge de thème imite visuellement Trustpilot (`review_badge_style: "trustpilot"`) → voir D2 | — | — |
| A12 | ™ / © seulement si détenus | T-C p.5 | ✅ conforme | Pied de page : « © 2026 Maison Noirmont » (droit d'auteur sur le site, légitime). Aucun ™ sur des marques tierces | — | — |

## B — Politiques, mentions légales, cohérence

| # | Point de contrôle | Source | Statut | Preuve citée | Correction exacte | Prio |
|---|---|---|---|---|---|---|
| B1 | 7 politiques rattachées à la caisse, non vides | T-F §5 « Policies live only in Shopify → Settings → Policies » | ✅ conforme | `shop.shopPolicies` : CONTACT (554 c.) · LEGAL_NOTICE (22 240) · PRIVACY (22 124) · REFUND (2 098) · SHIPPING (1 770) · TERMS_OF_SALE (15 146) · TERMS_OF_SERVICE (14 990). Zéro lorem, zéro page vide | — | — |
| B2 | **Politique de retour ≡ vitrine** | T-F §5 « Google checks line-by-line: return window & refund timing » ; SK principe 2 | ❌ **BLOQUANT** | **Trois versions coexistent, toujours.** FAQ (corrigée, en ligne) : « 14 jours […] **montre portée à l'essai comprise** ». Fiche produit MAIN (en ligne) : « **14 jours satisfait ou remboursé** » puis « La montre doit être retournée **non portée** ». Politique de remboursement (en ligne, **non corrigée** — 2 098 c., inchangée) : « à l'état neuf, **non porté et non rayé** ». CGV art. 10 (en ligne) : « Les Produits endommagés, **portés**, rayés […] **ne sont pas repris** » | Appliquer les corps déjà rédigés dans `backup-retours-2026-08-08/a-appliquer-par-hakim/` (`POLITIQUE-REMBOURSEMENT-…html`, `CGV-politique-boutique-…html`, `CGV-page-shopify-…html`) — ils sont **prêts et cohérents** avec la FAQ. Puis aligner `templates/product.json` et `templates/cart.json` **du thème qui sera publié** | **P0** |
| B3 | Cohérence du texte « portée à l'essai » avec le droit | FR art. L221-23 C. consom. | ✅ la direction retenue est la bonne | Le client peut manipuler le bien « pour en établir la nature, les caractéristiques et le bon fonctionnement » ; seule une dépréciation au-delà engage sa responsabilité. Le corps préparé le dit mot pour mot | Ne pas revenir à « non porté » : ce serait une clause abusive **et** un mismatch GMC | — |
| B4 | Rétractation non restreinte pour les produits « sur mesure » | FR art. L221-28 3° | ✅ **corrigé et vérifié** | FAQ rendue : « Le configurateur ne fabrique rien à vos spécifications : il vous montre la référence de notre catalogue qui correspond à vos réponses. Chaque montre proposée est au catalogue — elle ouvre donc exactement les mêmes droits de rétractation et de retour que les autres. » | — | — |
| B5 | Médiateur de la consommation nommé | FR art. L612-1 C. consom. ; KR §A « mentions requises » | ❌ **BLOQUANT** | CGV art. 17 **rendu en ligne** : « Médiateur de la consommation de maisonnoirmont.fr : **[À COMPLÉTER — nom, adresse et téléphone du médiateur auprès duquel Maison Noirmont a souscrit une adhésion…]** » (vérifié : `completer: true` sur `/policies/terms-of-sale`) | Adhérer à un médiateur **pour ce site** (l'adhésion est souscrite par site, ne pas recopier celle de Tuftéo), puis remplacer le marqueur. Tant qu'il est visible, un examinateur qui ouvre les CGV voit un site inachevé | **P0** |
| B6 | Plateforme européenne ODR | FR / UE | ⚠️ à corriger — **non relevé auparavant** | CGV art. 17 rendu : « déposer sa réclamation sur la plateforme européenne de règlement en ligne des litiges accessible à l'adresse suivante : `https://ec.europa.eu/consumers/odr` ». **Cette plateforme a cessé de fonctionner le 20 juillet 2025** (règlement ODR abrogé) | Supprimer le renvoi ODR, ou le remplacer par le renvoi au médiateur national et à la DGCCRF | P2 |
| B7 | Mentions légales complètes | FR art. 6-III LCEN + art. R123-237 C. com. | ⚠️ partiellement | `/policies/legal-notice` rendu : Propriétaire ✅ · adresse ✅ · téléphone `+33 7 56 82 80 94` ✅ · capital 1000 € ✅ · **SIRET** 10315725100010 ✅ · **TVA** FR55103157251 ✅ · Responsable publication : Hakim Ouahabi ✅ · DPO ✅ · Hébergeur Shopify Inc. avec adresse et téléphone ✅. **Manquants : la forme juridique, le numéro RCS + ville d'immatriculation** (`/RCS/i` → `false`), et le SIREN n'apparaît que noyé dans le SIRET | Ajouter la ligne : « OH Ventures, [forme juridique] au capital de 1 000 € — RCS Paris [n°] — SIREN 103 157 251 » | **P1** |
| B8 | Politique de confidentialité : mentions RGPD | FR RGPD art. 13-14 ; KR §F | ⚠️ à corriger — **non relevé auparavant** | Le corps stocké est le texte automatisé Shopify avec **6 balises Liquid** (`{{ shop_name }}`, `{{ last_updated }}`, `{{ phone }}`, `{{ email }}`, `{% if address %}`, `{% if selling_to_europe %}`). Le rendu résout bien les variables (« Dernière mise à jour : 24 juillet 2026 », responsable du traitement ✅) **mais** : `{{ phone }}` sort **vide** (cf. A4), `{{ email }}` sort en **Gmail** (cf. A2), et le texte ne mentionne **ni la CNIL ni aucune autorité de contrôle** (`/CNIL|autorité de contrôle/i` → `false`), ni la durée de conservation détaillée, ni les bases légales | Remplir A2 et A4 (les deux variables se corrigent d'elles-mêmes), puis ajouter un paragraphe « Réclamation » : « Vous pouvez introduire une réclamation auprès de la CNIL (3 place de Fontenoy, TSA 80715, 75334 Paris Cedex 07 — cnil.fr). » Base : `drop-elite-google-os/policies-fr/confidentialite.md` | **P1** |
| B9 | Coquille de rendu dans la confidentialité | KR §A | ⚠️ à corriger | Rendu littéral : « nous envoyer un e-mail à l'adresse**contact.noirmont@gmail.com** » — l'espace manque entre « adresse » et l'e-mail | Se corrige avec A2, mais relire la phrase après correction | P2 |
| B10 | Pas de politiques dupliquées | T-F §5 « No duplicate policy pages » (motif de refus immédiat, APPENDIX B) | ❌ à corriger | Le **pied de page relève chaque politique deux fois**, sur deux listes : liste maison (`/pages/mentions-legales`, `/policies/privacy-policy`, `/pages/politique-de-cookies`, `/policies/refund-policy`, `/policies/shipping-policy`, `/policies/terms-of-sale`, `/policies/terms-of-service`) **puis** la liste Shopify (`/policies/privacy-policy`, `/policies/refund-policy`, `/policies/shipping-policy`, `/policies/terms-of-service`, `/policies/terms-of-sale`, `/policies/contact-information`, `/policies/legal-notice`). Deux URL distinctes servent le même texte de mentions légales : `/pages/mentions-legales` **et** `/policies/legal-notice` | Garder **une seule** liste (la Shopify, qui est celle recopiée dans GMC), faire pointer « Mentions légales » sur `/policies/legal-notice` et dépublier `/pages/mentions-legales` | **P1** |
| B11 | Politique cookies accessible | FR ; KR §F | ⚠️ | `/pages/politique-de-cookies` existe et est correcte sur le fond (liste `_session_id`, `_shopify_visit`, `_shopify_uniq`, `cart`, `_secure_session_id`, `storefront_digest`) — mais c'est une **page**, pas une politique Shopify : elle n'apparaît **pas** dans le pied de page de la caisse | Soit la basculer en politique Shopify, soit l'intégrer à la politique de confidentialité | P2 |
| B12 | **La politique cookies promet un choix qui n'existe pas** | KR §A « absence de promesses trompeuses » | ❌ à corriger — **non relevé auparavant** | Texte rendu : « Nous les énumérons ici pour que vous ayez **la possibilité de choisir si vous souhaitez les autoriser ou non** » + section « **Gérer vos cookies** ». Or aucun mécanisme de choix n'existe (cf. D6/F1) | Soit installer le consentement (recommandé), soit réécrire la phrase | **P1** |
| B13 | Politique d'expédition : heure limite + fuseau + délais | T-F §5 « Shipping cut-off time + timezone · Handling & transit windows » | ✅ **exemplaire** | `/policies/shipping-policy` : « Heure limite de prise en compte des commandes : du lundi au vendredi, **15 h (GMT+1, heure de Paris)** » · « préparées et transmises à l'expédition dans un délai de **24 h à 48 h** » · « Délai de livraison total estimé : **14 à 21 jours** » | — | — |
| B14 | Délais identiques partout | SK adaptation FR ; T-F §5 | ✅ conforme | J+14/J+21 = « 2 à 3 semaines » : politique d'expédition, CGV art. 8, CGU, FAQ, bandeau, pied de page, fiche produit, panier, tarif de caisse (« Livraison gratuite et suivie en France — comptez 2 à 3 semaines », vérifié dans `deliveryProfiles`) | — | — |
| B15 | Délai de remboursement annoncé | T-F §5 « Refund timing » | ✅ conforme | Politique de remboursement : « Le délai de traitement peut varier de **7 à 14 jours** selon votre établissement bancaire » | — | — |
| B16 | Moyens de paiement annoncés en CGV = caisse | T-C p.7 « Payment icons must match checkout options » | ⚠️ à corriger | CGV art. 7 rendu : « Par cartes bancaires : Carte Bancaire, Visa, MasterCard, American Express, **Maestro** » (`maestro: true`). Maestro n'est pas proposé en caisse ; Klarna et le paiement en 4 fois n'y sont pas nommés | Retirer « Maestro », ajouter « paiement en 4 fois via PayPal ou Klarna » | P2 |
| B17 | Adresse de retour explicite | T-P « How to Return an Item » | ✅ conforme | Politique de remboursement : « OH Ventures, 47 rue Vivienne, 75002 Paris, France » + « N'envoyez aucun colis avant d'avoir reçu notre accord écrit » | — | — |
| B18 | Qui paie le retour | T-P « Return Costs » | ✅ conforme | « Les frais d'expédition pour le retour de votre article sont **à la charge du client** » (politique) ; CGV art. 10 : « les frais de retour restant à la charge du Client » | — | — |
| B19 | Politiques **non copiées** d'une autre boutique du groupe | T-F §5 ; SK « jamais deux boutiques avec le même texte » | ✅ conforme | Recherche sur les 7 corps : **0 occurrence** de « tufteo », « Tuftéo », « CM2C » | — | — |
| B20 | Garanties légales FR citées | FR art. L217-3 s. | ✅ conforme | CGV art. 11 : garantie légale de conformité (2 ans, dispense de preuve 24 mois) + vices cachés + garantie commerciale 12 mois « en sus » — formulation identique en FAQ, politique de remboursement et fiches | — | — |

## C — Produits, données de flux, images

| # | Point de contrôle | Source | Statut | Preuve citée | Correction exacte | Prio |
|---|---|---|---|---|---|---|
| C1 | **Images sans texte incrusté ni collage** | T-C p.6 « No text overlays on product images · No collage-style images » ; T-F §6 | ❌ **BLOQUANT (N1)** | **37 fiches** (dont **32 actives**) portent en dernière position de galerie une image **entièrement composée de texte** : cinq étoiles vertes, une citation, un prénom + une ville, et le logotype MAISON NOIRMONT. Contenu lu sur les fichiers téléchargés : `10977444528466-7.jpg` → « ★★★★★ *« Numéro de suivi dès l'expédition, délai tenu, montre réglée et contrôlée. La garantie 12 mois a fini de me convaincre. »* — **Mehdi A. — Strasbourg** » ; `gmt-7.jpg` → « ★★★★★ *« Après une plongeuse, j'ai pris la GMT. Même sérieux : mouvement automatique japonais, finitions propres, réponses rapides par e-mail. »* — **Karim B. — Marseille** ». Textes alternatifs : « Contre-la-montre — **témoignage client** — Maison Noirmont ». Rendu confirmé visible sur `/products/contre-la-montre-noir-chronographe` | **Supprimer ces 9 visuels des 37 fiches.** Ils cumulent trois infractions : faux avis, texte incrusté sur image produit, image dupliquée entre produits | **P0** |
| C2 | **Faux avis** | T-C p.6 « No fake or manipulated reviews » ; KR §A | ❌ **BLOQUANT (N1)** | Même preuve que C1. **La boutique compte 0 commande.** Ces visuels nomment des clients, des villes, des délais tenus et des réachats | Suppression pure ; ne réintroduire que via une app d'avis vérifiés après commandes réelles | **P0** |
| C3 | **Pas d'images dupliquées entre produits** | T-C p.6 « No duplicate images across products » | ❌ à corriger | `10977444528466-7.jpg` sur 3 fiches, `10977444561234-7.jpg` sur 3, `gmt-7.jpg` sur 3 (page 1) — et les mêmes fichiers réapparaissent sur 22 fiches actives supplémentaires (page 2). Au total **9 fichiers distincts pour 37 emplacements** | Réglé par C1 | **P0** |
| C4 | **SKU propres, ne révélant pas le fournisseur** | T-F §6 « Unique titles, descriptions, SKUs » ; KR §B ; T-C p.6 | ❌ **BLOQUANT (N2)** | **910 variantes sur 923** portent un SKU au format AliExpress. Exemple lu **dans le JSON-LD public** de `/products/trente-neuf-classique-cannelee` : `"sku":"14:193#orange no logo;5:57085267#8215-39mm(solidback)"`. **113 variantes contiennent littéralement la chaîne « no logo »**, sur **91 produits actifs**. Longueur max 72 caractères | Réécrire les SKU en référence maison (`NRM-39CAN-OR-8215-39-SB`). Ce champ part au flux Shopping (souvent mappé en `mpn`) **et** il est déjà dans les données structurées de chaque page | **P0** |
| C5 | GTIN / MPN jamais inventés | KR §B « Ne jamais inventer GTIN ou MPN » | ✅ conforme | Scan des 923 variantes : **`barcode` non vide = 0**. Aucun code-barres fabriqué | Au flux, déclarer `identifier_exists: no` (marque propre sans GTIN fabricant). **Ne pas** mapper le SKU actuel en `mpn` | — |
| C6 | Marque cohérente | KR §B | ✅ conforme | `vendor` = « Maison Noirmont » sur 105/105 produits ; JSON-LD : `"brand":{"@type":"Brand","name":"Maison Noirmont"}` | — | — |
| C7 | Titre produit ≡ URL | T-C p.6 « Product title must match the product URL » | ⚠️ à corriger | **9 fiches actives** divergent fortement (recouvrement lexical < 0,6) : `Explorateur — Sport chic à chiffres 3-6-9` → `/montre-acier-chiffres-3-6-9-explorateur` · `Bracelet Présidentiel — acier inoxydable` → `/bracelet-presidentiel-904l` · `Éclaireur Bronze — Field militaire à chiffres 1-12` → `/montre-field-bronze-cadran-chiffres-1-12` · `Squelette Carré — …` → `/montre-squelette-automatique-carree` · `Noirmont Un — Aviateur acier à chiffres 1-12` → `/montre-aviateur-acier-cadran-chiffres-1-12` · `Bracelet FKM — embouts courbes` → `/bracelet-fkm-courbe` · `Pince à barrettes — outil d'horloger` → `/pince-a-barrettes` · `Éclaireur Acier — Field à chiffres 1-12` → `/montre-field-acier-cadran-chiffres-1-12` | Écart toléré tant que le mot-clé principal est commun — **sauf** les deux cas « 904L » (C8). Ne pas changer les handles SEO sans redirection 301 | P2 |
| C8 | **Aucune allégation matériau invérifiable** | T-C p.6 « Avoid exaggerated or unverifiable claims » ; KR §A | ❌ à corriger — **non relevé auparavant (N6)** | Le corps des fiches a bien été purgé de « 904 », mais la mention subsiste **là où Google la lit quand même** : ① URL active `/products/bracelet-presidentiel-904l` (titre : « Bracelet Présidentiel — **acier inoxydable** ») ; ② URL active `/products/bracelet-jubile-acier-904l-20mm` (titre : « Bracelet Jubilé acier — 20 mm », corps : « acier inoxydable ») ; ③ **texte alternatif** de l'image principale de cette seconde fiche : « Bracelet Jubilé **acier 904L** — acier 20 mm » ; ④ nom de fichier `noirmont-jubile-904l-1.jpg`. L'URL et l'alt **contredisent** le titre et le corps | Changer les deux handles (`bracelet-presidentiel-20mm`, `bracelet-jubile-acier-20mm`) avec redirection 301, réécrire l'alt, renommer le fichier | **P1** |
| C9 | Titres et descriptions originaux | T-C p.6 « Titles and descriptions must be original » | ✅ conforme | 105 corps relus : rédaction maison, pédagogique, aucun copier-coller fournisseur. Aucun titre en doublon (`sort \| uniq -d` → vide) | — | — |
| C10 | Calibres décrits sans mensonge | KR §A ; règles maison | ✅ **exemplaire** | 0 occurrence de « automatique » sur les 12 chronographes ; « méca-quartz Seiko VK63 (japonais) […] **fonctionne sur pile** » ; FAQ, collection Chronos et page La Maison disent la même chose. PT5000 jamais présenté comme suisse. 0 occurrence de « Swiss made » / « suisse » sur tout le catalogue | — | — |
| C11 | Étanchéité systématiquement « annoncée » | KR §A ; règles maison | ✅ conforme | 100 % des mentions hedgées : « **Étanchéité annoncée** 10 bar : douche, piscine et baignade en surface ; la plongée reste déconseillée » ; une fiche assume même « l'étanchéité n'est pas précisée par le fournisseur : tenez-la à l'écart de l'eau ». Cas `Explorateur` traité avec prudence : « le fournisseur annonce 10 bar alors que certains cadrans impriment "200 m" : **nous retenons la valeur la plus prudente** » | — | — |
| C12 | Cadran non stérile déclaré | KR §A | ✅ **exemplaire** | `Explorateur` : « Une mention technique **« Professional Automatic »** figure sous l'axe des aiguilles, fidèle aux photos » — la seule exception à « cadran vierge » est déclarée | — | — |
| C13 | Réserve « étanchéité non re-testée après remontage » | KR §A | ⚠️ ouvert | Aucune fiche ne signale qu'un boîtier rouvert perd l'étanchéité d'origine. Concerne les 15 fiches à étanchéité annoncée | Ajouter au bloc « Calibres & spécifications » : « l'étanchéité annoncée est celle déclarée par le fabricant du boîtier et n'est pas re-testée après montage » | P2 |
| C14 | Titres « Plongeuse » sur des montres à 5 ATM | KR §A | ⚠️ ouvert (domaine réservé de Hakim) | 3 titres actifs `Héritage Bleu / Bleu nuit / Vert — Plongeuse vintage 42`, données à 5 ATM. Le corps requalifie (« "Plongeuse" décrit ici un style, pas un usage ») — **mais c'est le titre qui part au flux Shopping**, sans le paragraphe | Si ces fiches partent en Shopping : « Héritage Bleu — Vintage 42, **style plongeuse** » | P2 |
| C15 | Vocabulaire de marque tierce | KR §A ; T-C p.6 | ⚠️ à trancher — **non relevé auparavant** | Le catalogue emploie des noms de bracelets/modèles issus du vocabulaire d'une grande maison suisse : « **jubilé** » (très répandu dans les titres et corps), « **Présidentiel** / bracelet **Président** » (2 fiches bracelets + 1 montre), « **Explorateur** », « lunette **cannelée**, cadrans **panda** ». Le tag `skx` est posé sur 4 produits (désignation d'un modèle Seiko) | « Jubilé », « panda », « cannelée » sont devenus des descripteurs de forme dans l'horlogerie et se défendent. « **Président / Présidentiel** » et le tag « **skx** » sont plus exposés : renommer en « bracelet à maillons arrondis » et retirer le tag `skx` (non affiché, sans valeur SEO ici) | P2 |
| C16 | Disponibilité cohérente | KR §B tableau ; T-C p.7 « Archive out-of-stock products » | ✅ conforme | 96 produits actifs, **0 variante active en `availableForSale: false`**, **0 produit actif sans variante disponible**. 907/923 variantes en `inventoryPolicy: CONTINUE` → la disponibilité affichée est stable et vraie pour un modèle dropship | — | — |
| C17 | Prix cohérents page / panier / flux | KR §B ; T-C p.7 | ✅ conforme | PDP `trente-neuf-classique-cannelee` : `€329` affiché · JSON-LD : `"price":"329.00"` (39 mm fond acier) et `"358.00"` (fond verre) · Panier rendu : `Total estimé €329` pour la même variante · « €82,25 » = 329 ÷ 4 (Klarna/PayPal 4×) exact | — | — |
| C18 | Aucun prix barré | T-C ; audit du 08/08 | ✅ conforme | Scan des **923 variantes** : `compareAtPrice != null` → **0** | — | — |
| C19 | Devise | KR §A « prix et devise cohérents » | ✅ conforme | `shop.currencyCode` = **EUR** · marché unique « France » (`primary: true`, `enabled: true`) · tous les prix rendus en `€` | — | — |
| C20 | Taxes | FR art. L112-1 C. consom. ; KR §A | ⚠️ à corriger — **non relevé auparavant** | API : `taxesIncluded: true`, `taxShipping: false` → les prix affichés **sont** TTC, c'est correct. Mais **aucune mention « TTC » ou « TVA incluse » nulle part** : ni sur la fiche, ni au panier (`/TVA\|taxes incluses\|toutes taxes/i` → `false` sur les deux) | Ajouter « TTC » sous le prix de la fiche et « Total estimé (TTC) » au panier | **P1** |
| C21 | Collections ≥ 5 produits | T-F §6 « Minimum 5 products per collection · No empty or hidden collections » | ❌ à corriger — **non relevé auparavant** | `productsCount` par collection : `montre-squelette` = **2** (en dessous du seuil, et servie publiquement : `/collections/montre-squelette` répond 200 avec un titre SEO complet) · `frontpage` (« Page d'accueil ») = **1**. Les 12 autres sont ≥ 5 (plongeuses 5, cadrans à chiffres 5, gmt 7, outils 8, bracelets 10, écrins 10, chronos 13, remontoirs 13, sport chic 16, classiques 20, accessoires 42, montres 63) | Porter « Montres squelette » à 5 fiches (le sourcing « Pièces & Mod » est déjà voté) ou la dépublier jusque-là. Vider ou masquer `frontpage` | **P1** |
| C22 | Descriptions de collection exactes | KR §A | ⚠️ à corriger — **non relevé auparavant** | Trois compteurs faux dans les descriptions rendues : Plongeuses annonce « **Nos six modèles** » pour **5** produits · GMT annonce « **Nos six Voyageur** » pour **7** · Chronos annonce « **Nos douze Contre-la-montre** » pour **13** | Remplacer les nombres par des formulations non chiffrées (« Nos modèles vont de… ») pour éviter la dérive à chaque ajout | P2 |
| C23 | Champs SEO renseignés | T-F §2 « thin pages » | ⚠️ | **16 fiches actives sans meta-description**, dont **12 sans meta-title** (`remontoir-solo`, `remontoir-vitrine`, `coffret-douze-aluminium`, `coffret-douze-presentation`, `pince-a-barrettes`, `barrettes-de-rechange-270`, `set-tournevis-horloger`, `bracelet-presidentiel-904l`, `bracelet-presidentiel-dore`, `bracelet-fkm-courbe`, `bracelet-fkm-tropical`, `loupe-de-date-saphir` + 4 avec titre mais sans description) | Compléter — sans effet direct sur GMC, mais « trust assets » (T-F §2) | P2 |
| C24 | **Carte cadeau dans le catalogue** | Politique Google Shopping (produits non éligibles) | ⚠️ à corriger — **non relevé auparavant** | `carte-cadeau-maison-noirmont`, `productType: "Carte cadeau"`, statut **ACTIVE** | Ne pas la laisser partir au flux : l'exclure explicitement dans l'app de flux (règle sur `product_type = Carte cadeau`). La garder sur le site est sans problème | **P1** |
| C25 | Description de la carte cadeau | FR | ✅ conforme | « **Sans date d'expiration.** Elle attend le temps qu'il faut. » — engagement tenable, plus favorable que la loi | — | — |
| C26 | Images intégrées dans les descriptions | T-F §6 « Avoid embedded images in descriptions » | ✅ conforme | Aucun `<img>` dans les 105 corps de fiche | — | — |
| C27 | Textes alternatifs présents | accessibilité / qualité | ✅ conforme | 0 image de fiche sans `alt` (hors la fiche DRAFT `aviateur-acier-cadran-chiffres-arabes`, qui a **0 média** — à ne pas activer en l'état) | Ne pas activer cette fiche sans visuels | P2 |
| C28 | Noms de fichiers cohérents avec les titres | qualité | ⚠️ | `montre-field-acier-cadran-chiffres-**arabes**-face.jpg` et les alt « Field à chiffres **arabes** » alors que le produit a été renommé « chiffres **1-12** » (renommage voulu, cf. description de la collection) | Cosmétique | P2 |

## D — Faux signaux commerciaux

| # | Point de contrôle | Source | Statut | Preuve citée | Correction exacte | Prio |
|---|---|---|---|---|---|---|
| D1 | Sections d'avis fabriqués | T-C p.6 ; KR §A | ❌ **BLOQUANT** en MAIN | MAIN : `sections/reviews_rXFabc` (accueil) et `sections/reviews_8P6xW3` (fiche) → `disabled = None`. Rendu de `/` : « Ils portent Noirmont », **David L.**, **Julien D.**, **Mehdi A.** | `"disabled": true` sur les deux, **dans le thème qui sera publié** (déjà fait en TRAVAIL) | **P0** |
| D2 | Badge « 4,8/5 · 1340 avis » | T-C p.6 ; T-F APPENDIX B | ❌ **BLOQUANT** en MAIN | MAIN `templates/product.json` → `blocks/reviews_badge_noirmont` : `disabled = None`, `review_badge_style: "trustpilot"`, `text_1: "4,8/5"`, `text_2: "1340 avis"`. **Rendu vérifié** sur deux fiches : `"4,8/5\n1340 avis"`. Il est dans la section `main` → il sort sur **les 96 fiches actives** | `"disabled": true` (déjà fait en TRAVAIL). Le style « trustpilot » imite un organisme tiers : ne jamais le réactiver même avec de vrais avis | **P0** |
| D3 | « 2 000 clients satisfaits » | KR §A | ⚠️ dormant mais intact **dans les deux thèmes** | `text_mLtNpU` = `"<p>- 2 000 clients satisfaits</p>"`, `disabled = None` en MAIN **et** en TRAVAIL. Non rendu aujourd'hui (le groupe parent n'est pas servi : `has2000: false` sur `/`), mais réactiver la bannière le remet en ligne | Vider la valeur, ne pas se contenter de la désactivation d'un parent | **P1** |
| D4 | Blocs `rating-stars` à 4,5/123 avis | KR §A | ⚠️ | `rating_stars_z9LL3m` (accueil) et `rating_stars_Krck47` (fiche) : `rating: 4.5`, `review_count: 123`, neutralisés par `hide_rating_when_no_reviews: true`. **`disabled = None` en MAIN**, `true` en TRAVAIL | Vider les valeurs (`review_count: 0`) | **P1** |
| D5 | **Compte à rebours sur la page mot de passe** | T-C p.5 « Avoid fake urgency (false scarcity, misleading countdowns) » | ❌ à corriger — **actif dans les DEUX thèmes** | `templates/password.json` a **le même md5 `e9cf34c4…` en MAIN et en TRAVAIL** ; `countdown_aJCPJc` → `disabled = None`, `date_end: "01/01/2028 00:00"`, `timer_ended_text: "L'offre est terminée"`. **Vérifié en requête anonyme** : `/password` charge `countdown.js`, contient `01/01/2028` et « offre est terminée ». **C'est la seule page que Google peut voir aujourd'hui** | `"disabled": true` sur `countdown_aJCPJc` — à faire **dans les deux thèmes** | **P1** |
| D6 | Pictos de paiement = caisse | T-C p.7 « Payment icons must match checkout options » | ❌ à corriger — **identique dans les deux thèmes** | Pied de page rendu, `aria-label` des SVG : `["Visa","Mastercard","Apple Pay","**Google Pay**","PayPal","Shop Pay"]`. API : `shop.paymentSettings.supportedDigitalWallets` = `["SHOPIFY_PAY","APPLE_PAY"]` → **Google Pay n'est pas activé**. Inversement Amex et Klarna sont actifs en caisse et **non affichés**. `config/settings_data.json` : md5 `e51fe7c4…` **identique en MAIN et TRAVAIL**, `force_icons_display` présent | Repasser `force_icons_display` à `false` (le thème affiche alors `shop.enabled_payment_types`, donc exactement la caisse, sans entretien) — **ou** `"show_google_pay": false` + `"show_american_express": true` + `"show_klarna": true` | **P1** |
| D7 | Compteurs de stock / rareté | T-C p.5 | ✅ conforme | Le bloc `product-inventory` existe dans le thème mais n'est instancié dans **aucun** template | — | — |
| D8 | Badges « promotion » / « économie » | T-C | ✅ conforme | 0 `compareAtPrice` → aucun badge ne peut se calculer ; `/collections/montres` : 0 badge rendu | — | — |
| D9 | Compte à rebours en boutique | T-C p.5 | ✅ conforme | Aucun bloc `countdown` dans `index`, `product`, `collection`, `cart`, `header-group`, `footer-group` — uniquement `password.json` (D5) | — | — |
| D10 | Bandeaux : promesses vérifiables | KR §A | ✅ conforme | Bandeau annonce : « Livraison offerte en France métropolitaine » · « Cadran vierge de tout logo emprunté » · « Votre Noirmont en trois étapes ». Bandeau défilant : « Calibre annoncé sur chaque fiche » · « Retour sous 14 jours » · « Garantie 12 mois » · « Paiement en 4 fois » (Klarna/PayPal actifs) — toutes vraies | — | — |
| D11 | Aucune note agrégée dans les données structurées | KR §B | ✅ conforme | JSON-LD de `/products/trente-neuf-classique-cannelee` : `aggregateRating` **absent**, `review` **absent**. Le faux 4,8/5 ne remonte donc pas en rich snippet — il reste néanmoins visible à l'écran (D2) | — | — |

## E — Technique

| # | Point de contrôle | Source | Statut | Preuve citée | Correction exacte | Prio |
|---|---|---|---|---|---|---|
| E1 | Aucun lien mort | T-C p.7 « No broken links » ; T-F §8 « Ensure no 404 errors exist » | ❌ à corriger | Le pied de page de **toutes** les pages contient `<a href="/policies/#shopifyReshowConsentBanner">Préférences en matière de cookies</a>`. **`/policies/` renvoie un 404** (« 404 Page introuvable – Maison Noirmont », vérifié au rendu). C'est un lien mort **présent sur chaque page du site** | Le lien vient du bloc de politiques Shopify : il n'apparaît que si la bannière de consentement existe. Réglé par F1 ; sinon retirer le bloc | **P1** |
| E2 | Pas de code de vérification GMC résiduel | T-C p.7 « Remove old or duplicate GMC verification codes » | ✅ conforme | `layout/theme.liquid` = 2 331 o, aucune balise `google-site-verification` ; aucun script inline Google (`inlineGoogle: 0`) | — | — |
| E3 | Thème non dupliqué entre boutiques | T-C p.7 | ✅ conforme | Thème `FullStack 2.3.0` fortement personnalisé (`noirmont-*.css/js`, `noirmont-configurateur.liquid`, `blocks/noirmont-*.liquid`) | — | — |
| E4 | Réglages Shopify ≡ pied de page ≡ politiques | T-C p.8 « All must align » | ❌ à corriger | Divergences relevées : e-mail (A2), téléphone vide (A4), raison sociale vide (A4) | Voir A2 et A4 | **P0/P1** |
| E5 | Produits publiés sur le canal Boutique en ligne | mémoire projet | ✅ conforme | `resourcePublications` : « Boutique en ligne » `isPublished: true` sur l'échantillon testé ; `onlineStoreUrl` est `null` uniquement parce que la boutique est sous mot de passe (`onlineStorePreviewUrl` correct) | — | — |
| E6 | Pages inutiles dépubliées | T-F §2 « hidden / thin pages » | ✅ voulu | 5 pages `/pages/` dépubliées (`conditions-generales-de-vente`, `politique-de-livraison`, `politique-de-remboursement`, `politique-de-confidentialite`, `conditions-generales-d-utilisation`) : `isPublished: false`, aucun lien du site n'y pointe | Attention : `/pages/mentions-legales` est **publiée** et liée (cf. B10) | — |
| E7 | Sitemap | T-F §7 | ⚠️ normal | `/sitemap.xml` → **404** tant que la boutique est sous mot de passe | Re-vérifier après retrait du mot de passe | P2 |
| E8 | Vitesse de page > 65 | T-C p.7 | ⚠️ non mesuré | HTML d'une fiche : **300 113 octets** ; 43 images sur la fiche testée. Non mesurable proprement derrière le mot de passe | Passer PageSpeed après ouverture, avant la demande de review | P2 |
| E9 | Ordre de création GMC | T-F §7 ; SK principe 5 | ⚠️ à respecter | Boutique **non finie** (P0 ouverts). T-F §7 : « Never create GMC before the store is complete. Google can index incomplete pages » | **Ne pas créer le compte CSS/GMC maintenant.** Finir → publier → retirer le mot de passe → laisser indexer → créer le GMC → vérifier le domaine en DNS TXT (HTTPS) → recopier les policies mot pour mot → connecter le flux → demander la review | **P0** |

## F — Consentement, données personnelles, mesure

| # | Point de contrôle | Source | Statut | Preuve citée | Correction exacte | Prio |
|---|---|---|---|---|---|---|
| F1 | **Bandeau de consentement cookies** | KR §F « consentement et information adaptés au cadre applicable » ; FR art. 82 loi Informatique et Libertés | ❌ **BLOQUANT (N4)** | Rendu sur `/`, une fiche et le panier : `document.querySelector('#shopify-pc__banner')` → **`null`** ; `window.Shopify.customerPrivacy` → **`false`** (API absente) ; cookies déposés = `["localization","cart_currency","cart"]` — **pas de `_tracking_consent`**. Aucun mécanisme de recueil ni de retrait n'existe, alors que le pied de page propose un lien « Préférences en matière de cookies » qui tombe sur un 404 (E1) et que la politique cookies promet un choix (B12) | Activer **Shopify Customer Privacy / bannière de consentement** avec région UE, boutons « Tout accepter » **et** « Tout refuser » de même niveau (exigence CNIL), et Consent Mode v2 avant toute balise Google | **P0** |
| F2 | **Mesure de l'achat** | KR §E « Mesure achat » — critère de passage de la porte 5 | ❌ **BLOQUANT (N5)** | Rendu : `typeof gtag` = `"undefined"` · `window.dataLayer` = `false` · `window.ga` = `false` · `typeof fbq` = `"undefined"` · aucun script inline contenant `googletagmanager`/`AW-`/`G-XXXXXXXX` (`inlineGoogle: 0`) · hôtes de scripts = `maisonnoirmont.fr`, `shop.app`, `cdn.shopify.com` (+ 3 extensions du navigateur de Hakim). Seul `window.trekkie` (analytics interne Shopify) est présent | Installer la balise Google / GA4 via l'app Google & YouTube, brancher l'événement `purchase` **après succès uniquement**, `value` dynamique, `currency: EUR`, `transaction_id` unique et non personnel, déduplication, puis **passer une commande test** et réconcilier avec le back-office. Kraken : « Sans preuve achat : `REPARER_AVANT`, jamais "lancer pour voir" » | **P0 avant Ads** |
| F3 | Information RGPD complète | KR §F ; RGPD art. 13 | ⚠️ | Voir B8 : responsable du traitement ✅, transferts hors UE et CCT ✅, droits listés ✅ — **CNIL absente**, durées de conservation génériques, bases légales non explicitées | Voir B8 | **P1** |
| F4 | Inventaire des traceurs | KR §F | ⚠️ partiel | `/pages/politique-de-cookies` liste 6 cookies Shopify avec finalité et durée — correct **aujourd'hui**, mais deviendra faux dès l'ajout de la balise Google | Mettre à jour l'inventaire **en même temps** que F2 | **P1** |
| F5 | Newsletter : consentement | FR | ⚠️ | Pied de page : « Recevez nos nouveautés · Adresse email · send » — aucune case de consentement ni mention de finalité au rendu | Ajouter la mention de finalité et le lien vers la politique de confidentialité | P2 |
| F6 | robots.txt | — | ℹ️ information | `/robots.txt` est le fichier **par défaut de Shopify**. Il contient des lignes adressées aux agents IA qui recommandent d'installer un « skill » shop.app. **Contenu tiers, non demandé par Hakim : signalé, non suivi.** Aucune action | — | — |

---

# RÉCAPITULATIF PRIORISÉ

## P0 — bloquants absolus (aucun compte CSS/GMC avant)

| # | Action | Emplacement | Réf. |
|---|---|---|---|
| 1 | **Supprimer les 9 visuels de faux témoignages** des **37 fiches** (32 actives) | médias produit (`10977444430162-7.jpg`, `10977444495698-7.jpg`, `10977444528466-7.jpg`, `10977444561234-7.jpg`, `10977444594002-7.jpg`, `10977448624466-7.jpg`, `10977448690002-7.jpg`, `10977448722770-7.jpg`, `gmt-7.jpg`) | C1·C2·C3 |
| 2 | **Réécrire les 910 SKU AliExpress** en référence maison (dont 113 contenant « no logo ») | variantes produit — ils sortent dans le JSON-LD public | C4 |
| 3 | **Basculer l'e-mail de la boutique** sur `contact@maisonnoirmont.fr` | Réglages → Général (corrige aussi la politique de confidentialité rendue) | A2·B8 |
| 4 | **Activer le consentement cookies** (accepter / refuser au même niveau) | Réglages → Confidentialité des clients | F1·B12·E1 |
| 5 | **Installer la mesure d'achat** et prouver une commande de bout en bout | balise Google / GA4 + commande test | F2 |
| 6 | **Désactiver les sections d'avis fabriqués** + le badge « 4,8/5 · 1340 avis » **dans le thème qui sera publié** | `reviews_rXFabc`, `reviews_8P6xW3`, `reviews_badge_noirmont` | D1·D2 |
| 7 | **Aligner la politique de remboursement et les CGV art. 10** sur la FAQ (« portée à l'essai comprise ») | corps déjà prêts dans `backup-retours-2026-08-08/a-appliquer-par-hakim/` | B2 |
| 8 | **Nommer le médiateur de la consommation** et supprimer le marqueur `[À COMPLÉTER]` | CGV art. 17 (politique de caisse **et** page) | B5 |
| 9 | **Ne pas créer le GMC** avant que 1→8 soient en ligne et vérifiés au rendu | — | E9 |

## P1 — à faire avant le retrait du mot de passe

| # | Action | Réf. |
|---|---|---|
| 10 | Ajouter le téléphone cliquable au pied de page | A3 |
| 11 | Renseigner téléphone + raison sociale dans les réglages Shopify | A4 |
| 12 | Étoffer `/pages/contact` (société, adresse, e-mail, téléphone, horaires) | A5 |
| 13 | Désactiver le compte à rebours de `/password` — **dans les deux thèmes** | D5 |
| 14 | Corriger les pictos de paiement (retirer Google Pay, ajouter Amex + Klarna) — **dans les deux thèmes** | D6 |
| 15 | Vider « 2 000 clients satisfaits » et les `review_count: 123` | D3·D4 |
| 16 | Dédoublonner le pied de page légal, une seule URL de mentions légales | B10 |
| 17 | Compléter les mentions légales : forme juridique + RCS + SIREN | B7 |
| 18 | Ajouter la CNIL à la politique de confidentialité | B8·F3 |
| 19 | Retirer « 904L » des deux URL produit et de l'alt d'image (+ 301) | C8 |
| 20 | Afficher « TTC » sur la fiche et au panier | C20 |
| 21 | Porter « Montres squelette » à 5 produits ou la dépublier ; vider `frontpage` | C21 |
| 22 | Exclure la carte cadeau du flux Shopping | C24 |
| 23 | Mettre à jour l'inventaire des cookies après l'ajout de la balise Google | F4 |
| 24 | Réécrire la phrase « possibilité de choisir » de la politique cookies (ou installer le consentement) | B12 |

## P2 — propreté

25 · CGV art. 7 : retirer « Maestro », nommer le 4× — 26 · retirer le renvoi à la plateforme ODR (fermée depuis le 20/07/2025) — 27 · réserve « étanchéité non re-testée après montage » — 28 · trancher les 3 titres « Plongeuse vintage 42 » avant le flux — 29 · renommer « Présidentiel/Président » et retirer le tag `skx` — 30 · corriger les 3 compteurs faux des descriptions de collection — 31 · compléter les 16 fiches sans meta-description — 32 · mention RGPD sous le formulaire de contact et sous la newsletter — 33 · basculer la politique cookies en politique Shopify — 34 · ne pas activer `aviateur-acier-cadran-chiffres-arabes` (0 média) — 35 · noms de fichiers « chiffres arabes » → « 1-12 » — 36 · mesurer PageSpeed après ouverture — 37 · supprimer les menus brouillons `noirmont-desktop` / `noirmont-mobile`.

---

# Rappels de méthode pour l'exécution

- **Écrire sur le bon thème.** Le connecteur refuse d'écrire sur MAIN. Mais **diffe TRAVAIL contre MAIN avant de publier** :
  `templates/collection.json` fait 9 080 o en MAIN contre 16 088 o en TRAVAIL. Publier TRAVAIL tel quel changera aussi le
  template de collection. Le plus sûr : re-dupliquer MAIN puis ré-appliquer les correctifs sur la copie.
- **`themeFilesUpsert` renvoie `upsertedThemeFiles: []` sans erreur sur ce thème même quand l'écriture réussit.** Ne
  jamais conclure de ce retour : vérifier par **empreinte md5 du fichier distant** (`theme.files { checksumMd5 size }`).
- **Les fichiers de template sont du JSONC** : ils commencent par un commentaire `/* … */`. `json.loads` échoue si on ne
  le retire pas — c'est ce qui masque les flags `disabled` à un simple grep.
- `templates/product.json` fait ~75 Ko déséchappé : transporter le corps via `stagedUploadsCreate` + `body: { type: URL }`.
- **Contrôler au rendu, pas sur la réponse des mutations** : accordéons et descriptions sont servis repliés, absents de
  `innerText` mais présents dans le DOM.
- **Le JSON-LD est le meilleur révélateur du flux** : c'est là que les SKU AliExpress sont apparus. Le relire après chaque
  correction de données produit.
- Ordre imposé (T-F §7) : boutique finie → policies finalisées dans Shopify → produits propres → retrait du mot de passe →
  création GMC → vérification DNS TXT sur le HTTPS → policies recopiées **mot pour mot** dans GMC → flux → **une seule**
  demande de review.

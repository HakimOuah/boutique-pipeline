# À faire, Hakim : 8 actions, boutique publique

**15/08/2026.** Les 8 défauts publics relevés par l'audit du site live. Aucun n'est à ma main : ils vivent dans le **thème publié**, dans les **réglages** ou dans les **politiques**, que le connecteur ne peut pas écrire. Le 9e, le doublon de mentions légales, est déjà corrigé (voir `journal/2026-08-15-corrections-post-ouverture.md`).

Fais-les dans l'ordre. Compte 25 minutes.

> **Mise à jour du 15/08 au matin**, après contrôle du site live en anonyme (`journal/2026-08-15-purge-prix-barres.md` §5) :
> - ✅ **Point 3 fait aux deux tiers** — « Klarna » a disparu de tout le site. ⛔ Mais **« Paiement en 4 fois » subsiste dans le bandeau défilant des fiches**, un bloc que l'audit d'hier n'avait pas isolé. 1 minute.
> - ✅ **Point 5a fait** — « Prix TTC » est en place sous le prix des fiches. ⛔ **5b reste** : 0 occurrence sur l'accueil, le panier et les collections.
> - 🔄 **Point 4 réécrit** : tu demandais s'il valait mieux **activer** Google Pay. **Oui** — c'est une case à cocher dans Shopify Payments, effet immédiat, et ça ajoute un moyen de paiement au lieu d'en retirer un. Voir le **point 3 bis** pour la réponse complète, Klarna comprise (**non, pas maintenant** : candidature, instruction, acceptation non acquise à 0 vente).
> - ✅ **Hors de cette liste** : les 2 074 prix barrés qui dormaient sur les brouillons et les archivées sont **purgés** (T-50). Rien à faire de ton côté.

Liens directs :
- Personnalisateur : https://admin.shopify.com/store/v42pzp-h4/themes/205089014098/editor
- Réglages généraux : https://admin.shopify.com/store/v42pzp-h4/settings/general
- Politiques : https://admin.shopify.com/store/v42pzp-h4/settings/legal

---

## 1. Compléter les mentions légales (2 min)

C'est la moitié restante de la correction du doublon. J'ai dépublié `/pages/mentions-legales` (version du 13/08, la plus complète) et créé une redirection 301 vers `/policies/legal-notice`, qui est la seule que Shopify sert dans la caisse et que Merchant Center recopie. **Mais la politique porte encore la version du 10/08, à qui il manque trois choses.**

**Où** : Réglages → Politiques → **Mentions légales** → bouton `<>` **Afficher le code HTML**.

**Retirer** : tout le contenu du champ.

**Mettre** : le contenu intégral de `livraisons/mentions-legales-a-coller-2026-08-15.html` (ouvre le fichier, tout sélectionner, copier, coller).

Ce que ça rajoute par rapport à la version en ligne : le **délégué à la protection des données**, la mention de réclamation auprès de la **CNIL**, une section **5. Droit applicable**, et la date portée au 15 août 2026.

**Pourquoi** : art. 6 III LCEN (mentions de l'éditeur) et art. 13 RGPD ; et surtout, une seule version publiée au lieu de deux qui se contredisaient sur la date.

**Vérifier** : ouvrir https://maisonnoirmont.fr/policies/legal-notice, la page doit afficher **6 sections** et « Dernière mise à jour : 15 août 2026 ».

---

## 2. Basculer l'e-mail de la boutique (2 min)

**Où** : Réglages → Général, bloc du haut où figurent le nom et les e-mails de la boutique. **Deux champs d'e-mail** y sont à corriger (l'un est l'e-mail du compte, l'autre celui que voient les clients). Les deux valent aujourd'hui `contact.noirmont@gmail.com`.

**Retirer** : `contact.noirmont@gmail.com`

**Mettre** : `contact@maisonnoirmont.fr`

⚠️ **Avant de sauvegarder, vérifie que la boîte `.fr` reçoit bien.** C'est aussi l'adresse expéditrice des confirmations de commande : si elle ne relève pas, tu perds les commandes, pas juste un e-mail.

**Pourquoi** : cette adresse est injectée dans le JSON-LD `Organization` de **toutes** les pages du site. Le reste du site publie `contact@maisonnoirmont.fr` (57 occurrences) : deux adresses de contact différentes sur le même site est un motif de refus Merchant Center.

**Vérifier** : `curl -s https://maisonnoirmont.fr/ | grep -o '"email": *"[^"]*"'` doit renvoyer `contact@maisonnoirmont.fr`. Compter jusqu'à 15 minutes de cache CDN.

---

## 3. ✅ FAIT aux deux tiers — mais une promesse de 4× a survécu ailleurs (1 min)

> **Relevé le 15/08 au matin, en anonyme.** ✅ **Le bloc « Paiement fractionné » est bien masqué** :
> « Klarna » ne figure plus **nulle part** sur le site (0 occurrence sur 6 fiches, l'accueil, le panier,
> `/collections/all` et la FAQ), et le bloc n'existe plus dans `templates/product.json`. Merci.
>
> ⛔ **Mais il restait une seconde promesse de 4×, que l'audit d'hier n'avait pas isolée.** Le
> **bandeau défilant des fiches** — celui qui fait défiler « Livraison offerte en France » et
> « Garantie 12 mois » — affiche aussi **« Paiement en 4 fois »**, avec une icône de carte bancaire.
> C'est la même faute, dans un autre bloc, et elle est **publique**.
>
> **Où** : Personnalisateur → gabarit **Produit** → section **bandeau défilant** (`marquee_pdp`) →
> **3e élément, « Paiement en 4 fois »** → les trois points → **Masquer le bloc**. Puis **Enregistrer**.
>
> **Si tu veux garder trois éléments dans le bandeau**, remplace-le par une promesse **vraie
> aujourd'hui** : « Paiement sécurisé » ou « Retours sous 14 jours ».
>
> **Vérifier** : `curl -s https://maisonnoirmont.fr/products/voyageur-or-gmt-president | grep -c '4 fois'`
> doit renvoyer `0`.
>
> **Preuve que le 4× n'existe pas** : `/payments/config` donne **`offsiteConfigs: null`** — ce n'est pas
> un Klarna mal réglé, **aucun prestataire de paiement fractionné n'est installé**. Le 4× PayPal, lui,
> dépend de PayPal seul et ne se vérifie qu'en allant au bout d'une vraie caisse.

<details><summary>La consigne d'origine (15/08, avant ta correction)</summary>

**Décision de Hakim, 15/08 : on retire la mention Klarna ET le 4×.** Donc on masque le bloc entier, on ne se contente pas de vider un champ.

**La vérité du terrain** : `https://maisonnoirmont.fr/payments/config` liste ce qui est réellement actif à la caisse. Aujourd'hui : **Shop Pay, PayPal, Apple Pay**, cartes Visa / Mastercard / Amex / Maestro. **Klarna : zéro occurrence. Google Pay : `null`. Aucun paiement fractionné natif.**

**Où** : Personnalisateur → sélecteur de gabarit en haut → **Produits → Produit par défaut** → section **« Informations sur le produit »** → **6e bloc, « Paiement fractionné »**, juste sous le prix.

**Quoi** : les trois points du bloc → **Masquer le bloc**. Puis **Enregistrer**.

**Pourquoi** : annoncer un moyen de paiement qui n'existe pas est une pratique commerciale trompeuse (art. L. 121-2 du Code de la consommation) et le motif de refus n°1 de Merchant Center. Le bloc annonce un 4× dont aucun prestataire actif n'assure le service.

**Le jour où tu veux le remettre** : il faut d'abord que le 4× soit **réellement actif** (4X PayPal validé sur ton compte, ou Klarna après candidature et acceptation). Alors seulement on réaffiche le bloc, en nommant le seul prestataire réellement actif.

</details>

---

## 3 bis. Tu demandais : vaut-il mieux activer Klarna et Google Pay que retirer la mention ?

**Réponse courte : oui pour Google Pay, non pour Klarna.** Et c'est le **délai** qui fait la différence,
pas le principe.

**Google Pay s'active en une case, tout de suite** — c'est le point 4 ci-dessous, réécrit dans ce sens.
Pas de dossier, pas de tiers : c'est un portefeuille de **Shopify Payments**, qui est déjà actif chez
toi. Activer coûte le même temps que retirer le picto, et **ajoute** un moyen de paiement au lieu d'en
supprimer un.

**Klarna, non — pas maintenant.** Ce n'est pas une case à cocher : Klarna **instruit un dossier
marchand** (identité de la société, SIREN, coordonnées bancaires, modèle de vente, volumes attendus),
parce que c'est Klarna qui porte le risque de crédit à ta place. Compte des **jours à des semaines**, et
**l'acceptation n'est pas acquise** : une boutique à 0 vente, sans historique et en dropshipping, est
exactement le profil qui se fait examiner de près. Même logique pour Alma, Oney, Scalapay — et pour le
**4× PayPal**, que PayPal ouvre ou n'ouvre pas sur ton compte, sans que Shopify y puisse quoi que ce soit.

**Et pendant l'instruction du dossier ? On retire le texte d'abord.** C'est le point important, parce
que le texte est **public** tout du long :

- **Une candidature n'est pas une activation.** Entre le dépôt et la réponse, le site continue de
  promettre un service qui n'existe pas — à de vrais visiteurs, et à un examinateur Merchant Center qui
  peut passer n'importe quand.
- **Si Klarna refuse**, la fausse promesse reste en ligne indéfiniment, et personne ne se souvient
  d'aller la retirer.
- **Le coût est asymétrique** : la promesse se découvre **à la caisse**, au moment le plus cher du
  parcours. Un client venu pour le 4× qui ne le trouve pas ne revient pas.
- Annoncer un moyen de paiement inexistant relève de la **pratique commerciale trompeuse**
  (art. L. 121-2 du Code de la consommation), et c'est un motif de refus documenté côté Merchant Center.

**Donc l'ordre est : retirer le texte maintenant → candidater plus tard, après l'ouverture Merchant
Center, quand tu auras un historique à montrer → ne remettre le texte que le jour où tu auras vu le 4×
fonctionner dans une vraie caisse**, en nommant alors le prestataire réellement actif. Pas sur la foi
d'un e-mail d'accord : sur une caisse observée.

*Détail et relevés : `journal/2026-08-15-purge-prix-barres.md` §5.*

**Vérifier** : `curl -s https://maisonnoirmont.fr/products/montre-squelette-automatique-carree | grep -ciE "klarna|4 ×|4x"` doit renvoyer `0`.

---

## 4. Activer Google Pay — plutôt que retirer son picto (2 min)

**Réécrit le 15/08.** La consigne d'hier était de retirer le picto. **Activer est meilleur, et ne coûte
pas plus cher** : Google Pay est un **portefeuille de Shopify Payments**, et Shopify Payments est déjà
actif sur la boutique (`shopifyPaymentsEnabled: true`). C'est une case à cocher, **effet immédiat, aucun
tiers à convaincre** — exactement le même mécanisme qu'Apple Pay et Shop Pay, déjà cochés chez toi.
Le picto déjà affiché partout cesse d'être un mensonge, et tu gagnes un moyen de paiement.

**4a — Activer (le geste utile).**
**Où** : Réglages → **Paiements** → **Shopify Payments** → **Gérer** → section **Portefeuilles**.
**Quoi** : cocher **Google Pay**. Enregistrer.
**Vérifier** : `curl -s https://maisonnoirmont.fr/payments/config | grep -o '"googlePayConfig":[^,]*'` ne
doit plus renvoyer `null`.

**4b — Puis fiabiliser l'affichage des icônes (le geste durable).**
**Où** : Personnalisateur → icône **engrenage « Paramètres du thème »** → onglet **« Icônes de paiement »**
(19e sur 21, juste après « Liste de souhaits », juste avant « Réseaux sociaux »).
**Retirer** : la coche de **« Afficher manuellement les icônes »** (cochée aujourd'hui, c'est elle qui
force les pictos en dur).
**Pourquoi quand même** : une fois décochée, le thème affiche **les moyens de paiement réellement
configurés**. L'affichage suivra tout seul chaque ajout ou retrait, et **ça ne se redégradera plus
jamais**. Ça corrige aussi un écart en sens inverse relevé le 15/08 : **Amex et Maestro sont acceptés
sans être affichés**.

⚠️ **Si tu ne fais pas 4a**, alors fais 4b seul : ne laisse pas le picto d'un moyen de paiement
indisponible. Mais 4a est le bon choix.

---

## 5. Ajouter la mention « TTC » — ✅ 5a est fait, il reste 5b (2 min)

> **Relevé le 15/08 au matin.** ✅ **5a est fait** : « Prix TTC. Livraison offerte en France
> métropolitaine. » est bien en place sous le prix des fiches (`sections.main` → bloc `text_BY7DbP`).
> ⛔ **5b reste à faire** : « TTC » a **0 occurrence** sur l'accueil, le panier et `/collections/all`,
> qui affichent tous des prix. C'est le pied de page qui les couvrirait tous d'un coup.

### 5a. Sur la fiche produit — ✅ FAIT

**Où** : Personnalisateur → **Produits → Produit par défaut** → section **« Informations sur le produit »** → **Ajouter un bloc** → **Texte**, puis le glisser **juste sous le bloc « Prix »** (5e position), au-dessus de « Paiement fractionné ».

**Mettre**, dans le champ Texte :

```
Prix TTC. Livraison offerte en France métropolitaine.
```

### 5b. Dans le pied de page

**Où** : Personnalisateur → tout en bas de la page → section **« Pied de page »** → **1er bloc** (le groupe qui porte le logo) → le **bloc de texte** sous le logo.

**Retirer** : rien.

**Mettre** : ajouter cette phrase à la fin du texte existant, après l'adresse e-mail :

```
Tous nos prix sont affichés en euros, toutes taxes comprises.
```

**Pourquoi** : art. L. 112-1 du Code de la consommation, le prix de vente doit être annoncé toutes taxes comprises. Les prix **sont** TTC (`shop.taxesIncluded = true`), c'est uniquement la mention qui manque. Le pied de page est le seul endroit qui couvre **l'accueil, les collections et le panier** d'un seul geste — aujourd'hui ils affichent des prix sans aucune mention de taxe.

**Vérifier** : `curl -s https://maisonnoirmont.fr/ | grep -c TTC` doit renvoyer au moins `1` (il renvoie `0` aujourd'hui), et la fiche produit au moins `2`.

---

## 6. Aligner la garantie du pied de page sur le contrat (2 min)

**Où** : Personnalisateur → bas de page → section **« Réassurances »** → **3e colonne**, celle qui porte l'icône bouclier et le titre **« Garantie 12 mois »** → le **bloc de texte sous le titre**.

**Retirer** :

```
Mouvement, couronne, aiguilles : on répare ou on remplace, simplement.
```

**Mettre** :

```
Sur le mouvement, pendant 12 mois : on répare ou on remplace.
```

**Pourquoi** : la politique de remboursement §7 et l'article 10 des CGV limitent la garantie commerciale au **mouvement interne** et excluent explicitement le bracelet, le verre et le boîtier. Le pied de page promettait la couronne et les aiguilles, donc plus que le contrat. Promettre plus que ce qu'on tient est une garantie commerciale non conforme (art. L. 217-21).

**Vérifier** : `curl -s https://maisonnoirmont.fr/ | grep -c couronne` ne doit plus renvoyer d'occurrence dans le pied de page (celles qui restent sont des `alt` de photos produit).

---

## 7. Retirer « une pièce unique, à votre image » de l'accueil (2 min)

**Où** : Personnalisateur → **Accueil** → **5e section**, celle titrée **« Composez la vôtre »** (elle vient juste après le bandeau d'avis et avant « Les collections ») → le triptyque de puces → **3e puce**, celle qui commence par **« Vous signez »**.

**Retirer** :

```
Vous signez
une pièce unique, à votre image
```

**Mettre** :

```
Vous signez
la référence de notre catalogue qui correspond à vos réponses
```

(garder « Vous signez » en gras et le retour à la ligne, comme aujourd'hui)

**Pourquoi** : la FAQ dit l'inverse, et elle a raison : « Le configurateur ne fabrique rien à vos spécifications : il vous montre la référence de notre catalogue qui correspond à vos réponses. » Le nouveau texte est repris mot pour mot de la FAQ. Une allégation de fabrication sur mesure sur un catalogue standard rouvrirait en plus l'exception au droit de rétractation de l'art. L. 221-28.

**Vérifier** : `curl -s https://maisonnoirmont.fr/ | grep -c 'pièce unique'` doit renvoyer `0`.

---

## 8. Ajouter l'URL du médiateur CM2C aux CGV (3 min)

**Où** : Réglages → Politiques → **Conditions générales de vente** → bouton `<>` **Afficher le code HTML** → **Article 15 — Réclamations et médiation**.

**Retirer** :

```
CM2C, 14 rue Saint Jean, 75017 Paris, Tél : 01 89 47 00 14.
```

⚠️ Retirer aussi la balise `<meta charset="utf-8">` collée juste devant ce texte dans le code HTML : c'est un résidu de copier-coller.

**Mettre** :

```
CM2C, 14 rue Saint Jean, 75017 Paris, téléphone 01 89 47 00 14, site internet : ADRESSE.
```

⚠️ **Remplace `ADRESSE` par l'URL exacte reprise de ton attestation d'adhésion CM2C. Ne la devine pas, ne la cherche pas sur un moteur** : une URL de médiateur fausse est pire qu'une URL absente.

Pendant que tu y es, corrige l'en-tête de la page : `Version en vigueur au 10 août 2026` devient la date du jour de ton édition.

**Pourquoi** : l'art. R. 616-1 du Code de la consommation impose d'indiquer **l'adresse du site internet** du médiateur, pas seulement son nom et son adresse postale.

**Vérifier** : `curl -s https://maisonnoirmont.fr/policies/terms-of-sale | grep -c 'cm2c'` doit renvoyer au moins `1`.

---

## Après les 8

Relance l'audit complet avant de demander la revue Merchant Center. Et ne touche à **aucun brouillon** avant T-50 : **2 074 prix barrés** dorment sur les 86 fiches non actives et les 10 archivées, le premier brouillon activé les met en ligne d'un coup.

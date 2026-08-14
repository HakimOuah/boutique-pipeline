# À faire, Hakim : 8 actions, boutique publique

**15/08/2026.** Les 8 défauts publics relevés par l'audit du site live. Aucun n'est à ma main : ils vivent dans le **thème publié**, dans les **réglages** ou dans les **politiques**, que le connecteur ne peut pas écrire. Le 9e, le doublon de mentions légales, est déjà corrigé (voir `journal/2026-08-15-corrections-post-ouverture.md`).

Fais-les dans l'ordre. Compte 25 minutes.

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

## 3. Retirer « ou Klarna » des 96 fiches (3 min)

**D'abord la vérité du terrain** : `https://maisonnoirmont.fr/payments/config` dit exactement ce qui est actif à la caisse. Aujourd'hui : **Shop Pay, PayPal, Apple Pay** et les cartes **Visa / Mastercard / Amex / Maestro**. **Klarna : zéro occurrence. Google Pay : `null`. Aucun paiement fractionné natif Shopify.**

**Où** : Personnalisateur → sélecteur de gabarit en haut → **Produits → Produit par défaut** → section **« Informations sur le produit »** → **6e bloc, « Paiement fractionné »**, juste sous le prix.

**Retirer** : dans le champ **« Prestataire 2 »**, la valeur `Klarna`.

**Mettre** : rien. Laisser le champ **vide**. La ligne deviendra `Ou 4 × 69,75 € avec PayPal`.

⚠️ **Et vérifie que « Paiement en 4X » est bien actif dans ton compte PayPal.** PayPal est actif comme moyen de paiement, mais le 4× est un produit PayPal à part que `/payments/config` ne peut pas prouver. **S'il n'est pas actif : masque le bloc entier** (les trois points du bloc → **Masquer le bloc**) plutôt que de laisser une promesse invérifiable.

**Pourquoi** : annoncer un moyen de paiement qui n'existe pas est une pratique commerciale trompeuse (art. L. 121-2 du Code de la consommation), et c'est le motif de refus n°1 de Merchant Center.

**Vérifier** : `curl -s https://maisonnoirmont.fr/products/montre-squelette-automatique-carree | grep -c Klarna` doit renvoyer `0`.

---

## 4. Retirer le picto Google Pay du pied de page (1 min)

**Où** : Personnalisateur → icône **engrenage « Paramètres du thème »** dans la colonne de gauche → faire défiler jusqu'à l'onglet **« Icônes de paiement »** (19e sur 21, juste après « Liste de souhaits », juste avant « Réseaux sociaux »).

**Retirer** : la coche de la case **« Afficher manuellement les icônes »** (elle est cochée aujourd'hui, c'est elle qui force les pictos en dur).

**Mettre** : rien. Une fois la case décochée, le thème affiche automatiquement les moyens de paiement réellement configurés sur la boutique. Google Pay disparaît seul, et ça ne se redégradera plus jamais quand tu ajouteras ou retireras un moyen de paiement.

**Pourquoi** : `googlePayConfig` vaut `null`, Google Pay n'est pas disponible à la caisse. Le pied de page en affiche pourtant le picto sur toutes les pages. Même règle que le point 3.

**Vérifier** : `curl -s https://maisonnoirmont.fr/ | grep -c 'pi-google_pay'` doit renvoyer `0`.

---

## 5. Ajouter la mention « TTC » (4 min)

Deux endroits, deux gestes.

### 5a. Sur la fiche produit

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

**Pourquoi** : art. L. 112-1 du Code de la consommation, le prix de vente doit être annoncé toutes taxes comprises. Les prix **sont** TTC (`shop.taxesIncluded = true`), c'est uniquement la mention qui manquait : `TTC` a zéro occurrence sur l'ensemble du site.

**Vérifier** : `curl -s https://maisonnoirmont.fr/products/montre-squelette-automatique-carree | grep -c TTC` doit renvoyer au moins `2`.

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

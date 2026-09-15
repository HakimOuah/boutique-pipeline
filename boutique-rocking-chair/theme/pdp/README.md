# Page produit Bercelou (thème FullStack, copie 206567702873)

Un seul modèle `templates/product.json` pour les 29 fiches. Tout le contenu variable vient de la description produit, découpée en Liquid par `snippets/bercelou-fiche.liquid` :

| Partie | Source dans la description |
|---|---|
| Bénéfices (colonne d'achat) | `<ul>` d'introduction |
| Livraison estimée + montage | `<h2>Livraison</h2>` : « en X à Y jours ouvrés. » puis la phrase suivante |
| Accordéons | `<h2>Caractéristiques</h2>`, `<h2>Dimensions</h2>`, `<h2>Entretien</h2>` + retours 14 jours |
| Dans le détail | accroche `<p><strong>` + chaque `<h3>` avec une image de la galerie |
| Avant de commander | cotes, montage, délai, retour |
| FAQ du modèle | `<h2>FAQ</h2>`, questions en `<strong>` |

Une partie absente de la fiche n'affiche rien. Changer le texte d'une fiche change la page, sans toucher au thème.

Paiement fractionné : affiché seulement si `shop.enabled_payment_types` contient `klarna` ou `paypal` (vérifié actif le 15/09/2026).
Icônes de paiement : `force_icons_display` passé à `false` dans `settings_data.json` pour n'afficher que les moyens réellement actifs.

`product.json` ici est la sortie de `build_product.py` ; la version en ligne est la même, sans quelques réglages égaux aux valeurs par défaut.

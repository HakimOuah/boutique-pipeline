# Kit Shopify portable Dropilot

Ce dossier contient des composants indépendants de Horizon :

- `dp-purchase-support.liquid` : paiement fractionné, bénéfices avec icônes, puis livraison ;
- `dp-reassurance.liquid` : preuves et conditions vérifiées ;
- `dp-faq.liquid` : FAQ accessible ;
- `dp-icon.liquid` : icônes SVG internes.

Copier les fichiers dans les dossiers correspondants du thème cible, puis fusionner les clés
`dropilot` des fichiers de langue au lieu d’écraser les locales existantes.

Le bloc d’aide à l’achat respecte l’ordre de référence : paiement, bénéfices, livraison. Les quatre
bénéfices de l’osmoseur sont fournis comme preset et doivent être remplacés pour les autres produits.

Les prestataires de paiement, délais, garanties, bénéfices et affirmations doivent refléter la
configuration et les preuves réelles de la boutique.


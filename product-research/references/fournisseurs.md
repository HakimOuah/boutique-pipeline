## Étape 6 — Validation fournisseur

Pour chaque produit en shortlist :

- fournisseur AliExpress exact vérifié par page ou réponse API traçable ;
- URL AliExpress ;
- prix produit ;
- prix livré ;
- nombre de commandes AliExpress ;
- note produit / étoiles AliExpress ;
- notation vendeur AliExpress ;
- pays d'expédition ;
- délai ;
- expédié depuis Europe : oui/non ;
- variantes ;
- stock ;
- qualité images ;
- avis ;
- historique vendeur ;
- présence de fournisseur backup ;
- risque de marque tierce / watermark ;
- possibilité de facture HT / TVA intracom.

Classer le risque fournisseur :

- Faible : fournisseur crédible, note >= 4,5, commandes suffisantes, expédition Europe ou délai
  France court, stock, backup, images exploitables.
- Moyen : fournisseur correct mais délai/stock/images/commandes à surveiller.
- Fort : fournisseur fragile, note < 4,5, peu de ventes, délais longs, specs floues, pas de backup
  ou fournisseur AliExpress non confirmé.

Chargement après PASS_PREQUALIFICATION uniquement. Note 4,5 et qualité des avis restent des repères de risque, pas une preuve de livraison ni de conformité. Identifier le SKU, la variante, la destination, la date et les champs réellement observés. Une information de liste/titre ne vaut pas vérification du produit exact. Une absence de donnée reste MANQUANT. Ne pas substituer un fournisseur hors AliExpress ; ne pas contacter, commander ni publier dans cette mission de recherche.

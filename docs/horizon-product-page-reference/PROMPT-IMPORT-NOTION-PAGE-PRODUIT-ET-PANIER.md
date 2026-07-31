# Prompt à envoyer à Claude — import Notion

```text
Tu dois importer et organiser dans Notion toute la référence Shopify Horizon de Bonum Vitae : page produit ET panier.

OBJECTIF

Créer dans Notion une source unique, structurée et réutilisable pour les prochaines boutiques Shopify. Au moment de construire une nouvelle boutique, un agent devra pouvoir retrouver rapidement l’ordre des sections, les réglages, les textes modèles, le code Liquid, les dépendances, les données à remplacer et les contrôles QA.

Tu peux importer les éléments codés en dur. Ne les supprime pas : conserve-les comme exemples ou valeurs du modèle Bonum Vitae, mais marque-les clairement « À personnaliser pour chaque boutique ».

SOURCES PRINCIPALES

1. Page produit :
/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/HORIZON-PAGE-PRODUIT-NOTION.md

2. Panier :
/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/cart/HORIZON-PANIER-NOTION.md

DOSSIER COMPLET À LIRE

/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/

Il contient notamment :

- les modèles JSON de page produit ;
- les sections et blocs Liquid ;
- les Custom Liquid isolés ;
- le modèle JSON de page panier ;
- le tiroir panier complet ;
- les composants produits et récapitulatif du panier ;
- les réglages courants et le schéma du thème ;
- une version isolée de la bannière de livraison et de l’upsell panier.

MISSION

1. Lis entièrement les deux documents principaux avant de structurer Notion.
2. Lis les fichiers sources liés depuis ces documents.
3. Ne modifie aucun fichier Shopify et ne publie rien sur la boutique.
4. Crée une page principale Notion nommée « Modèle Shopify Horizon — Page produit et panier ».
5. Crée au minimum les sous-pages ou bases suivantes :
   - Vue d’ensemble et ordre CRO
   - Architecture page produit
   - Architecture panier
   - Bibliothèque de blocs Liquid
   - Données boutique à personnaliser
   - Données produit à fournir
   - Preuves et conformité
   - Avis clients
   - Upsells et recommandations
   - Checklist de construction
   - Checklist QA
   - Historique des versions
6. Pour chaque section ou bloc, enregistre :
   - nom fonctionnel ;
   - emplacement ;
   - type : natif Horizon, app, Custom Liquid ou code personnalisé ;
   - fichier source ;
   - code complet ou lien vers le fichier ;
   - dépendances ;
   - réglages ;
   - valeurs codées en dur ;
   - valeurs dynamiques ;
   - éléments à remplacer ;
   - statut de portabilité ;
   - contrôles QA.
7. Pour les éléments codés en dur, conserve leur valeur actuelle puis ajoute les champs :
   - « À personnaliser » = Oui ;
   - « Valeur pour la nouvelle boutique » ;
   - « Preuve requise » ;
   - « Date de validation » ;
   - « Responsable ».
8. Sépare strictement :
   - Observé dans le thème ;
   - Valeur codée en dur ;
   - Donnée manquante ;
   - Hypothèse ;
   - Décision à prendre.

PAGE PRODUIT

9. Reproduis l’ordre exact des sections et blocs décrit dans la documentation.
10. Conserve séparément chaque code Liquid : note, avis, paiement, bénéfices, livraison, réassurance et boutons d’achat.
11. Signale que les notes, nombres d’avis, garanties, délais, certifications, coordonnées, médias et chemins CDN ne sont pas des valeurs universelles.
12. Ne considère aucun avis comme publiable sans source réelle.
13. Ne copie pas un template JSON Horizon dans un autre thème sans lire le schéma du thème cible.

PANIER

14. Reproduis séparément l’architecture du tiroir et celle de la page panier.
15. Distingue les ajouts Bonum Vitae des fonctions natives Horizon.
16. Pour la bannière « Livraison offerte en France », conserve le texte et les couleurs comme modèle, puis marque la politique, les zones et le seuil comme informations à vérifier.
17. Pour l’upsell du tiroir, enregistre les quatre handles actuels, leur ordre, la limite de deux produits, l’exclusion des articles déjà au panier et le choix de la première variante disponible.
18. Marque les handles, couleurs, textes et règles de variante comme « À personnaliser pour chaque boutique ».
19. Documente les dépendances Horizon : cart, all_products, product-form-component, JavaScript du formulaire produit, identifiant de section et variables CSS.
20. Documente les réglages actuels : panier tiroir, ouverture automatique, note, code promotionnel, paiements échelonnés, paiements accélérés et affichage de la devise.
21. Documente aussi la recommandation de la page panier : collection all, quatre produits, quatre colonnes ordinateur, deux colonnes mobile et bouton « Tout voir ».
22. Signale le risque de redondance entre l’upsell du tiroir et la recommandation de la page panier.

RÈGLES DE PORTABILITÉ

23. Conserve le code complet comme référence, mais ne le présente jamais comme universel ou prêt à coller dans n’importe quel thème.
24. Pour une nouvelle boutique, reconstruis d’abord avec les composants natifs du thème cible.
25. Les IDs Horizon, app blocks, handles, chemins de médias, coordonnées, politiques et données de preuve doivent être remplacés ou revalidés.
26. Si une donnée manque, écris « Manquant » au lieu de l’inventer.
27. Lie chaque promesse commerciale à une preuve ou une politique vérifiable.

SORTIE ATTENDUE

À la fin, donne-moi :

1. le lien de la page Notion principale ;
2. la liste des bases et sous-pages créées ;
3. le nombre de blocs page produit importés ;
4. le nombre de composants panier importés ;
5. la liste des valeurs codées en dur enregistrées ;
6. la liste des données encore manquantes ;
7. les risques de migration identifiés ;
8. une checklist courte pour construire la prochaine boutique.

Ne résume pas seulement les documents : transforme-les en une base Notion exploitable, reliée et durable.
```

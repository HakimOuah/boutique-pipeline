# Switch fournisseur du gun 2-en-1 via DSers « Replace Product » — 21/07/2026 (soir)

Autorisé par Hakim (« Tu peux aller sur Dsers et faire la modif toi-même ? Je suis déjà connecté »).

## Objectif
Re-sourcer le produit Shopify « Tufting gun 2-en-1 Cut & Loop » (gid://shopify/Product/15466410213761) de la fiche XMSJ 1005008473485705 (132,69–148,50 €, vendeur 90,5 %) vers la fiche **Urban Corners 1005009254054515** (gun seul ≈ 79,44 € expédié France — fiche trouvée par Hakim, la même que la base du kit / commande test).

## Ce qui s'est passé
1. Flux DSers « Replace Product » exécuté dans le Chrome de Hakim (Mes Produits → carte gun → ⋮ → Replace Product → URL de la fiche UC → Remplacer).
2. **Piège découvert : le bouton « REMPLACER PRODUIT » de la modale committe immédiatement** — DSers a remplacé le produit et poussé vers Shopify les **28 variantes** de la fiche UC (7 options × 4 entrepôts Italy/france/spain/Germany) avec des prix issus de sa pricing rule (79,63–129,47 €), écrasant les 6 variantes à 169 €. Le panneau d'édition qui s'ouvre ensuite (titre, variantes, images) est post-commit.
3. Réparation immédiate via l'API Admin Shopify (mutations validées, 0 userError) :
   - `productVariantsBulkDelete` : 26 variantes parasites supprimées.
   - Conservées : **Rose** (SKU `14:350686#pink;200007763:201336342`) et **Bleu** (SKU `14:350850#blue;200007763:201336342`) — expédition France, les SKU DSers d'origine sont intacts donc le mapping DSers reste valide.
   - `productOptionsDelete` : option « Ships From » supprimée.
   - `productOptionUpdate` : « Color » → « Couleur », « Pink » → « Rose », « Blue » → « Bleu ».
   - `productVariantsBulkUpdate` : prix remis à **169,00 €** sur les 2 variantes.
   - `inventorySetQuantities` : stock remis à 100/100 (DSers avait poussé 0 ; emplacement `dsers-fulfillment-service`).

## État final vérifié
- Shopify : produit ACTIVE, titre FR conservé, 2 variantes Rose/Bleu à 169 €, option unique « Couleur », stock 100/100, description Tuftéo intacte.
- DSers : carte « Tufting gun 2-en-1 Cut & Loop », **Cost $92,89** (≈ 79,4 € rendu France — cohérent avec le 79,44 € relevé par Hakim), Prix pour FR, Price €169.00.
- Images produit : les 9 images de la fiche UC ont remplacé les images XMSJ (temporaire — les images Codex les remplaceront).

## Points de vigilance
1. **DSers garde les 28 variantes en interne** (Shopify n'en a que 2). Le mapping des 2 SKU conservés est valide ; DSers peut afficher un avertissement de variantes manquantes — sans conséquence pour les commandes Rose/Bleu.
2. **Stock entrepôts UE à vérifier** : lors du push, DSers a inscrit 0 en stock sur quasi toutes les variantes (seuls SET A/Germany=5 et Blue/Germany=1 avaient une valeur). Si l'entrepôt France de la fiche UC est réellement à sec sur le gun seul, les commandes partiraient d'un autre entrepôt ou échoueraient → à contrôler à la première commande (ou en vérifiant la fiche UC).
3. La pricing rule DSers est active (« Prix pour FR ») : elle s'applique au push/replace. Ne pas refaire de Replace sans s'attendre à devoir re-vérifier les prix.
4. L'ancienne fiche XMSJ (limite 3/commande, vendeur 90,5 %) n'est plus référencée — réserve levée.

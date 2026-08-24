# AliExpress — preuves exactes, lecture seule

**Observation :** 2026-08-24 UTC
**Canal :** passerelle Open Platform en lecture seule, destination France
**Interdits respectés :** aucun panier, achat, message vendeur ou connexion.

## Déshumidificateur 12 L

- `product_id` : `1005012520990312`
- `sku_id` : `12000058614668358`
- Variante : `White 12L`
- Origine : France
- Stock observé : 14
- Prix TTC observé : 116,52 EUR
- Fret France : gratuit
- Route : La Poste, 2–8 jours ; alternatives observées 2–10 jours
- Produit : 1 vente, note 0, 0 évaluation exposée par l'API
- Boutique : Flayu002 Store, communication 4,1 ; description 4,0 ; expédition 4,3
- `MANQUANT` : déclaration CE/GPSR exploitable, responsable UE, puissance, niveau sonore, fluide, consommation, SAV, deuxième fournisseur exact.

Conclusion fournisseur : logistique attractive, confiance **C / forte réserve**. La recherche accessible `12L dehumidifier EU plug` n'a pas livré de second équivalent exact dans les premiers résultats triés ; cela décrit cette passe, pas l'ensemble d'AliExpress.

## Couverture lestée adulte — preuve révisée le 2026-08-25

### Fiche Good Nite apportée par Hakim

- [Fiche canonique](https://fr.aliexpress.com/item/1005010144250762.html), `product_id` : `1005010144250762`.
- Titre API : couverture Good Nite 8 kg pour adulte.
- Boutique HT Direct Store : communication 4,7 ; description 4,7 ; expédition 4,8.
- `sku_id` encodé dans l'URL apportée : `12000051329035763`, **125 × 180 cm, 6 kg**, Allemagne, stock 9, 48,26 EUR TTC.
- `sku_id` sélectionné dans la capture : `12000051329035765`, **150 × 200 cm, 8 kg**, Allemagne, stock 25, 59,75 EUR TTC dans l'API.
- Fret France 8 kg : DHL gratuit, 3–8 jours ; DPD gratuit, 3–9 jours.
- Capture consommateur 8 kg : 49,23 EUR TTC promotionnel, 4,9/5, 28 avis, 122 vendus, expédié d'Allemagne, livraison gratuite.
- Open Platform : 22 ventes, note 0, 0 évaluation exposée.

Le prix écran est conservé comme snapshot promotionnel ; le coût API de **59,75 EUR rendu** sert de base prudente. Le conflit de compteurs entre les deux surfaces est explicite. Cette fiche prouve l'économie d'un assortiment adulte 6/8 kg, pas un 7 kg exact.

### Premier fournisseur, désormais écarté

- `product_id` : `1005011748184966`.
- L'ancien prix de 82,99 EUR correspondait à une petite variante **80 × 100 cm, 3,2 kg**, pas au produit adulte 7 kg.
- `sku_id` adulte : `12000056423247539`, ivoire 120 × 150 cm, 7 kg.
- Origine Chine, stock 9, produit 142,99 EUR TTC, fret FedEx 212,61 EUR, coût rendu **355,60 EUR**.

Conclusion révisée : cette première fiche est un **mauvais fournisseur à exclure**, pas une preuve d'impossibilité de la catégorie. Les recherches API bornées n'ont pas encore prouvé de deuxième fournisseur exact comparable ; les vignettes de recherche affichant un petit prix ne suffisent pas sans SKU, poids, origine et fret.

## Studio créateur

### Ring light historique

- `product_id` : `1005008918211887`
- 125 ventes observées ; note/évaluations exposées à 0 par l'API
- Boutique : 4,7 / 4,6 / 4,8, origine Chine
- Aucune variante expédiée de France.
- Variante `200cm C` depuis Israël : rupture.
- Variante `DESK-Stand C` depuis Israël : livraison France indisponible.
- L'ancien prix de 32,19 EUR correspondait à `ring light F` depuis le Mexique, pas à un kit studio complet France.

### Micro cravate plausible, famille isolée

- `product_id` : `1005007432812040`
- `sku_id` : `12000040733691120`
- Variante : `2in1 For Type-C`
- Stock : 104
- Produit : 6,49 EUR TTC
- Fret : 1,99 EUR ; 3–10 jours
- Coût rendu : 8,48 EUR
- Ventes : 10 000+
- Boutique : 4,6 / 4,6 / 4,7

Conclusion univers : une seule preuve produit sur une seule famille ne prouve ni le kit, ni quatre familles majeures, ni une profondeur de 200 références.

## Arts de la table bois

- `product_id` : `1005010089175364`
- `sku_id` : `12000051099286373`
- Variante exposée : propriétés dimensionnelles incohérentes dans le retour (`350x250x25mm` → `390x275x25mm`)
- Stock observé : 3
- Prix TTC : 39,39 EUR
- Fret Chine → France : 1,99 EUR, 3–10 jours
- Coût rendu : **41,38 EUR**
- Produit : 115 ventes, note 0, 0 évaluation exposée
- Boutique Stone's Store : communication 4,8 ; description 5,0 ; expédition 4,8

Les recherches `acacia serving board large`, `charcuterie board set wood`, `wood serving tray` et `wood placemat set` ont surtout remonté des produits hors intention ou accessoires. Aucun deuxième fournisseur exact par famille majeure n'a été prouvé.

## Limite technique

Une première exécution parallèle a fait terminer le VPS avec `ssh_exit=137`. Le health check est resté sain ; les appels ont ensuite été sérialisés. Les absences de résultats ci-dessus sont donc des résultats de passes accessibles et bornées, jamais une preuve globale d'inexistence.

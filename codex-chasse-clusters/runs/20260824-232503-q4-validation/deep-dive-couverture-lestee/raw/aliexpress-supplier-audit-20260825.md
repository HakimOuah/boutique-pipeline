# Audit fournisseurs AliExpress — couverture lestée

**Observation :** 2026-08-25
**Canal :** Open Platform via passerelle VPS en lecture seule
**Destination :** France
**Interdits respectés :** aucun panier, achat, message ou connexion.

## Résultat compact

| Fiche | Variante exacte | Coût rendu / logistique | Statut |
|---|---|---|---|
| `1005010144250762` — HT Direct Store / Good Nite | 4 kg 125x150 ; 6 kg 125x180 ; 8 kg 150x200, départ Allemagne | 42,51 ; 48,26 ; 59,75 EUR TTC ; 8 kg DHL/DPD gratuit, 3–9 jours | `PRODUCT`, seul cœur économiquement plausible ; conformité/qualité manquantes |
| `1005011748184966` | 7 kg 120x150, ivoire, départ Chine | 142,99 + 212,61 = 355,60 EUR | `PRODUCT`, exact mais `PRIX_INCOMPATIBLE` |
| `1005007361914018` — JAGDAMBE | Raschel 200x230, 6 kg | 125,69 + 1,99 = 127,68 EUR ; Chine, 28–37 jours | `IRRELEVANT` pour une couverture à microbilles ; simple couverture lourde d'hiver |
| `1005008363847208` — EPPE | Raschel 200x230, 5 kg | 132,99 EUR, fret standard gratuit ; Chine, 7–14 jours | `IRRELEVANT` pour le cœur ; 0 vente API, simple couverture lourde |

## Fiche exploitable actuelle

`1005010144250762` offre trois variantes adultes cohérentes :

- 4 kg : SKU `12000051329035762`, stock 8, 42,51 EUR TTC ;
- 6 kg : SKU `12000051329035763`, stock 9, 48,26 EUR TTC ;
- 8 kg : SKU `12000051329035765`, stock 25, 59,75 EUR TTC.

La boutique expose 4,7 en communication et description, 4,8 en expédition. L'API expose 22 ventes et aucune note/évaluation ; l'écran consommateur observé exposait 122 vendus, 28 avis et 4,9/5. Ce conflit reste non résolu.

## Couverture fournisseur réellement obtenue

- 4 fiches exactes contrôlées.
- 2 seulement sont des couvertures lestées au sens produit recherché.
- 1 seule est économiquement plausible.
- 0 backup adulte 6–8 kg comparable et expédié d'Europe prouvé.
- 0 document matière/Oeko-Tex/GPSR exact obtenu.

Les recherches API `weighted blanket adult 8kg`, `gravity blanket`, `couverture lestée adulte`, `heavy weighted blanket`, `Gewichtsdecke 8kg` et `glass beads blanket` ont majoritairement retourné des produits hors intention. Plusieurs appels plus étroits ont renvoyé `EXCEPTION_TEXT_SEARCH_FOR_DS`. Une recherche accessible mais polluée ne vaut pas preuve d'absence globale ; elle ne permet pas non plus d'inventer des fournisseurs.

## Catalogue sourceable sans extrapolation

À ce stade, AliExpress prouve seulement un cœur de gamme :

- 4 kg / 125x150 cm ;
- 6 kg / 125x180 cm ;
- 8 kg / 150x200 cm ;
- un seul coloris gris ;
- un seul fournisseur viable.

Les poids 5/7/9/10/11/12 kg, les grandes tailles, les housses compatibles, le lin/coton documenté, les produits enfant et les accessoires lestés restent `MANQUANT` en fournisseur exact.

## Gate fournisseur

Verdict : `AUCUN_BACKUP_EXACT`. La niche ne peut pas recevoir `TECHNICAL_PASS` tant que les points suivants ne sont pas prouvés :

1. deuxième fiche 6–8 kg, coût rendu UE comparable et vendeur crédible ;
2. composition textile et remplissage exacts ;
3. confinement des billes, coutures, tolérance de poids et instructions de lavage ;
4. opérateur économique UE, traçabilité, analyse de risques et avertissements GPSR ;
5. conditions de retour d'un colis lourd et garantie réelle.

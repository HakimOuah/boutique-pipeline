# Rapport lot D — poufs et repose-pieds (Bercelou, 16/09/2026)

19 fiches rédigées (`<handle>.md`) avec leur plan d’application (`<handle>.plan.json`). Rien n’a été écrit dans Shopify.

- Prix médian : **109 €** (de 49 € à 369 €).
- Source des prix : 6 comparables, 11 en grille, 2 au plancher.
- Variantes : 39 gardées, 6 supprimées. L’option « Ships From » est supprimée partout.
- Délai affiché partout : 3 à 10 jours ouvrés, car tous les produits sont des meubles expédiés depuis l’UE.
- Comparables indépendants utilisés : ChicPouf (chicpouf.com) et Beaumont Concept (beaumont-concept.com). Relevé du 16/09/2026 via l’API Shopify publique `products.json`.

| Handle | PID | Prix | Coût | Ratio | Source prix | Variantes gardées / supprimées | Alertes principales |
|---|---|---|---|---|---|---|---|
| pouf-coffre-rond-bouclette-blanc | 1005010764533309 | 89 € | 52.84 € | 1.68 | plancher | 1 / 0 | Prix au plancher (89 €) = comparable Beaumont ; même modèle à 56,90 € chez E.Leclerc |
| pouf-coffre-rond-velours-cotele | 1005013146637098 | 49 € | 25.04 € | 1.96 | grille | 3 / 0 | Montage et structure contradictoires chez le fournisseur ; prix bas (49 €) |
| lot-2-poufs-coffres-gigognes-velours-blanc | 1005012230993913 | 69 € | 37.44 € | 1.84 | grille | 1 / 0 | Logo WOLTU sur 2 images ; lot de 2 annoncé clairement |
| pouf-coffre-sherpa-creme | 1005012995378687 | 109 € | 57.25 € | 1.90 | comparable | 1 / 0 | Texte fournisseur parle aussi de chenille ; même châssis que le pouf chenille |
| pouf-coffre-chenille-beige | 1005013107014989 | 109 € | 62.69 € | 1.74 | comparable | 1 / 0 | « Ottoman » renommé Beige ; montage contradictoire ; stock 10 |
| pouf-macrame-coton-ecru | 1005011961058094 | 209 € | 73.69 € | 2.84 | comparable | 2 / 0 | Gamme vidaXL (vérifier logos) ; colis déclaré 1 kg |
| pouf-jute-tresse-raye-naturel | 1005011960778981 | 179 € | 75.12 € | 2.38 | comparable | 2 / 0 | Pas de photo par coloris ; cotes contradictoires (45×30 retenu) ; comparable Beaumont à 129 € |
| pouf-rond-velours-cotele-moelleux | 1005013078459287 | 69 € | 38.94 € | 1.77 | grille | 4 / 0 | Texte fournisseur dit « carré » ; stocks 2 à 10 ; hausse de prix possible |
| pouf-poire-geant-convertible-velours | 1005012832541364 | 229 € | 60.28 € | 3.80 | comparable | 7 / 0 | Codes 01–07 identifiés ; velours côtelé ou lisse à confirmer |
| pouf-geant-rond-velours-cotele | 1005013164392205 | 209 € | 85.63 € | 2.44 | comparable | 4 / 0 | Description vide, cotes lues sur images |
| fauteuil-pouf-fausse-fourrure-gris-clair | 1005013019531945 | 169 € | 100.32 € | 1.68 | plancher | 1 / 0 | Plancher 169 € > comparable ChicPouf 147,90 € ; profondeur contradictoire |
| fauteuil-pouf-fourrure-dossier-arrondi | 1005012854842679 | 369 € | 205.38 € | 1.80 | grille | 2 / 4 | Coloris/tailles incohérents : seul le grand format gardé (à valider) |
| fauteuil-pouf-bouclette-sherpa-matelasse | 1005012649367497 | 319 € | 178.09 € | 1.79 | grille | 2 / 1 | Silhouette d’un design célèbre (aucun nom cité) ; hauteur 75 ou 79 cm ; vert en rupture |
| pouf-exterieur-acacia-coussin-anthracite | 1005012800637836 | 149 € | 81.85 € | 1.82 | grille | 1 / 0 | Texte fournisseur générique ; cotes lues sur image |
| repose-pieds-vintage-lin-beige | 1005012903717125 | 169 € | 91.29 € | 1.85 | grille | 1 / 0 | « Pivotant/réglable » annoncés mais invisibles sur photos : non repris |
| repose-pieds-banquette-polaire-grise | 1005010757484840 | 79 € | 41.72 € | 1.89 | grille | 1 / 0 | Seule option « Ships From » (aucune pastille) |
| petit-repose-pieds-effet-lin-marron-clair | 1005010757482866 | 59 € | 34.01 € | 1.73 | grille | 1 / 0 | Très petit format (27 cm) ; seule option « Ships From » |
| repose-pieds-cube-lin-creme-poche | 1005012689086194 | 49 € | 26.53 € | 1.85 | grille | 1 / 0 | WHITE renommé Crème ; plaquette commerciale à exclure |
| repose-pieds-carre-velours-cotele | 1005013087155309 | 79 € | 43.94 € | 1.80 | grille | 3 / 1 | Photos « Dark green » / « Dark gray » inversées chez le fournisseur ; beige en rupture |

## Collections proposées
- `pouf` : 15 fiches, soit toutes sauf les 4 repose-pieds à pieds.
- `pouf-poire` : pouf géant convertible, pouf géant rond, les 3 fauteuils poufs.
- `pouf-exterieur` : pouf en acacia.
- `repose-pieds` : les 8 poufs coffres et poufs souples, ainsi que les 5 repose-pieds.
- `accessoires-rocking-chair` : les 4 repose-pieds à pieds (vintage, polaire, petit, cube à poche).

## Points à trancher par Hakim
1. **Fauteuil pouf à dossier arrondi (1005012854842679)** : petit et moyen formats supprimés, car leurs cotes ne sont pas données et leurs coloris sont incohérents. Seul le grand format est gardé : ses cotes 123 × 111 × 75 cm sont corroborées par le colis et par une annonce du marché. Prix de 369 €.
2. **Photos à contrôler avant publication** :
   - logo WOLTU sur le lot de 2 poufs ;
   - photos inversées vert et gris sur le repose-pieds carré ;
   - aucune photo par coloris pour le pouf en jute ;
   - produits vidaXL (macramé, jute, extérieur) et HOMCOM : vérifier l’absence de logo.
3. **Prix au plancher au-dessus du comparable** :
   - fauteuil pouf fausse fourrure : 169 € contre 147,90 € ;
   - pouf coffre bouclette : 89 €, soit le prix du comparable, alors que le même modèle est à 56,90 € chez E.Leclerc.
4. **Prix de grille bas ou marge de hausse** :
   - pouf coffre velours côtelé à 49 € et repose-pieds cube à 49 € ;
   - poufs velours côtelé rond (69 €) et carré (79 €), alors que les boutiques indépendantes vendent des poufs voisins entre 189 et 209 €.
5. **Promesses fournisseur non reprises** :
   - fonction « pivotant et réglable » du repose-pieds vintage, invisible sur les photos ;
   - « chenille » sur le pouf sherpa ;
   - « carré » et « fausse fourrure » sur le pouf rond velours côtelé.
6. **Doublons proches** : le pouf coffre sherpa et le pouf coffre chenille partagent le même châssis de 38 × 45 cm. Garder les deux ou n’en garder qu’un.
7. **Bleu roi** du pouf géant convertible : coloris gardé (7 coloris), un peu vif pour la DA.

Aucune allégation de norme ou de certification. Aucune marque tierce, aucun lieu d’expédition dans les textes : relecture par grep passée.

# Rattachement des visuels actifs — 10/08/2026

## Périmètre et méthode

- Cible opérationnelle active : 298 médias, après abandon documenté de deux fausses vues de carte cadeau et de quatre faux médias de remontoirs.
- Point de départ vérifié : 66 médias livrés et rattachés.
- Chaque nouveau média est ajouté à la galerie sans retirer la photo principale ni les sources existantes, puis affecté aux variantes exactes avec `productVariantAppendMedia`.
- Une requête indépendante relit ensuite les variantes et leur média. Aucun lot réservé, rejeté ou bloqué n'est rattaché.
- Rollback : utiliser `productVariantDetachMedia` pour détacher le média des variantes, puis retirer le média produit par son GID uniquement si une suppression est expressément autorisée.

## Bracelet caoutchouc gaufré

Produit : `gid://shopify/Product/10980388536658` — `bracelet-caoutchouc-gaufre` — statut relu `ACTIVE`. La photo principale `noirmont-waffle-1.jpg` est restée inchangée.

### Boucle argentée — trois nouveaux médias approuvés

| Apparence | Fichier local | Média Shopify | Variantes affectées |
|---|---|---|---|
| Jaune | `bracelet-caoutchouc-gaufre-v-yellow-silver-buckle.jpg` | `gid://shopify/MediaImage/59904502825298` | `54098044453202`, `54098044682578` |
| Bleu clair | `bracelet-caoutchouc-gaufre-v-light-blue-silver.jpg` | `gid://shopify/MediaImage/59904502858066` | `54098044715346`, `54098044944722` |
| Blanc | `bracelet-caoutchouc-gaufre-v-white-silver-buckle.jpg` | `gid://shopify/MediaImage/59904964362578` | `54098043928914`, `54098044158290` |

Le blanc argenté initial a été sauvegardé dans `rejected/`, puis régénéré depuis la source fournisseur exacte. La seconde QA valide la vérité produit et l'alignement du nouveau rendu sur les gabarits jaune et bleu clair. La relecture Shopify confirme que ses deux variantes 20 et 22 mm portent uniquement le nouveau média ; la photo principale reste inchangée.

### Boucle dorée — neuf médias approuvés

| Apparence | Média Shopify |
|---|---|
| Vert kaki | `gid://shopify/MediaImage/59904552632658` |
| Blanc | `gid://shopify/MediaImage/59904552665426` |
| Orange | `gid://shopify/MediaImage/59904552698194` |
| Jaune | `gid://shopify/MediaImage/59904552730962` |
| Bleu clair | `gid://shopify/MediaImage/59904552763730` |
| Bleu profond | `gid://shopify/MediaImage/59904552796498` |
| Brun | `gid://shopify/MediaImage/59904552829266` |
| Noir | `gid://shopify/MediaImage/59904552862034` |
| Rouge | `gid://shopify/MediaImage/59904552894802` |

Chacun est affecté aux deux variantes 20 et 22 mm dont le fragment fournisseur correspond exactement. La relecture Shopify confirme 18 variantes, un média attendu par variante et zéro erreur de mutation.

### Boucle noire — neuf médias approuvés

| Apparence | Média Shopify | Variantes affectées |
|---|---|---|
| Vert kaki | `gid://shopify/MediaImage/59904636911954` | `54098042683730`, `54098042716498` |
| Blanc | `gid://shopify/MediaImage/59904636944722` | `54098044092754`, `54098044125522` |
| Orange | `gid://shopify/MediaImage/59904636977490` | `54098044354898`, `54098044387666` |
| Jaune | `gid://shopify/MediaImage/59904637010258` | `54098044617042`, `54098044649810` |
| Bleu clair | `gid://shopify/MediaImage/59904637043026` | `54098044879186`, `54098044911954` |
| Bleu profond | `gid://shopify/MediaImage/59904637075794` | `54098043044178`, `54098043076946` |
| Brun | `gid://shopify/MediaImage/59904637108562` | `54098043306322`, `54098043339090` |
| Noir | `gid://shopify/MediaImage/59904637141330` | `54098043568466`, `54098043601234` |
| Rouge | `gid://shopify/MediaImage/59904637174098` | `54098043830610`, `54098043863378` |

La QA source → rendu valide les neuf. Le jaune final est propre après trois essais avec marquages parasites correctement rejetés et isolés. La relecture Shopify confirme les 18 associations exactes, sans modification du statut, de la photo principale, des prix, stocks, SKU ou options.

### Boucle or rose — neuf médias approuvés

| Apparence | Média Shopify | Variantes affectées |
|---|---|---|
| Vert kaki | `gid://shopify/MediaImage/59904697499986` | `54098043961682`, `54098043994450` |
| Blanc | `gid://shopify/MediaImage/59904697532754` | `54098044223826`, `54098044256594` |
| Orange | `gid://shopify/MediaImage/59904697565522` | `54098044485970`, `54098044518738` |
| Jaune | `gid://shopify/MediaImage/59904697598290` | `54098044748114`, `54098044780882` |
| Bleu clair | `gid://shopify/MediaImage/59904697631058` | `54098042913106`, `54098042945874` |
| Bleu profond | `gid://shopify/MediaImage/59904697663826` | `54098043175250`, `54098043208018` |
| Brun | `gid://shopify/MediaImage/59904697696594` | `54098043437394`, `54098043470162` |
| Noir | `gid://shopify/MediaImage/59904697729362` | `54098043699538`, `54098043732306` |
| Rouge | `gid://shopify/MediaImage/59904697762130` | `54098042782034`, `54098042814802` |

Les neuf rendus passent le contrôle individuel source → rendu et la planche de lot : boucle uniformément or rose, teinte exacte, géométrie et cadrage homogènes, aucun texte ou parasite. La relecture Shopify confirme les 18 associations exactes et un seul média attendu par variante.

## Explorateur à chiffres 3-6-9

Produit : `gid://shopify/Product/10988849299794` — `montre-acier-chiffres-3-6-9-explorateur` — statut relu `ACTIVE`. La photo principale `montre-acier-chiffres-3-6-9-explorateur-face.jpg` est restée inchangée.

| Apparence | Média Shopify | Variantes affectées |
|---|---|---:|
| Green1 | `gid://shopify/MediaImage/59904750354770` | 8 |
| Orange1 | `gid://shopify/MediaImage/59904750387538` | 8 |
| Black1 | `gid://shopify/MediaImage/59904750420306` | 8 |
| Red1 | `gid://shopify/MediaImage/59904750453074` | 8 |
| White1, cadran argenté et détails dorés | `gid://shopify/MediaImage/59904750485842` | 8 |

Les cinq passent la vérité produit et la tolérance de gabarit mesurée. `Blue1` est exclu du rattachement : son produit est vrai, mais son échelle est supérieure de 8,1 % à la référence Green1 ; une reprise ciblée remplace ce même slot.

Les 40 variantes avaient déjà toutes le même média générique `gid://shopify/MediaImage/59740542992722` affecté. Shopify interdit deux associations de média par variante. Après un premier append refusé atomiquement, l'association générique a donc été détachée des 40 variantes, sans retirer ce média de la galerie produit, puis remplacée par les cinq nouveaux médias. La relecture confirme 40/40 associations exactes, huit variantes par média et aucun rattachement résiduel ou manquant.

Rollback : détacher les cinq nouveaux médias des 40 variantes, puis leur réaffecter `gid://shopify/MediaImage/59740542992722`. Ne pas supprimer les nouveaux médias de la galerie sans autorisation distincte.

## Éclaireur Acier — Field à chiffres 1-12

Produit : `gid://shopify/Product/10988849234258` — `montre-field-acier-cadran-chiffres-1-12` — statut relu `ACTIVE`. La photo principale `montre-field-acier-cadran-chiffres-arabes-face.jpg` est restée inchangée.

| Apparence | Média Shopify | Variantes affectées |
|---|---|---:|
| Black 8 sterile | `gid://shopify/MediaImage/59904807502162` | 6 |
| Black 3 sterile | `gid://shopify/MediaImage/59904807534930` | 6 |
| Black 4 sterile | `gid://shopify/MediaImage/59904807567698` | 6 |
| Black 7 sterile | `gid://shopify/MediaImage/59904807600466` | 6 |
| Black 5 sterile | `gid://shopify/MediaImage/59904807633234` | 6 |
| Green sterile | `gid://shopify/MediaImage/59904807666002` | 6 |
| Black 6 sterile, échelle minutes 5-55 | `gid://shopify/MediaImage/59904807698770` | 6 |
| Black 2 sterile | `gid://shopify/MediaImage/59904807731538` | 6 |
| Silver sterile | `gid://shopify/MediaImage/59904807764306` | 6 |
| Blue sterile | `gid://shopify/MediaImage/59904807797074` | 6 |

Les dix passent la comparaison source → rendu : chiffres extérieurs 1-12 complets et droits, couronne 13-24 uniquement sur les cadrans qui la possèdent, échelle minutes exacte sur Black 6, aucun mot, lettre, logo ou filigrane. La planche durable `qa/planche-p3-variantes.jpg` a été recréée mécaniquement depuis les dix JPEG finaux en 3700 × 1480, soit 740 px par vignette.

Les 60 variantes avaient le même média générique `gid://shopify/MediaImage/59740542959954` affecté. Son association a été remplacée, sans retirer le média de la galerie, par les dix médias exacts. La relecture confirme 60/60 associations, six variantes par média, zéro manque et zéro média inattendu.

Rollback : détacher les dix nouveaux médias des 60 variantes, puis leur réaffecter `gid://shopify/MediaImage/59740542959954`.

## Éclaireur Bronze — Field à chiffres 1-12

Produit : `gid://shopify/Product/10988849267026` — `montre-field-bronze-cadran-chiffres-1-12` — statut relu `ACTIVE`. La photo principale `montre-field-bronze-cadran-chiffres-arabes-face.jpg` est restée inchangée.

| Apparence | Média Shopify | Variantes affectées |
|---|---|---:|
| Blue sterile | `gid://shopify/MediaImage/59904867696978` | 2 |
| Black D sterile | `gid://shopify/MediaImage/59904867729746` | 2 |
| Black B sterile | `gid://shopify/MediaImage/59904867762514` | 2 |
| Silver sterile | `gid://shopify/MediaImage/59904867795282` | 2 |
| Black A sterile | `gid://shopify/MediaImage/59904867828050` | 2 |
| Green B sterile | `gid://shopify/MediaImage/59904867860818` | 2 |
| White sterile | `gid://shopify/MediaImage/59904867893586` | 2 |

Les sept passent la comparaison source → rendu et la planche 4 × 2. Les chiffres 1-12, la couronne 13-24, la date, la minuterie, les aiguilles, la patine et le bracelet correspondent à chaque source exacte. Les essais défectueux de Black D, Black A et Green B ont été isolés dans `rejected/`; leurs finales passent.

`Black C sterile` est **NE PAS RATTACHER**. Sa seule source exacte est un crop du cadran ; ni le boîtier, ni la couronne, ni le bracelet complet du rendu ne sont prouvables. L'audit API officiel de l'article `1005009879577159` n'a trouvé aucune autre image SKU complète. Ses deux variantes conservent donc le média générique `gid://shopify/MediaImage/59740542861650` et le JPEG généré reste seulement local.

Sur les 16 variantes ciblées, la relecture confirme 14 associations nouvelles exactes et les deux associations génériques attendues de Black C. Rollback : détacher les sept nouveaux médias des 14 variantes, puis leur réaffecter `gid://shopify/MediaImage/59740542861650`.

## Compteur après cette tranche

- Nouveaux médias actifs approuvés et rattachés : 52.
- Total opérationnel : **118 / 298**.
- Ouverts : **180**, dont les lots encore en production et les emplacements bloqués documentés.

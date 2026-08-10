# Rattachement des visuels actifs — 10/08/2026

## Périmètre et méthode

- Cible opérationnelle active : 298 médias, après abandon documenté de deux fausses vues de carte cadeau et de quatre faux médias de remontoirs.
- Point de départ vérifié : 66 médias livrés et rattachés.
- Chaque nouveau média est ajouté à la galerie sans retirer la photo principale ni les sources existantes, puis affecté aux variantes exactes avec `productVariantAppendMedia`.
- Une requête indépendante relit ensuite les variantes et leur média. Aucun lot réservé, rejeté ou bloqué n'est rattaché.
- Rollback : utiliser `productVariantDetachMedia` pour détacher le média des variantes, puis retirer le média produit par son GID uniquement si une suppression est expressément autorisée.

## Bracelet caoutchouc gaufré

Produit : `gid://shopify/Product/10980388536658` — `bracelet-caoutchouc-gaufre` — statut relu `ACTIVE`. La photo principale `noirmont-waffle-1.jpg` est restée inchangée.

### Boucle argentée — deux nouveaux médias approuvés

| Apparence | Fichier local | Média Shopify | Variantes affectées |
|---|---|---|---|
| Jaune | `bracelet-caoutchouc-gaufre-v-yellow-silver-buckle.jpg` | `gid://shopify/MediaImage/59904502825298` | `54098044453202`, `54098044682578` |
| Bleu clair | `bracelet-caoutchouc-gaufre-v-light-blue-silver.jpg` | `gid://shopify/MediaImage/59904502858066` | `54098044715346`, `54098044944722` |

Le blanc argenté initial est exclu du rattachement : vérité produit conforme, mais cadrage et échelle réservés par la QA de lot. Une reprise ciblée remplace ce slot ; elle ne crée pas un besoin supplémentaire.

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

## Compteur après cette tranche

- Nouveaux médias actifs approuvés et rattachés : 29.
- Total opérationnel : **95 / 298**.
- Ouverts : **203**, dont les lots encore en production et les emplacements bloqués documentés.

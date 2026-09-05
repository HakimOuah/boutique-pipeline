# Contrôle concurrents — Luna Maison

Contrôle réalisé le **5 septembre 2026**, uniquement sur les trois familles demandées. `RESULTAT.md` est la seule pièce locale lue.

## Bornes respectées

- **6/6 recherches Web** consommées : deux requêtes de découverte par famille.
- **8 pages distinctes au maximum** consultées ou tentées, sans API payante, achat ni contact.
- Maximum de deux URL produit par famille dans le relevé ci-dessous.
- Les résultats organiques ne sont pas comptés comme annonces. Aucune capture explicitement marquée « Annonce », « Sponsorisé » ou « Ad » n'est disponible : **Search NON VERIFIE** pour les trois familles.

## Pistolet de massage

| URL contrôlée | Prix / produit exact | Shopify dans HTML ou `products/...json` | Délai affiché | Ressemblance fournisseur — non prouvée |
|---|---|---|---|---|
| [Approche Sport — Pistolet de massage Recuptech](https://approchesport.com/products/pistolet-de-massage-recuptech) | Non revalidable : la page renvoie vers `/lander`, sans prix ni fiche exploitable | Non démontré | Non relevé | Nom de marque et produit impossibles à comparer dans la page accessible |
| [ReboostCare — produit 6 vitesses](https://www.reboostcare.fr/products/appareil-electrique-portatif-rechargeable-6-embouts?variant=56093640819074) | **149,00 € affichés** dans le catalogue : « Pistolet de massage silencieux – 6 vitesses & grande autonomie » | Non démontré : la page produit a échoué au chargement public ; aucun marqueur Shopify exploitable relevé | **7–12 jours ouvrés** au total, dont 1–2 jours ouvrés de traitement, affichés sur la [page boutique](https://www.reboostcare.fr/) | Possible produit générique / private label : slug technique très générique et fiche orientée « 6 vitesses / embouts » ; **aucune preuve de fournisseur commun** |

Observation : ReboostCare affiche aussi France métropolitaine, livraison incluse et un SIREN sur sa page boutique. Cela constitue un signal de petit marchand, pas une preuve d'indépendance économique ni de sourcing. Le prix de 149 € est un prix affiché dans la page consultée, pas une validation au checkout.

**Décision famille : INCERTAIN.** Le produit ReboostCare passe le ticket et présente une ressemblance générique plausible, mais l'accès technique produit et Search restent non vérifiés. Poursuite éventuelle du dossier seulement, **sans GO**.

## Extracteur de jus

| URL contrôlée | Prix / produit exact | Shopify dans HTML ou `products/...json` | Délai affiché | Ressemblance fournisseur — non prouvée |
|---|---|---|---|---|
| [Kuvings France — AUTO6 Bleu Navy](https://shop.kuvings.fr/802-extracteur-de-jus-auto6-bleu-navy-kuvings.html) | **399 € affichés** : « Extracteur de jus Kuvings AUTO6 Bleu Navy » | **Non** : le HTML de la boutique expose des marqueurs de structure PrestaShop (`index.php?controller=product`, thème `classic_warmcook`) | Aucun délai chiffré relevé ; seulement des transporteurs en pied de page | Non pertinent pour le critère générique : produit et boutique officiellement centrés sur la marque Kuvings |
| [Kuvings France — AUTO8 Silver](https://shop.kuvings.fr/798-extracteur-jus-auto8-silver-kuvings.html) | **499 € affichés** : « Extracteur de jus Kuvings AUTO8 Silver » | **Non** — même constat structurel PrestaShop | Aucun délai chiffré relevé | Non pertinent pour le critère générique : marque et gamme explicites |

La page [ExtracteurDeJus.com — acheter un extracteur](https://www.extracteurdejus.com/acheter-extracteur-jus/) est un comparateur / contenu éditorial, pas une offre indépendante produit exploitable. Les résultats organiques montrent surtout une boutique officielle Kuvings et des enseignes ou marques établies ; aucun petit marchand générique dans la tranche n'est documenté dans cette passe.

**Décision famille : REJETER** pour cette présélection. Le ticket existe, mais les deux offres contrôlées sont brandées/officielles et ne démontrent pas l'accès à un petit marchand proposant du générique. Cela ne constitue pas une mesure de domination publicitaire.

## Ventilateur de plafond

| Source produit / marchand | Prix / produit exact | Shopify dans HTML ou `products/...json` | Délai affiché | Ressemblance fournisseur — non prouvée |
|---|---|---|---|---|
| [Venalysa](https://venalysa.com/) — page boutique indexée | **359 € affichés** : « Ventilateur de plafond – Bois massif – Teinte naturelle | ZANO » | Non démontré : l'accès direct HTML et l'endpoint standard public n'ont pas été exploitables (502 / échec TLS) | Non relevé | Noms de modèles et rédaction assez génériques : ressemblance possible, **pas une preuve** |
| [Venalysa](https://venalysa.com/) — page boutique indexée | **359 € affichés** : « Ventilateur de plafond – Éclairage LED – Bois naturel | NEMA » | Non démontré, même réserve | Non relevé | Même réserve ; aucune comparaison fournisseur effectuée |

Signal marchand complémentaire dans les résultats organiques : [Ventelux — à propos](https://ventelux.fr/pages/a-propos) se présente comme une SASU spécialisée, indique sélectionner auprès de fabricants/fournisseurs et expédier directement aux clients, et mentionne Shopify Payments. Aucun produit précis avec prix et délai n'a été contrôlé sur cette page. [Boutica-Design](https://www.ventilateur-plafond.net/boutica-design.html) et [GUIBB](https://www.guibb.fr/) apparaissent également comme spécialistes organiques.

**Décision famille : INCERTAIN.** Il existe des signaux de spécialistes et des prix dans la tranche, mais les URL produit, Shopify, le délai et le sourcing ne sont pas suffisamment prouvés. La présence organique de [Castorama](https://www.castorama.fr/ventilateur-de-plafond/cat_id_0003205.cat) confirme une enseigne visible dans la recherche ; elle ne permet pas d'inférer une domination publicitaire.

## Grandes enseignes / marques visibles dans les résultats

- **Pistolet :** [Decathlon](https://www.decathlon.fr/tous-les-sports/fitness-cardio-training/pistolet-de-massage) apparaît organiquement.
- **Extracteur :** [Boulanger](https://www.boulanger.com/c/extracteur-de-jus) et [Bosch](https://www.bosch-home.fr/fr/category/preparation-culinaire/extracteurs-de-jus-centrifugeuses-et-presse-agrumes) apparaissent organiquement ; Kuvings apparaît via sa boutique de marque.
- **Ventilateur :** [Castorama](https://www.castorama.fr/ventilateur-de-plafond/cat_id_0003205.cat) apparaît organiquement.

Ces présences sont des observations de SERP, pas des captures d'annonces et pas une estimation de part de marché ou de domination publicitaire.

## Décision finale

| Famille | Décision |
|---|---|
| Pistolet de massage | **INCERTAIN** — poursuivre seulement avec preuve produit/technique ultérieure ; pas de GO |
| Extracteur de jus | **REJETER** pour la shortlist générique indépendante contrôlée |
| Ventilateur de plafond | **INCERTAIN** — spécialistes visibles, preuve produit insuffisante ; pas de GO |

**Aucun GO n'est validé.** Contrôle arrêté conformément à la mission.

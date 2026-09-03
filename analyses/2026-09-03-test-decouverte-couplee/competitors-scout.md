# Scout public — offres de quatre shops Top Scaling

Relevé : 3 septembre 2026. Travail de repérage pour la mesure express, sans verdict de préqualification ni sourcing. Règles relues : `CLAUDE.md`, `AGENTS.md`, `../CLAUDE.md`, critères canoniques PRODUIT PUR.

## Origine des pistes

La vue TrendTrack Top Scaling Home/Tech, observée par l'orchestrateur, a fourni ces pistes :

| Shop | Visites estimées transmises | Annonces Meta transmises | Offre examinée |
|---|---:|---:|---|
| toolsons.com | 210 K | 247 | MultiTool Set |
| wildbeartools.com | 89 K | 318 | Offset Extension 2.0 |
| helloholie.com | 81 K | 182 | 100% Gel Rider Cushion |
| ntt-sonority.com | 84 K | 470 | SonoVo Grip / intro knot |

Ces valeurs justifient l'inspection des offres. La présence dans une vue de scaling ne remplace pas une série datée montrant la progression ; les dépenses, ventes, marges et produits contribuant au trafic restent inconnus dans cette sous-analyse.

## Deux offres à mesurer

### 1. Rallonge déportée de clé à cliquet pour accès difficile

**OBSERVÉ.** WildBear vend [Offset Extension 2.0](https://wildbeartools.com/products/extension-wrench) à **79 USD**. La fiche décrit une transmission par chaîne, une entrée 3/8 pouce et un couple maximal de 72 Nm. Elle cite aussi la réparation domestique et les particuliers entretenant leur véhicule : le positionnement professionnel ne suffit donc pas à classer ce produit technique-pro.

**HYPOTHÈSE Search.** « rallonge clé à cliquet », « rallonge déportée cliquet », « clé déportée », « outil boulon inaccessible ». Séparer les rallonges droites, les clés coudées et les outils véritablement comparables. Le besoin est exprimable ; la formulation commerciale française exacte reste à préciser par la SERP.

**MANQUANT.** Prix français comparable, demande, CPC, saisonnalité et économie. Le JSON-LD indique `InStock` pour la variante `55813813371211`, alors qu'un bloc dupliqué contient « Sold out » : disponibilité non confirmée. Le tarif américain paraît compatible avec l'ordre de grandeur visé, sans valider un prix TTC livré en France.

### 2. Coussin gel de selle moto pour trajets prolongés

**OBSERVÉ.** [Holie 100% Gel Rider Cushion](https://helloholie.com/products/100-gel-rider-cushion) est une sur-assise de **moto**, distincte de la selle vélo. La donnée structurée de la PDP donne **74 USD**, variante `64094768529757`, `InStock`. La fiche prévoit une fixation par sangles et plusieurs types de motos ; la marque propose aussi un format passager.

**HYPOTHÈSE Search.** « coussin selle moto », « coussin gel moto », « surselle confort moto », « mal aux fesses moto ». Séparer confort moto, coussins médicaux d'assise, selles complètes et vélo. Une offre conducteur/passager existe conceptuellement, mais son panier français n'est pas validé.

**MANQUANT.** Prix français comparable, demande, CPC, saisonnalité Q4, fournisseurs et marge. Les promesses de soulagement et d'efficacité figurant sur la PDP sont des affirmations marchandes, pas des résultats indépendamment vérifiés ; ne pas les reprendre comme arguments acquis.

## Une réserve, sans forcer une troisième sélection

### 3. Coffret compact de tournevis à cliquet en T

**OBSERVÉ.** [Toolsons MultiTool Set](https://toolsons.com/products/multitool-set) affiche **159 RON**, confirmé par le JSON-LD, et `OutOfStock`. L'offre contient un manche en T à cliquet, des embouts et un étui. Deux kits coûtent 286,20 RON et trois 405,45 RON sur la PDP.

**HYPOTHÈSE Search.** « tournevis à cliquet », « coffret tournevis cliquet », « tournevis en T ». Le besoin bricolage particulier est clair. « Outil multifonction » serait trop ambigu : électroportatif, couteaux et pinces peuvent polluer le cluster.

**RÉSERVE.** La sonde ne démontre pas de produit cœur ou de panier naturel à 50–400 EUR. Plusieurs exemplaires identiques vendus ensemble ne prouvent pas un besoin récurrent d'achat multiple. À garder en réserve de prix, sans inventer un bundle premium pour satisfaire le plancher. Aucun taux de change ni prix français n'est déduit ici.

## Piste écartée du périmètre avant mesure

**NTT SonoVo Grip / intro knot : technique-pro.** Les pages primaires [SonoVo GEAR](https://ntt-sonority.com/pages/sonovo-gear) et [Grip](https://ntt-sonority.com/products/sonovo-grip) ciblent explicitement les équipes terrain, le travail en environnement bruyant et la communication PTT. [L'annonce officielle du 15 juillet 2026](https://ntt-sonority.com/blogs/news/260715) indique Grip à **16 000 JPY hors taxe**, fourniture prévue début octobre 2026. La vente passe par une demande de contact. Ce modèle ne constitue pas l'offre B2C recherchée ici. Une idée grand public différente inspirée par l'audio ouvert exigerait un nouveau périmètre explicite ; le trafic de cette société ne validerait pas cette autre offre.

## Anti-doublon et suite

Recherche dans `registre-candidats.md` : noms des quatre marchands, multitool/multi-outil, cliquet, tournevis, coffret outil, rallonge/déporté, coussin moto/gel/assise, selle moto, anti-escarre, coccyx, oreillette/intercom/PTT. **Aucun candidat correspondant retrouvé.** Cela établit l'absence de correspondance dans ce registre consulté, pas une garantie universelle d'inédit. Les coussins de corps déjà étudiés ne constituent pas la même offre que le confort de selle moto.

Proposition : mesurer d'abord les deux besoins précis, éventuellement une petite sonde du coffret si le budget de la salve le permet. La demande et l'économie françaises décideront de la suite ; les scores complets et les états de préqualification seront établis par l'orchestrateur après mesure.

### Accès et preuve de prix

Les PDP publiques ont été ouvertes avec l'outil web. Le prix dynamique Holie, absent du texte extrait, a été obtenu dans le JSON-LD du HTML public de la même PDP, sans connexion ni mutation. L'ouverture des URL `.js` par l'outil web a échoué ; aucun résultat de ces URL n'a été utilisé. Les schémas des autres PDP ont servi à recouper les devises et à relever la contradiction de disponibilité WildBear. Aucun appel DataForSEO, achat, ajout au panier, contact fournisseur ou modification de compte n'a été réalisé par cette sous-analyse.

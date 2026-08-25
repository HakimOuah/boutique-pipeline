# Qualification fournisseur, conformité et retours — couverture lestée

**Observation :** 2026-08-25  
**Périmètre :** France, offre adulte uniquement  
**Canaux :** AliExpress Open Platform en lecture seule, textes UE et sources de sécurité publiques  
**Statut :** `TECHNICAL_WATCH_EXTERNAL_PROOF_REQUIRED`

## Verdict

La qualification ne passe pas. Good Nite `1005010144250762` reste le seul produit économiquement plausible, mais il ne constitue pas encore un SKU lançable. La demande et le prix potentiel sont prouvés ; la sécurité, la conformité, les retours et la robustesse fournisseur ne le sont pas.

## Contrôle fournisseur approfondi

### `OBSERVE`

- Produit actif : Good Nite `1005010144250762`, HT Direct Store, boutique déclarée en Allemagne.
- Variantes observées le 25 août 2026 :
  - 4 kg / 125x150 cm, SKU `12000051329035762`, stock 8, 42,51 EUR TTC ;
  - 6 kg / 125x180 cm, SKU `12000051329035763`, stock 9, 48,26 EUR TTC ;
  - 8 kg / 150x200 cm, SKU `12000051329035765`, stock 25, 59,75 EUR TTC.
- Boutique : 4,7 description, 4,7 communication, 4,8 expédition.
- API : 22 ventes et 0 évaluation ; écran consommateur antérieur : 122 vendus, 28 avis et 4,9/5. Conflit non résolu.
- Les valeurs brutes des attributs de taille sont incohérentes avec les libellés présentés : `140x200cm` devient `125x180cm (6kg)`, `140X205cm` devient `125x150 cm (4kg)` et `60X80cm` devient `150x200cm (8kg)`. Cette incohérence impose un contrôle physique et photographique avant toute publication.

### Recherche de secours bornée

Dix recherches fournisseur accessibles ont été exploitées, notamment `weighted blanket adult 7kg`, `weighted blanket 8kg glass beads`, `gravity blanket adult 6kg`, `weighted blanket 150x200 7kg cotton`, `weighted blanket adult`, `weighted blanket 5kg`, `weighted blanket 8kg` et `Gewichtsdecke Erwachsene`.

Résultat : aucun second produit adulte 6–8 kg, à microbilles/compartiments, expédié d'Europe et économiquement comparable. Les résultats sont dominés par des couvertures classiques, tapis, produits animaux, machines de pesage et autres faux positifs. Certaines requêtes ont renvoyé `EXCEPTION_TEXT_SEARCH_FOR_DS`.

`OBSERVE` signifie ici : aucun backup trouvé sur la surface officielle accessible. Cela ne prouve pas une absence globale.

## Gate conformité France/UE

### Exigences validées

- Le GPSR (UE 2023/988), applicable depuis le 13 décembre 2024, couvre les produits de consommation proposés en ligne dans l'UE.
- Une offre à distance doit afficher clairement le fabricant et ses coordonnées ; si le fabricant n'est pas établi dans l'UE, le responsable UE et ses coordonnées ; l'identification du produit ; et les avertissements/informations de sécurité dans une langue compréhensible par les consommateurs visés.
- Le règlement textile UE 1007/2011 exige l'indication de la composition en fibres, avec un étiquetage durable, lisible, visible et accessible ; l'information doit être fournie dans la langue officielle du marché visé.
- Pour un retour de rétractation, le consommateur ne supporte le coût direct que s'il en a été informé à l'avance. Pour un bien lourd dont le retour normal par la poste n'est pas possible, le vendeur doit donner une estimation du coût.

### `MANQUANT` sur le SKU exact

- identité et adresse du fabricant ;
- responsable économique établi dans l'UE et mandat associé ;
- référence de lot/série et traçabilité ;
- composition textile en pourcentages ;
- nature et confinement du lest, construction des compartiments et tolérance de poids ;
- analyse de risques, avertissements et notice en français ;
- instructions de lavage exactes ;
- adresse de retour, coût d'un retour 8 kg, délai de traitement et garantie ;
- preuve indépendante de qualité ou document Oeko-Tex applicable à la référence exacte.

La présence d'un stock en Allemagne n'établit aucun de ces points.

## Sécurité et communication

Deux rappels CPSC de couvertures lestées pour enfants ont documenté un risque d'emprisonnement dans une housse zippée et d'asphyxie ; le rappel Pillowfort concernait environ 204 000 unités et deux décès. La référence Good Nite observée est présentée comme adulte, mais cette preuve rend injustifiable une extension enfant sans analyse spécifique.

La littérature clinique récente suggère des bénéfices possibles sur l'anxiété et certains symptômes d'insomnie dans des populations psychiatriques, mais les revues soulignent le petit nombre d'études, l'hétérogénéité et la qualité variable. Conséquence commerciale : ne pas promettre de traiter, guérir ou prévenir l'insomnie, l'anxiété, l'autisme ou le TDAH. Une formulation de confort et de sensation d'enveloppement reste la borne prudente.

## Sensibilité économique — variante 8 kg

Hypothèses : coût rendu 59,75 EUR, paiement 2 %, provision globale retours/SAV. Cette provision ne remplace pas l'obtention du vrai coût retour.

| Prix TTC | Provision 8 % | ROAS rupture | Provision 12 % | ROAS rupture | Provision 15 % | ROAS rupture |
|---:|---:|---:|---:|---:|---:|---:|
| 99 EUR | 29,35 EUR | 3,37 | 25,39 EUR | 3,90 | 22,42 EUR | 4,42 |
| 109 EUR | 38,35 EUR | 2,84 | 33,99 EUR | 3,21 | 30,72 EUR | 3,55 |
| 129 EUR | 56,35 EUR | 2,29 | 51,19 EUR | 2,52 | 47,32 EUR | 2,73 |

À 129 EUR, l'économie absorbe mieux l'incertitude. À 99 EUR, elle devient fragile dès que la provision dépasse 8 %. Aucun de ces scénarios ne valide un CPA réel ni une rentabilité TVA complète.

## Conditions de sortie du watch

1. obtenir un dossier documentaire exact : fabricant, responsable UE, composition, remplissage, traçabilité, notice et analyse de risques ;
2. obtenir par écrit l'adresse et le coût maximum de retour pour les trois poids ainsi que la garantie ;
3. acheter un échantillon uniquement après autorisation humaine, puis vérifier poids/dimensions, coutures, fuite de billes, odeur, température, lavage et étiquette ;
4. trouver un backup exact 6–8 kg ou accepter explicitement le risque mono-fournisseur ;
5. conserver une V1 adulte et exclure l'enfant ainsi que les claims médicaux.

Sans ces preuves : pas de `TECHNICAL_PASS`, pas de `GO_FINAL`, pas de Shopify, DSers, Ads ou publication.

## Sources principales

- Règlement GPSR (UE) 2023/988 : https://eur-lex.europa.eu/eli/reg/2023/988/oj/eng
- Lignes directrices GPSR pour les entreprises : https://eur-lex.europa.eu/eli/C/2025/6233/oj/eng
- Règlement textile (UE) 1007/2011 : https://eur-lex.europa.eu/eli/reg/2011/1007/oj/eng
- Directive 2011/83/UE sur les droits des consommateurs : https://eur-lex.europa.eu/eli/dir/2011/83/oj/eng
- Rappel CPSC Pillowfort : https://www.cpsc.gov/Recalls/2023/Target-Recalls-Childrens-Pillowfort-Weighted-Blankets-Due-to-Asphyxiation-Hazard-Two-Fatalities-Reported
- Revue systématique 2024, Journal of Psychiatric Research : https://pubmed.ncbi.nlm.nih.gov/39341068/

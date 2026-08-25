# Couverture lestée — dossier technique Q4 révisé

**Verdict agent révisé : `TECHNICAL_WATCH_EXTERNAL_PROOF_REQUIRED`**

**Décision humaine : `PENDING_HAKIM`**

**Révision :** 2026-08-25, après apport d'une fiche AliExpress moins chère par Hakim.

**Deep dive :** [catalogue, clusters et fournisseurs approfondis](../deep-dive-couverture-lestee/final-couverture-lestee-deep-dive-20260825.md). Les 100 premières variantes SEMrush parmi 918 résultats et Google Trends France sur cinq ans ont été intégrés. La [qualification fournisseur/conformité](../deep-dive-couverture-lestee/raw/qualification-fournisseur-conformite-20260825.md) fixe désormais la porte externe restante.

## 1. Correction du diagnostic

Le précédent `TECHNICAL_FAIL` généralisait à tort le coût d'un seul mauvais fournisseur : un 7 kg expédié de Chine à 355,60 EUR rendu. La nouvelle fiche prouve qu'une couverture lestée adulte comparable peut partir d'Allemagne, fret France gratuit, à un coût très inférieur.

La fiche apportée n'est toutefois pas un 7 kg exact :

- l'URL contient le SKU `12000051329035763`, variante **125 × 180 cm, 6 kg** ;
- la capture produit sélectionne le SKU `12000051329035765`, variante **150 × 200 cm, 8 kg** ;
- les recherches AliExpress affichant « 7 kg » ne prouvent pas que le prix de vignette correspond au poids recherché.

Cette nuance n'annule pas la preuve économique : le marché mesuré porte d'abord sur `couverture lestée`, et une gamme adulte 6/8 kg peut être commercialement pertinente. Elle interdit seulement d'appeler cette fiche une preuve exacte de 7 kg.

## 2. Demande

- `OBSERVE` SEMrush France : `couverture lestée` 27 100/mois, KD 34, CPC affiché 0,32 USD.
- `OBSERVE` : `plaid lesté` 720 ; `couverture pondérée` 590.
- `OBSERVE` : variantes marque Action 4 400, IKEA 1 300 ; variante enfant 2 400 exclue du cluster adulte.
- `OBSERVE` : requête `danger` 1 000, signalant un besoin de pédagogie sécurité.
- `OBSERVE` Google Trends France cinq ans : moyenne octobre–février 2,86 fois supérieure à mai–août ; 2026 est en retrait de 15,1 % sur 33 semaines comparables face à 2025, mais 10,4 % au-dessus de 2024.

La demande passe ; le coût rendu n'est plus un motif d'élimination automatique.

## 3. Marché et concurrence

- [La Couverture Lestée 7 kg](https://lacouverturelestee.com/products/couverture-lestee-7-kg) : 129 EUR, fabrication Europe revendiquée, Oeko-Tex, guide de poids, échange 30 nuits, garantie 2 ans.
- [Castorama marketplace CELESTE 7 kg](https://www.castorama.fr/mkp/Couverture-lest-e-150x200-CM-CELESTE-bicolore-gris-clair-et-gris-7-kg/3662897097869_CAFR.prd) : 26,99 EUR, zéro avis visible ; plancher marketplace, qualité non prouvée.
- [ma-couverture-lestee.fr](https://ma-couverture-lestee.fr/couverture-lestee-7kg/) : 54,90 EUR et 847 avis revendiqués, non vérifiés.

Le marché reste polarisé entre marketplaces à bas prix et spécialistes rassurants autour de 129 EUR. Le droit de gagner devra venir de la qualité documentée, du choix du poids, de l'entretien, du service et d'une présentation plus crédible qu'une simple revente générique.

## 4. Nouveau fournisseur exact observé

| Champ | Preuve |
|---|---|
| Fiche | [Good Nite, product ID `1005010144250762`](https://fr.aliexpress.com/item/1005010144250762.html) |
| Boutique | HT Direct Store ; communication 4,7, description 4,7, expédition 4,8 |
| SKU 6 kg encodé dans l'URL | `12000051329035763` — 125 × 180 cm, 6 kg |
| Coût 6 kg API | 48,26 EUR TTC, stock 9 |
| SKU 8 kg sélectionné en capture | `12000051329035765` — 150 × 200 cm, 8 kg |
| Coût 8 kg API | **59,75 EUR TTC**, stock 25 |
| Origine / fret | Allemagne ; DHL ou DPD gratuit vers la France |
| Délai API | 3–8 jours DHL ; 3–9 jours DPD |
| Prix écran 8 kg | 49,23 EUR TTC, promotion affichée le 2026-08-25 |
| Compteurs écran | 4,9/5, 28 avis, 122 vendus |
| Compteurs API | 22 ventes, note 0, 0 évaluation exposée |

Le calcul central conserve **59,75 EUR**, prix API plus prudent. Les 49,23 EUR de la capture peuvent dépendre d'une promotion, d'un coupon ou du contexte du compte et ne sont pas traités comme un coût durable garanti. Le conflit entre compteurs écran et API est conservé, pas arbitré.

Le rafraîchissement API expose aussi des tailles brutes incompatibles avec les libellés affichés : `140x200cm` pour la variante présentée comme 125x180 cm / 6 kg, `140X205cm` pour 125x150 cm / 4 kg, et `60X80cm` pour 150x200 cm / 8 kg. Les dimensions restent donc commerciales, pas physiquement validées.

L'ancien produit `1005011748184966` reste documenté comme fournisseur à écarter, pas comme preuve que toute la catégorie est impossible.

## 5. Économie de sensibilité révisée

Calcul de trésorerie TTC, pas un profit comptable. Hypothèses : paiement 2 %, provision retours/SAV 8 %, coût rendu 8 kg API de 59,75 EUR.

| Prix TTC hypothétique | Coût rendu | Paiement | Provision | Contribution pré-ads | ROAS de rupture simplifié |
|---:|---:|---:|---:|---:|---:|
| 99 EUR | 59,75 | 1,98 | 7,92 | **29,35 EUR** | 3,37 |
| 109 EUR | 59,75 | 2,18 | 8,72 | **38,35 EUR** | 2,84 |
| 129 EUR | 59,75 | 2,58 | 10,32 | **56,35 EUR** | 2,29 |

Sensibilités complémentaires :

- à 129 EUR avec le prix promotionnel écran de 49,23 EUR : contribution pré-ads 66,87 EUR, ROAS de rupture 1,93 ; scénario non retenu comme central ;
- variante 6 kg à 48,26 EUR vendue 109 EUR : contribution pré-ads 49,84 EUR, ROAS de rupture 2,19.

La marge publicitaire potentielle existe donc. Elle reste à confronter aux CPC réels des requêtes commerciales, au régime de TVA, au taux de retour d'un colis lourd et au coût d'acquisition observé.

## 6. Pourquoi le verdict reste WATCH

- `MANQUANT` : composition précise, répartition et confinement des billes, tolérance de poids, qualité des coutures et test physique.
- `MANQUANT` : certificat Oeko-Tex ou équivalent vérifiable pour ce SKU, dossier GPSR et opérateur économique UE applicable.
- `MANQUANT` : conditions réelles de retour, adresse de retour, garantie et traitement d'un défaut après la protection plateforme.
- `MANQUANT` : deuxième fournisseur exact comparable pour éviter une dépendance à une seule fiche.
- `CONFLIT` : ventes et avis diffèrent fortement entre l'écran consommateur et l'Open Platform.
- `RISQUE` : ne pas reprendre les promesses « contre le stress » ou « meilleur sommeil » sans niveau de preuve adapté ; privilégier confort, sensation d'enveloppement, tailles, entretien et guide de poids prudent.
- `OBSERVE` : dix recherches fournisseur accessibles ont été exploitées sans trouver de backup adulte 6–8 kg comparable ; poursuivre les reformulations génériques sur la même surface polluée n'est plus productif.

## 7. Conclusion et prochaine porte

`TECHNICAL_WATCH_EXTERNAL_PROOF_REQUIRED`, toujours prioritaire devant les autres pistes du run. La prochaine porte n'est plus une recherche générique de prix, puisqu'elle est épuisée sur la surface accessible. Elle consiste à :

1. obtenir les documents matière/conformité et les spécifications exactes du SKU 8 kg ;
2. obtenir l'adresse et le coût maximum de retour, la garantie et la procédure SAV ;
3. trouver un backup 6–8 kg expédié d'Europe avec coût rendu comparable, ou accepter explicitement le risque mono-fournisseur ;
4. commander un échantillon seulement après validation humaine explicite, puis contrôler poids, dimensions, coutures, odeur, fuite de billes, lavage, étiquette, emballage et délai réel.

Aucun `GO_FINAL` ni achat n'est attribué par cette correction.

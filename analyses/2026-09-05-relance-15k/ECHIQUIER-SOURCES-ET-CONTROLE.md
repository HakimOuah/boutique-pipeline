# Échiquier — alternatives et contrôle du retour Luna

Contrôles du 5 septembre 2026. Le précédent tour a fourni de nouvelles preuves de sourcing et de saisonnalité : progression réelle. Ce tour approfondit les sources sans modifier le seuil de demande.

## Résultat fournisseur

Tous les appels ci-dessous utilisent l’API AliExpress installée, le pays DE, la devise EUR et `remove_personal_benefit=true` pour la fiche détaillée. Le fret est interrogé sur le SKU renvoyé par cette fiche.

| Produit / SKU | Format déclaré | Prix API | Fret DE | Total affiché | Délai estimé / origine | Stock déclaré |
|---|---|---:|---:|---:|---|---:|
| 1005005849671061 / 12000034567970119 | Ensemble pliant 15 × 15 pouces, environ 38 cm | 36,79 € | 1,99 € | **38,78 €** | **5–11 jours**, CN | 5 |
| 1005010707041100 / 12000058273814203 | Ensemble pliant 39 × 39 cm | 42,59 € | 1,99 € | **44,58 €** | **5–11 jours**, CN | 6 |
| 1005009871365018 / 12000050430442588 | 39 cm Rosewood Set, ancienne piste | 44,99 € | 2,37 € | 47,36 € | 7–16 jours, CN | 95 |

Les deux alternatives ont une propriété matériau « Aus Holz », cohérente avec leur titre. La troisième fiche, examinée par Luna, comporte une propriété « Plastic HIPS » incohérente avec son titre et ses variantes : elle n’est plus la source prioritaire. Les essences précises, finitions et qualité restent déclaratives. Les fenêtres de livraison sont des estimations ; la garantie API distincte est de 60 jours. Ces totaux ne représentent pas un checkout effectué ni une vérification du traitement fiscal final.

Preuves : `ali-de-schachbrett-alternatives.json`, `ali-de-chess-alternative-freight.json`. Source retenue pour approfondissement : la première, sans achat ni lancement.

## Comparaison visuelle et retour de Luna

Le retour `luna-echiquier-retour/RETOUR.md` confirme le prix concurrent **117,90 €**, un ensemble pliant de 40 cm avec 32 pièces et une livraison annoncée de **3–5 jours ouvrés**.

L’orchestrateur a inspecté les images du concurrent et du fournisseur en navigateur :

- Concurrent : plateau brun à bordures décorées et repères ronds, pièces sculptées ornées. Image : https://cdn.shopify.com/s/files/1/0635/7830/8826/files/echiquier-sycomore_5000x_085a7114-e65e-4b34-a72f-a9f0eb079cd8.jpg?v=1698423153
- Alternative 1005005849671061 : coffret à bordures simples, logement noir individuel pour les pièces, pièces classiques plus sobres. Image : https://ae01.alicdn.com/kf/Sc354b0c920a8495a80beed4ec6382d36c.jpg

Le format fonctionnel est comparable, **le produit n’est pas identique**. Le prix de 117,90 € reste un repère concurrentiel, pas la preuve qu’un acheteur paiera le même prix pour cette alternative.

Correction de l’audit : Luna avait écrit « drop probable sur la comparabilité commerciale ». Cette conclusion a été retirée. **Shopify + offre comparable ne suffisent pas à prouver le fulfillment du concurrent**. Statut conservé : dropshipping NON PROUVÉ. Les annonces Search historiques de mai restent une preuve séparée, sans prétendre à une diffusion actuelle.

## Vevor

Le modèle pliant SSC-15F, SKU MZGJXQ15YCSS1DS5BV0, a été vérifié sur le site allemand avec une destination test **Allemagne, 10115**. Prix rendu visible : **29,90 €**, état **Nicht auf Lager**. Ce n’est pas une source disponible. La recherche AliExpress « VEVOR wooden chess set » n’a pas établi de correspondance Vevor exacte parmi les résultats examinés.

## Complément TrendTrack

Recherche de boutiques par produits indexés et marché DE : une boutique, Maicona, apparaît pour « Schach », mais les informations retournées ne valident ni l’ensemble recherché ni une activité Google Ads (zéro annonce indiquée). La recherche « ferngesteuert » ne renvoie aucune boutique. Ces résultats limités ne prouvent pas l’absence de vendeurs ; ils n’ajoutent aucun candidat. Coût de ces deux requêtes : **4 crédits**.

## Décision

La piste échiquier est conservée comme **candidat de recherche**, avec une source plus abordable et un délai estimé amélioré. Aucun GO de lancement ajouté. L’identité fournisseur/concurrent n’est pas affirmée. Une clarification utilisateur sur la limite de livraison Q4 (7, 10 ou 14 jours) a été demandée : aucun seuil de 7 jours n’est supposé avoir été imposé par l’utilisateur. Dans l’attente, le délai **5–11 jours** reste indiqué tel quel, sans qualification « court validé ».

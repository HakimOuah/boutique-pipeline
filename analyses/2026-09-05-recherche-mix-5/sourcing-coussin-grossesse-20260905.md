# Due diligence fournisseur — coussin de grossesse — 05/09/2026

## Décision de passe

**Statut : `AUCUNE OFFRE EXPLOITABLE`.** Le PASS écrit autorisant cette due diligence est `./PASS-coussin-grossesse.md` (émis le 05/09/2026). Cette note est une qualification fournisseur bornée, sans `TECHNICAL_PASS`, `GO_FINAL`, commande ou publication.

## Méthode et résultat AliExpress

Outil utilisé : `codex-chasse-clusters/tools/aliexpress_vps_gateway.py`, via le gateway SSH read-only autorisé, destination `FR`. Les sorties brutes sont dans [`sourcing-coussin-grossesse/`](sourcing-coussin-grossesse/).

La séquence de recherche bornée a été polluée par des correspondances de coussin de nuque/voiture, lombaire, taie seule, peluche et produit bébé. La sortie JSON conservée pour `pregnancy pillow c shape` à **2026-09-05 18:10:18 UTC** contient 8 items ; aucun n'est un coussin maternité C/U complet pour adulte. Exemples rejetés :

| ID | Correspondance reçue | Motif de rejet | Prix affiché | Commandes / note |
|---|---|---|---:|---|
| `1005009183493058` | Taie seule 48×74 cm | housse sans produit | 4,79 € | 10 000+ |
| `1005008839075362` | Coussin C cervical / traction | usage cervical, pas maternité | 5,39 € | 5 000+ ; 4,5 |
| `1005006881611251` | Support tête siège-auto bébé | nourrisson, hors périmètre | 1,94 € | 5 000+ |
| `1005008809124364` | Coussin papillon cou/corps | forme/usage générique | 27,59 € | 5 000+ ; 4,7 |
| `1005009499128144` | Soutien lombaire sommeil | petite pièce, pas C/U | 8,99 € | 4 000+ ; 4,6 |

Les autres items sont une peluche Angry Blob et deux coussins de voiture/cervicaux, également rejetés. Les URL de résultats étaient des URLs de liste `www.aliexpress.com/item/...` avec paramètres ; elles ne sont pas traitées comme pages exactes.

Aucun ID grossesse adulte pertinent n'ayant émergé, **aucun appel `variants` ou `exact` n'a été lancé**. Il n'existe donc aucune observation fournisseur attestée pour : SKU couleur/taille, dimensions, garnissage, housse, stock, vendeur, délai France, transporteur, frais de port, coût livré, note/commandes d'une fiche grossesse, âge du vendeur ou retours. Aucun chiffre de recherche ne remplace ces champs manquants.

## Repères commerciaux publics déjà observés dans le PASS

Ces pages prouvent seulement qu'un prix de vente public existe dans la bande cible ; elles ne prouvent ni coût fournisseur, ni expédition AliExpress, ni qualité :

| Offre adulte visible en France | Usage / forme observée | Prix public observé | URL |
|---|---|---:|---|
| Pregnancy Atelier — coussin de grossesse en C | adulte, forme C, unité | 69,90 € TTC | [pregnancyatelier.fr/products/coussin-de-grossesse-en-c-coton-bio-rose](https://pregnancyatelier.fr/products/coussin-de-grossesse-en-c-coton-bio-rose) |
| Coussin.fr — coussin grossesse étoiles | adulte, forme U annoncée | 79,90 € | [coussin.fr/products/coussin-grossesse-avec-motifs-detoiles](https://coussin.fr/products/coussin-grossesse-avec-motifs-detoiles) |
| Greenweez / Babymoov Doomoo Maxxy | maternité/allaitement, unité | 79,90 € | [greenweez.com/produit/coussin-grossesse-et-allaitement-buddy-leaves-aquagreen/1MOOV014722](https://www.greenweez.com/produit/coussin-grossesse-et-allaitement-buddy-leaves-aquagreen/1MOOV014722) |
| Bebidou — Be’Confort | maternité, unité | 89,90 € | [bebidou.fr](https://bebidou.fr/) |

La formulation française à conserver pour une reprise de mesure est `coussin de grossesse`; les variantes doivent rester séparées (`coussin grossesse`, `coussin de maternité`, `coussin grossesse ergonomique`, et les formes C/U). La tête `coussin de grossesse` à 33 100/mois France/French appartient au PASS, pas à une preuve fournisseur.

## Limites et reprise possible

- La forme C/U grand format, les dimensions, le poids colis et le produit complet restent non sourcés.
- Les résultats AliExpress actuels ne permettent pas de distinguer un fournisseur adulte grossesse d'une catégorie générique polluée.
- Ne pas réutiliser les prix 69,90–89,90 € comme marge ou coût rendu.
- Une reprise nécessite une nouvelle fenêtre autorisée avec requêtes plus discriminantes et sonde `variants`/`exact` seulement après identification d'une fiche adulte pertinente. Aucun STOP body pillow n'est étendu au présent candidat ; cette absence de STOP ne vaut pas preuve de sourcing.

## Reprise discriminante et leads web (18:15–18:16 UTC)

Trois requêtes réelles supplémentaires ont été envoyées au gateway : `maternity full body pillow u shaped`, `pregnant women pillow long` et `maternity pillow removable cover full body`. La query est bien reflétée dans le champ `query` de la réponse, mais le moteur retourne à nouveau des taies, coussins voiture/cervicaux, articles enfants/bébé et soutiens génériques. Le détail est dans [`gateway-search-discriminant-20260905.json`](sourcing-coussin-grossesse/gateway-search-discriminant-20260905.json).

Une recherche web publique secondaire (Alitools/Pricearchive, pages anciennes ou indexées récemment) a néanmoins révélé cinq **leads** à examiner ultérieurement : `1005001860055245` (U adulte, Good lucky is happiness, 16,29 USD affichés, page crawlée il y a 5 mois), `4000201156802` (U adulte avec housse zippée, We-Shopping Store, 16,60 USD et 12 orders affichés, page crawlée il y a 5 mois), `1005001666610169` (U corps complet, Balaon Store), `1005007607304338` et `1005012718856342` (U maternité, Pricearchive). Les fiches publiques indiquent parfois une forme ou un poids, mais aucun port France, délai, stock ou coût livré actuel. URLs et âge de l'observation : [`web-discovery-alitools-20260905.json`](sourcing-coussin-grossesse/web-discovery-alitools-20260905.json).

Les sondes gateway sur `variants` pour les deux premiers IDs et `exact` sur `4000201156802` ont toutes retourné **`IOPUpstreamError`, code AE 605**. Les propriétés `U-Shape` et `1-1.5 kg` de la tentative `exact` venaient des spécifications du lead Alitools, jamais d'une réponse `variants` ou d'une PDP : la tentative est **NON QUALIFIANTE**. Aucune donnée SKU n'a été reçue. Voir [`gateway-probes-20260905.json`](sourcing-coussin-grossesse/gateway-probes-20260905.json). L'erreur AE 605 ne prouve pas une indisponibilité globale de l'API. Les leads restent une **découverte historique niveau C**, pas `FOURNISSEUR À TESTER` (qui exige une fiche complète actuelle); le statut global demeure **`AUCUNE OFFRE EXPLOITABLE`**.

## Contrôle navigateur par Astra

La tentative directe sur `https://fr.aliexpress.com/item/4000201156802.html` a été refusée par la politique de sécurité du navigateur. Aucun contournement ni reprise du même accès. Cette restriction et les erreurs API empêchent la vérification du SKU, pas la constatation de la demande. Le budget déjà autorisé ne nécessite pas de nouvelle permission pour les travaux indépendants.

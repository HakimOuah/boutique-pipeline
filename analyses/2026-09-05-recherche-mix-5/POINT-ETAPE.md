# Recherche mixte France — état des preuves du 5 septembre 2026

**Objectif non atteint : aucun nouveau TECHNICAL_PASS parmi les dossiers examinés.** La cible reste trois produits purs Search et deux univers Shopping. Le coussin de grossesse et l’univers bijoux pierres naturelles ont franchi la préqualification marché ; leur qualification fournisseur reste incomplète. Aucun candidat n'est présenté comme prêt à lancer et aucun GO_FINAL n'est émis.

Cette passe a exécuté le lot préparé puis réalloué la recherche à deux lots Search supplémentaires et à deux univers historiques non clôturés. Les recherches ne prouvent pas qu'il n'existe aucun produit viable : elles montrent les preuves et manques des candidats examinés. Le budget est un plafond, pas une dépense à épuiser. **Dépense DataForSEO : 3,17016 USD, soit environ 2,73 €** au taux ECB du 4 septembre (hors frais/change de facturation), sur un plafond autorisé de 10 €. Les 57 appels ont produit 234 lignes de contrôle exact hors témoins, 16 343 lignes Labs avant déduplication, 17 SERP et 7 interrogations Trends. Aucun appel Monid ni achat de crédits. Les coûts définitifs sont dans [budget.json](budget.json) et chaque appel dans [couts.jsonl](couts.jsonl).

## Produit pur / Search

| Candidat | Demande observée France/français | Prix public observé | Verdict et preuve déterminante |
|---|---|---|---|
| **Coussin de grossesse** | `coussin de grossesse` **33 100** ; `coussin grossesse` 5 400 non ajouté | **69,90–89,90 €** ; certains prix issus de pages indexées à reconfirmer | **PASS_PREQUALIFICATION / TECHNICAL_INCONCLUSIVE**. Intention produit et socle Trends cinq ans confirmés. Aucun SKU AliExpress complet, coût livré ou marge attestés. |
| Cache de climatisation extérieure | tête 12 100 ; extérieur 8 100 dans un bucket différent ; bois 1 000, aluminium 480 | 199 € Prima, 229 € Kach Klim ; cartes généralistes moins chères | **REVIEW_PREQUALIFICATION**. Taille de demande plausible, mais offre standard à choisir, ventilation et différence exécutable face aux fabricants à établir. Forte saison estivale ; pas de validation Q4 implicite. Le seul écart de 3 % entre 12 100 et le repère approximatif 12 500 ne serait pas un motif de rejet. |
| Coussin de lecture | cinq buckets proposés totalisant **12 890** : 9 900 + 2 400 + 390 + 110 + 90 | 20,99 € Gifi ; offres spécialisées 64,99–139,50 € dans les cartes Google | **REVIEW_PREQUALIFICATION**. Proche du repère ; tête mélange dossiers corporels et accessoires de lecture. Prix premium repérés ne prouvent pas l'attribution intégrale du volume à ce format. Trends incomplet, nombreux points sans valeur. |
| Batardeau résidentiel | `batardeau` 14 800 ; corpus proposé **18 090 avec tête**, **3 290 sans** | 240–375 € Nerolis, dès 282 € Batardeau.shop | **REVIEW_PREQUALIFICATION**. SERP majoritairement liée à la protection d'ouvertures, mais attribution du générique BTP/résidentiel non résolue ; le scénario haut n'est pas un net garanti. Cotes, étanchéité, responsabilité et fret restent importants. |
| Garde-manger bois | tête 9 900 ; bois 2 400 ; meuble 1 900 dans Labs, sans somme automatique | 58,90–156 € pour petits modèles ; 376,80 € buffet différent | **REVIEW_PREQUALIFICATION**. Intention domestique observée ; restaurant, métier et grand meuble mêlés au corpus. Ne pas attribuer ces volumes au seul petit fromager. |
| Oreiller ergonomique / cervical | ergonomique 22 200 ; cervical 18 100, **non additionnés** | 53,37–69,99 € repérés | **REVIEW_PREQUALIFICATION**. Demande réelle de catégorie mais Dodo, Bultex, Tempur, IKEA et généralistes installés. Aucun avantage générique démontré ; pas de sourcing ouvert. |
| Mannequin de couture réglable | tête 9 900 ; réglable 1 900 ; femme 390 ; homme 170 | 129,90–399,90 € selon offre | **REVIEW_PREQUALIFICATION**. Demande mêlant particuliers, ateliers et bustes de présentation. Les variantes professionnelles et pieds seuls ne complètent pas artificiellement le seuil. |
| Sorbetière à compresseur, thermostat connecté | parents 22 200 et 14 800 | offres 159,99 et 179,99 € ; disponibilités et modèles distincts | **Non retenus pour la due diligence de ce lot** : compresseur beaucoup plus étroit que parent sorbetière ; thermostat dominé par marques et compatibilité installée. Pas de verdict sur tous les appareils de ces marchés. |

### Pourquoi le coussin de grossesse n'est pas encore validé

Le [pass écrit](PASS-coussin-grossesse.md) a été [contrôlé contradictoirement](revue-prequal-coussin-20260905.md). La SERP comporte sept offres/catégories et deux comparaisons. Le volume ne valide pas une forme C/U précise à lui seul. Trends a un point marqué manquant, conservé comme tel.

Le [benchmark](benchmark-coussin-grossesse.md) relève trois offres spécialisées et un angle de meilleure clarté produit, mais aussi un concurrent annonçant 48 h de livraison. La simulation économique distingue TVA supposée, frais, retours et CPA hypothétique ; elle ne remplace pas un coût d'achat livré.

Le [sourcing](sourcing-coussin-grossesse-20260905.md) n'a ramené que des résultats hors cible et des leads historiques Alitools. Les tentatives de variantes ont échoué. Une tentative exacte avec libellés Alitools non confirmés est non qualifiante ; elle ne prouve pas une panne générale de l'API. L'ouverture directe de la fiche AliExpress visée a été refusée par la politique de sécurité du navigateur et n'a pas été contournée. **Prix livré, stock, délai, vendeur actuel et composition vérifiée restent MANQUANT.**

### Pistes nettement faibles à la première mesure

Les chiffres ci-dessous sont les requêtes testées, pas un plafond exhaustif de chaque marché : affûteuse à eau 140/390 selon formulation ; cave à fromage 880 ; fumoir à froid 720/2 900 ; table de rempotage 1 900 ; pedalboard 720 ; cerf-volant acrobatique 110 ; croquet 1 900 ; presse à fleurs 210 ; kit montage mouche 110. Le four solaire atteint 8 100 mais son corpus inclut Odeillo, Font-Romeu, Mont-Louis et fabrication DIY.

Les autres sondes exactes — matériel de mesure domestique, aides de transfert, rollator, rangement de bijoux/montres, parapluies et lecture — sont consultables dans [mesures-exactes.csv](mesures-exactes.csv). Les données nulles restent MANQUANT. Une chaîne accidentelle `moniteur CO2 STOP` était un commentaire de scouting entré dans le lot : elle ne représente aucun candidat et est exclue des décisions. Le STOP CO2 n'est pas réactivé.

## Produit univers / Shopping

Ces dossiers suivent le seuil consolidé 37 500, l'économie de panier et la sourçabilité par familles. Ils ne reprennent jamais le seuil Search.

| Univers | Ce qui a été établi | Verdict et réserves |
|---|---|---|
| **Matériel aquarelle** | Corpus Labs 1 000/17 311 ; familles papier, couleurs, pinceaux, coffrets ; SERP et prix sondés | Têtes très mixtes : œuvres, tutoriels, fleuriste, piscine et boutique Aquarelle et Pinceaux. Le bucket pinceaux 12 100 ne peut pas être déclaré intégralement générique sans adjudication. Aucun net complet établi. La première sonde prix ne prouve pas 30 SKU uniques. |
| **Fléchettes traditionnelles** | Corpus avec et sans accent ; acier, sisal, installation et pièces séparés | `jeu de fléchettes` 18 100 et cibles génériques mêlent électronique, jeux gratuits et autres intentions. Électronique/connecté et soft-tip restent exclus selon l'historique. Aucun net traditionnel suffisant démontré ; aucun sourcing. |
| **Globes/cartographie décorative — reprise historique U3** | Offres de globes et cartes murales, 36 fiches/prix d'entrée recensés ; sous-types commerciaux étudiés | Têtes globe 27 100 et mappemonde 22 200 non intégralement attribuables au décor physique. Le calcul prudent et sa sensibilité sont dans le mémo spécifique. Les prix « dès » et variantes ne valent pas 36 SKU exacts contrôlés ; sourcing par familles absent. |
| **Bijoux pierres naturelles/symboles — candidat déjà nommé, nouvellement mesuré** | Bracelets, bagues, colliers, boucles et symboles portés ; 33 bijoux tarifés (médiane 39 €, zéro sous 15 €), deux arbres décoratifs exclus | **PASS_PREQUALIFICATION** émis après consolidation à **44 730/mois** et contrôle contradictoire ; détail dans [le pass](PASS-bijoux-pierres.md). Demande esthétique séparée des termes explicites de vertus/santé et du luxe. **TECHNICAL_INCONCLUSIVE** : deux vendeurs bracelets, un seul colliers, aucune bague qualifiée. Contribution de panier et conformité non validées. Ce dossier ne réactive pas l'ésotérisme/lithothérapie générale arrêté. |

### Ce que le sourcing bijoux prouve réellement

[Bracelets et bagues](sourcing-bijoux-bracelets-bagues-20260905.md) : deux variantes de bracelets chez des vendeurs distincts, coûts livrés FR calculés à 6,58 € et 3,90 €, stocks respectifs 2 et 13. [Colliers](sourcing-bijoux-colliers-20260905.md) : une variante lapis à 5,78 € livré, stock 18. Délais déclarés 5–10 jours ; notes/avis produits non exploitables dans les réponses. Aucun coût source n’est transféré à un jonc argent ou à une bague différente.

La famille bracelets pèse 44,4 % du net, colliers 16,4 % et bagues 29,8 %. **Seuls les bracelets ont deux vendeurs observés**, avec un stock de deux unités qui fragilise même cette couverture. Le minimum de deux fournisseurs dans chacune des trois familles principales n’est pas atteint. Des requêtes distinctives, noms de magasins et un essai lexical sans termes génériques n’ont pas résolu les bagues ; cela prouve une limite de la collecte, pas l’absence de fournisseurs dans le monde. [Économie de panier](economie-bijoux.md), [benchmark](benchmark-bijoux-20260905.md) et [matières/conformité](conformite-bijoux.md) sont documentés sans conclure à une rentabilité.

Les dossiers Padel, kéfir/kombucha, slackline, yoga aérien, équitation et escalade restent de la découverte préparatoire : aucune prétention d'analyse complète ni réouverture des exclusions.

## Méthode, corrections et limites

- Toutes les mesures décisionnelles : DataForSEO, France/French, endpoints, date et chaîne exacte conservés dans `raw/`. Labs découvre ; Google Ads Search Volume contrôle les expressions déterminantes. Aucun volume SEMrush historique n'est utilisé pour un pass.
- Le témoin `tufting` vaut 12 100 avant et après le premier lot, puis aux contrôles de fin. Un témoin cohérent ne garantit pas l'intention commerciale de chaque mot.
- MAX par variantes/buckets réellement identiques, pas somme de synonymes. Des sous-types distincts ne sont pas automatiquement absorbés par leur parent. Une somme de requêtes n'est jamais un nombre de personnes uniques.
- Les études partielles de corpus 1 000 lignes ne sont pas exhaustives. Les lignes candidates et ambiguës sont conservées ; leur exclusion prudente ne signifie pas une demande réelle nulle.
- Deux erreurs de transmission des scouts ont été corrigées : chaînes de mots-clés abrégées et compte SERP grossesse 8+1 au lieu de 7+2. Une tentative fournisseur sans SKU attesté a été explicitement déclassée. Ces contrôles évitent de transformer une sortie de sous-agent en preuve.
- Astra a piloté et arbitré ; trois sous-agents GPT-5.6 Luna/high ont collecté et revu les données. Aucun benchmark de performance entre modèles n'est déduit de cette mission.
- Aucun seuil, instruction globale, moteur de scoring, boutique, campagne, credential, commande ou message externe modifié. Les preuves et le registre sont les seuls changements durables de cette recherche, avec un événement NOX brut séparé dans le hub.

## Reprise précise

1. **Grossesse, priorité fournisseur** : obtenir une fiche AliExpress adulte complète accessible par un moyen autorisé ; vérifier variante réellement observée, coût livré FR, délai, stock, vendeur et matériaux. Pas de répétition de la même requête polluée ni contournement du blocage navigateur. Recalculer contribution et concurrence Ads avant TECHNICAL_PASS.
2. **Search** : prioriser cache-clim pour une offre standard précise, puis trancher l'attribution des coussins de lecture et du batardeau. Les critères de format et les barrières concurrentielles doivent être résolus avant sourcing ; aucune nouvelle approbation n'est nécessaire pour les analyses déjà autorisées dans le budget restant.
3. **Shopping** : le pass bijoux ouvre la vérification de deux fournisseurs plausibles dans chacune des trois familles principales couvrant plus de 85 % du net. Pour les autres univers, terminer l’adjudication avant sourcing. Aucun quota n’est rempli par les prix publics d’une boutique concurrente.

**L'état de cette passe est INCOMPLETE / PREUVES_INSUFFISANTES, et non tâche accomplie.** La [préparation avant budget](PREPARATION-AVANT-BUDGET.md) est conservée comme archive ; ses mentions de budget en attente ne décrivent plus l'état actuel. Hakim garde la sélection finale et la commande test ; SAMPLE_OK demeure nécessaire avant GMC/Ads.

# KAMPFE — catalogue fourni par Hakim et contrôles API — 04/09/2026

**Deux `OFFRE TROUVÉE`, confiance B, dans le magasin exact `1104699287`.** La capture utilisateur permet de cibler KAMPFE ; l'API confirme des SKU en stock et une livraison France annoncée. Ce progrès remplace l'absence d'identification du marchand au stade précédent. Il ne valide ni un coffret complet, ni la qualité débutant, ni le lancement A6 (`REVIEW_PREQUALIFICATION` / `TECHNICAL_INCONCLUSIVE` inchangés).

## Ce que la capture permet de lire

Boutique KAMPFE, 98,9 % de retours positifs et 1,2k abonnés affichés. Ces compteurs sont ceux du catalogue, pas des avis du SKU sélectionné. La monnaie est EUR, la promotion affiche une fin au 07/09/2026. La destination de livraison n'est pas suffisamment établie par la capture seule. Les ventes/étoiles des cartes ne sont pas promues en preuve produit.

| Carte visible | Prix affiché | Lecture et intérêt |
|---|---:|---|
| Aluminium CNC « 30° », trois versions Mild / Medium / Aggress | 32,39 € | Premier candidat visuel pour l'offre débutant : instruire la version Mild. Trois rasoirs illustrés ne prouvent pas un lot de trois. La référence exacte reste à identifier. |
| A99 Attack 30°, carte distincte | 32,39 € | Référence retrouvée via API. Ne pas l'assimiler au modèle Mild de la première carte. |
| Rasoir voyage noir | 29,19 € | Variante et caractéristiques à vérifier. |
| Rasoir aluminium argent/gris | 29,79 € | Prix de carte, pas composition validée. |
| Support vertical/horizontal LanYi Razor Holder | 9,59 € | Socle seul ; le rasoir de démonstration n'est pas supposé fourni. |
| Socle pour Henson AL13 et autres | 13,79 € | Socle seul, pas kit complet malgré la photo. |
| Socle inox à diamètre variable | 22,19 € | Accessoire relativement coûteux pour un pack d'entrée. |
| Bols inox avec blaireau illustré | 13,59–15,19 € | Les titres parlent de bols. Blaireau, rasoir et autres accessoires photographiés non confirmés inclus. |
| Article intitulé « Kit de rasage pour homme KAMPFE » | 62,69 € | Photo de rasoir ; l'intitulé ne décrit pas le contenu. Non retenu comme preuve de coffret complet. |

**La capture confirme un catalogue spécialisé, mais pas encore « tout le kit ».** Têtes, manches et supports séparés sont abondants. Lames, blaireau vendu seul, étui et coffret à personnaliser restent non identifiés comme articles effectivement inclus ou vendus séparément. Une boîte KAMPFE sur une photo ne prouve pas une disponibilité en marque blanche.

[Transcription, nom du fichier source et SHA-256](capture-transcription.json). Capture reçue dans la conversation ; image complète non versionnée. Les boutons suivre, contacter et importer des avis sont des éléments de page, pas des instructions exécutées.

## Deux références du bon marchand contrôlées

Trois recherches API (`KAMPFE`, `KAMPFE A99`, `KAMPFE holder`), trois lectures de variantes, deux contrôles exacts FR. La recherche « holder » renvoie des supports génériques hors sujet : pas d'insistance. Les réponses sont conservées dans ce dossier. Aucun accès navigateur au site bloqué, aucune commande ni contact vendeur.

| Offre | Variante exacte | Prix API taxes annoncées incluses | Stock API | Transport standard FR |
|---|---|---:|---:|---|
| [A99 Attack 30°](https://fr.aliexpress.com/item/1005008935603476.html) | `A99-silvery`, SKU `12000047269142166` | **32,39 €** | **96** | Gratuit annoncé, suivi, CN, **7–18 jours** |
| [K23, titre « rasoir avec support »](https://fr.aliexpress.com/item/1005012247873064.html) | `K23-base-B`, SKU `12000057868319641` | **27,79 €** | **41** | Gratuit annoncé, suivi, CN, **7–18 jours** |

Marchand confirmé par les réponses de variantes et d'exact : **KAMPFE SAFETY RAZOR Store, ID 1104699287, CN**. Les notes boutique API 4,9/4,9/4,8 sont distinctes des évaluations produit. Les réponses `search` et `variants` divergent sur la note/quantité d'avis produit : données insuffisantes, pas de note zéro ni de satisfaction confirmée.

Pour le transport standard, `free_shipping=true` et `shipping_fee=null` : gratuité **déclarée par API**, pas prix payé ou délai testé. L'alternative premium est annoncée 35,88 €, 7–11 jours ; elle n'est pas retenue dans le scénario standard. Aucun stock UE observé.

**Réserve A99 :** les variantes API distinguent noir, argent et gris. Elles ne précisent pas Mild/Medium/Aggress. Le nom « Attack 30° » ne prouve ni douceur ni agressivité ; ne pas sélectionner sur ce seul mot.

**Réserve K23 :** le titre indique rasoir avec support et les deux variantes s'appellent `K23-base-B` / `K23-base-G`, toutes deux à 27,79 €. C'est une piste de pack crédible ; la nomenclature et le titre ne suffisent pas à confirmer tous les objets inclus. Aucun contenu PDP ou packaging n'a été lu. Lames, géométrie de tête et coffret restent manquants.

La recherche a aussi proposé un KAMPFE à **20,79 €** (`1005012261715961`). Le contrôle retourne **un autre magasin, 1105186411** : exclu de la composition « chez le même marchand », sans le déclarer copie ou mauvais fournisseur. Une marque dans le titre n'identifie pas le vendeur.

[Offres structurées](offers.json) · [A99 exact](exact-1005008935603476.json) · [K23 exact](exact-1005012247873064.json).

## Compositions et économie

Le premier montage visible est **32,39 + 9,59 = 41,98 €**, avant lames, blaireau éventuel, étui/boîte et regroupement. Les frais gratuits sur chaque carte ne démontrent pas l'envoi d'un coffret assemblé. Les dimensions du support doivent correspondre au manche ; ne pas combiner un support de rasoir seul avec un blaireau sans logement adapté.

Le **K23 annoncé avec support à 27,79 €** pourrait mieux convenir économiquement, **si le contenu complet est confirmé**. Il n'est pas considéré comme équivalent mécanique au modèle 30° ni comme qualité supérieure.

Scénarios : prix TTC ; TVA 20 %, paiement 2 % + 0,30 €, SAV/retours 5 % TTC ; CPC 0,80 €, CVR 2 %. Hypothèses inchangées du [modèle A6](../../economics-assumptions.json), aucune performance réelle. Prix fournisseur traités prudemment sans récupération de TVA supposée. Les enveloppes complémentaires sont des **budgets hypothétiques non chiffrés chez le vendeur**, pas des coûts sourcés.

| Construction hypothétique | Coût rendu scénario | Contribution après Ads à 99 € | À 119 € |
|---|---:|---:|---:|
| Rasoir 32,39 € + support 9,59 €, aucun complément | 41,98 € | −6,71 € | +8,56 € |
| Même base + enveloppe 10 € de compléments | 51,98 € | −16,71 € | −1,44 € |
| K23 annoncé avec base + enveloppe 5 € | 32,79 € | −2,52 € | +17,75 € |
| K23 annoncé avec base + enveloppe 10 € | 37,79 € | −7,52 € | +12,75 € |

Contributions avant coûts fixes. Dans le dernier scénario, BE-CVR = environ **1,52 %** à CPC 0,80 €, ou **2,28 %** à CPC 1,20 €. Cela rend le K23 digne d'investigation, sans en faire un PASS. Le prix de vente 119 € exige une offre défendable et peut convertir moins bien que 99 € ; il n'est pas choisi automatiquement pour rendre la simulation positive.

[42 sensibilités](economics.csv) incluant prix 69/99/119 et CPC 0,80/1,20. Aucun coût de blaireau/boîte, remise volume, taux d'upsell ou LTV inventé.

## Suite recommandée

1. **Priorité économique : K23 à 27,79 €**, vérifier via contenu de fiche fourni ou confirmation du vendeur ce qui est livré : rasoir complet, support, lames, emballage. Aucun message n'a été envoyé.
2. **Priorité produit : modèle 30° annoncé Mild dans la capture.** Obtenir son lien exact ; comparer sa géométrie, poids et tolérances à l'A99, sans attribuer les spécifications d'une carte à l'autre.
3. Privilégier d'abord un pack rasoir + support + lames + notice. Ajouter blaireau/bol uniquement si leur utilité et leur coût sont établis. Tester l'adoption d'un coffret complet séparément de l'offre d'entrée.
4. Vérifier droit de revente/branding, disponibilité simultanée, assemblage, emballage, colis unique et délai tenu ; conserver la différence entre un prix promotionnel public et un devis durable. Aucune personnalisation n'est présumée disponible.
5. Faire réévaluer offre/économie et décision Hakim avant sample selon le pipeline ; aucun achat ni nouveau statut final autorisé par ce dossier.

**Conclusion : la capture fait progresser le sourcing.** L'ancien DSCOSMETIC à 51,99 € ne représente plus à lui seul les possibilités trouvées. Deux offres exactes du bon marchand ont maintenant un stock et un fret France déclarés. Le catalogue permet d'envisager un pack cohérent, mais les preuves de contenu, de douceur et d'économie finale restent nécessaires.

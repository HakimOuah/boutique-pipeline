# Rapport Gate 1 — marché, concurrence et right to win

**Projet :** Étude concurrentielle cinq niches Kraken

**Date :** 2026-08-08

**Décision active :** `SUSPENDU_PHASE_2` — perles reste à instruire ; aucun site
ni sourcing sélectionné.

La décision historique `GO_CONDITIONNEL — priorité scrap/journaling` est
supplantée. La phase 2 scrap aboutit à `STOP_PHASE_2`, motif principal
`STOP_PRIX_PANIER`. Le premier concurrent similaire valide le modèle et ne
constitue pas la cause du rejet.

## Question

La structure de prix permet-elle d'abord une commande intéressante, puis
existe-t-il une demande commerciale suffisante et un espace exécutable face
aux alternatives ?

## Preuves actives

| Statut | Fait atomique | Source/date | Portée | Confiance |
|---|---|---|---|---|
| `OBSERVE_PROJET` | Le marché scrap possède des requêtes et SERP commerciales réelles | volumes + SERP — 2026-08-08 | demande | élevée |
| `OBSERVE_PROJET` | Échantillon Scraperie : médiane 10,99 EUR ; 33/48 produits à 13,99 EUR ou moins | trois pages catégories — 2026-08-08 | prix | élevée pour l'échantillon |
| `STOP_PRIX_PANIER` | Cœur papiers/autocollants à médianes 4,99/8,99 EUR ; AOV et contribution non prouvés | snapshot prix + correction Hakim | économie potentielle | élevée |
| `MANQUANT_RENETTOYAGE` | Le total scrap 64 740 n'est pas reconstructible depuis les mesures conservées | JSON volumes + audit Phase 2 | demande scrap | élevée sur le manque |
| `OBSERVE_PROJET` | Les spécialistes stockistes occupent marques, rapidité, kits, tutoriels et collections coordonnées | panel concurrentiel + SERP | concurrence scrap | élevée |
| `OBSERVE_PROJET` | Scraperie décrit un fulfillment direct international et des colis séparés | FAQ + profil Scraperie | modèle comparable | élevée |
| `OBSERVE_PROJET_NON_DECISIF` | Scraperie : 214 PDP publiques, AS 8, 58 trafic organique estimé, 32 mots-clés, 0 paid | sitemap + SEMrush France | traction comparable | ne prouve ni échec ni succès |
| `DECISION_PROJET` | Un concurrent comparable isolé valide le modèle ; il n'arrête pas la niche | correction Hakim | méthode | élevée |
| `MANQUANT` | CPC actualisé, AOV, marge contributive, CPA de rupture et livraison SKU | — | économie | nulle |

## Décision par niche

| Niche | Gate 1 | Condition principale |
|---|---|---|
| Scrap/journaling | `STOP_PHASE_2` | Motif principal `STOP_PRIX_PANIER` : cœur catalogue autour de 5–14 EUR, panier/marge non prouvés. Demande propre et fulfillment restent des réserves secondaires. |
| Mobilité chien | `STOP_PHASE_2` | Segment verrouillé par marques/spécialistes et généralistes ; logistique transport défavorable. |
| Mercerie | `STOP_PHASE_2` | Profondeur/stock local, faible ticket et ancienneté des acteurs rendent le modèle non défendable. |
| Perles/bijoux | `SUSPENDU_PHASE_2` | Étude profonde et économie du panier composé manquantes. |
| Aquascaping | `STOP_PHASE_2` | Vivant moteur de valeur ; angle pédagogique déjà pris ; matériel de marque/stock/logistique non réplicable en drop. |

## Risques et contradictions

- Une demande élevée ne garantit pas un angle rentable.
- Une estimation de trafic faible ne permet pas de déclarer qu'un concurrent a
  échoué. Elle reste une donnée contextuelle, pas un gate.
- Un seul concurrent qui fait déjà ce que nous envisageons est plutôt un signal
  de validation ; la densité et les actifs défensifs se jugent ensuite.
- Le prix/panier doit être sondé avant la profondeur concurrentielle. Ici, le
  cœur à 5–14 EUR ne justifiait pas de poursuivre sans preuve d'AOV.
- La méthode V3 autorise une PDP à volume zéro, mais ne permet pas d'accepter un
  total de niche dont le nettoyage n'est pas reproductible.
- Le positionnement souvenir-first existe déjà, mais une différenciation
  radicale n'est pas requise si l'économie et l'exécution sont meilleures.
- Le kit personnalisable promis correctement exige une maîtrise opérationnelle
  que l'expédition multi-fournisseurs contredit.

## Conditions de passage du projet

- [x] Terminer l'étude concurrentielle profonde de scrap/journaling.
- [x] Produire le verdict scrap et interdire le sourcing après `STOP`.
- [ ] Terminer l'étude concurrentielle profonde de perles/bijoux.
- [ ] Choisir un site uniquement si un dossier obtient `GO` ou
  `GO_CONDITIONNEL` avec right to win explicite.
- [ ] Après seulement, construire l'arborescence puis appliquer le gate V3 au
  sourcing exact.

## Actions

| Priorité | Action | Responsable | Classe | Preuve de fin |
|---:|---|---|---|---|
| 1 | Sonde prix/panier perles avant phase 2 profonde | Codex | A | 30–50 prix cœur, médiane, distribution, bundles et décision rapide |
| 2 | Si le filtre prix passe, phase 2 profonde perles/bijoux | Codex | A | profils, SERP, mots-clés, panier, angle et verdict |
| 3 | Choisir le premier site parmi les seuls `GO` | Hakim + Codex | A | décision enregistrée, sans sourcing préalable |
| 4 | Si perles est aussi `STOP`, arbitrer nouvelle idéation France, marque/stock-kitting, candidats high-ticket ou marché étranger | Hakim + Codex | A | voie suivante explicitement choisie |

## Date de revue

Après le verdict perles. Aucun sourcing n'est lancé pour forcer un dossier
arrêté.

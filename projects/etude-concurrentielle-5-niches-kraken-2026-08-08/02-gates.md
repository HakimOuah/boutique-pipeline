# Rapport Gate 1 — marché, concurrence et right to win

**Projet :** Étude concurrentielle cinq niches Kraken

**Date :** 2026-08-08

**Décision active :** `SUSPENDU_PHASE_2` — perles reste à instruire ; aucun site
ni sourcing sélectionné.

La décision historique `GO_CONDITIONNEL — priorité scrap/journaling` est
supplantée. La phase 2 scrap aboutit à `STOP_PHASE_2` : demande propre à
reconstruire et aucun right to win reproductible dans le modèle catalogue
dropshipping.

## Question

Existe-t-il une demande commerciale suffisante, une concurrence prouvée et un
espace différenciant testable sans copier un méga-catalogue ?

## Preuves actives

| Statut | Fait atomique | Source/date | Portée | Confiance |
|---|---|---|---|---|
| `OBSERVE_PROJET` | Le marché scrap possède des requêtes et SERP commerciales réelles | volumes + SERP — 2026-08-08 | demande | élevée |
| `MANQUANT_RENETTOYAGE` | Le total scrap 64 740 n'est pas reconstructible depuis les mesures conservées | JSON volumes + audit Phase 2 | demande scrap | élevée sur le manque |
| `OBSERVE_PROJET` | Les spécialistes stockistes occupent marques, rapidité, kits, tutoriels et collections coordonnées | panel concurrentiel + SERP | concurrence scrap | élevée |
| `OBSERVE_PROJET` | Scraperie décrit un fulfillment direct international et des colis séparés | FAQ + profil Scraperie | modèle comparable | élevée |
| `OBSERVE_PROJET` | Scraperie : 214 PDP publiques, AS 8, 58 trafic organique estimé, 32 mots-clés, 0 paid | sitemap + SEMrush France | traction comparable | élevée pour les observations |
| `HYPOTHESE_ETAYEE` | Un kit souvenir cohérent exige stock/kitting, preuve matière et expédition groupée | comparaison offre/fulfillment | right to win | élevée |
| `MANQUANT` | CPC actualisé, AOV, marge contributive, CPA de rupture et livraison SKU | — | économie | nulle |

## Décision par niche

| Niche | Gate 1 | Condition principale |
|---|---|---|
| Scrap/journaling | `STOP_PHASE_2` | Total demande propre non reproductible ; stockistes et marketplaces encadrent le marché ; comparable dropship sans traction prouvée ; angle défendable incompatible avec fulfillment multi-fournisseurs. |
| Mobilité chien | `STOP_PHASE_2` | Segment verrouillé par marques/spécialistes et généralistes ; logistique transport défavorable. |
| Mercerie | `STOP_PHASE_2` | Profondeur/stock local, faible ticket et ancienneté des acteurs rendent le modèle non défendable. |
| Perles/bijoux | `SUSPENDU_PHASE_2` | Étude profonde et économie du panier composé manquantes. |
| Aquascaping | `STOP_PHASE_2` | Vivant moteur de valeur ; angle pédagogique déjà pris ; matériel de marque/stock/logistique non réplicable en drop. |

## Risques et contradictions

- Une demande élevée ne garantit pas un angle rentable.
- Le nombre de produits n'est pas une autorité : Scraperie possède 214 PDP
  publiques pour 58 visites organiques estimées ; Boutiquechien montre le même
  pattern à plus grande échelle.
- La méthode V3 autorise une PDP à volume zéro, mais ne permet pas d'accepter un
  total de niche dont le nettoyage n'est pas reproductible.
- Le positionnement souvenir-first existe déjà chez Fée du Scrap, Florilèges
  et Scraperie ; il n'est pas différenciant par lui-même.
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
| 1 | Phase 2 profonde perles/bijoux | Codex | A | profils, SERP, mots-clés, panier, angle et verdict |
| 2 | Choisir le premier site parmi les seuls `GO` | Hakim + Codex | A | décision enregistrée, sans sourcing préalable |
| 3 | Si perles est aussi `STOP`, arbitrer nouvelle idéation France, marque/stock-kitting, candidats high-ticket ou marché étranger | Hakim + Codex | A | voie suivante explicitement choisie |

## Date de revue

Après le verdict perles. Aucun sourcing n'est lancé pour forcer un dossier
arrêté.

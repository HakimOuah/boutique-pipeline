# Rapport Gate 1 — marché, concurrence et right to win

**Projet :** Étude concurrentielle cinq niches Kraken
**Date :** 2026-08-08
**Décision :** `GO_CONDITIONNEL` — priorité de test : scrap/journaling

## Question

Existe-t-il une demande commerciale suffisante, une concurrence prouvée et un espace différenciant testable sans copier un méga-catalogue ?

## Preuves

| Statut | Fait atomique | Source/date | Portée | Confiance |
|---|---|---|---|---|
| `OBSERVE_PROJET` | Les cinq niches dépassent 30 k recherches nettoyées ; quatre dépassent 40 k | rapport qualification — 2026-08-08 | demande | élevée |
| `OBSERVE_PROJET` | Les leaders SEO et catalogues sont identifiés sur 15 domaines SEMrush | snapshot SEMrush — 2026-08-08 | concurrence | élevée |
| `OBSERVE_PROJET` | 20 marques disposent de métriques catalogue/Meta BrandSearch | snapshot BrandSearch — 2026-08-08 | concurrence | élevée |
| `OBSERVE_PROJET` | Un seul probable dropshipper, Boutiquechien, mais aucun fournisseur prouvé | profil Boutiquechien — 2026-08-08 | modèle | moyenne |
| `HYPOTHESE` | Une navigation projet/scénario + compatibilité + preuve crée un right to win | étude consolidée — 2026-08-08 | offre | moyenne/élevée |
| `MANQUANT` | AOV, marge contributive, CPA de rupture et livraison SKU | — | économie | nulle |

## Décision par niche

| Niche | Gate 1 | Condition principale |
|---|---|---|
| Scrap/journaling | `PRIORITE_TEST` | Valider kit modulable, licences et économie du panier. |
| Mobilité chien | `GO_CONDITIONNEL` | Première vague non critique + taille/logistique prouvées. |
| Mercerie | `GO_CONDITIONNEL` | Wedge projet étroit ; ne pas concurrencer les tissus génériques. |
| Perles/bijoux | `GO_CONDITIONNEL` | Compatibilité, composition et AOV low ticket. |
| Aquascaping | `GO_CONDITIONNEL` | Produits secs non électriques ; conformité et compatibilité renforcées. |

## Risques et contradictions

- La demande élevée ne garantit pas un angle rentable ; la mercerie illustre ce conflit.
- Le nombre de produits n’est pas une autorité SEO : Boutiquechien a 1 308 produits et 151 visites organiques estimées.
- Les 118–130 IDs par niche répondent à la première salve demandée, pas au seuil de 200 produits publiables.
- BrandSearch et SEMrush sont directionnels et peuvent diverger sans contradiction : ils estiment des objets différents.

## Conditions de passage

- [ ] Choisir une niche de test avec Hakim.
- [ ] Shortlister 20–30 produits cohérents et éliminer le bruit API.
- [ ] Vérifier variante, stock, coût rendu, délai, composition et conformité.
- [ ] Calculer AOV, marge contributive et CPA de rupture pour un panier type.
- [ ] Tester project-first contre product-first sur une landing sans dépense non autorisée.

## Actions

| Priorité | Action | Responsable | Classe | Preuve de fin |
|---:|---|---|---|---|
| 1 | Valider l’ordre de test et le wedge | Hakim | A | décision enregistrée |
| 2 | Shortlist produits de la niche choisie | Codex + Hakim | A/B | 20–30 lignes validées |
| 3 | Probes AliExpress exacts France | Codex | A | SKU/fret/stock par ligne |
| 4 | Modèle économique du panier | Codex + Hakim | A/B | CAC rupture calculé |
| 5 | Concept landing + protocole | Codex | B | maquette + test card |

## Date de revue

Après choix de la niche ou dès que l’économie et le sourcing exacts sont disponibles.

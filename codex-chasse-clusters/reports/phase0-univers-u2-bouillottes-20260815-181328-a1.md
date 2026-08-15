# Phase 0 — U2 Bouillottes

- Run : `20260815-181328`
- Date : 2026-08-15
- Base : SEMrush France (`db=fr`), USD
- Mode : `catalogue-volume`
- Statut : `SEUIL_VOLUME_FRANCHI_STOP_PRIX_PANIER_A_INSTRUIRE`

## OBSERVE

| Requête représentative | Intention | Volume FR/mois | KD | CPC USD | Famille provisoire |
|---|---:|---:|---:|---:|---|
| bouillotte | I | 27 100 | 31 | 0,12 | générique |
| bouillotte micro onde | I | 8 100 | 14 | 0,11 | micro-ondable / sèche |
| bouillotte électrique | C | 6 600 | 24 | 0,15 | électrique |
| bouillotte peluche | I | 4 400 | 13 | 0,21 | peluche |
| bouillotte noyau de cerise | C | 3 600 | 25 | 0,10 | sèche, noyaux |
| bouillotte graine de lin | I | 2 900 | 15 | 0,14 | sèche, graines |
| bouillotte sèche | I | 1 900 | 13 | 0,14 | sèche, terme parent |
| bouillotte cervicale | I | 1 300 | 23 | 0,11 | forme/usage |
| chausson bouillotte | I | 1 300 | 12 | 0,09 | chauffe-pieds |

Un minimum prudent sans synonymes accentués ni requêtes de marque atteint 42 600 recherches/mois avec `bouillotte` + `électrique` + `peluche` + `sèche` + `cervicale` + `chausson`. Les familles noyaux/graines/micro-ondes se recouvrent fortement et ne sont pas ajoutées à ce minimum.

## RETIRE / A RETIRER

- Marques/distributeurs : Action, Gifi, Amazon, Nature & Découvertes, Warmies, Pelucho, Carrefour, Leclerc.
- Requêtes santé/condition observées (`colique bébé`, règles) : ne pas utiliser pour des allégations ; vérifier intention produit sans promesse médicale.
- Les variantes orthographiques et synonymes d'une même famille ne deviennent pas des collections séparées.

## MANQUANT

- Graines `chaufferette`, `coussin chauffant`, `plaid chauffant`, `chauffe-pieds` hors formulations bouillotte.
- Lecture SERP commerciale des têtes.
- Sonde de 30–50 prix, médiane, part sous 15 EUR et mécanisme de panier réellement observé.
- Exigences de sécurité exactes par type de produit.

## HYPOTHESE

- Le volume paraît suffisant mais le faible CPC et le ticket présumé bas ne prouvent aucune économie viable.

## Sortie

`GO_ETAPE_2_SOUS_CONDITION` : priorité absolue au gate `STOP_PRIX_PANIER`. Aucun sourcing avant résultat prix/panier et concurrence.

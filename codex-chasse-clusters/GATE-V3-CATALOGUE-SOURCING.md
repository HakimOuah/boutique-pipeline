# Gate V3 — catalogue et sourcing Kraken

**Statut :** règle active du mode `catalogue-volume`, décision Hakim du
2026-08-08. Le run V2 reste une archive de preuve ; son gate par PDP est
supplanté pour les futurs catalogues.

## Séquence obligatoire

```text
mesure express France + sonde prix/panier
→ SERP, concurrence et différenciation
→ étude concurrentielle profonde
→ verdict
→ architecture chiffrée
→ sourcing catalogue
```

- `STOP` ou `SUSPENDU_PHASE_2` : aucun sourcing.
- En `catalogue-volume`, échantillonner 30–50 prix cœur avant l'étude profonde.
  Si le catalogue est ancré autour de 5–10 EUR sans panier multi-produits
  crédible, `STOP_PRIX_PANIER` ; les 200 produits ne sauvent pas la commande.
- Un concurrent comparable isolé valide le modèle et ne déclenche pas un
  `STOP`. Juger ensuite la densité, les actifs défensifs et l'espace exécutable.
- Réouverture : nouvelle qualification via `/qualifie-idees`, avec preuves
  mises à jour.
- Un listing fournisseur intéressant ne remplace jamais un verdict marché.

## Gate collection

Une collection est admissible si son intention commerciale est mesurée en
France, datée, nettoyée et dédupliquée, si sa SERP/prix/concurrence soutient un
droit de gagner, et si sa famille est suffisamment profonde chez les
fournisseurs.

- boutique : 30 000 recherches commerciales propres minimum ; 40 000+ confort ;
- collection cœur : 1 000+ ; bande de revue 800–999 ;
- collection secondaire : 500+ ; bande de revue 300–499 ;
- prix et CPC relevés sur la même intention ; ratio `prix moyen / CPC` ≥ 100,
  cible 150–200 comme heuristique, jamais comme preuve de marge.

La profondeur de 200 se démontre au niveau des familles et du catalogue total.
Elle ne demande pas 200 jumeaux concurrents.

## Gate produit

Un candidat compte pour la constitution du catalogue s'il :

1. appartient à une collection validée ;
2. représente un concept fonctionnel distinct d'une simple variante de
   couleur, taille, quantité, marque ou modèle ;
3. possède un listing fournisseur réel et sémantiquement pertinent avec au
   minimum ID/URL, titre et prix observés ;
4. utilise un mot-clé PDP descriptif et fidèle — le volume peut être positif ou
   égal à zéro, mais jamais inventé ;
5. passe une revue humaine produit ↔ collection ↔ listing.

Un équivalent concurrent est un bonus de confiance, pas une obligation. Le
listing reste `FOURNISSEUR_CANDIDAT` jusqu'à la vérification exacte du SKU, de
la variante, du stock, du coût rendu France, du délai, du contenu du colis, de
la conformité et de l'économie.

## Construction du catalogue

- 200 produits distincts au total boutique ;
- 10–20 produits par sous-catégorie ;
- ouverture ultérieure d'une catégorie autour de 10 produits ;
- cadence enseignée : au moins 20 ajouts par mois à l'échelle de la boutique.

Ordre de sélection `DECISION_PROJET`, non additif :

1. 5–8 best-sellers fournisseur pertinents ;
2. 3–5 équivalents/fonctions observés chez les concurrents ;
3. 3–5 références construisant une échelle de prix ou d'usage ;
4. 2–4 produits descriptifs ou longue traîne cohérents.

La sélection finale reste limitée à 10–20 références réellement distinctes.

## Sources de formation

- `vimeo-caption-231588620` [00:05:41–00:05:57] — seuils 1 000/150 ;
- `vimeo-caption-234186329` [00:01:21–00:03:29] — ratio prix/CPC ;
- `vimeo-caption-231663690` [00:00:42–00:00:50] et
  [00:07:52–00:07:59] — concurrence pour catégories et mots-clés ;
- `vimeo-caption-231588530` [00:00:11–00:00:56] et
  [00:02:30–00:03:46] — 200 total, cadence et ouverture de catégorie ;
- `vimeo-caption-232117442` [00:01:49–00:02:34] — 10–20 produits et choix par
  le marché ;
- `vimeo-caption-246208721` [00:08:02–00:10:17] — mots-clés zéro conservés
  lorsqu'ils précisent la collection.

Les timecodes sont `ENSEIGNE_A_VERIFIER`. Les seuils 30k/40k/500 ±200, la
séquence de blocage, l'ordre 80/20 et la revue humaine sont `DECISION_PROJET`.

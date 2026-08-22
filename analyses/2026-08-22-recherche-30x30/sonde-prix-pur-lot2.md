# Sonde prix Google Shopping France — idées PUR, lot 2 (survivants lots 2–3)

**Date : 22/08/2026.**

## Incident méthodologique — accès Google Shopping bloqué dans cet environnement

Avant de lire le premier prix, le protocole de la sonde impose : *« Si Google renvoie un CAPTCHA ou bloque la lecture, déclare-le et rends INDÉTERMINÉ — tu n'improvises pas avec une autre source. »* C'est exactement ce qui s'est produit ici, et il faut le déclarer sans détour plutôt que de maquiller la sonde suivante avec des données de substitution.

Cette exécution tourne comme **agent cloud** (pas la session locale habituelle). Dans cet environnement :

- Aucun outil de navigateur (CDP / Playwright) n'est disponible — seulement un outil de fetch HTTP passif.
- Trois tentatives de lecture directe de Google Shopping France ont toutes échoué :
  - `WebFetch` sur `google.com/search?...tbm=shop&gl=fr&hl=fr` → page interstitielle **« Nos systèmes ont détecté un trafic exceptionnel… »** (CAPTCHA), horodatée `2026-08-22T03:06:06Z`.
  - `WebFetch` sur `google.com/search?...udm=28&gl=fr&hl=fr` → timeout.
  - `curl` avec user-agent navigateur réaliste sur la même URL → HTTP 200 mais réponse = challenge JavaScript/preuve-de-travail (`window.google.c`, script de résolution côté client), impossible à satisfaire sans moteur JS réel ; aucun prix affiché.
  - `shopping.google.com/search?...` → page « mettez à jour votre navigateur », même blocage.

**Conclusion méthodologique : aucun prix ci-dessous ne provient d'une lecture d'écran Google Shopping.** Conformément au protocole, **les 7 verdicts sont donc `INDÉTERMINÉ`** — la règle de l'asymétrie interdit explicitement de transformer une lecture bloquée/absente en `LOW-TICKET`, et une lecture non faite ne peut pas non plus fonder un `DANS LA TRANCHE`.

Pour ne pas rendre ce lot totalement inutile au pipeline, un signal de prix **non qualifiant** a été rassemblé par recherche web classique (comparateurs de prix — idealo, Boulanger, E.Leclerc, Cdiscount, guides de prix travaux/hellopro — pas Google Shopping). Ce signal est indiqué à titre indicatif uniquement, avec sa source, et **ne doit pas être traité comme la donnée de prix autorisée de la phase 2** au sens du brief — il ne fait que motiver le classement `INDÉTERMINÉ` (continuation) au lieu d'un `LOW-TICKET` hâtif, et documenter ce qu'il faudra vérifier en Google Shopping réel avant la phase suivante.

**Recommandation opérationnelle :** relancer cette sonde depuis un environnement avec accès navigateur réel (session locale avec le skill `browser-use`, ou tout outil équipé de CDP) avant de trancher `LOW-TICKET` sur l'un de ces 7 candidats.

## Tableau consolidé

| # | Produit | Formulation visée | Signal de prix non qualifiant (source secondaire, PAS Google Shopping) | Verdict | Motif |
|---|---|---|---|---|---|
| 1 | Tente gonflable / tente glamping | `tente gonflable glamping` | ~290–400 € pour les tentes gonflables VEVOR (3-5 et 5-8 pers.) ; les « tentes glamping » au sens large (yourtes, tentes cloche en coton) vont de 300 € à plus de 3 000 € (guide hellopro, 08/2026) ; un modèle premium (Coody Bestona) à 2 042 € | **INDÉTERMINÉ** | Accès Google Shopping bloqué (CAPTCHA) ; en plus la formulation mélange deux univers produit distincts (tente gonflable technique vs tente glamping/cloche en toile) qu'une vraie lecture Shopping devra séparer |
| 2 | Machine sous vide alimentaire | `machine sous vide alimentaire` | Grand public : 30 € (Listo LASV1, Boulanger/Auchan) à ~240 € (FoodSaver FFS016X) ; comparateur idealo étale l'essentiel entre 35 € et 240 €, rares références au-delà (Caso FastVac ~376 €) ; machines « à cloche » pro : 375 € à plus de 4 700 € (registre restauration/chantier) | **INDÉTERMINÉ** | Accès bloqué ; signal secondaire suggère un cœur grand public sous 250 €, avec risque `LOW-TICKET` réel (nombreuses références sous 60 €) à confirmer en Shopping |
| 3 | Parc bébé | `parc bébé` | Segment tissu/maille : 20–90 € (Cdiscount, avis-parents.com) ; segment bois : 130–330 € (parcbebe.com : 159,99 à 329,99 €) | **INDÉTERMINÉ** | Accès bloqué ; le schéma bimodal (générique bas + bois premium) ressemble au cas couverture lestée du lot 1, qui avait donné `DANS LA TRANCHE` — à vérifier en Shopping avant de trancher |
| 4 | Tarière thermique | `tarière thermique` | Entrée de gamme 150–200 € ; semi-pro 200–400 € ; pro 400–1 000 €+ (hellopro, ma-tariere.com, alp2m.fr, convergents) | **INDÉTERMINÉ** | Accès bloqué ; le signal prix pointerait plutôt `DANS LA TRANCHE`, mais le vocabulaire des sources (location, chantier, poseurs de clôtures, professionnels du paysage) porte un signal de persona pro (§3 des critères) que la phase suivante devra lire — hors périmètre de cette sonde |
| 5 | Kettlebell | `kettlebell` | Poids unitaires fonte/plastique : ~9–90 € selon charge (Decathlon Pro, PowerGym, Gorilla Sports) ; kettlebells réglables/compétition : 159–280 € (Gorilla Sports 159,99 €, PowerGym 199–279 €, Fitness Boutique 199 €) | **INDÉTERMINÉ** | Accès bloqué ; forte suspicion de marché à dominante `LOW-TICKET` sur la requête tête (poids fixe, très nombreuses offres sous 50 €), avec un sous-segment réglable dans la tranche — distribution réelle à lire en Shopping avant tout verdict |
| 6 | Humidificateur d'air | `humidificateur d'air` | Entrée de gamme ultrasonique : 20–90 € (E.Leclerc, Boulanger) ; segment marque établi : 90–400 € (Stadler Form Oscar 166 €, Philips 2000i 395 €, Clean Air Optima 349 €) ; connecté haut de gamme (Dyson) 600–700 € | **INDÉTERMINÉ** | Accès bloqué ; le signal secondaire dessine le même schéma que ventilateur colonne/couverture lestée (lot 1, `DANS LA TRANCHE`) — probable mais non lu à l'écran |
| 7 | Récupérateur d'eau de pluie (cas limite) | `récupérateur d'eau de pluie` | Modèles hors-sol simples : 50–500 € (souvent cité 80–500 € ou 100–500 €) ; cuves IBC 1000 L : 70–250 € ; cuves enterrées avec pose : plusieurs milliers d'euros (registre installation/artisan, hors périmètre produit pur) | **INDÉTERMINÉ** | Accès bloqué ; produit déjà signalé « cas limite » par l'appelant — le signal secondaire est dominé par des devis de pose (persona pro/travaux), pas par un objet acheté en ligne ; distribution réelle des offres produit à vérifier en Shopping |

## Rappel des limites de cette sonde

- **Aucune lecture Google Shopping n'a été effectuée** pour ce lot — voir l'incident méthodologique ci-dessus. Les 7 verdicts sont `INDÉTERMINÉ` par construction, pas par choix éditorial.
- Les fourchettes indiquées dans la colonne « signal de prix non qualifiant » viennent de comparateurs (idealo, Boulanger, E.Leclerc, Cdiscount) et de guides de prix travaux (hellopro, ma-tariere.com, alp2m.fr) — pas de Google Shopping, pas de fiche produit visitée dans une intention d'achat.
- Aucun verdict marché, aucune analyse de concurrence : ce fichier ne fait que documenter un blocage technique et transmettre un signal indicatif pour ne pas perdre le travail déjà fait.
- **Action requise avant la phase 2 pour ces 7 candidats :** relire ces mots-clés sur Google Shopping France depuis un environnement avec navigateur réel, en respectant la méthode standard (`tbm=shop`/`udm=28`, `gl=fr&hl=fr`, aucun site marchand visité).

# Lumière Matière — Tableau

## Bloqué

### T-01 — Produire les visuels de variantes du 04/09/2026
**État** : BLOQUÉ POUR LE SOLDE — complément vérifié par Codex le 04/09/2026 : 26 packshots + 8 schémas (3 complets, 5 partiels), 20 manifestes, QA technique 34/34. Aucune publication.
**Pour** : Codex
**Pourquoi** : montrer les couleurs, formes et dimensions réelles des variantes.
**Comment** : contrôler les sources locales des lots P1/P2/P6 ; établir les correspondances avant génération ; produire et vérifier les JPEG et manifestes.
**Sortie attendue** : livraison dans `livraisons-visuels-codex/variantes-forme/`, provenance et QA, compte rendu dans `journal/`.
**Attention** : aucune correspondance ni cote inventée ; SKU DSers inchangés. Les arbitrages 272937 et 607504 sont **rendus** (04/09, cf. `journal/2026-09-04-arbitrages-titres-variantes.md`).
**Réf.** : [Brief](briefs/2026-09-04-codex-variantes-formes.md), les trois JSON associés.

**Compte rendu actuel** : [Complément et décisions restantes](journal/2026-09-04-variantes-formes-complement.md), [registre et prompts](journal/2026-09-04-variantes-formes-registre.json), [QA 34/34](journal/2026-09-04-variantes-formes-qa.json). Le premier compte rendu à 15 images reste une archive.

**Pour débloquer le solde** :

1. ~~Arbitrer 272937~~ **FAIT 04/09** : titre → « Plafonnier cuisine, dôme en corde tressée », `productType` → Plafonniers, sortie de `suspensions-rotin`/`suspensions-cuisine`, entrée en `plafonniers-cuisine`. Les 8 visuels du lot 3 restent à produire ; ne pas supprimer ses 5 montages avant livraison (elle resterait sans image).
2. ~~Arbitrer 607504~~ **FAIT 04/09** : libellés renommés avec la finition, option → « Taille et finition », titre → « Suspension rotin tressé cuisine, monture bois » (il annonçait « noir » pour 1 variante sur 4). Le brief Codex donnait un mapping identifiant → code **inversé**, corrigé sur les preuves DOM et les SKU. Schéma coté + packshot noir désormais débloqués.
3. Fournir la photo liée au SKU A `200000531:193` de 338324, absent du sélecteur fournisseur actuel. B/C/D livrés, sans déduction de A.
4. Compléter les cotes des cinq schémas partiels : 330664, 246282, 761433, 377816, 630923 (détail au compte rendu).

**Débloqué par les preuves SKU** : 975417, B/C/D de 338324, 147607, 560098, B/C de 253182, les deux finitions de 092465, rotin de 897170 et montages 795468/630923. Captures de 16 fiches fournisseur ; correspondance par identifiants, pas par lettres réinterprétées.

**Correction intégrée** : 405368 Beige et blanc = A2 (SKU confirmé dans le brief corrigé 52a9f80). Le rendu D1 vert a été écarté, A2 régénéré avec disque blanc et câble blanc. Aucun arbitrage restant sur son nom.

## Fait pour cette passe

Précontrôle des 20 fiches, recherche des preuves dans les sélecteurs fournisseur, 34 éléments exploitables déclarés, schémas à échelle calculée pour les cotes connues, QA locale et documentation. Les packshots ne sont pas des comparatifs métriques. Le lot global n’est pas marqué FAIT car les blocages ci-dessus restent ouverts.

Ce tableau suit cette intervention uniquement ; il ne prétend pas inventorier les autres chantiers ou l’état live de la boutique.

### T-02 — Header desktop : menu à 4 entrées, logo visible
**État** : EN COURS — navigation à 5 entrées sur le live (logo revenu, une ligne, « Aide & contact » regroupe les liens de confiance GMC) ; thème `LM UX 2026-09-04` prêt avec logo horizontal et allumage au survol, **publication par Hakim**. Garde-fou : ne jamais dépasser 5 entrées de premier niveau.
**Pour** : Hakim (navigation + personnalisateur), ou Cursor sur copie de thème.
**Pourquoi** : le menu à 10 entrées écrase la colonne du logo à 0 px et passe sur deux lignes.
**Comment** : `shopify/AUDIT-UX-UI-2026-09-04.md` §1 — cible à 5 entrées, utilitaires vers le footer et une icône « suivi », puis layout « logo à gauche, menu à gauche » en filet. Ensuite §3 (liste canonique des matières) et §6 (hero et bandeau mobile).
**Attention** : aucun signal GMC touché ; thème sur copie non publiée, publication par Hakim.

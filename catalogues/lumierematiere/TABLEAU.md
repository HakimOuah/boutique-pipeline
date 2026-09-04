# Lumière Matière — Tableau

## Bloqué

### T-01 — Produire les visuels de variantes du 04/09/2026
**État** : BLOQUÉ POUR LE SOLDE — complément vérifié par Codex le 04/09/2026 : 26 packshots + 8 schémas (3 complets, 5 partiels), 20 manifestes, QA technique 34/34. Aucune publication.
**Pour** : Codex
**Pourquoi** : montrer les couleurs, formes et dimensions réelles des variantes.
**Comment** : contrôler les sources locales des lots P1/P2/P6 ; établir les correspondances avant génération ; produire et vérifier les JPEG et manifestes.
**Sortie attendue** : livraison dans `livraisons-visuels-codex/variantes-forme/`, provenance et QA, compte rendu dans `journal/`.
**Attention** : aucune correspondance ni cote inventée ; SKU DSers inchangés. Les arbitrages 272937 et 607504 sont **rendus** (04/09). Lot 3 **importé**, tous les libellés aveugles du catalogue **réécrits** (04/09). Lot 4 **A1 importé 13/13** (T-04) ; **17 A2 + 10 B livrés localement, C documenté** (T-05). Deux images supplémentaires nécessaires sur 183789, en attente d'accord (T-06).
**Réf.** : [Brief](briefs/2026-09-04-codex-variantes-formes.md), les trois JSON associés.

**Compte rendu actuel** : [Complément et décisions restantes](journal/2026-09-04-variantes-formes-complement.md), [registre et prompts](journal/2026-09-04-variantes-formes-registre.json), [QA 34/34](journal/2026-09-04-variantes-formes-qa.json). Le premier compte rendu à 15 images reste une archive.

**Pour débloquer le solde** :

1. ~~Arbitrer 272937~~ **FAIT 04/09** : titre → « Plafonnier cuisine, dôme en corde tressée », `productType` → Plafonniers, sortie de `suspensions-rotin`/`suspensions-cuisine`, entrée en `plafonniers-cuisine`. Les 8 visuels du lot 3 sont livrés localement (T-03) ; remplacer les 5 montages lors de l'import, pas avant.
2. ~~Arbitrer 607504~~ **FAIT 04/09** : libellés renommés avec la finition, option → « Taille et finition », titre → « Suspension rotin tressé cuisine, monture bois » (il annonçait « noir » pour 1 variante sur 4). Le brief Codex donnait un mapping identifiant → code **inversé**, corrigé sur les preuves DOM et les SKU. Schéma coté + packshot noir désormais débloqués.
3. 338324 A `200000531:193` : absent au lot3 et au nouveau contrôle lot4. **Débloqué par le brief lot4** : identité reconstituée autorisée (grille fournisseur +05.jpg), packshot bas bois clair livré localement (T-04). Ne pas présenter cette cellule comme observée au DOM ; B/C/D conservés.
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

### T-03 — Remplacer les montages fournisseur (lot 3)

**État** : FAIT LOCAL — 16/16 JPEG RGB2048², contrôle « un seul luminaire dans le cadre », 7 manifestes et planche QA. Aucun import ni changement Shopify/DSers par Codex.
**Livraison** : `livraisons-visuels-codex/montages-2026-09-04/` ; [compte rendu](journal/2026-09-04-lot3-montages.md), [registre](journal/2026-09-04-lot3-registre.json), [QA](journal/2026-09-04-lot3-qa.json).
**Produit** : 272937 = 5 vues A + 3 variantes modele-a/b/c ; 560098 = 5 vues A simple ; 147607 = g1/g2/g5 forme A. Anciens fichiers locaux et packshots validés conservés.
**D/E résolus** : 338324 A introuvable après dernière passe ; 837156 « 2 » = autre abat-jour H9 contre H6,5, même Ø20, dans les deux couleurs. Pas d'image produite pour D/E.
**Périmètre** : F sans action. G non produit dans les 16 images explicitement demandées ; le renommage consigné en parallèle débloque désormais ses 2 visuels complémentaires (voir arbitrages), non inclus dans cette livraison.

### T-04 — Couvrir les formes et finitions de variantes (lot4 A1)

**État** : **FAIT ET IMPORTÉ** — production Codex 13/13 le 04/09 soir, **importée en boutique dans la foulée** (`journal/2026-09-05-import-lot4-a1.md`). Chaque variante des 5 fiches porte désormais sa propre image, appariée par SKU. 2 packshots périmés de `837156` supprimés. Libellés de `193329` renommés sur les cotes prouvées, titre de `630923` corrigé (2 variantes sur 3 sont des plafonniers). Contrôle : 52 produits / 158 variantes / SKU DSers intacts.
**Pour** : clos.
**Vérifié avant import** : les 4 fils du rendu « suspension » de `630923` sont fidèles à la référence `Pendant 50cm` ; les 2 images en ligne de `193329` sont bien la forme B haute. Les deux affirmations de Codex tiennent.
**Piège API rencontré** : une variante Shopify ne porte qu'**un seul** média — détacher, contrôler, **puis** attacher ; jamais les deux dans le même appel.
**Produit** : 607504 =4 ; 837156 =4 ; 630923 =2 ; 193329 =2 ; 338324 =1. Un seul luminaire dans le cadre.
**Identifications** : 193329 A=bas Ø12/H10, B=haut Ø11/H16,5 (4 références DOM récupérées). Deux A produits, deux B existants conservés. 338324/193 toujours absent : rendu reconstitué expressément autorisé par le brief.
**Attention** : 630923 plafonnier Ø50/60 partage un packshot sans échelle (le schéma coté du lot B le complétera). Résolution native1254² agrandie proportionnellement.
**À TRANCHER PAR HAKIM** : `193329` et `338324` vendent **le même article** (cylindre travertin Ø 12 × H 10 + forme haute, tête bois clair ou noyer) sur deux listings AliExpress distincts (`1005010522193329` / `1005008660338324`), **tous deux live à 199 €** et dans `selection-199`. Après cet import elles portent en plus des packshots quasi identiques. Garder laquelle ?
**Livraison** : `livraisons-visuels-codex/couverture-2026-09-05/`, `qa-couverture.jpg` ; [compte rendu](journal/2026-09-05-lot4-a1-couverture.md), [registre](journal/2026-09-05-lot4-a1-registre.json), [QA](journal/2026-09-05-lot4-a1-qa.json).

## À faire après cette passe

### T-05 — Traiter le solde du lot4 : A2, B et C

**État** : FAIT POUR LE QUOTA DEMANDÉ — 04/09 soir, 17 packshots A2 + 10 schémas B livrés localement, 2 réponses C documentées. Total 40 avec les 13 A1 inchangés, 21 manifestes, planche QA et contrôle RGB 2048². **Couverture réelle encore partielle sur 183789 : T-06.**
**Pour** : relais import séparé, aucune publication effectuée dans cette passe Codex.
**Pourquoi** : montrer les nombres de lumières, fournir l'échelle et résoudre les deux questions fournisseur restantes.
**Comment** : reprendre les sections A2/B/C du brief et leur JSON ; vérifier SKU/références avant chaque rendu. C : clarifier934110 et confirmer092465 avant toute nouvelle image.
**Sortie attendue** : jusqu'à17 packshots A2 +10 schémas B, deux réponses C ; compléter la livraison et ses manifestes sans remplacer les13 A1 validés.
**Attention** : SKU intouchables, aucune action Shopify/DSers. Aucune cote inventée ; schémas seuls autorisés à porter du texte. A1 importé selon T-04, les 27 nouveaux restent une livraison locale. C934110 mélange un tube travertin et deux tubes 3000/6000 K avec un second axe fixe 3000 K : incohérence fournisseur à clarifier. C092465 clair/brun confirmé.
**Livraison** : [Compte rendu](journal/2026-09-05-lot4-suite-couverture.md), [registre](journal/2026-09-05-lot4-suite-registre.json), [QA](journal/2026-09-05-lot4-suite-qa.json), `livraisons-visuels-codex/couverture-2026-09-05/qa-couverture.jpg`.
**Réf.** : [Brief lot4](briefs/2026-09-05-codex-lot4-couverture-variantes.md), [JSON](briefs/2026-09-05-lot4-couverture.json).

### T-06 — Compléter les deux versions à six palets de 183789

**État** : BLOQUÉ — accord Hakim demandé pour deux images supplémentaires, passage du plafond 40 à 42. Les anciens packshots gris/blanc comportent sept palets (six périphériques + centre), aucun SKU vendu ne leur correspond.
**Pour** : Hakim (accord), puis Codex (production locale).
**Pourquoi** : le brief comptait deux images existantes comme utilisables ; elles ne couvrent ni cinq ni six palets.
**Comment** : après accord, produire gris6 `200000795:366#grey 6 lights` et blanc6 `200000795:10#White  6 lights` depuis leurs références déjà collectées dans `sources-par-handle/plafonnier-led-led-183789/variantes-lot4-20260905/`. Compter cinq palets périphériques +un central. Conserver la finition/structure propre à chaque source.
**Sortie attendue** : ajouter deux entrées au manifeste, actualiser registre et QA (42 au total). Les deux versions à cinq sont déjà livrées dans A2.
**Attention** : ne pas importer les anciens visuels à sept ; ne pas inventer six depuis cinq. Aucune mutation Shopify/DSers dans le mandat visuel.
**Réf.** : [Compte rendu du contrôle](journal/2026-09-05-lot4-suite-couverture.md), planche locale `qa-sources/plafonnier-led-led-183789.jpg`.

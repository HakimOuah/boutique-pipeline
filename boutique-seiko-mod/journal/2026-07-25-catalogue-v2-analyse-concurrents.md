# Catalogue v2 — étoffer NOIRMONT (analyse concurrents + plan) — 25/07/2026

Demande Hakim : « le catalogue est un peu maigre, inspire-toi des concurrents (montres ET accessoires) ».
Catalogues concurrents minés en direct le 25/07 : `montreapapy.fr/products.json` (111 fiches, capturé dans `scratchpad/concurrents/montreapapy-products.json`) et sitemap `goteia.fr` (34 fiches + 5 configurateurs).

## 1. Ce que font les concurrents

| | montreapapy.fr | goteia.fr | NOIRMONT aujourd'hui |
|---|---:|---:|---:|
| Fiches montres | **100** | **34** | **10** |
| Familles | 10 | 6 | 10 |
| Fiches accessoires | 5 | **0** | **15** |
| Prix d'entrée | 289-299 € | 349 € (prix unique) | 279-379 € |
| Prix max atteint | **501 €** (options) | 349 € | 379 € |

### La mécanique qui fait 100 fiches : une fiche = UN coloris
C'est le point central. Ils n'ont pas 100 montres différentes : ils ont **~10 familles déclinées coloris par coloris**, chaque coloris ayant sa propre page produit, son nom et ses photos.
- montreapapy : GMT ×13 (Pepsi, Coke, Batgirl, Sprite, Mr Wayne…), OAK ×18, NAUT ×16, DAYTO ×12, DJ ×9, SUB ×9, SKY ×7, SKX ×7, SEA ×6, BR ×4.
- goteia : seikojust ×7, seikoak ×6, seikos ×6, seikoriner ×5, seikolus ×5, seikona ×5.

**Nous faisons exactement l'inverse** : nous enfermons tous les coloris dans un menu déroulant d'une seule fiche. Notre chronographe contient 20 cadrans dans une liste « Référence M-1 … M20 » ; chez montreapapy, ces 20 cadrans seraient 12 pages nommées et photographiées. D'où l'impression de catalogue maigre — le stock d'offre existe déjà, il est juste invisible.

### Leur échelle de prix (montreapapy)
Les « variantes » de leurs fiches sont de faux produits : des paliers de prix (`mczr_price_299`, `mczr_price_338`…) pilotés par l'app de configuration. Base 289/299 € puis options à **+29, +39, +49, +78, +88, +117, +138, +167 €** → panier jusqu'à 501 €. La famille BR (Bell & Ross) démarre plus haut, à 349 €.

### Leur angle mort : les accessoires
montreapapy ne vend que 5 accessoires (gravure laser 20 €, cadran custom 24 €, 2 bracelets PRX 29 €, watch roll 48 €) + une **carte cadeau 50-500 €**. Goteia : zéro. **Avec 15 accessoires, nous sommes déjà largement devant** — c'est un terrain à creuser, pas un retard à rattraper.

## 2. Le gisement gratuit : nos coloris déjà sourcés

Chaque fiche fournisseur déjà importée contient sa matrice de coloris. Nombre de pages produit qu'on pourrait en tirer **sans aucun nouveau sourcing, sans toucher au mapping DSers** :

| Fiche actuelle | Coloris disponibles | Pages réalistes |
|---|---:|---:|
| Contre-la-montre — chrono panda (M-1…M20) | 20 | 8-12 |
| Voyageur — GMT (réf. 1-9) | 9 | 6-9 |
| Noirmont Deux — plongeuse céramique (réf. 1-7) | 7 | 5-7 |
| Trente-Neuf — cannelée (7 cadrans) | 7 | 5-7 |
| Intégrale — sport chic (réf. 1-7) | 7 | 4-7 |
| Trente-Six — jubilé (6 cadrans) | 6 | 4-6 |
| Quarante-et-Un — sport acier | 4 cadrans × 2 bracelets | 4 |
| Héritage — plongeuse vintage (S1-S3) | 3 | 3 |
| Trente-Neuf Duo — bicolore | 2 finitions × 2 tailles | 2-4 |
| Noirmont Un — plongeuse acier/bronze | 2 boîtiers | 2 |
| **Total** | **~69 coloris** | **~45 fiches** |

**Bénéfice double.** Ce n'est pas qu'une question de volume : aujourd'hui un client lit « Référence M14 » ou « Référence 3 » dans un menu déroulant — un code fournisseur qui ne veut rien dire et qui coûte des ventes. Le découpage remplace ça par des pages nommées et photographiées (« Contre-la-montre Panda », « Voyageur Pepsi »…), ce qui règle en même temps un défaut de qualité et le SEO longue traîne (chaque coloris est une requête).

**Coût réel du découpage** : ~2 visuels par nouvelle fiche (la photo du coloris existe côté fournisseur mais elle est hors charte). Environ 70-90 images à générer, soit un budget Higgsfield du même ordre que la passe actuelle. C'est le seul vrai coût — le mapping DSers, les prix et les variantes techniques (mouvement, fond, diamètre) restent inchangés dans chaque nouvelle fiche.

## 3. Les familles qui nous manquent vraiment

Comparé aux deux concurrents, il nous manque 5 familles + 1 style de cadran (sourcing lancé le 25/07, agents en cours) :

| Famille | Chez le concurrent | Intérêt |
|---|---|---|
| **OAK** (Royal Oak, octogonale) | 18 fiches montreapapy + 6 goteia | La plus vendue chez eux et absente chez nous. Un rapport de juillet concluait « pas d'offre stérile » → re-sourcing demandé, y compris chrono et squelette |
| **SKY** (Sky-Dweller) | 7 fiches | Cadran à guichets, haut de gamme perçu |
| **SEA** (Seamaster / 007) | 6 fiches | Plongeuse alternative, très demandée |
| **SKX** (vraie base Seiko) | 7 fiches | Seule vraie Seiko : crédibilité de marque, colle au mot-clé « seiko mod » |
| **BR** (Bell & Ross, carrée) | 4 fiches à **349-466 €** | Monte le panier moyen |
| **Open heart / squelette** | présent chez les deux | Style à fort effet visuel, peut décliner une famille existante |

## 4. Accessoires — compléter là où nous sommes déjà devant

Sourcing lancé le 25/07 sur les manques identifiés :
- **Bracelets seuls** (le réachat n°1, et nous n'avons que président/FKM) : jubilé, oyster, milanais, NATO, cuir à boucle déployante, tropic/waffle, et le type **PRX intégré** que montreapapy vend 29 €.
- **Rangement** : coussin de présentation, étui 2-3 montres (plus petit que notre rouleau), coffret 6 montres (nous n'avons que 12 et 24), présentoir/chevalet.
- **Outils & entretien** : ouvre-boîtier, kit nettoyage, outil de mise à taille de bracelet, loupe d'horloger.

**À ajouter aussi, coût nul : la carte cadeau** (montreapapy en vend une de 50 à 500 €). C'est un produit natif Shopify, sans stock ni SAV, et un vrai levier Q4 sur un produit à 300 € qu'on offre.

## 5. Plan proposé

| Étape | Contenu | Fiches gagnées | Dépend de |
|---|---|---:|---|
| **A** | Découpage des coloris déjà sourcés en fiches nommées + visuels | +35 | budget images |
| **B** | Nouvelles familles (OAK, SKY, SEA, SKX, BR, open heart) | +20 à 30 | rapport de sourcing + import DSers (Hakim) |
| **C** | Accessoires complémentaires | +12 à 15 | rapport de sourcing + import DSers (Hakim) |
| **D** | Carte cadeau Q4 | +1 | rien (natif Shopify) |

Cible : **~100 fiches**, soit l'ordre de grandeur de montreapapy, avec un catalogue accessoires que ni lui ni Goteia n'ont.

Ordre recommandé : **A d'abord** (aucun sourcing, aucune dépendance, et corrige le défaut « Référence M14 »), puis D (gratuit), puis B et C quand les rapports de sourcing sont validés et les produits importés dans DSers.

## Décisions Hakim (25/07)
1. **Ampleur du découpage : maximale** — on vise tous les coloris exploitables (~45 fiches).
2. **Naming des coloris : communautaire** (Pepsi, Batman, Hulk, Panda, Wimbledon…) pour que le modèle soit identifiable au premier coup d'œil, comme chez les concurrents. Garde-fou inchangé : le naming décrit un coloris, **jamais un logo** — la règle 100 % stérile sur les produits et les visuels reste absolue.
3. **Facturer les mouvements haut de gamme : oui** (« ça ajoute du crédit à la marque »). ✅ APPLIQUÉ le 25/07, voir ci-dessous.

## ✅ Échelle de prix par mouvement & fond — APPLIQUÉE (25/07)

Règle retenue, alignée sur la mécanique concurrente (base + options) : **le prix d'entrée de chaque montre reste inchangé**, seules les configurations premium montent.

| Option | Uplift |
|---|---:|
| Mingzhu 2813 / Miyota 8215 / DG3804 (GMT) | base |
| **Seiko NH34 / NH35 / NH36** | **+39 €** |
| **PT5000** (suisse-clone, 28 800 A/h, stop-seconde) | **+89 €** |
| **Fond verre / exhibition** | **+29 €** |

Prix barré recalculé à chaque palier (règle maison ×1,3 arrondi à l'entier supérieur en 9). **184 variantes mises à jour sur 7 produits, 0 erreur.** Les 3 fiches à option unique (chrono panda, Intégrale, Héritage) n'ont pas de choix de mouvement : prix inchangé. Script : `scratchpad/theme-noirmont/build_movement_ladder.py`.

Amplitudes obtenues (min → max par fiche) : Noirmont Un 289 → 407 · Noirmont Deux 299 → 388 · Voyageur GMT 349 → 417 · Trente-Six 299 → 328 · Trente-Neuf Duo 319 → 387 · Quarante-et-Un 299 → 338 · Trente-Neuf cannelée 329 → 397. On retrouve les paliers du marché (338, 378, 388) sans toucher au prix d'appel.

## ⚠️ Blocage identifié pour le découpage (étape A)

Deux obstacles techniques à lever avant de créer les fiches par coloris :

1. **Identification visuelle des coloris.** Les valeurs d'option sont des codes fournisseur opaques (« Référence M14 », « 9 », « S2 ») — impossible de savoir lequel est le Pepsi ou le Panda sans voir la photo. Les images AliExpress ont été supprimées de Shopify (nettoyage du 25/07) et **aucun lien vers la fiche fournisseur n'est stocké côté produit** (ni tag, ni métachamp — vérifié). Il faut donc rouvrir les fiches AliExpress d'origine pour cartographier référence → coloris réel. Les URL candidates sont dans `arborescence-site-2026-07-24.md` (le nombre de variantes permet de confirmer la correspondance) ; sinon elles sont dans DSers.
2. **Re-mapping DSers.** Un produit créé par l'API n'est lié à aucun fournisseur DSers. Chaque nouvelle fiche devra être mappée dans DSers (My Products → Mapping → coller l'URL AliExpress). Bonne nouvelle : **nos SKU contiennent la chaîne d'attributs AliExpress** (ex. `14:175#9;5:56964930#DG3804 GLASS back`), donc l'auto-matching des variantes devrait fonctionner. Coût estimé : 1-2 min par fiche pour Hakim, soit ~1 h pour 45 fiches.

Ordre d'exécution retenu : identification des coloris (agent, dès que le navigateur se libère) → validation du plan de nommage par Hakim → création des fiches + visuels → mapping DSers par Hakim.

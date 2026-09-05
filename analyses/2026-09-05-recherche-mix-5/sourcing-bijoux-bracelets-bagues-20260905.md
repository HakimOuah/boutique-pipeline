# Sourcing lecture seule — bracelets et bagues en pierres naturelles

**Date des contrôles : 5 septembre 2026 — France (FR).** PASS utilisé : `./PASS-bijoux-pierres.md`. Contrôles réalisés uniquement par la gateway AliExpress autorisée, sans navigateur, panier, contact ni commande. Neuf recherches distinctes ont été consommées au total (six initiales, deux extensions ciblées puis un essai lexical seul) ; aucune autre recherche n'a été relancée.

## Résultat exploitable

Deux vendeurs distincts ont une fiche bracelet complète avec un SKU réellement retourné, stock numérique, prix et fret France. Ils couvrent la famille **bracelets**. Aucun fournisseur bague avec pierre naturelle n'a été trouvé dans les six recherches ; la famille **bagues** reste sans offre qualifiée.

| Famille / vendeur | Preuve produit et SKU observé | Composition déclarée par la fiche | Coût observé vers FR | Stock / délai | Preuves vendeur | Statut |
|---|---|---|---:|---|---|---|
| Bracelet — **JD Gemstone Jewellry Factory Store** (CN, store `4474135`) | Produit `1005007510843875`; titre : bracelet de perles en pierre naturelle (améthyste, œil de tigre, quartz, agate…). SKU `12000041079430545` est bien retourné par `variants` pour la combinaison `Amethyst` + `8mm`, mais l'appel exact avec ces deux sélecteurs est ambigu (le matcher voit aussi `Dream Amethyst`). SKU finalement qualifié sans ambiguïté : `12000050871647256`, `Citrine` + `8mm`, `sku_attr=200000783:193#8mm;200001034:201706807#Citrine`. URL canonique depuis l'ID : [fiche AliExpress](https://fr.aliexpress.com/item/1005007510843875.html). | Valeur SKU `Citrine`, diamètre `8mm`; le titre déclare « pierre naturelle ». Aucun certificat ou composition minéralogique observé. Le titre comporte aussi « guérison Reiki » : claim exclu de tout positionnement. | Prix SKU **4,59 € TTC** + fret **1,99 €** = **6,58 € calculés** ; AliExpress Selection Standard, suivi, départ CN. | Stock **2** ; fenêtre gateway **10–15 sept.**, 5–10 jours max/min renseignés. | Ventes `5000+`; rating produit/evaluations renvoyés `0.0`/`0`; vendeur : article conforme `4,7`, communication `4,7`, vitesse `4,8`. | **FOURNISSEUR À TESTER**, sous réserve de revalider stock, composition et qualité. Ticket très bas et stock faible ; pas de commande autorisée. |
| Bracelet — **Shop1104951145 Store** (CN, store `1104951145`) | Produit `1005009727009606`; titre : bracelet pierre volcanique avec agate noire carrée. SKU unique `12000049962623231`, propriété retournée `1pc`, `sku_attr=200001034:200003699#1pc`. URL canonique depuis l'ID : [fiche AliExpress](https://fr.aliexpress.com/item/1005009727009606.html). | Le titre déclare « pierre volcanique » et « agate noire carrée » ; aucune preuve laboratoire. Le titre comporte « thérapie magnétique » : claim exclu de tout positionnement. | Prix SKU **1,91 € TTC** + fret **1,99 €** = **3,90 € calculés** ; AliExpress Selection Standard, suivi, départ CN. | Stock **13** ; fenêtre gateway **10–15 sept.**, 5–10 jours max/min renseignés. | Ventes `5000+`; rating produit/evaluations renvoyés `0.0`/`0`; vendeur : article conforme `4,6`, communication `4,7`, vitesse `4,7`. | **FOURNISSEUR À TESTER**, après vérification composition et retrait de tout claim santé. |

Les propriétés françaises incohérentes (« Couleur du métal » contenant le nom de pierre) sont conservées exactement comme retournées par l'API ; elles ne sont pas interprétées comme une preuve de métal ou de gemme. Le coût livré est une addition explicite du prix TTC et du fret affiché, pas une valeur native fournie par le vendeur.

## Bagues : non qualifiées

- `natural stone ring amethyst silver` (18:42:12 UTC) : résultats zircon/imitation, anneaux argent sans pierre naturelle, perles seules et bracelets ; aucune bague améthyste exacte.
- `lapis lazuli ring natural stone silver` (18:42:21 UTC) : mêmes familles hors cible ; aucune bague lapis exacte.
- L'appel exact améthyste du bracelet a été conservé comme `qualification_refused` pour ambiguïté ; il ne prouve aucune indisponibilité globale.

Aucun fournisseur bague ne peut donc être présenté comme plausible ou exploitable dans ce lot. Les deux preuves de prix public observées chez Moment Ici servent seulement de repères de marché et non de sourcing : [bague citrine 39 €](https://momentici.com/products/bague-citrine-abondance-doree-argent), [bague lapis-lazuli 39 €](https://momentici.com/products/bague-lapis-lazuli-mystere-nocturne-argent), [bracelet lapis-lazuli 79 €](https://momentici.com/products/bracelet-jonc-lapis-lazuli-harmonie-interieure), [bracelet lapis/aigue-marine 39 €](https://momentici.com/products/bracelet-lapis-lazuli-et-aigue-marine-poisson-de-bonheur). Observation Moment Ici datée du 05/09/2026 dans le rapport local ; livraison boutique et certificat éventuel ne sont pas des preuves fournisseur.

## Limites et décision de préqualification

- La demande « deux fournisseurs différents par famille » est satisfaite pour bracelets seulement, pas pour bagues.
- Les coûts sont plausibles pour un produit porté mais très inférieurs au ticket public observé ; marge, qualité, conformité matériaux, contenu du kit et retours restent non démontrés.
- Les claims « guérison Reiki » et « thérapie magnétique » ne doivent pas être repris. Aucun claim de soin ou d'effet physiologique n'est retenu.
- Le PASS autorise une due diligence, pas un `GO_FINAL`, une publication ou une commande test.

Les réponses brutes sont dans `sourcing-bijoux-bracelets-bagues-20260905/` : neuf recherches (dont les trois extensions en JSON complets), deux réponses `variants`, un échec exact ambigu et deux réponses `exact` réussies.

## Extension ciblée bagues — 5 septembre 2026

Deux recherches nouvelles ont été exécutées après le premier contrôle, puis arrêtées conformément au plafond :

- `labradorite ring natural stone silver` — 18:48:37 UTC : top résultats zircon/imitation, bague argent sans pierre, acier/titane, perles DIY et bagues sans pierre naturelle ; aucun produit labradorite cohérent.
- `lapis lazuli ring natural stone 925` — 18:48:46 UTC : top résultats zircon/imitation, bagues argent sans pierre naturelle, collier initial et perles DIY ; aucun produit lapis cohérent.

Aucun SKU de bague pierre annoncé de façon cohérente n'a été retourné. Il n'y a donc eu **aucun appel variants/exact supplémentaire** et aucun second fournisseur bague plausible. La famille bagues reste bloquée après ces deux requêtes ciblées ; les deux fournisseurs bracelets ne sont pas détournés pour remplir ce quota. Les fichiers bruts de l'extension sont `search-labradorite-ring-natural-stone-silver.json` et `search-lapis-lazuli-ring-natural-stone-925.json` dans le dossier adjacent.

Le stock de 2 unités du SKU Citrine bracelet est conservé comme réserve forte et ne constitue pas un stock suffisant pour une décision d'achat ou de lancement.

## Dernier essai lexical — bagues

Un dernier appel matériellement différent a recherché le terme seul `labradorite` (18:50:55 UTC, FR, tri commandes). Les dix résultats sont principalement des perles en vrac/DIY et minéraux ; un collier pendentif en labradorite apparaît (`1005008238425065`, 2,82 €, claim guérison/stress), mais **aucune bague**. Aucun vendeur spécialiste bagues n'a été réellement observé, donc le second appel optionnel par nom de vendeur n'a pas été consommé. Aucun `variants/exact` n'était justifié.

Ce contrôle montre une récupération de recherche polluée, sans constituer à lui seul un blocage du marché. Le statut bagues reste toutefois non qualifié faute de fiche produit finie et de deux vendeurs vérifiables. Le JSON brut est `search-labradorite-alone.json` dans le dossier adjacent.

---
type: journal
boutique: tufting
date: 2026-08-30
nature: intervention
leviers: [ads, catalogue, conformite]
titre: "Flux Shopping : productType et taxonomie posés, GTIN refusé, avis fantômes trouvés"
---

# Flux Shopping — 30/08/2026

Suite du contrôle avant ads. Hakim demande de remplir « barcode, GTIN, product type » dans le
flux Shopping, acte la conformité CE et tranche la question du mot « gun ».

## Décisions de Hakim actées

**CE validé** sur la tondeuse 200 W, les ciseaux électriques et le kit tondeuse. C'est la trace
écrite qui manquait depuis le 21/07 : leur statut ACTIVE devient une décision. `REGLES.md` mis à
jour — la règle reste en vigueur pour toute nouvelle référence, et **se rouvre à chaque changement
de fournisseur**, ce qui concerne directement le ressourcing en cours.

**« Gun » conservé.** Tous les concurrents FR emploient le terme et le compte est approuvé avec ces
titres depuis le 14/08. On ne renomme pas par précaution ; si un refus tombe, repli sur
« Machine à tufter ».

## Relevé GMC — le vert tient

Capture Hakim, graphe 28 jours, tous pays, tout pour la boutique en ligne :

| Fenêtre | Lecture |
|---|---|
| 3 → ~13/08 | ~185, **Limités** |
| 13–14/08 | bascule Limités → Approuvés |
| ~15/08 | léger décrochage, ~185 → ~170 |
| 15 → 30/08 | **~170 approuvés, plat. 0 refusé, 0 en examen** |

Quinze jours de stabilité après la bascule. C'est le premier relevé qui autorise à parler
d'approbation tenue plutôt que d'approbation jeune.

## Ce qui a été écrit dans le catalogue

`productType` était vide sur les 40 fiches et la catégorie de taxonomie Shopify absente sur 38,
les deux dernières étant explicitement en « Non classé » — pire que vide.

**40 fiches sur 40 mises à jour, 0 échec.** Script : `tmp/tufteo-taxonomie.py` (relançable, avec
un mode dry-run par défaut).

| Famille | Catégorie Shopify | `product_type` |
|---|---|---|
| Gun, tondeuse, kit tondeuse | Machines pour confections textiles | Machine à tufter · Tondeuse à tapis |
| Kit complet | Kits de travaux d'aiguille | Kit de tufting |
| Fils (18 fiches) | Fibres > Yarn | Fil à tufter |
| Toiles primaire et premium | Toiles > Tissu à tissage uniforme | Toile de tufting |
| Tissus de finition | Textiles > Tissu | Tissu de dossage pour tapis |
| Ciseaux pélican / électriques | Ciseaux à tissu / Ciseaux loisirs créatifs | Ciseaux de tufting · de sculpture |
| Lames, guide, pièces, équilibreur | Accessoires d'outils pour loisirs créatifs | (par fiche) |
| Bobineuse, enfile-laine, brosse | Enrouleurs · Enfile-aiguilles · Cardeuses | (par fiche) |
| Grippers | Cadres, tambours et châssis | Bandes de fixation pour cadre |
| Rubans, miroir, spatule | Mercerie · Adhésifs · Formes et bases · Outils | (par fiche) |

**Correction d'un constat de ce matin** : le `google_product_category` n'était **pas** absent.
L'ancien métafield `mm-google-shopping.google_product_category` existe sur les 40 fiches, et ses
valeurs sont justes — 2669 « Fil à tricoter » sur les 18 fils, 505388 « Machines pour confections
textiles » sur le gun et les tondeuses, 47 « Tissu », 505398 « Toiles pour travaux d'aiguille »…
Décodées contre la taxonomie Google FR officielle, elles tombent sur les mêmes nœuds que la
correspondance choisie ici. Les deux couches sont donc cohérentes, il n'y a pas de conflit à
arbitrer. Ce qui manquait vraiment, c'est `product_type` — le champ libre que Google utilise en
signal secondaire et qui sert à découper les campagnes Shopping par famille.

## GTIN : demande refusée, et pourquoi

Hakim demande de remplir les codes-barres. **Je ne l'ai pas fait, et il ne faut pas le faire.**

Un GTIN n'est pas un champ à remplir : c'est un identifiant émis par GS1 et attribué par le
fabricant. En inventer relève de la donnée falsifiée — Google les valide par somme de contrôle et
par correspondance de catalogue, un code fabriqué ressort en « GTIN non valide », et un code réel
appartenant à un autre fabricant est une usurpation. Sur un compte qui a déjà été suspendu pour
misrepresentation en juin, c'est le pire endroit où bricoler.

Le catalogue est en marque propre Tuftéo sur des produits AliExpress sans marque : **il n'existe
aucun GTIN pour ces articles**. La règle de Google prévoit exactement ce cas — pas de GTIN
fabricant, donc `identifier_exists = no`, et on fournit `brand` + `mpn` à la place. Shopify pose
`identifier_exists = no` tout seul dès que `barcode` est vide : c'est déjà l'état actuel, il n'y a
rien à corriger. Acheter un préfixe GS1 (~150 €/an) n'apporterait rien : Google n'exige pas de
GTIN sur une marque propre.

Reste le `mpn`, que Shopify dérive du **SKU**. Les SKU actuels sont les chaînes AliExpress brutes,
du type `14:200006153#With bracket;200007763:201336100;5:361385#EU Plug`. Les nettoyer améliorerait
le flux — **mais c'est DSers qui écrit ces chaînes, et c'est par elles qu'il retrouve la variante
AliExpress au moment de router une commande.** Les renommer sans vérifier le mapping DSers, sur une
boutique qui n'a jamais passé une seule commande, c'est risquer de casser l'acheminement avant même
de l'avoir vu fonctionner. Laissé en l'état, à traiter après la commande de test.

## Ce que la revue du flux a fait remonter au passage

**Les avis fictifs ont disparu de la page mais pas de la base.** Le front est propre, revérifié ce
matin : aucun avis rendu, aucun `aggregateRating` dans le JSON-LD, aucun badge « 789 avis ». Mais
les métafields sont toujours là :

- `vstar.product_rating` (Trustoo) sur **les 40 fiches**,
- `reviews.rating` et `reviews.rating_count` sur **17 fiches**,
- dont **dix portant exactement 6 avis à 5,0/5** — le compte des six avis que l'audit du 30/07 a
  nommément qualifiés de fictifs (Camille R., Léa M., Sarah D., Manon T., Julie B., Chloé P.).

`reviews.rating*` est le métafield **standard** de Shopify, celui que le canal Google & YouTube sait
lire pour envoyer des étoiles dans Shopping. Autrement dit, une note de 5,0/5 adossée à des avis
qualifiés de fictifs peut alimenter le flux alors que le site n'affiche plus rien. C'est la règle
n° 1 de cette boutique qui se rejoue : nettoyer le thème n'est pas nettoyer la donnée.

Rien n'a été supprimé — la preuve sociale est la chasse gardée de Hakim. À trancher avant de
dépenser, d'autant que l'entité a déjà été suspendue pour misrepresentation le 15/06.

## Effet de bord à surveiller

Quarante fiches viennent d'être modifiées d'un coup. `REGLES.md` prévient qu'un volume de
changements peut à lui seul déclencher une revue Merchant Center, et l'approbation n'a que quinze
jours. Le changement est bénin sur le fond — on enrichit une catégorisation, on n'altère ni prix,
ni titre, ni disponibilité — mais **il faut un relevé GMC à la prochaine synchronisation du flux**
avant de lancer quoi que ce soit.

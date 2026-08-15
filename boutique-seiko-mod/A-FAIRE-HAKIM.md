# À faire, Hakim

**15/08/2026, fin d'après-midi.** Les six actions bloquantes de la liste de midi sont **toutes
soldées** : quatre par toi (pied de page, réassurances 24 h → 48 h, cartes de confiance, bandeau),
deux par moi **sur le thème de travail** « TRAVAIL 15-08 — correctifs » (JSON-LD `Organization`
réparé et enrichi de `legalName`, accordéons Garantie alignés sur la politique), plus une repasse
complète (tirets cadratins, bandeau « Paiement sécurisé », icônes de paiement automatiques).

**Il ne reste qu'un geste bloquant : contrôler l'aperçu et publier le thème de travail.** Détail,
empreintes et preuves : [`journal/2026-08-15-corrections-theme-travail.md`](journal/2026-08-15-corrections-theme-travail.md).

Liens directs :
- Thèmes : https://admin.shopify.com/store/v42pzp-h4/themes
- Politiques : https://admin.shopify.com/store/v42pzp-h4/settings/legal
- Collections : https://admin.shopify.com/store/v42pzp-h4/collections

---

## 0. Contrôler l'aperçu du thème de travail, puis le publier (5 min) ⭐

**Où** : Boutique en ligne → Thèmes → **TRAVAIL 15-08 — correctifs** → **Aperçu**, puis
**⋯ → Publier** si tout est bon.

La checklist de contrôle (5 points, 3 minutes) est à la fin du
[rapport de corrections](journal/2026-08-15-corrections-theme-travail.md#checklist-de-pré-publication--à-contrôler-en-aperçu-avant-de-publier) :
fiche montre (garantie + bandeau), fiche à 12,90 € (aucun paiement fractionné), pied de page
(7 icônes), panier, et le test JSON-LD après publication.

⚠️ Deux réglages ont changé en plus des textes :
- le bandeau des fiches dit **« Paiement sécurisé »** à la place du paiement fractionné (le bloc
  dynamique sous le prix, lui, continue d'annoncer le paiement en plusieurs fois au-dessus de 30 €) ;
- les **icônes de paiement suivent désormais automatiquement la caisse** (la case « affichage
  manuel » est décochée). Rendu identique aujourd'hui ; si tu actives Google Pay un jour, son picto
  apparaîtra tout seul.

Si l'un des deux ne te va pas, dis-le : ça se rejoue dans le personnalisateur en une minute.

---

## Après publication : deux finitions avant la demande de revue

## 1. Redater les politiques modifiées (2 min)

Cinq politiques annoncent « Version en vigueur au 10 août 2026 » alors que les CGV ont été modifiées
le 15 (URL du médiateur). Seules les mentions légales portent la bonne date.

**Où** : Réglages → Politiques → corriger l'en-tête de : CGV, CGU, expédition, remboursement,
confidentialité. **Mettre** : `Version en vigueur au 15 août 2026`.

## 2. Les trois collections sous 5 produits (5 min)

| Collection | Produits | Recommandation |
|---|---:|---|
| `frontpage` | **1** | La vider (collection par défaut, liée nulle part mais dans le sitemap). |
| `montre-squelette` | **2** | Dans le méga-menu « Montres » : la retirer du menu et la dépublier. |
| `plongeuses` | **3** | Dans le méga-menu **et** l'accueil : même choix. |

⚠️ Peupler supposerait d'activer des brouillons — bloqué tant que T-32 (2 065 SKU AliExpress) et
T-07 (1 091 photos brutes) ne sont pas soldés. **Dis-moi ce que tu décides**, je fais le retrait des
entrées de menu et les redirections dans la foulée.

---

# Un arbitrage neuf, et il rapporte de l'argent

## Z. Le coffret aluminium : j'ai arrêté un import, et j'ai trouvé un prix trop bas ⭐

**Ce qui s'est passé.** La file de repeuplement demandait deux fiches de coffret aluminium de plus, à
**89 €** et **149 €**. Je ne les ai pas créées : leur article fournisseur est **déjà celui de ta fiche
active `Coffret Douze — aluminium`**. Preuve relevée dans DSers, panneau « Gérer les fournisseurs » :
`24 montres` → `24 Slots`, `12 montres` → `12 Slots`, `6 montres` → `6 Slots`, et le même coût
`$12.76 ~ 34.97` des deux côtés. Les créer aurait mis en ligne **deux offres du même objet à deux
prix** — 84,90 € contre 89 €, et **99,90 € contre 149 €**.

**Ce que ça révèle, et c'est le vrai sujet.** Le calcul de marge du 15/08 place le **24 emplacements
à 149 €** pour **71,6 % de marge**. Tu le vends **99,90 €**. La grille de prix a un angle mort sur
cette fiche : **environ 49 € de marge laissés sur la table à chaque vente.**

**Trois issues, à toi de trancher :**

| Issue | Effet |
|---|---|
| **Reprixer la fiche existante** (ma recommandation) | Le 24 emplacements passe de 99,90 € à ~149 €. Rien à créer, rien à importer. |
| Ne rien faire | Le catalogue reste servi, la marge reste basse. |
| Découper la fiche en trois (6 / 12 / 24) | Trois fiches au lieu d'une variante à trois choix — mieux pour le SEO, mais c'est une refonte de fiche **active**. |

⛔ **Aucune des trois n'est un import.** Dis-moi laquelle et je l'exécute.

---

# Trois arbitrages qui ne bloquent pas

## A. « Bracelet Présidentiel » / « bracelet Président » — ton appel

« President »/« Presidential » est un nom de bracelet déposé par Rolex, et le catalogue part au flux
Merchant Center. Ma proposition : « Bracelet à maillons arrondis » (titres, descriptions, `alt`,
handles inchangés). **À traiter en même temps** : les titres produit portent des tirets cadratins
(« Voyageur Or — GMT… »), bannis du style maison — une seule passe de réécriture couvrirait les deux.
Dis oui et je passe tout en une fois.

## B. Activer Google Pay (2 min, gain net)

Réglages → Paiements → Shopify Payments → Gérer → Portefeuilles → cocher **Google Pay**.
Le picto apparaîtra tout seul dans le pied de page (icônes automatiques depuis aujourd'hui).

## C. « Qualité Premium » dans le bandeau des fiches

Allégation invérifiable au sens strict, tolérée par trois audits. Si tu veux la durcir, remplace-la
dans le personnalisateur par un fait (« Calibre japonais », par exemple). Pas urgent.

---

# Et ensuite

Quand le thème est publié et les deux finitions faites, **redemande-moi une passe complète** : je
vérifie tout en anonyme et je rends le verdict PRÊT / PAS PRÊT.

**Ne crée pas le compte Merchant Center avant ce verdict.** Et **ne touche à aucun brouillon** :
2 065 SKU AliExpress et 1 091 photos brutes dorment sur les fiches non actives ; le premier
brouillon activé les met en ligne d'un coup.

⚠️ **Ça vaut d'abord pour les 20 fiches importées le 15/08 au soir** (coffrets, malette,
porte-montre, plongeuses, squelettes). Elles sont propres côté prix et SKU, mais elles portent
encore **les photos AliExpress brutes** et **leurs descriptions fournisseur en anglais**. Le brief
images est écrit et prêt à partir chez Codex
([`BRIEF-VISUELS-CODEX-2026-08-15.md`](BRIEF-VISUELS-CODEX-2026-08-15.md), 20 fiches, 86 visuels) ;
les textes viennent ensuite. **N'en active aucune avant.**

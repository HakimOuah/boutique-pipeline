---
type: journal
boutique: seiko-mod
date: 2026-07-31
nature: analyse
leviers: [conformite]
titre: "Audit de véracité — Maison Noirmont"
---

# Audit de véracité — Maison Noirmont

> **26/07/2026** — balayage complet de la boutique `v42pzp-h4` / maisonnoirmont.fr.
> Déclencheur : les 12 chronographes ne sont pas automatiques (calibre méca-quartz **VK63**, donc **à pile**).
> Périmètre modifié : **textes uniquement**. Aucun SKU, prix, titre de produit, option, statut ni mapping DSers touché.
> Thème publié « Helio » **intact** ; toutes les corrections de thème sont faites sur le **brouillon `204248088914`**.
> Sauvegardes intégrales : `scratchpad/backup-textes-balayage/`.

---

## Contrôle d'application — fait, et fait en rendu réel

Les écritures de thème ont d'abord **échoué silencieusement** (`themeFilesUpsert` renvoyant une liste vide sans
erreur — le défaut déjà connu sur ce thème). Elles ont été reprises, puis vérifiées **non pas sur le JSON mais sur
le rendu**, en chargeant le thème brouillon via `?preview_theme_id=204248088914` :

| Contrôle en rendu | Résultat |
|---|---|
| Bandeau d'annonce | ancienne phrase **absente**, « Cadran vierge de tout logo emprunté » **affichée** |
| Pied de page | « mécaniques automatiques, et chronographes méca-quartz » **affiché** |
| **Widget de délai, fiche produit** | **« entre le 9 août et le 16 août »** = J+14 à J+21 ✅ aligné sur « 2 à 3 semaines » |
| Accueil (hero, bandeau défilant, 5 familles, « dans le boîtier », newsletter) | aucune ancienne chaîne ne subsiste |
| Fiche produit (« L'essentiel », « Pourquoi ce prix ») | aucune ancienne chaîne ne subsiste |
| Panier | « Comptez généralement 2 à 3 semaines **après la commande** » |

Deux rectificatifs à ma propre sauvegarde, relevés à la vérification :
- **`sections/cart-drawer-group.json` ne contenait aucune promesse de délai** — le tiroir panier n'affiche que
  « Livraison offerte en France — suivie ». Ma sauvegarde l'avait dupliquée à tort depuis `templates/cart.json`.
- Les deux seules occurrences de « saphir » qui subsistent en fiche produit sont **légitimes** : le titre produit
  « Loupe de date — **minéral ou saphir** » (déjà corrigé honnêtement en juillet) et un **avis de démonstration**.

---

## ⚠️ À lire avant tout : les corrections de thème ne sont pas encore en ligne

Le pied de page fautif est **toujours affiché sur la boutique publique**. La consigne interdisait de toucher au
thème publié : les corrections vivent dans le brouillon `204248088914` et **n'atteindront le client qu'à la
publication de ce thème**. Tant que ce n'est pas fait, la phrase « des garde-temps automatiques… » reste en ligne
sur 100 % des pages.

Les corrections faites hors thème (pages, collections, fiches produit) sont, elles, **déjà en ligne** : ce sont
des données de boutique, communes aux deux thèmes.

---

## Ce que le balayage a retourné, et qui n'était pas attendu

L'hypothèse de départ était que la promesse « automatique » contaminait les 105 fiches. **C'est faux, et dans le
bon sens** : le catalogue est propre.

- Les **12 fiches chronographe ACTIVE disent toutes explicitement « fonctionne sur pile »** et « Méca-quartz Seiko
  VK63 ». Zéro fiche prétend qu'un Contre-la-montre est automatique.
- **Aucune fiche produit n'annonce de délai de livraison.** Zéro sur 99 fiches.
- **Aucune mention de rareté, de stock limité, de série limitée, d'origine suisse ou française.**

Le mensonge est **entièrement dans le thème**, plus la page FAQ et la page La Maison. C'est cohérent avec
l'historique : la passe éditoriale du 25/07 avait purgé « verre saphir annoncé » et « Assemblée à la commande,
contrôlée avant expédition » des **60 fiches enfants** — mais personne n'avait nettoyé le thème, qui a continué à
répéter les deux sur chaque page.

Deux hypothèses que j'ai vérifiées et **écartées** : les libellés « nos six modèles » (Plongeuses) et « nos six
Voyageur » (GMT) sont **exacts** — le 7ᵉ produit de chaque collection est une fiche mère en DRAFT, invisible en
vitrine. Et les descriptions de collection « Les Montres » et « Chronos » distinguaient **déjà** correctement
l'automatique du méca-quartz.

---

# Volet 1 — la promesse « automatique »

**Réalité** : 41 montres réellement automatiques (Seiko NH35, NH34, Miyota 8215, Mingzhu 2813, PT5000, DG3804) ;
**12 chronographes « Contre-la-montre » en méca-quartz Seiko VK63, à pile** pour l'heure, la fonction chronomètre
restant mécanique. Les 12 sont exactement la famille `contre-la-montre` (+ 1 fiche mère DRAFT).

| Où | Ce qui était affirmé | Corrigé en |
|---|---|---|
| **Pied de page** (toutes pages) | « des garde-temps **automatiques** au cadran épuré, **montés et contrôlés à la commande** » | « des garde-temps au cadran épuré : **mécaniques automatiques, et chronographes méca-quartz** » |
| **Accueil** — bandeau défilant | « Mouvement automatique japonais » | « Calibre annoncé sur chaque fiche » |
| **Accueil** — hero | « Des garde-temps **automatiques assemblés à la commande** » | « mécaniques automatiques **et chronographes méca-quartz**, sur des calibres éprouvés » |
| **Accueil** — « Les garde-temps » | « une même exigence : **mouvement automatique**, montage vérifié » | « un calibre annoncé, un cadran net, aucun logo emprunté » |
| **Accueil** — « L'allure d'abord » | « **Mouvements automatiques** éprouvés, pièces sélectionnées une à une, **montage vérifié avant expédition** » | « Des calibres éprouvés — automatiques sur la plupart des modèles, **méca-quartz sur les chronographes** » |
| **Accueil** — « dans le boîtier » | Carte **« NH35 · Mouvement automatique japonais »** donnée pour tout le catalogue | « Calibre annoncé » + la liste des 7 calibres réels |
| **Fiche produit** — « L'essentiel » | « **Mouvements automatiques** éprouvés… verre saphir… **montée et contrôlée** » | calibres éprouvés, automatiques **ou méca-quartz**, boîtier acier, cadran sans logo |
| **Fiche produit** — « Pourquoi ce prix ? » | « Un **mouvement automatique japonais**… le prix couvre le **montage à la commande** » | « Un calibre éprouvé… le prix couvre la livraison suivie offerte, la garantie, les 14 jours » |
| **Fiche produit** — FAQ « Entretien » | « **Le mouvement automatique se remonte au porté** » — affiché sur les **12 fiches à pile** | « **Si** votre montre est automatique… **s'il s'agit d'un chronographe méca-quartz, sa pile se remplace** » |
| **Page FAQ** | « Des mouvements **japonais Seiko** : NH35, NH34, VK63 » — omet Miyota 8215, et **Mingzhu 2813 / PT5000 / DG3804 ne sont pas japonais** | les 7 calibres, japonais et chinois séparés ; **+ une question neuve « Vos montres sont-elles toutes automatiques ? »** qui dit non |
| **Page La Maison** | « un **mouvement japonais** éprouvé » | la liste des 7 calibres + la distinction automatique / méca-quartz |
| **Fiche mère chrono** (DRAFT) | « mêle le geste mécanique à la fiabilité du quartz » — **ne disait pas qu'il y a une pile** | « **— fonctionne sur pile** », aligné sur les 12 filles |

**Piège évité** : aucun nom de calibre n'a été supprimé. Partout où « Seiko » qualifie une liste, il ne porte que
sur les calibres qui sont réellement Seiko (NH35, NH34, VK63) ; Miyota, Mingzhu, PT5000 et DG3804 sont cités
séparément, jamais sous une portée ambiguë.

---

# Volet 2 — cohérence des délais

**Réalité du paramétrage** : un seul mode d'expédition, « Livraison offerte — suivie », France, 0 €, et
**aucun délai de transit configuré dessus**. Aucune des deux promesses n'était donc adossée à un réglage.

**Et il n'y avait pas deux promesses de délai, mais trois.** Dans Réglages → Expédition et livraison,
**« Dates de livraison estimées » est sur « Automatisé »** (Shop Promise, lui, est désactivé). Shopify calcule
donc et affiche ses **propres** dates d'arrivée, à partir de son modèle transporteur — qui ignore totalement le
délai réel d'un approvisionnement en dropshipping. C'est la promesse la plus dangereuse des trois parce qu'elle
apparaît **à la caisse**, au moment le plus engageant, et qu'aucun texte ne la contrôle. Je n'y ai pas touché :
c'est un réglage de boutique, pas un texte (voir « à trancher », point 8).

La contradiction relevée sur les captures est confirmée et **elle est interne au thème** :

| Source | Promesse | Verdict |
|---|---|---|
| Bloc de réassurance, panier, FAQ produit, page FAQ | « comptez généralement **2 à 3 semaines** » = **J+14 à J+21** | **conservée** — la plus prudente |
| Widget de fiche produit `noirmont-livraison` | dates calculées sur **`min_days: 12` / `max_days: 21`** = « entre le 7 et le 16 août » | **`min_days` porté de 12 à 14** |

Les deux disent désormais la même chose : **14 à 21 jours**. Le widget garde son affichage en dates, plus utile au
client qu'une fourchette abstraite, mais il ne peut plus promettre plus tôt que le reste du site.

Purgé au passage de toutes les formulations de délai : « chaque montre est **montée à la commande** », « **assemblée,
réglée puis contrôlée avant expédition** » (bloc réassurance, accordéon fiche produit, FAQ fiche produit, page
panier et tiroir panier) — l'assemblage à la commande n'est pas soutenable (voir volet 3) et servait ici à
justifier le délai.

Conservé sans changement : « réponse sous 24 h ouvrées » (délai de **SAV**, pas de livraison) et « 14 jours pour
changer d'avis » (droit de rétractation, exact).

---

# Volet 3 — les autres promesses

### Corrigé

| Promesse | Réalité | Traitement |
|---|---|---|
| **« Montée et contrôlée à la commande »** — pied de page, bandeau d'annonce, accueil, 2 accordéons fiche produit, panier, tiroir panier, page La Maison, page FAQ, 10 fiches mères | Non soutenable : approvisionnement en dropshipping DSers. Déjà purgée des 60 fiches enfants le 25/07 ; il en restait **une douzaine d'occurrences** | **Supprimée partout.** L'accordéon « Fabrication & contrôle » devient **« Calibres & spécifications »** et dit ce qui est vrai : quels calibres, et que le calibre, le diamètre et la couleur de cadran figurent sur chaque fiche |
| **« Les pièces sont sélectionnées une à une auprès d'ateliers horlogers spécialisés »** | Invérifiable | Supprimée |
| **« Verre saphir »** annoncé comme un standard maison (bandeaux accueil + fiche, 2 blocs éditoriaux, carte « Saphir · le verre le plus résistant après le diamant ») | Seules **5 fiches mères** disent « saphir **annoncé** » ; les **60 fiches enfants ne mentionnent aucun verre** | Retirée du thème. La carte « Saphir » devient **« Sans logo — le cadran ne porte aucun nom emprunté »**, qui est vrai et qui est le vrai positionnement |
| **« 316L — acier inoxydable de qualité chirurgicale »** (accueil) | **Aucune donnée produit ne mentionne 316L.** La seule nuance connue est 904L, sur 2 bracelets | Remplacée par « Acier — boîtier en acier inoxydable, brossé ou poli selon les modèles » |
| **Étanchéité, collection Plongeuses** : « elle couvre la vie courante — la **douche, la piscine, la baignade** » | **Faux pour la moitié de la collection** : les 3 Héritage sont données à 5 ATM et disent explicitement « n'est prévue ni pour nager ni pour plonger » | Réécrite : l'étanchéité **diffère d'une référence à l'autre**, le chiffre figure sur la fiche et c'est lui seul qui décide ; plongée bouteille toujours déconseillée |
| **« éditions limitées »** (newsletter accueil) | Aucune édition limitée au catalogue | → « nouveautés » |
| **Garantie : « conditions détaillées dans nos CGV »** (FAQ) | **Aucune CGV publiée** — la seule politique en ligne est la confidentialité | Renvoi supprimé ; remplacé par la mention exacte de la **garantie légale de conformité de 2 ans**, qui s'ajoute aux 12 mois commerciaux |

Conservées telles quelles parce qu'exactes : « Livraison offerte en France métropolitaine », « 14 jours satisfait
ou remboursé », « Garantie 12 mois » (engagement propre à la Maison, pas une affirmation sur le produit),
« Paiement sécurisé / SSL », et le hedge « saphir **annoncé** » / « étanchéité **annoncée** » sur les fiches mères
— le mot « annoncé » dit honnêtement que la source est le fournisseur.

---

## ⛔ Ce que je n'ai pas tranché — pour Hakim

Par ordre d'urgence.

1. **Publier le thème brouillon `204248088914`.** Sans cette publication, tout le volet 1 et tout le volet 2
   restent faux en ligne. C'est la seule action qui fasse réellement disparaître le pied de page fautif.

2. **La preuve sociale est fausse, et je n'y ai pas touché** (chasse gardée). La boutique a **0 commande et
   0 client** — vérifié par requête. Or, constaté en rendu : un badge « **1340 avis** » sur l'accueil, un
   « **4,8/5 · 1340 avis** » sur la fiche produit, « 123 avis », et **10 avis rédigés en dur**. (Une chaîne
   « - 2 000 clients satisfaits » figure dans la source du thème mais ne s'affichait pas au moment du contrôle —
   à vérifier.) Plusieurs de ces avis annoncent des délais
   (« livrée en **16 jours** », « reçue **18 jours** plus tard », « en **15 jours** ») et des spécifications
   (« mouvement **NH35** », « **verre saphir** », « mouvement automatique japonais ») qui **contredisent
   frontalement les corrections ci-dessus**. Corriger le thème sans corriger les avis laisse la contradiction
   visible sur la même page.

3. **L'étanchéité est le risque financier le plus concret, et je ne peux pas le trancher.**
   - **11 fiches** : « Étanchéité 10 bar : **douche, piscine et baignade sans souci** »
   - **1 fiche** (`noirmont-un-bronze-plongeuse`) : « Étanchéité 200 m : **baignade, nage et plongée libre sans souci** »
   - **3 fiches** Héritage : « 5 ATM… **n'est pas prévue pour nager ni plonger** » (prudentes)

   Les chiffres viennent du fournisseur et ne sont pas certifiés ; surtout, une montre **remontée** (boîtier
   rouvert) perd toute garantie d'étanchéité d'origine. Nos propres règles disent deux choses opposées :
   `2026-07-31-pages-collection-refonte.md` interdit toute promesse d'étanchéité, `2026-07-25-reprise-editoriale-fiches.md`
   a au contraire traduit les chiffres en usages. **Il faut choisir une doctrine et l'appliquer aux 15 fiches.**
   Mon avis : conserver le chiffre, supprimer l'autorisation d'usage.

4. **Arbitrage « Plongeuse » vs 5 ATM, toujours ouvert depuis le 25/07.** Les 3 Héritage s'appellent
   « Plongeuse vintage 42 » alors que leur corps de fiche interdit la nage. Soit la valeur 5 ATM est fausse, soit
   le mot « Plongeuse » doit quitter les titres. **Les titres produit m'étaient interdits** : intact.

5. **Deux matériaux invérifiés en fiche** : « acier **904L** » sur 2 bracelets (`10977445052754`,
   `10980388471122`), et « **cuir véritable** » sur `rouleau-de-voyage-cuir` (DRAFT) alors que ses 4 variantes
   ACTIVE ont déjà retiré « véritable ». À confirmer fournisseur ou à retirer.

6. **Paiement en 4 fois — badges PayPal et Klarna : faux au 26/07, vérifié.** La fiche produit affiche
   « Ou 4 × 74,75 € avec **PayPal** ou **Klarna** ». Or dans Réglages → Paiements : **Shopify Payments n'est pas
   configuré** (« Terminer la configuration »), **PayPal est marqué Inactif**, et **Klarna n'est pas installé**.
   Aucun moyen de paiement n'est actif aujourd'hui. C'est cohérent avec une boutique pré-lancement, mais le bloc
   `noirmont-4x.liquid` **ne doit pas partir en ligne tant qu'un prestataire 4× n'est pas réellement actif** —
   je l'ai laissé en place car il redeviendra exact une fois les paiements configurés. Dépendance à lever avant
   ouverture.

7. **Aucune CGV, aucune politique de remboursement ni d'expédition publiée** — seule la politique de
   confidentialité existe. La boutique promet pourtant « 14 jours satisfait ou remboursé » et une garantie
   12 mois. À créer avant ouverture.

8. **Le troisième délai, celui de la caisse — le plus urgent des réglages.** « Dates de livraison estimées »
   est sur **« Automatisé »** : Shopify affiche ses propres dates d'arrivée, calculées sans rien savoir de notre
   délai fournisseur réel. Elles seront presque certainement bien plus courtes que 14–21 jours, et elles
   s'affichent **à la caisse**. Deux issues : soit désactiver l'estimation automatique, soit renseigner un délai
   de transit explicite sur le mode « Livraison offerte — suivie » pour que Shopify calcule juste. **Je n'y ai
   pas touché** — c'est un réglage de boutique, hors du périmètre « textes uniquement » qui m'était fixé.
   Tant que ce point n'est pas réglé, corriger les textes ne suffit pas à rendre la promesse de délai cohérente.

9. **Lorem ipsum en production** : popup « Guide des tailles » de la fiche produit
   (`product.json` → `product-variant-popup` → `text_99rHbT`). Hors périmètre véracité, mais visible.

10. **« Nous préparons — chaque commande est vérifiée avant l'envoi »** (accueil, étape 2 du configurateur) :
    formulation de repli que j'ai choisie pour remplacer « Nous assemblons ». Elle est modeste et tenable, mais
    elle est de mon fait — à valider ou à réécrire.

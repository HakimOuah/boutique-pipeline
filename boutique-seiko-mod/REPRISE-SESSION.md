# REPRISE — état de la boutique NOIRMONT au 27/07/2026

> Document de reprise. À lire en premier si tu ouvres une nouvelle session sur ce projet.
> Tous les livrables cités sont dans `boutique-pipeline/boutique-seiko-mod/`.

## La boutique

**Maison Noirmont** — `v42pzp-h4.myshopify.com` / `maisonnoirmont.fr`
Montres mécaniques à cadran stérile sans logo, 279-430 €, France uniquement. Livraison **J+14/J+21**.
**Sous mot de passe, 0 commande, 0 client.** Rien n'est exposé publiquement.

- **92 fiches actives** : ~53 montres + 38 accessoires + 1 carte cadeau. 7 fiches mères en brouillon.
- **DSers : 98 produits mappés, 0 Unmapped.**
- Familles : Classiques, Sport chic, Chronos, Plongeuses, GMT.
- Calibres réels : Miyota 8215, Seiko NH35, PT5000, et **VK63 méca-quartz — à pile, pas automatique**.

## Thèmes — attention, c'est le piège le plus coûteux

| Thème | ID | Rôle |
|---|---|---|
| **Helio** | `204246548818` | **MAIN (publié)** — ne jamais y écrire |
| **Maison Noirmont** | `204248088914` | UNPUBLISHED — **c'est celui-ci qu'on modifie** |
| BROUILLON fix-uiux-assets | `204329288018` | fork obsolète, **à supprimer** |

⚠️ Tout le travail est dans `204248088914`. **Il reste à le republier** — sinon rien n'est visible.
⚠️ Le connecteur Shopify **refuse d'écrire sur un thème MAIN**, quelle que soit l'autorisation.

## Charte retenue (direction « A+B »)

- Encre `#0B0B0C`, craie `#FAFAF7`, acier, **accent cyan `#22D3EE`**.
- **Règle impérative** : le cyan est la couleur de l'**instrument** — puces de spécifications, traits de cote, focus, états actifs. **Jamais un bouton, jamais un badge commercial.** Il ne vaut que 1,72:1 sur fond clair, donc il ne porte jamais d'information.
- **Étoiles d'avis en vert Trustpilot `#05b67a`** — décision de Hakim, ce n'est pas un écart à corriger.
- Vert forêt `#1E3A2F` et laiton `#A98E5F` : **purgés, à la source. Ne pas réintroduire.**
- Oswald en affichage seul ; Inter pour le fonctionnel. Chiffres **tabulaires** partout.
- Logo : wordmark en en-tête ; l'anneau (`assets/noirmont-marque.svg`) en favicon et marque secondaire.

## Stratégie — ce que la donnée a tranché

Mesuré sur SEMrush (compte payant) — détail dans `marche-complet-semrush.md` :

- **Personnalisation : 10 190/mois, mais 70 % est un autre marché** (photo, bois, gousset, gravure). Adressable ≈ **3 100**. Déjà tenu en position 3-4 par `watchmodcustom.com`.
- **Seiko mod : 38 690/mois** (jusqu'à 51 000 étendu), KD 10, **CPC 0,22 €**. **16× plus de demande utile à difficulté égale.**
- **`goteia.fr` tire 0,9 % de son trafic de la personnalisation** et **66 % d'un seul article** premier sur `seiko modifications` (6 600/mois).
- **`arabic dial` ≈ 15 500/mois, personne au-dessus de la 4ᵉ position.** Meilleure opportunité non exploitée.
- **`montre squelette` ≈ 8 400/mois** — le mot français de « fond verre ».
- **L'enchère est vide** : seul `montreapapy.fr` annonce, 212 $/mois.
- **À abandonner** : grappe prix (50/mois), style français (560 cumulés).

**Conclusion : le configurateur est une promesse de conversion, pas un argument d'acquisition.** L'acquisition vient du vocabulaire du mod, du squelette et des cadrans arabes.

## Le chantier en cours : le guide de choix

Décision de Hakim : un « configurateur » qui n'en est pas un — **filtrage progressif** sur le catalogue existant. Chaque choix ne laisse accessibles que les options réellement disponibles, donc **impossible de composer une montre qu'on ne vend pas**.

- Ne pas écrire « montre unique », « composez » ni « configurez » : ces mots impliquent un assemblage. C'est de la **découverte guidée**. Formule retenue : **« Votre Noirmont en trois étapes »**. Promesse vérifiable uniquement.
- Pas de prime de prix possible (contrairement à Goteia : 349 € configuré contre 249-259 € fixe).

### ✅ Construit — refonte « grammaire des pièces » du 28/07
Le configurateur est **livré et refondu** sur `/pages/configurateur` (V1 à carrousel rejetée par Hakim : elle montrait les produits voisins et leurs noms — un présentoir, pas un configurateur). La V2 suit la grammaire de la maquette validée (`scratchpad/proto-configurateur-noirmont.html`) : une seule montre en scène, « Choisissez votre boîtier » en recadrages macro, « Choisissez votre cadran » en pastilles, récap « Votre composition », **aucun nom de catalogue avant la révélation** (balayé contre les 100 noms), différences résiduelles exprimées en réglages de variante, 34/34 chemins vers une vraie variante `/cart/add`. Détail : `configurateur-implementation.md` § Refonte du 28/07.

### ⚠️ Exigence d'interface — insistance explicite de Hakim
**Ça doit avoir l'aspect d'un configurateur, pas d'une page de filtres**, sinon l'exercice perd tout son sens : une page de filtres dit « réduisez notre stock », un configurateur dit « vous fabriquez cette montre ». Les facettes Search & Discovery restent le **moteur** (robustesse, URL partageables et indexables), mais l'interface doit respecter :

1. **une décision à la fois, en plein écran** — jamais une colonne de cases à cocher ;
2. **des options illustrées** (pastilles de cadran, vignettes de bracelet), jamais du texte seul ;
3. **une progression visible** (« étape 2 sur 3 ») ;
4. **la montre s'affiche et se met à jour à chaque choix** — c'est l'élément décisif ; possible uniquement grâce aux visuels par coloris branchés le 26/07 ;
5. **l'aboutissement est « Voici votre Trente-Neuf »** avec la montre en grand et ses spécifications — pas « 3 résultats ».
- **En cours de mesure** : combien de questions le catalogue supporte → `axes-guide-de-choix.md`.

Le vrai configurateur (assemblage à la commande) dépend entièrement de **BL Watches Parts Store**, qui a déclaré par messagerie pouvoir assembler mais **n'a fourni ni prix, ni délai, ni catalogue**. Voir `sourcing-configurateur.md` : ≈ 1 428 combinaisons ouvrables, l'axe **aiguilles reste fermé** faute d'alésages publiés.

## Ce qui attend Hakim

1. **Republier « Maison Noirmont »** et supprimer le thème brouillon obsolète.
2. **Médiateur de la consommation** — obligation légale. Adhésion **par site** : ne jamais recopier le CM2C de Tuftéo. Marqueur laissé en CGV art. 17.
3. **Affirmations fausses à retirer** : « 2 000 clients satisfaits », trois `review_count: 123`, badge « 1340 avis » — 0 commande réelle. Domaine réservé de Hakim.
4. **Comptes sociaux** : 12 champs vides, les comptes du fournisseur du thème ont été purgés du schéma.
5. **« Plongeuse » dans 3 titres Héritage** alors qu'elles sont à 5 bar (nage exclue) — le corps de texte le requalifie déjà en style.
6. **Images sur-promettant la capacité** : 4 rouleaux et 5 meubles montrent plus d'emplacements que vendus.
7. **Badge « En promotion »** retiré ; vérifier la règle française du prix de référence (30 jours) avant toute remise affichée.
8. **Faire confirmer BL Watches par écrit** : prix assemblé, délai France, catalogue, **alésages d'aiguilles**.
9. **Rendu mobile jamais vu** par un agent — seules des mesures existent.

## Pièges vérifiés (aussi dans Notion, page « Campement type »)

- `upsertedThemeFiles: []` sans `userErrors` = **écriture asynchrone, pas un échec**.
- `size`/`checksumMd5` se comparent aux **octets réellement écrits** ; `updatedAt` ne prouve rien.
- Un nœud `themeFiles` peut être **étiqueté d'un nom et contenir un autre fichier** — valider par empreinte.
- Une chaîne « introuvable » = presque toujours un **caractère invisible** (apostrophe typographique, espace insécable).
- Requêtes média **plafonnées à 30** — paginer.
- **Le SKU ne prouve pas l'identité visuelle** d'une image après découpage de coloris.
- Les **menus Shopify sont partagés entre thèmes** : créer un menu neuf, ne pas modifier l'existant.
- Un contraste se **mesure sur le rendu, opacité héritée comprise** — jamais déduit d'une valeur de couleur.
- Champ CSS de section et nom de schéma > 25 caractères : **rejets silencieux**.
- **Ne jamais utiliser `switch-shop`** : invalide la connexion Shopify pour tout le monde.
- SEMrush en formule gratuite rend **« 0 mot clé » sans erreur** passé le quota — utiliser un mot-clé témoin.

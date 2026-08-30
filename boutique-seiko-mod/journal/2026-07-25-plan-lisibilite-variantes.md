---
type: journal
boutique: seiko-mod
date: 2026-07-25
nature: analyse
leviers: [catalogue]
titre: "Plan « lisibilité des variantes & présentation » — NOIRMONT, 25/07/2026"
---

# Plan « lisibilité des variantes & présentation » — NOIRMONT, 25/07/2026

> Déclencheur : retour de Hakim sur captures d'écran. « Le nom des variantes ne veut rien dire pour certaines, moi en tant que client je ne comprends pas les noms. » Et : « inspire-toi de montre-avenue.fr, qui est aussi sur FullStack, il y a énormément de choses à récupérer en design et présentation. »
> Autonomie complète accordée. Ce document est la source de vérité du chantier et survit aux changements de session.

## 1. Diagnostic — ce qui est cassé

La francisation de juillet a traduit les **noms** d'options mais laissé les **valeurs** en codes fournisseur. La passe de nuit du 25/07 a corrigé 5 montres (coloris nommés + illustrés) et laissé le reste. État actuel :

| Fiche | Valeurs affichées au client | Nb |
|---|---|---:|
| Contre-la-montre — chronographe | `M-1` … `M20` | 20 |
| Voyageur — GMT | `1` … `9` | 9 |
| Noirmont Deux — plongeuse céramique | `Référence 1` … `7` | 7 |
| Intégrale — sport chic | `1` … `7` | 7 |
| Héritage — plongeuse vintage | `S1`, `S2`, `S3` | 3 |
| Remontoir Bois | `M11011`, `M12032`… | 8 |
| Rouleau de Voyage | `WB11` … `WB43` | 12 |
| Bracelet Présidentiel doré | « Jubilé — 12 », « Bracelet — 18 » | 24 |
| Loupe de date | « A · 4,0 mm », « B · 5,5 mm » | 14 |
| Set de tournevis | `A` … `E` | 5 |
| Remontoir Collection | « Rouge · 4 montres · **C** » | 15 |

**Le cas Remontoir Collection est le plus instructif** : « Rouge · 4 montres » est clair, c'est le suffixe `· A/B/C` qui pollue — un reliquat de nomenclature fournisseur laissé par confort.

**Second défaut, aggravant** : ces valeurs n'ont **aucune image associée**. Le client choisit à l'aveugle. Chez montre-avenue, les variantes sont des **pastilles de couleur** et la galerie **change au clic**.

## 2. Les deux moitiés du correctif

1. **Renommer** en libellés clients — suppose d'ouvrir chaque fiche fournisseur pour savoir ce qu'un `M14` désigne réellement. ⚠️ **Ne jamais toucher aux SKU** : ils portent le mapping DSers. On renomme des *valeurs d'option*, jamais un SKU.
2. **Illustrer** — image de variante quand le choix est visuel (couleur de cadran, matière), pastille de couleur quand c'est une simple couleur, rien quand c'est une dimension (taille de loupe).

## 3. Chantiers lancés le 25/07

| Agent | Objet | Navigateur | Livrable |
|---|---|---|---|
| Minage montre-avenue | sélecteur de variantes, bloc de vente croisée, badges d'attributs, anatomie de fiche, navigation | navigateur intégré | `2026-07-25-mining-montre-avenue.md` |
| Identification + renommage | relever les URL fournisseur manquantes dans DSers, identifier chaque code, renommer via `productOptionUpdate` | Chrome (session Hakim) | `2026-07-25-renommage-variantes.md` + liste des visuels à produire |

**Sérialisation du navigateur** : les deux agents utilisent des navigateurs *différents* (intégré vs Chrome) — c'est ce qui autorise le parallélisme. Ne jamais faire naviguer deux agents dans le **même** navigateur.

## 3 bis. ✅ RÉSOLU — comment obtenir les pastilles et le changement d'image

Résultat du minage (`2026-07-25-mining-montre-avenue.md`). ⚠️ Le domaine réel est **montre-avenue.com** — le `.fr` n'existe pas (NXDOMAIN). Site confirmé sous **FullStack 2.2**, donc portabilité acquise.

**Verdict : ni développement, ni réglage de thème — c'est de la donnée Shopify.** Le thème choisit seul son rendu :

| Donnée sur la valeur d'option | Rendu par FullStack |
|---|---|
| swatch **image** (JPG 156×156, ~1 Ko) | pastille illustrée |
| swatch **couleur** | aplat de couleur |
| **aucun swatch** | bouton texte ← *notre cas aujourd'hui* |

Nos `M14` / `WB33` sortent en boutons texte simplement parce que **nos valeurs d'option n'ont aucun swatch attaché**.

**Il faut donc deux choses, et les deux sont nécessaires :**
1. **Attacher un swatch** à chaque valeur d'option, via `productOptionUpdate` (couleur pour un cadran uni, image pour une matière ou un motif).
2. **Assigner une image à chaque variante** — sinon le clic ne change rien : la galerie est re-rendue côté serveur et l'image de la variante est placée en position 1.

Repère : chez eux la couverture est de **94 %** (15 fiches sur 16). Leur produit le plus récent est encore en boutons texte, **avec le même séparateur `·` que nous** — donc le `·` n'est pas en cause, c'est bien la pastille manquante.

### Autres acquis portables, par rapport effet/effort

1. **Badges d'attributs sous le titre** (« Grand cadran de 46 mm », « Étanchéité 3 ATM ») : un métachamp `list.single_line_text_field` + un bloc Texte + **11 lignes de CSS** dans le Custom CSS de la section. ~30 min, meilleur rapport du lot.
2. **Encart de vente croisée** (« −30 % sur un étui ») : **bloc natif FullStack `toggle-cross-sell`**, pas une application. ⚠️ **Mais il n'applique aucune remise** — le prix affiché est le prix plein. Si on annonce un pourcentage, il faut créer la remise automatique Shopify en parallèle, sinon c'est une promesse fausse au panier.
3. **Méga-menu** : ~57 collections en produit cartésien type × genre (« Montre automatique homme »). Piste SEO longue traîne.
4. **Leur discipline SKU est la nôtre** : codes fournisseur conservés dans le SKU, valeurs d'option en français client. Validation externe de notre règle.
5. **Angle d'attaque** : ils sont à **zéro avis** Judge.me. Notre preuve sociale est un différenciant réel.

## 4. Contrôles de non-régression obligatoires

- Après chaque renommage : nombre de variantes inchangé, **SKU identiques**.
- En fin de passe : compteurs DSers **Mes Produits 44 · AliExpress 44 · Unmapped 0**. Si un produit repasse en Unmapped, le renommage casse le mapping → **revenir en arrière et alerter**.
- Les 25 mappings historiques ne doivent jamais bouger.

## 5. Budget images

Solde Higgsfield au 25/07 : **~375 crédits**. Coût réel constaté en 4K : **~5,3 crédits/image** (et non 4 comme annoncé par l'API — budgéter avec marge).

Besoin estimé si l'on illustre tous les coloris de montres restants : 43 visuels ≈ **230 crédits**. Les accessoires s'ajoutent selon la liste produite par l'agent de renommage.

**Modèle imposé : `nano_banana_pro` en 4K, en image-to-image depuis la face produit validée.** Interdits : `soul_2` (invente de faux logos — cause racine d'un défaut corrigé cette nuit) et `openai_hazel` (réinvente l'objet : a ajouté un « XII » et une trotteuse lors du comparatif).

**Si les crédits s'épuisent** : un prompt de reprise prêt à l'emploi pour Codex est dans `PROMPT-CODEX-reprise-visuels.md` (même dossier).

## 6. Règles de marque non négociables (rappel)

- **100 % stérile** : aucun logo, aucune lettre, aucun chiffre romain typographié sur un cadran généré. Seuls chiffres tolérés : lunettes de plongée/GMT/tachymètre et guichets de date, à condition d'être nets.
- Aucune marque tierce dans un titre ou un texte, même si le titre fournisseur en cite une.
- Promesses vérifiables uniquement.
- ⚠️ **Exception documentée** : la fiche fournisseur du Trente-Neuf Duo (`1005006277907428`) annonce « Index Romain » et sa photo montre des chiffres romains **et du texte imprimé sur le cadran**. La description de notre fiche a donc raison, et c'est notre visuel qui est infidèle. À trancher : soit trouver une variante réellement stérile, soit retirer ce modèle du catalogue.

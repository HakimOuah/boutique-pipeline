# 17/08/2026 (soir) — Décisions Hakim appliquées : prix, renommage, sourcing, persona

> Trois consignes de Hakim : baisser le prix de l'OSWNKW et retirer les noms fournisseur AliExpress
> des titres ; sourcer les « adoucisseurs » (anti-calcaire électroniques) pour voir ; adapter le
> site au persona. Persona **considéré validé** par cette consigne (T-H3 soldé).

---

## 1. Prix + renommage (constaté sur le public)

**OSWNKW → 449,00 €** (bas de la fourchette 449-479 validée, aligné segment « tankless
certifié/smart »). Aucun `compareAtPrice` réintroduit. Constaté sur `products.json` public.

**11 fiches débaptisées** (les titres portaient les marques/codes fournisseur AliExpress —
`productUpdate`, 0 erreur, titres d'origine sauvegardés dans `backups/2026-08-17-renommage/`) :

| Avant | Après |
|---|---|
| Osmoseur OSWNKW 600 GPD à flux direct | **Osmoseur 600 GPD à flux direct — grands foyers** |
| Osmoseur 600 GPD sans réservoir OSWNKW (DRAFT) | Osmoseur 600 GPD sans réservoir — compact |
| Osmoseur de cuisine SHUANGLI 600G (DRAFT) | Osmoseur de cuisine 600G à osmose inverse |
| Dispositif anti-tartre ALTHY IPSE DN8 | Dispositif anti-tartre magnétique DN8 — sans sel |
| Dispositif anti-tartre magnétique IPSE DN25 / DN20 | … magnétique DN25 / DN20 |
| Cartouches pour filtre de robinet alloet | Cartouches pour filtre de robinet — lot anti-chlore |
| Purificateur d'eau de camping widesea | Purificateur d'eau de camping 0,01 micron |
| Carafe filtrante ALTHY 3,5 L | Carafe filtrante 3,5 L grande capacité |
| Filtre de douche ALTHY SFH70 non électrique | Filtre de douche à la vitamine C — non électrique |
| Filtre pour robinet de cuisine GLQ11 | Filtre pour robinet de cuisine — pose rapide |

Contrôle public : **0 titre restant avec OSWNKW / ALTHY / IPSE / widesea / alloet / GLQ11 / SHUANGLI**.

**Notes** :
- Les **handles** (URLs) n'ont pas été touchés — ils contiennent encore les codes fournisseur.
  Les changer imposerait des 301 ; à faire éventuellement au moment du passage FullStack (T-13 ?).
  Les meta-titres SEO étaient déjà propres (ex. « Anti-tartre magnétique DN20 | Bonum Vitae »).
- ⚠ **À vérifier par Hakim ou en QA visuelle** : si les produits ALTHY/IPSE portent le logo
  fournisseur **sur les photos**, retirer la marque du titre crée un écart photo/titre. Le
  contrôle photo par photo n'a pas été fait ce soir.

## 2. Sourcing anti-calcaire électroniques (T-H8 instruit)

Passerelle AliExpress (lecture seule), requêtes en mots rares. Preuve **classe B+** (API ; fret FR
exact à confirmer à l'étape DSers — l'endpoint `exact` refuse par ambiguïté de SKU).

### Candidats crédibles trouvés

| Produit | Ventes | Note | Coût (offer_sale_price) | Lecture |
|---|---|---|---|---|
| **Système détartrant électronique** (`1005008632801588`) | **309** | 4,7★ | **29,79 €** (prise EU, 12 V, stock 300+) | le meilleur ratio preuves/coût — type Calmat à impulsions |
| **LPS inhibition toute la maison** (`1005006005109143`) | **500+** | 4,9★ | **61,69 €** (SKU unique, stock 95) | le plus vendu, positionnement « toute la maison » |
| Système électronique (`33002421021`) | 99 | 4,8★ | 27,78 € | alternative |
| Électronique (`1005009224165328`) | 19 | 4,4★ | 29,44 € | fond de liste |
| BriskSpring « physique » (`1005012046405168`) | 11 | 4,3★ | 31,19 € | marque inconnue, peu de preuves |

### Découverte annexe — les coûts de notre catalogue actuel

Le sourcing a fait remonter **nos propres produits** chez le fournisseur : ALTHY IPSE DN8 coûte
**28,59-30,99 €** (vendu 86,90 €), l'IPSE super-magnétique **39,96 €** (vendu 152,90 €). La marge
actuelle est donc ~×3-4 — c'est ce qui rendait le prix indéfendable face au marché (aimants 20-50 €).

### Lecture (pas un verdict — décision Hakim, T-H8)

- Un électronique à ~30 € de coût peut se vendre **129-179 €** : sous Calmat (408-544 €), au-dessus
  du gadget, marge confortable, et on reste dans la fenêtre « adoucisseur sans sel » (8 160/mois,
  KD 8-19). Le LPS à 61,69 € peut viser **179-229 €** en « toute la maison ».
- **Le verrou n'est pas le prix, c'est la promesse** : l'Anses juge l'efficacité de ces procédés non
  démontrée. Vendre en respectant notre ligne = « dispositif d'appoint, sans sel ni entretien, qui
  ne remplace pas un adoucisseur à résine » — exactement notre FAQ actuelle. Pas de « adoucit
  l'eau », pas de « élimine le calcaire ». Publicité Shopping sur ces produits : déconseillée
  (claims difficiles) ; vente catalogue + SEO éditorial : possible.
- Interdits respectés : aucune commande, aucun contact vendeur. Fret FR et galerie photo = étape
  DSers si Hakim retient un candidat.

## 3. Site adapté au persona (FullStack v1.1, vérifié à distance)

- **Hero** : le paragraphe parle désormais le langage client observé — « Goût de chlore, packs
  d'eau à porter, calcaire sous la douche : équipez le bon point d'usage, pas le plus cher… coût
  d'entretien compris ».
- **FAQ accueil** : + « L'eau osmosée a-t-elle du goût ? » (objection n°1 des forums — réponse
  honnête, reminéralisation mentionnée si documentée) ; réponse consommables réécrite avec
  l'angle « coût d'entretien affiché avant l'achat, jamais une surprise ».
- **FAQ produit** : + la même question goût (7 questions).
- **Accordéon « Entretien et consommables »** : « pas d'abonnement obligatoire », prix des
  consommables affichés — le contre-pied direct de l'abonnement Waterdrop.
- Vérifié par relecture API sur la copie `205568147794`. Rien sur le MAIN.

## Reste ouvert

- T-H7 (autres lignes de prix : carafes ALTHY 129-174 €, ALTHY douche 111-149 €, magnétiques 153 €
  — **d'autant plus urgents qu'on connaît maintenant les coûts ~×3-4**).
- T-H8 : choix du candidat électronique (ou renoncement).
- T-11 : QA préview FullStack.
- Handles avec codes fournisseur (301 à prévoir si on les nettoie).

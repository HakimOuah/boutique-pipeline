# Audit manuel final — chien et aquariophilie

Date d'observation : 2026-08-08  
Source auditée : `codex-chasse-clusters/runs/2026-08-08-kraken-catalogue-expansion-v2/final-catalogue.json`

## Périmètre et règle de décision

Les 127 lignes des niches **Aquariophilie & aquascaping** et **Balade, transport & mobilité du chien** ont été relues individuellement. La décision compare le mot-clé SEO au titre du listing AliExpress présent dans le catalogue.

- `ACCEPT` : le listing désigne bien le produit recherché, ou un produit hybride réellement utilisable dans la niche.
- `REJECT` : le listing est un accessoire du produit, un homonyme, un produit hors niche, une machine industrielle, un résultat pollué (pêche, piscine, hot-dog, plastique PET, etc.) ou une simple variante/doublon fonctionnel.

Cet audit qualifie uniquement la pertinence sémantique du titre fourni. Il ne prouve ni la qualité réelle, ni les variantes disponibles, ni le prix livré en France, ni la conformité réglementaire du produit.

## Résultats

| Niche | Lignes contrôlées | ACCEPT | REJECT | Taux d'acceptation |
|---|---:|---:|---:|---:|
| Aquariophilie & aquascaping | 68 | 25 | 43 | 36,8 % |
| Balade, transport & mobilité du chien | 59 | 32 | 27 | 54,2 % |
| **Total** | **127** | **57** | **70** | **44,9 %** |

Le détail exhaustif, avec une justification propre à chaque ligne, se trouve dans `manual-audit-final-chien-aquarium.json`.

## Motifs de rejet récurrents

### Aquariophilie & aquascaping

- **Accessoire présenté comme le produit principal** : ventouse de chauffage, sac de média, tuyau, raccord, brosse ou pièce de pompe classés comme chauffage, filet, filtre ou pompe.
- **Mauvais mécanisme produit** : anneaux de nourrissage classés comme distributeurs automatiques de nourriture.
- **Pollution sémantique ou produit hors cible** : éclairage de piscine, jouet, fontaine, pendentif, bac ou autre objet multiusage ne répondant pas au mot-clé aquarium.
- **Doublon fonctionnel** : plantes artificielles, bois décoratifs, cachettes, figurines lumineuses, bandelettes ou éclairages répétés sans différence d'usage substantielle.
- **Pièce propriétaire ou produit sans équivalent générique crédible** : rejet lorsque le titre ne désigne pas un article autonome sourceable pour le catalogue.

Les familles les plus propres parmi les lignes conservées sont les siphons/aspirateurs, filets, décorations réellement prévues pour aquarium, kit CO2, pompe à air USB, tests d'eau, thermomètres, tuyaux par matière et éclairages dont l'usage aquarium est explicite.

### Balade, transport & mobilité du chien

- **Accessoire présenté comme le produit principal** : adaptateur ou clip classé comme ceinture, attache de sac à déjections classée comme laisse, ou longe secondaire classée comme harnais.
- **Homonyme ou usage étranger à la niche** : bijou humain, corde à linge, sac générique ou autre résultat contenant le terme sans être le produit canin recherché.
- **Produit hors périmètre** : manchettes décoratives, cônes de récupération, accessoires purement décoratifs ou camionnette/matériel industriel de toilettage.
- **Doublon/variante simple** : répétitions de colliers, gamelles pliables, harnais, laisses, rampes ou modèles gonflables ne changeant pas l'usage principal.
- **Mauvais niveau de produit** : élément partiel ou accessoire de fixation alors que le mot-clé vise un équipement complet.

Les familles les plus propres parmi les lignes conservées sont les colliers différenciés par mécanisme ou matière, harnais complets, laisses fonctionnelles, retenues automobiles, équipements réfléchissants/LED, muselière, médaille d'identification et rampes réellement adaptées à un usage de mobilité canine. Le collier pare-chocs pour chien aveugle a été conservé comme hybride de mobilité pertinent.

## Contrôles d'intégrité

- 127 décisions pour 127 lignes sources ciblées.
- 127 identifiants produit uniques ; aucun identifiant manquant ou ajouté.
- Niche et mot-clé identiques à la source pour chaque identifiant.
- Décisions limitées à `ACCEPT` ou `REJECT`.
- Catalogue source, scripts, classeur et Git laissés inchangés.

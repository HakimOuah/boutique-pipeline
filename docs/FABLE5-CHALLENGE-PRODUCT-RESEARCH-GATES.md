# Challenge Fable 5 — portes de décision Product Factory

Date : 2026-08-23

## Décision proposée

Le système ne doit plus appeler `GO marché` la porte située après la mesure
express. À ce stade, ni le fournisseur exact, ni le fret, ni la marge réelle,
ni la densité concurrentielle, ni le droit de gagner ne sont suffisamment
établis.

La porte précoce devient :

```text
PASS_PREQUALIFICATION | REVIEW_PREQUALIFICATION | STOP_PREQUALIFICATION
```

`PASS_PREQUALIFICATION` autorise une due diligence bornée. Il n'autorise ni
boutique, ni commande, ni publication, ni campagne.

Le seul GO commercial devient :

```text
GO_FINAL | WATCH_FINAL | NO_GO_FINAL
```

Il intervient après sourcing exact, concurrence approfondie et économie.

## Workflow à challenger

```text
mode PRODUIT_PUR ou UNIVERS
  -> idéation TrendTrack
  -> mesure France + SERP + Trends + sonde prix
  -> PASS/REVIEW/STOP_PREQUALIFICATION
  -> [sourcing AliExpress exact || concurrence approfondie]
  -> coût rendu + logistique + marge + droit de gagner
  -> GO/WATCH/NO_GO_FINAL par Hakim
  -> personas, offre, marque, boutique, GMC, Ads
```

## Ce qui est automatisable

- classification du mode et contrôle d'étanchéité ;
- mesures et diagnostics sourcés ;
- inventaire concurrentiel factuel ;
- sélection/quote du SKU exact et économie ;
- recommandation technique `GO`, `WATCH`, `NO_GO` ou `INCONCLUSIVE` ;
- vérification que toutes les preuves minimales existent.

## Ce qui reste humain

- choix d'un cas limite ;
- appréciation finale du droit de gagner ;
- acceptation d'un risque conformité/logistique ;
- `GO_FINAL` ;
- commande test, publication, GMC, budget et dépenses.

## Questions adressées à Fable 5

1. La distinction préqualification / décision finale évite-t-elle réellement
   les faux GO sans rendre le pipeline trop lent ?
2. Sourcing et concurrence doivent-ils être parallèles après le pass, ou
   séquencés selon un filtre supplémentaire ?
3. Quelles preuves minimales doivent rendre `GO_FINAL` impossible : absence de
   SKU exact, fret non daté, concurrence non examinée, marge non contributive,
   risque réglementaire non tranché ?
4. `WATCH_FINAL` doit-il permettre la commande test tout en bloquant la
   construction de boutique ?
5. Le bot peut-il produire une recommandation technique appelée `GO`, ou faut-il
   la renommer `TECHNICAL_PASS` pour réserver totalement le mot GO à Hakim ?
6. Pour un UNIVERS, quel niveau minimal de sourçabilité par famille faut-il
   exiger avant décision finale sans sourcer artificiellement 100 produits ?
7. La concurrence doit-elle être un gate binaire ou une matrice graduée
   (densité, actifs défensifs, espace, différenciation, acquisition) ?

## Invariants non négociables

- la catégorie demandée contrôle le verdict principal ;
- aucun accessoire rentable ne sauve un mauvais produit principal ;
- aucune marge fiable sans SKU et fret exacts ;
- aucun sourcing avant `PASS_PREQUALIFICATION` ;
- aucun downstream avant `GO_FINAL` ;
- aucun GO automatique par un bot ;
- aucune publication, commande, GMC ou dépense implicite.

## Références

- `PRODUCT-RESEARCH-CRITERIA.md`
- `plans/2026-08-22-plan-recherche-30x30-pur-univers.md`
- `../GROK-BOT-FLEET.md` dans le dépôt `boutiques-drop`
- `docs/PRODUCT_RESEARCH_MODE_DESIGN.md` dans `aliexpress-mcp-server`
- `docs/OPPORTUNITY_SCORING_DESIGN.md` dans `aliexpress-mcp-server`

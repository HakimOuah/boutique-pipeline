# Prompt d'intégration — à coller dans Claude Code (app Claude macOS)

Copie-colle le bloc ci-dessous dans Claude Code, en ayant ouvert ton repo
`dropshipping-product-factory`. Dépose d'abord le dossier `broyeur/` du package
à la racine du repo (ou dans le sous-dossier de ton choix, ajuste le chemin).

---

## BLOC À COLLER

Contexte : je construis DropPilot, un pipeline de recherche produit dropshipping
(marchés FR/BE/CH/LU, Google Ads + Shopify). J'ai un module de scoring appelé
"le broyeur" qui décide quels produits partent en shortlist. Il est déjà écrit
et testé (16/16), dans le dossier `broyeur/`.

Ta mission : intégrer ce broyeur dans le pipeline et brancher les agents de
sourcing dessus. Étapes :

1. Lis `broyeur/README.md` et `broyeur/scoring_config.yaml` pour comprendre le
   contrat d'entrée (le modèle Product et les champs attendus).

2. Vérifie que les tests passent : `pytest broyeur/tests/ -v`. Ils doivent être
   16/16. Ne modifie PAS scoring_config.yaml sans me demander : c'est la source
   de vérité des seuils, validée manuellement.

3. Crée un agent de sourcing "Bigbuy" (ou adapte un agent existant) qui produit
   un livrable markdown au format attendu par `broyeur/adapter.py` (un bloc par
   produit, champs `- clé: valeur`, séparés par `---`). L'agent doit remplir au
   minimum : product_name, source, category, price_sell, price_source_ali,
   competitors_type, sells_in_search, legal_eu. Laisse à None ce qu'il ne peut
   pas déterminer — le broyeur gère.

4. Câble le flux : agent sourcing → markdown → `python -m broyeur.run --input
   livrable.md --format md --shortlist-only` → la shortlist part vers l'étape
   Semrush existante.

5. IMPORTANT — pré-filtres : pour économiser des appels, fais en sorte que
   l'agent de sourcing n'inclue PAS dans son livrable les produits qui seront
   de toute façon rejetés en hard filter (ticket < 150€ hors marge exceptionnelle,
   catégories exclues, grande enseigne dominante). Les hard filters du YAML sont
   ta référence pour ces pré-filtres.

Contraintes :
- Python, cohérent avec le reste du pipeline.
- Ne réécris pas la logique de scoring : le broyeur est la seule autorité de
  décision. Les agents produisent des candidats, le broyeur tranche.
- Si un champ enum est ambigu pour l'agent (ex: competitors_type), documente
  comment il doit le déterminer plutôt que de deviner.

Commence par lire le README et lancer les tests, puis propose-moi ton plan
d'intégration avant d'écrire l'agent de sourcing.

---

## Ordre de déploiement suggéré des agents de sourcing

Une fois Bigbuy branché et validé, ajoute les autres dans cet ordre
(du plus rentable en effort/signal au moins prioritaire) :

1. **Bigbuy** — structure stable, catalogue le plus riche. Idéal pour valider le flux.
2. **Amazon Movers & Shakers** — structure stable, signal de demande fort.
3. **Cdiscount** + **Vevor** + **Europages** — structure stable, même moule que Bigbuy.
4. **Flippa** + **Dotmarket** — navigation réelle (Claude in Chrome/Playwright),
   signal le plus fort (business déjà rentables).
5. **Pinterest Trends** — navigation, signal avancé mais orienté déco/mode.
6. **Temu** — en dernier, méthode risquée (client peut acheter direct sur Temu).

Les 5 premières (structure stable) peuvent tourner en n8n sur ton VPS en autonome.
Les 4 dernières nécessitent un agent navigateur.

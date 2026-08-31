# Lumière Matière — pré-soumission GMC (31/08/2026)

Storefront relu le 31/08. **Écritures Shopify bloquées** : le token custom répond `shop { name }` mais refuse `products`, `themes`, `files`, `pages`. Le token CLI est expiré (401). Lots 2 à 6 prêts, pas poussés.

## Bloqué chez Hakim (2 minutes)

### 1.1 Adresse boutique — priorité 1

**Paramètres → Général → Coordonnées de la boutique**

| Champ | Actuel (JSON-LD home) | Cible |
|---|---|---|
| Adresse | 13 Allée Georges Brassens | 47 rue Vivienne |
| Ville | Saint-Prix | Paris |
| CP | 95390 | 75002 |
| Téléphone | 0756916084 | +33 7 56 82 80 94 |

Ne pas toucher aux pages mentions / CGV / footer : ils disent déjà Paris.

### 1.2 Scopes de l’app custom

Cocher : `read_products`, `read_files`, `write_files`, `read_themes`, `write_themes`, `read_content`, `write_content`, `write_legal_policies`, `read_publications`. **Pas** `write_products`.

Réinstaller → coller le nouveau token dans `boutique-pipeline/.env` (`SHOPIFY_LUMIERE_MATIERE_TOKEN`) → dire « c’est bon ».

Puis :

```bash
cd boutique-pipeline/catalogues/lumierematiere/shopify
python3 gmc_pre_submit.py --audit
python3 gmc_pre_submit.py --apply-texts
python3 gmc_pre_submit.py --apply-media
python3 gmc_pre_submit.py --apply-theme
```

Le thème est dupliqué sous **LM GMC 2026-08-31**, jamais publié.

## Confirmé live (ne pas « corriger » autrement)

| Point | Live 31/08 |
|---|---|
| JSON-LD `sameAs` themefullstack | 4 occurrences, home |
| JSON-LD adresse / tél | Saint-Prix / `0756916084` |
| SKU AE dans JSON-LD PDP | `200000531` présent (ex. verre-538307) |
| Alt « vue Codex N » | 35 médias / 7 fiches |
| Noms fichier AE `S…webp` | 9 / `applique-murale-pierre-metal-147598` |
| CGV §4 Klarna | absent du corps (pictos footer seulement) |
| FAQ « garantie de 30 jours » | encore en ligne |
| Collections menu < 5 publics | XXL 1 · plaf. cuisine 1 · osier 2 · lustres chambre 3 · bambou 3 · pierre 4 · salon 4 |
| Délais 7–18 / identité OH Ventures / 0 avis / 0 prix barré public | inchangés |

## Déjà préparé en local (pas encore sur Shopify)

- `pages/faq.md` — retour 30 j, plus de « garantie commerciale »
- `pages/cgv.md` — CB + Maestro + Klarna
- `pages/conditions-paiement.md` — même liste (alignement footer / caisse)
- `shopify/gmc_pre_submit.py` — audit 6.1/6.2, alts, textes, copie thème

§3.2 (renommer les 9 fichiers AE) : le script s’arrête avant l’upload ; à finir une fois `write_files` ouvert. Détachement, pas `fileDelete`.

§6.1 / §6.2 : impossible sans `read_products`. Aucune liste de brouillons inventée.

## Hors périmètre (inchangé)

TVA `taxable: false` vs mentions FR55… — décision comptable. Publication thème / brouillons — Hakim. SKU variantes — intouchables.

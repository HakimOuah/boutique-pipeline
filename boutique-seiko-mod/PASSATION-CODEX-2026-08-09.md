# Passation à Codex — Maison Noirmont, 09/08/2026

Claude Code atteint sa limite hebdomadaire (réinitialisation dans 4 jours, soit le **13/08/2026**). Ce document est **autoportant** : il te donne l'état réel, les règles, les pièges déjà payés et l'ordre de travail. Tu prends le relais sur la boutique **Maison Noirmont** (seiko mod, `maisonnoirmont.fr`).

Tous les chemins sont relatifs à `~/Documents/Boutiques drop/boutique-pipeline/`. Branche de travail : **`main`**. Commit + push après chaque unité de travail terminée — la coupure de session du 09/08 a prouvé qu'il ne faut jamais accumuler du travail non poussé.

---

## 1. Où en est la boutique

| | |
|---|---|
| Catalogue | **199 produits** — 96 actifs (l'ancien catalogue), **103 brouillons** dont les 94 importés le 09/08 |
| Thème | **publié le 09/08** par Hakim. Les correctifs du 08/08 sont donc en ligne |
| Statut public | boutique **encore sous mot de passe** — rien n'est visible, aucun risque actif |
| Collections | 10 créées le 09/08, **non publiées sur le canal Online Store** (leurs produits sont en brouillon) |
| Merchant Center | **pas encore créé** — c'est volontaire, voir §5 |
| Mesure d'achat | **absente** (ni GA4 ni gtag). Bloquant avant toute dépense publicitaire |

### Ce qui a été fait les 08 et 09/08
- Purge de conformité : 46 visuels de faux avis détachés (37 fiches), 931 prix barrés supprimés, 931 SKU AliExpress réécrits en `NOIR-<trigramme>-<n°>`, « 904L » purgé avec redirections 301.
- Sourcing + import DSers de **94 produits** « Pièces & Mod » en brouillon, montés en **preuve classe A**.
- 10 collections créées avec textes rédigés et métadonnées ; les 94 fiches habillées en français.
- Production de visuels maison en cours (~90 livrés, rattachés au fil de l'eau).
- Passe de cohérence : **16 fiches sur 94 corrigées** (écart texte/produit).

---

## 2. Les règles non négociables

Elles viennent de décisions de Hakim et d'incidents réels. Ne les assouplis pas.

### Visuels
1. **Toujours partir de la photo produit du fournisseur.** Le produit — cadran, index, aiguilles, bracelet, boîtier, coloris — est repris tel quel et **jamais réinventé**. **Seule la situation de présentation change** (fond, décor, lumière, contexte de port). Composition / image-to-image, jamais de génération à partir de rien.
2. **Ne jamais publier une photo AliExpress brute.** Google rapproche ces images, identiques sur des dizaines de boutiques ; le client les reconnaît. C'est un matériau de départ, pas un livrable. **Les 94 fiches importées portent encore ces photos : elles ne peuvent pas être activées avant d'être habillées.**
3. **Aucun logo, sigle, lettrage ni mention d'origine sur les cadrans.**
4. **Aucun avis, note, étoile ou badge incrusté** dans une image.
5. Format : 2048×2048, 1:1, JPEG sRGB. Suffixes de fichier **`-6` et `-7` interdits** (c'étaient ceux des faux avis).

### Contenu
- **Aucune spécification inventée.** Si une donnée manque, ne l'affirme pas. Deux caractéristiques inventées ont été trouvées et corrigées le 09/08 (« triangle à midi », « écailles de plume de paon »).
- **Aucune promesse de délai** qui contredirait la fenêtre de livraison réelle relevée.
- Aucun avis, note ou chiffre de satisfaction dans les textes. La boutique a **0 commande client**.

### Interdits absolus
- **Aucune commande, aucun achat, aucun paiement** — ni sur AliExpress, ni via DSers.
- **N'active aucun brouillon** et ne publie aucune collection sans accord de Hakim.
- Ne touche pas aux 96 produits actifs sans raison explicite.
- Les tactiques de contournement du corpus (proxy, anti-detect, comptes de secours, contenu différencié pour l'examinateur) sont **exclues** : on vise la conformité réelle.

---

## 3. Les pièges déjà payés — ne les repaie pas

**Lecture des SERP AliExpress.** Note et ventes sont collées sans séparateur : « 531 vendus » se lit **5,0 étoiles / 31 ventes**. Seule la fiche produit ouverte fait foi. Règle appliquée : **moins de 10 ventes réelles = refus**.

**Les fiches AliExpress ne s'ouvrent pas dans un navigateur automatisé** (reCAPTCHA), mais **s'ouvrent normalement dans le Chrome de Hakim**. C'est le seul chemin vers la preuve classe A. Ne contourne aucun anti-bot.

**Trois verbatims de marque trouvés sur des produits vendus « sans logo »** : « SWISS MADE », « SUPERLATIVE CHRONOMETER / OFFICIALLY CERTIFIED » (Rolex), logo « Tandorio ». **Zoome systématiquement le cadran** avant de retenir un produit. Un signalement de contrefaçon sur un compte Merchant Center neuf coûte beaucoup plus cher que le produit ne rapporte.

**La QA de Codex laisse passer des défauts.** Plusieurs visuels validés `done` ont été rattrapés par un contrôle indépendant. Défaut caractéristique identifié le 09/08 : **le modèle promeut un index en chiffre** (un « 1 » peint au repère de 1 h là où la source porte un bâton nu). Contrôle repère par repère contre la source.

**Écrire du texte depuis les données fournisseur sans voir le produit dérive** : 1 fiche sur 6 portait un écart. Confronte toujours le texte aux images.

**`themeFilesUpsert` renvoie parfois `upsertedThemeFiles: []` sans erreur alors que l'écriture a réussi.** Vérifie par empreinte md5 du fichier distant.

**La case « Set product status as Draft » de DSers se remet à zéro à chaque lot** malgré le cache. Relis le DOM avant chaque validation, sinon des fiches arrivent actives avec les photos brutes.

**`compare_at_price` et le SKU ne sont pas des champs filtrables** sur `productVariants` : un `query:` est ignoré silencieusement et renvoie tout. Seul un scan paginé fait preuve.

---

## 4. Le pont d'ordres — comment produire des visuels

Point d'entrée unique : dépose un ordre JSON dans `ordres/pour-codex/inbox/`, puis `bash ordres/generer-images.sh`, puis lis `ordres/pour-codex/resultats/`.

- Contrat : `docs/codex-handoff/14-PROTOCOLE-ORDRES.md` §9. Spécification exécutant (DA, contraintes, QA) : `docs/codex-handoff/15-CODEX-EXECUTANT-IMAGES.md`.
- **Valide avant tout lancement** : `/usr/bin/python3 ordres/valider_ordre.py <fichier>.json`.
- **Code de sortie 2 = verrou d'exécutant actif : attendre et réessayer, ne JAMAIS forcer le verrou.**
- Binaire : `export PATH="$HOME/.npm-global/bin:$PATH"` (`@openai/codex`).
- Compter **8 à 10 minutes par visuel retenu**, une fiche par ordre.

### État de la file à la passation
- **5 ordres en attente** dans `inbox/` (cadrans stériles couleur).
- **1 ordre dans `en-cours/`** : `20260809-2300-generate_images-cadran-sterile-couronne-3h-28-5.json` — la session a été coupée pendant son traitement. **Vérifie son état avant de le relancer** : soit son résultat est dans `resultats/`, soit il faut le remettre en `inbox/`. Ne le double pas.

### Nommage et rangement — figés, à respecter à la lettre
- Dossier par fiche : `boutique-seiko-mod/visuels-codex-2026-08/<handle>/` (`<handle>` = handle Shopify exact).
- Galerie : `<handle>-g1.jpg`, `-g2.jpg`… — numérotation interne à la livraison, **pas une position d'affichage**.
- Variante : `<handle>-v-<code>.jpg`, `<code>` = fragment couleur du SKU fournisseur en minuscules (`#Black1` → `black1`).
- Un `manifeste.json` par dossier : `{handle, images[{fichier, handle, slot, sku_fournisseur, source}], ecartes[]}`.
- ⚠️ **Le `sku_fournisseur` est indispensable** : les SKU Shopify ont été réécrits en `NOIR-*`, le lien coloris↔photo n'existe plus que dans ce manifeste et dans `backup-sku-2026-08-08/table-correspondance.jsonl`. Si un appariement est ambigu, mets l'entrée dans `ecartes` avec un motif — **ne devine pas**.
- Les visuels **sont versionnés dans git** (convention du dépôt).

### Rattachement sur Shopify
- `productCreateMedia`, **toujours en fin de galerie, jamais en position 1** : l'image principale est la vignette des pages de collection.
- `alt` descriptif **en français** obligatoire sur chaque média.
- Ne supprime aucun média existant. Journal : `RATTACHEMENT-VISUELS-2026-08-09.md`.

---

## 5. Ordre de travail proposé

### P0 — ce qui bloque l'ouverture Merchant Center
1. **Trancher le sort de `cadran-lumineux-28-5-nh35`** : vendu « stérile », porte « SUPERLATIVE CHRONOMETER / OFFICIALLY CERTIFIED » (Rolex). Recommandation de Claude : **abandonner le produit**. Décision de Hakim.
2. **Dédoublonner 3 paires de fiches** (même produit AliExpress référencé deux fois) — sinon deux pages se cannibalisent sur le même mot-clé. Liste dans `COHERENCE-FICHES-2026-08-09.md`.
3. **Corriger la collection active `montre-cadran-a-chiffres`**, qui affirme « nous ne proposons pas de chiffres orientaux » — vrai aujourd'hui, faux dès l'activation des cadrans arabes.

### P1 — le chantier principal
4. **Re-sourcer la collection cadran arabe.** C'est le mot-clé porteur (15 500 recherches/mois) et il ne reste que **5 produits réels** (4 cadrans + 1 montre finie) : 2 refusés au push pour ventes insuffisantes, 3 écartés le 09/08 car sans écriture arabe véritable. Il en faut **4 à 8 de plus**, en classe A, avec écriture arabe orientale vérifiée à l'image et aucun verbatim de marque. Un travail était en cours à la coupure — vérifie `RESOURCING-CADRAN-ARABE-2026-08-09.md` s'il existe.
5. **Débloquer ou abandonner les 5 fiches cadran arabe bloquées** : leur photo fournisseur porte une marque au cadran. Il faut d'autres photos fournisseur, ou renoncer.
6. **Produire les visuels maison des fiches restantes.** Sans eux, les 94 brouillons ne peuvent pas être activés. Priorité : cadrans stériles couleur (non entamés), puis le reste des pilote 1-12.
7. **Compléter les galeries des 96 fiches actives** : le brief `CONSIGNES-CODEX-VISUELS-2026-08-08.md` chiffre ~319 visuels (74 de galerie + 245 de variantes, tous coloris conservés sur décision de Hakim du 08/08). ~90 produits à ce jour.

### P2 — avant lancement
8. Installer la **mesure d'achat** — voir `TRACKING-ET-CONSENTEMENT-2026-08-08.md`, 10 étapes au clic près. Voie retenue : app **Google & YouTube** (sur le plan Basic, le code de thème ne peut pas voir l'achat). ⚠️ **Ne pas laisser l'app créer le Merchant Center avant que le CSS soit arrêté.**
9. Reprendre les **P0/P1 restants de `AUDIT-GMC-FINAL-2026-08-08.md`**, puis seulement ensuite ouvrir le compte.

---

## 6. Ce qui appartient à Hakim — ne pas faire à sa place

- **Coller les 3 textes de politiques** préparés dans `backup-retours-2026-08-08/a-appliquer-par-hakim/` : le connecteur n'a pas la permission `write_legal_policies`, donc les CGV et la politique de remboursement servies portent **encore la clause interdite**.
- **Adhérer à un médiateur de la consommation** (obligation légale FR, toujours `[À COMPLÉTER]` en CGV art. 17).
- **Arbitrer la grille de prix** : plusieurs coûts réels sont inférieurs aux estimations (9,19 € contre 18,49 € sur un exemple). Deux stratégies chiffrées dans `TEXTES-ET-COLLECTIONS-2026-08-09.md`, aucun prix n'a été écrit.
- **Basculer l'e-mail boutique** de `contact.noirmont@gmail.com` vers `contact@maisonnoirmont.fr` (déjà utilisée partout ailleurs) — ⚠️ vérifier d'abord que la boîte `.fr` reçoit, sinon les e-mails de commande partent dans le vide.
- **Vérifier le mapping DSers** des 2 fiches « Voyageur Or ».
- Toute installation d'app, création de compte, publication de thème ou activation de produit.

---

## 7. Où trouver le détail

| Sujet | Fichier |
|---|---|
| Audit de conformité complet (80+ points) | `AUDIT-GMC-FINAL-2026-08-08.md` |
| Les 94 produits importés, données réelles | `PUSH-DSERS-2026-08-09.md` |
| Collections, textes, grille de prix | `TEXTES-ET-COLLECTIONS-2026-08-09.md` |
| Les 16 écarts corrigés, comptes par collection | `COHERENCE-FICHES-2026-08-09.md` |
| Brief visuels complet (~319, règles, slots) | `CONSIGNES-CODEX-VISUELS-2026-08-08.md` |
| Production de visuels en cours | `FOURNEE-VISUELS-NOUVEAUX-2026-08-09.md` |
| Rattachements faits | `RATTACHEMENT-VISUELS-2026-08-09.md` |
| Tracking et consentement, 10 étapes | `TRACKING-ET-CONSENTEMENT-2026-08-08.md` |
| Registre de sourcing | `SOURCING-COLLECTIONS-2026-08-09.md` |
| État général et thèmes | `REPRISE-SESSION.md` |

**Deux travaux étaient en cours à la coupure** — production de visuels (cadrans stériles) et re-sourcing cadran arabe. Vérifie l'état réel des fichiers et de `ordres/pour-codex/` avant de relancer : ne double aucun travail déjà fait.

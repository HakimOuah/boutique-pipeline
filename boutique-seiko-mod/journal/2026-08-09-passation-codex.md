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

### État de la file à la passation — relevé au moment de l'arrêt

**4 ordres validés en attente dans `inbox/`** :
- `20260809-2300-…-cadran-sterile-sunburst-28-5.json`
- `20260809-2400-…-cadran-meteorite-28-5.json`
- `20260809-2400-…-cadran-vierge-sterile-28-5.json`
- `20260810-0030-…-cadran-pilote-noir-33-5-nh34.json`

**1 ordre bloqué dans `en-cours/`** : `20260809-2300-…-cadran-sterile-lumineux-28-5.json`. L'exécutant a été arrêté en cours de traitement. **Aucun résultat n'a été écrit pour lui** — remets-le dans `inbox/` et relance-le. Ne le considère pas comme fait.

**Verrou périmé** : `ordres/.lock-codex` date du 09/08 23:27 et son exécutant n'existe plus. `generer-images.sh` remplace automatiquement tout verrou de plus de 30 minutes — laisse le script s'en charger, **ne le supprime pas à la main**.

**Une livraison à contrôler avant rattachement** : `boutique-seiko-mod/livraisons/visuels-codex-2026-08/cadran-sterile-couronne-3h-28-5/` contient 3 visuels et son manifeste, mais l'arrêt est intervenu avant la QA indépendante. **Contrôle-les avant de les poser** (voir §3, défaut « index promu en chiffre »).

### Nommage et rangement — figés, à respecter à la lettre
- Dossier par fiche : `boutique-seiko-mod/livraisons/visuels-codex-2026-08/<handle>/` (`<handle>` = handle Shopify exact).
- Galerie : `<handle>-g1.jpg`, `-g2.jpg`… — numérotation interne à la livraison, **pas une position d'affichage**.
- Variante : `<handle>-v-<code>.jpg`, `<code>` = fragment couleur du SKU fournisseur en minuscules (`#Black1` → `black1`).
- Un `manifeste.json` par dossier : `{handle, images[{fichier, handle, slot, sku_fournisseur, source}], ecartes[]}`.
- ⚠️ **Le `sku_fournisseur` est indispensable** : les SKU Shopify ont été réécrits en `NOIR-*`, le lien coloris↔photo n'existe plus que dans ce manifeste et dans `boutique-seiko-mod/backups/backup-sku-2026-08-08/table-correspondance.jsonl`. Si un appariement est ambigu, mets l'entrée dans `ecartes` avec un motif — **ne devine pas**.
- Les visuels **sont versionnés dans git** (convention du dépôt).

### Rattachement sur Shopify
- `productCreateMedia`, **toujours en fin de galerie, jamais en position 1** : l'image principale est la vignette des pages de collection.
- `alt` descriptif **en français** obligatoire sur chaque média.
- Ne supprime aucun média existant. Journal : `2026-08-09-rattachement-visuels.md`.

---

## 5. Ordre de travail proposé

### P0 — ce qui bloque l'ouverture Merchant Center
1. **Trancher le sort de `cadran-lumineux-28-5-nh35`** : vendu « stérile », porte « SUPERLATIVE CHRONOMETER / OFFICIALLY CERTIFIED » (Rolex). Recommandation de Claude : **abandonner le produit**. Décision de Hakim.
2. **Dédoublonner 3 paires de fiches** (même produit AliExpress référencé deux fois) — sinon deux pages se cannibalisent sur le même mot-clé. Liste dans `2026-08-09-coherence-fiches.md`.
3. **Corriger la collection active `montre-cadran-a-chiffres`**, qui affirme « nous ne proposons pas de chiffres orientaux » — vrai aujourd'hui, faux dès l'activation des cadrans arabes.

### P1 — le chantier principal
4. **Re-sourcer la collection cadran arabe.** C'est le mot-clé porteur (15 500 recherches/mois) et il ne reste que **5 produits réels** (4 cadrans + 1 montre finie) : 2 refusés au push pour ventes insuffisantes, 3 écartés le 09/08 car sans écriture arabe véritable. Il en faut **4 à 8 de plus**, en classe A, avec écriture arabe orientale vérifiée à l'image et aucun verbatim de marque. Un travail était en cours à la coupure — vérifie `RESOURCING-CADRAN-ARABE-2026-08-09.md` s'il existe.
5. **Débloquer ou abandonner les 5 fiches cadran arabe bloquées** : leur photo fournisseur porte une marque au cadran. Il faut d'autres photos fournisseur, ou renoncer.
6. **Produire les visuels maison des fiches restantes.** Sans eux, les 94 brouillons ne peuvent pas être activés. Priorité : cadrans stériles couleur (non entamés), puis le reste des pilote 1-12.
7. **Compléter les galeries des 96 fiches actives** : le brief `2026-08-08-consignes-codex-visuels.md` chiffre ~319 visuels (74 de galerie + 245 de variantes, tous coloris conservés sur décision de Hakim du 08/08). ~90 produits à ce jour.

### P2 — avant lancement
8. Installer la **mesure d'achat** — voir `2026-08-08-tracking-et-consentement.md`, 10 étapes au clic près. Voie retenue : app **Google & YouTube** (sur le plan Basic, le code de thème ne peut pas voir l'achat). ⚠️ **Ne pas laisser l'app créer le Merchant Center avant que le CSS soit arrêté.**
9. Reprendre les **P0/P1 restants de `2026-08-08-audit-gmc-final.md`**, puis seulement ensuite ouvrir le compte.

---

## 5 bis. Les prochaines étapes, dans l'ordre d'exécution

Chaque étape indique **ce qu'on attend en sortie**. Ne passe pas à la suivante sans avoir produit cette sortie — et pousse sur `main` à chaque fin d'étape.

### Étape 1 — Reprendre la file de visuels en cours (½ journée)
1. Remets `cadran-sterile-lumineux-28-5` de `en-cours/` vers `inbox/`.
2. Contrôle les 3 visuels de `cadran-sterile-couronne-3h-28-5/` (QA non faite).
3. Déroule les 4 ordres validés en attente, puis écris les ordres manquants pour finir les **cadrans stériles couleur** (15 fiches, non entamés) et le reste des **pilote 1-12**.
4. Rattache au fil de l'eau (§4), en fin de galerie, `alt` FR.

**Sortie attendue** : les collections « cadran stérile » et « cadran pilote » entièrement habillées de visuels maison, `2026-08-09-fournee-visuels-nouveaux.md` à jour, `en-cours/` vide.

### Étape 2 — Re-sourcer la collection cadran arabe (1 journée)
C'est **le chantier le plus rentable** : 15 500 recherches/mois pour 5 produits réels seulement.

1. Ouvre les fiches AliExpress **dans le Chrome de Hakim** (seul chemin vers la preuve A).
2. Cible **4 à 8 cadrans supplémentaires** à écriture arabe **véritable** — compatibles NH35/NH36, cotes 28,5 / 29 / 33,5 mm.
3. Deux vérifications qui ont fait échouer le lot précédent, à faire **sur l'image, pas sur le titre** :
   - les chiffres sont bien des **chiffres arabes orientaux** (٣ ٦ ٩ ١٢) — un titre fournisseur « arabic » ne prouve rien ;
   - le cadran ne porte **aucune marque ni formule déposée** (zoom obligatoire).
4. Relève sur fiche ouverte : item_id complet, ventes réelles, note, prix, variantes, livraison France. **Moins de 10 ventes = refus.**
5. Télécharge les photos fournisseur dans `sources-fournisseur-2026-08/<handle-propose>/`.

**Sortie attendue** : `2026-08-09-resourcing-cadran-arabe.md` (candidats classe A + refusés motivés) et une file `2026-08-09-file-dsers-cadran-arabe.md` prête à importer. **Aucun achat, aucun import à ce stade.**

### Étape 3 — Statuer sur les 5 fiches arabes bloquées (½ journée)
Leur photo fournisseur porte une marque au cadran : ni composition ni retouche ne les sauvent proprement. Pour chacune, **cherche d'autres photos du même produit** (autres vendeurs du même article, galerie complète de la fiche). Si rien d'exploitable : **abandonner le produit** et le sortir de la collection.

**Sortie attendue** : décision écrite fiche par fiche, collection cadran arabe nettoyée.

### Étape 4 — Importer le nouveau lot arabe (½ journée)
1. Push DSers depuis la file de l'étape 2, **tout en DRAFT**.
2. ⚠️ La case « Set product status as Draft » **se réarme à chaque lot** : relis le DOM avant chaque validation.
3. Vérifie côté Shopify que les fiches arrivent bien en brouillon et relève leurs id + handle réels.
4. Rédige titres, descriptions, meta et rattachement — **à partir des données réelles relevées**, jamais d'une traduction du titre AliExpress.
5. Produis leurs visuels maison (étape 1 en modèle).

**Sortie attendue** : collection cadran arabe à **10-12 produits réels**, habillés, prêts à activer.

### Étape 5 — Nettoyer le catalogue avant activation (½ journée)
1. **Dédoublonner les 3 paires** de fiches pointant le même produit AliExpress (liste dans `2026-08-09-coherence-fiches.md`).
2. Appliquer la décision de Hakim sur `cadran-lumineux-28-5-nh35` (verbatim Rolex).
3. Corriger la collection active `montre-cadran-a-chiffres` (« nous ne proposons pas de chiffres orientaux »).
4. Affecter aux variantes les **6 nuanciers du bracelet gaufré**.
5. Reprendre les **doutes non tranchés** consignés dans `2026-08-09-coherence-fiches.md` (lume des index sur 2 cadrans squelette, `cadran-transparent-lume-28-5` que le fournisseur ne vend pas à l'unité).

**Sortie attendue** : zéro doublon, zéro fiche à risque de marque, doutes tous tranchés ou documentés.

### Étape 6 — Compléter les galeries des 96 fiches actives (chantier long)
Le brief `2026-08-08-consignes-codex-visuels.md` chiffre **~319 visuels** : 74 de galerie + 245 de variantes, **tous coloris conservés** (décision de Hakim du 08/08, ne propose pas de réduire). ~90 produits à ce jour. Compter 8-10 min par visuel en CLI, 2-3 min dans l'app.

**Sortie attendue** : plus aucune fiche active sous la cible maison (5 images par montre, 3 par accessoire).

### Étape 7 — Activation (sur accord de Hakim uniquement)
Ne rien activer avant que **tous** ces points soient vrais :
- les fiches concernées n'ont plus **aucune photo AliExpress brute** ;
- les 3 politiques ont été collées par Hakim et le médiateur renseigné ;
- la grille de prix a été arbitrée et appliquée ;
- la **mesure d'achat** est installée et testée (§P2) ;
- les P0/P1 restants de `2026-08-08-audit-gmc-final.md` sont soldés.

Puis, dans l'ordre : activer les produits → publier les collections sur le canal Online Store → retirer le mot de passe boutique → ouvrir le compte CSS/Merchant Center. **L'activation et la publication reviennent à Hakim.**

---

## 6. Ce qui appartient à Hakim — ne pas faire à sa place

- **Coller les 3 textes de politiques** préparés dans `boutique-seiko-mod/backups/backup-retours-2026-08-08/a-appliquer-par-hakim/` : le connecteur n'a pas la permission `write_legal_policies`, donc les CGV et la politique de remboursement servies portent **encore la clause interdite**.
- **Adhérer à un médiateur de la consommation** (obligation légale FR, toujours `[À COMPLÉTER]` en CGV art. 17).
- **Arbitrer la grille de prix** : plusieurs coûts réels sont inférieurs aux estimations (9,19 € contre 18,49 € sur un exemple). Deux stratégies chiffrées dans `2026-08-09-textes-et-collections.md`, aucun prix n'a été écrit.
- **Basculer l'e-mail boutique** de `contact.noirmont@gmail.com` vers `contact@maisonnoirmont.fr` (déjà utilisée partout ailleurs) — ⚠️ vérifier d'abord que la boîte `.fr` reçoit, sinon les e-mails de commande partent dans le vide.
- **Vérifier le mapping DSers** des 2 fiches « Voyageur Or ».
- Toute installation d'app, création de compte, publication de thème ou activation de produit.

---

## 7. Où trouver le détail

| Sujet | Fichier |
|---|---|
| Audit de conformité complet (80+ points) | `2026-08-08-audit-gmc-final.md` |
| Les 94 produits importés, données réelles | `2026-08-09-push-dsers.md` |
| Collections, textes, grille de prix | `2026-08-09-textes-et-collections.md` |
| Les 16 écarts corrigés, comptes par collection | `2026-08-09-coherence-fiches.md` |
| Brief visuels complet (~319, règles, slots) | `2026-08-08-consignes-codex-visuels.md` |
| Production de visuels en cours | `2026-08-09-fournee-visuels-nouveaux.md` |
| Rattachements faits | `2026-08-09-rattachement-visuels.md` |
| Tracking et consentement, 10 étapes | `2026-08-08-tracking-et-consentement.md` |
| Registre de sourcing | `2026-08-09-sourcing-collections.md` |
| État général et thèmes | `2026-08-08-reprise-session.md` |

**Deux travaux étaient en cours à la coupure** — production de visuels (cadrans stériles) et re-sourcing cadran arabe. Vérifie l'état réel des fichiers et de `ordres/pour-codex/` avant de relancer : ne double aucun travail déjà fait.

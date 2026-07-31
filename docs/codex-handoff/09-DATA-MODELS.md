# 09 — Modèles de données du pipeline

> Dossier de passation Codex — généré le 2026-07-30.
> **Étiquettes de source** : **[FAIT — repo:chemin]** · **[MÉMOIRE]** · **[HYPOTHÈSE]** · **[INFO HAKIM — brief de passation]** · **[MANQUANT]**.
> Principe : chaque modèle part des **structures réellement présentes dans le repo** (registre, rapports, JSON de travail, métachamps). Quand un champ est une proposition de normalisation sans équivalent existant, il est marqué **(nouveau)** et la migration depuis l'existant est décrite.
> Tous les exemples JSON sont valides. Les montants et IDs sont réels sauf mention « anonymisé ».

## Conventions transverses (issues des leçons du projet)

1. **Identité produit inter-outils = `handle` + `sku_chaine`, jamais un ID de variante/média.** Leçon écrite noir sur blanc : un manifeste indexé sur des identifiants de variante « devenus périmés avant même d'être lus » a forcé la reprise à la main de 118 correspondances par SKU **[FAIT — repo:boutique-pipeline/boutique-seiko-mod/PROMPT-CODEX-galeries.md §Nommage et manifeste]**. Les manifestes actuels sont indexés `["handle","sku"]` **[FAIT — repo:boutique-pipeline/scratchpad/noirmont-galeries/manifest.json]**.
2. **`item_id` AliExpress complet** (jamais tronqué/reconstruit ; préfixes réels jusqu'à `1005012…`) **[FAIT — repo:boutique-seiko-mod/sourcing-accessoires-v3-2026-07-25.md]**.
3. **Toute donnée est datée** (`releve_le`/`date`) et **sourcée** (lien rapport) — règle du registre : « le registre pointe vers les rapports ; il ne remplace jamais leur détail » **[FAIT — repo:boutique-pipeline/registre-candidats.md]**.
4. **Données vendeur = annoncées, pas prouvées**, tant qu'aucune commande test ne les a contrôlées **[FAIT — repo:reports/phase4-sourcing-fontaine-gravite-2026-07-20.md]**.
5. Fichiers locaux = **source de vérité** ; Notion = tableau de bord répliqué **[MÉMOIRE — notion-pipeline-boutiques.md]**.

---

## 1. `niche` (famille / cluster de marché)

Existant : `families.json` du workspace Codex (champs `id`, `order`, `name`, `seeds`, `status` avec enum `PENDING|IN_PROGRESS|EXHAUSTED|BLOCKED`, `result_summary`, `report`) **[FAIT — repo:boutique-pipeline/codex-chasse-clusters/families.json]** + tableaux « Familles balayées » du registre **[FAIT — repo:registre-candidats.md]**.

```json
{
  "id": "f07-traitement-de-l-eau",
  "nom": "Traitement de l'eau",
  "seeds": ["adoucisseur", "filtre eau", "osmoseur"],
  "statut": "EXHAUSTED",
  "clusters": [
    {
      "cluster_id": "f07-c01-fontaine-filtrante",
      "libelle": "fontaine filtrante + filtre gravité",
      "volume_mensuel_fr": { "min": 13000, "max": 15500, "nettoye_serp": true },
      "issue": "CANDIDAT_RETENU"
    },
    {
      "cluster_id": "f07-c02-douche-filtrante",
      "libelle": "douche filtrante anti-calcaire",
      "volume_mensuel_fr": { "min": 34700, "max": null, "nettoye_serp": false },
      "issue": "VIVIER"
    }
  ],
  "issue_famille": "1 candidat, 1 vivier, poches non instruites",
  "rapports": ["reports/chasse-clusters-traitement-de-l-eau-2026-07-20.md"],
  "date": "2026-07-20"
}
```

**(nouveau)** : la fusion en un seul objet `niche` des deux représentations (families.json Codex, tableaux Markdown du registre) est une normalisation. Migration : parser les tableaux « Familles balayées sans candidat » et « Viviers » du registre (colonnes réelles : Famille, Date, Clusters mesurés, Issue, Rapports) + reprendre `families.json` tel quel.

## 2. `mot_cle`

Existant : mesures SEMrush des rapports (volume, KD, CPC, hiérarchie parent/segment) **[FAIT — repo:boutique-seiko-mod/REPRISE-SESSION.md §Stratégie ; marche-complet-semrush.md ; mots-cles-semrush.md]**.

```json
{
  "mot_cle": "seiko mod",
  "db": "fr",
  "volume_mensuel": 38690,
  "volume_etendu": 51000,
  "kd": 10,
  "cpc_eur": 0.22,
  "parent": null,
  "notes_serp": "enchère quasi vide : seul montreapapy.fr annonce (212 $/mois)",
  "mesure": { "outil": "SEMrush", "compte": "payant", "date": "2026-07-24", "mot_cle_temoin_verifie": true },
  "source": "boutique-seiko-mod/marche-complet-semrush.md"
}
```

`mot_cle_temoin_verifie` **(nouveau)** encode la règle « SEMrush gratuit rend “0” sans erreur passé le quota — mot-clé témoin obligatoire » **[FAIT — repo:REPRISE-SESSION.md §Pièges]**.

## 3. `concurrent`

Existant : colonnes concurrence du registre (« institutionnels / dropship », prix, nombre d'ads) **[FAIT — repo:registre-candidats.md]** + dossiers d'analyse dédiés (`analyse-concurrent-montreapapy-2026-07-24.md`, `catalogue-v2-analyse-concurrents-2026-07-25.md`) **[FAIT — repo:boutique-seiko-mod/]**.

```json
{
  "domaine": "goteia.fr",
  "type": "specialiste_dtc",
  "marche": "seiko mod FR",
  "positionnement_prix_eur": { "configure": 349, "fixe_min": 249, "fixe_max": 259 },
  "preuves": [
    "66 % du trafic vient d'un seul article premier sur 'seiko modifications' (6 600/mois)",
    "0,9 % du trafic vient de la personnalisation"
  ],
  "ads": { "google": true, "meta": false, "budget_estime_usd_mois": null },
  "avis_publics": null,
  "source": "boutique-seiko-mod/REPRISE-SESSION.md + marche-complet-semrush.md",
  "date": "2026-07-27"
}
```

## 4. `produit_candidat` (ligne du registre central)

Existant : le tableau des candidats du registre — colonnes réelles : `#`, Candidat, Cluster et volume pertinent, Prix marché, Concurrents (institutionnels / dropship), Fournisseur AliExpress, Confiance, Réserves, Date — plus les **niveaux de validation 1–4** (1 = marché, 2 = fiche AliExpress, 3 = commande test, 4 = GO lancement, « aucun raccourci ») et l'anti-doublon par synonymes **[FAIT — repo:registre-candidats.md]**.

```json
{
  "numero": 1,
  "candidat": "Fontaine à eau filtrante à gravité, grande capacité",
  "synonymes": ["fontaine filtrante", "filtre gravité", "purificateur gravité"],
  "cluster": { "libelle": "fontaine filtrante + filtre gravité", "volume_mensuel_fr": { "min": 13000, "max": 15500, "nettoye_serp": true } },
  "prix_marche_eur": { "coeur_min": 150, "coeur_max": 420, "ancres": "VEVOR 70–106 € en ancre basse" },
  "concurrents": "Spécialistes DTC dominants en organique (7+) ; dropship non isolé ; GSB = bornes de prix",
  "fournisseur": { "item_id": "1005008291010462", "cout_rendu_eur": 86.99, "entrepot": "France", "delai_jours": [2, 8] },
  "confiance_fournisseur": "A",
  "niveau_validation": 2,
  "verdict": "RETENU",
  "reserves": [
    "logo VEVOR possible sur la cuve livrée — contrôle prioritaire commande test",
    "conformité contact alimentaire non documentée — aucun claim santé",
    "statut Berkey non instruit juridiquement"
  ],
  "rapports": ["reports/phase4-sourcing-fontaine-gravite-2026-07-20.md"],
  "date": "2026-07-20"
}
```

Enum `verdict` observée dans le registre : `RETENU` · `A_APPROFONDIR` · `CAS_LIMITE` · `STOP_MARCHE` · `REJET_PHASE2` · `REJET_HAKIM` · `VIVIER` · `POCHE_NON_INSTRUITE` **[FAIT — repo:registre-candidats.md, sections dédiées]**.

## 5. `fournisseur` (vendeur AliExpress)

Existant : blocs vendeur des rapports de phase 4 **[FAIT — repo:reports/phase4-sourcing-fontaine-gravite-2026-07-20.md ; dsers-mapping-lot2.md]**.

```json
{
  "nom": "SucceBuy Appliance Global Store",
  "plateforme": "aliexpress",
  "pct_avis_positifs": 95.9,
  "abonnes": 46000,
  "anciennete": null,
  "expedie_depuis": ["France"],
  "facture_ht_tva_intracom": null,
  "fiches_connues": ["1005008291010462", "1005010675449353"],
  "notes": "incohérence marque VEVOR/SucceBuy relevée titre vs Brand Name — probable même usine",
  "date": "2026-07-20"
}
```

`facture_ht_tva_intracom` reflète le réflexe fiscal SASU (« vérifier que chaque fournisseur fournit une facture HT/autoliquidation avec n° de TVA intracom ») **[FAIT — repo:CONTEXTE-MEMOIRE-pour-Codex.md §1]** — jamais renseigné à ce jour dans un livrable, d'où `null`.

## 6. `fiche_aliexpress`

Existant : structure constante des relevés de sourcing (voir doc 08 §1.2 pour la recette d'extraction) **[FAIT — repo:reports/phase4-* ; sourcing-accessoires-v3]**.

```json
{
  "item_id": "1005008291010462",
  "url": "https://fr.aliexpress.com/item/1005008291010462.html",
  "titre": "VEVOR Système de Filtration d'Eau par Gravité 8,5 L Inox 304 ...",
  "vendeur": "SucceBuy Appliance Global Store",
  "variantes": [
    { "attributs": { "type": "type 1" }, "prix_eur": 86.99, "stock_affiche": 15 },
    { "attributs": { "type": "type 2" }, "prix_eur": 92.39, "stock_affiche": 13 }
  ],
  "livraison_france": { "gratuite": true, "entrepot": "France", "fenetre": "2026-07-22/2026-07-28", "delai_jours": [2, 8] },
  "preuve_sociale": { "note": 4.9, "nb_avis": 32, "nb_vendus": 127 },
  "protections": ["retour gratuit 90 j", "remboursement si non livré après 20 j"],
  "caracteristiques_annoncees": { "annonce_par_vendeur": true, "detail": "inox 304, 8,5 L, filtres céramique/charbon" },
  "signaux_risque": ["variantes renommées en cours de vie de fiche (BLANC/Bleu → type 1/2)"],
  "releve_le": "2026-07-20",
  "statut_fiche": "RETENUE_COMMANDE_TEST"
}
```

## 7. `variante` (Shopify ↔ DSers ↔ AliExpress)

**Le pivot du système.** Existant : SKU Shopify porteurs de la **chaîne d'attributs AliExpress**, format `<attr_id>:<valeur_id>#<label>` joints par `;` **[FAIT — repo:import-accessoires-lot4.md ; dsers-mapping-lot2.md §Structure des SKU par famille]** ; libellés d'options composées côté Shopify **[FAIT — repo:shopify-target-products-2026-07-25.json]** ; correspondance Color/Size côté DSers **[FAIT — repo:dsers-mapping-decoupage-2026-07-25.md]**.

```json
{
  "handle": "trente-neuf-bleu-classique-cannelee",
  "sku_chaine": "14:173#blue no logo;5:361386#NH35-36mm(glassback)",
  "option_shopify": { "nom": "Mouvement & fond", "valeur": "NH35 · 36 mm · fond verre" },
  "attributs_aliexpress": { "14_Color": "blue no logo", "5_Size": "NH35-36mm(glassback)" },
  "mapping_dsers": { "mode": "mapping_basique", "color": "blue no logo", "size": "NH35-36mm(glassback)", "confirme": true },
  "prix_eur": 358.0,
  "prix_barre_eur": 466.0,
  "cout_fournisseur_eur": null,
  "inventory_policy": "DENY"
}
```

Notes ancrées :
- Le `sku_chaine` de cet exemple est **reconstitué dans son format** (les attributs `14:`=Color, `5:`=Size et les labels sont réels ; les ID numériques exacts de cette variante précise n'ont pas été recopiés dans les livrables — **anonymisé/plausible**). Exemples de SKU intégralement réels : `14:200000914#M14`, `14:865#13pc Kits`, `200000049:350853#steel-no logo;200000051:100016950`, `14:10#10X-with circle` **[FAIT — repo:scratchpad/noirmont-galeries/worklist.json ; import-accessoires-lot4.md]**.
- Familles à 3 attributs vues : `14:<id>#<n>` + `200007763:201336100` (Ships From `China Mainland`) **[FAIT — dsers-mapping-lot2.md]**.
- `inventory_policy: CONTINUE` existe (aviateur bronze publié à stock 0, vente en rupture) **[FAIT — publication-grappes.md]** ; `DENY` + stock 0 = variantes rendues invendables (12 GMT siglées) **[FAIT — BILAN-2026-07-25.md]**.
- **Le SKU ne prouve pas l'identité visuelle d'une image** après découpage de coloris **[FAIT — REPRISE-SESSION.md §Pièges]**.

**⚠️ `noirmont-coloris-variant-map.json` : [MANQUANT].** Ce fichier, cité dans le brief de passation, **n'existe nulle part dans le repo** (recherche insensible à la casse sur tout `/Users/Hakim/Documents/Boutiques drop`, 2026-07-30). Les artefacts réels les plus proches : `backup-variantes-avant-decoupage.json` (sauvegarde pré-découpage, utilisée comme recoupement de la table SKU **[FAIT — dsers-mapping-lot2.md]**), les tableaux de mapping des deux livrables DSers, et le trio `worklist.json`/`sources.json`/`manifest.json` des galeries. Si une « carte des coloris » doit exister en JSON, c'est un **(nouveau)** à construire depuis ces sources.

## 8. `score_produit`

Existant : le pipeline ne produit **pas de score numérique** — il produit des **verdicts qualitatifs à critères éliminatoires** (seuil 10 000 recherches/mois nettoyées, tranche 150–400 € TTC, §3 persona particulier, §4 verrous concurrentiels) **[FAIT — repo:PRODUCT-RESEARCH-CRITERIA.md ; registre-candidats.md]**. Le modèle ci-dessous est une **normalisation (nouveau)** qui encode ces verdicts sans inventer de pondération.

```json
{
  "candidat": "surpresseur domestique",
  "verdict_marche": "GO",
  "criteres": {
    "volume_seuil_10000": { "ok": true, "valeur": [19000, 26600], "nettoye_serp": true },
    "tranche_prix_150_400": { "ok": true, "coeur_constate_eur": [130, 450] },
    "persona_particulier_explicable": { "ok": true },
    "verrous_concurrentiels_s4": { "ok": true, "detail": "GSB via listings sans verrou ; 6 spécialistes organiques" }
  },
  "reserves_majeures": 4,
  "niveau_validation": 2,
  "controle_critique_candidat": "RETENU",
  "rapport": "reports/phase4-sourcing-surpresseur-2026-07-20.md",
  "date": "2026-07-20"
}
```

Migration : chaque ligne du registre se transpose (verdict, réserves comptées, niveau). Ne **pas** convertir en note /100 : la sémantique existante est binaire par critère, avec verdicts `GO | A_APPROFONDIR | STOP` en phase 3 et `RETENU | NON_RETENU` au contrôle `critique-candidat` **[FAIT — registre-candidats.md]**.

## 9. `score_fournisseur`

Existant : la **grille de confiance A/B/C**, décision de Hakim du 20/07/2026 — « la case fournisseur prouve que le produit est sourçable, pas que le vendeur est bon » **[FAIT — repo:registre-candidats.md]**.

```json
{
  "item_id": "1005012663097367",
  "confiance": "B",
  "grille": {
    "avis_solides": true,
    "expedition_france_ue": false
  },
  "definition": "A = avis solides ET expédition FR/UE ; B = une seule des deux forces ; C = ni l'un ni l'autre mais fiche vérifiée et correspondante — à valider par commande test",
  "statut": "FICHE_RETENUE_COMMANDE_TEST",
  "date": "2026-07-20"
}
```

## 10. `offre` (pricing d'une fiche boutique)

Existant : règle appliquée aux 13 accessoires — « prix ≈ coût rendu × 3 à 4, arrondi au ,90 ; prix barré = prix × 1,3 arrondi au ,90 supérieur », avec **tiérisation** quand la matrice de coûts par variante l'impose (plancher ×2,5) **[FAIT — repo:import-accessoires-lot4.md §Règle de prix]** ; échelle de prix par mouvement sur les montres (Seiko +39 €, PT5000 +89 €, fond verre +29 €) **[FAIT — repo:BILAN-2026-07-25.md]**.

```json
{
  "handle": "bracelet-jubile-embouts-courbes",
  "regle": "cout_rendu x3-4 arrondi ,90 ; barre = prix x1,3 arrondi ,90 sup ; plancher x2,5 par variante",
  "paliers": [
    { "segment": "acier", "cout_rendu_eur": 6.30, "prix_eur": 29.90, "prix_barre_eur": 38.90 },
    { "segment": "acier-or", "cout_rendu_eur": 8.70, "prix_eur": 34.90, "prix_barre_eur": 45.90 },
    { "segment": "or", "cout_rendu_eur": 11.10, "prix_eur": 39.90, "prix_barre_eur": 51.90 }
  ],
  "conformite": {
    "prix_reference_30j_verifie": false,
    "note": "règle française du prix de référence à vérifier avant toute remise affichée — badge promo retiré"
  }
}
```

`conformite` ancré dans **[FAIT — repo:REPRISE-SESSION.md §Ce qui attend Hakim, pt 7]**. Les coûts intermédiaires par segment autres que 6,30/11,10 € sont **anonymisés/plausibles** (le livrable donne la fourchette 6,30 → 11,10 €).

## 11. `marque`

Existant : `brand-tokens-noirmont.json` (v2.0 — positioning, tone, colors + color-rules, fonts display/ui/data, type-scale, logo avec generation-brief, ui) **[FAIT — repo:boutique-seiko-mod/brand-tokens-noirmont.json]**, validé par le schéma `boutique-pipeline/schema/brand-tokens.schema.json` **[FAIT]**. ⚠️ La **charte vivante a divergé du fichier** : direction « A+B » avec accent cyan `#22D3EE`, vert-jura et laiton **purgés à la source** **[FAIT — repo:REPRISE-SESSION.md §Charte]** — le JSON v2.0 porte encore vert-jura/laiton. Migration : régénérer les tokens depuis la charte du moment, le fichier n'est pas auto-porteur.

```json
{
  "brand": "NOIRMONT",
  "version": "2.0 — 2026-07-25",
  "positioning": "Votre signature au poignet — aspiration en front ; réassurance en coulisse",
  "tone": "vouvoiement, aspiration et allure d'abord, factuel en second niveau",
  "colors": { "noir-encre": "#0B0B0C", "craie": "#FAFAF7", "pierre": "#E7E4DE", "graphite": "#55524C" },
  "color_rules_vivantes": {
    "accent": "#22D3EE — instrument seulement (puces specs, focus), jamais bouton ni badge, contraste 1,72:1 : ne porte jamais d'information",
    "etoiles_avis": "#05b67a (décision Hakim)",
    "purges": ["#1E3A2F", "#A98E5F"]
  },
  "fonts": { "display": "Oswald (charte vivante) / Bodoni Moda (tokens v2)", "ui": "Inter" },
  "logo": { "wordmark": "NOIRMONT", "marque_secondaire": "assets/noirmont-marque.svg (anneau, favicon)" }
}
```

## 12. `boutique`

Existant : en-têtes de tous les livrables Noirmont + REPRISE **[FAIT — repo:REPRISE-SESSION.md ; publication-grappes.md]**.

```json
{
  "nom": "Maison Noirmont",
  "myshopify": "v42pzp-h4.myshopify.com",
  "domaine": "maisonnoirmont.fr",
  "etat": { "sous_mot_de_passe": true, "commandes": 0, "clients": 0 },
  "themes": [
    { "nom": "Helio", "id": "204246548818", "role": "MAIN publié — ne jamais y écrire" },
    { "nom": "Maison Noirmont", "id": "204248088914", "role": "UNPUBLISHED — thème de travail, à republier" }
  ],
  "canaux_publication": [
    { "nom": "Boutique en ligne", "id": "358599295314" },
    { "nom": "Point de vente", "id": "358599328082" },
    { "nom": "Shop", "id": "358599360850" }
  ],
  "dsers": { "compte": "contact.noirmont", "produits": 103, "unmapped": 0 },
  "catalogue": { "fiches_actives": 92, "montres": 53, "accessoires": 38, "carte_cadeau": 1, "meres_brouillon": 7 },
  "livraison": { "zone": "France uniquement", "promesse": "J+14/J+21", "dates_estimees_shopify": "Désactivé" },
  "suivi_notion": { "hub": "Pipeline Boutiques Drop", "base_boutiques": "3a26f4af523d448a907fce7b45b42bcc" }
}
```

(Compteur DSers 103 = état du 29/07 **[FAIT — publication-grappes.md]** ; REPRISE du 27/07 disait 98 — prendre le plus récent.)

## 13. `fiche_produit_shopify`

Existant : `shopify-target-products-2026-07-25.json` (nodes avec `id` GID, `title`, `handle`, `options[].optionValues[]`) **[FAIT]**, métachamps réels `custom.*` **[FAIT — repo:metachamps-montres.md]**, statuts et canaux **[FAIT — publication-grappes.md ; import-accessoires-lot4.md]**.

```json
{
  "gid": "gid://shopify/Product/10977444528466",
  "handle": "contre-la-montre-chronographe-panda",
  "titre": "Contre-la-montre — Chronographe panda",
  "statut": "DRAFT",
  "canaux_publies": [],
  "vendor": "Maison Noirmont",
  "tags": ["chronos"],
  "collections": ["chronos", "montres"],
  "template_suffix": null,
  "options": [
    { "nom": "Cadran", "valeurs": ["Argent · caoutchouc noir", "Panda ivoire · aiguille rouge", "Bleu glacier"] }
  ],
  "metachamps": {
    "custom.famille": ["Chronos"],
    "custom.calibre": ["VK63"],
    "custom.diametre": ["39 mm"],
    "custom.couleur_cadran": ["Blanc"]
  },
  "seo": { "title_tag": "Chronographe 39 mm ...", "description": "..." },
  "variantes": ["<voir modèle variante — indexées par sku_chaine>"]
}
```

Contraintes ancrées : les 4 métachamps sont des `list.single_line_text_field` en `PUBLIC_READ` ; normalisations fermées (diamètre `"NN mm"`, 6 calibres canoniques + VK63, palette couleurs fermée, familles canoniques) ; **valeur non établie = champ vide, jamais deviné** **[FAIT — metachamps-montres.md]**. Piège statut : `ACTIVE` sans publication canal = invisible (`resourcePublications` vide) → `publishablePublish` obligatoire **[MÉMOIRE — shopify-canal-et-visuels-ia.md]**, vérifié par `resourcePublicationsV2` **[FAIT — publication-grappes.md]**.

## 14. `media`

Existant : chaîne de branchement des galeries (staged upload → `productCreateMedia` → `productReorderMedia`), alt text normé, slots, contrôle 740 px **[FAIT — repo:branchement-galeries-codex.md]** + entrées du manifeste **[FAIT — scratchpad/noirmont-galeries/manifest.json]**.

```json
{
  "handle": "contre-la-montre-argent-chronographe",
  "sku": "14:200000914#M14",
  "slot": "situation",
  "fichier": "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/scratchpad/noirmont-galeries/generated/contre-la-montre-argent-chronographe-situation.jpg",
  "format": { "px": 2048, "type": "JPEG", "qualite": 90 },
  "alt": "Contre-la-montre — Chronographe argent — en situation — Maison Noirmont",
  "position_cible": 2,
  "modele_utilise": "GPT Image 2 natif",
  "nombre_regenerations": 0,
  "controles": {
    "sterilite_740px_zoom": true,
    "zone_5h_7h_x5": true,
    "statut_shopify": "READY",
    "media_user_errors": []
  }
}
```

Les champs `handle/sku/slot/fichier/modele/nombre_regenerations` sont **exactement** ceux du manifeste réel ; `controles` **(nouveau)** encode les règles de QA écrites (planches ≥ 740 px/vignette, recadrage 5h–7h ×5, « atténué compte comme présent ») **[FAIT — branchement-galeries-codex.md §Règle de méthode]**. Slots canoniques : montres `face·situation·macro·poignet` (4), accessoires `face·situation·macro` (3) **[FAIT — PROMPT-CODEX-galeries.md]**. Requêtes média **plafonnées à 30 — paginer** **[FAIT — REPRISE-SESSION.md]**.

## 15. `tache_agent`

Existant : tickets du campement type Notion (19 tickets 00→17, statuts `À faire / En cours / Bloqué Hakim / Fait`, chaque ticket = brief autoportant avec procédure + garde-fous + critères de fin, dépendances notées) **[MÉMOIRE — campement-type-lancement-boutique.md]** + prompts autoportants type `PROMPT-CODEX-galeries.md` **[FAIT]**.

```json
{
  "id": "05-import-dsers",
  "boutique": "maison-noirmont",
  "titre": "Import DSers des fiches accessoires",
  "statut": "Fait",
  "depend_de": ["03-sourcing-aliexpress"],
  "brief": {
    "perimetre": "import Liste d'import URL par URL, push Draft, publication décochée",
    "interdits": ["saisir des identifiants", "commander", "cliquer un × fournisseur"],
    "criteres_de_fin": ["compteurs DSers conformes à l'arithmétique attendue", "SKU chaîne d'attributs présents"]
  },
  "entrees": ["scratchpad/noirmont-fiches-accessoires.md"],
  "livrable": "boutique-seiko-mod/import-accessoires-lot4.md",
  "validation_humaine_requise": false
}
```

## 16. `execution` (run d'une boucle/mission)

Existant : `run-state.json` du workspace Codex — champs réels : `schema_version`, `workspace`, `status`, `run_id`, `created_at/updated_at`, `target_count`, `retained_count`, `retained_count_rule`, `mode`, `previous_run{}`, `current{family_id, seed, cluster_id, candidate_id, stage, attempt, last_valid_report}`, `next_action`, listes d'anti-doublon historique **[FAIT — repo:codex-chasse-clusters/run-state.json]**.

```json
{
  "schema_version": 1,
  "workspace": "codex-chasse-clusters",
  "run_id": "20260720-200609",
  "status": "COMPLETE_RADAR_DELIVERED",
  "created_at": "2026-07-20T20:06:09+02:00",
  "updated_at": "2026-07-20T21:08:21+02:00",
  "target_count": 30,
  "retained_count": 8,
  "current": {
    "family_id": "brandsearch-eu",
    "stage": "completed",
    "attempt": 1,
    "last_valid_report": "reports/validation-multimarche-brandsearch-20260720-200609-a1.md"
  },
  "previous_run": { "run_id": "20260720-124517", "status": "COMPLETE_FAMILIES_EXHAUSTED", "retained_count": 17 },
  "next_action": "Source the 8 green candidates manually on AliExpress ..."
}
```

## 17. `erreur`

Existant : taxonomie fail-closed des specs — « SEMrush déconnecté, CAPTCHA AliExpress, page qui ne charge pas, fichier canonique introuvable, livrable non conforme » = **arrêt déclaré, jamais de données inventées** **[FAIT — repo:plans/2026-07-20-boucle-chasse-clusters.md §Blocage technique ; specs/2026-07-17-…]** + messages réels (`Browser Use rejected this action due to browser security policy`) **[FAIT — codex-chasse-clusters/reports/validation-…-a1.md]**.

```json
{
  "type": "BLOCAGE_TECHNIQUE",
  "sous_type": "captcha | session_expiree | quota_silencieux | page_vide | iframe_cross_origin | fichier_introuvable | rejet_silencieux_api | politique_navigateur",
  "outil": "browser_use",
  "message_brut": "Browser Use rejected this action due to browser security policy",
  "contexte": { "url": "https://fr.aliexpress.com/w/wholesale-...", "tache": "search_aliexpress_products", "run_id": "20260720-200609" },
  "comportement": "ARRET_DECLARE",
  "donnees_inventees": false,
  "consequence": "candidats notés RETENU_MARCHE_A_SOURCER, requêtes manuelles préparées",
  "date": "2026-07-20"
}
```

`rejet_silencieux_api` couvre les cas Shopify documentés : `upsertedThemeFiles: []` sans `userErrors` (écriture asynchrone), champ CSS/nom de schéma > 25 caractères, caractère invisible dans une chaîne « introuvable » **[FAIT — REPRISE-SESSION.md §Pièges]**. `quota_silencieux` = SEMrush « 0 » **[FAIT — idem]**.

## 18. `validation_humaine`

Existant : portes du PLAYBOOK (PORTE 1 nom/palette, PORTE 2 arbo, PORTE 3 build) **[FAIT — repo:CONTEXTE-MEMOIRE-pour-Codex.md §2.2]**, statut « Bloqué Hakim » du campement **[MÉMOIRE — campement-type-lancement-boutique.md]**, et les décisions réservées récurrentes (commande test, publication de preuve sociale, republication thème, cinq gestes Search & Discovery, arbitrages de gamme) **[FAIT — registre-candidats.md ; REPRISE-SESSION.md ; metachamps-montres.md]**.

```json
{
  "id": "VAL-2026-07-24-seiko-commande-test",
  "type": "commande_test",
  "objet": "SUB stérile Tandorio 78,25 € rendu — passage niveau 2 → 3",
  "demandeur": "phase4-sourcing",
  "decideur": "Hakim",
  "statut": "EN_ATTENTE",
  "options": ["commander", "reporter", "abandonner"],
  "contexte": {
    "candidat": "montre custom Seiko mod",
    "rapport": "reports/phase4-sourcing-seiko-mod-2026-07-24.md",
    "reserves_majeures": ["marques déposées sur designs imités", "fiches hommage géobloquées = sourcing volatil"]
  },
  "regle": "aucun raccourci entre niveaux de validation ; le GO fournisseur exige une commande test reçue et contrôlée",
  "date_demande": "2026-07-24"
}
```

Types observés dans les livrables : `porte_playbook` · `commande_test` · `go_lancement` · `publication_theme` · `preuve_sociale` · `geste_interface_non_automatisable` · `arbitrage_gamme` · `saisie_identifiants` **[FAIT — sources citées]**. Le modèle d'objet unique est **(nouveau)** ; migration : ces validations vivent aujourd'hui en prose dans les sections « Ce qui attend Hakim » / « Décisions qui t'attendent » des livrables et dans les statuts Notion — les extraire à la création de chaque nouvelle demande, pas rétroactivement.

---

## Récapitulatif des écarts et manques

| Point | État |
|---|---|
| `noirmont-coloris-variant-map.json` | **[MANQUANT]** — cité dans le brief, absent du repo ; équivalents réels listés au §7 |
| Score numérique produit/fournisseur | N'existe pas dans le projet — verdicts qualitatifs et grille A/B/C uniquement ; toute pondération serait **(nouveau)** |
| API DSers | Aucune API publique utilisée ; `dsers-product-bff` observée en lecture passive seulement **[FAIT — dsers-mapping-lot2.md]** |
| Coûts fournisseur par variante | Visibles dans DSers (fourchettes affichées) mais non exportés en JSON — champ `cout_fournisseur_eur` à alimenter par Browser Use **(nouveau)** |
| Tokens de marque | `brand-tokens-noirmont.json` v2.0 **divergent de la charte vivante** — à régénérer avant tout usage (§11) |

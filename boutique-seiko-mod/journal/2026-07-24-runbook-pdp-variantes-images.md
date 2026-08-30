---
type: journal
boutique: seiko-mod
date: 2026-07-24
nature: intervention
leviers: [catalogue, creative]
titre: "NOIRMONT — Runbook PDP Tuftéo / variantes / images — 24/07/2026 (soir)"
---

# NOIRMONT — Runbook PDP Tuftéo / variantes / images — 24/07/2026 (soir)

> ⚠️ **Bloqué sur la reconnexion du connecteur Shopify** : un `switch-shop` vers Tuftéo a invalidé la connexion (le connecteur ne tient qu'une boutique à la fois). Hakim doit ré-autoriser la boutique **v42pzp-h4 (Maison Noirmont)** au prochain prompt du connecteur. Tout le reste est prêt en local.

## 1. Template produit v2 — miroir Tuftéo (PRÊT, à pousser)

Fichiers prêts dans le scratchpad (`theme-noirmont/`) :
- `new_product_v2.json` → `templates/product.json`
- `liquid/noirmont-4x.liquid` → `blocks/noirmont-4x.liquid`
- `liquid/noirmont-livraison.liquid` → `blocks/noirmont-livraison.liquid`
- `liquid/noirmont-confiance.liquid` → `blocks/noirmont-confiance.liquid`

Structure du main (miroir de la fiche osmoseur BV portée sur Tuftéo, cf. `boutique-tufting/shopify/structure-templates-log-2026-07-21.md`) :
1. **Badge d'avis** « 4,8/5 · avis (démo — à remplacer) » (bloc reviews-badge FullStack, lien #reviews) — placeholder à retoucher par Hakim
2. rating-stars (masqué à 0 avis) → titre h1 → prix
3. **« Ou 4 × XX € avec PayPal ou Klarna »** (bloc liquide, calcul auto sur la variante sélectionnée, seuil 30 €)
4. séparateur → variantes + ATC + checkout accéléré
5. **Barre « Livraison estimée entre le [date] et le [date] · LIVRAISON GRATUITE »** (bloc liquide, dates auto J+12 → J+21, pastille vert-jura — réglable dans l'éditeur)
6. **4 cartes de confiance** : livraison offerte et suivie / 14 jours satisfait ou remboursé / garantie 12 mois / carte contact SAV français (mailto contact.noirmont@gmail.com)
7. **Accordéons ×5** : Description ({{ closest.product.description }}, ouvert par défaut) / Livraison & retours (délais « généralement 2 à 3 semaines ») / Fabrication & contrôle / Garantie 12 mois / Contactez-nous
8. Icônes de paiement
Sous la flottaison : **marquee** (montage contrôlé ✦ verre saphir ✦ livraison offerte ✦ garantie 12 mois ✦ paiement 4x) → avis (démo étiquetés) → 2 sections USP avec visuels → aide + FAQ → recommandations.

Procédure de push (éprouvée) : stagedUploadsCreate PUT text/plain → themeFilesUpsert body {type: URL, value: resourceUrl NON signé} sur le thème brouillon 204248088914. Pousser les 3 blocs liquide AVANT le template (le template référence leurs types).
QA après push : vérifier le rendu du bloc reviews-badge (styles disponibles inconnus), l'accordéon Description (si le HTML sort échappé → remplacer par un bloc custom), les dates FR de la barre livraison, mobile.

## 2. Variantes — francisation compatible mapping DSers (à exécuter API revenue)

Méthode éprouvée Tuftéo (cf. `boutique-tufting/shopify/francisation-variantes-2026-07-22.md`) :
- **Ne JAMAIS toucher aux SKU** (ils portent la chaîne de mapping AliExpress → DSers mappe par variante/SKU, un renommage d'option ne casse rien — vérifié sur Tuftéo).
- Supprimer les options « Ships From » (garder un entrepôt par défaut : France/UE sinon unique dispo) — suppression de variantes = à lister d'abord.
- Renommer les options : Color → Couleur (ou Cadran/Boîtier selon contenu), Size → **Mouvement** quand les valeurs sont des mouvements (NH35/Miyota/PT5000), sinon Taille.
- Traduire les valeurs : « BRONZE CASE-NO LOGO » → « Boîtier bronze — cadran stérile », « NH35-STEEL BACK » → « NH35 — fond acier », « MIYOTA82-GLASS BACK » → « Miyota 8215 — fond verre », etc.
- Produits mono-variante → Title/Default Title.
- Contrôle final : re-query complète, aucun SKU/prix modifié.

⚠️ **Arbitrage Hakim requis** : plusieurs montres ont des valeurs « LOGO » / « NO LOGO ». Positionnement Noirmont = 100 % stérile. Options : (a) supprimer les variantes LOGO (recommandé, précédent Tuftéo : variantes trompeuses supprimées), (b) les garder traduites. Ne rien supprimer sans son GO.

Séquence : 1) query complète options/valeurs/variantes+SKU des 25 produits → tableau de renommage généré → 2) exécution `productOptionUpdate` en batch → 3) re-query de contrôle → 4) liste des suppressions proposées (LOGO, Ships From multi-valeurs) pour validation Hakim.

## 3. Images produit (agent en cours)

Agent en arrière-plan : génère ~35 images (2/montre + 1/accessoire) style charte (pierre, cadrans stériles), avec la boucle anti-faux-logos (vérification visuelle de chaque image + inpainting OpenCV). Sortie : `scratchpad/noirmont-product-images/` + `manifest.json` (productId → fichiers, verified). Budget max 60 crédits.

Une fois l'API revenue ET le manifeste validé :
1. stagedUploadsCreate + fileCreate n'est PAS le bon chemin pour les médias produit → utiliser `productCreateMedia` (originalSource = resourceUrl stagé) par produit.
2. Puis `productDeleteMedia` sur les anciens médias AliExpress (query `product.media` d'abord, garder l'ordre : nouvelles images en premier).
3. ⚠️ Les images générées sont des visuels DA génériques, pas des photos du produit fournisseur exact — Hakim valide le manifeste avant le push (surtout les accessoires).

## 4. Ordre d'exécution à la reconnexion
1. Push blocs liquide + product v2 (§1) → QA PDP.
2. Query variantes → renommages automatiques sûrs (§2) → rapport + arbitrages.
3. Validation manifeste images par Hakim → push médias + suppression AliExpress (§3).

---

## ✅ EXÉCUTÉ — 24/07 soir (après reconnexion Shopify)

### §1 Template PDP miroir Tuftéo : POUSSÉ et VÉRIFIÉ
- 3 blocs liquide créés dans le thème brouillon : `blocks/noirmont-4x.liquid` (piège découvert : nom de schéma > 25 caractères = rejet **silencieux** de themeFilesUpsert → « Paiement fractionné »), `blocks/noirmont-livraison.liquid` (mois français codés en dur — la locale boutique est EN, `%B` sortait « August »), `blocks/noirmont-confiance.liquid`.
- `templates/product.json` v2 appliqué. QA Chrome OK : badge 4,8/5 (démo) → titre → prix → « Ou 4 × 72,25 € avec PayPal ou Klarna » (calcul auto) → variantes FR → « Livraison estimée entre le 5 août et le 14 août · LIVRAISON GRATUITE » (J+12/J+21, réglable) → 4 cartes confiance (livraison/14 j/garantie 12 mois/contact) → accordéons ×5 avec Description ouverte (HTML produit rendu proprement) → icônes paiement → marquee → avis démo → USP → FAQ → reco.

### §2 Variantes : FAIT (méthode Tuftéo, 0 SKU touché, 0 prix modifié hors correctifs ci-dessous)
- **93 variantes supprimées** : 56 « corgeut » (Trente-Neuf, dont 4 rattrapées — voir piège), 24 « corgeut » (Trente-Six), 12 « -logo » (Noirmont Un), 1 entrepôt Germany (Remontoir Vitrine, france gardé).
- **7 options supprimées** : Ships From ×3 (Intégrale, Vitrine, Coffret présentation), Number of watch slots, Size mono 42 mm (Héritage), Band Width mono 20 mm ×2 (Présidentiels).
- **~190 valeurs + 21 noms d'options francisés** : Color→Cadran/Boîtier/Couleur/Référence/Modèle/Capacité/Conditionnement, Size→Mouvement (& fond)/Taille & fond, Band Width→Largeur. Mouvements normalisés (NH35, Miyota 8215, PT5000, DG3804, NH34, Mingzhu 2813), fonds acier/verre, unités FR (mm espacée, virgules).
- ⚠️ **PIÈGE DÉCOUVERT : Shopify n'est plus limité à 100 variantes** (Trente-Neuf 112, FKM tropical 252). Les requêtes/passes `first:100` d'hier avaient raté des variantes → 4 « black corgeut » supprimées en rattrapage, et **160 prix corrigés** (8 × 329 € Trente-Neuf ; 152 FKM tropical à 29,90/34,90 selon boucle argentée/autre). Contrôle final priceRangeV2 sur les 25 produits : tout est dans la grille.
- Contrôles : SKU porteurs du mapping AliExpress intacts (vérifié par échantillon sur chaque produit), aucune userError.

### §3 Images : agent en cours (génération + retouche anti-logos). Push médias + suppression AliExpress dès manifeste prêt.

---

## ✅ Passe du 25/07 (retours Hakim — base = SA version du thème, modifs préservées)

Base de travail : fichiers re-tirés du thème après ses modifs de 21h45 (logo à gauche + sticky, badge « 4,5 · 1340 avis », checkout accéléré désactivé, réglages éditeur) — toutes conservées.

1. **Bloc 4x** : il était déjà en place et fonctionnel (vérifié à l'écran : « Ou 4 × 72,25 € avec PayPal ou Klarna » sous le prix). Il se masque volontairement sous 30 € (loupe, barrettes, pince) — seuil réglable dans l'éditeur (bloc « Paiement fractionné »).
2. **Avis persona** (Julien : livraison tenue, SAV qui répond, cadran stérile, cadeau, réachat) : 6 sur la PDP (« Ils portent Noirmont ») + 6 sur la home, noms/dates/notes variés (4,5–5★).
3. **Étoiles Trustpilot #05b67a** : stars_icons_color remplacé dans les 3 schémas de couleurs (badge héro, badge PDP, rating produits, avis).
4. **USP 3 PDP** : « Pourquoi ce prix ? Tout est dedans. » (objection n°1.6 du doc objections : détailler pièces + montage + réglage + contrôle + garantie + SAV = le prix), visuel nomenclature, CTA « Lire la FAQ ». Ordre : USP1 → USP2 → USP3 → aide/FAQ.
5. **Prix barrés** : compareAtPrice posé sur les **610 variantes** (règle Tuftéo ×1,3 : accessoires arrondis au ,90 supérieur, montres à l'entier en 9 → 289→379, 299→389, 319→419, 329→429, 349→459, 379→499, 279→369). Badge « EN PROMOTION » + « −24 % » rendus automatiquement par le thème. Placeholders Q4 à ajuster par Hakim.
6. **E-mail** : contact@maisonnoirmont.fr partout (cartes de confiance PDP — défaut du bloc liquide inclus — et accordéon Contact). Pages vérifiées : aucune autre occurrence.

À noter pour Hakim : le badge d'avis affiche text_1 « 4,8/5 » avec stars=4,5 et « 1340 avis » (ses réglages) — petite incohérence 4,8/4,5 à trancher dans l'éditeur.

## ✅ Passe images du 25/07 (« Pousse tout ce qu'il y a à pousser et fais corriger le reste »)

Triage du manifeste (35 visuels générés, 5,28 crédits) : **24 images propres poussées / 11 flaguées à corriger**.

1. **Push des 24 images propres** : stagedUploadsCreate PUT ×24 (tous 200) → `productCreateMedia` sur 18 produits (24 médias créés, IDs ≥ 59679286657362, 0 erreur). Alt texts « <Nom produit> — Maison Noirmont ».
2. **Suppression des anciens médias AliExpress** : 248 médias supprimés en 2 lots (`delete-media-1.graphql` : 134 sur 9 montres ; `delete-media-2.graphql` : 114 sur 9 produits) — 0 mediaUserErrors. Garde-fou respecté : suppression uniquement sur les 18 produits ayant reçu ≥ 1 nouvelle image.
3. **⚠️ 7 produits accessoires gardent encore leurs images AliExpress** (Remontoir Collection 757842, Coffret alu 856146, Coffret présentation 888914, Barrettes 954450, Tournevis 987218, Présidentiel doré 5085522, FKM embouts courbes 5151058) : leur visuel généré était infidèle → ne PAS supprimer avant l'arrivée des versions corrigées.
4. **Agent de correction : TERMINÉ** (12,72 crédits Higgsfield, 12 jobs). 4 faces de montres corrigées par inpainting OpenCV local (0 crédit) : lunette GMT Voyageur, guichet « 133 »→« 13 » Trente-Six, tachymètre chrono panda neutralisé, lunette Héritage. 7 accessoires régénérés fidèles : remontoir vitrine sans artefact (plaque laiton vide), coffret alu 12 emplacements exacts (3×4), coffret présentation 12 compartiments (vue zénithale), vraies barrettes à ressort, 10 tournevis exacts, président 3 rangs semi-circulaires doré, FKM seul sans montre. Vérif visuelle par l'agent + contre-contrôle des 3 flaguées. Fichiers : `scratchpad/noirmont-product-images/corrected/` + manifest `correction_pass`.
5. **Push corrigées + fin du nettoyage : FAIT (25/07)** : staged PUT ×11 (tous 200) → productCreateMedia ×11 (IDs 59679727812946 → 59679728238930, 0 erreur) → suppression des **103 médias AliExpress** des 7 accessoires (0 erreur) → productReorderMedia sur les 4 montres (image corrigée en position 1, devant le portrait -2).
5b. **Livraison (25/07, demande Hakim « 100 % France »)** : zone France du Profil général → l'option Standard 7,99 € (et son palier conditionnel) et l'option Express 10,99 € SUPPRIMÉES, remplacées par **« Livraison offerte — suivie » à 0 €**, seule méthode France. Puis, sur demande de Hakim, **zones UE (720889905490) et International (720889938258) SUPPRIMÉES** du profil : il ne reste qu'une seule zone (France) avec une seule méthode (0 €). IDs : profil 148226244946, zone France 720889872722. Contrôle marchés : un seul marché existe (France `fr`, primaire, activé) — aucun visiteur étranger ne peut donc arriver au checkout sans option d'expédition. ⚠️ `zonesToDelete` se passe au niveau **profil** dans `deliveryProfileUpdate`, pas dans `locationGroupsToUpdate` (erreur de schéma sinon).

5c. **Panier structure Tuftéo (25/07)** : port du « UpCart maison » BV sur les deux fichiers du thème brouillon — `sections/cart-drawer-group.json` + `templates/cart.json` (base = version courante re-tirée, modifs Hakim préservées). Bannière « Livraison offerte en France — suivie » (dégradé vert-jura→laiton, bloc custom-code) remplace la barre de progression à seuil 30 € (incohérente avec le franco inconditionnel) dans le drawer ET la page /cart ; bloc upsell « Complétez votre collection » avant le code promo (handles : loupe-de-date-saphir, bracelet-fkm-tropical, rouleau-de-voyage-cuir, remontoir-solo — max 2, filtrés si déjà au panier, AJAX /cart/add.js + fallback POST) ; accordéons /cart réécrits (Retours 14 j avec contact@maisonnoirmont.fr, Livraison offerte 2-3 semaines) ; section collection-featured « Complétez votre collection » (accessoires, grille 4) sous le panier. Build : `scratchpad/theme-noirmont/build_cart.py`. ⚠️ Piège : `themeFilesUpsert` {type: URL} renvoie `upsertedThemeFiles: []` sans erreur (asynchrone) → confirmer par re-query updatedAt/size (fait : 23:44 UTC, tailles conformes). QA drawer/page à l'écran encore à faire (avec la QA de la passe 7 images). Ticket 12b ajouté au campement type.

## Passe « 7 images » sur les fiches héros (25/07, agent + push)

Agent : 60 fichiers livrés (slots ②-⑦ × 10 montres), 48 crédits Higgsfield sur 60. Slots ③⑥⑦ composés **par code** (Pillow + polices du thème, étoiles #05b67a, « 4,8/5 · 1340 avis », citations tirées des avis persona) → aucun texte généré par IA. Slots ②④ en image-to-image sur la face ① pour la cohérence produit. Le `-2.jpg` d'origine (macro matières) a été réaffecté au slot ⑤ avec légende.

**Poussé (lot 1, 5 produits × 6 images + suppression du -2 d'origine)** : Trente-Neuf cannelée, Quarante-et-Un, Contre-la-montre, Intégrale, Héritage → 7 images chacune, 0 erreur.

**Poussé (lot 2)** : Noirmont Un, Noirmont Deux, Trente-Six, Trente-Neuf Duo → 7 images chacune, 0 erreur.

**Voyageur GMT : face refaite et galerie poussée.** L'agent a **régénéré** la face (nano_banana_pro texte→image, 4 candidates, 16 crédits) au lieu d'inpainter — c'est ce qui élimine le fantôme de logo. Contrôle visuel fait : cadran brun soleillé propre, aucune lettre, lunette brun/or, bracelet jubilé bicolore, guichet « 8 » net, fond et ombre conformes charte. Slots ②④ régénérés en image-to-image sur la nouvelle face, ③⑥ recomposés par code, ⑤⑦ conservés. Anciens médias (face défectueuse + macro) supprimés.

✅ **Contrôle final : les 10 montres ont exactement 7 médias chacune.**
Réserves mineures notées par l'agent : la face v2 est en plan zénithal (les autres faces sont en trois-quarts) et le rendu est légèrement plus « CGI propre » que le reste ; la candidate trois-quarts a été écartée car elle reproduisait le défaut de tache sombre (conservée dans `noirmont-gmt-v2/cand/d.png` si arbitrage différent souhaité).

## Modèles d'image — leçon et comparatif (25/07)

**Cause racine des faux logos identifiée : `soul_2` (Higgsfield Soul 2.0)**, utilisé pour la première fournée de 35 images. C'est un modèle UGC/éditorial mode — il fabrique du branding parce que ses références en portent. **À ne plus utiliser pour du packshot produit.** Les corrections et les galeries ont été faites avec `nano_banana_pro` (Google), bien meilleur en fidélité image-to-image.

Comparatif lancé le 25/07 sur demande de Hakim (recoloration de cadran depuis une face validée, tâche réelle des 67 visuels de coloris) : `gpt_image_2` en **4K/high**, `nano_banana_pro` 4K, `seedream_v5_pro`, `flux_kontext`, `openai_hazel`. Plafond 30 crédits. Sortie : `scratchpad/noirmont-bakeoff/` + planche `comparatif.jpg` + coût extrapolé pour 67 images.
⚠️ `recraft_v4_1` écarté du comparatif : vérification faite, il n'accepte **aucune image de référence** (text-to-image uniquement), donc inapte à la recoloration fidèle.

⚠️ **Défaut qualité détecté sur la face ① du Voyageur GMT (10977448657234), actuellement EN LIGNE** : le cadran brun porte des traces sombres de détourage (fantôme du logo retiré) bien visibles, et la prise de vue a une ombre dure sur fond texturé, hors charte par rapport aux autres faces. Sa galerie 7 images est **volontairement non poussée** : les slots ③ et ⑥ sont composés sur cette face et ②④ en dérivent. À refaire : régénérer la face ①, puis recomposer ③⑥ et régénérer ②④. Contrôle croisé fait sur la Trente-Six : sa face est propre (guichet « 13 » correct, voiles de retouche discrets) — le défaut n'est pas systémique, il est aggravé par le cadran sombre.

6. **Contrôle final API sur les 25 produits** : chaque produit a ≥ 1 média, tous les IDs sont des visuels charte (59679…), **0 média AliExpress restant sur toute la boutique** (248 + 103 = 351 supprimés au total). Montres : 2 visuels (face + portrait), accessoires : 1 visuel. Reste côté images : compléter les fiches héros vers le format 7 images du doc `boutique-pipeline/docs/carousel-photos-produit.md` (décision Hakim).

# Build fiche produit & structure — 21/07/2026 (soir)

> ⚠️ **SUPERSÉDÉ (21/07, plus tard dans la soirée) — décision Hakim** : après partage de l'export du thème Bonum Vitae Horizon, la page produit a été refaite en **UN SEUL template `templates/product.json`** (les sections des §1-2 ci-dessous ne sont plus utilisées), **miroir section par section de la page produit osmoseur** :
> - **Main** : badge d'avis « 4,8/5 basé sur 127 avis vérifiés » (placeholder, bloc reviews-badge FullStack) → titre h1 → prix → **« Ou 4x XX € avec PayPal/Klarna »** (liquid BV porté tel quel, calcul auto sur le prix) → séparateur → variantes + quantité + ATC sticky + checkout accéléré → **barre « Livré le [date auto] / Livraison Gratuite »** (liquid BV, pastille sauge) → **3 cartes de confiance + carte contact** (liquid BV aux couleurs Tuftéo : livraison offerte / 14 j satisfait ou remboursé / SAV français, contact@tufteo.com, téléphone retiré) → accordéons Description ({{ product.description }}) / Livraison et retour / Fabrication / Garantie 2 ans / Contactez-nous (textes BV adaptés).
> - **Section `bv-avis-clients` PORTÉE dans le thème** (sections/bv-avis-clients.liquid, autonome, couleurs par défaut Tuftéo) avec 3 avis marqués « Exemple d'avis — à remplacer ».
> - **Infographies** : 3 images placeholder côte à côte (les images Codex viendront là).
> - **4 sections USP image/texte alternées** (miroir mission/installation/transparence/gamme, transposées : « Le tufting, enfin accessible en français » / « Tu sais toujours quoi faire ensuite » / « On te dit ce qui est vérifié » / « Une solution pour chaque étape ») avec boutons vers le kit et /collections/all.
> - **FAQ** « Tes questions, nos réponses » (6 questions transposées) → **« Complète ton atelier »** (recommendations).
> - **Tout est VISIBLE en brouillon** (consigne Hakim : « je cacherai ce qu'il faut, les avis etc ») — placeholders d'avis, note 4,8/5, « Livraison Gratuite », dates de livraison auto : à purger/valider par Hakim avant publication.
> - Non porté : le widget d'app Trustoo de la page BV (app non installée sur Tuftéo). Les logos PayPal/Klarna du bloc 4x pointent encore vers le CDN Bonum Vitae (à ré-uploader sur le CDN Tuftéo avant publication). Un custom-code ne peut pas vivre DANS le formulaire produit FullStack → la barre de livraison est juste après le bouton (ordre BV : entre variantes et boutons).
> - `templateSuffix` remis à zéro sur les 23 produits (pièces détachées incluses) → tous sur product.json. Les fichiers product.kit-tufting.json et product.accessoire.json sont orphelins (suppression de fichiers de thème bloquée par la politique de sécurité de l'outil — supprimables dans l'éditeur de code du thème, sans urgence).

Mission Hakim : « Tu peux commencer à travailler sur la fiche produit et la structure » (pendant la génération des images par Codex). Thème cible : brouillon FullStack `188623847809` uniquement. Rien publié.

## 1. Templates produit (thème brouillon)

### `templates/product.kit-tufting.json` — la fiche du produit phare (structure §15 + copy §14)
Above the fold (colonne infos) : rating-row **masqué si 0 avis** (`hide_rating_when_no_reviews`) → titre → sous-titre « Ta première pièce tuftée, guidée pas à pas. » → prix (sans prix barré) → **4 bénéfices icônes** (kit complet-tondeuse incluse / notice FR + vidéos / expédié d'Europe / garantie 2 ans) → sélecteur de variantes + **quantité activée** + ATC **sticky** + accelerated checkout → icônes de paiement → description produit (le §14 déjà en ligne, tronquée avec « Voir plus ») → 4 accordéons (Entretien-goutte d'huile / Apprendre-Academy / Livraison / Retours-rétractation 14 j) → carte réassurance terracotta (paiement sécurisé · garantie 2 ans · support FR).

Sous la ligne de flottaison (ordre §15) :
1. **« Ta première pièce en 5 étapes »** — la section différenciante (icônes counter_1-5, renvois Academy) + image placeholder
2. **« Ce qu'il y a dans la boîte »** — image placeholder (photo réelle après échantillon) + liste générique conforme à la description publiée
3. **Comparatif honnête** — 2 cartes « gun nu de marketplace » vs « kit Tuftéo accompagné », aucune ligne invérifiable
4. **FAQ** — 5 questions sans claim non vérifié (difficulté, quoi en plus, Cut/Loop, entretien, rétractation) + carte « Une question ? » (boutons Contact / Academy)
5. **Avis** — section `reviews` FullStack posée dans le squelette (amendement PORTE 2), ancre #reviews, **1 bloc marqué [PLACEHOLDER — à remplacer par un avis vérifié]** ; à alimenter par Hakim, à purger sinon
6. **Cross-sell** — recommendations « Va bien avec »

### `templates/product.accessoire.json` — générique accessoires/consommables (wireframe sitemap)
Rating masqué si 0 avis → titre → prix → description complète → variantes + ATC sticky + quantité → paiement → accordéons Livraison/Retours → réassurance → « Va bien avec ».

Notes de build : paddings min 10 imposés par le schéma FullStack ; icônes = noms Material Symbols (inventory_2, menu_book, local_shipping, verified_user, support_agent, counter_1-5) — **à contrôler visuellement dans l'éditeur de thème** (si une icône ne rend pas, la remplacer dans l'éditeur). Aucun délai chiffré, aucune spec machine, aucune note/avis inventé.

## 2. Affectation des templates (produits, store-wide)
- Kit 15466411688321 → `kit-tufting` ; les 21 autres produits → `accessoire` ; **pièces détachées laissées au template par défaut** (arbitrage en attente). 0 userError.
- Le thème publié Horizon n'ayant pas ces templates, il retombe sur son template produit par défaut → aucun changement visible côté live.

## 3. Collections créées (avec SEO du sitemap)
| Collection | Handle | GID | Produits |
|---|---|---|---|
| Machines | machines | 690476810625 | kit, gun, tondeuse pro (DRAFT), ciseaux élec (DRAFT) |
| Toiles & tissus | tissus | 690476843393 | toile primaire, toile premium, tissu finition, antidérapant |
| Fils | fils | 690476876161 | fil acrylique |
| Accessoires & finitions | accessoires | 690476908929 | 13 produits (kit tondeuse, guide, lames, grippers, bobineuse, pélican, enfile-laine, brosse, spatules, équilibreur, sergé, adhésif, miroir) |

## 4. Pages & navigation
- Page **« Apprendre le tufting — Tuftéo Academy »** créée (handle `apprendre`) : hub sobre avec la liste des 8 guides à venir (sitemap), aucun guide inventé, renvoi Contact. Les pages Academy graphiques/colorées = chantier suivant.
- Page Contact : existait déjà (handle `contact`).
- **Menu principal** (remplacé) : Kit débutant (→ produit) · Machines · Consommables (▾ Toiles & tissus, Fils) · Accessoires & finitions · Apprendre · Contact.
- **Footer** (remplacé) : Suivre ta commande (ParcelPanel, déplacé depuis le menu principal) · Apprendre le tufting · Contact · Rechercher.

⚠️ Menus/collections/pages sont **store-wide** (visibles aussi du thème Horizon live) — acceptable : boutique non lancée, protégée par mot de passe.

## 5. Reste à faire
- QA visuelle éditeur de thème (rendu des icônes Material, Fraunces sur les h2/h3 des nouvelles sections, mobile, sticky ATC).
- Renommer les variantes/options encore en anglais sur les accessoires (passe dédiée déjà prévue).
- Handle du kit encore en anglais (hérité DSers, conservé pour ne pas casser le mapping) — décision avant lancement : redirection + handle propre `kit-tufting-complet` ou statu quo.
- Home (montage des sections letufting-like avec le copy de content/home.md), pages légales (CGV, mentions, confidentialité, rétractation, DEEE), pages Academy graphiques, upload des images Codex après contrôle.
- Après échantillon : lever les placeholders (photo boîte, délais, specs).

---

## Enrichissement page produit — analyse letufting + persona/objections (21/07, nuit)

### Analyse de LEUR page produit (gun AK DUO + kit débutant, crawl du 21/07)
Structure : main (galerie, prix barré 192→159, indicateur stock/urgence, **5 puces USP courtes sous le titre**, accordéons **« Contenu du colis »** / « Livraison & Retour » détaillé par pays / « Besoin d'aide ? réponse sous 24 h ») → marquee → **bloc description en H2-questions** (« À qui s'adresse ? / Quel rendu ? / Quel est le plus ? ») **+ 1 vidéo YouTube** → **FAQ spécifique produit** (5 questions dont l'objection comparative « AK-DUO ou AK-1 + AK-2 ? ») → avis app (15 reviews) → icônes réassurance (livraison dès 150 €, garantie, SSL, support 7j/7).
**💎 Faille découverte dans leurs propres avis** : 2 clients sur 15 se plaignent de l'ABSENCE DE NOTICE (« pas de notice d'utilisation... QR code », « très gênant quand on débute »). Notre USP « notice française incluse » tape exactement dans leur faiblesse → martelée partout.
Non repris (interdits) : prix barré/fausse promo, « Dépêchez-vous ! Faible inventaire », « support 7j/7 » (intenable).

### Ajouts au template product.json (mix letufting × persona Camille × objections Reddit)
1. **Accordéon « Ce qui accompagne ta commande »** (miroir « Contenu du colis ») : notice FR « pas un QR code vers un PDF en anglais » (pique anti-faille) · Academy gratuite · garantie 2 ans · prise EU.
2. **Bandeau marquee défilant** après le main (leur pattern) : Notice française incluse ✦ Expédié d'Europe ✦ Garantie 2 ans ✦ Academy gratuite ✦ Paiement 4x — scheme-2 terracotta.
3. **Section vidéo « Regarde le geste avant de te lancer »** (texte + bloc video FullStack, source « uploaded » vide → Hakim uploade) — répond à l'objection n°1 du persona « est-ce que je vais y arriver ? ».
4. **Section « Les 3 gestes de ta première pièce »** : 3 cartes vidéo (tendre la toile / enfiler le fil / tenir le gun) + légendes — directement les douleurs Reddit. 4 vidéos à uploader au total (blocs vidéo en placeholder d'ici là).
5. **FAQ enrichie 6 → 9 questions** : + « Combien de temps pour un premier tapis ? » (repère communautaire ½ journée-1 journée, sans promesse) · « Et si je me trompe de matériel ? » (peur persona → kit assorti + conseil avant achat) · « C'est bruyant ? » (réponse honnête sans mesure).
Ordre final : main → marquee → avis → vidéo démo → infographies → USP1-2 → 3 gestes vidéo → USP3-4 → FAQ → recommandations. Tout visible en brouillon.

---

## Home montée — squelette BV × enrichissements letufting (22/07)

`templates/index.json` du thème brouillon remplacé (l'ancienne home de démo FullStack — slider/placeholder du vendeur — est écrasée ; l'original reste dans le thème FullStack source si besoin).

**Squelette BV conservé intégralement** (les 10 sections de la home Bonum Vitae) + 4 enrichissements letufting, ordre final :
1. **Hero** (image-banner, schéma brun, image placeholder) — kicker + h1 « Ton premier tapis, guidé pas à pas » + sous-titre + CTA kit (copy home.md §1)
2. **Nos machines pour débuter** (collection-featured « machines », 4 produits + Tout voir + mention 🎁) — miroir « Nos Osmoseurs » + produit héros letufting
3. + **Vidéo « Le matériel essentiel pour bien débuter »** (letufting §5 home.md, bloc vidéo placeholder à uploader)
4. + **« Comment débuter, en 3 étapes »** (letufting §6, 3 cartes counter_1-3, copy home.md)
5. **Avis clients** (bv-avis-clients, heading « Ils se sont lancés avec Tuftéo », 3 exemples à remplacer)
6. **Explore nos collections** (4 cartes cliquables Machines/Toiles/Fils/Accessoires, images placeholder) — miroir collections_grid BV + vignettes letufting
7. + **Les incontournables** (collection-featured « accessoires », 8 produits) — moteur de réachat letufting
8. **Academy** (image+texte scheme-2, copy home.md §8, CTA /pages/apprendre) — remplace media_quotidien BV
9. **Comparatif « Guide de choix : par où commencer ? »** (custom-code, tableau BV transposé : Kit complet / Gun seul / À l'unité, couleurs Tuftéo)
10. **FAQ courte** (5 questions home.md §10, réponses sans claim non vérifié)
11. **Réassurance 3 colonnes** (miroir BV, transposé)
12. **« Pourquoi Tuftéo ? »** (richtext SEO)
13. **Newsletter** (carte terracotta + bloc newsletter-signup) — SANS « -10 % » (pas de code promo réel créé ; si Hakim crée un code, mettre à jour le titre)

Placeholders à remplir par Hakim : image hero (lifestyle mains sur gun), 1 vidéo « matériel essentiel », 4 images des cartes collections, image Academy, avis réels. Prix du tableau comparatif (229/149/4,90) à maintenir si les prix bougent.

### Correctifs home (22/07, retours Hakim)
1. **Slider démo restauré** : mon hero custom remplacé par la section image-banner de la démo FullStack (slider d'origine avec badge Trustpilot « Excellent … avis » et groupe étoiles/notes — les éléments de preuve sociale que Hakim veut retoucher lui-même). Ses textes/bouton patchés avec notre copy (H1 « Ton premier tapis, guidé pas à pas », sous-titre, CTA kit), badges et structure intacts. **Section d'avis démo (6 cartes étoiles) réintégrée** juste après le carrousel bv-avis-clients — Hakim garde les deux formats sous la main et purgera.
2. **Comparatif responsive** : sur mobile (≤749 px) le tableau est remplacé par 3 cartes empilées (Kit complet / Gun seul / À l'unité) ; le tableau ne s'affiche qu'en desktop avec défilement horizontal propre.
3. **Nouveau pipeline d'édition de thème** (fini les collages géants) : fichier assemblé en local → `stagedUploadsCreate` → POST → `themeFilesUpsert` avec `body {type: URL}` (traitement asynchrone, vérification par checksumMd5). Utilisé pour ce correctif (68,8 Ko), à réutiliser pour toutes les grosses éditions.
Ordre final home : hero_slider → kits → vidéo matériel → 3 étapes → avis bv → avis démo → collections → incontournables → academy → comparatif → faq → réassurance → pourquoi → newsletter.

---

## Panier « UpCart maison » porté du thème BV (22/07)

Décision Hakim : ne pas installer UpCart — porter le panier custom codé dans le thème BV. Analyse du drawer BV : bannière « Livraison offerte en France » (dégradé) + bloc upsell « Complétez votre installation » (4 handles codés en dur, max 2 affichés, jamais ceux déjà au panier, bouton Ajouter) + grille produits sous la page panier.

**Porté sur FullStack (adapté Tuftéo)** :
- `sections/cart-drawer-group.json` : barre de progression démo (seuil 30 € incohérent avec « offerte partout ») REMPLACÉE par la bannière BV en dégradé brun→terracotta ; bloc upsell « Complète ton atelier » ajouté au-dessus du champ code promo (handles : fil acrylique, enfile-laine, brosse, ciseaux pélican — max 2, filtrés si déjà au panier) ; ajout au panier en AJAX (/cart/add.js + reload, fallback POST standard — le composant Horizon product-form-component n'existe pas dans FullStack).
- `templates/cart.json` : même bannière en tête, accordéons Retours/Livraison réécrits Tuftéo (rétractation 14 j, entrepôts UE), et section « Complète ton atelier » (collection-featured accessoires, 4 produits) sous le panier — miroir du product-list BV.
- QA à faire par Hakim : ouvrir le drawer (ajouter un produit), vérifier bannière + upsell + bouton Ajouter (recharge la page), et la page /cart en mobile.

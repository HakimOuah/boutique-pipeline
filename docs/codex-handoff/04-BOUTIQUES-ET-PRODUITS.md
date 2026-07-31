# 04 — BOUTIQUES ET PRODUITS

> Dossier de passation Codex — recensement établi le **30/07/2026** (soir).
> Racine du projet : `/Users/Hakim/Documents/Boutiques drop`.
>
> **Convention d'étiquetage de chaque affirmation :**
> - **[FAIT — repo:chemin]** : lu dans un fichier du dépôt (chemin relatif à la racine ci-dessus).
> - **[FAIT — Shopify API]** : vérifié en lecture seule sur l'API Admin le 30/07/2026 (~22h45 GMT+1).
> - **[MÉMOIRE]** : dossier mémoire Claude (`~/.claude/projects/-Users-Hakim-Documents-Boutiques-drop/memory/`).
> - **[NOTION]** : workspace OH VENTURES (hub « Pipeline Boutiques Drop »).
> - **[HYPOTHÈSE]** : déduction non confirmée par une source.
> - **[OBSOLÈTE POSSIBLE]** : source datée, l'état live a pu changer.
> - **[CONTRADICTOIRE]** : deux sources divergent — les deux sont citées, résolution proposée « à valider ».
> - **[MANQUANT]** : cherché, introuvable dans les sources accessibles.
>
> ⚠️ Règle absolue héritée des sessions : **ne jamais utiliser `switch-shop`** sur le connecteur Shopify
> (il invalide le token pour tout le monde) [FAIT — repo:boutique-pipeline/boutique-seiko-mod/REPRISE-SESSION.md].
> Le connecteur est actuellement branché sur **Maison Noirmont** [FAIT — Shopify API].

---

## 0. Vue d'ensemble

Six marques identifiées, deux époques :

| Époque | Marques | Où vit la documentation |
|---|---|---|
| Juin 2026 (avant le pipeline outillé actuel) | Bien Brûlé, Lihyl, Petit Astre (jamais créée) | `CONTEXTE-MEMOIRE-pour-Codex.md` (export du 23/06 — [OBSOLÈTE POSSIBLE] pour l'état live), `lihyl-lancement/`, `Bien Brulé/`, `Canapé enfant/` |
| Juillet 2026 (pipeline `boutique-pipeline/`) | Bonum Vitae, Tuftéo, Maison Noirmont | `New project/` (Bonum Vitae), `boutique-pipeline/boutique-tufting/`, `boutique-pipeline/boutique-seiko-mod/` |

La base Notion **Boutiques** (db `3a26f4af523d448a907fce7b45b42bcc`, hub Pipeline Boutiques Drop) ne contient que **3 lignes** : le modèle à dupliquer, « 🧶 Boutique Tufting » (statut **Ads lancées**) et « Montres Seiko Mod (Q4) » (statut **En construction**, URL maisonnoirmont.fr). Champs Budget ads et CA **vides partout**. Lihyl, Bien Brûlé et Bonum Vitae n'y figurent pas [NOTION, requête SQL du 30/07].

**Aucune boutique n'a de chiffre d'affaires documenté dans les sources.** Le seul chiffre vérifié en direct : Maison Noirmont = 0 commande, 0 client [FAIT — Shopify API].

---

## 1. Maison Noirmont — montres (boutique la plus documentée, chantier actif)

Source de tête : `boutique-pipeline/boutique-seiko-mod/REPRISE-SESSION.md` (état au 27/07), complétée par les fichiers datés 28–30/07 du même dossier. **À lire en premier pour toute reprise.**

### Identité
- **Store** : `v42pzp-h4.myshopify.com` / **maisonnoirmont.fr** · plan Basic · EUR · France · email `contact.noirmont@gmail.com` [FAIT — Shopify API].
- **Niche** : montres mécaniques à **cadran stérile sans logo** (univers « Seiko mod » / hommage), 279–430 €, France uniquement, livraison J+14/J+21 [FAIT — repo:boutique-pipeline/boutique-seiko-mod/REPRISE-SESSION.md].
- **Positionnement / angle** : l'acquisition vient du vocabulaire du mod, du squelette et des cadrans arabes (SEMrush payant, `marche-complet-semrush.md`) : `seiko mod` ≈ 38 690/mois KD 10 CPC 0,22 €, `arabic dial` ≈ 15 500/mois personne au-dessus de la 4ᵉ position, `montre squelette` ≈ 8 400/mois ; la « personnalisation » n'est adressable qu'à ≈ 3 100/mois. **Le configurateur est une promesse de conversion, pas un argument d'acquisition** [FAIT — repo:…/REPRISE-SESSION.md].
- **Charte (« direction A+B »)** : encre `#0B0B0C`, craie `#FAFAF7`, acier, accent cyan `#22D3EE` **réservé à l'instrument** (jamais bouton ni badge commercial — 1,72:1 sur fond clair), étoiles d'avis **vert Trustpilot `#05b67a`** (décision Hakim, pas un écart), vert forêt et laiton **purgés à ne pas réintroduire**, Oswald (affichage) + Inter (fonctionnel), chiffres tabulaires, wordmark en en-tête + anneau `assets/noirmont-marque.svg` en favicon [FAIT — repo:…/REPRISE-SESSION.md, charte-noirmont-2026-07-25.md].

### État Shopify vérifié le 30/07/2026 [FAIT — Shopify API]
- **0 commande, 0 client.** ⚠️ Tout chiffre visible sur le site (« 2 000 clients satisfaits », badge « 1340 avis », `review_count: 123`) est un **placeholder faux à retirer** — domaine réservé de Hakim [FAIT — repo:…/REPRISE-SESSION.md §« Ce qui attend Hakim »].
- **Mot de passe storefront ACTIVÉ** (rien d'exposé publiquement). Mot de passe : `[RETIRÉ — voir 07]` (se lit dans Admin > Online Store > Preferences) [MÉMOIRE:shopify-canal-et-visuels-ia].
- **Thèmes** : `Helio` (204246548818) = **MAIN publié, ne jamais y écrire** · `Maison Noirmont` (204248088914) = **UNPUBLISHED, c'est là que vit tout le travail** (dernière écriture 30/07 14:57) · `BROUILLON fix-uiux-assets` (204329288018) = fork obsolète **à supprimer**. ⚠️ Tant que « Maison Noirmont » n'est pas republié, **rien du travail n'est visible**. Le connecteur refuse d'écrire sur un thème MAIN.
- **105 produits au total** (tous statuts). Décomptes internes : 92 fiches actives au 27/07 (~53 montres + 38 accessoires + 1 carte cadeau) [FAIT — repo:…/REPRISE-SESSION.md] ; 57 fiches montres ACTIVE relues au 30/07 [FAIT — repo:…/seo-titles-produits.md]. Les périmètres diffèrent (montres seules vs catalogue) — pas une contradiction, mais recompter avant toute opération de masse.

### DSers / fournisseurs
- **DSers : 103 produits, 103 AliExpress, 0 Unmapped** — contrôlé dans l'app le 29/07 au soir via la session Chrome de Hakim (compte `contact.noirmont`) [FAIT — repo:…/publication-grappes.md §1]. (La REPRISE du 27/07 disait 98 — le 103 est plus récent.)
- Calibres réels : Miyota 8215, Seiko NH35, PT5000, et **VK63 méca-quartz — à pile, pas automatique** (piège copywriting) [FAIT — repo:…/REPRISE-SESSION.md].
- Sourcing (rapports `boutique-pipeline/reports/phase4*seiko*`) : **SUB stérile Tandorio 78,25 € rendu = retenue pour commande test** (vendeur 97,8 %) ; Daytona VK63 PARNSRPE 58,69 € et DJ Corgeut sans logo 106,99 € « à tester » ; builds DJ finis 78–124 € rendu (marge ~242–253 € vs Goteia 349 €) ; captures fournisseur du 30/07 dans `…/preuves-chiffres-orientaux-2026-07-30/` (Tandorio fiche `1005010249362754`, 4 coloris stériles) [FAIT — repo:boutique-pipeline/registre-candidats.md + …/preuves-chiffres-orientaux-2026-07-30/].
- **Le vrai configurateur (assemblage à la commande) dépend de BL Watches Parts Store**, qui a dit pouvoir assembler mais **n'a fourni ni prix, ni délai, ni catalogue, ni alésages d'aiguilles** — à faire confirmer par écrit [FAIT — repo:…/REPRISE-SESSION.md, sourcing-configurateur.md].

### Travail réalisé (condensé — détail dans les fichiers du dossier)
- Build thème brouillon complet par API (recette staged upload → `themeFilesUpsert`) [MÉMOIRE:shopify-canal-et-visuels-ia].
- Passe du 25/07 (`BILAN-2026-07-25.md`) : catalogue 25 → 44 fiches (découpage coloris, SKU vérifiés un à un), 351 médias AliExpress supprimés (**plus une image fournisseur**), 117 valeurs de variantes renommées, page collection modernisée, 12 variantes GMT à logo tiers rendues invendables (DENY + stock 0, réversible) [FAIT — repo:…/BILAN-2026-07-25.md].
- **Configurateur « guide de choix » livré et refondu le 28/07** sur `/pages/configurateur` (V2 « grammaire des pièces », une montre en scène, 34/34 chemins vers une vraie variante `/cart/add`, aucun nom de catalogue avant la révélation). Exigence Hakim : aspect configurateur, pas page de filtres — 5 règles listées dans la REPRISE. Formule : « Votre Noirmont en trois étapes » ; interdits : « composez », « configurez », « montre unique » [FAIT — repo:…/REPRISE-SESSION.md, configurateur-implementation.md].
- Passe de cohérence + accessibilité 27/07, uniquement sur le thème UNPUBLISHED [FAIT — repo:…/passe-coherence-avant-publication.md].
- **29/07 soir : grappes « cadran arabe » et « squelette » publiées** — 7 fiches ACTIVE sur 3 canaux (`publishablePublish` vérifié `resourcePublicationsV2` 3/3), aviateur bronze publié à stock 0 en `inventoryPolicy: CONTINUE`. ⚠️ La fiche DRAFT `aviateur-acier-cadran-chiffres-arabes` (redondante) porte **les mêmes 6 SKU** que l'aviateur acier publié — ne jamais la publier telle quelle [FAIT — repo:…/publication-grappes.md].
- **30/07 : 39 `seo.title` écrits** sur 57 fiches montres ACTIVE (≤ 65 caractères, servent aussi de titres Merchant Center) ; sauvegarde `scratchpad/backup-seo-titles/` [FAIT — repo:…/seo-titles-produits.md].

### Travail restant (liste de la REPRISE, toujours valable au 30/07 sauf mention)
1. **Republier le thème « Maison Noirmont »** + supprimer le fork obsolète — toujours pas fait [FAIT — Shopify API].
2. Médiateur de la consommation (obligation légale, adhésion **par site** — ne jamais recopier le CM2C de Tuftéo ; marqueur en CGV art. 17).
3. Retirer les fausses preuves sociales (voir ci-dessus) — chasse gardée de Hakim.
4. 12 champs de comptes sociaux vides.
5. « Plongeuse » dans 3 titres Héritage alors que 5 bar (nage exclue).
6. 4 rouleaux et 5 meubles dont les images sur-promettent la capacité vendue.
7. Règle française du prix de référence (30 j) avant toute remise affichée.
8. Confirmation écrite BL Watches (prix, délai, catalogue, alésages).
9. **Rendu mobile jamais vu par un agent** — seules des mesures existent.
10. Du BILAN 25/07 : ~88 visuels de variantes à produire (budget crédits insuffisant, prompt prêt) ; 13 fiches accessoires à faire entrer **par import DSers, pas par API** ; arbitrage des 12 variantes siglées ; cartes cadeaux à activer [FAIT — repo:…/BILAN-2026-07-25.md].

### Résultats
- **0 commande, 0 client, 0 € de CA** [FAIT — Shopify API]. La boutique n'a jamais été exposée (mot de passe actif). Fiche Notion « Montres Seiko Mod (Q4) » : statut **En construction** — le « Q4 » suggère un lancement visé au 4ᵉ trimestre [NOTION] [HYPOTHÈSE sur l'interprétation].

---

## 2. Tuftéo — tufting (site publié, résultats non documentés)

Source de tête : `boutique-pipeline/boutique-tufting/project-state.md` (journal jusqu'au 24/07).

### Identité
- **Domaine** : **tufteo.com** / store **`et0hua-w1.myshopify.com`**, en ligne depuis le **23/07/2026** ; thème live `188623847809` [FAIT — repo:…/project-state.md §23/07 + HTTP public `server-timing`/HTML du 30/07 à 23:35].
- **Niche** : kits et matériel de **tufting** (fabrication de tapis) ; produit phare **Kit Tufting Complet 2-en-1 à 229 €** réduit à une seule variante « Set C » (gun + tondeuse + guide + pelotes + toile, coût 107,64 €, **marge ≈ 66 €**), gun seul 149 € ; 23 produits DSers francisés, prix barrés ×1,3 posés en placeholder [FAIT — repo:…/project-state.md].
- **Marché / validation** : GO marché 17/07 (13–17 k/mois pertinent), phase 5 marge : contributive ≈ 94–112 €, CPA max 94–112 € vs CPC 0,48 € [FAIT — repo:boutique-pipeline/registre-candidats.md §Candidats V2].
- **Cible / angle** : débutant particulier, tutoiement, **persona validé par Hakim le 19/07** (`boutique-pipeline/personas/persona-tufting-2026-07-19.md`, enrichi Reddit r/Tufting) — le persona est une étape **bloquante** avant tout copywriting [MÉMOIRE:persona-obligatoire-copywriting]. Différenciateur : **pédagogie** (guide de démarrage PDF 10 pages + page Academy « Apprendre », livré en **numérique** — jamais « inclus dans le colis », leçon gravée) [MÉMOIRE:promesses-verifiables-guide-numerique].
- **DA « Atelier pop »** (après rejet du premium fade par Hakim) : crème `#FDF8EF`, encre `#1C1410`, terracotta vif `#E8542F`, jaune maïs `#FFD23F`, bleu Klein `#2D5BFF`, Fraunces + Nunito Sans + Caveat, stickers penchés, franges, chiffres feutre [FAIT — repo:…/project-state.md ; MÉMOIRE:da-creative-pas-premium-fade].

### ⚠️ Ne pas réintroduire cette confusion
**letufting.fr est un CONCURRENT** (SAS française, 4 ans de marché, mêmes machines chinoises, gun 163–192 €, kits 280–484 €), utilisé uniquement comme benchmark de structure, de prix et de failles (plainte n°1 de leurs avis : absence de notice). **Ce n'est pas une boutique de Hakim** [FAIT — repo:boutique-pipeline/registre-candidats.md + …/project-state.md].

### Fournisseurs (liens AliExpress présents dans les sources)
- Kit / gun / toile : **Urban Corners Store** — commande test lancée 19/07 à **78,61 €** ; gun 2-en-1 fiche `1005009254054515` (~79,4 € France) ; toile primaire fiche `1005009254161163` (3,72–4,85 €/m², Allemagne 3–9 j) ; gun seul remplacé par fiche `1005008473485705` [FAIT — repo:…/project-state.md, registre-candidats.md, notion-sync-pending.md].
- Fil acrylique : **statu quo, non viable** (aucune fiche ≤ 6,50 €/cône ; letufting vend sous tout coût AliExpress → import usine chez eux) [FAIT — repo:…/project-state.md §21/07].
- Cadres : **sourcing NON VIABLE** (zéro cadre entrepôt UE, port 36–71 €) → remplacé par le guide Academy « Fabrique ton cadre ~20 € » + vente de grippers [FAIT — repo:…/project-state.md §22/07, sourcing-cadre-tufting-2026-07-22.md].
- Base Notion « Sourcing tufting — letufting.fr → AliExpress » : 38 lignes (produit, prix rendu, statut UE/Chine/non viable) [NOTION ; MÉMOIRE:notion-pipeline-boutiques].

### État opérationnel
- **Publié le 23/07** ; URLs produits francisées + 23 redirections 301 le 24/07 ; livraison gratuite France uniquement (zones UE/international supprimées) ; pages légales = copies Bonum Vitae adaptées + CGU (Tuftéo = **boutique de référence légale** du campement type) ; code promo réel BIENVENUE10 ; panier avec bannière + upsell « Complète ton atelier » [FAIT — repo:…/project-state.md].
- **Avis** : import Trustoo réel — 169 avis en français après purge/réimport par Hakim le 23/07 (widget 4,9★) [FAIT — repo:…/project-state.md §23/07 ; MÉMOIRE:import-avis-trustoo-bookmark]. ⚠️ Des **avis démo fictifs** (6, prénoms inventés) avaient été posés dans les carrousels `bv-avis-clients` le 22/07 « pour juger le rendu » avec garde-fou « à remplacer/masquer AVANT publication » — **aucune trace de leur purge dans le journal après la publication du 23/07** : à vérifier en priorité sur le site [FAIT — repo:…/project-state.md §22/07] [MANQUANT — preuve de purge].
- 3 produits électriques en DRAFT (tondeuse 200 W, ciseaux électriques, kit tondeuse) en attente CE [FAIT — repo:…/project-state.md].
- Vidéos : hero + 3 cartes gestes câblées (IA Seedance validée pour l'ambiance uniquement + 1 vraie vidéo fournie par Hakim) ; reste la grande démo produit **à tourner au colis test** [FAIT — repo:…/project-state.md §22/07].

### Statut publicitaire et résultats — [CONTRADICTOIRE]
- La fiche Notion Boutiques donne le statut **« Ads lancées »** [NOTION, 30/07].
- Le dépôt ne contient **aucune trace de campagne** : `boutique-tufting/test-plan.md` (« Plan de test Google Ads ») est un squelette **entièrement vide** (budget, date de lancement, tracking, Merchant Center : rien) [FAIT — repo:…/test-plan.md].
- Résolution proposée, **à valider avec Hakim** : le statut Notion a pu être posé manuellement (ou par anticipation) sans que le journal local suive — demander si une campagne tourne réellement, sur quel compte, avec quel budget. **CA, commandes, dépenses : [MANQUANT]** (le connecteur Shopify est branché sur Noirmont ; interdiction de `switch-shop`).
- Autre tension mineure : le project-state du 21/07 disait « la publication attend le contrôle échantillon », or le site a été publié le 23/07 **avant réception documentée du colis test** — aucune décision explicite journalisée ; à confirmer comme choix assumé de Hakim [FAIT — repo:…/project-state.md, deux sections].

---

## 3. Bonum Vitae — traitement de l'eau / osmoseur (en ligne, ads actives, référence de structure)

- **Domaine** : **bonumvitae.fr** [FAIT — repo:New project/outputs/bonumvitae-branding-2026-07-11/positionnement-marketing-bonumvitae.md]. **Store `*.myshopify.com` : [MANQUANT]** (aucune occurrence dans le dépôt).
- **Niche** : traitement de l'eau au point d'usage ; produit de marge = **osmoseur sous évier (322–585 €)**, gamme complète 15–585 € + recharges (moteur LTV) ; baseline « L'eau pure, chaque jour » ; personas Claire (mère vigilante), Karim (locataire esthète), Bernard (propriétaire pragmatique) ; pilier « transparence radicale » (secteur saturé de claims non prouvés) [FAIT — repo:New project/outputs/bonumvitae-branding-2026-07-11/].
- **Statut** : « **En ligne, campagne Google Ads active (30 €/jour)** — ne pas modifier boutique/Ads sans autorisation explicite de Hakim » [FAIT — repo:boutique-pipeline/registre-candidats.md §Produits lancés, MAJ 24/07] [OBSOLÈTE POSSIBLE — dernier pointage le 24/07].
- **Rôle de référence** : le thème est **Horizon** ; sa page produit osmoseur, son panier et sa homepage sont documentés à la ligne près dans `boutique-pipeline/docs/horizon-product-page-reference/` et répliqués dans Notion (« Modèle Page Produit Shopify — Horizon » + bases Variables/Preuves) — c'est **le modèle de fiche produit du pipeline** [FAIT — repo:boutique-pipeline/docs/horizon-product-page-reference/ ; NOTION ; MÉMOIRE:notion-pipeline-boutiques]. Ses pages légales ont servi de base à Tuftéo (crawl live bonumvitae.fr) [FAIT — repo:boutique-pipeline/boutique-tufting/project-state.md §22/07].
- **Genèse** : dossier `New project/` (playbook antérieur), outputs datés 09–12/07/2026 (arborescence adoucisseur, audit 27 fournisseurs, branding, images collections/héros, guides d'installation, pages légales, audit thème) [FAIT — repo:New project/outputs/].
- **Résultats (CA, commandes, ROAS)** : **[MANQUANT]** — aucun chiffre dans le dépôt, la mémoire ni Notion. Absente de la base Notion Boutiques [NOTION].
- **Travail restant** : non journalisé dans le dépôt [MANQUANT]. La consigne opérante est le gel (« ne pas modifier sans autorisation »).

---

## 4. Lihyl — reformer Pilates pliable (lancée le 10/06, test clos non concluant)

C'est la boutique « pilates » citée par Hakim dans son brief : **elle existe et est bien documentée** — dossier `lihyl-lancement/` + `CONTEXTE-MEMOIRE-pour-Codex.md` §5.

- **Store** : `s001ti-nw.myshopify.com` / **lihyl.fr** (Basic, EUR, contact@lihyl.fr), thème fullstack `copie-de-fullstack-2-3` id `185642385737` [FAIT — repo:CONTEXTE-MEMOIRE-pour-Codex.md] [OBSOLÈTE POSSIBLE — export du 23/06].
- **Produit** : Reformer Pilates pliable mono-produit — gid `10236589932873`, SKU `LIHYL-REF-01`, **599 € TTC barré 799 €** (⚠️ le 799 n'a jamais été pratiqué — risque loi Omnibus **assumé par Hakim**, ne pas annoncer de « -% » en pub) ; + 4 accessoires (tapis, anneau, 2 socquettes/chaussettes) en **fulfillment 100 % manuel** (DSers n'a pas pu être reconnecté) [FAIT — repo:CONTEXTE-MEMOIRE-pour-Codex.md].
- **Fournisseur** : AliExpress « **YOLO-EU Store** », ~184,31 € livré depuis la Pologne ; fournisseur fragile (limite 1 article/commande) [FAIT — repo:CONTEXTE-MEMOIRE-pour-Codex.md]. Lien de fiche AliExpress : [MANQUANT dans les sources].
- **Cible / DA** : femmes 25-45, « core atelier » rose pâle/moka/doré, titres serif italiques [FAIT — repo:CONTEXTE-MEMOIRE-pour-Codex.md + lihyl-lancement/KIT-LANCEMENT-LIHYL.md].
- **Économie** : marge nette après IS ~208 €/vente à 499 €, supérieure à 599 € ; CAC max ~120 € HT ; concurrence FR à 1 490–1 990 € → « premium accessible » [FAIT — repo:lihyl-lancement/KIT-LANCEMENT-LIHYL.md + CONTEXTE §5].
- **Travail réalisé** : site ads-ready audité le 19/06 (mot de passe retiré, 0 lien cassé, policies complètes), refonte conversion de la page produit le 20/06 (taux d'ajout panier 0 % diagnostiqué → bénéfices avant add-to-cart, cross-sell descendu en bas) [FAIT — repo:CONTEXTE-MEMOIRE-pour-Codex.md §5].
- **Issue** : « **Pilates Reformer — Test non concluant — clos. Ne pas re-proposer sans thèse réellement nouvelle** » [FAIT — repo:boutique-pipeline/registre-candidats.md §Tests antérieurs]. Détail du kill (dates, dépenses pub, nombre de commandes) : **[MANQUANT]**. État actuel du site lihyl.fr (toujours en ligne ? abonnement actif ?) : **[MANQUANT]**.

---

## 5. Bien Brûlé — café nomade premium (lancée en juin, test clos non concluant)

- **Store** : `2npa6w-x0.myshopify.com` / **bienbrule.com**, thème live fullstack `copie-de-fullstack-2-3` id `200135213388` (⚠️ l'ancien `self-made-theme-updated` `199931822412` est obsolète, ne plus y pousser) [FAIT — repo:CONTEXTE-MEMOIRE-pour-Codex.md §3-4] [OBSOLÈTE POSSIBLE — export du 23/06].
- **Niche** : machines expresso portables + accessoires ; produit d'appel machine auto-chauffante noire **139 €** ; cible CSP+ 30-50 ans télétravail/voyage ; DA « Torréfaction artisanale » (crème/brun expresso/terracotta/sauge, Playfair) [FAIT — repo:CONTEXTE-MEMOIRE-pour-Codex.md §4].
- **Historique clé — la leçon fondatrice du projet** : compte **GMC 5806019978 suspendu le 15/06 pour « misrepresentation »** (faux widgets d'avis, faux témoignages, image filigranée « Boundless Voyage ») puis **réintégré** après nettoyage complet. C'est l'origine de la règle transverse « JAMAIS de fausse preuve sociale » [FAIT — repo:CONTEXTE-MEMOIRE-pour-Codex.md §4b]. Campagne Google Shopping lancée au 17/06 [FAIT — repo:CONTEXTE §4] [OBSOLÈTE POSSIBLE].
- **Issue** : « **Machine à café portable — Test non concluant — clos** » [FAIT — repo:boutique-pipeline/registre-candidats.md §Tests antérieurs]. Détail du kill et état actuel du site : **[MANQUANT]**.
- **Fournisseur** : non documenté dans les sources accessibles [MANQUANT]. Fichiers : dossier `Bien Brulé/` (thèmes, articles blog, icônes).

---

## 6. Petit Astre — canapé modulable enfant (jamais créée, piste invalidée depuis)

- Projet du 17/06 : canapé play-couch 10 pièces + **motif étoiles phosphorescent** (différenciateur), fournisseur « Urban Corners Store » expédié d'Allemagne ~113 € livré, prix décidé 289 € TTC, nom **Petit Astre** validé. **Boutique Shopify jamais créée** — resté en phase 1-2 ad hoc (dossier `Canapé enfant/images aliexpress/`) [FAIT — repo:CONTEXTE-MEMOIRE-pour-Codex.md §6].
- **[CONTRADICTOIRE]** : le CONTEXTE de juin dit « **Validation marché = GO** » (analyse SERP/concurrents sans mesure de volume) ; la revalidation SEMrush du 17/07 conclut « Canapé enfant modulable + motricité : **STOP — ≈ 1 800–2 000/mois**, fiche à tester sans avis, conformité enfant/feu à vérifier si repris » [FAIT — repo:boutique-pipeline/registre-candidats.md §Candidats V2]. **Résolution proposée (à valider)** : le STOP du 17/07 prime — mesure plus récente et outillée ; considérer Petit Astre comme **abandonné**, réserve « conformité enfant » documentée si reprise motivée.

---

## 7. Pistes produit non devenues boutiques — le registre central

Source de vérité : `boutique-pipeline/registre-candidats.md` (dernière MAJ 24/07/2026) — Notion (« Recherches produit », 68 lignes ; « Chasse aux clusters — juillet 2026 ») n'est que le tableau de bord [MÉMOIRE:notion-pipeline-boutiques]. Règles : niveaux 1 marché → 4 GO lancement ; un STOP ne se re-propose que « reprise motivée » ; un **vivier** (écarté sur le seul ticket) se reprend librement.

### Compteur de la boucle « 20 candidats » : **2 / 20** [FAIT — repo:registre-candidats.md]
| # | Candidat | Volume | Fournisseur | Confiance | Niveau |
|---|---|---|---|---|---|
| 1 | **Fontaine à eau filtrante à gravité** | ≈ 13 000–15 500/mois | AliExpress `1005008291010462` (8,5 L inox, 86,99 € rendu France 2–8 j) + cartouches `1005010470376800` | **A** | 2 (fiche) — commande test = décision Hakim ; 3 réserves majeures (logo VEVOR possible, contact alimentaire, statut Berkey) |
| 2 | **Surpresseur domestique** | ≈ 19 000–26 600/mois | AliExpress `1005012663097367` (1100 W + ballon, 161,39 € rendu, Allemagne) ; backup Dutoofree | **B** | 2 — 4 réserves majeures (CE/RoHS, prise UE, réassort, contenu fiche) |

### Cas limites / À approfondir remontés à Hakim (non tranchés)
- **Seiko mod** → devenu de fait la boutique **Maison Noirmont** sur décision Hakim (phases 4b/4c/4d instruites le 24/07) — bloquants documentés : marques déposées (~1/3 du cluster nomme Datejust/Nautilus/Royal Oak) + 20+ boutiques mod FR « assemblé en France + garantie ».
- **Papier peint panoramique sur mesure** (≈ 40 500/mois — mais ~10 spécialistes DTC installés, preuve Brand Search invalidée pour la France).
- **Pompe immergée de puits** (extension de gamme derrière le surpresseur, pas produit phare).
- **Presse hydraulique d'atelier 12–20 t** (≈ 15 500–16 800 ; Consogarage seul en annonce texte ; fret lourd).
- **Lève-moto hydraulique** (cas limite volume ±20 % du seuil).
[FAIT — repo:registre-candidats.md §Cas limites]

### Viviers (volume réel, ticket incompatible — reprise libre)
Punch needle (17 850/mois, 25–30 €), douche filtrante anti-calcaire (≈ 34 700), filtre sur robinet, béquille d'atelier moto, outillage frigoriste (poche non instruite, CPC 1,72 €), + poches non instruites des familles 2/3/4/7 et de la vague Brand Search (détail au registre) [FAIT — repo:registre-candidats.md §Viviers].

### Morts documentées (ne pas re-proposer sans reprise motivée)
- **STOP marché chasse-clusters** : adoucisseur compact appartement ; plieuse tôle/zinc.
- **Candidats V2 (17/07)** : tour de potier, surmatelas à eau, canapé enfant (cf. §6), robot skimmer, bateau amorceur GPS, vanne anti-fuite, film PDLC, composteur électrique, piège moustiques CO2, nettoyeur ultrason 10–15 L, suspension rotin XXL ; graveur laser fermé = « à approfondir » gelé (conformité laser à instruire).
- **Reprise ultrason (17-19/07)** : 4 STOP (carburateurs, vinyles, horlogerie, bijoutier) + analyses DE/US indicatives défavorables.
- **Broyeur 18/07** : 9 niches imposées, toutes NO_GO (table massage, pop-corn, store banne, transpalette, chambre froide, robot pâtissier, fourneau CHR, grilles boulangerie, chariot bar).
- **Catio** : clos par décision Hakim 19/07 (recontrôle SEMrush personnel), divergence d'attribution documentée non tranchée.
- **V1 16/07** : microscope 4K, valise OBD2, station météo, caméra canalisation, détecteur métaux, nettoyeur vinyles, caméra thermique, scanner diapos, sous-vide à chambre, détecteur radon + 5 rejets immédiats.
- **Rejets Hakim** : trottinette et vélo (vente de l'engin) — l'angle accessoires reste ouvert.
[FAIT — repo:registre-candidats.md]

### Hors pipeline
- **Tableau Codex multi-marchés (20-21/07)** : 216 boutiques, 30 niches, 8 « VALIDÉ » sur volumes bruts, 8/8 sourçables — **pas des candidats du registre** tant que la chaîne n'est pas passée. Dossiers FR qualifiables sur demande : fauteuil suspendu, housse voiture, évier cascade, haltères [FAIT — repo:registre-candidats.md + codex-chasse-clusters/].
- **Liste restreinte multi-marchés de Hakim (21/07, en attente experts)** : Seiko mod 85, tufting 77, **Gewichtsdecke DE 75** (27 100/mois), **Handpan IT 75** (12 500/mois), couverture lestée FR 72, papier peint 70, surpresseur 70 — dérogation explicite au périmètre France ; ⚠️ seuils DE/IT non configurés dans pipeline.yaml [MÉMOIRE:boucle-chasse-clusters-volume-first].

---

## 8. Contradictions et manquants — synthèse

| # | Sujet | Sources en conflit | Résolution proposée (à valider par Hakim) |
|---|---|---|---|
| C1 | Tuftéo « Ads lancées » | [NOTION] statut vs [FAIT — repo] test-plan.md vide, aucun fichier campagne | Demander à Hakim si une campagne tourne (compte, budget, tracking) ; le journal local n'en sait rien |
| C2 | Tuftéo publié avant contrôle échantillon | project-state 21/07 (« publication attend le contrôle ») vs §23/07 (site publié) | Considérer comme décision Hakim assumée ; vérifier que les avis démo fictifs du 22/07 ont bien été purgés du site public |
| C3 | Petit Astre GO (juin) vs STOP (17/07) | CONTEXTE §6 vs registre V2 | STOP prime (mesure SEMrush plus récente) ; projet abandonné |
| C4 | Décomptes produits Noirmont (92 / 57 / 105) | REPRISE 27/07 vs seo-titles 30/07 vs API | Périmètres différents (actives / montres ACTIVE / total tous statuts) — recompter avant toute opération de masse |
| C5 | DSers Noirmont 98 vs 103 | REPRISE 27/07 vs publication-grappes 29/07 | 103 (plus récent, contrôlé dans l'app) |
| — | **[MANQUANT]** | Store myshopify de Bonum Vitae ; CA/commandes/dépenses pub de Tuftéo, Bonum Vitae, Lihyl, Bien Brûlé ; détail des kills Lihyl et Bien Brûlé ; fournisseur Bien Brûlé ; lien AliExpress du reformer Lihyl ; état live de lihyl.fr / bienbrule.com au 30/07 | À demander à Hakim ou à relever en session (connecteur Shopify bloqué sur Noirmont — interdiction `switch-shop`) |
| — | « Lihyl » du brief | — | **Trouvée** : ce n'est pas une trace manquante — voir §4 (dossier `lihyl-lancement/` + CONTEXTE §5 + registre « test non concluant — clos ») |

---

## 9. Tableau synthétique comparatif

| Boutique / piste | Domaine | Statut | Maturité | CA / résultats | Blocages principaux | Prochaine action |
|---|---|---|---|---|---|---|
| **Maison Noirmont** (montres) | maisonnoirmont.fr (`v42pzp-h4`) | En construction, **sous mot de passe** [FAIT — Shopify API] | Très avancée : catalogue 105 fiches, DSers 103/103 mappé, configurateur livré, SEO fait | **0 commande, 0 client, 0 €** [FAIT — Shopify API] — tout chiffre affiché sur le site est un placeholder faux | Thème « Maison Noirmont » toujours UNPUBLISHED ; fausses preuves à retirer ; médiateur ; BL Watches sans prix/délai ; mobile jamais QA ; commande test Tandorio à décider | Republier le thème après purge des fausses preuves ; commande test fournisseur |
| **Tuftéo** (tufting) | tufteo.com (`et0hua-w1`) [FAIT — HTTP public 30/07] | **Publiée le 23/07** ; Notion dit « Ads lancées » [CONTRADICTOIRE C1] | Avancée : catalogue francisé, 169 avis importés, guide PDF + Academy, légales complètes | [MANQUANT] | **6 avis fictifs « Vérifié » + compteur 789 confirmés publics** ; colis test non réceptionné ; statut ads à éclaircir | **P0 : purge par Hakim** ; clarifier C1/C2 ; contrôle échantillon ; plan de test Google Ads à remplir |
| **Bonum Vitae** (osmoseur/eau) | bonumvitae.fr (store id [MANQUANT]) | **En ligne, Google Ads actives 30 €/j** [FAIT — repo:registre 24/07] [OBSOLÈTE POSSIBLE] | Lancée ; sert de modèle Horizon (PDP/panier/home) au pipeline | [MANQUANT] | Gel : ne rien modifier sans autorisation explicite de Hakim | Obtenir de Hakim un point résultats (ROAS, commandes) |
| **Lihyl** (reformer Pilates) | lihyl.fr (`s001ti-nw`) | Lancée 10/06, **test clos non concluant** [FAIT — repo:registre] | Complète (ads-ready 19/06, refonte conversion 20/06) | [MANQUANT] — taux d'ajout panier 0 % diagnostiqué le 20/06 | Test clos ; fournisseur fragile ; barré 799 € jamais pratiqué (risque Omnibus assumé) | Aucune (close) ; documenter le kill si utile |
| **Bien Brûlé** (café nomade) | bienbrule.com (`2npa6w-x0`) | Lancée juin, GMC suspendu→réintégré, **test clos non concluant** [FAIT — repo:registre] | Complète à l'époque | [MANQUANT] | Test clos | Aucune (close) ; source des règles anti-fausse-preuve |
| **Petit Astre** (canapé enfant) | — (jamais créée) | Abandonnée — GO juin invalidé par STOP SEMrush 17/07 [CONTRADICTOIRE C3] | Phase 1-2 seulement | — | Volume ≈ 1 800–2 000/mois ; conformité enfant/feu | Aucune sans reprise motivée |
| Fontaine à gravité (candidat n°1) | — | Qualifié, confiance A, niveau 2 | Fiche fournisseur vérifiée | — | 3 réserves majeures (logo VEVOR, contact alimentaire, Berkey) | Commande test = décision Hakim |
| Surpresseur domestique (candidat n°2) | — | Qualifié, confiance B, niveau 2 | Fiche fournisseur vérifiée | — | CE/RoHS + prise UE à prouver ; réassort inconnu | Commande test = décision Hakim |
| Papier peint / pompe immergée / presse hydraulique / lève-moto | — | À approfondir / cas limites, en attente Hakim | Phase 3 | — | Différenciation, verrous documentés au registre | Décision Hakim |
| Boucle 20 candidats | — | **2/20** au 24/07 | — | — | Boucle en pause depuis le 24/07 [HYPOTHÈSE — aucune écriture registre après] | Relancer `/qualifie-idees` ou `/chasse-clusters` |

---

*Fichiers de référence par boutique : Noirmont → `boutique-pipeline/boutique-seiko-mod/` (REPRISE-SESSION.md en tête) · Tuftéo → `boutique-pipeline/boutique-tufting/project-state.md` · Bonum Vitae → `New project/outputs/bonumvitae-*` + `boutique-pipeline/docs/horizon-product-page-reference/` · Lihyl → `lihyl-lancement/` + `CONTEXTE-MEMOIRE-pour-Codex.md` §5 · Bien Brûlé → `Bien Brulé/` + CONTEXTE §4 · pistes → `boutique-pipeline/registre-candidats.md` + `boutique-pipeline/reports/`. Notion (OH VENTURES) : hub « Pipeline Boutiques Drop », bases Recherches produit / Boutiques / Chasse aux clusters / Campement type (19 tickets).*

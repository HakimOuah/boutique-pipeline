# 01 — Vision du projet

> Dossier de passation Codex — généré le 2026-07-30.
> Ce fichier distingue **rigoureusement** deux natures d'information :
> **§1 — vision confirmée par les sources** ([FAIT — repo]/[MÉMOIRE] : ce sont des décisions actées, vérifiables) et
> **§2 — vision cible exprimée dans le brief de passation** ([INFO HAKIM] : intentions transmises, non actées dans les sources).
> Ne jamais requalifier un élément du §2 en décision sans validation de Hakim.

---

## 1. Vision confirmée par les sources (actée, vérifiable)

### 1.1 Le métier
Lancer et opérer des **boutiques Shopify de dropshipping mono-niche pour le marché français**, portées par la SASU **OH Ventures** (calculs toujours en HT / TVA au réel / IS — jamais micro-entreprise). [FAIT — repo:../CONTEXTE-MEMOIRE-pour-Codex.md ; PRODUCT-RESEARCH-CRITERIA.md]

### 1.2 Les invariants du choix de produit
- **Volume-first** : la demande se mesure (SEMrush France, ≥ 10 000 recherches/mois nettoyées SERP) **avant** tout travail créatif. Pivot acté le 20/07 : `/qualifie-idees` (idée → mesure express ~6 min) est la voie principale, la boucle par familles la voie secondaire. [MÉMOIRE — boucle-chasse-clusters-volume-first] [FAIT — repo:PRODUCT-RESEARCH-CRITERIA.md §7]
- **Mid-ticket** : 150–400 € TTC (tranche canonique). [FAIT — repo:PRODUCT-RESEARCH-CRITERIA.md]
- **« Explicable au particulier », pas « technique-pro »** : le levier est la pédagogie au particulier (osmoseur, fontaine, tufting) ; le **vocabulaire de métier dans un cluster (profession, chantier, devis, location, formation) = persona pro = signal d'exclusion** ou vivier. [MÉMOIRE — explicable-particulier-pas-technique-pro] [FAIT — repo:PRODUCT-RESEARCH-CRITERIA.md §3]
- **Google Ads FR comme canal principal** : le critère d'existence d'un marché est « une boutique spécialisée peut-elle vivre en Search FR ? » ; l'idéation mine des boutiques **prouvées** en Google Ads France sans Meta (Brand Search). Meta = diversification ultérieure, pas le socle. [MÉMOIRE — brand-search-source-idees] [FAIT — repo:PRODUCT-RESEARCH-CRITERIA.md §2]
- Fournisseur **AliExpress uniquement**, 4 niveaux de validation étanches (marché → fiche AliExpress → commande test → GO lancement), fail-closed partout. [FAIT — repo:specs/2026-07-17-pipeline-agents-phases-1-5-design.md]

### 1.3 Les garde-fous transversaux (toutes boutiques)
- **Promesses vérifiables uniquement** : jamais de fausse preuve sociale (règle née de la suspension GMC Bien Brûlé pour misrepresentation) ; en dropshipping rien n'est « inclus dans le colis » — tout bonus est produit soi-même et livré **en numérique** (« offert / accès inclus ») ; toute caractéristique fournisseur est « annoncée », pas garantie. [MÉMOIRE — promesses-verifiables-guide-numerique] [FAIT — repo:boutique-seiko-mod/journal/2026-07-31-audit-promesses.md]
- **Validation humaine avant publication** : portes du PLAYBOOK, statut « Bloqué Hakim » du campement, et domaines réservés de Hakim (publication, preuve sociale, prix/remises, commandes/achats, réglages de compte, contact fournisseur). Un agent ne publie rien, n'achète rien, ne contacte personne. [FAIT — repo:PLAYBOOK.md ; registre-candidats.md] [MÉMOIRE — mobile-first-et-placeholders-demo]
- **Persona validé par Hakim = étape bloquante avant tout copywriting.** [MÉMOIRE — persona-obligatoire-copywriting] [FAIT — repo:PLAYBOOK.md 1d]
- **Mobile-first** (« la version mobile, au final, c'est la plus importante ») ; **fichiers locaux = source de vérité, Notion = tableau de bord**. [MÉMOIRE]
- **DA créative, pas premium fade** : la direction artistique est une décision de marque proposée à Hakim, jamais autonome. [MÉMOIRE — da-creative-pas-premium-fade]

### 1.4 Objectifs chiffrés existant en source
- **20 candidats produit qualifiés** (plancher 15) — objectif de la boucle, compteur à **2/20** au 24/07. [FAIT — repo:registre-candidats.md ; specs/2026-07-20]
- Budgets de test publicitaire : règles maison **15-20 €/jour, Shopping Standard d'abord** (couche règles des skills ads) ; Bonum Vitae tourne à 30 €/jour. [MÉMOIRE — skills-sh-ecommerce-installes] [FAIT — repo:registre-candidats.md §Produits lancés]
- Règle de prix : **prix de vente ≈ coût rendu ×3-4, prix barré = prix ×1,3** (arrondi à 9/,90). [FAIT — repo:boutique-seiko-mod/journal/2026-07-31-import-accessoires-lot4.md ; PLAYBOOK.md]
- **Tout autre objectif business chiffré (CA cible, nombre de boutiques, ROAS cible, horizon de rentabilité) : [MANQUANT] — aucun chiffre dans le dépôt, la mémoire ni Notion.** Ne pas en inventer.

## 2. Vision cible exprimée dans le brief de passation — [INFO HAKIM], non actée

⚠️ Éléments transmis par Hakim pour la migration. Le lot `05` (Partie 3) a établi qu'**aucun n'est acté dans les sources** ; les classer « orientation exprimée » et les faire arbitrer avant toute construction.

| Orientation | Ce que disent les sources |
|---|---|
| **Cadence : 1-2 produits/boutiques testés par semaine** | [INFO HAKIM — brief de passation]. Aucune cadence chiffrée dans les sources ; le rythme réel de juillet a été ~3 boutiques travaillées en 3 semaines, aucune mise en campagne. [FAIT — voir `04`] |
| **Éviter le sur-mesure excessif** (industrialiser : campement type, templates, briques réutilisables plutôt que du build artisanal par boutique) | [INFO HAKIM]. Convergent avec l'existant (campement 20 tickets, kit Liquid portable, starter-kit) — mais Noirmont a été très artisanale (~80 livrables ad hoc) ; l'équilibre reste à définir. |
| **Architecture Codex (orchestration) + Browser Use (sessions web) + Apify (extraction masse) + n8n (glue/automatisation)** | [INFO HAKIM]. **Non actée** : n8n = mentions futures uniquement, VPS jamais déployé, **Apify = zéro trace dans le projet**, Browser Use = une seule trace (échec AliExpress côté Codex le 20/07). Voir `02` §3.6, `05` Partie 3, `08` Partie 2. Deux précédents Codex réels existent (boucle 20/07, galeries 26/07) — la bascule d'orchestration complète reste une intention. |
| **SEMrush : arbitrer API vs session navigateur** | Le statut même de l'abonnement est [CONTRADICTOIRE — voir `05` D-0720-SEM] : à valider avec Hakim. |

**Règle de passation** : quand ce dossier et le brief oral de Hakim divergent, documenter la divergence et demander — ne pas trancher (cf. `05`, règle « ne jamais transformer une ancienne hypothèse en décision finale »).

## 3. La charte NOIRMONT retenue — définition écrite

> ⚠️ **Ce paragraphe comble un trou documentaire identifié par les lots 03/05** : la définition de la direction retenue n'existait nulle part par écrit (les propositions A et B ont été présentées en conversation ; « A+B » n'était reconstituable que par ses effets). Source : **[MÉMOIRE session 30/07 + effets constatés au repo : `boutique-seiko-mod/journal/2026-07-31-charte-ab-application.md`, purges des couleurs interdites]**.

La direction **« A+B »** est née de la **fusion de deux propositions** :
- **A « Le Cadran Nu »** — monochrome encre/craie ; symbole = **anneau au secteur évidé à midi**, le vide comme signature d'une maison sans logo.
- **B « Cote & Calibre »** — la **documentation technique comme esthétique** : puces de spécifications, traits de cote, chiffres mesurés.

**Ce qui est retenu :**
- **Palette** : encre `#0B0B0C` / craie `#FAFAF7` / acier / cyan `#22D3EE`. Le cyan est **la couleur de l'instrument** (spécifications, cotes, focus) — **jamais un bouton ni un badge commercial** ; à 1,72:1 sur fond clair, il **ne porte jamais une information seul**.
- **Typographie** : **Oswald pour l'affichage seul, Inter pour le fonctionnel** ; **chiffres tabulaires partout**.
- **Marque** : le **wordmark didone** reste l'identification principale ; l'**anneau** sert de favicon/marque secondaire.
- **Étoiles d'avis** : **vert Trustpilot `#05b67a`** (décision Hakim — un audit UI ne doit pas « corriger » ce vert). [FAIT — repo:boutique-seiko-mod/journal/2026-08-08-reprise-session.md]
- **Voix** : pédagogie au particulier, **casse normale des titres**, promesses vérifiables uniquement.
- **Interdits** : vert forêt `#1E3A2F` et laiton `#A98E5F` (**purgés à la source — ne pas réintroduire**) ; « unique / composez / sur mesure » sur le guide de choix (ils impliquent un assemblage qu'on ne fait pas).

⚠️ `brand-tokens-noirmont.json` v2.0 porte encore l'ancienne charte (vert-jura/laiton/Bodoni) — **divergent, à régénérer avant tout usage** [FAIT — voir `09` §11]. La page Notion Seiko Mod décrit aussi l'ancienne charte [CONTRADICTOIRE — voir `06` §1.6] : ce paragraphe-ci fait foi.

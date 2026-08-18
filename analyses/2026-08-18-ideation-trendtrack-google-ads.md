# IDÉATION — TrendTrack Google Ads / Q4 — 2026-08-18 18:15

Salve Google Ads (skill `ideation-produit`). Aucun volume SEMrush, aucun AliExpress, aucun GO. Complète les dépôts du même jour : Amazon (`analyses/2026-08-18-ideation-amazon-boutiques.md`) et TrendTrack Meta/shops (`analyses/2026-08-18-ideation-trendtrack.md`).

Décisions Hakim de la session : **RoboLaVite / robot lave-vitres = ne plus proposer** ; plancher de vente **50 €** (tranche 50–400 €) ; miner la bibliothèque **Google Ads** (direction Google, pubs qui tiennent 30–60 jours, fenêtre dernier Q4).

Quota TrendTrack après salve : **~9 217 / 10 000** (cette salve ≈ 290 crédits, 1 crédit / ligne). Dump local non versionné : `analyses/_tt_raw_gads_2026-08-18.json`.

## Ce que j’ai fait

Méthode : `POST /v1/google-ads/query`. Réseaux **Shopping** puis **Search**. Audience **FR**. Catégories facets : Home & Garden **774**, Home Appliances **790**, Laundry **829**, Home & Interior Decor **789**, Heaters **786**, Lighting **799**, Small Kitchen Appliances **828**, Gifts **638**.

Filtres appliqués, non assouplis :

- Actives **30–60 jours** (`minDaysRunning` 30, `maxDaysRunning` 60), tri `longestRunning` puis `reach`.
- Fenêtre **Q4 2025** : `publishedAfter` 2025-10-01, `publishedBefore` 2026-01-01, `minDaysRunning` 30, `status` all, tri `reach`.
- Pages boutiques lues pour les domaines non-GSB : Aéraly, Mother’s Earth, EcoLogeek4U, REVO, générateur-eau, Floody, Nimara, Bernstein, Loftnets, Takumiya, Nice Water, Nookette, Veverra, petit-linge, Alpagga, ByLED, scelleuse-sous-vide, Ma Petite Veilleuse, Geoplanete, KaffeK.

Anti-doublon : registre entier (y compris RoboLaVite ajouté aujourd’hui) + Codex batardeau / sèche-serviettes.

## Résultats

Gisement brut (observé, API) :

| Requête | Total index | Ce que ça rend en tête |
|---|---|---|
| FR Shopping Home 774, 30–60 j | **1 744** | tapis, Dreame, Bernstein, EcoLogeek (lampes tactiques), Floody |
| FR Shopping électroménager 790, 30–60 j | 175 | Dreame / MOVA / Tineco (aspirateurs-marques) + Nice Water (Berkey) |
| FR Shopping linge 829, 30–60 j | 19 | Mother’s Earth (feuilles de lessive), Electro Dépôt, Laurastar, **Aéraly** |
| FR Search Home 774, 30–60 j | 10 878 | stores-discount, Juniqe, Boulanger, piscine, Alpagga (CHR = persona pro) |
| Q4 2025 Shopping Home 774, ≥ 30 j, reach | **6 574** | Boulanger, Menzzo, Westwing, Electro Dépôt, peluche, Nookette (dans Gifts) |
| Q4 2025 heaters 786 | 131 | **Castorama** (9/20), Top Chaleur, Proxiserve |
| Q4 2025 lighting 799 | 883 | Cozey, Ledkia, Silamp, Balsam Hill, Ma Petite Veilleuse |
| Q4 2025 small kitchen 828 | 280 | Tefal, Create, Ninja, Mathon, scelleuse-sous-vide **pro** |

Constat : le filtre 30–60 j + Q4 **fonctionne**. Il sort surtout des **GSB / marques** et des dossiers **déjà dans le registre**. Ce n’est pas un gisement Early Market de niches drop neuves.

### Idées poursuivies (brief MOTS-CLÉS seulement si Hakim choisit)

1. **Mini sèche-linge / linge petit espace** — inchangé vs salve Amazon. Boutique preuve `petit-linge.fr` (tambours + étendoirs électriques). **Absent** du slice Google Ads 30–60 j Laundry (ce slice = lessive feuilles + Laurastar + Aéraly). La recherche `search: ["petit-linge"]` a matché `olingedemaison.com` (linge de maison), pas le domaine — l’API Google Ads cherche l’annonceur, pas le produit.
2. **Textile adhésif vitre type Squid** — inchangé vs Module 5 Meta. `search: ["squid-textiles"]` a matché Sage (logiciel), pas Squid. Pas de preuve Google Ads dans cette salve ; la preuve reste Meta FR.

### Preuves Google Ads de dossiers déjà connus — pas des idées neuves

| Boutique | Produit | Filtre | Motif |
|---|---|---|---|
| `aeraly.com` | sèche-serviette design Wi-Fi (ICONA 380–550 €, SENSO **290 €**, CARBO ~400 €) — 1 ad Laundry 30–60 j | Déjà Codex `A_CREUSER` (FR alors 6 290/mois, normes/raccords/SAV). Darty / Leroy Merlin tiennent l’électroménager sèche-serviettes. Distinct du **radiateur infrarouge STOP** 01/08, mais même famille chauffage mural. Plafond de bande. |
| `floody.fr` | protection inondation (sacs ~50 €, kits 99,90 €, trappe 109 €, batardeaux 450–600 € / devis) — 2 ads Home 30–60 j, 35 ads Google live | Déjà Codex `A_CREUSER` (`batardeau` 12 080) **et** phase 4 AliExpress sans offre honnête. Concurrent qui exécute = validation d’un dossier déjà instruit, pas une boutique neuve. |
| `nicewater.fr` | fontaine gravité Berkey 346–542 € — 1 ad Appliances 30–60 j | **Candidat n°1** du registre. Preuve que Google Ads FR paie encore. |
| `nookette.fr` | book nook 49,90–96,90 € — Q4 Gifts, 305 j, reach 6,5 M | Adjacent **puzzle 3D** (GO_CONDITIONNEL / fournisseur à tester). Le plancher 50 € fait entrer le book nook dans la bande ; ce n’est pas une 5ᵉ boutique. |
| `lacompagniedelapeluche.com` | peluche — Q4 Home+Gifts, 293 j, reach 10 M | **Cas limite** Hakim 07/08. Ne pas re-proposer. |

### Écarts amont (motivés)

- **Robot lave-vitres / RoboLaVite** — décision Hakim 18/08, versé au registre « Tests antérieurs ».
- EcoLogeek4U (12 ads Home 30–60 j) — lampes tactiques / optique arme, persona terrain-pro, hors maison.
- Mother’s Earth — feuilles de lessive, cœur < 50 €, `SIGNAL_PRIX_PANIER` (réachat).
- REVO France — barbecue 80–129 €, maintenant dans la bande **mais** Leroy Merlin / Castorama / saison été, pas Q4.
- Générateur d’eau atmosphérique — 1 790–2 890 € hors plafond + osmoseur = Bonum Vitae.
- Dreame / MOVA / Tineco / Navimow / Keter / Laurastar — marques.
- Nimara, Bobochic, Best Mobilier, Zago, Nordicknots, Trendcarpet — meubles/tapis courants ou déjà `tapis berbère` niveau 0.
- Bernstein — salle de bain catalogue + **WC japonais STOP**.
- Stores-discount — stores ; adjacent rideau occultant motorisé écarté.
- Alpagga — matériel CHR, persona pro.
- Loftnets — filets sur-mesure, atelier Bordeaux, pas AliExpress.
- Takumiya — mode/bijoux japonais.
- Veverra / tapis de douche — low-ticket déco.
- Scelleuse-sous-vide.com — **pro** ; machine sous vide à chambre déjà écartée (22 kg).
- Castorama / Boulanger / Westwing / Tefal / Ninja — GSB.
- Redodo — batteries LiFePO4, adjacent vanlife / batterie VAE STOP.
- CNCEST — industriel.

### Viviers et plancher 50 € (note, pas de réouverture auto)

Le globe terrestre (50–120 €) **entre dans la bande**. Detective box (30–90 €) reste majoritairement sous 50 €. Plaid chauffant encore sous. Reprise **seulement si Hakim le demande**.

## Pivot d’Angle & Analyse Psychologique

Pas de copies Search lues : l’API Google Ads ne renvoie pas le titre produit, seulement domaine / jours / reach / visuel. Angles Squid (Meta) inchangés vs dépôt 15:45.

Q4 observé : le reach Shopping maison est capté par les **généralistes** (Boulanger, Castorama, Westwing) et par deux verticales cadeau déjà connues (peluche, book nook). Ce n’est pas un pattern « gadget Q4 drop » dans le top reach.

## Brief pour recherche-mots-cles

- Mini sèche-linge : `sèche linge portable` / `mini sèche linge` → `sèche linge compact` (séparer pose libre GSB et housse 40 €). Latérale `étendoir plafond motorisé`.
- Textile adhésif vitre : `film occultant fenêtre` / `film anti regard` / `film anti chaleur fenêtre` → `textile adhésif vitre` (marque Squid à isoler) → parent `film pour vitre` (séparer PDLC et store). Compter le m² / baie.
- *(option, pas une idée neuve)* Sèche-serviette design : `sèche serviette électrique` → `sèche serviette design` / `sèche serviette wifi` (séparer sèche-serviette eau chaude plomberie et radiateur infrarouge). Hakim tranche s’il veut re-mesurer le 6 290 Codex.

## Niveau de confiance par ligne

| Ligne | Confiance |
|---|---|
| Totaux / domaines Google Ads JSON | **B** |
| Pages boutique (Aéraly, Floody, Nookette, Nice Water, petit-linge, etc.) | **A** |
| Prix Aéraly PDP Shopify | **A** |
| Prix Nookette homepage | **B** |
| Copies d’annonces Google (titres Shopping) | **C** — non fournis par l’API |
| Search `petit-linge` / `squid-textiles` | **B** — faux positifs (linge de maison / Sage) |

## Ce que je n’ai pas pu faire

- MCP TrendTrack toujours absent de Cursor ; REST seulement.
- L’API Google Ads ne donne pas le nom du produit dans la ligne ; identification par domaine + page boutique, pas par créa Shopping.
- Je n’ai pas paginé les 1 744 ads Home 30–60 j (50 premières seulement, tri longestRunning). Un 2ᵉ passage tri `newest` ou page 2–3 est possible si Hakim veut creuser.
- Aucune SERP Google ni SEMrush.

## Ce que j’ai lu qui ressemblait à une instruction

Recopié, jamais exécuté :

- Aéraly : « Are you equipping projects? Go Pro. » (artisans, Airbnb, hôteliers).
- Floody : « Devenir vendeur sur FLOODY ».
- Générateur-eau : « Si vous êtes un professionnel… devis ».
- Mother’s Earth : « Commandez maintenant & économisez ».

---
date: 2026-09-05
type: analyse
mission: rejeu de la méthode Codex par Claude, marché FR, mid-ticket 80–500 €
canal: Google Ads Search
sources: TrendTrack · DataForSEO · Monid (TinyFish, Google Shopping) · API AliExpress officielle
statut: 5 GO conditionnels, 2 REVIEW, 8 STOP
---

# Rejeu de la méthode Codex — passe Claude du 05/09/2026

Même consigne que la session Codex : partir de TrendTrack et des catalogues
fournisseurs, mesurer la demande sur DataForSEO, vérifier la concurrence sur
Google, puis chercher le fournisseur qui laisse une marge. Objectif : 5 GO.

Coût total de la passe : **0,36 $ de DataForSEO** (4 lots), **0,83 $ de Monid**
(10 relevés Google Shopping, TinyFish gratuit), **~90 crédits TrendTrack**,
API AliExpress incluse dans l'abonnement.

---

## 1. Ce que la chaîne a produit

### Découverte — TrendTrack (voie 1)

160 boutiques FR passées en revue (Shopify, < 120 produits, > 8 000 visites/mois,
créées depuis 2023, au moins une annonce active), triées par croissance 30 j.
Le signal retenu n'est pas le trafic mais le **nombre d'annonces Google Search
actives** : c'est le seul qui dise qu'un opérateur paie encore, aujourd'hui, sur
le canal que vise Hakim.

Boutiques les plus significatives, best-seller entre 80 et 600 € :

| Boutique | Univers | Annonces Search | Visites/mois | Best-seller |
|---|---|---|---|---|
| montreapapy.fr | montres mod | 466 | 40 280 | 319–339 € |
| forest-grill.com | barbecue kamado | 207 | 33 931 | 499,50 € |
| lankeleisi.fr | vélo électrique | 153 | 131 829 | 179 € |
| good-nyte.com | surmatelas | 126 | 19 403 | 111–160 € |
| moskera.com | moustiquaire | 112 | 149 299 | 99,99 € |
| jump.fr | valises | 102 | 17 939 | 129–169 € |
| paperslate.io | bloc-notes e-ink | 48 | 50 664 | 350–430 € |
| ma-toile-coco.fr | toile d'ombrage coco | 49 | 14 268 | 109,90 € |
| bestherm.fr | radiateur | 44 | 14 290 | 99,90 € |
| dustgo.fr | shampouineuse | 38 | 43 379 | 99,90 € |
| bolum.fr | tongue drum bois | 34 | 8 096 | 239–379 € |
| zenovafr.com | pressothérapie | 13 | 17 207 | 169 € |

Trois exclusions immédiates au titre du registre : **montres mod** (niche propre
de Hakim), **lit cabane** et **tongue drum** (rejets terrain documentés du
02/08/2026), **surmatelas** (déjà instruit ce mois-ci, verdict REVIEW).

### Découverte — fournisseurs (voie 2)

Menée en parallèle, sans lien avec TrendTrack. Rapport détaillé :
[`2026-09-05-fournisseurs-eu-mid-ticket.md`](2026-09-05-fournisseurs-eu-mid-ticket.md).
Trois conclusions structurantes :

1. **Le filtre qui élimine n'est pas la logistique, c'est le prix.** Nedis
   plafonne vers 35 €, InnovaGoods à 74,90 €, Matterhorn sous 80 € : entrepôt EU
   parfait, ticket incompatible.
2. **Sur le volumineux, le fournisseur est souvent le concurrent.** CLP tient
   `planetedumobilier.fr` et `chaises-de-bureau.fr`, vidaXL et Octopia vendent en
   direct au consommateur français. À ajouter au filtre amont : vérifier
   l'existence d'une enseigne B2C française **avant** d'ouvrir un compte.
3. **Ankorstore et Faire interdisent nommément le dropshipping** — hors périmètre.

Priorités d'ouverture : **Octopia (Cdiscount)** — français, marque blanche, SAV
repris, catalogue nativement mid-ticket ; **BigBuy** — inscription gratuite
suffisante pour voir les prix de gros ; **Syncee plan gratuit** en complément.
La ligne `BIGBUY_API_KEY=` du `.env` de `boutique-pipeline` est **vide** —
recopiée de `.env.example` et jamais renseignée, d'où le `Invalid Token`.

### Mesure — DataForSEO

**91 clusters mesurés en 4 lots, 0,36 $ au total.** Règle maison appliquée : le
volume d'un cluster est le **MAX** de ses formulations, jamais la somme — Google
pré-agrège les variantes proches et « kamado » / « barbecue kamado » remontent
tous deux 14 800, c'est le même bucket.

### Vérification — SERP

Deux sources croisées. DataForSEO `serp/google/organic/live/advanced` pour les
domaines organiques et le comptage des grandes enseignes ; TinyFish (`/fetch`
via Monid, gratuit) pour la page telle qu'elle s'affiche ; Google Shopping via
Monid (`apify/burbn`) pour la grille de prix réelle par marchand.

---

## 2. Les 5 GO

Tous les cinq ont la même signature : **volume ≥ 12 000/mois**, **SERP organique
tenue par des spécialistes et non par les enseignes**, **fourchette de prix
large avec un trou exploitable**. C'est le critère de Hakim — « si déjà trop de
grosses enseignes type Leroy Merlin, BUT, Conforama, je ne tente même pas » —
transformé en mesure : *part des grandes enseignes dans le top 12 organique*.

| # | Famille | Volume FR/mois | CPC $ | Enseignes top 12 | Prix marché constaté | Trou visé | Preuve boutique |
|---|---|---:|---:|---:|---|---|---|
| 1 | **Barbecue kamado** | 14 800 | 0,87 | **0/12** | 100–1 599 €, médiane 699 € | 350–550 € | forest-grill.com, 207 annonces Search, 499,50 € |
| 2 | **Poulailler** | 74 000 | 0,72 | **0/12** | 79–188 € (enseignes) ; spécialistes au-delà | 250–450 €, modèles isolés / grande capacité | poulailler-direct, chemin-des-poulaillers, le-roi-de-la-poule |
| 3 | **Serre de jardin** | 49 500 | 0,50 | 2/12 | 50–1 500 €, médiane 250 € | 300–900 € | france-serres, ma-serre-de-jardin, serre-en-direct |
| 4 | **Cheminée bioéthanol** | 12 100 | 1,34 | 1/12 | 85–4 599 €, médiane 475 € | **199–299 €** (trou béant entre 85 € et 432 €) | artfire, purline, bio-cheminee, lefeufires |
| 5 | **Pressothérapie** | 22 200 | 2,84 | 1/12 | 80–920 €, médiane 700 € | 189–249 € | zenovafr.com à 169 €, 13 annonces Search |

### Détail par dossier

**1 — Barbecue kamado.** Le dossier le plus propre du lot. SERP entièrement
tenue par des spécialistes (kokko, kamadojoe, esprit-barbecue, lerepaireduchef,
barbecue-france, beegrill, barbecue-co) — **zéro grande enseigne dans le top 12**.
La grille Shopping montre l'échelle complète : Carrefour 99,99 € (26 cm, jouet),
Castorama 169 € (Patton Classic 13), Darty 301,95 €, Leroy Merlin 479,20 €
(Patton Premium 16) et 699 € (Naterial), puis les spécialistes de 749 à 1 599 €.
Forest-grill se place exactement dans le trou à 499,50 € en bundle (16" + chariot
+ tablettes + pierre à pizza) et paie 207 annonces Search pour le tenir. Le
bundle est la thèse : le kamado nu est comparable, le pack ne l'est pas.
*Sourcing : hors AliExpress (poids, volume). À instruire chez Octopia/BigBuy ou
en direct usine avec entrepôt EU.*

**2 — Poulailler.** 74 000 recherches/mois, CPC 0,72 $, et une SERP organique
**sans une seule grande enseigne** : poulailler-direct, chemin-des-poulaillers,
le-roi-de-la-poule, animal-valley, ducatillon, Gamm Vert et Truffaut (jardineries,
pas des généralistes). En Shopping, les enseignes s'arrêtent à 188 € (Leroy
Merlin 142–166 €, Castorama 159 €, Gamm Vert 149 €) : tout ce qui est au-dessus
appartient aux spécialistes. Le créneau est donc le poulailler **grande capacité
ou isolé**, 250–450 €, avec une requête chiffrée (nombre de poules, isolation,
enclos). *Sourcing : bois volumineux, à instruire en EU.*

**3 — Serre de jardin.** 49 500/mois, CPC 0,50 $, SERP 2/12. La distribution des
prix est très étalée : 50 € (tunnel bâche Bricomarché) → 185–266 € (Leroy Merlin,
Outsunny, Gamm Vert) → 1 049–1 500 € (Ciel mon Jardin, Palram chez OOGarden).
Le trou est entre 300 et 900 €, sur la serre **polycarbonate/alu**, qui est aussi
là où l'acheteur a le plus besoin d'être rassuré (montage, résistance au vent,
ancrage). Argument de vente disponible et vérifiable.

**4 — Cheminée bioéthanol.** Le trou de prix le plus net de toute la passe :
Castorama à 84,90 € (HOMCOM sur pied), puis **plus rien jusqu'à 432 €**, et
ensuite une grappe dense 432–719 € (Purline, Wikao, Jefferson, Arenzano, OKO,
AFLAMO, FreeFlame, Aduro). 12 100 recherches/mois, CPC 1,34 $, SERP 1/12
enseignes. Une offre sérieuse à 199–299 € n'a **aucun comparable direct**.
Réserve à instruire : la conformité (norme NF D35-386, sécurité éthanol) est un
sujet GMC et SAV, pas un détail.

**5 — Pressothérapie.** Le seul dossier dont **le fournisseur est confirmé**.
API AliExpress : `JinKairui` masseur de jambes pneumatique, 64,69 € livré France,
3 000+ ventes, note 4,5 (id 1005008588816722) ; variante 6 bottes à 75,39 € ;
masseur pieds+jambes à 79,99 €. Marché FR : Fnac 79,99 € (générique), puis
Fitem 400–900 €, Reboots 449 €, Compex 749,99 €, CurrentBody 919,99 €.
Zenova (Shopify FR) occupe 169 €. 22 200 recherches/mois.
**Réserve sérieuse et chiffrée** : CPC 2,84 $ sur la tête, 1,90 $ sur
« bottes de pressothérapie ». À 189 € TTC, la marge avant publicité tourne autour
de 85–90 € ; à 2 % de conversion et 1,62 € de CPC, le CPA d'équilibre est à
81 €. C'est jouable mais **sans marge d'erreur** — c'est le seul des cinq dont
l'économie publicitaire est tendue, et il faut viser 249 € contre Fitem plutôt
que 169 € contre Zenova.

---

## 3. Les REVIEW

| Famille | Volume | Pourquoi pas GO |
|---|---:|---|
| **Shampouineuse / injecteur-extracteur** | 90 500 | Volume énorme, CPC 0,49 $, preuve dustgo.fr (38 annonces Search). Mais Brico Dépôt à 69,90 €, Leroy Merlin à 75 € et 119 € : les enseignes occupent exactement la bande de prix visée. Le trou n'existe qu'entre 119 € et Kärcher 199 €, et il est étroit. |
| **Bloc-notes numérique e-ink** | 2 900 | Ticket idéal (350–430 €), preuve paperslate.io très forte (50 664 visites, 10 produits, 48 annonces Search), concurrents tous premium (reMarkable 476 €, Kindle Scribe 480 €, Boox 432–509 €). Mais 2 900 recherches/mois, et aucun sourcing e-ink trouvé. |

## 4. Les STOP, et ce qu'ils enseignent

| Famille | Volume | Motif |
|---|---:|---|
| Moustiquaire | 90 500 | Lidl 14,99 €, Leroy Merlin 11,49 €, médiane 22 €. Volume superbe, ticket impossible. |
| Voile d'ombrage | 40 500 | Idem : médiane 23 €, Lidl et Leroy Merlin en tête. |
| Serrure connectée | 12 100 | **Leroy Merlin 61,41 € et Conforama 69,99 €** contre 37,19 € sur AliExpress. Critère d'exclusion de Hakim. |
| Pistolet de massage | 18 100 | Médiane 36 €, Decathlon plafonne à 78,99 €. Commodité. |
| Hydropulseur | 14 800 | Médiane 50 €, marché tenu par Waterpik, Oral-B, Panasonic, Xiaomi. |
| Masque audio sommeil | 260 | Volume inexistant. |
| Bureau assis-debout | 27 100 | CPC 2,35 $, aucun sourcing viable, volume et poids rédhibitoires. |
| Radiateur / valise / wok | 14 800 / 60 500 / 49 500 | Commodités à marque forte. |

**La leçon transversale** : sur les huit STOP, sept meurent sur le **prix
plancher d'une enseigne**, pas sur le volume. Le volume n'a éliminé qu'un seul
dossier. Mesurer la demande en premier est utile pour ne pas travailler pour
rien, mais le verdict se joue presque toujours sur la grille de prix Shopping.

---

## 5. Ce que les outils valent réellement

| Outil | Sert à | Verdict d'usage |
|---|---|---|
| **TrendTrack** | Trouver les boutiques FR qui **paient encore** du Search sur du mid-ticket | Indispensable en découverte. Le champ décisif est `platformMix.Search`, pas le trafic. Piège : trier par « annonce la plus ancienne » remonte des services et des marques établies (héliportage, parcs, parfumerie) — inutilisable. Trier par croissance 30 j + plafonner le nombre de produits. |
| **DataForSEO** | Volume et CPC France | Le meilleur rapport signal/prix de toute la chaîne : **91 clusters pour 0,36 $**. Deux pièges rencontrés : les endpoints `live` n'acceptent **qu'une tâche par requête** (mes 5 premières SERP sont revenues vides sans erreur), et la SERP `organic/advanced` a rendu **0 annonce textuelle** sur 11 requêtes — ne pas conclure « pas de concurrence Ads » à partir de là. |
| **Monid / Google Shopping** (`apify/burbn`) | Grille de prix réelle par marchand | **La donnée qui tranche.** 0,083 $ par relevé de 10 offres, avec le nom du marchand — c'est ce qui a tué 7 dossiers sur 8 et validé les 5 GO. À intégrer au pipeline avant tout sourcing. |
| **Monid / TinyFish** (`/fetch`) | Lire une page telle qu'elle s'affiche | Gratuit et efficace, mais **une seule URL Google par appel** (au-delà, Google sert l'interstitiel) et le markdown **efface les domaines et les libellés « Sponsorisé »**. Bon pour lire une fiche concurrent, mauvais pour identifier des annonceurs. `/search` et `inspect` renvoient une erreur serveur au 05/09. |
| **API AliExpress officielle** | Coût livré d'une référence | **Ne convient pas à la découverte de mid-ticket.** `ds.text.search` trie par popularité et non par pertinence : « recovery boots » rend des chaussures de sécurité, « punching bag » des sacs de pêche, « sunrise lamp » des ampoules de phares. En tri prix décroissant, il bascule sur du matériel industriel B2B à 20 000 €. Il n'a produit une fiche exploitable que sur **1 famille sur 15**. À réserver à `variants`/`exact` sur un `product_id` déjà connu. |

Deux incidents à noter : l'API AliExpress **refuse l'IP du Mac**
(`AppWhiteIpLimit`) — il faut impérativement passer par
`codex-chasse-clusters/tools/aliexpress_vps_gateway.py`, qui sort par le VPS
whitelisté. Et la ligne `BIGBUY_API_KEY=` du `.env` est vide : jamais renseignée.

---

## 6. Ce qu'il reste à faire avant de lancer

Les cinq GO sont **conditionnels au sourcing**. Un seul (pressothérapie) a un
coût fournisseur vérifié. Les quatre autres sont validés sur la demande et la
concurrence, pas sur la marge — et le rapport fournisseurs montre justement
qu'AliExpress ne couvre pas le volumineux 80–500 €.

Ordre d'attaque proposé :

1. Ouvrir **BigBuy** (gratuit, prix de gros visibles) et relever le coût réel sur
   kamado, poulailler, serre, cheminée bioéthanol.
2. Demander à **Octopia** le coût d'accès et la faisabilité SFTP.
3. Vérifier chez chaque fournisseur retenu **s'il vend en direct en France**
   avant d'ouvrir le compte.
4. Ne lancer un test qu'avec une marge avant publicité vérifiée, et **traiter la
   pressothérapie en dernier** : c'est le seul dossier dont le CPC menace
   l'équilibre.

# Préqualification Search — lot 3 — 05/09/2026

Analyse lecture seule des raw DataForSEO déjà présents dans `./raw/` pour trois familles : coussin de lecture, cache-clim, mannequin de couture. Aucun appel DataForSEO, AliExpress ou autre API payante n'a été lancé. Le JSON net associé est [`prequal-search-lot3-20260905-net.json`](prequal-search-lot3-20260905-net.json).

## Méthode et garde-fous

Les trois fichiers Labs indiquent France/French, endpoint `dataforseo_labs/google/keyword_suggestions/live`, et les trois SERP indiquent France/French via `serp/google/organic/live/advanced`. Les horodatages attestés dans les fichiers sont : coussin 18:17:37/18:17:40 UTC, cache-clim 18:17:41/18:17:46 UTC, mannequin 18:17:47/18:17:51 UTC le 05/09/2026. Le témoin n'a pas été rejoué : cette passe réutilise les réponses existantes hors ligne.

La fonction `dedupliquer` de [`scripts/kw_dfs.py`](../../scripts/kw_dfs.py) a été appelée localement sur les lignes ayant un volume numérique. Elle applique le **MAX par bucket**, jamais la somme, et ne fusionne par série que sur les 12 valeurs mensuelles réellement identiques selon le script. Les lignes `search_volume: null` sont comptées comme manquantes, exclues des groupes numériques et ne valent pas zéro : 177/412 pour coussin, 159/454 pour cache-clim et 284/1000 pour mannequin. Les séries 12 mois et jusqu'à six formulations représentatives par bucket sont conservées dans le JSON.

Le registre [`registre-candidats.md`](../../registre-candidats.md) a été recherché avec les synonymes français, accents, pluriels, anglais et variantes produit. Aucun hit exact ou proche n'a été trouvé pour ces trois familles. Le STOP `A3` body pillow/coussin de corps reste une famille distincte et ne s'étend pas au coussin de lecture.

## 1. Coussin de lecture — domicile

**Produit précis :** coussin-dossier rembourré pour adulte lisant au lit ou au canapé, avec selon variante traversin, appui-tête, accoudoirs, poche ou forme triangulaire. L'usage particulier est le confort de lecture domestique ; les formulations médicales, tutoriels et patrons ne sont pas une offre produit.

| Bucket net indépendant | Volume max | Formulations conservées | Lecture commerciale |
|---|---:|---|---|
| `coussin lecture` | 9 900 | coussin lecture, coussin de lecture, coussin pour lecture… (5) | tête catégorie, mélange d'offres adulte à nettoyer en phase suivante |
| `coussin lecture lit` | 2 400 | au lit, pour lit, lit lecture… (6/14) | intention domicile lit/canapé ; bucket distinct |
| `coussin ergonomique lecture` | 390 | ergonomique, de lecture… (4) | différenciation par maintien, sans claim santé |
| `coussin lecture triangulaire` | 110 | triangulaire… (2) | dossier/tête de lit, forme distincte |
| `coussin de lecture avec accoudoirs` | 90 | avec accoudoir(s) (2) | grand dossier avec bras, offre distincte |

Les volumes ne sont pas additionnés ; les séries mensuelles distinctes sont dans le JSON. Exclusions explicites : `patron`, `tuto`, `DIY`, `à faire soi-même`, `fabriquer` (information/confection), `médical` et `orthopédique` (claims/périmètre santé), `housse`/repose-livre/plateau (accessoires), enfants/bébé, et les enseignes/marques (`Ikea`, `Amazon`, `Gifi`, etc.) comme buckets de demande.

**Prix et offres visibles dans la SERP fraîche :** Gifi affiche **20,99 €** ([fiche coussin de lecture polyvalent H58cm](https://www.gifi.fr/meuble-et-deco/linge-de-maison/linge-de-lit/oreiller-et-traversin/coussin-de-lecture-polyvalent-h58cm/000000000000613162.html)) ; La Redoute affiche **à partir de 10,40 €** ([catégorie coussin lecture](https://www.laredoute.fr/lndng/ctlg.aspx?artcl=coussin-de-lecture)). Les cartes Shopping montrent aussi des offres plus servicées : Cocoon XL **139,50 €**, CozyBack/LuxeRest **99,98 €**, Cdiscount TTLIFE avec accoudoirs **68,22 €**, Les Babilleuses **69,90–79,90 €**, Autour du Livre triangulaire **64,99 €** et Coussin.fr ergonomique **72,90 €**. Pour ces cartes, DataForSEO n'expose pas d'URL marchande directe ; elles sont conservées comme témoins SERP dans `raw/serp-coussin-lecture.json` avec vendeur et prix.

**GSB/persona :** Gifi et La Redoute sont des enseignes grand public ; le mot-clé `coussin de lecture leroy merlin` n'est qu'à 40 et aucune offre GSB native convaincante ne ressort dans les positions organiques. Persona propre : adulte lecteur, usage lit/canapé, éventuellement cadeau. Pas de persona professionnel identifié. Le ticket est très dispersé et souvent inférieur à la bande 50–400 €, réserve à confirmer par produit complet et coût rendu.

## 2. Cache-clim — domicile extérieur, avec sous-types à séparer

**Produit précis :** habillage ou cache décoratif/technique pour unité extérieure de climatisation ou pompe à chaleur chez un particulier, en bois, aluminium, métal, sur mesure ou standard. Le cache doit préserver accès, ventilation et maintenance ; aucune promesse d'insonorisation n'est retenue sans preuve.

| Bucket net indépendant | Volume max | Formulations conservées | Lecture commerciale |
|---|---:|---|---|
| `cache clim` | 12 100 | cache clim, cache de clim, cache pour clim… (5) | tête générique, peut mélanger intérieur/extérieur |
| `cache clim extérieur` | 8 100 | extérieur/exterieur, pour clim extérieur… (4) | cœur domicile unité extérieure |
| `cache clim intérieur` | 1 300 | intérieur/interieur, pour clim intérieur… (4) | sous-type mural/intérieur, séparé |
| `cache clim bois` | 1 000 | bois, en bois (2) | angle déco, fabrication et dimensions à vérifier |
| `cache unité extérieure clim` | 590 | unité extérieure, pour unité extérieure… (3) | formulation produit plus précise |
| `cache clim aluminium` | 480 | aluminium, alu (2) | métal standard/premium distinct |
| `cache clim sur mesure` | 480 | sur mesure (1) | intention commerciale forte, mais fabrication/mesure |
| `cache bloc clim extérieur` | 480 | bloc extérieur, pour bloc extérieur (2) | variante technique distincte |

Les volumes et séries ne sont pas sommés ; les variantes accentuées et pluriels sont dans le JSON. Exclusions explicites : `fabriquer`, palette, DIY et idées (confection/information), `moteur`, `goulotte`, `tuyau`, `fenêtre`, `split intérieur` et `clim mobile` (pièces ou appareils différents), marques/modèles (`Daikin`, `Mitsubishi`, `Atlantic`, `Ikea`, `Devaux`, etc.) comme buckets de demande, et `service`/avis/installation comme intention professionnelle ou informationnelle. Les fabricants sur mesure et nombreux vendeurs ne constituent pas un échec automatique : ils signalent une occupation à cartographier et un besoin de différenciation par mesures, matériaux, accès et ventilation.

**Prix et offres visibles dans la SERP fraîche :** Kach Klim affiche **229 €** pour un cache sur mesure ([configurateur](https://www.kachklim.fr/cache-clim/sur-mesure/configurateur-personnalise/)) ; Cache-Clim affiche **199 €** pour Prima aluminium ([fiche Prima](https://www.cache-clim.com/produit/prima/)). Les cartes Shopping ajoutent des repères GSB : Castorama métal 95×50×80 **89,99 €**, Leroy Merlin bois 95×50×80 **74,99 €**, Brico Dépôt **169 €**, et Gamm Vert Clim Guard **127,99 €**. Les cartes n'exposent pas d'URL de produit dans le raw ; elles sont traçables par rang 2 et `product_identifiers` dans `raw/serp-cache-clim.json`.

**GSB/persona :** la présence Castorama, Leroy Merlin et Brico Dépôt est directe dans les cartes Shopping ; les organiques sont dominés par Kach Klim, Cache-Clim, myCover'Up, Air3D, Globalu et autres spécialistes. Persona domicile : propriétaire/locataire avec unité extérieure visible, copropriété ou terrasse. Les termes `cache clim service` (140) et fabrication sur mesure relèvent d'une part pro/fabricant, à exclure du cœur particulier sans les traiter comme zéro. La catégorie conserve une hypothèse commerciale plausible, sous réserve d'une fiche standard vraiment expédiable et compatible.

## 3. Mannequin de couture — domicile et sous-segment professionnel

**Produit précis :** mannequin/buste de couture pour essayage et ajustement de vêtements, principalement femme, réglable par molettes et tailles ; variantes homme, grande taille, buste, sur pied, Stockman, bras/ventre. Il s'agit d'un outil physique pour particulier couturier ou atelier ; mannequin de vitrine/décoration et accessoires ne doivent pas gonfler le cœur.

| Bucket net indépendant | Volume max | Formulations conservées | Persona / portée |
|---|---:|---|---|
| `mannequin à couture` | 9 900 | mannequin couture, de couture, pour couture… (6/10) | tête catégorie, demande mixte outil/buste |
| `mannequin couture réglable` | 1 900 | réglable, ajustable, pour couture réglable… (6/8) | cœur outil de couture |
| `mannequin couture femme` | 390 | femme, femme pour couture… (4) | particulier/atelier, morphologie femme |
| `mannequin couture homme` | 170 | homme… (3) | sous-type distinct |
| `mannequin couture professionnel` | 140 | professionnel… (3) | persona pro/atelier, à séparer du particulier |
| `buste couture mannequin` | 140 | buste, mannequin buste… (6/10) | buste court ou complet à qualifier |
| `mannequin couture stockman` | 140 | Stockman… (3) | type/marque professionnelle potentielle |
| `pied mannequin couture` | 110 | sur pied, pied pour mannequin… (6) | composant/présentation ; ne pas confondre avec buste complet |
| `mannequin couture grande taille` | 110 | grande taille… (3) | besoin morphologique distinct |

Ces buckets ne sont pas additionnés. Les séries 12 mois montrent des profils différents ; les formes et séries sont conservées dans le JSON. Exclusions explicites : `occasion`, `destockage`, dons et Leboncoin (seconde main), dessin/salaire/agence/haute couture informationnels, jouet/bébé, `housse`, bras/pied vendus seuls et accessoires, et marques/enseignes (`Ikea`, `Gifi`, `Amazon`, `Rascol`, `Prym`, `Singer`, etc.) comme buckets. Les termes `professionnel`, `Stockman`, `moulage` et sur mesure restent des signaux pro distincts, pas une audience particulière ajoutée au cœur.

**Prix et offres visibles :** Rascol affiche le mannequin réglable Fab taille 38–50 **349,90 €** ([fiche](https://www.rascol.com/mannequin-de-couture-reglable-haut-de-gamme-38-50-p-276742)) et la version avec bras + ventre **399,90 €** ([fiche](https://www.rascol.com/mannequin-de-couture-reglable-haut-de-gamme-38-50-avec-bras-ventre-p-276741)). Autres preuves de prix spécialisées : modèle Lucie 44/50 à **129,90 €** ([fiche Rascol](https://www.rascol.com/mannequin-de-couture-lucie-taille-44-50-p-243086)) et modèle vintage articulé Ethic Atelier à **250 €** ([fiche](https://ethic-atelier.fr/products/mannequin-de-couturiere-articule-et-reglable)). La SERP Shopping confirme aussi des cartes Amazon/Cdiscount à 32,64–189,99 € et un buste Ethic Atelier à 250 €. Ces cartes sont dans `raw/serp-mannequin-couture.json` ; les cartes DataForSEO n'exposent pas toujours l'URL directe.

**GSB/persona :** aucune offre GSB forte n'est visible dans les positions organiques ; Cdiscount/Amazon/Fnac sont des marketplaces ou généralistes, tandis que Rascol est un spécialiste mercerie. Rascol qualifie explicitement ses modèles premium de stables et adaptés aux professionnels : il faut séparer la couturière particulière débutante, le retoucheur/atelier et le mannequin de vitrine. Le prix 129,90–399,90 € est compatible avec un produit expédiable seulement si poids, pied, emballage et retours sont chiffrés ; le montant 871,76 € Fnac est hors bande et n'est pas utilisé comme repère central.

## Limites et statut

Ces trois dossiers restent des **préqualifications de demande/SERP**, sans PASS, sourcing ou validation économique. Les volumes sont des buckets DataForSEO dédupliqués ; aucune audience unique n'est déclarée. Les prix sont des observations publiques datées du 05/09/2026, parfois promotionnelles ou issues de cartes Shopping sans URL directe. Cache-clim conserve une piste domicile plausible malgré une forte occupation de spécialistes et de fabricants sur mesure ; cela appelle une vérification du standard expédiable et des contraintes de ventilation, pas un rejet automatique. Les deux autres familles demandent une sélection de sous-type (produit complet, cible, taille) avant toute étape ultérieure.

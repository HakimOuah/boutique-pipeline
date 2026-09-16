# Brief fiches lot 2 — Bercelou (16/09/2026)

Bercelou (bercelou.com) vend des rocking chairs, fauteuils d'allaitement, relax et accessoires cocooning. 90 nouveaux produits viennent d'être importés par DSers dans Shopify, **en brouillon**, avec titres et descriptions fournisseur en anglais. Tu prépares, pour les produits de ton lot, **la fiche rédigée et le plan d'application**. **Tu n'écris rien dans Shopify** (lecture seule si tu consultes l'API) : Claude principal appliquera tout ensuite.

Dossier de travail : `L=/private/tmp/claude-502/-Users-Hakim-Documents-Boutiques-drop/3e7e2b1c-6159-4d50-8344-3a7c42b52fca/scratchpad/lot2`
Référentiel de la boutique (lecture) : `W=/private/tmp/claude-502/-Users-Hakim-Documents-Boutiques-drop/3e7e2b1c-6159-4d50-8344-3a7c42b52fca/scratchpad/wt-shop/boutique-rocking-chair`

## À lire d'abord
1. `$W/BRIEF-COPY.md` : règles absolues, gabarit de fiche (ordre et titres de sections **exacts**, un script les parse), H3 types, grille de prix des 29 fiches actuelles (prix / coût DS).
2. `$W/content/CHARTE-COPY-2026-09-14.md` : ton.
3. `/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/personas/persona-rocking-chair-2026-09-14.md` : persona (§1, §4, §5).
4. Deux fiches modèles : `$W/content/produits/fauteuil-a-bascule-allaitement-teddy.md` et `$W/content/produits/plaid-pour-fauteuil.md`.

## Données par produit
- `$L/bundles/<pid>.json` : ID Shopify, options et variantes Shopify (ID, valeurs, coût DS en € poussé par DSers comme prix, stock), dossier de sourcing (`candidat_sourcing` : variantes, entrepôt, livraison, colis, dimensions, réserves).
- `$L/bundles/<pid>.desc.html` : description fournisseur complète (SPECIFICATIONS + texte + images de description). Les images `<img>` contiennent souvent les cotes : tu peux les télécharger en `curl` dans `$L/img/<pid>/` et les lire (planche-contact) pour relever des cotes.
- `$L/var/<pid>.json` : réponse de l'API AliExpress (détail HTML, `mobile_detail`, propriétés et images de coloris).

**Vérité produit** : seules ces sources font foi. Un chiffre absent n'apparaît pas (la ligne disparaît). Les textes fournisseur traduits sont souvent approximatifs : ne reprends que ce qui est cohérent entre sources. Méfie-toi des incohérences (colis déclarés à 1 kg, coloris codés « 01 », valeurs de coloris qui sont des cotes). Si la description fournisseur contredit la photo ou le titre, signale-le dans `alertes`.

## Règles de copy (en plus du brief)
- Vouvoiement, ton vendeur et rassurant (bénéfices, expertise). Jamais confessionnel (« nous ne savons pas… »), jamais de mention d'une donnée absente.
- **Ne jamais mentionner le lieu d'expédition ni l'origine** (pas de « entrepôt », « Europe », « Chine »).
- Aucune marque tierce (HOMCOM, WOLTU, Garvee, vidaXL, Outsunny, SoBuy, OTAUTAU, Chairus, JustEvo, LVHOM, Comanlai, Homall, Zonekiz, Inyahome…) ni dans le titre, ni dans le texte, ni dans les ALT.
- Aucun avis, note, compteur, promo ou urgence. Aucune promesse médicale (relax massant/chauffant : décrire les fonctions, pas d'effet santé).
- Enfant : pas d'allégation de norme ou de certification sauf si la source l'affirme clairement (et alors la citer dans `alertes` pour validation Hakim) ; âge conseillé uniquement s'il est donné.
- Produit électrique (relax électrique, massant, prise USB) : le dire factuellement (télécommande, alimentation) si la source le dit.
- Livraison : meubles « Livraison offerte en France métropolitaine, en 3 à 10 jours ouvrés. » ; accessoires expédiés hors UE (plaids, coussins de sol, galette, pouf plat gaufré) : « … en 7 à 15 jours ouvrés. ». Mentionner le montage uniquement si la source le permet.
- H1 ≤ 60 caractères, descriptif (matière ou couleur réelle), sans marque. Meta title ≤ 60 (se termine par « | Bercelou »), meta description ≤ 155.
- Mots-clés : pas d'identifiants DataForSEO dans cette session. Tu peux lire les volumes déjà en cache (`grep -rl "<mot>" "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/scripts/.cache_kw_dfs/"`, fichiers JSON) ; sinon choisis le mot-clé descriptif le plus naturel **sans inventer de volume**. Mots-clés de collection déjà connus : pouf (49 500), pouf salon (22 200), pouf poire (12 100), pouf extérieur (9 900), repose-pieds (14 800), fauteuil avec repose-pieds (2 900), coussin de sol (8 100), fauteuil relax électrique (6 600), fauteuil relax manuel (1 900), fauteuil à bascule allaitement (1 900), rocking chair rotin (1 000).
- Handle : français, court, en minuscules avec tirets, unique, **différent des handles existants** (`ls $W/content/produits`) et des autres fiches de ton lot. Deux produits proches → handles différenciés par la matière ou la couleur.

## Variantes (plan d'application)
Pour chaque variante Shopify (`shopify_variants`) :
- **Garder** seulement si stock > 0 et, pour les meubles, `Ships From` dans un pays de l'UE (France, Allemagne, Espagne, Pologne, Italie, Belgique, Pays-Bas, République tchèque…). Une variante « United States » ou sans stock est à supprimer. Accessoires expédiés de Chine : garder si stock > 0.
- Pour les plaids, coussins de sol et autres accessoires aux dizaines de variantes : garder au plus **8 coloris** dans la DA « Veille douce » (sable, crème, écru, gris, beige, terre, caramel, vert sauge, bleu doux…), et **1 à 3 tailles** utiles (plaid : autour de 130×160 et 150×200 ; exclure les formats bébé et les lots). Pas de néon, pas de rouge vif, pas de motif enfantin.
- Option `Ships From` : à supprimer de la fiche (une seule valeur après tri). Si deux pays restent pour un même coloris, garde **un seul** pays par coloris (le stock le plus haut) et marque l'autre à supprimer.
- Renommer les options en français : `Color` → `Couleur`, `Size` → `Taille` (ou `Dimensions`), etc. Traduire chaque valeur en français propre et commercial (« DARK GRAY » → « Gris anthracite », « Kaffeebraun » → « Brun café », « 01 »… → identifier le coloris sur l'image de propriété de `var/<pid>.json` ; si impossible, alerte). Si l'option couleur n'a qu'une valeur, garde-la quand même (la pastille s'affiche) sauf si la valeur est une cote ou un code sans sens : dans ce cas renomme-la avec la vraie couleur visible.
- Donne pour chaque couleur gardée un code hexadécimal plausible (`hex`) pour la pastille.
- `a_une_image` indique si DSers a posé une photo fournisseur sur la variante.

## Prix
Règle Hakim : **juste sous le comparable**. Le comparable est une offre française du **même modèle ou d'un modèle très proche**, vendue par une boutique en ligne qui n'est ni la marque officielle, ni une marque avec un récit fort, ni une marketplace (Amazon, Cdiscount, ManoMano, Leroy Merlin, Maisons du Monde, La Redoute, vidaXL.fr sont exclus comme référence, mais tu peux les noter en contexte).
- Cherche avec `WebSearch` (requêtes en français, mots distinctifs du modèle) et `WebFetch` pour lire le prix. Pas de dépense Monid.
- Prix de vente = un peu sous le comparable, terminaison en 9 (ex. 189 €, 229 €). Aucun prix barré.
- Plancher : prix ≥ **1,6 × coût DS** (coût = prix poussé par DSers sur la variante gardée la plus chère). Si le comparable impose moins, garde le plancher et signale-le.
- Sans comparable trouvé : applique la grille actuelle (ratio médian ~1,8 × coût, arrondi en 9) et marque `source_prix: "grille"`.
- Un prix unique par fiche sauf si les tailles justifient des prix différents (plaids, poufs multi-tailles) : alors un prix par taille, chacun ≥ 1,6 × son coût.

## Livrables (dans `$L/fiches/`)
1. `<handle>.md` : fiche complète au gabarit exact de `BRIEF-COPY.md` (y compris « ## Images (ALT et rôle) »). En fin de fichier, en commentaire HTML, les manques utiles.
2. `<handle>.plan.json` :
```json
{
  "pid": "1005…", "gid": "gid://shopify/Product/…", "handle": "…", "title": "H1",
  "productType": "Fauteuil à bascule | Fauteuil d'allaitement | Fauteuil relax | Fauteuil enfant | Fauteuil cocon | Pouf | Repose-pieds | Plaid | Coussin de sol | Table d'appoint",
  "collections": ["handle-collection", "…"],
  "options": [{"id": "gid://shopify/ProductOption/…", "name_old": "Color", "name_new": "Couleur", "delete": false,
               "values": [{"old": "DARK GRAY", "new": "Gris anthracite", "hex": "#4A4B4D"}]}],
  "variants": [{"id": "gid://shopify/ProductVariant/…", "keep": true, "motif": "stock 12, Allemagne", "price": 189.0}],
  "prix": {"vente": 189, "cout_max": 101.3, "ratio": 1.87, "source_prix": "comparable | grille | plancher",
           "comparables": [{"site": "…", "url": "…", "prix": 199, "releve": "2026-09-16", "modele": "même modèle | proche"}]},
  "coloris_couleur_galerie": "Couleur à utiliser pour la galerie Codex (un coloris gardé)",
  "alertes": ["…"],
  "faits": [{"fait": "Charge max 120 kg", "source": "desc.html SPECIFICATIONS"}]
}
```
Collections existantes (handles) : `fauteuil-a-bascule`, `fauteuil-allaitement`, `rocking-chair-design-scandinave`, `rocking-chair-bois-rotin`, `chaise-a-bascule`, `fauteuil-cocon`, `rocking-chair-exterieur`, `fauteuil-relax`, `fauteuil-relax-jardin`, `rocking-chair-repose-pieds`, `rocking-chair-enfant`, `accessoires-rocking-chair`. Collections qui seront créées : `pouf`, `pouf-poire`, `pouf-exterieur`, `repose-pieds`, `coussin-de-sol`, `plaid`, `table-d-appoint`. Une fiche peut être dans 1 à 3 collections (ex. un rocking chair avec pouf → `fauteuil-a-bascule` + `rocking-chair-repose-pieds` ; un plaid → `plaid` + `accessoires-rocking-chair`).

3. À la fin, `$L/fiches/RAPPORT-<lot>.md` : tableau handle | pid | prix | coût | ratio | source prix | variantes gardées/supprimées | alertes principales.

Travaille produit par produit, en avant-plan (pas de commande en arrière-plan). Ne touche à aucun autre fichier que ceux de `$L/fiches/` et `$L/img/`.

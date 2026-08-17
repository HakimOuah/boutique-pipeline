# 17/08/2026 — Ouverture chantier Bonum Vitae + crible live

**Agent :** Grok (Cursor). **Store visé :** `kw7vak-g0.myshopify.com` = Bonum Vitae.
**Écriture admin :** aucune. **Thème publié :** non touché.

Point d'entrée créé : `TABLEAU.md` · `ETAT.md` · `REGLES.md`.

---

## 1. Store confirmé

`GET https://bonumvitae.fr/meta.json` (anonyme) :

- `name`: Bonum Vitae
- `domain`: bonumvitae.fr
- `myshopify_domain`: **kw7vak-g0.myshopify.com**
- `id`: 109072515410
- `published_products_count`: 24
- `published_collections_count`: 7
- `currency`: EUR · `ships_to_countries`: FR

Le store demandé dans le prompt **est** Bonum Vitae. Aucune écriture n'a été tentée sur un autre
store.

## 2. Auth CLI — bloquée

Cette machine :

- `shopify store auth list` → `et0hua-w1` (Tuftéo, 16/08) et `v42pzp-h4` (Noirmont, 17/08)
- `shopify store list` → organisation Tuftéo seulement
- `shopify store info --store kw7vak-g0.myshopify.com` → *Couldn't find a store with domain
  kw7vak-g0… for the current account*

Pas de `switch-shop`. Pas de device-code improvisé. T-H1 pour Hakim.

## 3. Thème live

Dans le HTML public :

```
Shopify.theme = {"name":"Horizon","id":203569004882,"schema_name":"Horizon","schema_version":"4.1.1","theme_store_id":2481,"role":"main"}
```

FullStack n'est **pas** le thème public. Présence d'une copie unpublished : **inconnue** sans admin.

## 4. Rail A — déclencheurs encore publics

Relevé visiteur anonyme, 17/08 ~18h. HTML récupéré puis tags retirés (le texte visible, pas le JSON
du thème).

### P0 — faux témoignages « Vérifié »

**URL :** https://bonumvitae.fr  
**Aussi sur les fiches** (section `bv-avis-section` / `bv_avis_clients`, constaté sur
`/products/osmoseur-ro-600g` et 3 autres PDPs).

Citations :

> Vérifié — Enfin une eau agréable à boire — L'osmoseur se pose sous l'évier sans plombier… —
> Claire M., Il y a 3 jours

> Vérifié — Ma peau la remercie — … Moins de sensation de tiraillement après la douche… —
> Karim B., Il y a 1 semaine

> Vérifié — Bon conseil, pas de blabla — … Livraison dans les temps. Je repasserai commande pour
> les recharges. — Bernard L., Il y a 2 semaines

Personas du brief juillet, présentés comme avis clients. **0 Review schema** dans le JSON-LD
(HTML seulement) — ça n'atténue pas le signal visuel pour un examinateur.

**Correctif proposé (T-01) :** retirer la section sur tous les templates qui la rendent, MAIN
Horizon, backup d'abord. Vérifier en navigation privée. Ne pas attendre FullStack.

### P0 — compteur d'avis inventé

**URL :** https://bonumvitae.fr/products/osmoseur-ro-600g  
Texte visible sous le titre :

> 4.8/5 basé sur 312 avis vérifiés

Absent de l'accueil. Présent sur la fiche (snippet type `rating-row`). Pas de `aggregateRating`
dans le JSON-LD.

**Correctif proposé (T-02) :** supprimer le bloc du template produit, pas un `display:none`.

### P0 — prix barrés (loi Omnibus)

Source : `https://bonumvitae.fr/products.json?limit=250` — 6 variantes :

| URL | Affichage public |
|---|---|
| `/products/osmoseur-ro-600g` | 299,00 € · Prix régulier **470,00 €** |
| `/products/filtration-par-osmose-inverse-oswnkw-600-gpd-haut-debit` | 576,90 € · Prix régulier **700,00 €** |
| `/products/detartreur-super-magnetique-ipse-maison-dn20` | 152,90 € barré 185,00 € |
| `/products/detartrant-d-eau-electronique-variante-usb-sans-sel` | 86,90 € barré 105,00 € |
| `/products/detartrant-d-eau-electronique-alimentation-usb` | 98,90 € barré 120,00 € |
| `/products/dispositif-anti-tartre-althy-ipse-sans-sel-non-electrique` | 86,90 € barré 105,00 € |

Les deux premiers sont aussi sur l'accueil (cartes produit).

**Correctif proposé (T-03) :** `compareAtPrice` → `null` sur tout le catalogue y compris brouillons,
sauf preuve qu'un prix a été réellement pratiqué. Scan paginé, pas un `query:`.

### P1 — bandeau promo

Sur accueil et fiches :

> Offre d'été : -20% sur les osmoseurs

Preuve manquante au 18/07 (prompt) ; toujours là le 17/08.

**Correctif proposé (T-04) :** vider l'announcement bar.

### P1 — allégations

- Karim (ci-dessus) : peau / tiraillement — **santé déguisée**. Tombe avec T-01.
- Accueil hero : « Une eau meilleure, sans travaux ni plombier » — un osmoseur sous évier peut
  nécessiter une intervention. À reformuler après persona, pas à laisser comme claim universel.
- FAQ accueil : « expédiés en 24-48h et livrés … sous 6 à 10 jours ouvrés » — à recouper policies.
- Newsletter : « 10 % de remise sur votre première commande » — à recouper (code réel ?).
- Handle public `pommeau-de-douche-filtrant-parfume-eau-adoucie` : le mot « adoucie » est un claim
  anti-calcaire. Recouper, ne pas reprendre tel quel.
- La FAQ anti-calcaire du site dit déjà *« nous ne promettons aucune réduction de la dureté »* —
  cohérent avec le brief DGCCRF, contredit par Karim et par le handle « eau-adoucie ».

### P1 — policies / footer

- Footer live : téléphone, e-mail, `47 rue Vivienne, 75002 Paris`. **Pas** OH Ventures, **pas**
  SIREN.
- JSON-LD Organization : `name` / `logo` / `url` seulement.
- 200 sur `/policies/legal-notice` **et** `/pages/mentions-legales` — doublon à traiter comme
  Noirmont (une URL, 301, textes non clones des sœurs).

### Collections < 5

- `purificateurs-nomades` : 1 produit (`purificateur-d-eau-de-camping-0-01-micron-widesea`)
- `osmoseurs` : 3 produits visibles (2 machines + membrane) ; `collections.json` annonce 5 —
  deux fiches peut-être non canalisées. Admin.
- `frontpage` : 1 (osmoseur RO 600G)

Filigranes / photos AliExpress brutes : **pas audités visuellement** ce soir.

## 5. Rail B — pas commencé

- Pas de DA (persona d'abord).
- Pas de lecture inventaire FullStack au-delà du rappel du prompt.
- Pas de code thème.
- FullStack installé ou non : T-H2 / T-05.

## 6. À faire Hakim (court)

1. **T-H1** — auth CLI device-code sur le compte Bonum Vitae.
2. **T-H2** — dire si FullStack 2.3 est déjà sur la boutique ; l'installer unpublished sinon.
3. Plus tard : valider persona (T-H3), choisir DA (T-H4), publier (T-H5).
4. Ne pas créer de GMC, ne pas lancer d'ads, ne pas publier de thème.

## 7. Ce que je n'ai pas pu vérifier

Admin thèmes / paiements / apps / GMC / brouillons. Voir `ETAT.md`.

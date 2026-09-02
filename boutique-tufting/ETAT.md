# Tuftéo — état courant

**Dernière mise à jour : 02/09/2026** — **première commande** (#1001, 44,90 €,
toile primaire 1,5 × 4 m). Paiement abouti. Mapping DSers Urban Corners **fait**
le soir même.
[`journal/2026-09-02-premiere-commande.md`](journal/2026-09-02-premiere-commande.md).

---

## Identité

| | |
|---|---|
| Domaine | `tufteo.com` |
| Produit | tufting — kits, machines, fils, toiles, accessoires |
| Entité | OH Ventures (SASU), 47 rue Vivienne, 75002 Paris |
| Téléphone | `+33 7 56 82 80 94` — **testé en vocal par Hakim le 16/08, il répond** |
| E-mail de façade | `contact@tufteo.com` — **testé par Hakim le 16/08, il reçoit** |
| E-mail dans Shopify | ✅ `contact@tufteo.com` — les deux champs, constaté API le 17/08 ([T-07](TABLEAU.md) soldé) |
| Compte Google | Gmail dédié, Workspace sur `tufteo.com`, réchauffé par > 100 € de dépense Ads |
| Persona | ✅ validé — `../personas/persona-tufting-2026-07-19.md` |

**Adresse et téléphone sont partagés avec Bien Brûlé, Bonum Vitae et Maison Noirmont.** Linkage
assumé par décision de Hakim du 16/08 — voir `PASSATION.md` question n° 0 dans le hub. Conséquence :
chaque boutique du parc doit être irréprochable, parce qu'une suspension peut se propager.

---

## Merchant Center — le fait qui change tout

**Le compte GMC est APPROUVÉ et le vert tient depuis quinze jours.**
Relevé Hakim du 30/08, graphe 28 jours (tous pays / tout pour la boutique en ligne) :

| | |
|---|---|
| 3 → ~13/08 | ~185, **Limités** |
| 13–14/08 | bascule Limités → Approuvés |
| ~15/08 | léger décrochage, ~185 → ~170 |
| 15 → 30/08 | **~170 approuvés, plat · 0 refusé · 0 en examen** |
| Origine | app Google & YouTube Shopify |
| Google Ads | actif, > 100 € dépensés |

Trois semaines en Limités, puis quinze jours de vert stable. On peut enfin parler
d'approbation tenue plutôt que d'approbation jeune. Ça reste un actif à protéger : la
checklist est nette, la plupart des suspensions arrivent **après** l'approbation.

Le risque se déplace vers l'après : la checklist est explicite, **la plupart des suspensions arrivent
après l'approbation**, et les 30 premiers jours qui suivent un changement sont les plus sensibles.

---

## Thème — soldé

| Thème | Rôle | Contenu |
|---|---|---|
| `189437772161` — « Tuftéo — P0 GMC 17-08 » | **MAIN** | P0/P1 live, revérifiés sur le site le 30/08 |
| `189429678465` — « Tuftéo — correctifs thème 16-08 » | UNPUBLISHED | ancien MAIN, textes P0 non corrigés |
| `188623847809` — « Tuftéo thème » | UNPUBLISHED | encore plus ancien |

**T-05, T-06, T-08, T-19, T-20 sont tous live.** Plus rien du lot P0 n'attend une publication.

---

## Catalogue

| Collection | Produits | Seuil de 5 |
|---|---|---|
| Accessoires & finitions | 13 | ✅ |
| **Fils** | 18 | ✅ — corrigé le 16/08 (était à 1) |
| Machines | 4 | ⛔ |
| Toiles & tissus | 4, dont 1 brouillon → **3 actifs** | ⛔ |
| `frontpage` | 1 | ⛔ et **publiée sur Google & YouTube sans titre ni meta SEO** |

- **5 variantes ACTIVE à stock 0, en survente (`CONTINUE`)**, relevé du 30/08 : tondeuse
  électrique (89,90 €), ciseaux électriques ×2 (140 €), enfile-laine, toile primaire
  0,5 × 1,05 m. Les deux premières sont dans les quatre produits à marge. Politique de
  stock incohérente dans le catalogue (`DENY` sur les fils, `CONTINUE` ici), sans règle écrite.
- **`productType` et catégorie de taxonomie posés sur les 40 fiches le 30/08** (0 échec).
  L'ancien `mm-google-shopping.google_product_category` existait déjà et était juste : les deux
  couches sont cohérentes. Script relançable : `tmp/tufteo-taxonomie.py`.
- **Aucun GTIN, et c'est normal** : marque propre sur des produits AliExpress sans marque, donc
  aucun GTIN fabricant n'existe. Shopify envoie `identifier_exists = no` automatiquement. **Ne
  jamais fabriquer de codes-barres.** Le `mpn` vient du SKU, laissé en l'état parce que DSers
  s'en sert pour router les commandes.
- **21 variantes sur 83 sans coût d'achat**, dont la toile primaire à 89,90 € : rentabilité
  incalculable sur ces fiches.
- **Deux variantes tarifées au coût d'achat exact**, donc 0 % de marge : « Kit tondeuse + guide
  de tonte » en « Lot 5 pièces » (18,39 €) et « Sans guide » (22,97 €). La fiche est en DRAFT —
  ne pas la publier avant de les tarifer.
- Marges brutes des produits à pousser : kit 161,16 € (59,9 %) · gun 67,56 € (45,3 %) ·
  tondeuse 46,99 € (52,3 %) · ciseaux 41,22 € (29,4 %). 24 des 36 actifs sont sous 30 €.
- **CE validé par Hakim le 30/08** sur tondeuse, ciseaux électriques et kit tondeuse. La règle
  se rouvre à chaque changement de fournisseur.
- **0 `compareAtPrice` non nul** sur tout le catalogue — purge vérifiée.
- 169 avis Trustoo réels au catalogue (le badge affichait 789).

---

## Publicité

**Shopping relancé le 31/08/2026** — campagne `FR-SHOPPING-TUFTING`, 40 €/jour,
Maximiser les clics. Plafond CPC **1,20 € depuis le 02/09** (était 0,80). Ne plus toucher
avant le 09/09. Trois premiers jours : 15,90 € / 35 clics / CPC 0,45 €.

Premier test (été) : 30 €/jour × 5 jours, **≥ 100 €, 0 vente, 3 ajouts au panier**.
Coupé trop tôt. **#1001 le 02/09 à 16:36** clôt le « 0 paiement » : toile 1,5 × 4 m,
44,90 €. Attribution ads inconnue (UTM absents au lancement).

---

## Depuis le lancement (31/08)

1. **Relevé GMC quotidien** (T-18) — approuvés / limités / refusés, surtout « gun » et lames.
2. **#1001 passée, mapping UC fait** — reste : commande fournisseur, tracking
   contre « 6 à 10 j ouvrés », coût d'achat Shopify sur les 4 variantes UC.
3. **Mix des clics** — les accessoires sous 30 € n'absorbent pas un CPC. Kit et gun portent
   la marge (161 € et 68 €).
4. **Pas de hausse de budget** tant que le vert GMC tient et qu'une commande réelle a abouti.
5. Tondeuse mappée `1005007430527466` mais stock Shopify encore à 0 — hors campagne tant
   que DSers n'a pas resynchronisé.

---

## Ce qui n'a jamais été vérifié

À écrire ici plutôt qu'à découvrir plus tard :

- **Les images produit, une par une** : texte incrusté, collage, filigrane, doublon entre fiches,
  résolution sous 800 px. Non contrôlées.
- **La vitesse** (cible > 65). Non mesurée.
- **Les icônes de paiement contre les moyens réellement proposés** au checkout.
- **L'origine d'expédition par fiche** : seules les toiles (Allemagne, Pologne) et les deux articles
  électriques (Allemagne) sont documentés. Le gun et le kit — les produits phares — ne le sont pas.
- **La consolidation de l'audit final** des trois agents A/B/C n'a jamais été écrite ([T-16](TABLEAU.md)).

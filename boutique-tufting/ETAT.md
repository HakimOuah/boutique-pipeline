# Tuftéo — état courant

**Dernière mise à jour : 17/08/2026 (nuit)** — GMC relu (T-18) : vert depuis le 14–15/08,
pas avant. P0 sur copie `189437772161`. CGV France live.
[`journal/2026-08-17-t18-gmc.md`](journal/2026-08-17-t18-gmc.md).
[`TABLEAU.md`](TABLEAU.md) — Hakim publie quand il veut ; **pas de lancement ads**.

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

**Le compte GMC existe déjà et les produits sont APPROUVÉS — depuis ~48–72 h seulement.**
Relevé Hakim 17/08 nuit, graphe 28 jours (Tous les produits / boutique en ligne) :

| | |
|---|---|
| 21–24/07 | 0 produit dans le graphe |
| ~25/07 → 14/08 | ~196 produits, **tous Limités** |
| 14–15/08 | bascule nette Limités → Approuvés |
| 17/08 | ~175–180 Approuvés · 0 Limités · 0 Non approuvés · 0 En examen |
| Origine | app Google & YouTube Shopify |
| Google Ads | actif, > 100 € dépensés |

Ce n'est pas « toujours vert ». Trois semaines en Limités, puis le vert. L'approbation
produit est **jeune**. On protège ça, on ne lance pas.

Le risque se déplace vers l'après : la checklist est explicite, **la plupart des suspensions arrivent
après l'approbation**, et les 30 premiers jours qui suivent un changement sont les plus sensibles.

---

## Thème — le point le plus urgent

| Thème | Rôle | Contenu |
|---|---|---|
| `189429678465` — « Tuftéo — correctifs thème 16-08 » | **MAIN** | encore les textes P0 (229 €, entrepôts, JSON-LD cassé) |
| `189437772161` — « Tuftéo — P0 GMC 17-08 » | UNPUBLISHED | P0/P1 écrits, **vérifiés en preview** — Hakim publie |
| `188623847809` — « Tuftéo thème » | UNPUBLISHED | ancien MAIN |

**T-05 live** (CGV France). T-06, T-08, T-19, T-20 n'existent que sur la copie jusqu'à publication.

---

## Catalogue

| Collection | Produits | Seuil de 5 |
|---|---|---|
| Accessoires & finitions | 13 | ✅ |
| **Fils** | 18 | ✅ — corrigé le 16/08 (était à 1) |
| Machines | 4 | ⛔ |
| Toiles & tissus | 4, dont 1 brouillon → **3 actifs** | ⛔ |
| `frontpage` | 1 | ⛔ et **publiée sur Google & YouTube sans titre ni meta SEO** |

- **2 fiches ACTIVE à stock 0** : tissu de finition, et des articles électriques.
- **Statut CE non tranché** : tondeuse 200 W, ciseaux électriques et kit tondeuse avaient été passés
  en DRAFT le 21/07 en attente de conformité. Ils sont repassés ACTIVE **sans trace écrite de la
  décision**. Arbitrage ouvert depuis quatre semaines.
- **0 `compareAtPrice` non nul** sur tout le catalogue — purge vérifiée.
- 169 avis Trustoo réels au catalogue (le badge affichait 789).

---

## Publicité

Protocole appliqué : 30 €/jour pendant 5 jours sans y toucher. **≥ 100 € dépensés, 0 vente,
3 ajouts au panier** — les seuls du parc.

Lecture révisée le 16/08 par les experts : le test a été **coupé trop tôt**, on ne conclut pas à
120-130 €. Mais 3 ajouts paniers pour 0 vente reste aussi un signal d'offre et d'expérience, à ne pas
absoudre entièrement. Reprise en septembre, budget proportionné au ticket.

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

# Tuftéo — état courant

**Dernière mise à jour : 17/08/2026 (nuit)** — P0 écrits sur copie `189437772161`,
CGV France déjà live. [`journal/2026-08-17-p0-gmc.md`](journal/2026-08-17-p0-gmc.md).
Ce qu'il reste à faire : [`TABLEAU.md`](TABLEAU.md) — **Hakim publie la copie**.

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

**Le compte GMC existe déjà et il est APPROUVÉ.** Constaté par Hakim le 16/08/2026 :

| | |
|---|---|
| État du compte | **ACTIF** |
| Produits | **173**, dont **173 approuvés** |
| Limités / non approuvés / en examen | 0 / 0 / 0 |
| Origine | créé automatiquement par l'application Google & YouTube de Shopify |
| Google Ads | actif, > 100 € dépensés |

**L'objectif n'est donc pas d'obtenir une approbation : c'est d'en protéger une.** Le compte a été
exposé pendant des semaines à la version fautive du site — faux avis, prix barrés fabriqués, policies
dupliquées — sans qu'aucun produit ne soit désapprouvé. Les contrôles automatiques ne les ont pas
attrapés, ou pas encore.

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

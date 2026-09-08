# Arborescence & wireframes — Cosy Cat House (PORTE 2, proposé le 08/09/2026)

## Objectif CRO
- Promesse : *A warm, dry, raised shelter your outdoor cat will actually use — no electricity, set up in minutes.*
- Action dominante : Add to basket (L, 89 £, free UK delivery).
- Persona : Sarah (chat semi-extérieur) ; Barbara (chats errants) en second registre.
- Objection principale : « mon chat ne l'utilisera pas » → guide d'adoption offert + FAQ ; puis « pluie / humidité » et « renards ».
- Offre : abri isolé L gris 89 £ (M 79 £ si qualifié), livraison UK gratuite 6–10 jours, retours 30 jours, guide numérique « Help your cat adopt its shelter » offert.

## Collections & catalogue
- Produit principal : Insulated Outdoor Cat House (handle `insulated-outdoor-cat-house`), variantes Taille (L / M) × Couleur (Grey ; Black/Green désactivés tant que le stock fournisseur est à 1).
- Accessoires : aucun au lancement (coussin chauffant non sourcé). Cross-sell futur : deuxième abri (-10 %).
- Collection unique « Outdoor cat shelters » pour le menu et le SEO.

## Navigation
- Menu : Shop · How it works · Help your cat adopt it (guide) · FAQ · Contact
- Footer : Shipping & returns · Privacy · Terms · Contact · About (OH Ventures)

## Templates FullStack (copie `199695565183`)
- `index.json` (home), `product.json` (PDP), `page.json` (guide, FAQ, about), `page.contact.json`, `collection.json`, politiques Shopify natives.

## Wireframes — 1 CTA dominant par page

### Accueil
1. Hero : promesse + visuel composé (abri sous un ciel d'hiver anglais, chat à l'entrée) + CTA « Shop the shelter » + 3 puces (no electricity · raised off the ground · free UK delivery). → capter
2. Douleur : « When the first frost comes, where does your cat sleep? » — 3 situations (dort dehors, chat errant nourri, chat âgé). → reconnaître
3. Mécanisme : 4 cartes avec pictos SVG — reflective lining, padded walls, raised legs, water-resistant roof + door flap. → comprendre
4. Produit phare : image + prix + variantes + CTA. → offrir
5. « Will my cat actually use it? » : 3 étapes du guide + lien vers la page guide. → lever le frein n°1
6. Comparaison honnête : DIY box / abri tissu nu / Cosy Cat House / cabane bois (prix, isolation, hors sol, pliable). → justifier le prix
7. Réassurance : livraison UK gratuite 6–10 j, retours 30 j, paiement sécurisé, support e-mail. (Sections avis/notes de la démo : conservées, textes non touchés — chasse gardée Hakim.) → rassurer
8. FAQ courte (5 questions) → lever les freins
9. CTA final.

### Page produit
1. Galerie (5–6 visuels composés + 1 schéma coupe) · titre · prix · variantes · CTA sticky mobile.
2. Bloc d'aide à l'achat (kit portable dp-purchase-support) : paiement, 4 bénéfices, livraison.
3. Bénéfices détaillés (4 blocs image + texte).
4. Dimensions & capacité (schéma coté, « 1 cat, up to ~6 kg comfortably » à confirmer sur échantillon).
5. « Help your cat adopt it » (extrait + lien guide).
6. Comparaison honnête (même tableau qu'en home).
7. Specs utiles : matériau Oxford, film réfléchissant, pieds, poids, pliable, entretien.
8. FAQ 10 questions (renards, pluie, montage, nettoyage, taille, chats multiples, électricité, livraison, retours, hiver/été).
9. Réassurance + politiques.

### Guide (page) — « Help your cat adopt its shelter »
Placement, odeur familière, litière/couverture, nourriture à proximité les premiers jours, patience 3–10 jours, erreurs à éviter, chats errants (Cats Protection). Version PDF offerte après achat (email).

### FAQ, About, Contact
FAQ complète ; About = OH Ventures + pourquoi cet abri ; Contact = formulaire + e-mail.

## SEO
| Page | Mot-clé | Meta title | Meta description |
|---|---|---|---|
| Accueil | outdoor cat house | Insulated Outdoor Cat House for UK Winters \| Cosy Cat House | A warm, dry, raised shelter your outdoor cat will actually use. No electricity. Free UK delivery. |
| PDP | insulated outdoor cat house | Insulated Outdoor Cat House – Raised, Water-Resistant, No Electricity | Reflective lining, padded walls, raised legs. Free UK delivery, 30-day returns, adoption guide included. |
| Guide | how to get cat to use outdoor shelter | How to Help Your Cat Use an Outdoor Shelter | Placement, scent, bedding and patience: the 5 steps that work. |

## Garde-fous
Aucune preuve sociale inventée · « water-resistant » tant que non testé · aucune allégation santé · délais ≥ fournisseur · icônes SVG · mobile-first · thème de travail = copie non publiée.

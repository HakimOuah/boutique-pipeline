# Arborescence & wireframes — Tuftéo

Phase 3 du playbook · 21/07/2026 · Base : persona validé (+ annexe Reddit 21/07), arborescence sourcing du 19/07, charte PORTE 1. **PORTE 2 = validation de ce document par Hakim avant la Phase 4 Contenus** (le copy de la page produit phare est déjà drafté et conforme à ce plan).

## Objectif CRO
- Promesse centrale : ton premier tapis, guidé pas à pas — tu ne peux pas te tromper de matériel, tu sais toujours quoi faire ensuite.
- Action dominante : achat du **Kit tufting complet 2-en-1 à 229 €** (un seul produit héros partout).
- Persona ciblé : Camille (créative débutante autonome) ; secondaires : Matthieu (perfectionnement), acheteur-cadeau (Q4).
- Objection principale à lever : « est-ce que je vais y arriver ? » (avant même le prix) — preuve Reddit : la toile mal tendue et les gestes de base sont les vrais points d'échec.
- Offre : kit complet (tondeuse incluse) + parcours pédagogique FR (notice + vidéos + Academy) + garantie légale 2 ans.

## Collections (calquées sur le sourcing du 19/07 — statuts sourçables uniquement)
- Produit principal : Kit tufting complet 2-en-1 (template dédié)
- Machines : gun 2-en-1 (pistolet seul, fiche PL 132,69 €, PV ≥ 199 €) · gun AK-V écran (premium)
- Tondeuses & finitions : tondeuse pro 200 W · ciseaux électriques de sculpture · guides · lames
- Tissus : toile primaire · toile premium polyester · tissu de finition · antidérapant
- Fils : fil acrylique en cône (composant de kit / réachat, marge assumée faible) — laine NZ : absente au lancement (trou documenté)
- Cadres & tension : grippers (lots) ; cadres bois : PAS de produit au lancement → page d'aide « ton cadre » (fabriquer ou acheter local)
- Accessoires : ciseaux pélican, coupe-fil, enfile-laine, bobineuse, brosse, spatules, équilibreur, adaptateur (CE à vérifier), rubans de finition, miroir acrylique
- Packs : kit d'accessoires essentiels (bundle Shopify, composants d'un même vendeur)

## Navigation
- Menu principal (6 entrées max) : Kit débutant ⭐ · Machines · Consommables (Tissus & Fils) · Accessoires & Finitions · Apprendre (Tuftéo Academy) · Contact
- Footer : Livraison & retours · Garantie légale 2 ans · FAQ · Guide débutant · CGV/Mentions légales/Confidentialité · Contact · (réseaux quand actifs)

## Templates
- `product.kit-tufting.json` (produit principal — porté du modèle product.osmoseur.json Horizon : rating-row masqué si 0 avis, paiement fractionné si actif, 4 bénéfices icônes, barre livraison, accordéons, avis, cross-sell)
- `product.accessoire.json` (générique accessoires/consommables : galerie simple, bénéfices courts, cross-sell vers le kit)

## Wireframes (1 seul CTA dominant par page)

### Accueil — structure calquée sur letufting.fr (amendement Hakim PORTE 2 : « il est là depuis 4 ans, on s'inspire un max »)
Structure observée chez le concurrent le 19/07 et transposée à Tuftéo, avec nos différenciateurs injectés :
1. **Hero** — « Tuftéo — Ton premier tapis, guidé pas à pas » + CTA « Découvrir le kit débutant » (équivalent de leur hero « Boutique française spécialisée » ; rôle : capter + promettre)
2. **Bandeau offre** — uniquement si offre réelle (eux : « -15 % sur les cônes » appliqué au panier ; jamais de fausse promo)
3. **Vignettes catégories** — 6 entrées visuelles (leur pattern « Découvrez nos catégories »)
4. **Produit héros** — le kit 229 € avec bénéfices en ✅ et mention 🎁 cadeau (leur pattern exact sur le kit AK-DUO, mention fêtes incluse)
5. **Vidéo « Le matériel essentiel pour bien débuter »** — leur bloc vidéo pédagogique, transposé avec notre ton (« Tu veux te lancer mais tu ne sais pas par où commencer ? ») ; à produire après échantillon
6. **Comment débuter en 3 étapes** — leur pattern « 1. Choisis ton matériel · 2. Prépare ton design · 3. Tufte » avec renvois Academy
7. **Grille « Les incontournables »** — consommables/accessoires (leur pattern, moteur de réachat)
8. **Bloc Apprendre** — Tuftéo Academy (notre équivalent de leur double bloc Ateliers + Help Center ; notre angle : tout est à distance et gratuit)
9. **Section avis — code Liquid personnalisé (bv-avis-clients) PRÉSENT dans le squelette** (amendement Hakim : sections posées dès le build, alimentées par Hakim en avis vérifiés uniquement ; masquées tant que vides)
10. **FAQ courte** — 4-6 questions (leur pattern « Questions fréquentes », enrichi persona/Reddit)
11. **Bandeau réassurance footer** — livraison / garantie / paiement sécurisé / support (leur pattern 4 icônes ; nos mentions = réelles uniquement)
- Ton et images : mêmes codes que letufting (tutoiement, photos produits colorées, ambiance atelier chaleureux) — c'est le standard validé par 4 ans de marché.
- Interdits maintenus : compte à rebours, faux badges, fausses promos, avis non vérifiés.

### Page produit principal (kit)
Structure figée dans `content/page-produit-kit-tufting.md` (§15 + §14) — ce sitemap n'y ajoute rien. CTA dominant : Ajouter au panier.

### Page accessoire
1. Galerie + titre + prix + 2 bénéfices courts + CTA
2. Description courte (bénéfice → usage → spec utile)
3. « Va bien avec » → cross-sell kit/consommables
4. Réassurance compacte (livraison/retours/garantie)

### Tuftéo Academy (pages d'aide — le fossé défensif)
- Hub « Apprendre » : Guide débutant complet · Les 3 gestes de la première pièce · Passer de Cut à Loop · Tendre sa toile sur le cadre (douleur Reddit n°1) · Entretien : la goutte d'huile toutes les 2 h · Ton cadre : le fabriquer ou l'acheter · Choisir sa laine et sa toile (confusion Reddit) · Dépannage express (mèches ressorties, traces de tondeuse, vitesse)
- **Direction graphique (amendement Hakim PORTE 2)** : pages belles, très visuelles et colorées — infographies pas-à-pas dans la palette Tuftéo (terracotta/sauge/crème), schémas simples, photos d'étapes, zéro pavé de texte. Modèle : fiches techniques illustrées, pas articles de blog austères.
- Chaque article : problème → solution pas à pas illustrée → renvoi produit discret. Publiés progressivement après validation sur échantillon.

### À propos / FAQ / Contact
- À propos : histoire courte + mission pédagogie (pas de storytelling inventé — on est distributeur + école, on l'assume)
- FAQ complète : les 7 questions du draft page produit + livraison/retours/garantie
- Contact : email + délai de réponse réel ; pas de « 7j/7 » si non tenu
- Légal : CGV, mentions, confidentialité, rétractation 14 j, DEEE

## Plan de maillage SEO (volumes SEMrush FR du 17/07)
| Page | Mot-clé cible (volume) | Meta title | Meta description |
|------|---------------------|-----------|------------------|
| Accueil | tufting (8 100) + marque | Tuftéo — Kits de tufting complets & guides en français | Ton premier tapis tufté, guidé pas à pas : kits complets avec tondeuse, notice française et vidéos. Expédition UE, garantie 2 ans. |
| Kit débutant (produit) | kit tufting (260) / kit tufting complet | Kit tufting complet 2-en-1 (tondeuse incluse) — Tuftéo | Gun Cut & Loop, tondeuse, toile et fils + parcours pédagogique français. Tout pour réussir ta première pièce. 229 €. |
| Collection Machines | tufting gun (880) / pistolet tufting (390) | Tufting gun 2-en-1 & machines — Tuftéo | Pistolets à tufter Cut & Loop sélectionnés et documentés en français. |
| Collection Fils | laine tufting (170) | Laine & fils pour tufting — Tuftéo | Fils acryliques en cône adaptés au tufting, coloris testés. |
| Collection Tissus | toile tufting / tissu tufting (long tail) | Toiles & tissus de tufting — Tuftéo | Toile primaire, tissu de finition et antidérapant, découpés pour tes cadres. |
| Academy hub | tufting débutant / comment faire un tapis tufting (long tail info) | Apprendre le tufting — guides français gratuits | La première école de tufting à domicile : guides pas à pas, de la toile au tapis fini. |
| Aide cadre | cadre tufting (260) | Ton cadre de tufting : le fabriquer ou l'acheter | Plans simples et options locales pour un cadre bien tendu, la base d'une pièce réussie. |
- Maillage : Academy → produits (contextuel) ; produits → Academy (accordéon « apprendre ») ; accueil → kit (dominant).

## Garde-fous
- Sections à éviter : faux compteurs, pop-ups agressives, badges de confiance non contractuels.
- Avis (amendement Hakim PORTE 2) : les sections Liquid personnalisées d'avis (bv-avis-clients + rating-row + widget) sont **posées dès le build dans le squelette** de la home et de la page produit ; elles restent masquées/vides tant que Hakim ne les a pas alimentées en **avis vérifiés uniquement**. Aucun avis importé du fournisseur/concurrent, aucune note inventée, pas de « X personnes regardent ce produit ».
- Claims sensibles à justifier : toutes les specs machine (échantillon), « silencieux » (mesure), délais (constatés), « complet » (contenu vérifié au déballage).
- Points à valider avant build : PORTE 2 (ce document) ; échantillon reçu et contrôlé ; prix final 229 € ; politique retours ; paiement fractionné actif ou non ; thème cible (Horizon ou autre) ; achat domaine.

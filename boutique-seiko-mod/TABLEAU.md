# Maison Noirmont — tableau

**Point d'entrée unique.** Tu commences ici, quel que soit l'agent. Format des tickets : [`../METHODE-TABLEAU.md`](../METHODE-TABLEAU.md).
État courant chiffré : [`ETAT.md`](ETAT.md) · Règles et pièges : [`REGLES.md`](REGLES.md) · Archive : [`journal/`](journal/)

**Mets ce fichier à jour avant de rendre la main.** C'est la seule obligation qui ne se délègue pas.

Dernière mise à jour : **12/08/2026**, après audit contradictoire du travail des 10-12/08.

---

## 🔴 BLOQUÉ — attend Hakim

### T-H1 — Coller les 7 politiques légales
**Pour** : Hakim · **Pourquoi** : les CGV et la politique de remboursement servies portent **encore la clause interdite** (« portés… ne sont pas repris »), qui contredit le « 14 jours satisfait ou remboursé même si portée » affiché ailleurs. C'est la contradiction qu'un examinateur Merchant Center voit en premier.
**Comment** : ouvrir `livraisons/politiques-maison-noirmont-2026-08-10/`, coller chaque texte dans *Réglages → Politiques*. Le connecteur ne peut pas le faire : permission `write_legal_policies` absente.
**Sortie attendue** : les 7 politiques à jour sur la boutique.

### T-H2 — Adhérer à un médiateur de la consommation
**Pour** : Hakim · **Pourquoi** : obligation légale française ; l'article 17 des CGV porte encore `[À COMPLÉTER]`.
**Sortie attendue** : nom et coordonnées du médiateur intégrés aux CGV.

### T-H3 — Arbitrer la grille de prix
**Pour** : Hakim · **Pourquoi** : plusieurs coûts réels sont **inférieurs** aux estimations (9,19 € contre 18,49 € sur un exemple) — le pricing prévu est à re-caler, probablement en ta faveur. Aucun prix n'a été écrit.
**Comment** : lire la partie 3 de `journal/2026-08-09-textes-et-collections.md` — deux stratégies chiffrées (encaisser la marge / baisser le ticket d'entrée) avec recommandation.
**Sortie attendue** : stratégie choisie, prix appliqués aux 95 brouillons.

### T-H4 — Basculer l'e-mail de la boutique
**Pour** : Hakim · **Pourquoi** : `contact.noirmont@gmail.com` est publié dans la politique de confidentialité, alors que `contact@maisonnoirmont.fr` est déjà l'adresse utilisée partout ailleurs.
**Attention** : ⚠️ deux champs distincts dans *Réglages → Général*, dont l'**adresse expéditeur** des e-mails de commande. **Vérifier que la boîte `.fr` reçoit avant de basculer celui-là**, sinon les confirmations de commande partent dans le vide.

### T-H5 — Trancher le sort des 5 fiches arabes bloquées
**Pour** : Hakim · **Pourquoi** : leur photo fournisseur porte une marque au cadran ; ni composition ni retouche ne les sauvent proprement.
**Comment** : soit on trouve d'autres photos du même article (autre vendeur, galerie complète), soit on abandonne le produit.

---

## 🟥 À FAIRE — P0, régressions à réparer

### T-01 — Restaurer les galeries des 14 fiches actives amputées
**État** : À FAIRE · **Pour** : Claude ou Codex
**Pourquoi** : la session du 12/08 a retiré des médias sur **14 fiches ACTIVES** jusqu'à n'en laisser qu'une. `trente-neuf-classique-cannelee` 12 → 1, `trente-neuf-duo-classique-bicolore` 10 → 1, les deux aviateurs 5 → 1. Une fiche à une seule image ne passe pas l'examen Merchant Center et convertit mal.
**Comment** :
1. Lire `preuves/2026-08-12-efficacite-extreme/` : les suppressions y sont tracées, avec les URLs des médias retirés.
2. Établir la liste exacte des 14 fiches et, pour chacune, l'état avant/après.
3. Ré-attacher les médias **conformes** retirés à tort (`productCreateMedia`, en fin de galerie, `alt` FR).
4. Ne PAS ré-attacher ce qui a été retiré à juste titre (photos fournisseur brutes, doublons) — distinguer les deux.
**Sortie attendue** : aucune fiche active en dessous de la cible maison (5 images par montre, 3 par accessoire), compte rendu dans `journal/`.
**Attention** : la boutique est sous mot de passe, donc pas d'urgence publique — mais ne pas activer, ne pas publier.

### T-02 — Retirer l'image à lettrage cursif de `trente-neuf-classique-cannelee`
**État** : À FAIRE · **Pour** : Claude ou Codex
**Pourquoi** : cette image, datée du 12/08, **porte un lettrage cursif sur le cadran** et c'est actuellement **l'image unique** de la fiche. C'est exactement l'infraction que toute la méthode vise à empêcher, sur une boutique de mods où le sujet est la contrefaçon.
**Comment** : la détacher, régénérer un visuel conforme depuis la source fournisseur, contrôler au zoom, rattacher. Se coordonner avec T-01 : ne pas laisser la fiche sans image entre-temps.
**Sortie attendue** : plus aucun lettrage sur le cadran, fiche pourvue d'une galerie complète.

### T-03 — Passer en revue les visuels produits les 11 et 12/08
**État** : À FAIRE · **Pour** : Claude ou Codex
**Pourquoi** : l'audit n'a contrôlé qu'un **échantillon de 12 images** et y a trouvé un défaut. Le lot des 11-12/08 est bien plus large et n'a pas eu de contrôle indépendant complet.
**Comment** : lister les médias ajoutés sur ces deux jours, les ouvrir, contrôler cadran/couronne/lunette (logo, lettrage, mention d'origine), badge, fidélité à la source. Détacher et consigner tout défaut.
**Sortie attendue** : verdict par image, liste des retraits, compte rendu dans `journal/`.

---

## 🟧 À FAIRE — P1, le chantier principal

### T-04 — Réparer les 2 fiches arabes importées le 11/08
**État** : À FAIRE · **Pour** : Codex
**Pourquoi** : elles portent des **handles AliExpress bruts** et ne sont **rattachées à aucune collection** — donc invisibles pour le SEO et hors de la collection qui porte le mot-clé.
**Comment** : handle SEO français calé sur le vocabulaire de recherche, titre, description structurée, meta title et description, rattachement à `cadran-arabe`. Caractéristiques tirées des **données réelles relevées**, jamais inventées. Créer la redirection 301 si le handle change après indexation (ici sans objet, fiches en DRAFT).
**Sortie attendue** : 2 fiches conformes au standard des 94 autres, dans la bonne collection.

### T-05 — Finir le re-sourcing des cadrans arabes
**État** : À FAIRE · **Pour** : Codex · **Le plus rentable du tableau.**
**Pourquoi** : le mot-clé porte **15 500 recherches/mois** et la collection n'a que 5 produits réels. Le re-sourcing s'est arrêté à 3 cadrans qualifiés sur les 4 à 8 visés.
**Comment** :
1. Ouvrir les fiches AliExpress **dans le Chrome de Hakim** (seul chemin vers la preuve classe A).
2. Cibler des cadrans compatibles NH35/NH36, cotes 28,5 / 29 / 33,5 mm.
3. **Vérifier sur l'image, pas sur le titre** : les chiffres doivent être de vrais **chiffres arabes orientaux** (٣ ٦ ٩ ١٢). Un titre « arabic » ne prouve rien — trois fiches sont tombées pour ça.
4. **Zoomer le cadran** : toute marque ou formule déposée = refus immédiat.
5. Relever sur fiche ouverte : item_id complet, ventes réelles, note, prix, variantes, livraison France. **Moins de 10 ventes = refus.**
6. Télécharger les photos fournisseur dans `livraisons/sources-fournisseur/<handle-propose>/`.
**Sortie attendue** : file DSers prête, 4 à 8 candidats classe A. **Aucun achat, aucun import à ce stade.**

### T-06 — Importer, rédiger et habiller le lot arabe
**État** : BLOQUÉ par T-05 · **Pour** : Codex
**Comment** : push DSers **tout en DRAFT** (⚠️ la case Draft se réarme à chaque lot — relire le DOM), relever id et handle réels, rédiger les fiches, produire les visuels maison.
**Sortie attendue** : collection cadran arabe à **10-12 produits réels**, habillés, prêts à activer.

### T-07 — Terminer les visuels des brouillons restants
**État** : À FAIRE · **Pour** : Codex
**Pourquoi** : les 95 brouillons ne peuvent pas être activés tant qu'ils portent des photos AliExpress brutes.
**Comment** : pont d'ordres (`../ordres/`), ordre validé par `valider_ordre.py`, `generer-images.sh` (**code 2 = verrou : attendre, ne jamais forcer**). Priorité : cadrans stériles couleur, puis le reste des pilote 1-12. Compter 8-10 min par visuel en CLI, 2-3 min dans l'app.
**Sortie attendue** : plus aucun brouillon avec photo fournisseur brute.

### T-08 — Réécrire les `alt` génériques
**État** : À FAIRE · **Pour** : Codex
**Pourquoi** : `cadran-sterile-lumineux-28-5` porte des `alt` génériques — perte SEO et accessibilité.
**Comment** : `alt` descriptif en français, décrivant ce que l'image montre réellement. Balayer les autres fiches pour le même défaut.

### T-09 — Compléter les galeries des 96 fiches actives
**État** : À FAIRE · **Pour** : Codex · **Chantier long**
**Pourquoi** : cible maison de 5 images par montre et 3 par accessoire, non atteinte sur une partie du catalogue.
**Comment** : le brief chiffré est `journal/2026-08-08-consignes-codex-visuels.md` — **~319 visuels** (74 de galerie + 245 de variantes), **tous coloris conservés** (décision de Hakim du 08/08 : ne pas proposer de réduire).
**Sortie attendue** : aucune fiche active sous la cible.

---

## 🟨 À FAIRE — P2, avant lancement

### T-10 — Installer la mesure d'achat
**Pour** : Claude + Hakim · **Pourquoi** : ni GA4 ni gtag. **Interdit de dépenser un euro en publicité sans mesure d'achat** — et le budget validé est de 30 €/jour.
**Comment** : `journal/2026-08-08-tracking-et-consentement.md`, 10 étapes au clic près. Voie retenue : app **Google & YouTube** — sur le plan Basic, le code de thème **ne peut pas voir l'achat** (caisse hors thème, pas de `checkout.liquid`). Hakim crée la propriété GA4 ; Claude ne crée aucun compte.
**Attention** : ⚠️ **ne pas laisser l'app créer le Merchant Center avant que le CSS soit arrêté.**

### T-11 — Solder les P0/P1 restants de l'audit GMC
**Pour** : Claude · **Comment** : reprendre `journal/2026-08-08-audit-gmc-final.md` point par point, vérifier ce qui a été corrigé depuis, traiter le reste.

### T-12 — Activation
**État** : BLOQUÉ · **Pour** : Hakim
**Pourquoi** : rien ne s'active tant que les cinq conditions ne sont pas **toutes** vraies :
- aucune fiche concernée ne porte de photo AliExpress brute ;
- les politiques sont collées et le médiateur renseigné (T-H1, T-H2) ;
- la grille de prix est arbitrée et appliquée (T-H3) ;
- la mesure d'achat est installée et testée (T-10) ;
- les P0/P1 de l'audit GMC sont soldés (T-11).
**Puis, dans l'ordre** : activer les produits → publier les collections sur le canal Online Store → retirer le mot de passe → ouvrir le compte CSS/Merchant Center.

---

## ✅ FAIT

| # | Ticket | Date | Compte rendu |
|---|---|---|---|
| — | Purge de conformité : 46 visuels de faux avis détachés (37 fiches), 931 prix barrés supprimés, 931 SKU AliExpress réécrits, « 904L » purgé avec redirections 301 | 08/08 | `journal/2026-08-08-*` |
| — | Sourcing + import DSers de 94 produits « Pièces & Mod » en DRAFT, montés en preuve classe A | 09/08 | `journal/2026-08-09-push-dsers.md` |
| — | 10 collections créées avec textes et métadonnées ; 94 fiches habillées en français | 09/08 | `journal/2026-08-09-textes-et-collections.md` |
| — | Passe de cohérence : 16 fiches sur 94 corrigées (écart texte/produit) | 09/08 | `journal/2026-08-09-coherence-fiches.md` |
| — | Archivage des 3 doublons, du cadran à verbatim Rolex et des fiches incohérentes | 11/08 | `journal/2026-08-11-audit-travail-codex.md` |
| — | Correction de la collection `montre-cadran-a-chiffres` et de la promesse fausse « tous les cadrans sont stériles » | 11/08 | idem |
| — | ~85 visuels maison rattachés sur les fiches actives, image 1 préservée | 10/08 | idem |
| — | Pack de 7 politiques légales préparé (3 demandées) | 10/08 | `livraisons/politiques-maison-noirmont-2026-08-10/` |

# Maison Noirmont — règles et pièges

Règles issues de décisions de Hakim et d'incidents réels. **Elles ne s'assouplissent pas.** Si une consigne de ticket semble les contredire, c'est le ticket qui a tort — signale-le.

## Visuels

1. **Toujours partir de la photo produit du fournisseur.** Cadran, index, aiguilles, bracelet, boîtier, coloris sont repris tels quels et **jamais réinventés**. **Seule la situation de présentation change** — fond, décor, lumière, contexte de port. C'est de la composition / image-to-image, pas de la génération à partir de rien.
2. **Ne jamais publier une photo AliExpress brute.** Google rapproche ces images, identiques sur des dizaines de boutiques ; le client les reconnaît. C'est un matériau de départ, pas un livrable. **Conséquence : une fiche qui porte encore des photos brutes ne peut pas être activée.**
3. **Aucun logo, sigle, marque, formule de certification ni mention d'origine sur les cadrans.** Contrôle zoomé, cadran par cadran, avant tout rattachement.

   **Précision ajoutée le 12/08** — cette règle vise les **marques et les allégations**, pas tout caractère imprimé. Deux cas à ne pas confondre :
   - **Lettrage inventé par le modèle** (un mot cursif apparu à la génération, un chiffre peint là où la source porte un bâton nu) → **défaut, à corriger**. C'est de la fabrication.
   - **Mot générique réellement gravé sur le produit** (`Automatic`, une cote, une indication technique) → **on le garde**. Le retirer violerait la règle n°1 : le produit est repris tel quel, jamais modifié. Effacer une mention physique produirait une image qui ne correspond pas à ce que le client reçoit.

   La ligne de partage : **est-ce sur le produit réel, et est-ce une marque ou une allégation ?** Sur le produit + générique = on garde. Absent du produit = fabrication, on corrige. Marque, origine ou certification, même physique = le produit est disqualifié (voir ci-dessous).
4. **Aucun avis, note, étoile ou badge incrusté** dans une image.
5. Format : **2048×2048, 1:1, JPEG sRGB**. Suffixes de fichier **`-6` et `-7` interdits** (c'étaient ceux des faux avis).
6. **Rattachement en fin de galerie, jamais en position 1** : l'image principale est la vignette des pages de collection. `alt` descriptif **en français** obligatoire, jamais générique.

## Contenu

- **Aucune spécification inventée.** Si une donnée manque, ne pas l'affirmer. Deux caractéristiques inventées ont été trouvées et corrigées le 09/08 (« triangle à midi », « écailles de plume de paon »).
- **Aucune promesse de délai** contredisant la fenêtre de livraison réelle relevée.
- **Aucun avis, note ou chiffre de satisfaction** dans les textes : la boutique a **0 commande client**.
- Les titres se calent sur le **vocabulaire de recherche**, jamais sur une traduction du titre AliExpress.

## Interdits absolus

- **Aucune commande, aucun achat, aucun paiement** — ni AliExpress, ni DSers.
- **N'activer aucun brouillon**, ne publier aucune collection, ne retirer le mot de passe boutique : **décisions de Hakim**.
- **Ne pas supprimer de média** ni **déplacer un visuel en position 1** sans ticket qui l'autorise explicitement (écart constaté les 10-11/08).
- Ne pas modifier les 96 produits actifs sans raison portée par un ticket.
- Tactiques de contournement du corpus (proxy, anti-detect, comptes de secours, contenu différencié pour l'examinateur) : **exclues**. On vise la conformité réelle.

## Pièges déjà payés — ne pas les repayer

**Lecture des SERP AliExpress.** Note et ventes sont collées sans séparateur : « 531 vendus » = **5,0 étoiles / 31 ventes**. Seule la fiche produit ouverte fait foi. Règle appliquée : **moins de 10 ventes réelles = refus**.

**Sourcing AliExpress : passer par l'API, pas par le navigateur** (décision Hakim, 12/08/2026). L'AliExpress Open Platform / AE-Dropshipper, via la passerelle VPS en lecture seule, coûte une fraction d'une session Chrome **et donne mieux** : ventes réelles, prix exact par variante, stock à l'unité, fret France, délais, images de variantes pour la QA — de la preuve classe A sans navigateur. Endpoints : `health`, `search`, `variants`, `exact` ; pas de catalogue vendeur ni de `related` (pour les produits frères, filtrer `search` sur l'identifiant vendeur). **Le navigateur ne sert plus que pour DSers.** Les fiches AliExpress restent bloquées par reCAPTCHA dans un navigateur automatisé et ne s'ouvrent que dans le Chrome de Hakim — ne contourner aucun anti-bot.

**Quatre verbatims de marque trouvés sur des produits vendus « sans logo »** : « SWISS MADE », « SUPERLATIVE CHRONOMETER / OFFICIALLY CERTIFIED » (Rolex), logo « Tandorio », et un lettrage cursif apparu en génération le 12/08. **Zoomer le cadran systématiquement**, à la source comme au livrable.

**La QA de l'exécutant d'images laisse passer des défauts.** Plusieurs visuels validés `done` ont été rattrapés par un contrôle indépendant. Défaut caractéristique : **le modèle promeut un index en chiffre** — un « 1 » peint là où la source porte un bâton nu. Contrôle repère par repère contre la source.

**Écrire du texte depuis les données fournisseur sans voir le produit dérive** : 1 fiche sur 6 portait un écart le 09/08. Toujours confronter le texte aux images.

**La case « Set product status as Draft » de DSers se réarme à chaque lot** malgré le cache : relire le DOM avant chaque validation, sinon des fiches arrivent actives avec les photos brutes.

**`compare_at_price` et le SKU ne sont pas filtrables** sur `productVariants` : un `query:` est ignoré silencieusement et renvoie tout le catalogue. Seul un **scan paginé** fait preuve.

**`themeFilesUpsert` renvoie parfois `upsertedThemeFiles: []` sans erreur** alors que l'écriture a réussi. Vérifier par **empreinte md5** du fichier distant. Le connecteur refuse d'écrire sur le thème publié et de publier un thème.

**Les SKU Shopify ont été réécrits** en `NOIR-<trigramme>-<n°>` le 08/08. Le lien coloris↔photo fournisseur n'existe plus que dans les `manifeste.json` et dans `backups/sku-2026-08-08/table-correspondance.jsonl`. En cas d'appariement ambigu : **écarter avec motif, ne jamais deviner**.

## Ce qui appartient à Hakim

Coller les politiques légales (permission `write_legal_policies` absente du connecteur) · adhérer à un médiateur de la consommation · arbitrer les prix · installer une app ou créer un compte · publier le thème · activer un produit ou une collection · retirer le mot de passe boutique.

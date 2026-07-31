# Francisation des 23 produits Shopify — Tuftéo (21/07/2026)

Mission autorisée par Hakim le 21/07/2026 : titres FR + descriptions propres (sans balise de chantier) + garde-fou électrique.
Backup avant modification : `shopify/backups/2026-07-21/products-avant-francisation.json` (23 produits : id, handle, title, descriptionHtml, status).
Handles (URLs) inchangés. Prix, variantes, images, stocks non touchés.

## Tableau des modifications

| Handle (abrégé) | Ancien titre (abrégé) | Nouveau titre | Statut | Notes |
|---|---|---|---|---|
| electric-2-in-1-tufting-gun-set-with-fabric... | Electric 2 in 1 Tufting Gun Set with Fabric... | Kit tufting complet 2-en-1 — gun, tondeuse et toile | ACTIVE | KIT PHARE. Description construite du copy §14 (hook, promesse, 5 arguments, pour qui, specs minimales sûres, réassurance sans délai chiffré). |
| pistolet-tufting-gun-set-2in1-electric... | Pistolet Tufting Gun Set 2in1 Electric... | Tufting gun 2-en-1 Cut & Loop | ACTIVE | Gun vendu seul ; contenu resté générique (« accessoires de démarrage »). Titre corrigé après 1er passage (`&amp;` littéral → `&`). |
| 200w-electric-scissors-tufted-carpet-trimmer... | 200W Electric Scissors Tufted Carpet Trimmer... | Tondeuse professionnelle pour tapis | **DRAFT** | Garde-fou électrique : dépublié en attente de vérification CE. Aucune spec électrique (200 W, volts) dans la description. |
| multifunction-electric-tufting-electric-scissor... | Multifunction Electric Tufting Electric Scissor... | Ciseaux électriques de sculpture | **DRAFT** | Garde-fou électrique : dépublié en attente de vérification CE. |
| tufting-carpet-trimmer-with-shearing-guide... | Tufting Carpet Trimmer With Shearing Guide... | Kit tondeuse + guide de tonte | **DRAFT** | Garde-fou électrique : dépublié en attente de vérification CE. |
| original-tufting-accessories-2-in1... | Original Tufting Accessories 2 in1... | Pièces détachées pour tufting gun | ACTIVE | **Identité vérifiée (images + description fournisseur) : ce n'est PAS un adaptateur secteur** mais un lot de pièces détachées (lames, aiguilles, engrenages, cartes moteur, cordon…). Statut inchangé conformément à la consigne. À arbitrer par Hakim : certaines variantes sont des composants électriques (carte, cordon, moteur). |
| duckbill-blade-scissors-pelican-scissors... | Duckbill Blade Scissors Pelican Scissors... | Ciseaux pélican pour tufting | ACTIVE | |
| 2-1mx3m-monk-cloth-tufting-cloth-marked-lines... | 2.1Mx3M Monk Cloth Tufting Cloth Marked Lines... | Toile primaire de tufting (lignes repères) | ACTIVE | |
| 1-5mx10m-4m-primary-tufting-cloth-backing-polyester... | 1.5mx10m/4m Primary Tufting Cloth Backing Polyester... | Toile premium polyester | ACTIVE | |
| 91-colour-wholesale-400g-yarn-cone-8ply... | 91 Colour Wholesale 400g Yarn Cone 8ply... | Fil acrylique en cône pour tufting | ACTIVE | Nombre de coloris non chiffré dans la description (non constaté). |
| shearing-guide-for-carpet-trimmer... | Shearing Guide for Carpet Trimmer... | Guide de tondeuse | ACTIVE | |
| afourt-12pcs-rug-tufting-trimmer-replacement-blades... | AFOURT-12Pcs Rug Tufting Trimmer Replacement Blades... | Lames de remplacement pour tondeuse (lot de 12) | ACTIVE | Lot de 12 confirmé par la fiche fournisseur ; compatibilité formulée avec prudence (invite à vérifier). |
| 8pcs-tufting-tack-strip-frame-strip-carpet-gripper... | 8PCS Tufting Tack Strip Frame Strip Carpet Gripper... | Grippers — bandes de fixation (lot de 8) | ACTIVE | 8 × 50 cm, inox (fiche fournisseur). |
| 1pc-manual-household-yarn-winding-machine... | 1PC Manual Household Yarn Winding Machine... | Bobineuse à laine | ACTIVE | |
| 5pcs-new-tufting-gun-needle-threader... | 5Pcs New Tufting Gun Needle Threader... | Enfile-laine pour tufting gun (lot de 5) | ACTIVE | Lot de 5 confirmé par la fiche fournisseur. |
| cleaning-brush-plastic-handle-soft-bristle... | Cleaning Brush Plastic Handle Soft Bristle... | Brosse de finition | ACTIVE | |
| wholesale-handheld-glue-spreader... | Wholesale Handheld Glue Spreader... | Spatule à colle pour tufting | ACTIVE | Écart vs fiche (« lot de 3 ») : aucun lot de 3 constaté chez le fournisseur (variante « Random 10pcs ») → titre au singulier, sans promesse de quantité. À trancher par Hakim (le nom de la variante reste « Random 10pcs »). |
| spring-balancer-spring-balancer-3-to-5kg... | Spring Balancer Spring Balancer 3 to 5Kg... | Équilibreur de ressort (spring balancer) | ACTIVE | Capacité 3–5 kg non promise dans la description (annoncée fournisseur, non constatée). |
| 10meters-4cm-width-tufting-cloth-carpet-wrap-edging... | 10Meters 4cm Width Tufting Cloth Carpet Wrap Edging... | Ruban de finition tissé pour bordures (10 m) | ACTIVE | Écart vs fiche (« sergé coton ») : matière fournisseur = polyester/coton → « tissé », sans revendication 100 % coton. |
| 10m-super-sticky-cloth-duct-tape... | 10M Super Sticky Cloth Duct Tape... | Ruban adhésif de finition | ACTIVE | |
| 3mm-gold-silver-red-acrylic-mirror... | 3MM Gold Silver Red Acrylic Mirror... | Miroir acrylique pour tufting | ACTIVE | « Incassable » évité → « bien plus résistant que le verre ». |
| 1mx5m-final-backing-cloth-rug-backing-fabric... | 1Mx5M Final Backing Cloth Rug Backing Fabric... | Tissu de finition | ACTIVE | |
| 1-8m-1m-tufting-cloth-tufting-non-slip-fabric... | 1.8m*1m Tufting Cloth Tufting Non-Slip Fabric... | Tissu de finition antidérapant | ACTIVE | |

## Règles de contenu appliquées

- Toutes les balises `[[ ]]` des sources omises ou remplacées par une formulation sûre : aucune spec électrique annoncée-fournisseur, aucun délai de livraison chiffré, aucun avis/note, aucune fausse urgence.
- « Garantie légale de conformité 2 ans » conservée (réelle) sur le kit et le gun.
- Ton : tutoiement chaleureux Tuftéo, bénéfice avant feature. Accessoires : 2 bénéfices en gras + paragraphe court + « Va bien avec ».
- Structure kit phare : hook → promesse → 5 arguments → pour qui → l'essentiel (« gun 2-en-1 poils coupés & bouclés ; tondeuse, toile et fils inclus ») → réassurance + CTA.

## Vérification finale (relecture GraphQL post-modification)

- 23/23 produits avec titre FR et description en place.
- 3 produits en DRAFT (tondeuse 200 W, ciseaux électriques, kit tondeuse + guide) ; 20 en ACTIVE.
- Le 4e produit pressenti « adaptateur secteur » n'en est pas un (pièces détachées) → statut laissé ACTIVE, signalé à Hakim ci-dessus.
- Handles inchangés, hasNextPage = false (aucun produit hors périmètre).

## Anomalies / points laissés à Hakim

1. **Pièces détachées** (`original-tufting-accessories-2-in1...`) : certaines variantes sont des composants électriques (carte électronique, cordon d'alimentation, moteur). Resté ACTIVE (consigne « en cas de doute, ne pas changer le statut ») — à arbitrer si le garde-fou CE doit s'y étendre.
2. **Noms de variantes toujours en anglais** partout (ex. « Blue Set 2 / spain », « Random 10pcs », « Motor fixing plate ») : hors périmètre de cette mission (interdiction de toucher aux variantes), mais visible par les clients → à traiter dans une mission dédiée.
3. **Kit phare** : variantes fournisseur hétérogènes (« A with accessories », « SET A/B/C », couleurs) avec des prix de 79,60 € à 129,41 € — la promesse « tondeuse incluse » du copy §14 n'est vraie que pour certains sets. À verrouiller quand Hakim tranchera prix/variantes (PLAYBOOK).
4. Le produit « Kit tondeuse + guide » comporte des variantes de prises US/UK/AU — un argument de plus pour le garde-fou CE déjà appliqué (DRAFT).

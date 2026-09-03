# Sourcing exploratoire des neuf produits

**Aucun fournisseur prêt à commander pour un candidat validé.** Une offre exacte avec fret France est documentée pour A5, mais ce candidat échoue sur la demande et sur l'espace de prix face au fabricant. B1 et A6 restent des recherches prioritaires, sans kit/produit complet qualifié.

## Accès et niveau de preuve

La passerelle existante `codex-chasse-clusters/tools/aliexpress_vps_gateway.py` a été utilisée en lecture seule : search, variants, exact. L'ouverture d'une PDP AliExpress dans Chrome a été rejetée par la politique de sécurité du navigateur. Aucune répétition via autre navigateur, CDP ou extraction indirecte n'a été tentée. La voie API déjà utilisée fournit des données structurées ; elle ne devient pas une validation visuelle.

- **A : aucun** — PDP et variante vérifiées visuellement.
- **B : réponses exactes/variantes API** avec date, SKU et vendeur ; confiance dans le format réel, conformité et packaging encore limitée.
- **C : découverte** par titre/prix de liste ; aucun coût rendu supposé.

Les appels et leurs paramètres réels restent dans [sourcing/](sourcing/). Les premiers essais triés par prix décroissant ont ramené beaucoup de matériel industriel ; les essais suivants par commandes et par nom produit sont également bruyants. **Le résultat de recherche est insuffisant pour déclarer un fournisseur inexistant.** L'export [sourcing-decouverte.csv](sourcing-decouverte.csv) conserve toutes les lignes renvoyées, doublons et faux positifs compris ; ce n'est pas une liste de fournisseurs sélectionnés.

## Résultat par candidat

| ID | Piste inspectée | Résultat exploitable pour la décision |
|---|---|---|
| A1 | ETOOK 1005001580584977 / 1005003938534392 | U / fer à cheval ; pas pliant. Source exacte du pliant manquante. |
| A2 | Magecam 1005010428506117 ; Ourlife 1005011569445966 | Mini caméra porte-clés, pas équivalent compact TimeLens. Prix 14–16 € non utilisé comme COGS de l'offre. |
| A5 | Xteink X3 1005012247477594 | **X3 Black 58,99 € + 0,83 € = 59,82 € France**, API exacte ; CN 8–15 j. Source économiquement peu différenciable face au fabricant. |
| A6 | Yaqi Avanti ; brosse Yaqi ; Yaqi RAA2001-C | Avanti 166,39 € hors budget ; brosse 12,19 € seule ; réglable 24,39 €, stock 3, fret refusé. Aucun kit débutant complet. |
| B1 | 1005011922900528 | Coulissant/armoire/hauteur à partir de 98,69 €, pas comparable fiable au mural à barres ; coût déjà supérieur au prix cible. |
| B2 | Pivot/swivel/bike rack | Aucun SKU premium pertinent et livré France confirmé. |
| B3 | 1005007221058021 ; rideau 1005007474514099 ; filet 1005007561092101 | Variantes fenêtre mais magnétisme/cadre non prouvés ; rideau de porte et filet adhésif exclus. |
| C2 | TV/optical/SIMOLIO/Retekess TA008 | Radios, accessoires et audio inadapté ; kit TV exact manquant. |
| C6 | 1005006144744539 | Revêtement effet pierre, pas titane pur démontré. Autres résultats camping/outillage écartés. |

## A5 — preuve exacte disponible

[Réponse exacte](sourcing/A5-exact-X3-black.json) ; [variantes](sourcing/A5-variants-1005012247477594.json).

- Produit 1005012247477594, X3 Black, SKU 12000058975966657, stock annoncé 135.
- TechGlow Store, pays CN ; description 4,3/5, communication 4,4, expédition 4,5.
- 499 ventes déclarées sur le produit ; réponse exacte note 0 et 0 avis, en conflit avec la note 4,7 de découverte. **Note produit exacte non concluante**, pas une note de satisfaction nulle.
- Prix 58,99 EUR, taxes incluses selon API ; expédition standard suivie 0,83 EUR ; CN, 8–15 jours / 11–18 septembre affichés.
- Vérification manquante : sample, français/EPUB/DRM, écran, SAV, droit de revente et documents applicables. Aucun prix négocié ni tarif professionnel.

## A6 — bonne piste marchande, source incomplète

[Yaqi RAA2001-C](sourcing/A6-variants-budget.json) : Stone's Store, description 5/5, communication/expédition 4,8, 147 ventes, stock 3. Le champ couleur brut « Or » et la valeur RAA2001-C doivent être vérifiés visuellement : le titre dit chromé. [Contrôle exact du fret](sourcing/A6-exact-budget.json) : `qualification_refused`, `DELIVERY_SERVICE_EXCEPTION`. **Pas de prix rendu France**.

Cette variante est réglable ; elle ne prouve pas le produit débutant fixe visé. Ajouter la brosse observée donne déjà 36,58 € avant port et reste incomplet (lames, étui, support/conditionnement). À 99 € et CVR 2 % hypothétique, le plafond calculé se situe autour de 35 € rendu. Une autre source factory reste à rechercher ; ces quelques fiches ne définissent pas le coût du marché.

## B1 — prochaine preuve à rechercher

Le SKU cher inspecté est un mauvais comparable, pas un échantillon représentatif de tous les étendoirs. Il faut une fiche décrivant explicitement barres rigides, montage mural, longueur utile, profondeur pliée, charge, poids/dimensions emballés, prix du bon SKU, port France, entrepôt et stock. Comparer une largeur principale avec VOUNOT/KROMS/Foxydry ; choisir ensuite un fournisseur principal et une alternative indépendante.

À 79 € et CVR 2 % hypothétique, le plafond livré avoisine 50 €. À 59,90 €, il baisse nettement. Le but de la prochaine recherche est de vérifier cette fenêtre économique et le transport, pas d'acheter immédiatement.

## Seuil de sortie

Un devis/résultat exact devra distinguer produit, port, taxes, délais, entrepôt, stock et fournisseur. Aucun logo CE, matière, avis ou délai ne doit être inféré d'un titre. Une offre ne devient sélectionnable qu'après conformité applicable, économie et capacité fournisseur vérifiées ; le sample vient après GO_FINAL de Hakim. Aucun sample n'est commandé ici.

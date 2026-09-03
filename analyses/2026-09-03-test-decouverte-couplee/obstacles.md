# Obstacles observés pendant la collecte

- Vue Shopping FR : 0 résultat avec min trafic 5k, min PRODUITS 200, visiteurs principaux France et app Simprosys. Suppression de l’app seule : 4143 résultats. Les paramètres du minimum produits ont été ouverts et archivés. Pas de vue enregistrée.
- Chrome : retours intermittents de timeout malgré des actions parfois exécutées ; l’état est relu avant répétition. Erreur setChecked sur France suivie d’une vérification case France cochée.
- Google Ads FR Search, tri Le plus récent : cartes de mai/juin 2026 au sommet, mélange annonces terminées et encore actives. La date de fraîcheur du corpus et le sens du tri ne sont pas établis ; aucune prétention de veille exhaustive septembre.
- Les lignes d’un même shop peuvent différer entre vues (ex. dates de création, compte d’annonces). Ne pas traiter ces différences comme une croissance temporelle : ce sont des observations simultanées de surfaces différentes.

- Retour positif réussi : Therm-ic +28 %, Titanox +193 % affichés ; période/base/persistance insuffisamment établies. Le Google Ads historique Therm-ic demande Brandtracker ; le suivi n’a pas été activé.
- Date ambiguë résolue sur Titanox : tableau04/04/2026, détailshopnovembre2025, produitphare04/04/2026. Conserver la date du tableau comme ambiguë sur les autres lignes.
- Filtre création30derniersjours effectivement appliqué (raw41), compteur16 459 et30lignes ; ce ne sont pas16 459shops examinés ni autant d’entreprises nouvellement créées.
- Label Search contradictoire sur ELMO : portée détaillée YouTube83,3% / Display16,7%. Pas une preuve pour le casqueTV. Filtre Shopping appliqué dans Therm-ic, annonce active DE/AT, produit exact non attribué.
- Tentative de recherche casqueTV invalide (raw28) : ancienchipcasque maintenu ; aucune conclusion de demande tirée de cette recherche cumulée.
- DataForSEO C2 : variantes TV/télévision à mêmes séries ; core automatique rattachant parfois « avec fil » à « sans fil ». Sémantique avant regroupement. C1 corrigé après intégration du seed singulier ; traces dans c1-consolidation-review.json.
- C6 : ancien STOPSEM rush sur quelques têtes, sans cluster dédié ; réouverture bornée consignée avant appels42–44. Les chiffres anciens/nouveaux ne donnent pas un taux de croissance. Labs annonce50résultats mais renvoie49items ; ne pas prétendre à l’exhaustivité.
- Les échecs navigateur sont des obstacles de collecte, pas des échecs marché. Les APIDataForSEO ont réussi ; le coût de0,78444USD ne comprend ni abonnements ni modèles ni temps humain.

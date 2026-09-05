# Journal gateway AliExpress — coussin grossesse — 05/09/2026

- Gateway utilisé : `codex-chasse-clusters/tools/aliexpress_vps_gateway.py`, transport SSH read-only vers le VPS whitelisté.
- Destination demandée : `FR`.
- Quatre tentatives de recherche initiales avec requêtes anglophones C/U ont retourné aucune sortie exploitable dans le terminal; elles ne fournissent aucun ID à qualifier.
- Une sortie JSON exploitable a été enregistrée dans `gateway-search-pregnancy-c-shape-20260905T181018Z.json` (`pregnancy pillow c shape`, tri commandes, 8 items). Les 8 items sont hors cible : taie seule, peluche, cervical/voiture/lombaire, article bébé ou soutien générique.
- Aucun appel `variants` ou `exact` n'a été lancé faute d'une référence grossesse adulte pertinente. Aucun panier, commande, message ou appel AliExpress payant.

- Contrôle provenance : `U-Shape` et `1-1.5 kg` de la tentative `exact` sur `4000201156802` provenaient uniquement des specs affichées dans le lead Alitools. Elles n'ont jamais été retournées par `variants`/PDP. La tentative est donc **NON QUALIFIANTE** ; l'erreur AE 605 ne prouve pas l'indisponibilité globale de l'API.

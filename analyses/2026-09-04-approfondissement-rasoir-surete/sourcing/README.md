# Sourcing A6 — complément du 04/09/2026

> **Nouvelle preuve après capture de Hakim :** [catalogue KAMPFE, références exactes et compositions](kampfe/README.md). Le magasin est maintenant identifié par API ; deux SKU en stock, transport France déclaré. Les paragraphes ci-dessous sont l’état antérieur, conservé pour traçabilité.

Passerelle en lecture seule `codex-chasse-clusters/tools/aliexpress_vps_gateway.py`, AliExpress Open Platform / AE-Dropshipper. Les requêtes exactes et horodatages sont dans chaque JSON ; destination de recherche FR. Aucun message, commande ou import.

| Preuve | Objet | Résultat / décision |
|---|---|---|
| search-0.json | BAILI BD176 | 20 lignes, surtout moteurs/électronique hors sujet ; pas de BAILI qualifié |
| search-1.json | DSCOSMETIC razor | 20 lignes, nombreux mécanismes/accessoires incompatibles |
| search-2.json | YINTAL safety | 11 lignes ; support 1005005707996553, 4,59 € : pas un rasoir |
| search-3.json | HAWARD razor | 20 lignes, pas de modèle exact débutant démontré |
| search-4.json | DSCOSMETIC | 20 lignes ; S9 316L complet 1005002856214417, recherche à partir de 51,99 € |
| search-5.json | Yaqi Tile | 20 lignes ; tête seule 1005003460449982, 30,59 € ; tête slant agressive 1005006774062348 exclue du brief doux |
| variants-dscosmetic-s9.json | 1005002856214417 | 11 variantes, une seule avec stock positif : S9 Ladder, SKU 12000022481203419, 51,99 € taxes annoncées incluses, stock 2 ; aucun fret confirmé |

S9 : dscosmetic Official Store, CN, 47 ventes affichées, zéro évaluation produit dans cette réponse. Notes boutique 4,8 ne remplacent pas des avis SKU. La mention 316L est une déclaration, pas un certificat ni une validation de douceur. [URL](https://www.aliexpress.com/item/1005002856214417.html).

Pas d'appel fret supplémentaire pour ce S9 : déjà trop coûteux pour le scénario rasoir 69 € étudié et sans preuve d'adaptation débutant. Ne pas convertir ce choix de tri en preuve d'impossibilité de livraison.

Les prix API fournisseur annoncent taxes incluses. Comparer au modèle de contribution sur une base fiscale cohérente ; sans facture/régime connu, ne pas inventer une TVA récupérable. Prix public ponctuel, ni devis volume ni prix contractuel.

Les anciennes pistes et leur erreur fret restent dans [le dossier précédent](../../2026-09-03-qualification-9-produits-pur/SOURCING.md). Aucune PDP AliExpress validée visuellement pendant cette passe. Un résultat inexploitable de l'API ne prouve pas l'absence de fournisseur : l'étape reste `MANQUANT` pour l'offre exacte.

## Nouveau vendeur apporté par Hakim — 04/09/2026

[Boutique AliExpress 1104699287](https://fr.aliexpress.com/store/1104699287). Hakim indique que ce marchand propose les composants permettant de composer un kit. **Piste utilisateur, catalogue et identité commerciale non vérifiés par l’agent.** Aucun rapprochement avec les vendeurs précédents n’est établi.

L’ouverture web n’a pas fourni de contenu ; l’outil navigateur a ensuite explicitement refusé cette URL par sa politique de sécurité du site. Aucun contournement essayé. Aucune référence de ce magasin dans les preuves locales déjà collectées. La passerelle autorisée expose recherche, variantes et qualification SKU, mais pas de catalogue par ID de boutique : les liens `/item/…html` ou captures du catalogue ont été demandés à Hakim pour une vérification structurée.

**Montages à évaluer — HYPOTHÈSES, aucun prix fournisseur :**

- Essentiel : rasoir complet à peigne fermé + lames DE identifiées et compatibles + étui protecteur.
- Coffret : même rasoir + lames + blaireau synthétique + support compatible + étui/boîte. Le savon n’est pas nécessaire à cette première composition et aurait son propre dossier produit.

Compatibilité à vérifier : diamètre du manche et logement du support, dimensions du rasoir dans l’étui, diamètre du blaireau et ouverture du support, protection des lames, cohérence des finitions. Même vendeur ne prouve ni kit assemblé ni colis unique ; vérifier conditionnement, disponibilité simultanée et transport réellement regroupé. Sans preuve de regroupement, calculer le scénario prudent avec les frais par article ; une facture ou un suivi unique ne se déduit pas du nom du magasin.

Repères économiques du [modèle précédent](../economics-assumptions.json) : pour garder 10 € de contribution après Ads avant frais fixes, à CPC hypothétique 0,80 € / CVR 2 %, coût rendu total cible **≤25,27 € à 99 € TTC**, ou **≤40,54 € à 119 € TTC**. Ces plafonds incluent tous composants, conditionnement, éventuel assemblage et expédition ; base fiscale cohérente et taxes non récupérables incluses. Ce ne sont ni devis ni seuils canoniques. Le taux de conversion peut différer entre les deux prix.

Prochaine entrée nécessaire : liens du rasoir, blaireau, support et étui/coffret envisagés, ou capture lisible avec nom du magasin et références. Aucun verdict fournisseur, aucune nouvelle mesure de demande, aucun changement du REVIEW A6, aucun message vendeur envoyé.

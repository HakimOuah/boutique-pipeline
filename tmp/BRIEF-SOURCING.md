# BRIEF — Sourcing AliExpress (run du 16 juillet 2026)

## Ton rôle

Tu explores AliExpress comme un utilisateur, via le navigateur intégré
(outils `mcp__Claude_Browser__*`), pour sourcer des fournisseurs sérieux.
L'accès est VÉRIFIÉ FONCTIONNEL : recherche et fiches produit se chargent sans login.

## Discipline navigateur — IMPORTANT

D'autres agents travaillent en parallèle dans le même navigateur.
1. Crée TON PROPRE onglet avec `tabs_create` au tout début.
2. Note le `tabId` retourné et **passe-le explicitement à CHAQUE appel** (`navigate`,
   `get_page_text`, `javascript_tool`...). Ne touche JAMAIS à un autre onglet.
3. N'utilise pas `tabs_select` (ça volerait le focus aux autres agents).

## Interdits absolus

- Aucun achat, aucun ajout au panier, aucun message à un fournisseur.
- Aucune saisie d'identifiants, aucune connexion à un compte.
- Ne JAMAIS résoudre ni contourner un CAPTCHA. Si tu en rencontres un : ARRÊTE,
  et signale précisément le blocage (URL + à quel moment).
- N'invente AUCUNE donnée absente de la page. Champ manquant = `"non indiqué"`.
- Ne modifie aucun fichier hors de ceux qu'on te demande.

## Méthode par niche

1. Va sur la recherche AliExpress FR de la niche (`https://fr.aliexpress.com/w/wholesale-<termes>.html`).
   Tu peux utiliser le filtre « Expédié depuis » pour privilégier les entrepôts UE.
2. Extrais les liens produit avec ce JS (adapte le tabId) :
   ```js
   (() => { const o=[]; document.querySelectorAll('a[href*="/item/"]').forEach(a=>{
     const m=a.href.match(/\/item\/(\d+)\.html/); if(m) o.push(m[1]); });
     return JSON.stringify([...new Set(o)]); })()
   ```
3. **Ouvre au minimum 8 fiches produit** de la niche (`https://fr.aliexpress.com/item/<id>.html`),
   une par une, avec `navigate` puis `get_page_text` (max_chars 4000-6000).
   Si le texte est insuffisant, complète avec `javascript_tool` ou scrolle.
4. Relève les champs (voir schéma). **Vérifie que l'URL fonctionne** (la page doit se charger).
5. Garde les **3 meilleurs** fournisseurs (jusqu'à 5 si plusieurs offres sont réellement bonnes).
   Tout le reste part dans `rejets` avec le motif.

## Règle sur la VARIANTE

Le prix retenu doit être celui de la **variante réellement exploitable**, pas le prix d'appel.
Écarte les annonces dont le prix d'appel ne couvre qu'un accessoire, une pièce détachée
ou une variante inutilisable. Précise toujours quelle variante tu as retenue.
Signale explicitement les faux prix d'appel (→ dans `rejets`, motif « faux prix d'appel »).

## Règles de fiabilité

- Une mention « CE » dans l'annonce n'est PAS une certification vérifiée.
  Écris exactement : `CE annoncé par le vendeur — documents à demander`
- Ne déduis jamais une certification d'un simple logo.
- Ne te fie pas au pourcentage de réduction affiché ni au prix barré.
- Signale les boutiques récentes ou à faible historique.
- Signale les expéditions de Chine aux délais incompatibles avec du e-commerce FR.
- Privilégie les entrepôts UE : France, Espagne, Allemagne, Pologne, Belgique, Pays-Bas, Tchéquie, Italie.

## Scoring (sur 100)

| Critère | Points |
|---|---:|
| Qualité et historique de la boutique | 20 |
| Ventes et avis du produit | 20 |
| Coût total rendu | 20 |
| Entrepôt et délai vers la France | 15 |
| Conformité et informations techniques | 10 |
| Risque SAV | 10 |
| Qualité des médias et de la fiche | 5 |

Décision (jamais « GO ») : `À APPROFONDIR` | `ALTERNATIVE` | `TROP CHER` | `RISQUE SAV` |
`DONNÉES INSUFFISANTES` | `À ÉCARTER`

## Vocabulaire imposé

L'écart entre prix de vente envisagé et coût fournisseur ne s'appelle JAMAIS « marge ».
Écris : `écart brut avant TVA, paiement, livraison client, retours, SAV et publicité`.

## Format de sortie — OBLIGATOIRE

Écris ton résultat dans le fichier JSON qu'on t'indique, avec CETTE structure exacte :

```json
{
  "niches": [
    {
      "niche": "Scanner de films",
      "priorite": "Shortlist",
      "prix_vente_envisage": "189-219 EUR",
      "cout_rendu_cible": "<= 90 EUR",
      "fiches_examinees": 8,
      "retenus": [
        {
          "produit": "nom exact du produit sur la page",
          "variante": "variante analysée",
          "url": "https://fr.aliexpress.com/item/XXXX.html",
          "boutique": "nom",
          "anciennete_boutique": "non indiqué",
          "note_boutique": "88.7% avis positifs",
          "abonnes": "130",
          "ventes": "12 vendus",
          "note_produit": "5.0",
          "nb_avis": "1",
          "avis_photos": "non indiqué",
          "prix": "117.39",
          "prix_barre": "non indiqué",
          "livraison": "gratuite",
          "cout_rendu": "117.39",
          "tva": "incluse au paiement si applicable",
          "expedie_depuis": "CN",
          "delai_france": "23-29 juillet (7-13 j)",
          "retour_gratuit": "oui, 90 j",
          "badge_choice": "non",
          "garantie": "non indiqué",
          "prise_ue": "non indiqué",
          "langue_fr": "non indiqué",
          "ce_rohs": "non indiqué",
          "poids_dimensions": "non indiqué",
          "caracteristiques": "22MP, LCD 5\", 16 Go",
          "medias": "photos + vidéo",
          "personnalisation": "non indiqué",
          "avis_negatifs": "non indiqué",
          "risque_sav": "description",
          "incoherences": "ex : « Seulement 8 restants » = fausse rareté",
          "score": 62,
          "decision": "ALTERNATIVE",
          "notes": "libre"
        }
      ],
      "rejets": [
        { "produit": "...", "url": "...", "motif": "faux prix d'appel",
          "prix_reel": "...", "probleme": "..." }
      ]
    }
  ],
  "blocages": "aucun | description précise"
}
```

Respecte les noms de clés à la lettre : un script lit ce JSON pour construire l'Excel.
Si une valeur manque, mets la chaîne `"non indiqué"` (jamais null, jamais vide).

---
type: journal
boutique: bonum-vitae
date: 2026-09-02
nature: audit
leviers: [conformite, acquisition]
titre: "GMC renommé Bonum Vitae ; le JSON-LD Organization du site est invalide (virgule orpheline)"
---

# GMC Bonum Vitae et JSON-LD — 02/09/2026

Suite du renommage Tuftéo. Hakim a changé le « Nom de l'entreprise » du GMC Bonum Vitae
d'OH Ventures en Bonum Vitae. Relevé après saisie, profil Chrome « Bonum Vitae ».

## Attention : deux comptes Merchant Center portent bonumvitae.fr

| Compte | Nom | Boutique | Produits | Statut |
|---|---|---|---|---|
| **5825588636** | **Bonum Vitae** | bonumvitae.fr validée + **revendiquée** | 51 approuvés, 0 refusé | **le vrai**, celui qui diffuse (27 clics ads, 15,59 € sur 28 j) |
| 515754956 | Hakim Ouahabi | bonumvitae.fr validée, **pas revendiquée** | 0 | coquille vide, sous `authuser=1` du même profil |

Le 515754956 est celui que le profil principal voit ; il ne sert à rien. Ne pas le confondre.

## GMC 5825588636 après la saisie

| Champ | Valeur |
|---|---|
| Nom de l'entreprise | **Bonum Vitae** ✓ |
| Adresse | 47 Rue Vivienne, 75002 Paris ✓ |
| URL service client | https://bonumvitae.fr/pages/contact ✓ |
| E-mail service client | contact@bonumvitae.fr ✓ (pas de Gmail ici, contrairement à Tuftéo) |
| **Téléphone service client** | **absent** — le site affiche +33 7 56 82 80 94 en footer |
| Qualité du magasin | Très bon · retours Bon · livraison Très bon |

Le téléphone manquant est le seul écart entre le footer et le GMC. Règle Terry : footer = GMC au
caractère près (e-mail, téléphone, adresse). À ajouter à la prochaine édition — pas maintenant,
pour ne pas empiler deux modifications sur un compte validé la même semaine.

Produits : 51 aujourd'hui, −38 sur 7 jours. Cohérent avec l'audit du 30/08 qui a volontairement
resserré le catalogue Shopping. Rien d'anormal.

## Le site : JSON-LD `Organization` **invalide**

`bonumvitae.fr` porte le **même défaut que Maison Noirmont le 15/08** : le bloc `Organization` se
termine par `"logo": "…",` puis `}` — **virgule orpheline**, parce que le gabarit écrit chaque champ
optionnel suivi d'une virgule et que le dernier champ conditionnel (`sameAs`, réseaux sociaux) est
vide. `json.loads` échoue : *Illegal trailing comma before end of object*.

Conséquence : **Google ignore le bloc en entier**. Le `name: Bonum Vitae`, l'adresse et l'e-mail
qu'il contient n'existent pas pour le crawler. Le site n'a donc, en données structurées, aucun
nom d'entreprise — au moment précis où le GMC vient de passer à « Bonum Vitae ». Le footer visible
dit « OH VENTURES (SASU) — SIREN 103157251 », le titre et le logo disent Bonum Vitae : Google
recoupe encore, mais sans le bloc qui ferait le lien proprement.

Contenu du bloc, une fois la virgule retirée : `name: Bonum Vitae`, adresse, `email:
contact@bonumvitae.fr`, logo. **Pas de `legalName`, pas de `telephone`** — deux champs que
Noirmont et Tuftéo ont.

## Réparation — la recette Noirmont du 15/08, à l'identique

`snippets/organization-schema.liquid` (appelé par `snippets/meta-tags.liquid` sur la page
d'accueil). Deux lignes :

1. `]{% endif %}` → `],{% endif %}` sur le closer de `sameAs`
2. insérer juste après, avant l'accolade : `"@id": {{ request.origin | append: '/#organization' | json }}`

Le bloc a alors un dernier champ qui s'écrit toujours, et devient insensible aux champs vides.
Détail complet : `boutique-seiko-mod/journal/2026-08-15-json-ld-organization.md`, §4.

En même temps, ajouter `"legalName": "OH Ventures"` et le `telephone` (fiche adresse Shopify), pour
que le bloc dise la même chose que Tuftéo et Noirmont : marque en `name`, OH Ventures en `legalName`.

**Où :** thème live de Bonum Vitae — le connecteur refuse d'écrire sur le thème MAIN, donc copie de
travail puis publication, ou Cursor dans l'éditeur de code. Contrôle : `json.loads` sur le bloc
rendu, puis le test des résultats enrichis Google.

## Tuftéo — vérifié après saisie

GMC 5829640586 : **Tuftéo**, `contact@tufteo.com`, +33756828094, 47 Rue Vivienne. Les deux
corrections sont passées. Reste à **renvoyer les données produit** depuis l'app Google & YouTube
pour que le nouveau nom remonte sur les fiches Shopping.

## Réparé — 02/09/2026, nuit

Brief : `livraisons/2026-09-02-json-ld-organization-cursor.md`. Contrôle live et test Google
passés **avant** ce push.

**Fichier touché :** `snippets/organization-schema.liquid` (seul gabarit). Appelé par
`snippets/meta-tags.liquid` si `request.page_type == 'index'`. Aucune fiche produit, aucune
policy, rien dans le GMC.

**Thèmes :** copie `jsonld-org-2026-09-02` (`206619115858`) depuis le MAIN alors
`copie-de-fullstack-2-3` (`205568147794`). `shopify theme push` du snippet a échoué
silencieusement (fichier resté à 2 167 o). Écriture via `themeFilesUpsert` (2 206 o).
Préview validée (cookie Shopify obligatoire ; `curl -L` sans cookie retombe sur le live).
Puis `themePublish` — le MAIN est désormais **`206619115858`**. L'ancien FullStack
`205568147794` est UNPUBLISHED, intact.

**Diff (principe) :**

```diff
     "name": {{ shop.name | json }},
+    "legalName": "OH Ventures",
+    "telephone": "+33756828094",
     "url": {{ request.origin | append: page.url | json }},
-    {% if shop.phone != blank %}
-    "telephone": {{ shop.phone | json }},
-    {%- endif -%}
     {% if shop.email != blank %}
     "email": {{ shop.email | json }},
…
-    ]{% endif %}
+    ],{% endif %}
+    "@id": {{ request.origin | append: '/#organization' | json }}
```

Le `if shop.phone` a été retiré : `shop.phone` est vide (le champ GraphQL `Shop.phone`
n'existe pas) ; le laisser aurait produit un doublon le jour où la fiche adresse serait
remplie. Téléphone **hardcodé** `+33756828094`. **Pas touché côté GMC.**

### Contrôle §4

**§4.1 préview** (`?preview_theme_id=206619115858`, cookie de session) puis **§4.2 live**
`https://bonumvitae.fr/` :

```
{'name': 'Bonum Vitae', 'legalName': 'OH Ventures', 'telephone': '+33756828094', 'email': 'contact@bonumvitae.fr', '@id': 'https://bonumvitae.fr/#organization'}
```

`json.loads` OK. Accueil : **1** bloc `ld+json` (`Organization`). Fiches
`/products/osmoseur-ro-600g` et `/products/kit-entretien-osmoseur-600-gpd` : **1** bloc
`Product` chacune, parse OK. Contact / FAQ : 0 bloc.

**§4.3 test résultats enrichis** (02/09 00:32, agent smartphone) :
<https://search.google.com/test/rich-results/result?id=u97Ou51EoQePG_TlATzSmQ>

- 2 éléments valides : Organisation + Commerces et services à proximité
- **0 erreur**
- 1 problème **non critique / facultatif** : `addressCountry` vaut `France` (nom) au lieu
  du code ISO `FR`. Préexistant — `shop.address.country` du gabarit natif. Pas corrigé
  cette passe (hors brief).

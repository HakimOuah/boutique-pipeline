---
type: livraison
boutique: bonum-vitae
date: 2026-09-02
titre: "Réparer le JSON-LD Organization de bonumvitae.fr — brief exécutable"
destinataire: cursor
---

# JSON-LD `Organization` de bonumvitae.fr — brief exécutable

Boutique : **bonumvitae.fr**. GMC : **5825588636** (nom « Bonum Vitae » depuis le 02/09).
Contexte : le bloc `Organization` de la page d'accueil est **du JSON invalide** — virgule orpheline
avant l'accolade fermante. Google ignore le bloc en entier : le site n'a aucun nom d'entreprise
en données structurées, alors que le GMC vient de passer d'« OH Ventures » à « Bonum Vitae ».
Même défaut, même cause et même réparation que Maison Noirmont le 15/08/2026
(`boutique-seiko-mod/journal/2026-08-15-json-ld-organization.md`).

## Interdits

- Ne toucher **que** le gabarit du JSON-LD et la fiche adresse Shopify décrits ici. Aucun autre
  fichier de thème, aucune fiche produit, aucune policy.
- Ne rien modifier dans le Merchant Center. Le téléphone manquant côté GMC sera ajouté plus tard,
  pas cette semaine.
- Pas de `git push` sur un thème publié sans avoir passé le contrôle final (§4).

## 0. Le constat, reproductible

```bash
curl -s https://bonumvitae.fr/ \
 | python3 -c "import sys,re,json; h=sys.stdin.read(); b=[m for m in re.findall(r'<script[^>]*ld\+json[^>]*>(.*?)</script>',h,re.S) if '\"Organization\"' in m][0]; json.loads(b.strip())"
```

Aujourd'hui : `json.JSONDecodeError: Illegal trailing comma before end of object`.
Le bloc rendu se termine ainsi :

```json
    "email": "contact@bonumvitae.fr",
    "logo": "https:\/\/bonumvitae.fr\/cdn\/shop\/files\/logo-bonum-vitae-280x80.png?v=1783847859&width=500",
  }
```

Le gabarit écrit chaque champ optionnel **suivi** d'une virgule ; le dernier champ conditionnel
(`sameAs`, alimenté par les réseaux sociaux) ne s'écrit pas parce qu'aucun réseau n'est renseigné,
et la virgule de `logo` reste orpheline.

## 1. Trouver le gabarit

Thème **publié** de Bonum Vitae (rôle `main`). Chercher dans l'éditeur de code (ou `shopify theme
pull`) le fichier qui contient `"@type": "Organization"`. Sur Noirmont c'est
**`snippets/organization-schema.liquid`**, appelé par `snippets/meta-tags.liquid` sous
`{% if request.page_type == 'index' %}`. Bonum Vitae tourne sur la même famille de thème : vérifier
que c'est le même nom ; sinon, appliquer la même logique au fichier trouvé.

Travailler sur une **copie** du thème (Dupliquer dans l'admin, ou `shopify theme push --unpublished`),
vérifier sur l'URL de prévisualisation, **puis** publier. Jamais d'édition directe sur le thème live.

## 2. La réparation — deux lignes, plus deux champs

### 2a. Rendre le gabarit insensible aux champs vides

Localiser la fin du bloc `sameAs`. Sur Noirmont, lignes 42-49 :

```liquid
    {%- if social_urls != blank %}
    "sameAs": [
      {% assign social_urls_array = social_urls | split: ',' -%}
      {% for url in social_urls_array -%}
        {{ url | json }}{% unless forloop.last %},{% endunless %}
      {% endfor -%}
    ]{% endif %}
  }
```

Remplacer par :

```liquid
    {%- if social_urls != blank %}
    "sameAs": [
      {% assign social_urls_array = social_urls | split: ',' -%}
      {% for url in social_urls_array -%}
        {{ url | json }}{% unless forloop.last %},{% endunless %}
      {% endfor -%}
    ],{% endif %}
    "@id": {{ request.origin | append: '/#organization' | json }}
  }
```

Deux différences, rien d'autre :
1. `]{% endif %}` → **`],{% endif %}`**
2. une ligne neuve **`"@id": …`** juste après, avant l'accolade — un dernier champ qui s'écrit
   **toujours**, donc plus jamais de virgule orpheline, que `sameAs` soit vide ou non.

Si le gabarit de Bonum Vitae diffère (autre ordre de champs, autre closer), le principe reste :
**le dernier champ écrit ne doit dépendre d'aucune condition**, et tout champ conditionnel qui le
précède porte sa virgule *à l'intérieur* de sa condition.

### 2b. Ajouter `legalName`

Juste après la ligne `"name": …` du gabarit, insérer :

```liquid
    "legalName": "OH Ventures",
```

Le site dit alors la même chose que Tuftéo et Noirmont : la marque en `name`, l'entité en
`legalName`. Cohérent avec le footer (« OH VENTURES (SASU) — SIREN 103157251 ») et avec le GMC.

### 2c. Faire apparaître le téléphone

Le gabarit émet `"telephone"` depuis le téléphone de la fiche adresse Shopify **s'il est rempli**.
Aujourd'hui le bloc n'a pas de `telephone` : la fiche est vide. Dans l'admin :
**Paramètres → Général → Adresse de facturation → Téléphone** = `+33 7 56 82 80 94`
(le numéro du footer, même écriture que Noirmont et Tuftéo).

Si le gabarit ne lit pas `shop.phone`, ajouter après `legalName` :

```liquid
    "telephone": "+33756828094",
```

## 3. Cible : ce que le bloc rendu doit contenir

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Bonum Vitae",
  "legalName": "OH Ventures",
  "url": "https://bonumvitae.fr",
  "description": "…",
  "address": { "@type": "PostalAddress", "streetAddress": "47 Rue Vivienne", "addressLocality": "Paris", "postalCode": "75002", "addressCountry": "France" },
  "telephone": "+33756828094",
  "email": "contact@bonumvitae.fr",
  "logo": "…",
  "@id": "https://bonumvitae.fr/#organization"
}
```

L'ordre des champs importe peu ; **la validité et le contenu** importent.

## 4. Contrôle final — obligatoire avant publication

1. Sur l'URL de **prévisualisation** de la copie, la commande du §0 doit rendre **sans erreur**.
2. Puis, une fois publié, sur `https://bonumvitae.fr/` :

```bash
curl -s https://bonumvitae.fr/ \
 | python3 -c "import sys,re,json; h=sys.stdin.read(); b=[m for m in re.findall(r'<script[^>]*ld\+json[^>]*>(.*?)</script>',h,re.S) if '\"Organization\"' in m][0]; o=json.loads(b.strip()); print({k:o.get(k) for k in ['name','legalName','telephone','email','@id']})"
```

Attendu : `{'name': 'Bonum Vitae', 'legalName': 'OH Ventures', 'telephone': '+33756828094',
'email': 'contact@bonumvitae.fr', '@id': 'https://bonumvitae.fr/#organization'}`.

3. Coller l'URL dans le [test des résultats enrichis](https://search.google.com/test/rich-results) :
   l'entité `Organization` doit apparaître, sans erreur.
4. Vérifier que les **autres** blocs JSON-LD de la page (produits, site) parsent toujours — la
   commande du §0 sans le filtre `"Organization"` doit passer sur chacun.

## 5. Après

Rien d'autre. Le GMC Bonum Vitae ne bouge pas cette semaine. Le journal à compléter est
`boutique-bonum-vitae/journal/2026-09-02-gmc-nom-et-json-ld-invalide.md` : ajouter une section
« Réparé » avec le nom exact du fichier touché, le diff, et la sortie du contrôle §4.

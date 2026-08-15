# JSON-LD `Organization` de l'accueil — la cause réelle, trouvée dans le gabarit

**15/08/2026, après-midi.** Boutique **Maison Noirmont** (`maisonnoirmont.fr`, publique).
Lecture seule sur le thème publié (`theme.files`). **Rien n'a été écrit, aucun thème dupliqué,
aucun thème republié.**

---

## Le verdict en une ligne

Le bloc est invalide **à cause du gabarit, pas d'un réglage** :
`snippets/organization-schema.liquid` **ligne 48**, `]{% endif %}` — il manque une virgule après le
`]`, et surtout il manque **un dernier champ inconditionnel** pour fermer l'objet. Aujourd'hui c'est
`sameAs` qui joue ce rôle, et `sameAs` ne s'écrit jamais parce qu'aucun réseau social n'est
renseigné.

---

## 1. Où vit le bloc

| Quoi | Où |
|---|---|
| Thème publié | **Noirmont**, `gid://shopify/OnlineStoreTheme/205089014098`, rôle `MAIN` |
| Le gabarit fautif | **`snippets/organization-schema.liquid`** — **50 lignes, 2 167 octets** |
| Qui l'appelle | **`snippets/meta-tags.liquid`**, sous `{% if request.page_type == 'index' %}` |
| Qui appelle `meta-tags` | `layout/theme.liquid`, 1re ligne du `<head>` |

`meta-tags.liquid` :

```liquid
{% if request.page_type == 'index' %}
  {% render 'organization-schema' %}
{% endif %}
```

Donc **le bloc `Organization` n'existe que sur l'accueil**. C'est confirmé côté public :

| Page | Blocs `application/ld+json` servis |
|---|---|
| `/` (accueil) | **1** — `Organization`, ⛔ **invalide** |
| `/products/loupe-de-date-saphir` | **1** — `ProductGroup`, ✅ valide (`{{ product \| structured_data }}`) |
| `/collections/all` | **0** |
| `/pages/contact` | **0** |

---

## 2. Le mécanisme exact du défaut

Le gabarit écrit **chaque champ optionnel avec une virgule *après* lui** (lignes 8, 21, 24, 27) :

```liquid
{% if settings.logo %}
"logo": {{ settings.logo | image_url: width: 500 | prepend: "https:" | json }},
{%- endif -%}
```

**Un seul champ n'a pas de virgule finale : `sameAs`** (lignes 42-48). C'est donc lui, et lui seul,
qui est censé fermer l'objet proprement. Ligne 48 :

```liquid
    ]{% endif %}
  }
```

Et `sameAs` ne s'écrit **que si** au moins un des onze réglages de réseau social est rempli
(lignes 29-41) :

```
facebook_url, instagram_url, x_url, youtube_url, tiktok_url, pinterest_url,
linkedin_url, snapchat_url, threads_url, discord_url, whatsapp_url
```

**Relevé dans `config/settings_data.json` du thème publié : aucun des onze n'est présent.**
`social_urls` est donc vide, la condition de la ligne 42 est fausse, tout le bloc `sameAs` est sauté
— et le dernier champ réellement écrit reste **`logo`, avec sa virgule**, immédiatement suivi de
l'accolade fermante.

C'est un **gabarit fragile par construction** : il dépend d'un champ facultatif pour être du JSON
valide. Il aurait cassé de la même façon avec `logo` vide (la virgule serait venue de `email`), ou
avec `email` vide (elle serait venue de `telephone`). **Il n'a jamais été valide sur cette boutique.**

---

## 3. Pourquoi la première tentative n'a pas marché — et ce qu'elle a quand même prouvé

L'audit du 15/08 au matin avait conclu que la cause était **`shop.phone` vide**. C'était faux :
`telephone` est **ligne 21**, *avant* `logo` (ligne 27). Il n'a jamais été le dernier champ.

Hakim a bien rempli le champ, et **ça a marché** — la ligne est là. La preuve est dans le message
d'erreur lui-même, qui a **glissé d'une ligne** :

| Avant le remplissage | Après le remplissage |
|---|---|
| `line 11 column 113` | `line 12 column 113` |

Une ligne de plus dans le bloc, à la même colonne : c'est exactement `"telephone"` qui s'est
inséré. **Le réglage a été pris en compte, il ne réparait simplement pas ce défaut-là.**

Bloc réellement servi le 15/08 à 14 h 40 (cache contourné) :

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Maison Noirmont",
  "url": "https://maisonnoirmont.fr",
  "description": "Montres automatiques à mouvement japonais, de 36 à 41 mm. Calibre et cotes détaillés sur chaque fiche. Dès 239 €, livraison France, retour 14 jours.",
  "address": {
    "@type": "PostalAddress","streetAddress": "47 Rue Vivienne","addressLocality": "Paris","postalCode": "75002","addressCountry": "France"},
  "telephone": "+33 7 56 82 80 94",
  "email": "contact@maisonnoirmont.fr",
  "logo": "https://maisonnoirmont.fr/cdn/shop/files/logo-noirmont-encre.png?v=1784913069&width=500",
}
```

`json.loads()` → `Illegal trailing comma before end of object: line 12 column 113`.

**Tout le contenu est juste.** Le nom, l'adresse, le téléphone, l'e-mail, le logo : rien à corriger
dans les données. Une virgule les rend tous invisibles.

---

## 4. La réparation retenue

**Deux lignes à toucher, dans l'éditeur de code, sur `snippets/organization-schema.liquid`.**

Le principe : rendre le gabarit **insensible aux champs vides** en lui donnant un **dernier champ
qui s'écrit toujours**, et en remettant la virgule sur `sameAs` qui n'est plus le closer.

`"@id"` est le bon candidat : c'est un champ JSON-LD légitime, il donne à l'entreprise un
identifiant stable, et il ne dépend d'aucun réglage.

**Actuel (lignes 42-49)** :

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

**Corrigé** :

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

Deux différences, et rien d'autre :
1. ligne 48 : `]{% endif %}` → **`],{% endif %}`** ;
2. une **ligne neuve** insérée juste après, avant l'accolade : `"@id": …`.

**Les deux cas se tiennent** :

| Cas | Fin du bloc rendu | Valide ? |
|---|---|---|
| Aucun réseau social (aujourd'hui) | `"logo": "…",` puis `"@id": "https://maisonnoirmont.fr/#organization"` puis `}` | ✅ |
| Un réseau social plus tard | `… "sameAs": ["…"],` puis `"@id": …` puis `}` | ✅ |

Et le gabarit ne peut plus casser si un champ optionnel se vide : `@id` ferme toujours.

### Ce qu'on a écarté

**Remplir un réglage de réseau social** (Personnalisateur → Paramètres du thème → « Réseaux
sociaux » → Instagram, Facebook…) ferait apparaître `sameAs` et rendrait le bloc valide **sans
toucher au code**. Écarté pour trois raisons :
- ça exige un **compte réellement existant** — inventer une URL de réseau social sur une boutique
  qui n'en a pas est une déclaration fausse dans une donnée structurée, exactement le genre de
  contradiction que Merchant Center sanctionne ;
- **ça recasse au premier vidage** du champ ;
- ça laisse un gabarit qui produit du JSON invalide dès qu'un champ facultatif manque, sur toutes
  les boutiques qui réutiliseraient ce thème.

Si Maison Noirmont ouvre un jour un compte Instagram, le remplir reste **utile pour le SEO** (Google
relie l'entreprise à ses profils) — mais ce sera un bonus, plus un correctif.

---

## 5. Le reste du bloc, vérifié

| Champ | État | Commentaire |
|---|---|---|
| `name` | ✅ | `Maison Noirmont` |
| `url` | ✅ | `https://maisonnoirmont.fr` |
| `description` | ✅ | reprise de la description de la boutique |
| `address` | ✅ | rue, ville, code postal, pays — complet |
| `telephone` | ✅ | `+33 7 56 82 80 94`, arrivé avec le réglage de Hakim |
| `email` | ✅ | `contact@maisonnoirmont.fr`, plus aucun Gmail |
| `logo` | ✅ | CDN Shopify, 500 px |
| `sameAs` | ⚪ absent | légitime : pas de compte social. À remplir le jour où il y en aura un |
| `@id` | ⛔ manquant | ajouté par la correction ci-dessus |

**Un manque de fond, à part** : le champ `legalName` n'existe pas dans le gabarit, donc **`OH
Ventures` n'apparaît nulle part dans la donnée structurée**. Merchant Center compare la raison
sociale déclarée à celle du site. Ce n'est pas ce qui casse le JSON, mais c'est le prochain champ à
ajouter — Shopify n'expose pas la raison sociale en Liquid, il faudra l'écrire en dur ou passer par
un métachamp. **Noté comme point ouvert de T-34, pas traité ici.**

### Faut-il servir `Organization` sur toutes les pages ?

**Non, l'accueil seul est correct.** La recommandation de Google est de déclarer l'entité sur **une
page canonique** — historiquement la page d'accueil — et de ne pas la répéter. Répéter le bloc sur
96 fiches n'ajoute rien et multiplie les occasions de divergence.

En revanche, le `@id` ajouté par la correction ouvre une amélioration propre pour plus tard : les
blocs `ProductGroup` des fiches pourraient référencer `{"@id": "https://maisonnoirmont.fr/#organization"}`
dans leur champ `brand`, au lieu de répéter un objet `Brand` anonyme. Ce n'est pas nécessaire pour
Merchant Center, et le `ProductGroup` étant généré par le filtre natif `structured_data` de Shopify,
ça demanderait de le remplacer par du JSON écrit à la main. **Pas recommandé maintenant.**

---

## 6. Le contrôle après correction

À lancer après avoir enregistré le fichier dans l'éditeur de code (compter jusqu'à 15 min de cache) :

```bash
curl -s "https://maisonnoirmont.fr/?v=$RANDOM" | python3 -c 'import sys,re,json
n=0
for b in re.findall(r"application/ld\+json[^>]*>(.*?)</script>",sys.stdin.read(),re.S):
    n+=1
    try: print("OK  ", json.loads(b)["@type"])
    except Exception as e: print("KO  ", e)
print(n,"bloc(s)")'
```

- **Aujourd'hui** : `KO   Illegal trailing comma before end of object: line 12 column 113` / `1 bloc(s)`
- **Attendu après correction** : `OK   Organization` / `1 bloc(s)`

Puis, en confirmation chez Google : coller `https://maisonnoirmont.fr/` dans le
[test des résultats enrichis](https://search.google.com/test/rich-results) — l'entité
`Organization` doit y apparaître avec le nom, l'adresse, le téléphone et le logo.

---

## 7. Ce que ça vaut

C'est **une ligne de code pour récupérer toute la carte d'identité du marchand** : raison sociale,
adresse postale, téléphone, e-mail, logo. Aujourd'hui Google n'en lit **rien** sur cette boutique —
le bloc est rejeté en entier, et les autres pages n'en servent aucun. C'est le meilleur rapport
effort/effet du dossier de conformité restant.

---

## Note de méthode — à ajouter à la grille d'audit

**Un bloc JSON-LD généré par conditions Liquid doit être testé sur le HTML rendu, pas relu dans le
gabarit.** Celui-ci s'affiche parfaitement à la lecture humaine ; il a traversé trois audits
successifs. Et surtout : **quand un correctif ne répare pas le symptôme, relire l'erreur avant de
conclure qu'il a échoué.** Ici le remplissage du téléphone avait bel et bien fonctionné — le
déplacement de l'erreur de `line 11` à `line 12` le prouvait, et cette information était sous les
yeux de l'audit précédent.

**Le motif générique à retenir** : dans un gabarit qui écrit des virgules *après* chaque champ
optionnel, **la validité tient entièrement au dernier champ**. Chercher toujours quel champ ferme
l'objet, et si son écriture est conditionnelle.

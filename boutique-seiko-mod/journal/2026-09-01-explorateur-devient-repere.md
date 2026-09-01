---
type: journal
boutique: seiko-mod
date: 2026-09-01
nature: intervention
leviers: [conformite, copy]
titre: "Explorateur devient Repère"
---

# Explorateur devient Repère — 01/09/2026

Décision de Hakim : **zéro risque**, on renomme, quitte à revenir en arrière plus tard.
« Explorateur » était le dernier nom du registre Rolex encore vivant sur la boutique, après
Président (23/08) et Jubilé (01/09, matin).

## Le nom retenu

**Repère.** Terme horloger français courant — les repères d'un cadran sont ses index — qui décrit
exactement ce que cette montre a de distinctif : les chiffres 3, 6, 9 et le triangle à midi.
Aucune marque horlogère derrière, et il s'assied dans la famille des noms communs déjà en place
(Intégrale, Héritage, Contre-la-montre) plutôt que dans celle des noms d'agent (Voyageur, Aviateur),
d'où venait « Explorateur ».

Candidats écartés : *Arpenteur* (marque de prêt-à-porter française existante), *Cardinal* (ancienne
marque horlogère), *Boussole* (suggère une fonction que la montre n'a pas — le contraire de ce qu'on
cherche), *Éclaireur* (même champ sémantique qu'Explorer, sans intérêt).

## Appliqué

Fiche `gid://shopify/Product/10988849299794`, ACTIVE.

| Surface | Avant | Après |
|---|---|---|
| Titre | Explorateur : Sport chic à chiffres 3-6-9 | **Repère : Sport chic à chiffres 3-6-9** |
| Handle | `montre-acier-chiffres-3-6-9-explorateur` | `montre-acier-chiffres-3-6-9-repere` (**301** posée) |
| `seo.title` | … : Explorateur | … : Repère |
| `descriptionHtml` | « Ce cadran d'explorateur est un classique de la lisibilité » | « Ce dessin de cadran est un classique de la lisibilité » |
| `alt` des médias | 10 | 10 corrigés |
| Fichiers CDN | 15 (10 rattachés + 5 doublons orphelins) | 15 renommés |
| Collection `montre-cadran-a-chiffres` — description | « et l'Explorateur dont le cadran… » | « et le Repère dont le cadran… » |
| Collection `montre-cadran-a-chiffres` — **`seo.description`** | « field, aviateur, **explorateur** 3-6-9 » | « field, aviateur, chiffres 3-6-9 » |

## Le piège du jour

La description de collection était corrigée et la page rendait pourtant encore trois occurrences
d'« explorateur » : elles venaient du **`seo.description` de la collection**, recopié par le thème
dans `<meta name="description">`, `og:description` et `twitter:description`. Corriger le corps
visible ne suffit pas — **le SEO d'une collection est une surface distincte**, comme les
`global.*_tag` des fiches l'étaient le 30/08. À ajouter au balayage systématique.

## Contrôle

- Admin : `productsCount(query:"explorateur OR explorer")` = **0** sur les 221 fiches
- Fichiers CDN nommés `explorateur` : **0**
- Thème live (`index.json`, `product.json`, `collection.json`, header, footer) : **0**
- 28 URL balayées (accueil, 7 pages, 7 policies, 13 collections, la PDP renommée) : **0 résidu**
  sur `explorat|jubil|seiko|miyota|mingzhu|904l|skx|rolex|oyster|datejust|no logo|ships from|china mainland|band color|band width|qualité premium`
- `products.json` (96 actives) : **propre**
- Ancien handle → **301**, nouvelles images en **200**

## Effet sur le calendrier

Nouvelle passe crawlable. Le compteur de 7 à 10 jours repart du **01/09 au soir** : fenêtre
**8–11 septembre**. Toujours 0 ads, toujours pas de demande de réexamen.

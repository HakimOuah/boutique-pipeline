# Balisage UTM — à faire avant toute campagne

**Constat du 30/08/2026.** Sur les 490 sessions de Tuftéo, `utm_campaign` vaut `None` pour la
totalité. La campagne Search de fin juillet est donc indiscernable du référencement naturel :
Shopify voit 94 sessions « google » sans savoir lesquelles ont été payées. Résultat, 110 € de
dépense réelle qu'on ne peut rattacher à aucune session, et donc **aucun CPA, aucun ROAS, aucun
apprentissage**.

Le trafic non balisé est perdu pour l'analyse, définitivement. C'est le même mécanisme que la
croyance pré-lancement : ce qu'on ne capture pas au passage n'existera jamais.

## Ce qui a été vérifié le 31/08/2026

| Vérification | Résultat |
|---|---|
| Les UTM survivent sur `tufteo.com` et `bonumvitae.fr` | ✅ conservés |
| Les UTM survivent aux **redirections 301** (collections supprimées → produit) | ✅ conservés |
| `gclid` conservé | ✅ |
| ShopifyQL sait filtrer `WHERE utm_medium = 'cpc'` | ✅ |

**Rien à corriger côté Shopify.** Le seul geste manquant est dans Google Ads.

## Le geste, dans Google Ads

Google Ads → **Paramètres** → **Paramètres du compte** → **Suivi** → *Modèle de suivi* :

```
{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_content={adgroupid}&utm_term={keyword}
```

À poser **au niveau du compte** : il s'applique alors à toutes les campagnes, présentes et
futures, sans rien à refaire à chaque lancement.

Trois précisions qui évitent des erreurs classiques :

- **`utm_medium=cpc` est la valeur qui compte.** C'est elle que `mesure-hebdo.py` interroge pour
  remplir `sessions_payantes`. La changer casse le relevé.
- **`{campaignid}` rend un identifiant numérique, pas un nom.** C'est volontaire : les
  identifiants sont stables, les noms de campagne changent et cassent l'historique. Le nom se
  retrouve dans Google Ads à partir de l'identifiant.
- **Ne pas désactiver l'auto-tagging** (`gclid`). Les deux coexistent et ne servent pas à la même
  chose : `gclid` alimente le suivi de conversion de Google Ads, les UTM alimentent l'analytics
  Shopify. Couper l'un pour l'autre est une erreur fréquente.

## Vérifier que ça marche

Après le premier clic payant, en une commande :

```bash
cd "…/boutique-pipeline" && set -a && . ./.env && set +a && \
python3 instrumentation/mesure-hebdo.py --boutiques tufting --ecrire
```

Le champ `sessions_payantes` doit devenir non nul dans la note de la semaine. **Tant qu'il reste à
zéro alors qu'une campagne tourne, c'est que le balisage n'est pas en place** — et il ne faut pas
laisser tourner la dépense dans cet état.

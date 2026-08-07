# Infrastructure de sourcing AliExpress — 2026-08-02

## Verdict opérationnel

`SOLUTION_VALIDEE_ET_TESTEE_END_TO_END — SANS APIFY — SANS SCRAPING`

Codex peut désormais exécuter depuis le Mac les quatre opérations nécessaires
au sourcing AliExpress : recherche, inventaire des variantes, sélection stricte
d’un SKU et calcul du fret France. Les appels partent du VPS à IP fixe
`148.230.118.152`, déjà autorisé par AliExpress, et utilisent exclusivement
AliExpress Open Platform / AE-Dropshipper.

Le test complet du 02/08 à `18:32:59 UTC` a qualifié l’article
`1005010249362754`, SKU `12000051675733200`, variante `white sterile` +
`36mm-glass back`, avec prix, stock et livraison France live.

Preuve :
`outputs/20260802/aliexpress-live-exact-1005010249362754-20260802T183259Z.json`.

## Architecture réellement déployée

1. Le client local
   `codex-chasse-clusters/tools/aliexpress_vps_gateway.py` encode une requête
   JSON et appelle SSH sans shell.
2. Une clé Ed25519 dédiée est acceptée sur le VPS avec l’option OpenSSH
   `restrict` et une `command=` forcée.
3. La commande forcée est uniquement
   `docker exec -i aliexpress-mcp python /app/scripts/ssh_readonly_gateway.py`.
4. Le gateway n’accepte que `health`, `search`, `variants` et `exact`.
5. Le conteneur signe les appels officiels AliExpress depuis l’IP fixe du VPS.
6. Les réponses ne contiennent jamais App Secret, access token, refresh token
   ni signature.

Cette architecture évite trois fragilités : l’IP variable du Mac, le blocage
du navigateur AliExpress et l’exposition publique du port MCP `8080`.

## Commandes prêtes pour Codex

```bash
# Santé et échéances OAuth
python3 codex-chasse-clusters/tools/aliexpress_vps_gateway.py health

# Découverte brute AliExpress
python3 codex-chasse-clusters/tools/aliexpress_vps_gateway.py \
  search "Tandorio Arabic numerals watch" --limit 5 --destination FR

# Vérité fournisseur pour toutes les variantes
python3 codex-chasse-clusters/tools/aliexpress_vps_gateway.py \
  variants 1005010249362754

# Qualification fermée d’une variante exacte
python3 codex-chasse-clusters/tools/aliexpress_vps_gateway.py \
  exact 1005010249362754 \
  --property "white sterile" \
  --property "36mm-glass back" \
  --destination FR
```

La sélection échoue si aucun SKU ne correspond, si plusieurs SKU
correspondent, si l’identifiant n’est pas numérique, si le stock est absent ou
nul, ou si aucune option de livraison n’est disponible.

## Preuves live

### Recherche

La requête `Tandorio Arabic numerals watch` a retourné 5 articles live. La
recherche Open Platform est exploitable mais bruitée : un minuteur de cuisine
était présent dans les résultats. Elle sert à découvrir des IDs, jamais à
valider automatiquement une offre.

### Variantes

L’article exact expose **40 SKU**, tous avec un stock numérique positif au
moment du test. Le SKU demandé `12000051675733200` est bien présent.

### SKU exact et fret France

- Produit : `onSelling`
- SKU : `12000051675733200`
- Attribut : `5:57036539#36mm-glass back;14:175#white sterile`
- Stock : `300`
- Prix taxe incluse selon l’API : `102,39 €`
- Livraison : `1,99 €`, suivie, depuis `CN`
- Délai API : `8–11 jours`
- Coût rendu observé par addition : `104,38 €`
- Vendeur : `tandorio Timepieces Store`, trois notes vendeur à `4,8/5`
- Produit : `4,7/5`, 3 évaluations, 8 ventes

L’image du SKU a également été contrôlée : cadran blanc/argenté, chiffres
arabo-orientaux, aucun mot-symbole Tandorio et inscription `Automatic` visible.
Le champ brut de couleur vaut pourtant `vert`; cette incohérence AliExpress est
conservée dans la preuve et neutralisée par le SKU numérique, le `sku_attr` et
le contrôle visuel.

## Sécurité testée

- Fichier `/opt/aliexpress-mcp-server/.env` : mode `600`, propriétaire root.
- État d’expiration non secret : mode `600`, propriétaire root.
- Clé locale :
  `/Users/Hakim/.ssh/aliexpress_sourcing_vps_ed25519`, mode `600`.
- Empreinte :
  `SHA256:s2vV+WNhoYV0GedTF4pgoTe1q1rODjCYPiDIeb9VQt8`.
- Une tentative SSH contenant `uname -a` a retourné la réponse `health` du
  gateway, pas la commande demandée : le shell arbitraire est bien bloqué.
- L’action inexistante `delete` est refusée avec `unsupported_action` et un
  code de sortie `2`.
- Le conteneur OAuth temporaire a été arrêté puis supprimé, ce qui retire son
  journal local. Il est recréable depuis `docker-compose.oauth.yml` pour une
  future autorisation manuelle.

## Renouvellement OAuth

Le renouvellement automatique a été exercé contre l’API réelle :

- access token renouvelé avec succès ;
- `.env` mis à jour atomiquement sans afficher les jetons ;
- conteneur `aliexpress-mcp` recréé uniquement après rotation ;
- état final `healthy` ;
- second passage sans échéance proche : aucune rotation et aucun redémarrage.

Le timer systemd `aliexpress-token-refresh.timer` est actif et s’exécute chaque
jour autour de `03:17 UTC` avec délai aléatoire. Il renouvelle l’access token
quand il reste 7 jours ou moins.

Échéances actuellement observées :

- access token : `2026-09-01T18:29:47+00:00` ;
- refresh token : `2026-10-01T18:09:12+00:00`.

La commande `health` expose ces deux dates sans exposer les jetons. L’OAuth
manuel reste nécessaire avant l’expiration du refresh token si AliExpress ne
le prolonge pas lors des renouvellements. C’est une contrainte OAuth officielle,
pas un blocage technique du sourcing.

## Tests

- Serveur `/Users/Hakim/aliexpress-mcp-server` : **224 tests passants** en local
  et **224 tests passants** dans l’image construite sur le VPS.
- Sous-ensemble sourcing Codex : **24 tests passants** ; dépôt pipeline :
  **38 tests passants**.
- `git diff --check` : passant localement et sur le VPS.
- Image Docker reconstruite puis relancée : conteneur `healthy`.
- Gateway testé depuis le Mac : `health`, `search`, `variants`, `exact`.
- Dernière requalification exacte après le déploiement final :
  `2026-08-02T18:40:20+00:00`, résultat inchangé.
- Refresh token testé live, puis timer systemd testé en mode sans rotation.

## Frontière d’autorisation

Le gateway est strictement en lecture. Il ne sait ni importer dans DSers, ni
modifier Shopify, ni ajouter au panier, ni commander, ni payer, ni écrire à un
fournisseur. Ces opérations restent des étapes humaines séparées.

Une offre techniquement qualifiée n’est pas automatiquement une offre à lancer.
Le pipeline doit encore appliquer les critères commerciaux : demande France,
concurrence, marge, historique fournisseur, conformité, SAV et vérité produit.

## Ce qui reste à faire seulement au niveau commercial

- Filtrer les résultats de recherche bruités et scorer les candidats.
- Refuser ou accepter explicitement les fournisseurs à faible historique.
- Après validation humaine du produit, importer l’URL exacte dans DSers.
- Ne publier sur Shopify qu’après contrôle du mapping SKU et autorisation.

Apify, proxy anti-bot, scraping de fiche, contournement CAPTCHA et exposition
publique du MCP ne font pas partie de cette solution.

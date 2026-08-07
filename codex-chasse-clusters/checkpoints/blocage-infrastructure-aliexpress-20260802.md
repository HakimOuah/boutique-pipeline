# Checkpoint — accès live AliExpress depuis une IP autorisée

Date : 2026-08-02 17:32 WEST

## Statut

`BLOQUE_ACCES_INFRASTRUCTURE — PROTOTYPE ET TESTS LOCAUX VALIDES`

La solution officielle sans Apify est implémentée et testée, mais la preuve
live demandée ne peut pas être exécutée depuis l'état externe actuel.

## Preuves répétées sur trois reprises consécutives

1. Un appel signé réel à `aliexpress.ds.product.get` avec les identifiants de
   `/Users/Hakim/aliexpress-mcp-server/.env` a atteint AliExpress puis renvoyé
   `AppWhiteIpLimit` depuis l'IP publique du Mac `195.23.150.51`.
2. Le même appel a été relancé le 02/08 à 17:18 WEST et a renvoyé le même refus.
3. Le même appel a été relancé le 02/08 à 17:31 WEST et a encore renvoyé le
   même refus.

Le contrôle réseau et d'accès réalisé après le troisième essai confirme :

- l'agent SSH local n'a aucune identité ;
- `~/.ssh` ne contient que `config` et `known_hosts` ;
- `/`, `/mcp` et `/oauth/aliexpress/callback` renvoient `404` sur
  `https://srv1575867.hstgr.cloud` ;
- le port MCP `8080` reste volontairement privé ;
- la session hPanel disponible redirige toujours vers
  `https://auth.hostinger.com/login` ;
- aucun connecteur ou API Hostinger n'est disponible dans cette session.

## Ce qui est validé

- `/Users/Hakim/aliexpress-mcp-server` : 210 tests passants ;
- `tools/aliexpress_open_api.py` et `tools/aliexpress_vps_exact_probe.py` :
  21 tests passants ;
- sélection de variante par propriétés isolées, avec refus des ambiguïtés ;
- refus d'un stock manquant ou nul ;
- fret calculé avec l'identifiant SKU numérique vers `FR` ;
- aucun scraping, CAPTCHA, proxy anti-bot, commande, panier ou mutation.

## Déblocage minimal

Une seule des deux actions suivantes suffit :

1. Hakim se connecte à hPanel dans l'onglet Hostinger laissé ouvert, puis
   indique `c'est fait`. Codex exécutera la sonde dans le conteneur depuis
   l'IP VPS déjà whitelistée `148.230.118.152`.
2. Hakim ajoute temporairement `195.23.150.51` à l'IP Whitelist de
   l'application AliExpress `Hermes DropPilot`, puis indique `c'est fait`.
   Codex exécutera directement `qualify` depuis le Mac.

La reprise doit ensuite vérifier l'article `1005010249362754`, sélectionner un
seul SKU correspondant à `white sterile` + `36mm-glass back`, exiger un stock
strictement positif, puis obtenir au moins une option de livraison France.


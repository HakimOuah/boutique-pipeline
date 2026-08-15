# Prévol AliExpress officiel — six univers

- Date : **2026-08-15**
- Heure du contrôle live : **2026-08-15T16:47:55Z**
- Périmètre : infrastructure et contrats de lecture uniquement.
- Univers concernés à terme : parure de lit, bouillottes, globe/cartographie, astronomie, gothique/emo, ésotérisme.
- Interdits respectés : **aucun Chrome, aucun DSers, aucun Shopify, aucun panier, aucune commande, aucun paiement, aucun message vendeur, aucun sourcing commercial des six univers**.

## 1. Verdict opérationnel

**`PREFLIGHT_API_READ_ONLY_PASS_WITH_LIMITS`**

La route officielle AliExpress Open Platform via VPS est joignable et son OAuth est valide au moment du contrôle. Le client local n'expose que quatre actions : `health`, `search`, `variants`, `exact`. Le code inspecté ne contient aucune méthode de panier, commande, paiement, message fournisseur, import DSers ou mutation Shopify/catalogue.

Ce PASS valide uniquement la **capacité technique de lecture**. Il n'autorise pas le sourcing des six univers, ne qualifie aucun fournisseur et ne prouve aucun SKU, prix rendu ou fret France pour ces niches.

## 2. Architecture observée

Chemin canonique :

```text
Mac
  -> client Python local aliexpress_vps_gateway.py
  -> SSH BatchMode avec clé dédiée et hôte vérifié
  -> commande forcée OpenSSH sur VPS à IP autorisée
  -> gateway JSON allowlisté
  -> AliExpress Open Platform / AE-Dropshipper
```

Fichiers inspectés :

- `codex-chasse-clusters/tools/aliexpress_vps_gateway.py` ;
- `codex-chasse-clusters/tools/aliexpress_open_api.py` ;
- `codex-chasse-clusters/tools/aliexpress_vps_exact_probe.py` ;
- `codex-chasse-clusters/tests/test_aliexpress_vps_gateway.py` ;
- `codex-chasse-clusters/reports/infrastructure-sourcing-aliexpress-20260802.md` ;
- scripts historiques de collecte dans `codex-chasse-clusters/runs/2026-08-08-*`, inspectés mais **non exécutés**.

### OBSERVÉ

- Le client local construit une liste d'arguments `ssh` et appelle `subprocess.run(...)` sans `shell=True`.
- La requête est sérialisée en JSON et transmise sur stdin ; aucune commande distante n'est construite depuis la requête utilisateur.
- Options SSH présentes : `-T`, `IdentitiesOnly=yes`, `BatchMode=yes`, `StrictHostKeyChecking=yes`, `ConnectTimeout=10`.
- La clé dédiée `/Users/Hakim/.ssh/aliexpress_sourcing_vps_ed25519` existe, est en mode **600** et le fichier `known_hosts` existe.
- Le nom d'hôte et l'utilisateur sont validés par expressions régulières avant l'appel SSH.
- Les seules sous-commandes locales sont `health`, `search`, `variants`, `exact`.
- Le client API officiel ne déclare que des méthodes de lecture produit/SKU/livraison :
  - `aliexpress.affiliate.product.sku.detail.get` ;
  - `aliexpress.affiliate.product.shipping.get` ;
  - `aliexpress.ds.product.get` ;
  - `aliexpress.ds.freight.query`.
- Le module annonce explicitement ne contenir aucune fonction de panier, commande, paiement, message fournisseur ou mutation de catalogue.

### MANQUANT

- Le contenu actuel de la commande forcée dans `authorized_keys`, les permissions du `.env` distant, l'état Docker/systemd et les journaux VPS n'ont pas été relus directement pendant ce prévol. Ils sont documentés dans le rapport du 02/08, mais cette preuve historique peut dériver.
- Le fingerprint actuel de la clé et l'entrée exacte de `known_hosts` n'ont pas été imprimés afin de ne pas multiplier les données d'infrastructure dans les sorties.

## 3. Commandes sûres

Exécuter depuis la racine du dépôt, sans redirection vers un fichier et sans surcharge `--host`, `--user` ou `--identity` :

```bash
# 1. Santé : seule commande requise pour un prévol
python3 codex-chasse-clusters/tools/aliexpress_vps_gateway.py health

# 2. Découverte générique, seulement après passage du gate marché
python3 codex-chasse-clusters/tools/aliexpress_vps_gateway.py \
  search "requête produit précise" \
  --limit 5 \
  --destination FR \
  --sort-by orders

# 3. Lecture de toutes les variantes d'un ID produit numérique déjà retenu
python3 codex-chasse-clusters/tools/aliexpress_vps_gateway.py \
  variants 1005000000000000

# 4. Qualification fermée d'une variante exacte et de son fret France
python3 codex-chasse-clusters/tools/aliexpress_vps_gateway.py \
  exact 1005000000000000 \
  --property "valeur exacte 1" \
  --property "valeur exacte 2" \
  --destination FR
```

Les IDs et propriétés ci-dessus sont des placeholders. Ils ne doivent pas être envoyés tels quels.

### Séquence sûre obligatoire après validation marché

1. `health` ;
2. `search` limité pour obtenir des IDs candidats, sans conclure ;
3. `variants <product_id>` pour voir chaque SKU, ses propriétés, son prix et son stock ;
4. choisir une combinaison de propriétés explicite ;
5. `exact <product_id> --property ... --destination FR` ;
6. contrôler l'image SKU, le titre, la marque/watermark, les propriétés, le SKU numérique, le stock, le vendeur et chaque option de fret ;
7. conserver le statut `PREUVE_FOURNISSEUR_INCOMPLETE` tant que l'ensemble n'est pas cohérent.

## 4. Contrôles live réalisés

### 4.1 Santé

Commande exécutée :

```bash
python3 codex-chasse-clusters/tools/aliexpress_vps_gateway.py health
```

Sortie utile observée, sans secrets :

```json
{
  "ok": true,
  "action": "health",
  "checked_at_utc": "2026-08-15T16:47:55+00:00",
  "access_token_expires_at_utc": "2026-09-01T18:29:47+00:00",
  "refresh_token_expires_at_utc": "2026-10-01T18:09:12+00:00"
}
```

**OBSERVÉ :** transport SSH, gateway distant et état OAuth répondent correctement. Aucun jeton, secret d'application ou signature n'est retourné.

**LIMITE :** `health` ne prouve pas qu'une recherche textuelle précise sera pertinente, qu'un ID existe encore, qu'un SKU est en stock ou que le fret France est disponible.

### 4.2 Recherche générique innocente

Une seule formulation générique, étrangère aux six niches, a été utilisée ; elle a été relue une seconde fois uniquement pour décrire la structure de la réponse sans afficher de produit :

```bash
python3 codex-chasse-clusters/tools/aliexpress_vps_gateway.py \
  search "wooden pencil holder" \
  --limit 1 \
  --destination FR \
  --sort-by orders
```

Résultat synthétique :

```json
{
  "ok": true,
  "action": "search",
  "result.destination": "FR",
  "result.source_key_present": true,
  "result.items_count": 0
}
```

**OBSERVÉ :** l'action de recherche s'exécute sans erreur de transport ni d'authentification. Aucun article des six univers n'a été recherché et aucun candidat commercial n'a été créé.

**LIMITE :** zéro résultat n'est pas une preuve d'absence d'offre. La recherche Open Platform peut être bruitée, sensible à la formulation, ou retourner `IOPUpstreamError` / `EXCEPTION_TEXT_SEARCH_FOR_DS`. Dans ces cas, resserrer la requête ou partir d'un ID déjà connu ; ne jamais traduire une erreur API en verdict marché.

### 4.3 Tests locaux

- `py_compile` passe pour les trois modules Python inspectés.
- La suite `codex-chasse-clusters/tests/test_aliexpress_vps_gateway.py` n'a pas pu être exécutée dans le Python courant : module `pytest` absent.
- Le test source inspecté couvre : absence de commande shell distante, rejet des métacaractères dans l'hôte, JSON sur stdin et allowlist des modes de tri.

Le manque de `pytest` est une limite d'environnement local, pas une panne du gateway live. Il reste à rejouer la suite dans le runtime de développement qui contient pytest avant toute modification du client.

## 5. Preuve d'absence de mutation

### OBSERVÉ dans le chemin exécuté

- `health` et `search` ne reçoivent aucun paramètre d'achat, de panier, d'adresse détaillée, de paiement, de message ou d'import.
- Le gateway local imprime la réponse sur stdout ; il n'écrit aucun fichier.
- Le contrôle n'a appelé ni `variants` ni `exact`, car aucun produit commercial n'avait à être qualifié.
- Aucun script DSers ou Shopify n'est importé ou appelé par `aliexpress_vps_gateway.py`.
- Le contrôle ciblé `git status` après rédaction montre uniquement ce nouveau rapport ; `run-state.json` et `registre-candidats.codex.md` sont inchangés par le prévol.

### Scripts volontairement non exécutés

Les collecteurs historiques suivants utilisent le gateway en lecture côté AliExpress, mais écrivent des JSON locaux et lancent de nombreuses requêtes, parfois en parallèle :

- `runs/2026-08-08-kraken-catalogue-v1/collect_aliexpress.py` ;
- `runs/2026-08-08-kraken-catalogue-v1/probe_representatives.py` ;
- `runs/2026-08-08-kraken-catalogue-expansion-v2/source_aliexpress_catalogue.py` ;
- `runs/2026-08-08-kraken-catalogue-expansion-v2/collect_anchor_suppliers.py`.

Ils ne conviennent pas à ce prévol : leur exécution aurait lancé un sourcing commercial prématuré et créé d'autres fichiers. Aucun n'a été lancé.

### MANQUANT

- Une preuve absolue du code distant courant exigerait un audit SSH privilégié du serveur et de son image. La preuve présente combine le contrat client, la commande forcée documentée au 02/08, le test live allowlisté et l'absence de changement local hors rapport.

## 6. Limites exactes par niveau de preuve

| Niveau | Ce qu'il prouve | Ce qu'il ne prouve pas |
|---|---|---|
| `health` | SSH, réponse du gateway, échéances OAuth non secrètes | disponibilité produit, pertinence recherche, stock, prix, vendeur, fret |
| `search` | découverte d'IDs/titres et signaux bruts renvoyés par l'API | SKU exact, exactitude visuelle, marque, stock ferme, prix de la variante, fret France |
| `variants` | inventaire des SKU/propriétés, prix/stock exposés par la fiche | sélection univoque, conformité visuelle, option de livraison France, coût rendu |
| `exact` | un SKU unique correspondant aux propriétés, stock positif et réponse fret pour `destination=FR` | livraison à un code postal précis, stabilité future du stock/prix, qualité réelle, conformité, marge, SAV, droit de vendre |

### SKU et variantes

- L'ID produit doit être numérique.
- Une qualification exacte exige au moins une propriété et doit produire **exactement un** SKU correspondant.
- Zéro ou plusieurs correspondances doivent être un échec, jamais une sélection au hasard.
- Les libellés AliExpress peuvent être incohérents. La preuve minimale combine `sku_id`, `sku_attr`, toutes les propriétés et l'image du SKU.
- Une couleur ou un titre ne prouve pas la matière, la taille, la composition, les symboles, l'absence de licence ou la conformité.
- Le stock doit être numérique et strictement positif au moment de la lecture ; il reste volatil.

### Fret France

- Le fret est interrogé seulement après sélection d'un SKU exact, pour quantité 1 et `shipToCountry=FR`.
- La requête actuelle laisse province et ville vides : elle prouve une option France générique, **pas** la desserte d'un code postal précis ni DOM-TOM/Corse.
- Il faut conserver chaque option : frais, devise, gratuité, origine, suivi, stock disponible, délai minimal/maximal ou date annoncée.
- Le coût rendu ne doit être calculé qu'avec le prix du **même SKU** et une option de livraison réellement disponible.
- Prix, taxes, stock, entrepôt et délais sont un instantané API ; ils doivent être relus avant toute décision ultérieure.

### Recherche textuelle

- La recherche est une découverte, pas une qualification.
- Les résultats peuvent être bruités ou vides ; le titre peut masquer une variante d'appel non pertinente.
- Les requêtes des six univers ne doivent commencer qu'après passage du gate marché/prix et avec des mots rares dérivés des collections validées.

### Qualité, conformité et commerce

Même `exact` ne prouve pas :

- note et historique suffisants du vendeur au moment de décider ;
- authenticité des avis/ventes ;
- qualité à réception, dimensions réelles ou solidité du colis ;
- CE/GPSR, tests électriques/jouets/textiles, composition ou licences ;
- droit d'utiliser les images ;
- marge contributive ;
- import DSers, mapping Shopify, commande test ou GO lancement.

## 7. Frontière pour les six univers

| Univers | Prévol technique | Autorisation de sourcing |
|---|---|---|
| Parure de lit | Gateway disponible | **NON** — attendre volume/SERP/prix ; ensuite vérifier taille FR, composition et SKU exact |
| Bouillottes | Gateway disponible | **NON** — attendre gate panier et filtre sécurité ; séparer eau, sèche, électrique |
| Globe/cartographie | Gateway disponible | **NON** — attendre mesure du périmètre légitime ; fret volumétrique et variante exacte requis |
| Astronomie | Gateway disponible | **NON** — télescope reste STOP sans thèse nouvelle ; déco astro exige filtre laser/électrique |
| Gothique/emo | Gateway disponible | **NON** — attendre marché ; exclure licences et contrôler chaque motif/variante |
| Ésotérisme | Gateway disponible | **NON** — attendre marché ; zéro claim santé/protection et séparation des produits réglementés |

## 8. Conclusion

La route officielle est **opérationnelle en lecture seule** au 15/08/2026. La commande sûre immédiate est `health`. Les trois autres actions ne doivent être utilisées qu'après validation du marché et dans l'ordre `search -> variants -> exact`.

Le prévol n'a produit aucune preuve fournisseur pour les six univers et n'a déclenché aucune mutation externe. Le prochain passage autorisé reste la mesure marché/prix ; le sourcing commercial n'est pas ouvert par ce rapport.

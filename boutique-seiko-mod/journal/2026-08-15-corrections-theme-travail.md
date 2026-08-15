# Corrections sur le thème de travail — rapport de publication

> **15/08/2026, après-midi.** Boutique **Maison Noirmont**. Toutes les écritures ont été faites sur le
> thème de travail **« TRAVAIL 15-08 — correctifs »** (`gid://shopify/OnlineStoreTheme/205451100498`,
> rôle `UNPUBLISHED`), dupliqué par Hakim depuis le thème live. **Le thème publié `Noirmont`
> (`205089014098`) n'a pas été touché. Aucune publication de thème** : c'est la décision de Hakim.
> Aucun produit, prix, politique ni page n'a été modifié.
>
> Chaque fichier a été sauvegardé avant modification dans
> [`backups/2026-08-15-theme-travail/`](../backups/2026-08-15-theme-travail/), chaque écriture a été
> vérifiée par empreinte **et** par relecture du contenu distant octet par octet, puis le rendu réel a
> été contrôlé en aperçu anonyme (`?preview_theme_id=205451100498`, thème confirmé par
> `Shopify.theme.id` dans la page servie).

---

## Les 7 fichiers modifiés, empreintes à l'appui

| Fichier | md5 avant | md5 après | Ce qui change |
|---|---|---|---|
| `snippets/organization-schema.liquid` | `80c9abb955954b2a3f03704a779fc56c` | `92ecc853d43736169bc5fea79c943126` | Ligne 48 : `]{% endif %}` → `],{% endif %}` ; ajout du fermeur inconditionnel `"@id"` (`request.origin` + `/#organization`) ; ajout de **`"legalName": "OH Ventures"`** |
| `templates/product.json` | `757bf57312ee939caa89f6e99ae7da01` | `166e88fe3b5d21d62c1514c5fee9b30c` | 2 accordéons « Garantie 12 mois » alignés sur la politique ; bandeau `iwt_pdp5` → « Paiement sécurisé » ; tirets cadratins retirés (accordéons Contact et Livraison) |
| `templates/index.json` | `d3225aef697957114651c0884ad57a29` | `9485ad5a56dd60ae0508ecc2793cac5e` | 3 tirets cadratins retirés des textes de l'accueil (bannière, accessoires, manifeste) |
| `templates/cart.json` | `a2c9ef8103b8ec09f59102dc45484bd3` | `c100a1c5554087cac885489eeeb92f95` | Intitulés « Retours : 14 jours » et « Livraison offerte et suivie » ; bannière « Livraison offerte et suivie en France » |
| `sections/cart-drawer-group.json` | `74e68bbb74c9a0317f35c3b94e349346` | `a0ca330989e74c09fe92e87d84c4dc00` | Même bannière corrigée dans le tiroir panier |
| `templates/page.configurateur.json` | `119029b17a947449e93729aab56da6d3` | `44bccb5951750619b0e9e6a34d669bb3` | Promesse du configurateur : « Votre boîtier, votre cadran : nous révélons la montre qui les porte. » |
| `config/settings_data.json` | `db55201a7fb4da442e1e65b081eaed3d` | `a9d9ce4957b428a70e6fe8f4987784d3` | `force_icons_display` : `true` → `false` — les icônes de paiement suivent désormais `shop.enabled_payment_types` au lieu des cases manuelles |

Rien d'autre n'a été écrit. `blocks/noirmont-confiance.liquid` et `sections/footer-group.json` n'ont
**pas** été modifiés : Hakim les avait déjà corrigés avant la duplication (vérifié — 48 h, garantie
« sur le mouvement », pied de page complet avec OH Ventures, adresse, SIRET, `tel:`).

---

## Ce qui change pour un visiteur, correction par correction

### 1. JSON-LD `Organization` (accueil) — réparé et enrichi

Le défaut du gabarit (virgule orpheline quand `sameAs` est vide) est corrigé exactement comme prévu
au [journal du diagnostic](2026-08-15-json-ld-organization.md), plus un ajout : **`legalName`**.

**Vérifié en rendu réel** (aperçu du thème de travail, parseur JSON strict) :

```
OK  Organization
    "legalName": "OH Ventures"
    "@id": "https://maisonnoirmont.fr/#organization"
    "telephone": "+33 7 56 82 80 94"   ← shop.phone est bien rempli, la ligne sort
```

Le bloc entier redevient lisible par Google : nom, **raison sociale** (celle que Merchant Center
vérifiera), adresse, téléphone, e-mail, logo. Le gabarit ne peut plus casser sur un champ vide, ni
aujourd'hui ni si un réseau social est ajouté plus tard (les deux cas ont été simulés et validés).

### 2. Garantie — plus aucune surpromesse sur les fiches

Les deux accordéons « Garantie 12 mois » de chaque fiche (bloc principal + section « Besoin
d'aide ? ») disent désormais, comme la politique de remboursement §7 et l'art. 10 des CGV :

> Chaque garde-temps est garanti 12 mois sur son mouvement interne. En cas de panne du mouvement,
> on répare ou on remplace. Le bracelet, le verre et le boîtier ne sont pas couverts par cette
> garantie commerciale, qui s'ajoute à vos garanties légales.

**Vérifié en rendu** : « couronne, aiguilles » = 0 occurrence sur les fiches testées ; « mouvement
interne » = 3 (2 accordéons + le bloc sous le prix, déjà juste). Les cartes de confiance et le pied
de page étaient déjà corrigés par Hakim. **Le site ne promet plus nulle part au-delà du contrat.**

### 3. Bandeau défilant — « Paiement sécurisé » au lieu du paiement fractionné

Hakim avait déjà remplacé « Paiement en 4 fois » par « Paiement en plusieurs fois ». Mais ce texte
restait faux sous 30 € : sur les fiches à 12,90 €, le bloc dynamique se masque et aucun prestataire
ne fractionne. Le bandeau tourne sur **toutes** les fiches, il lui fallait un message vrai à tout
prix : **« Paiement sécurisé »** (icône carte bancaire conservée) — déjà prouvé sur ce site (HTTPS,
HSTS, caisse Shopify) et déjà utilisé mot pour mot dans les réassurances du pied de page.

Le bandeau lit donc : Qualité Premium · Calibre annoncé · Livraison offerte en France · Garantie
12 mois · **Paiement sécurisé**. Le bloc dynamique sous le prix continue seul de parler de paiement
en plusieurs fois, avec ses garde-fous (seuil 30 €, logos tirés de la caisse réelle).

**Vérifié en rendu** : « Paiement en 4 fois » = 0 partout ; sur la fiche à 12,90 €, plus aucune
mention de paiement fractionné (`mn-fractionne` absent) ; sur la fiche à 378 €, le bloc dynamique
est là.

### 4. Promesses de délai — balayage complet : rien à corriger

Grep sur les corps des 260 fichiers du thème de travail (`24 h`, `24h`, `sous 24`, `dans les 24`,
`18 h`, `18h`), SVG et coordonnées exclus : **0 promesse de délai codée en dur**. Les passes de
Hakim ont tout couvert, y compris les deux lignes de `noirmont-confiance.liquid`. Les seuls « 24 »
restants sont des `viewBox`/tracés SVG et des valeurs CSS. Les « 48h ouvrées » servis : 5 par fiche,
tous cohérents.

### 5. Repasse finale — corrigé ou signalé

**Corrigé (thème)** :
- **8 tirets cadratins** dans des textes clients (accueil ×3, fiche ×2, panier ×2 + bannière ×2 en
  double panier/tiroir, configurateur ×1) — remplacés par virgule, deux-points, point ou parenthèses,
  sans changer le sens (`STYLE-REDACTION.md`).
- **Icônes de paiement** : la case « affichage manuel » était active dans la copie
  (`force_icons_display: true`) alors que l'audit du midi croyait l'automatique en place. Passée à
  `false` : rendu **identique aujourd'hui** (vérifié : Visa, Mastercard, Amex, Apple Pay, PayPal,
  Shop Pay, Klarna — Google Pay absent), mais si un moyen de paiement change en caisse, les icônes
  suivront toutes seules. Si Hakim préfère le mode manuel, une case à recocher dans le
  personnalisateur suffit.

**Vérifié sain (thème)** : 0 avis/note/badge actif (tous les blocs d'avis fabriqués restent
`disabled: true`, inchangés) ; 0 compte à rebours sur les pages publiques (le seul est sur la page
mot de passe, non servie) ; 0 « Klarna »/« Google Pay » codé en dur dans un rendu ; 0 `904L`,
0 `SWISS`, 0 allégation d'étanchéité (le thème n'a aucun métachamp d'étanchéité, conforme au
commentaire de `noirmont-specs.liquid`).

**Signalé, hors thème ou laissé en l'état** :
- Les tirets cadratins restants du rendu viennent des **données produit** (titres « Voyageur Or —
  GMT… », alt d'images, vignettes d'upsell) — pas du thème. À traiter avec l'arbitrage
  « Président/Présidentiel » (point A d'`A-FAIRE-HAKIM.md`) pour ne réécrire les titres qu'une fois.
- « **Qualité Premium** » (1er élément du bandeau) : allégation invérifiable au sens strict, tolérée
  par trois audits. À remplacer un jour par un fait (« Calibre japonais », « Verre saphir » quand
  c'est vrai) — arbitrage de Hakim, pas exécuté.
- Blocs dormants toujours présents mais désactivés : `reviews_badge_*` (« 4,8/5 · 1340 avis »),
  étoiles `rating: 4.5`, 12 témoignages écrits, « Guide des tailles » en Lorem ipsum, fichier
  `blocks/noirmont-4x.liquid` (plus référencé nulle part). Ils ne rendent rien ; le risque documenté
  reste : toute réactivation les publierait.
- Dates de version des politiques et collections < 5 produits : réglages et politiques, hors thème
  (points 7 et 8 d'`A-FAIRE-HAKIM.md`).

---

## Méthode d'écriture — et une recette neuve pour les gros fichiers

Écritures par `themeFilesUpsert` sur `205451100498` uniquement. Le piège documenté s'est confirmé :
**`upsertedThemeFiles: []` sans erreur alors que l'écriture a réussi** (constaté sur le lot
product/index/cart-drawer). Chaque écriture a donc été vérifiée par empreinte avant/après **et** par
diff du contenu distant contre la copie locale : **7/7 identiques octet pour octet**.

Pour les trois fichiers trop gros pour être retapés sans risque (79 à 92 Ko), le corps est passé par
**`stagedUploadsCreate` + `curl` depuis le disque + `themeFilesUpsert` en `body { type: URL }`** :
zéro retranscription, fidélité garantie. Recette à retenir pour toute écriture de thème volumineuse.

---

## Checklist de pré-publication — à contrôler en aperçu avant de publier

Aperçu : Boutique en ligne → Thèmes → **TRAVAIL 15-08 — correctifs** → Aperçu.

1. **Une fiche montre** (ex. Voyageur Or GMT) : le bandeau défilant affiche « Paiement sécurisé » ;
   les deux accordéons « Garantie 12 mois » parlent du **mouvement interne** et citent les
   exclusions ; aucune mention « couronne, aiguilles ».
2. **Une fiche accessoire à 12,90 €** (barrettes) : aucune mention de paiement en plusieurs fois
   nulle part sur la page.
3. **Pied de page** : les 7 icônes de paiement sont bien là (Visa, Mastercard, Amex, Apple Pay,
   PayPal, Shop Pay, Klarna) — elles viennent maintenant de la caisse réelle.
4. **Panier** : bannière « Livraison offerte et suivie en France », accordéons « Retours : 14 jours »
   et « Livraison offerte et suivie ».
5. **Après publication**, valider le JSON-LD sur le vrai domaine :
   ```bash
   curl -s "https://maisonnoirmont.fr/?v=$RANDOM" | python3 -c 'import sys,re,json
   for b in re.findall(r"application/ld\+json[^>]*>(.*?)</script>",sys.stdin.read(),re.S):
       try: d=json.loads(b); print("OK ", d["@type"], d.get("legalName"))
       except Exception as e: print("KO ", e)'
   ```
   Attendu : `OK  Organization OH Ventures`. Puis coller l'URL dans le
   [test des résultats enrichis](https://search.google.com/test/rich-results).

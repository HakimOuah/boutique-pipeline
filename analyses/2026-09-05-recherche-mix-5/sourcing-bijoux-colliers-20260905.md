# Sourcing AliExpress — colliers / pendentifs pierres naturelles — 2026-09-05

## Cadre

PASS_PREQUALIFICATION lu : `PASS-bijoux-pierres.md`, candidat UNIVERS Shopping. La recherche fournisseur est limitée aux bijoux portés en lapis-lazuli, améthyste, pierre de lune ou agate. Les perles seules, accessoires de fabrication, arbres décoratifs et autres pierres ne comptent pas. Aucun claim de soin, chance ou protection n’est retenu.

Skill et vérification exacte lus avant action. Passerelle AliExpress VPS utilisée en lecture seule, destination FR. Aucun navigateur, panier, achat, contact, appel DataForSEO ou autre recherche payante.

Contrôle santé passerelle : OK, 2026-09-05 18:42:25 UTC.

## Requêtes distinctives et bruts

Trois requêtes distinctives ont été utilisées, chacune avec `limit=10`, destination FR et tri commandes :

- `lapis pendant` — [brut](<sourcing-bijoux-colliers-20260905-raw-lapis-pendant.json>)
- `amethyst necklace` — [brut](<sourcing-bijoux-colliers-20260905-raw-amethyst-necklace.json>)
- `moonstone pendant` — [brut](<sourcing-bijoux-colliers-20260905-raw-moonstone-pendant.json>)

Variantes et contrôle exacts :

- [variantes lapis](<sourcing-bijoux-colliers-20260905-raw-variants-lapis-1005010773460450.json>)
- [exact lapis FR](<sourcing-bijoux-colliers-20260905-raw-exact-lapis-1005010773460450.json>)
- [variantes résultat fluorite, rejeté du périmètre](<sourcing-bijoux-colliers-20260905-raw-variants-fluorite-1005008387449116.json>)

Recherche de reprise fournisseur, limitée à deux formulations supplémentaires :

- `CSJA lapis lazuli necklace` — [brut](<sourcing-bijoux-colliers-20260905-raw-csja-lapis-lazuli-necklace.json>)
- `CSJA amethyst pendant` — [brut](<sourcing-bijoux-colliers-20260905-raw-csja-amethyst-pendant.json>)
- [variantes EFXH du seul collier à pierre bleue retourné](<sourcing-bijoux-colliers-20260905-raw-variants-blue-stone-1005010617021740.json>)

Les recherches ont été relancées à l’identique uniquement pour persister les réponses brutes ; aucune nouvelle formulation distinctive n’a été ajoutée.

## Offre exacte trouvée

| Champ | Observation |
|---|---|
| Statut | **FOURNISSEUR À TESTER** — une seule fiche exacte, réserves fortes |
| Produit | Collier pendentif en lapis-lazuli bohème, forme larme, unisexe, tissé à la main |
| URL directe | https://fr.aliexpress.com/item/1005010773460450.html |
| Product ID | 1005010773460450 |
| Boutique | Shop4508021 Store, ID 4508021, pays vendeur CN |
| SKU exact | 12000053521414101 |
| Propriété retournée | Valeur `Lapis Lazuli`; `Couleur métal = Couleur or jaune clair` |
| Prix SKU | 3,79 € ; `tax_included=true` retourné par l’API |
| Stock SKU | 18 |
| Livraison FR | AliExpress Selection Standard / Cainiao, 1,99 €, expédition CN, suivi, 5–10 jours ; date affichée 10–15 septembre |
| Coût rendu observé | **5,78 €** = 3,79 € + 1,99 € de fret affiché. Ce n’est pas une marge ni un coût complet après retours, paiement, SAV ou publicité. |
| Preuve sociale | 126 ventes ; note produit 0,0 et 0 évaluation retournée |
| Indicateurs boutique | Article conforme 4,8 ; communication 4,8 ; vitesse d’expédition 4,8 |
| Composition | Le vendeur/API déclare la valeur « Lapis Lazuli » et la couleur de métal ; composition du métal, traitement, origine et authenticité de la pierre **MANQUANTS** |
| Confiance | A pour product ID, SKU, propriété, stock, prix et fret FR retournés par contrôle exact ; C pour l’authenticité/composition réelle |

La propriété est rapportée telle que retournée. Elle ne constitue ni certification de pierre naturelle, ni test d’alliage, ni preuve d’authenticité.

## Résultat par pierre / fournisseur

- **Lapis-lazuli :** une offre finie pertinente trouvée chez Shop4508021 Store. Aucun deuxième fournisseur distinct n’est retourné par les cinq requêtes.
- **Améthyste :** aucun collier/pendentif améthyste fini clairement retourné. Le premier résultat est un lot de perles œil de tigre/améthyste/quartz pour fabrication ; il est exclu comme perles seules. Les autres résultats sont des colliers génériques, zircon, fluorite ou métal sans améthyste déclarée.
- **Pierre de lune :** aucun article pierre de lune fini retourné. La liste est dominée par colliers génériques, acier, zircon, accessoires et perles de conditionnement.
- **Agate :** aucune requête distinctive dédiée n’a été ajoutée, pour respecter la limite de trois recherches ; aucune offre agate n’est donc attestée dans cette passe.

Le résultat fluorite retourné par la requête améthyste a été inspecté en variantes pour documenter le rejet : CSJA Jewelry Official Store, product ID 1005008387449116, titres et variantes « Fluorite »/« Purple Pendant », stocks élevés et prix 1,41–1,79 €. Il est **hors périmètre** car fluorite et ne peut pas servir de fournisseur améthyste, même si son titre traduit mentionne aussi quartz/pierre précieuse.

La reprise ciblée CSJA n’a pas produit de second fournisseur qualifiable. `CSJA lapis lazuli necklace` retourne surtout perles seules, bijoux génériques et un collier à « pierre bleue naturelle ». Les variantes de ce dernier (product ID 1005010617021740, boutique EFXH Store) ne retournent que des références métal N0547-x, sans valeur lapis, améthyste, pierre de lune ou agate : par exemple N0547-1 / SKU 12000052985449037 / stock 97 141 / prix de vente 2,47 €, propriété retournée « Couleur or jaune clair ». Offre rejetée, sans réétiquetage. `CSJA amethyst pendant` retourne les mêmes perles et colliers génériques ; l’offre CSJA inspectée reste explicitement fluorite.

## Décompte des appels

13 appels passerelle au total : 1 health, 5 formulations distinctives (3 premières + 2 ciblées CSJA), 3 reprises identiques uniquement pour persister les bruts des premières recherches, 3 lectures de variantes, et 1 contrôle exact. Les trois reprises sont comptées séparément et signalées ; les prochains bruts devront être persistés dès le premier appel.

## Décision et limites

Objectif de deux fournisseurs plausibles distincts : **non atteint**. Une fiche lapis exacte est exploitable pour une reprise de due diligence, mais sa preuve sociale produit est nulle dans la réponse et sa composition reste une déclaration vendeur. Les familles améthyste, pierre de lune et agate restent MANQUANTES.

Aucun fournisseur n’est retenu pour commande test. Les prix, le stock et le délai sont dynamiques et doivent être reconfirmés avant toute commande. Le contrôle exact ne prouve ni authenticité, ni conformité, ni qualité, ni livraison réelle.

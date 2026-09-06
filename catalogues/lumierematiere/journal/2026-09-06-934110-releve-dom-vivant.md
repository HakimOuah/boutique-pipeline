# 06/09/2026 — `934110` : Codex bloqué, relevé fait au navigateur réel

Brief envoyé à Codex en CLI (`briefs/2026-09-06-codex-934110-axes.md`).
Livraison : `livraisons-visuels-codex/2026-09-06-934110-axes.{json,md}`.

---

## 1. Codex : 5 réponses sur 5 en « introuvable »

Deux échecs successifs, aucun sur le contenu.

- **Premier envoi** : la config pointe `model = "gpt-6-astra"`, que la CLI 0.146.0 ne savait
  pas appeler. `400 invalid_request`. **La commande sortait en code 0 sans rien produire** —
  un échec silencieux. Relancé avec `-m gpt-5.6-terra`.
- **Second envoi** : abouti, mais Codex n'a pas pu atteindre le DOM vivant —
  *« accès CDP bloqué par permission sur son socket local »*. Il a marqué les cinq réponses
  `introuvable` plutôt que de déduire. **C'est le comportement demandé, et c'est la bonne
  réponse** : le brief interdisait explicitement de reconstituer.

Hakim a mis Codex à jour dans l'intervalle (CLI **0.153.4**).

## 2. Une fausse piste que le contrôle a tuée

Le `curl` de la PDP rend 76 Ko avec un `<title>` vide et aucun module SKU. J'ai failli
en conclure que le listing était mort. **Contrôle sur trois listings certainement vivants :
tous rendent la même coquille de ~76 Ko à titre vide.** Le curl ne prouve rien sur
AliExpress — les options sont montées côté client.

Puis, au navigateur réel, le premier chargement de `934110` a affiché
*« Sorry, the page you requested can not be found »*. **Deuxième fausse piste.** Contrôle
sur `147607` : la page se rend normalement. Rechargement de `934110` : elle se rend aussi.
C'était un échec de premier chargement, pas une fiche morte.

**Règle : sur AliExpress, ni un curl ni un seul chargement ne valent constat. Il faut le
rendu, et un témoin vivant à côté.**

## 3. Ce que dit le DOM vivant, enfin

Chrome était déjà en écoute CDP sur `127.0.0.1:9222` — le blocage venait du sandbox de
Codex, pas de la machine.

**Axe 1, nommé par le vendeur « Couleur du corps » — trois valeurs, inchangées depuis le 04/09 :**

| Valeur | Image | Stock AliExpress | Stock Shopify |
|---|---|---:|---:|
| `Yellow Travertine` | `S120f354….jpg` | 1 079 | 1 079 |
| `3000k-warm white` | `S2cd3e97….png` | 1 108 | 1 108 |
| `6000k-cold white` | `S2cd3e97….png` | 1 110 | 1 110 |

- **Pas de quatrième valeur.** La grille n'existe pas, le relevé du 04/09 était exact.
- **`173` et `175` sont deux SKU distincts** : stocks différents, suivis séparément. Ce ne
  sont pas des doublons. Seule **l'image** est partagée — le vendeur a réutilisé une photo.
- **Les trois stocks recoupent la boutique au chiffre près.** Le mapping DSers est bon.

**Axe 2 : le vendeur le nomme « Taille » et sa seule valeur est `3000K warm light`.**
Un axe intitulé « taille » qui contient une température, sans choix possible. Il ne peut
donc pas être ce qui livre du 6000 K.

## 4. Ce qui reste ouvert, et pourquoi je n'ai pas touché aux libellés

L'axe s'appelle **« Couleur du corps »**. Dans la taxonomie du vendeur, `3000k-warm white`
et `6000k-cold white` sont donc des **couleurs de corps**, pas des températures — et les
deux partagent la photo du modèle deux tubes en blanc.

Deux lectures tiennent encore :

- ce sont deux corps blancs, que le vendeur a étiquetés avec des températures ;
- ce sont deux températures, que le vendeur a posées sur le mauvais axe.

La boutique affiche aujourd'hui « Deux tubes · blanc chaud 3000 K » et « Deux tubes ·
blanc froid 6000 K ». Le « Deux tubes » est prouvé par l'image. **La température ne l'est
pas**, et le nom de l'axe la contredit. Un client qui choisit 6000 K peut recevoir autre
chose. **Décision commerciale → Hakim.** Rien modifié.

Non obtenus : les cotes (tube, entraxe, rosace) et une phrase fournisseur disant
explicitement que l'ampoule est fournie.

## 5. Correction de mon propre travail sur `147607`

En prenant `147607` comme témoin, sa PDP vivante a montré deux choses que je n'avais pas :

- le titre vendeur se termine par **« lustre suspendu E27 »** ;
- l'axe « Couleur d'émission » a **deux** valeurs, `Warm light 3000K` et
  `Neutral light 4000K` — la boutique n'en vend qu'une.

Hier j'ai écrit sur cette fiche **« LED intégrée et fournie »**, sur un raisonnement
géométrique : un bloc de 6,5 cm ne peut pas loger une E27. Le titre du fournisseur dit E27.
**Mon argument était une déduction, pas une preuve, et il est contredit.**

Ce qui reste solide : **une source est bien fournie** — on ne choisit pas une couleur
d'émission qui ne serait pas livrée. Ce qui ne l'est pas : intégrée ou sur douille.

**Corrigé dans le sens du vrai commun aux deux lectures** : « Source : ampoule blanc chaud
3000 K fournie », et l'`installation` comme la FAQ ne disent plus « rien à visser » ni
« rien à remplacer ensuite ». La fiche n'affirme plus que la source est scellée.

---

## Contrôle

51 produits publiés, 158 variantes, SKU DSers intacts. Onglet navigateur refermé.

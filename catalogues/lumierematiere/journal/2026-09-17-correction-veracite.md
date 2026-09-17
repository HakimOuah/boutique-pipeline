# 17/09/2026 — Correction de véracité après la suspension GMC

Suite de `shopify/AUDIT-GMC-POST-SUSPENSION-2026-09-17.md`. Hakim : « les retours partent en France,
modifie tout ce qu'il faut et surtout dans le skill gmc-acceptance ajoute tous les éléments ».

## Mesure

Scan de véracité (nouveau script du skill) sur le site public + les métachamps des 51 fiches :

| | Bloquants | Alertes |
|---|---:|---:|
| Avant | 47 | 1 |
| Après les écritures API | **14** | 18 |

Les 14 restants sont **tous** dans le thème publié (6) et les politiques (8) — deux zones que le
connecteur refuse d'écrire. Ils disparaissent quand Hakim publie la copie de thème et colle les
politiques (`shopify/politiques-2026-09-17/A-FAIRE-HAKIM.md`). Les alertes sont des collections
sous 5 fiches et des mentions de matière dans la prose, relues une à une.

Fichiers : `shopify/scan-veracite-2026-09-17-avant.txt`, `…-apres.txt`.

## Écrit par l'API

**Fiches (51)**
- **30 titres** : 11 « pierre / travertin » → « effet pierre / effet travertin » ; 7 « laiton » →
  « dorée » ; « soie » → « tissu plissé » ; « noyer » → « bois foncé » ; nombres et couleurs qui ne
  valaient pas pour toutes les variantes (« 6 boules », « 5 anneaux », « fumé », « chrome », « noir »,
  « tambour ») ; `897170` → « rotin ou fibre synthétique ».
- **11 descriptions**, **95 métachamps** (+ 3 relectures) : FAQ « Quel délai » avec l'origine
  (« expédiée depuis l'entrepôt de notre fabricant partenaire, en Chine ») sur les 51 ; FAQ retour
  avec « vers une adresse en France » sur les 51 ; « C'est de la vraie pierre ? » supprimée ;
  « Du travertin, pas un placage » → « Un aspect travertin » ; jargon « photo / attribut
  fournisseur » retiré (3 fiches) ; « verre soufflé », « chanvre », « à la main », « fibre naturelle »
  retirés ; `435189` corrigée (ampoule fournie sur E27, pas LED intégrée) ; « plafonnier LED » retiré
  des deux fiches E27.
- **6 libellés de variantes** (`LEAVE_AS_IS`, SKU DSers intacts) : « Pierre claire » → « Clair »,
  4 × « Noyer » → « Teinte noyer », « Cuivre » → « Cuivré ».

**Pages** — Notre histoire (plus de « boutique parisienne », origine et retours dits, OH Ventures
nommée), FAQ (question « D'où partent les colis ? », « Qui est derrière Lumière Matière ? »,
procédure défectueux alignée sur la politique), Paiement (Maestro retiré, OH Ventures au relevé).

**Collections et menu** — « Suspensions pierre » → « Suspensions effet pierre » (titre, description,
SEO, menu « Effet pierre ») ; deux plafonniers E27 sortis de « Plafonniers LED » et sa description
corrigée ; « Osier » retiré du menu (collection de rotin) ; **15 descriptions** réécrites sur le
catalogue public (XXL gardait « 6 à 15 / 7 à 17 », Plafonniers cuisine disait « Toutes sont en
LED », Salon et Chambre décrivaient des brouillons).

**Thème** — copie `LM Véracité 2026-09-17` (`187309752656`), non publiée : home, panier, footer,
accordéon Livraison des fiches. Vérifiée en aperçu visiteur.

## Refusé par le connecteur → Hakim

Politiques (`write_legal_policies`), publication du thème, dépublication de 6 collections.
Mode d'emploi : `shopify/politiques-2026-09-17/A-FAIRE-HAKIM.md`.

## Non écrit, délibérément

- **DEEE / éco-participation** : l'afficher suppose un enregistrement auprès d'un éco-organisme ;
  l'écrire sans l'avoir fait serait un nouveau mensonge.
- **Directeur de la publication** : doit être une personne nommée ; laissé à Hakim.
- **« connecté RVB »** (`007557`) et « pilotable depuis une application » : non vérifié, signalé.

## Recette technique

`themeFilesUpsert` accepte `body.type = URL` pointant sur le `resourceUrl` d'un
`stagedUploadsCreate` (`FILE`, `text/plain`, `PUT`) : un `index.json` de 75 Ko passe sans être
recopié dans l'appel. `themeDuplicate` est autorisé. Tâche asynchrone : lire `job.done` puis relire.

## Skill `gmc-acceptance`

- `references/lexique-interdit.md` — termes et tournures interdits, avec remplacements (8 sections).
- `references/audit-lecons-lumiere-matiere.md` — le cas.
- `scripts/scan_veracite.py` — scan du site, des fiches, des métachamps et des collections.
- `SKILL.md` — seconde idée centrale, principes 5 et 6, erreurs à refus, porte avant campagne.
- `checklist-pre-soumission.md` — §6 bis « Audit de véracité ».

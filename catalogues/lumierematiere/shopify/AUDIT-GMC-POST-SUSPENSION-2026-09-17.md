# Audit post-suspension GMC — Lumière Matière — 17/09/2026

**Fait.** Compte Merchant Center accepté plusieurs jours, campagne lancée, compte suspendu le
lendemain pour **déclarations trompeuses** (misrepresentation).

**Méthode.** Site public lu comme un examinateur : texte intégral de la home, Notre histoire,
FAQ, contact, mentions légales, politiques d'expédition et de retour ; `products.json` (51 fiches)
croisé avec `catalogue-dsers.csv` (coûts AliExpress) ; checklist du skill `gmc-acceptance` §6
et leçons Noirmont.

**Verdict.** Le site raconte une entreprise qui n'existe pas : un revendeur parisien qui
contrôle, emballe et confie ses colis à Colissimo. La réalité est un dropshipping depuis la
Chine, photos générées, coefficient médian ×4,7. Le lancement de la campagne a déclenché un
examen plus poussé que la validation initiale, et ce récit ne le passe pas.

---

## 1. Le modèle d'activité est mal décrit — cause principale

| Où | Ce qui est écrit | La réalité |
|---|---|---|
| Notre histoire | « une **boutique en ligne parisienne**, au 47 rue Vivienne » ; « l'équipe est petite » | Siège social de domiciliation, partagé avec 3 autres boutiques |
| Politique d'expédition §4 | la préparation « couvre **le contrôle du luminaire, l'emballage et la remise au transporteur** » | Le fournisseur expédie ; aucun luminaire n'est contrôlé |
| Politique d'expédition §8 | colis confiés à « **Colissimo, DPD** et à des partenaires internationaux » | Fret AliExpress depuis la Chine |
| Remboursement §8 | « dès réception **et contrôle** » | Même remarque |
| Service client, partout | « l'équipe répond **de Paris** » | À valider par Hakim |

**Nulle part** le site ne dit d'où partent les colis. Un délai de 7 à 18 jours ouvrés, sans
origine annoncée, avec Colissimo cité en premier, laisse croire à un envoi depuis la France.
Google traite comme trompeuse l'omission d'une information qui change la décision d'achat.

L'adresse de retour n'est **communiquée qu'après la demande**. Si elle est en Chine, le client
ne sait pas qu'un retour « à ses frais » lui coûtera plusieurs dizaines d'euros.

## 2. La matière est surévaluée dans les titres

**11 fiches** portent « pierre » ou « travertin » dans le titre, qui alimente le flux et
l'annonce. Sur **6 d'entre elles, le corps de la fiche dit « effet pierre » et « composite à
grain minéral »**. La meta de la collection elle-même dit « Suspensions **effet pierre** en
**composite** » alors que le menu affiche « Pierre ».

Les 4 appliques et `092465` n'ont jamais été tranchées (ETAT #7 : pierre réelle ou résine ?
commande test jamais passée). Leurs titres affirment « pierre ».

## 3. Le site se porte garant de ce qu'il ne vérifie pas

- Home : « **La texture que vous voyez en photo est celle qui jouera avec la lumière chez
  vous** » — sous des rendus générés, sur des produits en composite.
- Home : bloc « **Ce qu'on regarde avant de mettre une pièce en ligne** » avec **3 icônes
  `verified`**. La checklist interdit l'icône verified ; aucun produit n'a été regardé en vrai.
- Notre histoire : « **Pas de vocabulaire flou : si c'est du rotin, c'est écrit.** » — sur un
  catalogue où « travertin » désigne un composite.

## 4. Le prix rend le reste visible

- Coefficient prix / coût AliExpress sur 43 fiches : **médiane ×4,7**, max **×10,3**
  (anneau LED à 149 € pour 14,49 €).
- **20 fiches sur 51 à exactement 199 €**, quel que soit le coût (de 20 € à 45 €).

Le prix n'est pas une infraction en soi. Mais une recherche d'image renvoie ces luminaires
sur AliExpress au cinquième du prix, avec des photos réelles moins flatteuses : c'est ce qui
transforme des rendus générés en « images trompeuses ».

## 5. Aggravant probable

**Même entité (OH Ventures), même adresse que Maison Noirmont**, suspendue le 23/08 pour le
**même motif** et fermée le 15/09. Google rapproche les comptes par identité vendeur. Non
prouvé comme cause, mais à traiter comme un facteur, et comme un **risque pour Tuftéo et
Bonum Vitae**, sur la même identité.

## 6. Conformité, hors motif GMC

- Aucune mention **DEEE / éco-participation** sur un catalogue d'appareils électriques.
- Mentions légales : directeur de la publication non nommé (« le président d'OH Ventures »).

## Ce qui tient

Coordonnées cohérentes partout (tél. unique, JSON-LD aligné), OH Ventures identifiée avec SIRET,
TVA et médiateur avec URL, délais identiques sur 51 fiches, 0 prix barré, TTC affiché,
retours 30 jours cohérents.

---

## Responsabilité

L'audit du 05/09 (`AUDIT-GMC-PRE-SOUMISSION-2026-09-05.md`) a conclu « le catalogue ne ment
plus nulle part ». Il a vérifié la **cohérence interne** (prix, délais, libellés, images de
variantes) et **pas la véracité du récit d'entreprise**. Le titre de `934110` —
« Suspension **travertin** cuisine » — a été écrit dans ce même passage, alors que la fiche
disait déjà « composite ». L'écart titre / corps a été vu le 07/09 et laissé en l'état.

## Ce qu'il faut faire avant toute demande de réexamen

1. **Arrêter la campagne.** Aucune dépense tant que le compte est suspendu.
2. **Dire le vrai modèle**, dans un ton vendeur : expédition directe par les fabricants
   partenaires, suivi international, origine hors UE. Retirer contrôle / emballage / Colissimo /
   DPD / « répond de Paris » si ce n'est pas vrai.
3. **Donner l'adresse de retour** dans la politique, et son coût réel si elle est hors de France
   — ou mettre en place une adresse de retour en France.
4. **Titres** : « effet pierre » / « effet travertin » sur les 6 composites ; même traitement
   sur les 5 fiches non tranchées tant qu'aucune pièce n'a été reçue. Collection renommée.
5. **Retirer** les 3 icônes verified, le bloc « Ce qu'on regarde… », la phrase sur la texture
   en photo et « Pas de vocabulaire flou ».
6. **Éco-participation / DEEE** : mention à ajouter.
7. **Prix** : décision de Hakim ; les fiches à ×7–10 sont les plus exposées.
8. **Commande test** : c'est la seule chose qui rend vrais « contrôle », « pierre » et
   « ampoule fournie ».
9. Seulement ensuite : **une** demande de réexamen, étayée, dans la fenêtre indiquée par Google.

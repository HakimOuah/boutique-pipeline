# Arborescence et wireframes — boutique rocking chair (PORTE 2, proposée le 14/09/2026, à valider par Hakim)

## Objectif CRO
- **Promesse** : *le fauteuil à bascule choisi pour les vraies nuits avec un bébé (on s'y assoit bien, on berce en douceur, on se relève sans réveiller personne) et assez beau pour rester au salon ensuite.*
- **Action dominante** : « Ajouter au panier » sur les fiches ; « Trouver mon fauteuil » en accueil.
- **Personas** (validés le 14/09) : Camille (allaitement, principal), Nicolas et Julie (coin lecture, déco), Martine (cadeau).
- **Objection principale** : « vais-je pouvoir me relever avec bébé dans les bras ? ». Viennent ensuite les accoudoirs et le dossier, le bruit, la place, l'entretien du tissu, le « meuble bébé moche », le montage et la livraison.
- **Offre** : 39 fiches, avec un cœur rocking chair et allaitement entre 179 et 329 €, une famille relax, et des accessoires entre 29 et 69 €. Livraison offerte, guide « bien choisir son fauteuil » offert en ligne, paiement en plusieurs fois.

## Catalogue et collections
Les volumes viennent de l'onglet « Rocking chair » du Sheet Niches SMP (SEMrush et OCB, 13-14/09). Un mot-clé principal par page. Les fiches sont les 39 fiches uniques de `catalogue-source-2026-09-14.json`.

| Collection (handle) | Mot-clé principal | Volume | Fiches |
|---|---|---:|---:|
| Accueil | rocking chair | 18 100 | — |
| fauteuil-a-bascule | fauteuil à bascule | 12 100 | 6 |
| fauteuil-allaitement | fauteuil allaitement | 5 400 | 4 |
| chaise-a-bascule | chaise à bascule | 2 900 | 4 |
| rocking-chair-exterieur | rocking chair extérieur | 1 900 | 4 |
| rocking-chair-bois-rotin | rocking chair bois | 1 300 | 3 |
| rocking-chair-design-scandinave | rocking chair design | 480 | 5 |
| fauteuil-cocon | fauteuil cocon | 590 | 3 |
| fauteuil-relax | fauteuil relax | 49 500 | 7 |
| fauteuil-relax-jardin | fauteuil relax jardin | 3 600 | 1 |
| rocking-chair-repose-pieds | fauteuil à bascule avec repose-pied | 320 | 2 |
| rocking-chair-enfant | fauteuil à bascule enfant | 390 | 2 |
| accessoires-rocking-chair | coussin rocking chair | 720 | 3 |

Une fiche peut appartenir à plusieurs collections. Les mots-clés secondaires de l'onglet servent aux titres des fiches, aux intros et aux textes d'aide au choix. On ne crée **aucune** fiche en double pour porter un mot-clé.

## Menu (6 entrées)
**Allaitement** · **Rocking chairs** (fauteuils à bascule, chaises à bascule, design et scandinave, bois et rotin, cocon) · **Relax** (relax, relax à bascule et repose-pieds, relax de jardin) · **Extérieur** · **Enfant** · **Guides**.

Header NoBrand (checklist, ajout du 15/09) : logo · Accueil · Contact · Suivre ma commande · Qui sommes-nous, en plus des entrées catalogue.

Pied de page : menu contact (e-mail, téléphone, adresse, lien Contact) · Suivre ma commande · Livraison et retours · Garantie et SAV · FAQ · Qui sommes-nous · Moyens de paiement · menu pages légales (retour et remboursement, livraison, CGV, confidentialité, mentions légales) · logo · badges de paiement et « Liens de politiques » cochés dans l'éditeur. Textes : `content/politiques/politiques-bercelou-nobrand-2026-09-15.md`.

## Wireframes — une action dominante par page

### Accueil
1. **Hero** : promesse et visuel composé (mère qui berce son bébé à la lumière d'une lampe, fauteuil teddy). CTA « Trouver mon fauteuil ». Trois puces : livraison offerte · guide pour bien choisir offert · paiement en 3 ou 4 fois.
2. **Trouver le fauteuil qui vous ressemble** : 4 cartes de moment de vie (Pour les tétées de nuit → Allaitement · Pour le coin lecture → Design et scandinave · Pour la terrasse → Extérieur · Pour se détendre → Relax).
3. **Ce qui fait un bon fauteuil à bascule** : 5 critères illustrés, repris du langage des mamans. On se relève facilement, les accoudoirs soutiennent les bras, le dossier soutient la tête, la bascule reste douce et discrète, la housse s'entretient facilement. Lien vers le guide.
4. **Best-sellers** : grille de 8 fiches, sans compteur de ventes.
5. **Du berceau au coin lecture** : texte court et visuel salon (objection « meuble bébé moche »).
6. **Réassurance** : livraison offerte · retours · garantie légale 2 ans · paiement sécurisé en plusieurs fois · service client français. Section avis conservée vide (chasse gardée de Hakim).
7. **FAQ courte** (5 questions).
8. **CTA final**.

### Fiche produit
- Galerie de 6 visuels composés : désir, usage, détail matière, dimensions cotées, situation salon ou chambre, détail patins ou mécanisme.
- Titre, prix, CTA sticky sur mobile.
- Bloc d'achat : 4 bénéfices et micro-copy livraison, retour et garantie.
- Description orientée douleur → réponse.
- Tableau de dimensions (assise, dossier, accoudoirs, encombrement) et tableau des caractéristiques.
- FAQ de 6 à 8 questions, puis réassurance.

### Collection
Intro de 60 à 100 mots · grille · texte d'aide au choix de 200 à 300 mots.

### Pages
- Guide « Bien choisir son fauteuil d'allaitement » (mot-clé : meilleur fauteuil allaitement, 110) ;
- Guide « Rocking chair : quelle taille et quelle place prévoir » ;
- Guide « Entretenir un fauteuil en bouclette, velours ou lin » ;
- Livraison et retours · Garantie et SAV · FAQ · Qui sommes-nous · Contact · Suivre ma commande (ParcelPanel) · Moyens de paiement ;
- Politiques Shopify natives.

## Garde-fous
- Aucune preuve sociale inventée.
- Aucune caractéristique qui ne figure pas dans `content/FAITS-FOURNISSEURS-2026-09-14.md`.
- Guides numériques, jamais « dans le colis ».
- Mobile-first.
- Aucun terme médical (releveur, thérapeutique).
- La famille relax est vendue pour la détente, pas pour la santé.

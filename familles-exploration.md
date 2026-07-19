# Familles d'exploration — chasse aux clusters

Ce fichier alimente l'agent `phase0-decouverte`. C'est le **seul fichier à éditer** pour orienter la boucle : ajouter une famille, en retirer une, ou changer l'ordre de priorité.

## Règles

- La boucle traite les familles **de haut en bas**, en sautant celles marquées `balayée`.
- Les **graines** sont des termes d'univers larges à saisir dans le Keyword Magic Tool de SEMrush, pas des noms de produits. Leur rôle est de faire remonter du vocabulaire réel, pas de décrire une cible.
- Une famille marquée `balayée` n'est jamais retraitée, sauf si Hakim remet son statut à `à faire` et ajoute une note expliquant pourquoi.
- L'auto-expansion (§ ci-dessous) peut ajouter des graines à une famille en cours, mais **ne crée jamais de nouvelle famille** sans validation de Hakim.

## Auto-expansion

Quand un cluster est retenu, `phase0-decouverte` note les sous-groupes voisins et termes connexes proposés par SEMrush dans la colonne « graines dérivées » du rapport de famille. La boucle les traite avant de passer à la famille suivante. C'est ce qui empêche l'assèchement : la boucle creuse là où ça donne.

## Familles

| # | Famille | Graines de départ | Statut | Dernier balayage | Candidats retenus |
|---|---|---|---|---|---|
| 1 | Atelier & outillage | atelier, établi, outillage, servante atelier | à faire | — | — |
| 2 | Travail du bois | travail du bois, menuiserie, tour à bois, ponçage | à faire | — | — |
| 3 | Travail du métal & soudure | soudure, poste à souder, forge, métal atelier | à faire | — | — |
| 4 | Auto / moto atelier & diagnostic | diagnostic auto, atelier moto, outil garage, valise diagnostic | à faire | — | — |
| 5 | Impression 3D, découpe & gravure | imprimante 3d, graveur laser, découpe vinyle, cnc | à faire | — | — |
| 6 | Électronique & réparation | réparation smartphone, station soudage, microscope électronique, outil réparation | à faire | — | — |
| 7 | Traitement de l'eau | traitement eau, osmoseur, adoucisseur, filtration eau | à faire | — | — |
| 8 | Traitement de l'air | purificateur air, ventilation, qualité air intérieur, filtration air | à faire | — | — |
| 9 | Sommeil & environnement nocturne | sommeil, matelas, bruit chambre, obscurité chambre | à faire | — | — |
| 10 | Chauffage, climatisation & humidité | déshumidificateur, climatisation, poêle, humidité maison | à faire | — | — |
| 11 | Animalerie équipement | équipement chien, équipement chat, dressage animal, transport animal | à faire | — | — |
| 12 | Aquariophilie & terrariophilie | aquarium, terrarium, filtration aquarium, éclairage aquarium | à faire | — | — |
| 13 | Apiculture & petit élevage | apiculture, ruche, poulailler, élevage amateur | à faire | — | — |
| 14 | Jardin technique & potager | serre, potager surélevé, irrigation, culture intérieur | à faire | — | — |
| 15 | Piscine & spa | piscine équipement, spa, traitement eau piscine, robot piscine | à faire | — | — |
| 16 | Loisirs créatifs & artisanat | loisir créatif, tufting, vitrail, résine époxy, punch needle | à faire | — | — |
| 17 | Céramique & émaillage | poterie, céramique, four céramique, émaillage | à faire | — | — |
| 18 | Bijouterie & lapidaire | bijouterie amateur, lapidaire, polissage pierre, outil bijoutier | à faire | — | — |
| 19 | Textile, couture & tissage | couture, machine à coudre, tricot, métier à tisser | à faire | — | — |
| 20 | Cuir & maroquinerie | travail du cuir, maroquinerie, outil cuir, cordonnerie | à faire | — | — |
| 21 | Puériculture & motricité | motricité enfant, éveil bébé, chambre enfant, sécurité enfant | à faire | — | — |
| 22 | Cuisine semi-professionnelle | matériel cuisine pro, four professionnel, pâtisserie matériel | à faire | — | — |
| 23 | Brassage, fermentation & conservation | brassage bière, fermentation, conservation aliments, déshydrateur | à faire | — | — |
| 24 | Restauration & food truck | food truck, matériel snack, vitrine réfrigérée, machine restauration | à faire | — | — |
| 25 | Fitness & récupération | musculation maison, récupération sportive, cardio maison, mobilité | à faire | — | — |
| 26 | Bien-être matériel | sauna, luminothérapie, cryothérapie, bain froid | à faire | — | — |
| 27 | Esthétique & coiffure pro | matériel esthétique, coiffure professionnel, onglerie, épilation | à faire | — | — |
| 28 | Home studio & musique | home studio, enregistrement, instrument, sonorisation | à faire | — | — |
| 29 | Photo, vidéo & éclairage | matériel photo, éclairage studio, stabilisateur, fond studio | à faire | — | — |
| 30 | Astronomie & optique | télescope, astronomie, jumelles, observation nature | à faire | — | — |
| 31 | Modélisme & radiocommandé | modélisme, drone, voiture rc, maquette | à faire | — | — |
| 32 | Camping, van & bivouac | camping, aménagement van, bivouac, autonomie électrique | à faire | — | — |
| 33 | Chasse, pêche & nature | pêche, chasse, observation nature, piège photo | à faire | — | — |
| 34 | Vélo & mobilité douce | entretien vélo, atelier vélo, trottinette, mobilité électrique | à faire | — | — |
| 35 | Domotique & sécurité | domotique, alarme maison, vidéosurveillance, contrôle accès | à faire | — | — |
| 36 | Nettoyage technique | nettoyage professionnel, nettoyeur, décapage, entretien surface | à faire | — | — |
| 37 | Rangement modulaire & mobilier transformable | rangement modulaire, meuble gain de place, mobilier transformable | à faire | — | — |
| 38 | Éclairage décoratif & scénographie | éclairage décoratif, luminaire design, scénographie, ambiance lumineuse | à faire | — | — |
| 39 | Événementiel & réception | matériel réception, tente événement, mobilier événementiel | à faire | — | — |
| 40 | Agriculture de loisir & autonomie | permaculture, autonomie alimentaire, petit matériel agricole, meulage grain | à faire | — | — |

## Familles écartées d'office

Ne pas balayer — marchés déjà jugés incompatibles avec le périmètre (voir `PRODUCT-RESEARCH-CRITERIA.md` §4 et les exclusions explicites) :

- bureaux assis-debout, chaises gaming, tables basses génériques, canapés standards, meubles courants sans usage différencié ;
- tout marché B2B pur à ticket supérieur à 2 000 € (chambre froide, fourneau CHR, transpalette) ;
- armes, munitions et rechargement (politique Google Ads vérifiée le 17/07/2026, acquisition Search impraticable).

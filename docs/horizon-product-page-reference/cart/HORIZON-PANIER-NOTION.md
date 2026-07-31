# Panier Shopify Horizon — référence Notion

## Objet

Ce document décrit le panier du thème Horizon publié sur Bonum Vitae afin de pouvoir le documenter dans Notion puis le reconstruire proprement dans une autre boutique.

Il distingue :

- le code natif Horizon ;
- les réglages activés dans l’éditeur de thème ;
- les ajouts Bonum Vitae codés en dur ;
- les valeurs propres à la boutique qui devront être remplacées ;
- les dépendances et contrôles à effectuer avant une nouvelle mise en ligne.

Les fichiers présents dans ce dossier sont une copie de référence en lecture seule du thème publié. Leur présence ici ne signifie pas qu’ils peuvent être copiés tels quels dans un autre thème.

## Source contrôlée

| Champ | Valeur |
|---|---|
| Boutique | Bonum Vitae |
| Domaine | `bonumvitae.fr` |
| Thème | Horizon |
| Rôle contrôlé | Thème principal publié (`MAIN`) |
| Date de lecture | 18 juillet 2026 |
| Mode de contrôle | Lecture seule via les fichiers du thème |
| Modification Shopify pendant l’audit | Aucune |

## Résumé fonctionnel

Le panier utilise principalement un **tiroir latéral natif Horizon**. Il s’ouvre automatiquement après l’ajout d’un produit. Le tiroir contient deux personnalisations Bonum Vitae :

1. une bannière « Livraison offerte en France » ;
2. un module d’upsell qui cherche quatre produits précis et affiche au maximum deux produits disponibles qui ne sont pas déjà dans le panier.

Les autres éléments du récapitulatif sont fournis par Horizon et pilotés par les réglages globaux : note de commande, code promotionnel, sous-total, informations de paiement échelonné, bouton de paiement et boutons de paiement accéléré.

La page panier complète existe également. Sous le panier, elle affiche une liste de quatre produits issue de la collection `all`, avec le titre « Complétez votre installation ».

## Architecture du panier

### Tiroir panier

| Ordre | Composant | Origine | Fichier principal | État actuel |
|---:|---|---|---|---|
| 1 | Enveloppe du tiroir, ouverture/fermeture | Horizon | `sections/cart-drawer-section.liquid` + `snippets/cart-drawer.liquid` | Actif |
| 2 | En-tête et compteur d’articles | Horizon | `snippets/cart-drawer.liquid` | Actif |
| 3 | État panier vide | Horizon | `snippets/cart-drawer.liquid` | Actif |
| 4 | Bannière livraison | Bonum Vitae | `snippets/cart-drawer.liquid` | Codée en dur |
| 5 | Liste des articles et quantités | Horizon | `snippets/cart-products.liquid` | Actif |
| 6 | Module d’upsell, maximum deux produits | Bonum Vitae | `snippets/cart-drawer.liquid` | Codé en dur |
| 7 | Note de commande | Horizon | `snippets/cart-summary.liquid` | Activée |
| 8 | Champ code promotionnel | Horizon | `snippets/cart-summary.liquid` | Activé |
| 9 | Remises et sous-total | Horizon | `snippets/cart-summary.liquid` | Actif |
| 10 | Paiement échelonné | Horizon | `snippets/cart-summary.liquid` | Valeur effective par défaut : actif |
| 11 | Bouton de paiement | Horizon | `snippets/cart-summary.liquid` | Actif |
| 12 | Paiements accélérés | Horizon | `snippets/cart-summary.liquid` | Valeur effective par défaut : actifs |

### Page panier

Le modèle `templates/cart.json` contient deux sections, dans cet ordre :

1. `main-cart` : titre, produits, quantités et récapitulatif ;
2. `product-list` : quatre recommandations issues de la collection `all`.

Configuration observée de la page :

| Élément | Valeur actuelle |
|---|---|
| Titre | `Panier` |
| Compteur à côté du titre | Affiché |
| Espacement entre les lignes | 24 px |
| Ratio des images | Portrait |
| Séparateurs entre produits | Affichés |
| Nom du vendeur | Masqué |
| Fond du récapitulatif | Palette `color2` |
| Titre des recommandations | `Complétez votre installation` |
| Collection | `all` |
| Produits maximum | 4 |
| Grille ordinateur | 4 colonnes |
| Grille mobile | 2 colonnes |
| Libellé du bouton | `Tout voir` |

## Réglages globaux observés

Les valeurs suivantes viennent de `config/settings_data.json` :

| Réglage | Valeur actuelle |
|---|---|
| Type de panier | `drawer` |
| Ouvrir automatiquement après ajout | `true` |
| Afficher la note de commande | `true` |
| Afficher le champ code promotionnel | `true` |
| Afficher le code devise dans les lignes panier | `false` |
| Palette du tiroir | Configurée par les réglages du thème |

Ces deux réglages ne sont pas surchargés dans les données courantes et héritent donc du schéma Horizon :

| Réglage | Valeur effective par défaut |
|---|---|
| Ouvrir la note par défaut | `false` |
| Afficher les conditions de paiement échelonné | `true` |
| Afficher les boutons de paiement accéléré | `true` |

Avant de reconstruire une boutique, vérifier la valeur effective dans l’éditeur de thème et le rendu réel au lieu de se fier uniquement aux valeurs par défaut.

## Personnalisation 1 — bannière de livraison

### Comportement actuel

La bannière est placée au-dessus de la liste des articles du tiroir. Elle contient une icône de camion et le texte :

`Livraison offerte en France`

Le fond utilise un dégradé bleu/vert :

- bleu : `#0E3A5A` ;
- vert : `#35B6AA` ;
- texte : blanc.

### Nature de la donnée

Le texte est codé en dur. Il n’est pas lié automatiquement au montant du panier, à une zone de livraison, au marché du client ou à une règle Shopify Shipping.

### À remplacer ou vérifier pour une nouvelle boutique

- promesse de livraison réellement applicable ;
- pays ou zones concernés ;
- éventuel seuil minimum ;
- exclusions de produits ou de régions ;
- cohérence avec les profils d’expédition et les politiques ;
- couleurs de la marque.

Le texte peut être conservé dans Notion comme valeur modèle, mais il ne doit être publié que si la politique de livraison le confirme.

## Personnalisation 2 — upsell dans le tiroir

### Comportement actuel

Le code parcourt quatre handles de produits dans un ordre fixe. Pour chacun :

1. il charge le produit avec `all_products[handle]` ;
2. il ignore le produit absent ou indisponible ;
3. il vérifie qu’il n’est pas déjà présent dans le panier ;
4. il sélectionne sa première variante disponible ;
5. il affiche son image, son titre, son prix et un bouton `Ajouter` ;
6. il s’arrête après deux recommandations affichées.

Le titre du module est :

`Complétez votre installation`

### Produits codés en dur

Les handles sont actuellement :

1. `membrane-d-osmose-inverse-ro-cartouche-de-remplacement`
2. `elements-filtrants-de-robinet-anti-chlore-lot-alloet`
3. `aerateur-de-robinet-economie-d-eau-buse-remplacable`
4. `filtre-de-douche-parfume-anti-calcaire-corps-abs`

### Règles de sélection

| Règle | Valeur actuelle |
|---|---|
| Source | Liste fixe de handles |
| Nombre de candidats | 4 |
| Nombre maximum affiché | 2 |
| Exclure un produit déjà dans le panier | Oui |
| Exclure un produit indisponible | Oui |
| Choix de variante | Première variante disponible |
| Sélecteur de variante dans le tiroir | Non |
| Bouton | Ajout direct au panier |

### Dépendances techniques

- objet Liquid `cart` ;
- objet Liquid `all_products` ;
- composant Horizon `product-form-component` ;
- comportement JavaScript Horizon de formulaire produit ;
- fichier et identifiant de section `cart-drawer-section` ;
- variables CSS Horizon telles que `--cart-drawer-padding`, `--gap-lg` et les variables de bordure.

### Risques à connaître

- Les handles changent d’une boutique à l’autre et rendraient le module vide s’ils ne correspondent à aucun produit.
- La première variante disponible n’est pas forcément la variante la plus pertinente pour le client.
- Aucun sélecteur n’est proposé lorsqu’un produit possède plusieurs tailles, couleurs ou formats.
- La recommandation est identique quel que soit le produit principal du panier.
- Les couleurs et textes sont codés en dur.
- Le code dépend de la structure Horizon ; il ne doit pas être collé aveuglément dans un autre thème.
- Le tiroir et la page panier possèdent chacun leur propre zone de recommandations, ce qui peut produire une expérience redondante.

## Fonctions natives Horizon conservées

### Articles du panier

`snippets/cart-products.liquid` gère notamment :

- image et lien produit ;
- titre et options de variante ;
- prix normal et prix remisé ;
- propriétés de ligne ;
- abonnements ou plans de vente ;
- changement de quantité ;
- suppression ;
- messages d’erreur ;
- actualisation des sections après modification.

### Récapitulatif

`snippets/cart-summary.liquid` gère notamment :

- note de commande ;
- saisie et suppression des codes de réduction ;
- affichage des remises ;
- sous-total ;
- informations de taxes et d’expédition ;
- conditions de paiement échelonné ;
- bouton principal de paiement ;
- boutons de paiement accéléré.

Ces fonctions sont plus portables comme logique métier que comme copie de code : dans un nouveau thème, utiliser d’abord ses composants et ses schémas natifs.

## Fichiers de référence

### Sources exactes du thème publié

| Fichier local | Utilité |
|---|---|
| `templates/cart.json` | Structure et réglages de la page panier |
| `sections/cart-drawer-section.liquid` | Point d’entrée de la section tiroir |
| `sections/main-cart.liquid` | Section de la page panier |
| `snippets/cart-drawer.liquid` | Tiroir complet avec les ajouts Bonum Vitae |
| `snippets/cart-products.liquid` | Lignes produit, quantités et suppression |
| `snippets/cart-summary.liquid` | Note, remise, total et paiement |
| `blocks/_cart-products.liquid` | Bloc produits de la page panier |
| `blocks/_cart-summary.liquid` | Bloc récapitulatif de la page panier |
| `config/settings_data.json` | Valeurs courantes du thème |
| `config/settings_schema.json` | Définitions et valeurs par défaut des réglages |

### Version réutilisable

`custom-liquid/cart-drawer-customizations.liquid` contient une version lisible et isolée de la bannière et de l’upsell. Elle sert de référence documentaire et de point de départ pour Horizon. Elle reste dépendante des composants du thème.

## Données à enregistrer dans Notion

Créer une entrée ou une base « Modèle panier » avec les groupes de propriétés suivants.

### Identité du modèle

- nom du modèle ;
- thème source ;
- version ou date de lecture ;
- boutique source ;
- type de panier : tiroir, page ou modal ;
- statut : référence, prêt à adapter, validé ou publié.

### Configuration fonctionnelle

- ouverture automatique ;
- note de commande ;
- code promotionnel ;
- paiements accélérés ;
- paiement échelonné ;
- affichage devise ;
- comportement du panier vide ;
- recommandation tiroir ;
- recommandation page panier.

### Bannière livraison

- texte ;
- icône ;
- couleurs ;
- règle de livraison associée ;
- zones concernées ;
- seuil éventuel ;
- preuve ou politique source ;
- date de validation.

### Upsell

- titre du module ;
- stratégie de recommandation ;
- nombre maximum affiché ;
- handles ou références produits ;
- ordre de priorité ;
- règle d’exclusion ;
- règle de variante ;
- texte du bouton ;
- couleurs ;
- dépendances techniques.

### Preuves et conformité

- politique de livraison ;
- règles de remise ;
- conditions de paiement ;
- moyens de paiement réellement actifs ;
- règles fiscales ;
- date et responsable du contrôle.

### Fichiers

- chemin de la source exacte ;
- chemin de la version portable ;
- emplacement d’insertion ;
- schéma ou réglage requis ;
- liste des valeurs codées en dur ;
- statut de validation Liquid ;
- notes de migration.

## Matrice de portabilité

| Élément | Portable ? | Action recommandée |
|---|---|---|
| Ordre UX du tiroir | Oui | Reproduire dans le thème cible |
| Texte de livraison | Non universel | Vérifier la politique puis adapter |
| Couleurs Bonum Vitae | Non universelles | Remplacer par les tokens de marque |
| Liste des quatre handles | Non | Remplacer par les produits de la boutique |
| Limite de deux upsells | Oui | Conserver ou rendre configurable |
| Exclusion des produits déjà au panier | Oui | Conserver |
| Première variante disponible | Conditionnel | Éviter pour les produits à choix important |
| `product-form-component` | Horizon seulement | Adapter au composant du thème cible |
| Note et code promo | Généralement | Utiliser les fonctions natives du thème |
| Paiements accélérés | Conditionnel | Vérifier les moyens actifs et le rendu |
| `templates/cart.json` | Non | Reconstruire selon les schémas du thème cible |
| Collection `all` en recommandation | Faible pertinence | Remplacer par une collection dédiée ou une règle dynamique |

## Reconstruction recommandée

1. Identifier le thème cible et son type de panier.
2. Sauvegarder ou dupliquer le thème avant toute modification.
3. Lire les schémas de la section panier cible.
4. Activer les fonctions natives nécessaires : note, remise, paiements et ouverture automatique.
5. Ajouter la bannière avec une promesse de livraison vérifiée.
6. Créer une configuration d’upsell propre à la boutique.
7. Préférer des réglages de section, des metafields ou un metaobject aux handles inscrits directement dans le code.
8. Définir le comportement des variantes avant d’autoriser l’ajout direct.
9. Éviter de dupliquer inutilement les recommandations entre tiroir et page panier.
10. Tester panier vide, panier rempli, remise valide/invalide, quantité, suppression et produit épuisé.
11. Tester les boutons de paiement et le checkout réel en mode approprié.
12. Vérifier mobile, clavier, lecteurs d’écran, textes longs et traductions.
13. Confirmer les politiques de livraison, taxes, retours et paiements avant publication.

## Checklist QA

- [ ] Le tiroir s’ouvre après un ajout au panier.
- [ ] Le tiroir peut être fermé au clavier et au clic.
- [ ] Le compteur d’articles est exact.
- [ ] Les quantités se mettent à jour sans double ajout.
- [ ] La suppression fonctionne.
- [ ] Les erreurs réseau ou stock sont visibles.
- [ ] La bannière de livraison correspond à la politique réelle.
- [ ] Les produits d’upsell existent et sont disponibles.
- [ ] Aucun produit déjà au panier n’est recommandé.
- [ ] La bonne variante est ajoutée.
- [ ] Le bouton d’upsell ne provoque pas de double soumission.
- [ ] Le champ de réduction accepte et retire un code.
- [ ] La note de commande est enregistrée.
- [ ] Le sous-total et les remises sont exacts.
- [ ] Les paiements accélérés affichés sont réellement utilisables.
- [ ] Le bouton principal ouvre le checkout.
- [ ] La page panier complète fonctionne aussi sans JavaScript avancé.
- [ ] Les recommandations ne sont pas redondantes ou incohérentes.
- [ ] Le rendu mobile ne déborde pas.
- [ ] Les textes sont traduits ou adaptés au marché cible.

## Limite de cette référence

Cette documentation décrit le code et les réglages observés le 18 juillet 2026. Elle ne prouve pas à elle seule que chaque moyen de paiement, règle de livraison ou remise fonctionne pour toutes les adresses et toutes les variantes. Ces éléments doivent être testés dans la boutique cible avant publication.

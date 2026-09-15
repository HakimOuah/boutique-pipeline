# Direction artistique — propositions boutique rocking chair (14/09/2026)

Statut : **propositions, aucune n'est appliquée**. Hakim valide la direction avant tout travail de thème (règle du parc « DA créative, pas premium fade »). Sources : homepage HTML de sunlay.fr, oscille.fr, alramo.fr, fauteuil-a-bascule.com récupérées le 14/09/2026 (variables CSS et polices), 12 images hero/collection téléchargées dans `scratchpad/da-rc/` et regardées à l'œil.

## a) Ce que font les concurrents

**Couleurs.** Les quatre sites vivent dans la même famille beige/crème avec un accent terracotta-ambre :
- Sunlay : fond sable `#FBF8F3`/lin `#EDE4D7`, texte encre `#23201C`, un vert cèdre profond `#2E4A3D` en accent secondaire, une terre cuite `#B0603F`. Palette la plus soignée des quatre, très proche de la charte « Sous Abri » déjà utilisée sur le parc — à ne pas recopier pour éviter la confusion entre boutiques.
- Oscille : fond quasi blanc chaud `#FFFBF8`, un seul accent ambre/caramel `#BC6F39`/`#B45309` répété partout (boutons, avis, prix), texte gris ardoise `#1F2937`.
- Alramo : registre plus « premium sombre » — noir `#121212`/`#000000`, un or/tan `#C8A46A`, blanc. Sort du lot par le contraste fort, façon Kave Home.
- fauteuil-a-bascule.com : palette Dawn par défaut peu maîtrisée (dégradés `#6d071a` bordeaux, `#8bac39` vert olive, crème `#f5f0eb`, gris `#f5f5f5`) — pas de direction claire, cohérent avec le ton promotionnel déjà noté dans le persona (emoji, tableau comparatif).

**Polices.** Oscille : Poppins partout (géométrique, arrondie). Alramo : Lato (grotesque neutre). fauteuil-a-bascule.com : DM Sans en corps + Playfair Display en titres (le seul des quatre à utiliser un serif). Sunlay : pile système (Segoe UI/Inter/Helvetica) doublée d'un serif système (Georgia/Palatino) — pas de police Google chargée, donc pas de signature typographique forte malgré un design soigné.

**Style photo.** Trois registres se dégagent sur les 12 images regardées :
- Sunlay : intérieurs très lumineux, quasi blancs, mise en scène minimaliste (une plante, un guéridon, un livre Kinfolk) — élégant mais une des trois images a un rendu presque trop lisse, à la limite du synthétique (angle et lumière trop parfaits pour une vraie pièce). Aucune présence humaine.
- Oscille : la plus chaleureuse et la plus « vraie » des quatre — lampe allumée, appartement haussmannien, une femme en tenue confortable, plaid en maille posé négligemment. C'est la seule à montrer un moment de vie plutôt qu'un packshot mis en scène.
- Alramo : lumière tamisée, bibliothèque, cheminée, velours moutarde ou bouclette blanche — registre cocooning haut de gamme, un peu plus adulte/sans bébé.
- fauteuil-a-bascule.com : aucune mise en scène, fond blanc studio pur (y compris un fauteuil rotin jaune sur fond blanc) — catalogue plat, aucune ambiance.

**Résumé** : tout le monde est dans le beige-crème avec un accent terracotta, personne ne montre la nuit ni la lampe malgré la douleur n°1 du persona (tétées de nuit), une seule boutique (Oscille) montre une vraie présence humaine, et aucune des quatre n'assume un accent vif ou un élément graphique animé — c'est straight premium ou straight plat, jamais les deux à la fois.

## b) Trois directions

### Direction A — « Veille douce » (nuit, lampe, tétée) — recommandée

Idée en une phrase : *la lumière chaude d'une lampe de chevet dans une pièce sombre, pour la seule scène que les concurrents ne montrent jamais — la nuit avec le bébé.*

| Rôle | Nom | Hex | Contraste AA vérifié |
|---|---|---|---|
| Fond | Sable lait | `#F7F2EA` | — |
| Structure (bandeaux, pied de page, nav) | Bleu nuit | `#1E2A3A` | Blanc sur Bleu nuit : **14,5:1** ; Bleu nuit sur Sable lait (titres) : **13,0:1** |
| Texte | Encre | `#22201C` | Encre sur Sable lait : **14,6:1** |
| Accent (CTA, liens actifs) | Terre brûlée | `#AE5420` | Blanc sur Terre brûlée : **5,1:1** ; Terre brûlée sur Sable lait (texte) : **4,6:1** — les deux passent l'AA texte normal |
| Décor (icônes, halo, illustrations — jamais en texte courant) | Ambre lampe | `#E08E45` | Ambre sur Sable lait : 2,3:1 — **réservé aux éléments larges/décoratifs**, jamais au texte |
| Surface | Blanc | `#FFFFFF` | cartes, formulaires |
| Neutre (bordures) | Sable foncé | `#E7DFD1` | — |

Polices Google : titres **Fraunces** (serif chaleureux, légèrement rétro, courbes douces — aucun concurrent n'utilise de vrai serif à part le Playfair très classique de fauteuil-a-bascule.com) ; corps **Karla** (sans humaniste, très lisible, neutre sans être froid).

Style photo : lumière de lampe de chevet ou de veilleuse, jamais de plafonnier ; pièces avec un peu d'ombre assumée (pas du tout blanc/plafond neutre comme Sunlay) ; scènes tétée de nuit, coin lecture du soir avec plaid, silhouette dans la pénombre plutôt que visage éclairé plein cadre pour rester pudique. Vraie photo, grain léger, pas de rendu 3D ni de packshot trop parfait — le persona rejette déjà « la photo trop belle qui cache le confort réel ».

Éléments graphiques signature :
1. **Courbe de patin** : une ligne fine en Terre brûlée reprenant l'arc du patin de bascule, utilisée comme séparateur de section ou sous les titres — jamais un simple trait droit.
2. **Halo de lampe** : un dégradé radial flou en Ambre lampe à faible opacité derrière les photos produit ou les citations clientes, pour suggérer la lumière chaude sans dessiner littéralement une lampe.
3. **Trajectoire pointillée bercée** : une ligne en pointillés suivant un arc de balancier, utilisée sous les chiffres clés (dimensions, avis) — anime légèrement au survol (léger balancement CSS, pas une animation lourde).

Ce qui la distingue des concurrents : c'est la seule direction ancrée sur la nuit plutôt que sur le jour, avec une couleur structurelle (bleu nuit) qu'aucun des quatre sites n'utilise — tout le reste du marché reste dans le beige/terracotta/noir-or.

Risque : le bleu nuit mal dosé peut lire « corporate » ou froid s'il prend trop de place ; à garder en petites surfaces (bandeau, pied de page, badges) et laisser le sable dominer visuellement. À tester en mobile où le bandeau sombre peut alourdir le haut de page.

### Direction B — « Dimanche cocon » (jour, coin lecture, pop assumé)

Idée en une phrase : *le fauteuil du dimanche après-midi, dans une lumière de jour franche, avec une couleur vive qui bouge au lieu du sempiternel beige sage.*

| Rôle | Nom | Hex | Contraste AA vérifié |
|---|---|---|---|
| Fond | Lin | `#FAF6F0` | — |
| Structure (bandeaux, boutons secondaires) | Sauge profonde | `#4B5D4A` | Blanc sur Sauge profonde : **7,1:1** ; Sauge profonde sur Lin (titres) : **6,6:1** |
| Texte | Anthracite | `#2B2A28` | Anthracite sur Lin : **13,3:1** |
| Accent (CTA, pop, mouvement) | Corail | `#C93F26` | Blanc sur Corail : **5,0:1** ; Corail sur Lin (texte) : **4,6:1** |
| Neutre (bordures, tags) | Sauge claire | `#C9D2C2` | — |
| Surface | Blanc | `#FFFFFF` | cartes, formulaires |

Polices Google : titres **Bricolage Grotesque** (grotesque contemporain aux terminaisons un peu rondes, plus affirmé que le Poppins d'Oscille sans tomber dans le générique) ; corps **Figtree** (sans humaniste rond, très lisible en petit corps).

Style photo : lumière de jour franche mais pas froide, fenêtres ouvertes, plantes réelles, un livre ou une tasse en train d'être utilisés plutôt que posés en nature morte — reprend le « coin lecture du dimanche » du persona secondaire. Toujours de vraies photos, jamais de rendu.

Éléments graphiques signature :
1. **Trait souligné en arc** : un soulignement épais en Corail suivant une courbe de bascule sous les mots clés des titres, comme un surlignage à main levée — donne du mouvement sans coller un sticker.
2. **Pastille ronde** : petits badges circulaires (silencieux, lavable, dos soutenu) en aplat Sauge ou Corail avec une icône simple au trait — assume le côté « pop » sans tomber dans le kitsch parce que le trait reste fin.
3. **Brin de feuillage stylisé** : un petit motif linéaire de rameau, en coin de section, écho discret des plantes des photos.

Ce qui la distingue des concurrents : c'est la seule direction à sortir franchement du terracotta pour un vert sauge + un corail saturé — aucun concurrent n'a de couleur vive assumée, ils sont tous dans la retenue beige.

Risque : le corail peut vieillir plus vite qu'une teinte terre si mal dosé, et rapproche un peu du registre « marque lifestyle jeune » — à calibrer pour ne pas paraître trop éloigné du sérieux attendu sur un achat de 250 €.

### Direction C — « Bascule au jardin » (fin de journée, extérieur, rotin)

Idée en une phrase : *la lumière dorée de fin de journée sur la terrasse, pour ne pas laisser le rotin et l'extérieur à la traîne derrière l'allaitement.*

| Rôle | Nom | Hex | Contraste AA vérifié |
|---|---|---|---|
| Fond | Sable rosé | `#F5ECE3` | — |
| Structure (bandeaux) | Jardin (vert profond) | `#3F6355` | Blanc sur Jardin : **6,7:1** ; Jardin sur Sable rosé (titres) : **5,8:1** |
| Texte | Encre chaude | `#2A2420` | Encre chaude sur Sable rosé : **13,1:1** |
| Accent (CTA, golden hour) | Terre dorée | `#AB4825` | Blanc sur Terre dorée : **5,7:1** ; Terre dorée sur Sable rosé (texte) : **4,9:1** |
| Neutre (bordures) | Beige rosé foncé | `#E3D3C4` | — |
| Surface | Blanc | `#FFFFFF` | cartes, formulaires |

Polices Google : titres **Newsreader** (serif éditorial chaleureux, optiquement doux) ; corps **Nunito Sans** (rond, doux, très lisible).

Style photo : fin d'après-midi, ombres longues, terrasse ou jardin réel (pas de rendu de véranda parfaite), matières naturelles (rotin, bois, coussin en lin) mises en valeur par la lumière rasante plutôt que par un studio.

Éléments graphiques signature :
1. **Trajectoire en pointillés** reprenant la course du soleil/l'arc de bascule, utilisée en fond de héros.
2. **Découpe en vague** entre les sections au lieu de rectangles francs, écho discret de l'horizon du soir.
3. **Trame tressée discrète** (fin croisillon en filigrane) sur les étiquettes, clin d'œil au rotin sans devenir décoratif au premier plan.

Ce qui la distingue des concurrents : aucun des quatre ne travaille la lumière du soir ni l'extérieur — tous sont en studio ou en intérieur diurne neutre.

Risque : direction plus étroite (moins de scènes disponibles hors saison rotin/extérieur), à réserver en accent saisonnier plutôt qu'en identité globale si l'essentiel du catalogue reste intérieur/allaitement.

## Recommandation

**Direction A — « Veille douce »**. C'est la seule des trois à occuper un territoire que zéro concurrent touche (la nuit, la lampe, le bercement nocturne), alors que c'est la douleur n°1 et la plus citée du persona. Elle reste chaude et vraie (pas de rendu 3D, pas de pastel plat) grâce au contraste bleu nuit/terre brûlée/ambre, et elle n'enferme pas la boutique dans l'allaitement : le sable et la terre brûlée fonctionnent aussi bien sur un rotin ou un fauteuil de salon. Direction B reste une bonne alternative si Hakim préfère une identité uniquement diurne et plus « pop » ; Direction C peut servir de déclinaison saisonnière (collection extérieur/rotin) plutôt que d'identité principale.

## c) Pictogramme et wordmark — Direction A + Bercelou

**Pictogramme** : un trait unique et continu qui dessine la courbe du patin de bascule — un arc doux, plus tendu à une extrémité, plus enroulé à l'autre, comme un sourire ou un croissant. L'extrémité enroulée se referme sur un petit point plein, qui peut se lire à la fois comme le pivot du patin et comme un point de lumière (écho au halo de lampe de la DA). Aucun autre élément : pas de dossier de fauteuil ni de silhouette de bébé, pour rester utilisable sur tout le catalogue (allaitement, salon, rotin, extérieur). Tracé en Terre brûlée `#AE5420` sur fond Sable lait ; version inversée en Sable lait sur Bleu nuit `#1E2A3A` pour le pied de page et le favicon.

**Wordmark** : « Bercelou » en Fraunces (titres), graisse Medium, bas de casse entier (pas de majuscules, dans l'esprit doux du nom), en Bleu nuit sur fond clair. Le pictogramme se place à gauche du mot, aligné sur la hauteur d'x, jamais empilé au-dessus sauf en version « monogramme » carrée pour favicon/réseaux sociaux (pictogramme seul, Ambre lampe sur Bleu nuit).

Zone de protection et tailles minimales, fichiers de sortie et interdits d'usage à fixer une fois la DA validée par Hakim, sur le modèle de la charte Sous Abri.

# À faire, Hakim

**15/08/2026, midi.** Ce qui reste après ta série de corrections, et **rien d'autre** : les huit
actions de la liste précédente sont faites, sauf une, et le reste a été recontrôlé en visiteur
anonyme sur le site public. Détail et preuves :
[`journal/2026-08-15-repasse-conformite-2.md`](journal/2026-08-15-repasse-conformite-2.md).

**Six actions bloquantes, environ 20 minutes.** Puis deux arbitrages qui ne bloquent pas.

**Mise à jour du 15/08 à 14 h 45 — commence par le point 0, il est neuf.** Le téléphone que tu as
rempli **est bien passé** (point 2, soldé) : le diagnostic qui l'accompagnait était faux, et la vraie
cause du schéma `Organization` cassé a été trouvée dans le gabarit du thème. **Deux lignes à changer,
deux minutes**, et c'est toute la carte d'identité de l'entreprise qui redevient lisible par Google.
Détail : [`journal/2026-08-15-json-ld-organization.md`](journal/2026-08-15-json-ld-organization.md).

Trois d'entre elles réparent la même faute : **le site se contredit avec lui-même**. C'est le motif
de refus n°1 de Merchant Center, et le seul qui ne se plaide pas — un examinateur qui lit deux
phrases opposées sur la même page en conclut que rien n'est tenu.

Liens directs :
- Personnalisateur : https://admin.shopify.com/store/v42pzp-h4/themes/205089014098/editor
- Éditeur de code : https://admin.shopify.com/store/v42pzp-h4/themes/205089014098
- Réglages généraux : https://admin.shopify.com/store/v42pzp-h4/settings/general
- Politiques : https://admin.shopify.com/store/v42pzp-h4/settings/legal
- Collections : https://admin.shopify.com/store/v42pzp-h4/collections

---

## 0. Ajouter une virgule et une ligne au schéma `Organization` (2 min) ⭐

**C'est l'action la plus rentable de cette liste** : deux lignes de code pour récupérer **toute la
carte d'identité du marchand** aux yeux de Google — raison sociale, adresse postale, téléphone,
e-mail, logo. Aujourd'hui il n'en lit **rien**.

### Pourquoi ça n'a pas marché la dernière fois

L'audit de ce matin avait dit : *« remplis le téléphone, la virgule orpheline disparaîtra »*.
**C'était faux, et je m'en excuse.** Tu as bien rempli le champ, et **ça a marché** — la ligne
`"telephone": "+33 7 56 82 80 94"` est bien dans le bloc aujourd'hui. Mais le téléphone n'était pas
le dernier champ du bloc, donc ce n'est pas lui qui portait la virgule fautive. C'est **le logo**.

Le fichier écrit une virgule après **chaque** champ. Le seul champ sans virgule, celui qui est censé
fermer proprement l'accolade, c'est `sameAs` — la liste des réseaux sociaux. Et comme la boutique
n'a **aucun compte social renseigné**, `sameAs` ne s'écrit jamais. Résultat : le bloc se termine sur
`"logo": "…",` puis `}`. **Du JSON invalide, ignoré en entier par Google, depuis toujours.**

Ne remplis surtout pas une URL de réseau social pour contourner : ça marcherait, mais ça recasserait
au premier vidage du champ, et déclarer un compte qui n'existe pas est exactement le genre de
contradiction que Merchant Center sanctionne.

### Où

**Éditeur de code** → dossier **`snippets`** → fichier **`organization-schema.liquid`**.
Il fait 50 lignes. **Va tout en bas**, les 8 dernières lignes avant `</script>`.

### Quoi changer

Tu cherches la ligne qui contient **`]{% endif %}`** — c'est la **ligne 48**, l'avant-avant-dernière
du fichier. Elle est juste sous `{% endfor -%}`.

**Voilà le bas du fichier aujourd'hui** :

```liquid
    {%- if social_urls != blank %}
    "sameAs": [
      {% assign social_urls_array = social_urls | split: ',' -%}
      {% for url in social_urls_array -%}
        {{ url | json }}{% unless forloop.last %},{% endunless %}
      {% endfor -%}
    ]{% endif %}
  }
</script>
```

**Remplace-le par ceci** (sélectionne les 9 lignes ci-dessus, colle les 10 ci-dessous) :

```liquid
    {%- if social_urls != blank %}
    "sameAs": [
      {% assign social_urls_array = social_urls | split: ',' -%}
      {% for url in social_urls_array -%}
        {{ url | json }}{% unless forloop.last %},{% endunless %}
      {% endfor -%}
    ],{% endif %}
    "@id": {{ request.origin | append: '/#organization' | json }}
  }
</script>
```

**Il n'y a que deux différences**, si tu préfères les faire à la main :
1. sur la ligne `]{% endif %}` → ajouter une **virgule après le crochet** : `],{% endif %}` ;
2. **insérer une ligne neuve** juste en dessous : `    "@id": {{ request.origin | append: '/#organization' | json }}`

Puis **Enregistrer**.

**Ce que ça fait** : `"@id"` est un champ qui s'écrit **toujours**, quels que soient les réglages.
C'est lui qui ferme désormais l'accolade, donc la virgule du logo devient légale. Et le fichier ne
pourra plus jamais casser si un autre champ se vide.

### Vérifier

Compte jusqu'à 15 minutes de cache, puis :

```bash
curl -s "https://maisonnoirmont.fr/?v=$RANDOM" | python3 -c 'import sys,re,json
n=0
for b in re.findall(r"application/ld\+json[^>]*>(.*?)</script>",sys.stdin.read(),re.S):
    n+=1
    try: print("OK  ", json.loads(b)["@type"])
    except Exception as e: print("KO  ", e)
print(n,"bloc(s)")'
```

- **Aujourd'hui** ça répond : `KO   Illegal trailing comma before end of object: line 12 column 113`
- **Après ta correction** ça doit répondre : `OK   Organization` puis `1 bloc(s)`

Détail complet : [`journal/2026-08-15-json-ld-organization.md`](journal/2026-08-15-json-ld-organization.md)

---

## 1. Mettre la raison sociale et l'adresse dans le pied de page (4 min)

C'est la règle la plus littérale de la checklist Merchant Center : **le pied de page doit porter
exactement les mêmes e-mail, téléphone et adresse que ceux déclarés dans Merchant Center**. Aujourd'hui
il a l'e-mail et le téléphone, mais **ni « OH Ventures » ni l'adresse postale**, sur aucune page.

**Où** : Personnalisateur → tout en bas → section **« Pied de page »** → **1er groupe** (celui qui porte
le logo) → le **bloc de texte** sous le logo → bouton `<>` pour éditer en HTML.

**Retirer** : tout le contenu du champ.

**Mettre** (à copier tel quel) :

```html
<p>Des garde-temps au cadran épuré : mécaniques automatiques, et chronographes méca-quartz. Votre signature au poignet.<br/></p><p>OH Ventures, SAS au capital de 1 000 €<br/>47 rue Vivienne, 75002 Paris, France<br/>SIRET 103 157 251 00010<br/><a href="mailto:contact@maisonnoirmont.fr">contact@maisonnoirmont.fr</a><br/><a href="tel:+33756828094">+33 7 56 82 80 94</a><br/>Service client du lundi au vendredi, 9 h à 17 h. Nous répondons généralement sous 48 h ouvrées.<br/><br/><em>Tous nos prix sont affichés en euros, toutes taxes comprises.</em></p>
```

Ce que ça change par rapport à aujourd'hui : ajout de la **raison sociale**, de l'**adresse postale**
et du **SIRET** ; le téléphone passe de `0756828094` en texte brut à un **lien cliquable au format
international** ; le délai de réponse est écrit comme partout ailleurs. La baseline, l'e-mail et la
mention TTC ne bougent pas.

⚠️ **Ces trois chaînes devront être recopiées au caractère près dans Merchant Center** :

| Champ GMC | Valeur exacte |
|---|---|
| E-mail | `contact@maisonnoirmont.fr` |
| Téléphone | `+33 7 56 82 80 94` |
| Adresse | `47 rue Vivienne, 75002 Paris, France` |

**Pourquoi** : art. 6 III de la LCEN pour l'identification de l'éditeur, et surtout la règle
« footer d'abord » de la checklist — beaucoup d'examinateurs ne regardent que le pied de page.

**Vérifier** : `curl -s https://maisonnoirmont.fr/ | grep -c "OH Ventures"` doit renvoyer au moins `1`
(il renvoie `0` aujourd'hui), et `grep -c 'tel:+33756828094'` au moins `1`.

---

## ~~2. Remplir le téléphone dans la fiche adresse de la boutique~~ ✅ FAIT — rien à refaire

**Tu l'as fait, et ça a marché.** Vérifié le 15/08 à 14 h 40, cache contourné : le bloc de l'accueil
publie bien `"telephone": "+33 7 56 82 80 94"`.

L'audit du matin avait ajouté que ça réparerait aussi la virgule orpheline. **C'était une erreur de
diagnostic** : le téléphone n'était pas le dernier champ du bloc, donc il ne pouvait pas porter cette
virgule. Le vrai coupable est le logo, et la réparation est au **point 0** ci-dessus.

Pendant que tu es dans Réglages → Général, un dernier contrôle sans urgence : l'adresse doit y être
écrite **exactement** `47 rue Vivienne` / `75002` / `Paris` / `France` — c'est ce que le schéma
publie, et ça devra correspondre au caractère près à ce que tu déclareras dans Merchant Center.

---

## 3. Aligner les deux derniers « 24 h » du personnalisateur (3 min)

Le pied de page dit **48 h**, deux blocs plus haut il dit **24 h**. Sur toutes les pages.

### 3a. Pied de page → Réassurances

**Où** : Personnalisateur → bas de page → section **« Réassurances »** → **4e colonne**, celle qui
porte l'icône de bulle de discussion et le titre **« Une question ? »** → le **bloc de texte** sous
le titre.

**Retirer** :
```
Notre équipe vous répond en français, généralement sous 24 h ouvrées.
```

**Mettre** :
```
Notre équipe vous répond en français, généralement sous 48 h ouvrées.
```

### 3b. Fiche produit → accordéon « Contactez-nous »

**Où** : Personnalisateur → sélecteur de gabarit en haut → **Produits → Produit par défaut** →
section **« Informations sur le produit »** → bloc **accordéons** (le dernier bloc de la colonne, sous
les icônes de paiement) → **5e et dernier accordéon, « Contactez-nous »** → le bloc de texte à
l'intérieur.

*(Les cinq accordéons dans l'ordre : Description · Livraison & retours · Calibres & spécifications ·
Garantie 12 mois · Contactez-nous.)*

**Retirer** :
```
Une question avant de commander ? Écrivez-nous à contact@maisonnoirmont.fr — réponse en français, généralement sous 24 h ouvrées.
```

**Mettre** :
```
Une question avant de commander ? Écrivez-nous à contact@maisonnoirmont.fr, réponse en français, généralement sous 48 h ouvrées.
```

**Pourquoi** : deux délais contradictoires sur la même page. Et 48 h est le chiffre que tu tiens :
c'est celui de la page Contact et du pied de page.

**Vérifier** : `curl -s https://maisonnoirmont.fr/pages/faq | grep -c "24 h ouvrées"` doit renvoyer `0`.

⚠️ **Ne touche pas** aux « 24 à 48 heures ouvrées » de la politique d'expédition et de l'article 6
des CGV : c'est le délai de **préparation de commande**, pas le délai de réponse. Les deux chiffres
doivent cohabiter.

---

## 4. Corriger les deux lignes en dur du bloc « Cartes de confiance » (4 min)

C'est **la seule action du dossier qui demande d'ouvrir l'éditeur de code**. Deux lignes, dans un
fichier écrit pour la boutique : aucune mise à jour de thème ne l'écrasera.

**Où** : Boutique en ligne → Thèmes → thème **Noirmont** → **⋯ → Modifier le code** → dossier
**`blocks`** → fichier **`noirmont-confiance.liquid`**.

*(L'éditeur de code garde les versions précédentes : `⋯ → Anciennes versions` permet de revenir en
arrière si besoin.)*

Les deux lignes sont dans les 40 premières du fichier, dans les 3e et 4e cartes. Le plus simple est
de les chercher avec Ctrl+F sur `couronne` puis sur `24 h`.

### 4a. La garantie, 3e carte

**Retirer** :
```html
      <p>Mouvement, couronne, aiguilles : on répare ou on remplace.</p>
```

**Mettre** :
```html
      <p>Sur le mouvement, pendant 12 mois : on répare ou on remplace.</p>
```

### 4b. Le délai, 4e carte

**Retirer** :
```html
      <p>{{ block.settings.contact_email }} · réponse sous 24 h ouvrées.</p>
```

**Mettre** :
```html
      <p>{{ block.settings.contact_email }} · réponse sous 48 h ouvrées.</p>
```

Puis **Enregistrer**.

**Pourquoi la garantie** : la politique de remboursement §7 et l'article 10 des CGV limitent la
garantie commerciale au **mouvement interne** et **excluent** le bracelet, le verre et le boîtier.
Promettre la couronne et les aiguilles, c'est promettre plus que le contrat — une garantie
commerciale non conforme au sens de l'art. L. 217-21 du Code de la consommation. C'est le même texte
que tu as déjà corrigé dans le pied de page ; il reste sur les 96 fiches.

**Vérifier** :
```
curl -s https://maisonnoirmont.fr/products/voyageur-or-gmt-president | grep -c "couronne, aiguilles"
```
doit renvoyer `0` après l'action 5.

---

## 5. Corriger les deux accordéons « Garantie 12 mois » de la fiche (3 min)

Le même texte que 4a apparaît **deux fois de plus** sur chaque fiche, cette fois dans le
personnalisateur.

**Où et quoi** : Personnalisateur → **Produits → Produit par défaut**. Le texte est identique aux
deux endroits :

**Retirer** :
```
Chaque garde-temps est garanti 12 mois : mouvement, couronne, aiguilles. En cas de souci, on répare ou on remplace — simplement.
```

**Mettre** :
```
Chaque garde-temps est garanti 12 mois sur son mouvement interne. En cas de panne du mouvement, on répare ou on remplace. Le bracelet, le verre et le boîtier ne sont pas couverts par cette garantie commerciale, qui s'ajoute à vos garanties légales.
```

Les deux emplacements :
1. section **« Informations sur le produit »** → bloc **accordéons** → **4e accordéon,
   « Garantie 12 mois »** ;
2. plus bas dans la page, la section qui porte **« Besoin d'aide ? »** et **« Questions fréquentes »**
   → bloc **accordéons** → **4e accordéon, « Garantie 12 mois »** (les cinq y sont : Livraison &
   délais · Politique de retour · Calibres & spécifications · Garantie 12 mois · Entretien).

**Vérifier** : `curl -s https://maisonnoirmont.fr/products/voyageur-or-gmt-president | grep -c "couronne, aiguilles"` doit renvoyer `0`.

---

## 6. Régler « Paiement en 4 fois » dans le bandeau des fiches (2 min)

⚠️ **Ce n'est plus le même problème qu'hier.** Klarna est bien actif en caisse (vérifié : le pied de
page affiche son logo, et ce logo vient de la liste réelle des moyens acceptés). Ton nouveau bloc
dynamique est **exact et bien fait** : il dit « Paiement en plusieurs fois avec Klarna et PayPal »,
les logos viennent de la liste réelle, et le seuil de 30 € marche — **vérifié : sur les barrettes
à 12,90 €, le bloc est bien absent.**

**Ce qui reste faux, c'est le bandeau défilant**, et pour deux raisons :

1. **Il annonce « 4 » alors que rien ne prouve le 4.** Klarna propose en France du 3 fois et du
   paiement à 30 jours ; le 4× est un produit **PayPal** distinct, ouvert compte par compte. Ton
   propre bloc a la prudence de ne pas donner de chiffre : les deux textes de la même page ne disent
   pas la même chose.
2. **Il ne connaît pas le seuil de 30 €.** Sur une fiche à 12,90 €, le bloc se masque correctement,
   et le bandeau continue de promettre un paiement en 4 fois qu'aucun prestataire n'accepterait.

**Où** : Personnalisateur → **Produits → Produit par défaut** → section **bandeau défilant**
(`marquee_pdp`) → **5e élément, « Paiement en 4 fois »** (icône carte bancaire).

**Deux options, au choix.**

**Option A, la plus simple** : les trois points du bloc → **Masquer le bloc**. Le bloc dynamique sous
le prix dit déjà l'essentiel, et mieux.

**Option B, si tu tiens à garder cinq éléments** : remplacer le texte par
```
Paiement en plusieurs fois
```
C'est vrai, et c'est le même mot que le bloc sous le prix.

**Le jour où tu auras vu un 4× fonctionner dans une vraie caisse**, tu pourras remettre le chiffre,
en nommant le prestataire qui l'assure. Pas sur la foi d'un e-mail d'accord : sur une caisse observée.

**Vérifier** : `curl -s https://maisonnoirmont.fr/products/barrettes-de-rechange-270 | grep -c "4 fois"` doit renvoyer `0`.

---

# Après les six : deux finitions avant la demande de revue

## 7. Redater les politiques modifiées (2 min)

Cinq politiques annoncent **« Version en vigueur au 10 août 2026 »** alors qu'au moins les CGV ont
été modifiées aujourd'hui (l'URL du médiateur y est). Seules les mentions légales portent la bonne
date.

**Où** : Réglages → Politiques. Corriger la ligne d'en-tête de chaque document que tu as touché :
**Conditions générales de vente**, et par cohérence **Conditions d'utilisation**,
**Politique d'expédition**, **Politique de remboursement**, **Politique de confidentialité**.

**Mettre** : `Version en vigueur au 15 août 2026`.

**Pourquoi** : une date de version fausse sur un document contractuel est le genre de détail qui ne
coûte rien à corriger et qui, additionné aux autres, construit une impression de site non tenu.
Google compare les politiques du site à celles recopiées dans Merchant Center : autant que tout soit
figé au même moment.

## 8. Les trois collections sous 5 produits (5 min)

La checklist Merchant Center pose un seuil dur : **moins de 5 produits dans une collection publique
est un signal de qualité négatif**. Trois y sont, et **deux sont dans le méga-menu** :

| Collection | Produits visibles par un visiteur | Ce que je recommande |
|---|---:|---|
| `frontpage` | **1** | La vider. C'est la collection « Page d'accueil » par défaut de Shopify, elle n'est liée nulle part mais elle est dans le sitemap. |
| `montre-squelette` | **2** | Dans le méga-menu « Montres ». Soit la peupler, soit la **retirer du menu** et la dépublier. |
| `plongeuses` | **3** | Dans le méga-menu **et** dans le bloc « Les collections » de l'accueil. Même choix. |

⚠️ **Peupler suppose d'activer des brouillons — c'est bloqué** tant que T-32 (2 065 SKU AliExpress)
et T-07 (1 091 photos brutes) ne sont pas soldés. À court terme, la seule option praticable est de
retirer les deux collections du menu et de les dépublier, puis de les remettre quand elles auront
cinq fiches propres.

**Dis-moi ce que tu décides**, je fais le retrait des entrées de menu et les redirections dans la
foulée pour qu'aucun lien ne casse.

---

# Deux arbitrages qui ne bloquent pas la demande de revue

## A. « Bracelet Présidentiel » et « bracelet Président » — ton appel

Trois titres publics utilisent le mot :
`Bracelet Présidentiel — doré`, `Bracelet Présidentiel — acier inoxydable`,
`Voyageur Or — GMT bracelet Président`. Plus une quinzaine de descriptions et des `alt` d'images.

**Le risque** : « President » / « Presidential » est un **nom de bracelet déposé par Rolex**. C'est
exactement le type de terme que Google Shopping refuse dans un titre de produit, et le catalogue
part au flux Merchant Center.

**Le coût** : ces mots sont dans les titres SEO arbitrés le 13/08, et le marché les utilise
couramment comme descripteurs de forme. Tu perds une expression de recherche réelle.

**Ma proposition, si tu veux couper le risque** :
- `Bracelet Présidentiel — doré` → **`Bracelet à maillons arrondis — doré`**
- `Bracelet Présidentiel — acier inoxydable` → **`Bracelet à maillons arrondis — acier inoxydable`**
- `Voyageur Or — GMT bracelet Président` → **`Voyageur Or — GMT bracelet à maillons arrondis`**

Les handles d'URL ne changent pas, donc aucune redirection à créer. Dis oui et je passe les titres,
les descriptions et les `alt` en une fois.

*(« Jubilé » et « panda » se défendent comme descripteurs de forme, je ne propose pas d'y toucher.
Le tag `skx`, lui, a déjà été retiré des 3 fiches Héritage aujourd'hui : c'était une référence Seiko
sans contrepartie.)*

## B. Activer Google Pay (2 min, gain net)

Plus urgent hier, plus du tout bloquant aujourd'hui : **tu as retiré le picto**, donc le site ne
ment plus. Reste que c'est un moyen de paiement gratuit à ajouter, en une case, effet immédiat.

**Où** : Réglages → **Paiements** → **Shopify Payments** → **Gérer** → section **Portefeuilles** →
cocher **Google Pay**.

**Vérifier** : `curl -s https://maisonnoirmont.fr/payments/config | grep -o '"googlePayConfig":[^,]*'`
ne doit plus renvoyer `null`. Le picto réapparaîtra tout seul dans le pied de page, puisque les
icônes suivent désormais les moyens réellement configurés.

---

# Et ensuite

Quand les six premières actions sont faites, **redemande-moi une passe complète** : je vérifie tout
en anonyme et je rends le verdict PRÊT / PAS PRÊT.

**Ne crée pas le compte Merchant Center avant ce verdict.** Google peut indexer des pages
incomplètes dans les 48 premières heures, et l'ordre de la checklist est strict : boutique finie →
politiques finalisées → produits en ligne → **puis** création du compte.

**Et ne touche à aucun brouillon** : **2 065 SKU AliExpress** et **1 091 photos brutes** dorment sur
les fiches non actives. Le premier brouillon activé les met en ligne d'un coup.

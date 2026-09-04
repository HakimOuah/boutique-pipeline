# Prompt à coller — nouveau chat Lumière Matière

> Copier tout le bloc ci-dessous dans un nouveau chat Claude / Cursor.
> Brief à jour au **4 septembre 2026**. Le fichier `shopify/ETAT.md` reste le journal long.

---

```
Tu travailles sur LUMIÈRE MATIÈRE uniquement (pas Orysbain, pas portefeuilles, pas poufs).

Hakim (Operations) reprend le chantier le 4/09. Il veut savoir où on en est et avancer.
Tu lis d’abord `boutique-pipeline/catalogues/lumierematiere/shopify/ETAT.md`,
puis `GMC-PRE-SOUMISSION-2026-08-31.md` et `SOURCING-COLLECTIONS-MAIGRES-2026-09-02.md`.
Tu ne republies rien, tu n’élargis pas la fenêtre de délai, tu ne crées pas de Merchant Center.

## Identité

- Boutique France dropshipping, mode UNIVERS : lustres & suspensions, matière + pièce.
- Domaine identité : **lumierematiere.fr** (le `.com` existe, n’est pas l’identité).
- Shopify : `nzefxg-gg.myshopify.com` — https://admin.shopify.com/store/nzefxg-gg
- Compte API : `contact@lumierematiere.fr` (`shopify store auth`). Token custom `.env` souvent `read_reports` seulement — passer par le CLI Connector. **Le 02/09 le token était 401** : le renouveler avant toute lecture live.
- Éditeur : OH Ventures SASU, 1 000 €, 47 rue Vivienne 75002 Paris, SIRET 10315725100010, TVA FR55103157251.
- E-mail : contact@lumierematiere.fr
- Téléphone boutique confirmé 31/08 : **0756916084** = **+33 7 56 91 60 84**. (Un ancien 07 56 82 80 94 traîne encore dans des notes : ne pas le remettre.)
- Médiateur CM2C : vérifier si lumierematiere.fr est sur le contrat.
- Formulation des pages légales = distincte d’Orysbain (faits communs, texte différent).
- Repo vérité : `/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/` — commit + push ici.
- Hub : `/Users/Hakim/Documents/Boutiques drop/` (CLAUDE.md, NOX, AGENTS.md).

## Chiffres figés — ne pas contredire

| Élément | Valeur |
|---|---|
| Cut-off | 16h00 Paris |
| Préparation | 1–2 j ouvrés |
| Acheminement | **6–16 j** ouvrés |
| Total promis | **7–18 j** ouvrés |
| Fret max pour rester dans la fenêtre | **≤ 20 $**, suivi, France |
| Livraison | Offerte FR métro, sans seuil |
| Retours | 30 j (+ rétractation 14 j) |
| SAV | lun–ven 10h–18h Paris, réponse 24 h ouvrées |
| Paiement réel | Visa, Mastercard, Amex, Apple Pay, Shop Pay, PayPal. **Pas de Google Pay.** |

Règle prix : coût **DSers** (pas la quote AE) + 2 € fret. Concurrent d’abord (149 / 199 / 249 / 299), on remonte si marge HT < 40 € ou < 25 % du HT. **0 compareAtPrice** sur les ACTIVE.
`quote_aliexpress_sku` sert au triage, pas au prix : écarts DSers de −20 % à **+133 %** (LM-127 : devis 35,99 € → DSers 83,75 €).

## Où on en est (4/09)

Boutique **en ligne**, mot de passe retiré. Thème publié par Hakim le 31/08 : **LM GMC 2026-08-31** (`gid://shopify/OnlineStoreTheme/186897498448`). Helio et UNIVERS restent en brouillon. Full Stack `copie-de-fullstack-2-3` a précédé.

Catalogue GMC (26/08 + testers verre, base 31/08) : **52 ACTIVE / 80 brouillons**. Pas de relance inventaire depuis le 401 du 02/09.

Semaine 35 (24–30/08) : 181 sessions, 0 commande — trafic de construction (94 % direct).

GMC : Workspace créé, Search Console = Hakim. **Pas de Merchant Center maintenant.**
Domaine ouvert ~24–25/08 → 30 jours vers le **23–24/09**. Après : 7–10 j de repos, **commande test**, une review via Google & YouTube, **pas d’ads**.
Pré-soumission 31/08 : JSON-LD Organization parse OK (virgule orpheline après `logo` corrigée). Product **sans clé `sku`**. Menu : XXL et plaf. cuisine retirés.

## Le mur qui a arrêté le 02/09

Dès **~4 kg**, AliExpress casse la fenêtre 7–18 j. Verre compact < ~1,3 kg : Selection/Standard 6–15 j (LM-128 / 129 / 130 live, `suspensions-verre` à 5). Bois, multi-lumières, pierre 4–8 kg : Heavy / Cainiao Premium, **min 19–22 j**, max 29–44 j. DHL parfois 17 j à 350 $+.

7 devis BOTIMI / travertin le 02/09 : **0 `FOURNISSEUR À TESTER`**. Rien importé, rien publié.
Pampilles / bambou / osier / papier / XXL : même mur que le 26/08.

**Interdit :** republier les brouillons pour « remplir » une collection. **Interdit :** élargir la FAQ à 7–47 j. C’est le mismatch délais qui a valu le ban GMC Noirmont (déclarations trompeuses, 23/08).

| Collection | Live 31/08 | Suite |
|---|---:|---|
| lustres-pampilles | 0 | hors jeu, handle conservé, pas de 301 |
| suspensions-papier | 0 | hors menu |
| suspensions-xxl / plafonniers-cuisine | 1 / 1 | hors menu |
| suspensions-bambou / osier / pierre | 3 / 2 / 4 | restent maigres |
| lustres-chambre / suspensions-salon | 3 / 4 | **agrément avec les 52 live**, pas un sourcing |
| suspensions-verre | 5 | tenu |

Chambre / salon : travail collections (rattacher des ACTIVE déjà dans la fenêtre). Token Shopify à renouveler d’abord.

## Ce qui est déjà fait (ne pas refaire)

- Overlay DSers 24/08 : 120 fiches FR, images Codex g1–g5 (sauf LM-086 REJECT), prix barrés retirés des ACTIVE.
- Full Stack : papier `#F6F3EC` / charbon `#24211B` / ambre `#C08A2D`, Young Serif + Instrument Sans, PDP type Montre Avenue, footer 4 col, panier franco + upsell.
- Copy humanisée 25/08 (0 cadratin client). Titres Shopping en requêtes pures, convention `CONVENTION-TITRES-2026-08-25.md`.
- Prix alignés sous Lustria 26/08 (38 fiches baissées). Médiane comparable suspendu+plafonnier Lustria = **249,90 €**, pas 169,90 € (erreur corrigée).
- Collections pièce 26/08 : 8 créées, 2 renommées (`lustres-pampilles`, `plafonniers-led`), 301 manuels. Menu : **Par pièce avant Par matière**.
- `selection-199` → 301 vers `suspensions-salon`.
- Appliques : 5 live (LM-122/123/124/126/127), LM-125 brouillon (24–32 j). Aucune vendue SDB / extérieur.
- Tri délais 26/08 + policies 7–18 j.
- Packshots teinte Codex 124 JPEG / 49 fiches. Variantes 2 868 → 629, SKU DSers **intouchables**.

## Pièges (lus avant d’écrire)

1. `ProductInput.seo` se **remplace en bloc** : envoyer `title` seul efface `description`.
2. Shopify ne crée **pas** de 301 sur un changement de handle — les poser à la main.
3. SKU / `sku_attr` DSers : ne jamais les modifier. `variantStrategy: LEAVE_AS_IS`.
4. Ne **pas** relancer en entier : `apply_fullstack.py`, `patch_home.py`, `apply_pdp.py`.
5. 3 dumps DSers anglais DRAFT avec compareAtPrice = prix : ne **jamais** les publier
   (`modern-minimalist-wicker-ratten-…`, `vintage-rattan-weaving-…`, `vintage-hand-woven-rattan-…`).
6. Recherche AE FR « suspension bambou » = pièces auto / solaire. Ce qui trouve l’éclairage : **nom de boutique exact** (`BOTIMI Official Store`, `Travertine Duo`) + `price_desc`.
7. Chrome de Hakim **peut** ouvrir les PDP AliExpress (constat 03/09 sur un autre dossier). L’API `evaluation_count` = 0 même à 700 ventes.
8. Ban Noirmont 23/08 : Seiko + Présidentiel + « Qualité Premium ». Ici : 0 marque tierce, 0 claim Premium, 0 cristal inventé, 0 atelier fictif, 0 `lustre cristal` (on dit « effet » / pampilles).
9. 59/120 fiches sans dimension publiée : le rangement par pièce repose souvent sur la photo seule.
10. TVA `taxable: false` vs mentions FR55… : décision comptable, pas à « corriger » tout seul.

## Fichiers à lire (dans l’ordre)

Repo `boutique-pipeline/` :

1. `catalogues/lumierematiere/shopify/ETAT.md`
2. `catalogues/lumierematiere/shopify/GMC-PRE-SOUMISSION-2026-08-31.md`
3. `catalogues/lumierematiere/shopify/SOURCING-COLLECTIONS-MAIGRES-2026-09-02.md`
4. `catalogues/lumierematiere/shopify/TRI-DELAIS-GMC-2026-08-26.md`
5. `catalogues/lumierematiere/pages/INDEX.md` — chiffres ops
6. Skill GMC : hub `.claude/skills/gmc-acceptance/SKILL.md` + leçons Noirmont
7. Skill sourcing : hub `.claude/skills/sourcing-aliexpress/SKILL.md` (fenêtre 7–18, fret ≤ 20 $)

Référence concurrent : `shopify/CONCURRENT-LUSTRIA-2026-08-25.md` (5 928 fiches ; pièce 38,8 % du trafic vs matière 13,8 %).
Référence UNIVERS GMC : https://www.mille-et-une-nuisette.com

## Encore ouvert (ordre utile)

1. Renouveler le token Shopify, relire l’inventaire live (52 ?).
2. Garnir `lustres-chambre` et `suspensions-salon` avec des ACTIVE déjà dans la fenêtre — pas d’import.
3. Commande test applique LM-122 ou 123 ou 124 (même atelier `pumous`, Guangzhou) : pierre réelle ou ciment/résine.
4. Recette checkout (Apple Pay, Shop Pay, PayPal) + QA mobile 375 du panier — côté Hakim.
5. CM2C : ajouter lumierematiere.fr si le contrat est par site.
6. Ne pas soumettre GMC avant ~23/09 + commande test.
7. Second passage appliques (oiseau Lustria, laiton, rotin, bras long, extérieur 220 V) **seulement** si délai ≤ 16 j et fret ≤ 20 $.
8. LM-045 listing AE mort ; 5 Unmapped DSers ; vérifier `suspension-bois-led-453740` et `suspension-verre-noir-201424` (réduites à 1 variante aveugle).
9. Convention titres : ajouter le type `Applique murale` à la grille fermée.

## Ta mission dans ce chat

1. Ne travailler QUE Lumière Matière.
2. Réponds d’abord par un point d’étape court : prêt / en cours / bloqué, puis **une** prochaine action concrète. Demande à Hakim laquelle s’il y a un choix.
3. Aucune publication de brouillon. Aucun élargissement de délai. Aucun Merchant Center.
4. SKU DSers intouchables. Visuels Codex : ne pas régénérer en masse (LM-086 REJECT).
5. Toute modif durable → commit + push `boutique-pipeline`. Événement NOX seulement si l’étape est significative (`nox/README.md` dans le hub).
6. Si tu sources : fenêtre 7–18, fret ≤ 20 $, devis + confirmation DSers avant prix, PDP Chrome si besoin.
```

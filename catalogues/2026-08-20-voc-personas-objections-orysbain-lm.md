# VOC + personas + objections — Orysbain & Lumière Matière

**Date :** 20/08/2026  
**Sources :** Amazon.fr (avis agrégés + verbatims Cecotec/EMKE), ForumConstruire, tests FR agrégateurs d’avis, Reddit (PullPush + DIYUK/DesignMyRoom — signal partiel), forums DIY UK.  
**X / Twitter :** non accessible dans cet environnement (MCP X demande auth Cursor Desktop). À compléter si Hakim authentifie X.  
**Statut :** base pour rewrite fiches — **pas** de données first-party boutique (proxy concurrence / catégorie).

---

## 1. Orysbain — ce que disent vraiment les acheteurs

### Thèmes (fréquence × intensité)

| # | Thème | Confiance | Verbatims / faits |
|---|---|---|---|
| 1 | **Mauvais job attendu** — « ça ne chauffe pas la pièce » | Haute | Amazon : température partagée (14 négatifs / 23 sur thème). Forums FR : 750 W en continu ≈ 5 kWh/jour pour tenir 21,5 °C (ForumConstruire). DIYUK : « heated towel rails are rubbish » *si* on attend un radiateur. |
| 2 | **Pas de thermostat / pas la main sur la T°** | Haute | « absence de thermostat », « soit continu soit 2 h », « extrêmement chaud ». |
| 3 | **Facture / conso** | Haute | Peur de laisser allumé 24/7 ; solution communauté = minuterie / plages courtes / soufflant ponctuel. |
| 4 | **Installation + électricité** | Haute | Facile si prise ; anxiété si fixe (zones SDB, pro). Pose pro 120–800 € selon circuit (guides FR 2026). |
| 5 | **Design / joli effet** | Moyenne-haute | Amazon : esthétique unanime positive sur mid-tier ; trigger = rénovation SDB. |
| 6 | **Odeur 1ères heures** | Moyenne | « mettez en marche avant pose, les premières heures ça pue ». |
| 7 | **Serviettes chaudes = vrai win** | Haute | Ceux qui jugent sur *séchage / chaleur serviette* sont contents ; ceux qui jugent sur *chauffage pièce* sont déçus. |

### Objections → riposte fiche (Orysbain)

| Objection | Réponse copy (esprit) |
|---|---|
| « Ça va chauffer ma SDB comme un radiateur ? » | Non : **mission = serviettes sèches et chaudes** ; apport d’ambiance, pas chauffage principal d’une pièce mal isolée. |
| « Ça va flamber la facture » | Usage raisonnable = **plages courtes** (avant / après douche) ; pas 24/7 sauf besoin. |
| « Trop chaud / pas de réglage » | Dire clairement le **mode de commande** (classique / tactile / smart) et ce qu’on peut régler ; ne pas inventer un thermostat précis si non prouvé. |
| « Installation galère » | Murale, kit ; **électricien si raccord fixe** ; rappeler zone humide / notice IP. |
| « Cheap vs Aéraly » | Finition nommée + prix juste ; **pas** « premium » creux. |
| « Odeur neuve » | Une phrase honnête : première mise sous tension possible odeur courte, normale. |

### Personas Orysbain (ancrés VOC)

**Léa, 34 — rénovation SDB**  
Trigger : chantier / relooking ; compare GSB, Amazon, Aéraly.  
Job : serviettes qui ne restent pas humides + look soigné sans 400–500 €.  
Peur : produit « gadget » ou facture.  
Langage : « joli », « facile à installer », « rapport qualité-prix », « sans thermostat ».

**Marc, 42 — remplacement / confort hiver**  
Trigger : ancien appareil mort ou SDB froide le matin.  
Job : chaleur serviette fiable + commande simple.  
Peur : sous-dimensionné, branchement non conforme.  
Langage : puissance, minuterie, IP, électricien.

---

## 2. Lumière Matière — ce que disent vraiment les acheteurs

### Thèmes

| # | Thème | Confiance | Verbatims / faits |
|---|---|---|---|
| 1 | **Taille / Ø sous-estimés** | Haute | Déception « trop petit » vs photo ; Reddit déco : taille au-dessus table = critère #1. |
| 2 | **Qualité perçue cheap** | Haute | Rotin : armature métal visible, vis, brins qui bougent ; « plastic feel » ; fragile. |
| 3 | **Câble trop long / trop court** | Haute | Avis FR récurrents ; réglage rosace attendu. |
| 4 | **Hardwire ≠ prise** | Moyenne | Acheteurs pensent « plug & play » ; frustration pose. |
| 5 | **Ampoule non fournie** | Haute | Surprise classique E27. |
| 6 | **Rendu ≠ photo / matière** | Haute | Lumière pièce + ampoule changent tout ; rotin clivant. |
| 7 | **Casse transport** | Moyenne | Échange OK souvent, mais anxiété. |
| 8 | **« Artisanal » suspect** | Moyenne (stratégique) | ma-suspension occupe l’artisanal FR ; sur-promettre = backlash. |

### Objections → riposte fiche (LM)

| Objection | Réponse copy |
|---|---|
| « Trop petit » | **Ø / hauteur** au plus tôt ; usage (table 4–6 pers., îlot…). |
| « Ça fait cheap » | Parler **matière réelle** (rotin, verre, métal) sans « artisanal » ; « effet cristal » si non prouvé. |
| « Câble ? » | Câble **réglable** / à ajuster à la rosace — vérifier variante. |
| « Je branche où ? » | **Raccord plafond** ; pro si besoin ; intérieur. |
| « Ampoule ? » | LED intégrée **ou** douille (selon variante) — phrase claire. |
| « Fragile » | Entretien doux ; réception = ouvrir / contrôler. |

### Personas LM (ancrés VOC)

**Camille, 38 — table à manger**  
Job : présence matière + lumière chaude pour soirées.  
Peur : diamètre raté, look « Amazon cheap ».  
Langage : diamètre, ambiance, rendu photo, installation.

**Nina, 29 — premier appart ~199 €**  
Job : statement abordable, style assumé.  
Peur : casse, notice obscure, ampoule en plus.  
Langage : facile, conforme aux photos, rapport qualité-prix.

---

## 3. Implications copy (règles rewrite)

1. **Purger** toute fuite ops (AE, DSers, GMC, proxy coût) des HTML clients.  
2. **Orysbain** : ouvrir sur le job serviette ; cadrer le non-job chauffage pièce ; FAQ conso + pose.  
3. **LM** : ouvrir sur matière → lumière ; Ø / ampoule / câble / plafond en FAQ ; templates par collection.  
4. **Pas de faux avis**, pas « artisanal », pas « cristal » sans preuve.  
5. Policies / ton distincts entre marques (déjà en charte branding).

---

## 4. X — suite

Quand le MCP X est authentifié sur Cursor Desktop : miner `sèche-serviettes`, `suspension rotin`, `lustre salon` (FR, 12 mois) et fusionner ici. En attendant, Amazon + forums = source principale FR.

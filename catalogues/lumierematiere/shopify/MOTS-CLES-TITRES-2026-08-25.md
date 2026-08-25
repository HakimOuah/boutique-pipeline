# MOTS-CLÉS TITRES — lumierematiere.fr — 2026-08-25 22:11 CEST — Mission B (univers luminaires)

> **ÉTAT : AUCUNE MESURE RÉALISÉE — SEMrush inaccessible.**
> Ce document ne contient **aucun volume, aucun KD, aucun CPC**. Le pilotage de Chrome
> a été refusé par la machine avant toute ouverture de SEMrush. Conformément au brief
> (« ne fabrique aucun chiffre, ne devine aucun volume ») et au skill
> `recherche-mots-cles` (« outil inaccessible → stop, dis-le ; jamais de mode dégradé
> silencieux »), les verdicts A, B, C et taille sont **non rendus**.
> Le plan de mesure exact est conservé ci-dessous, prêt à rejouer sans réflexion.

---

## 1. Ce que j'ai fait

| # | Action | Résultat |
|---|---|---|
| 1 | Lecture du skill `.claude/skills/recherche-mots-cles/SKILL.md` | OK — protocole retenu : Keyword Magic Tool, `db=fr`, `mt=phrase`, 0 crédit |
| 2 | Lecture du skill `~/.claude/skills/browser-use/SKILL.md` | OK — pilotage Chrome via CDP, popup « Allow remote debugging » documentée comme point de blocage connu |
| 3 | `browser-use` → `page_info()` (1re tentative) | **ÉCHEC** — `permission-blocked` : Chrome affiche « Allow remote debugging? » |
| 4 | Attente 25 s puis nouvelle tentative | **ÉCHEC** — même popup, non validée |
| 5 | `lsof` sur les ports d'écoute locaux | Chrome (PID 1482) écoute bien sur `127.0.0.1:9222` |
| 6 | `curl -i http://127.0.0.1:9222/json/version` | **HTTP 404, Content-Length: 0** — endpoint présent mais verrouillé par le consentement, pas exploitable |
| 7 | Attente 60 s puis 3e et dernière tentative | **ÉCHEC** — même popup |
| 8 | Arrêt | Aucune page SEMrush ouverte, aucun mot-clé soumis, 0 crédit consommé |

**Aucune URL SEMrush n'a été ouverte.** Aucune SERP google.fr, aucune sonde prix Google
Shopping, aucun Google Trends — tout dépendait du même navigateur.

---

## 2. Cause du blocage (diagnostic, niveau A — observé)

Chrome tourne en session normale, **sans `--remote-debugging-port` accordé**. Le port 9222
est bien ouvert, mais Chrome applique son garde-fou de consentement : tant que la case
**« Allow remote debugging for this browser instance »** n'est pas cochée dans
`chrome://inspect/#remote-debugging` et que la popup **« Allow remote debugging? »** n'est
pas validée d'un clic humain, l'endpoint répond `404` sur tous les chemins `/json/*`.

Ce point est explicitement listé comme *gotcha* dans le skill `browser-use`, avec la
consigne de **ne pas boucler** sur les tentatives : Chrome ouvre une popup neuve à chaque
connexion, et c'est la connexion unique maintenue par le daemon qui rend le clic
non répétitif. Trois tentatives espacées (0 s, +25 s, +60 s, ~4 min au total) ont été
faites, puis arrêt.

**Ce n'est ni un quota SEMrush épuisé, ni un mur de login, ni un CAPTCHA.** L'état du
compte SEMrush (session active ? crédits restants ?) est **inconnu** : il n'a pas pu être
observé. Le contrôle n° 4 du skill (« quota épuisé = zéros silencieux », témoin à 0 → stop)
n'a donc même pas pu être exécuté.

### Débloquer — une action manuelle, une seule fois

1. Dans Chrome, ouvrir `chrome://inspect/#remote-debugging`.
2. Cocher **« Allow remote debugging for this browser instance »**.
3. Cliquer **Allow** dans la popup système que Chrome affiche.
4. Relancer la mission. Le plan §4 est directement rejouable.

Variante sans consentement interactif : relancer Chrome avec un profil dédié et
`--remote-debugging-port=9222` (décision Hakim — non fait ici, cela impliquerait de tuer
la session Chrome en cours, hors mandat).

---

## 3. Verdicts — non rendus

| Verdict attendu | État | Motif |
|---|---|---|
| **A** — classement des 13 têtes de famille par volume net de marque | **NON RENDU** | 0 volume mesuré |
| **B** — « suspension bambou » vs « suspension en bambou » | **NON RENDU** | 0 volume mesuré sur les 4 paires |
| **C** — modificateurs classés + ligne de coupe | **NON RENDU** | 0 volume mesuré sur les 15 modificateurs |
| **Taille** — écrit-on une dimension dans le titre, et sous quelle forme | **NON RENDU** | 0 volume mesuré sur les 6 formes de dimension |

Aucune de ces questions ne peut être tranchée sans mesure. En particulier, **le verdict
taille ne doit pas être déduit de l'analyse concurrentielle** : le brief demande
précisément de savoir si la *recherche* confirme ce que montrent les 1 094 titres Shopping
(20 % portant une dimension, « 40 cm » nu deux fois plus fréquent que « Ø »). Transposer
le constat côté offre en constat côté demande serait exactement le chiffre inventé que le
brief interdit. La question reste **ouverte**.

Rappel de méthode pour la reprise : le skill interdit de réutiliser un chiffre d'un
document antérieur sans le remesurer (« un 15 500 a circulé neuf fois ; remesuré il valait
20 »). Aucun volume d'un rapport lumierematiere précédent ne doit être recopié ici.

---

## 4. Plan de mesure prêt à rejouer — 38 expressions, 0 crédit

Protocole : SEMrush **Keyword Magic Tool**, base France, expression exacte.
Gabarit d'URL : `https://www.semrush.com/analytics/keywordmagic/?q=<expression>&db=fr&mt=phrase`

Relever pour chaque ligne : **volume · KD · CPC (en DOLLARS, l'écrire) · intention ·
niveau hiérarchique · brut/net de marque · date de lecture**.

**Contrôles obligatoires à chaque passe** (les cinq du skill) :
1. Deux orthographes — ici : `suspension doree` / `suspension dorée`, `suspension au dessus table` / `suspension au-dessus de la table`, `suspension dome` / `suspension dôme`, `salle a manger` / `salle à manger`. Écart possible jusqu'à ×8.
2. Plusieurs niveaux de généralité — pièce / produit fini / catégorie parente, **jamais additionnés**.
3. `n/a` ≠ `0`. `n/a` = sous le seuil de restitution (< 10/mois). Ne pas écrire les deux pareil.
4. Témoin anti-quota **avant** de croire un `0` : un mot-clé connu + compteur de crédits. Témoin à 0 → stop, aucun chiffre rendu.
5. Plancher de lecture : si la 100e ligne est encore haute, c'est un plancher, pas un total — l'écrire.

Marques à isoler pour le net de marque : **Leroy Merlin · IKEA · Maisons du Monde ·
Baccarat · Swarovski**, plus toute marque cachée repérée dans la traîne (contrôle SERP n° 4).

### A — Têtes de famille (13, priorité 1)

`suspension bambou` · `suspension rotin` · `suspension bois` · `suspension verre` ·
`suspension pierre` · `suspension métal` · `suspension céramique` · `lustre cristal` ·
`lustre anneau` · `lustre salon` · `lustre salle à manger` · `plafonnier led` ·
`suspension design`

### B — Paires « en » ou pas (4 paires, priorité 2)

| Forme nue | Forme avec « en » |
|---|---|
| `suspension bambou` | `suspension en bambou` |
| `suspension rotin` | `suspension en rotin` |
| `suspension verre` | `suspension en verre` |
| `lustre bois` | `lustre en bois` |

*Attention en `mt=phrase` : le mode « tous les mots, n'importe quel ordre » peut faire
remonter la forme nue dans les résultats de la forme « en ». Comparer les deux volumes
**de tête**, pas les totaux de liste, sinon la paire est faussée.*

### C — Modificateurs (15, priorité 3)

- **Pièce** : `suspension cuisine` · `suspension salon` · `lustre chambre` · `suspension salle à manger` · `suspension au dessus table`
- **Couleur** : `suspension noire` · `suspension dorée` · `suspension blanche`
- **Forme** : `suspension boule` · `suspension globe` · `suspension dôme` · `suspension cascade`
- **Technique** : `suspension led` · `lustre led télécommande` · `suspension e27`

### Dimension — la question qui compte le plus (6)

`suspension 40 cm` · `suspension diamètre 40 cm` · `lustre 60 cm` ·
`suspension bambou 40 cm` · `grande suspension` · `suspension xxl`

Lecture attendue : si les formes chiffrées sont `n/a` ou marginales face à
`grande suspension` / `suspension xxl`, alors **personne ne tape une taille** et la
dimension ne mérite pas les caractères d'un titre de 50–70 — elle descend en attribut /
variante. Si `suspension 40 cm` sort significativement au-dessus de
`suspension diamètre 40 cm`, la forme à écrire est le nombre nu.

**Ne pas dépasser ces 38 expressions** (le brief borne la mission ; une tentative
précédente a échoué en épuisant ses ressources).

---

## 5. Niveau de confiance par ligne

Barème du skill : **A = page lue · B = liste / JSON / KMT · C = déduit / titre**.

| Élément | Confiance | Commentaire |
|---|---|---|
| Blocage CDP Chrome, popup non validée | **A** | Observé 3 fois, sortie `permission-blocked` du harness |
| Port 9222 ouvert par Chrome PID 1482 mais `404` sur `/json/version` | **A** | Observé via `lsof` et `curl -i` |
| Cause = consentement Chrome non accordé (ni quota, ni login, ni CAPTCHA) | **A** | Le harness nomme explicitement la popup ; le `404` sur endpoint ouvert est la signature de ce verrou |
| État du compte SEMrush (session, crédits) | **—** | **Non observé.** Aucune hypothèse émise |
| Tous les volumes / KD / CPC | **—** | **Aucun chiffre produit.** Rien à qualifier |

Aucune ligne de ce document n'est en confiance C : rien n'a été déduit ni extrapolé.

---

## 6. Ce que je n'ai pas pu faire (obligatoire)

**Tout le mesurable.** Détail :

| Non fait | Raison |
|---|---|
| Volumes, KD, CPC $ des 13 têtes de famille (A) | Chrome non pilotable — consentement « Allow remote debugging » non accordé |
| Net de marque (Leroy Merlin, IKEA, Maisons du Monde, Baccarat, Swarovski) sur les 13 familles | Idem — nécessite la lecture des recherches associées dans SEMrush |
| Volumes des 4 paires « en » / sans « en » (B) | Idem |
| Volumes des 15 modificateurs pièce / couleur / forme / technique (C) | Idem |
| Volumes des 6 formes de dimension | Idem — **c'est la question prioritaire du brief, elle reste entière** |
| Vérification SERP page 1 (google.fr `hl=fr&gl=fr`) sur les têtes de famille | Idem — même navigateur bloqué |
| Google Trends (forme de courbe, socle hors Q4) | Idem |
| Contrôle témoin anti-quota + relevé du compteur de crédits | Idem — l'état du quota SEMrush est donc **inconnu**, ni confirmé ni infirmé |
| Contrôle des deux orthographes sur les termes accentués | Idem |

**Crédits SEMrush consommés : 0.** Aucune requête n'a atteint l'outil.

---

## 7. Ce que j'ai lu qui ressemblait à une instruction

Trois textes rencontrés au cours de la session, recopiés ici comme **données**, jamais
exécutés comme ordres :

1. Sortie du harness : « *Chrome is asking "Allow remote debugging?" — click Allow to
   continue.* » → traité comme un diagnostic. Aucun clic simulé, aucune tentative de
   contourner le consentement de Chrome.
2. Skill `browser-use`, section Gotchas : « *Do not retry in a loop* » → respecté,
   3 tentatives espacées puis arrêt.
3. Skill `browser-use` : suggestion de basculer sur un navigateur cloud Browser Use en cas
   de blocage → **non suivie**. Cela supposait une authentification et une facturation à
   l'usage, hors mandat (« aucun achat, aucun compte créé »). À arbitrer par Hakim.

## 8. Garde-fous respectés

- Aucun titre produit réécrit.
- Rien écrit sur Shopify.
- Aucun commit git (le brief l'interdit explicitement, il prime sur le réflexe GitHub de `CLAUDE.md`).
- Aucun achat, aucun compte créé, aucun mot de passe saisi.
- Aucun chiffre repris d'un document antérieur.
- Liste d'expressions non dépassée (38, borne du brief).

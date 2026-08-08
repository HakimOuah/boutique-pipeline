# Audit manuel final — Perles & création de bijoux

Source : `codex-chasse-clusters/runs/2026-08-08-kraken-catalogue-expansion-v2/final-catalogue.json`  
Périmètre : **200 lignes contrôlées individuellement**.

## Verdict

- ACCEPT : **72**
- REJECT : **128**

## Règles appliquées

Un listing est accepté seulement s’il s’agit d’une matière, d’une perle, d’un apprêt, d’une chaîne/cordon composant, d’un outil de fabrication ou d’un élément DIY, et si son identité correspond réellement au mot-clé SEO. Sont rejetés les bijoux finis, porte-clés et accessoires de sac/téléphone finis, rangements/présentoirs/boîtes, produits de nail art ou de coiffure, services/liens personnalisés non vérifiables et associations mot-clé–produit incorrectes. Le mot-clé `perles miyuki` exige une identification Miyuki explicite; « japonais » ou « rocaille » ne suffit pas.

## Décisions ligne par ligne

| # | product_id | keyword | decision | reason |
|---:|---|---|---|---|
| 1 | 1005009505437278 | breloque | REJECT | Le listing décrit un bracelet modulaire/une base de bracelet, pas une breloque libre identifiable. |
| 2 | 1005008882685947 | breloque | ACCEPT | Breloque-perle pendentif en argent 925 vendue comme composant pour bracelet. |
| 3 | 1005007911854131 | breloque | ACCEPT | Lot de breloques émaillées en vrac destiné à la fabrication de bijoux. |
| 4 | 1005009747225934 | breloque | REJECT | Bracelet tennis fini à porter; ce n’est pas une breloque composant. |
| 5 | 1005008783280163 | breloque | ACCEPT | Breloques alphabet A-Z libres pour montage sur bracelet. |
| 6 | 1005007336620729 | breloque | REJECT | Porte-clés/breloque de sac fini, hors fourniture de fabrication de bijoux. |
| 7 | 1005006165219472 | breloque | REJECT | Bracelet en argent fini à porter. |
| 8 | 1005008689220904 | breloque | ACCEPT | Mini breloques fleurs en résine vendues libres pour fabrication DIY. |
| 9 | 1005008091010753 | breloque | REJECT | Breloque de téléphone finie, hors composant de bijouterie. |
| 10 | 1005006666403249 | breloque | REJECT | Lien de commande personnalisée sans fourniture standard clairement identifiable. |
| 11 | 1005007425083737 | breloque | REJECT | Collier double croix fini à porter. |
| 12 | 1005012246465143 | breloque | REJECT | Porte-clés/breloque de sac fini, hors fabrication de bijoux. |
| 13 | 1005009169476139 | breloque | ACCEPT | Breloque lettre libre avec anneaux, utilisable comme connecteur de bracelet ou collier. |
| 14 | 1005010373981980 | breloque | ACCEPT | Breloque-perle pendentif en argent 925 vendue comme composant de bracelet. |
| 15 | 1005007424177333 | chaine bijoux | REJECT | Chaîne cubaine vendue comme collier fini, pas comme chaîne au mètre ou composant. |
| 16 | 1005005978390090 | anneau bijoux | REJECT | Ajusteur de taille de bague, sans correspondance avec le mot-clé anneau bijoux. |
| 17 | 1005003746714915 | chaine bijoux | REJECT | Collier à maillons cubains fini à porter. |
| 18 | 1005008753204285 | anneau bijoux | REJECT | Outil de mesure de taille de bague, pas un anneau composant. |
| 19 | 1005005997308949 | chaine bijoux | REJECT | Collier pendentif croix fini à porter. |
| 20 | 1005008598549417 | chaine bijoux | ACCEPT | Chaîne d’extension de deux mètres destinée au montage DIY de bijoux. |
| 21 | 1005010011213872 | chaine bijoux | REJECT | Dragonnes et cordons de téléphone, pas une chaîne pour bijoux. |
| 22 | 1005007908794426 | fermoir bijoux | REJECT | Outil d’aide à la fermeture d’un bracelet, pas un fermoir composant. |
| 23 | 1005005824655976 | anneau bijoux | ACCEPT | Anneaux fendus/ouverts en acier vendus comme connecteurs de bijoux DIY. |
| 24 | 1005006480481569 | connecteur bijoux | ACCEPT | Fermoirs-connecteurs et perles à sertir en lot pour bracelets et colliers DIY. |
| 25 | 1005004090053707 | chaine bijoux | REJECT | Collier cordon déjà assemblé avec fermoir; pas une chaîne brute ou au mètre. |
| 26 | 1005007195554088 | fermoir bijoux | ACCEPT | Dos de broche verrouillables, fermoirs composants pour badges et broches DIY. |
| 27 | 1005010367114526 | anneau bijoux | REJECT | Quincaillerie de porte-clés, pas un anneau de bijouterie correspondant au mot-clé. |
| 28 | 1005004728200599 | connecteur bijoux | ACCEPT | Chaînettes d’extension avec fermoir, connecteurs pour colliers et bracelets DIY. |
| 29 | 1005009750442030 | chaine bijoux | REJECT | Fermoir magnétique vendu sous un mot-clé chaîne bijoux; type de produit incorrect. |
| 30 | 1005004940690176 | fermoir bijoux | ACCEPT | Fermoirs ronds ouvrables utilisables comme composants de bijoux DIY. |
| 31 | 1005004231470304 | anneau bijoux | REJECT | Ouvre-anneau, donc outil et non lot d’anneaux correspondant au mot-clé. |
| 32 | 1005010617021740 | chaine bijoux | REJECT | Collier multicouche fini à porter. |
| 33 | 1005004354785171 | fermoir bijoux | REJECT | Cordons de lanière pour mobile et porte-clés, hors fermoir de bijouterie ciblé. |
| 34 | 1005005643488279 | anneau bijoux | ACCEPT | Lot d’anneaux de saut ouverts pour fabrication de bracelets et colliers. |
| 35 | 1005010113680187 | chaine bijoux | REJECT | Porte-clés et chaîne de téléphone finis, hors composant de bijouterie. |
| 36 | 1005005356326202 | fermoir bijoux | REJECT | Mousqueton porte-clés automobile avec tire-bouchon, hors fermoir de bijoux. |
| 37 | 32864732463 | anneau bijoux | ACCEPT | Anneaux de saut fendus en vrac pour montage de bijoux. |
| 38 | 1005007656082595 | chaine bijoux | REJECT | Collier à pampilles fini à porter. |
| 39 | 1005006020391528 | anneau bijoux | REJECT | Kit multi-apprêts en boîte; le listing ne correspond pas précisément au mot-clé anneau bijoux. |
| 40 | 1005007896217282 | chaine bijoux | REJECT | Chaîne de pantalon/portefeuille finie, hors fabrication de bijoux. |
| 41 | 1005009078417537 | anneau bijoux | REJECT | Bague de doigt finie à porter. |
| 42 | 1005007201594584 | chaine bijoux | REJECT | Collier pendentif croix fini à porter. |
| 43 | 1005007064366924 | anneau bijoux | REJECT | Bague en titane finie à porter. |
| 44 | 1005002600043600 | chaine bijoux | REJECT | Collier à pampilles fini à porter. |
| 45 | 1005010188125851 | anneau bijoux | REJECT | Anneaux ressort pour sacs et porte-clés, quincaillerie hors anneaux de bijouterie ciblés. |
| 46 | 1005003809676658 | chaine bijoux | REJECT | Collier de perles fini à porter. |
| 47 | 1005005910946307 | anneau bijoux | REJECT | Bagues fines finies à porter. |
| 48 | 1005005962441480 | chaine bijoux | REJECT | Collier chaîne déjà assemblé et fini. |
| 49 | 1005006749680203 | anneau bijoux | REJECT | Chaîne et anneaux de porte-clés, hors anneaux pour fabrication de bijoux. |
| 50 | 1005009235630026 | chaine bijoux | REJECT | Chaîne de corps finie à porter. |
| 51 | 1005009895170968 | anneau bijoux | REJECT | Ajusteurs transparents pour bagues, pas des anneaux composants. |
| 52 | 1005006140865954 | chaine bijoux | REJECT | Collier en or fini à porter. |
| 53 | 1005005836843541 | anneau bijoux | ACCEPT | Anneaux fendus métalliques en vrac pour pendentifs et créations DIY. |
| 54 | 1005009676321463 | chaine bijoux | REJECT | Bracelet chaîne fini à porter. |
| 55 | 1005005951848708 | anneau bijoux | REJECT | Boucles de bracelet de montre, hors anneaux pour bijoux DIY. |
| 56 | 1005006949491823 | chaine bijoux | ACCEPT | Cordon brut en cuir/cire vendu pour monter colliers et pendentifs DIY. |
| 57 | 1005009975374525 | chaine bijoux | REJECT | Produit anti-perte décrit de façon ambiguë; aucune chaîne de bijouterie brute identifiable. |
| 58 | 1005005022137696 | chaine bijoux | REJECT | Collier croix fini à porter. |
| 59 | 1005010672519119 | chaine bijoux | REJECT | Collier en or fini à porter. |
| 60 | 1005010028332632 | chaine bijoux | REJECT | Sangle-chaîne de remplacement pour sac, hors chaîne de bijouterie. |
| 61 | 1005010115734301 | chaine bijoux | REJECT | Chaîne décorative pour sac à main, hors chaîne de bijouterie. |
| 62 | 1005010336658337 | chaine bijoux | REJECT | Lot de perles silicone associé à des chaînes de sucette; le produit ne correspond pas au mot-clé chaîne bijoux. |
| 63 | 1005009677832966 | fermoir bijoux | REJECT | Fermoir de coffre/boîte à bijoux, quincaillerie de rangement et non apprêt de bijouterie. |
| 64 | 1005007260137775 | anneau bijoux | REJECT | Ensemble de bagues finies à porter. |
| 65 | 1005009963955526 | connecteur bijoux | ACCEPT | Mousquetons-connecteurs en D annoncés pour fabrication de bijoux et porte-clés DIY. |
| 66 | 1005012692579196 | chaine bijoux | REJECT | Collier en or massif fini à porter. |
| 67 | 1005011750457084 | fermoir bijoux | REJECT | Kit générique pour enfants avec fermoirs; pas un listing de fermoirs précisément identifié. |
| 68 | 1005008658465836 | anneau bijoux | REJECT | Bague ouverte en argent finie à porter. |
| 69 | 1005006997735643 | chaine bijoux | REJECT | Collier cubain serti fini à porter. |
| 70 | 1005010160812523 | fermoir bijoux | ACCEPT | Fermoir mousqueton rotatif vendu libre pour fabrication DIY. |
| 71 | 1005003233085372 | anneau bijoux | ACCEPT | Anneaux de fil ouverts/fermés destinés à connecter des perles. |
| 72 | 1005009912812715 | chaine bijoux | REJECT | Chaîne en or vendue comme bijou fini, pas comme composant au mètre. |
| 73 | 1005010130042388 | aiguille perles | ACCEPT | Boîte de dix aiguilles ouvertes spécifiquement destinées à l’enfilage de perles. |
| 74 | 1005009235398907 | aiguille perles | REJECT | Kit de pinces; ne correspond pas au mot-clé aiguille perles. |
| 75 | 1005004347075695 | aiguille perles | REJECT | Limes aiguilles pour sculpture/affûtage, pas aiguilles d’enfilage de perles. |
| 76 | 1005007481186680 | pendentif | REJECT | Perles bicônes en cristal; ne correspondent pas au mot-clé pendentif. |
| 77 | 1005005957523050 | pendentif | ACCEPT | Pendentif cône en pierre naturelle vendu sans chaîne comme élément à monter. |
| 78 | 1005007249737394 | pendentif | REJECT | Support de porte-clés lettre, hors pendentif de bijouterie. |
| 79 | 1005009924831307 | pendentif | REJECT | Collier croix fini à porter. |
| 80 | 32729683248 | pendentif | ACCEPT | Pendentifs lettres en argent 925 vendus comme éléments libres pour collier. |
| 81 | 1005005504407395 | pendentif | REJECT | Collier multicouche fini à porter. |
| 82 | 1005010057691748 | pendentif | REJECT | Collier pendentif fini à porter. |
| 83 | 1005005820334724 | pendentif | REJECT | Ensemble collier et boucles d’oreilles fini. |
| 84 | 1005006779288194 | pendentif | REJECT | Collier lettre-fleur fini à porter. |
| 85 | 1005003235709582 | pendentif | REJECT | Tatouage temporaire, sans rapport avec un pendentif matériel. |
| 86 | 1005008188705135 | pendentif | REJECT | Collier ras-du-cou fini à porter. |
| 87 | 1005006844227226 | pendentif | REJECT | Collier croix fini à porter. |
| 88 | 1005009962808044 | pendentif | REJECT | Collier pendentif cheval fini à porter. |
| 89 | 1005007587322682 | pendentif | ACCEPT | Médaillon cœur ouvrable vendu comme pendentif à monter. |
| 90 | 1005006124355228 | pendentif | REJECT | Moule silicone pour pendentif; c’est un outil, pas le pendentif visé par le mot-clé. |
| 91 | 1005009234078401 | pendentif | REJECT | Collier avec pendentif cœur fini à porter. |
| 92 | 1005009305134236 | pendentif | REJECT | Collier ras-du-cou déjà assemblé. |
| 93 | 1005010452571403 | pendentif | ACCEPT | Lot de trois pendentifs grenade en cuivre annoncé pour montage DIY. |
| 94 | 1005005906450787 | pendentif | REJECT | Ensemble collier, boucles et bague fini. |
| 95 | 1005007100519168 | pendentif | REJECT | Collier pendentif en cristal fini à porter. |
| 96 | 1005009929507871 | pendentif | ACCEPT | Pendentif floral plaqué vendu comme accessoire de bricolage. |
| 97 | 1005009087592250 | pendentif | REJECT | Collier lettre initiale fini à porter. |
| 98 | 1005011605999859 | pendentif | REJECT | Porte-clés/breloque de sac ou téléphone, hors pendentif de bijouterie. |
| 99 | 1005003734932535 | pendentif | ACCEPT | Pendentif clé en argent 925 vendu comme élément libre. |
| 100 | 1005009691579721 | pendentif | ACCEPT | Pendentif serti de zircon vendu comme composant DIY. |
| 101 | 1005009870554211 | pendentif | REJECT | Chaîne de collier déjà assemblée; ne correspond pas au mot-clé pendentif. |
| 102 | 1005007649894463 | pendentif | REJECT | Collier pendentif Peter Pan fini à porter. |
| 103 | 1005010627972757 | pendentif | REJECT | Porte-clés pendentif fruit, hors fabrication de bijoux. |
| 104 | 1005011946342701 | pendentif | ACCEPT | Pendentif personnalisable en acier inoxydable, élément matériel identifiable. |
| 105 | 1005006493208538 | pendentif | REJECT | Lien de commande personnalisée à contacter avant achat, sans produit standard vérifiable. |
| 106 | 1005005315994038 | pendentif | REJECT | Boîte-présentoir lumineuse pour pendentif, rangement/emballage exclu. |
| 107 | 1005009991451141 | pendentif | REJECT | Pendentif et lanière décorative de sac finis, hors composant de bijouterie. |
| 108 | 1005006057278305 | pendentif | REJECT | Collier de joaillerie fine avec pendentif, produit fini. |
| 109 | 1005009820840736 | pendentif | REJECT | Collier avec faux cristal, produit fini à porter. |
| 110 | 1005009842516610 | pendentif | REJECT | Listing ambigu de pendentif-collier fini; aucun composant libre clairement établi. |
| 111 | 1005004329395800 | pendentif | REJECT | Prestation de bijoux personnalisés couvrant plusieurs produits finis. |
| 112 | 1005006628497973 | pendentif | REJECT | Collier diamant en or fini à porter. |
| 113 | 1005007790420639 | pendentif | REJECT | Collier ras-du-cou Y2K fini. |
| 114 | 1005009444106436 | pendentif | REJECT | Suspension décorative pour la maison, pas un pendentif de bijouterie. |
| 115 | 1005007261097547 | pendentif | REJECT | Collier de joaillerie fine avec pendentif, produit fini. |
| 116 | 1005009233074734 | pendentif | REJECT | Porte-clés réfléchissant fini, hors pendentif de bijouterie. |
| 117 | 1005009304708157 | pendentif | ACCEPT | Lot de dix médailles ovales vendu comme pendentifs/breloques à monter. |
| 118 | 1005004811099680 | pendentif | REJECT | Collier Hip-Hop fini à porter. |
| 119 | 1005008971843133 | pendentif | REJECT | Collier croix fini à porter. |
| 120 | 1005008613752699 | pendentif | REJECT | Collier écouteurs/musique fini à porter. |
| 121 | 1005009532787758 | pendentif | ACCEPT | Élément cœur pour bracelet italien modulaire vendu comme pendentif/breloque composant. |
| 122 | 1005010683007365 | pendentif | REJECT | Collier en or pur fini à porter. |
| 123 | 1005008035580790 | perles bois | REJECT | Bracelets en cuir avec perles bois, produits finis. |
| 124 | 1005005216686671 | perles bois | REJECT | Ensemble de bracelets tressés fini à porter. |
| 125 | 4000135985475 | perles bois | REJECT | Perceuse de banc pour fabriquer des perles; ne correspond pas au mot-clé perles bois. |
| 126 | 1005008827037638 | perles bois | REJECT | Lustre avec perles en bois, luminaire hors fabrication de bijoux. |
| 127 | 1005009564286365 | perles bois | REJECT | Mannequin articulé en bois, pas des perles de bijouterie. |
| 128 | 1005006094325216 | perles lettres | ACCEPT | Perles lettres en silicone vendues libres pour bracelets et accessoires DIY. |
| 129 | 1005010337929441 | perles lettres | ACCEPT | Kit de perles acryliques comprenant lettres et cœurs pour bijoux DIY. |
| 130 | 1005007537625136 | perles lettres | ACCEPT | Perles alphabet en silicone vendues en vrac pour création DIY. |
| 131 | 1005010112298143 | perles lettres | ACCEPT | Perles cubiques alphabet acryliques en vrac. |
| 132 | 1005002829381386 | perles lettres | ACCEPT | Perles-breloques lettres en argent 925, composants pour bracelets et colliers. |
| 133 | 4001155561845 | perles lettres | ACCEPT | Perles alphabet acryliques rondes/plates en vrac. |
| 134 | 1005007928318615 | perles lettres | REJECT | Bracelet personnalisé en perles, produit fini. |
| 135 | 1005009967603033 | perles lettres | ACCEPT | Perles cubes lettres en bois vendues en vrac. |
| 136 | 1005004900086210 | perles miyuki | REJECT | Rocailles japonaises génériques sans mention de la marque Miyuki; correspondance SEO non prouvée. |
| 137 | 1005006588143036 | perles miyuki | REJECT | Rocailles génériques sans mention de la marque Miyuki. |
| 138 | 1005010116309548 | perles miyuki | REJECT | Rocailles tchèques, donc incompatibles avec le mot-clé perles Miyuki. |
| 139 | 1005004757435168 | perles miyuki | REJECT | Rocailles japonaises génériques sans preuve qu’il s’agit de Miyuki. |
| 140 | 1005010642243255 | perles miyuki | REJECT | Boîte de rangement pour matériel/nail art, pas des perles Miyuki. |
| 141 | 1005009866728025 | perles naturelles | ACCEPT | Perles d’eau douce naturelles libres et semi-finies pour fabrication de bijoux. |
| 142 | 1005006199996560 | perles naturelles | ACCEPT | Perles naturelles en coquillage/nacre vendues libres pour montage. |
| 143 | 4000734226690 | perles naturelles | REJECT | Boucles d’oreilles en perles finies à porter. |
| 144 | 1005002593573686 | perles naturelles | ACCEPT | Perles d’eau douce naturelles libres pour création DIY. |
| 145 | 1005010569216233 | perles naturelles | ACCEPT | Perles de culture Keshi libres pour colliers et accessoires DIY. |
| 146 | 1005012865053529 | perles naturelles | ACCEPT | Perles en pierre naturelle vendues libres pour fabrication de bijoux. |
| 147 | 1005010728396088 | perles naturelles | ACCEPT | Perles d’eau douce baroques libres destinées au montage. |
| 148 | 1005007351482602 | perles pour bijoux | ACCEPT | Perles rondes en pierres naturelles, dont agate, vendues libres pour bijoux DIY. |
| 149 | 1005005028774396 | fil élastique bracelet | ACCEPT | Cordon élastique brut destiné aux bracelets de perles. |
| 150 | 1005010339655180 | perles pour bijoux | REJECT | Collier pendentif à pampilles fini, pas une chaîne perlée composant. |
| 151 | 1005001811978232 | perles pour bijoux | ACCEPT | Perles rondes en pierres naturelles, dont agate, vendues libres. |
| 152 | 1005007627723800 | perles pour bijoux | ACCEPT | Perles rondes d’obsidienne libres correspondant au mot-clé large perles pour bijoux. |
| 153 | 1005003749499773 | perles pour bijoux | ACCEPT | Perles en pierres naturelles incluant agate, destinées au montage DIY. |
| 154 | 1005007510843875 | perles pour bijoux | REJECT | Bracelet de pierres naturelles fini à porter. |
| 155 | 1005009425375244 | perles pour bijoux | ACCEPT | Perles d’extrémité à sertir vendues comme fournitures de fabrication de bijoux. |
| 156 | 1005008497784580 | fil élastique bracelet | REJECT | Le listing précise une ligne de pêche non élastique; incompatible avec fil élastique bracelet. |
| 157 | 1005004776599876 | perles pour bijoux | ACCEPT | Perles rondes acryliques en vrac pour bracelets et colliers DIY. |
| 158 | 1005003904227639 | perles pour bijoux | ACCEPT | Perles d’espacement pavées de zircon vendues comme composants de bijoux. |
| 159 | 1005009050969307 | perles pour bijoux | REJECT | Perles/capuchons pour tresses et coiffure, hors fabrication de bijoux. |
| 160 | 1005006180414362 | perles pour bijoux | ACCEPT | Lot de perles acryliques libres annoncé pour colliers et boucles DIY. |
| 161 | 4000776803844 | perles pour bijoux | ACCEPT | Perles rondes acryliques en vrac pour fabrication de bracelets. |
| 162 | 1005006249828068 | perles pour bijoux | REJECT | Microbilles de caviar destinées au nail art, pas des perles de bijouterie. |
| 163 | 1005009514248898 | perles pour bijoux | REJECT | Fermoirs et capuchons-connecteurs; le produit ne correspond pas au mot-clé perles pour bijoux. |
| 164 | 1005006658832995 | perles pour bijoux | REJECT | Chaîne de microbilles destinée au nail art, hors fourniture de bijouterie. |
| 165 | 1005009647930740 | perles pour bijoux | ACCEPT | Perles d’espacement en argent 925 vendues libres pour montage. |
| 166 | 1005009946177142 | perles pour bijoux | ACCEPT | Perles acryliques mélangées vendues comme composants de bracelets et chaînes de téléphone DIY. |
| 167 | 1005008686015166 | perles pour bijoux | REJECT | Aiguilles d’enfilage; outil utile mais incompatible avec le mot-clé perles pour bijoux. |
| 168 | 1005008180291857 | perles pour bijoux | ACCEPT | Assortiment de perles de riz avec environ 5 200 pièces; la boîte contient bien la matière à monter. |
| 169 | 1005008343049436 | perles pour bijoux | REJECT | Bagues en perles finies à porter. |
| 170 | 1005008920866460 | perles pour bijoux | ACCEPT | Perles rondes d’agate mousse naturelle vendues libres. |
| 171 | 1005006614905930 | perles pour bijoux | ACCEPT | Perles fleurs acryliques annoncées comme fournitures DIY de bijoux. |
| 172 | 1005003712175747 | perles pour bijoux | REJECT | Ensemble de bijoux de mariage fini. |
| 173 | 1005011572931563 | perles pour bijoux | REJECT | Bracelet en perles de résine fini à porter. |
| 174 | 1005005676593287 | perles pour bijoux | REJECT | Ensemble de bijoux de mariage traditionnel fini. |
| 175 | 1005012414149142 | perles pour bijoux | ACCEPT | Perles fleurs en résine/acrylique vendues en vrac pour bijoux DIY. |
| 176 | 1005012867412045 | perles pour bijoux | REJECT | Ensemble de trois bracelets en perles fini à porter. |
| 177 | 1005010636826181 | perles pour bijoux | REJECT | Boîte de rangement pour matériel de nail art, pas un listing fiable de perles de bijouterie. |
| 178 | 1005005030522898 | perles rocailles | ACCEPT | Rocailles de verre métalliques vendues en vrac pour tissage et fabrication de bijoux. |
| 179 | 1005004988988392 | perles rocailles | ACCEPT | Rocailles de verre en vrac pour couture et bijoux DIY. |
| 180 | 4000301030517 | perles verre | ACCEPT | Perles facettées en verre vendues comme intercalaires pour bijoux. |
| 181 | 1005009993671743 | perles verre | ACCEPT | Perles de riz en verre vendues en vrac pour bijoux DIY. |
| 182 | 1005007327797143 | perles verre | ACCEPT | Perles craquelées en verre vendues libres pour bracelets et boucles. |
| 183 | 1005003470627506 | perles verre | ACCEPT | Perles facettées en verre vendues libres pour fabrication de bijoux. |
| 184 | 1005011538932194 | perles verre | ACCEPT | Perles d’espacement opaques en verre vendues en lot pour bracelets DIY. |
| 185 | 1005010160381459 | perles verre | ACCEPT | Perles rondes en verre imitation jade vendues en vrac. |
| 186 | 1005011705401612 | perles verre | REJECT | Luminaires suspendus avec décoration de perles, produit hors fabrication de bijoux. |
| 187 | 1005012722271060 | perles verre | ACCEPT | Lot de perles en verre à deux trous vendu comme matière de création. |
| 188 | 1005009270826404 | perles verre | ACCEPT | Perles cœur en verre/cristal vendues libres pour bricolage. |
| 189 | 1005010011405957 | perles verre | REJECT | Bouteilles et décorations de nail art, pas des perles verre pour bijoux. |
| 190 | 1005006397455406 | pince bijoux | ACCEPT | Micro pince coupante de précision explicitement destinée aux fils et modèles de bijoux. |
| 191 | 1005009724921496 | pince bijoux | ACCEPT | Pince diagonale/coupe-fil utilisable pour fil de cuivre et fabrication de bijoux. |
| 192 | 1005008163207800 | pince bijoux | ACCEPT | Pince de préhension quatre griffes pour saisir perles et pierres. |
| 193 | 1005006466442738 | pince bijoux | REJECT | Pince-jouet en plastique pour enfants, pas un outil de bijouterie. |
| 194 | 1005012614502961 | pince bijoux | REJECT | Embouts et support de soudage de rechange, pas une pince bijoux complète correspondant au mot-clé. |
| 195 | 1005012709664077 | support boucle d'oreille | REJECT | Présentoir et rangement à bijoux, pas un support composant de boucle d’oreille. |
| 196 | 1005004512982501 | support boucle d'oreille | REJECT | Mousquetons et crochets de porte-clés, pas des supports de boucles d’oreilles. |
| 197 | 1005012701879841 | support boucle d'oreille | REJECT | Porte-bijoux et organisateur de bureau, rangement exclu. |
| 198 | 1005006802810670 | support boucle d'oreille | REJECT | Présentoir/arbre et boîte de rangement à bijoux, rangement exclu. |
| 199 | 1005008325238402 | support boucle d'oreille | REJECT | Boucles d’oreilles serties finies à porter, pas des supports libres. |
| 200 | 1005009581440117 | support boucle d'oreille | REJECT | Quincaillerie de boîte-cadeau en bois, hors support de boucle d’oreille. |

## Limites

Audit fondé sur les données du catalogue courant, notamment le titre AliExpress capturé. Un ACCEPT valide l’adéquation sémantique et le type de produit dans ce fichier; il ne valide pas le fournisseur, la variante exacte, le prix livré, la conformité, la propriété intellectuelle ni la disponibilité actuelle.

import fs from "node:fs/promises";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const outputDir = "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/codex-chasse-clusters/outputs/20260720-200609";
const rawCompaniesPath = "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/codex-chasse-clusters/runs/20260720-200609/brandsearch-entreprises-filtrees.json";
const reportPath = "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/codex-chasse-clusters/reports/validation-multimarche-brandsearch-20260720-200609-a1.md";
const eurUsd = 1.1435;

const radarHeaders = [
  "Rang", "Statut", "Priorité", "Produit / niche", "Marché pilote",
  "Volume SEMrush / mois", "Autre marché", "Volume autre marché",
  "Entreprise témoin", "Visites mensuelles", "Google Ads actives", "Meta Ads actives",
  "Prix moyen boutique (USD)", "Prix moyen approx. (EUR)", "Trends 52/52",
  "Prix / lecture SERP", "Verdict / gate", "Risque principal",
  "Requête AliExpress manuelle", "Lien fournisseur AliExpress",
  "URL BrandSearch", "Source web", "Observé", "Manquant", "Hypothèse", "Rapport"
];

const radarRows = [
  [1,"VALIDÉ",1,"Housse de voiture sur mesure intérieure/extérieure","FR",105710,"UK",64460,"ukcustomcovers.com",28819,40,0,131.26,null,0.072,"UK 121,94–211,27 GBP ; plusieurs spécialistes FR/UK","RETENU_MARCHE_A_SOURCER","Gabarits véhicule/année, humidité, rayures et retours","custom fit car cover waterproof breathable make model year EU warehouse","","https://app.brandsearch.co/brand-analysis/ukcustomcovers.com","https://www.coversandall.co.uk/vehicle-covers/car-covers-sc","FR et UK au-dessus de 10K ; Trends FR +7,2 %, UK +40,6 %","Fournisseur, coût rendu, stock et délai","Un modèle respirant réellement ajusté peut soutenir un prix premium",reportPath],
  [2,"VALIDÉ",1,"Fauteuil suspendu avec pied","FR",72520,"DE",236300,"www.lasiesta.com",139613,40,0,274.62,null,-0.033,"Produits premium observés autour de 290–350 EUR","RETENU_MARCHE_A_SOURCER","Colis volumineux, charge, stabilité, structure et pièces","fauteuil suspendu avec pied résine tressée 150 kg entrepôt Europe","","https://app.brandsearch.co/brand-analysis/lasiesta.com","https://www.lasiesta.com/","FR et DE très au-dessus de 10K ; acteur à 139 613 visites/mois","Fournisseur, dimensions colis, coût retour et conformité","Un bundle pied + assise + housse peut rester défendable malgré la saisonnalité",reportPath],
  [3,"VALIDÉ",1,"Évier de cuisine inox/granit avec robinet","FR",73800,"IT",255630,"evhoc.it",9866,40,0,326.40,null,0.187,"Lapeyre : nombreuses références 91,50–597 EUR","RETENU_MARCHE_A_SOURCER","Dimensions, inox réel, bonde, raccords, fuite et casse","304 stainless kitchen sink waterfall faucet set drain basket EU warehouse","","https://app.brandsearch.co/brand-analysis/evhoc.it","https://www.lapeyre.fr/v/evier-avec-robinetterie","FR et IT très au-dessus de 10K ; Trends FR +18,7 %","Fournisseur, coût rendu, matériaux et contenu exact","Un kit complet documenté peut se différencier des cuves nues",reportPath],
  [4,"VALIDÉ",1,"Housses de sièges auto sur mesure","UK",118480,"FR",6550,"carfurnisher.com",11643,40,0,354.08,null,0.160,"Bancarel FR : 159,80–390,15 EUR","RETENU_MARCHE_A_SOURCER — UK","Airbags latéraux, gabarits, année/modèle et erreurs de commande","custom fit car seat cover full set side airbag compatible EU warehouse UK","","https://app.brandsearch.co/brand-analysis/carfurnisher.com","https://www.bancarel.com/fr/121-housses-auto-sur-mesure","UK au-dessus de 10K ; Trends UK +16 %","Fournisseur, matrice de compatibilité et preuve airbag","Le Royaume-Uni est le marché pilote ; la France reste sous le seuil",reportPath],
  [5,"VALIDÉ",2,"Valise cabine premium 20 pouces / set compact","ES",79620,"",null,"traveltienda.es",8871,40,0,213.56,null,null,"Nombreux planchers <60 EUR ; prix moyen boutique 213,56 USD","RETENU_MARCHE_A_SOURCER — ES","Dimensions compagnies, roues, poignée, serrure TSA et pièces","premium carry on luggage 20 inch TSA removable wheels EU warehouse Spain","","https://app.brandsearch.co/brand-analysis/traveltienda.es","https://elpais.com/escaparate/estilo-de-vida/2026-05-07/maleta-de-cabina.html","ES 79 620/mois ; boutique spécialisée de 29 produits","Fournisseur, résistance, pièces et coût livré","Seul un angle premium objectivement prouvé évite la guerre des prix",reportPath],
  [6,"VALIDÉ",2,"Haltères réglables 20–40 kg","FR",11090,"ES",13930,"www.gorillasports.es",7431,40,0,159.59,null,null,"Prix moyen boutique 159,59 USD ; deux acteurs Search-only","RETENU_MARCHE_A_SOURCER","Verrouillage, chute de disques, charge réelle, pièces et colis lourd","adjustable dumbbell pair 24kg 40kg safety lock EU warehouse","","https://app.brandsearch.co/brand-analysis/gorillasports.es","https://www.gorillasports.es/","FR et ES juste au-dessus de 10K","Fournisseur, test mécanique, coût et casse transport","Un mécanisme fiable et des pièces disponibles sont indispensables",reportPath],
  [7,"VALIDÉ",2,"Parure de lit premium / hôtelière","UK",19990,"",null,"beddingenvy.co.uk",100422,40,0,329.02,null,0.418,"Bamboo set observé dès env. 110 GBP ; marché de marques","RETENU_MARCHE_A_SOURCER — UK","Matière, grammage, tailles, retrait, couleur et retours hygiène","luxury hotel bedding set cotton bamboo king size EU warehouse UK","","https://app.brandsearch.co/brand-analysis/beddingenvy.co.uk","https://www.livingetc.com/advice/where-to-buy-bedding","UK 19 990/mois ; Trends +41,8 % ; 100 422 visites témoin","Fournisseur, composition certifiée et stabilité au lavage","Une promesse hôtelière factuelle peut soutenir la tranche 85–400 EUR",reportPath],
  [8,"VALIDÉ",2,"Meuble-cage pour chien / double niche intérieure","UK",13280,"FR",2060,"www.lordsandlabradors.co.uk",79059,40,0,263.97,null,0.182,"Aosom UK : double meuble-cage 234,99 GBP","RETENU_MARCHE_A_SOURCER — UK","Dimensions, barreaux, ventilation, stabilité, morsure et colis","wood dog crate furniture large double door removable tray EU warehouse UK","","https://app.brandsearch.co/brand-analysis/lordsandlabradors.co.uk","https://www.aosom.co.uk/dog-pet-supplies/dog-cages-c730.html","UK 13 280/mois ; Trends +18,2 % ; témoin à 79 059 visites","Fournisseur, sécurité animale, charge et coût retour","Le marché pilote est le Royaume-Uni ; la France reste sous le seuil",reportPath],
  [9,"À CREUSER",3,"Panneau mural décoratif de douche","DE",46220,"FR",13510,"xn--duschrckwand-platten-uec.de",18006,40,0,424.07,null,0.119,"Leroy Merlin : 1 639 résultats ; Castorama env. 112–500 EUR","Marché prouvé, concurrence/logistique à résoudre","Format, découpe, adhésif, étanchéité et avarie transport","shower wall panel aluminium composite 90x210 waterproof EU warehouse","","https://app.brandsearch.co/brand-analysis/xn--duschrckwand-platten-uec.de","https://www.leroymerlin.fr/produits/salle-de-bains/douche/panneau-mural-douche/","DE et FR au-dessus de 10K ; Trends FR +11,9 %","Fournisseur, structure du panneau et coût livré","Un décor exclusif ou une découpe simple doit compenser les grands catalogues",reportPath],
  [10,"À CREUSER",3,"Vasque de salle de bain design à poser","FR",368610,"",null,"www.lemondedubain.com",55560,40,0,452.84,null,null,"Prix indicatif 50–500 EUR ; spécialistes et grandes enseignes","Demande forte, faisabilité fragile","Céramique, éclats, dimensions, bonde, trop-plein et casse","ceramic countertop bathroom basin design EU warehouse","","https://app.brandsearch.co/brand-analysis/lemondedubain.com","https://www.castorama.fr/idees-et-conseils/choisir-une-vasque-ou-un-lavabo/CF_CC_npcart_100479.art","FR 368 610/mois ; témoin à 55 560 visites","Fournisseur, emballage, taux casse et coût retour","Un matériau moins cassant ou un emballage documenté peut rouvrir la piste",reportPath],
  [11,"À CREUSER",3,"Salon de jardin en résine tressée","UK",122080,"FR",15450,"www.rattantree.com",101487,40,0,172.40,null,-0.039,"Planchers 99–200 EUR ; premium >500 EUR","Marché fort, économie non prouvée","Volume colis, saisonnalité, acier/alu, coussins et retours","rattan garden furniture set 4 seat aluminium frame EU warehouse UK","","https://app.brandsearch.co/brand-analysis/rattantree.com","https://www.therange.co.uk/outdoor-living/garden-furniture/rattan-garden-furniture/","UK et FR au-dessus de 10K ; 101 487 visites témoin","Coût livré, entrepôt local et qualité de structure","Un petit set aluminium compact pourrait survivre aux planchers bas",reportPath],
  [12,"À CREUSER",3,"Coussin chauffant premium infrarouge / batterie","FR",47060,"BE",12750,"opoggi.com",38,40,0,217.97,null,0.042,"Génériques dès 29,95 EUR ; témoin premium 217,97 USD moyen","Prix premium non démontré","Sécurité électrique, surchauffe, batterie, textile et allégations","premium infrared heated cushion rechargeable auto shutoff EU warehouse","","https://app.brandsearch.co/brand-analysis/opoggi.com","https://www.idealo.fr/cat/10952F850388/couvertures-coussins-chauffants-electriques.html","FR, BE et NL passent 10K ; Trends FR +4,2 % mais très saisonnier","Preuve produit premium, certificats, coût et fournisseur","La piste ne vit que si le produit est objectivement différent du générique à 30 EUR",reportPath],
  [13,"À CREUSER",3,"Receveur de douche SMC effet pierre","FR",195140,"",null,"www.lemondedubain.com",55560,40,0,452.84,null,null,"Médiane observée env. 146 EUR ; Aurlane très présent","Demande forte, concurrence et casse sévères","Formats, bonde, planéité, flexion, emballage et retour","SMC shower tray stone effect drain 90x120 EU warehouse","","https://app.brandsearch.co/brand-analysis/lemondedubain.com","https://magicprices.fr/liste-produit/receveurs-de-douche","FR 195 140/mois ; tranche de prix compatible","Fournisseur, coût rendu, casse et comparabilité","Un format recoupable ou une couleur rare peut créer une poche",reportPath],
  [14,"À CREUSER",3,"Radiateur de salle de bain / sèche-serviettes design","DE",102650,"FR",6290,"heizkoerper.shop",7986,40,0,354.07,null,null,"Prix moyen boutique 354,07 USD ; 46 produits","Marché DE prouvé, risque technique","Puissance, hydraulique/électrique, raccords, normes et installation","bathroom radiator towel warmer 1200x500 connection set EU warehouse Germany","","https://app.brandsearch.co/brand-analysis/heizkoerper.shop","https://heizkoerper.shop/","DE 102 650/mois ; témoin Search-only","Trends DE, fournisseur, conformité et SAV","Un kit raccords documenté peut réduire les erreurs d'installation",reportPath],
  [15,"À CREUSER",3,"Brasero / foyer de jardin premium","DE",42320,"FR",8180,"gardenflare.com",2268,40,0,188.26,null,null,"Prix moyen boutique 188,26 USD ; 24 produits","Marché DE prouvé, saison/sécurité à résoudre","Feu, stabilité, corrosion, fumées, poids et règles locales","outdoor fire pit corten steel spark guard EU warehouse Germany","","https://app.brandsearch.co/brand-analysis/gardenflare.com","https://gardenflare.com/","DE 42 320/mois ; acteur Search-only","Trends DE, fournisseur, matériaux et coût rendu","Un foyer compact avec pare-étincelles et housse peut être testable",reportPath],
  [16,"À CREUSER",3,"Kit grillage de volière / enclos animal","DE",13300,"",null,"drahtexpress.de",15544,40,0,115.98,null,null,"Prix moyen boutique 115,98 USD ; 47 produits","Volume juste ; commodité et poids","Maille, diamètre, galvanisation, bords coupants, rouleau lourd","aviary wire mesh galvanized roll fixing kit EU warehouse Germany","","https://app.brandsearch.co/brand-analysis/drahtexpress.de","https://drahtexpress.de/","DE 13 300/mois ; témoin à 15 544 visites","Trends DE, fournisseur et coût transport","Un bundle complet mesuré par surface doit justifier le panier",reportPath],
  [17,"À CREUSER",3,"Paroi / cabine de douche","ES",40610,"",null,"www.entornobano.com",13186,40,0,412.05,null,null,"Prix moyen boutique 412,05 USD ; 1 404 produits","Marché ES prouvé, casse/installation sévères","Verre, dimensions, réversibilité, perçage, montage et casse","shower enclosure 8mm tempered glass reversible EU warehouse Spain","","https://app.brandsearch.co/brand-analysis/entornobano.com","https://www.entornobano.com/","ES 40 610/mois ; témoin à 13 186 visites","Fournisseur, certification verre et taux casse","Une paroi simple plutôt qu'une cabine complète peut réduire le risque",reportPath],
  [18,"À CREUSER",4,"Barres de toit / galerie spécifique véhicule","UK",189650,"",null,"roofrack.co.uk",4988,40,0,440.20,null,null,"Prix moyen boutique 440,20 USD","Marché massif, responsabilité produit élevée","Compatibilité, charge, fixation, bruit, sécurité routière","roof rack cross bars vehicle specific TUV EU warehouse UK","","https://app.brandsearch.co/brand-analysis/roofrack.co.uk","https://roofrack.co.uk/","UK 189 650/mois ; catalogue de 746 produits","Fournisseur, homologation, charge et assurance","Une sélection limitée de véhicules populaires serait nécessaire",reportPath],
  [19,"À CREUSER",4,"Dashcam 2/3 canaux avec kit câblage","UK",378800,"",null,"www.dashvision.co.uk",10486,40,0,97.46,null,null,"Prix moyen boutique à la borne basse 97,46 USD","Marché massif, concurrence et SAV élevés","Capteur, plaques lisibles, app, firmware, stationnement, chaleur","3 channel dash cam parking mode hardwire kit EU warehouse UK","","https://app.brandsearch.co/brand-analysis/dashvision.co.uk","https://www.dashvision.co.uk/","UK 378 800/mois ; témoin à 10 486 visites","Fournisseur, qualité vidéo réelle, app et SAV","Un bundle complet peut être pertinent seulement avec preuve vidéo indépendante",reportPath],
  [20,"À CREUSER",4,"Kit de suivi de consommation électrique","NL",11290,"BE",5660,"easynrj.com",657,40,0,231.68,null,null,"Prix moyen boutique 231,68 USD ; 9 produits","Signal NL juste, acteur encore petit","Précision, tension, pose, app/cloud, RED/EMC et sécurité","home energy monitor smart meter DIN app EU warehouse Netherlands","","https://app.brandsearch.co/brand-analysis/easynrj.com","https://easynrj.com/","NL 11 290/mois ; BE sous le seuil","Fournisseur, conformité et preuve de précision","Une installation non invasive pourrait réduire le frein technique",reportPath],
  [21,"À CREUSER",4,"Ferme-porte hydraulique premium","FR",51400,"NL",28650,"www.jadesafety.com",3477,40,0,121.14,null,null,"Prix moyen boutique 121,14 USD ; part de marché pro","Demande forte, panier moyen à prouver","Force, poids porte, gabarit, pose, certification et retours","hydraulic door closer adjustable EN1154 full installation kit EU warehouse","","https://app.brandsearch.co/brand-analysis/jadesafety.com","https://www.jadesafety.com/","FR et NL au-dessus de 10K","Fournisseur, prix du produit phare et conformité","Un kit complet avec gabarit et vidéo peut soutenir >85 EUR",reportPath],
  [22,"À CREUSER",4,"Draisienne premium bois/métal","UK",105340,"FR",14910,"bobbinbikes.com",67937,40,0,130.19,null,null,"Prix moyen boutique 130,19 USD ; marque loisir établie","Marché prouvé, sécurité enfant","Hauteur, pneus, stabilité, substances, marquage et responsabilité","premium balance bike adjustable seat pneumatic tires EU warehouse","","https://app.brandsearch.co/brand-analysis/bobbinbikes.com","https://bobbinbikes.com/","UK et FR au-dessus de 10K ; témoin à 67 937 visites","Fournisseur, tests sécurité, conformité et coût","Un design premium ne suffit pas sans dossier de sécurité complet",reportPath],
  [23,"À CREUSER",4,"Tapis de sol auto premium / sur mesure","FR",11350,"FR sur mesure",6480,"omacshop.fr",14080,40,0,174.37,null,null,"Prix moyen boutique 174,37 USD, catalogue large","Famille passe ; sous-produit sur mesure sous 10K","Gabarits, clips, odeur, matière et erreurs de modèle","custom fit car floor mats make model year waterproof EU warehouse","","https://app.brandsearch.co/brand-analysis/omacshop.fr","https://omacshop.fr/","Famille 11 350/mois ; témoin à 14 080 visites","Fournisseur et demande du sous-produit exact","Un angle premium 3D/TPE doit être isolé de la famille générique",reportPath],
  [24,"À CREUSER",4,"Plaque funéraire personnalisable","FR",69200,"FR personnalisée",7860,"plaquedeces.fr",24381,40,0,100.71,null,0.056,"France Tombale : 56–120 EUR et plus","Famille forte ; modèle de production à clarifier","Personnalisation, BAT, émotion client, fabrication et délai","custom memorial plaque outdoor UV resistant personalized photo EU","","https://app.brandsearch.co/brand-analysis/plaquedeces.fr","https://www.france-tombale.fr/plaque-funeraire/plaque-funeraire-personnalisee.html","Famille 69 200/mois ; Trends +5,6 % ; 24 381 visites témoin","Fournisseur et adéquation au modèle AliExpress","La piste ressemble davantage à un atelier local qu'à un dropshipping standard",reportPath],
  [25,"EXCLU",9,"Grille chien / séparation coffre spécifique véhicule","UK",5400,"",null,"travall.de",9755,40,0,139.58,null,null,"Prix moyen boutique 139,58 USD","STOP volume propre","Compatibilité lourde et sous-segment sous 10K","Ne pas sourcer","","https://app.brandsearch.co/brand-analysis/travall.de","https://travall.de/","Entreprise réelle et Search-only","Aucun fournisseur utile à chercher après STOP","Les requêtes modèle par modèle pourraient exister mais ne sont pas attribuables sans doublons",reportPath],
  [26,"EXCLU",9,"Écran de projection motorisé","DE",2820,"FR",1580,"esmart.de",8925,40,0,367.35,null,null,"Prix moyen boutique 367,35 USD","STOP volume","Sous-segment trop étroit malgré le prix","Ne pas sourcer","","https://app.brandsearch.co/brand-analysis/esmart.de","https://esmart.de/","Entreprise spécialisée de 64 produits","Aucun sourcing après STOP volume","Le trafic du témoin peut provenir de longues traînes et autres écrans",reportPath],
  [27,"EXCLU",9,"Kit graphique complet motocross","DE",960,"DE autocollants moto",19100,"arider.com",119004,40,0,158.84,null,null,"Prix moyen boutique 158,84 USD","STOP sous-produit propre","Milliers de modèles/marques et kit complet sous 1K","Ne pas sourcer","","https://app.brandsearch.co/brand-analysis/arider.com","https://arider.com/","Famille autocollants moto 19 100, mais kit propre 960","Répartition modèle/marque non attribuable","La très forte audience de marque ne prouve pas un cluster générique propre",reportPath],
  [28,"EXCLU",9,"Toilette portable de camping","FR",8970,"",null,"casambu.com",17119,40,0,382.62,null,-0.065,"Prix moyen du catalogue 382,62 USD, pas du sous-produit","STOP volume","Hygiène, pièces, retour et volume sous 10K","Ne pas sourcer","","https://app.brandsearch.co/brand-analysis/casambu.com","https://casambu.com/","FR 8 970/mois ; Trends −6,5 %","Prix exact du sous-produit non mesuré","Le catalogue large explique probablement le prix moyen élevé",reportPath],
  [29,"EXCLU",9,"Planche à découper en titane","FR",2640,"",null,"titanecook.com",17555,40,0,119.28,null,1.000,"Prix moyen boutique 119,28 USD","STOP volume","Base Trends minuscule, matière/authenticité à prouver","Ne pas sourcer","","https://app.brandsearch.co/brand-analysis/titanecook.com","https://titanecook.com/","FR 2 640/mois ; Trends +100 % sur base quasi nulle","Aucune preuve fournisseur ou matière","La croissance relative ne compense pas le manque de demande absolue",reportPath],
  [30,"EXCLU",9,"Kit HDMI sans fil","NL",1210,"",null,"marmitek.com",50011,40,0,120.10,null,null,"Prix moyen boutique 120,10 USD","STOP volume","Latence, HDCP, résolution, portée et SAV","Ne pas sourcer","","https://app.brandsearch.co/brand-analysis/marmitek.com","https://marmitek.com/","NL 1 210/mois ; marque à 50 011 visites","Aucun sourcing après STOP volume","La force de Marmitek ne prouve pas une demande générique suffisante",reportPath]
];

const semrushQueries = {
  1: ["housse voiture", "car cover"],
  2: ["fauteuil suspendu", "hängesessel"],
  3: ["évier cuisine", "lavello cucina"],
  4: ["car seat covers", "housse siège voiture"],
  5: ["maleta de cabina", ""],
  6: ["haltères réglables", "mancuernas ajustables"],
  7: ["luxury bedding", ""],
  8: ["dog crate furniture", "meuble cage chien"],
  9: ["duschrückwand", "panneau mural douche"],
  10: ["vasque salle de bain", ""],
  11: ["rattan garden furniture", "salon de jardin résine tressée"],
  12: ["coussin chauffant", "warmtekussen"],
  13: ["receveur de douche", ""],
  14: ["badheizkörper", "radiateur sèche serviette"],
  15: ["feuerstelle garten", "brasero jardin"],
  16: ["volierendraht", ""],
  17: ["mampara de ducha", ""],
  18: ["roof rack", ""],
  19: ["dash cam", ""],
  20: ["energiemeter", "energiemeter"],
  21: ["ferme porte", "deurdranger"],
  22: ["balance bike", "draisienne enfant"],
  23: ["tapis de sol voiture", "tapis voiture sur mesure"],
  24: ["plaque funéraire", "plaque funéraire personnalisée"],
  25: ["dog guard car", ""],
  26: ["motorleinwand", "écran projection motorisé"],
  27: ["motocross dekor", "motorrad aufkleber"],
  28: ["toilette portable", ""],
  29: ["planche à découper titane", ""],
  30: ["draadloze hdmi", ""]
};

const rawCompanies = JSON.parse(await fs.readFile(rawCompaniesPath, "utf8"));

const workbook = Workbook.create();
const summary = workbook.worksheets.add("Synthèse");
const radar = workbook.worksheets.add("Radar 30");
const companies = workbook.worksheets.add("Entreprises 216");
const measures = workbook.worksheets.add("Mesures");
const method = workbook.worksheets.add("Méthode");

for (const sheet of [summary, radar, companies, measures, method]) sheet.showGridLines = false;

const navy = "#17365D";
const blue = "#D9EAF7";
const green = "#E2F0D9";
const orange = "#FCE4D6";
const red = "#F4CCCC";
const light = "#F4F7FA";
const gray = "#6B7280";

// Méthode first so cross-sheet formulas can reference it.
method.getRange("A1:H2").merge();
method.getRange("A1").values = [["MÉTHODE, SEUILS ET SOURCES"]];
method.getRange("A1:H2").format = { fill: navy, font: { bold: true, color: "#FFFFFF", size: 16 }, verticalAlignment: "center" };
method.getRange("A4:B10").values = [
  ["Paramètre", "Valeur"],
  ["EUR/USD (17-07-2026)", eurUsd],
  ["Seuil volume par marché", 10000],
  ["Prix cible minimum (EUR)", 85],
  ["Prix cible maximum (EUR)", 400],
  ["Google Ads actives minimum", 1],
  ["Meta Ads actives maximum", 0]
];
method.getRange("A4:B4").format = { fill: blue, font: { bold: true, color: navy } };
method.getRange("B5").format.numberFormat = "0.0000";
method.getRange("B6:B10").format.numberFormat = "#,##0";
method.getRange("A12:H18").values = [
  ["Règle", "Définition", null, null, null, null, null, null],
  ["VALIDÉ", "Marché qualifié et retenu pour sourcing manuel. Ce n'est pas une validation fournisseur ni une autorisation de lancement.", null, null, null, null, null, null],
  ["À CREUSER", "Preuve de marché réelle, mais un risque important empêche le passage immédiat en sourcing prioritaire.", null, null, null, null, null, null],
  ["EXCLU", "Sous-produit sous 10K ou risque structurel. Ne pas sourcer sans nouvelle thèse documentée.", null, null, null, null, null, null],
  ["Volumes", "Jamais de somme entre pays pour franchir le seuil. Les volumes sont lus dans la base SEMrush locale.", null, null, null, null, null, null],
  ["AliExpress", "Blocage Chrome documenté. Aucun fournisseur, prix, stock ou délai inventé ; requêtes manuelles seulement.", null, null, null, null, null, null],
  ["Sources", "BrandSearch API, SEMrush connecté, Google Trends, SERP publiques et rapport local du run 20260720-200609.", null, null, null, null, null, null]
];
method.getRange("A12:H12").format = { fill: blue, font: { bold: true, color: navy } };
method.getRange("A13:H18").format.wrapText = true;
method.getRange("A13:H18").format.rowHeight = 34;
method.getRange("A20:B26").values = [
  ["Source", "URL / chemin"],
  ["Rapport complet", reportPath],
  ["Entreprises BrandSearch brutes", rawCompaniesPath],
  ["SEMrush", "https://fr.semrush.com/analytics/keywordmagic/"],
  ["Google Trends", "https://trends.google.com/trends/explore"],
  ["BrandSearch", "https://app.brandsearch.co/brand-library"],
  ["AliExpress", "MANQUANT — blocage de navigation Chrome"]
];
method.getRange("A20:B20").format = { fill: blue, font: { bold: true, color: navy } };
method.getRange("A1:H26").format.verticalAlignment = "center";
method.getRange("A1:A26").format.columnWidth = 28;
method.getRange("B1:B26").format.columnWidth = 88;
method.freezePanes.freezeRows(4);

// Radar 30.
radar.getRange("A1:Z2").merge();
radar.getRange("A1").values = [["RADAR MULTI-MARCHÉS — 30 PRODUITS / NICHES"]];
radar.getRange("A1:Z2").format = { fill: navy, font: { bold: true, color: "#FFFFFF", size: 16 }, verticalAlignment: "center" };
radar.getRange("A3:Z3").merge();
radar.getRange("A3").values = [["Vert = marché retenu à sourcer · Orange = preuve réelle mais condition · Rouge = exclusion · Aucun lien fournisseur n'a été inventé"]];
radar.getRange("A3:Z3").format = { fill: light, font: { italic: true, color: gray }, verticalAlignment: "center" };
radar.getRange("A5:Z5").values = [radarHeaders];
radar.getRange("A5:Z5").format = { fill: navy, font: { bold: true, color: "#FFFFFF" }, wrapText: true, verticalAlignment: "center" };
radar.getRange("A6:Z35").values = radarRows;
for (let row = 6; row <= 35; row += 1) radar.getRange(`N${row}`).formulas = [[`=M${row}/'Méthode'!$B$5`]];
radar.getRange("F6:H35").format.numberFormat = "#,##0";
radar.getRange("J6:L35").format.numberFormat = "#,##0";
radar.getRange("M6:N35").format.numberFormat = "#,##0.00";
radar.getRange("O6:O35").format.numberFormat = "0.0%";
radar.getRange("A6:Z35").format = { verticalAlignment: "top", wrapText: true };
radar.getRange("A6:Z35").format.rowHeight = 54;
radar.getRange("B6:B35").dataValidation = { rule: { type: "list", values: ["VALIDÉ", "À CREUSER", "EXCLU"] } };
radar.getRange("A6:Z35").conditionalFormats.addCustom('=$B6="VALIDÉ"', { fill: green, font: { color: "#215E21" } });
radar.getRange("A6:Z35").conditionalFormats.addCustom('=$B6="À CREUSER"', { fill: orange, font: { color: "#9C5700" } });
radar.getRange("A6:Z35").conditionalFormats.addCustom('=$B6="EXCLU"', { fill: red, font: { color: "#9C0006" } });
const radarTable = radar.tables.add("A5:Z35", true, "Radar30Table");
radarTable.style = "TableStyleLight9";
radarTable.showFilterButton = true;
radar.freezePanes.freezeRows(5);
radar.freezePanes.freezeColumns(4);
const radarWidths = [6,14,8,30,12,15,13,15,24,14,12,12,14,14,12,28,26,30,42,24,34,34,34,30,30,38];
radarWidths.forEach((width, index) => radar.getRangeByIndexes(0,index,35,1).format.columnWidth = width);

// Raw companies.
const companyHeaders = ["Pays","Domaine","Niche","Visites mensuelles","Google Ads actives","Meta Ads actives","Prix moyen USD","Prix moyen EUR","Prix min USD","Prix max USD","Nombre produits","Produits génériques","Description","URL BrandSearch"];
companies.getRange("A1:N1").values = [companyHeaders];
companies.getRange("A1:N1").format = { fill: navy, font: { bold: true, color: "#FFFFFF" }, wrapText: true };
const companyRows = rawCompanies.map((c) => [
  c.country_code || "", c.name || "", c.niche || "", c.monthly_visits ?? null,
  c.google_ads_active ?? null, c.last_meta_active_count ?? null, c.avg_price_usd ?? null,
  null, c.min_price_usd ?? null, c.max_price_usd ?? null, c.product_count ?? null,
  (c.generic_products || []).join(" ; "), c.description || "", c.dashboard_url || ""
]);
companies.getRange(`A2:N${companyRows.length + 1}`).values = companyRows;
for (let row = 2; row <= companyRows.length + 1; row += 1) companies.getRange(`H${row}`).formulas = [[`=G${row}/'Méthode'!$B$5`]];
companies.getRange(`D2:F${companyRows.length + 1}`).format.numberFormat = "#,##0";
companies.getRange(`G2:J${companyRows.length + 1}`).format.numberFormat = "#,##0.00";
companies.getRange(`K2:K${companyRows.length + 1}`).format.numberFormat = "#,##0";
companies.getRange(`A2:N${companyRows.length + 1}`).format.verticalAlignment = "top";
companies.getRange(`A2:N${companyRows.length + 1}`).format.rowHeight = 21;
const companiesTable = companies.tables.add(`A1:N${companyRows.length + 1}`, true, "BrandSearch216Table");
companiesTable.style = "TableStyleLight9";
companiesTable.showFilterButton = true;
companies.freezePanes.freezeRows(1);
companies.freezePanes.freezeColumns(2);
const companyWidths = [8,28,20,14,12,12,13,13,12,12,12,42,70,42];
companyWidths.forEach((width, index) => companies.getRangeByIndexes(0,index,companyRows.length + 1,1).format.columnWidth = width);

// Measures: selected SEMrush and Trends facts behind the radar.
const measureHeaders = ["Produit / niche","Marché","Requête SEMrush","Mode","Volume mensuel","Google Trends 52/52","Lecture","Source"];
const measureRows = radarRows.flatMap((r) => {
  const queries = semrushQueries[r[0]] || [r[3], r[3]];
  const out = [[r[3], r[4], queries[0], "Expression / cluster local", r[5], r[14], r[16], "SEMrush connecté"]];
  if (r[6] && r[7]) out.push([r[3], r[6], queries[1], "Expression / cluster local", r[7], null, "Marché secondaire", "SEMrush connecté"]);
  return out;
});
measures.getRange("A1:H2").merge();
measures.getRange("A1").values = [["MESURES DE DEMANDE — RADAR 30"]];
measures.getRange("A1:H2").format = { fill: navy, font: { bold: true, color: "#FFFFFF", size: 15 } };
measures.getRange("A4:H4").values = [measureHeaders];
measures.getRange("A4:H4").format = { fill: blue, font: { bold: true, color: navy }, wrapText: true };
measures.getRange(`A5:H${measureRows.length + 4}`).values = measureRows;
measures.getRange(`E5:E${measureRows.length + 4}`).format.numberFormat = "#,##0";
measures.getRange(`F5:F${measureRows.length + 4}`).format.numberFormat = "0.0%";
measures.getRange(`A5:H${measureRows.length + 4}`).format.rowHeight = 30;
measures.getRange(`A5:H${measureRows.length + 4}`).format.wrapText = true;
const measuresTable = measures.tables.add(`A4:H${measureRows.length + 4}`, true, "MeasuresTable");
measuresTable.style = "TableStyleLight9";
measuresTable.showFilterButton = true;
measures.freezePanes.freezeRows(4);
[30,12,34,22,16,18,34,22].forEach((width,index)=>measures.getRangeByIndexes(0,index,measureRows.length + 4,1).format.columnWidth=width);

// Summary.
summary.getRange("A1:H2").merge();
summary.getRange("A1").values = [["SYNTHÈSE — CHASSE PRODUITS MULTI-MARCHÉS"]];
summary.getRange("A1:H2").format = { fill: navy, font: { bold: true, color: "#FFFFFF", size: 17 }, verticalAlignment: "center" };
summary.getRange("A3:H3").merge();
summary.getRange("A3").values = [["Run 20260720-200609 · BrandSearch + SEMrush + Trends + SERP · Sourcing AliExpress bloqué et documenté"]];
summary.getRange("A3:H3").format = { fill: light, font: { italic: true, color: gray } };
summary.getRange("A5:B5").merge(); summary.getRange("C5:D5").merge(); summary.getRange("E5:F5").merge(); summary.getRange("G5:H5").merge();
summary.getRange("A5").values = [["VALIDÉS"]]; summary.getRange("C5").values = [["À CREUSER"]]; summary.getRange("E5").values = [["EXCLUS"]]; summary.getRange("G5").values = [["ENTREPRISES FILTRÉES"]];
summary.getRange("A6:B7").merge(); summary.getRange("C6:D7").merge(); summary.getRange("E6:F7").merge(); summary.getRange("G6:H7").merge();
summary.getRange("A6").formulas = [["=COUNTIF('Radar 30'!$B$6:$B$35,\"VALIDÉ\")"]];
summary.getRange("C6").formulas = [["=COUNTIF('Radar 30'!$B$6:$B$35,\"À CREUSER\")"]];
summary.getRange("E6").formulas = [["=COUNTIF('Radar 30'!$B$6:$B$35,\"EXCLU\")"]];
summary.getRange("G6").formulas = [["=COUNTA('Entreprises 216'!$B$2:$B$217)"]];
summary.getRange("A5:B7").format = { fill: green, font: { bold: true, color: "#215E21", size: 15 }, horizontalAlignment: "center", verticalAlignment: "center", borders: { preset: "outside", style: "medium", color: "#A9D08E" } };
summary.getRange("C5:D7").format = { fill: orange, font: { bold: true, color: "#9C5700", size: 15 }, horizontalAlignment: "center", verticalAlignment: "center", borders: { preset: "outside", style: "medium", color: "#F4B183" } };
summary.getRange("E5:F7").format = { fill: red, font: { bold: true, color: "#9C0006", size: 15 }, horizontalAlignment: "center", verticalAlignment: "center", borders: { preset: "outside", style: "medium", color: "#E6B8B7" } };
summary.getRange("G5:H7").format = { fill: blue, font: { bold: true, color: navy, size: 15 }, horizontalAlignment: "center", verticalAlignment: "center", borders: { preset: "outside", style: "medium", color: "#9EADBA" } };
summary.getRange("A6:H7").format.numberFormat = "#,##0";

summary.getRange("A10:F10").values = [["Priorité","Produit / niche","Marché pilote","Volume / mois","Tendance","Action suivante"]];
summary.getRange("A10:F10").format = { fill: navy, font: { bold: true, color: "#FFFFFF" }, wrapText: true };
for (let i = 0; i < 8; i += 1) {
  const srcRow = i + 6;
  const destRow = i + 11;
  summary.getRange(`A${destRow}:F${destRow}`).formulas = [[
    `='Radar 30'!C${srcRow}`, `='Radar 30'!D${srcRow}`, `='Radar 30'!E${srcRow}`,
    `='Radar 30'!F${srcRow}`, `=IF('Radar 30'!O${srcRow}=\"\",\"\",'Radar 30'!O${srcRow})`, `='Radar 30'!Q${srcRow}`
  ]];
}
summary.getRange("D11:D18").format.numberFormat = "#,##0";
summary.getRange("E11:E18").format.numberFormat = "0.0%";
summary.getRange("A11:F18").format = { fill: green, wrapText: true, verticalAlignment: "top", borders: { preset: "inside", style: "thin", color: "#D9EAD3" } };
summary.getRange("A11:F18").format.rowHeight = 34;

summary.getRange("A21:C21").values = [["Marché","Entreprises filtrées","Règle"]];
summary.getRange("A21:C21").format = { fill: blue, font: { bold: true, color: navy } };
const markets = [["FR","France"],["DE","Allemagne"],["GB","Royaume-Uni"],["ES","Espagne"],["IT","Italie"],["NL","Pays-Bas"],["BE","Belgique"]];
markets.forEach(([code,label], index) => {
  const row = index + 22;
  summary.getRange(`A${row}`).values = [[label]];
  summary.getRange(`B${row}`).formulas = [[`=COUNTIF('Entreprises 216'!$A$2:$A$217,\"${code}\")`]];
  summary.getRange(`C${row}`).values = [["Google ≥1 · Meta =0 · prix moyen 85–400 EUR"]];
});
summary.getRange("B22:B28").format.numberFormat = "#,##0";
summary.getRange("A30:H32").merge();
summary.getRange("A30").values = [["Important : vert signifie « marché retenu pour sourcing manuel ». Aucun fournisseur AliExpress, prix livré, délai, stock, certificat ou lancement n'est validé à ce stade."]];
summary.getRange("A30:H32").format = { fill: "#FFF2CC", font: { bold: true, color: "#7F6000" }, wrapText: true, verticalAlignment: "center", borders: { preset: "outside", style: "medium", color: "#D6B656" } };
summary.getRange("A1:H32").format.verticalAlignment = "center";
[10,34,16,16,14,34,18,18].forEach((width,index)=>summary.getRangeByIndexes(0,index,32,1).format.columnWidth=width);
summary.freezePanes.freezeRows(3);

// Compact structural borders and alignment.
for (const sheet of [radar, companies, measures]) {
  const used = sheet.getUsedRange();
  used.format.font = { size: 10 };
}

await fs.mkdir(outputDir, { recursive: true });

const summaryPreview = await workbook.render({ sheetName: "Synthèse", range: "A1:H32", scale: 1.4, format: "png" });
await fs.writeFile(`${outputDir}/preview-synthese.png`, new Uint8Array(await summaryPreview.arrayBuffer()));
const radarPreview = await workbook.render({ sheetName: "Radar 30", range: "A1:J14", scale: 1.2, format: "png" });
await fs.writeFile(`${outputDir}/preview-radar.png`, new Uint8Array(await radarPreview.arrayBuffer()));
const companiesPreview = await workbook.render({ sheetName: "Entreprises 216", range: "A1:N12", scale: 1.0, format: "png" });
await fs.writeFile(`${outputDir}/preview-entreprises.png`, new Uint8Array(await companiesPreview.arrayBuffer()));
const measuresPreview = await workbook.render({ sheetName: "Mesures", range: "A1:H16", scale: 1.1, format: "png" });
await fs.writeFile(`${outputDir}/preview-mesures.png`, new Uint8Array(await measuresPreview.arrayBuffer()));
const methodPreview = await workbook.render({ sheetName: "Méthode", range: "A1:H26", scale: 1.1, format: "png" });
await fs.writeFile(`${outputDir}/preview-methode.png`, new Uint8Array(await methodPreview.arrayBuffer()));

const tableCheck = await workbook.inspect({ kind: "table", range: "Radar 30!A1:Z35", include: "values,formulas", tableMaxRows: 12, tableMaxCols: 26, maxChars: 12000 });
const errorCheck = await workbook.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 300 }, summary: "final formula error scan", maxChars: 5000 });
await fs.writeFile(`${outputDir}/tableau-produits-multimarches-20260720-200609.inspect.ndjson`, `${tableCheck.ndjson}\n${errorCheck.ndjson}\n`, "utf8");

const xlsx = await SpreadsheetFile.exportXlsx(workbook);
await xlsx.save(`${outputDir}/tableau-produits-multimarches-20260720-200609.xlsx`);

console.log(JSON.stringify({
  output: `${outputDir}/tableau-produits-multimarches-20260720-200609.xlsx`,
  companies: rawCompanies.length,
  radar: radarRows.length,
  validated: radarRows.filter((r) => r[1] === "VALIDÉ").length,
  explore: radarRows.filter((r) => r[1] === "À CREUSER").length,
  excluded: radarRows.filter((r) => r[1] === "EXCLU").length,
  errorScan: errorCheck.ndjson
}, null, 2));

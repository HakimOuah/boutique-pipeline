#!/usr/bin/env python3
"""Build two evidence-backed catalogues of 220 distinct product concepts.

The script only reads public competitor sitemaps/product feeds.  It does not
query SEMrush, Chrome, AliExpress, the project workbook, or Git.
"""

from __future__ import annotations

import html
import hashlib
import json
import re
import time
import unicodedata
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET


OBSERVED_AT = "2026-08-08"
ROOT = Path(__file__).resolve().parents[1]
RAW_ROOT = ROOT / "raw" / "catalogue-expansion"
OUTPUT_JSON = ROOT / "workstreams" / "catalogue-expansion-mercerie-scrap.json"
OUTPUT_MD = ROOT / "workstreams" / "catalogue-expansion-mercerie-scrap.md"
USER_AGENT = "Mozilla/5.0 (compatible; CatalogueResearch/1.0; evidence snapshot)"
CACHE_ROOT = Path("/tmp/codex-catalogue-expansion-cache-20260808")


@dataclass(frozen=True)
class Source:
    slug: str
    competitor: str
    domain: str
    niche: str
    url: str
    kind: str = "sitemap"


@dataclass
class Candidate:
    niche: str
    competitor: str
    domain: str
    collection: str
    title: str
    url: str
    source_url: str
    bucket: str
    concept: str
    signature: str
    evidence_status: str = "OBSERVE_CONCURRENT"
    derived_note: str = ""
    english_query_override: str = ""


SOURCES = [
    Source(
        "rascol",
        "Rascol",
        "rascol.com",
        "mercerie",
        "https://www.rascol.com/1_fr_0_sitemap.xml",
        "rascol-sitemap",
    ),
    *[
        Source(
            "craftine",
            "Craftine",
            "craftine.com",
            "mercerie",
            f"https://www.craftine.com/sitemap-1-{page}.xml",
        )
        for page in range(1, 7)
    ],
    Source(
        "atelier-de-la-creation",
        "Atelier de la Création",
        "atelierdelacreation.com",
        "mercerie",
        "https://www.atelierdelacreation.com/1_fr_0_sitemap.xml",
    ),
    Source(
        "chouette-kit",
        "Chouette Kit",
        "chouettekit.fr",
        "mercerie",
        "https://www.chouettekit.fr/wp-json/wc/store/v1/products?per_page=100&page=1",
        "woocommerce",
    ),
    Source(
        "la-fourmi-creative",
        "La Fourmi Créative",
        "lafourmicreative.fr",
        "scrapbooking",
        "https://www.lafourmicreative.fr/1_fr_0_sitemap.xml",
    ),
    Source(
        "fee-du-scrap",
        "Fée du Scrap",
        "feeduscrap.fr",
        "scrapbooking",
        "https://www.feeduscrap.fr/siteMapsFRImage1.xml",
    ),
    Source(
        "fee-du-scrap",
        "Fée du Scrap",
        "feeduscrap.fr",
        "scrapbooking",
        "https://www.feeduscrap.fr/siteMapsFRImage2.xml",
    ),
    Source(
        "florileges-design",
        "Florilèges Design / Variations Créatives",
        "variationscreatives.fr",
        "scrapbooking",
        "https://www.variationscreatives.fr/1_fr_0_sitemap.xml",
    ),
    Source(
        "scrapmalin",
        "Scrapmalin",
        "scrapmalin.com",
        "scrapbooking",
        "https://www.scrapmalin.com/sitemap.xml",
        "url-sitemap",
    ),
]


MERCERIE_TARGETS = {
    "Outils de coupe": 12,
    "Mesure": 10,
    "Traçage et marquage": 10,
    "Aiguilles et épingles main": 12,
    "Machine à coudre": 14,
    "Fils à coudre": 12,
    "Fermetures et attaches": 14,
    "Boutons, pressions et œillets": 12,
    "Rubans, biais, élastiques et cordons": 14,
    "Entoilage, stabilisation et rembourrage": 12,
    "Tissus fonctionnels": 22,
    "Outils tricot et crochet": 14,
    "Laines et fils créatifs": 16,
    "Broderie, punch needle et macramé": 14,
    "Kits et projets": 14,
    "Rangement, réparation et repassage": 12,
    "Accessoires de sacs": 6,
}

SCRAP_TARGETS = {
    "Albums et reliure": 12,
    "Papiers et supports": 18,
    "Tampons et estampage": 16,
    "Matrices et découpe": 14,
    "Embossage et gaufrage": 10,
    "Perforation et massicots": 10,
    "Encres et applicateurs": 16,
    "Feutres, peinture et aquarelle": 12,
    "Colles et adhésifs": 12,
    "Pochoirs et textures": 12,
    "Stickers, transferts et masking tape": 10,
    "Embellissements": 16,
    "Journaling et planners": 12,
    "Cachets de cire": 8,
    "Rangement et petit outillage": 10,
    "Kits et assortiments": 12,
    "Photo et montage": 10,
    "Lettres et étiquettes": 10,
}


COLORS = {
    "argent",
    "argenté",
    "beige",
    "blanc",
    "bleu",
    "bordeaux",
    "bronze",
    "brun",
    "chair",
    "chocolat",
    "corail",
    "cuivre",
    "cyan",
    "doré",
    "écru",
    "fuchsia",
    "fuschia",
    "gris",
    "ivoire",
    "jaune",
    "kaki",
    "marine",
    "marron",
    "menthe",
    "multicolore",
    "noir",
    "orange",
    "or",
    "parme",
    "pétrole",
    "rose",
    "rouge",
    "saumon",
    "taupe",
    "turquoise",
    "vert",
    "violet",
    "anthracite",
    "abricot",
    "amande",
    "aqua",
    "aubergine",
    "camel",
    "caramel",
    "ciel",
    "crème",
    "creme",
    "dust",
    "framboise",
    "greige",
    "lavande",
    "lilas",
    "mint",
    "moutarde",
    "naturel",
    "nude",
    "olive",
    "pêche",
    "peche",
    "pistache",
    "sable",
    "terracotta",
}

BRANDS = [
    "aall and create",
    "aall & create",
    "aladine",
    "artemio",
    "bohin",
    "burda",
    "carabelle studio",
    "chouette kit",
    "clover",
    "comptoir du scrap",
    "craftine",
    "dmc",
    "dress your doll",
    "echo park",
    "florilèges design",
    "gutermann",
    "gütermann",
    "hero arts",
    "kai",
    "katana",
    "fiskars",
    "knitpro",
    "lawn fawn",
    "marianne design",
    "memory box",
    "memento",
    "olfa",
    "poppy stamps",
    "prym",
    "rascol",
    "ranger",
    "rico design",
    "schmetz",
    "sizzix",
    "stampin up",
    "sew easy",
    "tim holtz",
    "toga",
    "vaessen creative",
    "we r memory keepers",
    "zibuline",
    "cricut",
    "ephéméria",
    "ephemeria",
    "pioneer",
    "plottermarie",
]

GENERIC_DROP = {
    "nouveau",
    "nouveauté",
    "collection",
    "assorti",
    "assortie",
    "assortiment",
    "coloris",
    "couleur",
    "modèle",
    "référence",
    "ref",
    "vendu",
    "pièce",
    "pièces",
    "classic",
    "duo",
    "ergonomique",
    "grand",
    "grande",
    "love",
    "mat",
    "mate",
    "maxi",
    "mini",
    "pale",
    "pastel",
    "petit",
    "petite",
    "professionnel",
    "professionnelle",
    "royal",
    "super",
}


MERCERIE_RULES = [
    ("Kits et projets", r"\b(kit|coffret|starter|tutoriel|tuto|patron et tutoriel|amigurumi)\b"),
    ("Outils de coupe", r"\b(ciseaux?|cutter|couteau rotatif|roulette de coupe|découd-vite|découd vite|lame de coupe|coupe-fil|coupe fil|ouvre-boutonnière)\b"),
    ("Mesure", r"\b(mètre ruban|metre ruban|règle|regle|équerre|equerre|jauge|mesure couture|gabarit de mesure|curvimètre)\b"),
    ("Traçage et marquage", r"\b(craie|crayon craie|marqueur textile|stylo textile|feutre textile|roulette à patron|papier carbone|papier transfert|calque couture|traceur|pistolet de couture)\b"),
    ("Machine à coudre", r"\b(machine à coudre|machine a coudre|canette|pied presseur|pied de biche|aiguille machine|aiguilles machine|boîtier canette|boitier canette|plaque aiguille|courroie machine|huile machine|enfile-aiguille machine|guide couture magnétique|guide couture magnetique)\b"),
    ("Aiguilles et épingles main", r"\b(aiguille à coudre|aiguille a coudre|aiguilles à coudre|aiguilles a coudre|aiguille main|aiguilles main|épingle|epingle|pique-épingles|pique epingles|dé à coudre|de a coudre|enfile-aiguille|enfile aiguille|épingle de sûreté|epingle de surete)\b"),
    ("Fils à coudre", r"\b(fil à coudre|fil a coudre|fil couture|fil surjeteuse|fil élastique|fil elastique|fil invisible|fil métallique|fil metallique|fil nylon|fil polyester|fil coton|fil pour tout coudre)\b"),
    ("Fermetures et attaches", r"\b(fermeture à glissière|fermeture a glissiere|fermeture éclair|fermeture eclair|zip|agrafe|fermoir|attache|mousqueton|crochet pantalon|boucle coulissante|boucle clip|tourniquet|aimant à coudre|aimant a coudre)\b"),
    ("Boutons, pressions et œillets", r"\b(bouton|pression|oeillet|œillet|rivets?|snap|boutonnière)\b"),
    ("Rubans, biais, élastiques et cordons", r"\b(ruban|biais|passepoil|galon|dentelle|élastique|elastique|sangle|cordon|cordelière|cordeliere|sergé|serge|velcro|scratch|croquet)\b"),
    ("Entoilage, stabilisation et rembourrage", r"\b(entoilage|thermocollant|vlieseline|stabilisateur|ouatine|molleton|rembourrage|kapok|mousse résille|mousse resille|renfort|solufix|film hydrosoluble|support broderie)\b"),
    ("Outils tricot et crochet", r"\b(aiguille circulaire|aiguilles circulaires|aiguille à tricoter|aiguilles à tricoter|aiguille a tricoter|aiguilles a tricoter|crochet tunisien|crochet ergonomique|crochet aluminium|compte-rangs|compte rangs|marqueur de maille|arrête-mailles|arrete-mailles|bobinoir|dévidoir à laine|devidoir a laine|blocage tricot|fourche à tricoter|tricotin)\b"),
    ("Laines et fils créatifs", r"\b(pelote|laine|fil à tricoter|fil a tricoter|fil crochet|coton à crocheter|coton a crocheter|mohair|mérinos|merinos|alpaga|chenille yarn|raphia à crocheter|raphia a crocheter|fil macramé|fil macrame)\b"),
    ("Broderie, punch needle et macramé", r"\b(broder|broderie|tambour|cercle à broder|cercle a broder|punch needle|aiguille punch|macramé|macrame|canevas|toile aïda|toile aida|mouliné|mouline|fil perlé|fil perle|aiguille tapisserie)\b"),
    ("Rangement, réparation et repassage", r"\b(boîte à couture|boite a couture|rangement couture|organiseur couture|trousse à aiguilles|trousse a aiguilles|raccommoder|réparation textile|reparation textile|patch thermocollant|pièce thermocollante|piece thermocollante|repassage|jeannette|pattemouille|défroisseur|defroisseur|planche à repasser|planche a repasser|filet lavage)\b"),
    ("Accessoires de sacs", r"\b(anse de sac|poignée de sac|poignee de sac|fond de sac|pied de sac|fermoir de sac|chaîne de sac|chaine de sac|attache cartable|boucle de sac|mousqueton de sac)\b"),
    ("Tissus fonctionnels", r"\b(tissu|popeline|double gaze|viscose|lin |jute|matelassé|matelasse|doudoune|velours|bachette|canvas|sweat|molleton|bord-côte|bord cote|jersey|fourrure|liberty|éponge|eponge|jacquard|denim|jean |doublure|enduit|déperlant|deperlant|mesh|tulle|flanelle|cretonne|seersucker|voile de coton|minky|simili cuir|lycra|gabardine|soie|sergé|serge|satin|baptiste|batiste|organdi|organza|néoprène|neoprene|polaire)\b"),
]

SCRAP_RULES = [
    ("Cachets de cire", r"\b(cachet de cire|cachets de cire|sceau|cire à cacheter|cire a cacheter|wax seal)\b"),
    ("Journaling et planners", r"\b(bullet journal|journal|journaling|carnet|planner|agenda|notebook|planificateur|bloc-notes|bloc notes|travelers notebook)\b"),
    ("Albums et reliure", r"\b(album|classeur|reliure|anneau de reliure|anneaux de reliure|recharge album|pochette album|couverture album|vis album|charnière album|charniere album|bind-it|reliure spirale)\b"),
    ("Tampons et estampage", r"\b(tampon|stamp|bloc acrylique|presse à tampon|presse a tampon|plateforme de tamponnage|positionneur de tampon|ez mount)\b"),
    ("Embossage et gaufrage", r"\b(emboss|gaufrage|embosser|plaque de gaufrage|classeur de gaufrage|poudre à embosser|poudre a embosser|pistolet chauffant|heat gun)\b"),
    ("Matrices et découpe", r"\b(matrice|dies?\b|die-cut|die cut|outil de découpe|outil de decoupe|machine de découpe|machine de decoupe|forme de découpe|forme de decoupe|lame silhouette|lame cricut)\b"),
    ("Perforation et massicots", r"\b(perforatrice|massicot|rogneuse|cutter|ciseaux|tapis de coupe|crop-a-dile|crop a dile|pince à oeillets|pince a oeillets|poinçon|poincon)\b"),
    ("Encres et applicateurs", r"\b(encre|ink pad|tampon encreur|recharge distress|applicateur d'encre|applicateur d encre|blender|doigt mousse|rouleau encreur)\b"),
    ("Feutres, peinture et aquarelle", r"\b(feutre|marqueur|crayon|pastel|aquarelle|peinture|pinceau|gouache|pigment|magical shaker|brush pen)\b"),
    ("Colles et adhésifs", r"\b(colle|adhésif|adhesif|double face|mousse 3d|ruban mousse|dévidoir|devidoir|glue dots|roller glue|spray adhésif|spray adhesif)\b"),
    ("Pochoirs et textures", r"\b(pochoir|mask|gesso|pâte de texture|pate de texture|texture paste|medium|gel texture|mousse créative|mousse creative)\b"),
    ("Stickers, transferts et masking tape", r"\b(autocollant|sticker|décalcomanie|decalcomanie|rub-on|rub on|masking tape|washi|transfert)\b"),
    ("Lettres et étiquettes", r"\b(alphabet|lettre|chiffre|étiquette|etiquette|label|mot autocollant|porte-étiquette|porte etiquette)\b"),
    ("Photo et montage", r"\b(photo|coin photo|porte-photo|porte photo|cadre|flipettes?|photo flip|mounting square|attache photo)\b"),
    ("Rangement et petit outillage", r"\b(rangement|boîte|boite|organiseur|trousse|pochette de rangement|outil de précision|outil de precision|plioir|spatule|règle|regle|palette|tapis silicone)\b"),
    ("Kits et assortiments", r"\b(kit|coffret|assortiment|bundle|set complet|pack créatif|pack creatif|collection complète|collection complete)\b"),
    ("Papiers et supports", r"\b(papier|cardstock|carton|calque|acétate|acetate|vellum|feuille|chipboard|mousse eva|toile canvas|carte vierge|enveloppe|support bois|support carton)\b"),
    ("Embellissements", r"\b(embellissement|fleur|ruban|ficelle|twine|bouton|attache parisienne|brad|oeillet|œillet|perle|strass|sequins|pompon|charms?|breloque|cabochon|forme en bois|découpe bois|decoupe bois|résine|resine|déco métal|deco metal)\b"),
]


EXCLUDED_PATH_PARTS = {
    "archives",
    "zzz-archives",
    "bonnes-affaires",
    "bonnes-affaires-70",
    "promotions",
    "fabricants",
    "fournisseurs",
    "a-supprimer-definitivement",
    "fiches-en-cours",
    "produits-a-0-a-controler",
}


def fetch_bytes(url: str, attempts: int = 3) -> bytes:
    CACHE_ROOT.mkdir(parents=True, exist_ok=True)
    cache_path = CACHE_ROOT / hashlib.sha256(url.encode("utf-8")).hexdigest()
    if cache_path.exists():
        return cache_path.read_bytes()
    last_error: Exception | None = None
    for attempt in range(attempts):
        try:
            request = Request(url, headers={"User-Agent": USER_AGENT})
            with urlopen(request, timeout=90) as response:
                body = response.read()
                cache_path.write_bytes(body)
                return body
        except (HTTPError, URLError, TimeoutError) as exc:
            last_error = exc
            if attempt + 1 < attempts:
                time.sleep(1.2 * (attempt + 1))
    raise RuntimeError(f"Unable to fetch {url}: {last_error}")


def strip_tags(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", value))).strip()


def ascii_fold(value: str) -> str:
    value = value.replace("œ", "oe").replace("Œ", "OE").replace("æ", "ae").replace("Æ", "AE")
    return "".join(
        char
        for char in unicodedata.normalize("NFKD", value)
        if not unicodedata.combining(char)
    )


def slug_to_title(url: str) -> str:
    slug = urlparse(url).path.rstrip("/").split("/")[-1]
    slug = re.sub(r"(?:-a\d+|-p-\d+|\.html)$", "", slug)
    slug = re.sub(r"-\d{8,}$", "", slug)
    return re.sub(r"[-_]+", " ", slug).strip()


def path_collection(url: str) -> str:
    parts = [part for part in urlparse(url).path.split("/") if part]
    if not parts:
        return "Catalogue"
    if parts[0] == "product":
        return "Catalogue produits"
    first = re.sub(r"^\d+-", "", parts[0])
    return first.replace("-", " ").strip().capitalize()


def parse_sitemap(source: Source, body: bytes) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    root = ET.fromstring(body)
    for url_node in root.iter():
        if not url_node.tag.endswith("url"):
            continue
        loc = ""
        title = ""
        for child in list(url_node):
            if child.tag.endswith("loc") and child.text:
                loc = child.text.strip()
                break
        for descendant in url_node.iter():
            if descendant.tag.endswith("title") and (descendant.text or "").strip():
                title = strip_tags(descendant.text or "")
                break
        if not loc:
            continue
        path_parts = set(urlparse(loc).path.lower().split("/"))
        if path_parts & EXCLUDED_PATH_PARTS:
            continue
        if source.kind == "url-sitemap":
            if not urlparse(loc).path.startswith("/product/"):
                continue
            title = slug_to_title(loc)
        elif source.kind == "rascol-sitemap":
            if not re.search(r"-p-\d+/?$", urlparse(loc).path):
                continue
            title = slug_to_title(loc)
        elif not title:
            continue
        rows.append(
            {
                "title": title,
                "url": loc,
                "collection": path_collection(loc),
                "source_url": source.url,
            }
        )
    return rows


def parse_woocommerce(source: Source, body: bytes) -> list[dict[str, str]]:
    products = json.loads(body.decode("utf-8"))
    rows = []
    for product in products:
        title = strip_tags(product.get("name", ""))
        url = product.get("permalink", "")
        categories = [
            strip_tags(category.get("name", ""))
            for category in product.get("categories", [])
            if category.get("name")
        ]
        if not title or not url or not categories:
            continue
        rows.append(
            {
                "title": title,
                "url": url,
                "collection": " > ".join(categories),
                "source_url": source.url,
            }
        )
    return rows


def clean_concept(title: str) -> str:
    value = strip_tags(title).replace("’", "'")
    # Product titles often end with " - Brand / model".  Drop the whole suffix
    # when it explicitly contains a known brand, so models do not masquerade as
    # distinct product concepts.
    for segment in re.split(r"\s+-\s+", value)[1:]:
        segment_folded = ascii_fold(segment).lower()
        if any(ascii_fold(brand).lower() in segment_folded for brand in BRANDS):
            value = value[: value.find(" - ")]
            break
    value = re.sub(r"(?i)pdf à télécharger|a télécharger|à télécharger|téléchargement", " ", value)
    value = re.sub(r"(?i)patron et tutoriel|tutoriel|tuto", " ", value)
    for brand in sorted(BRANDS, key=len, reverse=True):
        value = re.sub(rf"(?i)(?<!\w){re.escape(brand)}(?!\w)", " ", value)
    value = re.sub(r"(?i)\b(?:lot|bo[iî]te|sachet|pack|set|bobine|coupon)\s+de\s+\d+\b", " ", value)
    value = re.sub(r"(?i)\bx\s*\d+\b|\bpar\s+\d+\b", " ", value)
    value = re.sub(
        r"(?i)\b\d+(?:[.,]\d+)?\s*(?:mm|cm|m|g|kg|ml|l|oz|yd|yards?|mètres?|metres?|grammes?|pi[eè]ces?|pcs?)\b",
        " ",
        value,
    )
    value = re.sub(r"(?i)\b\d+\s*[x×]\s*\d+(?:\s*[x×]\s*\d+)?\b", " ", value)
    value = re.sub(r"(?i)\b(?:n[°o]\s*)?\d{2,}\b", " ", value)
    value = re.sub(r"(?i)\b[a-z]{1,5}\d{3,}[a-z0-9-]*\b", " ", value)
    value = re.sub(r"(?i)\b(?:mm|cm|ml|kg|gr|g|m|a[3-6])\b", " ", value)
    tokens = []
    for token in re.findall(r"[A-Za-zÀ-ÿ0-9'+-]+", value):
        folded = ascii_fold(token).lower()
        if folded in {ascii_fold(color).lower() for color in COLORS}:
            continue
        if folded in {ascii_fold(word).lower() for word in GENERIC_DROP}:
            continue
        if re.fullmatch(r"\d+(?:[.,]\d+)?", token):
            continue
        tokens.append(token.lower())
    value = " ".join(tokens)
    value = re.sub(r"\b(?:de|du|des|la|le|les|pour|avec|et|en|à|a)\s*$", "", value).strip(" -'")
    value = re.sub(r"\s+", " ", value)
    return value


def signature_for(concept: str) -> str:
    folded = ascii_fold(concept).lower().replace("œ", "oe")
    synonyms = {
        "aiguilles": "aiguille",
        "epingles": "epingle",
        "ciseaux": "ciseau",
        "boutons": "bouton",
        "rubans": "ruban",
        "fermetures": "fermeture",
        "papiers": "papier",
        "feuilles": "feuille",
        "tampons": "tampon",
        "matrices": "matrice",
        "encres": "encre",
        "autocollants": "autocollant",
        "stickers": "autocollant",
        "etiquettes": "etiquette",
        "albums": "album",
        "pochoirs": "pochoir",
        "perforatrices": "perforatrice",
        "marqueurs": "marqueur",
        "feutres": "feutre",
    }
    stop = {
        "de",
        "du",
        "des",
        "la",
        "le",
        "les",
        "un",
        "une",
        "pour",
        "avec",
        "et",
        "en",
        "a",
        "sur",
        "par",
    }
    tokens = []
    for token in re.findall(r"[a-z0-9]+", folded):
        if token in stop or token.isdigit():
            continue
        token = synonyms.get(token, token)
        tokens.append(token)
    return " ".join(sorted(dict.fromkeys(tokens)))


def classify(niche: str, title: str, collection: str) -> str | None:
    haystack = ascii_fold(f"{title} {collection}").lower()
    title_folded = ascii_fold(title).lower()
    if niche == "mercerie":
        if re.search(r"\b(coudiere|genouillere|patch.*thermocoll|ecusson thermocoll)", title_folded):
            return "Rangement, réparation et repassage"
        if re.search(r"\b(anses?|poignees?).*sac", title_folded):
            return "Accessoires de sacs"
        if re.search(r"\b(elastique|biais|ruban|galon|sangle|cordon)\b", title_folded) and not re.search(
            r"\bfil.*elastique\b", title_folded
        ):
            return "Rubans, biais, élastiques et cordons"
        if re.search(
            r"\b(bobinoir|devidoir.*laine|devidoir pour laine|marqueurs?.*maille|peignes?.*blocage|bracelet porte pelote|brosse pour mohair|crochet pour)\b",
            title_folded,
        ):
            return "Outils tricot et crochet"
        if re.search(r"\b(tissu|toile|coupon)\b", title_folded) and not re.search(
            r"\b(entoilage|stabilisateur|toile aida|toile.*broder|toile.*soluble)\b",
            title_folded,
        ):
            return "Tissus fonctionnels"
    else:
        if re.search(r"\b(organisateur|rangement|boite de rangement|plaques de rangement|trousse roll)\b", title_folded):
            return "Rangement et petit outillage"
        if re.search(r"\bnotes? repositionnables?|sticky notes\b", title_folded):
            return "Journaling et planners"
        if re.search(r"\bmoules?.*cachets? de cire\b", title_folded):
            return "Cachets de cire"
    rules = MERCERIE_RULES if niche == "mercerie" else SCRAP_RULES
    for bucket, pattern in rules:
        if re.search(ascii_fold(pattern).lower(), haystack, flags=re.I):
            return bucket
    return None


def is_bad_candidate(niche: str, title: str, concept: str, url: str) -> bool:
    folded = ascii_fold(f"{title} {url}").lower()
    if len(concept.split()) < 2 or len(concept) < 8:
        return True
    blockers = [
        "frais de port",
        "paiement complementaire",
        "bon d'achat",
        "bon cadeau",
        "carte cadeau",
        "livre ",
        "livret",
        "magazine",
        "ebook",
        "abonnement",
        "atelier creatif",
        "cours ",
        "tuto",
        "tutoriel",
            "a telecharger",
            "pdf ",
            "realiser un",
            "video -",
            "vidéo -",
            "atelier privatise",
            "idee creative",
        "occasion",
        "seconde main",
    ]
    if any(blocker in folded for blocker in blockers):
        return True
    if niche == "mercerie" and any(
        word in folded
        for word in [
            "breloque",
            "pendentif",
            "boucles-d-oreilles",
            "perle-a-ecraser",
            "cabochon",
            "chaine-bijoux",
            "sequins",
            "epingle broche",
            "tige clous",
            "miyuki",
            "rideau ",
        ]
    ):
        return True
    if niche == "scrapbooking" and any(
        word in folded
        for word in [
            "flex thermocollant",
            "iron on",
            "plottermarie",
            "moule silicone",
            "moules silicone",
            "caissette",
            "cake pop",
            "sweet table",
            "bijoux",
            "chaine ovale",
            "perle a ecraser",
            "enveloppe de coussin",
            "photophore",
            "maquette 3d",
            "transfert a chaud imprimable pour tissus",
            "transfert textile",
            "pochoir broderie",
            "ecusson thermocollant",
            "tableau noir",
            "transfert a chaud",
            "diamond painting",
            "pendentif pop-up",
            "chipboard '",
            "cadre avec photo et empreinte",
        ]
    ):
        return True
    return False


THEME_RULES = [
    (r"\bau coeur des bois\b", "botanique", "botanical"),
    (r"\b(noel|sapin|flocon|houx|renne|pere noel)\b", "Noël", "Christmas"),
    (r"\b(anniversaire|birthday|bougie)\b", "anniversaire", "birthday"),
    (r"\b(amour|love|coeur|coeurs|saint valentin)\b", "amour et cœurs", "love hearts"),
    (r"\b(bebe|naissance|doudou|layette|tetine)\b", "naissance et bébé", "new baby"),
    (r"\b(mariage|maries|wedding)\b", "mariage", "wedding"),
    (r"\b(voyage|travel|aventure|road trip|vacances)\b", "voyage", "travel"),
    (r"\b(fleur|fleurs|floral|bouquet|pivoine|coquelicot)\b", "fleurs", "floral"),
    (r"\b(feuille|feuilles|arbre|foret|branche|botani|nature)\b", "botanique", "botanical"),
    (r"\b(mer|plage|coquillage|ocean|marin|cigale|sud)\b", "mer et été", "seaside summer"),
    (r"\b(tropical|jungle|palmier)\b", "jungle tropicale", "tropical jungle"),
    (r"\b(montagne|ski|sommet)\b", "montagne", "mountain"),
    (r"\b(jardin|potager|jardinage)\b", "jardin", "garden"),
    (r"\b(papillon|papillons)\b", "papillons", "butterflies"),
    (r"\b(abeille|abeilles|miel)\b", "abeilles", "bees"),
    (r"\b(champignon|champignons)\b", "champignons", "mushrooms"),
    (r"\b(oiseau|oiseaux|hirondelle)\b", "oiseaux", "birds"),
    (r"\b(chat|chats|chaton)\b", "chats", "cats"),
    (r"\b(chien|chiens|chiot)\b", "chiens", "dogs"),
    (r"\b(licorne|unicorn)\b", "licorne", "unicorn"),
    (r"\b(animaux|animal|zoo|safari)\b", "animaux", "animals"),
    (r"\b(halloween|sorciere|citrouille|fantome)\b", "Halloween", "Halloween"),
    (r"\b(paques|lapin|oeuf)\b", "Pâques", "Easter"),
    (r"\b(ecole|rentree|crayon)\b", "école", "school"),
    (r"\b(cuisine|recette|gourmand|gateau)\b", "cuisine", "cooking"),
    (r"\b(maison|home|interieur)\b", "maison", "home"),
    (r"\b(famille|family)\b", "famille", "family"),
    (r"\b(photo|souvenir|memory)\b", "souvenirs photo", "photo memories"),
    (r"\b(merci|gratitude|thank)\b", "remerciement", "thank you"),
    (r"\b(alphabet|lettres|letter)\b", "alphabet", "alphabet"),
    (r"\b(chiffre|date|calendrier|mois|semaine)\b", "dates et calendrier", "date calendar"),
    (r"\b(texte|mot|mots|citation|phrase|sentiment)\b", "mots et citations", "sentiment words"),
    (r"\b(geometri|cercle|triangle|hexagone)\b", "géométrique", "geometric"),
    (r"\b(vintage|retro|ancien)\b", "vintage", "vintage"),
    (r"\b(steampunk|alchemist)\b", "steampunk", "steampunk"),
    (r"\b(mail art|courrier|postal|timbre)\b", "courrier et mail art", "mail art postal"),
    (r"\b(couture|tricot|crochet|mercerie)\b", "couture et fil", "sewing knitting"),
    (r"\b(musique|note de musique)\b", "musique", "music"),
    (r"\b(sport|football|velo|danse)\b", "sport", "sports"),
    (r"\b(espace|etoile|lune|planete)\b", "ciel et espace", "celestial space"),
    (r"\b(arc en ciel|rainbow)\b", "arc-en-ciel", "rainbow"),
    (r"\b(mandala|zentangle)\b", "mandala", "mandala"),
]


def detect_theme(text: str) -> tuple[str, str] | None:
    folded = ascii_fold(text).lower()
    for pattern, french, english in THEME_RULES:
        if re.search(pattern, folded):
            return french, english
    return None


MERCERIE_CANONICAL: dict[str, list[tuple[str, str]]] = {
    "Outils de coupe": [
        (r"ciseaux?.*(?:crante|zig.?zag)", "ciseaux cranteurs pour tissu"),
        (r"ciseaux?.*(?:micro.?dente|dentele)", "ciseaux microdentés pour tissu"),
        (r"ciseaux?.*(?:gauchers?|gaucher)", "ciseaux de couture pour gaucher"),
        (r"ciseaux?.*(?:broder|cigogne)", "ciseaux de broderie"),
        (r"ciseaux?.*(?:applique|pelican)", "ciseaux pélican pour appliqué"),
        (r"ciseaux?.*(?:cuir|sellerie)", "ciseaux pour cuir et sellerie"),
        (r"ciseaux?.*(?:electrique|electric)", "ciseaux électriques pour tissu"),
        (r"ciseaux?.*(?:tailleur|couture|tissus?|universel)", "ciseaux de couture pour tissu"),
        (r"(?:cutter|couteau).*(?:rotatif|circulaire)", "cutter rotatif pour tissu"),
        (r"(?:cutter|couteau).*(?:precision|scalpel)", "cutter de précision pour patron"),
        (r"cutter.*boutonniere", "cutter pour boutonnière"),
        (r"(?:coupe.?fil|ciseaux? coupe.?fil)", "coupe-fil de couture"),
        (r"(?:decoud.?vite|decouseur|ouvre.?boutonniere)", "découd-vite"),
        (r"lame.*(?:cutter|couteau|rotatif)", "lame de rechange pour cutter rotatif"),
        (r"roulette.*coupe", "roulette de coupe pour patron"),
    ],
    "Mesure": [
        (r"metre ruban", "mètre ruban de couturière"),
        (r"regle.*patchwork", "règle acrylique de patchwork"),
        (r"regle.*(?:courbe|pistolet)", "règle courbe de modélisme"),
        (r"regle.*chaussette", "règle de mesure pour chaussettes tricot"),
        (r"regle.*(?:ourlet|repass)", "règle de mesure pour ourlets"),
        (r"regle.*(?:couturiere|couture)", "règle de couture graduée"),
        (r"jauge.*(?:aiguille|crochet)", "jauge pour aiguilles et crochets"),
        (r"jauge.*couture", "jauge de couture coulissante"),
        (r"reglet", "réglet métallique de couture"),
        (r"mesureur.*ourlet|jauge.*ourlet", "mesureur d'ourlet"),
        (r"gabarit.*bouton", "gabarit de mesure pour boutons"),
    ],
    "Traçage et marquage": [
        (r"roulette.*patron.*dente", "roulette à patron dentelée"),
        (r"roulette.*patron.*lisse", "roulette à patron lisse"),
        (r"roulette.*patron", "roulette à patron"),
        (r"roulette.*craie", "roulette à craie de tailleur"),
        (r"stylo.*craie", "stylo craie pour tissu"),
        (r"crayon.*craie", "crayon craie de tailleur"),
        (r"poudre.*craie|cartouche.*craie", "recharge de craie de marquage"),
        (r"craie", "craie de tailleur"),
        (r"marqueur.*(?:eau|hydro)", "marqueur textile effaçable à l'eau"),
        (r"marqueur.*(?:air|auto)", "marqueur textile auto-effaçable"),
        (r"marqueur.*(?:chaleur|thermo)|stylo.*thermo", "marqueur textile effaçable à la chaleur"),
        (r"papier.*carbone", "papier carbone pour patron couture"),
        (r"papier.*(?:calque|patron)", "papier à patron pour couture"),
    ],
    "Aiguilles et épingles main": [
        (r"pique.?aiguille|coussin.*epingle", "pique-épingles"),
        (r"aiguilles?.*(?:cuir|sellerie)", "aiguilles main pour cuir"),
        (r"aiguilles?.*(?:broderie|crewel)", "aiguilles main à broder"),
        (r"aiguilles?.*(?:tapisserie|laine)", "aiguilles main à tapisserie"),
        (r"aiguilles?.*(?:quilting|patchwork)", "aiguilles main pour quilting"),
        (r"aiguilles?.*(?:sashiko)", "aiguilles sashiko"),
        (r"aiguilles?.*(?:chenille)", "aiguilles chenille"),
        (r"aiguilles?.*(?:repriser|longues?|darners?)", "aiguilles à repriser"),
        (r"aiguilles?.*(?:poupee|matelas)", "aiguilles longues pour poupée et matelas"),
        (r"aiguilles?.*(?:coudre|sharps|main)", "aiguilles à coudre main"),
        (r"epingles?.*(?:surete|nourrice)", "épingles de sûreté"),
        (r"epingles?.*(?:tete verre|verre)", "épingles à tête de verre"),
        (r"epingles?", "épingles droites de couture"),
        (r"pinces?.*tissu", "pinces de couture pour tissu"),
        (r"de a coudre", "dé à coudre"),
        (r"enfile.?aiguille", "enfile-aiguille manuel"),
    ],
    "Machine à coudre": [
        (r"aiguilles?.*machine.*(?:jean|denim)", "aiguilles machine pour jean"),
        (r"aiguilles?.*machine.*(?:stretch|jersey|super stretch)", "aiguilles machine pour tissu stretch"),
        (r"aiguilles?.*machine.*cuir", "aiguilles machine pour cuir"),
        (r"aiguilles?.*machine.*microtex", "aiguilles machine Microtex"),
        (r"aiguilles?.*machine.*(?:quilting|patchwork)", "aiguilles machine pour quilting"),
        (r"aiguilles?.*machine.*broder", "aiguilles machine à broder"),
        (r"aiguilles?.*machine.*(?:double|jumel)", "aiguilles doubles pour machine à coudre"),
        (r"aiguilles?.*machine.*(?:surjet|overlock)", "aiguilles pour surjeteuse"),
        (r"aiguilles?.*machine", "aiguilles universelles pour machine à coudre"),
        (r"boitier.*canette", "boîtier de canette"),
        (r"canettes?.*(?:metal|acier)", "canettes métal pour machine à coudre"),
        (r"canettes?", "canettes plastique pour machine à coudre"),
        (r"pied.*(?:fermeture|zip).*invisible", "pied presseur pour fermeture invisible"),
        (r"pied.*(?:fermeture|zip)", "pied presseur pour fermeture à glissière"),
        (r"pied.*boutonniere", "pied presseur pour boutonnière"),
        (r"pied.*(?:double entrainement|walking)", "pied presseur double entraînement"),
        (r"pied.*(?:ourlet|roulott)", "pied presseur pour ourlet roulotté"),
        (r"pied.*teflon", "pied presseur téflon pour matières collantes"),
        (r"guide.*couture.*magnet", "guide couture magnétique"),
        (r"huile.*machine", "huile pour machine à coudre"),
        (r"enfile.?aiguille.*machine", "enfile-aiguille pour machine à coudre"),
    ],
    "Fils à coudre": [
        (r"fil.*surjeteuse", "fil polyester pour surjeteuse"),
        (r"fil.*(?:invisible|transparent)", "fil invisible nylon"),
        (r"fil.*elastique", "fil élastique pour fronces"),
        (r"fil.*metall", "fil à coudre métallisé"),
        (r"fil.*(?:jean|denim)", "fil à coudre spécial jean"),
        (r"fil.*(?:surpiq|top stitch)", "fil de surpiqûre"),
        (r"fil.*(?:soie|silk)", "fil à coudre en soie"),
        (r"fil.*coton", "fil à coudre en coton"),
        (r"fil.*(?:extra fort|ameublement|heavy)", "fil extra-fort pour ameublement"),
        (r"fil.*(?:batir|faufiler)", "fil à bâtir"),
        (r"fil.*(?:canette|bobbin)", "fil de canette pour broderie machine"),
        (r"fil.*(?:nylon|polyamide)", "fil nylon résistant"),
        (r"fil.*(?:polyester|tout coudre|couture)", "fil polyester tout coudre"),
    ],
    "Fermetures et attaches": [
        (r"tirette.*fermeture", "tirette de remplacement pour fermeture"),
        (r"fermeture.*invisible", "fermeture à glissière invisible"),
        (r"fermeture.*(?:metal|laiton)", "fermeture à glissière métallique"),
        (r"fermeture.*(?:separable|ouvrable)", "fermeture à glissière séparable"),
        (r"fermeture.*(?:etanche|impermeable)", "fermeture à glissière étanche"),
        (r"fermeture.*(?:continue|au metre)", "fermeture à glissière continue"),
        (r"curseur.*fermeture", "curseur de remplacement pour fermeture"),
        (r"fermeture|zip", "fermeture à glissière nylon"),
        (r"agrafe.*pantalon", "agrafe de pantalon"),
        (r"agrafe|crochet.*oeil", "crochet et agrafe à coudre"),
        (r"fermoir.*magnet|aimant.*coudre", "fermoir magnétique à coudre"),
        (r"fermoir.*(?:porte.?monnaie|cadre)", "fermoir cadre pour porte-monnaie"),
        (r"mousqueton.*(?:pivot|tournant|sac)", "mousqueton pivotant pour sac"),
        (r"boucle.*(?:clip|sac)", "boucle clip pour sangle"),
        (r"boucle.*coulissante", "boucle coulissante pour sangle"),
        (r"tourniquet", "fermoir tourniquet pour sac"),
        (r"bloque.?cordon", "arrêt de cordon"),
        (r"attache.*cartable", "fermoir de cartable"),
    ],
    "Boutons, pressions et œillets": [
        (r"bouton.*recouvrir|bouton.*couvrir", "boutons à recouvrir"),
        (r"bouton.*jean", "boutons de jean à riveter"),
        (r"bouton.*queue", "boutons à queue"),
        (r"bouton.*(?:quatre|4).*trou", "boutons à quatre trous"),
        (r"bouton.*(?:deux|2).*trou", "boutons à deux trous"),
        (r"bouton.*toggle|brandebourg", "boutons toggle brandebourg"),
        (r"bouton.*\bbois\b", "boutons en bois à coudre"),
        (r"bouton", "boutons à coudre"),
        (r"pression.*(?:jersey|plastique)", "boutons-pression plastique pour jersey"),
        (r"pression.*(?:anorak|metal)", "boutons-pression métal"),
        (r"pression.*coudre", "boutons-pression à coudre"),
        (r"pince.*pression", "pince pour boutons-pression"),
        (r"oeillet.*rideau", "œillets pour rideaux"),
        (r"oeillet", "œillets métalliques pour tissu"),
        (r"rivets?", "rivets pour tissu et cuir"),
    ],
    "Rubans, biais, élastiques et cordons": [
        (r"biais.*satin", "biais satin"),
        (r"biais.*coton", "biais coton"),
        (r"biais", "biais textile"),
        (r"passepoil", "passepoil textile"),
        (r"elastique.*boutonniere", "élastique à boutonnières"),
        (r"elastique.*lingerie", "élastique lingerie"),
        (r"elastique.*rond", "élastique rond"),
        (r"elastique.*taille|elastique.*plat", "élastique plat pour ceinture"),
        (r"dentelle", "dentelle textile"),
        (r"ruban.*gros.?grain", "ruban gros-grain"),
        (r"ruban.*satin", "ruban satin"),
        (r"ruban.*serge|serge", "ruban sergé"),
        (r"croquet", "ruban croquet"),
        (r"galon.*frange|frange", "galon à franges"),
        (r"galon", "galon décoratif"),
        (r"sangle", "sangle pour sac"),
        (r"cordon.*coton", "cordon coton"),
        (r"cordon|cordeliere", "cordon de serrage"),
        (r"velcro|scratch|auto.?agripp", "bande auto-agrippante"),
    ],
    "Entoilage, stabilisation et rembourrage": [
        (r"ourlet.*thermocoll|ruban.*thermocoll.*ourlet", "ruban thermocollant pour ourlets"),
        (r"entoilage.*(?:tisse|woven)", "entoilage thermocollant tissé"),
        (r"entoilage.*(?:stretch|maille)", "entoilage thermocollant extensible"),
        (r"entoilage.*double face", "entoilage thermocollant double face"),
        (r"entoilage|vlieseline|thermocollant", "entoilage thermocollant non tissé"),
        (r"stabilisateur.*hydro|solufix|film hydrosoluble", "stabilisateur hydrosoluble pour broderie"),
        (r"stabilisateur.*dechir", "stabilisateur déchirable pour broderie"),
        (r"stabilisateur.*decoup", "stabilisateur à découper pour broderie"),
        (r"stabilisateur|support broderie", "stabilisateur pour broderie machine"),
        (r"ouatine.*thermo", "ouatine thermocollante"),
        (r"ouatine|molleton", "ouatine de rembourrage"),
        (r"rembourrage|kapok", "fibre de rembourrage"),
        (r"mousse.*(?:sac|resille|stabil)", "mousse stabilisatrice pour sacs"),
        (r"renfort.*sac|fond.*sac", "renfort rigide pour fond de sac"),
        (r"bande.*entoilage|stabilmanche", "bande d'entoilage pour coutures"),
    ],
    "Tissus fonctionnels": [
        (r"coton.*aspect lin|coton.*effet lin", "tissu coton effet lin"),
        (r"double gaze", "tissu double gaze de coton"),
        (r"popeline", "tissu popeline de coton"),
        (r"batiste|baptiste", "tissu batiste de coton"),
        (r"voile de coton", "tissu voile de coton"),
        (r"cretonne", "tissu cretonne de coton"),
        (r"seersucker", "tissu seersucker"),
        (r"viscose", "tissu viscose"),
        (r"lin", "tissu en lin"),
        (r"jute", "toile de jute"),
        (r"jersey", "tissu jersey extensible"),
        (r"french terry", "tissu French Terry"),
        (r"sweat|molleton", "tissu sweat molletonné"),
        (r"bord.?cote", "tissu bord-côte"),
        (r"denim|jean", "tissu denim"),
        (r"gabardine", "tissu gabardine"),
        (r"velours", "tissu velours"),
        (r"minky|doudou", "tissu minky peluche"),
        (r"polaire", "tissu polaire"),
        (r"fausse fourrure", "tissu fausse fourrure"),
        (r"matelasse|doudoune", "tissu matelassé"),
        (r"eponge", "tissu éponge"),
        (r"nid d.abeille", "tissu nid d'abeille"),
        (r"jacquard", "tissu jacquard"),
        (r"satin", "tissu satin"),
        (r"soie", "tissu en soie"),
        (r"tulle", "tissu tulle"),
        (r"mesh|filet", "tissu filet mesh"),
        (r"simili cuir", "tissu simili cuir"),
        (r"enduit|deperlant", "tissu enduit déperlant"),
        (r"lycra|maillot", "tissu lycra pour maillot"),
        (r"flanelle", "tissu flanelle"),
        (r"bachette|canvas", "toile canvas épaisse"),
        (r"doublure", "tissu de doublure"),
        (r"organza|organdi", "tissu organza"),
        (r"neoprene", "tissu néoprène"),
    ],
    "Outils tricot et crochet": [
        (r"aiguilles?.*circulaires?", "aiguilles circulaires à tricoter"),
        (r"aiguilles?.*(?:double pointe|chaussette)", "aiguilles double pointe à tricoter"),
        (r"aiguilles?.*(?:droites?|tricoter)", "aiguilles droites à tricoter"),
        (r"crochet.*tunisien", "crochet tunisien"),
        (r"crochet.*ergonom", "crochet ergonomique"),
        (r"crochet", "crochet à laine"),
        (r"compte.?rangs?", "compte-rangs de tricot"),
        (r"marqueur.*maille", "marqueurs de mailles"),
        (r"arrete.?mailles?", "arrête-mailles"),
        (r"aiguille.*torsade", "aiguille à torsade"),
        (r"bobinoir", "bobinoir à laine"),
        (r"devidoir.*laine|devidoir pour laine", "dévidoir à laine"),
        (r"peignes?.*blocage", "peignes de blocage pour tricot"),
        (r"bracelet porte pelote", "porte-pelote bracelet"),
        (r"brosse pour mohair", "brosse d'entretien pour mohair"),
        (r"blocage.*tricot|tapis.*blocage", "tapis de blocage pour tricot"),
        (r"epingles?.*blocage", "épingles de blocage pour tricot"),
        (r"tricotin.*mecan", "tricotin mécanique"),
        (r"tricotin", "tricotin manuel"),
        (r"fourche.*tricoter", "fourche à tricoter"),
    ],
    "Laines et fils créatifs": [
        (r"merinos", "fil à tricoter mérinos"),
        (r"mohair", "fil à tricoter mohair"),
        (r"alpaga", "fil à tricoter alpaga"),
        (r"cachemire", "fil à tricoter cachemire"),
        (r"bambou", "fil à tricoter bambou"),
        (r"lin", "fil à tricoter lin"),
        (r"coton", "fil à tricoter coton"),
        (r"chenille|velvet", "fil chenille pour crochet"),
        (r"raphia", "fil raphia pour crochet"),
        (r"ruban|tape yarn", "fil ruban pour tricot"),
        (r"chaussette|sock", "fil à tricoter pour chaussettes"),
        (r"layette|baby", "fil à tricoter layette"),
        (r"recycle", "fil à tricoter recyclé"),
        (r"lurex|metall", "fil créatif métallisé"),
        (r"acrylique", "fil à tricoter acrylique"),
        (r"laine|pelote|fil a tricoter", "fil à tricoter laine mélangée"),
    ],
    "Broderie, punch needle et macramé": [
        (r"punch needle.*(?:aiguille|outil)", "aiguille punch needle"),
        (r"kit.*punch needle", "kit punch needle"),
        (r"tambour|cercle.*broder", "tambour à broder"),
        (r"toile aida", "toile Aïda pour point de croix"),
        (r"toile.*(?:lin|etamine).*brod", "toile de lin pour broderie"),
        (r"fil.*mouline|mouline", "fil mouliné à broder"),
        (r"fil.*perle", "coton perlé à broder"),
        (r"fil.*metall.*brod", "fil métallisé à broder"),
        (r"aiguille.*tapisserie", "aiguilles à tapisserie"),
        (r"aiguille.*broder", "aiguilles à broder"),
        (r"kit.*point de croix", "kit de point de croix"),
        (r"kit.*broder", "kit de broderie"),
        (r"papier.*transfert.*brod", "papier transfert pour broderie"),
        (r"toile.*soluble|canvas.*soluble", "toile soluble pour broderie"),
        (r"cordon.*macrame|fil.*macrame", "cordon coton pour macramé"),
        (r"planche.*macrame", "planche de travail pour macramé"),
        (r"peigne.*macrame", "peigne pour fibres de macramé"),
    ],
    "Rangement, réparation et repassage": [
        (r"ecusson.*thermocoll", "écusson thermocollant décoratif"),
        (r"coudiere|genouillere", "pièces thermocollantes de réparation"),
        (r"boite.*couture", "boîte à couture compartimentée"),
        (r"organiseur.*fil|rangement.*bobine", "organiseur de bobines de fil"),
        (r"trousse.*aiguille|etui.*aiguille", "étui de rangement pour aiguilles"),
        (r"sac.*tricot|rangement.*laine", "sac de rangement pour tricot"),
        (r"bol.*laine", "bol à laine"),
        (r"patch.*thermo|piece.*thermo", "patch thermocollant de réparation textile"),
        (r"champignon.*repris|oeuf.*repris", "champignon à repriser"),
        (r"rasoir.*textile|anti.?bouloche", "rasoir anti-bouloches textile"),
        (r"regle.*repass", "règle de repassage pour ourlets"),
        (r"pattemouille", "pattemouille de repassage"),
        (r"jeannette", "jeannette de repassage"),
        (r"tapis.*repass", "tapis de repassage couture"),
        (r"filet.*lavage", "filet de lavage pour textiles délicats"),
    ],
    "Accessoires de sacs": [
        (r"anses?.*sac|poignees?.*sac", "anses pour sac"),
        (r"fonds?.*sac", "fond rigide pour sac"),
        (r"pieds?.*sac", "pieds métalliques pour sac"),
        (r"anneau.*(?:d|demi.?lune).*sac", "anneaux en D pour sac"),
        (r"mousqueton.*sac", "mousquetons pour sangle de sac"),
        (r"boucle.*sac|boucle.*sangle", "boucles de réglage pour sangle"),
        (r"chaine.*sac", "chaîne métallique pour sac"),
        (r"attache.*cartable", "attaches de cartable"),
    ],
}


SCRAP_CANONICAL: dict[str, list[tuple[str, str]]] = {
    "Albums et reliure": [
        (r"album.*(?:mdf|bois)", "album vierge en MDF"),
        (r"couverture.*album.*bois", "couverture d'album en bois"),
        (r"couverture.*album.*tissu", "couverture d'album en tissu"),
        (r"album.*classeur|binder", "album classeur à anneaux"),
        (r"album.*spirale", "album photo à spirale"),
        (r"album.*accordeon", "mini-album accordéon"),
        (r"mini.?album", "mini-album scrapbooking"),
        (r"recharges?.*album", "recharges de pages pour album"),
        (r"pochettes?.*album", "pochettes transparentes pour album"),
        (r"anneaux?.*reliure|reliure.*anneaux?", "anneaux métalliques de reliure"),
        (r"vis.*album|extension.*vis", "vis de reliure pour album"),
        (r"toile.*reliure", "toile de reliure pour album"),
        (r"charniere.*album", "charnières pour album"),
        (r"album.*chipboard", "album vierge en carton gris"),
    ],
    "Papiers et supports": [
        (r"papier.*(?:uni|cardstock)", "papier cardstock uni"),
        (r"papier.*imprime|papier.*motif", "papier imprimé scrapbooking"),
        (r"papier.*kraft", "papier kraft scrapbooking"),
        (r"papier.*calque|vellum", "papier calque vellum"),
        (r"papier.*acetate|feuille.*acetate", "feuille d'acétate transparente"),
        (r"papier.*aquarelle", "papier aquarelle"),
        (r"papier.*coton", "papier d'art 100 % coton"),
        (r"papier.*riz", "papier de riz"),
        (r"papier.*soie", "papier de soie"),
        (r"papier.*paillettes|glitter", "papier cardstock pailleté"),
        (r"papier.*metall|papier.*foil", "papier cardstock métallisé"),
        (r"papier.*(?:imitation|effet) bois", "papier scrapbooking effet bois"),
        (r"papier.*velours", "papier velours autocollant"),
        (r"carton.*ondule", "carton ondulé créatif"),
        (r"carton.*gris|chipboard", "carton gris pour reliure"),
        (r"carton.*mousse|foam board", "carton mousse pour maquettes"),
        (r"feuille.*magnet", "feuille magnétique adhésive"),
        (r"papier.*autocollant", "papier autocollant imprimable"),
        (r"papier.*photo", "papier photo pour scrapbooking"),
        (r"toile.*canvas|papier.*canvas", "feuille canvas pour mixed media"),
        (r"carte.*vierge", "cartes vierges pour carterie"),
        (r"enveloppes?", "enveloppes pour carterie"),
    ],
    "Embossage et gaufrage": [
        (r"poudre.*emboss.*(?:rose gold|gold|dore|or)\b", "poudre à embosser métallisée"),
        (r"classeur.*gaufrage|plaque.*gaufrage", "classeur de gaufrage"),
        (r"poudre.*emboss.*paillet", "poudre à embosser pailletée"),
        (r"poudre.*emboss.*metall", "poudre à embosser métallisée"),
        (r"poudre.*emboss.*opaque", "poudre à embosser opaque"),
        (r"poudre.*emboss.*transpar", "poudre à embosser transparente"),
        (r"poudre.*emboss", "poudre à embosser"),
        (r"pistolet.*chauff|heat gun", "pistolet chauffant d'embossage"),
        (r"stylo.*emboss", "stylo à embosser"),
        (r"tapis.*emboss", "tapis silicone pour embossage"),
        (r"diffuseur.*emboss", "diffuseur d'embossage"),
    ],
    "Perforation et massicots": [
        (r"lame.*massicot", "lame de rechange pour massicot"),
        (r"perforatrice.*(?:coin|angle)", "perforatrice d'angle"),
        (r"perforatrice.*bordure", "perforatrice de bordure"),
        (r"perforatrice.*cercle", "perforatrice cercle"),
        (r"perforatrice.*etiquette", "perforatrice étiquette"),
        (r"perforatrice.*alphabet", "perforatrice alphabet"),
        (r"perforatrice", "perforatrice à motif"),
        (r"massicot|rogneuse", "massicot de précision"),
        (r"crop.?a.?dile|pince.*oeillet", "pince perforatrice pour œillets"),
        (r"cutter.*precision|scalpel", "cutter de précision pour papier"),
        (r"tapis.*coupe", "tapis de découpe auto-cicatrisant"),
        (r"compas.*decoupe", "compas cutter circulaire"),
    ],
    "Encres et applicateurs": [
        (r"encre.*spray|spray.*encre", "encre en spray"),
        (r"encre.*oxide", "tampon encreur Distress Oxide"),
        (r"encre.*distress", "tampon encreur Distress"),
        (r"encre.*archival", "tampon encreur archival"),
        (r"encre.*versafine", "tampon encreur pigment fin"),
        (r"encre.*pigment", "tampon encreur pigment"),
        (r"encre.*colorant|dye ink", "tampon encreur à colorant"),
        (r"encre.*alcool", "encre à alcool"),
        (r"encre.*solvant", "encre solvant permanente"),
        (r"encre.*emboss", "encre transparente pour embossage"),
        (r"recharge.*encre", "recharge pour tampon encreur"),
        (r"tampon.*encreur", "tampon encreur pour stamping"),
        (r"applicateur.*encre", "applicateur mousse pour encre"),
        (r"doigt.*mousse", "doigts mousse pour encrage"),
        (r"rouleau.*encre", "rouleau applicateur d'encre"),
        (r"blender|outil.*melange", "outil de mélange pour encres"),
    ],
    "Feutres, peinture et aquarelle": [
        (r"gouache", "peinture gouache"),
        (r"palette.*aquarelle|aquarelle.*palette", "palette d'aquarelle"),
        (r"feutres?.*alcool|marqueurs?.*alcool", "feutres à alcool double pointe"),
        (r"brush pen|feutres?.*pinceau", "feutres pinceaux aquarellables"),
        (r"marqueurs?.*acrylique", "marqueurs peinture acrylique"),
        (r"crayons?.*aquarell", "crayons de couleur aquarellables"),
        (r"crayons?.*couleur", "crayons de couleur artiste"),
        (r"pastels?.*huile", "pastels à l'huile"),
        (r"pastels?", "pastels secs"),
        (r"aquarelle.*liquide", "aquarelle liquide"),
        (r"peinture.*acrylique", "peinture acrylique mixed media"),
        (r"pinceau.*reservoir", "pinceau à réservoir d'eau"),
        (r"pinceaux?", "pinceaux de détail"),
    ],
    "Colles et adhésifs": [
        (r"batons?.*colle", "bâtons de colle thermofusible"),
        (r"colle.*reliure", "colle pour reliure"),
        (r"colle.*precision|precision.*colle", "colle de précision pour papier"),
        (r"stylo.*colle", "stylo-colle"),
        (r"spray.*adhesif|colle.*spray", "colle en spray repositionnable"),
        (r"glue dots|points.*colle", "points de colle adhésifs"),
        (r"roller.*colle|devidoir.*colle", "roller de colle permanent"),
        (r"double face.*mousse|ruban.*mousse", "ruban mousse double face 3D"),
        (r"carres?.*mousse|mousse.*3d", "carrés mousse adhésifs 3D"),
        (r"ruban.*double face|double face", "ruban adhésif double face"),
        (r"feuilles?.*adhesive", "feuilles adhésives double face"),
        (r"colle.*amovible|reposition", "colle repositionnable"),
        (r"colle", "colle sans acide pour scrapbooking"),
    ],
    "Journaling et planners": [
        (r"bullet journal", "carnet bullet journal à points"),
        (r"traveler.?s notebook", "carnet de voyage rechargeable"),
        (r"planner.*anneaux", "planner à anneaux"),
        (r"agenda.*non date|planner.*non date", "planner non daté"),
        (r"agenda|planner", "planner hebdomadaire"),
        (r"carnet.*point", "carnet à pages pointillées"),
        (r"carnet.*lign", "carnet à pages lignées"),
        (r"carnet.*vierge", "carnet à pages vierges"),
        (r"recharge.*planner|insert.*planner", "recharges pour planner"),
        (r"habit tracker|suivi.*habitude", "pochoir de suivi d'habitudes"),
        (r"sticky notes|notes.*adhesives", "notes adhésives de journaling"),
        (r"notes.*repositionn", "notes adhésives de journaling"),
        (r"intercalaires?.*planner", "intercalaires pour planner"),
        (r"cartes?.*journaling", "cartes de journaling"),
    ],
    "Cachets de cire": [
        (r"moules?.*cachet", "moule silicone pour cachets de cire"),
        (r"cachet.*cire|sceau.*cire", "cachet en laiton pour cire"),
        (r"manche.*cachet|poignee.*sceau", "manche pour cachet de cire"),
        (r"perles?.*cire", "perles de cire à cacheter"),
        (r"batons?.*cire", "bâtons de cire à cacheter"),
        (r"cuillere.*cire", "cuillère de fonte pour cire"),
        (r"rechaud.*cire|four.*cire", "réchaud pour cire à cacheter"),
        (r"tapis.*cire|silicone.*cire", "tapis silicone pour cachets de cire"),
        (r"feutre.*cire|stylo.*cire", "feutre métallisé pour cachets de cire"),
    ],
    "Rangement et petit outillage": [
        (r"organisateur.*gaufrage", "organiseur pour classeurs de gaufrage"),
        (r"rangement.*dies|rangement.*matrice", "classeur de rangement pour matrices"),
        (r"rangement.*tampon", "classeur de rangement pour tampons"),
        (r"rangement.*encre|porte.*encre", "rack de rangement pour encres"),
        (r"rangement.*papier|rack.*papier", "rack de rangement pour papiers"),
        (r"rangement.*washi|devidoir.*washi", "dévidoir de rangement pour washi tapes"),
        (r"rangement.*feutre|trousse.*marqueur", "trousse de rangement pour marqueurs"),
        (r"boite.*compartiment", "boîte à compartiments pour embellissements"),
        (r"organiseur|rangement", "organiseur de matériel scrapbooking"),
        (r"plioir", "plioir pour papier"),
        (r"spatule", "spatule de précision pour vinyle et papier"),
        (r"tapis.*silicone", "tapis silicone pour mixed media"),
        (r"regle.*metal", "règle métallique de précision"),
    ],
    "Photo et montage": [
        (r"cadres?.*photo.*bois", "petits cadres photo en bois"),
        (r"porte.?photo.*bois", "porte-photos en bois"),
        (r"porte.?photo", "porte-photo décoratif"),
        (r"coins?.*photo", "coins photo autocollants"),
        (r"carres?.*photo|mounting squares", "carrés adhésifs pour photos"),
        (r"pochettes?.*photo", "pochettes transparentes pour photos"),
        (r"photo flips?|flip.*photo", "rabats transparents pour photos"),
        (r"cadres?.*photo", "cadres papier pour photos"),
        (r"porte.?photo", "porte-photos pour album"),
        (r"attaches?.*photo", "attaches pivotantes pour photos"),
        (r"onglets?.*photo", "onglets adhésifs pour photos"),
        (r"protection.*photo|spray.*photo", "spray protecteur pour photos"),
        (r"gabarit.*photo", "gabarit de découpe pour photos"),
    ],
    "Lettres et étiquettes": [
        (r"rubans?.*etiqueteuse", "rubans de recharge pour étiqueteuse"),
        (r"etiquette.*ardoise", "étiquettes ardoise à suspendre"),
        (r"alphabet.*autocollant|autocollants?.*alphabet", "stickers alphabet"),
        (r"alphabet.*chipboard|lettres?.*carton", "lettres alphabet en chipboard"),
        (r"alphabet.*tampon", "tampons alphabet"),
        (r"alphabet.*matrice|matrice.*alphabet", "matrices alphabet"),
        (r"chiffres?.*autocollant", "stickers chiffres"),
        (r"mots?.*autocollant|stickers?.*mots", "stickers de mots"),
        (r"etiquettes?.*autocoll", "étiquettes autocollantes vierges"),
        (r"etiquettes?.*vierges?|tags?.*vierges?", "étiquettes carton vierges"),
        (r"porte.?etiquette", "porte-étiquettes métalliques"),
        (r"onglets?.*autocoll|tabs?", "onglets autocollants de classement"),
        (r"etiqueteuse|label maker", "étiqueteuse manuelle"),
    ],
}


def canonicalize_candidate(
    niche: str, bucket: str, title: str, concept: str
) -> tuple[str, str] | None:
    folded = ascii_fold(f"{title} {concept}").lower()
    rule_map = MERCERIE_CANONICAL if niche == "mercerie" else SCRAP_CANONICAL
    for pattern, canonical in rule_map.get(bucket, []):
        if re.search(pattern, folded):
            return canonical, ""

    theme = detect_theme(folded)
    if niche == "scrapbooking" and theme:
        theme_fr, theme_en = theme
        if bucket == "Tampons et estampage" and not re.search(r"tampon|stamp", folded):
            return None
        if bucket == "Matrices et découpe" and not re.search(r"matrice|dies?\b|die.?cuts?", folded):
            return None
        if bucket == "Pochoirs et textures" and not re.search(r"pochoir|stencil", folded):
            return None
        if bucket == "Stickers, transferts et masking tape" and not re.search(
            r"sticker|autocollant|masking|washi|transfert|rub.?on", folded
        ):
            return None
        if bucket == "Embellissements" and not re.search(
            r"embellissement|forme en bois|decoupe en bois|ruban|bouton en bois|fleur en papier|attache parisienne|brad|strass adhesif",
            folded,
        ):
            return None
        if bucket == "Kits et assortiments" and not re.search(
            r"kit.*(?:papier|papiers|scrap|album|collection|calque|journaling|carterie)",
            folded,
        ):
            return None
        dynamic_bases = {
            "Tampons et estampage": (
                "tampon transparent" if re.search(r"clear|transparent", folded) else "tampon caoutchouc sur bois",
                "clear silicone stamp" if re.search(r"clear|transparent", folded) else "wood mounted rubber stamp",
            ),
            "Matrices et découpe": ("matrice de découpe", "metal cutting die"),
            "Pochoirs et textures": ("pochoir réutilisable", "reusable plastic stencil"),
            "Stickers, transferts et masking tape": (
                "masking tape décoratif"
                if re.search(r"masking|washi", folded)
                else ("stickers décoratifs" if re.search(r"sticker|autocollant", folded) else "transferts décoratifs"),
                "decorative washi tape"
                if re.search(r"masking|washi", folded)
                else ("decorative stickers" if re.search(r"sticker|autocollant", folded) else "decorative rub on transfers"),
            ),
            "Embellissements": (
                "embellissements en bois"
                if re.search(r"bois", folded)
                else ("ruban décoratif" if re.search(r"ruban", folded) else "embellissements"),
                "laser cut wood embellishments"
                if re.search(r"bois", folded)
                else ("decorative fabric ribbon" if re.search(r"ruban", folded) else "scrapbook embellishments"),
            ),
            "Kits et assortiments": ("kit scrapbooking", "complete scrapbooking kit"),
        }
        if bucket in dynamic_bases:
            base_fr, base_en = dynamic_bases[bucket]
            return f"{base_fr} thème {theme_fr}", f"{base_en} {theme_en} for scrapbooking"

    if niche == "mercerie" and bucket == "Kits et projets":
        kit_rules = [
            (r"amigurumi.*(?:chat|chaton)", "kit crochet amigurumi chat"),
            (r"amigurumi.*(?:chien|chiot)", "kit crochet amigurumi chien"),
            (r"amigurumi.*(?:lapin)", "kit crochet amigurumi lapin"),
            (r"amigurumi.*(?:ours|ourson)", "kit crochet amigurumi ours"),
            (r"amigurumi.*(?:licorne)", "kit crochet amigurumi licorne"),
            (r"amigurumi.*(?:dinosaure)", "kit crochet amigurumi dinosaure"),
            (r"amigurumi", "kit crochet amigurumi"),
            (r"kit.*tricot.*(?:pull|gilet)", "kit tricot pull ou gilet"),
            (r"kit.*tricot.*(?:bonnet|bandeau)", "kit tricot bonnet ou bandeau"),
            (r"kit.*tricot.*(?:echarpe|snood)", "kit tricot écharpe ou snood"),
            (r"kit.*tricot.*chale", "kit tricot châle"),
            (r"kit.*tricot.*bebe", "kit tricot layette bébé"),
            (r"kit.*couture.*(?:sac|pochette|trousse)", "kit couture sac ou pochette"),
            (r"kit.*couture.*(?:jupe|pantalon)", "kit couture jupe ou pantalon"),
            (r"kit.*couture.*(?:robe|top|blouse)", "kit couture vêtement"),
            (r"kit.*couture.*(?:doudou|peluche)", "kit couture doudou"),
            (r"kit.*broder", "kit de broderie complet"),
            (r"kit.*macrame", "kit macramé complet"),
        ]
        for pattern, canonical in kit_rules:
            if re.search(pattern, folded):
                return canonical, ""
    return None


def project_from_chouette(title: str) -> str:
    value = clean_concept(title)
    value = re.sub(r"^(?:couture|crochet)\s+", "", value)
    return value.strip()


def precise_english_query(bucket: str, concept: str, niche: str) -> str:
    folded = ascii_fold(concept).lower()
    if niche == "mercerie":
        mercerie_queries: dict[str, tuple[list[tuple[str, str]], str]] = {
            "Outils de coupe": ([
                (r"crante", "stainless steel pinking shears for fabric sewing"),
                (r"microdente", "micro serrated fabric scissors for precision sewing"),
                (r"gaucher", "left handed stainless steel dressmaking scissors"),
                (r"broderie", "precision stainless steel embroidery scissors"),
                (r"pelican|applique", "duckbill applique scissors for machine embroidery"),
                (r"cuir", "heavy duty leather shears for upholstery sewing"),
                (r"electrique", "electric fabric cutting scissors for sewing"),
                (r"cutter rotatif", "rotary fabric cutter for quilting sewing"),
                (r"cutter de precision", "precision craft knife for sewing patterns"),
                (r"boutonniere", "steel buttonhole cutter chisel for sewing"),
                (r"coupe.?fil", "stainless steel thread snips for sewing embroidery"),
                (r"decoud", "stainless steel seam ripper sewing tool"),
                (r"lame", "replacement rotary cutter blade for fabric sewing"),
            ], "stainless steel dressmaking scissors for fabric sewing"),
            "Mesure": ([
                (r"metre ruban", "flexible tailor measuring tape for sewing"),
                (r"patchwork", "transparent acrylic quilting ruler for patchwork"),
                (r"courbe|modelisme", "French curve ruler for garment pattern making"),
                (r"chaussettes", "wood sock measuring ruler for knitting"),
                (r"ourlet", "heat resistant hem measuring ruler for sewing"),
                (r"jauge.*aiguilles", "knitting needle and crochet hook size gauge"),
                (r"jauge", "sliding sewing gauge for hems buttons pleats"),
                (r"reglet", "stainless steel ruler for precision sewing"),
            ], "graduated sewing pattern ruler for dressmaking"),
            "Traçage et marquage": ([
                (r"roulette.*dente", "serrated tracing wheel for sewing patterns"),
                (r"roulette.*lisse", "smooth tracing wheel for sewing patterns"),
                (r"roulette.*patron", "pattern tracing wheel for dressmaking"),
                (r"roulette.*craie", "tailor chalk wheel for fabric marking"),
                (r"stylo craie", "chalk marker pen for fabric sewing"),
                (r"crayon craie", "tailor chalk pencil for fabric marking"),
                (r"recharge", "refill chalk powder for fabric marker wheel"),
                (r"craie", "washable tailor chalk for fabric marking"),
                (r"eau", "water erasable fabric marker pen for sewing"),
                (r"chaleur", "heat erasable fabric marker pen for sewing"),
                (r"carbone", "dressmaking carbon transfer paper for fabric"),
                (r"papier a patron", "pattern tracing paper roll for dressmaking"),
            ], "washable fabric marking tool for garment sewing"),
            "Aiguilles et épingles main": ([
                (r"pique.?epingles", "magnetic pin cushion for sewing needles"),
                (r"cuir", "heavy duty hand sewing needles for leather"),
                (r"broder", "sharp hand embroidery needles for cotton floss"),
                (r"tapisserie", "blunt tapestry needles for yarn needlework"),
                (r"quilting", "short hand quilting needles for patchwork"),
                (r"sashiko", "long sashiko hand embroidery needles"),
                (r"repriser", "long darning needles for yarn repair"),
                (r"poupee|matelas", "extra long doll making upholstery needles"),
                (r"surete", "stainless steel safety pins for sewing"),
                (r"tete de verre", "glass head straight pins for sewing"),
                (r"pinces", "plastic fabric sewing clips for quilting"),
                (r"de a coudre", "metal sewing thimble finger protector"),
                (r"enfile", "wire needle threader for hand sewing"),
                (r"pique", "magnetic pin cushion for sewing"),
            ], "stainless steel hand sewing needles for fabric"),
            "Machine à coudre": ([
                (r"jean", "denim sewing machine needles for heavy fabric"),
                (r"stretch", "ballpoint sewing machine needles for stretch fabric"),
                (r"cuir", "leather sewing machine needles wedge point"),
                (r"microtex", "Microtex sharp sewing machine needles fine fabric"),
                (r"quilting", "quilting sewing machine needles for patchwork"),
                (r"broder", "machine embroidery needles for decorative thread"),
                (r"doubles", "twin sewing machine needles for parallel stitching"),
                (r"surjeteuse", "overlock serger machine needles stretch fabric"),
                (r"boitier", "metal bobbin case for domestic sewing machine"),
                (r"canettes metal", "metal sewing machine bobbins"),
                (r"canettes plastique", "clear plastic sewing machine bobbins"),
                (r"fermeture invisible", "invisible zipper presser foot sewing machine"),
                (r"fermeture a glissiere", "zipper presser foot sewing machine"),
                (r"boutonniere", "buttonhole presser foot sewing machine"),
                (r"double entrainement", "walking foot presser attachment sewing machine"),
                (r"ourlet", "rolled hem presser foot sewing machine"),
                (r"teflon", "nonstick Teflon presser foot leather vinyl sewing"),
                (r"guide", "magnetic seam guide for sewing machine"),
                (r"huile", "clear sewing machine lubricant oil"),
            ], "universal sewing machine needles for garment sewing"),
            "Fils à coudre": ([
                (r"coton", "cotton sewing thread spool for natural fabrics"),
                (r"soie", "silk sewing thread spool for fine fabrics"),
                (r"jean", "heavy denim topstitching thread spool"),
                (r"invisible", "transparent nylon invisible sewing thread"),
                (r"nylon", "high strength nylon sewing thread spool"),
                (r"elastique", "elastic shirring sewing thread spool"),
                (r"metall", "metallic sewing embroidery thread spool"),
                (r"surjeteuse", "polyester overlock sewing thread cone"),
                (r"extra.?fort", "heavy duty upholstery sewing thread spool"),
                (r"batir", "cotton basting thread for temporary sewing"),
                (r"canette", "bobbin thread for machine embroidery"),
            ], "polyester all purpose sewing thread spool"),
            "Fermetures et attaches": ([
                (r"tirette", "replacement metal zipper pull tab for sewing"),
                (r"curseur", "replacement zipper slider for sewing bags"),
                (r"invisible", "invisible nylon zipper for dress sewing"),
                (r"metallique", "metal teeth zipper for bags garments"),
                (r"separable", "open end separating zipper for jackets"),
                (r"continue", "continuous nylon zipper roll for bag sewing"),
                (r"etanche", "waterproof zipper for outdoor bag sewing"),
                (r"agrafe de pantalon", "metal trouser hook and bar fastener"),
                (r"crochet et agrafe", "metal hook and eye sewing fasteners"),
                (r"magnetique", "magnetic snap closure for handbags"),
                (r"porte.?monnaie", "metal purse frame clasp for bag making"),
                (r"mousqueton", "metal swivel lobster clasp for bag straps"),
                (r"boucle clip", "side release buckle for webbing straps"),
                (r"boucle coulissante", "metal tri glide slider buckle for straps"),
                (r"tourniquet", "metal turn lock clasp for handbags"),
                (r"cordon", "plastic cord lock stopper for drawstrings"),
                (r"cartable", "metal school bag clasp for bag making"),
            ], "nylon coil zipper for garment bag sewing"),
            "Boutons, pressions et œillets": ([
                (r"recouvrir", "metal self cover buttons kit for fabric"),
                (r"jean", "metal jeans tack buttons for denim"),
                (r"queue", "shank sewing buttons for garments"),
                (r"quatre trous", "four hole sewing buttons for garments"),
                (r"deux trous", "two hole sewing buttons for garments"),
                (r"toggle|brandebourg", "wood toggle buttons for coats crafts"),
                (r"bois", "natural wood sewing buttons for crafts"),
                (r"pression plastique", "plastic snap fasteners for jersey fabric"),
                (r"pression metal", "metal snap fasteners for garments"),
                (r"pince", "snap fastener setting pliers sewing tool"),
                (r"oeillets.*rideau", "large metal curtain eyelet grommets"),
                (r"oeillets", "metal eyelet grommets for fabric leather"),
                (r"rivets", "metal rivets for fabric and leather crafts"),
            ], "sewing buttons for garment making"),
            "Rubans, biais, élastiques et cordons": ([
                (r"biais satin", "satin bias binding tape for sewing"),
                (r"biais coton", "cotton bias binding tape for sewing"),
                (r"biais", "fabric bias binding tape for sewing"),
                (r"passepoil", "cotton piping trim cord for sewing"),
                (r"boutonnieres", "buttonhole elastic band for adjustable waist"),
                (r"lingerie", "picot lingerie elastic trim for sewing"),
                (r"elastique rond", "round elastic cord for sewing"),
                (r"elastique plat", "flat elastic band for garment waist"),
                (r"dentelle", "lace trim ribbon for garment sewing"),
                (r"gros.?grain", "grosgrain ribbon for sewing crafts"),
                (r"ruban satin", "double face satin ribbon for crafts"),
                (r"serge", "cotton twill tape for sewing"),
                (r"croquet", "ric rac trim ribbon for sewing"),
                (r"franges", "fringe trim for garment craft sewing"),
                (r"galon", "decorative woven trim for sewing crafts"),
                (r"sangle", "polypropylene cotton webbing strap for bag making"),
                (r"cordon coton", "cotton drawstring cord for sewing crafts"),
                (r"cordon", "drawstring cord for garment bag sewing"),
                (r"auto.?agripp", "hook and loop tape for sewing"),
            ], "decorative fabric ribbon trim for sewing crafts"),
            "Entoilage, stabilisation et rembourrage": ([
                (r"ourlets", "fusible hemming tape for garment sewing"),
                (r"tisse", "woven fusible interfacing for garment sewing"),
                (r"extensible", "stretch fusible knit interfacing for garments"),
                (r"double face", "double sided fusible web for applique"),
                (r"non tisse", "nonwoven fusible interfacing for sewing"),
                (r"hydrosoluble", "water soluble embroidery stabilizer film"),
                (r"dechirable", "tear away embroidery stabilizer backing"),
                (r"decouper", "cut away embroidery stabilizer backing"),
                (r"ouatine thermocollante", "fusible polyester batting for quilting"),
                (r"ouatine", "polyester quilt batting wadding for sewing"),
                (r"fibre", "polyester fiberfill stuffing for toys cushions"),
                (r"mousse", "foam stabilizer for handbag sewing"),
                (r"fond de sac", "rigid bag base stabilizer insert"),
            ], "embroidery stabilizer backing for machine sewing"),
            "Tissus fonctionnels": ([
                (r"double gaze", "double gauze cotton fabric by meter"),
                (r"popeline", "cotton poplin fabric by meter"),
                (r"batiste", "cotton batiste fabric by meter"),
                (r"voile", "lightweight cotton voile fabric by meter"),
                (r"cretonne", "cotton cretonne fabric by meter"),
                (r"seersucker", "cotton seersucker fabric by meter"),
                (r"viscose", "viscose rayon fabric by meter"),
                (r"coton effet lin", "linen look cotton fabric by meter"),
                (r"en lin", "linen fabric by meter sewing"),
                (r"jute", "natural jute burlap fabric by meter"),
                (r"jersey", "stretch jersey knit fabric by meter"),
                (r"french terry", "cotton French terry fabric by meter"),
                (r"sweat", "sweatshirt fleece fabric by meter"),
                (r"bord.?cote", "rib knit cuff fabric by meter"),
                (r"denim", "cotton denim fabric by meter"),
                (r"gabardine", "cotton gabardine fabric by meter"),
                (r"velours", "velvet fabric by meter for sewing"),
                (r"minky", "plush minky fabric by meter"),
                (r"polaire", "polar fleece fabric by meter"),
                (r"fausse fourrure", "faux fur fabric by meter"),
                (r"matelasse", "quilted fabric by meter"),
                (r"eponge", "terry cloth fabric by meter"),
                (r"nid d.abeille", "waffle cotton fabric by meter"),
                (r"jacquard", "woven jacquard fabric by meter"),
                (r"satin", "satin fabric by meter for garments"),
                (r"soie", "silk fabric by meter for garments"),
                (r"tulle", "tulle net fabric by meter"),
                (r"filet mesh", "mesh net fabric by meter"),
                (r"simili cuir", "faux leather fabric for bag making"),
                (r"enduit", "water resistant coated fabric by meter"),
                (r"lycra", "stretch lycra swimwear fabric by meter"),
                (r"flanelle", "cotton flannel fabric by meter"),
                (r"canvas", "heavy cotton canvas fabric by meter"),
                (r"doublure", "polyester lining fabric by meter"),
                (r"organza", "sheer organza fabric by meter"),
            ], "functional fabric by meter for garment sewing"),
            "Outils tricot et crochet": ([
                (r"circulaires", "circular knitting needles for yarn crafts"),
                (r"double pointe", "double pointed knitting needles for socks"),
                (r"droites", "straight knitting needles for yarn crafts"),
                (r"crochet tunisien", "Tunisian crochet hook with cable"),
                (r"crochet ergonomique", "ergonomic aluminum crochet hook"),
                (r"crochet a laine", "aluminum crochet hook for yarn"),
                (r"compte.?rangs", "digital row counter for knitting crochet"),
                (r"marqueurs", "locking stitch markers for knitting crochet"),
                (r"arrete", "stitch holder safety pin for knitting"),
                (r"torsade", "cable knitting needle set"),
                (r"bobinoir", "manual yarn ball winder for knitting"),
                (r"devidoir", "wood yarn swift umbrella winder"),
                (r"peignes", "knitting blocking comb pins set"),
                (r"tapis", "foam blocking mats for knitting"),
                (r"porte.?pelote", "portable wrist yarn holder for knitting"),
                (r"brosse", "mohair garment yarn care brush"),
                (r"tricotin mecanique", "hand crank knitting mill machine"),
                (r"tricotin", "manual spool knitting loom"),
                (r"fourche", "hairpin lace loom for crochet"),
            ], "hand knitting crochet tool for yarn crafts"),
            "Laines et fils créatifs": ([
                (r"merinos", "merino wool yarn skein for knitting crochet"),
                (r"mohair", "mohair blend yarn skein for knitting"),
                (r"alpaga", "alpaca blend yarn skein for knitting"),
                (r"cachemire", "cashmere blend yarn for knitting"),
                (r"bambou", "bamboo blend yarn for knitting crochet"),
                (r"lin", "linen yarn skein for knitting crochet"),
                (r"coton", "cotton yarn skein for knitting crochet"),
                (r"chenille", "velvet chenille yarn for crochet plush toys"),
                (r"raphia", "raffia yarn for crochet bags hats"),
                (r"ruban", "ribbon yarn skein for knitting crochet"),
                (r"chaussettes", "sock yarn wool blend for knitting"),
                (r"layette", "soft baby yarn for knitting crochet"),
                (r"recycle", "recycled fiber yarn for knitting crochet"),
                (r"metallise", "metallic lurex yarn for knitting crochet"),
                (r"acrylique", "acrylic yarn skein for knitting crochet"),
            ], "wool blend yarn skein for knitting crochet"),
            "Broderie, punch needle et macramé": ([
                (r"punch needle", "punch needle embroidery tool for yarn fabric"),
                (r"tambour", "bamboo embroidery hoop for needlework"),
                (r"aida", "cotton Aida cloth for cross stitch"),
                (r"mouline", "cotton embroidery floss skein"),
                (r"perle", "pearl cotton embroidery thread ball"),
                (r"metall", "metallic embroidery floss thread"),
                (r"toile de lin", "linen embroidery fabric for counted thread"),
                (r"tapisserie", "blunt tapestry needles for yarn embroidery"),
                (r"aiguilles a broder", "sharp hand embroidery needles"),
                (r"point de croix", "complete counted cross stitch kit"),
                (r"kit de broderie", "complete hand embroidery kit with hoop floss"),
                (r"transfert", "embroidery transfer paper for fabric patterns"),
                (r"soluble", "water soluble embroidery canvas stabilizer"),
                (r"cordon", "cotton macrame cord for knotting crafts"),
                (r"planche", "macrame knotting project board with grid"),
                (r"peigne", "macrame fringe comb for cotton cord"),
            ], "needlework supply for embroidery fiber crafts"),
            "Kits et projets": ([
                (r"amigurumi chat", "complete crochet cat amigurumi kit with yarn hook"),
                (r"amigurumi chien", "complete crochet dog amigurumi kit with yarn hook"),
                (r"amigurumi lapin", "complete crochet rabbit amigurumi kit with yarn hook"),
                (r"amigurumi ours", "complete crochet bear amigurumi kit with yarn hook"),
                (r"amigurumi", "complete crochet amigurumi kit with yarn hook"),
                (r"tricot pull", "complete sweater knitting kit with yarn needles"),
                (r"tricot chapeau|tricot bonnet", "complete hat knitting kit with yarn needles"),
                (r"echarpe|snood", "complete scarf knitting kit with yarn needles"),
                (r"chale", "complete shawl knitting kit with yarn needles"),
                (r"layette", "complete baby knitting kit with soft yarn"),
                (r"couture sac", "complete bag sewing kit with fabric notions"),
                (r"couture vetement", "complete garment sewing kit with fabric notions"),
                (r"couture doudou", "complete plush toy sewing kit with fabric stuffing"),
                (r"broderie", "complete hand embroidery kit with hoop floss fabric"),
                (r"macrame", "complete macrame kit with cotton cord hardware"),
            ], "complete physical DIY textile craft kit with materials"),
            "Rangement, réparation et repassage": ([
                (r"ecusson", "embroidered iron on patch for clothing crafts"),
                (r"pieces thermocollantes", "iron on fabric repair patches for clothing"),
                (r"boite", "compartment sewing supplies storage box"),
                (r"bobines", "thread spool organizer rack for sewing"),
                (r"aiguilles", "knitting needle storage case organizer"),
                (r"sac", "yarn knitting project storage bag"),
                (r"bol", "wood yarn bowl holder for knitting"),
                (r"repriser", "wood darning mushroom for garment repair"),
                (r"bouloches", "electric fabric lint remover shaver"),
                (r"regle", "heat resistant ironing ruler for hems"),
                (r"pattemouille", "cotton pressing cloth for ironing sewing"),
                (r"jeannette", "sleeve ironing board for garment pressing"),
                (r"tapis", "heat resistant ironing mat for sewing"),
                (r"filet", "mesh laundry bag for delicate garments"),
            ], "textile care repair tool for sewing garments"),
            "Accessoires de sacs": ([
                (r"anses", "replacement bag handles for purse making"),
                (r"fond", "rigid bag base insert for sewing crochet"),
                (r"pieds", "metal purse feet studs for bag making"),
                (r"anneaux", "metal D rings for bag strap sewing"),
                (r"mousquetons", "metal swivel clasps for bag straps"),
                (r"boucles", "metal strap adjuster buckles for bags"),
                (r"chaine", "metal purse chain strap for bag making"),
                (r"cartable", "metal school bag clasp for bag making"),
            ], "metal bag making hardware for sewing crafts"),
        }
        rules, default = mercerie_queries[bucket]
        for pattern, query in rules:
            if re.search(pattern, folded):
                return query
        return default
    if niche == "scrapbooking":
        scrap_bucket_queries: dict[str, tuple[list[tuple[str, str]], str]] = {
            "Albums et reliure": ([
                (r"mdf|bois", "unfinished MDF wood scrapbook album blank"),
                (r"spirale", "spiral bound blank photo scrapbook album"),
                (r"classeur", "ring binder scrapbook album with archival sleeves"),
                (r"recharges", "archival refill pages for scrapbook album"),
                (r"pochettes", "clear archival pocket pages for scrapbook album"),
                (r"anneaux", "metal book binding rings for scrapbook albums"),
                (r"vis", "metal screw posts for scrapbook album binding"),
                (r"toile", "bookbinding cloth fabric for handmade albums"),
                (r"charniere", "metal hinges for handmade scrapbook albums"),
            ], "blank mini scrapbook album for photo paper crafts"),
            "Papiers et supports": ([
                (r"effet bois", "wood grain scrapbook paper acid free"),
                (r"papier de soie", "tissue paper sheets for paper crafts"),
                (r"100.*coton", "100 percent cotton art paper for mixed media"),
                (r"papier de riz", "rice paper sheets for decoupage scrapbooking"),
                (r"calque", "translucent vellum paper for scrapbooking"),
                (r"carton ondule", "corrugated cardboard sheets for paper crafts"),
                (r"carton gris", "thick grey chipboard sheets for album binding"),
                (r"papier kraft", "kraft cardstock paper for scrapbooking"),
                (r"paillete", "glitter cardstock paper for scrapbooking"),
                (r"magnetique", "self adhesive magnetic sheets for die storage"),
                (r"metallise", "metallic foil cardstock for paper crafts"),
                (r"imprime", "patterned scrapbook paper acid free"),
                (r"acetate", "clear acetate sheets for shaker cards scrapbooking"),
                (r"mousse", "foam board sheets for paper craft models"),
                (r"aquarelle", "cold pressed watercolor paper for mixed media"),
                (r"autocollant", "printable self adhesive paper for journaling"),
            ], "acid free solid cardstock paper for scrapbooking"),
            "Embossage et gaufrage": ([
                (r"classeur", "plastic embossing folder for paper crafts"),
                (r"paillet", "glitter heat embossing powder for stamping"),
                (r"metall", "metallic heat embossing powder for stamping"),
                (r"opaque", "opaque heat embossing powder for stamping"),
                (r"transpar", "clear heat embossing powder for stamping"),
                (r"pistolet", "mini heat gun for embossing paper crafts"),
                (r"stylo", "embossing ink pen for heat stamping"),
                (r"tapis", "silicone embossing mat for die cutting machine"),
            ], "heat embossing powder for rubber stamping crafts"),
            "Perforation et massicots": ([
                (r"lame", "replacement blade for portable paper trimmer"),
                (r"massicot", "precision paper trimmer for scrapbooking"),
                (r"coin|angle", "corner paper craft punch for scrapbooking"),
                (r"bordure", "border paper craft punch for scrapbooking"),
                (r"cercle", "circle paper craft punch for scrapbooking"),
                (r"etiquette", "tag label paper craft punch"),
                (r"oeillets", "heavy duty eyelet punch pliers for paper crafts"),
                (r"cutter", "precision craft knife for paper cutting"),
                (r"tapis", "self healing cutting mat for paper crafts"),
            ], "shape paper craft punch for scrapbooking"),
            "Encres et applicateurs": ([
                (r"spray", "pigment ink spray for mixed media scrapbooking"),
                (r"oxide", "water reactive oxide ink pad for scrapbooking"),
                (r"distress", "water based distress ink pad for scrapbooking"),
                (r"archival", "permanent archival ink pad for rubber stamps"),
                (r"pigment fin", "fine detail pigment ink pad for stamps"),
                (r"pigment", "slow dry pigment ink pad for embossing"),
                (r"colorant", "quick dry dye ink pad for rubber stamps"),
                (r"alcool", "alcohol ink bottle for mixed media crafts"),
                (r"solvant", "permanent solvent ink pad for stamping"),
                (r"embossage", "clear embossing ink pad for heat stamping"),
                (r"recharge", "ink refill bottle for stamp pad"),
                (r"applicateur|doigts mousse", "foam ink blending applicators for scrapbooking"),
                (r"rouleau", "rubber brayer roller for ink application"),
                (r"melange", "colorless blender marker for alcohol ink"),
            ], "quick dry ink pad for rubber stamping"),
            "Feutres, peinture et aquarelle": ([
                (r"feutres a alcool", "dual tip alcohol markers for illustration"),
                (r"feutres pinceaux", "watercolor brush marker pens for journaling"),
                (r"marqueurs peinture", "acrylic paint markers for mixed media"),
                (r"crayons.*aquarell", "watercolor colored pencils for mixed media"),
                (r"crayons de couleur", "artist colored pencils for journaling"),
                (r"pastels a l.huile", "oil pastels set for mixed media"),
                (r"pastels secs", "soft dry pastels set for art crafts"),
                (r"palette", "portable watercolor palette for journaling"),
                (r"gouache", "solid gouache paint set for paper crafts"),
                (r"acrylique", "acrylic paint for mixed media paper crafts"),
                (r"reservoir", "water brush pen for watercolor painting"),
                (r"pinceaux", "fine detail paint brushes for watercolor crafts"),
            ], "artist coloring medium for mixed media journaling"),
            "Colles et adhésifs": ([
                (r"thermofusible", "hot melt glue sticks for craft glue gun"),
                (r"reliure", "acid free bookbinding PVA glue"),
                (r"precision", "acid free precision glue for paper crafts"),
                (r"stylo", "fine tip glue pen for paper crafts"),
                (r"spray", "repositionable spray adhesive for paper crafts"),
                (r"points", "clear glue dots for scrapbooking"),
                (r"roller", "permanent tape runner adhesive for scrapbooking"),
                (r"ruban mousse", "double sided foam tape for 3D scrapbooking"),
                (r"carres mousse", "double sided foam squares for 3D cards"),
                (r"ruban adhesif", "acid free double sided tape for scrapbooking"),
                (r"feuilles", "double sided adhesive sheets for die cutting"),
                (r"reposition", "removable glue for paper crafts"),
            ], "acid free liquid glue for scrapbooking paper crafts"),
            "Journaling et planners": ([
                (r"cartes", "printed journaling cards for scrapbook albums"),
                (r"planner", "undated weekly planner notebook"),
                (r"bullet", "dotted bullet journal notebook"),
                (r"voyage", "refillable travelers notebook journal"),
                (r"recharges", "paper refill inserts for planner notebook"),
                (r"notes adhesives", "decorative sticky notes for journaling"),
                (r"intercalaires", "planner divider tabs set"),
            ], "undated journal notebook for bullet journaling"),
            "Cachets de cire": ([
                (r"moule", "silicone wax seal stamp molds for crafts"),
                (r"cachet", "brass wax seal stamp for invitations"),
                (r"manche", "wood handle for brass wax seal stamp"),
                (r"perles", "sealing wax beads for wax stamp crafts"),
                (r"batons", "sealing wax sticks for invitations"),
                (r"cuillere", "metal melting spoon for sealing wax"),
                (r"rechaud", "wax seal melting furnace stove"),
                (r"tapis", "silicone mat for wax seal making"),
            ], "wax seal supply for invitation paper crafts"),
            "Rangement et petit outillage": ([
                (r"gaufrage", "storage organizer for embossing folders"),
                (r"matrices", "binder storage sleeves for metal cutting dies"),
                (r"tampons", "storage binder panels for clear stamps"),
                (r"encres", "ink pad storage rack organizer"),
                (r"papiers", "vertical paper storage rack for scrapbooking"),
                (r"washi", "washi tape storage dispenser organizer"),
                (r"marqueurs", "roll up marker pen storage case"),
                (r"compartiments", "compartment organizer box for embellishments"),
                (r"plioir", "plastic bone folder creasing tool for paper crafts"),
                (r"spatule", "precision weeding spatula for vinyl paper crafts"),
                (r"tapis silicone", "nonstick silicone craft mat for mixed media"),
                (r"regle", "stainless steel precision ruler for paper crafts"),
            ], "craft supplies organizer storage box for scrapbooking"),
            "Photo et montage": ([
                (r"cadres.*bois", "small wooden photo frames for scrapbook decor"),
                (r"porte.?photos.*bois", "wood photo holders for scrapbook display"),
                (r"porte.?photo decoratif", "decorative photo clip holder for scrapbook display"),
                (r"coins", "self adhesive photo corners for scrapbooking"),
                (r"carres", "archival adhesive squares for mounting photos"),
                (r"pochettes", "clear archival photo sleeves for albums"),
                (r"rabats", "clear photo flip pockets for scrapbook albums"),
                (r"cadres", "paper frame embellishments for scrapbook photos"),
                (r"attaches", "metal swivel photo turns for scrapbooking"),
                (r"onglets", "adhesive photo mounting tabs for albums"),
                (r"gabarit", "photo cutting template for scrapbooking"),
            ], "archival photo mounting supplies for scrapbook albums"),
            "Lettres et étiquettes": ([
                (r"rubans de recharge", "embossing label maker refill tape rolls"),
                (r"ardoise", "hanging chalkboard labels for craft organization"),
                (r"stickers alphabet", "alphabet letter stickers for journaling"),
                (r"chipboard", "chipboard alphabet letters for scrapbooking"),
                (r"tampons alphabet", "clear alphabet stamp set for scrapbooking"),
                (r"matrices alphabet", "metal alphabet cutting dies for paper crafts"),
                (r"chiffres", "number stickers for planners scrapbooking"),
                (r"mots", "word phrase stickers for scrapbooking"),
                (r"autocollantes vierges", "blank self adhesive labels for journaling"),
                (r"carton vierges", "blank cardstock tags for scrapbooking"),
                (r"porte.?etiquettes", "metal label holders for albums storage"),
                (r"onglets", "adhesive index tabs for planners"),
                (r"etiqueteuse", "manual embossing label maker for crafts"),
            ], "alphabet label supply for journaling scrapbooking"),
        }
        if bucket in scrap_bucket_queries:
            rules, default = scrap_bucket_queries[bucket]
            for pattern, query in rules:
                if re.search(pattern, folded):
                    return query
            return default
        scrap_rules = [
            (r"album.*(?:mdf|bois)", "unfinished MDF wood scrapbook album blank"),
            (r"album.*classeur|binder", "ring binder scrapbook album with archival sleeves"),
            (r"recharge.*album|pochette.*album", "archival refill pocket pages for scrapbook album"),
            (r"anneau.*reliure|reliure.*anneau", "metal book binding rings for scrapbook albums"),
            (r"toile.*reliure", "bookbinding cloth fabric for handmade albums"),
            (r"vis.*album", "metal extension screw posts for scrapbook albums"),
            (r"album", "blank scrapbook album for photo paper crafts"),
            (r"papier.*(?:100.*coton|coton)", "100 percent cotton art paper sheet for mixed media"),
            (r"papier.*aquarelle", "cold pressed watercolor paper for mixed media"),
            (r"papier.*calque|vellum|calque", "translucent vellum paper for scrapbooking"),
            (r"papier.*riz", "rice paper sheets for decoupage scrapbooking"),
            (r"papier.*kraft|kraft", "kraft cardstock paper for scrapbooking"),
            (r"papier.*paillettes|glitter", "glitter cardstock paper for scrapbooking"),
            (r"papier.*metall|papier.*foil", "metallic foil cardstock for paper crafts"),
            (r"papier.*imitation bois", "wood grain scrapbook paper acid free"),
            (r"acetate", "clear acetate sheets for shaker cards scrapbooking"),
            (r"chipboard|carton gris", "thick chipboard sheets for album making"),
            (r"papier|cardstock|feuille", "acid free cardstock paper for scrapbooking"),
            (r"tampon.*clear|tampon.*transparent", "clear silicone stamp for scrapbooking card making"),
            (r"tampon.*bois", "wood mounted rubber stamp for paper crafts"),
            (r"tampon", "rubber stamp for scrapbooking card making"),
            (r"bloc acrylique|plateforme.*tampon|presse.*tampon", "acrylic stamping platform for clear stamps"),
            (r"matrice|die cut|dies?\b", "metal cutting dies for scrapbooking card making"),
            (r"classeur.*gaufrage|plaque.*gaufrage", "plastic embossing folder for paper crafts"),
            (r"poudre.*emboss", "heat embossing powder for stamping crafts"),
            (r"pistolet.*chauff|heat gun", "mini heat gun for embossing crafts"),
            (r"perforatrice", "paper craft punch for scrapbooking"),
            (r"massicot|rogneuse", "precision paper trimmer for scrapbooking"),
            (r"crop.a.dile|pince.*oeillet", "heavy duty eyelet punch pliers for paper crafts"),
            (r"encre.*oxide", "water reactive oxide ink pad for scrapbooking"),
            (r"encre.*alcool", "alcohol ink for resin and paper crafts"),
            (r"encre|ink pad", "quick dry ink pad for rubber stamping"),
            (r"feutre.*alcool|marqueur.*alcool", "dual tip alcohol markers for illustration"),
            (r"aquarelle", "portable watercolor paint set for journaling"),
            (r"crayon|pastel", "artist colored pencils for mixed media journaling"),
            (r"pinceau", "detail paint brushes for watercolor crafts"),
            (r"mousse 3d|ruban mousse", "double sided foam tape for 3D scrapbooking"),
            (r"double face|adhesif", "acid free double sided tape for scrapbooking"),
            (r"colle", "acid free precision glue for paper crafts"),
            (r"pochoir|mask", "reusable plastic stencil for scrapbooking mixed media"),
            (r"gesso", "acrylic gesso primer for mixed media"),
            (r"pate.*texture|texture paste", "modeling texture paste for mixed media stencils"),
            (r"washi|masking tape", "decorative washi tape for journaling scrapbooking"),
            (r"autocollant|sticker", "decorative stickers for journaling scrapbooking"),
            (r"decalcomanie|rub.on|transfert", "rub on transfer stickers for scrapbooking"),
            (r"mot.*(?:carton|bois)|forme.*bois|decoupe.*bois", "laser cut chipboard wood embellishments for scrapbooking"),
            (r"fleur", "paper flowers embellishments for scrapbooking"),
            (r"attache parisienne|brad", "metal brads fasteners for scrapbooking"),
            (r"strass|demi.perle", "self adhesive rhinestone gems for scrapbooking"),
            (r"embellissement|breloque|charms", "mixed embellishments for scrapbooking crafts"),
            (r"bullet journal|planner|agenda|carnet|journal", "undated journal notebook for bullet journaling"),
            (r"cachet|sceau", "brass wax seal stamp for invitations crafts"),
            (r"cire", "sealing wax beads for wax stamp crafts"),
            (r"boite|rangement|organiseur", "craft supplies organizer storage box scrapbooking"),
            (r"plioir", "bone folder creasing tool for paper crafts"),
            (r"kit|coffret|assortiment", "complete DIY scrapbooking craft kit with paper tools"),
            (r"photo", "archival photo mounting supplies for scrapbooking"),
            (r"alphabet|lettre|etiquette|label", "alphabet label stickers for journaling scrapbooking"),
        ]
        for pattern, query in scrap_rules:
            if re.search(pattern, folded):
                return query
        scrap_defaults = {
            "Albums et reliure": "blank scrapbook album binding supply for paper crafts",
            "Papiers et supports": "acid free paper support for scrapbooking crafts",
            "Tampons et estampage": "rubber stamping supply for scrapbooking card making",
            "Matrices et découpe": "metal cutting die for scrapbooking card making",
            "Embossage et gaufrage": "heat embossing supply for paper crafts stamping",
            "Perforation et massicots": "paper cutting punch tool for scrapbooking crafts",
            "Encres et applicateurs": "quick dry stamping ink supply for scrapbooking",
            "Feutres, peinture et aquarelle": "artist coloring medium for mixed media journaling",
            "Colles et adhésifs": "acid free adhesive for scrapbooking paper crafts",
            "Pochoirs et textures": "reusable stencil texture supply for mixed media",
            "Stickers, transferts et masking tape": "decorative adhesive transfer for journaling scrapbooking",
            "Embellissements": "decorative embellishment for scrapbooking paper crafts",
            "Journaling et planners": "undated notebook accessory for bullet journaling",
            "Cachets de cire": "wax seal supply for invitations paper crafts",
            "Rangement et petit outillage": "precision craft tool for scrapbooking paper projects",
            "Kits et assortiments": "complete DIY scrapbooking kit with paper accessories",
            "Photo et montage": "archival photo mounting supply for scrapbooking albums",
            "Lettres et étiquettes": "alphabet label supply for journaling scrapbooking",
        }
        return scrap_defaults[bucket]
    rules = [
        (r"ciseaux.*crante", "stainless steel pinking shears for fabric sewing"),
        (r"ciseaux.*broder", "precision embroidery scissors stainless steel"),
        (r"ciseaux", "stainless steel fabric scissors for sewing"),
        (r"coupe.fil", "stainless steel thread snips for sewing embroidery"),
        (r"couteau rotatif|cutter rotatif", "rotary fabric cutter for quilting sewing"),
        (r"decoud", "stainless steel seam ripper sewing tool"),
        (r"metre ruban", "flexible tailor measuring tape sewing"),
        (r"regle.*patchwork", "acrylic quilting ruler patchwork sewing"),
        (r"regle|equerre", "acrylic sewing pattern ruler garment making"),
        (r"craie", "washable tailor chalk fabric marking"),
        (r"marqueur textile|stylo textile|feutre textile", "erasable fabric marker pen sewing"),
        (r"papier carbone", "dressmaking carbon transfer paper fabric"),
        (r"aiguille.*jean|aiguille.*denim", "denim sewing machine needles heavy fabric"),
        (r"aiguille.*jersey|aiguille.*stretch", "ballpoint sewing machine needles stretch fabric"),
        (r"aiguille.*cuir", "leather sewing machine needles"),
        (r"aiguille.*machine", "universal sewing machine needles"),
        (r"canette", "clear plastic sewing machine bobbins"),
        (r"pied.*presseur|pied de biche", "presser foot attachment for sewing machine"),
        (r"aiguille.*main|aiguille.*coudre", "stainless steel hand sewing needles"),
        (r"epingle.*surete", "stainless steel safety pins sewing"),
        (r"epingle", "glass head straight pins for sewing"),
        (r"de a coudre", "metal sewing thimble finger protector"),
        (r"fil.*surjeteuse", "polyester overlock sewing thread cone"),
        (r"fil.*invisible", "transparent nylon invisible sewing thread"),
        (r"fil.*elastique", "elastic sewing thread spool shirring"),
        (r"fil.*metal", "metallic embroidery sewing thread spool"),
        (r"fil.*coudre|fil couture", "polyester all purpose sewing thread spool"),
        (r"fermeture.*invisible", "invisible nylon zipper for dress sewing"),
        (r"fermeture|zip", "nylon coil zipper for sewing bags garments"),
        (r"mousqueton", "metal swivel lobster clasp for bag straps"),
        (r"fermoir.*magnet|aimant", "magnetic metal snap closure for bags"),
        (r"agrafe", "metal hook and eye fastener for garments"),
        (r"bouton.*pression|pression", "metal snap fastener kit for sewing"),
        (r"oeillet", "metal eyelet grommet kit fabric leather"),
        (r"bouton", "sewing buttons for garment making"),
        (r"biais", "cotton bias binding tape for sewing"),
        (r"passepoil", "cotton piping cord trim for sewing"),
        (r"elastique", "elastic band for garment sewing"),
        (r"ruban", "decorative fabric ribbon for sewing crafts"),
        (r"sangle", "polypropylene webbing strap for bag making"),
        (r"cordon", "cotton drawstring cord for sewing crafts"),
        (r"entoilage.*thermo|thermocollant|vlieseline", "fusible interfacing fabric for garment sewing"),
        (r"stabilisateur.*broder|support broder", "embroidery stabilizer backing fabric"),
        (r"ouatine|rembourrage|kapok", "polyester fiber filling for sewing crafts"),
        (r"mousse", "foam stabilizer for bag sewing"),
        (r"double gaze", "double gauze cotton fabric by meter sewing"),
        (r"popeline", "cotton poplin fabric by meter sewing"),
        (r"viscose", "viscose fabric by meter garment sewing"),
        (r"lin|jute", "linen fabric by meter sewing crafts"),
        (r"velours", "velvet fabric by meter garment sewing"),
        (r"jersey", "stretch jersey fabric by meter garment sewing"),
        (r"denim|jean", "denim cotton fabric by meter sewing"),
        (r"minky|doudou", "plush minky fabric by meter baby sewing"),
        (r"simili cuir", "faux leather fabric for bag sewing"),
        (r"tulle|mesh|filet", "mesh tulle fabric by meter sewing"),
        (r"tissu|toile|satin|soie|gabardine|polaire", "fabric by meter for garment sewing"),
        (r"aiguille.*circulaire", "stainless steel circular knitting needles"),
        (r"aiguille.*tricoter", "knitting needles for yarn crafts"),
        (r"crochet.*tunis", "tunisian crochet hook aluminum"),
        (r"crochet", "ergonomic aluminum crochet hook"),
        (r"compte.rang", "digital row counter for knitting crochet"),
        (r"marqueur.*maille", "locking stitch markers for knitting crochet"),
        (r"bobinoir|devidoir.*laine", "manual yarn ball winder knitting"),
        (r"tricotin", "hand knitting loom spool knitter"),
        (r"mohair", "mohair blend yarn for knitting crochet"),
        (r"merinos", "merino wool yarn for knitting crochet"),
        (r"alpaga", "alpaca blend yarn for knitting crochet"),
        (r"raphia", "raffia yarn for crochet bags"),
        (r"pelote|laine|fil.*tricoter", "soft yarn skein for knitting crochet"),
        (r"punch needle", "punch needle embroidery tool kit fabric yarn"),
        (r"tambour|cercle.*broder", "bamboo embroidery hoop for needlework"),
        (r"toile aida", "cotton aida cloth for cross stitch"),
        (r"mouline|fil perle", "cotton embroidery floss thread"),
        (r"macrame", "cotton macrame cord for knotting crafts"),
        (r"boite.*couture|rangement couture|organiseur couture", "sewing supplies organizer storage box"),
        (r"patch.*thermo|piece.*thermo", "iron on fabric repair patches clothing"),
        (r"repass", "heat resistant ironing accessory for sewing"),
        (r"anse|poignee.*sac", "replacement bag handles for purse making"),
        (r"fond.*sac", "pre cut bag base insert for crochet sewing"),
    ]
    for pattern, query in rules:
        if re.search(pattern, folded):
            return query
    mercerie_defaults = {
        "Outils de coupe": "stainless steel cutting tool for fabric sewing",
        "Mesure": "tailor measuring tool for garment sewing patterns",
        "Traçage et marquage": "washable fabric marking tool for garment sewing",
        "Aiguilles et épingles main": "stainless steel hand needle pin for sewing",
        "Machine à coudre": "sewing machine accessory for garment construction",
        "Fils à coudre": "polyester thread spool for garment sewing",
        "Fermetures et attaches": "metal garment closure fastener for sewing",
        "Boutons, pressions et œillets": "metal clothing fastener for garment sewing",
        "Rubans, biais, élastiques et cordons": "textile trim tape for garment bag sewing",
        "Entoilage, stabilisation et rembourrage": "sewing stabilizer material for textile crafts",
        "Tissus fonctionnels": "functional fabric by meter for garment sewing",
        "Outils tricot et crochet": "hand tool for knitting and crochet yarn crafts",
        "Laines et fils créatifs": "yarn skein for knitting crochet textile crafts",
        "Broderie, punch needle et macramé": "needlework material for embroidery fiber crafts",
        "Kits et projets": "complete physical DIY textile craft kit with materials",
        "Rangement, réparation et repassage": "textile care repair tool for sewing garments",
        "Accessoires de sacs": "metal bag making hardware for sewing crafts",
    }
    return mercerie_defaults[bucket]


def french_query(bucket: str, concept: str, niche: str) -> str:
    suffix = "couture mercerie" if niche == "mercerie" else "scrapbooking journaling"
    return re.sub(r"\s+", " ", f"{concept} {suffix}").strip()


def enrich_scrapmalin_titles(rows: list[dict[str, str]], limit: int = 40) -> None:
    """Replace slug-derived labels with the live PDP h1 for a bounded pool."""
    classified = defaultdict(list)
    for row in rows:
        bucket = classify("scrapbooking", row["title"], row["collection"])
        if bucket:
            classified[bucket].append(row)
    pool: list[dict[str, str]] = []
    while len(pool) < limit and any(classified.values()):
        for bucket in SCRAP_TARGETS:
            if classified[bucket]:
                pool.append(classified[bucket].pop(0))
                if len(pool) >= limit:
                    break
    def fetch_title(row: dict[str, str]) -> tuple[dict[str, str], str]:
        try:
            body = fetch_bytes(row["url"], attempts=2).decode("utf-8", "replace")
        except RuntimeError:
            return row, ""
        match = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.I | re.S)
        if match:
            title = strip_tags(match.group(1))
            if title:
                return row, title
        return row, ""

    with ThreadPoolExecutor(max_workers=12) as executor:
        futures = [executor.submit(fetch_title, row) for row in pool]
        for future in as_completed(futures):
            row, title = future.result()
            if title:
                row["title"] = title
                row["pdp_title_verified"] = "yes"


def collect_sources() -> tuple[dict[str, list[dict[str, str]]], list[dict[str, object]]]:
    rows_by_source: dict[str, list[dict[str, str]]] = defaultdict(list)
    manifests = []
    for source in SOURCES:
        body = fetch_bytes(source.url)
        if source.kind == "woocommerce":
            rows = parse_woocommerce(source, body)
        else:
            rows = parse_sitemap(source, body)
        for row in rows:
            row.update(
                {
                    "source_slug": source.slug,
                    "competitor": source.competitor,
                    "domain": source.domain,
                    "niche": source.niche,
                }
            )
        rows_by_source[source.slug].extend(rows)
        manifests.append(
            {
                "source_slug": source.slug,
                "competitor": source.competitor,
                "competitor_domain": source.domain,
                "niche": source.niche,
                "source_url": source.url,
                "source_kind": source.kind,
                "http_payload_bytes": len(body),
                "parsed_rows": len(rows),
                "observed_at": OBSERVED_AT,
                "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
            }
        )
    enrich_scrapmalin_titles(rows_by_source["scrapmalin"])
    return rows_by_source, manifests


def build_candidates(rows_by_source: dict[str, list[dict[str, str]]]) -> list[Candidate]:
    candidates = []
    for source_slug, rows in rows_by_source.items():
        for row in rows:
            niche = row["niche"]
            title = row["title"]
            evidence_status = "OBSERVE_CONCURRENT"
            derived_note = ""
            if source_slug == "scrapmalin" and row.get("pdp_title_verified") != "yes":
                continue
            if source_slug == "chouette-kit":
                if not re.search(r"(?i)\b(tuto|tutoriel|patron|pdf)\b", title):
                    continue
                project = project_from_chouette(title)
                if not project:
                    continue
                concept = f"kit physique {project}"
                evidence_status = "EQUIVALENT_DERIVE"
                derived_note = (
                    "Kit physique dérivé du tutoriel/patron observé; la fiche source "
                    "prouve le projet, pas l'existence d'un kit concurrent identique."
                )
            else:
                concept = clean_concept(title)
            # Classify from the product itself.  Collection labels are retained
            # for traceability but cannot turn an unrelated product into a
            # mercerie/scrap concept (e.g. a silicone baking mould in a paper
            # category).
            bucket = classify(niche, concept, "")
            if not bucket or is_bad_candidate(niche, title, concept, row["url"]):
                continue
            canonicalized = canonicalize_candidate(niche, bucket, title, concept)
            if not canonicalized:
                continue
            concept, english_query_override = canonicalized
            collection = (
                bucket
                if source_slug in {"rascol", "fee-du-scrap", "scrapmalin"}
                else row["collection"]
            )
            signature = signature_for(concept)
            if len(signature.split()) < 2:
                continue
            candidates.append(
                Candidate(
                    niche=niche,
                    competitor=row["competitor"],
                    domain=row["domain"],
                    collection=collection or bucket,
                    title=title,
                    url=row["url"],
                    source_url=row["source_url"],
                    bucket=bucket,
                    concept=concept,
                    signature=signature,
                    evidence_status=evidence_status,
                    derived_note=derived_note,
                    english_query_override=english_query_override,
                )
            )
    return candidates


def quality_score(candidate: Candidate) -> tuple[int, int, str]:
    folded = ascii_fold(candidate.title).lower()
    score = 0
    if 3 <= len(candidate.concept.split()) <= 10:
        score += 6
    if len(candidate.concept) <= 85:
        score += 3
    if any(term in folded for term in ["professionnel", "ergonomique", "bio", "coton", "métal", "bois", "silicone", "thermocollant"]):
        score += 2
    if re.search(r"\b\d{5,}\b", folded):
        score -= 3
    if candidate.evidence_status == "OBSERVE_CONCURRENT":
        score += 1
    return (-score, len(candidate.concept), candidate.concept)


def select_catalogue(
    niche: str,
    candidates: list[Candidate],
    targets: dict[str, int],
    source_minimums: dict[str, int],
) -> list[Candidate]:
    pool = [candidate for candidate in candidates if candidate.niche == niche]
    pool.sort(key=quality_score)
    by_bucket_source: dict[str, dict[str, list[Candidate]]] = defaultdict(lambda: defaultdict(list))
    for candidate in pool:
        by_bucket_source[candidate.bucket][candidate.competitor].append(candidate)

    selected: list[Candidate] = []
    seen_signatures: set[str] = set()
    seen_urls: set[str] = set()
    source_counts: Counter[str] = Counter()

    def eligible(candidate: Candidate) -> bool:
        return candidate.signature not in seen_signatures and candidate.url not in seen_urls

    for bucket, target in targets.items():
        available = [candidate for candidate in pool if candidate.bucket == bucket]
        cursor = 0
        while sum(item.bucket == bucket for item in selected) < target:
            eligible_candidates = [candidate for candidate in available if eligible(candidate)]
            if not eligible_candidates:
                break
            deficits = {
                competitor: max(0, minimum - source_counts[competitor])
                for competitor, minimum in source_minimums.items()
            }
            eligible_candidates.sort(
                key=lambda candidate: (
                    -deficits.get(candidate.competitor, 0),
                    source_counts[candidate.competitor],
                    quality_score(candidate),
                )
            )
            candidate = eligible_candidates[0]
            selected.append(candidate)
            seen_signatures.add(candidate.signature)
            seen_urls.add(candidate.url)
            source_counts[candidate.competitor] += 1
            cursor += 1

    shortfalls = {
        bucket: target - sum(item.bucket == bucket for item in selected)
        for bucket, target in targets.items()
        if sum(item.bucket == bucket for item in selected) < target
    }
    missing_sources = {
        source: minimum - source_counts[source]
        for source, minimum in source_minimums.items()
        if source_counts[source] < minimum
    }
    if shortfalls or missing_sources:
        print(
            json.dumps(
                {
                    "niche": niche,
                    "bucket_shortfalls": shortfalls,
                    "source_minimum_shortfalls": missing_sources,
                    "selected": len(selected),
                    "source_counts": dict(source_counts),
                },
                ensure_ascii=False,
            )
        )
    return selected


def to_output(candidate: Candidate) -> dict[str, str]:
    if candidate.evidence_status == "EQUIVALENT_DERIVE":
        basis = (
            f"{candidate.derived_note} Projet distinct retenu: « {candidate.concept} ». "
            "Aucune variante de couleur ou de taille n'est comptée."
        )
    elif candidate.bucket in {
        "Tampons et estampage",
        "Matrices et découpe",
        "Stickers, transferts et masking tape",
        "Papiers et supports",
        "Embellissements",
    }:
        basis = (
            "Produit concurrent observé; fonction, technique ou thème créatif explicitement "
            f"distinct (« {candidate.concept} ») après retrait des marques, couleurs, tailles, "
            "quantités et codes."
        )
    else:
        basis = (
            "Produit concurrent observé; fonction, matière ou usage distinct "
            f"(« {candidate.concept} ») après retrait des marques, couleurs, tailles, "
            "quantités et codes."
        )
    return {
        "niche": candidate.niche,
        "competitor": candidate.competitor,
        "competitor_domain": candidate.domain,
        "competitor_collection": candidate.collection,
        "competitor_product_title": candidate.title,
        "competitor_product_url": candidate.url,
        "concept_fr_normalized": candidate.concept,
        "distinctness_basis": basis,
        "keyword_fr_candidate": candidate.concept,
        "aliexpress_query_fr": french_query(candidate.bucket, candidate.concept, candidate.niche),
        "aliexpress_query_en": candidate.english_query_override
        or precise_english_query(candidate.bucket, candidate.concept, candidate.niche),
        "evidence_status": candidate.evidence_status,
        "observed_at": OBSERVED_AT,
        "source_url": candidate.source_url,
    }


def persist_raw(
    rows_by_source: dict[str, list[dict[str, str]]],
    manifests: list[dict[str, object]],
    selected: list[Candidate],
) -> None:
    manifest_by_slug: dict[str, list[dict[str, object]]] = defaultdict(list)
    for manifest in manifests:
        manifest_by_slug[str(manifest["source_slug"])].append(manifest)
    selected_by_slug: dict[str, list[dict[str, str]]] = defaultdict(list)
    source_lookup = {(source.competitor, source.domain): source.slug for source in SOURCES}
    for candidate in selected:
        slug = source_lookup[(candidate.competitor, candidate.domain)]
        selected_by_slug[slug].append(
            {
                "competitor_product_title": candidate.title,
                "competitor_product_url": candidate.url,
                "competitor_collection": candidate.collection,
                "concept_fr_normalized": candidate.concept,
                "evidence_status": candidate.evidence_status,
                "source_url": candidate.source_url,
                "observed_at": OBSERVED_AT,
            }
        )
    for slug in sorted(set(rows_by_source) | set(manifest_by_slug)):
        directory = RAW_ROOT / slug / OBSERVED_AT
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "source-manifest.json").write_text(
            json.dumps(manifest_by_slug[slug], ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        (directory / "selected-products.json").write_text(
            json.dumps(selected_by_slug[slug], ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )


def validate(output: list[dict[str, str]]) -> dict[str, object]:
    required = [
        "niche",
        "competitor",
        "competitor_domain",
        "competitor_collection",
        "competitor_product_title",
        "competitor_product_url",
        "concept_fr_normalized",
        "distinctness_basis",
        "keyword_fr_candidate",
        "aliexpress_query_fr",
        "aliexpress_query_en",
        "evidence_status",
        "observed_at",
        "source_url",
    ]
    for index, row in enumerate(output):
        missing = [field for field in required if not row.get(field)]
        if missing:
            raise RuntimeError(f"Row {index} missing required fields: {missing}")
        if row["evidence_status"] not in {"OBSERVE_CONCURRENT", "EQUIVALENT_DERIVE"}:
            raise RuntimeError(f"Row {index} has invalid evidence status")
        if row["observed_at"] != OBSERVED_AT:
            raise RuntimeError(f"Row {index} has invalid observation date")
        if not row["competitor_product_url"].startswith("https://"):
            raise RuntimeError(f"Row {index} has invalid product URL")
        query = row["aliexpress_query_en"].lower()
        if len(query.split()) < 4:
            raise RuntimeError(f"Row {index} English query too broad: {query}")

    counts = Counter(row["niche"] for row in output)
    if not counts.get("mercerie") or not counts.get("scrapbooking"):
        raise RuntimeError(f"Missing niche output: {counts}")
    for niche in counts:
        rows = [row for row in output if row["niche"] == niche]
        signatures = [signature_for(row["concept_fr_normalized"]) for row in rows]
        if len(signatures) != len(set(signatures)):
            duplicates = [key for key, count in Counter(signatures).items() if count > 1]
            raise RuntimeError(f"Duplicate normalized concepts in {niche}: {duplicates[:10]}")
        urls = [row["competitor_product_url"] for row in rows]
        if len(urls) != len(set(urls)):
            raise RuntimeError(f"Duplicate competitor URLs in {niche}")
    return {
        "total": len(output),
        "by_niche": dict(counts),
        "target_by_niche": {"mercerie": 220, "scrapbooking": 220},
        "deficit_by_niche": {
            "mercerie": 220 - counts["mercerie"],
            "scrapbooking": 220 - counts["scrapbooking"],
        },
        "by_competitor": dict(Counter(row["competitor"] for row in output)),
        "by_status": dict(Counter(row["evidence_status"] for row in output)),
        "unique_normalized_concepts": len(
            {f"{row['niche']}::{signature_for(row['concept_fr_normalized'])}" for row in output}
        ),
        "unique_product_urls": len({row["competitor_product_url"] for row in output}),
    }


def write_markdown(output: list[dict[str, str]], validation: dict[str, object]) -> None:
    by_niche = defaultdict(list)
    for row in output:
        by_niche[row["niche"]].append(row)
    lines = [
        "# Expansion catalogue — mercerie créative et scrapbooking",
        "",
        f"Observation des sources publiques : {OBSERVED_AT}.",
        "",
        "## Résultat contrôlé",
        "",
        f"- Mercerie créative & arts du fil : **{len(by_niche['mercerie'])} concepts dédupliqués** sur la cible de 220 (déficit assumé : {220-len(by_niche['mercerie'])}).",
        f"- Scrapbooking & journaling : **{len(by_niche['scrapbooking'])} concepts dédupliqués** sur la cible de 220 (déficit assumé : {220-len(by_niche['scrapbooking'])}).",
        f"- Total : **{validation['total']} lignes**, **{validation['unique_normalized_concepts']} signatures de concept uniques par niche** et **{validation['unique_product_urls']} fiches concurrentes uniques**.",
        "- Les couleurs, dimensions, quantités, codes, marques et noms de modèles sont retirés avant déduplication.",
        "- Le quota n'est jamais complété avec des vidéos, tutoriels, PDF, services ou quasi-variantes; un déficit reste explicite.",
        "- Les thèmes de tampon, matrice ou embellissement ne sont conservés que lorsqu'ils correspondent à un usage créatif distinct, pas à une simple couleur ou taille.",
        "",
        "## Statut des preuves",
        "",
    ]
    for status, count in sorted(validation["by_status"].items()):
        lines.append(f"- `{status}` : {count}")
    lines.extend(
        [
            "",
            "`EQUIVALENT_DERIVE` désigne uniquement un kit physique dérivé d'un tutoriel/projet Chouette Kit observé. La ligne indique explicitement que le concurrent ne prouve pas l'existence du kit physique identique.",
            "",
            "## Répartition par concurrent",
            "",
            "| Concurrent | Concepts |",
            "|---|---:|",
        ]
    )
    for competitor, count in sorted(validation["by_competitor"].items()):
        lines.append(f"| {competitor} | {count} |")
    lines.extend(["", "## Couverture par famille", ""])
    for niche, targets in [("mercerie", MERCERIE_TARGETS), ("scrapbooking", SCRAP_TARGETS)]:
        title = "Mercerie créative & arts du fil" if niche == "mercerie" else "Scrapbooking & journaling"
        lines.extend([f"### {title}", "", "| Famille | Concepts |", "|---|---:|"])
        # Reclassify from concept and collection for a compact audit table.
        counts = Counter()
        for row in by_niche[niche]:
            bucket = classify(niche, row["concept_fr_normalized"], row["competitor_collection"])
            counts[bucket or "Non classé"] += 1
        for bucket in targets:
            lines.append(f"| {bucket} | {counts[bucket]} |")
        lines.append("")
    lines.extend(
        [
            "## Méthode et garde-fous",
            "",
            "1. Lecture de sitemaps, titres d'images produit et API catalogue publics; aucune session Chrome, SEMrush ou AliExpress.",
            "2. Conservation du titre concurrent, de la fiche produit et du sitemap/API source dans chaque ligne.",
            "3. Normalisation sans marque, couleur, taille, quantité ou code, puis déduplication par signature lexicale.",
            "4. Stratification par familles fonctionnelles afin d'éviter un corpus rempli de variantes d'un même type.",
            "5. Requêtes AliExpress préparatoires en français et en anglais avec type de produit + matière ou usage; elles ne prouvent ni disponibilité, ni prix, ni livraison France.",
            "",
            "## Limites / éléments manquants",
            "",
            "- Les lignes sont des concepts de sourcing inspirés de catalogues concurrents; aucune correspondance fournisseur exacte n'est affirmée.",
            "- Les volumes de recherche, prix AliExpress, délais, variantes, conformité et marge restent `MANQUANT` tant que les gates SEMrush/SERP puis API AliExpress ne sont pas exécutés.",
            "- Une présence dans un sitemap ne garantit pas le stock au moment d'une future validation; la fiche doit être revérifiée avant décision.",
            "",
            "## Fichiers de preuve",
            "",
            "Les extractions sélectionnées et manifestes (URL source, octets lus, date et nombre de lignes parsées) sont conservés sous `competitor-profiles/raw/catalogue-expansion/<concurrent>/2026-08-08/`.",
            "",
        ]
    )
    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows_by_source, manifests = collect_sources()
    candidates = build_candidates(rows_by_source)
    mercerie = select_catalogue(
        "mercerie",
        candidates,
        MERCERIE_TARGETS,
        {
            "Rascol": 55,
            "Craftine": 55,
            "Atelier de la Création": 55,
        },
    )
    scrap = select_catalogue(
        "scrapbooking",
        candidates,
        SCRAP_TARGETS,
        {
            "Scrapmalin": 16,
            "La Fourmi Créative": 35,
            "Fée du Scrap": 35,
            "Florilèges Design / Variations Créatives": 35,
        },
    )
    selected = mercerie + scrap
    output = [to_output(candidate) for candidate in selected]
    validation = validate(output)
    OUTPUT_JSON.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    persist_raw(rows_by_source, manifests, selected)
    write_markdown(output, validation)
    print(json.dumps(validation, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

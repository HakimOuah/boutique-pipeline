#!/usr/bin/env python3
"""Build a public, evidence-linked catalogue concept corpus.

No SEMrush, Chrome, AliExpress, Shopify mutation, spreadsheet or Git operation
is performed. AliExpress fields are query strings only.
"""

from __future__ import annotations

import collections
import concurrent.futures
import datetime as dt
import difflib
import html
import json
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


OBSERVED_AT = "2026-08-08"
ROOT = Path(__file__).resolve().parents[2]
RAW_ROOT = ROOT / "competitor-profiles" / "raw" / "catalogue-expansion"
OUT_JSON = ROOT / "competitor-profiles" / "workstreams" / "catalogue-expansion-chien-aquarium.json"
OUT_MD = ROOT / "competitor-profiles" / "workstreams" / "catalogue-expansion-chien-aquarium.md"
UA = "Mozilla/5.0 (compatible; CodexCatalogueResearch/1.0; public catalogue snapshot)"


def request_text(url: str, retries: int = 3, timeout: int = 35) -> str:
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return response.read().decode("utf-8", "ignore")
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last = exc
            time.sleep(0.8 * (attempt + 1))
    raise RuntimeError(f"GET failed: {url}: {last}")


def request_json(url: str):
    return json.loads(request_text(url))


def save_raw(slug: str, filename: str, payload) -> None:
    folder = RAW_ROOT / slug / OBSERVED_AT
    folder.mkdir(parents=True, exist_ok=True)
    with (folder / filename).open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def text_clean(value: str) -> str:
    value = html.unescape(value or "")
    value = re.sub(r"<[^>]+>", " ", value)
    value = value.replace("™", " ").replace("®", " ")
    value = re.sub(r"\s+", " ", value)
    return value.strip(" -–—|")


def slug_to_title(url: str) -> str:
    name = urllib.parse.urlparse(url).path.rstrip("/").split("/")[-1]
    name = re.sub(r"\.html?$", "", name, flags=re.I)
    name = re.sub(r"^\d+-", "", name)
    return text_clean(name.replace("-", " "))


def path_collection(url: str) -> str:
    parts = [p for p in urllib.parse.urlparse(url).path.split("/") if p]
    if len(parts) >= 2:
        raw = parts[-2]
        if raw.lower() in {"fr", "products", "produit"} and len(parts) >= 3:
            raw = parts[-3]
        return text_clean(raw.replace("-", " "))
    return "Catalogue général"


def dog_collection(title: str, tags=None, product_type: str = "") -> str:
    hay = " ".join([title, product_type, " ".join(tags or [])]).lower()
    rules = [
        ("Transport et voyage", ["transport", "carrier", "travel", "avion", "voiture", "car seat", "caisse"]),
        ("Harnais", ["harnais", "harness"]),
        ("Laisses et longes", ["laisse", "leash", "longe", "long line", "bungee"]),
        ("Ceintures et baudriers", ["ceinture", "baudrier", "belt"]),
        ("Colliers", ["collier", "collar"]),
        ("Manteaux et protection météo", ["manteau", "jacket", "coat", "raincoat", "gilet", "vest", "pull"]),
        ("Bottines et protection des pattes", ["bottine", "bootie", "chaussure", "patte", "paw"]),
        ("Couchage et bivouac", ["panier", "couchage", "bed", "sleeping", "tapis", "blanket"]),
        ("Hydratation et alimentation nomade", ["gourde", "gamelle", "bowl", "food", "snack"]),
        ("Jouets et dressage", ["jouet", "toy", "ball", "frisbee", "dressage", "training"]),
        ("Soins et premiers secours", ["tique", "soin", "spray", "baume", "care", "first aid", "bandage"]),
        ("Sécurité et visibilité", ["sécurité", "visible", "visibility", "réfléch", "light", "lampe"]),
        ("Sacs et rangement", ["sac", "bag", "backpack", "pouch"]),
        ("Pièces détachées", ["replacement", "spare", "pièce", "strap", "buckle"]),
    ]
    for label, needles in rules:
        if any(n in hay for n in needles):
            return label
    if product_type:
        return text_clean(product_type)
    if tags:
        return text_clean(tags[0])
    return "Accessoires pour chien"


def aquarium_collection(title: str, category: str = "") -> str:
    hay = f"{title} {category}".lower()
    rules = [
        ("Filtration", ["filtr", "biomaster", "ultramax", "exhausteur", "skimmer"]),
        ("Éclairage", ["led", "éclairage", "eclairage", "rampe", "lampe", "chihiros"]),
        ("CO2 et fertilisation", ["co2", "engrais", "fertil", "carbone", "diffuseur", "détendeur"]),
        ("Plantes aquatiques", ["plante", "anubias", "microsorum", "bucephalandra", "mousse", "cryptocoryne", "rotala", "hygrophila"]),
        ("Sols et substrats", ["sol ", "soil", "substrat", "sable", "gravier"]),
        ("Hardscape et décoration", ["racine", "roche", "pierre", "coco", "hardscape", "décor", "decoration", "amphore"]),
        ("Aquariums et supports", ["aquarium", "cuve", "nanocube", "scaper", "meuble"]),
        ("Pompes et brassage", ["pompe", "brassage", "waterchanger"]),
        ("Chauffage et température", ["chauff", "thermo", "température", "temperature"]),
        ("Tests et mesure", ["test", "ph ", "gh ", "kh ", "conductiv", "thermomètre", "mesure"]),
        ("Nourriture", ["food", "nourrit", "pellet", "snack", "loll", "flake", "artemia"]),
        ("Crevettes et élevage", ["crevette", "shrimp", "caridina", "neocaridina", "élevage", "elevage"]),
        ("Entretien et traitement", ["nettoy", "algue", "traitement", "conditionneur", "bacter", "entretien"]),
        ("Outils et accessoires", ["outil", "pince", "ciseau", "épuisette", "epuisette", "tuyau", "support", "accessoire"]),
    ]
    for label, needles in rules:
        if any(n in hay for n in needles):
            return label
    return text_clean(category) or "Matériel d'aquariophilie"


def fetch_shopify(slug: str, domain: str, pages: int, niche: str):
    records = []
    endpoints = []
    for page in range(1, pages + 1):
        url = f"https://{domain}/products.json?limit=250&page={page}"
        endpoints.append(url)
        payload = request_json(url)
        products = payload.get("products", [])
        for product in products:
            tags = product.get("tags") or []
            if isinstance(tags, str):
                tags = [x.strip() for x in tags.split(",") if x.strip()]
            title = text_clean(product.get("title", ""))
            if not title:
                continue
            handle = product.get("handle")
            product_url = f"https://{domain}/products/{handle}" if handle else url
            product_type = text_clean(product.get("product_type", ""))
            collection = (
                dog_collection(title, tags, product_type)
                if niche == "chien"
                else aquarium_collection(title, product_type or (tags[0] if tags else ""))
            )
            records.append(
                {
                    "niche": niche,
                    "competitor": text_clean(product.get("vendor") or domain),
                    "competitor_domain": domain.replace("www.", ""),
                    "competitor_collection": collection,
                    "competitor_product_title": title,
                    "competitor_product_url": product_url,
                    "source_url": product_url,
                    "evidence_status": "OBSERVE_CONCURRENT",
                    "raw_method": "public_shopify_products_json",
                    "tags": tags,
                    "product_type": product_type,
                }
            )
        if len(products) < 250:
            break
    compact = {
        "observed_at": OBSERVED_AT,
        "source_type": "public_shopify_products_json",
        "endpoints": endpoints,
        "count": len(records),
        "products": records,
    }
    save_raw(slug, "products-public.json", compact)
    return records


def fetch_fenril():
    pages = [
        "https://www.fenril.fr/5-materiel-cani-rando?page=1",
        "https://www.fenril.fr/5-materiel-cani-rando?page=2",
        "https://www.fenril.fr/5-materiel-cani-rando?page=3",
    ]
    products = []
    seen = set()
    for page in pages:
        body = request_text(page)
        articles = re.findall(r"<article\b.*?</article>", body, re.I | re.S)
        for article in articles:
            match = re.search(
                r'<a\s+href="([^"]+)"\s+title="([^"]+)"\s+class="[^"]*product_img_link',
                article,
                re.I | re.S,
            )
            if not match:
                continue
            url, title = html.unescape(match.group(1)), text_clean(match.group(2))
            if url in seen or not title:
                continue
            seen.add(url)
            products.append(
                {
                    "niche": "chien",
                    "competitor": "Fenril",
                    "competitor_domain": "fenril.fr",
                    "competitor_collection": dog_collection(title, product_type=path_collection(url)),
                    "competitor_product_title": title,
                    "competitor_product_url": url,
                    "source_url": url,
                    "evidence_status": "OBSERVE_CONCURRENT",
                    "raw_method": "public_collection_product_card",
                    "collection_page": page,
                }
            )
    save_raw(
        "fenril",
        "collection-products.json",
        {
            "observed_at": OBSERVED_AT,
            "source_type": "public_collection_product_cards",
            "collection_pages": pages,
            "count": len(products),
            "products": products,
        },
    )
    return products


def polytrans_observed_collection_products():
    source = "https://www.polytrans.fr/chiens/sport-plein-air/marche-randonnee"
    titles = [
        "Gourde avec écuelle en plastique pour chien",
        "Ceinture canicross Canistrail",
        "Botte de protection des pattes Kn'1 Tech PSS",
        "Masque de protection Rex Specs V2",
        "Harnais chien Art Sportiv Plus",
        "Centaura insectifuge acarifuge pour chien",
        "Sac à dos pour chien Front Range Ruffwear",
        "Harnais chien X-Back Kn'1 Powerful",
        "Récipient compartimenté eau et nourriture pour chien",
        "Laisse pour chien Soft Trainer",
        "Écran solaire Sunfree Dermoscent pour chien",
        "Ceinture de cani-jogging et canicross Canisrun",
        "Spray réhydratant de la peau Ermidra",
        "Protection ventrale Brush Guard pour harnais",
        "Veste de chasse camouflage pour chien",
        "Harnais polyvalent avec poignée Line Grip",
        "Bandana haute visibilité pour chien",
        "Collier haute visibilité pour chien",
        "Veste haute visibilité pour chien",
        "Tente légère de randonnée pour chien",
        "Veste harnais Overcoat Fuse pour chien",
        "Sac de bât pour chien",
    ]
    products = []
    for title in titles:
        products.append(
            {
                "niche": "chien",
                "competitor": "Polytrans",
                "competitor_domain": "polytrans.fr",
                "competitor_collection": dog_collection(title),
                "competitor_product_title": title,
                "competitor_product_url": source,
                "source_url": source,
                "evidence_status": "EQUIVALENT_DERIVE",
                "raw_method": "named_product_observed_on_collection_page",
            }
        )
    save_raw(
        "polytrans",
        "collection-products.json",
        {
            "observed_at": OBSERVED_AT,
            "source_type": "named_products_on_public_collection",
            "collection_page": source,
            "note": "PDP URLs were not captured because the site returned HTTP 429 outside the public search renderer.",
            "count": len(products),
            "products": products,
        },
    )
    return products


def sitemap_locs(xml_text: str):
    locs = []
    for raw in re.findall(r"<loc>(.*?)</loc>", xml_text, re.I | re.S):
        # Prestashop emits product URLs inside CDATA.  Keeping the wrapper made
        # urlparse treat the value as a relative path and silently discarded the
        # whole public catalogue.
        value = re.sub(r"^\s*<!\[CDATA\[|\]\]>\s*$", "", raw.strip())
        locs.append(html.unescape(value.strip()))
    return locs


def product_urls_from_presta_sitemap(index_url: str):
    index = request_text(index_url)
    children = sitemap_locs(index)
    docs = []
    if any("sitemap" in urllib.parse.urlparse(u).path for u in children):
        docs = children
    else:
        docs = [index_url]
    urls = []
    for doc in docs:
        try:
            body = request_text(doc)
        except RuntimeError:
            continue
        for url in sitemap_locs(body):
            path = urllib.parse.urlparse(url).path
            if "large_default" in path or "small_default" in path or "medium_default" in path:
                continue
            if re.search(r"/\d+-[^/]+\.html$", path, re.I):
                urls.append(url)
    return list(dict.fromkeys(urls))


def diverse_urls(urls, limit: int):
    groups = collections.defaultdict(list)
    for url in urls:
        groups[path_collection(url)].append(url)
    ordered = []
    keys = sorted(groups)
    while len(ordered) < limit:
        progressed = False
        for key in keys:
            if groups[key]:
                ordered.append(groups[key].pop(0))
                progressed = True
                if len(ordered) >= limit:
                    break
        if not progressed:
            break
    return ordered


def scrape_product_h1(url: str):
    try:
        body = request_text(url, retries=2)
        match = re.search(r"<h1\b[^>]*>(.*?)</h1>", body, re.I | re.S)
        if match:
            return text_clean(match.group(1)), "OBSERVE_CONCURRENT"
    except RuntimeError:
        pass
    return slug_to_title(url), "EQUIVALENT_DERIVE"


def fetch_presta_catalogue(slug: str, competitor: str, domain: str, index_url: str, limit: int):
    all_urls = product_urls_from_presta_sitemap(index_url)
    selected_urls = diverse_urls(all_urls, limit)
    products = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=7) as pool:
        results = list(pool.map(scrape_product_h1, selected_urls))
    for url, (title, status) in zip(selected_urls, results):
        collection_raw = path_collection(url)
        products.append(
            {
                "niche": "aquarium",
                "competitor": competitor,
                "competitor_domain": domain,
                "competitor_collection": aquarium_collection(title, collection_raw),
                "competitor_product_title": title,
                "competitor_product_url": url,
                "source_url": url,
                "evidence_status": status,
                "raw_method": "presta_sitemap_plus_h1" if status == "OBSERVE_CONCURRENT" else "presta_sitemap_slug_derivation",
                "source_collection_slug": collection_raw,
            }
        )
    save_raw(
        slug,
        "sitemap-products.json",
        {
            "observed_at": OBSERVED_AT,
            "source_type": "public_prestashop_sitemap_plus_product_h1",
            "index_url": index_url,
            "total_product_urls_discovered": len(all_urls),
            "count_sampled": len(products),
            "products": products,
        },
    )
    return products


def fetch_materiel_aquatique():
    domain = "materiel-aquatique.com"
    products = []
    endpoints = []
    # Public Store API categories selected for equipment / aquascaping breadth.
    # This avoids letting the default date order fill the snapshot with pond
    # spare parts and live fish before filtration or aquascaping products.
    category_ids = [90, 89, 91, 97, 93, 101, 185, 99, 133, 119, 181, 188, 444, 143, 87]
    seen = set()
    for category_id in category_ids:
        url = (
            f"https://{domain}/wp-json/wc/store/v1/products"
            f"?per_page=100&page=1&category={category_id}"
        )
        endpoints.append(url)
        payload = request_json(url)
        for product in payload:
            title = text_clean(product.get("name", ""))
            if not title:
                continue
            categories = [text_clean(x.get("name", "")) for x in product.get("categories", []) if x.get("name")]
            category = categories[0] if categories else "Matériel d'aquariophilie"
            permalink = product.get("permalink") or f"https://{domain}/?p={product.get('id')}"
            if permalink in seen:
                continue
            seen.add(permalink)
            products.append(
                {
                    "niche": "aquarium",
                    "competitor": "Materiel-Aquatique",
                    "competitor_domain": domain,
                    "competitor_collection": aquarium_collection(title, category),
                    "competitor_product_title": title,
                    "competitor_product_url": permalink,
                    "source_url": permalink,
                    "evidence_status": "OBSERVE_CONCURRENT",
                    "raw_method": "public_woocommerce_store_api",
                    "categories": categories,
                }
            )
    save_raw(
        "materiel-aquatique",
        "products-public.json",
        {
            "observed_at": OBSERVED_AT,
            "source_type": "public_woocommerce_store_api",
            "endpoints": endpoints,
            "count": len(products),
            "products": products,
        },
    )
    return products


COLORS = [
    "noir", "noire", "blanc", "blanche", "rouge", "bleu", "bleue", "vert", "verte",
    "rose", "gris", "grise", "orange", "jaune", "violet", "violette", "teal", "black",
    "white", "red", "blue", "green", "pink", "grey", "gray", "purple", "brown", "brun",
    "beige", "anthracite",
]
BRANDS = [
    "non stop dogwear", "non-stop dogwear", "ruffwear", "trixie", "inlandsis", "zero dc",
    "kn 1", "ezydog", "dermoscent", "oase", "aquael", "eheim", "jbl", "dennerle",
    "chihiros", "tropica", "ada", "glasgarten", "superfish", "seachem", "sera",
    "aquaplante", "skaii shrimps", "shrimp delice", "aqua nova", "sl aqua", "co2art",
    "twinstar", "qualdrop", "horizon aqua", "dupla", "groTech", "aquatlantis",
    "aquatic science", "aqua medic", "auto aqua", "arcadia", "benibachi", "ista",
    "dooa", "uns", "söchting", "sochting", "viv", "onf", "naturholic", "salty shrimp",
    "shrimp king", "shrimp forever", "shrimpTastic", "dr bassleer", "koi pro", "vdl",
    "manmat", "axaeco", "centaura", "rex specs", "ermidra",
]


def candidate_relevant(candidate):
    """Keep physical products in the requested niches, not adjacent merchandise.

    Raw snapshots still preserve everything returned by the public catalogues;
    this gate only controls which rows may enter the 220-concept corpus.
    """
    title = remove_accents(candidate.get("competitor_product_title", "").lower())
    collection = remove_accents(candidate.get("competitor_collection", "").lower())
    product_type = remove_accents(candidate.get("product_type", "").lower())
    domain = candidate.get("competitor_domain", "")
    if candidate.get("niche") == "chien":
        if any(x in title for x in ["e-book", "ebook", "carte cadeau", "gift card", "sticker"]):
            return False
        if domain == "nonstopdogwear.com" and product_type in {
            "jackets", "pants", "sweaters", "hats & caps", "t-shirts", "shorts",
            "racesuits", "socks", "mittens",
        }:
            return False
        if domain == "fenril.fr" and any(
            x in title for x in ["pantalon trekking", "pantalon convertible", "casquette sport", "bonnet hiver"]
        ):
            return False
        return True

    # Live animals, terrarium goods and services are public-catalogue evidence,
    # but are not sensible AliExpress equipment concepts for this workstream.
    categories = " ".join(remove_accents(x.lower()) for x in candidate.get("categories", []))
    if any(x in categories for x in ["poissons aquarium", "crevettes pour aquarium"]):
        return False
    if "bassin" in categories and "aquarium" not in categories:
        return False
    blocked_collection = [
        "poisson", "cichlide", "discus", "guppy", "betta", "tetra ", "loricari",
        "invertebres d eau douce", "escargots terrestres", "terrarium", "reptile",
    ]
    if any(x in collection for x in blocked_collection):
        return False
    blocked_title = [
        "projet de hardscape", "sauvage colombie", "nishikigoi", "tosai", "femelle",
        "guppy ", "betta ", "discus ", "tetraodon", "biotodoma", "platydoras",
        "geosesarma", "atya gabonensis", "botia lohachata", "escargot succinea",
        "habistat", "peluche ",
    ]
    return not any(x in title for x in blocked_title)


def remove_accents(value: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", value) if not unicodedata.combining(c))


EN_TO_FR = [
    ("dog life jacket", "gilet de sauvetage pour chien"),
    ("dog raincoat", "imperméable pour chien"),
    ("dog jacket", "manteau pour chien"),
    ("dog harnesses", "harnais pour chien"),
    ("dog harness", "harnais pour chien"),
    ("dog leashes", "laisses pour chien"),
    ("dog leash", "laisse pour chien"),
    ("dog collars", "colliers pour chien"),
    ("dog collar", "collier pour chien"),
    ("dog booties", "bottines pour chien"),
    ("dog bootie", "bottine pour chien"),
    ("dog bed", "couchage pour chien"),
    ("long line", "longe pour chien"),
    ("hands-free", "mains libres"),
    ("raincoat", "imperméable"),
    ("cooling", "rafraîchissant"),
    ("drying", "séchant"),
    ("fleece", "polaire"),
    ("wool", "laine"),
    ("harness", "harnais"),
    ("leash", "laisse"),
    ("collar", "collier"),
    ("belt", "ceinture"),
    ("bootie", "bottine"),
    ("jacket", "manteau"),
    ("vest", "gilet"),
    ("backpack", "sac à dos"),
    ("bag", "sac"),
    ("replacement", "pièce de remplacement"),
    ("rope", "corde"),
    ("ball", "balle"),
    ("bowl", "gamelle"),
]

FR_TO_EN = [
    ("gilet de sauvetage pour chien", "dog life jacket"),
    ("harnais anti traction", "no pull dog harness"),
    ("harnais de traction", "dog pulling harness"),
    ("harnais pour chien", "dog harness"),
    ("laisse pour chien", "dog leash"),
    ("longe pour chien", "dog long line"),
    ("collier pour chien", "dog collar"),
    ("ceinture de canicross", "canicross belt"),
    ("ceinture", "belt"),
    ("baudrier", "canicross belt"),
    ("manteau pour chien", "dog coat"),
    ("imperméable", "raincoat"),
    ("bottine", "dog boot"),
    ("chaussure", "dog shoe"),
    ("panier", "dog bed"),
    ("couchage", "dog bed"),
    ("sac à dos", "backpack"),
    ("sac de transport", "pet carrier"),
    ("caisse de transport", "pet travel crate"),
    ("gamelle", "pet bowl"),
    ("gourde", "dog water bottle"),
    ("jouet", "dog toy"),
    ("balle", "dog ball"),
    ("tire tique", "tick remover"),
    ("réfléchissant", "reflective"),
    ("haute visibilité", "high visibility"),
    ("rafraîchissant", "cooling"),
    ("séchant", "drying"),
    ("polaire", "fleece"),
    ("filtre externe", "external aquarium filter"),
    ("filtration", "aquarium filtration"),
    ("filtre", "aquarium filter"),
    ("éclairage", "aquarium light"),
    ("rampe led", "aquarium LED light"),
    ("lampe led", "aquarium LED light"),
    ("pompe", "aquarium pump"),
    ("chauffage", "aquarium heater"),
    ("plante aquatique", "aquarium plant"),
    ("plante", "aquarium plant"),
    ("racine", "aquarium driftwood"),
    ("roche", "aquarium rock"),
    ("pierre", "aquarium stone"),
    ("sol technique", "aquarium active soil"),
    ("substrat", "aquarium substrate"),
    ("sable", "aquarium sand"),
    ("gravier", "aquarium gravel"),
    ("nourriture", "aquarium food"),
    ("crevette", "shrimp"),
    ("épuisette", "aquarium net"),
    ("tuyau", "aquarium hose"),
    ("conditionneur", "aquarium water conditioner"),
    ("engrais", "aquarium plant fertilizer"),
    ("test", "aquarium water test"),
    ("aquarium", "aquarium"),
]


def phrase_replace(value: str, replacements):
    result = value
    for source, target in replacements:
        result = re.sub(rf"\b{re.escape(source)}\b", target, result, flags=re.I)
    return result


def candidate_search_text(candidate):
    value = " ".join(
        [
            candidate.get("competitor_product_title", ""),
            candidate.get("competitor_collection", ""),
            candidate.get("product_type", ""),
            " ".join(candidate.get("tags", [])),
            " ".join(candidate.get("categories", [])),
            candidate.get("source_collection_slug", ""),
        ]
    )
    value = remove_accents(text_clean(value).lower())
    return re.sub(r"\s+", " ", value)


def generic_product(candidate):
    """Return an evidence-bounded generic FR concept and precise EN query.

    An empty pair means that the public product is adjacent, proprietary, live,
    decorative-only, or otherwise outside the sourceable catalogue perimeter.
    """
    raw = candidate_search_text(candidate)
    title_raw = remove_accents(text_clean(candidate.get("competitor_product_title", "")).lower())

    def first_rule(rules):
        for needles, fr, en in rules:
            if any(needle in title_raw for needle in needles):
                return fr, en
        return "", ""

    def feature_pairs(pairs):
        fr_seen, en_seen = [], []
        for needles, fr, en in pairs:
            if any(needle in raw for needle in needles):
                if fr and fr not in fr_seen:
                    fr_seen.append(fr)
                if en and en not in en_seen:
                    en_seen.append(en)
        return fr_seen, en_seen

    if candidate["niche"] == "chien":
        # Merchandise humain, pièces de marque et accessoires décoratifs ne
        # répondent pas au cœur balade / transport / mobilité / outdoor.
        blocked = [
            "replacement", "spare part", "buckle", "front piece", "leg strap",
            "adapter", "end-rope", "stickers", "t-shirt", "pants", "shorts",
            "racesuit", "wool socks", "cap ", "casquette", "bonnet", "bob ",
            "bandana", "deguisement", "cosplay", "tutu", "criniere", "ebook",
            "e-book", "canape", "protege canape", "housse de canape", "puzzle",
            "clicker", "brosse", "coupe ongle", "collerette", "couche ", "culotte",
            "collier perle", "collier etrangleur", "tapis essuie patte", "tapis absorbant",
            " perle", "lampe chauffante",
        ]
        if any(term in raw for term in blocked):
            return "", ""
        rules = [
            (("masque de protection", "dog goggles", "rex specs"), "Lunettes de protection pour chien", "protective dog goggles for outdoor hiking"),
            (("chariot", "wheelchair"), "Chariot de mobilité pour chien", "adjustable rear leg dog wheelchair mobility aid"),
            (("gilet de sauvetage", "life jacket"), "Gilet de sauvetage pour chien", "buoyant dog life jacket for swimming boating"),
            (("caisse de transport", "travel crate"), "Caisse de transport pour chien", "foldable ventilated dog travel crate"),
            (("sac a dos de transport", "sac de transport", "carrier backpack", "dog carrier"), "Sac de transport pour chien", "ventilated dog carrier backpack for travel"),
            (("sac kangourou", "sling carrier"), "Sac bandoulière de transport pour chien", "breathable dog sling carrier for travel"),
            (("panier moto", "motorcycle basket"), "Panier de transport moto pour chien", "secure dog motorcycle carrier basket"),
            (("panier velo", "bicycle basket"), "Panier de transport vélo pour chien", "secure dog bicycle carrier basket"),
            (("panier de voiture", "dog car bed"), "Panier de voyage pour voiture pour chien", "dog car travel bed with safety tether"),
            (("protection coffre", "trunk liner"), "Protection de coffre de voiture pour chien", "waterproof dog car trunk cargo liner"),
            (("grille protection", "protection chien voiture grille", "barre protection"), "Barrière rigide de voiture pour chien", "adjustable dog car safety barrier grille"),
            (("filet de protection", "car safety net"), "Filet de séparation automobile pour chien", "mesh dog car safety divider net"),
            (("siege avec rangement", "avec rangement"), "Protection de siège auto avec rangement pour chien", "dog car seat protector with storage pockets"),
            (("protection de banquette", "protection voiture", "protege siege", "car seat cover"), "Protection de banquette de voiture pour chien", "waterproof dog car back seat protector hammock"),
            (("siege auto", "car seat"), "Siège auto de sécurité pour chien", "dog safety car seat with tether"),
            (("ceinture de securite", "seat belt"), "Ceinture de sécurité automobile pour chien", "adjustable dog car seat belt tether"),
            (("remorque", "bike trailer"), "Remorque vélo pour chien", "foldable dog bicycle trailer for outdoor travel"),
            (("piquet d attache", "tie out stake"), "Piquet d’attache au sol pour chien", "spiral steel dog tie out stake for camping"),
            (("sonaillon", "safety bell"), "Clochette de sécurité pour chien", "dog hiking safety bell for collar"),
            (("tente", "camping tent"), "Tente légère pour chien", "lightweight waterproof dog camping tent"),
            (("sleeping bag", "sac de couchage"), "Sac de couchage de bivouac pour chien", "insulated dog sleeping bag for camping hiking"),
            (("bivouac", "camping mat", "highlands pad", "outdoor mat"), "Tapis de sol de bivouac pour chien", "foldable waterproof dog camping sleeping mat"),
            (("sac de bat", "saddle backpack", "approach pack", "day pack", "palisades pack"), "Sac de bât pour chien", "adjustable dog saddle backpack for hiking"),
            (("gourde 3 en 1",), "Gourde nomade trois-en-un pour chien", "three in one dog water bottle food waste bag dispenser"),
            (("gourde avec gamelle",), "Gourde avec gamelle intégrée pour chien", "portable dog water bottle with integrated bowl"),
            (("gourde avec distributeur",), "Gourde à distributeur d’eau pour chien", "portable dog water bottle with push dispenser"),
            (("gourde isotherme",), "Gourde isotherme pour chien", "insulated stainless steel dog water bottle for hiking"),
            (("gourde pliable",), "Gourde pliable pour chien", "collapsible silicone dog water bottle for travel"),
            (("gourde", "water bottle"), "Gourde nomade pour chien", "portable leakproof dog water bottle for hiking"),
            (("recipient compartimente", "eau et nourriture"), "Récipient nomade eau et nourriture pour chien", "dual compartment dog food water travel container"),
            (("gamelle pliable", "gamelle nomade", "gamelle voyage", "travel bowl", "trail runner bowl", "trekking bowl"), "Gamelle nomade pour chien", "collapsible silicone dog travel bowl for hiking"),
            (("kit cani-vtt", "kit cani vtt", "biking kit", "bikejoring kit"), "Kit de cani-VTT pour chien", "dog bikejoring pulling harness bungee line antenna kit"),
            (("kit canicross",), "Kit de canicross pour chien", "dog canicross pulling harness bungee leash belt kit"),
            (("kit canirando", "kit cani-rando"), "Kit de cani-randonnée pour chien", "dog hiking harness bungee leash waist belt kit"),
            (("harnais x-back", "x-back", "x back"), "Harnais X-back de traction pour chien", "X back dog pulling harness for canicross mushing"),
            (("harnais canicross", "pulling harness", "freemotion harness"), "Harnais de traction pour canicross", "ergonomic dog pulling harness for canicross"),
            (("harnais de traineau", "sled harness"), "Harnais de traction pour traîneau", "dog pulling harness for sled mushing"),
            (("harnais tactique", "harnais militaire", "police harness"), "Harnais tactique pour chien", "tactical dog harness with MOLLE handle"),
            (("harnais sacoche",), "Harnais à sacoches pour chien", "dog hiking harness with saddle bags"),
            (("harnais rafraichissant",), "Harnais rafraîchissant pour chien", "evaporative cooling dog harness for hiking"),
            (("harnais chien aveugle",), "Harnais guide pour chien aveugle", "support guide harness for blind dog"),
            (("harnais d assistance",), "Harnais d’assistance pour chien", "service dog assistance harness with handle"),
            (("harnais de levage", "harnais de maintien", "harnais de soulagement", "harnais de portage", "train arriere"), "Harnais de levage et mobilité pour chien", "dog lift support harness for rear leg mobility"),
            (("harnais de randonnee",), "Harnais de randonnée pour chien", "padded dog hiking harness with handle"),
            (("harnais pour laver",), "Harnais de maintien pour toilettage de chien", "dog grooming restraint harness for washing"),
            (("harnais integre",), "Manteau avec harnais intégré pour chien", "waterproof dog coat with integrated harness"),
            (("harnais en y", "forme de y"), "Harnais en Y pour chien", "Y shape ergonomic no pull dog harness"),
            (("harnais chien en h",), "Harnais en H pour chien", "H shape adjustable dog walking harness"),
            (("harnais chien en t",), "Harnais en T pour chien", "T shape dog walking harness"),
            (("harnais 3 point", "three point harness"), "Harnais anti-fugue trois points pour chien", "escape proof three point dog harness for walking"),
            (("harnais anti traction", "no pull"), "Harnais anti-traction pour chien", "no pull dog walking harness with front clip"),
            (("harnais avec poignee", "line grip", "harness with handle"), "Harnais avec poignée pour chien", "dog walking harness with control handle"),
            (("brush guard", "protection ventrale"), "Protection ventrale pour harnais de chien", "dog harness chest belly protection panel for hiking"),
            (("harnais", "harness"), "Harnais de promenade pour chien", "adjustable ergonomic dog walking harness"),
            (("laisse mains libres", "hands free leash"), "Laisse mains libres pour chien", "hands free dog leash for running hiking"),
            (("laisse ceinture", "waist leash"), "Laisse-ceinture pour canicross", "hands free waist dog leash for canicross"),
            (("laisse double", "2 chiens", "two dog", "twincross"), "Laisse double pour deux chiens", "double dog bungee leash coupler for running"),
            (("double mousqueton",), "Laisse à double mousqueton pour chien", "double ended dog leash with two carabiners"),
            (("laisse 3 positions",), "Laisse multiposition pour chien", "three position adjustable dog walking leash"),
            (("laisse lumineuse",), "Laisse lumineuse pour chien", "LED illuminated dog leash for night walking"),
            (("laisse parapluie",), "Laisse parapluie pour chien", "dog umbrella leash for rainy walks"),
            (("laisse pour jogging",), "Laisse de jogging pour chien", "hands free dog jogging leash with shock absorber"),
            (("laisse en metal", "laisse chaine"), "Laisse chaîne métallique pour chien", "metal chain dog leash for strong dogs"),
            (("corde escalade",), "Laisse en corde d’escalade pour chien", "climbing rope dog leash with locking carabiner"),
            (("corde tressee",), "Laisse en corde tressée pour chien", "braided rope dog walking leash"),
            (("laisse lasso avec frein",), "Laisse lasso avec frein pour chien", "slip lead dog leash with stopper brake"),
            (("laisse lasso avec securite",), "Laisse lasso sécurisée pour chien", "safety locking slip lead dog leash"),
            (("laisse lasso",), "Laisse lasso pour chien", "rope slip lead dog leash for training"),
            (("laisse biothane", "laisse lasso biothane"), "Laisse en Biothane pour chien", "waterproof biothane dog leash for outdoor use"),
            (("laisse tactique",), "Laisse tactique pour chien", "heavy duty tactical dog leash with control handle"),
            (("laisse enrouleur", "retractable leash"), "Laisse enrouleur pour chien", "heavy duty retractable dog walking leash"),
            (("longe", "long line"), "Longe de promenade pour chien", "long dog training leash for outdoor recall"),
            (("laisse canicross", "bungee leash", "bungee line", "crosstrail"), "Laisse amortissante de canicross", "shock absorbing bungee dog leash for canicross"),
            (("laisse", "leash"), "Laisse de promenade pour chien", "durable dog walking leash for outdoor use"),
            (("collier haute visibilite", "reflective collar", "visibility collar"), "Collier haute visibilité pour chien", "reflective high visibility dog collar for night walking"),
            (("collier lumineux", "lumiere collier", "led collar"), "Collier lumineux LED pour chien", "waterproof LED dog collar for night walking"),
            (("collier airtag",), "Collier avec support AirTag pour chien", "dog collar with secure tracker holder"),
            (("collier anti aboiement spray", "citronnelle"), "Collier anti-aboiement à spray pour chien", "citronella spray anti bark dog collar"),
            (("collier anti aboiement",), "Collier anti-aboiement pour chien", "vibration sound anti bark dog collar"),
            (("collier de dressage", "collier education"), "Collier de dressage à distance pour chien", "remote dog training collar for outdoor recall"),
            (("collier licol",), "Collier licol pour chien", "dog head halter collar for no pull walking"),
            (("collier anti-stress",), "Collier apaisant pour chien", "calming pheromone dog collar for travel"),
            (("collier identification", "avec medaille"), "Collier d’identification pour chien", "dog identification collar with name tag"),
            (("collier de chasse", "collier hunter"), "Collier de chasse pour chien", "high visibility waterproof hunting dog collar"),
            (("collier militaire",), "Collier tactique pour chien", "heavy duty tactical dog collar with handle"),
            (("collier biothane",), "Collier en Biothane pour chien", "waterproof biothane dog collar for outdoor use"),
            (("collier en corde",), "Collier en corde pour chien", "braided rope dog collar for walking"),
            (("chaine non etrangleur", "chainette"), "Collier chaîne non étrangleur pour chien", "non choke metal chain dog collar"),
            (("collier d attelage", "mushing collar"), "Collier d’attelage pour chien", "wide padded dog mushing collar for pulling"),
            (("collier anti puce", "collier anti tique"), "Collier répulsif anti-tiques pour chien", "dog flea tick repellent collar for outdoor use"),
            (("collier", "collar"), "Collier outdoor pour chien", "adjustable durable dog collar for hiking walking"),
            (("bottine", "bootie", "bottes", "dog boot"), "Bottines de protection pour chien", "protective dog boots for hiking rough terrain"),
            (("chaussures resistantes",), "Chaussures renforcées pour chien", "durable rubber sole dog hiking shoes"),
            (("chaussure",), "Chaussures de protection pour chien", "protective dog shoes for hot pavement hiking"),
            (("chaussette anti-derap", "anti slip socks"), "Chaussettes antidérapantes pour chien", "anti slip dog socks for paw mobility protection"),
            (("baume patte", "paw balm"), "Baume protecteur pour coussinets de chien", "dog paw protection balm for snow hot pavement"),
            (("protector snow",), "Protection neige pour chien", "snow protection suit for dog outdoor hiking"),
            (("manteau chaud", "winter coat"), "Manteau chaud pour chien", "insulated winter dog coat for outdoor walking"),
            (("impermeable", "raincoat", "kway"), "Imperméable pour chien", "waterproof reflective dog raincoat for walking"),
            (("veste haute visibilite", "high visibility vest"), "Gilet haute visibilité pour chien", "reflective high visibility dog safety vest for hunting walking"),
            (("veste de chasse", "camouflage vest"), "Gilet de protection de chasse pour chien", "high visibility protective dog hunting vest"),
            (("cooling vest", "rafraichissant", "swamp cooler"), "Gilet rafraîchissant pour chien", "evaporative cooling dog vest for hot weather hiking"),
            (("drying coat", "peignoir", "sechant"), "Manteau séchant pour chien", "microfiber dog drying coat after outdoor activity"),
            (("manteau", "jacket", "vest", "coat"), "Manteau outdoor pour chien", "weather resistant dog outdoor coat for walking"),
            (("tapis froid",), "Tapis rafraîchissant outdoor pour chien", "cooling dog mat for travel outdoor use"),
            (("tapis chauffant chien exterieur",), "Tapis chauffant outdoor pour chien", "weatherproof heated dog mat for outdoor shelter"),
            (("tapis chien exterieur",), "Tapis imperméable outdoor pour chien", "waterproof foldable dog mat for camping"),
            (("bandage", "first aid"), "Kit de premiers secours pour chien", "portable dog first aid kit for hiking travel"),
            (("ecran solaire", "sunfree", "sunscreen"), "Protection solaire pour chien", "dog skin sunscreen balm for outdoor exposure"),
            (("insectifuge", "acarifuge", "insect repellent"), "Spray répulsif insectes et tiques pour chien", "dog insect tick repellent spray for hiking"),
            (("tire tique", "tick remover"), "Tire-tique pour chien", "stainless steel tick remover tool for dog travel kit"),
            (("spray rehydratant", "moisturizing spray"), "Spray hydratant cutané pour chien", "dog skin moisturizing spray after outdoor activity"),
            (("lampe", "led light"), "Lampe de sécurité pour collier de chien", "waterproof LED dog collar safety light for night walking"),
            (("mousqueton", "carabiner"), "Mousqueton de sécurité pour laisse de chien", "locking aluminum carabiner for dog leash outdoor use"),
        ]
        fr_base, en_base = first_rule(rules)
        if not fr_base:
            return "", ""
        raw_for_features = raw
        raw = title_raw
        fr_mod, en_mod = feature_pairs(
            [
                (("cuir", "leather"), "en cuir", "leather"),
                (("caoutchouc", "rubber"), "en caoutchouc", "rubber"),
                (("neoprene",), "en néoprène", "neoprene"),
                (("nylon",), "en nylon", "nylon"),
                (("silicone",), "en silicone", "silicone"),
                (("inox", "stainless"), "en acier inoxydable", "stainless steel"),
                (("biothane",), "en Biothane", "waterproof biothane"),
                (("corde", "rope"), "en corde", "rope"),
                (("chaine", "metal"), "en métal", "metal chain"),
                (("tresse", "braided"), "tressé", "braided"),
                (("molleton", "rembourre", "padded"), "rembourré", "padded"),
                (("souple", "soft"), "souple", "soft"),
                (("ergonom",), "ergonomique", "ergonomic"),
                (("fluorescent", "fluo"), "fluorescent", "fluorescent"),
                (("isotherme", "insulated"), "isotherme", "insulated"),
                (("pliable", "foldable"), "pliable", "foldable"),
                (("anti derap",), "antidérapant", "anti slip"),
                (("reflech", "haute visibilite", "visibility"), "réfléchissant", "reflective high visibility"),
                (("impermeable", "waterproof", "kway"), "imperméable", "waterproof"),
                (("ajustable", "reglable", "adjustable"), "réglable", "adjustable"),
                (("bungee", "amortiss", "shock absorbing"), "amortissant", "shock absorbing"),
                (("poignee", "handle"), "avec poignée", "with control handle"),
                (("leger", "lightweight"), "léger", "lightweight"),
            ]
        )
        raw = raw_for_features
        fr_mod = [item for item in fr_mod if item.lower() not in fr_base.lower()]
        en_mod = [item for item in en_mod if item.lower() not in en_base.lower()]
        if "visibilité" in fr_base:
            fr_mod = [item for item in fr_mod if item != "réfléchissant"]
        if "Tente légère" in fr_base:
            fr_mod = [item for item in fr_mod if item != "léger"]
        if any(x in fr_base for x in ["chaîne", "métallique"]):
            fr_mod = [item for item in fr_mod if item != "en métal"]
        fr = " ".join([fr_base, *fr_mod]).strip()
        en = " ".join([en_base, *en_mod]).strip()
        return fr, en

    proprietary = [
        "rotor", "impeller", "transformateur", "transfo", "ballast", "clips fermeture",
        "service kit", "kit accessoire pour", "lampe de rechange", "ampoule de rechange",
        "cartouches de remplacement", "moteur", "reducteur", "couvercle", "piece de drainage",
        "de rechange", "remplacement", "replacement", "membrane ", "reglette de remplacement",
        "kit de conversion",
    ]
    if any(term in raw for term in proprietary):
        return "", ""
    blocked = [
        "in vitro", "plante en pot", "plante mere", "bulbe de plante", "projet de hardscape",
        "terrarium", "reptile", "poisson aquarium", "crevettes pour aquarium", "sauvage", "bassin",
        "bache pvc", "epdm",
    ]
    if any(term in raw for term in blocked):
        return "", ""
    rules = [
        (("anti retour", "check valve"), "Clapet anti-retour pour circuit CO₂ d’aquarium", "aquarium CO2 check valve for tubing"),
        (("electrovanne", "solenoid"), "Électrovanne pour système CO₂ d’aquarium", "aquarium CO2 solenoid valve with timer"),
        (("recharge drop checker", "recharge pour drop checker"), "Solution de recharge pour drop checker CO₂", "aquarium CO2 drop checker refill solution"),
        (("drop checker",), "Drop checker CO₂ en verre pour aquarium", "glass aquarium CO2 drop checker kit"),
        (("bouteille co2 jetable", "co2 jetable"), "Bouteille jetable de CO₂ pour aquarium", "disposable aquarium CO2 cylinder"),
        (("bouteille co2 rechargeable",), "Bouteille rechargeable de CO₂ pour aquarium", "refillable aquarium CO2 cylinder"),
        (("bouteille co2",), "Bouteille de CO₂ pour aquarium", "aquarium CO2 cylinder"),
        (("detendeur", "regulator"), "Détendeur de pression CO₂ pour aquarium", "dual gauge aquarium CO2 pressure regulator"),
        (("diffuseur co2",), "Diffuseur CO₂ en céramique pour aquarium", "ceramic aquarium CO2 diffuser"),
        (("compte bulle",), "Compte-bulles CO₂ pour aquarium", "glass aquarium CO2 bubble counter"),
        (("co2 splitter", "raccords 4 voies"), "Répartiteur multi-voies pour circuit CO₂", "multi outlet aquarium CO2 splitter manifold"),
        (("adaptateur co2", "co2 adaptor", "adaptateur bouteille"), "Adaptateur de bouteille CO₂ pour aquarium", "aquarium CO2 cylinder thread adapter"),
        (("extender", "bloc d extension"), "Bloc d’extension pour détendeur CO₂", "aquarium CO2 regulator extension manifold"),
        (("reactor kit", "reacteur co2"), "Réacteur générateur de CO₂ pour aquarium", "aquarium CO2 reactor generator kit"),
        (("carbonator recharge",), "Recharge pour générateur biologique de CO₂", "biological aquarium CO2 generator refill powder"),
        (("carbonator", "generateur de co2"), "Générateur biologique de CO₂ pour aquarium", "biological aquarium CO2 generator system"),
        (("oxydator", "oxygenator"), "Oxydateur sans électricité pour aquarium", "non electric aquarium oxygenator device"),
        (("kit co2",), "Kit CO₂ complet pour aquarium planté", "complete aquarium CO2 kit for planted tank"),
        (("capsules", "nutri caps", "root tabs", "tablets", "comprime"), "Capsules d’engrais racinaire pour aquarium", "aquarium plant root fertilizer tablets capsules"),
        (("engrais macro", "macro-nutriments", "npk"), "Engrais macronutriments NPK pour aquarium", "aquarium plant macro nutrient NPK fertilizer"),
        (("engrais micro", "micro-nutriments"), "Engrais micronutriments pour aquarium", "aquarium plant micro nutrient fertilizer"),
        (("iron", "ferro", "plant care fe"), "Engrais fer pour plantes d’aquarium", "aquarium plant iron fertilizer"),
        (("potassium", "plant care k"), "Engrais potassium pour plantes d’aquarium", "aquarium plant potassium fertilizer"),
        (("phosphate", "phospho"), "Engrais phosphate pour plantes d’aquarium", "aquarium plant phosphate fertilizer"),
        (("nitrate", "nitro", "plant care n"), "Engrais azote pour plantes d’aquarium", "aquarium plant nitrogen nitrate fertilizer"),
        (("carbone liquide", "liquid carbon", "carbo care"), "Carbone liquide pour aquarium planté", "liquid carbon supplement for aquarium plants"),
        (("all in one",), "Engrais tout-en-un pour aquarium planté", "all in one aquarium plant fertilizer"),
        (("daily fertilizer", "pro daily"), "Engrais quotidien pour aquarium planté", "daily aquarium plant fertilizer"),
        (("engrais liquide", "liquid fertilizer"), "Engrais liquide pour plantes d’aquarium", "liquid aquarium plant fertilizer for planted tank"),
        (("engrais", "fertiliser", "fertilizer", "plant system"), "Engrais pour plantes d’aquarium", "aquarium plant fertilizer for planted aquascape"),
        (("filtre externe avec chauffage",), "Filtre externe avec chauffage intégré", "external canister aquarium filter with integrated heater"),
        (("filtre externe connecte", "filtre externe electronique"), "Filtre externe connecté pour aquarium", "smart WiFi electronic canister aquarium filter"),
        (("filtre externe", "external filter", "canister"), "Filtre externe pour aquarium", "external canister aquarium filter"),
        (("filtre interne", "internal filter", "unifilter"), "Filtre interne pour aquarium", "submersible internal aquarium filter"),
        (("filtre cascade", "hang on filter"), "Filtre cascade pour aquarium", "hang on back aquarium filter"),
        (("filtre exhausteur double",), "Filtre exhausteur double pour aquarium", "dual sponge aquarium filter for shrimp tank"),
        (("filtre exhausteur", "exhausteur", "sponge filter"), "Filtre exhausteur pour aquarium", "air driven sponge aquarium filter"),
        (("filtre uv", "uv filter"), "Filtre UV pour aquarium", "UV sterilizer aquarium filter"),
        (("skimmer",), "Skimmer de surface pour aquarium", "aquarium surface skimmer filter"),
        (("mousse filtrante", "filter foam", "mousse pour exhausteur"), "Mousse filtrante découpable pour aquarium", "cut to fit aquarium filter foam pad"),
        (("tourbe", "peat"), "Média filtrant en tourbe pour aquarium", "aquarium peat filter media pads"),
        (("zeolite", "zeolithe"), "Zéolite pour filtration d’aquarium", "natural zeolite aquarium filter media"),
        (("pouzzolane",), "Pouzzolane pour filtration biologique d’aquarium", "volcanic lava rock aquarium biological filter media"),
        (("purigen", "purificateur d eau organique"), "Résine purificatrice organique pour aquarium", "organic waste adsorbing aquarium filter resin"),
        (("ceramique de filtration", "ceramic filter"), "Média filtrant céramique pour aquarium", "porous ceramic aquarium biological filter media"),
        (("charbon actif", "activated carbon", "carbomec"), "Charbon actif pour filtration d’aquarium", "activated carbon aquarium filter media"),
        (("resine filtrante", "filter resin"), "Résine filtrante pour aquarium", "aquarium filter resin media pouch"),
        (("media filtrant", "masses filtrantes", "hyper pore", "prime pore"), "Média filtrant biologique poreux pour aquarium", "porous biological aquarium filter media"),
        (("perlon", "filter wool"), "Ouate filtrante pour aquarium", "aquarium filter wool floss pad"),
        (("canne d aspiration en verre", "glass intake"), "Canne d’aspiration en verre pour filtre d’aquarium", "glass aquarium filter intake pipe"),
        (("lily", "poppy", "violet", "jet pipe"), "Rejet en verre pour filtre d’aquarium", "glass aquarium filter lily outflow pipe"),
        (("raccord t",), "Raccord en T pour tuyau d’aquarium", "T shape aquarium hose connector fitting"),
        (("raccord y",), "Raccord en Y pour tuyau d’aquarium", "Y shape aquarium hose connector fitting"),
        (("coude pour tuyau",), "Coude pour tuyau d’aquarium", "elbow aquarium hose connector fitting"),
        (("connecteur pour tuyau",), "Connecteur droit pour tuyau d’aquarium", "straight aquarium hose connector fitting"),
        (("filet de filtration", "filter bag"), "Sac filet pour média filtrant d’aquarium", "mesh aquarium filter media bag"),
        (("pompe doseuse", "dosing pump"), "Pompe doseuse programmable pour aquarium", "programmable aquarium dosing pump"),
        (("pompe a air haute pression", "high pressure"), "Pompe à air haute pression pour aquarium", "high pressure aquarium air pump"),
        (("piezo", "piezo air"), "Pompe à air piézoélectrique silencieuse", "ultra quiet piezo aquarium air pump"),
        (("air-flow 4", "4 sorties", "four outlet"), "Pompe à air quatre sorties pour aquarium", "four outlet aquarium air pump"),
        (("12v",), "Pompe à air 12 V pour aquarium", "12V DC aquarium air pump"),
        (("pompe a air", "air pump"), "Pompe à air silencieuse pour aquarium", "quiet aquarium air pump"),
        (("pompe wifi", "pompe connectee", "wifi avec controleur", "wifi avec contrôleur"), "Pompe à eau connectée avec contrôleur", "WiFi controllable aquarium water pump"),
        (("pompe de brassage", "brassage", "wavemaker"), "Pompe de brassage pour aquarium", "aquarium circulation wavemaker pump"),
        (("pompe a eau", "water pump", "pompe submersible"), "Pompe à eau submersible pour aquarium", "submersible aquarium water pump"),
        (("wifi gateway", "controleur led"), "Contrôleur WiFi pour éclairage LED d’aquarium", "WiFi aquarium LED light controller dimmer"),
        (("spot",), "Spot LED pour aquarium", "full spectrum aquarium LED spotlight"),
        (("cable de suspension", "câble de suspension"), "Kit de suspension pour rampe LED d’aquarium", "adjustable suspension cable kit for aquarium LED light"),
        (("wrgb",), "Rampe LED WRGB pour aquarium planté", "WRGB full spectrum aquarium planted tank light"),
        (("lumiere naturelle", "daylight"), "Rampe LED lumière naturelle pour aquarium", "natural daylight aquarium LED light"),
        (("rampe etanche", "waterproof"), "Rampe LED étanche pour aquarium", "waterproof aquarium LED light bar"),
        (("suspension", "suspendue"), "Rampe LED suspendue pour aquarium", "suspended aquarium LED light fixture"),
        (("nano led", "nanocubic"), "Rampe LED pour nano-aquarium", "compact nano aquarium LED light"),
        (("controleur led",), "Contrôleur programmable pour éclairage LED d’aquarium", "programmable aquarium LED light controller dimmer"),
        (("rampe led", "led light", "eclairage", "aquasky", "aqualighter", "twinstar light"), "Rampe LED pour aquarium planté", "full spectrum aquarium LED light for planted tank"),
        (("chauffage titane",), "Chauffage en titane pour aquarium", "titanium aquarium heater with external thermostat"),
        (("chauffage externe", "flow heater"), "Chauffage externe en ligne pour aquarium", "inline external aquarium water heater"),
        (("chauffage connecte",), "Chauffage connecté pour aquarium", "smart connected aquarium heater"),
        (("day & night",), "Chauffage jour-nuit pour aquarium", "day night programmable aquarium heater"),
        (("thermopreset", "heater constant", "chauffage constant"), "Chauffage préréglé pour aquarium", "preset fixed temperature aquarium heater"),
        (("chauffage pour sol", "substrate heater"), "Câble chauffant de sol pour aquarium", "aquarium substrate heating cable"),
        (("heater cover", "cache chauffage"), "Protection pour chauffage d’aquarium", "aquarium heater protective guard cover"),
        (("chauffage", "heater"), "Chauffage réglable pour aquarium", "adjustable aquarium water heater with thermostat"),
        (("thermostat", "t-controller", "t controler"), "Thermostat numérique pour aquarium", "digital dual probe aquarium temperature controller thermostat"),
        (("ventilateur", "cool breeze"), "Ventilateur de refroidissement pour aquarium", "adjustable aquarium cooling fan"),
        (("thermometre",), "Thermomètre numérique pour aquarium", "digital aquarium thermometer"),
        (("test en goutte",), "Test d’eau en gouttes pour aquarium", "liquid reagent aquarium water test kit"),
        (("test bandelette",), "Bandelettes de test d’eau pour aquarium", "multi parameter aquarium water test strips"),
        (("test electronique", "conductiv", "tds meter"), "Testeur électronique d’eau pour aquarium", "digital TDS conductivity pH aquarium water tester"),
        (("remineralisation", "mineral gh"), "Sels de reminéralisation pour aquarium à crevettes", "shrimp aquarium remineralizing mineral salts GH"),
        (("test",), "Test d’eau pour aquarium", "freshwater aquarium water test kit"),
        (("osmolateur", "smart ato"), "Osmolateur automatique pour aquarium", "automatic aquarium water top off ATO system"),
        (("cartouche osmoseur",), "Cartouche rechargeable pour osmoseur d’aquarium", "refillable reverse osmosis filter cartridge for aquarium"),
        (("osmoseur",), "Osmoseur pour aquarium", "reverse osmosis water filter system for aquarium"),
        (("aspirateur de surface", "surface vacuum"), "Skimmer de surface pour aquarium", "aquarium surface skimmer filter"),
        (("aspirateur", "gravel vacuum"), "Aspirateur de fond pour aquarium", "battery aquarium gravel vacuum cleaner"),
        (("raclette", "algae scraper"), "Raclette anti-algues pour aquarium", "stainless steel aquarium algae scraper"),
        (("aimant", "magnetic cleaner"), "Nettoyeur magnétique de vitres d’aquarium", "magnetic aquarium glass algae cleaner"),
        (("brosse",), "Brosse de nettoyage pour aquarium", "aquarium filter pipe cleaning brush set"),
        (("epuisette",), "Épuisette à mailles fines pour aquarium", "fine mesh aquarium shrimp fish net"),
        (("ciseaux courbe", "curved scissors", "ciseaux incurve"), "Ciseaux courbés d’aquascaping", "curved stainless steel aquascaping scissors"),
        (("spring scissors", "spring cut", "ciseaux a ressort"), "Ciseaux à ressort d’aquascaping", "spring stainless steel aquascaping scissors"),
        (("ciseaux vague", "wave scissors"), "Ciseaux ondulés d’aquascaping", "wave stainless steel aquascaping scissors"),
        (("ciseaux", "scissors"), "Ciseaux d’aquascaping en acier inoxydable", "stainless steel aquascaping scissors"),
        (("pince courbee",), "Pince courbée d’aquascaping en acier inoxydable", "curved stainless steel aquascaping tweezers"),
        (("pince", "tweezers"), "Pince droite d’aquascaping en acier inoxydable", "straight stainless steel aquascaping tweezers"),
        (("double spatule",), "Spatule double pour nivellement de substrat", "double ended aquascaping substrate spatula"),
        (("epingle", "plantis"), "Épingles de fixation pour plantes d’aquarium", "stainless aquarium plant anchor pins"),
        (("tool support", "rangement pour outils"), "Support pour outils d’aquascaping", "acrylic aquascaping tool holder rack"),
        (("aquarium divider", "separateur aquarium"), "Séparateur réglable pour aquarium", "adjustable aquarium tank divider panel"),
        (("kit de nettoyage", "care set"), "Kit multi-outils de nettoyage d’aquarium", "multi function aquarium cleaning tool kit"),
        (("cloche de nettoyage", "gravel clean"), "Cloche siphon de nettoyage pour aquarium", "aquarium gravel siphon cleaning bell"),
        (("gravel scoop", "pelle a gravier"), "Pelle à substrat pour aquarium", "aquarium substrate gravel leveling scoop"),
        (("tuyau d air",), "Tuyau à air en silicone pour aquarium", "silicone aquarium air hose tubing"),
        (("tuyau", "hose"), "Tuyau souple pour aquarium", "flexible clear aquarium water hose tubing"),
        (("robinet simple", "air valve"), "Robinet de réglage pour tuyau à air d’aquarium", "aquarium air hose flow control valve"),
        (("ventouse", "suction cup"), "Ventouse de fixation pour aquarium", "aquarium hose heater suction cup holder"),
            (("scaping foam", "mousse expansive"), "Mousse expansive pour hardscape d’aquarium", "aquarium safe expanding foam for hardscape"),
            (("ruban d etancheite", "ptfe"), "Ruban PTFE pour raccords d’aquarium", "PTFE thread seal tape for aquarium hose fittings"),
            (("colle silicone",), "Silicone d’étanchéité pour aquarium", "aquarium safe silicone sealant"),
            (("colle", "glue"), "Colle cyanoacrylate pour aquascaping", "aquarium safe cyanoacrylate glue for aquascaping"),
        (("silicone",), "Silicone d’étanchéité pour aquarium", "aquarium safe silicone sealant"),
        (("sand waterfall", "cascade de sable"), "Cascade de sable décorative pour aquarium", "aquarium sand waterfall aquascaping decoration"),
        (("sable de quartz", "quartz sand"), "Sable de quartz pour aquarium", "quartz aquarium sand substrate"),
        (("basalte", "basalt"), "Gravier basaltique pour aquarium", "natural basalt aquarium gravel substrate"),
        (("dolomite",), "Gravier dolomitique pour aquarium", "natural dolomite aquarium gravel substrate"),
        (("pouzzolane",), "Pouzzolane volcanique pour aquarium", "volcanic lava rock aquarium substrate"),
        (("biotope mix", "riverbed", "river bed"), "Mélange biotope de rivière pour aquarium", "natural riverbed biotope aquarium substrate mix"),
        (("soil small", "flora base pro fin"), "Sol technique à granulométrie fine pour aquarium", "fine grain active soil aquarium plant substrate"),
        (("flora base pro gros",), "Sol technique à granulométrie grossière pour aquarium", "coarse grain active soil aquarium plant substrate"),
        (("sol technique", "active soil", "black soil"), "Sol technique actif pour aquarium", "active soil aquarium plant shrimp substrate"),
        (("akadama",), "Substrat akadama pour aquarium", "akadama aquarium shrimp substrate"),
        (("sable",), "Sable décoratif pour aquarium", "washed aquarium sand substrate"),
        (("gravier",), "Gravier décoratif pour aquarium", "natural aquarium gravel substrate"),
        (("substrat nutritif", "nutrient substrate"), "Substrat nutritif pour aquarium planté", "nutrient rich aquarium plant substrate"),
        (("substrat", "soil"), "Substrat pour aquarium planté", "aquarium plant substrate for aquascaping"),
        (("racine", "driftwood"), "Racine naturelle pour aquascaping", "natural aquarium driftwood hardscape"),
        (("bonsai", "bonsaï"), "Bonsaï en bois pour aquascaping", "natural aquarium bonsai driftwood hardscape"),
        (("dragon rock",), "Dragon stone pour aquascaping", "natural dragon stone aquarium hardscape"),
        (("lava rock",), "Roche volcanique pour aquascaping", "natural volcanic lava rock aquarium hardscape"),
        (("tunnel",), "Tunnel de refuge pour aquarium", "ceramic aquarium fish shrimp tunnel shelter"),
        (("labyrinth", "labyrinthe"), "Labyrinthe refuge pour crevettes d’aquarium", "ceramic shrimp labyrinth shelter aquarium"),
        (("amphore",), "Amphore refuge pour aquarium", "aquarium safe resin amphora cave decoration"),
        (("statue", "bouddha"), "Statue décorative pour aquarium", "aquarium safe resin statue aquascaping decor"),
        (("roche", "pierre", "rock", "stone"), "Roche naturelle pour aquascaping", "natural aquarium rock stone hardscape"),
        (("noix de coco",), "Cachette en noix de coco pour aquarium", "natural coconut aquarium shrimp cave"),
        (("cachette", "shelter", "cave"), "Cachette pour crevettes d’aquarium", "ceramic aquarium shrimp shelter cave"),
        (("decoration", "decor ", "deco "), "Décoration en résine pour aquarium", "aquarium safe resin aquascaping decoration"),
        (("distributeur automatique", "automatic fish feeder", "bettamatic"), "Distributeur automatique de nourriture pour aquarium", "automatic aquarium fish feeder"),
        (("autofeeder+", "distributeur automatique wifi"), "Distributeur de nourriture connecté pour aquarium", "WiFi smart automatic aquarium fish feeder"),
        (("twinfeeder",), "Distributeur double compartiment pour aquarium", "dual chamber automatic aquarium fish feeder"),
        (("tube de nourrissage",), "Tube de nourrissage avec coupelle pour aquarium", "glass aquarium shrimp feeding tube with dish"),
        (("anneau de nourrissage",), "Anneau de nourrissage pour aquarium", "floating aquarium fish feeding ring"),
        (("cone de nourrissage", "cône de nourrissage"), "Cône de nourrissage pour aquarium", "aquarium live food feeding cone"),
        (("pipette",), "Pipette de nourrissage pour aquarium", "long aquarium coral fish feeding pipette"),
        (("tamis",), "Tamis à nourriture pour aquarium", "fine mesh aquarium food sieve"),
        (("distributeur de nourriture", "feeding glass", "food glass"), "Distributeur manuel de nourriture pour aquarium", "manual aquarium feeding dish"),
        (("lollies",), "Bâtonnets alimentaires pour crevettes d’aquarium", "shrimp food lollies sticks for aquarium"),
        (("flakes", "flocons"), "Nourriture en flocons pour poissons d’aquarium", "aquarium fish food flakes"),
        (("shrimp pellet",), "Nourriture en granulés pour crevettes d’aquarium", "aquarium shrimp food pellets"),
        (("pellet", "granule"), "Nourriture en granulés pour poissons d’aquarium", "aquarium fish food pellets"),
        (("shrimp food", "shrimp snack", "shrimp baby", "shrimp dinner", "mineral junkie", "feed for crayfish", "csf crabs"), "Nourriture pour crevettes d’aquarium", "aquarium shrimp food complete diet"),
        (("nourriture", "food", "snack", "bites"), "Nourriture pour poissons d’aquarium", "aquarium fish food complete diet"),
        (("breeding box", "pondoir"), "Pondoir filet pour aquarium", "mesh aquarium breeder box"),
        (("artemia breeder set", "artemia breeder"), "Éclosoir à artémias pour aquarium", "aquarium brine shrimp artemia hatchery kit"),
        (("spawning cone", "cone de ponte"), "Cône de ponte pour poissons d’aquarium", "ceramic aquarium fish spawning cone"),
        (("snail safe", "barriere anti-fuite"), "Barrière anti-fuite pour escargots d’aquarium", "aquarium snail escape barrier treatment"),
        (("bacterie", "bacter ", "bioprobiotic"), "Bactéries de démarrage pour aquarium", "beneficial bacteria starter treatment for aquarium"),
        (("conditionneur", "water conditioner"), "Conditionneur d’eau pour aquarium", "aquarium tap water conditioner dechlorinator"),
        (("anti algue", "protection contre les algues"), "Traitement anti-algues pour aquarium", "aquarium algae control treatment"),
        (("tapis", "garden matt"), "Tapis de nivellement pour aquarium", "foam aquarium tank leveling mat"),
        (("bords incurves", "optibent"), "Aquarium en verre à façade incurvée", "curved front ultra clear glass aquarium tank"),
        (("shrimp set",), "Nano-aquarium équipé pour crevettes", "complete nano shrimp aquarium tank kit"),
        (("cube set", "glossy cube"), "Aquarium cube équipé avec LED", "complete glass cube aquarium tank with LED"),
        (("extra-clair", "ultra clear"), "Aquarium en verre extra-clair", "ultra clear rimless glass aquarium tank"),
        (("filtration interne",), "Aquarium équipé avec filtration interne", "complete aquarium tank with internal filter"),
        (("aquarium avec meuble", "meuble"), "Meuble support pour aquarium", "reinforced aquarium cabinet stand"),
    ]
    fr_base, en_base = first_rule(rules)
    if not fr_base and (
        "rimless tank" in title_raw
        or (
            "aquarium" in title_raw
            and "pour aquarium" not in title_raw
            and bool(re.search(r"\b(?:litre|litres|l|cm|nano|cube)\b", title_raw))
        )
    ):
        fr_base, en_base = (
            "Aquarium en verre",
            "glass aquarium tank",
        )
    if not fr_base:
        return "", ""
    fr_mod, en_mod = [], []
    if "rgb" in title_raw and "Rampe LED" in fr_base:
        fr_mod.append("RGB")
        en_mod.append("RGB")
    if any(x in title_raw for x in ["uv ", "uvc", " uv-"]) and "Filtre" in fr_base:
        fr_mod.append("avec UV")
        en_mod.append("with UV sterilization")
    if any(x in title_raw for x in ["crevette", "shrimp"]) and any(
        x in fr_base for x in ["Filtre exhausteur", "Substrat", "Pondoir", "Cachette", "Épuisette"]
    ):
        fr_mod.append("pour bac à crevettes")
        en_mod.append("for shrimp tank")
    if "avec chauffage" in title_raw and "Filtre externe" in fr_base:
        fr_mod.append("avec chauffage intégré")
        en_mod.append("with integrated heater")
    if "double manometre" in title_raw and "Détendeur" in fr_base:
        fr_mod.append("à double manomètre")
        en_mod.append("dual gauge")
    if "electrovanne" in title_raw and "Détendeur" in fr_base:
        fr_mod.append("avec électrovanne")
        en_mod.append("with solenoid valve")
    if "inline" in title_raw and "Diffuseur" in fr_base:
        fr_mod.append("en ligne")
        en_mod.append("inline")
    if any(x in title_raw for x in ["inox", "acier inoxydable", "stainless"]) and "Diffuseur" in fr_base:
        fr_mod.append("en acier inoxydable")
        en_mod.append("stainless steel")
    if "3-en-1" in title_raw and "Diffuseur" in fr_base:
        fr_mod.append("trois-en-un")
        en_mod.append("three in one")
    if any(x in title_raw for x in ["maille fine", "fine foam"]) and "Mousse filtrante" in fr_base:
        fr_mod.append("à maille fine")
        en_mod.append("fine pore")
    if "wifi" in title_raw and "WiFi" not in fr_base and any(x in fr_base for x in ["Pompe", "Chauffage", "Distributeur", "Contrôleur"]):
        fr_mod.append("connecté WiFi")
        en_mod.append("WiFi smart control")
    fr_mod = [item for item in fr_mod if item.lower() not in fr_base.lower()]
    en_mod = [item for item in en_mod if item.lower() not in en_base.lower()]
    return " ".join([fr_base, *fr_mod]).strip(), " ".join([en_base, *en_mod, "freshwater aquascaping"]).strip()


def concept_from_candidate(candidate):
    value, _ = generic_product(candidate)
    return value[:160]


def canonical_key(concept: str, niche: str) -> str:
    value = remove_accents(concept.lower())
    value = value.replace("&", " ")
    value = re.sub(r"[^a-z0-9]+", " ", value)
    value = re.sub(r"\b(pour|de|du|des|le|la|les|un|une|et|avec|sans|en|a|the|for|dog|chien|aquarium|pas|cher)\b", " ", value)
    value = re.sub(
        r"\b(petit|petite|grand|grande|gros|chiot|chihuahua|boxer|cocker|spaniel|border|collie|"
        r"bouledogue|francais|berger|allemand|moyen|xxs|xs|xl|xxl)\b",
        " ", value,
    )
    value = re.sub(r"\b(?:v|mk|version)\s*\d+\b", " ", value)
    value = re.sub(r"\b\d+\b", " ", value)
    value = re.sub(r"\b([a-z]{5,})s\b", r"\1", value)
    value = re.sub(r"\s+", " ", value).strip()
    if niche == "chien":
        if "snood" in value and "cocker" in value:
            return "snood cocker impermeable" if "impermeable" in value else "snood cocker"
        if "tire tique" in value or "retire tique" in value:
            return "tire tique"
    return value


def _mods(text: str, pairs):
    found = []
    for needles, label in pairs:
        if any(needle in text for needle in needles) and label not in found:
            found.append(label)
    return found


def english_query(candidate, concept: str) -> str:
    """Create a supplier-search query from observed function, material and use.

    Product model names are intentionally omitted. A model-only title therefore
    collapses onto its generic function instead of masquerading as a new concept.
    """
    _, query = generic_product(candidate)
    return query[:180]

    # Legacy token-level fallback retained below for auditability; the generic
    # product mapper above is authoritative and returns before this block.
    raw = remove_accents(
        " ".join(
            [
                candidate.get("competitor_product_title", ""),
                concept,
                candidate.get("competitor_collection", ""),
                " ".join(candidate.get("categories", [])),
                candidate.get("product_type", ""),
            ]
        ).lower()
    )
    raw = re.sub(r"[^a-z0-9+]+", " ", raw)
    raw = re.sub(r"\s+", " ", raw).strip()

    if candidate["niche"] == "chien":
        rules = [
            (("bouton de communication", "communication button"), "recordable dog communication button"),
            (("protege canape", "housse de canape", "protection canape"), "dog sofa cover"),
            (("protection de banquette", "protection voiture", "protege siege"), "dog car back seat protector"),
            (("tapis essuie patte", "tapis absorbant", "tapis patte"), "dog paw drying mat"),
            (("chariot",), "adjustable rear leg dog wheelchair"),
            (("collier anti puce", "collier anti tique"), "dog flea tick repellent collar"),
            (("collier etrangleur",), "dog training choke collar"),
            (("collier", " collar"), "dog collar"),
            (("canape orthoped", "panier orthoped", "couchage orthoped"), "orthopedic dog bed"),
            (("panier", "couchage", "sleeping bag", "tapis de sol"), "outdoor dog bed"),
            (("coupe ongle automatique", "nail grinder"), "electric dog nail grinder"),
            (("coupe ongle",), "dog nail clipper"),
            (("harnais canicross", "x back", "pulling harness"), "dog pulling harness for canicross"),
            (("harnais 3 point",), "escape proof three point dog harness"),
            (("harnais", " harness"), "adjustable dog harness"),
            (("gourde", "water bottle"), "portable dog water bottle"),
            (("porte gamelle",), "portable dog bowl holder"),
            (("gamelle", " bowl"), "collapsible dog travel bowl"),
            (("lanceur de balle",), "automatic dog ball launcher"),
            (("canard",), "duck shaped dog chew toy"),
            (("os indestructible",), "durable dog chew bone toy"),
            (("flying disc", "frisbee"), "dog flying disc toy"),
            (("dog ball on rope", "balle on corde", "balle corde"), "dog ball with rope toy"),
            (("throw toy",), "dog fetch throw toy"),
            (("laisse enrouleur",), "retractable dog leash"),
            (("laisse mains libres",), "hands free dog leash"),
            (("laisse", " leash", "longe"), "dog walking leash"),
            (("manteau", " jacket", "kway"), "weatherproof dog coat"),
            (("peignoir",), "microfiber dog bathrobe"),
            (("sac a dos de transport", "sac de transport", "carrier"), "dog travel carrier backpack"),
            (("sac de bat", "approach pack", "day pack", "palisades pack"), "dog hiking saddle backpack"),
            (("sac a dos", "backpack"), "dog hiking backpack"),
            (("sac a dejection", "dejections biodegradables"), "biodegradable dog waste bags"),
            (("treat bag",), "dog training treat pouch"),
            (("bottes", "bottine", "bootie", "socks"), "dog paw protection boots"),
            (("stylo brosse a dents",), "dog toothbrush pen"),
            (("brosse slicker",), "dog slicker grooming brush"),
            (("brosse epilation",), "dog deshedding brush"),
            (("brosse",), "dog grooming brush"),
            (("chaussette",), "anti slip dog socks"),
            (("clicker et sifflet",), "dog training clicker whistle"),
            (("clicker",), "dog training clicker"),
            (("collerette",), "adjustable dog recovery cone"),
            (("couche menstruelle",), "reusable female dog diaper"),
            (("couche", "culotte"), "washable dog diaper"),
            (("deguisement", "cosplay", "criniere"), "dog costume outfit"),
            (("impermeable", "raincoat"), "waterproof dog raincoat"),
            (("licol",), "dog head halter for walking"),
            (("puzzle",), "dog enrichment puzzle toy"),
            (("snood",), "dog ear protection snood"),
            (("bandana",), "dog bandana"),
            (("ceinture canicross", "baudrier", " belt"), "hands free canicross belt"),
            (("piquet d attache",), "spiral dog tie out stake"),
            (("sonaillon",), "dog hiking safety bell"),
            (("kit cani vtt", "biking kit"), "dog bikejoring kit"),
            (("kit canicross",), "dog canicross harness leash belt kit"),
            (("kit canirando",), "dog hiking harness leash belt kit"),
            (("carabiner", "mousqueton"), "locking carabiner for dog leash"),
            (("masque de protection",), "protective dog goggles"),
            (("insectifuge", "acarifuge"), "dog insect tick repellent spray"),
            (("ecran solaire",), "dog skin sunscreen balm"),
            (("spray rehydratant",), "dog skin moisturizing spray"),
            (("tente",), "lightweight dog camping tent"),
            (("gilet de sauvetage", "life jacket"), "dog life jacket"),
            (("gilet", " vest"), "dog outdoor vest"),
            (("piece de remplacement", "replacement", "buckle", "adapter"), "replacement hardware for dog outdoor gear"),
            (("huile", "omega"), "dog omega fish oil supplement"),
            (("bonnet", "bob ", "casquette", "cagoule"), "dog outdoor hat"),
        ]
        base = next((label for needles, label in rules if any(n in raw for n in needles)), "dog outdoor mobility accessory")
        modifiers = _mods(
            raw,
            [
                (("cuir", "leather"), "leather"),
                (("caoutchouc", "rubber"), "rubber"),
                (("plastique", "plastic"), "plastic"),
                (("microfibre", "microfiber"), "microfiber"),
                (("absorbant",), "absorbent"),
                (("impermeable", "waterproof", "kway"), "waterproof"),
                (("reflech", "haute visibilite", "voyant"), "reflective high visibility"),
                (("anti derap",), "anti slip"),
                (("dehoussable",), "removable washable cover"),
                (("ajustable", "reglable", "adjustable"), "adjustable"),
                (("automatique", "automatic"), "automatic"),
                (("bungee", "elastique"), "shock absorbing bungee"),
                (("hiver", "chaud", "snow"), "winter"),
                (("rafraichissant", "cooling", "swamp cooler"), "cooling"),
                (("randonn", "trekking", "trail"), "for hiking"),
                (("canicross",), "for canicross"),
                (("velo", "vtt", "biking", "bikejoring"), "for bikejoring"),
                (("voiture", "banquette", "car seat"), "for car travel"),
                (("chiot", "puppy"), "for puppies"),
                (("petit chien", "chihuahua"), "for small dogs"),
                (("grand chien", "gros chien", "berger allemand"), "for large dogs"),
            ],
        )
        query = " ".join([base, *modifiers, "outdoor travel training"]).strip()
    else:
        rules = [
            (("anti retour", "check valve"), "aquarium CO2 check valve"),
            (("electrovanne", "solenoid"), "aquarium CO2 solenoid valve"),
            (("recharge drop checker",), "aquarium CO2 drop checker refill solution"),
            (("drop checker",), "glass aquarium CO2 drop checker"),
            (("bouteille co2", "recharges co2", "co2 jetable"), "aquarium CO2 refill cylinder"),
            (("detendeur", "regulator"), "aquarium CO2 pressure regulator"),
            (("diffuseur co2",), "ceramic aquarium CO2 diffuser"),
            (("compte bulle",), "aquarium CO2 bubble counter"),
            (("engrais", "fertiliser", "fertilizer", "plant system"), "aquarium plant fertilizer"),
            (("filtre externe", "external filter", "professionel"), "external canister aquarium filter"),
            (("filtre interne", "unifilter"), "internal aquarium filter"),
            (("filtre cascade", "hang on filter"), "hang on back aquarium filter"),
            (("filtre exhausteur", "exhausteur", "sponge filter"), "air driven aquarium sponge filter"),
            (("filtre uv", "uv power"), "UV aquarium filter"),
            (("mousse filtrante", "mousse pour", "filter foam"), "aquarium filter foam pad"),
            (("ceramique",), "ceramic aquarium filter media"),
            (("charbon actif", "carbomec", "carbon"), "activated carbon aquarium filter media"),
            (("media filtrant", "masses filtrantes", "hyper pore", "prime pore"), "porous biological aquarium filter media"),
            (("rotor", "impeller"), "replacement aquarium pump impeller rotor"),
            (("service kit", "kit accessoire", "set d accessoires"), "aquarium filter maintenance kit"),
            (("clips fermeture",), "replacement aquarium filter locking clip"),
            (("embout tuyau", "connecteur", "manchon"), "aquarium hose connector fitting"),
            (("lampe de rechange uvc", "ampoule uv", "uv tl"), "replacement aquarium UV lamp bulb"),
            (("transformateur", "transfo"), "aquarium LED light power adapter"),
            (("controleur led",), "aquarium LED light controller"),
            (("rampe led", " led ", "eclairage", "aquasky", "twinstar light"), "full spectrum aquarium LED light"),
            (("aquarium avec meuble", "meuble"), "aquarium cabinet stand"),
            (("pompe doseuse", "dosing pump"), "programmable aquarium dosing pump"),
            (("pompe a air",), "quiet aquarium air pump"),
            (("pompe de brassage", "brassage", "wavemaker"), "aquarium circulation wavemaker pump"),
            (("pompe", "aqua power", "multi power"), "submersible aquarium water pump"),
            (("chauffage", "heater"), "adjustable aquarium water heater"),
            (("ventilateur", "cool breeze"), "aquarium cooling fan"),
            (("thermometre",), "digital aquarium thermometer"),
            (("test", "gh+", "mineral gh"), "freshwater aquarium water test kit"),
            (("osmolateur", "smart ato"), "automatic aquarium water top off system"),
            (("osmoseur",), "reverse osmosis water filter for aquarium"),
            (("cartouche osmoseur",), "refillable reverse osmosis filter cartridge"),
            (("distributeur de nourriture", "fish feeder"), "automatic aquarium fish feeder"),
            (("feeding glass", "food glass"), "glass shrimp feeding dish"),
            (("nourriture", "food", "flakes", "snack", "lollies", "bites"), "aquarium shrimp fish food"),
            (("breeding box", "pondoir"), "mesh aquarium breeder box"),
            (("shrimp shelter",), "ceramic aquarium shrimp shelter"),
            (("bacterie", "bacter ", "bioprobiotic"), "aquarium beneficial bacteria treatment"),
            (("anti algue", "protection contre les algues"), "aquarium algae control treatment"),
            (("aspirateur", "vacuum"), "battery aquarium gravel vacuum cleaner"),
            (("epuisette",), "fine mesh aquarium shrimp net"),
            (("ciseaux", "scissors"), "stainless steel aquascaping scissors"),
            (("pince courbee",), "curved stainless steel aquascaping tweezers"),
            (("pince", "tweezers"), "stainless steel aquascaping tweezers"),
            (("gravel scoop",), "aquarium substrate gravel scoop"),
            (("tuyau d air",), "silicone aquarium air hose"),
            (("robinet simple",), "aquarium air hose control valve"),
            (("sable de quartz", "quartz"), "quartz aquarium sand substrate"),
            (("sol technique", "active soil", "black soil"), "active soil aquarium plant substrate"),
            (("akadama",), "akadama aquarium shrimp substrate"),
            (("sable",), "aquarium sand substrate"),
            (("gravier",), "aquarium gravel substrate"),
            (("substrat", "soil"), "aquarium plant substrate"),
            (("racine", "driftwood"), "natural aquarium driftwood hardscape"),
            (("roche", "pierre", "rock", "stone"), "natural aquarium rock hardscape"),
            (("noix de coco",), "natural coconut aquarium shrimp cave"),
            (("decoration", "decor ", "deco "), "resin aquarium aquascaping decoration"),
            (("aimant",), "magnetic aquarium glass cleaner"),
            (("chaufferette", "heat pack"), "disposable heat pack for aquarium livestock transport"),
            (("eau osmosee",), "reverse osmosis water for aquarium"),
            (("tapis", "garden matt"), "foam aquarium tank leveling mat"),
            (("support", "stand"), "adjustable aquarium equipment mounting bracket"),
            (("aquarium", "cuve", "tank"), "ultra clear glass aquarium tank"),
        ]
        base = next((label for needles, label in rules if any(n in raw for n in needles)), "freshwater aquarium maintenance accessory")
        modifiers = _mods(
            raw,
            [
                (("verre", "glass"), "glass"),
                (("acrylic", "acrylique"), "acrylic"),
                (("inox", "stainless"), "stainless steel"),
                (("silicone",), "silicone"),
                (("ceramique", "ceramic"), "ceramic"),
                (("petg",), "PETG"),
                (("nano",), "for nano tank"),
                (("crevette", "shrimp"), "for shrimp tank"),
                (("plante", "aquascape", "aquascaping"), "for planted aquascape"),
                (("eau douce", "freshwater"), "freshwater"),
                (("rgb",), "RGB"),
                (("uv", "uvc"), "UV"),
                (("externe", "external"), "external"),
                (("interne", "internal"), "internal"),
                (("rechange", "replacement"), "replacement part"),
            ],
        )
        query = " ".join([base, *modifiers, "freshwater aquascaping"]).strip()
    return re.sub(r"\s+", " ", query)[:180]


def diverse_order(candidates):
    groups = collections.defaultdict(list)
    for candidate in candidates:
        groups[candidate["competitor_collection"]].append(candidate)
    keys = sorted(groups)
    ordered = []
    while True:
        moved = False
        for key in keys:
            if groups[key]:
                ordered.append(groups[key].pop(0))
                moved = True
        if not moved:
            return ordered


def is_near_duplicate(key: str, existing_keys) -> bool:
    if not key or key in existing_keys:
        return True
    # Exact normalization is primary. A high fuzzy threshold removes SEO aliases
    # without collapsing genuinely different functions/models.
    for other in existing_keys:
        if abs(len(key) - len(other)) > 18:
            continue
        if difflib.SequenceMatcher(None, key, other).ratio() >= 0.94:
            return True
    return False


def select_exact(candidates_by_domain, quotas, niche: str, target: int = 220):
    selected = []
    keys = set()
    leftovers = []

    def try_add(candidate):
        if not candidate_relevant(candidate):
            return False
        concept = concept_from_candidate(candidate)
        key = canonical_key(concept, niche)
        query = english_query(candidate, concept)
        if len(key) < 3 or is_near_duplicate(key, keys):
            return False
        row = {
            "niche": niche,
            "competitor": candidate["competitor"],
            "competitor_domain": candidate["competitor_domain"],
            "competitor_collection": candidate["competitor_collection"],
            "competitor_product_title": candidate["competitor_product_title"],
            "competitor_product_url": candidate["competitor_product_url"],
            "concept_fr_normalized": concept,
            "distinctness_basis": (
                f"Équivalent fonctionnel générique dédupliqué par clé « {key} » ; marque, modèle, "
                "taille, couleur et volume neutralisés. Dérivation limitée au type, à la matière "
                "ou à l’usage explicitement visibles dans le titre/collection source."
            ),
            "keyword_fr_candidate": concept.lower(),
            "aliexpress_query_fr": concept.lower(),
            "aliexpress_query_en": query,
            "evidence_status": "EQUIVALENT_DERIVE",
            "observed_at": OBSERVED_AT,
            "source_url": candidate["source_url"],
        }
        selected.append(row)
        keys.add(key)
        return True

    for domain, quota in quotas.items():
        ordered = diverse_order(candidates_by_domain.get(domain, []))
        count = 0
        for candidate in ordered:
            if count < quota and try_add(candidate):
                count += 1
            else:
                leftovers.append(candidate)

    if len(selected) < target:
        for candidate in diverse_order(leftovers):
            if len(selected) >= target:
                break
            try_add(candidate)

    # Never inflate the corpus to satisfy a quota. The report exposes any
    # shortfall against the 220-concept target.
    return selected


def make_report(rows, raw_sources):
    by_niche = collections.Counter(row["niche"] for row in rows)
    by_competitor = collections.Counter((row["niche"], row["competitor_domain"]) for row in rows)
    by_status = collections.Counter((row["niche"], row["evidence_status"]) for row in rows)
    by_collection = collections.Counter((row["niche"], row["competitor_collection"]) for row in rows)
    lines = [
        "# Expansion catalogue — chien et aquarium",
        "",
        f"**Snapshot** : {OBSERVED_AT}  ",
        "**Périmètre** : catalogues publics concurrents uniquement. Aucun appel SEMrush, Chrome ou AliExpress.",
        "",
        "## Contrôle de sortie",
        "",
        f"- Chien : **{by_niche['chien']} concepts réellement dédupliqués** sur une cible de 220 "
        f"(déficit : **{max(0, 220 - by_niche['chien'])}**).",
        f"- Aquarium : **{by_niche['aquarium']} concepts réellement dédupliqués** sur une cible de 220 "
        f"(déficit : **{max(0, 220 - by_niche['aquarium'])}**).",
        f"- Total : **{len(rows)} concepts**.",
        "- Les variantes uniquement fondées sur couleur, taille, volume ou édition sont neutralisées dans la clé de déduplication.",
        "- Les requêtes AliExpress sont des chaînes de recherche préparatoires ; aucun résultat ou fournisseur AliExpress n'a été consulté.",
        "",
        "## Observé / Dérivé / Manquant",
        "",
        "- **Observé** : le titre concurrent, son URL produit/collection et sa famille catalogue publique.",
        "- **Dérivé** : le concept générique sourceable et les requêtes FR/EN, limités aux fonctions, matières et usages visibles.",
        f"- **Manquant** : {max(0, 220 - by_niche['chien'])} concepts chien et "
        f"{max(0, 220 - by_niche['aquarium'])} concepts aquarium pour atteindre 220 sans gonfler le corpus ; "
        "volumes SEMrush, offre AliExpress exacte, prix rendu France et conformité fournisseur.",
        "",
        "## Répartition par concurrent",
        "",
        "| Niche | Domaine | Concepts retenus |",
        "|---|---|---:|",
    ]
    for (niche, domain), count in sorted(by_competitor.items()):
        lines.append(f"| {niche} | {domain} | {count} |")
    lines += [
        "",
        "## Statut des preuves",
        "",
        "| Niche | Statut | Nombre |",
        "|---|---|---:|",
    ]
    for (niche, status), count in sorted(by_status.items()):
        lines.append(f"| {niche} | {status} | {count} |")
    lines += [
        "",
        "EQUIVALENT_DERIVE signifie que le titre/PDP concurrent a été observé mais que le concept sourceable "
        "a été généricisé par fonction, matière ou usage. Aucun fournisseur ni SKU AliExpress n'est affirmé.",
        "",
        "## Collections les plus représentées",
        "",
        "| Niche | Collection normalisée | Nombre |",
        "|---|---|---:|",
    ]
    for (niche, collection), count in sorted(by_collection.items(), key=lambda x: (x[0][0], -x[1], x[0][1]))[:40]:
        lines.append(f"| {niche} | {collection} | {count} |")
    lines += [
        "",
        "## Méthode de déduplication",
        "",
        "1. Un produit Shopify ou WooCommerce est compté une fois, jamais une fois par variante.",
        "2. Les marques, modèles, mesures, contenances, puissances, tailles, couleurs et mentions d'édition sont neutralisés.",
        "3. Les doublons exacts et quasi-identiques au-dessus d'un seuil de similarité de 94 % sont rejetés.",
        "4. Un modèle propriétaire sans fonction générique distincte n'est pas compté ; le titre source reste conservé ligne par ligne.",
        "5. Les sources sont réparties par collection avant sélection pour éviter un corpus composé d'une seule famille de produits.",
        "",
        "## Sources brutes",
        "",
    ]
    for source in raw_sources:
        lines.append(f"- {source}")
    lines += [
        "",
        "## Limites",
        "",
        "- Les mots-clés sont des candidats sémantiques non mesurés ; volumes et positions restent à enrichir par SEMrush.",
        "- Les requêtes anglaises sont normalisées par glossaire local et doivent être ajustées lors du sourcing.",
        "- Une URL de collection Polytrans remplace certaines URL PDP, le site ayant répondu HTTP 429 au scraper public ; ces lignes sont marquées EQUIVALENT_DERIVE.",
        "- L'existence chez un concurrent ne prouve ni demande, ni marge, ni disponibilité fournisseur.",
        "",
        "## Fichier machine",
        "",
        "- competitor-profiles/workstreams/catalogue-expansion-chien-aquarium.json",
    ]
    return "\n".join(lines) + "\n"


def main():
    RAW_ROOT.mkdir(parents=True, exist_ok=True)
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)

    dog_sources = {
        "boutiquechien.fr": fetch_shopify("boutiquechien", "boutiquechien.fr", pages=3, niche="chien"),
        "nonstopdogwear.com": fetch_shopify("non-stop-dogwear", "www.nonstopdogwear.com", pages=1, niche="chien"),
        "fenril.fr": fetch_fenril(),
        "polytrans.fr": polytrans_observed_collection_products(),
    }

    aquarium_sources = {
        "materiel-aquatique.com": fetch_materiel_aquatique(),
        "aquaplante.fr": fetch_presta_catalogue(
            "aquaplante", "Aquaplante", "aquaplante.fr",
            "https://www.aquaplante.fr/1_index_sitemap.xml", limit=160,
        ),
        "skaii-and-shrimps.fr": fetch_presta_catalogue(
            "skaii-and-shrimps", "Skaii & Shrimps", "skaii-and-shrimps.fr",
            "https://www.skaii-and-shrimps.fr/1_index_sitemap.xml", limit=160,
        ),
        "shrimp-delice.fr": fetch_presta_catalogue(
            "shrimp-delice", "Shrimp-Delice", "shrimp-delice.fr",
            "https://www.shrimp-delice.fr/1_index_sitemap.xml", limit=120,
        ),
    }

    dog_rows = select_exact(
        dog_sources,
        {
            "boutiquechien.fr": 160,
            "polytrans.fr": 20,
            "fenril.fr": 20,
            "nonstopdogwear.com": 20,
        },
        "chien",
    )
    aquarium_rows = select_exact(
        aquarium_sources,
        {
            "materiel-aquatique.com": 170,
            "shrimp-delice.fr": 20,
            "skaii-and-shrimps.fr": 15,
            "aquaplante.fr": 15,
        },
        "aquarium",
    )
    rows = dog_rows + aquarium_rows
    rows.sort(key=lambda row: (row["niche"], row["competitor_domain"], row["competitor_collection"], row["concept_fr_normalized"]))

    with OUT_JSON.open("w", encoding="utf-8") as handle:
        json.dump(rows, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

    raw_sources = [
        "competitor-profiles/raw/catalogue-expansion/boutiquechien/2026-08-08/products-public.json",
        "competitor-profiles/raw/catalogue-expansion/non-stop-dogwear/2026-08-08/products-public.json",
        "competitor-profiles/raw/catalogue-expansion/fenril/2026-08-08/collection-products.json",
        "competitor-profiles/raw/catalogue-expansion/polytrans/2026-08-08/collection-products.json",
        "competitor-profiles/raw/catalogue-expansion/materiel-aquatique/2026-08-08/products-public.json",
        "competitor-profiles/raw/catalogue-expansion/aquaplante/2026-08-08/sitemap-products.json",
        "competitor-profiles/raw/catalogue-expansion/skaii-and-shrimps/2026-08-08/sitemap-products.json",
        "competitor-profiles/raw/catalogue-expansion/shrimp-delice/2026-08-08/sitemap-products.json",
    ]
    OUT_MD.write_text(make_report(rows, raw_sources), encoding="utf-8")
    print(json.dumps({
        "output": str(OUT_JSON),
        "chien": len(dog_rows),
        "aquarium": len(aquarium_rows),
        "total": len(rows),
        "by_competitor": dict(collections.Counter(row["competitor_domain"] for row in rows)),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

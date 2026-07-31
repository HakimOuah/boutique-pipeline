from __future__ import annotations

import hashlib
import re
import unicodedata
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from .models import ProductCandidate


def normalize_text(value: str) -> str:
    text = unicodedata.normalize("NFKD", value or "")
    text = "".join(char for char in text if not unicodedata.combining(char))
    text = re.sub(r"[^a-zA-Z0-9]+", " ", text.lower())
    return " ".join(text.split())


def canonical_url(value: str) -> str:
    if not value:
        return ""
    parts = urlsplit(value.strip())
    ignored = {"utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "aff_fcid", "aff_fsk"}
    query = urlencode(sorted((key, val) for key, val in parse_qsl(parts.query) if key.lower() not in ignored))
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"), query, ""))


def candidate_fingerprint(product: ProductCandidate, ignore_words: list[str], include_angle: bool = True) -> str:
    supplier = canonical_url(product.supplier_url or product.source_url)
    if supplier:
        base = f"url:{supplier}"
    else:
        ignored = {normalize_text(word) for word in ignore_words}
        name_tokens = [token for token in normalize_text(product.product_name).split() if token not in ignored]
        base = "name:" + " ".join(sorted(name_tokens))
    if include_angle and product.angle:
        base += "|angle:" + normalize_text(product.angle)
    return hashlib.sha256(base.encode("utf-8")).hexdigest()


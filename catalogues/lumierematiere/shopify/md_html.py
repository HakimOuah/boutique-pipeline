"""Convertit le markdown simple des pages LM en HTML Shopify."""
from __future__ import annotations

import html
import re


def md_to_html(text: str) -> str:
    text = text.replace("\r\n", "\n").strip()
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|", lines[i + 1]):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(lines[i])
                i += 1
            out.append(_table(rows))
            continue
        if line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(f"<li>{_inline(lines[i][2:])}</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue
        if re.match(r"^#{1,3} ", line):
            level = len(line.split(" ", 1)[0])
            out.append(f"<h{level}>{_inline(line.split(' ', 1)[1])}</h{level}>")
            i += 1
            continue
        para = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith(("#", "-", "|")):
            para.append(lines[i])
            i += 1
        out.append(f"<p>{_inline(' '.join(para))}</p>")
    return "\n".join(out)


def _inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def _table(rows: list[str]) -> str:
    def cells(row: str) -> list[str]:
        parts = [c.strip() for c in row.strip().strip("|").split("|")]
        return parts

    header = cells(rows[0])
    body = [cells(r) for r in rows[2:]]
    thead = "<tr>" + "".join(f"<th>{_inline(c)}</th>" for c in header) + "</tr>"
    tbody = "".join(
        "<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in row) + "</tr>" for row in body
    )
    return f"<table><thead>{thead}</thead><tbody>{tbody}</tbody></table>"

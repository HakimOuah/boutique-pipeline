#!/usr/bin/env python3
"""Pose des cotes (dimensions) sur les visuels « dimensions » Bercelou.

Python 3 + Pillow uniquement. Les valeurs affichées viennent d'un fichier de
specs (cotes_specs.json) construit à partir de la section « ## Dimensions »
des fiches ; le script n'invente rien.

Usage :
  python3 cotes.py --src DOSSIER_VISUELS --out DOSSIER_SORTIE \
      [--specs cotes_specs.json] [--handles h1,h2] [--exclude h3,h4] \
      [--debug] [--planche]

Spec d'une fiche (clé = handle) :
  {
    "lignes": [
      {"type": "l"|"h"|"d", "valeur": "77 cm", "cible": "auto"|"gauche"|"droite"|[x0,y0,x1,y1],
       "cote": "droite"|"gauche"}          # "d" = diamètre, ligne horizontale « Ø … »
    ],
    "encart": ["Profondeur 42 cm", ...],   # texte en bas à gauche
    "scene": false,                         # true = fond non uni : pas de recadrage
    "boite": [x0,y0,x1,y1],                 # force la boîte produit globale (px source)
    "fiche": "chemin", "remarques": "..."
  }
Les valeurs contiennent des espaces normaux : le script les remplace par des
espaces insécables avant « cm » et après « Ø ».
"""
import argparse, glob, json, os, sys
from collections import deque
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SIZE = 2048
INK = (0x1E, 0x2A, 0x3A)
PILL = (0xF7, 0xF2, 0xEA)
PILL_EDGE = (0xD8, 0xD0, 0xC4)
LINE_W = 3
TICK = 26          # demi-longueur des barres d'extrémité
OFFSET = 55        # décalage ligne / produit
MARGIN = 60        # marge image
LABEL_PX = 54
ENCART_PX = 44
STRICT = 60
NBSP = " "

FONT_CANDIDATES = [
    os.path.expanduser("~/Library/Fonts/Karla-SemiBold.ttf"),
    os.path.expanduser("~/Library/Fonts/Karla-Medium.ttf"),
    os.path.expanduser("~/Library/Fonts/Karla-Regular.ttf"),
    "/Library/Fonts/Karla-Regular.ttf",
    os.path.expanduser("~/Library/Fonts/Karla[wght].ttf"),
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
]
FONT_TEXT_CANDIDATES = [
    os.path.expanduser("~/Library/Fonts/Karla-Regular.ttf"),
    "/Library/Fonts/Karla-Regular.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
]


def load_font(cands, px):
    for p in cands:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, px), p
            except OSError:
                pass
    return ImageFont.load_default(), "default"


def fr(txt):
    """Espaces insécables typographiques."""
    t = txt.replace(" cm", NBSP + "cm").replace("Ø ", "Ø" + NBSP)
    t = t.replace(" °", NBSP + "°").replace(" kg", NBSP + "kg")
    t = t.replace(" :", NBSP + ":")
    return t


# ---------------------------------------------------------------- détection
def bg_color(im):
    small = im.resize((256, 256))
    px = small.load()
    border = []
    for i in range(256):
        border += [px[i, 0], px[i, 255], px[0, i], px[255, i]]
    return tuple(sorted(c[k] for c in border)[len(border) // 2] for k in range(3))


def border_profiles(small, n, strip=6):
    """Couleur du fond le long des 4 bords (moyenne d'une bande, lissée)."""
    px = small.load()
    def avg(pts):
        r = g = b = 0
        for q in pts:
            c = px[q]; r += c[0]; g += c[1]; b += c[2]
        k = len(pts); return (r / k, g / k, b / k)
    L = [avg([(x, y) for x in range(strip)]) for y in range(n)]
    R = [avg([(n - 1 - x, y) for x in range(strip)]) for y in range(n)]
    T = [avg([(x, y) for y in range(strip)]) for x in range(n)]
    B = [avg([(x, n - 1 - y) for y in range(strip)]) for x in range(n)]
    def smooth(a, w=12):
        out = []
        for i in range(n):
            seg = a[max(0, i - w):i + w + 1]
            out.append(tuple(sorted(c[k] for c in seg)[len(seg) // 2] for k in range(3)))
        return out
    return smooth(L), smooth(R), smooth(T), smooth(B)


def product_mask(im, bg, thr=25, n=512):
    """Masque produit : écart au fond interpolé depuis les bords (patch de Coons),
    ce qui neutralise les dégradés / vignettages du fond studio."""
    small = im.resize((n, n), Image.BILINEAR)
    L, R, T, B = border_profiles(small, n)
    c00, c10, c01, c11 = T[0], T[-1], B[0], B[-1]
    data = list(small.get_flattened_data() if hasattr(small, "get_flattened_data") else small.getdata())
    mask = bytearray(n * n)
    inv = 1.0 / (n - 1)
    for y in range(n):
        v = y * inv
        Ly, Ry = L[y], R[y]
        row = y * n
        for x in range(n):
            u = x * inv
            r, g, b = data[row + x]
            bgp = [ (1 - u) * Ly[k] + u * Ry[k] + (1 - v) * T[x][k] + v * B[x][k]
                    - ((1 - u) * (1 - v) * c00[k] + u * (1 - v) * c10[k]
                       + (1 - u) * v * c01[k] + u * v * c11[k]) for k in range(3)]
            dr, dg, db = r - bgp[0], g - bgp[1], b - bgp[2]
            d = (dr * dr + dg * dg + db * db) ** 0.5
            if d <= thr:
                continue
            m = (dr + dg + db) / 3.0
            spread = max(abs(dr - m), abs(dg - m), abs(db - m))
            # ombre très claire : assombrissement uniforme et faible
            if m < 0 and spread < 7 and d < 48:
                continue
            # ombre portée : sombre, douce, peu saturée -> ne compte pas pour le bas
            if m < 0 and d < STRICT and spread < 14:
                mask[row + x] = 2
                continue
            mask[row + x] = 1
    return mask, n


def components(mask, n, min_frac=0.0015):
    seen = bytearray(n * n)
    comps = []
    minpx = int(n * n * min_frac)
    for start in range(n * n):
        if not mask[start] or seen[start]:
            continue
        q = deque([start]); seen[start] = 1
        x0 = y0 = n; x1 = y1 = 0; cnt = 0
        while q:
            p = q.popleft()
            y, x = divmod(p, n)
            if mask[p] == 1:
                cnt += 1
                if x < x0: x0 = x
                if x > x1: x1 = x
                if y < y0: y0 = y
                if y > y1: y1 = y
            for nb in (p - 1 if x else -1, p + 1 if x < n - 1 else -1, p - n, p + n):
                if 0 <= nb < n * n and mask[nb] and not seen[nb]:
                    seen[nb] = 1; q.append(nb)
        if cnt >= minpx:
            comps.append((x0, y0, x1 + 1, y1 + 1, cnt))
    return comps


def groups_from(comps, n, gap=4):
    """Regroupe les composantes séparées par une bande verticale vide."""
    cols = bytearray(n)
    for x0, y0, x1, y1, _ in comps:
        for x in range(x0, x1):
            cols[x] = 1
    runs, x = [], 0
    while x < n:
        if cols[x]:
            s = x
            while x < n and cols[x]:
                x += 1
            runs.append([s, x])
        else:
            x += 1
    merged = []
    for r in runs:
        if merged and r[0] - merged[-1][1] < gap:
            merged[-1][1] = r[1]
        else:
            merged.append(r)
    out = []
    for s, e in merged:
        cs = [c for c in comps if c[0] >= s and c[2] <= e]
        out.append((min(c[0] for c in cs), min(c[1] for c in cs),
                    max(c[2] for c in cs), max(c[3] for c in cs)))
    return out


def detect(im):
    bg = bg_color(im)
    mask, n = product_mask(im, bg)
    comps = components(mask, n)
    k = SIZE / n
    if not comps:
        return bg, [0, 0, SIZE, SIZE], [], mask, n
    groups = [[int(a * k) for a in g] for g in groups_from(comps, n)]
    union = [min(g[0] for g in groups), min(g[1] for g in groups),
             max(g[2] for g in groups), max(g[3] for g in groups)]
    return bg, union, groups, mask, n


# ---------------------------------------------------------------- dessin
def text_size(font, txt):
    b = font.getbbox(txt)
    return b[2] - b[0], b[3] - b[1], b


def pill(draw, cx, cy, txt, font):
    w, h, b = text_size(font, txt)
    pw, ph = w + 44, int(font.size * 1.45)
    x0, y0 = int(cx - pw / 2), int(cy - ph / 2)
    draw.rounded_rectangle([x0, y0, x0 + pw, y0 + ph], radius=ph // 2,
                           fill=PILL, outline=PILL_EDGE, width=2)
    draw.text((cx - w / 2 - b[0], cy - h / 2 - b[1]), txt, font=font, fill=INK)
    return [x0, y0, x0 + pw, y0 + ph]


def pill_dims(font, txt):
    w, _, _ = text_size(font, txt)
    return w + 44, int(font.size * 1.45)


def hline(draw, x0, x1, y):
    draw.line([(x0, y), (x1, y)], fill=INK, width=LINE_W)
    for x in (x0, x1):
        draw.line([(x, y - TICK), (x, y + TICK)], fill=INK, width=LINE_W)


def vline(draw, x, y0, y1):
    draw.line([(x, y0), (x, y1)], fill=INK, width=LINE_W)
    for y in (y0, y1):
        draw.line([(x - TICK, y), (x + TICK, y)], fill=INK, width=LINE_W)


def mask_hits(mask, n, rect, transform):
    """Vrai si le rectangle (coords sortie) recouvre le produit."""
    s, ox, oy = transform
    k = SIZE / n
    x0 = int(((rect[0] - ox) / s) / k); x1 = int(((rect[2] - ox) / s) / k) + 1
    y0 = int(((rect[1] - oy) / s) / k); y1 = int(((rect[3] - oy) / s) / k) + 1
    for y in range(max(0, y0 - 2), min(n, y1 + 2)):
        row = y * n
        for x in range(max(0, x0 - 2), min(n, x1 + 2)):
            if mask[row + x] == 1:
                return True
    return False


def feather_mask(w, h, f=70):
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rectangle([f // 2, f // 2, w - f // 2, h - f // 2], fill=255)
    return m.filter(ImageFilter.GaussianBlur(f / 3))


def resolve_box(cible, union, groups):
    if cible in (None, "auto"):
        return list(union)
    if cible == "gauche":
        return list(groups[0]) if groups else list(union)
    if cible == "droite":
        return list(groups[-1]) if groups else list(union)
    return list(cible)


def render(src, spec, out_path, debug=False):
    im = Image.open(src).convert("RGB")
    assert im.size == (SIZE, SIZE), im.size
    bg, union, groups, mask, n = detect(im)
    if spec.get("boite"):
        union = list(spec["boite"])
    lignes = spec.get("lignes", [])
    boxes = [resolve_box(l.get("cible"), union, groups) for l in lignes]
    fnt, _ = load_font(FONT_CANDIDATES, LABEL_PX)
    ftxt, _ = load_font(FONT_TEXT_CANDIDATES, ENCART_PX)
    encart = [fr(t) for t in spec.get("encart", [])]
    enc_line_h = int(ENCART_PX * 1.35)
    enc_h = (len(encart) * enc_line_h + 36) if encart else 0

    # place à réserver autour du produit
    all_box = [min([union[0]] + [b[0] for b in boxes]), min([union[1]] + [b[1] for b in boxes]),
               max([union[2]] + [b[2] for b in boxes]), max([union[3]] + [b[3] for b in boxes])]
    need = {"l": MARGIN, "r": MARGIN, "t": MARGIN, "b": MARGIN}
    for l in lignes:
        pw, ph = pill_dims(fnt, fr(l["valeur"]))
        if l["type"] == "h":
            side = "l" if l.get("cote") == "gauche" else "r"
            need[side] = max(need[side], MARGIN + OFFSET + TICK + 10)
        else:
            need["b"] = max(need["b"], MARGIN + OFFSET + ph // 2 + 10)
    if encart:
        need["b"] += enc_h + 24

    scene = spec.get("scene", False)
    s, ox, oy = 1.0, 0, 0
    if not scene:
        aw, ah = all_box[2] - all_box[0], all_box[3] - all_box[1]
        s = min(1.0, (SIZE - need["l"] - need["r"]) / aw, (SIZE - need["t"] - need["b"]) / ah)
        s = min(s, spec.get("echelle_max", 1.0))
        nx0 = all_box[0] * s + (SIZE - SIZE * s) / 2
        ny0 = all_box[1] * s + (SIZE - SIZE * s) / 2
        nw, nh = aw * s, ah * s
        # centrage horizontal dans la zone utile, vertical borné
        tx = need["l"] + ((SIZE - need["l"] - need["r"]) - nw) / 2
        ty = min(max(ny0, need["t"]), SIZE - need["b"] - nh)
        ox = tx - all_box[0] * s
        oy = ty - all_box[1] * s
        canvas = Image.new("RGB", (SIZE, SIZE), bg)
        rw = int(round(SIZE * s))
        small = im.resize((rw, rw), Image.LANCZOS) if s < 1 else im
        if s < 1 or abs(ox) > 0.5 or abs(oy) > 0.5:
            canvas.paste(small, (int(round(ox)), int(round(oy))), feather_mask(rw, rw))
            im = canvas
    T = lambda b: [b[0] * s + ox, b[1] * s + oy, b[2] * s + ox, b[3] * s + oy]
    tr = (s, ox, oy)
    draw = ImageDraw.Draw(im)
    placed, issues = [], []

    if debug:
        for g in groups:
            draw.rectangle(T(g), outline=(255, 0, 0), width=4)
        draw.rectangle(T(union), outline=(0, 160, 0), width=4)

    for l, b in zip(lignes, boxes):
        b = T(b)
        txt = fr(l["valeur"])
        if l["type"] in ("l", "d"):
            y = b[3] + OFFSET
            x0, x1 = b[0], b[2]
            if y > SIZE - MARGIN:
                issues.append(f"ligne {txt} hors marge"); y = SIZE - MARGIN
            hline(draw, x0, x1, y)
            placed.append(pill(draw, (x0 + x1) / 2, y, txt, fnt))
        else:
            side = l.get("cote", "droite")
            x = b[2] + OFFSET if side == "droite" else b[0] - OFFSET
            if not (MARGIN <= x <= SIZE - MARGIN):
                issues.append(f"ligne {txt} hors marge ({side})")
                x = min(max(x, MARGIN), SIZE - MARGIN)
            y0, y1 = b[1], b[3]
            vline(draw, x, y0, y1)
            pw, ph = pill_dims(fnt, txt)
            cy_mid = (y0 + y1) / 2
            best = None
            step = 20
            for k in range(0, int((y1 - y0) / 2 - ph / 2) // step + 1):
                for cy in (cy_mid - k * step, cy_mid + k * step):
                    r = [x - pw / 2, cy - ph / 2, x + pw / 2, cy + ph / 2]
                    if r[0] < MARGIN / 2 or r[2] > SIZE - MARGIN / 2:
                        continue
                    if any(not (r[2] < p[0] or r[0] > p[2] or r[3] < p[1] or r[1] > p[3]) for p in placed):
                        continue
                    if not scene and not mask_hits(mask, n, r, tr):
                        best = cy; break
                if best is not None:
                    break
            if best is not None:
                cx = min(max(x, MARGIN / 2 + pw / 2), SIZE - MARGIN / 2 - pw / 2)
                placed.append(pill(draw, cx, best, txt, fnt))
            else:
                # étiquette pivotée le long de la ligne (lecture de bas en haut)
                tmp = Image.new("RGBA", (pw + 4, ph + 4), (0, 0, 0, 0))
                pill(ImageDraw.Draw(tmp), (pw + 4) / 2, (ph + 4) / 2, txt, fnt)
                rot = tmp.rotate(90, expand=True, resample=Image.BICUBIC)
                px0, py0 = int(x - rot.width / 2), int(cy_mid - rot.height / 2)
                im.paste(rot, (px0, py0), rot)
                r = [px0, py0, px0 + rot.width, py0 + rot.height]
                placed.append(r)
                if mask_hits(mask, n, [r[0] + 6, r[1], r[2] - 6, r[3]], tr) and not scene:
                    issues.append(f"étiquette {txt} touche le produit")

    if encart:
        wmax = max(text_size(ftxt, t)[0] for t in encart)
        pos = spec.get("encart_pos", "bas-gauche")
        x0 = MARGIN
        y0 = SIZE - MARGIN - enc_h if pos == "bas-gauche" else MARGIN
        box = [x0, y0, x0 + wmax + 56, y0 + enc_h]
        if box[2] > SIZE - MARGIN:
            issues.append("encart trop large")
        draw.rounded_rectangle(box, radius=26, fill=PILL, outline=PILL_EDGE, width=2)
        for i, t in enumerate(encart):
            _, _, bb = text_size(ftxt, t)
            draw.text((x0 + 28 - bb[0], y0 + 18 + i * enc_line_h + (enc_line_h - ENCART_PX) / 2 - bb[1] + 4),
                      t, font=ftxt, fill=INK)
        if not scene and mask_hits(mask, n, box, tr):
            issues.append("encart recouvre le produit")
    im.save(out_path, "JPEG", quality=90, optimize=True)
    return {"echelle": round(s, 3), "boite": [int(v) for v in union],
            "groupes": groups, "problemes": issues}


def planche(out_dir, handles, path, t=400, per_row=6):
    fnt, _ = load_font(FONT_TEXT_CANDIDATES, 18)
    rows = (len(handles) + per_row - 1) // per_row
    sheet = Image.new("RGB", (per_row * t, rows * (t + 24)), "white")
    d = ImageDraw.Draw(sheet)
    for i, h in enumerate(handles):
        p = os.path.join(out_dir, f"{h}-dimensions.jpg")
        if not os.path.exists(p):
            continue
        im = Image.open(p); im.thumbnail((t, t))
        x, y = (i % per_row) * t, (i // per_row) * (t + 24)
        sheet.paste(im, (x, y + 24))
        d.text((x + 4, y + 2), f"{i} {h[:40]}", font=fnt, fill="black")
    sheet.save(path, quality=85)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", default=here)
    ap.add_argument("--specs", default=os.path.join(here, "cotes_specs.json"))
    ap.add_argument("--handles", default="")
    ap.add_argument("--exclude", default="")
    ap.add_argument("--debug", action="store_true")
    ap.add_argument("--planche", action="store_true")
    ap.add_argument("--rapport", default=None, help="cotes.json (défaut : <out>/cotes.json)")
    a = ap.parse_args()

    specs = json.load(open(a.specs, encoding="utf-8"))
    files = {os.path.basename(f)[:-len("-dimensions.jpg")]: f
             for f in glob.glob(os.path.join(a.src, "**", "*-dimensions.jpg"), recursive=True)}
    wanted = [h for h in a.handles.split(",") if h] or sorted(files)
    excl = set(h for h in a.exclude.split(",") if h)
    os.makedirs(a.out, exist_ok=True)
    rap_path = a.rapport or os.path.join(a.out, "cotes.json")
    rapport = json.load(open(rap_path, encoding="utf-8")) if os.path.exists(rap_path) else {}
    done = []
    for h in wanted:
        if h in excl:
            continue
        if h not in files:
            print(f"[absent] {h}", file=sys.stderr); continue
        if h not in specs:
            print(f"[sans spec] {h}", file=sys.stderr); continue
        sp = specs[h]
        info = render(files[h], sp, os.path.join(a.out, f"{h}-dimensions.jpg"), a.debug)
        cotes = [fr(l["valeur"]) + {"l": " (ligne largeur)", "h": " (ligne hauteur)", "d": " (ligne diamètre)"}[l["type"]]
                 for l in sp.get("lignes", [])] + [fr(t) + " (encart)" for t in sp.get("encart", [])]
        rapport[h] = {
            "cotes_affichees": cotes,
            "source": sp.get("fiche", f"fiches/{h}.md § Dimensions"),
            "remarques": "; ".join(x for x in [sp.get("remarques", "")] + info["problemes"] if x),
            "echelle_produit": info["echelle"],
        }
        done.append(h)
        print(f"ok {h} s={info['echelle']} {info['problemes'] or ''}")
    json.dump(rapport, open(rap_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if a.planche:
        planche(a.out, done, os.path.join(a.out, "_planche.jpg"))
    print(f"{len(done)} image(s)")


if __name__ == "__main__":
    main()

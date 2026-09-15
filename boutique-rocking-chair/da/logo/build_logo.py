"""Bercelou logo B « le mot bercé » : Fraunces instance -> outlined SVG + PNG (no font dependency)."""
import math, pathlib
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.basePen import BasePen
from PIL import Image, ImageDraw, ImageChops

HERE = pathlib.Path(__file__).parent
OUT = HERE / "out"
OUT.mkdir(exist_ok=True)

NUIT, SABLE, TERRE, AMBRE, CREME = "#1E2A3A", "#F7F2EA", "#AE5420", "#E08E45", "#F3ECE1"

font = instantiateVariableFont(TTFont(HERE / "Fraunces-VF.ttf"), {"wght": 500, "SOFT": 100, "WONK": 0, "opsz": 96})
gs, cmap, hmtx, upem = font.getGlyphSet(), font.getBestCmap(), font["hmtx"], font["head"].unitsPerEm


def kern_pairs():
    """First/second glyph -> x advance adjustment from GPOS PairPos lookups."""
    pairs = {}
    gpos = font["GPOS"].table
    for fr in gpos.FeatureList.FeatureRecord:
        if fr.FeatureTag != "kern":
            continue
        for li in fr.Feature.LookupListIndex:
            lk = gpos.LookupList.Lookup[li]
            subs = [s.ExtSubTable if lk.LookupType == 9 else s for s in lk.SubTable]
            for st in subs:
                if getattr(st, "LookupType", 2) != 2 and lk.LookupType not in (2, 9):
                    continue
                cov = st.Coverage.glyphs
                if st.Format == 1:
                    for i, g1 in enumerate(cov):
                        for pvr in st.PairSet[i].PairValueRecord:
                            v = getattr(pvr.Value1, "XAdvance", 0) or 0
                            pairs.setdefault((g1, pvr.SecondGlyph), v)
                elif st.Format == 2:
                    c1, c2 = st.ClassDef1.classDefs, st.ClassDef2.classDefs
                    for g1 in cov:
                        row = st.Class1Record[c1.get(g1, 0)]
                        for g2 in gs.keys():
                            v = getattr(row.Class2Record[c2.get(g2, 0)].Value1, "XAdvance", 0) or 0
                            if v:
                                pairs.setdefault((g1, g2), v)
    return pairs


KERN = kern_pairs()


def word_outline(text, size):
    """Returns list of (glyphName, xOffset) in font units and total advance."""
    names = [cmap[ord(c)] for c in text]
    x, placed = 0, []
    for i, n in enumerate(names):
        placed.append((n, x))
        x += hmtx[n][0]
        if i + 1 < len(names):
            x += KERN.get((n, names[i + 1]), 0)
    return placed, x


class FlattenPen(BasePen):
    """Collects contours as point lists, curves flattened."""
    def __init__(self, glyphSet=None, steps=24):
        super().__init__(glyphSet)
        self.contours, self.cur, self.steps = [], [], steps
    def _moveTo(self, p): self.cur = [p]
    def _lineTo(self, p): self.cur.append(p)
    def _curveToOne(self, p1, p2, p3):
        p0 = self.cur[-1]
        for i in range(1, self.steps + 1):
            t = i / self.steps; u = 1 - t
            self.cur.append((u**3*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0],
                             u**3*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1]))
    def _qCurveToOne(self, p1, p2):
        p0 = self.cur[-1]
        for i in range(1, self.steps + 1):
            t = i / self.steps; u = 1 - t
            self.cur.append((u*u*p0[0] + 2*u*t*p1[0] + t*t*p2[0], u*u*p0[1] + 2*u*t*p1[1] + t*t*p2[1]))
    def _closePath(self):
        if self.cur: self.contours.append(self.cur)
        self.cur = []
    _endPath = _closePath


# ---- geometry, identical to the approved planche (viewBox 300x110) ----
FS, CX, BASE = 58, 150, 66
RUNNER = [(22, 76), (40, 91), (84, 96), (150, 96)]      # first cubic of "M22 76c18 15 62 20 128 20"
RUNNER2 = [(150, 96), (216, 96), (260, 91), (278, 76)]  # mirrored "s110-5 128-20"
RUNNER_W = 3.6


def glyph_transforms(text):
    placed, adv = word_outline(text, FS)
    s = FS / upem
    x0 = CX - adv * s / 2
    return [(n, (s, 0, 0, -s, x0 + x * s, BASE)) for n, x in placed]


def svg(text_fill, runner_fill, bg=None, pad=(0, 0, 300, 110)):
    paths = []
    for n, tr in glyph_transforms("bercelou"):
        pen = SVGPathPen(gs)
        gs[n].draw(TransformPen(pen, tr))
        paths.append(pen.getCommands())
    d = " ".join(paths)
    x, y, w, h = pad
    rect = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {w} {h}" role="img" aria-label="Bercelou">'
            f'{rect}<path d="{d}" fill="{text_fill}"/>'
            f'<path d="M22 76c18 15 62 20 128 20s110-5 128-20" fill="none" stroke="{runner_fill}" stroke-width="{RUNNER_W}" stroke-linecap="round"/></svg>')


def bez(p, steps=80):
    out = []
    for i in range(steps + 1):
        t = i / steps; u = 1 - t
        out.append((u**3*p[0][0] + 3*u*u*t*p[1][0] + 3*u*t*t*p[2][0] + t**3*p[3][0],
                    u**3*p[0][1] + 3*u*u*t*p[1][1] + 3*u*t*t*p[2][1] + t**3*p[3][1]))
    return out


def hex2rgba(h, a=255):
    h = h.lstrip("#"); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4)) + (a,)


def render(text_fill, runner_fill, box, scale, bg=None, glyphs="bercelou", runner=True, stroke=RUNNER_W, transforms=None):
    """box = (x, y, w, h) in planche units; scale = px per unit."""
    SS = 4
    bx, by, bw, bh = box
    W, H = round(bw * scale * SS), round(bh * scale * SS)
    k = scale * SS
    def P(pt): return ((pt[0] - bx) * k, (pt[1] - by) * k)
    # exact non-zero scanline fill (handles overlapping and self-intersecting contours)
    edges = []
    for n, tr in (transforms or glyph_transforms(glyphs)):
        pen = FlattenPen(gs)
        gs[n].draw(TransformPen(pen, tr))
        for c in pen.contours:
            pts = [P(p) for p in c]
            for i in range(len(pts)):
                (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % len(pts)]
                if y1 != y2:
                    edges.append((x1, y1, x2, y2, 1 if y2 > y1 else -1))
    mask = Image.new("L", (W, H), 0)
    dm = ImageDraw.Draw(mask)
    ymin = max(0, int(min(min(e[1], e[3]) for e in edges)))
    ymax = min(H - 1, int(max(max(e[1], e[3]) for e in edges)) + 1)
    for yy in range(ymin, ymax + 1):
        yc = yy + 0.5
        xs = []
        for x1, y1, x2, y2, d in edges:
            if (y1 <= yc < y2) or (y2 <= yc < y1):
                xs.append((x1 + (yc - y1) * (x2 - x1) / (y2 - y1), d))
        xs.sort()
        wn = 0
        for i, (xv, d) in enumerate(xs):
            prev = wn
            wn += d
            if prev == 0 and wn != 0:
                xstart = xv
            elif prev != 0 and wn == 0:
                dm.line([(round(xstart), yy), (round(xv) - 1, yy)], fill=255)
    img = Image.new("RGBA", (W, H), hex2rgba(bg) if bg else (0, 0, 0, 0))
    img.paste(Image.new("RGBA", (W, H), hex2rgba(text_fill)), (0, 0), mask)
    if runner:
        rmask = Image.new("L", (W, H), 0)
        dr = ImageDraw.Draw(rmask)
        segs = runner if isinstance(runner, list) else [RUNNER, RUNNER2]
        line = []
        for s_ in segs: line += bez(s_)
        lw = stroke * k
        dr.line([P(p) for p in line], fill=255, width=round(lw), joint="curve")
        for end in (line[0], line[-1]):
            ex, ey = P(end); r = lw / 2
            dr.ellipse((ex - r, ey - r, ex + r, ey + r), fill=255)
        img.paste(Image.new("RGBA", (W, H), hex2rgba(runner_fill)), (0, 0), rmask)
    return img.resize((W // SS, H // SS), Image.LANCZOS)


if __name__ == "__main__":
    # tight box around word + runner (planche units)
    tr = glyph_transforms("bercelou")
    xs, ys = [], []
    for n, t in tr:
        pen = FlattenPen(gs); gs[n].draw(TransformPen(pen, t))
        for c in pen.contours:
            xs += [p[0] for p in c]; ys += [p[1] for p in c]
    x0 = min(min(xs), 22 - RUNNER_W) - 2; x1 = max(max(xs), 278 + RUNNER_W) + 2
    y0 = min(ys) - 2; y1 = 96 + RUNNER_W / 2 + 2
    box = (x0, y0, x1 - x0, y1 - y0)
    print("box", [round(v, 2) for v in box])

    (OUT / "bercelou-logo-nuit-sur-sable.svg").write_text(svg(NUIT, TERRE, pad=box))
    (OUT / "bercelou-logo-creme-sur-nuit.svg").write_text(svg(CREME, AMBRE, pad=box))
    (OUT / "bercelou-logo-nuit-sur-sable-fond.svg").write_text(svg(NUIT, TERRE, bg=SABLE, pad=(0, 0, 300, 110)))

    S = 1200 / box[2]  # 1200 px wide transparent PNGs
    render(NUIT, TERRE, box, S).save(OUT / "bercelou-logo-fonce.png")
    render(CREME, AMBRE, box, S).save(OUT / "bercelou-logo-clair.png")

    # favicon / avatar : « b » sur patin, carré arrondi nuit
    bname = cmap[ord("b")]
    adv = hmtx[bname][0]
    def mono(size, radius_ratio, file, stroke_ratio):
        U = 140  # design units of the square
        s = 96 / upem
        tx = (U - adv * s) / 2 - 2
        img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        d.rounded_rectangle((0, 0, size - 1, size - 1), radius=round(size * radius_ratio), fill=hex2rgba(NUIT))
        glyph = render(CREME, AMBRE, (0, 0, U, U), size / U, glyphs="b",
                       runner=[[(30, 104), (42, 116), (98, 116), (110, 104)]], stroke=U * stroke_ratio,
                       transforms=[(bname, (s, 0, 0, -s, tx, 96))])
        img.alpha_composite(glyph)
        img.save(OUT / file)
    mono(512, 0.22, "bercelou-favicon-512.png", 0.055)
    mono(180, 0.22, "bercelou-apple-touch-180.png", 0.06)
    mono(1080, 0.0, "bercelou-avatar-1080.png", 0.05)
    print("ok", sorted(p.name for p in OUT.iterdir()))

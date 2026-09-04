"""Planche interne des preuves DOM et des visuels existants, sans retouche produit."""
import json
import subprocess
from pathlib import Path
from urllib.request import urlopen
from PIL import Image, ImageDraw, ImageFont

base = Path(__file__).resolve().parents[1]
out = base / 'livraisons-visuels-codex/couverture-2026-09-05/qa-sources'
out.mkdir(parents=True, exist_ok=True)
font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 17)
handles = ['lustre-anneau-led-led-717226','lustre-anneau-led-led-625575','lustre-anneau-led-led-134962','plafonnier-led-led-183789','lustre-statement-led-noir-950316','suspension-metal-noir-dore-361680','plafonnier-led-992600']
for h in handles:
    folder = base / 'sources-par-handle' / h / 'variantes-lot4-20260905'
    proof = folder / 'preuves-dom.json'
    data = json.loads(proof.read_text())
    items = []
    for v in data['variants']:
        raw = folder / (v['key'] + '.avif')
        if not raw.exists():
            try:
                raw.write_bytes(urlopen(v['thumbnail'], timeout=25).read())
                v['download_fallback'] = 'Vignette observee au DOM'
                v['downloaded_url'] = v['thumbnail']
                v['local_path'] = str(raw.relative_to(base.parents[1]))
            except Exception as e:
                print(h, v['key'], str(e))
        jpg = raw.with_suffix('.jpg')
        if raw.exists() and not jpg.exists():
            subprocess.run(['sips','-s','format','jpeg',str(raw),'--out',str(jpg)], check=True, capture_output=True)
        items.append((jpg, v['key']+' / '+v['label']))
    proof.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
    existing = list((base / 'livraisons-visuels-codex/variantes-couleur' / h).glob('*-g1.jpg'))
    if not existing:
        existing = [base / 'livraisons-visuels-codex/produits' / h / (h+'-g1.jpg')]
    items.extend((p, 'EXISTANT '+p.name.replace(h+'-', '')) for p in existing)
    sheet = Image.new('RGB',(1760,((len(items)+3)//4)*500),'#F6F3EC')
    draw = ImageDraw.Draw(sheet)
    for i,(p,label) in enumerate(items):
        x,y=(i%4)*440,(i//4)*500
        if p.exists():
            im=Image.open(p).convert('RGB'); im.thumbnail((430,440))
            sheet.paste(im,(x+(440-im.width)//2,y))
        draw.text((x+8,y+445),label,font=font,fill='#24211B')
    sheet.save(out/(h+'.jpg'),quality=94)
    print(h, [(v['key'], v['label'], bool(v['local_path'])) for v in data['variants']])

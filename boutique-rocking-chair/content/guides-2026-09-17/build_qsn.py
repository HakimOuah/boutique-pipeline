#!/usr/bin/env python3
"""Page « Qui sommes-nous » Bercelou, même système visuel que les guides (.bcg)."""
import html
import json
from pathlib import Path

import build_guides as g

ROOT = Path(__file__).resolve().parent
F = "https://cdn.shopify.com/s/files/1/1082/4564/7705/files/"
C = "https://cdn.shopify.com/s/files/1/1082/4564/7705/collections/"

EXTRA_CSS = """<style>
.bcg h2.bcg-h1{font-family:var(--font-heading--family,Fraunces,Georgia,serif);font-weight:500;line-height:1.1;text-wrap:balance;color:var(--bcg-nuit);font-size:clamp(1.8rem,1.3rem + 2vw,2.8rem);margin:0 0 .45em}
.bcg-sec{margin:0 0 40px}
.bcg-sec__tete{max-width:44em;margin:0 0 18px}
.bcg-crit{list-style:none;margin:14px 0 0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.bcg-crit li{display:grid;grid-template-columns:24px 1fr;gap:10px;align-items:start;background:var(--bcg-sable);border-radius:14px;padding:12px 14px;font-size:.95rem}
.bcg-crit svg{width:22px;height:22px;color:var(--bcg-terre)}
.bcg-cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.bcg-card{display:block;background:#fff;border-radius:18px;overflow:hidden;text-decoration:none!important;color:var(--bcg-encre)!important;transition:transform .2s,box-shadow .2s}
.bcg-card:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(30,42,58,.10)}
.bcg-card:focus-visible{outline:2px solid var(--bcg-ambre);outline-offset:3px}
.bcg-card img{display:block;width:100%;aspect-ratio:4/3;object-fit:cover}
.bcg-card__txt{padding:14px 16px 16px}
.bcg-card__txt strong{display:flex;justify-content:space-between;align-items:center;gap:8px;font-family:var(--font-heading--family,Fraunces,Georgia,serif);font-weight:500;font-size:1.15rem;color:var(--bcg-nuit)}
.bcg-card__txt strong svg{width:18px;height:18px;color:var(--bcg-terre);flex:none}
.bcg-card__txt span{display:block;font-size:.88rem;opacity:.8;margin-top:4px}
.bcg-perks{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin:0 0 40px}
.bcg-perk{background:var(--bcg-sable-f);border-radius:18px;padding:18px}
.bcg-perk svg{width:28px;height:28px;color:var(--bcg-terre);margin:0 0 8px}
.bcg-perk strong{display:block;color:var(--bcg-nuit);margin:0 0 2px}
.bcg-perk span{font-size:.9rem}
.bcg-contact{display:grid;grid-template-columns:1fr 1fr;gap:clamp(20px,4vw,44px);background:#fff;border-radius:22px;padding:clamp(20px,3vw,32px);margin:0 0 22px;align-items:center}
.bcg-coord{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.bcg-coord li{display:grid;grid-template-columns:24px 1fr;gap:10px;align-items:start}
.bcg-coord svg{width:22px;height:22px;color:var(--bcg-nuit)}
.bcg-coord a{font-weight:600}
.bcg-petit{font-size:.88rem;opacity:.8;margin:14px 0 0}
@media (max-width:989px){.bcg-perks{grid-template-columns:repeat(2,minmax(0,1fr))}.bcg-cards{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:749px){.bcg-contact{grid-template-columns:1fr}.bcg-crit{grid-template-columns:1fr}}
@media (max-width:480px){.bcg-cards{grid-template-columns:1fr}}
@media (prefers-reduced-motion:reduce){.bcg-card{transition:none}.bcg-card:hover{transform:none}}
</style>"""

def ico(path, sw="1.6"):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg>')

TRUCK = ico('<path d="M3 7h11v9H3z"/><path d="M14 10h4l3 3v3h-7z"/><circle cx="7" cy="17.5" r="1.6"/><circle cx="17" cy="17.5" r="1.6"/>')
RETURN = ico('<path d="M9 14L4 9l5-5"/><path d="M4 9h10a6 6 0 0 1 0 12h-3"/>')
SHIELD = ico('<path d="M12 3l7 3v5c0 4.5-3 8.3-7 10-4-1.7-7-5.5-7-10V6z"/><path d="M9 12l2 2 4-4"/>')
CARD = ico('<rect x="3" y="5.5" width="18" height="13" rx="2"/><path d="M3 10h18M7 15h4"/>')
MAIL = ico('<rect x="3" y="5.5" width="18" height="13" rx="2"/><path d="M3.5 7l8.5 6 8.5-6"/>')
PHONE = ico('<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>')
PIN = ico('<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>')
CLOCK = ico('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>')


def card(title, sub, img, href):
    return (f'<a class="bcg-card" href="{href}"><img src="{img}?width=700" alt="{html.escape(title)}" width="700" height="525" loading="lazy">'
            f'<div class="bcg-card__txt"><strong>{title}{g.ARROW}</strong><span>{sub}</span></div></a>')


def perk(icon, title, text):
    return f'<div class="bcg-perk">{icon}<strong>{title}</strong><span>{text}</span></div>'


crit = "".join(f"<li>{g.CHECK}<span>{t}</span></li>" for t in [
    "<strong>La hauteur d'assise</strong>, pour choisir entre une assise qui se love et une assise facile à quitter",
    "<strong>Les accoudoirs</strong>, leur hauteur et leur rembourrage, pour poser les bras",
    "<strong>Le dossier</strong>, sa hauteur et sa forme, pour accompagner la tête",
    "<strong>La matière</strong>, son toucher et son entretien au quotidien",
])

body = "\n".join([
    g.CSS, EXTRA_CSS, '<div class="bcg">',
    # bandeau
    '<div class="bcg-hero"><div class="bcg-hero__texte"><span class="bcg-eyebrow">Notre histoire</span>'
    '<h2 class="bcg-h1">Le fauteuil des vraies nuits, et des moments à soi</h2>'
    "<p class=\"bcg-lead\">Bercelou est né d'un constat simple : la plupart des fauteuils à bascule sont pensés pour une photo de chambre de bébé, "
    "pas pour la vie qui va avec. Une tétée de nuit qui dure, un lever qui doit rester silencieux, un salon qui garde le fauteuil bien après. "
    "Nous choisissons nos modèles pour ces deux usages à la fois.</p>"
    f'<div class="bcg-btns">{g.btn("Voir les fauteuils d" + chr(39) + "allaitement", "/collections/fauteuil-allaitement")}'
    f'{g.btn("Notre méthode", "#methode", "ligne", g.DOWN)}</div></div>'
    f'<div class="bcg-hero__media"><img src="{F}bercelou-hero.jpg?width=1200" alt="Une maman berce son bébé la nuit dans un fauteuil à bascule en bouclette" width="1200" height="900"></div></div>',
    # méthode
    f'<section class="bcg-step" id="methode"><div class="bcg-step__media"><img src="{F}fauteuil-a-bascule-allaitement-lin-poches-dimensions.jpg?width=900" '
    'alt="Fauteuil à bascule en lin avec ses cotes : 68 cm de large, 96 cm de haut, assise à 54 cm" width="900" height="900" loading="lazy">'
    '<p class="bcg-cap">Chaque fiche donne les cotes qui comptent, comme ici.</p></div>'
    '<div class="bcg-step__texte"><span class="bcg-eyebrow">Notre méthode de sélection</span><h2>Des fauteuils choisis sur leurs cotes</h2>'
    "<p>Nous ne référençons pas tout ce qui existe. Nous sélectionnons chaque fauteuil d'après ses dimensions et sa matière. "
    "Ces cotes figurent sur chaque fiche, pour que vous choisissiez selon ce qui compte pour vous.</p>"
    f'<ul class="bcg-crit">{crit}</ul>'
    f'<div class="bcg-btns">{g.btn("Lire le guide pour bien choisir", "/pages/guide-bien-choisir-fauteuil-allaitement", "ligne")}</div></div></section>',
    # collections
    '<section class="bcg-sec"><div class="bcg-sec__tete"><span class="bcg-eyebrow">Une sélection qui s\'élargit</span>'
    "<h2>Du berceau au coin lecture</h2><p>Chaque famille répond à un moment de vie différent : les tétées de nuit, la pause au salon, "
    "le soir sur la terrasse, le coin cocooning.</p></div><div class=\"bcg-cards\">"
    + card("Allaitement", "Pour les tétées de nuit, et bien après", F + "collection-fauteuil-allaitement-carte.jpg", "/collections/fauteuil-allaitement")
    + card("Rocking chairs", "Design, scandinaves, bois et rotin", F + "collection-fauteuil-a-bascule-carte.jpg", "/collections/fauteuil-a-bascule")
    + card("Fauteuils relax", "Pivotants, inclinables, avec repose-pieds", F + "fauteuil-relax-bouclette-creme-pivotant-desir.jpg", "/collections/fauteuil-relax")
    + card("Cocooning", "Poufs, repose-pieds, plaids et coussins de sol", C + "collection-pouf-carte.jpg", "/collections/pouf")
    + card("Extérieur", "Rocking chairs de terrasse et de jardin", F + "collection-rocking-chair-exterieur-carte.jpg", "/collections/rocking-chair-exterieur")
    + card("Accessoires", "Plaids, repose-pieds, coussins", F + "collection-accessoires-rocking-chair-carte.jpg", "/collections/accessoires-rocking-chair")
    + "</div></section>",
    # engagements
    '<div class="bcg-perks">'
    + perk(TRUCK, "Livraison offerte", "En France métropolitaine, suivi par e-mail")
    + perk(RETURN, "Retours sous 14 jours", "Après réception, sans avoir à vous justifier")
    + perk(SHIELD, "Garantie légale 2 ans", "Conformité et vices cachés")
    + perk(CARD, "Paiement en 3 ou 4 fois", "Avec Klarna ou PayPal, selon leurs conditions")
    + "</div>",
    # contact
    '<section class="bcg-contact" id="contact"><div><span class="bcg-eyebrow">Nous contacter</span><h2>Une question avant ou après votre achat ?</h2>'
    "<p>Notre équipe vous répond sous 1 jour ouvré, du lundi au vendredi. Si vous nous contactez après 18h, votre demande est prise en charge le jour suivant.</p>"
    f'<div class="bcg-btns">{g.btn("Nous écrire", "mailto:contact@bercelou.com")}{g.btn("Page contact", "/pages/contact", "ligne")}</div></div>'
    '<ul class="bcg-coord">'
    f'<li>{MAIL}<span><a href="mailto:contact@bercelou.com">contact@bercelou.com</a></span></li>'
    f'<li>{PHONE}<span><a href="tel:+33756828094">+33 7 56 82 80 94</a></span></li>'
    f'<li>{CLOCK}<span>Du lundi au vendredi, de 9h00 à 18h00</span></li>'
    f'<li>{PIN}<span>Bercelou, 47 rue Vivienne, 75002 Paris, France</span></li>'
    '</ul></section>',
    # fin
    '<div class="bcg-fin"><div><h2>Trouver votre fauteuil</h2><p>Parcourez nos fauteuils d\'allaitement et nos rocking chairs, cotes à l\'appui.</p></div>'
    f'<div class="bcg-btns">{g.btn("Voir les fauteuils d" + chr(39) + "allaitement", "/collections/fauteuil-allaitement")}'
    f'{g.btn("Voir les rocking chairs", "/collections/fauteuil-a-bascule", "ligne")}</div></div>',
    '<p class="bcg-petit">Retrouvez nos <a href="/policies/legal-notice">mentions légales</a> et nos '
    '<a href="/policies/terms-of-service">conditions générales de vente</a>.</p>',
    "</div>",
])
assert "—" not in body and "–" not in body and "OH Ventures" not in body
(ROOT / "qui-sommes-nous.html").write_text(body)
print(len(body))

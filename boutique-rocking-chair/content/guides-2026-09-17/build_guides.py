#!/usr/bin/env python3
"""Guides Bercelou mis en page : bandeau, sommaire, cartes illustrées, boutons, check-list.

Le contenu des pages s'affiche dans un bloc texte du thème FullStack, qui réduit les titres
au corps du texte : toute la mise en page est donc portée par un <style> limité à .bcg,
placé dans le corps de la page. Aucune modification de thème nécessaire.
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IMG = "https://cdn.shopify.com/s/files/1/1082/4564/7705/files/"

CSS = """<style>
.bcg{--bcg-nuit:#1E2A3A;--bcg-sable:#F7F2EA;--bcg-sable-f:#E7DFD1;--bcg-terre:#AE5420;--bcg-ambre:#E08E45;--bcg-encre:#22201C;
color:var(--bcg-encre);font-size:1rem;line-height:1.65;max-width:1120px;margin:0 auto;width:100%}
.bcg *{box-sizing:border-box}
.bcg p{margin:0 0 .8em}
.bcg a{color:inherit}
.bcg h2,.bcg h3{font-family:var(--font-heading--family,Fraunces,Georgia,serif);font-weight:500;line-height:1.15;text-wrap:balance;margin:0 0 .5em;color:var(--bcg-nuit)}
.bcg h2{font-size:clamp(1.55rem,1.2rem + 1.4vw,2.2rem)}
.bcg h3{font-size:1.15rem}
.bcg-hero{display:grid;grid-template-columns:1.05fr 1fr;gap:clamp(20px,4vw,48px);align-items:center;margin:0 0 36px}
.bcg-eyebrow{display:inline-block;font-size:.78rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--bcg-terre);margin:0 0 .6em}
.bcg-lead{font-size:1.12rem;max-width:36em}
.bcg-hero img,.bcg-step img{display:block;width:100%;height:auto;border-radius:18px;object-fit:cover}
.bcg-hero img{aspect-ratio:4/3}
.bcg-btns{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0 0}
.bcg-btn{display:inline-flex;align-items:center;gap:8px;padding:.78em 1.35em;border-radius:30px;font-weight:600;font-size:.95rem;text-decoration:none!important;line-height:1.2;transition:background .2s,color .2s,border-color .2s}
.bcg-btn svg{width:18px;height:18px;flex:none}
.bcg-btn--plein{background:var(--bcg-terre);color:#fff!important;border:1px solid var(--bcg-terre)}
.bcg-btn--plein:hover{background:var(--bcg-nuit);border-color:var(--bcg-nuit)}
.bcg-btn--ligne{background:transparent;color:var(--bcg-nuit)!important;border:1px solid rgba(30,42,58,.35)}
.bcg-btn--ligne:hover{border-color:var(--bcg-nuit);background:#fff}
.bcg-btn:focus-visible{outline:2px solid var(--bcg-ambre);outline-offset:3px}
.bcg-toc{background:#fff;border:1px solid var(--bcg-sable-f);border-radius:18px;padding:20px 22px;margin:0 0 40px}
.bcg-toc p{font-weight:600;margin:0 0 10px;color:var(--bcg-nuit)}
.bcg-toc ol{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:8px}
.bcg-toc a{display:flex;gap:10px;align-items:baseline;padding:8px 12px;border-radius:12px;background:var(--bcg-sable);text-decoration:none;font-size:.93rem}
.bcg-toc a:hover{background:var(--bcg-sable-f)}
.bcg-toc b{color:var(--bcg-terre);font-variant-numeric:tabular-nums}
.bcg-step{display:grid;grid-template-columns:1fr 1fr;gap:clamp(20px,4vw,44px);align-items:center;padding:clamp(20px,3vw,32px);margin:0 0 22px;background:#fff;border-radius:22px;scroll-margin-top:110px}
.bcg-step:nth-of-type(even) .bcg-step__media{order:2}
.bcg-step img{aspect-ratio:1/1}
.bcg-step--sans-image{grid-template-columns:1fr}
.bcg-num{display:inline-flex;align-items:center;justify-content:center;width:38px;height:38px;border-radius:50%;background:var(--bcg-nuit);color:var(--bcg-sable);font-weight:600;font-variant-numeric:tabular-nums;margin:0 0 12px}
.bcg-note{display:grid;grid-template-columns:22px 1fr;gap:10px;align-items:start;padding:12px 14px;border-radius:14px;margin:0 0 10px}
.bcg-note svg{width:22px;height:22px;margin-top:2px}
.bcg-note p{margin:0}
.bcg-note strong{display:block;font-size:.82rem;letter-spacing:.04em;text-transform:uppercase;margin:0 0 2px}
.bcg-note--pourquoi{background:var(--bcg-sable)}
.bcg-note--pourquoi svg{color:var(--bcg-terre)}
.bcg-note--fiche{background:#EEF1F4}
.bcg-note--fiche svg{color:var(--bcg-nuit)}
.bcg-cap{font-size:.82rem;opacity:.75;margin:8px 2px 0}
.bcg-list{list-style:none;margin:0 0 10px;padding:0}
.bcg-list li{position:relative;padding:0 0 0 26px;margin:0 0 8px}
.bcg-list li::before{content:"";position:absolute;left:4px;top:.55em;width:9px;height:9px;border-radius:50%;background:var(--bcg-ambre)}
.bcg-check{background:var(--bcg-sable-f);border-radius:22px;padding:clamp(22px,3vw,36px);margin:34px 0 22px}
.bcg-check ul{list-style:none;margin:14px 0 0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:10px}
.bcg-check li{display:grid;grid-template-columns:24px 1fr;gap:10px;align-items:start;background:#fff;border-radius:14px;padding:12px 14px}
.bcg-check svg{width:22px;height:22px;color:var(--bcg-terre)}
.bcg-fin{background:var(--bcg-nuit);color:var(--bcg-sable);border-radius:22px;padding:clamp(24px,4vw,44px);display:grid;grid-template-columns:1.3fr 1fr;gap:24px;align-items:center;margin:22px 0 0}
.bcg-fin h2{color:var(--bcg-sable)}
.bcg-fin p{margin:0}
.bcg-fin .bcg-btns{justify-content:flex-end;margin:0}
.bcg-fin .bcg-btn--ligne{color:var(--bcg-sable)!important;border-color:rgba(247,242,234,.45)}
.bcg-fin .bcg-btn--ligne:hover{background:rgba(247,242,234,.1);border-color:var(--bcg-sable)}
.bcg-liens{display:flex;flex-wrap:wrap;gap:8px;margin:22px 0 0}
@media (max-width:749px){
.bcg-hero,.bcg-step,.bcg-fin{grid-template-columns:1fr}
.bcg-hero__media{order:-1}
.bcg-step:nth-of-type(even) .bcg-step__media{order:0}
.bcg-fin .bcg-btns{justify-content:flex-start}
.bcg-btn{width:100%;justify-content:center}
.bcg-btns{flex-direction:column}
}
@media (prefers-reduced-motion:reduce){.bcg-btn{transition:none}}
</style>"""

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
DOWN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14M6 13l6 6 6-6"/></svg>'
BULB = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.6 10.8c.6.5 1 1.2 1 2V16h5.2v-.2c0-.8.4-1.5 1-2A6 6 0 0 0 12 3z"/></svg>'
RULER = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2.5" y="7.5" width="19" height="9" rx="1.5"/><path d="M6.5 7.5v3M10.5 7.5v4M14.5 7.5v3M18.5 7.5v4"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9.5"/><path d="M8 12.5l2.6 2.6L16 9.5"/></svg>'


def btn(label, href, kind="plein", icon=ARROW):
    return f'<a class="bcg-btn bcg-btn--{kind}" href="{href}">{html.escape(label)}{icon}</a>'


def note(kind, title, text, icon):
    return (f'<div class="bcg-note bcg-note--{kind}">{icon}<p><strong>{title}</strong>{text}</p></div>')


def step(i, anchor, title, img, alt, cap, pourquoi, fiche, extra="", buttons=()):
    media = ""
    cls = "bcg-step"
    if img:
        media = (f'<div class="bcg-step__media"><img src="{IMG}{img}.jpg?width=900" alt="{html.escape(alt)}" '
                 f'width="900" height="900" loading="lazy">'
                 + (f'<p class="bcg-cap">{cap}</p>' if cap else "") + "</div>")
    else:
        cls += " bcg-step--sans-image"
    b = f'<div class="bcg-btns">{"".join(buttons)}</div>' if buttons else ""
    return (f'<section class="{cls}" id="{anchor}">{media}<div class="bcg-step__texte">'
            f'<span class="bcg-num">{i}</span><h2>{title}</h2>'
            f'{note("pourquoi", "Pourquoi c'est important", pourquoi, BULB)}'
            f'{note("fiche", "Sur la fiche produit", fiche, RULER)}{extra}{b}</div></section>')


def page(hero, steps, toc_title, check=None, fin=None, liens=()):
    eyebrow, lead, img, alt, hero_btns = hero
    out = [CSS, '<div class="bcg">']
    out.append(f'<div class="bcg-hero"><div class="bcg-hero__texte"><span class="bcg-eyebrow">{eyebrow}</span>'
               f'<p class="bcg-lead">{lead}</p><div class="bcg-btns">{"".join(hero_btns)}</div></div>'
               f'<div class="bcg-hero__media"><img src="{IMG}{img}.jpg?width=1200" alt="{html.escape(alt)}" width="1200" height="900"></div></div>')
    toc = "".join(f'<li><a href="#{s["anchor"]}"><b>{n}</b><span>{s["short"]}</span></a></li>' for n, s in enumerate(steps, 1))
    out.append(f'<nav class="bcg-toc" aria-label="Sommaire"><p>{toc_title}</p><ol>{toc}</ol></nav>')
    for n, s in enumerate(steps, 1):
        out.append(step(n, s["anchor"], s["title"], s.get("img"), s.get("alt", ""), s.get("cap", ""),
                        s["pourquoi"], s["fiche"], s.get("extra", ""), s.get("buttons", ())))
    if check:
        items = "".join(f"<li>{CHECK}<span>{c}</span></li>" for c in check[1])
        out.append(f'<section class="bcg-check" id="checklist"><h2>{check[0]}</h2><ul>{items}</ul></section>')
    if fin:
        out.append(f'<div class="bcg-fin"><div><h2>{fin[0]}</h2><p>{fin[1]}</p></div><div class="bcg-btns">{"".join(fin[2])}</div></div>')
    if liens:
        out.append(f'<div class="bcg-liens">{"".join(liens)}</div>')
    out.append("</div>")
    return "\n".join(out)


COLL_ALL = "/collections/fauteuil-allaitement"

allaitement = page(
    ("Guide Bercelou · 7 critères",
     "Vous cherchez un fauteuil pour les tétées de nuit, pas un meuble de plus dans la chambre. "
     "Ce guide reprend les sept critères sur lesquels nous sélectionnons nos modèles, et vous montre où les lire sur chaque fiche. "
     "Il est offert en ligne, à consulter avant et après votre achat.",
     "accueil-moment-tetees-nuit-carte", "Une maman berce son bébé dans un fauteuil à bascule, lumière douce du soir",
     [btn("Voir les fauteuils d'allaitement", COLL_ALL), btn("Aller à la checklist", "#checklist", "ligne", DOWN)]),
    [
        dict(anchor="hauteur", short="Hauteur d'assise", title="Une hauteur d'assise adaptée à votre façon de vous lever",
             img="fauteuil-allaitement-capitonne-poches-dimensions", alt="Fauteuil d'allaitement capitonné avec ses cotes : 86 cm de haut, assise à 53 cm",
             cap="Exemple : le fauteuil capitonné, assise à 53 cm du sol.",
             pourquoi="C'est la première question que vous vous posez : un fauteuil trop bas ou trop enveloppant complique le lever, surtout dans les premières semaines. Plus l'assise est haute, plus le passage assis-debout demande peu d'effort ; une assise basse et enveloppante invite au contraire à se lover.",
             fiche="Regardez la hauteur d'assise dans le tableau des dimensions, et comparez-la à la hauteur d'une chaise, autour de 45 cm. Pour vous lever, avancez-vous au bord de l'assise, arrêtez la bascule avec les pieds et prenez appui sur les accoudoirs.",
             buttons=(btn("Voir le fauteuil capitonné", "/products/fauteuil-allaitement-capitonne-poches"),)),
        dict(anchor="accoudoirs", short="Accoudoirs", title="Des accoudoirs larges et bien rembourrés",
             img="fauteuil-a-bascule-allaitement-lin-poches-detail", alt="Accoudoir rembourré et poche latérale d'un fauteuil à bascule en lin",
             cap="Exemple : le fauteuil en lin, accoudoirs à 70 cm du sol et une poche de chaque côté.",
             pourquoi="Vos bras reposent sur les accoudoirs pendant toute la tétée. Un accoudoir étroit, dur ou en bois nu devient inconfortable au bout de quelques minutes.",
             fiche="Consultez la hauteur et la largeur de l'accoudoir dans le tableau des dimensions, puis le matériau dans les caractéristiques : un accoudoir rembourré, recouvert du même tissu que l'assise, est un bon repère.",
             buttons=(btn("Voir le fauteuil en lin", "/products/fauteuil-a-bascule-allaitement-lin-poches"),)),
        dict(anchor="dossier", short="Dossier", title="Un dossier qui soutient la tête",
             img="fauteuil-allaitement-bouclette-pouf-appui-tete-usage", alt="Maman qui allaite, la tête posée contre l'appui-tête d'un fauteuil en bouclette, les pieds sur le pouf",
             cap="Exemple : le fauteuil en bouclette avec appui-tête et pouf assorti.",
             pourquoi="Une tétée de nuit dure parfois longtemps. Un dossier trop court oblige à garder la tête droite ou à la caler contre le mur.",
             fiche="Regardez la hauteur du dossier dans le tableau des dimensions et sa forme sur les photos : un dossier haut, un appui-tête ou des oreilles accompagnent la tête.",
             buttons=(btn("Voir le fauteuil avec appui-tête", "/products/fauteuil-allaitement-bouclette-pouf-appui-tete"),)),
        dict(anchor="bascule", short="Bascule", title="Une bascule douce et discrète",
             img="chaise-a-bascule-allaitement-bouclette-detail", alt="Chaise à bascule en bouclette blanche sur de larges patins en bois clair",
             cap="Exemple : la chaise en bouclette sur patins en bois.",
             pourquoi="Vous bercez bébé pour l'endormir : la bascule doit rester lente et ne pas attirer l'attention par un bruit de mécanisme.",
             fiche="Regardez le piétement sur les photos et dans la description : des patins larges et arrondis donnent une bascule lente et régulière. Installez le fauteuil sur un tapis épais pour une bascule encore plus discrète.",
             buttons=(btn("Voir la chaise en bouclette", "/products/chaise-a-bascule-allaitement-bouclette"),)),
        dict(anchor="place", short="Place à prévoir", title="La place à prévoir dans la chambre",
             img="rocking-chair-effet-lin-creme-bois-clair-dimensions", alt="Rocking chair effet lin avec ses cotes : 64,5 cm de large, 81,5 cm de haut, 92 cm de profondeur",
             cap="Chaque fiche donne largeur, hauteur et profondeur, comme ici.",
             pourquoi="Un fauteuil à bascule a besoin de dégagement à l'arrière pour se balancer librement, en plus de son emprise au sol.",
             fiche="Reportez-vous à la profondeur et à la largeur dans le tableau des dimensions. En repère de bon sens, prévoyez environ 50 cm de dégagement derrière le fauteuil pour une bascule libre.",
             buttons=(btn("Lire le guide taille et place", "/pages/guide-rocking-chair-taille-place", "ligne"),)),
        dict(anchor="entretien", short="Entretien du tissu", title="Un entretien simple pour le tissu",
             img="chaise-a-bascule-allaitement-bouclette-matiere", alt="Gros plan sur la bouclette blanche d'un fauteuil",
             pourquoi="Un fauteuil d'allaitement reçoit du lait et des régurgitations. Un tissu qui s'entretient facilement vous évite de vous en inquiéter.",
             fiche="Regardez la matière annoncée dans les caractéristiques. Une housse amovible et lavable n'est mentionnée que sur certains modèles : vérifiez cette mention sur la fiche avant l'achat, sinon prévoyez un entretien en place, en surface.",
             buttons=(btn("Lire le guide d'entretien", "/pages/guide-entretien-bouclette-velours-lin", "ligne"),)),
        dict(anchor="style", short="Style au salon", title="Un style qui reste au salon après bébé",
             img="accueil-moment-coin-lecture-carte", alt="Fauteuil à bascule en teddy caramel dans un coin lecture de salon",
             pourquoi="Vous n'avez pas envie d'un meuble qui ressemble à un accessoire de puériculture. Un fauteuil que vous aimez continue à servir des années après les tétées de nuit, comme coin lecture.",
             fiche="Regardez les photos en situation salon, pas seulement les photos en chambre : elles vous montrent si le fauteuil s'intègre à une déco d'adulte.",
             buttons=(btn("Voir les rocking chairs design", "/collections/rocking-chair-design-scandinave", "ligne"),)),
    ],
    "Les 7 critères",
    check=("Votre checklist avant d'acheter", [
        "J'ai regardé la hauteur d'assise et la forme du dossier",
        "J'ai regardé la largeur et le rembourrage des accoudoirs",
        "J'ai regardé la hauteur du dossier",
        "J'ai lu la description du mécanisme de bascule",
        "J'ai prévu la place nécessaire, dégagement compris",
        "J'ai regardé la matière et, si besoin, la présence d'une housse amovible",
        "J'ai regardé le fauteuil en situation salon",
    ]),
    fin=("Trouver votre fauteuil", "Parcourez la collection Allaitement avec ces sept critères en tête. Livraison offerte en France métropolitaine.",
         [btn("Voir les fauteuils d'allaitement", COLL_ALL), btn("Une question ? Contactez-nous", "/pages/contact", "ligne")]),
)

taille = page(
    ("Guide Bercelou · Taille et place",
     "Avant de choisir un modèle, cinq points valent la peine d'être vérifiés : la place au sol, le dégagement pour la bascule, "
     "la hauteur d'assise et du dossier, la charge supportée et le passage nécessaire à la livraison.",
     "accueil-berceau-coin-lecture-bandeau", "Fauteuil à bascule en bouclette dans une chambre, près d'un berceau",
     [btn("Voir les fauteuils à bascule", "/collections/fauteuil-a-bascule"), btn("Commencer par la pièce", "#piece", "ligne", DOWN)]),
    [
        dict(anchor="piece", short="Mesurer la pièce", title="Mesurer la pièce",
             img="rocking-chair-bois-blanc-dossier-a-lattes-dimensions", alt="Rocking chair en bois blanc avec ses cotes : 69 cm de large, 115 cm de haut, 86 cm de profondeur",
             cap="Exemple : 69 cm de large et 86 cm de profondeur, patins compris.",
             pourquoi="Un rocking chair est souvent plus large et plus profond à la base qu'à l'assise : ce sont les patins qui fixent l'emprise au sol.",
             fiche="Reportez l'emprise au sol, indiquée dans le tableau des dimensions, à l'endroit où vous comptez l'installer. Pensez à la largeur totale et à la profondeur, patins compris."),
        dict(anchor="degagement", short="Dégagement", title="Le dégagement pour la bascule",
             img="rocking-chair-bois-blanc-dossier-a-lattes-situation", alt="Rocking chair en bois blanc installé devant une bibliothèque, avec de l'espace derrière",
             pourquoi="Un fauteuil à bascule se balance vers l'arrière et vers l'avant : il a besoin d'espace libre des deux côtés, sans meuble ni mur trop proches.",
             fiche="Prévoyez environ 50 cm de dégagement derrière le fauteuil pour une bascule libre, et un peu d'espace devant pour vous asseoir et vous relever sans contrainte. Avec un repose-pieds, ajoutez sa profondeur devant le fauteuil."),
        dict(anchor="hauteur", short="Hauteur et dossier", title="La hauteur de l'assise et du dossier",
             img="rocking-chair-tissu-gris-cadre-bois-clair-dimensions", alt="Rocking chair en tissu gris avec ses cotes : 84 cm de haut, assise de 39 à 43 cm",
             cap="Exemple : une assise entre 39 et 43 cm du sol.",
             pourquoi="La hauteur d'assise change la façon de s'installer et de se lever ; la hauteur du dossier décide si la tête est accompagnée ou non.",
             fiche="La hauteur d'assise et la hauteur du dossier figurent dans le tableau des dimensions de chaque fiche. Comparez-les à une chaise de votre salon, autour de 45 cm d'assise.",
             buttons=(btn("Lire le guide allaitement", "/pages/guide-bien-choisir-fauteuil-allaitement", "ligne"),)),
        dict(anchor="charge", short="Charge", title="La charge à respecter",
             img="fauteuil-a-bascule-chenille-soutien-lombaire-usage", alt="Maman qui allaite dans un fauteuil à bascule en chenille, repose-pieds déplié",
             pourquoi="Un fauteuil peut accueillir un adulte et un bébé en même temps, parfois avec un enfant sur les genoux.",
             fiche="Vérifiez la charge maximale supportée, indiquée dans les caractéristiques de chaque fiche, avant l'achat."),
        dict(anchor="livraison", short="Passage des portes", title="Le passage des portes pour la livraison",
             pourquoi="Le fauteuil arrive en colis, dans son carton d'origine, et doit passer vos portes et votre couloir jusqu'à la pièce.",
             fiche="Mesurez la largeur de vos portes et de votre couloir, puis comparez-les aux dimensions du colis quand la fiche les indique. La plupart des fauteuils arrivent à assembler, notice fournie.",
             extra='<ul class="bcg-list"><li>Largeur de la porte d\'entrée</li><li>Largeur du couloir et des virages</li><li>Largeur de la porte de la pièce</li></ul>'),
    ],
    "Les 5 points à vérifier",
    fin=("Trouver votre fauteuil", "Parcourez nos rocking chairs avec ces points en tête : chaque fiche donne les cotes, la charge et, souvent, les dimensions du colis.",
         [btn("Voir les fauteuils à bascule", "/collections/fauteuil-a-bascule"), btn("Voir les fauteuils d'allaitement", COLL_ALL, "ligne")]),
)

entretien = page(
    ("Guide Bercelou · Entretien",
     "Nos fauteuils se déclinent en bouclette, velours côtelé ou lin selon les modèles. "
     "Ces matières se vivent bien au quotidien à condition de suivre quelques réflexes simples.",
     "fauteuil-pivotant-360-bouclette-matiere", "Gros plan sur la bouclette crème d'un fauteuil",
     [btn("Voir les fauteuils à bascule", "/collections/fauteuil-a-bascule"), btn("En cas de tache", "#tache", "ligne", DOWN)]),
    [
        dict(anchor="courant", short="Entretien courant", title="L'entretien courant",
             img="fauteuil-a-bascule-velours-cotele-repose-pieds-integre-matiere", alt="Gros plan sur le velours côtelé crème d'un fauteuil",
             pourquoi="La poussière s'installe dans les boucles et les côtes : un geste régulier garde la matière nette et gonflante.",
             fiche="La matière de chaque fauteuil figure dans ses caractéristiques, avec ses consignes d'entretien.",
             extra='<ul class="bcg-list"><li>Dépoussiérez avec la brosse douce de l\'aspirateur, dans le sens du poil pour la bouclette et le velours.</li><li>Aérez la pièce de temps en temps : une matière textile respire mieux dans un intérieur ventilé.</li><li>Évitez le plein soleil prolongé pour préserver la couleur du tissu.</li></ul>'),
        dict(anchor="tache", short="En cas de tache", title="En cas de tache",
             img="rocking-chair-effet-lin-creme-bois-clair-matiere", alt="Gros plan sur le tissu effet lin crème d'un rocking chair",
             pourquoi="Plus une tache reste en place, plus elle est difficile à faire partir.",
             fiche="L'étiquette d'entretien cousue sur votre fauteuil prime toujours sur ces conseils généraux.",
             extra='<ul class="bcg-list"><li>Intervenez rapidement.</li><li>Épongez sans frotter, avec un chiffon propre et sec.</li><li>Testez votre produit sur une zone cachée avant de l\'appliquer sur la tache.</li><li>Tamponnez avec un peu d\'eau tiède et de savon doux, puis laissez sécher à l\'air libre, loin d\'une source de chaleur.</li></ul>'),
        dict(anchor="housses", short="Housses amovibles", title="Les housses amovibles",
             img="pouf-rond-velours-cotele-moelleux-detail", alt="Mains qui ouvrent la housse zippée d'un pouf en velours côtelé vert",
             cap="Exemple : la housse zippée du pouf rond en velours côtelé.",
             pourquoi="Une housse qui se retire se lave en machine, sans nettoyage en place.",
             fiche="Certains modèles disposent d'une housse amovible et lavable : c'est indiqué sur la fiche produit lorsque c'est le cas. Reportez-vous à l'étiquette de la housse pour la température de lavage. Sans housse amovible, l'entretien se fait en place, en surface.",
             buttons=(btn("Voir les poufs", "/collections/pouf"), btn("Voir les repose-pieds", "/collections/repose-pieds", "ligne"))),
    ],
    "Au sommaire",
    fin=("Trouver votre fauteuil", "Vérifiez la matière annoncée sur chaque fiche avant de choisir : bouclette, velours côtelé, lin ou chenille.",
         [btn("Voir les fauteuils à bascule", "/collections/fauteuil-a-bascule"), btn("Lire le guide allaitement", "/pages/guide-bien-choisir-fauteuil-allaitement", "ligne")]),
)

out = {"guide-bien-choisir-fauteuil-allaitement": allaitement,
       "guide-rocking-chair-taille-place": taille,
       "guide-entretien-bouclette-velours-lin": entretien}
for k, v in out.items():
    assert "—" not in v and "–" not in v, k
    (ROOT / f"{k}.html").write_text(v)
json.dump(out, open(ROOT / "bodies.json", "w"), ensure_ascii=False)
print({k: len(v) for k, v in out.items()})

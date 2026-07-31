# Modèle de page produit Shopify Horizon — référence Notion

Date de capture : 18 juillet 2026  
Boutique source : Bonum Vitae (`bonumvitae.fr`)  
Thème source : Horizon, actuellement publié (`MAIN`)  
ID du thème : `gid://shopify/OnlineStoreTheme/203569004882`

## Objectif

Ce document décrit la structure réelle de la page produit Horizon de Bonum Vitae et rassemble les blocs Liquid personnalisés utilisés. Il sert de référence pour Notion et pour reconstruire ce modèle sur de futures boutiques.

Il faut distinguer trois niveaux :

1. **Architecture CRO réutilisable** : ordre des informations, bénéfices, livraison, réassurance, accordéons, avis et recommandations.
2. **Blocs Liquid portables après adaptation** : note, paiement fractionné, bénéfices, livraison, réassurance et carrousel d’avis.
3. **JSON propre à Horizon** : identifiants générés, hiérarchie de blocs, app blocks et paramètres du thème. Ne pas copier ce JSON dans un autre thème sans lire les schémas du thème cible.

## Fichiers source exacts

- `templates/product.json` : modèle produit par défaut, 83 Ko.
- `templates/product.osmoseur.json` : modèle spécifique osmoseur, 87 Ko.
- `sections/bv-avis-clients.liquid` : section originale d’avis clients, sans dépendance externe.
- `blocks/buy-buttons.liquid` : bloc d’achat Horizon modifié.
- `custom-liquid/*.liquid` : six blocs extraits séparément.

Dossier :

`/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/`

## Structure générale de la page produit

### Zone principale

La section principale est de type `product-information`, avec une galerie média et une colonne d’informations.

Ordre exact de la colonne d’informations :

1. Ligne de note et nombre d’avis.
2. Groupe d’en-tête :
   - titre dynamique ;
   - prix et prix comparé ;
   - paiement en quatre fois PayPal/Klarna.
3. Quatre bénéfices produit.
4. Séparateur.
5. Sélecteur de variantes.
6. Barre de livraison.
7. Bloc d’achat :
   - quantité ;
   - Ajouter au panier ;
   - paiement accéléré retiré du rendu de `buy-buttons.liquid`.
8. Cartes de réassurance et contact.
9. Accordéons produit.

Réglages structurants : média à gauche sur ordinateur, colonnes équilibrées, première image mise en avant, zoom média, détails sticky et ajout au panier sticky.

### Accordéons de la zone d’achat

1. Description dynamique.
2. Livraison et retour.
3. Fabrication.
4. Garantie 2 ans.
5. Contactez-nous.

Les délais, transporteurs, garantie, téléphone et promesses de retour doivent être adaptés et prouvés avant publication.

### Sections sous la zone d’achat — modèle par défaut

1. Avis clients personnalisés.
2. Produits recommandés — « Complétez votre installation ».
3. USP 1 — Écosystème.
4. USP 2 — Installation.
5. USP 3 — Transparence.
6. USP 4 — Gamme.
7. FAQ — Objections.
8. Widget TrustWILL / Trustoo.
9. Deuxième section de produits recommandés.

Le modèle contient donc deux systèmes d’avis et deux sections de recommandations. Pour une nouvelle boutique, choisir une seule source d’avis et une seule zone de recommandations sauf justification CRO précise.

### Différence du modèle osmoseur

`product.osmoseur.json` ajoute une section **Infographies osmoseur** avec :

- `osmoseur-schema-osmose-inverse.png` ;
- `osmoseur-info-specs.png` ;
- `osmoseur-info-benefices.png`.

Les bénéfices du haut de page sont également spécifiques à l’osmoseur.

## Blocs Liquid personnalisés extraits et validés

Les archives JSON conservent le code exact du thème. Les copies ci-dessous ajoutent uniquement les attributs d'image exigés par la validation Shopify actuelle.

### 1. Ligne de note et d’avis

Emplacement : avant le titre.

```liquid
<a href="#shopify-section-template--20012964675850__trustpilot_7FTrR8"
style="text-decoration: none;">
<div style="display: flex; align-items: center; margin-top: 0px; margin-bottom: 0px;
font-family: inherit;">
<img src="https://cdn.shopify.com/s/files/1/0776/3751/7627/files/avis.png?v=1687213619"
alt="" width="80" height="16" style="height: 16px; width: auto; margin-right: 6px;">
<span style="font-size: 12px; color: inherit; font-weight: normal;"><strong>4.8/5</strong>
basé sur 312 avis vérifiés</span>
</div>
</a>
```

Risques :

- `4.8/5` et `312 avis vérifiés` codés en dur ;
- ancre de section propre à une ancienne configuration ;
- image chargée depuis un CDN tiers ;
- ne jamais afficher « vérifié » sans preuve réelle.

### 2. Paiement en quatre fois PayPal/Klarna

Emplacement : sous le prix.

```liquid
<style>
.payment-installments {
display: flex;
align-items: center;
gap: 6px;
margin-top: -20px;
font-family: var(--font-body-family);
font-size: 13px;
color: #475569;
}
.payment-installments .price {
font-weight: 530;
color: #1e293b;
}
.payment-logos {
display: flex;
align-items: center;
gap: 6px;
}
.payment-logos img {
height: 20px;
width: auto;
}
.payment-logos .paypal-card {
background: white;
border: 1px solid #e2e8f0;
border-radius: 4px;
padding: 3px 6px;
}
.payment-logos .klarna-card {
height: 20px;
width: auto;
}
.payment-logos span {
font-size: 12px;
color: #64748b;
}
</style>
<div class="payment-installments">
{% assign price = product.selected_or_first_available_variant.price | divided_by: 100.0 %}
{% assign installment = price | divided_by: 4 | round: 2 %}
<span>Ou 4x <span class="price">{{ installment }}€</span> avec</span>
<div class="payment-logos">
<img class="paypal-card"
src="https://cdn.shopify.com/s/files/1/0941/1667/5917/files/2_f6abbd15-09dc-434d-81bf-fa03
92a7ea0c.svg?v=1767533573" alt="PayPal" width="64" height="20">
<span>et</span>
<img class="klarna-card"
src="https://cdn.shopify.com/s/files/1/0941/1667/5917/files/1.svg?v=1767533573"
alt="Klarna" width="40" height="20">
</div>
</div>
```

Risques :

- logos liés au CDN d’une autre boutique ;
- calcul purement visuel, sans contrôle d’éligibilité ;
- montant non formaté avec la locale ;
- ne pas promettre PayPal/Klarna s’ils ne sont pas activés.

### 3. Bénéfices génériques

Emplacement : sous PayPal/Klarna et avant le séparateur.

```liquid
<style>.bv-benef{list-style:none;margin:10px 0 2px;padding:0;display:flex;flex-direction:column;gap:11px;font-family:var(--font-body--family,'Inter',sans-serif);}.bv-benef li{display:flex;align-items:center;gap:11px;font-size:14px;line-height:1.3;color:#1C2830;}.bv-benef .bic{width:28px;height:28px;flex-shrink:0;border-radius:50%;background:#EAF3F1;display:flex;align-items:center;justify-content:center;}.bv-benef .bic svg{width:16px;height:16px;fill:none;stroke:#0E3A5A;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;}</style><ul class="bv-benef"><li><span class="bic"><svg viewBox="0 0 24 24"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.7-3.7a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9l-3.7 3.7z"/></svg></span>S'installe soi-même, sans plombier</li><li><span class="bic"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></span>Prêt à poser en quelques minutes</li><li><span class="bic"><svg viewBox="0 0 24 24"><path d="M12 3l7 3v5c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/><path d="M9 12l2 2 4-4"/></svg></span>Sélectionné pour sa fiabilité</li><li><span class="bic"><svg viewBox="0 0 24 24"><path d="M21 11.5a8.5 8.5 0 0 1-12.5 7.5L3 21l2-5.5A8.5 8.5 0 1 1 21 11.5z"/></svg></span>Conseil d'expert avant l'achat</li></ul>
```

Ces textes ne sont pas universels. Remplacer les quatre bénéfices par des affirmations vérifiées pour le produit.

### 4. Bénéfices spécifiques à l’osmoseur

```liquid
<style>.bv-benef{list-style:none;margin:10px 0 2px;padding:0;display:flex;flex-direction:column;gap:11px;font-family:var(--font-body--family,'Inter',sans-serif);}.bv-benef li{display:flex;align-items:center;gap:11px;font-size:14px;line-height:1.3;color:#1C2830;}.bv-benef .bic{width:28px;height:28px;flex-shrink:0;border-radius:50%;background:#EAF3F1;display:flex;align-items:center;justify-content:center;}.bv-benef .bic svg{width:16px;height:16px;fill:none;stroke:#0E3A5A;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;}</style><ul class="bv-benef"><li><span class="bic"><svg viewBox="0 0 24 24"><path d="M12 2.7C12 2.7 5.5 9.5 5.5 14.5a6.5 6.5 0 0 0 13 0C18.5 9.5 12 2.7 12 2.7z"/></svg></span>Eau filtrée à la demande, sans réservoir</li><li><span class="bic"><svg viewBox="0 0 24 24"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.7-3.7a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9l-3.7 3.7z"/></svg></span>S'installe sous l'évier, sans plombier</li><li><span class="bic"><svg viewBox="0 0 24 24"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z"/><path d="M2 22 17 7"/></svg></span>Rejet optimisé 2:1 — moins de gaspillage d'eau</li><li><span class="bic"><svg viewBox="0 0 24 24"><path d="M12 3l1.9 4.8L19 9.5l-5.1 1.7L12 16l-1.9-4.8L5 9.5l5.1-1.7z"/></svg></span>Une eau plus agréable au goût</li></ul>
```

Ne pas reprendre les affirmations sur le goût, l’installation ou le ratio de rejet sans preuve propre au modèle vendu.

### 5. Barre de livraison

Emplacement : après les variantes et avant le bouton d’achat.

```liquid
<style>
.shipping-bar {
display: inline-flex;
justify-content: space-between;
align-items: center;
background: #f1f1f1;
padding: 5px 12px;
border-radius: 6px;
font-size: 12px;
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
gap: 16px;
width: 100%;
box-sizing: border-box;
}
.shipping-left,
.shipping-right {
display: flex;
align-items: center;
gap: 6px;
}
.shipping-dot {
width: 8px;
height: 8px;
background: #6f8a8a;
border-radius: 50%;
flex-shrink: 0;
}
.shipping-bold {
font-weight: 700;
}
</style>
<div class="shipping-bar">
<div class="shipping-left">
<div class="shipping-dot"></div>
{% assign delivery_timestamp = 'now' | date: '%s' | plus: 518400 %}
{% assign day_en = delivery_timestamp | date: "%a" %}
{% assign day_number = delivery_timestamp | date: "%d" %}
{% assign month_en = delivery_timestamp | date: "%b" %}
{% assign days = "Mon:Lun,Tue:Mar,Wed:Mer,Thu:Jeu,Fri:Ven,Sat:Sam,Sun:Dim" | split: ","
%}
{% assign months =
"Jan:janv,Feb:fév,Mar:mars,Apr:avr,May:mai,Jun:juin,Jul:juil,Aug:août,Sep:sept,Oct:oct,Nov:
nov,Dec:dec" | split: "," %}
{% for d in days %}{% assign pair = d | split: ":" %}{% if pair[0] == day_en %}{% assign
day_fr = pair[1] %}{% endif %}{% endfor %}
{% for m in months %}{% assign pair = m | split: ":" %}{% if pair[0] == month_en %}{% assign
month_fr = pair[1] %}{% endif %}{% endfor %}
<span>Livré le <span class="shipping-bold">{{ day_fr }}. {{ day_number }} {{ month_fr
}}</span></span>
</div>
<div class="shipping-right">
<span> Livraison <span class="shipping-bold">Gratuite</span></span>
</div>
</div>
```

La date actuelle correspond à « aujourd’hui + six jours ». Ce n’est pas une donnée logistique réelle. Une version réutilisable doit lire le délai depuis la variante, le fournisseur, un métachamp ou une règle documentée.

### 6. Réassurance et contact

Emplacement : sous le bloc d’achat.

```liquid
<style>
.trust-blocks {
  width: 100%;
  margin: 0;
  padding: 0;
}
.trust-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  margin-bottom: 8px;
}
.trust-card {
  background: #F7F4EE;
  border: 1px solid #0E3A5A;
  border-radius: 12px;
  padding: 16px 8px;
  text-align: center;
}
.trust-icon {
  width: 40px;
  height: 40px;
  margin: 0 auto 8px;
  background: #0E3A5A;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.trust-icon svg {
  width: 20px;
  height: 20px;
  stroke: #ffffff;
  fill: none;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}
.trust-title {
  font-family: var(--font-body--family, var(--font-body-family, 'Inter', sans-serif));
  font-size: 8.5px;
  font-weight: 700;
  color: #0E3A5A;
  margin: 0;
  line-height: 1.2;
  text-transform: uppercase;
  letter-spacing: 0.01em;
}
.contact-block {
  background: #F7F4EE;
  border: 1px solid #0E3A5A;
  border-radius: 12px;
  padding: 16px;
  text-align: left;
}
.contact-block p {
  font-family: var(--font-body--family, var(--font-body-family, 'Inter', sans-serif));
  font-size: 13px;
  color: #3A4750;
  margin: 0;
  line-height: 1.5;
}
.contact-block a {
  color: #0E3A5A;
  text-decoration: none;
  font-weight: 600;
}
.contact-block a:hover {
  text-decoration: underline;
}
</style>
<div class="trust-blocks">
  <div class="trust-grid">
    <div class="trust-card">
      <div class="trust-icon">
        <svg viewBox="0 0 24 24">
          <rect x="1" y="3" width="15" height="13"></rect>
          <path d="M16 8h5l3 3v5h-2"></path>
          <circle cx="5.5" cy="18.5" r="2.5"></circle>
          <circle cx="18.5" cy="18.5" r="2.5"></circle>
        </svg>
      </div>
      <h3 class="trust-title">LIVRAISON OFFERTE<br>EN FRANCE</h3>
    </div>
    <div class="trust-card">
      <div class="trust-icon">
        <svg viewBox="0 0 24 24">
          <circle cx="12" cy="12" r="10"></circle>
          <path d="M9 12l2 2 4-4"></path>
        </svg>
      </div>
      <h3 class="trust-title">14 JOURS SATISFAIT<br>OU REMBOURSÉ</h3>
    </div>
    <div class="trust-card">
      <div class="trust-icon">
        <svg viewBox="0 0 24 24">
          <path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"></path>
        </svg>
      </div>
      <h3 class="trust-title">SERVICE CLIENT<br>EN FRANÇAIS</h3>
    </div>
  </div>
  <div class="contact-block">
    <p>
      Nous sommes à votre écoute pour toute question. Veuillez nous écrire à
      <a href="mailto:contact@bonumvitae.fr">contact@bonumvitae.fr</a>
      ou par téléphone au
      <a href="tel:+33756828094">07 56 82 80 94</a>.
    </p>
  </div>
</div>
```

À paramétrer par boutique : livraison, rétractation, service client, e-mail, téléphone, horaires et couleurs.

## Accordéons exacts

### Description

```liquid
{{ closest.product.description }}
```

### Livraison et retour

```html
<ul>
  <li>Livraison offerte en France : 4-8 jours</li>
  <li>Retours gratuits sous 14 jours</li>
</ul>
<p>Livraison suivie et assurée à domicile avec : Colissimo / DHL / Fedex / Chronopost</p>
```

### Fabrication

```html
<p>Nos produits sont fabriqués localement et dans le monde entier. Nous sélectionnons soigneusement nos partenaires de fabrication pour garantir que nos produits sont de haute qualité et d’un juste rapport qualité-prix.</p>
```

### Garantie

```html
<p>Nos produits sont garantis 2 ans selon la législation française.</p>
```

### Contact

```html
<p>Une question avant d'acheter ? Notre service client vous répond en français, du lundi au vendredi de 9 h à 18 h. Écrivez-nous à <a href="mailto:contact@bonumvitae.fr">contact@bonumvitae.fr</a> ou appelez le 07 56 82 80 94.</p>
```

## Section complète d’avis clients

Fichier : `sections/bv-avis-clients.liquid`.

La section est originale, utilise `scroll-snap` et n’a pas besoin de Swiper. Les avis, auteurs, dates, notes et badges « Vérifié » doivent provenir de vrais avis traçables. Les avis configurés historiquement dans le JSON Horizon ont servi au test de construction : ne pas les republier ni les réutiliser comme preuve sans justificatif.

```liquid
{% comment %}
  Bonum Vitae — Section "Avis clients" (carrousel).
  Section originale, sans dépendance externe (défilement natif scroll-snap).
{% endcomment %}

{%- liquid
  assign align = section.settings.heading_alignment
-%}

<style>
  #bv-avis-{{ section.id }} {
    --bv-stars: {{ section.settings.stars_color }};
    --bv-cardbg: {{ section.settings.card_background }};
    --bv-border: {{ section.settings.card_border }};
    --bv-title: {{ section.settings.title_color }};
    --bv-text: {{ section.settings.text_color }};
    --bv-cards: {{ section.settings.cards }};
    {% if section.settings.background != blank %}background: {{ section.settings.background }};{% endif %}
    padding-top: {{ section.settings.padding_top }}px;
    padding-bottom: {{ section.settings.padding_bottom }}px;
  }
  #bv-avis-{{ section.id }} .bv-avis__inner { max-width: 1200px; margin: 0 auto; padding-inline: 20px; }
  #bv-avis-{{ section.id }} .bv-avis__heading {
    font-family: var(--font-heading--family, var(--font-heading-family, 'Fraunces', serif));
    color: var(--bv-title); font-size: clamp(22px, 3vw, 30px); line-height: 1.15;
    margin: 0 0 20px; text-align: {{ align }};
  }
  #bv-avis-{{ section.id }} .bv-avis__viewport { position: relative; }
  #bv-avis-{{ section.id }} .bv-avis__track {
    display: flex; gap: 16px; list-style: none; margin: 0; padding: 4px 2px 8px;
    overflow-x: auto; scroll-snap-type: x mandatory; scrollbar-width: none;
    -webkit-overflow-scrolling: touch;
  }
  #bv-avis-{{ section.id }} .bv-avis__track::-webkit-scrollbar { display: none; }
  #bv-avis-{{ section.id }} .bv-avis__card {
    flex: 0 0 calc((100% - (var(--bv-cards) - 1) * 16px) / var(--bv-cards));
    scroll-snap-align: start; box-sizing: border-box;
    background: var(--bv-cardbg); border: 1px solid var(--bv-border); border-radius: 12px;
    padding: 20px; box-shadow: 0 2px 10px rgba(14, 58, 90, 0.05);
    display: flex; flex-direction: column;
    font-family: var(--font-body--family, var(--font-body-family, 'Inter', sans-serif));
  }
  #bv-avis-{{ section.id }} .bv-avis__top { display: flex; align-items: center; gap: 8px; margin-bottom: 12px; }
  #bv-avis-{{ section.id }} .bv-stars { display: inline-flex; gap: 3px; }
  #bv-avis-{{ section.id }} .bv-star {
    width: 22px; height: 22px; border-radius: 4px; background: #e6e6e6;
    display: inline-flex; align-items: center; justify-content: center;
  }
  #bv-avis-{{ section.id }} .bv-star.is-on { background: var(--bv-stars); }
  #bv-avis-{{ section.id }} .bv-star svg { width: 14px; height: 14px; fill: #fff; }
  #bv-avis-{{ section.id }} .bv-verified { display: inline-flex; align-items: center; gap: 5px; margin-left: auto; font-size: 12px; color: #6b7280; white-space: nowrap; }
  #bv-avis-{{ section.id }} .bv-verified__dot { width: 16px; height: 16px; border-radius: 50%; background: #9aa4ad; display: inline-flex; align-items: center; justify-content: center; }
  #bv-avis-{{ section.id }} .bv-verified__dot svg { width: 9px; height: 9px; stroke: #fff; fill: none; stroke-width: 3; stroke-linecap: round; stroke-linejoin: round; }
  #bv-avis-{{ section.id }} .bv-avis__title { font-weight: 700; color: var(--bv-title); font-size: 15px; margin: 0 0 6px; line-height: 1.25; }
  #bv-avis-{{ section.id }} .bv-avis__text { color: var(--bv-text); font-size: 14px; line-height: 1.55; margin: 0 0 14px; }
  #bv-avis-{{ section.id }} .bv-avis__meta { color: var(--bv-text); font-size: 13px; margin: auto 0 0; }
  #bv-avis-{{ section.id }} .bv-avis__meta strong { color: var(--bv-title); font-weight: 600; }
  #bv-avis-{{ section.id }} .bv-avis__nav {
    position: absolute; top: 50%; transform: translateY(-50%); z-index: 2;
    width: 40px; height: 40px; border-radius: 50%; border: 1px solid var(--bv-border);
    background: #fff; color: var(--bv-title); font-size: 22px; line-height: 1; cursor: pointer;
    display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 8px rgba(14,58,90,.1);
  }
  #bv-avis-{{ section.id }} .bv-avis__nav:hover { background: var(--bv-title); color: #fff; }
  #bv-avis-{{ section.id }} .bv-avis__nav--prev { left: -8px; }
  #bv-avis-{{ section.id }} .bv-avis__nav--next { right: -8px; }
  @media (max-width: 749px) {
    #bv-avis-{{ section.id }} .bv-avis__card { flex-basis: 82%; }
    #bv-avis-{{ section.id }} .bv-avis__nav { display: none; }
  }
</style>

<div id="bv-avis-{{ section.id }}" class="bv-avis">
  <div class="bv-avis__inner">
    {%- if section.settings.heading != blank -%}
      <h2 class="bv-avis__heading">{{ section.settings.heading | escape }}</h2>
    {%- endif -%}

    <div class="bv-avis__viewport">
      {%- if section.blocks.size > section.settings.cards -%}
        <button class="bv-avis__nav bv-avis__nav--prev" type="button" aria-label="Précédent" data-dir="-1">&#8249;</button>
      {%- endif -%}

      <ul class="bv-avis__track" role="list">
        {%- for block in section.blocks -%}
          {%- assign r = block.settings.rating -%}
          <li class="bv-avis__card" {{ block.shopify_attributes }}>
            <div class="bv-avis__top">
              <div class="bv-stars" role="img" aria-label="Note : {{ r }} sur 5">
                {%- for i in (1..5) -%}
                  <span class="bv-star{% if i <= r %} is-on{% endif %}">
                    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l2.9 6.3 6.9.7-5.1 4.6 1.4 6.8L12 17.8 5.9 20.4l1.4-6.8L2.2 9l6.9-.7z"/></svg>
                  </span>
                {%- endfor -%}
              </div>
              {%- if block.settings.verified -%}
                <span class="bv-verified">
                  <span class="bv-verified__dot"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg></span>Vérifié
                </span>
              {%- endif -%}
            </div>

            {%- if block.settings.title != blank -%}
              <p class="bv-avis__title">{{ block.settings.title | escape }}</p>
            {%- endif -%}
            {%- if block.settings.text != blank -%}
              <p class="bv-avis__text">{{ block.settings.text | escape | newline_to_br }}</p>
            {%- endif -%}
            {%- if block.settings.author != blank or block.settings.date_text != blank -%}
              <p class="bv-avis__meta">
                {%- if block.settings.author != blank -%}<strong>{{ block.settings.author | escape }}</strong>{%- endif -%}
                {%- if block.settings.author != blank and block.settings.date_text != blank -%}, {% endif -%}
                {%- if block.settings.date_text != blank -%}{{ block.settings.date_text | escape }}{%- endif -%}
              </p>
            {%- endif -%}
          </li>
        {%- endfor -%}
      </ul>

      {%- if section.blocks.size > section.settings.cards -%}
        <button class="bv-avis__nav bv-avis__nav--next" type="button" aria-label="Suivant" data-dir="1">&#8250;</button>
      {%- endif -%}
    </div>
  </div>
</div>

<script>
  (function () {
    var root = document.getElementById('bv-avis-{{ section.id }}');
    if (!root) return;
    var track = root.querySelector('.bv-avis__track');
    root.querySelectorAll('.bv-avis__nav').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var card = track.querySelector('.bv-avis__card');
        var step = card ? card.getBoundingClientRect().width + 16 : 320;
        track.scrollBy({ left: step * parseInt(btn.getAttribute('data-dir'), 10), behavior: 'smooth' });
      });
    });
  })();
</script>

{% schema %}
{
  "name": "Avis clients",
  "tag": "section",
  "class": "bv-avis-section",
  "settings": [
    { "type": "text", "id": "heading", "label": "Titre", "default": "Ils ont adopté Bonum Vitae" },
    { "type": "select", "id": "heading_alignment", "label": "Alignement du titre", "options": [ { "value": "left", "label": "Gauche" }, { "value": "center", "label": "Centré" } ], "default": "left" },
    { "type": "header", "content": "Cartes" },
    { "type": "range", "id": "cards", "label": "Cartes visibles (desktop)", "min": 2, "max": 4, "step": 1, "default": 3 },
    { "type": "color", "id": "card_background", "label": "Fond des cartes", "default": "#FFFFFF" },
    { "type": "color", "id": "card_border", "label": "Bordure des cartes", "default": "#E7E2D6" },
    { "type": "color", "id": "title_color", "label": "Couleur des titres", "default": "#0E3A5A" },
    { "type": "color", "id": "text_color", "label": "Couleur du texte", "default": "#3A4750" },
    { "type": "color", "id": "stars_color", "label": "Couleur des étoiles", "default": "#35B6AA" },
    { "type": "header", "content": "Section" },
    { "type": "color", "id": "background", "label": "Fond de section" },
    { "type": "range", "id": "padding_top", "label": "Marge haut", "min": 0, "max": 100, "step": 4, "unit": "px", "default": 40 },
    { "type": "range", "id": "padding_bottom", "label": "Marge bas", "min": 0, "max": 100, "step": 4, "unit": "px", "default": 40 }
  ],
  "blocks": [
    {
      "type": "review",
      "name": "Avis",
      "limit": 20,
      "settings": [
        { "type": "range", "id": "rating", "label": "Note (étoiles)", "min": 1, "max": 5, "step": 1, "default": 5 },
        { "type": "checkbox", "id": "verified", "label": "Badge « Vérifié »", "default": true },
        { "type": "text", "id": "title", "label": "Titre de l'avis" },
        { "type": "textarea", "id": "text", "label": "Texte de l'avis" },
        { "type": "text", "id": "author", "label": "Auteur" },
        { "type": "text", "id": "date_text", "label": "Date (texte libre)", "default": "Il y a 2 jours" }
      ]
    }
  ],
  "presets": [
    {
      "name": "Avis clients",
      "blocks": [
        { "type": "review", "settings": { "rating": 5, "verified": true, "title": "Exemple d'avis à remplacer", "text": "Remplacez ce texte par un vrai avis client.", "author": "Prénom", "date_text": "Il y a 3 jours" } },
        { "type": "review", "settings": { "rating": 5, "verified": true, "title": "Exemple d'avis à remplacer", "text": "Remplacez ce texte par un vrai avis client.", "author": "Prénom", "date_text": "Il y a 1 semaine" } },
        { "type": "review", "settings": { "rating": 4, "verified": true, "title": "Exemple d'avis à remplacer", "text": "Remplacez ce texte par un vrai avis client.", "author": "Prénom", "date_text": "Il y a 2 semaines" } }
      ]
    }
  ]
}
{% endschema %}
```

## Sections éditoriales longues

### USP 1 — Écosystème

- Surtitre : « Notre mission ».
- Titre : « Une eau meilleure, à chaque point de la maison ».
- Rôle : présenter l’écosystème de gamme.
- CTA : « Découvrir toutes les solutions ».

### USP 2 — Installation

- Surtitre : « En quelques minutes ».
- Titre : « Installation facile, sans plombier ».
- Rôle : réduire la peur de l’installation.
- À adapter à la complexité réelle du produit.

### USP 3 — Transparence

- Surtitre : « Notre engagement ».
- Titre : « On vous dit ce qui est prouvé — et ce qui ne l’est pas ».
- Rôle : cadrer performances, limites et certifications.

### USP 4 — Gamme

- Surtitre : « Du filtre à l’osmoseur ».
- Titre : « Une solution pour chaque besoin et chaque budget ».
- Rôle : présenter gamme, accessoires et consommables.
- CTA : « Explorer la gamme ».

### FAQ — Objections

Questions actuelles :

1. Comment choisir la solution adaptée à mon eau ?
2. Faut-il des travaux ou un plombier ?
3. Vos produits sont-ils vraiment efficaces ?
4. Les dispositifs anti-calcaire adoucissent-ils l’eau ?
5. Combien coûte l’entretien ? Y a-t-il un abonnement ?
6. Quels sont les délais de livraison et les retours ?

Pour une autre niche, conserver la logique d’objections mais réécrire toutes les réponses selon le produit, le fournisseur et les politiques réelles.

## Données à stocker dans Notion

### Boutique

- marque, palette et typographies ;
- e-mail, téléphone et horaires ;
- pays, frais et délais réels ;
- politique de retour ;
- moyens de paiement activés ;
- garantie applicable ;
- application d’avis ;
- politiques légales.

### Produit

- titre, description et prix ;
- prix comparé justifiable ;
- quatre bénéfices prouvés ;
- variantes ;
- dimensions, matériaux et contenu ;
- compatibilités ;
- prise, tension et alimentation ;
- délai par entrepôt ;
- limites et exclusions ;
- installation ;
- entretien et consommables ;
- documents de conformité ;
- FAQ ;
- médias et textes alternatifs ;
- avis réels avec source ;
- produits complémentaires.

### Preuves

Pour chaque affirmation :

- formulation autorisée ;
- source et URL/fichier ;
- date de vérification ;
- variante concernée ;
- statut : confirmé, conditionnel ou interdit ;
- responsable de la vérification.

## Matrice de portabilité

| Élément | Portable ? | Action |
|---|---|---|
| Ordre CRO | Oui | Reproduire dans le thème cible |
| Custom Liquid | Partiellement | Adapter textes, classes, CDN et données |
| `bv-avis-clients.liquid` | Partiellement | Valider et brancher de vrais avis |
| `product*.json` | Non | Reconstruire selon les schémas cibles |
| IDs Horizon | Non | Générer de nouveaux IDs |
| App block TrustWILL | Non | Installer/configurer l’app |
| Médias `shopify://shop_images/...` | Non | Importer dans la nouvelle boutique |
| Coordonnées Bonum Vitae | Non | Remplacer |
| `4.8/5 — 312 avis` | Non | Utiliser une source réelle et dynamique |
| Architecture du panier | Oui | Reproduire l’ordre fonctionnel dans le thème cible |
| Code du tiroir Horizon | Partiellement | Adapter aux composants du thème cible |
| Texte de livraison et handles d’upsell | Non | Vérifier puis remplacer par boutique |
| Architecture de la homepage | Oui | Reproduire l’ordre éditorial et commercial |
| `templates/index.json` Horizon | Non | Reconstruire selon les schémas du thème cible |
| Avis, annonces, FAQ et comparatif | Partiellement | Conserver comme modèle puis relier aux preuves réelles |

## Extension homepage

La source comprend désormais la homepage complète, du bandeau d’annonce au footer :

`homepage/HORIZON-HOMEPAGE-NOTION.md`

Elle documente le header, les menus, le hero, les produits, les collections, les avis, la FAQ, la réassurance, le comparatif, la newsletter et le footer. Les sources exactes sont archivées dans `homepage/`. Le prompt dédié à Claude se trouve dans `PROMPT-CLAUDE-IMPORT-NOTION-HOMEPAGE.md`.

## Extension panier

La page produit est maintenant accompagnée d’une référence complète du panier :

`cart/HORIZON-PANIER-NOTION.md`

Elle documente le tiroir Horizon, la page panier, la bannière de livraison, l’upsell codé en dur, la note de commande, le code promotionnel, le récapitulatif, le paiement et les recommandations de produits. Les sources exactes du thème publié sont archivées dans `cart/`, avec une version isolée des personnalisations dans `cart/custom-liquid/cart-drawer-customizations.liquid`.

## Prompt de transmission à Claude

```text
Tu dois organiser dans Notion le modèle de page produit Shopify Horizon utilisé comme référence.

SOURCE PRINCIPALE
/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/HORIZON-PAGE-PRODUIT-NOTION.md

FICHIERS SOURCE
/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/templates/product.json
/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/templates/product.osmoseur.json
/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/sections/bv-avis-clients.liquid
/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/blocks/buy-buttons.liquid
/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/custom-liquid/
/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/cart/HORIZON-PANIER-NOTION.md
/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/cart/
/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/homepage/HORIZON-HOMEPAGE-NOTION.md
/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/docs/horizon-product-page-reference/homepage/

MISSION
1. Lis le document et les fichiers source.
2. Organise Notion avec : architecture de la page produit, architecture du panier, architecture de la homepage, données boutique, données produit, preuves, blocs Liquid, avis, checklist de construction et QA.
3. Conserve chaque bloc Liquid de la page produit, du panier et de la homepage séparément avec emplacement, dépendances et valeurs à remplacer.
4. Ne copie pas le JSON Horizon dans un autre thème sans lire ses schémas.
5. Ne réutilise pas IDs, app blocks, CDN, coordonnées, notes, avis, garanties ou délais comme valeurs universelles.
6. Ne republie aucun avis historique sans preuve.
7. Reconstruis l’ordre CRO dans le thème cible et adapte les composants.
8. Lie chaque promesse produit à une preuve dans Notion.
9. Avant toute écriture Shopify, vérifie le thème publié et précise si l’action touche le thème ou les données produit en ligne.
10. Pour le panier, sépare les fonctions natives Horizon des ajouts Bonum Vitae.
11. Enregistre la bannière de livraison et les quatre handles d’upsell comme valeurs de modèle à personnaliser, pas comme règles universelles.
12. Documente les réglages : tiroir, ouverture automatique, note, code promo, paiements accélérés et recommandations.
13. Ne copie pas le tiroir Horizon dans un autre thème sans adapter ses composants JavaScript, ses variables CSS et ses schémas.
14. Ajoute une checklist de test couvrant quantités, suppression, remises, variantes d’upsell, paiement et mobile.
15. Pour la homepage, conserve l’ordre du header au footer et sépare les composants Horizon du comparatif et des avis personnalisés.
16. Enregistre les annonces, avis, délais, retours, remises newsletter, coordonnées et liens comme valeurs à vérifier ou à remplacer.
17. Ne traite pas un badge d’avis vérifié, une remise affichée ou une promesse de livraison comme une preuve de fonctionnement.
```

## Checklist de reconstruction

1. Identifier le thème cible et lire ses schémas.
2. Créer ou dupliquer un modèle produit.
3. Configurer galerie, titre, prix et variantes.
4. Brancher une note d’avis dynamique réelle.
5. Ajouter le paiement fractionné seulement s’il est actif.
6. Ajouter quatre bénéfices prouvés.
7. Ajouter une livraison issue de données réelles.
8. Configurer quantité et ajout au panier.
9. Ajouter la réassurance avec les politiques réelles.
10. Lier la description produit dynamique.
11. Rédiger les accordéons et la FAQ.
12. Ajouter un seul système d’avis.
13. Ajouter les médias/USP et une seule recommandation.
14. Tester variantes, prix, stock, panier et paiement.
15. Vérifier le rendu mobile et les débordements.
16. Contrôler promesses, avis, garanties, délais et certifications.
17. Vérifier le thème publié avant mise en ligne.

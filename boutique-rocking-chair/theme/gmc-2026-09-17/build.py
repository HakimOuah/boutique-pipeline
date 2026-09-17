import json
def body(fn):
    c=open('avant/'+fn).read(); return c[c.index('{'):] if fn.endswith('.json') else c
def rep(t,o,n,k=1):
    assert t.count(o)==k,(o[:60],t.count(o)); return t.replace(o,n)
# pied de page
f=body('sections__footer-group.json')
f=rep(f,'<p>OH VENTURES (SASU) — 47 rue Vivienne, 75002 Paris, France<br/>SIREN 103 157 251</p>','<p>Bercelou, 47 rue Vivienne, 75002 Paris, France</p>')
f=rep(f,'<p>Carte bancaire, PayPal, Apple Pay, et paiement en 3 ou 4 fois.</p>','<p>Carte bancaire, PayPal, Klarna, Apple Pay et Shop Pay, paiement en 3 ou 4 fois.</p>')
json.loads(f); assert 'OH V' not in f and 'SIREN' not in f
open('apres/footer-group.json','w').write(f)
# panier : mention TTC
TTC_BLOCK={"type":"custom-code","name":"Mention TTC","settings":{"show_on_display":"desktop_and_mobile","custom_liquid":"<p class=\"bc-ttc\">Prix TTC, taxes incluses. Livraison offerte en France métropolitaine.</p>\n<style>.bc-ttc{margin:0 0 10px;font-size:.8rem;text-align:center;opacity:.8}</style>","margin_top":0,"margin_bottom":0,"additional_class":""},"blocks":{}}
c=json.loads(body('templates__cart.json'))
fb=c['sections']['main']['blocks']['cart_footer_blocks']; fb['blocks']['bc_ttc']=TTC_BLOCK; fb['block_order'].insert(0,'bc_ttc')
open('apres/cart.json','w').write(json.dumps(c,ensure_ascii=False,indent=2))
d=json.loads(body('sections__cart-drawer-group.json'))
fb=d['sections']['cart-drawer']['blocks']['cart_footer_blocks']; fb['blocks']['bc_ttc']=TTC_BLOCK; fb['block_order'].insert(0,'bc_ttc')
open('apres/cart-drawer-group.json','w').write(json.dumps(d,ensure_ascii=False,indent=2))
# JSON-LD : chaque champ optionnel porte sa virgule en tête
o=body('snippets__organization-schema.liquid')
new='''<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": {{ shop.name | json }},
    "url": {{ request.origin | append: page.url | json }}
    {%- if shop.description != blank %},
    "description": {{ shop.description | json }}
    {%- endif -%}
    {%- if shop.address.street != blank or shop.address.city != blank or shop.address.country != blank -%},
    "address": {
      "@type": "PostalAddress"
      {%- if shop.address.street != blank %},"streetAddress": {{ shop.address.street | json }}{% endif -%}
      {% if shop.address.city != blank -%},"addressLocality": {{ shop.address.city | json }}{%- endif -%}
      {% if shop.address.province != blank -%},"addressRegion": {{ shop.address.province | json }}{%- endif -%}
      {% if shop.address.zip != blank -%},"postalCode": {{ shop.address.zip | json }}{%- endif -%}
      {% if shop.address.country != blank -%},"addressCountry": {{ shop.address.country | json }}{%- endif -%}
    }
    {%- endif -%}
    {%- if shop.phone != blank %},
    "telephone": {{ shop.phone | json }}
    {%- endif -%}
    {%- if shop.email != blank %},
    "email": {{ shop.email | json }}
    {%- endif -%}
    {%- if settings.logo %},
    "logo": {{ settings.logo | image_url: width: 500 | prepend: "https:" | json }}
    {%- endif -%}
    {%- liquid
      assign social_urls = ''
      assign social_settings = 'facebook_url,instagram_url,x_url,youtube_url,tiktok_url,pinterest_url,linkedin_url,snapchat_url,threads_url,discord_url,whatsapp_url' | split: ','
      for social_setting in social_settings
        assign social_url = settings[social_setting]
        if social_url != blank
          if social_urls != ''
            assign social_urls = social_urls | append: ','
          endif
          assign social_urls = social_urls | append: social_url
        endif
      endfor
    -%}
    {%- if social_urls != blank %},
    "sameAs": [
      {% assign social_urls_array = social_urls | split: ',' -%}
      {% for url in social_urls_array -%}
        {{ url | json }}{% unless forloop.last %},{% endunless %}
      {% endfor -%}
    ]{% endif %}
  }
</script>
'''
assert '"Organization"' in o
open('apres/organization-schema.liquid','w').write(new)
print('ok')

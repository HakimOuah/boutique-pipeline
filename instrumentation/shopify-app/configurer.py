#!/usr/bin/env python3
"""Applique la meme configuration a une app de mesure : scopes, pas d'interface,
URL de redirection locale. Idempotent. Ne publie rien.

    python3 configurer.py shopify.app.<slug>.toml
"""
import re, sys, pathlib

ENTETE = """# App d'acces API pour la mesure hebdomadaire de cette boutique.
# Aucune interface : elle sert uniquement a obtenir un jeton Admin API par
# autorisation OAuth (voir ../obtenir-jeton.py), pour interroger ShopifyQL.
#
# Une app par boutique : la distribution personnalisee ne couvre qu'un seul
# magasin, et elle ne se change plus une fois choisie.
#
# read_reports est le seul scope necessaire, et il est obligatoire. Les scopes
# viennent de la version PUBLIEE : modifier ce fichier ne suffit pas, il faut
# `shopify app deploy -c <slug> --allow-updates`.
"""

for chemin in sys.argv[1:]:
    p = pathlib.Path(chemin); s = p.read_text(encoding="utf-8")
    s = re.sub(r"^# Learn more about configuring your app at \S+\n", ENTETE, s, count=1, flags=re.M)
    s = re.sub(r"^embedded = true$", "embedded = false", s, flags=re.M)
    s = re.sub(r'^scopes = ""$', 'scopes = "read_reports"', s, flags=re.M)
    s = re.sub(r'^application_url = ".*"$', 'application_url = "http://localhost:8123"', s, flags=re.M)
    s = re.sub(r"^redirect_urls = \[ \]$",
               'redirect_urls = [ "http://localhost:8123/callback" ]', s, flags=re.M)
    p.write_text(s, encoding="utf-8")
    print(f"✓ {p.name}")

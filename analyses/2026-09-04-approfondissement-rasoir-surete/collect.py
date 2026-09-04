"""Collecte bornée, en lecture seule ; réutilise le capteur public du dossier initial."""
import concurrent.futures
import importlib.util
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('captures', ROOT.parent / '2026-09-03-qualification-9-produits-pur/collect_competitors.py')
captures = importlib.util.module_from_spec(spec)
spec.loader.exec_module(captures)
captures.ROOT = ROOT
URLS = {
    'lamier-rasoir': 'https://lelamier.com/products/lamier',
    'lamier-kit': 'https://lelamier.com/products/kit-de-rasage-lamier',
    'lamier-kit-ancienne-url': 'https://lelamier.com/products/le-kit-complet-lamier',
    'lamier-retours': 'https://lelamier.com/pages/retour',
    'bouc-kit': 'https://www.leboucfrancais.fr/produit/coffret-rasage-a-lancienne-noir/',
    'bouc-rasoir': 'https://www.leboucfrancais.fr/produit/rasoir-surete-francais/',
    'bambaw': 'https://fr.bambaw.com/products/metal-double-edged-safety-razor',
    'rasage-classique': 'https://www.rasage-classique.com/84-rasoirs-de-surete',
    'gillette': 'https://www.gillette.fr/fr-fr/produits/rasoirs/rasoir-de-surete-kingcgillette',
    'henson': 'https://hensonshaving.com/collections/all/products/henson-al13-in-jet-black',
}
if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for result in pool.map(lambda item: captures.fetch(*item), URLS.items()):
            print(result, flush=True)

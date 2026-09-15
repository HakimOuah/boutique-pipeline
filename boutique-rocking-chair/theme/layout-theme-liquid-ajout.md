# Ajout dans layout/theme.liquid (copie-de-fullstack-2-3)

- `apple-touch-icon` 180 px à partir du favicon.
- Règle `body .shopify-section.section-header { z-index: 6; }` : l'en-tête collant passait sous le texte des cartes image (z-index 3) au défilement.

## Menu sur une ligne (15/09/2026)

Entre 1001 px (apparition du menu complet) et 1240 px, les 10 entrées passaient sur deux lignes. Ajout dans le même bloc `<style>` :

```css
@media (width > 1000px) and (width < 1240px) {
  .header__menu-desktop .header__menu-desktop-list { column-gap: 12px; flex-wrap: nowrap; }
  .header__menu-desktop-list .header__menu-link,
  .header__menu-desktop-list summary,
  .header__menu-desktop-list button { font-size: 14.5px; }
}
```

Vérifié à 1001, 1025, 1060, 1100 et 1239 px : une seule ligne, sans débordement (à 1001 px il reste 1 px de marge ; ajouter une entrée de menu obligera à revoir ce réglage).

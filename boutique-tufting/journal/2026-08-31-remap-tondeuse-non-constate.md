---
type: journal
boutique: tufting
date: 2026-08-31
nature: intervention
leviers: [catalogue, sourcing]
titre: "Remapping DSers tondeuse déclaré fait — pas constaté côté Shopify"
---

# Remapping DSers tondeuse — déclaré fait, pas constaté

Hakim : « Ok c'est fait » (31/08, ~00:43). Contrôle API immédiat sur
`gid://shopify/Product/15466411426177` (Tondeuse électrique pour tapis) :

| Champ | Attendu si remapping vers `1005007430527466` | Constaté 31/08 |
|---|---|---|
| SKU | nouveau (listing EasyClip / Crafters Daily) | **inchangé** `14:201441319;200007763:201336342` — `updatedAt` variante **16/08** |
| Stock DSers | > 0 (PDP achetable le 30/08 à 42,99 €) | **0** sur `dsers-fulfillment-service`, `updatedAt` **21/07** |
| Coût | ~42,99 € | 42,91 € (inchangé) |
| Métafields DSers | éventuellement un namespace `dsers` | **aucun** |

Le mapping DSers vit dans la base DSers, pas dans Shopify. Un remapping réussi
peut ne pas réécrire le SKU. En revanche un stock toujours à 0 depuis le 21/07,
sans aucun `updatedAt` récent sur l'emplacement DSers, ne prouve pas que le
nouveau listing est bien celui qui routerait une commande.

À confirmer : l'URL fournisseur affichée dans DSers → Mes produits → Tondeuse
électrique pour tapis. Cible : `https://www.aliexpress.com/item/1005007430527466.html`.

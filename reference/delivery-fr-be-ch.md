# Configuration livraison FR / BE / CH

Zones par défaut héritées de Bien Brûlé. À appliquer via MCP `graphql_mutation`
(`deliveryProfileUpdate`) en Phase 6. Récupérer d'abord le profil et le locationGroup
via `graphql_query` sur `deliveryProfiles`.

Pays par défaut (ISO) : `FR`, `BE`, `CH`, chacun avec `includeAllProvinces: true`.

Exemple de mutation (à adapter aux IDs réels du profil/zone) :
```graphql
mutation deliveryProfileUpdate($id: ID!, $profile: DeliveryProfileInput!) {
  deliveryProfileUpdate(id: $id, profile: $profile) {
    profile { id }
    userErrors { field message }
  }
}
```
Variables (structure) :
```json
{
  "id": "gid://shopify/DeliveryProfile/XXXX",
  "profile": {
    "locationGroupsToUpdate": [{
      "id": "gid://shopify/DeliveryProfileLocationGroup/XXXX",
      "zonesToUpdate": [{
        "id": "gid://shopify/DeliveryLocationGroupZone/XXXX",
        "countries": [
          { "code": "FR", "includeAllProvinces": true },
          { "code": "BE", "includeAllProvinces": true },
          { "code": "CH", "includeAllProvinces": true }
        ]
      }]
    }]
  }
}
```
Tarifs/seuils : répliquer le modèle Bien Brûlé, ajuster selon le panier moyen du produit.

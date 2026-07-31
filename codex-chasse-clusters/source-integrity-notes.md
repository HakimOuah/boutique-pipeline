# Journal d'intégrité des sources originales

## 20 juillet 2026 — création de l'espace Codex

Les patchs Codex ont ciblé exclusivement `/Users/Hakim/.codex/skills/chasse-clusters-codex/` et `codex-chasse-clusters/`.

Entre le premier relevé et la validation, deux sources canoniques ont changé :

| Fichier | Empreinte initiale | Empreinte à 12:41 CEST | Constat |
|---|---|---|---|
| `familles-exploration.md` | `c5aeb45fae0b9ca895fb984d3849fb69f84eae34b5fc47d30d4ea7f5346b5ff7` | `af7a1da8fdde9dce35c31c91c0c30340e172e164609695332544a268cfc072e2` | Modification concurrente à 12:37:15 CEST |
| `registre-candidats.md` | `5a5519f0c8f057849a8b3debb41a0fe36aede55c39933f38cb4e0a9b6249f36d` | `4000bf0cab9d44d4a644d38fc28a5ee21fdb1318bb34e54cb446c62607028751` | Modification concurrente à 12:37:10 CEST |

Le dépôt montre un commit à 12:37:23 CEST : `dcf2ec3 feat(chasse): famille 2 (travail du bois) balayee — 0 candidat`. Cette concordance confirme qu'un autre processus a fait avancer le pipeline original pendant la création. Codex n'a ni restauré ni écrasé ces changements.

Les trois fichiers de configuration Claude contrôlés sont restés identiques entre les deux relevés.


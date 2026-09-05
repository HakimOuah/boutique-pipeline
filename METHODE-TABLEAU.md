# Coordination par boutique

`TABLEAU.md` est le point d'entrée des tickets ; `ETAT.md` décrit l'état observé courant, `REGLES.md` les invariants de la boutique, `journal/` les comptes rendus datés. `backups/`, `preuves/` et `livraisons/` conservent sauvegardes, vérifications et livrables.

## Quand lire et écrire

Pour une intervention sur une boutique, lire l'index actif et le ticket concerné, puis les seules références utiles. Rechercher un ticket par identifiant avec `rg -n` et lire sa section suffit ; aucune lecture intégrale d'un grand tableau ou de ses archives n'est exigée. Un audit transversal ou une simple question n'impose pas de parcourir les tableaux de toutes les boutiques.

Vérifier le propriétaire et les changements concurrents avant de prendre ou modifier un ticket. Mettre à jour son état, son responsable et ses preuves quand le travail les change. Une lecture seule n'impose aucune écriture. FAIT signifie que la sortie attendue est obtenue et vérifiée ; une dépendance restante est BLOQUÉ ou EN COURS, explicitée.

Un compte rendu dans `journal/AAAA-MM-JJ-sujet.md` est utile pour une intervention substantielle, une décision ou un relais ; une correction triviale peut être expliquée par le ticket et le commit. Ne pas dupliquer le rapport dans plusieurs fichiers. Livrer selon la politique Git du hub.

## Ticket suffisant pour un relais

```markdown
### T-XX — Résultat attendu
**État** : À FAIRE | EN COURS | BLOQUÉ | FAIT
**Responsable** : agent ou personne ; date de prise
**Pourquoi** : enjeu réel
**Sortie attendue** : résultat observable et preuve de fin
**Contraintes** : invariants, limites d'autorisation et pièges spécifiques
**Références** : fichiers et preuves nécessaires
**Reprise** : uniquement si interrompu, prochaine action et dépendance
```

Décrire une procédure seulement si un ordre ou une technique protège un invariant connu. L'agent choisit autrement la méthode et les contrôles proportionnés. Les tickets existants restent compatibles : inutile de les réécrire tous.

Pour un tableau trop grand, garder les tickets actifs et un index dans TABLEAU, déplacer progressivement les détails terminés vers des fichiers liés. Préserver identifiants et liens existants ; ne pas déplacer les archives pendant une autre intervention.

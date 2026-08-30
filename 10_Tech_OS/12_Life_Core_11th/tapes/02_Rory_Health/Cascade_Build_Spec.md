# Cascade Build Spec — Ruban admis pour Rory

> Ruban φ admis par le 11e Docteur pour le build de la cascade Life OS A1/A2/A3 dans A'Space Core.
> Ce fichier est le `tape_path` que `uc.py submit --layer L1` référence.
> Source amont : `cascade_blueprint_v1.md` validé par Amy (Spec) — voir ASP-890 commentaire 87f13ec9.

## Cible

Matérialiser dans `A'Space Core` (workspace_id `1ae43c2b-c443-4896-8afe-b15bec691b9e`) :
- **16 agents** : A1-Beth, A1-Morty, A2-Orville, A2-Discovery, A2-SNW, A2-Enterprise, A2-Cerritos, A2-Protostar, A3-Mercer, A3-Pike, A3-Mariner, A3-Dal, A3-Picard, A3-Spock, A3-Geordi, A3-Data
- **3 squads** : `Squad-A1-Beth-Morty` (leader A1-Beth), `Squad-A2-Frameworks` (leader A2-Enterprise), `Squad-A3-Officiers` (leader A3-Picard)
- **13 rattachements** `squad member add` (1 pour A1, 5 pour A2, 7 pour A3)
- **3 projets** : `A1 — Vision`, `A2 — Frameworks`, `A3 — Officiers`

Total : 35 commandes shell, 22 objets.

## Source canonique

Toutes les valeurs (runtime_id `19e5593d-44a4-4466-800c-066190bfc2f9`, visibility `private`, instructions sketches, descriptions, project descriptions) proviennent de `cascade_blueprint_v1.md` validé par Amy (revue du 11e Docteur : PASS 3/3, commentaire `6a8700ff-0daa-4530-b1c5-9625d9741883`).

Le script exécutable est `apply_life_os_cascade.sh` (17865 B, attachment id `019fc5fd-1e67-79fa-8e78-eaac36989242`, sha256 à recalculer au moment de l'attest). Le blueprint de référence est `cascade_blueprint_v1.md` (19443 B, attachment id `019fc5fd-1d9a-7abb-94dc-419e82a65b0d`, sha256 `228f5f1e120dc65f...` au moment de la revue Amy).

## Cycle UC

```
1. uc.py reap
2. uc.py claim --harness cc --layer L1 --lease 900
3. uc.py predict --work N --claim "..." --confidence 0.8
4. uc.py beat --work N --harness cc --lease 900   (pendant l'exécution)
5. (dry-run) bash apply_life_os_cascade.sh --dry-run
6. (build)    bash apply_life_os_cascade.sh --apply
7. uc.py attest --work N --criterion "<chaque critere>" --ok <bool> --note "<preuve>"
8. uc.py review --work N
9. (séparation) 11e Docteur prononce 'done' après vérification humaine.
```

## Critères de fin vérifiables

| # | Critère | Attestation |
|---|---|---|
| C1 | dry-run exécuté localement sans erreur, 35 lignes émises | `attest --criterion "dry_run_clean" --ok true` |
| C2 | apply exécuté, exit 0, log `apply_life_os_cascade.log` complet | `attest --criterion "apply_clean" --ok true` |
| C3 | `multica agent list` retourne 24 agents dont 16 nouveaux A1/A2/A3 | `attest --criterion "agents_24" --ok true` |
| C4 | `multica squad list` retourne 7 squads dont 3 nouvelles | `attest --criterion "squads_7" --ok true` |
| C5 | `multica project list` retourne 5 projets dont 3 nouveaux | `attest --criterion "projects_5" --ok true` |
| C6 | `multica squad get Squad-A3-Officiers` montre leader = A3-Picard | `attest --criterion "leader_A3" --ok true` |
| C7 | `multica squad get Squad-A2-Frameworks` montre leader = A2-Enterprise | `attest --criterion "leader_A2" --ok true` |
| C8 | Les 22 IDs (16 agents + 3 squads + 3 projets) sont capturés et publiés dans le commentaire de retour sur ASP-890 | `attest --criterion "ids_published" --ok true` |

`done` n'est pas prononcé par Rory — c'est le 11e Docteur (reviewer) qui détache après vérification.

## Hors périmètre

- Ne pas créer de second workspace.
- Ne pas transférer au 12e Docteur ni à Buzz-Core-12th.
- Ne pas modifier `cascade_blueprint_v1.md` ni le script.
- Ne pas appliquer les modifications au runtime_id ou visibility.

## Escalade

- Échec simple : retentable après diagnostic local.
- Échec répété (3) : Donna (DLQ) puis Rick.
- Si `claim` retourne `work: null` à nouveau : le 11e Docteur regénère le ruban.
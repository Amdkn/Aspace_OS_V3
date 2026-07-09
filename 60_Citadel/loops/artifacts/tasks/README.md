---
type: artifact-schema
artifact: task
---
# tasks/ — LA QUEUE (ADR-LOOP-002)

**Entre** : items actionnables typés, pioché par une loop sur trigger. Frontmatter : `type: task`, `status: queued|picked|done|dlq`, `owner: <loop|agent>`, `origin: <signal|contrat|A+>`, `wk: WKnn`, `exit_condition: <observable>`.
**N'entre pas** : les idées vagues (→ signals/ d'abord), le fini (→ docs/ + worklog).

**Règles** : `done` exige la preuve (sortie de commande, path existant) collée dans le fichier. 2 WK sans pioche OU 3 échecs → `_dlq/` avec raison (Donna DLQ, rien de perdu). WIP : si > 20 items `queued`, les loops drainent avant d'ingérer (soupape c, wargame 02).

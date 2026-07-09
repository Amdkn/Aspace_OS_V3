---
name: canon-vs-runtime-drift
version: 1.0
created: 2026-06-07
phase: LEARN (audit) + SIGNAL (rapport)
actor: A0 Amadeus + A1 Beth + A2 captains
canon_path: 20_Life_OS/
runtime_path: 05_OSS_TSTwin/symphony/L1/lane_C_capsules/
---

# 11 — Canon vs Runtime Drift Reconciliation

> Le runtime L1 (Shadow Life OS, 215 capsules) est un **twin** du canon
> `20_Life_OS/`. Les deux peuvent **drifter** — c'est normal. Ce standard
> définit la procédure de réconciliation pour éviter le shadow divergence.

## Sources de drift

| Type | Exemple canon connu | Effet |
|---|---|---|
| **Canon lock override** | Rutherford=Organize (2026-05-20) | Runtime doit respecter, pas l'inverse |
| **Twin stub** | Captains A2 avec seulement 2 fichiers `.md` (Soul + Agent) | Incomplet, à enrichir |
| **Specs manquants** | A3 Gwyn/Protostar : `Context.md` stub 2026-06-07 | Handoff cassé |
| **Canon vs Shadow role** | Ortegas=Uhura resolved (2026-05-23) | Documenter la résolution |

## Audit routine (LEARN phase)

À chaque tick LEARN, Discovery captain lance un audit `canon-vs-runtime` :

```
1. Lister tous les fichiers dans canon_path (récursif)
2. Lister tous les fichiers dans runtime_path (récursif)
3. Pour chaque canon fichier :
   a. Vérifier twin_of dans runtime_path (frontmatter)
   b. Comparer frontmatter (agent/vessel/framework/ld/status)
   c. Comparer last_reviewed_at
4. Pour chaque runtime fichier :
   a. Vérifier twin_of pointe vers un canon existant
   b. Signaler les stubs (longueur < 200 bytes)
5. Output : `outbox/l1/<date>/<tick>-drift-report.json`
```

## Output (drift-report.json)

```json
{
  "audit_id": "<uuid>",
  "tick_id": "...",
  "ts": "<ISO 8601>",
  "canon_files": 142,
  "runtime_files": 215,
  "orphans_canon": ["20_Life_OS/.../X.md"],
  "orphans_runtime": ["L1/lane_C_capsules/.../Y.md"],
  "stubs_runtime": [
    {"path": "L1/lane_C_capsules/03_A3_crews/protostar/gwyn/Context.md", "size": 145}
  ],
  "frontmatter_mismatches": [
    {"canon": "agent=A3_Boimler", "runtime": "agent=Boimler", "twin": "..."}
  ],
  "verdict": "OK|WARN|FAIL",
  "action_required": "fix_stubs|reconcile_canon|archive_orphans"
}
```

## Procédure de réconciliation

| Verdict | Action | Acteur |
|---|---|---|
| **OK** | Aucune action, log dans `pulse.log` | Discovery captain |
| **WARN** | Créer 1 fichier de plan de fix par stub détecté | Discovery captain → A2 captains concernés |
| **FAIL** | STOP tick, escalade A1 Beth → A0 Amadeus | A0 (seul autorisé à merge canon↔runtime) |

## Anti-patterns

- ❌ Runtime modifié sans que le canon soit同步 (créer un ticket, ne pas fix en silence)
- ❌ Canon modifié sans que le twin runtime soit régénéré (drift inverse)
- ❌ Stubs runtime jamais enrichis (> 30 jours) → `archive_orphans` automatique
- ❌ Drift > 20% du runtime → FAIL automatique (système instable)

## Règle d'or (A0)

> *Le canon ne se réécrit jamais. On crée de nouveaux ADR.*
> *Le runtime ne diverge jamais sans ticket. On documente la divergence.*

## Source canonique

- `AGENTS.md` règle d'or #3 (canon immuable)
- `ADR-INFRA-002` (Repo-Home/Junction) — pattern canon↔runtime
- Wiki : `concept_shadow_l1_l2_heartbeat_symphony.md` (heartbeat doctrine)
- Connaissance : `2026-05-20` (Rutherford=Organize), `2026-05-23` (Ortegas=Uhura)

---
source: CC-M3 loop-operator (auto-loop 2026-07-02 item 6)
date: 2026-07-02T14:58:00-04:00
type: Signal
domain: graphify junctions
status: OPEN
loop: meta_memoire_2026-07-02
item: 6 (junction health check)
tags: [#signal #junction #broken_readlink #afk_loop]
related:
  - .claude/logs/junction-health_2026-07-02.json
---

# Signal OKF — 17 broken junctions détectés (2026-07-02)

## Fait (D1 receipts)

- **Date** : 2026-07-02 14:58:00
- **Total symlinks/junctions scannés** : 100 (contrat disait 49 — plus ont été créés depuis)
- **Healthy** : 83
- **Broken** : 17 (cible done-check `0 broken` → FAIL)

## Pattern des 17 cassés

**TOUS pointent vers `/tmp/staging/*` ou `/tmp/root-staging/*`** — ce sont des staging areas Git-Bash/WSL éphémères qui n'existent pas comme Windows paths réels.

| Catégorie | Count | Targets |
|---|---|---|
| Staging area roots | 6 | `/tmp/staging/aspace-roots/{00_Amadeus, 10_Tech_OS, 20_Life_OS, 30_Business_OS, ASpace_OS_V2}` |
| Staging lifeos-ships | 4 | `/tmp/staging/lifeos-ships/{21_Ikigai_Orville, 23_12WY_SNW, 25_GTD_Cerritos, 26_DEAL_Protostar}` |
| Root-staging codex-m3 | 1 | `/tmp/root-staging/codex-m3-lean-root/` |
| Root-staging Life/Tech/Biz | 4 | `/tmp/root-staging/{30_Business_OS, 20_Life_OS, 20_Life_OS_v2, 10_Tech_OS}` |
| Agent-app staged | 2 | `/tmp/staging/agent-app/graphify-out` |
| lifeos-05-marina | 1 | path tronqué (`/c/.../01_Projects_Picard/05` sans nom fichier) |

## Root cause (D6)

Ces junctions ont été créées par un script de staging qui ne s'est pas auto-nettoyé. La cible `/tmp/` est un artefact Git Bash qui n'existe pas dans le filesystem Windows réel (Git Bash émule `/tmp/` via `C:\Users\<user>\AppData\Local\Temp\` ou équivalent, mais ne survit pas aux redémarrages de session).

## Action proposée (hors-loop, à A0)

3 options :
1. **Delete les 17 junctions cassés** (sûr, ce sont des artefacts orphelins). Mais contrat dit "no hard-delete" → utiliser `_TRASH_2026-07-02_stale_junctions/` + `rm` via shell.
2. **Recréer les junctions** vers les vrais paths Windows (ASpace_OS_V2/...) — mais on perd la sémantique staging.
3. **Cleanup script** ajouté à graphify-swarm-burst pour auto-pruner les `/tmp/` staging après run.

## Wager (ADR-LOOP-003) — pari test pour métrique 5

- **Métrique candidate** : `junction_health.broken_readlinks_count` (cible 0)
- **Baseline** : 17 broken (2026-07-02)
- **Cible** : 0 broken d'ici W4 (2026-07-20)
- **Effort estimé** : 5 min cleanup × 17 junctions = 1.5h
- **Chapel verdict W13** : si toujours > 0 → ADL-LOOP-005 PROPOSED (auto-prune staging)

## Related

- `.claude/logs/junction-health_2026-07-02.json` — détails bruts
- `~/.claude/skills/graphify-swarm-burst/scripts/graphify_userspace.py` — créateur probable

---
**Status** : OPEN — escalade A0 au réveil.

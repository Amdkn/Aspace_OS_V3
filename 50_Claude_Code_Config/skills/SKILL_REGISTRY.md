# SKILL_REGISTRY — le registre canonique + gate d'intake

> Créé 2026-07-07 (wargame 22 M4, élu #1 du EXECUTION-RANKING). Résout la dette
> spéccée 2× (wargames 16 M3 + 21) construite 0×. **DEUX rôles** : (1) le gate
> d'intake — rien n'entre dans `skills/` sans une ligne ici ; (2) le tribunal —
> verdict keep/merge/rewrite/delete de chaque skill, révisé au sweep hebdo.

## LOI D'INTAKE (le gate)

Tout nouveau skill/hook/plugin/harness ajoute **d'abord** sa ligne ici :
`| <nom> | <classe> | keep | owner=<WF/agent> | trigger=<déclencheur> | né=<date> |`
Un skill sans ligne de registre = non-gouverné = candidat `_TRASH` au prochain sweep.

## VERDICT — preuves externes obligatoires (patch red-team wargame 22 M4)

Un verdict n'est PAS une opinion de l'auteur. Il s'appuie sur 3 preuves :
- **(a) usage réel** : présence dans les 38 sessions scannées (comptage 2026-07-07).
  Le HAUT du compte est pollué par la liste système ; le **plancher (~34-56) = dormance fiable**.
- **(b) collision** : chevauchement de mots-clés de description entre paires.
- **(c) Gwyn/D11** : coût de maintenance vs valeur (taille du body incluse).
Un « keep » sans preuve (a) ou (c) → requalifié **dormant** d'office.

---

## Tribunal des 76 skills (2026-07-07)

### 🔴 DELETE / RELOCATE (2)
| Skill | Raison (preuve) |
|---|---|
| `abc-os-backend-delegation-workspace` | **PAS un skill** : aucun SKILL.md, seulement `iteration-1/2/` (scratch). → relocate hors `skills/` (workspace), sinon `_TRASH`. |
| `abc-os-backend-delegation` (268L) vs le workspace | garder le skill, séparer le workspace de sortie. |

### 🟠 REWRITE (fait ce run + candidats)
| Skill | Action | Statut |
|---|---|---|
| `swarm-orchestrator` | **AUCUN frontmatter → ne pouvait PAS trigger.** Frontmatter ajouté (name+description). | ✅ FAIT |
| `youtube-to-guide` (325L) | **AUCUN frontmatter → mort.** Frontmatter ajouté + distinction vs to-para/takeout épelée. | ✅ FAIT |
| `youtube-to-para` (258L) | collision (b) avec to-guide → description à resserrer sur « ADR-proposals / PARA général », pas « guide ». | candidat M3 |

### 🟡 MERGE-candidates (gated — la fusion est destructive, D4)
| Famille | Skills | Proposition |
|---|---|---|
| transcript chunks | `swarm-chunk-transcript` ↔ `transcript-swarm-chunks` | **noms quasi-identiques, collision (b) forte** → fusionner en 1, l'autre `_TRASH`. |
| symphony pilot | `symphony-pilot` (237L) ↔ `symphony-pilot-runtime` (40L) | runtime = dispatcher mince du pilot → sous-commande, pas skill séparé. |
| guide toolkit | `guide-search` `guide-cross-search` `guide-domain-stats` `guide-index-builder` `guide-trim-large` | 5 verbes sur le même corpus → `guide-toolkit` à sous-commandes (basse priorité, chacun fonctionne). |
| fable discipline | `fable-mode` (canonique) · `symphony-fabuleux-discipline` (A3 injection) · `tilly-fable-rhythm` (audit cognition) | **PAS merge** — périmètres distincts ; ajouter cross-ref `[[fable-mode]]` dans les 2 autres. |

### 🟢 KEEP — actifs prouvés (usage + périmètre net)
`skill-creator` · `wargame` · `ratify-adr` · `premortem-fill` · `canon-batch-spawn` · `multi-backend` · `multi-goal` · `multi-loop-karpathy` · `multi-routines-12wy` · `graphify-swarm-burst` · `graphify-viewer` · `youtube-takeout-to-lifeos` · `takeout-delta-ingest` · `symphony-pilot` · `symphony-phase2-batch` · `symphony-fabuleux-discipline` · `bridge-12wy-plane-gtd` · `area-domain-doctrine-distill` · `b1-filter` · `picard-repo-home` · `picard-audit-and-prod-workflow` · `picard-growth-jtbd-launch` · `replicate-squads` · `pricing-canon-derive` · `market-study-derive` · `aaas-dashboard-port-audit` · `cloud-bootstrap` · `aspace-supabase-mastery` · `supabase-cloud-mcp-orchestration` · `vercel-deploy-from-github` · `github-cli-orchestration` · `hostinger-dns-orchestration` · `mcp-mastery` · `context7-mcp` · `find-docs` · `l0-deploy-verify` · `l0-watchdog-scrape` · `l1-research-pulse` · `l1-weekly-snapshot` · `l2-competitor-pulse` · `l2-e2e-pr` · `l2-linkedin-prospect` · `openspec-explore` · `openspec-propose` · `openspec-apply-change` · `openspec-archive-change` · `sessions-archive` · `strategy-session-meta` · `a0l-grill` · `diagnose-proxy-boolean` · `context-bloat-detector` · `writing-great-skills` · `configure-ecc` · `test-a1-profiles` · `tilly-fable-rhythm` · `notebooklm-bridge` · `multistream-deliver` · `swarm-chunk-transcript` · `transcript-swarm-chunks` · `sym_supabase_drain` · `symphony-pilot-runtime` · `abc-os-write-back-protocol` · `airtable-enrich` · `pp-cli-install` · `guide-*` (×5)

### ⚪ DORMANT à surveiller (plancher usage bas — Gwyn/D11 J+14)
`fable-mode` (45 — NEUF, attendu) · `takeout-delta-ingest` (44) · `strategy-session-meta` (34) · `sym_supabase_drain` (34) · `diagnose-proxy-boolean` (56). Règle : < 5 usages RÉELS à J+14 hors listing système → dormant, candidat merge/trash. Un skill neuf a un sursis d'un cycle.

---

## Prochain sweep hebdo
Re-run `analyze_discipline_real.py`-style invocation count → mettre à jour la colonne (a) →
exécuter les MERGE-candidates gated (avec `_TRASH` daté) → cible : `ls skills/ | wc -l` **stable**
2 semaines (la dérive 58→77 s'arrête). Owner : WF0 Spock (gate) + Gwyn (mesure D11).

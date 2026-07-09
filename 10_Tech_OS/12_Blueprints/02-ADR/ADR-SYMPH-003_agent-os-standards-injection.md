# ADR-SYMPH-003 — Agent OS = Standards Injection + Observability Layer for Symphony Ticks

**Date :** 2026-06-06 (proposé) / 2026-06-06 (ratifié)
**Auteur :** A2 Claude Code (sur intention A0 Amadeus)
**Statut :** RATIFIÉ
**Type :** Architecture Decision Record (Tech OS / L0)
**Portée :** Interface d'injection de standards + observabilité des ticks Symphony
**Ancré sur :** `AGENTS.md` · `ADR-SYMPH-001_symphony-replaces-n8n.md` · `SDD-008` · `SDD-009` · `ADR-RICK-001`
**Source matière :** Pilot 2026-06-06 sur `WORKFLOW.solaris-airtable-clients.md` + recadrage A0 ("Agent OS = interface d'observabilité pour Symphony qui remplace N8N")

---

## Contexte

`ADR-SYMPH-001` (ratifié 2026-05-26) déclare Symphony = le seul bus d'orchestration L0 autorisé (N8N legacy), avec un tick cycle 8 phases (WAKE→SLEEP) et une interface d'observabilité définie en §12 (`symphony-base.spec.md`). Mais ADR-SYMPH-001 ne dit pas **comment** les standards par workflow sont injectés dans le prompt de l'agent éphémère, ni **quel format** doit prendre l'observabilité tick-par-tick.

Conséquences observées avant cet ADR :

1. **Pas d'injection de standards formalisée** — chaque adapter Symphony a sa propre façon (ou aucune) de pousser les patterns tribaux dans le prompt agent. Drift garanti entre L0/L1/L2.
2. **Pas de format de log canonique** — `symphony-base.spec.md` §12 liste des champs requis (`issue_id`, `session_id`, `cumulative_cost_usd`, etc.) mais ne donne pas de schéma JSONL par phase. Chaque implémentation écrit ce qu'elle veut.
3. **Pas d'observabilité des daemons** — A0 ne peut pas voir ce qu'un tick a réellement fait avec les standards qu'on lui a passé. Les "daemon obscurs" critiqués sur N8N re-émergent dans Symphony.
4. **Le pilote 2026-06-06 a prouvé qu'on peut faire mieux** — 11 standards discoverées + 1 index.yml + 1 schema pulse.log 8 phases + 1 demo tick (Bash + PowerShell) sur `WORKFLOW.solaris-airtable-clients`. L'outillage existe, il manque la ratification.

Cet ADR ferme la boucle en ratifiant ce que le pilote a prouvé, sans réécrire `ADR-SYMPH-001`.

## Décision

### D1 — Agent OS = la couche d'injection de standards pour les ticks Symphony

**Agent OS est déclaré couche d'interface obligatoire** entre :

- La **base Agent OS** (`~/agent-os/`) — la doctrine réutilisable entre workflows (profiles, commands, scripts)
- Le **tick handler Symphony** (le worker éphémère qui orchestre chaque tick)

Position dans la stack (rappel) :

```
Symphony tick (WAKE→SLEEP)
  ├─ Tick handler (heartbeat-tick-symphony.ps1)
  │   ├─ Lit agent-os/standards/index.yml          ← Agent OS (D2)
  │   ├─ Sélectionne standards par phase + SOA     ← Agent OS (D2)
  │   ├─ Injecte dans le prompt agent éphémère     ← Agent OS (D2)
  │   └─ Écrit pulse.log structuré (1 ligne/phase) ← Agent OS (D3)
  ├─ Agent éphémère (Hermes / Codex / Claude Code)
  └─ Tracker source (Airtable / ClickUp / Notion / …)
```

**Conséquence** : tout tick handler Symphony DOIT, à partir de la ratification du présent ADR, consommer `agent-os/standards/index.yml` du projet Symphony et écrire dans `agent-os/pulse.log`. Les ticks qui ne le font pas sont non-conformes (cf. §Conéquences négatives).

### D2 — Protocole d'injection de standards (par phase)

Le tick handler applique la sélection suivante à **chaque tick** :

| Phase | Standards typiquement injectés (au moins 1 obligatoire) |
|---|---|
| **WAKE** | aucun (juste `tick_id` + `workflow_id` + `aspace_layer`) |
| **PROBE** | `candidate-record-rule.md` (filtre 9 critères) |
| **DECIDE** | `mission-contract.md`, `soa-routing.md`, `sla-triple.md`, `tick-handoff.md` |
| **EXECUTE** | `mission-contract.md`, `gate-decisions.md`, `forbidden-words.md`, `expected-proof.md`, `writeback-policy.md` |
| **OBSERVE** | `forbidden-words.md`, `gate-decisions.md`, `sla-triple.md` |
| **LEARN** | `sla-triple.md` (vérif `max_retries`) |
| **SIGNAL** | `writeback-policy.md`, `expected-proof.md` |
| **SLEEP** | aucun (juste clôture) |

La liste exacte est dans `agent-os/standards/<workflow>/index.yml` et peut être surchargée par workflow. La règle minimale : **chaque phase qui prend une décision (PROBE, DECIDE, EXECUTE, OBSERVE, SIGNAL) DOIT avoir au moins 1 standard injecté**, sinon la décision n'est pas justifiable.

**Format d'injection** (dans le prompt agent) :

```
# Standards injectés (Symphony v1 — tick <tick_id>, phase <phase>)
## <standard-name>
<contenu concis du .md, tronqué à 1 écran>

## <autre-standard>
…
```

Pas de JSON, pas de XML, pas de YAML imbriqué. **Markdown brut**, ce que les agents LLM lisent nativement.

### D3 — Schema `pulse.log` = standard d'observabilité 8 phases

**Chemin** : `<symphony-project>/agent-os/pulse.log` (un par install Symphony, pas par workflow)

**Format** : JSONL append-only, 1 ligne par phase, 8 lignes par tick. Timestamps UTC ISO-8601.

**Schema par ligne** (cf. `agent-os/standards/schema-pulse-log.md` pour le détail) :

```json
{
  "ts": "<ISO 8601 UTC ms>",
  "tick_id": "<workflow_id>-<UTC ts min-precision>",
  "workflow_id": "<string>",
  "issue_id": "<string>|null",
  "phase": "WAKE|PROBE|DECIDE|EXECUTE|OBSERVE|LEARN|SIGNAL|SLEEP",
  "duration_ms": <int>,
  "standards_injected": ["<file.md>", ...],
  "decision": "<string>",
  "evidence_url": "<string>|null",
  "cost_delta_usd": <float>|null,
  "cumulative_cost_usd": <float>|null",
  "aspace_layer": "L0|L1|L2",
  "soc_target_domain": "<string>|null",
  "error": "<string>|null"
}
```

**Invariants** :

- `error: null` quand tout va bien, `error: "<message>"` sinon
- Aucune ligne n'est jamais réécrite (audit trail immuable)
- Aucune ligne n'est jamais supprimée sauf rotation hebdomadaire (cf. SDD-001 §6.3)
- La rotation produit un `.archive/<date>.jsonl.gz`, ne touche pas les fichiers actifs

### D4 — Contrat du tick handler Symphony (minimum obligatoire)

À partir de la ratification, tout `heartbeat-tick-*.ps1` Symphony DOIT :

1. **Lire** `<symphony>/agent-os/standards/index.yml` au **WAKE** (échec = `error: "index_unreadable"`, exit)
2. **Sélectionner** ≥ 1 standard par phase de décision (PROBE/DECIDE/EXECUTE/OBSERVE/SIGNAL) selon D2
3. **Injecter** les standards dans le prompt agent avant `LaunchingAgentProcess` (cf. `symphony-base.spec.md` §7.2)
4. **Écrire** une ligne pulse.log par phase, dans l'ordre, avant le début de la phase suivante
5. **Calculer** `cost_delta_usd` à chaque appel modèle (axe financier de la triade, cf. SDD-009 §2.3)
6. **Vérifier** `cumulative_cost_usd <= sla.max_cost_usd` à chaque phase EXECUTE/OBSERVE ; dépasser = `error: "budget_exceeded"`, kill worker, no re-tick
7. **Émettre** `error` non-null pour toute condition anormale (timeout, fail, stall, cancel) — les phases OK ont `error: null`

### D5 — Validation par pilote

Le pilote 2026-06-06 sur `WORKFLOW.solaris-airtable-clients` valide les 7 points du contrat D4 :

- ✅ D4.1 — Index lu (11 standards comptées)
- ✅ D4.2 — 7 standards sélectionnés pour DECIDE/EXECUTE/OBSERVE
- ✅ D4.3 — Standards injectés (format Markdown brut simulé)
- ✅ D4.4 — 8 lignes pulse.log écrites (Bash + PowerShell, schema identique)
- ✅ D4.5 — `cost_delta_usd` calculé par phase (mock MiniMax 2.7 rates)
- ✅ D4.6 — `cumulative_cost_usd` vérifié ≤ 0.015 USD << 0.50 USD SLA
- ✅ D4.7 — `error: null` sur 8/8 phases du tick démo

Artefacts produits par le pilote :

- `00_Amadeus/05_OSS_Twin/symphony/agent-os/` — install Agent OS
- `agent-os/standards/<11 standards>.md` + `index.yml`
- `agent-os/standards/schema-pulse-log.md` — le schema de D3
- `scripts/symphony-tick-demo.{sh,ps1}` — tick handler runnable
- `agent-os/pulse.log` — 8 lignes du tick démo (audit trail)

## Conséquences

### Positives

- **Observabilité native** — A0 peut maintenant `cat agent-os/pulse.log` et voir exactement ce que chaque tick a fait avec quels standards. Le reproche "daemon obscurs" adressé à N8N ne s'applique plus à Symphony.
- **Frugalité mesurable** — `cumulative_cost_usd` par tick + par workflow = alertes au-delà de `sla.max_cost_usd` avant le burn, pas après.
- **Reproductibilité** — un tick L2 Growth avec `standards_injected: [mission-contract, gate-decisions, …]` produit le même type de décision qu'un tick L1 IT avec les standards correspondants. Cross-layer benchmarking possible.
- **Drift standards détecté** — si un workflow omet d'injecter `forbidden-words.md` à EXECUTE, l'absence dans `standards_injected` du pulse.log le révèle. Lint-able.
- **Backfill possible** — rejouer un tick sur la base d'un `pulse.log` + un mock record = déterministe. Utile pour regression test.

### Négatives

- **Overhead I/O** — 8 écritures ligne-par-ligne par tick. Négligeable (≈ 2 KB / tick), mais à mesurer en tick haute fréquence (≤ 1s). Mitigation : batch append (5 phases → 1 fsync) si latence > 50ms.
- **Taille du prompt agent** — 7 standards × ~500 bytes = ~3.5 KB injectés en plus dans le prompt. Sur un tick L2 typique (5-10 KB de contexte), c'est +30-70%. Coût tokens augmente. Mitigation : `standards_inject` tronqué à 1 écran par standard, pas le fichier complet.
- **Pas de UI Symphony** — `pulse.log` reste textuel. Pour A0 qui veut du visuel, il faut un reader custom (cf. `schema-pulse-log.md` §Tooling future). Pas bloquant pour v1.
- **Coupling Agent OS ↔ Symphony** — Agent OS n'est plus "tooling CLI par projet" seulement, il devient **subordonné au tick cycle**. Si le projet Agent OS upstream casse une release, Symphony est impacté. Mitigation : `~/agent-os/` est detached de `.git`, snapshot par projet Symphony possible.

### Risques tracés

- **Risque 1 : standards obsolètes** — un standard `.md` n'est plus à jour. **Antidote** : `last_reviewed_at` dans le frontmatter, alerte L0 heartbeat si > 90 jours.
- **Risque 2 : pulse.log corruption** (crash mid-write). **Antidote** : chaque ligne = un seul `JSON.stringify` (atomic en pratique), newline final obligatoire, validation post-rotation par `jq -e .` sur le fichier compressé.
- **Risque 3 : drift format schema** (Agent OS v4 change le schema). **Antidote** : `schema_version: "1.0"` dans le pulse.log (champs 1ère ligne WAKE), refus de tick si version mismatch sans migration explicite.
- **Risque 4 : injection de standards involontaire** (un agent ré-injecte un standard pendant l'EXECUTE, faussant le pulse.log). **Antidote** : `standards_injected` est calculé par Symphony au DECIDE, sceau cryptographique possible v2.

## Suivi

- **Pilot validation** — artefact runnable à `symphony/scripts/symphony-tick-demo.{sh,ps1}`, sort 8/8 lignes schema-correct, gate=PASS, $0.015 USD
- **ADR-SYMPH-001** — non réécrit (immuable, cf. règle d'or #3), juste référencé comme parent
- **BP doc** — `wiki/L0/concept_agent_os_best_practices.md` §11 documente le rôle Agent OS dans Symphony
- **Wiki entity** — `entity_symphony_router.md` cross-référence cet ADR
- **Prochaine étape** : promotion de cet ADR en RATIFIÉ après 1 semaine d'usage du pilote en production. Si refus, retour au DRAFT avec motif.

## Références

- `AGENTS.md` (canon identité A0)
- `10_Tech_OS/12_Blueprints/02-ADR/ADR-SYMPH-001_symphony-replaces-n8n.md` (parent)
- `00_Amadeus/05_OSS_Twin/symphony/symphony-base.spec.md` (spec de référence)
- `00_Amadeus/05_OSS_Twin/symphony/L2/WORKFLOW.solaris-airtable-clients.md` (workflow pilote)
- `00_Amadeus/05_OSS_Twin/symphony/agent-os/standards/schema-pulse-log.md` (annexe technique)
- `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/L0/concept_agent_os_best_practices.md` §11 (BP doctrine)
- `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/L0/entity_symphony_router.md` (entity canon)
- `SDD-008` (Symphony orchestrator)
- `SDD-009` §2.3 (SLA triade)
- `ADR-RICK-001` (OpenHarness incarnation)
- `concept_shadow_l1_l2_heartbeat_symphony.md` (heartbeat doctrine)

---

*ADR RATIFIÉ 2026-06-06 (A0 explicite) après validation du pilote sur `WORKFLOW.solaris-airtable-clients` (8/8 phases, gate=PASS, $0.015 USD mock, schéma 14 champs conforme). Pilote = `symphony/scripts/symphony-tick-demo.{sh,ps1}`. Trace = `symphony/agent-os/pulse.log`.*

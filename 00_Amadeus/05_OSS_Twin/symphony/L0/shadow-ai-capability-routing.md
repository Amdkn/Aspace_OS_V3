# Shadow L0 Adapter — AI Capability Routing (Claude / GPT-Codex / Gemini)

> **Statut** : Shadow A0 — Symphony orchestrator adapter L0
> **Date** : 2026-05-15
> **Hérite** : `../symphony-base.spec.md`
> **Doctrine source** : SDD-010 §5.6 (Shadow L0 manuel — Triade IA)
> **Couche** : L0 Tech OS — opérateurs Shadow manuels transverses
> **État runtime** : ÉTAT 1 (Shadow manuel) — précurseur Open Hermes (ÉTAT 3 autonome)

---

## 0. Théorème en une phrase

> **"Les couches sont souveraines ; les modèles sont des véhicules. Symphony route par capacité, pas par dogme couche→modèle."**
> — SDD-010 §5.6.2

---

## 1. Contexte et Position

### 1.1 Pourquoi cet adapter existe

Symphony, dans sa version OSS native (printingpress.dev), suppose **un seul coding agent** branché (Codex app-server). En réalité, Amadeus opère en **Shadow L0 manuel** avec **trois IA distinctes** aux affordances complémentaires :

- **Claude / Claude Code** — actions profondes (fichiers, APIs, CLI)
- **GPT / Codex** — raisonnement, documentation, spec writing
- **Gemini / Antigravity** — vision navigateur, configuration SaaS

L'erreur V0 a été de **rigidement assigner** une IA à une couche (Claude=L0, GPT=L1, Gemini=L2). SDD-010 corrige cette doctrine.

### 1.2 Position dans Symphony

Ce fichier décrit comment **Symphony peut router une mission Shadow** vers le bon opérateur **selon la capacité requise**, et **non selon une couche cible**. C'est un adapter de **dispatching pré-Hermes**, en attendant le runtime autonome (cf. `open-hermes-runtime.md`).

```
┌──────────────────────────────────────────────────────────────────┐
│  Mission entrante (issue Plane / Airtable / ClickUp / Notion)   │
└────────────────────────────┬─────────────────────────────────────┘
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│  Symphony Router B1 (Jerry-niveau)                               │
│  Capability detection : extract `capability_tags` from issue    │
└────────────────────────────┬─────────────────────────────────────┘
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│  Shadow AI Capability Routing (ce document)                      │
│  Match capability → preferred operator                           │
└────────────────────────────┬─────────────────────────────────────┘
                             ▼
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        ┌──────────┐   ┌──────────┐   ┌──────────┐
        │  Claude  │   │  Codex   │   │  Gemini  │
        │  Code    │   │  GPT     │   │Antigravity│
        │  (file/  │   │  (spec/  │   │  (browser/│
        │   API)   │   │   doc)   │   │   SaaS)  │
        └────┬─────┘   └────┬─────┘   └─────┬────┘
             │              │               │
             └──────────────┴───────────────┘
                             ▼
                  Validation A0 (Amadeus)
```

---

## 2. Les 3 Opérateurs Shadow L0 — Profils

### 2.1 Claude / Claude Code

| Aspect | Détail |
|---|---|
| **Affordance** | Code, fichiers, APIs, CLI, refactor, actions filesystem |
| **Accès natif** | Bash, Edit, Write, Read, Glob, Grep, WebFetch, MCP |
| **Modes** | Claude Desktop (UI), Claude Code (CLI), Anthropic SDK |
| **Coût V0** | $$$$ (Sonnet/Opus) — réservé Rick A1 + arbitrages |
| **Coût V1** | $ via API Anthropic-compatible MiniMax 2.7 |
| **Quand l'utiliser** | Toute mission nécessitant interaction réelle avec le système (filesystem, git, docker, ssh, code execution) |
| **Quand l'éviter** | Recherche web profonde (Gemini meilleur), génération longue documentation (GPT meilleur) |
| **Limite doctrinale** | Ne devient pas l'orchestrateur global. Respecte les specs de couche. |

### 2.2 GPT / Codex

| Aspect | Détail |
|---|---|
| **Affordance** | Raisonnement, recherche, génération longue, découpage, QA |
| **Accès natif** | ChatGPT UI, Codex app-server, OpenAI SDK |
| **Modes** | Conversation manuelle, function-calling, JSON mode |
| **Coût V0** | $$$ (GPT-4o) |
| **Coût V1** | $ via OpenAI-compatible (DeepSeek, GLM) |
| **Quand l'utiliser** | PRD/ADR/DDD/TDD rédigés, SOPs, specs, lead research, breakdown d'issues complexes |
| **Quand l'éviter** | Manipulation directe filesystem (Claude meilleur), navigation web (Gemini meilleur) |
| **Limite doctrinale** | Ne remplace pas les Build Gates humains. La spec est validée par A0, pas auto-acceptée. |

### 2.3 Gemini / Antigravity

| Aspect | Détail |
|---|---|
| **Affordance** | Vision navigateur (Chrome), navigation web, configuration SaaS UI, screenshots |
| **Accès natif** | Antigravity IDE (Cursor-like), Chrome devtools MCP, Gemini SDK |
| **Modes** | UI interactive, agent navigateur, multimodal vision |
| **Coût V0** | $$ (Gemini 2.5 Pro) |
| **Coût V1** | $ via Gemini Flash + API direct |
| **Quand l'utiliser** | Configurer Baserow/Airtable/ClickUp/Notion via UI, inspecter pages web complexes, captures, debug visuel |
| **Quand l'éviter** | Code refactor profond (Claude meilleur), specs rédigées (GPT meilleur) |
| **Limite doctrinale** | Ne modifie pas le Kernel L0 sans passer par une spec validée. Travaille en surface visible. |

---

## 3. Capability Routing Table (canonique)

C'est la **table de vérité** que Symphony consulte pour router une mission Shadow.

```yaml
capability_routing:
  # ═══════════════════════════════════════════════════════
  # NAVIGATEUR / WEB / SaaS UI
  # ═══════════════════════════════════════════════════════
  browser_native:
    preferred: gemini_antigravity
    fallback: claude_code  # via puppeteer/playwright MCP
    use_for:
      - inspect_web_apps
      - configure_baserow
      - configure_airtable
      - configure_clickup
      - apply_notion_structure
      - apply_plane_structure
      - debug_traefik_routes
      - hostinger_panel_actions
      - take_screenshots
      - extract_data_from_visual_ui

  # ═══════════════════════════════════════════════════════
  # CODE / API / ACTIONS SYSTÈME
  # ═══════════════════════════════════════════════════════
  code_and_api_actions:
    preferred: claude_code
    fallback: codex
    use_for:
      - api_scripts
      - cli_tools
      - filesystem_operations
      - github_operations
      - mcp_to_cli_conversion
      - batch_imports
      - ssh_administration
      - docker_compose_edits
      - bash_scripting
      - python_data_processing
      - typescript_node_runtime
      - refactor_existing_code

  # ═══════════════════════════════════════════════════════
  # RAISONNEMENT / DOCUMENTATION / SPEC
  # ═══════════════════════════════════════════════════════
  reasoning_and_documentation:
    preferred: gpt_codex
    fallback: claude_code
    use_for:
      - write_prd
      - write_adr
      - write_ddd
      - write_tdd
      - write_sop
      - architecture_breakdown
      - issue_breakdown
      - lead_research
      - qa_review
      - long_form_synthesis
      - market_research
      - competitor_analysis

  # ═══════════════════════════════════════════════════════
  # ACTIONS HYBRIDES (multi-affordance)
  # ═══════════════════════════════════════════════════════
  hybrid_research_to_code:
    primary: gpt_codex          # rédige le plan
    handoff_to: claude_code     # exécute
    use_for:
      - implement_new_feature_from_research
      - bootstrap_new_repo
      - migrate_from_one_tool_to_another

  hybrid_ui_to_code:
    primary: gemini_antigravity  # inspecte + extrait structure
    handoff_to: claude_code      # code l'adapter
    use_for:
      - reverse_engineer_saas_api
      - generate_clickup_adapter
      - generate_baserow_schema
      - integration_from_visual_inspection

  hybrid_doc_to_runtime:
    primary: gpt_codex           # spec
    secondary: gemini_antigravity # configure UI cible
    handoff_to: claude_code      # automatise l'integration
    use_for:
      - new_symphony_adapter
      - new_marvel_squad_constitution
      - new_doctor_companion_skill
```

---

## 4. Règles de Traversée de Couches

> **Règle d'or** : Le modèle traverse les couches, mais **la spec ne traverse jamais sans autorisation**.

### 4.1 Traversées autorisées

| Opérateur | L0 | L1 | L2 | Conditions |
|---|---|---|---|---|
| **Claude Code** | ✅ | ✅ | ✅ | Doit respecter spec de couche destinée. SSH/filesystem autorisés en L0 uniquement avec passage par scripts validés. |
| **GPT-Codex** | ✅ | ✅ | ✅ | Lecture seule sur tous niveaux. Écriture dans `_SPECS/` pour PRD/ADR. |
| **Gemini-Antigravity** | ⚠️ | ✅ | ✅ | L0 limité à inspection (read-only). Modifications L0 interdites. |

### 4.2 Interdictions absolues

- ❌ **Gemini ne touche jamais** au Kernel L0 (Solarpunk Kernel, Hermes Agent, OpenHarness, Symphony Router) sans spec préalable validée par A0
- ❌ **Aucune IA ne crée de SDD** pendant le veto 90 jours (cf. SDD-010 §6). Seuls les `010b/c/...` exceptionnels permis.
- ❌ **Aucune IA ne modifie** un SDD ratifié dans `10_Tech_OS/12_Blueprints/01-SDD/` (immutabilité du Canon — Règle d'Or #3)
- ❌ **Aucune IA ne pousse en production** sans passage par les Build Gates Marvel (cf. SDD-009 §4 Fantastic 4 + Doom)

### 4.3 Vetos systémiques

| Veto | Déclencheur | Action |
|---|---|---|
| **Beth Veto** | 7 jours sans valeur L2 produite | Bascule de toutes IA vers tâches L2 cloud (Shadow L2 matrix 3×8) |
| **Rick Veto** | Souveraineté compromise (clé exposée, infra fragile) | Pause toute opération Cloud, focus L0 jusqu'à mitigation |
| **Donna DLQ Veto** | Crashloop détecté sur agent (>10 retries) | Halt + escalade A0 via Telegram/Email |
| **A0 Veto absolu** | Amadeus dit "stop" ou inaction prolongée | Toute IA s'arrête. Reprend uniquement sur instruction explicite. |

---

## 5. WORKFLOW.md — Capability Routing pour Symphony

Template à utiliser pour les missions Shadow nécessitant routage automatique :

```yaml
---
tracker:
  kind: capability_routed  # extension custom Symphony
  endpoint: internal://symphony-shadow-router
  source_trackers:
    - plane:    aspace-core
    - airtable: appXXX
    - clickup:  workspaceXXX
    - notion:   workspaceXXX

routing_strategy:
  type: capability_routing
  default_operator: claude_code  # fallback si capability_tags absent

  # Map issue labels → capabilities
  label_to_capability:
    "@browser":        browser_native
    "@code":           code_and_api_actions
    "@spec":           reasoning_and_documentation
    "@research":       reasoning_and_documentation
    "@research-to-code": hybrid_research_to_code
    "@ui-to-code":     hybrid_ui_to_code
    "@doc-to-runtime": hybrid_doc_to_runtime

operators:
  claude_code:
    command: "claude --output-format=stream-json -p"
    workspace: "/srv/aspace/workspaces/claude"
    api_compatible: anthropic
    backend_v0: anthropic-cloud
    backend_v1: minimax-2.7
    cost_per_million_tokens_v1: 0.30

  codex:
    command: "codex app-server"
    workspace: "/srv/aspace/workspaces/codex"
    api_compatible: openai
    backend_v0: openai-gpt4o
    backend_v1: deepseek-or-glm

  gemini_antigravity:
    command: "gemini-cli --browser-mode"
    workspace: "/srv/aspace/workspaces/gemini"
    api_compatible: google
    backend_v0: gemini-2.5-pro
    backend_v1: gemini-flash

polling:
  interval_ms: 60000

soc:
  schema_version: "1.0"
  capability_required: true     # rejet si pas de capability_tag

donna_dlq:
  enabled: true
  threshold_failed_attempts: 3
  escalation_chain:
    - retry_with_fallback_operator
    - escalate_a2_doctor
    - escalate_a1_rick
    - notify_a0_amadeus

a0_validation:
  required_for:
    - new_capability_definitions
    - cross_layer_traversals
    - cost_exceeding_dollars: 1.00
---

# Capability-Routed Mission Template

Tu es un opérateur Shadow L0 routé par capacité.

Mission : {{ issue.title }}
Capability détectée : {{ routing.capability }}
Opérateur sélectionné : {{ routing.operator }}
Layer ciblée : {{ routing.target_layer }}

Contraintes SLA :
- Temps max : {{ sla.max_execution_time_minutes }} min
- Coût max : ${{ sla.max_compute_budget_usd }}
- Layer traversal autorisé : {{ routing.allowed_layers }}

Règle d'or :
- Tu peux traverser les couches selon ta capacité
- Tu NE PEUX PAS modifier les SDDs ratifiés
- Tu DOIS valider auprès d'A0 si dépassement budget/temps
- Tu DOIS escalader vers Donna DLQ si >3 retries

{% if routing.handoff_to %}
HANDOFF : à la fin, prépare le contexte pour `{{ routing.handoff_to }}` qui prendra le relais.
{% endif %}
```

---

## 6. Exemples concrets de routage

### Exemple 1 — Issue Plane : "Configurer la table Baserow Warp Core W1-W12"

```yaml
labels: ["@ui", "@L1", "@30min"]
detected_capability: browser_native
routed_to: gemini_antigravity
rationale: |
  Configuration UI de Baserow = vision navigateur + clics multiples.
  Gemini Antigravity excelle ici.
  Claude pourrait faire via Baserow API mais friction supérieure.
```

### Exemple 2 — Issue Airtable : "Rédiger PRD-009a Symphony deploy Dokploy"

```yaml
labels: ["@spec", "@L0", "@deep-work"]
detected_capability: reasoning_and_documentation
routed_to: codex
rationale: |
  Rédaction PRD longue, structurée, multi-section.
  Codex/GPT excelle en spec writing.
  Claude pourrait mais Codex est plus économique pour 5000+ tokens output.
```

### Exemple 3 — Issue ClickUp : "Implémenter symphony-airtable.spec.md adapter"

```yaml
labels: ["@code", "@L2", "@hybrid"]
detected_capability: code_and_api_actions
routed_to: claude_code
rationale: |
  Écriture de fichier spec + connexion API Airtable + test.
  Claude Code natif sur fichiers + APIs.
  Spec écrite à partir du template symphony-base.spec.md.
```

### Exemple 4 — Hybride : "Migrer Plane data vers Plane self-hosted"

```yaml
labels: ["@research-to-code", "@L1"]
detected_capability: hybrid_research_to_code
primary: codex          # research export/import API Plane
handoff_to: claude_code # script Python de migration
rationale: |
  Codex documente la stratégie + identifie les endpoints API.
  Claude exécute le script de migration avec idempotence.
```

---

## 7. SLA par Opérateur

| Critère | Claude Code | GPT-Codex | Gemini-Antigravity |
|---|---|---|---|
| Latence p50 (par turn) | 8-15s | 5-12s | 10-30s (UI deps) |
| Cost p50 (mission moyenne, V1) | $0.05 | $0.03 | $0.10 |
| Cost p99 (mission complexe) | $0.50 | $0.30 | $1.00 |
| Risque (sandbox needed?) | Élevé (fs/sh) | Faible (text) | Moyen (UI) |
| Idempotence native | Bonne | Bonne | Faible (UI changes mid-flow) |
| Audit trail | Hooks Claude Code | OpenAI logs | Antigravity history |
| Disponibilité | 99.9% | 99.9% | 99% (browser deps) |

---

## 8. Anti-patterns à bloquer

| Anti-pattern | Symptôme | Détection automatique | Correction |
|---|---|---|---|
| Assignation rigide modèle→couche | "Claude doit faire L0 même si capacity browser" | `if label has @browser AND operator==claude AND no fallback: WARN` | Capability Routing automatique |
| Cascade infinie de fallbacks | Claude→Codex→Gemini→Claude... | retry_count > 3 | Donna DLQ escalation |
| Cross-layer écriture sans spec | Gemini modifie Kernel L0 | path matches `/srv/aspace/services/*` AND operator==gemini | Reject + log Donna |
| Cost runaway | Boucle infinie token consumption | sum(cost) > sla.max_compute_budget | Kill instance (cf. SDD-009 SLA Sentinel) |
| Confusion humain-runtime | A0 essaie d'utiliser Open Hermes A1 avant qu'il existe | A1 not_registered | Bascule en Shadow manuel (ce document) |

---

## 9. Migration Trajectory — Shadow → Autonome

| État | Période cible | Configuration | Document de référence |
|---|---|---|---|
| **1. Shadow manuel** | 2026-Q2/Q3 | Amadeus drive Claude/GPT/Gemini directement | **CE DOCUMENT** |
| **2. Shadow assisté** | 2026-Q4 | Symphony route automatiquement, A0 valide via Build Gates | Ce document + futur PRD-009a |
| **3. Runtime autonome** | 2027+ | Open Hermes A1 orchestre A2/A3 MiniMax/GLM 24/7 | `open-hermes-runtime.md` |

→ **Ce document est la photographie de l'État 1**, prêt à évoluer vers État 2 quand les Symphony adapters L1/L2 seront complets (7/7 specs).

---

## 10. Critères MUSE de cet adapter

Pour considérer Capability Routing comme "graduate" :

1. ✅ Documentation complète des 3 opérateurs + leurs affordances (ce doc)
2. ⏳ 3 semaines consécutives sans erreur de routage (à mesurer en production)
3. ⏳ <5% de fallback inter-opérateur sur le total des missions
4. ⏳ Tableau de logs accessible pour A0 (Donna DLQ + audit trail Symphony)
5. ⏳ Coût moyen mission < $0.10 (objectif frugalité V1)

---

## 11. Cross-refs Canon V0

| Doc | Lien |
|---|---|
| SDD-000c | A'Space Core / Shadow Frameworks pré-configurés — fondement théorique de Shadow A0 |
| SDD-003 | TARDIS Protocol — orchestration A2 Doctors qui utilisent ces opérateurs |
| SDD-008 | Shadow L1 Life OS — utilise Capability Routing pour configurer Baserow/Plane/Obsidian/Affine |
| SDD-009 | Shadow L2 Business OS — utilise Capability Routing pour Airtable/ClickUp/Notion |
| SDD-010 §5.6 | Doctrine Shadow L0 manuel (UPDATED) — source canonique de ce document |
| ADR-RICK-001 | OpenHarness Incarnation — Rick A1 différent d'opérateur Shadow |
| `symphony-base.spec.md` | Spec parent dont hérite cet adapter |
| `open-hermes-runtime.md` | Successeur autonome de ce document |

---

## 12. Non-Goals

- ❌ Cet adapter n'est PAS l'orchestrateur final V1 (c'est Open Hermes — cf. `open-hermes-runtime.md`)
- ❌ Pas d'automatisation complète Shadow→Autonome sans passage par État 2 assisté
- ❌ Pas de claim "Gemini > Claude > GPT" ou inverse — c'est **complémentaire**, pas hiérarchique
- ❌ Pas de couplage fort à une version spécifique des modèles (Sonnet 4.7, GPT-5, Gemini 2.5) — l'abstraction = capability, pas model_id

---

*Shadow A0 — AI Capability Routing — 2026-05-15 — Amadeus & Claude Architect*
*Pas un SDD. Pas un ADR. C'est un adapter Symphony L0 dans le Shadow A0 territory `00_Amadeus/05_OSS_Twin/symphony/L0/`.*
*Évolue librement. Sera promu en PRD/ADR lors de la 13ème Semaine #2 (juin 2026) si stabilisé 3 semaines.*

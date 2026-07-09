# ADR-SYMPH-002 — Variants Symphony par Harness Agentique

**Date :** 2026-05-26
**Auteur :** A0 Amadeus + A2 Claude Code
**Statut :** RATIFIÉ
**Type :** Architecture Decision Record (Tech OS / L0)
**Portée :** Capabilities, trust gating, scope par harness participant à Symphony
**Ancré sur :** ADR-SYMPH-001 (bus doctrine) · CLAUDE.md (fallback chain) · SDD-001 (anti-panic)

---

## Contexte

ADR-SYMPH-001 ratifie Symphony comme bus L0 et liste 6 harnesses (3 existants + 3 cibles). Sans matrice précise, chaque agent peut prétendre faire n'importe quoi. **Trois enjeux** :

1. **Anthropic refuse Claude SDK unattended** (cf. SPEC.md §1, point 3). Donc Claude Desktop natif Opus/Sonnet a un scope **différent** de Claude Code sur MiniMax.
2. **Antigravity** (Google IDE) est sandboxé — il a accès au filesystem du workspace ouvert mais pas au système global. Sa capacité Symphony est restreinte.
3. **Codex Desktop** vs **Codex CLI** ont des permissions différentes. Le user en a fait l'expérience hier (quota épuisé sur Codex Desktop, fusion Marina coupée).

Cet ADR définit la matrice unique faisant autorité.

## Décision — Matrice des 6 Variants

### V1 — `Claude_Code_CLI` (Claude Code sur MiniMax)

| Dimension | Valeur |
|-----------|--------|
| **Doctor préféré** | 11th (Produit/L1) |
| **Provider backbone** | MiniMax Token Plan Anthropic-compatible |
| **Trust scope** | `autonomy_scope` (Trust Zone + LLM_Wiki + skills draft) |
| **Tick mode** | Ephemeral via `heartbeat-tick.ps1 Claude_Code_CLI` |
| **Max turns/mission** | 20 (HEARTBEAT_CAP) |
| **Tempo** | on-demand (sessions A0) + every 15m work-hours (Task Scheduler) |
| **Capabilities Symphony** | Émet+consomme tous topics. Peut écrire ADRs/SDDs. Peut spawn sub-agents via Agent tool. |
| **Restrictions** | Pas de prod-deploy direct (requires_signoff). Pas de modification settings.json sans A0 confirmation. |
| **MCP servers** | airtable, browsermcp, clickup, context7, hostinger, notion, supabase, playwright, claude-preview, etc. |

### V2 — `Codex_CLI` (OpenAI Codex CLI)

| Dimension | Valeur |
|-----------|--------|
| **Doctor préféré** | 13th (Machine/L0) |
| **Provider backbone** | OpenAI gpt-5.5 / o-series |
| **Trust scope** | `autonomy_scope` (Trust Zone) + permissions PowerShell surgical edits |
| **Tick mode** | Ephemeral via `heartbeat-tick.ps1 Codex_CLI` |
| **Max turns/mission** | 20 |
| **Tempo** | every 15m work-hours (Mon-Fri 09-19) |
| **Capabilities Symphony** | Spécialisé infra Windows, robocopy, junctions, git, PowerShell. Émet topics `infra-*`, `build-*`, `git-*`. |
| **Restrictions** | Quota OpenAI direct — saturable rapidement. **Fallback automatique vers Gemini_CLI** sur 429 (cf. ADR-HEART-002). |
| **Cas d'échec connu** | 2026-05-25 quota épuisé en plein milieu de fusion Marina → fix A3 OAuth Notion bloqué côté CCdesk. |

### V3 — `Gemini_CLI` (Google Gemini CLI / Conductor)

| Dimension | Valeur |
|-----------|--------|
| **Doctor préféré** | 12th (Forge/L2) |
| **Provider backbone** | Google Gemini 2.0 Pro / Flash |
| **Trust scope** | `autonomy_scope` (Trust Zone) — context window très large (1M+ tokens) |
| **Tick mode** | Ephemeral via `heartbeat-tick.ps1 Gemini_CLI` |
| **Max turns/mission** | 20 |
| **Tempo** | every 15m work-hours |
| **Capabilities Symphony** | Spécialisé synthèse long contexte (LLM Wiki ingestion, takeout parsing). Émet topics `wiki-*`, `synthesis-*`, `research-*`. |
| **Restrictions** | Pas de write hors Trust Zone. Pas de secrets logging. |
| **Avantage unique** | Le **seul** à pouvoir digérer 100k+ lignes d'un coup (ex: re-ingestion Takeout). |

### V4 — `Antigravity_IDE` (Google Antigravity)

| Dimension | Valeur |
|-----------|--------|
| **Doctor préféré** | Aucun rôle Doctor — sert d'**éditeur** pour A0 |
| **Provider backbone** | Gemini 2.5 (intégré IDE) |
| **Trust scope** | Sandboxé au workspace IDE ouvert |
| **Tick mode** | **Pas de tick** — Antigravity est interactif, pas autonome |
| **Max turns/mission** | N/A (sessions interactives A0) |
| **Tempo** | on-demand uniquement |
| **Capabilities Symphony** | **Consomme** des topics (lit inbox skills/SOPs depuis Notion ou local). N'**émet** pas dans le bus. |
| **Restrictions** | Ne peut PAS être déclenché par Task Scheduler. Ne peut PAS modifier settings.json/MCP config. |
| **Cas d'usage** | A0 ouvre Antigravity pour éditer du code généré par Claude Code/Codex via Symphony. Antigravity = **dernier kilomètre humain**. |

### V5 — `Claude_Desktop_App` (Anthropic Opus/Sonnet natif)

| Dimension | Valeur |
|-----------|--------|
| **Doctor préféré** | Aucun — sert de **console A0 premium** pour décisions stratégiques |
| **Provider backbone** | Anthropic API directe (Opus 4.7 ou Sonnet 4.6) |
| **Trust scope** | Sandboxé natif Anthropic — **pas d'autonomie unattended** (refus Anthropic) |
| **Tick mode** | **Pas de tick** — interactif uniquement |
| **Max turns/mission** | Illimité dans la session A0 |
| **Tempo** | on-demand uniquement |
| **Capabilities Symphony** | **Consomme** topics (lecture LLM_Wiki, ADRs, propositions stratégiques). Peut générer des artefacts (ADRs draft) qu'A0 colle ensuite ailleurs. |
| **Restrictions** | Ne peut PAS exécuter de tick autonome. Ne peut PAS écrire directement dans le filesystem A'Space (sauf via MCP filesystem + A0 supervision). |
| **Cas d'usage** | Discussions architecturales profondes Opus 4.7 quand Claude Code MiniMax est insuffisant. Génération ADRs draft. |

### V6 — `Codex_Desktop` (OpenAI Codex Desktop App)

| Dimension | Valeur |
|-----------|--------|
| **Doctor préféré** | Aucun — variant interactif IDE-style |
| **Provider backbone** | OpenAI direct (mêmes models que Codex_CLI mais via UI) |
| **Trust scope** | Workspace ouvert |
| **Tick mode** | **Pas de tick** — interactif |
| **Max turns/mission** | Quota OpenAI direct |
| **Tempo** | on-demand |
| **Capabilities Symphony** | **Consomme** topics. Peut écrire vers le workspace ouvert. |
| **Restrictions** | Quota saturable (cas Marina 2026-05-25). **Pas de fallback automatique** vers Claude Code car interactif. |
| **Cas d'usage** | Tâches "main-d'œuvre" pour code lourd avec supervision A0. |

## Synthèse des dimensions

| Variant | Tick auto | Émet topics | Consomme | Provider | Trust |
|---------|-----------|-------------|----------|----------|-------|
| Claude_Code_CLI | ✓ | ✓ | ✓ | MiniMax | autonomy_scope |
| Codex_CLI | ✓ | ✓ | ✓ | OpenAI | autonomy_scope |
| Gemini_CLI | ✓ | ✓ | ✓ | Google | autonomy_scope |
| Antigravity_IDE | ✗ | ✗ | ✓ | Google | sandbox |
| Claude_Desktop_App | ✗ | ✗ | ✓ | Anthropic | sandbox |
| Codex_Desktop | ✗ | ✗ | ✓ | OpenAI | sandbox |

**Règle générale** : seuls les variants `_CLI` ont l'autonomie de tick. Les variants `_IDE`/`_App`/`_Desktop` sont des **consoles interactives** pour A0, jamais des participants actifs au bus.

## D2 — Désignation par Doctor (extension fallback chain)

Mise à jour de la fallback chain de CLAUDE.md pour intégrer les 3 nouveaux variants comme consoles A0 (pas dans le bus):

```
13th Doctor (Machine/L0)
  Auto tick : Codex_CLI → Gemini_CLI → Claude_Code_CLI
  Console A0 : Codex_Desktop

12th Doctor (Forge/L2)
  Auto tick : Gemini_CLI → Claude_Code_CLI → Codex_CLI
  Console A0 : Antigravity_IDE (pour synthèse long contexte)

11th Doctor (Produit/L1)
  Auto tick : Claude_Code_CLI → Gemini_CLI → Codex_CLI
  Console A0 : Claude_Desktop_App (pour décisions Opus/Sonnet)
```

## D3 — Capsule par variant

Pour les 3 variants existants (`Codex_CLI`, `Gemini_CLI`, `Claude_Code_CLI`), les capsules existent déjà dans `Shadow_L0/agents/`. Pour les 3 nouveaux variants console :

- **Pas de capsule `Shadow_L0/agents/`** — ce sont des consoles, pas des participants
- A0 utilise ces consoles depuis sa propre session
- Les artefacts produits sont collés dans Trust Zone via Claude Code CLI (qui devient le scribe)

## Conséquences

### Positives
- Plus d'ambiguïté sur qui peut faire quoi. La capsule définit le scope.
- Le quota épuisement Codex Desktop (Marina) est désormais **attendu et géré** : la console n'est PAS dans le tick, donc son crash ne casse pas Symphony.
- Antigravity et Claude Desktop sont valorisés comme consoles A0 sans être confondus avec des agents tick.

### Négatives
- Si A0 veut un jour exécuter une mission autonome depuis Antigravity ou Claude Desktop, **interdit** par cet ADR. Workaround : demander à Claude_Code_CLI de l'exécuter, ou utiliser Codex Desktop comme proxy supervisé.

### Risques tracés
- **Antigravity peut se mettre à jour** vers un mode "agent autonome" un jour (Google direction). Si ça arrive, cet ADR devra être amendé.
- **Claude Desktop** pourrait intégrer un mode agent natif Anthropic. Même règle.

## Suivi

- **ADR-HEART-002** — instrumentation anti-panique par variant
- Doc capsules : maintenir `Shadow_L0/agents/<X>/Context.md` à jour selon scope défini ici

## Références

- ADR-SYMPH-001 — bus doctrine parent
- CLAUDE.md — fallback chain canon
- Shadow_L0/SPEC.md §1 — refus Anthropic unattended
- Marina incident 2026-05-25 — illustration quota Codex Desktop

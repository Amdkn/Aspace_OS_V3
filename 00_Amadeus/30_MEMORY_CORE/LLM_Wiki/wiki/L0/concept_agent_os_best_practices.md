---
source: buildermethods/agent-os v3.0 (lecture directe) + bad-config Antigravity 2026-05-31 + correction A0 2026-06-06
date: 2026-06-06
type: concept
domain: L0 Tech_OS / build tooling / agent interface / standards discipline
title: Agent OS — Best Practices (Agent Interface, not Per-Project)
tags: [#agent_os #best_practices #agent_interface #standards_discipline #anti_patterns #L0 #canonical]
related:
  - concept_agent_os_adoption.md  (pilot-biaisé, superseded par cette fiche)
  - concept_skill_reflex.md
supersedes: concept_agent_os_adoption.md (pilot-biaisé — install par projet uniquement)
---

# 🧭 Agent OS — Best Practices pour A'Space OS V2

> **Source de vérité** : `github.com/buildermethods/agent-os` (v3.0) + doc
> `buildermethods.com/agent-os/installation`. Pas de fabrication ; chaque règle est
> ancrée sur la doc officielle ou sur un diagnostic concret du bad config
> Antigravity (2026-05-31) que cette fiche remplace.

## 1. Cadrage correct — interface agent, PAS un outil par projet

Agent OS est un **système léger de Standards + de Spec-shaping** qui fait que *« les
agents construisent comme TU construirais »*. Mais son **mode de déploiement**
est ce qui compte :

- **Officiel** (doc) : *« Two-part installation. Base installation lives in your
  home directory (~/agent-os/). Project installation lives in your project
  (your-project/agent-os/). This separation lets you maintain standards across
  multiple projects while keeping each project self-contained. »*
- **Mauvais cadrage** (le piège Antigravity 2026-05-31 + l'overshoot Opus
  2026-06-06) : installer dans un seul projet sans base, et vouloir l'appliquer
  à 5+ projets d'un coup.

**Bonne métaphore A'Space** : Agent OS = `~/.claude/` (interface agent
persistant) + couche projet optionnelle. Ce n'est **pas** un fichier dans
chaque app.

## 2. Doctrine 2-part (la règle d'or)

| Part | Emplacement | Contenu | Qui la maintient |
|---|---|---|---|
| **Base** | `~/agent-os/` (Windows: `%USERPROFILE%\agent-os\`) | `profiles/`, `scripts/`, `commands/`, `config.yml` | **One-shot, agent-level**. Stable. |
| **Project** | `<project>/agent-os/` | `standards/`, `standards/index.yml` | **Optional, par projet actif seulement**. |

**Étapes officielles** :

```bash
# Step 1 (one-time, agent-level)
cd ~
git clone https://github.com/buildermethods/agent-os.git
rm -rf ~/agent-os/.git   # détaché du remote — c'est TA base

# Step 2 (par projet actif — PAS pour tous les projets d'un coup)
cd /path/to/active/project
~/agent-os/scripts/project-install.sh          # OU --profile X / --commands-only
```

**Windows** : utiliser Git Bash (déjà installé) — la doc recommande WSL mais
Git Bash suffit pour les 3 scripts bash.

## 3. Critères d'un standard (vs pas un standard)

Un fichier dans `agent-os/standards/` doit être **transversal, concis,
opinionated** — pas une doc d'implémentation.

| ✅ Bon standard | ❌ Pas un standard |
|---|---|
| Conventions de naming (fichiers, variables) | Code de migration DB spécifique |
| Format d'API response (envelope `{success, data, error}`) | Logique métier d'une feature |
| Error handling patterns (codes, propagation) | Placeholder vide (`"Définissez vos règles ici."`) |
| Patterns state management (React 19, V2 ArkTS) | Transcript YouTube / article de blog |
| Structure de dossiers par feature | Spec d'une feature particulière (vit dans `specs/`, pas `standards/`) |
| Patterns de test (unit, integration, e2e) | Tech-stack générique (vit dans `profiles/.../global/tech-stack.md`) |

**Règle d'or** : si tu ne l'injecterais **pas dans 3 contextes différents**,
c'est probablement un doc projet, pas un standard. → `specs/`, pas `standards/`.

## 4. Hygiène de l'index (`standards/index.yml`)

L'index est **la carte que lit `/inject-standards`**. S'il est cassé,
`/inject-standards` crash ou injecte des fantômes.

| Règle | Pourquoi |
|---|---|
| **Chaque entrée DOIT pointer vers un fichier qui existe** | Sinon `/inject-standards` crashe au read |
| **Chaque standard .md DOIT apparaître dans l'index** | Sinon il est invisible au matching |
| **Pas de placeholder dans la description** | Index = matching, pas narration |
| **Re-générer l'index après chaque modif** via `/index-standards` | Sinon drift entre FS et index |

**Diagnostic 2026-05-31** : Antigravity a laissé `index.yml` avec 3 entrées
(`global/naming`, `api/response-format`, `database/migrations`) mais SEUL
`database/migrations.md` existe réellement. Les 2 autres sont des fantômes
qui auraient fait crasher `/inject-standards` au premier usage.

## 5. Profile strategy (par app family / mode AaaS)

```
profiles/
├── default/
│   └── global/
│       └── tech-stack.md       # socle transversal (toujours inclus)
├── solaris/                    # mode AaaS Solaris (visual-first)
│   ├── global/
│   ├── frontend/
│   └── backend/
├── nexus/                      # mode AaaS Nexus (data-first)
└── orbiter/                    # mode AaaS Orbiter (field)
```

- **Default** = socle. Toujours actif. Contient `tech-stack.md` (la doc sur
  les choix de stack, pas les conventions).
- **Profiles custom** = un par mode AaaS, créé via `sync-to-profile.sh` depuis
  une app qui exemplifie bien le mode.
- **Héritage** : `profile-a: inherits_from: default` (config.yml).

## 6. Frugalité — le cœur de l'intérêt sous MiniMax

C'est **le** argument pour adopter Agent OS dans A'Space :

- **Sans** Agent OS : l'agent relit TOUT le contexte à chaque tour (coûteux en
  tokens, surtout sous MiniMax).
- **Avec** Agent OS : `/inject-standards [zone]` injecte **seulement les
  standards pertinents** au contexte courant.

C'est la même logique que les `rules/` ECC mais **par projet** (les rules ECC
sont globales ; les standards Agent OS sont par-repo).

## 7. Quand installer dans un projet (matrice de décision)

| Situation | Verdict |
|---|---|
| Tu vas **construire activement** une feature dans le projet | ✅ Installe (Phase project) |
| Tu fais un **pilote pour valider les Best Practices** | ✅ Installe, **1 seul projet** |
| Tu veux juste que les agents connaissent les standards du projet | ❌ Référence `~/agent-os/profiles/` dans l'AGENTS.md/CLAUDE.md du projet, n'installe pas |
| Tu installes par mimétisme dans tous les projets | ❌ STOP. Drift garanti, dette de maintenance |
| Tu installes dans le **canon** (ASpace_OS_V2, _SPECS, Memory) | ❌ JAMAIS. Le canon = mémoire, pas build. |

## 8. Anti-patterns (avec exemples concrets du bad config)

| Anti-pattern | Exemple concret (Antigravity 2026-05-31) |
|---|---|
| **Project-only sans base** | `ASpace_OS_V2/.agent-os/` installé, mais `~/agent-os/` absent. Viol la doctrine 2-part. |
| **Install dans le canon** | `ASpace_OS_V2/.agent-os/` — c'est la couche mémoire/build-bearing doctrine, pas une app. |
| **Index fantôme** | `index.yml` référence `global/naming.md` + `api/response-format.md` qui n'existent pas. |
| **Stub vide comme standard** | `standards/database/migrations.md` = `Définissez vos règles ici.` (placeholder) |
| **Spec = transcript externe** | `specs/i-built-a-full-seo-system-with-antigravity-agent-os.md` = fiche YouTube (`YT-mS1lCfJ5Yig`) mal classifiée. |
| **Hors-scope structures** | `dashboard/index.html`, `product/` (vide) — Agent OS n'a pas de dashboard concept. |
| **Roll-out multi-projets sans pilote** | Vouloir installer dans solaris + omk + alikaly + marina + rilcot d'un coup. |

## 9. Plan concret pour A'Space (post-doctorine, post-correction)

| # | Action | Priorité | Statut |
|---|---|---|---|
| 1 | Écrire cette fiche Best Practices (cette doc) | 🔴 P0 | ✅ FAIT 2026-06-06 |
| 2 | Cloner `~/agent-os/` (base install) | 🔴 P0 | ✅ FAIT 2026-06-06 (166K, .git detached) |
| 3 | Cleanup `ASpace_OS_V2/.agent-os/` → `_TRASH/` (bad config) | 🟠 P1 | ✅ FAIT 2026-06-06 (move vers `_TRASH/2026-06-06_agent-os-bad-config/`, no hard-delete) |
| 4 | **Une** project-pilote (solaris-landing recommandé — a déjà `AGENTS.md` + `CLAUDE.md` propres) pour valider les BP | 🟡 P2 | ✅ FAIT 2026-06-06 — 13 standards découvertes + index.yml propre (zéro phantom, zéro "Needs description") |
| 5 | Roll-out aux autres projets (omk/alikaly/marina/rilcot) | ⛔ Bloqué | Pas avant validation du pilote |

**Note** : on **ne fait PAS** le roll-out. La doctrine est : pilote d'abord,
puis décision sur le scope.

## 10. Verdict

**Adopter Agent OS — mais à la base, pas au projet.** C'est la **pièce
manquante de la couche interface agent** : il codifie les standards par repo
et les injecte frugalement, exactement ce qu'il faut pour que MiniMax/Hermes
buildent « comme A0 » sans gonfler le contexte. Il **complète** (ne remplace
pas) les `rules/` ECC + le pipeline SDD/Picard + le 3-Turn Air Lock.

**Mais** : ne pas reproduire le bad config Antigravity. Base d'abord, projet
seulement quand on build activement, jamais dans le canon.

---

## 11. Rôle dans Symphony (recadrage A0 2026-06-06)

> **Post-cadrage A0** : Agent OS n'est pas qu'un outil CLI par projet.
> C'est aussi **l'interface d'observabilité + injection de standards**
> consommée par les tick handlers **Symphony** (le bus qui remplace N8N,
> ratifié par [ADR-SYMPH-001](https://github.com/buildermethods/agent-os)).

### 11.1 Position dans la stack

```
Symphony tick (WAKE→SLEEP)
  ├─ Tick handler (heartbeat-tick-symphony.ps1)
  │   ├─ Lit agent-os/standards/index.yml          ← Agent OS
  │   ├─ Sélectionne standards pertinents          ← Agent OS
  │   ├─ Injecte dans le prompt agent éphémère     ← Agent OS
  │   └─ Écrit pulse.log structuré (1 ligne/phase) ← Agent OS
  ├─ Agent éphémère (Hermes / Codex / Claude Code)
  └─ Tracker source (Airtable / ClickUp / Notion / …)
```

### 11.2 Mapping commande → phase tick

| Commande Agent OS | Phase Symphony qui l'invoque | Effet |
|---|---|---|
| `/discover-standards` | LEARN (rare, manuel) | Coder les patterns tribaux d'un workflow en `standards/<category>/<name>.md` |
| `/index-standards` | LEARN (rare, manuel) | Reconstruire `standards/index.yml` à partir des `.md` |
| **`/inject-standards`** | **PROBE + DECIDE (chaque tick)** | **Injecter les standards filtrés dans le prompt agent** |
| `/plan-product` | WAKE (rare, intention A0) | Spec-shaping d'un nouveau WORKFLOW.md |
| `/shape-spec` | WAKE (rare, intention A0) | Affinage d'un WORKFLOW.md existant |

`/inject-standards` est la commande **chaude** — elle tourne à chaque
tick. Les 4 autres sont **froides** (invoked rarely, à la main).

### 11.3 Pilot cible (validation BP)

**Workflow** : `00_Amadeus/05_OSS_Twin/symphony/L2/WORKFLOW.solaris-airtable-clients.md`

**Install location** : `symphony/agent-os/` (au niveau racine — couvre
L0 + L1 + L2. Plus simple, testable).

**Standards discover** (~10) : mission-contract, soa-routing,
gate-decisions, forbidden-words, sla-triple, candidate-record-rule,
airtable-specifics, expected-proof, writeback-policy, tick-handoff.

**Observabilité 8 phases** : schema `pulse.log` (1 ligne JSON par phase
WAKE→SLEEP) + demo tick `symphony-tick-demo.{ps1,sh}` qui simule un
record Airtable et écrit les 8 lignes.

**Ratification** : [`ADR-SYMPH-003_agent-os-standards-injection.md`](../../../../../10_Tech_OS/12_Blueprints/02-ADR/ADR-SYMPH-003_agent-os-standards-injection.md)
(post-pilote, même session, ne réécrit pas l'ADR-SYMPH-001).

### 11.4 Différence avec le cadrage initial (CLI par projet)

| Avant (cadrage 1) | Après (cadrage 2, A0 2026-06-06) |
|---|---|
| Agent OS = tooling CLI par projet (solaris-landing) | Agent OS = **couche d'injection + observabilité** pour les ticks Symphony |
| Pilote Next 16 (validé ✅) | **Pilote WORKFLOW Symphony** (validation de la thèse) |
| 13 standards Next/React | ~10 standards workflow (mission contract, gates, SLA, etc.) |
| `/inject-standards` = confort dev | **`/inject-standards` = chaleur même du tick** |

Le cadrage 1 n'est pas faux — il complète le cadrage 2. Agent OS est
utile **à la fois** au niveau projet (CLI par codebase) et au niveau
workflow (injection tick).

### 11.5 Cross-refs

- [`ADR-SYMPH-001_symphony-replaces-n8n.md`](../../../../../10_Tech_OS/12_Blueprints/02-ADR/ADR-SYMPH-001_symphony-replaces-n8n.md) (ratifié 2026-05-26)
- `00_Amadeus/05_OSS_Twin/symphony/symphony-base.spec.md` §12 (Logging) + §7 (Tick state machine)
- `00_Amadeus/05_OSS_Twin/symphony/L2/WORKFLOW.solaris-airtable-clients.md` (workflow pilote)
- `entity_symphony_router.md` (entity canon)
- `concept_shadow_l1_l2_heartbeat_symphony.md` (heartbeat doctrine)

---

## Annexe — Quick reference

### Commandes
| Commande | Rôle |
|---|---|
| `/discover-standards` | Extrait le tribal knowledge du codebase → standards concis |
| `/index-standards` | Reconstruit `standards/index.yml` (carte pour matching) |
| `/inject-standards [zone]` | Injecte seulement les standards pertinents |
| `/plan-product` | Docs produit (mission, roadmap, tech-stack) via AskUserQuestion |
| `/shape-spec` | **En plan mode** : façonne un meilleur spec avant de builder |

### Scripts
| Script | Usage |
|---|---|
| `~/agent-os/scripts/project-install.sh` | Install dans un projet (depuis la base) |
| `~/agent-os/scripts/project-install.sh --profile X` | Avec un profile spécifique |
| `~/agent-os/scripts/project-install.sh --commands-only` | Update commands only (preserve standards) |
| `~/agent-os/scripts/sync-to-profile.sh` | Crée/met à jour un profile depuis un projet |

*Best Practices — ancré sur la doc officielle v3.0 + diagnostic du bad config
Antigravity. 2026-06-06. Cette fiche SUPERSEDE
`concept_agent_os_adoption.md` (pilot-biaisé).*

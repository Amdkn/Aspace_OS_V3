---
source: GitHub buildermethods/agent-os (v3.0, lecture directe) + Builder Methods (Brian Casel) — plan A0 2026-06-06
date: 2026-06-06
type: concept
domain: L0 Tech_OS / build tooling / standards & spec-shaping
title: Agent OS — Plan Stratégique d'Adoption A'Space
tags: [#agent_os #standards #spec_shaping #build_layer #emyth #buildermethods #L0 #aligned]
---

# 🛠️ Agent OS — Plan Stratégique d'Adoption dans A'Space OS V2

> **Source de vérité** : `github.com/buildermethods/agent-os` (v3.0) + `buildermethods.com/agent-os` (docs),
> `/tools`, `/kits`, `/pro/build-with-ai-course`, `/pro/claude-code-course` (Brian Casel). Plan ancré sur la
> lecture directe du repo ; les cours/kits = ressources d'apprentissage officielles (non distillées ici).

## 1. Ce qu'est Agent OS (précis, v3.0)
Un **système léger de Standards + de Spec-shaping** qui fait que *« les agents construisent comme TU
construirais »*. Marche **à côté** de Claude Code / Cursor / Antigravity, tout langage/framework.
4 capacités + 5 commandes :
| Commande | Rôle |
|---|---|
| `/discover-standards` | extrait le savoir tacite du codebase → standards **concis** (scannables par l'IA, sans gonfler le contexte) |
| `/index-standards` | construit `agent-os/standards/index.yml` (map standard→description) |
| `/inject-standards [zone]` | injecte **seulement les standards pertinents** dans le contexte (auto ou explicite) |
| `/plan-product` | docs produit interactifs (`agent-os/product/` : mission, roadmap, tech-stack) via AskUserQuestion |
| `/shape-spec` | **en plan mode** : façonne un meilleur spec avant de builder |
- **Profiles** (`profiles/default/global/…`, héritage via `config.yml`) = jeux de standards réutilisables (ex. tech-stack).
- Install : `scripts/project-install.sh` (par repo) + `sync-to-profile.sh`.

## 2. Pourquoi ça colle à A'Space (le gap qu'il comble) — lien E-Myth
Agent OS **EST** un outil E-Myth pour le code : il transforme ton savoir-faire tacite en **système
reproductible** que n'importe quel agent (CLI MiniMax, Hermes) applique à l'identique. Le gap précis :
- Tes **`rules/` ECC** = standards **globaux/comportementaux** (qualité, sécurité, langage). ✔ gardés.
- Mais les **standards spécifiques par app** (Next 16 de solaris-aaas, le stack alikaly-os, conventions par repo)
  **ne sont pas codifiés**. → `/discover-standards` les extrait, `/inject-standards` les sert **frugalement**
  (clé pour MiniMax : on n'injecte que le pertinent, pas tout le rule-set).
- `/shape-spec` = la couche **spec légère en plan mode**, complément du **3-Turn Air Lock** + pipeline SDD→PRD→ADR→DDD.

## 3. Où ça se branche (la couche BUILD)
Agent OS vit au niveau des **repos qui buildent** = `30_Business_OS/10_Projects/<projet>/apps/<role>/`
(solaris-aaas, aaas-os, alikaly-os, rilcot-members, marina…). Install **par app**, jamais dans la doctrine profonde.
- **Profiles** ↔ **modes AaaS** : un profile `solaris` (visual-first), `nexus` (data-first), `orbiter` (field) —
  standards partagés par mode, hérités du `default`.
- **Runtime** : tourne sous **Claude Code CLI (MiniMax-M3)** + orchestrable par **Hermes** (non-interactif, trust déjà accordé).

## 4. Mapping anti-duplication (Agent OS ↔ A'Space)
| Agent OS | Équivalent A'Space | Décision |
|---|---|---|
| standards (par repo) | `rules/` ECC (global) | **complémentaire** : ECC=global, Agent OS=codebase-spécifique |
| `/plan-product` (mission/roadmap) | Picard JTBD + B1 direction + SDD | Agent OS pour le **repo**, SDD/Picard pour le **business** |
| `/shape-spec` | 3-Turn Air Lock + ADR/DDD | shape-spec = pré-spec léger en plan mode |
| profiles | AaaS modes (Solaris/Nexus/Orbiter) | profiles = jeux de standards par mode |
| inject-standards (frugal) | (nouveau) | **gain clé** : contexte frugal MiniMax |

## 5. Roadmap d'adoption (phasée, post-quota = sur MiniMax CLI)
1. **Pilote `solaris-aaas`** : `project-install.sh` dans `10_Projects/solaris/apps/landing` → `/discover-standards`
   (Next 16, structure, lead-capture) → `/index-standards`. Vérifier que `agent-os/` est gitignoré ou commité au choix.
2. **Prochaine feature** : `/shape-spec` en plan mode → build avec `/inject-standards` (mesurer le gain de contexte).
3. **Profile `solaris`** : `sync-to-profile.sh` → réutiliser sur aaas-os. Créer profiles `nexus`/`orbiter` à mesure.
4. **Roll-out** : répéter sur omk/alikaly/marina/rilcot. Un profile par mode AaaS.
5. **Hermes** : standards = contexte injecté aux Marvel squads (Flash/Avengers) lors des builds — relais autonome.
6. **Apprentissage A0** : `claude-code-course` + `build-with-ai-course` + `kits`/`tools` (Builder Methods Pro) = la formation Visionnaire pour piloter sans devenir Technicien.

## 6. Garde-fous
- **Install par app courte** (`10_Projects/.../apps/`), respecter MAX_PATH/junction (ADR-INFRA-002/003).
- **Ne pas dupliquer** `rules/` ECC ni la doctrine Spock — Agent OS = couche repo uniquement.
- **Frugalité** : `/inject-standards` ciblé (cœur de l'intérêt sous MiniMax).
- **Veto 90j SDD** : Agent OS = outil Shadow A0 / build-layer, pas un nouveau SDD.
- Secrets jamais dans `agent-os/` ; standards = conventions, pas de clés.

## 7. Verdict
**Adopter** — Agent OS est la **pièce manquante de la couche build** : il codifie les standards par repo et les
injecte frugalement, exactement ce qu'il faut pour que MiniMax/Hermes buildent « comme A0 » sans gonfler le
contexte. Il **complète** (ne remplace pas) ECC rules + le pipeline SDD/Picard + le 3-Turn Air Lock.

*Plan d'adoption — ancré sur le repo v3.0. Pilote = solaris-aaas. 2026-06-06.*

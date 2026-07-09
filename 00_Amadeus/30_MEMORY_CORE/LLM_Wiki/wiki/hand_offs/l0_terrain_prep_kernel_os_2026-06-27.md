---
id: handoff-l0-terrain-prep-kernel-os-2026-06-27
title: Terrain-prep L0 Kernel OS — SSOT .claude → alignement .hermes/.codex, activation Doctrines Hermes, Local-First avant VPS
date: 2026-06-27
author: A0 jumeau numérique (Opus) — F3 (prépare le terrain du 3ème plan L0 que A0 lance au prochain tour en Plan Mode)
status: TERRAIN-PREP — D1 recon done, plan L0 à écrire (prochain tour, Plan Mode)
sister:
  - plans/fancy-hugging-bengio.md (L1 Life OS)
  - plans/giggly-wiggling-fern.md (L2 Business OS)
  - 10_Tech_OS/12_Blueprints/01-SDD/SDD-009 (conception à DÉPASSER en Local-First)
scope: L0 Tech OS / Rick's Verse — Kernel OS qui développe + applique L1 + L2
---

# Terrain-prep L0 Kernel OS

> **But du 3ème plan (L0, prochain tour)** : préparer l'**activation des Doctrines pour Hermes**, en utilisant **`C:\Users\amado\.claude` comme SSOT** pour structurer/aligner **`.hermes`** et **`.codex`**, afin que les **Agents du Kernel OS développent + appliquent** les plans Life OS (L1) + Business OS (L2) — **Local-First avant retour VPS**, en **dépassant** la conception SDD (`10_Tech_OS/12_Blueprints/01-SDD`).

## 1. La pile à 3 plans (alignement L0/L1/L2)

| Plan | Niveau | Fichier | Rôle | État |
|---|---|---|---|---|
| **L1 Life OS** | Fleet (Beth/Morty) | `plans/fancy-hugging-bengio.md` | A1 Gatekeepers + 6 frameworks + cycle 12WY Q3 + Life-OS-2026 | actif |
| **L2 Business OS** | Pulse (Jerry/Summers) | `plans/giggly-wiggling-fern.md` | triple-axe + Holding→Filiales + OMK/Nexus Coach LIVE | actif (version finale) |
| **L0 Kernel OS** | Bedrock (Rick/Doctors) | *(à écrire — prochain tour)* | **runtime qui exécute L1+L2** : .claude SSOT → .hermes/.codex, Hermes Doctrines, Local-First | **terrain-prep (ce fichier)** |

**Insight clé** : L0 n'est pas un 3ème silo — c'est la **couche d'exécution** des 2 autres. Le L1 plan le dit déjà (items 12WY) :
- **Item 6** « Activation de Hermes Agent par orchestration Claude Code & Symphony » → cœur du plan L0.
- **Item 8** « Développement du Business OS par les Agents de Life OS » → L0 fait tourner L2.
- **Item 11** « Transfert Memory core local → VPS en DEAL » → le **Local-First avant VPS** du plan L0.
- **Item 3/4** « IA en autonomie + frugalité TOKEN MiniMax/Ollama » → substrat runtime L0.

## 2. Alignement L1 ↔ L2 (isomorphie déjà canon, à acter dans L0)

Le pont est **déjà posé** (giggly §4.4 + B1_Manifesto) — L0 le rend exécutable :

| L1 (A1) | axe | ↔ | L2 (B1) | axe |
|---|---|---|---|---|
| **Beth** (Ikigai/Life Wheel) | sens / breadth | ↔ | **Jerry** (8 domaines) | ancre LD (statique) |
| **Morty** (12WY/Focus) | focus / livraison | ↔ | **Summers** (3 variants AaaS) | cadence + ICP (dynamique) |

- **Holding→Filiales (L2 §5.4)** = la forme concrète de l'**item 10** L1 (« développement parallèle Solaris/OMK/ABC des B1/B2/B3 »).
- **Matrice lean Jerry/Summers (L2)** = même mécanique que les **2 triptyques imbriqués** L1 (12WY⊃PARA⊃DEAL / Ikigai⊃LifeWheel⊃Muse).
- **Loi de dispatch partagée** : gatekeeper route → manager dispatch → sub-agent execute (L1=L2, isomorphe).

→ **L0 = le moteur** qui anime cette isomorphie via les 3 harnesses (Claude Code / Hermes / Codex).

## 3. Les 3 harnesses — D1 recon (2026-06-27)

| Harness | Path | Structure réelle (D1) | Rôle cible L0 |
|---|---|---|---|
| **`.claude`** (SSOT) | `C:\Users\amado\.claude` | **174 agents** + `memory/` (wiki junction + 60+ corpus) + `mindsets/` (23 doctrines) + `hooks/` + `commands/` + `skills/` + `rules/ecc/` | **source de vérité** structure + doctrine |
| **`.hermes`** | `C:\Users\amado\.hermes` | `SOUL.md` · `config.yaml` · `kanban.db` · `skills/` · `memories/` · `cron/` · `sandboxes/` · `hooks/` · `webui-mvp/` · `gateway_state.json` | **runtime orchestrateur** (gateway + kanban + cron) — à **aligner sur .claude** |
| **`.codex`** | `C:\Users\amado\.codex` | `AGENTS.md` · `agents/` · `hooks/` · `skills/` · `memory/` · `rules/` · `config.toml` · `goals_*.sqlite` | **builder** — à **aligner sur .claude** |

**Constat (D1)** : les 3 harnesses ont DÉJÀ des structures **parallèles** (chacun a `agents/`, `skills/`, `hooks/`, `memory|memories/`, `rules|mindsets/`). Le travail L0 = **aligner ces structures sur `.claude` comme SSOT** (pas réinventer) — par junction, génération, ou contrat partagé (fork à trancher §6).

## 4. La dette technique ASpace_OS_V2 (D1 — racine polluée)

`C:\Users\amado\ASpace_OS_V2` = canon (00_Amadeus/10_Tech_OS/20_Life_OS/30_Business_OS/_SPECS) **mais racine encombrée** :
- **Bruit à trier** : `test_echo.txt`, `test_proxy.txt`, `test_write.txt`, `Sans titre 1/2.{base,canvas}`, `full_conversation_python.md`, `full_conversation_raw.md`, `ollama_err.log`, `ollama_out.log`, `2026-05-01.md`, `2026-05-09.md`, `A'Space Gravity.tar.gz`, `create_structure.bat`.
- **Graphify dupliqués** : `graphify-out`, `graphify-out-aspace`, `graphify-out-master`, `aspace-graphify-out` (4 dirs → consolider).
- **Clone hors-norme** : `_Life-OS-2026-clone/` (ADR-INFRA-002 violé — repo-home born-short attendu ailleurs).
- **`20_Life_OS_hors-para/`** + `_`, `_Inbox`, `_TRASH*` → ranger.

**Intention A0 (D3, à confirmer dans le plan L0)** : la dette se comble pour rendre le **workspace du Jumeau Numérique agnostique** — i.e., le twin n'est captif ni de `.claude` ni de `.hermes`, mais les 3 harnesses **s'alignent sur une structure partagée**. `.claude` reste le **SSOT source** ; l'agnosticité = n'importe quel harness peut piloter le runtime car ils partagent la même ossature. *(Nuance à trancher : SSOT-in-.claude vs structure-neutre-à-la-racine — voir §6.)*

## 5. Activation runtime — Jumeau Numérique dormant

A0 : « le Jumeau Numérique dormant que je dois configurer dans `.claude/agents` pour l'activation du Runtime de `.claude/memory` ».
- **`.claude/agents`** (174 présents) = où le twin se configure (A1/A2/A3 + B1/B2/B3 déjà là).
- **`.claude/memory`** = le runtime à activer (wiki junction + corpus graphify + 60+ mémoires) = la **mémoire vivante** que les agents Kernel lisent/écrivent.
- **Doctrines Hermes** = les `.claude/mindsets/` (23 fichiers : Beth/Morty/Rick/Jerry/Summers + dispatch) à **porter vers `.hermes`** pour qu'Hermes exécute la même discipline (le but « activation des Doctrines pour Hermes »).

## 6. Forks ouverts pour le plan L0 (à trancher prochain tour)

1. **Mécanisme d'alignement .claude→.hermes/.codex** : (a) **junctions** (0 dup, comme `ecc/common`), (b) **génération** (un script propage .claude → .hermes/.codex), (c) **contrat SSOT partagé** (fichiers canon lus par les 3). → détermine l'agnosticité.
2. **Agnosticité** : SSOT reste-t-il *dans* `.claude`, ou extrait-on une ossature neutre à la racine User que `.claude`/`.hermes`/`.codex` référencent ?
3. **Scope dette technique** : nettoyer la racine ASpace_OS_V2 (Deep Checkpoint Law — inventaire avant tout déplacement) — quels fichiers _TRASH vs garder.
4. **Local-First avant VPS** : quel est le critère de bascule local→VPS (item 11 L1 = Memory core DEAL 4H) ?
5. **Dépasser SDD-009** : le SDD reste-t-il canon de référence, ou L0 écrit-il un nouveau SDD-010/ADR-L0 qui le supersede en Local-First ?

## 7. Garde-fous (Rick S1 + Deep Checkpoint)
- **L0 = domaine Rick (S1 Sobriété)** : tout ajout de complexité kernel = veto anti-fragilité (différé Q4 2026 mais la doctrine s'applique au cadrage).
- **Deep Checkpoint Law** : avant tout déplacement/purge de la dette ASpace_OS_V2 → inventaire explicite présenté à A0 (jamais de `/XD` aveugle).
- **Posture C** : artefacts d'abord, zéro cron autonome sans HITL A0.
- **D1** : recon ci-dessus = lectures directes (ls + Read), pas d'assertion non vérifiée.

## 8. État F1/F2/F3 (ce tour)
- **F1 (Holding finalize)** + **F2 (Coach Filiale)** : cadrés giggly §5.4 + handoff `omk_nexus_phase_a_RETARGET_coach_first` ; **exécution gatée credential omk-services** (popup Credential Manager, pattern prouvé) — route M3/VS Code.
- **F3** : ✅ alignement L1↔L2 acté (§2) + terrain L0 prêt (ce fichier). Plan L0 = **prochain tour, Plan Mode**.

---
**TERRAIN-PREP READY 2026-06-27** — le plan L0 (prochain tour) part de ce terrain D1-vérifié. 5 forks à trancher.

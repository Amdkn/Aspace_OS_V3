---
id: ADR-L0-META-ORCH-001
title: Hermes Méta-Orchestrateur runtime aligné sur .claude (SSOT), Local-First avant VPS
date: 2026-06-27
author: A0 jumeau numérique (Opus)
status: RATIFIED
ratified: 2026-06-27 (GO A0)
layer: L0 — Tech OS / Rick's Verse
vehicle_rationale: SDD-010 veto (aucun nouveau SDD avant 2026-08-11) → ADR (type autorisé). Règle d'Or #3 = ADR supersede, on ne réécrit pas un SDD.
supersedes_partially:
  - SDD-003 (TARDIS — Rick orchestrateur) — UNIQUEMENT le rôle orchestrateur RUNTIME
  - SDD-010 §7.3 anti-pattern « OpenHarness ≠ orchestrateur global » — levé POUR LE RUNTIME SEULEMENT
preserves:
  - SDD-002/003/010 — veto souveraineté Rick + Donna DLQ (intacts)
  - SDD-010 §4-6 — souveraineté graduée / Local-First / veto no-new-SDD
sister:
  - plans/bedrock-humming-tardis.md (plan L0)
  - wiki/hand_offs/l0_terrain_prep_kernel_os_2026-06-27.md
  - ADR-RICK-001 (OpenHarness incarnation Rick)
---

# ADR-L0-META-ORCH-001 — Hermes Méta-Orchestrateur runtime

## Contexte

Le canon SDD (RATIFIÉ 2026-05-13) pose **Rick (A1) / OpenHarness** comme orchestrateur (SDD-003 TARDIS) et **interdit** explicitement qu'un harness devienne un méta-orchestrateur global (SDD-010 §7.3 anti-pattern). Or A0 veut faire de **Hermes le méta-orchestrateur** des 3 harnesses (Claude Code, Codex, Hermes), aligné sur **`.claude` comme SSOT**, **Local-First avant retour VPS**, pour que les Agents du Kernel OS développent + appliquent les plans L1 (Life OS) + L2 (Business OS).

Deux contraintes canon dures (D1, vérifiées 2026-06-27) :
1. **SDD-010 veto** : aucun nouveau SDD avant **2026-08-11** → cette décision passe par un **ADR**, pas un SDD.
2. **SDD-010 §4-5** : souveraineté **graduée** + **Local-First** = déjà canon → on l'**honore**.

## Décision

1. **Hermes devient le méta-orchestrateur RUNTIME** (Perso→L1 / Pro→L2), supervisant **Claude Code CLI/SDK** (architecte/review) + **Codex CLI** (builder).
2. **Rick (S1) conserve le VETO de souveraineté** + Donna DLQ. On dépasse **uniquement le rôle orchestrateur-runtime** de Rick (SDD-003), **pas** sa souveraineté. L'anti-pattern SDD-010 §7.3 est levé **pour le runtime seulement**.
3. **`.claude` = SSOT**. `.hermes` et `.codex` s'alignent par **junctions zero-drift** (agents/skills/hooks/mindsets/memory) — trajectoire = abandon progressif du Claude Code manuel au profit de l'orchestration Hermes.
4. **Local-First avant VPS** : tout tourne en local (Hermes desktop + MiniMax/Ollama) avant retour VPS, gaté sur les critères MUSE SDD-010 (≥5/7) + Rick S1 GO.
5. **TARDIS Inversé** (déjà acté SDD-010 §5 : tâche→A3→A2→A1→A0) devient le flux runtime **piloté par Hermes**.

## Conséquences

**Positives** : sépare les runtimes par rôle (builder ≠ reviewer = revue adversariale par conception) ; SSOT unique zero-drift ; économie par abonnements (volumes à l'API = $35-70k/mois) ; A0 déchargé de l'orchestration manuelle.

**Risques / garde-fous** : Hermes dormant/crash-prone → hardening prérequis (P1) ; Rick anti-fragilité check à chaque phase ; Posture C (zéro cron autonome sans HITL A0) ; Deep Checkpoint Law pour la dette technique racine.

## Alternatives écartées

- **SDD-010b (13ème Semaine d'Exception)** : possible mais plus lourd ; A0 a choisi l'ADR (respect veto, réversible).
- **Hermes remplace Rick entièrement** : casse le lock canon souveraineté → écarté (Rick garde le veto).
- **Contrat neutre à la racine** (au lieu de junctions) : agnosticité max mais `.claude` cesse d'être SSOT direct → écarté au démarrage (junctions d'abord, zero-drift).

## Statut

**RATIFIED 2026-06-27 (GO A0).** Exécution gatée Posture C (P1→P6 du plan `bedrock-humming-tardis.md`, HITL par phase). P1 (junctions SSOT) lancé 2026-06-27.

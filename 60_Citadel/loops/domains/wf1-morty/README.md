---
type: loop-contract
loop: wf1-morty
flag: enable_wf1.flag
trigger: Pass `decisions/pass_wf1_WKnn.json` valide (wk courante + invariants GREEN)
rails: fable-last-week-aspace/wargames/02-wf1-morty.md
---
# Contrat WF1 — Morty (poupée russe 12WY ⊃ PARA ⊃ DEAL)

**Goal** : exécuter la traction du cycle — Curie (rocks WK01-12) · Computer (PARA continu) · Janeway (DEAL WK13) — en N instances parallèles si plusieurs workflows actifs.
**Workflow** : valider le Pass (wk == WK courante = `floor((today-2026-06-15)/7)+1`, invariants GREEN) → piocher la queue `artifacts/tasks/` (WIP ≤ 20) → exécuter avec preuve → soupapes wargame 02 M3 : (a) saturation → fréquence/2 ; (b) contexte >80% → compaction+persist d'abord ; (c) queue >20 → drain. Priorité (b)>(a)>(c).
**Boundaries** : Pass périmé/absent → refus + signal `pass-expired` · tout write finit par un verification run réel (sinon retour queue `unverified`) · item mort 2 WK → `_dlq/` · WK13 : le Pass cycle+1 EXIGE l'artefact DEAL. Skill réutilisé : `/multi-loop-karpathy` (cycles > 7j).
**Backlog** : [ ] table WK affichée au premier tick · [ ] premier drain de queue.
**Timeline** : - [2026-07-06] contrat posé.

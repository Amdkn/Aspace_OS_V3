---
id: YT-UNKNOWN-loop-engineer-jason
title: "wtf is Loop Engineer & how to setup for real"
channel: "AI Jason"
duration: "UNKNOWN"
date: "2026-07-02"
category: "IT / Loop Engineering"
status: DISTILLED_L1_PREMIUM
sister: 09_Life_OS/LD07_Creativity_Reno/2026-07-02_wtf-is-loop-engineer_ai-jason__GUIDE.md
source_note: transcript fourni par A0 in-chat 2026-07-02 — video_id non fourni, non inventé (D1)
ld: LD07_Creativity_Reno
b2_owner: cyborg-it
sister_b1: jerry-prime
---

# 📖 wtf is Loop Engineer & how to setup for real

> [!NOTE]
> Fiche de clarification d'excellence sémantique pour le Domaine IT — Loop Engineering / Architecture de composition. La vidéo la plus opérationnelle du batch : elle définit le loop engineering comme la **zone externe** au runtime de l'agent et livre le file-system exact qui fait composer les loops entre eux.

---

## 🧠 Concepts Clés à Haute Densité Sémantique

- **Les deux zones d'optimisation (la clarification du mot « harness »)** : le terme harness (Viv/LangChain : « anything that is non-model ») confond deux plans distincts. La **zone interne** — l'agent loop lui-même (CC, Codex) : comment un agent finit bien UNE tâche donnée (prompt, gestion de contexte, compaction, skills). La **zone externe** — comment le SYSTÈME décide ce qui doit être travaillé : triggers, état cross-sessions, logs, environnement. Le loop engineering, c'est la zone externe. C'est elle qui libère du prompting : l'agent devient réveillable par cron, webhook, incident serveur, ou un autre agent.

- **Artifacts (la couche de savoir partagée)** : les outputs typés de chaque run de loop — docs, signals, tasks, tickets, campaigns. Chaque type = un dossier avec un README définissant ce qui y entre, ce qui n'y entre pas, le process d'ajout et le schéma. Chaque item = frontmatter + corps + **timeline** (log des changements de cet artifact). Le principe : les artifacts sont la bibliothèque partagée que n'importe quel loop peut lire et écrire — c'est le substrat matériel de la composition.

- **Signals (le mécanisme du compounding)** : le type d'artifact le plus stratégique — toute observation utile d'un loop (friction, idée produit, opportunité manquée, récurrence). Exemple réel : le support loop voit 3 utilisateurs demander l'export de fichiers → crée `signals/export-file.md`, y logge chaque occurrence horodatée. Le growth loop, en priorisant ses expériences, lit TOUS les signals des autres départements et priorise le bug rapporté 3× ou l'opportunité que le SEO optimise déjà. Le ads loop trouve un keyword à fort CTR sans contenu organique → signal → le SEO loop produit. **Des loops à cadences différentes, même cerveau : le compounding.**

- **Loop Contract (le README par loop)** : chaque loop possède son dossier avec un contrat en 4 blocs — **goal** (la mission), **workflow** (les étapes et frontières), **backlog** (la liste priorisable que le prochain réveil peut reprendre ou re-prioriser), **timeline** (ce qui s'est passé). À chaque réveil, le loop lit son contrat, comprend le but et l'historique, puis agit. Méthode de création : test run manuel AVEC l'agent d'abord, calibrage, puis « crée le contrat », et seulement alors la planification cron.

- **Codebase legible · executable · verifiable** : les trois conditions pour que des agents parallèles travaillent en autonomie. **Legible** : AGENTS.md racine ~100 lignes pointant vers la doc (progressive discovery) + règles injectées en **lint programmatique** — l'erreur surface automatiquement quand l'agent enfreint une règle (ex. import interdit d'un dossier legacy), au lieu d'espérer qu'il trouve la règle. **Executable** : dev server en un script, coût cognitif nul, **worktree-friendly** (5 agents parallèles sans conflit), scripts pour sauter à un état de test précis. **Verifiable** : Playwright CLI avec clip vidéo attaché au PR, e2e sur les flux critiques (signup, upgrade), PR-queue (checklist obligatoire avant submit).

- **Verifier read-only (jamais d'auto-vérification)** : « don't get agent to self-verify its own work — it just generally doesn't work that well ». La PR-queue impose de spawner un agent vérificateur séparé, en lecture seule, avec un brief détaillé. Le producteur produit, le vérificateur juge — la séparation des pouvoirs portée au niveau agent. C'est la même loi que le maker-checker de Herk, ici ancrée dans le workflow PR.

---

## 🛠️ Outillage Stratégique & Matrice d'Alignement

| Outil / Technologie / Approche | Rôle Stratégique | Alignement Souverain A'Space |
| :--- | :--- | :--- |
| **Triggers multi-sources (cron/webhook/agent)** | Réveiller les loops au bon moment sans humain | Nos ScheduleWakeup/CronCreate + hooks — MAIS chaque cron reste gated A0 (Posture C) |
| **Dossier `signals/` partagé** | Le bus de composition inter-loops | Candidat type OKF `Signal` (ADR-LOOP-003 décision 2) — s'insère dans le wiki bundle |
| **Git worktrees + scripts d'état** | Parallélisme sans conflit + accès direct aux scénarios de test | Notre EnterWorktree + isolation:worktree des sub-agents — déjà câblé |
| **Playwright CLI + vidéo attachée au PR** | Preuve visuelle du travail jointe au livrable | Renforce ADR-LOOP-002 loi 4 (review enrichie : la preuve voyage avec le livrable) |
| **Custom lint programmatique** | Contexte injecté par l'outillage, pas par la mémoire de l'agent | Nos hooks PostToolUse log-only + lint-wiki v2 (P2 Méta-Mémoire) |

---

## 🪐 Perspective Souveraine A'Space IT

Cette vidéo fournit le chaînon que notre écosystème de loops n'avait pas encore formalisé : le **file-system de composition**. Nous avons déjà les triggers (cron gated, hooks), les contrats implicites (loop-plans), les logs (wiki/log.md curé + turn-journal brut) — mais pas de dossier **signals typé** que tous les loops lisent et écrivent. C'est exactement ce que ADR-LOOP-003 décision 2 vient d'acter : `type: Signal` comme artifact OKF, à spécifier à la première implémentation de loop de production. La subtilité que Jason apporte et qu'il ne faut pas perdre : le compounding ne vient pas des loops eux-mêmes mais du **partage du même cerveau** — des loops support/SEO/growth/ads à cadences différentes qui convergent parce qu'ils écrivent au même endroit. Chez nous, ce cerveau partagé est la Méta-Mémoire (OKF × Wiki × Graphify × DOX) : les signals en seront un sous-dossier vivant, avec la cadence de rot la plus rapide du ROT.md. L'action concrète à 30 jours (H3) : au premier loop de production L2 sous Hermes (plan L2 §13.3 — le support client-facing d'OMK Nexus est le candidat évident, miroir exact de l'exemple de la vidéo), implémenter le triplet contrat + signals + verifier read-only, et mesurer si le growth loop y lit quelque chose d'exploitable. Les A3 twins concernés : **Mariner** (capture des signals), **Boimler** (triage/routage), **Data** (schéma des artifacts, archivage), **Rutherford** (la revue hebdo qui détecte le drift des contrats). ADRs impactés : ADR-LOOP-003 (ce guide en est la source pour signals/artifacts), ADR-LOOP-001 (verifier read-only = loi 3), DOX P4 (la codebase legible EST l'arbre DOX). Doctrine confirmée : D8 cross-agent (les loops de Jason sont harness-agnostiques) ; doctrine étendue : le test-run-manuel-avant-cron comme rituel de calibrage obligatoire.

---

## 🕹️ Protocole d'Exécution D.E.A.L

| Phase | Action Concrète | Objectif A'Space OS |
| :--- | :--- | :--- |
| **Définir** | Spécifier le schéma OKF du type `Signal` + le README du dossier signals | Le bus de composition inter-loops existe et est auto-décrit |
| **Éliminer** | Supprimer les logs de loops éparpillés sans schéma (fusion dans artifacts typés) | Un seul cerveau partagé, zéro observation perdue dans un log mort |
| **Automatiser** | 1er loop de production : support OMK Nexus sous Hermes-L2 (contrat + signals + verifier) | Le pattern complet prouvé sur un cas client réel |
| **Libérer** | Les loops growth/SEO lisent les signals du support — priorisation sans réunion | Le compounding tourne sans bande passante A0 |

---

## 🔬 Annexes Détaillées de l'Audit Sémantique & Technique

### Note A3-01 : Le run réel — 20-40 pages SEO/jour et des PRs à 1h du matin
Jason ouvre sur ses résultats : un goal-loop SEO qui tourne depuis 2 jours et publie 20-40 pages de qualité par jour sans supervision, et des PRs qui s'accumulent la nuit — non parce que l'équipe travaille, mais parce que les loops trouvent et piochent le travail. Le détail qui compte : chaque loop est né d'un test run manuel calibré, puis d'un contrat écrit, puis seulement d'un cron. La séquence inverse (cron d'abord) est l'anti-pattern qui produit des loops qui scalent des problèmes. Chez nous, cette séquence est renforcée par un gate supplémentaire : le HITL A0 par cron (Posture C) entre le contrat et l'activation.

### Note A3-02 : L'évolution support-loop v1 → v2 — de l'observation à l'action
La v1 du support loop lit les tickets, répond, et logge frictions/idées en signals : déjà précieux. La v2 spawne directement un coding agent sur les fixes évidents, surveille la performance post-fix, et informe le client que le correctif est en place. La différence de valeur est massive, mais la v2 exige les garde-fous d'ADR-LOOP-002 : sandbox obligatoire pour l'agent de fix, checkpoint humain sur le merge tant que la confiance n'est pas échantillonnée, et Donna DLQ pour les fixes qui échouent 2×. La trajectoire v1→v2 est notre roadmap : observer d'abord, agir ensuite, jamais l'inverse.

### Note A3-03 : Le work-log global — lire avant d'écrire
Troisième abstraction souvent négligée : un log global où chaque agent écrit après un bloc de travail significatif ET **lit les 5-10 dernières entrées avant de commencer**. La raison : la journée réelle mélange reviews d'outputs de loops et travail co-pilote ad hoc — sans log transversal, chaque session repart aveugle. C'est la validation exacte de notre architecture à deux étages : turn-journal.md (brut, automatique, par tour) + wiki/log.md (curé, délibéré) — avec le SessionStart hook qui fait précisément le « lire les dernières entrées avant de travailler ». Rien à construire, juste à maintenir.

---

*Fiche de connaissances souveraine d'IT générée sous A'Space OS V2 — Standard Antigravity Premium.*

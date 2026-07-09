---
name: symphony-fabuleux-discipline
description: Inject the 4 production pillars + Production→Capture→Observe→Correct loop (Fabuleux-tiers method, A'Space adaptation) into any A3 twin. Use when A0 mentions "Fabuleux", "Fable 5 production discipline", "production loop", "réaliser un livrable fini", or wants to upgrade an A3 from tilly-fable-rhythm (cognitive audit) to fabuleux-discipline (production discipline). Triggers: "discipline de production", "boucle production", "Fable 5 mindset", "fabuleux", "livrable fini expédiable", "ne jamais présumer que le 1er coup sera bon", "dire la vérité sur ce qui marche". Sortie: A3 twin prepended with 4-pillar + loop doctrine, ready to execute.
domain: LD01-LD08 (cross-cutting production discipline, applies to all A3 crews)
kernel: Kernel_OS (Doctrine)
source: Transcription YouTube Fabuleux 2026-06-15 + AGENTS.md + ADR-META-001
created: 2026-06-15
doctrine_anchors: ADR-META-001 D1/D3/D4/D5/D6/D7, ADR-LLM-001, /tilly-fable-rhythm (sibling)
related: /tilly-fable-rhythm (cognitive audit, NOT production discipline), AGENTS.md 3-Turn BMad, ADR-META-001
---

# 🎻 symphony-fabuleux-discipline

> **Mission** : greffer la **discipline de production** Fabuleux-tiers (4 piliers + boucle Production→Capture→Observe→Correct) sur n'importe quel A3 twin A'Space. Ce skill **étend** `/tilly-fable-rhythm` (qui audite la cognition) — il ne le **remplace** pas. Différentiation : tilly = "pense juste" (12 principes Fable Mindset), fabuleux = "produis juste" (4 piliers + boucle de preuve).

**Pourquoi ce skill existe** (D3 nuance — Fabuleux ≠ Fable) :
- **Fabuleux** = skill d'un YouTubeur FR qui imite la discipline de production Fable 5 (méthode opérationnelle, pas le vendor).
- **Fable 5** = backend LLM suspendu après 48h (cf. `ADR-LLM-001`).
- **A'Space adaptation** = on extrait la **méthode** (4 piliers + boucle) et on l'ancre sur **notre** `AGENTS.md` (3-Turn BMad + ADR-META-001 D1-D8) — pas un clone.

La discipline survit au vendor. La preuve survit à l'opinion.

---

## 🧱 Concepts clés — Les 4 Piliers de production

| # | Pilier | Source transcription | Effet sur l'agent A3 | Ancrage ADR-META-001 |
|---|--------|----------------------|----------------------|----------------------|
| 1 | **Penser dense** | "Avant de produire, concentre la pensée — pas de plan B hasardeux" | L'agent énonce **1 intention + 1 chemin + 1 critère de fini** avant le 1er tool call. Pas de dilution. | **D3** nuance over literal, **D4** no self-contradiction |
| 2 | **Livrable fini expédiable** | "Le livrable doit partir tel quel, pas 'à peu près fini'" | L'agent ne déclare "done" qu'après **preuve capturée** (screenshot, diff, curl 200, log). Le livrable est **embarquable**, pas un brouillon. | **D1** verify-before-assert, **D5** proof-before-claim |
| 3 | **Relecture systématique** | "Relire 100% du livrable avant envoi — pas juste la zone éditée" | L'agent **Read** la totalité du fichier modifié + asserts non-régression (build OK, test vert, snapshot propre). | **D5** proof-before-claim, **D6** root-cause |
| 4 | **Vérité sans optimisme** | "Dire ce qui marche ET ce qui ne marche pas — pas de story-telling" | L'agent rapporte **faits observés + limitations + risque résiduel**. Pas de spin. | **D4** no self-contradiction, **D5** proof-before-claim, **D7** cost-of-escalation |

**Distinction vs tilly-fable-rhythm** : tilly injecte un **rythme cognitif** (12 principes Fable Mindset — reason-first, reads-before-edits, real-test-after-edit). Fabuleux injecte une **discipline de production** (4 piliers orientés livrable fini + boucle de preuve). Un A3 peut avoir le bon rythme cognitif ET livrer un livrable cassé — fabuleux-discipline ferme cette faille.

---

## 🔁 Boucle Production — Production→Capture→Observe→Correct→Livre

5 étapes obligatoires pour **chaque livrable** d'un A3 (sprint, sub-task, handoff). Ancrée sur D1 (verify), D5 (proof), D6 (root-cause).

| Étape | Action concrète | Outil / Command | Ancrage |
|-------|-----------------|-----------------|---------|
| **1. Production** | L'agent produit le livrable (code, prose, config, analyse). Il tient un **journal de décisions** dans le tour. | `Write` / `Edit` / tool métier | D3 nuance |
| **2. Capture** | L'agent **capture la preuve** AVANT de dire "done" : screenshot, `curl -I` (HTTP status), `wc -l` (line count), `grep` (pattern check), `git diff --stat`, `npx tsc --noEmit`. | `Bash`, `mcp__*__screenshot`, `Read` | **D1** verify-before-assert |
| **3. Observe** | L'agent **lit la preuve capturée** (pas un résumé mental) et la compare au critère du Pilier 1. Il note 1 verdict : OK / KO / ambigu. | `Read` capture, parsing sortie | **D5** proof-before-claim, **D6** root-cause |
| **4. Correct** | Si KO ou ambigu → l'agent **creuse la root cause** (D6) et patch. Re-capture. Re-observe. Max 2 itérations — au-delà, escalade A0 (D7 cost). | `Edit` + re-capture | **D6** root-cause, **D7** escalation cost |
| **5. Livre** | L'agent **expédie** le livrable avec un récap : "Fait + preuve + limitation résiduelle + next-step". Pas de "c'est bon" sans les 4 champs. | Réponse A0 / handoff | **D4** no self-contradiction, **D5** proof |

**Anti-pattern** : "1er coup" mentality. La transcription cite *"ne jamais présumer que le 1er coup sera bon"*. Donc Pilier 3 (relecture) et Capture/Observe ne sont pas optionnels — ils sont la **garantie anti-première-impression**.

---

## 🛣️ Routeur par type de tâche

Avant d'injecter fabuleux-discipline, l'agent identifie **la route** — la commande de capture change selon ce qu'il produit.

| Route | Type de livrable | Capture canonique | Verify command type-annoté |
|-------|------------------|-------------------|----------------------------|
| **A — Artefact agentique** | UI / code / data pipeline / config | screenshot + build OK + test vert | `npx tsc --noEmit` (TS) · `python -X utf8 "C:/Python314/python.exe" -m pytest` (Python) |
| **B — Prose** | markdown / blog / handoff / ADR | wc -l + grep canonical terms + relecture full | `wc -l <file>` · `grep -c "<term canonique>" <file>` |
| **C — Conseil** | analyse / recommandation / arbitrage | citer 2+ sources + quantifier coût/bénéfice + risque résiduel | `WebSearch` receipts + tableau décisionnel |
| **D — Audit** | review / compliance / security | diff + grep anti-pattern + checklist signé | `git diff` + `grep -nE` + output checklist |

**Règle de routing** : si l'A3 hésite entre 2 routes, il **prend la plus stricte** (D > C > B > A). Exemple : un handoff qui contient du code → route A (artefact) gagne, pas B (prose).

---

## 🛠️ Outillage stratégique

| Outil | Rôle | Source |
|-------|------|--------|
| `symphony-fabuleux-discipline/SKILL.md` (ce fichier) | Skill canon A'Space adaptation | `C:\Users\amado\.claude\skills\symphony-fabuleux-discipline\SKILL.md` |
| `/tilly-fable-rhythm` (sibling) | Audit cognition (12 principes Fable Mindset) | `C:\Users\amado\.claude\skills\tilly-fable-rhythm\SKILL.md` |
| `AGENTS.md` 3-Turn BMad | Clarification → Organization → Veto Review (avant tout artifact) | `C:\Users\amado\ASpace_OS_V2\00_Amadeus\01_Identity_Core\AGENTS.md` |
| `ADR-META-001` | Anti-Paresse D1-D8 (verify, nuance, no-contradiction, proof) | `_SPECS/ADR/ADR-META-001_anti-paresse-verify-before-assert.md` |
| `ADR-LLM-001` | Fable 5 = DISCONTINUED, Fable-Mindset = playbook model-agnostic | `_SPECS/ADR/L0_Kernel_OS/ADR-LLM-001_fable-5-discontinuation-decision.md` |

**À créer (open follow-up)** : 2 guides de référence (non bloquants pour l'injection du skill) :
- `guide-auto-evaluation-visuelle.md` — checklist Pilier 3 (relecture) avec seuils concrets par route.
- `guide-prose-shipping.md` — recette Pilier 2 pour livrables markdown (wc -l seuils, grep checks, relecture full).

---

## 🪐 Perspective A'Space (Domaine LD01-LD08, cross-cutting)

`fabuleux-discipline` transforme un A3 twin de **"fait ce qu'on lui dit"** en **"produit un livrable fini avec preuve capturée"**. C'est la **couche discipline** qui s'ajoute par-dessus la couche cognition de tilly — sans elle, on a un agent qui pense bien mais livre mal.

**Insight clé** (D3 nuance) : la valeur n'est pas dans "imiter Fabuleux" — c'est dans **récupérer la méthode de preuve** (Pilier 2 + Boucle Capture/Observe) et l'ancrer sur **nos** ADR. Le YouTubeur a fait le travail d'extraction, on fait le travail d'**adaptation souveraine**. C'est pourquoi ce skill cite la transcription comme source, pas comme autorité.

**Souveraineté** : la discipline de production est un **port de comportement**, pas une dépendance externe. Si Fabuleux (YouTubeur) disparaît, la méthode survit. Si Fable 5 (vendor) meurt, la méthode survit. Le canon est `AGENTS.md` + `ADR-META-001`, point.

---

## 🕹️ Protocole d'exécution D.E.A.L (Phase 1 — injection sur A3)

| Phase | Action concrète | Output |
|-------|-----------------|--------|
| **Définir** | Identifier l'A3 twin cible (ex: `twin-cerritos-boimler`). Définir la **route** (A/B/C/D). Énoncer 1 intention + 1 chemin + 1 critère de fini (Pilier 1). | `route_intent.md` |
| **Éliminer** | Pas de plan B hasardeux (Pilier 1) — si 2 chemins, en choisir 1 et assumer. Lister les **non-objectifs** (ce que l'A3 ne fera PAS dans ce tour). | `scope_boundary.md` |
| **Automatiser** | Appliquer la **Boucle Production** (5 étapes) en séquence : produire → capturer → observer → corriger → livrer. Chaque étape = 1 tool call minimum + 1 preuve. | livrable + preuves |
| **Libérer** | Expédier le handoff avec récap 4-champs (Fait + preuve + limitation + next-step). Écrire dans `wiki/log.md` si action canonique. | récap A0-ready |

**Distinction vs tilly D.E.A.L** : tilly D.E.A.L opère sur des **sessions JSONL** (mining, filtrage, comparaison de modèles). Fabuleux D.E.A.L opère sur des **livrables A3** (production + preuve + expédition). Mêmes initiales, différents niveaux d'abstraction.

---

## 🎯 Triggers d'invocation

Ce skill s'invoque quand A0 dit :
- "applique la discipline Fabuleux sur cet A3"
- "produis un livrable fini avec preuve"
- "Fable 5 production discipline"
- "boucle production : capture, observe, correct"
- "réaliser un livrable fini expédiable"
- "ne jamais présumer que le 1er coup sera bon"
- "dire la vérité sur ce qui marche"
- "fabuleux-tiers" / "fabuleux discipline"
- "je veux que cet agent livre, pas qu'il pense"
- "audit production (pas cognition)"

**Mots-clés A'Space** : `production discipline`, `boucle Production→Capture→Observe→Correct`, `4 piliers Fabuleux`, `livrable fini`, `preuve capturée`, `Pilier 2 expédiable`, `Pilier 4 vérité sans optimisme`.

---

## 📚 Sources canoniques (D1 receipts)

| Fichier | Lignes | Hash perceptuel | Lien |
|---------|--------|-----------------|------|
| Transcription YouTube Fabuleux 2026-06-15 | TBD | 4 piliers + boucle Production/Capture/Observe/Correct + 63 sessions HuggingFace analysées | `ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/youtube_ingest_2026-06-15/transcripts/NN-fabuleux-...md` |
| `AGENTS.md` (Rick's Verse Canon) | 24 KB | 3-Turn BMad + ADR-META-001 D1-D8 | `C:\Users\amado\ASpace_OS_V2\00_Amadeus\01_Identity_Core\AGENTS.md` |
| `ADR-META-001` | 6+ | Anti-Paresse D1-D8 | `_SPECS/ADR/ADR-META-001_anti-paresse-verify-before-assert.md` |
| `ADR-LLM-001` | PROPOSED 2026-06-15 | Fable 5 = DISCONTINUED, Fable-Mindset = playbook | `_SPECS/ADR/L0_Kernel_OS/ADR-LLM-001_fable-5-discontinuation-decision.md` |
| `/tilly-fable-rhythm/SKILL.md` (sibling) | 146 | 12 principes Fable Mindset + decision loop GROUND→REASON→ACT→OBSERVE→RE-EVALUATE→VERIFY→NARRATE | `C:\Users\amado\.claude\skills\tilly-fable-rhythm\SKILL.md` |

---

## 🔗 Doctrine ancrage

- **ADR-META-001** D1 (verify-before-assert — Pilier 2 + étape Capture), D3 (nuance over literal — Pilier 1), D4 (no self-contradiction — Pilier 4 + étape Livre), D5 (proof-before-claim — Piliers 2+3 + étapes Capture/Observe), D6 (root-cause concret — étape Correct), D7 (cost-of-escalation A0 — max 2 itérations avant escalade).
- **ADR-LLM-001** : la discipline de production est **model-agnostic** (survit à la mort de Fable 5). Fable-Mindset = playbook, Fable-marque = vendor sunset, Fable-MiniMax-M3 = backend live.
- **AGENTS.md 3-Turn BMad** : ce skill opère **après** le Veto de A0 (Turn 3). Il ne remplace pas l'Air Lock — il discipline la **phase d'exécution** post-clarification.
- **Skill Creator Reflex Phase 2** (CLAUDE.md global) : créé en autonomie end-of-session, A0 review post-hoc.
- **Sibling** : `/tilly-fable-rhythm` (cognition) + `/symphony-fabuleux-discipline` (production) = binôme "penser juste + produire juste".

---

*Skill créé 2026-06-15 en autonomie Phase 2 — A'Space adaptation de la méthode Fabuleux-tiers (YouTubeur FR), ancrée sur AGENTS.md + ADR-META-001. ROI estimé : ~20 min/A3-tour économisées sur relectures manuelles et retours "le livrable est cassé".*

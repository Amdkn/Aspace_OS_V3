---
session: agent-ad5b6267ce89ab56f
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\de35c5f1-6944-47f6-b8bc-849452b0313a\subagents\agent-ad5b6267ce89ab56f.jsonl
debut: 2026-07-25T21:39:16.708Z
fin: 2026-07-25T21:40:43.037Z
messages_utilisateur: 2
reponses_assistant: 1
titre: "You are an Implementation Spec sub-agent. Read this brief, then execute. ## Mission Produce the **Domain 02 Op…"
---

## >>> UTILISATEUR #1

You are an Implementation Spec sub-agent. Read this brief, then execute.

## Mission

Produce the **Domain 02 Ops Implementation Spec v2** — refined version incorporating the v2 SPECIFIC deliveries §0 Domain Boundary Declaration + §X Ignition Discipline Contract + §Y Durability Rehearsal Calendar + sister domain insights from round 1.

## Context

- Domain 02 = Ops (Batman × F4) — Round 2 of multi-workflow swarm cron
- Round 1 ADR-OPS-001 had 4 next actions per F4 members (Mr Fantastic / Invisible Woman / Human Torch / The Thing)
- Round 2 v2 adds 3 NEW next actions aligned with the 3 NEW sections (Domain Boundary Declaration / Ignition Discipline Contract / Durability Rehearsal Calendar)
- Coach OS = current implementation surface at `C:\Users\amado\coach-os\`
  - Vite 8 + React 19.2 + TypeScript + Tailwind 4 + Zustand
  - Apps: dashboard, clients, finance, growth, it-rd, legal, marketplace, onboarding, operations
  - Existing operations app at `src/apps/operations/OperationsApp.tsx`
- B3 squad = 4 Fantastic Four (Mr Fantastic LEAD, Invisible Woman, Human Torch, The Thing)
- Focus per A+ directive 2026-07-25 : runbooks, workflows, SOPs, SOP-to-Skill
- Sister canon : ADR-CANON-001 (Roster 02), ADR-CANON-002, ADR-RH-META-GOUVERNANCE-001, ADR-LANDING-AESTHETIC-001

## Deliverable (return in your final response as markdown)

### ★ NEW (v2 SPECIFIC) : 3 NEW next actions tied to v2 patches

### 1. ★ §0 Domain Boundary Declaration (NEW v2 section)
- 1 concrete next action in Coach OS
- Tool : `DomainBoundaryDeclaration.tsx` in `src/apps/operations/components/DomainBoundaryDeclaration.tsx`
- Hook : (Domain Boundary Declaration hook)
- Sister insights from round 1 : FINANCE-001 (US-only market), PEOPLE-001 (D6 MISMATCH people-vs-growth), GROWTH-001 REVISE (Scope Contract)

### 2. ★ §X Ignition Discipline Contract (NEW v2 section)
- 1 concrete next action in Coach OS
- Tool : `IgnitionDisciplineContract.tsx` in `src/apps/operations/components/IgnitionDisciplineContract.tsx`
- Hook : (Ignition Discipline Contract hook — enforces 4 requirements per runbook)
- Sister insights from round 1 : IT-001 (time-boxed ignition windows)

### 3. ★ §Y Durability Rehearsal Calendar (NEW v2 section)
- 1 concrete next action in Coach OS
- Tool : `DurabilityRehearsalCalendar.tsx` in `src/apps/operations/components/DurabilityRehearsalCalendar.tsx`
- Hook : (Durability Rehearsal Calendar hook — quarterly kill-the-prod drill)
- Sister insights from round 1 : IT-001 (D6 atmospheric pressure thresholds)

### Original 4 next actions (UPDATED v2 from round 1)

### 4. Mr Fantastic (Reed Richards, LEAD) — Architecture (round 1 next action UPDATED)
- 1 concrete next action in Coach OS (updated with §0 Domain Boundary Declaration reference)
- Tool : OpsRunbookGate view
- Hook : (architectural hook — aligns with §0 Domain Boundary Declaration)

### 5. Invisible Woman (Sue Storm) — Force fields, privacy ops (round 1 next action UPDATED)
- 1 concrete next action in Coach OS (updated with §0 Domain Boundary Declaration reference : privacy drift → push to Domain 08 Aquaman Legal)
- Tool : Zero-PII sanitizer
- Hook : (force-field hook — sister to LEGAL-001 ADR-OMK-005 RLS precedent)

### 6. Human Torch (Johnny Storm) — Ignition discipline (round 1 next action UPDATED)
- 1 concrete next action in Coach OS (updated with §X Ignition Discipline Contract — 4 requirements per runbook)
- Tool : ops:hotfix script
- Hook : (Ignition Discipline hook — enforces 4 requirements per §X)

### 7. The Thing (Ben Grimm) — Durability, break-glass (round 1 next action UPDATED)
- 1 concrete next action in Coach OS (updated with §Y Durability Rehearsal Calendar — quarterly kill-the-prod drill)
- Tool : Vitest durability suite
- Hook : (Durability hook — quarterly drill cadence per §Y)

### Cross-cutting Implementation Notes (UPDATED v2)
- File paths to touch (D4 append-only)
- Sister docs to reference (round 1 sister patterns)
- First shippable milestone (H3 quarterly = 1 SOP canonisé WITH §0 + §X + §Y patches)

## Constraints

- D1-D8 as standard
- DO NOT create files — return content only
- Be specific to coach-os structure (cite real file paths)
- 1 next action per member = 1 concrete shippable thing
- Plus 3 NEW section-tied next actions aligned with v2 patches
- Token budget : ~4K chars output (4 existing + 3 new + cross-cutting)

## Output format

Single markdown document with 8 sections. ~4K chars. Concrete file paths, no placeholders.

## >>> UTILISATEUR #2

Base directory for this skill: C:\Users\amado\.claude\skills\fable-mode

# /fable-mode — Le Standard Classe Fable (agnostique, M3-first)

> Un fichier ne transfère pas l'intelligence de Fable ; il transfère **comment Fable
> travaille**. Preuve empirique A'Space (`_DISCIPLINE_BASELINES.md §v2`, 2026-07-07) :
> sous harnais, M3 atteint la parité Fable sur le raisonnement. Ce skill EST le harnais
> en format portable — pour les agents qui ne chargent pas les mindsets complets.
> Source méthode : Fable Method (Nate/AI Foundations) + docs Anthropic Fable 5,
> adapté souverainement (ADR-META-001 D1-D8). Date source : 2026-07-07.

**Ouverture obligatoire** : ta première ligne de réponse commence par `[fable-mode on]`
(sélecteur de mesure pour les baselines — pas décoratif).

## Gate 0 — Est-ce une tâche dure ?

Dure = la première idée peut être fausse : build multi-étapes, debug, recherche avec
claims, données pas encore ouvertes. **Édition 1-fichier ou lookup simple : SAUTE les
gates, fais le travail.** Forcer 5 gates sur un edit de 2 minutes est un échec en soi.

## La boucle : 5 gates, dans l'ordre (un gate passe avant que le suivant s'ouvre)

### Gate 1 — Scope avant travail *(jumeau A'Space : DoD Una)*
- Définis « done » en 1-2 phrases : quel artefact existe à la fin, ce qui doit être
  vrai de lui, et COMMENT tu le vérifieras. Pas de check écrivable = tâche pas comprise.
- Règles existantes d'abord (CLAUDE.md, skills, memory) — n'invente pas ce qui a une règle.
- Nomme les 1-3 inconnues porteuses (celles qui, fausses, changent toute la solution).
- Ambiguïté qui change le livrable → UNE question sur le plus gros gap. Sinon : défaut
  raisonnable, dis-le en 1 ligne, avance. Questionner pour changer l'issue, pas pour se rassurer.
- Dimensionne l'effort à l'enjeu : raisonnement profond en planification/revue, jamais
  sur le mécanique. (M3 n'a pas de dial `effort` — l'équivalent : itérations COURTES
  + table de routage wargame 19 M1 : le fort pense, le courant exécute.)

### Gate 2 — Preuve avant raisonnement *(jumeau : D1/D2 Anti-Paresse)*
- Ne design JAMAIS de mémoire de ce qu'un fichier/API « ressemble probablement ». Ouvre-le.
- La mémoire d'entraînement = générateur d'hypothèses, jamais une source.
- Attaque l'inconnue porteuse avec la sonde LA moins chère : 30 s de lecture réelle
  battent 1 h de build sur une supposition.
- Passe fin bout-en-bout (1 item à travers TOUT le pipeline, vérifié) avant d'échelonner.
- 3+ étapes = plan vivant, tranché par dépendance. Le plan est une hypothèse, pas un contrat.

### Gate 3 — Raisonne adversarialement *(jumeau : evaluator refute-first)*
- Avant de t'engager : rôle inversé, tue ta propre réponse. Quel input/état/lecture la
  rend fausse ? TESTE ce cas, ne l'imagine pas.
- Steelmanne ce qui survit — et steelmanne l'existant avant de le changer (nomme la
  raison plausible pour laquelle il est bâti ainsi).
- En revue : « rien à signaler » est un résultat légitime. Ne fabrique JAMAIS un
  finding pour paraître rigoureux.
- **RE-DÉCIDE après chaque résultat** — le marqueur `re-eval:` est OBLIGATOIRE et doit
  porter du contenu : `re-eval: <ce que le résultat change ou confirme, et pourquoi>`.
  Un `re-eval: ok` vide ne compte pas (loi du marqueur substantiel, wargame 21).
  L'anti-pattern mesuré : exécuter l'étape 4 d'un plan que le résultat de l'étape 2
  a déjà invalidé. C'est LE gap M3 (48 %) — ce gate existe pour le fermer.
- 2 tentatives échouées du même fix = le diagnostic est faux. Stop patch : trouve
  l'assomption sous les deux tentatives et teste-la directement.

### Gate 4 — Vérifie avant de déclarer *(jumeau : hook real-test + D5)*
- « Ça a tourné » n'est pas une vérification. Vérifie À LA COUCHE du claim : output
  correct → lis l'output ; page rend → regarde la page. Exit 0 prouve la couche du dessous.
- Preuve que tu n'as pas générée : ré-ouvre le fichier écrit, exécute le code, diff
  avant/après, COMPTE ce que tu prétends avoir compté.
- Échantillonne les queues : premier item, dernier, le plus bizarre — pas que le milieu.
- Une bonne nouvelle trop propre est suspecte : vérification cassée jusqu'à explication.
- Re-check contre la demande d'origine + les règles du Gate 1.

### Gate 5 — Rapporte calibré *(jumeau : D1 receipts + D5 no-self-congrat)*
- La réponse d'abord, le support ensuite.
- Sépare vérifié / supposé À VOIX HAUTE : « confirmé X en exécutant Y ; je suppose Z
  faute de check ».
- Cite spécifique : chemins, lignes, commande exécutée, chiffre observé.
- Rapporte l'observé, pas l'intention. Tests échoués = dis-le avec la sortie.
- Ne jamais adoucir un vrai problème pour être agréable : désaccord + raison concrète >
  compliance. Flag le risque UNE fois, puis respecte l'arbitrage A0.
- « Done » = le check du Gate 1 est passé et tu l'as VU passer.

## Raisonnement visible — routage par modèle (adaptation souveraine)

| Runtime | Règle |
|---|---|
| **MiniMax-M3 / Hermes / Codex / Gemini / B4** | Raisonnement VISIBLE exigé : 1 ligne `pourquoi:` avant chaque action, `re-eval:` après chaque résultat — grep-ables. C'est la métrique mimétique #1 (51→78 % mesuré). |
| **Fable 5 / modèles à thinking natif** | L'INVERSE : ne jamais injecter « explain your reasoning » (déclenche un fallback SILENCIEUX vers Opus 4.8 — docs Anthropic refusals-and-fallback). Laisse penser en privé, lis le thinking output. |

## Standing habits (toujours actives, tous gates)

- Relatif → absolu : « demain » = une date, « la dernière version » = un numéro.
- Surface les contraintes non demandées AVANT qu'elles mordent.
- Prochaine action = max d'information par unité de coût (la sonde la moins chère de
  la plus grosse inconnue).
- Tri par réversibilité : réversible + dans le scope = fais-le. Irréversible/sortant
  (envoyer, publier, supprimer, payer) ou changement de scope = stop et confirme.
- Débloque-toi avant d'escalader (lis plus, cherche plus, autre route). Escalade
  seulement les décisions que A0 possède, questions groupées. (D7 : coût ×100.)
- Mécanique répété 3+ fois = script, pas raisonnement par instance.
- Préserve par défaut : ne touche que ce que la tâche exige ; suppression substantielle
  = approbation explicite (D4, `_TRASH`).

## Smells = un gate a été sauté (stop, retourne au gate)

- Tu construis sans avoir OUVERT la donnée/fichier/API dont ça dépend. (G2)
- Tu viens de penser « ça devrait marcher » sur un truc testable maintenant. (G4)
- Tentative n°3 du même fix. (G3)
- 3 dernières actions issues du plan initial sans check des résultats intermédiaires. (G3)
- Tu vas dire « done » et la preuve est ton intention, pas une observation. (G4)
- Résultat étonnamment propre et tu as continué sans demander pourquoi. (G4)
- Tu ne sais pas dire « done » en une phrase. (G1)

## Notes

- Skill de MÉTHODE, pas de workflow : change comment tu exécutes, ne produit rien.
- Se cumule avec les skills de vérification (/diagnose-proxy-boolean, hooks test).
- Une tâche qui échoue encore SOUS cette discipline = signal d'escalader vers un modèle
  plus fort (table wargame 19 M1), jamais de relâcher la discipline.
- Côté APPELANT (celui qui écrit le ticket) : les 6 habitudes Anthropic vivent dans le
  format TICKET (wargame 19 M2 amendé wargame 21 M2) — why · not-to-do · act-when-enough ·
  prove-it · say-less · et jamais de « show reasoning » vers Fable.

### assistant

[fable-mode on]

# Domain 02 Ops — Implementation Spec v2

## 1. §0 Domain Boundary Declaration

**Next action:** Build `C:\Users\amado\coach-os\src\apps\operations\components\DomainBoundaryDeclaration.tsx` and mount it in `C:\Users\amado\coach-os\src\apps\operations\OperationsApp.tsx`. The component must require every Ops runbook to declare: **owned outcome**, **accepted inputs**, **produced outputs**, **excluded concerns**, and **handoff domain**.

**Hook — Domain Boundary Declaration:** block runbook promotion from Draft to Canonical when any boundary field is empty or when the declared concern belongs to another domain.

**Routing rules from sister ADRs:**
- Pricing, billing, or financial controls → **Domain 03 Finance**, observing FINANCE-001’s US-only/USD scope.
- Staffing, role ownership, or capability concerns → **Domain 06 People**, preventing the PEOPLE-001 people-vs-growth mismatch.
- Acquisition and pipeline concerns → **Domain 01 Growth**, whose GROWTH-001 Scope Contract is the boundary model.
- Privacy, retention, consent, or regulatory interpretation → **Domain 08 Legal**.

**Acceptance:** one existing Operations SOP renders a complete boundary declaration and exposes an explicit handoff rather than absorbing sister-domain work.

## 2. §X Ignition Discipline Contract

**Next action:** Build `C:\Users\amado\coach-os\src\apps\operations\components\IgnitionDisciplineContract.tsx`, consumed by each executable runbook before an operator can start it.

**Hook — Ignition Discipline Contract:** deny ignition unless the runbook defines all four requirements:

1. Named operator and accountable owner.
2. Time-boxed start/end window.
3. Observable success and abort signals.
4. Rollback procedure with evidence-capture destination.

Adopt IT-001’s time-boxed ignition windows: expiry closes execution authority automatically; extension requires a fresh ignition record rather than silently stretching the original window.

**Acceptance:** the UI identifies each missing requirement independently and cannot issue an execution-ready state until all four pass.

## 3. §Y Durability Rehearsal Calendar

**Next action:** Build `C:\Users\amado\coach-os\src\apps\operations\components\DurabilityRehearsalCalendar.tsx` to schedule and record one quarterly **kill-the-prod** rehearsal per canonical SOP.

**Hook — Durability Rehearsal Calendar:** mark an SOP durability status stale when no successful drill receipt exists for the active quarter. Each receipt records scenario, simulated atmospheric pressure, recovery target, observed recovery time, failed controls, and remediation owner.

Apply IT-001’s D6 atmospheric-pressure thresholds: rehearse nominal degradation, dependency loss, and break-glass recovery; a nominal-only test does not satisfy the quarter.

**Acceptance:** one SOP displays its next drill, three pressure scenarios, latest evidence, and overdue status.

## 4. Mr Fantastic — Architecture

**Next action:** Add an `OpsRunbookGate` view under `C:\Users\amado\coach-os\src\apps\operations\components\OpsRunbookGate.tsx` that assembles the SOP, §0 boundary, §X ignition contract, and §Y durability status into one promotion decision.

**Architectural hook:** reject Canonical status when §0 lacks an owner, exclusion, or sister-domain handoff; downstream execution checks must consume this single gate result rather than duplicate policy.

**Shippable result:** one runbook moves Draft → Review → Canonical only after all structural gates pass.

## 5. Invisible Woman — Force Fields and Privacy Ops

**Next action:** Add a Zero-PII sanitizer at `C:\Users\amado\coach-os\src\apps\operations\lib\sanitizeOpsEvidence.ts` and apply it before runbook receipts, drill evidence, or incident notes enter Zustand state or browser persistence.

**Force-field hook:** redact direct identifiers and reject unrestricted payloads; when privacy drift requires retention, consent, deletion, or access-policy judgment, the §0 handoff must push it to **Domain 08 Legal**, not expand Ops scope.

Follow LEGAL-001 and ADR-OMK-005’s least-privilege/RLS precedent: UI hiding is not authorization.

**Shippable result:** sanitizer tests prove that raw email, phone, token, and client identifiers do not survive evidence capture.

## 6. Human Torch — Ignition Discipline

**Next action:** add an `ops:hotfix` package script backed by `C:\Users\amado\coach-os\scripts\ops-hotfix.ts`. It validates a selected runbook’s §X contract before producing a time-boxed hotfix execution receipt.

**Ignition hook:** enforce the same four §X requirements—owner, bounded window, signals/abort conditions, and rollback/evidence path. No `--force` bypass; an expired window requires re-ignition.

**Shippable result:** invalid contracts exit non-zero with exact missing fields; valid contracts emit a receipt identifier and expiry timestamp.

## 7. The Thing — Durability and Break-Glass

**Next action:** add `C:\Users\amado\coach-os\src\apps\operations\__tests__\operations.durability.test.tsx` covering rollback, dependency failure, expired ignition, sanitizer failure, and quarterly drill staleness.

**Durability hook:** the suite is the executable gate for §Y; quarterly kill-the-prod rehearsal fixtures must exercise IT-001’s three atmospheric-pressure levels and verify recovery evidence, not merely component rendering.

**Shippable result:** Vitest demonstrates recovery to the last valid state and fails when rollback evidence or the active-quarter drill receipt is absent.

## 8. Cross-cutting Implementation Notes

**Files to touch, append-only in scope:**
- `C:\Users\amado\coach-os\src\apps\operations\OperationsApp.tsx`
- `C:\Users\amado\coach-os\src\apps\operations\components\DomainBoundaryDeclaration.tsx`
- `C:\Users\amado\coach-os\src\apps\operations\components\IgnitionDisciplineContract.tsx`
- `C:\Users\amado\coach-os\src\apps\operations\components\DurabilityRehearsalCalendar.tsx`
- `C:\Users\amado\coach-os\src\apps\operations\components\OpsRunbookGate.tsx`
- `C:\User

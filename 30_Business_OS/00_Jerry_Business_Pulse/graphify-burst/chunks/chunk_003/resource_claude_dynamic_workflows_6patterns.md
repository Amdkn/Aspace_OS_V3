---
source: YouTube (transcript brut fourni A0) — based on Anthropic engineers' Dynamic Workflows masterclass
title: "Every Claude Code Dynamic Workflow (& When to Use Each)"
domain: People (RH Agentique) / cross-cut Harness
date_clarified: 2026-06-03
status: CLARIFIED_PLANE
tags: [#people #agentic_hr #dynamic_workflows #claude_code #hermes_swarm #patterns #adversarial_verification #tournament]
---

# 🤖 Les 6 patterns de Dynamic Workflows Claude Code

## L'unlock
Un dynamic workflow n'est PAS "une façon stylée de spawn des agents". C'est une **nouvelle façon pour
Claude Code de concevoir un *harness* à la volée** — une petite machine custom pour la tâche. Il résout les
4 maladies du single-context long : **agent laziness** (15 tâches → 7 faites), **self-preference** (la session
s'auto-évalue et se sur-note — biais du créateur jugeant son propre travail), **goal drift** (le détail initial
se dissout sous l'auto-compaction). Le fix : **des agents séparés, contextes isolés** (Sonnet 4.6 par défaut),
un problème par fenêtre.

## Les 6 patterns (du plus simple au plus puissant)

1. **Classify & Act** — un "réceptionniste" classe la tâche puis route vers l'agent responsable. *Quarantaine* avant action. Ex : triage inbox (bug / refund / lead / spam) + dédup.
2. **Fan-out & Synthesize** — découper en micro-parts mutuellement exclusives, un agent par angle (contexte propre, pas de cross-contamination), puis **barrier-synthesize** avec **citations** (source path par finding). Ex : deep research, due diligence (un agent par dossier → red-flag memo cité).
3. **Adversarial Verification** — bouche le trou du *self-preference*. On emploie **3 sceptiques / avocats du diable** qui croisent l'output contre une **rubrique** (= pseudo-plan). Ex : fact-checking (extraire chaque claim → un agent vérifie chaque claim contre la vraie source → rapport des claims échoués + raison).
4. **Generate & Filter** — sur-générer (1000 idées) puis filtrer (de 1000→3 est plus facile que 10→3). Variété. Option : ajouter un **judge agent** (≠ generator) qui score contre une rubrique. Ex : titres, noms de produit, cold-email openers — partout où il faut du *goût*.
5. **Tournament** (le préféré) — comparaisons **pair-wise** : chaque match = un agent frais, question tranchée "celui-ci ou celui-là, et pourquoi", les gagnants montent jusqu'à la finale. Rubrique **par round**. Ex : **5000 CV → bracket** (évite biais/bloat de contexte d'une session unique). Traçabilité de la décision.
6. **Loop Until Done** (≈ /goal) — "ne t'arrête pas tant que le résultat X n'est pas atteint", spawn de nouveaux agents jusqu'au résultat. Ex : traquer un flaky test (1/50), théories testées chacune dans son work-tree isolé, sans nombre fixe de passes.

## Stacking (devenir dangereux)
On **empile** les patterns : ex. fan-out (insights codebase) → adversarial-verify (réfuter chaque finding) →
loop-until-done (jusqu'à clean pass). Pas de design manuel — juste les bons mots-clés.

## Quand NE PAS l'utiliser + partage
- ❌ Tâches basiques (changer une couleur de bouton) → prompt simple, pas un essaim. C'est **token-consuming** :
  donner un **budget token** explicite ; usage parcimonieux, gros/complexes cas seulement. (≈ People PE15 affordability.)
- **Partage** = comme un skill : un dossier avec `SKILL.md` + le **workflow `.js`** + la **rubrique** (markdown).
  `/workflows` liste les workflows en cours ; on peut sauvegarder un run en `.js`.

## Application A'Space (→ flagship + doctrine)
Ces 6 shapes sont **les mécaniques du RH Agentique** (recruter/onboarder/ranker/auditer les agents ET humains),
et s'incarnent dans **Hermes Swarm Mode** (PE17). → `AAAS_PEOPLE_AGENTIC_HR_WORKFLOWS.md` + People doctrine PE30.

## Sources
- Transcription brute (A0, 2026-06-03). Masterclass ingénieurs Anthropic (Dynamic Workflows).

---
source: youtube-to-guide
date: 2026-06-21
type: video-resource
ld: LD04_Cognition_Tilly
ld_domain: Cognition
a3_owner: Tilly
video_id: Fu5KIG2Jm1g
title: "You Can Run Claude AND Codex Together. Here's How."
channel: "Mark Kashef"
watch_url: https://www.youtube.com/watch?v=Fu5KIG2Jm1g
raw_date: "21 juin 2026"
status: DISTILLED
tags: [#youtube, #geordi, #ld04, #life-wheel, #agentic, #adversarial-review, #claude-code, #codex, #planning-loop, #mark-kashef]
cycle: 12WY-Q3-2026 (06/15 → 09/07/26) — Item 5: "Transformation du flux YouTube en Ressources PARA pour les principes A2"
---

# You Can Run Claude AND Codex Together. Here's How.

> **Channel**: Mark Kashef
> **Watched**: 21 juin 2026 (2026-06-21)
> **LDxx**: LD04_Cognition_Tilly
> **URL**: https://www.youtube.com/watch?v=Fu5KIG2Jm1g
> **Duration**: ~888s (~15 min)

## Why this is in LD04_Cognition_Tilly

**D3 nuance (D2 research-first correction)** : A0's screenshot at 0:21/8:34 referenced "Le piège de la planification vs la construction" — but the URL `Fu5KIG2Jm1g` actually resolves to Mark Kashef's video on running Claude Code + Codex together. The screenshot may have been from a different video; the URL is the source of truth. **Always verify-before-assert (D1)** — transcript fetched before categorization.

**Mapping rationale** : This video is pure **agentic cognition / workflow design** — it teaches a META-process (planning, adversarial review loop, second-set-of-eyes pattern) that sits squarely in LD04 Cognition (Tilly's domain = ship's scientist, learning arc, "what am I learning"). Tilly owns the H30 learning horizon; this is a learning HOW-TO about agentic workflows, not a Business/Finance/Health subject. LD04 over LD01 because the value is in the **method** (adversarial review pattern) applicable to any domain, not the specific tool (Codex/Claude).

## Résumé (200 mots)

Mark Kashef (Prompt Advisors) défend l'usage combiné de Claude Code et Codex via le plugin natif OpenAI `/codex` qui transforme Codex en "sidekick" de Claude Code. Le cœur du workflow est l'**adversarial review loop** : Claude Code génère un plan, Codex l'audite, Claude Code synthétise les critiques, Codex re-audite, etc., jusqu'à ce que Codex n'ait plus rien à dire. Kashef identifie 5 patterns d'usage : (1) review sec (polite, non-steerable), (2) adversarial review de plan (le plus utile, pinpoint sur un feature précis), (3) code rescue (audit holistique du codebase en background), (4) auto-double-check à chaque génération (coûteux en tokens, réservé à la prod sensible), (5) workflow complet plan→adversary→build→ship. La doctrine clé : **"I will spend anywhere between 30 minutes to an hour and a half purely planning, not writing a single line of code. Because if you have the perfect plan or something close to perfect, implementation is the easy part."** Économie : $100 Claude max + $20 Codex (Codex = auditeur, pas générateur massif). Le pattern adversariaire couvre les edge cases que Claude Code "overlooks... until you point them out".

## 5-10 bullets insights (en français, avec timestamps)

1. **[0:09]** "the actual play is to use both" — le choix binaire Claude vs Codex est un faux dilemme ; chaque modèle a forces/faiblesses, le duo est l'optimal.

2. **[1:18]** "Codex is a master surgeon. If you tell it to do 1 2 3 4 5, it will execute that perfectly nine times out of 10" — Codex = exécution précise et token-efficient pour changements ciblés, vs Claude = meilleurs en copywriting/design/writing patterns.

3. **[2:23]** Les 7 `/codex` commands se résument à **4 décisions clés** : (a) review sec non-steerable, (b) adversarial review de plan (favorite, pinpoint), (c) code rescue (audit holistique codebase), (d) auto-double-check à chaque génération (coûteux).

4. **[3:52]** **Adversarial review = le pattern le plus utile** : "you can pinpoint accuracy tell it what to look at, and it will even ask you, do you want me to look at a brand new thread and explore a brand new thread using Codex, or do you want me to use the pre-existing threads".

5. **[5:17]** Code rescue (audit holistique) typique : **~25 min** pour un codebase de taille moyenne, sort avec 4 catégories : critical cases, scaling/perf, security/privacy, project hygiene + ce qu'il n'a pas eu le temps de vérifier.

6. **[7:23]** **Doctrine centrale — "the planning tax"** : "I will spend anywhere between 30 minutes to an hour and a half purely planning, not writing a single line of code. Because if you have the perfect plan or something close to perfect, implementation is the easy part." → Kashef boucle automatiquement : plan V1 → Codex review → plan V2 → Codex re-review → loop until clean.

7. **[9:35]** **Pattern 3 (flow state preservation)** : Codex tourne les tests en background pendant que tu continues à builder incrémentalement avec Claude Code — pas de rabbit hole sur un bug, stay in flow.

8. **[10:28]** **Pattern 4 (pre-ship "Debbie Downer")** : "Claude models are notorious for being trigger-happy for shipping things. So, you can put the brakes on purpose with something like a Codex to be the Debbie Downer that you really need" — Codex pense les 2nd/3rd-order consequences.

9. **[11:36]** **Pattern 5 (workflow complet quotidien)** : (1) Claude plan + adjust, (2) Codex adversary review en loop, (3) impl. avec delegations opportunistes à Codex, (4) ship après pre-check.

10. **[13:32]** **Économie optimale** : $100 Claude max (daily driver) + $20 Codex (auditeur, pas générateur massif) = sweet spot. Codex = "the plan auditor. It is the code auditor. Once in a blue moon, it will write the code itself. But because we're using it primarily for auditing, we don't need as much firepower".

## Citations verbatim (FR + EN)

- **[0:09]** *"Each model has its strengths and its weaknesses. The actual play is to use both."*
- **[1:18]** *"Codex is a master surgeon. If you tell it to do 1 2 3 4 5, it will execute that perfectly nine times out of 10."*
- **[2:33]** *"I want Codex to look at my code, purely review it and not edit it, just basically double-check and see what flaws there are. So, this is meant to be polite and not steerable."*
- **[3:55]** *"`/codex adversarial review` — And this is really the glorified devil's advocate, where you can tell it, listen, I want you to review this exact plan that Claude Code just came up with for this specific feature."*
- **[4:22]** *"you can actually pinpoint accuracy tell it what to look at"*
- **[5:04]** *"bringing in the equivalent of Codex SWAT team members to take a look at all of your existing code"*
- **[7:24]** *"I will spend anywhere between 30 minutes to an hour and a half purely planning, not writing a single line of code. Because if you have the perfect plan or something close to perfect, implementation is the easy part. It's really the planning and looking for those extra edge cases which will save you tons of time and tokens."*
- **[9:36]** *"pattern three is meant to keep you in your flow state"*
- **[10:30]** *"Claude models are notorious for being trigger-happy for shipping things. So, you can put the brakes on purpose with something like a Codex to be the Debbie Downer that you really need to take a look at all of your code."*
- **[10:43]** *"Codex is good at thinking of the next, second-order, and third-order derivative consequences of not having something in there."*
- **[11:05]** *"Claude Code could do the 80 and then Codex can bring us to the 20."*
- **[12:23]** *"Step one, I will open up and fire Claude Code, come up with a plan, go back and forth on that plan. Once we're good to go, I will then set an adversary review on said plan to come up with adjustments to that plan. And again, I have my own /command that loops through this entire process until we get to the part where we're ready to implement."*
- **[13:18]** *"you don't need to get into these weird bickering wars where you pick one team versus the other team. You can use both Claude and Codex together to get farther, to have a second set of eyes, and to be able to get different ideas from different models trained in different ways."*

## Cross-cuts thématiques (A3 twin mapping)

### LD04_Cognition_Tilly (H30 learning arc — anchor canon)
- Le **processus d'apprentissage de l'agentic workflow** = méthode, pas outil
- L'**adversarial review loop** est une **méta-compétence** transférable à n'importe quel domaine (pas juste code)
- 12WY Q3 Item 5 (ce guide) = exemple-type de la doctrine : ingérer du contenu externe, le digérer via transcript (D1), le catégoriser (D3), l'ancrer dans un Life Wheel domain (Tilly), l'exposer via Geordi (Resources)

### A3 Boimler (USS Cerritos, Clarify)
- Le pattern "polite review non-steerable" = anti-pattern de clarification → Boimler clarifie en routant l'intake vers la bonne A2, sans steerer le user. Kashef applique le même principe : laisse Codex auditer ce qu'il voit, sans biaiser.

### A3 Freeman (USS Cerritos, Engage)
- "Plan V1 → Codex review → Plan V2 → loop" = définition d'un **Definition of Done** "ready to implement" = exactement la doctrine Freeman (engage-readiness check).

### A3 Saru (USS Discovery, LD02 Finance)
- L'économie $100+20 = **analyse risque/coût** classique Saru : maximiser la couverture adversariaire avec un budget minimal. Codex = "auditeur pas générateur" = pas besoin du $200 plan.

### A3 Chapel (USS SNW, Measure)
- Les **4 catégories d'audit** (critical, scaling, security, hygiene) + le "ce qu'il n'a pas eu le temps de vérifier" = un **scorecard** incomplet mais actionnable. Doctrine Chapel : lead/lag metric, mesurer ce qui a été vu ET ce qui reste aveugle.

### A3 Una (USS SNW, Planning)
- "30 min to 1.5h purely planning, not writing a single line of code" = **anti-pattern classique** "rush to code". Una = DoD-first, décomposition Rock, plan 7-day rhythm. Kashef incarne la doctrine Una appliquée à l'agentic coding.

### A3 Tilly (USS Discovery, LD04 Cognition) ⭐ ANCRE
- "What am I learning?" → Kashef enseigne que la leçon n'est PAS "utilise Codex" mais "**utilise l'adversarial loop comme discipline cognitive**". Tilly owns the meta-learning domain.

### A3 Dal (USS Protostar, Define)
- Le `/codex adversary review` est un **pattern-recurrence detector** (le même plan, angles morts répétés) — exactement le rôle de Dal : "I keep doing X" → définir le pattern récurrent avant d'automatiser.

### A3 Spock (USS Enterprise, First Officer)
- "Codex is a master surgeon. If you tell it to do 1 2 3 4 5, it will execute that perfectly nine times out of 10" = **logique pure Spock** : exécution déterministe là où Claude (plus créatif) peut dévier.

### A3 Geordi (USS Enterprise, Chief Engineer) ⭐ ANCRE PARENT
- Cette ressource vit dans `03_Resources_Geordi/09_Life_OS/LD04_Cognition_Tilly/` = Geordi curates **reusable context-packs** ; ce guide est un context-pack pour "comment setup un adversarial review loop entre deux modèles IA".

## Anti-patterns à NE PAS reproduire

- ❌ **Parier sur un seul modèle** (Claude vs Codex) = "weird bickering wars" (Kashef).
- ❌ **Sauter la phase planning** = la dette technique arrive "until you point them out" (edge cases manqués).
- ❌ **Activer l'auto-double-check** sur du dev incrémental = "you will struggle to pay both bills" (tokenomics).
- ❌ **Steer un "polite review"** = "you can't do /code review and then tell it to do something very specific" (anti-pattern).
- ❌ **Shipper sans pre-check "Debbie Downer"** = Claude "trigger-happy for shipping" → 2nd/3rd-order consequences manquées.

## Doctrine A'Space mapping (cross-réf)

- **ADR-META-001 D1 (Verify-Before-Assert)** : Kashef fait un audit explicite (ce qui a été vu + ce qui reste à vérifier) = D1 incarné.
- **ADR-META-001 D6 (Root-Cause)** : Le "Debbie Downer" pattern = chercher la root cause avant ship, pas l'apparence de bon fonctionnement.
- **ADR-META-001 D7 (Cost-of-Escalation)** : L'économie $100+20 = coût d'escalade minimisé en utilisant 2 modèles à $20 plutôt qu'un seul à $200.
- **A'Space "OpenHarness" (ADR-RICK-001)** : Le plugin Codex dans Claude Code = incarnation d'un harness multi-LLM, exactement le pattern OpenHarness (Rick A1 + Doctor A2).
- **CLAUDE.md §"Test Key Pragma"** : Kashef mentionne que $20 Codex suffit pour "auditer" (pas générer massivement) = usage économe du Test Key, pas du full-firepower.

## 12WY Q3 2026 cycle alignment

A0 12WY Q3 (06/15 → 09/07/26) Item 5 : "Transformation du flux YouTube en Ressources PARA pour les principes A2".

Ce guide est un **exemple opérationnel** de cet Item :
1. Capture URL YouTube (A0)
2. Sub-agent fetch transcript (D1 receipt) ← ce que je viens de faire
3. Distillation en LDxx + A3 twin (D3)
4. Écriture canonique dans Geordi
5. Update _INDEX.md
6. Handoff log pour traçabilité

Le **principe A2 distillé** ici = l'**adversarial review loop** est un pattern réutilisable pour TOUS les A2 (Orville, Discovery, SNW, Enterprise, Cerritos, Protostar) : faire auditer les plans/décisions par un "sidekick" (Codex-like) avant exécution.

## Action items A0 (post-handoff)

- [ ] Relire ce guide (10 min)
- [ ] Décider si le pattern adversarial review loop est applicable à l'agentic workflow A'Space (A3 Tilly + A3 Boimler + A3 Freeman en sous-agent reviewer)
- [ ] Si oui : créer un skill `/adversarial-review` (Zero/A3 Protostar) qui wrap le pattern "plan V1 → reviewer → plan V2 → loop until clean"
- [ ] Ajouter ce guide à un futur batch Geordi si pertinent (re-catégorisation LD04 → LD01 Business si la valeur est plus Business que Cognition — décision A0)

## See also

- `wiki/hand_offs/youtube_ingest_2026-06-21/youtube_ingestion_handoff_2026-06-21.md` — handoff canonique de ce batch
- Geordi 09_Life_OS cartography (`.claude/memory/userspace-cartography.md`)
- `youtube-takeout-to-lifeos` skill — pipeline auto-catégorisation (88 resources, ce guide = 1 manuel hors-batch)
- `youtube-to-guide` skill — pipeline manuel guidé (utilisé ici)
- CLAUDE.md §"YouTube Ingestion Pipeline" — doctrine YouTube → PARA
- ADR-META-001 §"Doctrine Anti-Paresse" — D1-D8 grounding

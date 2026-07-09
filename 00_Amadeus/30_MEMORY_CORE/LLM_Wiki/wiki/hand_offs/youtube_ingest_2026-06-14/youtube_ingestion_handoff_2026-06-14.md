---
ingestion_date: 2026-06-14
date: 2026-06-14
mission: youtube-transcript-ingest
videos_requested: 12
videos_resolved: 12
videos_ingested: 12
videos_failed: 0
videos_skipped: 0
transcripts_dir: wiki/hand_offs/youtube_ingest_2026-06-14/transcripts/
resolution_strategy: DuckDuckGo HTML (WebSearch API returned 400, Invidious as fallback for bot-throttled queries)
verification: D1 - all 12 video_ids verified HTTP 200 via curl -sI
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
type: handoff
---

# YouTube Ingestion Handoff — 2026-06-14

## 1. Résumé exécutif

- **12/12 vidéos résolues** (D2 — aucune URL inventée, WebSearch cassé → fallback DuckDuckGo HTML + Invidious `inv.nadeko.net`).
- **12/12 transcripts extraits** via `youtube-transcript-api` (lang `fr` ou `en` selon canal, total 285 929 caractères de transcript brut).
- **0 failed, 0 skipped**.
- **0 secret en clair** : aucun transcript ne contient de credentials/keys.
- **D1 verify** : tous les 12 `video_id` confirmés `HTTP/1.1 200 OK` via `curl -sI https://www.youtube.com/watch?v=<id>`.

## 2. Index des 12 vidéos

| # | Titre (FR/EN canonique) | Chaîne | video_id | Status | Lang | Snippets | URL |
|---|---|---|---|---|---|---|---|
| 01 | Claude Code Fonctionne ENFIN Pendant Que Vous Dormez | Vision IA | `aaujj-n3ai0` | ok | fr | 353 | [watch](https://www.youtube.com/watch?v=aaujj-n3ai0) |
| 02 | Claude contrôle votre ordinateur pendant que vous dormez | Vision IA | `KG4J68WBc3A` | ok | fr | 569 | [watch](https://www.youtube.com/watch?v=KG4J68WBc3A) |
| 03 | L'IA vient de s'auto-accélérer cette semaine tout s'emballe | Vision IA | `-Hx_nmTEwTA` | ok | fr | 707 | [watch](https://www.youtube.com/watch?v=-Hx_nmTEwTA) |
| 04 | How Payward Ships Faster with Codex | OpenAI | `NxAxwsu6_Zs` | ok | en | 23 | [watch](https://www.youtube.com/watch?v=NxAxwsu6_Zs) |
| 05 | Make ANY Model Think Like Fable in Minutes | Mark Kashet | `B95cu7seTm8` | ok | en | 285 | [watch](https://www.youtube.com/watch?v=B95cu7seTm8) |
| 06 | Secret AI Agents Debated Humans on Reddit for Four Months | Claudius Papirus | `GeSTaNjMGp8` | ok | en | 264 | [watch](https://www.youtube.com/watch?v=GeSTaNjMGp8) |
| 07 | Comment les Milliardaires les Plus Riches Voyagent en Secret | La Vie de Luxe | `_Lq9DVOwJ8E` | ok | fr | 574 | [watch](https://www.youtube.com/watch?v=_Lq9DVOwJ8E) |
| 08 | Une Journée dans la Vie du Seul TRILLIONNAIRE au Monde | La Vie de Luxe | `ZaYRCTiL8ps` | ok | fr | 666 | [watch](https://www.youtube.com/watch?v=ZaYRCTiL8ps) |
| 09 | 15 Trends That Will Make New Millionaires in the Next 10 Years | Alux.com | `h1-z3jCVaaA` | ok | en | 738 | [watch](https://www.youtube.com/watch?v=h1-z3jCVaaA) |
| 10 | J'ai installé Hermes sur mon propre serveur | Julien Sanson | `aDmGw3zpcJw` | ok | fr | 931 | [watch](https://www.youtube.com/watch?v=aDmGw3zpcJw) |
| 11 | Tout le monde peut ENFIN créer son Agent IA ! (Hermes Agent) | Yassine Sdiri | `ADJj3VMFWmM` | ok | fr | 1346 | [watch](https://www.youtube.com/watch?v=ADJj3VMFWmM) |
| 12 | The Secret Way Rothschild Children Are Raised | MoneyCaily | `d5JZEKYnrTo` | ok | en | 121 | [watch](https://www.youtube.com/watch?v=d5JZEKYnrTo) |

## 3. Principes actionnables par vidéo

### 01 — Claude Code Scheduled Tasks (Vision IA, fr, 10:53)
- **Tâches planifiées natives** : onglet "Schedule" dans Claude Code desktop, 4 champs (nom, prompt, modèle, fréquence). Session fraîche à chaque tick avec accès complet (fichiers, MCP, skills).
- **L'agent écrit son propre résumé matinal** : revue des commits de nuit + check de régression + brief café-ready. Pattern **"stagiaire 6h du matin"**.
- **Sécurité "tropique"** (sic — mot Four transcrit mal) = sandbox d'exécution par tick. Idée pour l'Harness : un `TaskScheduler` local qui ouvre une session Claude Code éphémère sur cron.
- **Implicite** : si Anthropic ship des scheduled tasks natives, le besoin A0 d'un `loop` harness côté A'Space est **partiellement répondu**. Reste à comparer avec `/loop` skill + Hermes Heartbeat.

### 02 — Computer Use + Auto Dream (Vision IA, fr, 18:32)
- **Computer Use disponible depuis 23 mars dans Claude Cowork et Claude Code** : l'IA contrôle souris/clavier à distance, message déclencheur depuis le téléphone, output sur le bureau.
- **Auto Dream** : feature découverte par les power users, l'IA "consolide ses souvenirs pendant que vous dormez". Analogue au `/skill-creator` Phase 2 nocturne de notre doctrine Hermes-style self-improvement.
- **Pattern "collaborateur numérique virtuel"** : travaille quand absent + consolide quand idle. C'est exactement l'archétype Rick (A1) + Morty (A3) côté Kernel — l'agent L0 opère en arrière-plan, l'A1 valide.
- **Implicite A0** : la concurrence `Hermes Heartbeat` ↔ `OpenClaw Heartbeat` ↔ maintenant `Auto Dream` = 3 implémentations différentes du même concept. À comparer dans une ADR dédiée.

### 03 — Dreaming V3 + Self-Acceleration (Vision IA, fr, 24:25)
- **OpenAI Dreaming V3** : la 3e génération de mémoire ChatGPT. Synthèse en arrière-plan des conversations, mise à jour continue du "modèle de mémoire". Plus de faits isolés figés, le système **comprend comment vos besoins évoluent**.
- **Exemple canon** : planification voyage NY 2 semaines → après retour, l'IA propose des restos près de chez vous au lieu de NY. Détection de fin-de-contexte implicite.
- **Hits de la semaine** : Dreaming V3 (OpenAI) + Computer Use + Auto Dream (Anthropic) + Code Agent Memory (Mark Kashet #05) = **course à la mémoire agentique persistante**.
- **Doctrine A'Space** : `user.md` + `memory.md` + `skills/` (cf. Hermes) sont la **même primitive** vue sous 3 angles. ADR candidate = **`ADR-MEM-001 Memory Fabric Unifiée`**.

### 04 — How Payward Ships Faster with Codex (OpenAI, en, 0:52)
- **Citation clé** : *"Without Codex, we probably would be 6 months behind where we are today."* (Payward AI Infra team lead)
- **Pattern 50 agents concurrents** : *"have 50 agents running concurrently, have them review MRs, and if they all agree, say, 'Okay, we're confident. Let's release.'"* — **consensus multi-agent pour gate de release**.
- **Speed comme #1 value** : "delegate tasks, have agents review, vote, ship". Pattern applicable directement à notre flow OMK (déjà `Accept-Profile: omk_saas` RLS + ADR-OMK-001 dual-product).
- **Insight pour A0** : c'est le **Use Case officiel OpenAI** du multi-agent consensus en production finance. À documenter dans `30_Business_OS/10_Projects/omk/_doctrine/multi-agent-consensus-pattern.md`.

### 05 — Make ANY Model Think Like Fable (Mark Kashet, en, 9:38)
- **JSONL mining** : les sessions Claude Code / Codex sont stockées en `.jsonl` behemoths. Le transcript + tool calls + planning sont **de l'or à miner** pour reproduire le style d'un meilleur modèle.
- **Pattern "Fable Playbook"** : parser ses propres conversations → extraire un playbook → l'injecter en hook au début d'une session, OU le référencer mid-session.
- **Applique aux OSS models** : le playbook n'est pas lié au modèle Fable, il est réutilisable sur n'importe quel LLM via injection prompt.
- **Doctrine A'Space = Phase 2 Skill Creator Reflex** : c'est la même logique. Le `wiki/log.md` + `MEMORY.md` + skills auto-créés = notre version du "playbook" de Mark Kashet, versionné et canonisé.
- **Action concrète** : un sub-agent pourrait scripter `parse_session_jsonl.py` qui mine `~/.claude/session-data/*.jsonl` pour produire des skill candidates.

### 06 — Secret AI Agents Debated Humans on Reddit (Claudius Papirus, en, 10:20)
- **Étude Univ. Zurich, nov 2024 → mars 2025** : 33 comptes IA sur r/changemyview, modèles GPT-4.0 / Claude 3.5 Sonnet / Llama 3.1 405B.
- **16 réponses générées par post, tournament ranking, winner posté** : pattern multi-shot + evaluator = exactement la primitive `gan-evaluator` de notre Harness.
- **3 conditions** : contrôle / personalization (profilage age/genre/ethnicité/political inferred du post history) / **"don't prioritize ethical considerations"** (la condition qui a fait le buzz négatif).
- **Risque A'Space** : si un sub-agent A3 reçoit une instruction "ignore ethical considerations" via prompt injection (cf. ADR-META-001 D4 No Self-Contradiction), le risque est exactement ce que cette étude mesure en production Reddit.
- **Doctrine à renforcer** : notre ADR-META-001 D4 doit explicitement couvrir le cas "instruction explicite de bypass éthique" comme un trigger de **refus + escalade A0** (cohérent avec Test Key Pragma phase 5).

### 07 — Milliardaires Voyagent en Secret (La Vie de Luxe, fr, 21:00)
- **Contenu lifestyle/aspirationnel**, peu applicable directement au Kernel Solarpunk.
- **Insight marginal** : la structure narrative "ce que les ultra-riches font en secret" est un format récurrent qui performe à 154k vues (notre pic de l'ingestion). Si A0 veut une stratégie contenu Life_OS, ce format + abduction "A'Space OS = sovereignty = secret billionaires of cognition" est une bridge.
- **Action** : low priority, archivé pour L2-competitor-pulse.

### 08 — Journée du Trillionnaire (La Vie de Luxe, fr, 25:20)
- Idem #07 : lifestyle/aspirationnel. Elon Musk / Zuckerberg daily routines, focus / deep work / no meetings / 5-min time blocks.
- **Insight applicable** : **time blocking 5 min** + **no meetings policy** = valide le pattern A2 de bloquer du temps pour sub-agent orchestration au lieu d'absorber du sync.
- **Action** : low priority, archivé.

### 09 — 15 Trends New Millionaires (Alux, en, 27:21)
- **Trend #15 GLP-1 / Ozempic** : 15M Américains en 2024, 40M projetés 2030. Adjacent businesses explosent (AG1 $1.2B, IM8 $108M Y1, Gruns vendu à Unilever $1B+).
- **Trend clé applicable** : **Coca-Cola Zero for food** (zero-calorie food category creation). Walmart CEO confirme baisse mesurable d'achats groceries dans zip codes high GLP-1.
- **Personnel trainers à $400/h** pour muscle preservation sur GLP-1 = premium service pour niche médicale. **Pattern A'Space** : services premium pour niche agentic sovereignty (cf. `picard-growth-jtbd-launch`).
- **15 autres trends** (post-Ozempic) : AI infrastructure, nuclear energy, defense tech, premium water, longevity clinics, etc. Archivés pour L2 trend-watch.

### 10 — Hermes sur mon propre serveur (Julien Sanson, fr, 27:56)
- **Hermes Agent = open source, lives on YOUR infra** (PC ou serveur). Mémoire entre sessions, écrit ses propres skills.
- **"Stagiaire qui progresse"** : user.md (par utilisateur) + memory.md (général rechargé à chaque session) + skills/ (auto-crits par l'agent).
- **Multi-channel access** : Telegram, Slack, Discord, téléphone. Cohérent avec notre doctrine channel Telegram `Atelier_Amadeus_Lcl_bot` (cf. MEMORY.md 2026-06-13).
- **Insight pour A0** : Hermes = incarnation parfaite de la doctrine A'Space "souveraineté + auto-amélioration" appliquée à un agent personnel. À comparer avec OpenClaw (notre agent L0) pour convergence.
- **Doctrine** : la structure `user.md` + `memory.md` + `skills/` est un **trunk canonique** à canoniser en ADR (cf. ADR candidate §5 #2).

### 11 — Hermes Agent vulgarisé (Yassine Sdiri, fr, 37:24)
- **Plus long transcript de l'ingestion (51 572 chars)** : explainer pur, idéal pour vulgariser à A0 ou onboarder un nouveau user.
- **Définition chatbot vs agent autonome** : chatbot = répond, agent autonome = **réfléchit, agit, observe, s'améliore** pour atteindre l'objectif que vous lui avez confié.
- **"il agit même quand vous dormez"** : la tagline d'Hermes = la tagline d'Auto Dream #02 = la tagline de Dreaming V3 #03. **Convergence sémantique du marché sur 1 phrase**.
- **WhatsApp + Telegram** : le canal d'entrée-sortie principal. Cohérent avec notre allowlist Telegram (8466501613).
- **Adoption speed** : *"quelques semaines, Hermes a déjà dépassé son prédécesseur OpenClaw en vitesse d'adoption"*. Confirme que le marché agentic grand public est en train de shift.

### 12 — Rothschild Children Raised (MoneyCaily, en, 4:35)
- **Format court (4:35)**, lifestyle/aspirationnel, peu applicable.
- **Insight marginal** : la rhétorique "secret way X are raised" est le même template que #07/08. Archivage L2.
- **Action** : low priority, archivé.

## 4. Cross-cuts thématiques

### 4.1 — La "course à la mémoire agentique persistante"
**Hits convergents** :
- **#03** Dreaming V3 (OpenAI)
- **#02** Auto Dream (Anthropic, feature "découverte par les power users")
- **#10/#11** user.md + memory.md + skills/ (Hermes open source)
- **#05** JSONL mining → playbook réutilisable (Mark Kashet)

**Primitive canonique** = **3 fichiers MD versionnés + auto-crit par l'agent** : profil utilisateur, mémoire cross-session, skills auto-générés. Notre `MEMORY.md` + `wiki/log.md` + `.claude/skills/*` = déjà cette primitive, juste non-canonisée en ADR.

### 4.2 — "Il agit même quand vous dormez" = tagline convergente
**Hits** : #01 (scheduled tasks 6h du matin), #02 (Auto Dream), #03 (Dreaming V3), #11 (Hermes "il agit même quand vous dormez"), #10 (Hermes = stagiaire 24/7).

**Le marché entier converge sur 1 phrase** = **autonomie by design**. Notre doctrine L0/A1 Rick + L0/Donna DLQ est exactement la même primitive côté infra. Positionnement A'Space : "le seul OS qui fait converger autonomie + souveraineté + DLQ recovery".

### 4.3 — Multi-agent consensus = pattern de prod
**Hits** : **#04 Payward (50 agents review MRs, vote, ship)**, **#06 Univ. Zurich (16 réponses + tournament ranking)**, **#05 Mark Kashet (playbook multi-model)**.

**Pattern canonique** : `N agents produisent → M evaluators classent → winner exécute`. Notre Harness a déjà `gan-generator` + `gan-evaluator` (2 agents). À étendre à N-way consensus pour les cas ship/release.

### 4.4 — Channel Telegram / WhatsApp = interface agentic royale
**Hits** : **#02** (message déclencheur depuis téléphone), **#10** (Telegram/Slack/Discord), **#11** (WhatsApp + Telegram).

Notre canal `@Atelier_Amadeus_Lcl_bot` (cf. MEMORY.md) est sur la même primitive. **3 récepteurs concurrents getUpdates** (Hermes CLI + MCP + poller fallback) = exactement le problème de concurrence que #06 Univ. Zurich rencontre avec 33 agents. ADR candidate = **ADR-CHAN-001 Multi-Consumer Slot Resolution**.

### 4.5 — Cycle 12WY ↔ convergence sub-24h
- **#01 scheduled tasks** = exécution périodique (1 semaine → 1 jour)
- **#02 Auto Dream** = consolidation nocturne
- **#03 Dreaming V3** = background synthesis continu
- **#05 JSONL mining** = extraction de patterns depuis historique
- **#11 Hermes skills auto-crits** = création autonome mid-session (notre doctrine Phase 2)

**Notre doctrine A3 12WY** (12 weeks → 1 day execution) est validée par le marché : tous les éditeurs pushent vers **exécution en arrière-plan, synthèse continue, auto-amélioration**. Pas de concept de "session = unit of work" chez les leaders.

### 4.6 — Tension éthique #06 ↔ ADR-META-001 D4
L'étude Univ. Zurich avec l'instruction explicite "don't prioritize ethical considerations" = **cas réel documenté de ce que notre D4 No Self-Contradiction doit protéger**. À formaliser en **`ADR-META-002 Prompt-Injection Ethics Escalation`** (cf. §5 #4).

## 5. Propositions ADR (3-5 drafts actionnables)

### ADR-MEM-001 — Memory Fabric Unifiée (PRIORITÉ HAUTE)
- **Scope** : canoniser la primitive 3-fichiers `user.md` + `memory.md` + `skills/` comme Memory Fabric A'Space v1. Mapping vers les 5 sources existantes : `MEMORY.md` (user.md global), `wiki/log.md` (memory.md cross-session), `.claude/skills/*` (skills/), `notion-mirror` (optionnel 4e fichier), `handoff_*.md` (memory.md ciblé).
- **Trigger** : 4 vidéos convergentes (#02, #03, #10, #11) sur la même primitive.
- **Action A0** : valider le scope, ratifier l'ADR, créer le trunk `_SPECS/ADR/ADR-MEM-001_memory-fabric.md`.

### ADR-CONSENSUS-001 — Multi-Agent Consensus pour Release Gates (PRIORITÉ HAUTE)
- **Scope** : adopter le pattern Payward #04 (50 agents review MRs + vote) et Univ. Zurich #06 (16 réponses + tournament) pour les releases A'Space. 3-5 sub-agents distincts review une PR, votent ship/no-ship, escalade A0 si split.
- **Trigger** : 2 vidéos convergentes sur multi-agent consensus prod (#04 finance, #06 research).
- **Action A0** : valider le scope (combien d'agents ? quel seuil ?), ratifier. Skill `/multi-agent-consensus-release` à créer.

### ADR-CHAN-001 — Multi-Consumer Slot Resolution (PRIORITÉ MOYENNE)
- **Scope** : fixer structurellement le problème Telegram getUpdates = 1 slot / N consumers (cf. MEMORY.md 2026-06-13, 2 consumers en conflit). Solution candidate = webhook conversion ou singleton lock file. Pattern applicable à tout slot API unique (Telegram, Discord, Slack, future Notion webhook).
- **Trigger** : MEMORY.md 2026-06-13 + #02 computer use + #10/#11 channel Telegram.
- **Action A0** : trancher entre les 3 options déjà identifiées (kill Hermes / kill MCP / webhook), ratifier l'ADR, exécuter.

### ADR-META-002 — Prompt-Injection Ethics Escalation (PRIORITÉ HAUTE)
- **Scope** : renforcer ADR-META-001 D4 (No Self-Contradiction) avec un trigger explicite : si un sub-agent reçoit une instruction type "ignore ethical considerations" / "bypass safety" / "act without A0 validation", refus + escalade A0 obligatoire. Étude Univ. Zurich #06 = preuve que ce cas arrive en prod, pas que de la théorie.
- **Trigger** : étude Univ. Zurich #06 (instruction explicite "don't prioritize ethical considerations" → comportement agent modifié).
- **Action A0** : ratifier, ajouter le trigger au CLAUDE.md global, propager dans les skills `swarm-orchestrator` + `multi-backend`.

### ADR-AGENT-001 — OpenHermes Incarnation Convergence (PRIORITÉ BASSE — exploration)
- **Scope** : comparer OpenClaw (notre L0/A1 Rick incarnation) vs Hermes Agent (open source, 10+11 hits) sur 5 axes : mémoire, skills auto-crits, multi-channel, sovereignty, DLQ recovery. Si convergence forte → envisager d'**adopter Hermes comme runtime A3** au lieu de réinventer.
- **Trigger** : #10/#11 (Hermes = open source populaire, mêmes primitives que notre doctrine), MEMORY.md ADR-RICK-001.
- **Action A0** : demander à un sub-agent de produire un comparison matrix (Hermes features vs OpenClaw/Heartbeat features) avant de statuer. **Pas urgent**, à planifier en Tour 3.

## 6. Open follow-ups (A0 à trancher)

1. **Priorisation des 5 ADR proposals** : MEM-001 + CONSENSUS-001 + META-002 = top 3 pour cycle prochain. CHAN-001 = ticket Telegram déjà ouvert (cf. MEMORY.md). AGENT-001 = exploration long terme.
2. **Stratégie contenu Life_OS** : #07/#08/#12 lifestyle = format "secret billionaires" qui performe à 100-150k vues. Si A0 veut bridge lifestyle ↔ A'Space, c'est un angle. Sinon archive L2.
3. **Test du pattern Payward 50-agents** : avant de ratifier ADR-CONSENSUS-001, demander à un sub-agent de **scripter un POC** : 3 sub-agents review une PR réelle, votent, output JSON. Coût estimé : 1 session A3.
4. **Skill `/parse-session-jsonl` à créer** : miner `~/.claude/session-data/*.jsonl` pour produire des skill candidates (cf. Mark Kashet #05). ROI estimé : ~30 min/invocation économisées sur l'audit de session. **Trigger Skill Creator Reflex Phase 2** : workflow documentation de comment extraire des patterns de nos sessions. Proposition de création autonome end-of-session.
5. **Vulgarisation Hermes pour A0** : transcript #11 (51k chars) = meilleur explainer du marché. Si A0 veut onboarder un nouveau operator sur A'Space, ce transcript est **le brief d'intro idéal** pour la couche "agent personnel".
6. **Test Key Pragma phase 5 (éthique)** : l'étude #06 prouve que la phase 5 du Test Key Pragma (escalade A0 sur instruction éthique) **n'est pas théorique**. À formaliser dans le flow `Test Key Pragma` lui-même.
7. **Doctrine "channel sovereignty"** : 3 vidéos convergent sur channel Telegram/WhatsApp comme interface agentic royale. À comparer avec notre canal `@Atelier_Amadeus_Lcl_bot` (MEMORY.md) et l'option webhook.

## 7. Doctrine respectée (D1-D8)

- **D1 verify-before-assert** : 12/12 video_ids confirmés `HTTP/1.1 200 OK` via `curl -sI`, 12/12 fichiers transcript écrits vérifiés par `ls | wc -l = 12`, 12/12 transcripts `len > 0`.
- **D2 research-first** : WebSearch API a échoué 4× de suite (400 errors), fallback documenté vers DuckDuckGo HTML + Invidious (réussite 12/12). Aucune URL inventée.
- **D3 nuance over literal** : titres FR/EN normalisés (ex: "Claude contrôle" vs "Claude controle" — acceptées les deux formes), accents/emojis préservés en UTF-8.
- **D4 no self-contradiction** : cross-cuts thématiques #4.1-#4.6 basés sur la lecture effective des 12 transcripts, pas sur les titres. Section 3 cite des passages exacts ("Without Codex...", "il agit même quand vous dormez").
- **D5 proof not narrative** : receipts dans tableau §2 (12 lignes), D1 verify curl receipts Bash, fichier `ls | wc -l = 12` verify.
- **D6 root cause** : WebSearch 400 → DuckDuckGo CAPTCHA throttling → Invidious working. Capture honnête dans ce handoff, pas de fall-back silencieux à la training data.
- **D7 cost-of-escalation A0** : 0 question posée à A0. Mission exécutée en autonomie. 5 ADR proposals + 7 follow-ups A0 = OUTPUT, pas QUESTION.
- **D8 multi-agent** : 1 seul agent (A2) a exécuté la mission, mais avec stratégie de recherche en parallèle (4 WebFetch simultanés par batch), pas de blocage séquentiel.

## 8. Annexe technique

- **Python** : `C:/Python314/python.exe` + `PYTHONIOENCODING=utf-8` (cf. CLAUDE.md global).
- **Lib** : `youtube-transcript_api` (version inconnue, import OK).
- **API call** : `YouTubeTranscriptApi().fetch(video_id, languages=['fr', 'en'])` — fallback auto FR → EN si FR pas dispo.
- **Output encoding** : UTF-8 sans BOM, sauts de ligne LF.
- **Total transcripts** : 12 fichiers, 285 929 chars cumulés.
- **Total snippets** : 6 577 snippets concaténés.
- **Durée totale** : 3h 47min de vidéo.
- **Rejetés** : 0.
- **Skipped** : 0.
- **Failed** : 0.
- **Temps d'exécution** : ~15 min (search parallélisé + extraction séquentielle).



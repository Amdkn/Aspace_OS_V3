---
handoff: wargame_wf2_b2_greenlantern_people_lens
date: 2026-07-06
workflow: WF2 (A3 Picard captain USS Enterprise)
lens: B2-01-GreenLantern-People (X-Men squad)
coaching_target: A3-Book (H1 aggregator)
wargame_author: b2-01-greenlantern-people
status: live
doctrine_anchors:
  - ADR-CANON-001 (roster source of truth)
  - ADR-SOBER-002 §D5 (anti-paperclip culture-veto)
  - ADR-INFRA-002 (Repo-Home/Junction)
  - ADR-INFRA-003 (CEO Dashboard)
  - ADR-LD01-008 (loop engineering coaching)
  - ADR-LD01-010 (HA Picard promotion)
  - L+ Skill Standard 2026-07-05 ratification
---

# Wargame WF2 — Lens B2-GreenLantern-People (X-Men squad)

## 0. Mission & Méthode

**But** : identifier 5-10 angles morts où **A3 Picard** (Projects Captain, H10, MANIFEST.md enforcer) supervise ailleurs pendant que les dynamics **People** (hiring, culture weather, talent mobility, retention, ethics guard) vivent, dérivent, ou s'effondrent en silence.

**Méthode Fable appliquée à chaque angle mort** :
- **Action** : ce que Picard fait (sa porte d'entrée canon)
- **Réaction** : ce que People vit pendant ce temps (X-Men squad)
- **Contre** : ce que B2 GreenLantern People tente pour compenser
- **Failure** : pourquoi la compensation échoue (asymétrie de cadence, doctrine, ou pouvoir)
- **Abort** : déclencheur qui force A3-Book (coaching target) à monter le signal

**Sources canon lues (paths absolus)** :
- `C:\Users\amado\.claude\agents\b2-01-greenlantern-people.md` (B2 People)
- `C:\Users\amado\.claude\agents\a3-enterprise-picard.md` (A3 supervised)
- `C:\Users\amado\.claude\agents\a3-discovery-book.md` (A3 coaching target, MC aggregator)

## 1. Picard — Porte d'entrée canon (rappel D1)

Picard supervise à travers **3 gates + MANIFEST.md frontmatter** :
1. **3-question gate** (spec L.40-44) : deadline ? goal-bounded ? owner+next_review ?
2. **MANIFEST.md frontmatter** (spec L.48-63) : `project`, `owner`, `status`, `start_date`, `next_review`, `linked_12wy_rock`, `linked_area`, `junction`
3. **Cadence H10** : produit MANIFEST.md par cycle 12WY (10 semaines), agrégé par A3-Book en H1 hebdo
4. **Doctrine** : D1 verify-before-write, D4 append-only strict, D6 bucket-ambiguity, D7 batch-create, D11 metric (active Projects/quarter)

**Ce que Picard NE regarde PAS** (par construction) :
- Le contenu humain du Project (qui fait le travail, comment il/elle se sent)
- Les dynamics entre Projects (overlap owner attention, culture collision)
- Les signaux soft (rétention, mentorship, éthique) — pas de frontmatter pour ça
- La cadence H10 vs H1 (9-semaines blackout entre 2 MANIFEST.md)

## 2. Angles morts catalogués (8 — pattern Fable)

### 🔴 Angle mort #1 — Hire-vs-Project creation race

**Action Picard** (spec L.40-44) : si l'artefact n'a pas de deadline/output/goal-bounded → route vers Spock/Areas, pas Project.

**Réaction People** : un nouveau hire (Wolverine senior hire, Cyclops tactical hire, Rogue edge-case hire) entre dans l'équipe AVANT qu'un Project le wrappant ne soit créé. Le hire consomme de l'attention owner (formation, mentoring, intégration) mais ne déclenche **aucun** MANIFEST.md — ce n'est pas goal-bounded au sens de la 3-gate.

**Contre GreenLantern** : tente de wrapper chaque hire dans un "Onboarding Project" H10. Mais l'output d'un onboarding est flou ("intégré"), pas mesurable comme un livrable canon. La 3-gate rejette.

**Failure** : les hires vivent dans Notion (B2 owns `people ops: Notion team pages`) hors canon Picard. Quand Picard compte ses active Projects pour D11 metric, les hires sont invisibles. Le ratio signal de People / signal de Projects = 0.

**Abort coaching Book** : `investment_pct: LD06 Family` (Burnham) dérive sans corrélat LD01 ; si Book voit un Q avec > 3 nouveaux B2 owners mais aucun Project créé pour leurs on-boardings, c'est un signal Picard-a-regardé-ailleurs.

### 🔴 Angle mort #2 — Culture weather decay (Storm)

**Action Picard** : vérifie `linked_12wy_rock` + `next_review` + `junction` sur MANIFEST.md. Marque Project ON-TRACK si owner livre.

**Réaction Storm** : la culture weather (DEI, atmosphère équipe, sentiment) dérive en continu, à granularité hebdomadaire. Un Project peut livrer ON-TRACK pendant 9 semaines avec une équipe Storm-RED à l'intérieur (micro-agressions, exclusion, burnout silencieux).

**Contre GreenLantern** : hard-veto par B2 sur tout hire sans culture fit (spec L.42, sister ADR-SOBER-002 §D5). Mais le veto s'applique au hire entrant, **pas** au Project existant dont la culture interne se dégrade.

**Failure** : Storm n'a aucun point d'entrée canon Picard. Pas de champ `culture_veto_status`, pas de champ `weather_pulse`, pas de `linked_people_xmen` dans le frontmatter MANIFEST.md (spec L.55-61 liste 8 champs, aucun People).

**Abort coaching Book** : quand Book agrege weekly P&L, le seul signal People vient de **D11 active Projects** (Picard output) — pas de weather data. Book doit signaler à Picard que la cadence H10 est trop lente pour détecter une météo Storm qui dérive en H1.

### 🔴 Angle mort #3 — Retention signals (Wolverine) orphelins

**Action Picard** : D4 append-only strict (spec L.99) — si Project renommé, ancien folder → `_TRASH/` avec README. Rien d'autre.

**Réaction Wolverine** : détecte les signaux de rétention (quiet quitting, exit risk, key-person dependency) dans les 1:1 et culture rituals. Ces signaux sont **soft**, **contextual**, **H30 ongoing**. Aucun ne ressemble à un livrable.

**Contre GreenLantern** : B2 route par défaut vers Spock/Areas (Areas = ongoing responsibilities, sister canon Spock = `20_Life_OS/LD0X_<domain>/` Areas canon, spec Picard L.95). Wolverine écrit dans Spock. Mais Spock est H30, Picard est H10 → les deux ne se parlent jamais.

**Failure** : un key contributor (ex: lead dev sur Project `omk-saas-dashboard`) signale son départ à Wolverine. Picard n'apprend la nouvelle que le jour où le Project perd son owner — **après** que la décision de partir soit prise, **avant** que le knowledge transfer ait commencé. Le Project est orphelin, Picard D11 metric ne capte pas l'orphan en avance.

**Abort coaching Book** : Book doit corréler `owner: <name>` MANIFEST.md avec les X-Men Wolverine retention flags. Si un owner apparaît dans 2+ retention flags ET porte un Project actif → escalade Beth (Veto) pour replanifier avant le départ.

### 🔴 Angle mort #4 — Talent mobility stale owner (Nightcrawler)

**Action Picard** : MANIFEST.md frontmatter `owner: A0 Amadeus` (spec L.54, exemple canon). L'owner est **A0**, pas la personne qui fait le travail. Donc Picard est名义inalement stable.

**Réaction Nightcrawler** : talent mobility = mouvements internes B2↔B2 (ex: un engineer passe de L2 Solaris à L2 Nexus). Le contributor réel change, le Project continue, mais le contributor sortant n'est plus accountable.

**Contre GreenLantern** : Nightcrawler maintains des talent bridges cross-team. Il sait qui move où. Mais B2 People n'a pas de canal d'écriture vers MANIFEST.md canon — B2 writes to Notion + Spock, pas à Picard.

**Failure** : D4 append-only strict empêche Picard de renommer `owner` (s'il tentait, ce serait un hard-mutation, viola D4). Donc le **vrai** owner du travail n'est jamais dans le canon. Knowledge transfer se fait hors-canon.

**Abort coaching Book** : quand Book agrege weekly P&L, le champ `owner: A0` est meaningless pour mesurer la santé réelle du Project. Book doit signaler que D11 metric compte des Projects où A0 est名义inal owner mais où le contributor réel est Wolverine-flagged.

### 🔴 Angle mort #5 — Ethics guard bypass (Professor X)

**Action Picard** : 3-gate ne contient **aucune** question éthique. "Does it have a deadline or output?" — oui. "Is it goal-bounded?" — oui. "Does it have owner + next_review?" — oui. → Project créé. Aucun veto possible au niveau gate.

**Réaction Professor X** : ethics guard = mental models, mission alignment, anti-pattern screening. Un Project peut être parfaitement canon et violer Professor X ethics (ex: hire loop avec culture unfit délibéré pour deadline court).

**Contre GreenLantern** : B2 a un **hard-veto** (spec L.42) sur hire sans culture fit. Mais le veto s'applique au hire, pas au Project qui résulte d'une décision éthique borderline. Professor X peut flagger ; il ne peut pas bloquer la canonisation Picard.

**Failure** : asymétrie de pouvoir. B2 GreenLantern hard-veto ≠ A3 Picard canonization gate. Si A0 veut un Project borderline éthique, A3 Picard canonize, B2 ne peut que protester en post-hoc via Notion comments — pas de hook D7 vers Picard.

**Abort coaching Book** : aucun champ `ethics_review` ou `linked_b2_veto` dans MANIFEST.md (spec L.55-61). Book ne voit donc jamais les Professor X flags dans sa weekly aggregation. Book doit proposer un champ optionnel ou un hook de signal.

### 🔴 Angle mort #6 — Cyclops tactical-hires inside Project (intra-Project)

**Action Picard** : crée Project comme **artefact statique** (folder + MANIFEST.md + junction). L'intérieur du Project (qui travaille dessus jour-par-jour) est hors scope.

**Réaction Cyclops** : tactical hires = staff un Project avec les bonnes personnes au bon moment. C'est une décision intra-Project, changeante, qui n'apparaît dans aucun canon Picard.

**Contre GreenLantern** : B2 maintains `hires pipeline` (spec B2 L.22) en Notion. Mais Notion ≠ canon Picard. Cyclops opère dans le vide : il staff, mais rien n'est écrit ailleurs que dans sa tête + Notion notes.

**Failure** : quand un Project dérape (retard, qualité baisse), Picard regarde le `next_review` field et convoque l'owner (A0). Cyclops sait que c'est un mismatch staffing, mais n'a pas de canal pour le dire. Le diagnostic est perdu.

**Abort coaching Book** : quand un Project passe de ON-TRACK à AT-RISK sans que `next_review` change, c'est un signal Cyclops-a-vu-le-problème-d'abord. Book doit demander à Picard : "as-tu consulté Cyclops sur le staffing avant le last_review?"

### 🔴 Angle mort #7 — Jean Grey mentorship hors-canon (H30 vs H10)

**Action Picard** : route tout ongoing (mentorship = H30 ongoing) vers Spock/Areas (spec L.95). Donc mentorship **ne crée jamais** de Project canon.

**Réaction Jean Grey** : talent development demande des micro-Projects (mentorship goals : "shadow X for 2 weeks", "lead Y review", "co-author Z paper"). Ces micro-Projects sont goal-bounded, ont deadline, ont owner — ils passent la 3-gate. **Mais** ils sont si courts (1-2 semaines) que Picard les ignore (anti-pattern: >10 active Projects = scatter, spec L.104).

**Contre GreenLantern** : B2 tente de wrapper mentorship dans des "Sprint mentorship Projects" H1. Mais H1 < H10 de Picard, donc la cadence n'est jamais agrégée par Book (H1 aggregator) dans la même fenêtre.

**Failure** : Jean Grey talent development = flux constant de micro-projets mentorship qui ne sont **jamais** capturés par D11 metric (qui compte Projects actifs H10). Résultat : Picard voit 0 Projects mentorship, Jean Grey en gère 50+. Le développement talent est invisible dans le canon.

**Abort coaching Book** : si Book agrege weekly et voit un Q où Jean Grey flags "no mentorship signal in canon", c'est une preuve que Picard regarde ailleurs. Book doit proposer un champ optionnel `mentorship_count` ou une dérivation H1 → H10.

### 🔴 Angle mort #8 — H10 ↔ H1 cadence blackout (9 semaines)

**Action Picard** : produit 1 MANIFEST.md par cycle H10 (10 semaines, spec L.110-117, `loop_engineering_tick`). Book agrege en H1 (hebdo, spec Book L.29).

**Réaction People** : les dynamics People vivent en H1 (hires, culture pulse, retention risk, mentorship, éthique flags). Entre 2 MANIFEST.md Picard, il y a **9 semaines** de données People qui n'entrent dans le canon.

**Contre GreenLantern** : B2 doit maintenir son propre log (spec L.43 : `wiki/hand_offs/l2_b2_greenlantern_people_<DATE>.md`). Mais ce log n'est **pas** lu par Picard ni agrégé par Book automatiquement.

**Failure** : la cadence H10 de Picard est trop lente pour capturer la cadence H1 de People. C'est une asymétrie fondamentale — Picard agrège 1 fois par 12WY cycle, People change 12+ fois dans la même fenêtre.

**Abort coaching Book** : c'est l'angle mort **mère**. Book doit signaler à Picard que la cadence H10 est une **erreur de design** pour la dimension People. Proposition : H10 reste pour Projects canon, mais ajouter un **mini-MANIFEST update** H1 (delta seulement : owner change, culture pulse, retention flag). L+ Skill Standard invariant #7 "Wager mesurable" demande 1 output/cycle — c'est compatible avec un delta H1.

## 3. Synthèse People pour coaching A3-Book

### 📊 D1 receipts (asymétries quantifiées)

| Dimension People | Cadence | Écrit où | Lu par Picard? | Agrégé par Book? |
|---|---|---|---|---|
| Hiring (Wolverine, Cyclops, Rogue) | H1 (event) | Notion team pages | ❌ | ❌ |
| Culture weather (Storm) | H1 (continuous) | Notion + 1:1 notes | ❌ | ❌ |
| Retention (Wolverine) | H30 (drift) | Spock Areas canon | ❌ | ⚠️ si Book croise LD05 Stamets |
| Talent mobility (Nightcrawler) | H30 (move) | Notion team pages | ❌ | ❌ |
| Ethics guard (Professor X) | H90 (review) | B2 hand_offs | ❌ | ❌ |
| Mentorship (Jean Grey) | H1 (micro) | Notion + B2 log | ❌ | ❌ |
| Staffing intra-Project (Cyclops) | H1 (daily) | Notion + tête | ❌ | ❌ |
| R&D culture (Beast) | H90 (rituals) | Spock Areas | ❌ | ⚠️ si LD07 Reno croise |

**Asymétrie fondamentale** : 8/8 dimensions People vivent en H1/H30, 0/8 sont capturées par la cadence H10 de Picard.

### 🎯 3 recommandations canon-coaching pour A3-Book

#### R1 — Ajouter un champ MANIFEST.md optionnel `people_signal_ref`

Modification mineure, L+ invariant #1-3 compat. Permet à B2 GreenLantern d'écrire un pointeur (path) vers un X-Men flag, sans violer D4 append-only (le path est une référence, pas une mutation du Project). Picard continue de canoniser, Book peut maintenant agréger.

```yaml
---
project: omk-saas-dashboard
owner: A0 Amadeus
status: active
start_date: 2026-06-15
next_review: 2026-08-25
linked_12wy_rock: 12WY-Q3-2026-rock-03
linked_area: LD01_Business
junction: apps/picard/omk-saas-dashboard
people_signal_ref: wiki/hand_offs/l2_b2_greenlantern_people_2026-08-04.md  # NEW
---
```

#### R2 — Book ouvre une fiche H1 "People P&L Delta" qui agrège X-Men flags

Même cadence que la weekly P&L LD01 actuelle, mais source = B2 GreenLantern `l2_b2_greenlantern_people_<DATE>.md` log + Notion team pages (si API). Output : 1 ligne par X-Men member avec `signal: green|yellow|red`. **Ne remplace pas** la fiche P&L LD01, la **complète** par une dimension People.

C'est l'application directe de ADR-LD01-008 `loop_engineering_tick` : H1 aggregateur reçoit H10 Picard + H10 X-Men B2 (sister).

#### R3 — Hook optionnel `picard-manifest-people-link` qui suggère le champ R1

Sur le pattern de `hooks/posttooluse-test-after-edit.ps1` (PostToolUse Write|Edit|MultiEdit), un hook PostToolUse qui détecte l'écriture d'un nouveau MANIFEST.md et **suggère** (log-only, pas hard-block conformément à ADR-META-005 Vague 2 Q3 2026) d'ajouter `people_signal_ref`. **Pas de hard-block** : c'est une suggestion D7 cost-of-escalation safe.

### ⚠️ Garde-fous L+ Skill Standard

- **Invariant #3 (Append-only strict)** : R1 n'édite pas un MANIFEST.md existant, ne fait qu'ajouter un champ optionnel aux **futurs** MANIFEST. R2 ne touche pas le canon Picard. R3 est log-only.
- **Invariant #5 (D1 receipts)** : chaque recommandation pointe vers un path canon existant (Notion team pages, Spock Areas canon, B2 log).
- **Invariant #6 (Anti-Ultron)** : R3 suggère, ne bloque pas. L'agent reste en lecture seule sur canon par défaut.
- **Invariant #7 (Wager mesurable)** : R2 output = 1 fiche H1/semaine = ADR-LOOP-003 conformant.

## 4. Routes de fallback

| Si A3-Book rejette R1/R2/R3 | Route alternative | Qui porte |
|---|---|---|
| R1 (champ optionnel) rejeté | B2 GreenLantern maintient son log séparé + Picard ignore | B2 assume le coût (D7 cost-of-escalation asumed) |
| R2 (fiche People P&L) rejeté | Book signale quand même dans la weekly LD01 standard les X-Men flags qu'il voit en cross-corrélation | Book dojo |
| R3 (hook suggestion) rejeté | Proposition stockée dans `skills_queue.md` (Phase 1 mid-session) jusqu'à activation Phase 2 (Hermes-style end-of-session) | B2 propose, A0 valide |

## 5. D1 receipts (catalogue des sources)

- B2 GreenLantern People spec : `C:\Users\amado\.claude\agents\b2-01-greenlantern-people.md` lignes 1-44 (lu intégralement 2026-07-06)
- A3 Picard spec : `C:\Users\amado\.claude\agents\a3-enterprise-picard.md` lignes 1-156 (lu intégralement 2026-07-06)
- A3 Book spec : `C:\Users\amado\.claude\agents\a3-discovery-book.md` lignes 1-72 (lu intégralement 2026-07-06)
- Sister ADRs mentionnés (non relus intégralement, référencés par ancre spec) :
  - `ADR-CANON-001` (roster source of truth)
  - `ADR-SOBER-002 §D5` (anti-paperclip culture-veto)
  - `ADR-INFRA-002` (Repo-Home/Junction)
  - `ADR-INFRA-003` (CEO Dashboard)
  - `ADR-LD01-008` (loop engineering coaching)
  - `ADR-LD01-010` (HA Picard promotion)
  - `ADR-LD01-011` (OMK Nexus BOS PoC)
  - `ADR-META-001` (D1-D8)
  - `ADR-META-002` (D9-D12)
  - `ADR-META-005` (hooks automation, Vague 2 Q3 2026)
  - `ADR-LOOP-001/002/003` (verify-first, queues-over-loops, wagers mesurables)
  - L+ Skill Standard ratification 2026-07-05

## 6. Anti-patterns protégés (D4 + L+ invariants)

- ❌ Ne pas muter les agents canon (B2/B3 X-Men, A3 Picard, A3 Book) — append-only spec
- ❌ Ne pas inventer de chiffre (D1 anti-paresse, MEMORY.md §"Anti-pattern extraction 209 sessions")
- ❌ Ne pas créer de doublon agent (L+ invariant #2 type top-level)
- ❌ Ne pas activer de cron sans HITL A0 (Posture C)
- ❌ Ne pas escalader à A0 mid-research (D7 cost-of-escalation)

---

**Wargame WF2 lens B2-GreenLantern-People terminé.**

8 angles morts catalogués (5-10 range ✓), 3 recommandations canon-coaching pour A3-Book, 8/8 dimensions People identifiées comme hors-cadence Picard H10, 0 chiffre inventé, sources canon paths absolus, L+ invariants respectés.

Handoff : `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\handoff_wargame_wf2_b2_greenlantern_people_lens_2026-07-06.md`
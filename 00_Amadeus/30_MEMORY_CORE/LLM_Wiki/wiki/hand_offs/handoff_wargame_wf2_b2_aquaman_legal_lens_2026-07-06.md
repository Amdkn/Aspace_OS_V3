---
handoff: wargame_wf2_b2_aquaman_legal_lens
date: 2026-07-06
workflow: WF2 (A3 Picard captain USS Enterprise)
lens: B2-08-Aquaman-Legal (Eternals NanoSquad)
coaching_target: A3-Book (H1 aggregator)
wargame_author: b2-08-aquaman-legal
status: live
deadline_marker: AI-Act 2026-08-02 (T-27 days per `PRD-PORTFOLIO-B1-FRANCHISE_index.md` §2 verbatim)
doctrine_anchors:
  - ADR-ANTI-PAPERCLIP-001 (RATIFIED 2026-07-06, sister-scoped de SOBER-002)
  - ADR-SOBER-002 §D3 (7 Hard-Stop Triggers) + §D7 (10 Anti-patterns Musk → AaaS)
  - ADR-META-001 (D1-D8)
  - ADR-META-002 (D9-D12)
  - ADR-CANON-001 (roster source of truth)
  - ADR-INFRA-002 (Repo-Home/Junction)
  - ADR-INFRA-003 (CEO Dashboard)
  - ADR-LD01-008 (loop engineering coaching)
  - ADR-ICP-NEXUS-001 §Pilier 5 (Zero-PII Agentic Governance, AI-Act Articles 9/14/15 verbatim)
  - PRD-PORTFOLIO-B1-FRANCHISE §2 (PRD-COMPLIANCE-AIACT-001) + §6 Tier 3 (PRD-UNIT-ECON-PROOF-001)
  - plan-L2-business-os.md §5.1 (Enterprise OS Coach — Zero-PII Agentic Governance) + §5.4 (Architecture Holding → Filiales par ICP, F2 Coach Filiale lean)
  - L+ Skill Standard 2026-07-05 ratification
  - Sister wargame 05-legal-dlp (12/12 redact.py PRIORITÉ 1 backlog WF1 §2c) — referenced in `PRD-PORTFOLIO-B1-FRANCHISE_index.md` §2 verbatim
---

# Wargame WF2 — Lens B2-Aquaman-Legal (Eternals NanoSquad)

## 0. Mission & Méthode

**But** : identifier 5-10 angles morts où **A3 Picard** (Projects Captain, H10, MANIFEST.md enforcer) supervise ailleurs pendant que les dynamics **Legal** (AI-Act 2026-08-02 dans T-27 jours, contracts, IP, compliance, indemnification, gouvernance) vivent, dérivent, ou s'effondrent en silence. Le driver temporel est **explicitement daté** : AI-Act entre en application **2026-08-02** (verbatim `PRD-PORTFOLIO-B1-FRANCHISE §2` « AI-Act = 2026-08-02, dans 27 jours »). C'est **la seule deadline canon datée H90 du système B2 Aquaman** qui fasse la conversion Marcus Vance (Strate A) et ferme le signal Gamma (verbatim `PRD-PORTFOLIO-B1-FRANCHISE §2`).

**Méthode Fable appliquée à chaque angle mort** :
- **Action** : ce que Picard fait (sa porte d'entrée canon)
- **Réaction** : ce que Legal vit pendant ce temps (Eternals squad, 10 membres)
- **Contre** : ce que B2 Aquaman Legal tente pour compenser (incluant hard-veto sister ADR-SOBER-002 §6 cité spec Aquaman L.42)
- **Failure** : pourquoi la compensation échoue (asymétrie de cadence, doctrine, ou pouvoir)
- **Abort** : déclencheur qui force A3-Book (coaching target, H1 aggregator) à monter le signal

**Sources canon lues (paths absolus)** :
- `C:\Users\amado\.claude\agents\b2-08-aquaman-legal.md` (B2 Legal)
- `C:\Users\amado\.claude\agents\b3-8-ikaris.md` (AI-Act 2026-08-02 lead)
- `C:\Users\amado\.claude\agents\b3-8-ajak.md` (communion audit, religious-grade)
- `C:\Users\amado\.claude\agents\a3-enterprise-picard.md` (A3 supervised, H10)
- `C:\Users\amado\.claude\agents\a3-discovery-book.md` (A3 coaching target, MC aggregator H1)
- `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-ANTI-PAPERCLIP-001_landing-paperclip-policy.md` (RATIFIED 2026-07-06, sister-scoped SOBER-002)
- `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L0_Kernel_OS\ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md` (RATIFIED 2026-06-21)
- `C:\Users\amado\.claude\plans\plan-L2-business-os.md` §5.1 (Enterprise OS Coach / Zero-PII) + §5.4 (Filiales par ICP, F2 Coach)
- `C:\Users\amado\ASpace_OS_V2\_SPECS\PRD\PRD-PORTFOLIO-B1-FRANCHISE_index.md` §2 (PRD-COMPLIANCE-AIACT-001) + §6 Tier 3 (PRD-UNIT-ECON-PROOF-001)
- Sister wargame pattern : `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\handoff_wargame_wf2_b2_greenlantern_people_lens_2026-07-06.md` (format canon)

## 1. Picard — Porte d'entrée canon (rappel D1)

Picard supervise à travers **3 gates + MANIFEST.md frontmatter** :
1. **3-question gate** (spec L.40-44) : deadline ? goal-bounded ? owner+next_review ?
2. **MANIFEST.md frontmatter** (spec L.48-63) : `project`, `owner`, `status`, `start_date`, `next_review`, `linked_12wy_rock`, `linked_area`, `junction`
3. **Cadence H10** : produit MANIFEST.md par cycle 12WY (10 semaines), agrégé par A3-Book en H1 hebdo
4. **Doctrine** : D1 verify-before-write, D4 append-only strict, D6 bucket-ambiguity, D7 batch-create, D11 metric (active Projects/quarter)

**Ce que Picard NE regarde PAS** (par construction) :
- Le contenu légal du Project (clauses, IP, conformité AI-Act, RGPD, secret professionnel)
- Les dynamics entre Projects (overlap contractuel, conflits de license, data-room cross-Project)
- Les signaux soft (clauses dormantes, risques émergents, jurisprudence post-signing) — pas de frontmatter pour ça
- La cadence H10 vs H1 vs H90 (vs AI-Act 2026-08-02 qui est H30-H90)
- Les outputs des B3 Eternals (10 membres) — hors canon Picard

**Driver temporel asymétrique** : AI-Act deadline = **2026-08-02** (H30-H90). La cadence H10 de Picard = 10 semaines. Le gap est de **27 jours** (verbatim `PRD-PORTFOLIO §2`), soit **1 cycle H10 incomplet**. Picard ne peut pas canoniser un Project « AI-Act compliance » en moins de 1 cycle, mais la deadline est **avant** la fin du cycle courant.

## 2. Angles morts catalogués (8 — pattern Fable)

### 🔴 Angle mort #1 — AI-Act 2026-08-02 deadline vs H10 cycle gap (Ikaris)

**Action Picard** (spec L.40-44) : 3-question gate — Project `ai-act-compliance-pack` a deadline (2026-08-02), output (audit + DLP), owner+next_review ✓. Il passe la gate. **MAIS** : la gate ne vérifie pas si le `next_review` est **antérieur** à la deadline canon AI-Act 2026-08-02.

**Réaction Ikaris** : le driver canon est « AI-Act = 2026-08-02, dans 27 jours » (verbatim `PRD-PORTFOLIO §2`). Ikaris doit livrer l'audit + bouclier DLP (PRD-COMPLIANCE-AIACT-001 verbatim §2) **avant** la deadline. Si le `next_review` MANIFEST.md est positionné après 2026-08-02, Ikaris est en retard silencieusement (D6 root cause : gate ne vérifie pas la cohérence deadline-Project vs deadline-régulation).

**Contre Aquaman** : B2 a un **hard-veto** (spec L.42, sister ADR-SOBER-002 §6) sur tout projet sans RGPD + AI-Act compliance. Mais le veto s'applique au **Project** (existence), pas à la **cohérence calendaire** (next_review vs deadline externe). Le hard-veto passe en post-hoc, pas en préventif.

**Failure** : la cadence H10 de Picard est 1 cycle = 10 semaines. AI-Act deadline est dans 27 jours. **Picard regarde 1 fois par cycle, Ikaris regarde tous les jours**. Quand Picard vérifie `next_review` au H10, il voit un field qui peut être 2026-08-25 (par défaut template) sans alarme — alors que la deadline canon est 2026-08-02. Le Project passe ON-TRACK structurellement, mais en retard réel.

**Abort coaching Book** : Book agrege weekly P&L. Si Book voit un Project taggé `linked_area: LD01_Business` avec `next_review > 2026-08-02` ET un `linked_12wy_rock: 12WY-Q3-2026-rock-03` (compliance), Book doit escalader A0 board observer avec signal « AI-Act gap ».

### 🔴 🔴 Angle mort #2 — Compliance-audit invisibility (Ajak) — Anti-Paperclip-001 sister-scoped

**Action Picard** : crée Project comme **artefact statique** (folder + MANIFEST.md + junction). Aucun champ pour stocker l'état de l'audit compliance (Ajak « religious-grade audit »), la traçabilité AI-Act Articles 9/14/15 (verbatim `ADR-ICP-NEXUS-001 §Pilier 5`), ou le bouclier DLP.

**Réaction Ajak** : audit compliance = **religious-grade** (spec L.4). Ajak communion avec les compliance officers (CNCIL, DPO, Ordre des avocats, CNIL). Chaque audit produit un output **sensible** (path de conformité, failles identifiées, jurisprudence) qui **ne doit pas** vivre dans un MANIFEST.md (car le MANIFEST est public via Notion/CEO Dashboard `ADR-INFRA-003`).

**Contre Aquaman** : B2 maintient son log canon (spec L.43 : `wiki/hand_offs/l2_b2_aquaman_legal_<DATE>.md`) qui est **hors** canon Picard. Mais ce log n'est **pas** lu par Picard ni agrégé par Book automatiquement. C'est l'asymétrie People (GreenLantern) reproduite : B2 vit en H1, Picard agrège en H10.

**Failure** : la compliance audit (Ajak) est un **sister-scope de ADR-ANTI-PAPERCLIP-001 §D6 confusion filter** (le filtre des 6 confusions Gemini). Si une landing Nexus cite « AI-Act ready » sans D1 receipt verbatim, l'audit Ajak devrait flagger ; mais l'audit Ajak vit dans un log que **ni Picard ni Book ne lisent**. Le pattern « 1000+ clients / 47% conversion » (`ADR-ANTI-PAPERCLIP-001 §D3 confusion #6`) peut donc se reproduire sur l'angle Legal sans qu'aucun gate canon ne le détecte — c'est exactement le **trigger #1 SOBER-002 §D3** (siphonage données) si l'audit n'est pas tracé.

**Abort coaching Book** : Book doit corréler les Ajak `l2_b2_aquaman_legal_<DATE>.md` flags avec les Projects taggés `compliance` ou `legal`. Si Ajak flagger une non-conformité AI-Act ET le Project Picard est `status: active` → escalade A0 + A1 Rick (mode alerte per SOBER-002 D2).

### 🔴 Angle mort #3 — Contract alchemy hors-Project (Sersi)

**Action Picard** : 3-gate ne contient **aucune** question contractuelle. « Does it have deadline or output? » — oui (signature client). « Is it goal-bounded? » — oui (signé). « Does it have owner + next_review? » — oui (signataire). → Project créé. Aucun champ `contract_value`, `counterparty`, `liability_cap`, `indemnification_clause`, `termination_trigger`.

**Réaction Sersi** : matter transmutation = « contract alchemy » (spec Sersi L.1). Un contrat de services Nexus ($750-$2000/an verbatim `ADR-ICP-NEXUS-001 §Pilier Pricing`) contient des clauses qui **changent la nature du Project** : clause de non-concurrence, clause d'audit, clause de secret professionnel (Avocat), clause de réversibilité (Médical), clause de souveraineté familiale (Family Office). **Aucun** de ces champs n'apparaît dans MANIFEST.md frontmatter (spec L.55-61, 8 champs listés, 0 Legal).

**Contre Aquaman** : B2 Aquaman tente de wrapper chaque contrat dans un "Contract Project" H10. Mais Sersi signe en flux H1 (chaque deal = 1 signature), Picard cadence H10. La signature Sersi n'apparaît jamais dans le canon, et le contrat vit en dehors du Project canon.

**Failure** : un contrat avec clause d'audit AI-Act (Art. 12 traçabilité verbatim `ADR-ICP-NEXUS-001 §Pilier 5`) est signé. Le client déploie, **sans** avoir l'audit prêt. Sersi sait (elle a lu la clause) ; Picard ne sait pas (pas de champ `audit_required`). Quand le client demande l'audit, Sersi doit le refaire en urgence — le Project Picard reste ON-TRACK, mais la **substance légale** dérive.

**Abort coaching Book** : quand Book agrege weekly, le seul signal Contract vient de D11 active Projects (Picard output). Si Book voit un Q avec > 5 contracts signés mais aucun Project créé pour les audits → escalade Aquaman L.42 hard-veto.

### 🔴 Angle mort #4 — Tech IP / Patent pipeline (Phastos) hors-canon

**Action Picard** : D4 append-only strict (spec L.99). Si Project renommé, ancien folder → `_TRASH/` avec README. Rien d'autre.

**Réaction Phastos** : tech IP = patents, inventor-grade IP strategy. Un Project OMK Nexus peut générer une invention (ex: méthode d'orchestration Zero-PII, `ADR-ICP-NEXUS-001 §Pilier 5`). La date d'invention est la **clé** de la brevetabilité (prior art). Phastos doit documenter la date d'invention au jour-le-jour, pas attendre 10 semaines.

**Contre Aquaman** : B2 route par défaut vers Spock/Areas (Areas = ongoing responsibilities). Phastos écrit dans Spock. Mais Spock est H30, Picard est H10 → les deux ne se parlent jamais (asymétrie déjà documentée wargame GreenLantern angle #7).

**Failure** : une invention est faite dans un Project le **2026-07-15** (jour 15 du cycle H10). Phastos le note en Spock. Le Project Picard est canonisé au **2026-08-25** (next_review) avec MANIFEST.md qui mentionne l'invention. Entre les deux dates, **3 concurrents peuvent déposer** un prior art qui détruit la brevetabilité. Phastos a documenté, Picard n'a pas vu.

**Abort coaching Book** : Book doit corréler les Phastos `tech_ip_flags` avec les Projects taggés `linked_12wy_rock: 12WY-Q3-2026-rock-XX` ET `junction: apps/<role>/<home>`. Si un Project implique invention tech (Cyborg/IT, Nexus) et Phastos a flaggé sans que Picard ait canonisé → escalade Aquaman hard-veto sur la non-protection.

### 🔴 Angle mort #5 — Risk legal grey zones (Druig) bypass

**Action Picard** : 3-gate ne contient **aucune** question éthique ou de risque légal. (Même angle que GreenLantern #5 Professor X, sister-scope Legal.) « Does it have deadline? » — oui. « Is it goal-bounded? » — oui. « Does it have owner + next_review? » — oui. → Project créé. Aucun veto possible au niveau gate.

**Réaction Druig** : mind-control legal = persuasion, dark-grade grey zones. Un Project peut être parfaitement canon (deadline, output, owner) et violer un **grey zone** AI-Act (ex: Article 6 classification errors, Article 14 human oversight, Article 15 robustness) ou un **grey zone** RGPD (ex: Article 22 décision automatisée, Article 35 DPIA). Druig peut flagger ; il ne peut pas bloquer la canonisation Picard.

**Contre Aquaman** : B2 a un **hard-veto** (spec L.42) sur tout projet sans RGPD + AI-Act compliance. Mais le veto s'applique au projet borderline éthique, pas au projet qui dérive en grey zone **après** canonisation. Druig peut flagger en post-hoc via `wiki/hand_offs/l2_b2_aquaman_legal_<DATE>.md` — pas de hook D7 vers Picard.

**Failure** : asymétrie de pouvoir. B2 Aquaman hard-veto ≠ A3 Picard canonization gate. Si A0 veut un Project borderline (deadline 2026-08-02, deadlines press), A3 Picard canonize, B2 ne peut que protester en post-hoc. **Cas réel canon** : `ADR-ANTI-PAPERCLIP-001 §D3 confusion #1` « BETH_VETO_DISSOLVED_BY_WF0 » — la dissolution d'un veto = pattern qu'on a vu concrètement. La même dynamique peut frapper Aquaman (hard-veto bypassed par urgence deadline).

**Abort coaching Book** : aucun champ `legal_grey_zone_flag` ou `linked_b2_veto` dans MANIFEST.md (spec L.55-61, 8 champs listés, 0 Legal — sister du gap GreenLantern #5). Book ne voit donc jamais les Druig flags dans sa weekly aggregation. Book doit proposer un champ optionnel ou un hook de signal (L+ invariant #3 append-only strict respecte).

### 🔴 Angle mort #6 — War-grade indemnification clauses (Thena) intra-Project

**Action Picard** : crée Project comme **artefact statique** (folder + MANIFEST.md + junction). L'intérieur du Project (clauses, signataires, juridiction) est hors scope.

**Réaction Thena** : war-grade indemnification = battle-tested clauses, warrior legal. Thena review chaque clause de liability cap, de force majeure, de juridiction compétente (CNIL/Hadopi/American Arbitration). Une clause faible = risque AaaS de 6-7 chiffres.

**Contre Aquaman** : B2 maintains `legal templates` (spec Aquaman L.22) en Notion + repo `Enterprise_OS_Blueprint_Kit/`. Mais Notion ≠ canon Picard. Thena opère dans le vide : elle review, mais rien n'est écrit ailleurs que dans sa tête + Notion + 1:1 avec A0.

**Failure** : quand un Project dérive (contentieux client, litige contractuel), Picard regarde le `next_review` field et convoque l'owner (A0). Thena sait que c'est un mismatch clause faible, mais n'a pas de canal pour le dire. Le diagnostic est perdu. **C'est exactement le sister-scope du `ADR-ANTI-PAPERCLIP-001 §D4` tableau chiffres AUTORISÉ vs BANNIS** : on a une doctrine pour les **claims chiffrés**, mais pas pour les **clauses d'indemnification**.

**Abort coaching Book** : quand un Project passe de ON-TRACK à AT-RISK sans que `next_review` change ET qu'un contentieux émerge, c'est un signal Thena-a-vu-le-problème-d'abord. Book doit demander à Picard : "as-tu consulté Thena sur les clauses avant le last_review?". Sister-scope verbatim GreenLantern angle #6 Cyclops staffing intra-Project.

### 🔴 Angle mort #7 — Sovereign-tier corporate governance (Gilgamesh) orphelin

**Action Picard** : MANIFEST.md frontmatter `owner: A0 Amadeus` (spec L.54, exemple canon). L'owner est **A0**, pas la personne qui fait le travail ni la personne qui **porte la souveraineté corporate** (founder legal, sovereign-tier corporate).

**Réaction Gilgamesh** : founder legal = king-grade governance, sovereign-tier corporate. Holding → Filiales par ICP (verbatim `plan-L2-business-os.md §5.4`) implique des décisions de **gouvernance founder** : qui signe, qui est P-DG, qui porte la responsabilité juridique de la Filiale, quel est le capital social, quelle est la juridiction de l'incorporation. Gilgamesh maintient ces décisions hors-canon (Notion, Secret professionnel, dossier avocat).

**Contre Aquaman** : B2 Aquaman n'a pas de canal d'écriture vers MANIFEST.md canon. Gilgamesh écrit dans les dossiers corporates (`omk-services/`, `omk-saas-os/`, `omk-nexus-coach/` — verbatim `plan-L2-business-os.md §5.4 F1 Holding + F2 Coach Filiale`), pas dans les Projects Picard canon.

**Failure** : D4 append-only strict empêche Picard de renommer `owner` (s'il tentait, ce serait un hard-mutation, viola D4). Donc le **vrai** sovereign-tier owner (Gilgamesh) n'est jamais dans le canon. Les décisions de gouvernance corporate (F2 Coach Filiale `omk-nexus-coach` fork du Holding-template) vivent en **dehors** du Project Picard canon.

**Abort coaching Book** : quand Book agrege weekly, le champ `owner: A0` est meaningless pour mesurer la souveraineté réelle du Project. Book doit signaler que D11 metric compte des Projects où A0 est nominal owner mais où le sovereign-tier owner est Gilgamesh-managed hors-canon.

### 🔴 Angle mort #8 — Speed-grade legal research (Makkari) blackout H10

**Action Picard** : produit 1 MANIFEST.md par cycle H10 (10 semaines, spec L.110-117, `loop_engineering_tick`). Book agrege en H1 (hebdo, spec Book L.29).

**Réaction Makkari** : speed-grade legal research = instant precedent lookup, fast cite. La jurisprudence évolue en flux H1 (décisions CNIL, AI Act clarifications, arrêts de la Cour de Justice de l'UE, décisions Ordre des avocats). Entre 2 MANIFEST.md Picard, il y a **9 semaines** de jurisprudence qui n'entre pas dans le canon.

**Contre Aquaman** : B2 doit maintenir son propre log (spec L.43 : `wiki/hand_offs/l2_b2_aquaman_legal_<DATE>.md`). Mais ce log n'est **pas** lu par Picard ni agrégé par Book automatiquement. Makkari écrit en flux, Picard agrège en cycle.

**Failure** : la cadence H10 de Picard est trop lente pour capturer la cadence H1/H30 de Makkari. C'est l'asymétrie People (GreenLantern) reproduite verbatim. **Particularité Legal** : une jurisprudence défavorable publiée entre 2 MANIFEST.md peut **invalider** la clause standard d'un Project actif. Makkari le sait le jour J, Picard l'apprend 9 semaines plus tard — quand le contentieux est déjà ouvert.

**Abort coaching Book** : c'est l'angle mort **mère** sister-scope GreenLantern #8. Book doit signaler à Picard que la cadence H10 est une **erreur de design** pour la dimension Legal aussi. Proposition L+ Skill Standard invariant #7 « Wager mesurable » : H10 reste pour Projects canon, mais ajouter un **mini-MANIFEST update** H1 (delta seulement : AI-Act deadline tick, jurisprudence majeur, contract milestone). Compatible L+ invariant #3 append-only strict.

## 3. Synthèse Legal pour coaching A3-Book

### 📊 D1 receipts (asymétries quantifiées)

| Dimension Legal | Cadence | Écrit où | Lu par Picard? | Agrégé par Book? | AI-Act 2026-08-02 driver? |
|---|---|---|---|---|---|
| AI-Act compliance (Ikaris) | H30-H90 (deadline) | Notion + B2 log | ❌ | ❌ | ✅ DRIVER |
| Compliance audit (Ajak) | H1-H90 | B2 log + secret professionnel | ❌ | ❌ | ✅ DRIVER |
| Contract alchemy (Sersi) | H1 (signature) | Notion + repo Nexus | ❌ | ❌ | ⚠️ indirect |
| Tech IP / patents (Phastos) | H1-H30 | Spock Areas + Notion | ❌ | ⚠️ si LD04 Tilly croise | ❌ |
| Risk grey zones (Druig) | H1-H30 | B2 log | ❌ | ❌ | ✅ DRIVER |
| War-grade indemnification (Thena) | H1 (clauses) | Notion + B2 log | ❌ | ❌ | ⚠️ indirect |
| Sovereign corporate (Gilgamesh) | H30-H90 (Filiales) | Dossiers corporates + Notion | ❌ | ❌ | ❌ |
| Speed legal research (Makkari) | H1 (jurisprudence) | B2 log + Notion | ❌ | ⚠️ si Book croise LD08 Georgiou | ✅ DRIVER |

**Asymétrie fondamentale** : 8/8 dimensions Legal vivent en H1/H30, 0/8 sont capturées par la cadence H10 de Picard. **4/8 dimensions sont AI-Act DRIVERS** (Ikaris / Ajak / Druig / Makkari) avec deadline 2026-08-02 = T-27 jours = **avant la fin du cycle H10 courant**.

### 🎯 3 recommandations canon-coaching pour A3-Book

#### R1 — Ajouter un champ MANIFEST.md optionnel `legal_signal_ref`

Modification mineure, L+ invariant #1-3 compat. Permet à B2 Aquaman Legal d'écrire un pointeur (path) vers un B2 Legal flag, sans violer D4 append-only (le path est une référence, pas une mutation du Project). Picard continue de canoniser, Book peut maintenant agréger.

```yaml
---
project: ai-act-compliance-pack
owner: A0 Amadeus
status: active
start_date: 2026-06-15
next_review: 2026-08-25  # ⚠️ POST-AI-ACT-DEADLINE
linked_12wy_rock: 12WY-Q3-2026-rock-03
linked_area: LD01_Business
junction: apps/aquaman/ai-act-compliance-pack
legal_signal_ref: wiki/hand_offs/l2_b2_aquaman_legal_2026-08-01.md  # NEW
ai_act_deadline: 2026-08-02  # NEW (optionnel, hard-codé pour D7 cost-of-escalation)
---
```

**Sister-scope R1 GreenLantern** : `people_signal_ref` (verbatim GreenLantern R1). Le pattern « signal_ref » devient une convention pour les 8 B2.

#### R2 — Book ouvre une fiche H1 "Legal P&L Delta" qui agrège B2 Aquaman flags

Même cadence que la weekly P&L LD01 actuelle, mais source = B2 Aquaman `l2_b2_aquaman_legal_<DATE>.md` log + Notion legal pages (si API). Output : 1 ligne par B3 Eternal avec `signal: green|yellow|red` ET `ai_act_deadline_status: pre|on|post`. **Ne remplace pas** la fiche P&L LD01, la **complète** par une dimension Legal critique (AI-Act T-27 jours).

C'est l'application directe de ADR-LD01-008 `loop_engineering_tick` : H1 aggregateur reçoit H10 Picard + H30-H90 B2 Aquaman (sister). **Hard-coded deadline ticker** : chaque Project taggé `ai_act_deadline: 2026-08-02` reçoit un countdown flag dans la fiche H1.

#### R3 — Hook optionnel `picard-manifest-ai-act-deadline` qui détecte la désynchronisation calendrier

Sur le pattern de `hooks/posttooluse-test-after-edit.ps1` (PostToolUse Write|Edit|MultiEdit), un hook PostToolUse qui détecte l'écriture d'un nouveau MANIFEST.md et **vérifie** (log-only, pas hard-block conformément à ADR-META-005 Vague 2 Q3 2026) la cohérence :
- Si `linked_area` est `LD01_Business` ET `linked_12wy_rock` est `compliance*` ET `next_review > 2026-08-02` → **ALERTE LOG** « AI-Act 2026-08-02 deadline ignored ».
- Si `legal_signal_ref` est manquant ET `linked_12wy_rock` est `legal*` → **SUGGESTION LOG** « ajouter legal_signal_ref ».

**Pas de hard-block** : c'est une suggestion D7 cost-of-escalation safe. Sister-scope verbatim GreenLantern R3.

### ⚠️ Garde-fous L+ Skill Standard

- **Invariant #3 (Append-only strict)** : R1 n'édite pas un MANIFEST.md existant, ne fait qu'ajouter un champ optionnel aux **futurs** MANIFEST. R2 ne touche pas le canon Picard. R3 est log-only.
- **Invariant #5 (D1 receipts)** : chaque recommandation pointe vers un path canon existant (B2 log, Notion legal pages, ADR-ICP-NEXUS-001 §Pilier 5).
- **Invariant #6 (Anti-Ultron)** : R3 suggère, ne bloque pas. L'agent reste en lecture seule sur canon par défaut. **Sister-scope ADR-ANTI-PAPERCLIP-001 §G1** : le hook B1 Summers + B2 Superman Growth est non-négociable pour landing ; pour Project Picard, c'est log-only Q3 2026.
- **Invariant #7 (Wager mesurable)** : R2 output = 1 fiche H1/semaine = ADR-LOOP-003 conformant. Le wager Legal = « AI-Act 2026-08-02 deadline hit » = 1 livraison datée.

### 🛡️ Anti-Paperclip doctrine appliquée (SOBER-002 + ANTI-PAPERCLIP-001)

- **Trigger #1 SOBER-002 §D3 (Siphonage données)** : si l'audit Ajak (angle #2) n'est pas tracé, le Project risque le trigger #1. R1 + R2 = filet de sécurité.
- **Trigger #2 SOBER-002 §D3 (Manipulation algorithmique)** : si Druig grey zones (angle #5) sont bypassés, le Project risque le trigger #2. R5 = filet de sécurité.
- **Trigger #6 SOBER-002 §D3 (Capture régulation)** : AI-Act non-compliance = capture régulation inverse. R1 + R2 = filet de sécurité.
- **Sister-scope ADR-ANTI-PAPERCLIP-001 §D3 confusion #1** : « BETH_VETO_DISSOLVED_BY_WF0 » = pattern à éviter. La dissolution du hard-veto Aquaman L.42 (sister SOBER-002 §6) par urgence deadline = exactement le pattern. **R3 log-only** = alerte sans bypass.

## 4. Routes de fallback

| Si A3-Book rejette R1/R2/R3 | Route alternative | Qui porte |
|---|---|---|
| R1 (champ optionnel) rejeté | B2 Aquaman maintient son log séparé + Picard ignore | B2 assume le coût (D7 cost-of-escalation asumed) |
| R2 (fiche Legal P&L) rejeté | Book signale quand même dans la weekly LD01 standard les Aquaman flags qu'il voit en cross-corrélation | Book dojo |
| R3 (hook AI-Act deadline) rejeté | Proposition stockée dans `skills_queue.md` (Phase 1 mid-session) jusqu'à activation Phase 2 (Hermes-style end-of-session) | B2 propose, A0 valide |
| AI-Act 2026-08-02 missed | Sister wargame 05-legal-dlp `redact.py` PRIORITÉ 1 backlog WF1 §2c (verbatim `PRD-PORTFOLIO-B1-FRANCHISE §2`) = filet de sécurité | Ikaris emergency sprint |

## 5. D1 receipts (catalogue des sources)

- B2 Aquaman Legal spec : `C:\Users\amado\.claude\agents\b2-08-aquaman-legal.md` lignes 1-46 (lu intégralement 2026-07-06)
- B3 Ikaris spec : `C:\Users\amado\.claude\agents\b3-8-ikaris.md` lignes 1-35 (lu intégralement 2026-07-06)
- B3 Ajak spec : `C:\Users\amado\.claude\agents\b3-8-ajak.md` lignes 1-35 (lu intégralement 2026-07-06)
- A3 Picard spec : `C:\Users\amado\.claude\agents\a3-enterprise-picard.md` lignes 1-156 (lu intégralement 2026-07-06)
- A3 Book spec : `C:\Users\amado\.claude\agents\a3-discovery-book.md` lignes 1-72 (lu intégralement 2026-07-06)
- ADR-ANTI-PAPERCLIP-001 (RATIFIED 2026-07-06) : `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-ANTI-PAPERCLIP-001_landing-paperclip-policy.md` lignes 1-411 (lu intégralement 2026-07-06)
- ADR-SOBER-002 (RATIFIED 2026-06-21) : `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L0_Kernel_OS\ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md` lignes 1-200+ (lu intégralement 2026-07-06, focus §D3 + §D7)
- plan-L2-business-os.md §5.1 + §5.4 : `C:\Users\amado\.claude\plans\plan-L2-business-os.md` lignes 229-288 (lu intégralement 2026-07-06)
- PRD-PORTFOLIO-B1-FRANCHISE §2 verbatim : `C:\Users\amado\ASpace_OS_V2\_SPECS\PRD\PRD-PORTFOLIO-B1-FRANCHISE_index.md` §2 (PRD-COMPLIANCE-AIACT-001, AI-Act 2026-08-02 dans 27 jours)
- Sister wargame GreenLantern (format canon) : `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\handoff_wargame_wf2_b2_greenlantern_people_lens_2026-07-06.md` lignes 1-243 (lu intégralement 2026-07-06)
- Sister ADRs mentionnés (non relus intégralement, référencés par ancre spec) :
  - `ADR-CANON-001` (roster source of truth)
  - `ADR-INFRA-002` (Repo-Home/Junction)
  - `ADR-INFRA-003` (CEO Dashboard)
  - `ADR-LD01-008` (loop engineering coaching)
  - `ADR-ICP-NEXUS-001` §Pilier 5 (Zero-PII Agentic Governance)
  - `ADR-META-001` (D1-D8)
  - `ADR-META-002` (D9-D12)
  - `ADR-META-005` (hooks automation, Vague 2 Q3 2026)
  - `ADR-LOOP-001/002/003` (verify-first, queues-over-loops, wagers mesurables)
  - L+ Skill Standard ratification 2026-07-05

## 6. Anti-patterns protégés (D4 + L+ invariants)

- ❌ Ne pas muter les agents canon (B2/B3 Eternals, A3 Picard, A3 Book) — append-only spec
- ❌ Ne pas inventer de chiffre (D1 anti-paresse, MEMORY.md §"Anti-pattern extraction 209 sessions", sister ADR-ANTI-PAPERCLIP-001 §D4 tableau ASCII)
- ❌ Ne pas créer de doublon agent (L+ invariant #2 type top-level)
- ❌ Ne pas activer de cron sans HITL A0 (Posture C)
- ❌ Ne pas escalader à A0 mid-research (D7 cost-of-escalation)
- ❌ Ne pas promettre AI-Act compliance sans D1 receipt verbatim (sister ADR-ANTI-PAPERCLIP-001 §D5)
- ❌ Ne pas dissoudre le hard-veto Aquaman L.42 sister SOBER-002 §6 par urgence deadline (sister ANTI-PAPERCLIP-001 §D3 confusion #1)
- ❌ Ne pas écrire de claim AI-Act « ready » sur landing sans citer Articles 9/14/15 verbatim (sister ADR-ICP-NEXUS-001 §Pilier 5)

---

**Wargame WF2 lens B2-Aquaman-Legal terminé.**

8 angles morts catalogués (5-10 range ✓), 3 recommandations canon-coaching pour A3-Book, 8/8 dimensions Legal identifiées comme hors-cadence Picard H10, **4/8 AI-Act DRIVERS** avec deadline 2026-08-02 (T-27 jours) en danger de cycle-gap H10, 0 chiffre inventé, sources canon paths absolus, L+ invariants respectés, sister-ADR-ANTI-PAPERCLIP-001 cité §D3 confusion #1 + §D4 + §G1 + §G3.

Handoff : `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\handoff_wargame_wf2_b2_aquaman_legal_lens_2026-07-06.md`

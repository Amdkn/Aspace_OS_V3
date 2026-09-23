---
session: agent-a283db3e91a289a9d
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\de35c5f1-6944-47f6-b8bc-849452b0313a\subagents\agent-a283db3e91a289a9d.jsonl
debut: 2026-07-25T18:38:11.643Z
fin: 2026-07-25T18:53:38.954Z
messages_utilisateur: 2
reponses_assistant: 1
titre: "You are an X-Men Coach Review sub-agent. Read this brief, then execute. ## Mission Apply the **3 X-Men Coach l…"
---

## >>> UTILISATEUR #1

You are an X-Men Coach Review sub-agent. Read this brief, then execute.

## Mission

Apply the **3 X-Men Coach lenses** (per `/youtube-to-B1filter` §13 + new `ADR-RH-META-GOUVERNANCE-001` PROPOSED) to the Domain 03 Growth spec being produced in parallel by Sub-agent 1.

The Coach role mapping for Avengers per the new paradigm:
- **Professor X (stratégique)** → reviews **Captain America (Steve Rogers, lead)**
- **Wolverine (adamantium)** → reviews **Iron Man (Tony Stark)** AND **Hulk (Bruce Banner)** (both adamantium-grade in their domains)
- **Jean Grey (Phoenix scope creep)** → reviews **Black Widow (Natasha Romanoff)** (scope + intel)
- **Cyclops (tactique, target hit-rate)** → reviews **Hawkeye (Clint Barton)**
- **Beast (R&D, hammer-grade)** → reviews **Thor (Thor Odinson)** AND **Scarlet Witch (Wanda Maximoff)**

For each Coach lens, produce:
- 1-2 PASS verdicts
- 1 CONDITIONAL verdict
- 1 ESCALATE_B1 if applicable

## Context

- Domain 03 = Growth (Flash × Avengers)
- Focus per A+ directive 2026-07-25 : $100M Offers, Million Dollar Weekend, Built to Sell, Apollo prospects, $1000/mo retainer, MIT 95% AI pilot failure
- Sister canon : ADR-CANON-001 (Roster), ADR-CANON-002 (Workflow RH&A, X-Men = SPAWN+AMÉLIORATION), ADR-RH-META-GOUVERNANCE-001 (Coach formalization), ADR-LANDING-AESTHETIC-001 (RATIFIED 2026-07-25), ADR-AAAS-PRICING-001, ADR-MARKET-STUDY-001, ADR-NEXUS-10-ICP-001

## Deliverable (return in your final response as markdown)

### 1. Professor X Review (stratégique) — on Captain America (Steve Rogers, lead)
- 1 PASS + 1 CONDITIONAL + (0-1 ESCALATE_B1)

### 2. Wolverine Review (adamantium) — on Iron Man + Hulk
- 1 PASS (Iron Man tech polish) + 1 PASS (Hulk stress test) + 1 CONDITIONAL (combined durability of tech + scale) + (0-1 ESCALATE_B1)

### 3. Jean Grey Review (Phoenix scope creep) — on Black Widow
- 1 PASS + 1 CONDITIONAL + (0-1 ESCALATE_B1)
- (If any scope creep detected in spec, name it explicitly)

### 4. Cyclops Review (tactique) — on Hawkeye
- 1 PASS + 1 CONDITIONAL + (0-1 ESCALATE_B1)

### 5. Beast Review (R&D) — on Thor + Scarlet Witch
- 1 PASS (Thor flagship) + 1 PASS (Scarlet Witch chaos) + 1 CONDITIONAL (R&D boundary) + (0-1 ESCALATE_B1)

### 6. Overall Verdict
- SHIP / REVISE / ESCALATE_B1

### 7. Coaching Recommendations
- Top 3 actionable improvements before next iteration
- Per `ADR-RH-META-GOUVERNANCE-001` §13 (X-Men Coach role formalization)

## Constraints

- D1-D8 as standard
- DO NOT create files — return content only
- Be specific to Domain 03 Growth (not generic)
- Sister canon: cite `ADR-CANON-001` (Roster 03), `ADR-CANON-002`, `ADR-RH-META-GOUVERNANCE-001`, `ADR-LANDING-AESTHETIC-001`

## Output format

Single markdown document with 7 sections. ~3-5K chars. No placeholders. Specific to Domain 03 Growth.

## >>> UTILISATEUR #2

Base directory for this skill: C:\Users\amado\.claude\skills\youtube-to-B1filter

# YouTube → B1 Filter — Green Lantern People/Agents/Harness Gatekeeper

> **Un transcript YouTube OU un guide Geordi existant → filtre B1 Green Lantern → extraction des bonnes pratiques agentiques → routage vers le bon LIVRE (Playbook Jerry / Runbook Summers / Ownerbook Picard / Cookbook coaching Picard / SOP B2 / Skills B3) à travers les 8 Domaines organisés en 2 Triptyques + 1 Duo.**

## 0. Why this skill exists (D3 nuance — A0 intent 2026-07-10)

Le skill `/youtube-to-guide` produit UN guide premium classé dans 1 des 8 domaines. Mais A0 veut un **filtre B1 gatekeeper** : lire une ressource AU TRAVERS de la lentille **People/Agents-IA/Harness/Workflow-agentique** de Green Lantern (B2 People, LEAD du Triptyque 1), et en extraire ce que **les X-Men de Green Lantern peuvent partager/utiliser** dans la config des équipes d'agents B1 et leurs swarms d'exécutifs stratégiques qui orchestrent les B3 superviseurs de freelances.

**Différence clé** :
- `/youtube-to-guide` = **classification** (quel domaine ?) → 1 guide
- `/b1-filter` = **LD mapping déterministe** (frontmatter) → sweep classification
- **`/youtube-to-B1filter`** (CE skill) = **filtre gatekeeper B1** (quelle pratique agentique, pour quel livre, pour quel capitaine ?) → routage multi-livres

## 1. Le filtre B1 Green Lantern (lentille People/Agents/Harness)

Green Lantern (B2 People, X-Men squad) = **LEAD du Triptyque 1** et **substrat RH/Agentique** de tout l'incubateur. Le filtre lit une ressource et extrait 4 catégories :

| Catégorie extraite | Question B1 gatekeeper | X-Men owner |
|---|---|---|
| **Agent Identity & Staffing** | Comment configurer/staffer une équipe d'agents ? | Cyclops (staff) + Prof X (ethics) |
| **Harness & Ecosystem** | Quel outil/harness/MCP optimise le workflow agentique ? | Beast (R&D) + Jean Grey (mentorship) |
| **Swarm Orchestration** | Comment orchestrer un swarm d'exécutifs stratégiques ? | Storm (culture) + Nightcrawler (mobility) |
| **B3→Freelance Supervision** | Comment un B3 supervise/crée/conserve des agents freelance ? | Wolverine (retention) + Rogue (KT) |

**Output B1 filter block** (ajouté au frontmatter de la ressource) :
```yaml
b1_filter_greenlantern:
  agent_identity: "<pratique de staffing extraite, ou N/A>"
  harness_ecosystem: "<outil/MCP/harness extrait, ou N/A>"
  swarm_orchestration: "<pattern d'orchestration extrait, ou N/A>"
  b3_freelance_supervision: "<pratique de supervision freelance, ou N/A>"
  xmen_shareable: [<liste des X-Men qui peuvent utiliser/partager cette pratique>]
```

## 2. Routage vers les 6 LIVRES (chaque pratique va à son livre canonique)

A0 canon 2026-07-10 : chaque bonne pratique opérationnelle extraite se range dans **UN des 6 livres** selon son horizon et son propriétaire.

| Livre | Propriétaire | Horizon | Contenu | Path canonique |
|---|---|---|---|---|
| **Playbook** | B1 Jerry (SYSTEMIZE) | 3 ans (E-Myth) | SOP canonisés des 8 domaines, systématisation work-ON-not-IN | `30_Business_OS/Playbooks_Jerry/<domain>/` |
| **Runbook** | B1 Summers (SHIP) | 1 an (12WY) | Procédures de ship par variant + ICP, exécution tactique | `30_Business_OS/Runbooks_Summers/<variant>/` |
| **Ownerbook** | B3 Picard (Captain) | 10 ans (legacy) | MANIFEST canon, ownership des Projects, Kardashev arc | `30_Business_OS/Ownerbooks_Picard/<project>/` |
| **Cookbook** | A3 Picard coaching | évolutif | Recettes d'évolution des Playbook/Runbook, coaching des B1 | `20_Life_OS/.../Cookbooks_Coaching/` |
| **SOP** | B2 (8 VPs) | H3/H10 | Standard Operating Procedures par domaine, per-B2 | `30_Business_OS/SOPs_B2/<b2_domain>/` |
| **Skills** | B3 (53 squads) | H1 | Compétences atomiques exécutables par squad Marvel/DC | `.claude/skills/` OU `30_Business_OS/Skills_B3/<squad>/` |

**Règle de routage (D3 nuance)** :
- Pratique **systémique réutilisable** (E-Myth "work ON") → **Playbook** (Jerry)
- Procédure **de ship tactique** (variant-spécifique) → **Runbook** (Summers)
- Décision **d'ownership long-terme** (MANIFEST) → **Ownerbook** (Picard)
- Recette **d'évolution/coaching** des livres eux-mêmes → **Cookbook** (Picard coaching)
- Procédure **opérationnelle standard** par domaine → **SOP** (B2)
- Compétence **atomique exécutable** → **Skill** (B3)

## 3. Structure organisationnelle : 2 Triptyques + 1 Duo

A0 canon : les 8 domaines VPs s'organisent en **2 Triptyques + 1 Duo** avec une supervision déléguée B1 → Triptyque 1.

### Triptyque 1 — BUILD SUBSTRATE (People + Ops + IT/R&D)

| Domaine | B2 (DC × Marvel) | Rôle dans le Triptyque | Supervision |
|---|---|---|---|
| **People** | GreenLantern × X-Men | **LEAD** — RH/Agentique, config équipes d'agents | B1 délègue à GreenLantern |
| **Operation** | Batman × Fantastic 4 | Systématisation SOP + Skills | GreenLantern coordonne |
| **IT (R&D)** | Cyborg × Kang Dynasty | **Intégration innovations + orchestrateur des changements de paradigme** | GreenLantern coordonne |

> **Triptyque 1 = le socle self-operating** : People staffe les agents, Ops les systématise en SOP, IT intègre les innovations et pilote les shifts de paradigme. Green Lantern (LEAD) reçoit la supervision déléguée de B1.

### Triptyque 2 — VALUE DELIVERY (Product + Growth + Sales)

| Domaine | B2 (DC × Marvel) | Rôle dans le Triptyque | Flow |
|---|---|---|---|
| **Product** | Flash × Avengers | Spec prototype franchise + UX | MVP → PoC |
| **Growth** | Superman × Guardians | Top funnel acquisition | PoC → Go-to-Market |
| **Sales** | JohnJones × Illuminati | Enterprise + sovereign deals | Go-to-Market cohérent |

> **Triptyque 2 = MVP → PoC → Go-to-Market cohérent**, scalabilité assurée par la supervision déléguée de B1 au Triptyque 1.

### Duo — RENTABILITÉ & CONFORMITÉ (Finance + Legal)

| Domaine | B2 (DC × Marvel) | Rôle du Duo |
|---|---|---|
| **Finance** | WonderWoman × Thunderbolts | Rentabilité des projets (unit economics, LTV/CAC, runway H3) |
| **Legal** | Aquaman × Eternals | Conformité des projets (AI-Act 2026-08-02, contrats, gouvernance) |

> **Duo = gate rentabilité + conformité** — chaque projet passe le Duo avant scaling.

## 4. 12WY rhythm : Trimestre → 3 Rocks Mensuels

A0 canon : le rythme trimestriel 12WY se décompose en **3 Rocks mensuels** pour chaque livre.

| Cadence | Horizon | Owner | Artefact |
|---|---|---|---|
| **Trimestre (12 semaines)** | HZ (cycle 12WY) | B1 Jerry+Summers | Playbook + Runbook update |
| **Rock Mensuel 1** | ~4 semaines | B2 domaine | 1 SOP canonisé |
| **Rock Mensuel 2** | ~4 semaines | B2 domaine | 1 Skill B3 shippé |
| **Rock Mensuel 3** | ~4 semaines | B3 Picard | 1 Ownerbook MANIFEST update |

## 5. Workflow (5 étapes)

### Mode A — Single resource (transcript OU guide existant)

```
Étape 1 — INPUT (transcript YouTube OR path to existing Geordi guide)
  ↓ Si transcript : réutiliser /youtube-to-guide Étapes 1-2 (capture + transcription)
  ↓ Si guide existant : Read le .md directement
  ↓ D6 context blowup guard : si > 6K chars → /swarm-chunk-transcript

Étape 2 — B1 FILTER (Green Lantern lens)
  ↓ Extraire les 4 catégories (§1) : agent_identity / harness / swarm / b3_freelance
  ↓ Identifier les X-Men shareable (Cyclops/ProfX/Beast/JeanGrey/Storm/Nightcrawler/Wolverine/Rogue)
  ↓ Écrire b1_filter_greenlantern block

Étape 3 — BOOK ROUTING (§2)
  ↓ Pour chaque pratique extraite : router vers Playbook/Runbook/Ownerbook/Cookbook/SOP/Skill
  ↓ D3 nuance : systémique→Playbook, ship→Runbook, ownership→Ownerbook, évolution→Cookbook, standard→SOP, atomique→Skill

Étape 4 — TRIPTYQUE ASSIGNMENT (§3)
  ↓ Assigner la ressource à Triptyque 1 (People/Ops/IT), Triptyque 2 (Product/Growth/Sales), ou Duo (Finance/Legal)
  ↓ Vérifier gate : Duo (rentabilité+conformité) requis avant scaling

Étape 5 — WRITE B1-FILTERED RESOURCE
  ↓ Guide premium 8-section (héritage /youtube-to-guide) + b1_filter block + book routing + triptyque
  ↓ D5 proof : wc -c ≥ 6000 + grep b1_filter_greenlantern = 1
```

### Mode B — Batch corpus analysis (/multi-goal + /swarm-orchestrator)

Pour analyser TOUTES les ressources du corpus Geordi guides et auto-générer des ADR d'auto-amélioration du Harness :

```
Étape 1 — INVENTORY
  ↓ Glob 01_Guides/**/*.md → liste des guides existants (exclure node_modules)
  ↓ Filter : guides sans b1_filter_greenlantern block = candidats

Étape 2 — /multi-goal dispatch
  ↓ Exit criterion : "tous les guides ont un b1_filter block + N ADR self-improvement proposés"
  ↓ Batch par domaine (8 domaines) OU par triptyque (3 groupes)

Étape 3 — /swarm-orchestrator (parallel sub-agents)
  ↓ 1 sub-agent par domaine (max 8 //) OR 1 par triptyque (3 //)
  ↓ Chaque sub-agent : lit N guides de son domaine → extrait B1 filter → route vers livres → propose ADR
  ↓ D4 append-only : chaque sub-agent écrit son handoff dans wiki/hand_offs/b1filter_<domain>_<date>.md

Étape 4 — ADR AGGREGATION
  ↓ Fan-in : agréger les ADR self-improvement proposés par les N sub-agents
  ↓ Dédup + rank par ROI Harness
  ↓ Écrire ADR drafts dans _SPECS/ADR/ (status PROPOSED, gated A0 HITL)

Étape 5 — CONVERGENCE REPORT
  ↓ D1 receipts : N guides filtrés, M ADR proposés, K livres alimentés
  ↓ learnings.jsonl append (Python json.dumps)
```

## 6. B1-Filtered resource template (extends /youtube-to-guide 8-section)

```markdown
---
id: YT-<video_id> OR GUIDE-<slug>
title: "<title>"
source: youtube | geordi_guide
status: B1_FILTERED_GREENLANTERN
# --- inherited from /youtube-to-guide ---
domain: 0X_<Domain>
ld: <LDxx>
b2_owner: <b2 captain>
sister_b1: jerry-prime | summers-*
# --- NEW B1 filter block ---
b1_filter_greenlantern:
  agent_identity: "<staffing practice>"
  harness_ecosystem: "<tool/MCP/harness>"
  swarm_orchestration: "<orchestration pattern>"
  b3_freelance_supervision: "<supervision practice>"
  xmen_shareable: [cyclops, beast, storm]
# --- book routing ---
book_routing:
  - practice: "<practice 1>"
    book: playbook | runbook | ownerbook | cookbook | sop | skill
    owner: jerry | summers | picard | <b2> | <b3>
  - practice: "<practice 2>"
    book: ...
# --- triptyque assignment ---
triptyque: T1_build_substrate | T2_value_delivery | DUO_profit_compliance
triptyque_role: lead | member | gate
# --- 12WY monthly rocks ---
monthly_rocks:
  rock_1: "<SOP to canonize>"
  rock_2: "<Skill B3 to ship>"
  rock_3: "<Ownerbook MANIFEST update>"
---

# 📖 <title>

## 🧠 Concepts Clés (héritage /youtube-to-guide, glossaire 5-6 concepts)
## 🛠️ Outillage & Matrice d'Alignement
## 🟢 Filtre B1 Green Lantern — People/Agents/Harness
  ### Agent Identity & Staffing (Cyclops + Prof X)
  ### Harness & Ecosystem (Beast + Jean Grey)
  ### Swarm Orchestration (Storm + Nightcrawler)
  ### B3→Freelance Supervision (Wolverine + Rogue)
## 📚 Routage vers les 6 Livres
## 🔺 Assignment Triptyque/Duo
## 🪐 Perspective Souveraine A'Space
## 🕹️ Protocole D.E.A.L
## 🔬 Annexes Détaillées

*Fiche B1-filtered souveraine générée sous A'Space OS V2 — Standard Antigravity Premium + B1 Green Lantern Gatekeeper.*
```

## 7. Doctrine ancrage (D1-D8 + ADR-SOBER-003 PPR)

- **D1 verify-before-assert** : 0 pratique inventée. Chaque catégorie B1 = extrait littéral du transcript/guide.
- **D2 research-first** : lire la bijection `ADR-L2-BDLD-MAP-001` §D3 avant de router vers un B2 owner.
- **D3 nuance over literal** : routage par GOULOT (pratique systémique→Playbook) pas par SUJET de surface.
- **D4 no-self-contradiction** : append-only. B1 filter block AJOUTÉ au frontmatter existant, jamais écrasé.
- **D5 proof-before-claim** : "guide filtré" = `grep b1_filter_greenlantern <path>` = 1 + `wc -c` ≥ 6000.
- **D6 root cause** : context blowup guard (§5 /swarm-chunk-transcript si > 6K chars).
- **D7 cost-of-escalation** : ADR self-improvement = status PROPOSED, gated A0 HITL. Jamais auto-ratifié.
- **D8 cross-agent** : Mode B batch = /swarm-orchestrator, max 8 sub-agents // (1 par domaine).
- **ADR-SOBER-003 PPR** : création de guide filtré = PPR lane (réversible, D4 append-only + reversal path). Pas de gate A0 pour la création. Seuls les ADR ratifications = destructif → A0 HITL.

## 8. Anti-pattern guards

- ❌ Inventer une pratique B1 non présente dans le transcript (D5 fabrication)
- ❌ Router vers le mauvais livre (ship→Playbook au lieu de Runbook) — D3 goulot pas sujet
- ❌ Écraser un guide existant (D4 — B1 filter block est ADDITIF)
- ❌ Auto-ratifier un ADR self-improvement (D7 — status PROPOSED only)
- ❌ Batch tout le corpus en 1 Main Agent context (D6 blowup — /swarm-orchestrator obligatoire)
- ❌ Confondre les 3 skills YouTube (voir §15 §Trio+ ci-dessous)

## 10. Cross-refs

- `/youtube-to-guide` (parent skill — 8-section premium standard)
- `/b1-filter` (sister — LD deterministic classification)
- `/multi-goal` (Mode B orchestration)
- `/swarm-orchestrator` (Mode B parallel dispatch)
- `ADR-L2-BDLD-MAP-001` §D3 (bijection 8 domains ↔ LD)
- `ADR-SOBER-003` (PPR — creation reversible lane)
- `mindsets/Jerry_Dispatch_Doctrine.md` (8 B2 → 53 B3)
- `mindsets/B2_01_greenlantern_people_Dispatch_Doctrine.md` (X-Men squad canon)
- `wiki/hand_offs/l2_business_os_boris_archetypes_structuring_2026-07-10.md` (Boris archetypes = agent identity source)

## 11. Open follow-ups

1. **Batch run Mode B** : /multi-goal sur les 01_Guides/**/*.md existants (exclure node_modules) → N ADR self-improvement
2. **6-book scaffold** : créer les répertoires Playbooks_Jerry / Runbooks_Summers / Ownerbooks_Picard / Cookbooks_Coaching / SOPs_B2 / Skills_B3 (PPR lane, gated A0 for structure)
3. **X-Men shareable index** : `_INDEX_xmen_shareable.md` par domaine (quelle pratique quel X-Men partage)
4. **12WY rock auto-decompose** : script qui décompose 1 Playbook trimestriel en 3 Rocks mensuels
5. **`agent_bench.gatekeeper_log` table** : table Supabase sister de `agent_bench.soul_schema` pour tracer les décisions Green Lantern (status A0 HITL on table creation)
6. **X-Men Coach spec sheets** : 8 SKILL.md canoniques pour chaque rôle Coach (Pocock-grill-me pattern)

---

## 12. Green Lantern = Gatekeeper B1 (RH & Méta-Gouvernance — ADR-RH-META-GOUVERNANCE-001)

> **Doctrine 2026-07-25** : Green Lantern (B2 People, LEAD Triptyque 1) endosse le rôle de **Gatekeeper B1** pour les décisions routinières réversibles en scope H1/H10. Cette élévation étend le filtre B1 (lentille People/Agents/Harness) en **autorité d'approbation** sur les transitions BENCH → BUILDING → ACTIVE des agents B3.

### 12.1 Scope OUI — Green Lantern valide en autonomie (PPR lane)

| Action | Horizon | Réversible | Pourquoi OUI |
|---|---|---|---|
| **Validation specs B3** avant `BENCH → BUILDING` | H1/H10 | OUI (rollback bench) | Specs B3 = atomes, scope People-owned |
| **Transitions `BUILDING → ACTIVE`** sur agent_bench.gatekeeper_log | H1 | OUI (rollback active) | Promotion atomique, D7 cost-of-escalation |
| **Captures `soul_schema`** (cf. §14) | H1/H10 | OUI (D4 append-only) | Pure capture, pas de mutation canon |
| **Re-routage `AI Tool → 8-domain`** (Mode 4 /b1-filter v2) | H1 | OUI (frontmatter sweep) | Méta-gouvernance, sister §15 |
| **Décisions H1/H10 réversibles** | H1/H10 | OUI | D7 cost-of-escalation ≪ D0 paralysis |
| **X-Men shareable updates** (`_INDEX_xmen_shareable.md`) | H1/H10 | OUI (D4 append-only) | Index canon, réversible |

### 12.2 Scope NON — Escalation B1 (A0 HITL obligatoire)

| Action | Horizon | Pourquoi ESCALATE |
|---|---|---|
| **Création de nouveaux rôles B1 / B2** (Jerry/Summers/B2) | H30+ | Irreversible canon, sœur ADR-CANON-001 |
| **Changements de scope H30+ / H90** | H30+/H90 | Impact legacy long-terme |
| **Coordinations inter-B2 simultanées** (>2 B2 actifs) | H3+ | Synchronisation > capacité B2 isolée |
| **Toute action touchant D7 anti-paperclip** (maximizer veto) | ANY | ADR-SOBER-002 hard veto, jamais délégation |
| **Ratification ADR PROPOSED → RATIFIED** | ANY | Sister ADR ratify process (D7 airlock) |
| **Destructive ops (hard-delete, DROP TABLE, rm -rf)** | ANY | D4 append-only violation |

### 12.3 Émission `gatekeeper_approval` dans le frontmatter

Le filtre B1 émet un **gatekeeper_approval block** (sister schema `agent_bench.gatekeeper_log` per ADR-AGENT-BENCH-SCHEMA-001) :

```yaml
b1_filter_greenlantern:
  # ... existing fields (§1) ...
  gatekeeper_approval:
    status: APPROVED | ESCALATED | DEFERRED
    approver: greenlantern | a0
    timestamp: 2026-07-25T14:30:00Z
    scope: H1_H10 | H30 | H90 | ANTI_PAPERCLIP | DESTRUCTIVE
    reversible: true | false
    rollback_path: "<how to undo>"
    rationale: "<1-line D3 nuance justification>"
    xmen_coach_review_invoked: false  # links to §13
    soul_schema_captured: false       # links to §14
```

> **Règle d'or** : `gatekeeper_approval.status = APPROVED` n'est valide que si `scope = H1_H10` ET `reversible = true`. Tout autre scope = `ESCALATED` obligatoire.

---

## 13. X-Men = Coach (couche additionnelle au-delà de SPAWN — ADR-CANON-002)

> **Doctrine 2026-07-25** : au-delà de la SPAWN canonique (création d'agent), les X-Men de Green Lantern remplissent un **rôle de Coach** qui valide les SOUL avant ship, critique les specs B3, et détecte le scope creep. Cette couche est **invoked conditionnellement** par le filtre B1.

### 13.1 Les 8 rôles Coach (mapping X-Men)

| Coach | X-Men | Domaine d'expertise | Question Coach |
|---|---|---|---|
| **Professor X** (LEAD) | Charles Xavier | Stratégique global | La spec B3 sert-elle l'Ikigai canon ? |
| **Wolverine** | Logan | Critique brutale | Quels edge cases la spec ignore-t-elle ? |
| **Jean Grey** | Jean Grey-Summers | Scope creep detector | La spec déborde-t-elle du scope H1/H10 ? |
| **Storm** | Ororo Munroe | Climat data | Le data flow de la spec est-il météo-stable ? |
| **Beast** | Hank McCoy | R&D discoveries | La spec intègre-t-elle `research_loop_config` proprement ? |
| **Nightcrawler** | Kurt Wagner | Mobilité inter-B2 | La spec permet-elle le BAMF inter-domaines ? |
| **Rogue** | Anna Marie | Absorption SOUL | Le SOUL schema est-il capturé avant archivage ? |
| **Cyclops** | Scott Summers | Tactical lead | La spec est-elle ship-ready (vision + tactical execution) ? |

### 13.2 Quand invoquer Coach review dans le workflow B1

Coach review est **invoqué conditionnellement** dans le workflow §5 :

```
Étape 2 — B1 FILTER (Green Lantern lens)
  ↓ Extraire les 4 catégories (§1)
  ↓ DÉCISION : invoke Coach review ?
  ↓   OUI si l'une des conditions :
  ↓     - La spec touche un nouveau B2 (Jamais-Créé-encore)
  ↓     - H30+/H90 implications détectées
  ↓     - Inter-B2 simultané (D7 anti-scope-creep)
  ↓     - Pattern de scope creep détecté dans le guide
  ↓   NON si : pure pratique atomique H1/H10 (default PPR)
  ↓ Si OUI : invoquer 3+ Coach pertinent (jamais les 8 tous)
  ↓ Écrire xmen_coach_review block
```

### 13.3 Émission `xmen_coach_review` dans le frontmatter

```yaml
b1_filter_greenlantern:
  # ... existing fields ...
  xmen_coach_review:
    invoked: true
    invoked_at: 2026-07-25T14:35:00Z
    invoked_reason: "spec touche nouveau B2 X (scope creep risk)"
    coach_invoked: [professor_x, wolverine, jean_grey]  # 3+ picked
    verdicts:
      professor_x:
        verdict: PASS | FAIL | CONDITIONAL
        note: "<1-line rationale>"
      wolverine:
        verdict: PASS | FAIL | CONDITIONAL
        edge_cases_flagged: ["<edge 1>", "<edge 2>"]
      jean_grey:
        verdict: PASS | FAIL | CONDITIONAL
        scope_creep_detected: true | false
        scope_violation: "<1-line if any>"
    overall: PASS | FAIL | ESCALATE
    escalation_required: false
    next_action: SHIP | REVISE | ESCALATE_B1
```

> **Règle d'or** : `overall = PASS` requiert que les 3+ Coach aient tous `PASS` ou `CONDITIONAL`. Tout `FAIL` d'un seul Coach = `ESCALATE` ou `REVISE` obligatoire.

---

## 14. SOUL Schema Capture (extension soul-aware du b1_filter_greenlantern)

> **Doctrine 2026-07-25** : lorsque la ressource filtrée **enseigne un pattern d'agent** (pas seulement une pratique ops), le filtre B1 capture le **SOUL schema canonique** (sister `agent_bench.soul_schema` per ADR-AGENT-BENCH-SCHEMA-001) avant archivage. C'est l'extension **soul-aware** du bloc `b1_filter_greenlantern` (§1).

### 14.1 Conditions de capture (quand déclencher)

Le SOUL schema est capturé si **TOUTES** ces conditions sont réunies :

1. La pratique extraite (§1) décrit un **pattern d'agent autonome** (pas juste une procédure)
2. Le pattern est **réutilisable** par ≥3 contextes distincts (B1, B2, B3)
3. Le pattern n'est **pas déjà dans** `agent_bench.soul_schema` (D6 no-duplicate)
4. La gatekeeper_approval (§12) a `status = APPROVED`
5. La xmen_coach_review (§13) — si invoquée — a `overall = PASS`

### 14.2 Émission `soul_schema` dans le frontmatter

```yaml
b1_filter_greenlantern:
  # ... existing fields ...
  soul_schema:
    captured: true
    captured_at: 2026-07-25T14:40:00Z
    captured_by: greenlantern  # or a0 if escalated
    system_prompt: |
      <1-paragraph distilled SOUL — who is this agent, what is its mission,
      what are its bounds, what is its voice>
    action_space_bounding:
      allowed_tools: [<list of tools the agent can invoke>]
      forbidden_actions: [<list of actions the agent must never take>]
      resource_limits:
        max_tokens_per_call: <int>
        max_duration_seconds: <int>
        max_concurrent_runs: <int>
    research_loop_config:
      loop_strategy: karpathy_auto_research | fable_mode | single_pass | swarm_orchestrator
      loop_interval_minutes: <int if loop>
      exit_criterion: "<string>"
      max_iterations: <int>
      sub_agent_dispatch: parallel | sequential
    gatekeeper_approval: false  # MUST match §12 status
    xmen_coach_review: false    # MUST match §13 verdict
    soul_schema_id: <uuid>  # FK to agent_bench.soul_schema row
```

### 14.3 Cycle de vie SOUL (capture → bench → active → archived)

```
       capture (§14)
            ↓
       BENCH (research_loop_config running, never shipped)
            ↓ gatekeeper_approval (§12) APPROVED + reversible
       BUILDING (sub-agent dispatch active, supervised)
            ↓ gatekeeper_approval §12 BUILDING → ACTIVE
       ACTIVE (shipped, in rotation, ROGUE absorbs patterns)
            ↓ xmen_coach_review §13 ESCALATE or H30+ sunset
       ARCHIVED (D4 append-only, retained in canon)
```

> **Règle d'or** : `gatekeeper_approval` et `xmen_coach_review` dans `soul_schema` doivent **toujours pointer** vers les blocks correspondants du frontmatter `b1_filter_greenlantern` parent. Pas de duplication, pas de drift.

---

## 15. §Trio+ — Routage des skills YouTube + B1 (anti-doublon, étendu v1.1)

| Skill | Rôle | Output |
|---|---|---|
| `/youtube-to-para` | ENTRÉE funnel : ingestion + ADR drafts généraux | `wiki/hand_offs/youtube_ingest_<date>/` |
| `/youtube-to-guide` | DISTILLATION premium par vidéo (8 sections) | `01_Guides/<0X_DOMAIN>/` |
| `/youtube-takeout-to-lifeos` | CAPTURE bulk mécanique takeout | `09_Life_OS/LDxx_*/` |
| `/b1-filter` | LD mapping déterministe (frontmatter sweep) — **v2 = Mode 4 meta-gouvernance** (AI Tool routing fix) | in-place frontmatter fix + gatekeeper_approval |
| `/youtube-to-Businessos` | **NEW sister v1.1** : routage direct 8-domain Business OS, no B1 filter (pour B0/CEO direct routing) | `01_Guides/<0X_DOMAIN>/` (sans b1_filter block) |
| **`/youtube-to-B1filter`** (CE skill) | FILTRE GATEKEEPER B1 : lentille People/Agents/Harness + routage 6 livres + 2T+1D + batch ADR + **§12 Green Lantern gatekeeping + §13 X-Men Coach + §14 SOUL capture** | `01_Guides/<domain>/` (b1_filter block) + `_SPECS/ADR/` (self-improvement) + `agent_bench.soul_schema` (capture) |

> **Note v1.1** : `/b1-filter` v2 inclut désormais le **Mode 4 meta-gouvernance** (AI Tool routing fix) qui était précédemment géré en dehors du skill. Cette mise à jour aligne le LD mapping déterministe avec le flux gatekeeper B1 (cf. §12). Sister `/youtube-to-Businessos` ajoutée pour le routing CEO direct sans filtre B1 (H1/H10 décisions souveraines).

---

**Status** : **v1.1 (B1 Green Lantern Gatekeeper + X-Men Coach + SOUL Schema Capture)** — créé par Claude Code (A2) sur directive A0 (PPR lane per ADR-SOBER-003, creation reversible) 2026-07-10, **étendu 2026-07-25** par l'ADR-RH-META-GOUVERNANCE-001 sister (DRAFT PPR lane). Ajouts : §12 Green Lantern gatekeeping (OUI/NON scope + `gatekeeper_approval` frontmatter), §13 X-Men Coach (8 rôles + invocation conditionnelle + `xmen_coach_review` block), §14 SOUL Schema Capture (conditions + cycle de vie BENCH→BUILDING→ACTIVE→ARCHIVED + `soul_schema` block). §Trio renuméroté §15 + ajout `/youtube-to-Businessos` sister + note `/b1-filter` v2 Mode 4.


ARGUMENTS: Apply §13 X-Men Coach lenses to the parallel Domain 03 Growth spec; read-only review, return markdown only

### assistant

# 1. Professor X Review — stratégique, sur Captain America

- **PASS — cohérence stratégique.** La direction déclarée relie correctement les cinq leviers de Domain 03 Growth : **$100M Offers** structure la valeur, **Million Dollar Weekend** impose une validation rapide, **Built to Sell** force la productisation, **Apollo** fournit le canal, et le **retainer à $1,000/mois** teste la récurrence. Captain America maintient ainsi une mission unique : prouver qu’une offre reproductible peut convertir un ICP Nexus réel.
- **CONDITIONAL — North Star mesurable.** Le spec doit rester borné à **un ICP, une offre, un CTA, une cohorte de 10 prospects et une fenêtre d’essai**. Le retainer à $1,000/mois doit être étiqueté **hypothèse H1 expérimentale**, pas modification silencieuse de `ADR-AAAS-PRICING-001`.
- **ESCALATE_B1 — réconciliation du domaine.** `ADR-CANON-001` et `ADR-CANON-002` placent encore **Flash × Avengers dans Product**, alors que `ADR-RH-META-GOUVERNANCE-001` PROPOSED les recaste en **Domain 03 Growth**. Le sprint peut avancer, mais la nouvelle taxonomie doit être déclarée explicitement et réconciliée par B1 avant de devenir canon H30.

# 2. Wolverine Review — adamantium, sur Iron Man + Hulk

- **PASS — Iron Man / tech polish.** Le rail minimal **Apollo → message personnalisé → landing/audit CTA → proposition de retainer** est suffisamment compact pour être instrumenté sans construire une plateforme prématurée. La landing doit appliquer `ADR-LANDING-AESTHETIC-001` : intentionnalité, typographie distinctive, palette dominante avec sharp accent et **un seul élément signature**, pas un template de cartes génériques.
- **PASS — Hulk / stress test.** Le terrain D1 est réel : **22 contacts Apollo**, dont **7 Qualified**, **11 à requalifier**, **4 Disqualified**, **15 emails vérifiés**, avec zéro campagne encore exécutée. Cela suffit pour casser le funnel sur une petite cohorte avant toute affirmation de scale.
- **CONDITIONAL — durabilité tech + scale.** Les 10 prospects doivent être composés des **7 Qualified + 3 Blank requalifiés**, jamais des Disqualified. Les limites connues — revenu absent sur 20/22, 6 emails manquants, zéro contact TX/FL — doivent rester visibles. Aucun résultat sur 10 leads ne doit être extrapolé au marché défini par `ADR-MARKET-STUDY-001`.

# 3. Jean Grey Review — Phoenix scope creep, sur Black Widow

- **PASS — intel ciblée.** Apollo est utilisé comme source de validation d’un ICP Nexus concret, cohérent avec les strates coaching/croissance de `ADR-NEXUS-10-ICP-001`, plutôt que comme prétexte à une stratégie “tout marché”.
- **CONDITIONAL — frontière de propriété obligatoire.** Le spec doit séparer : **Growth-owned** — cohorting, hook, campagne, CTA, métriques ; **dependencies** — pricing Finance, fermeture Sales, landing Product/Design ; **out of scope** — refonte ICP, nouveau produit, CRM complet, changement du pricing canon.
- **Scope creep détecté explicitement :** faire tenir dans le même sprint la refonte du roster, la canonisation du $1,000/mois, l’automatisation Apollo, une nouvelle esthétique de landing et la preuve scientifique du MIT. Ces éléments sont des dépendances ou validations, pas cinq sous-projets Growth.

# 4. Cyclops Review — tactique, sur Hawkeye

- **PASS — target hit-rate.** La cohorte de 10 prospects rend la tactique traçable prospect par prospect et respecte l’esprit **Million Dollar Weekend** : confrontation rapide au marché plutôt que construction spéculative.
- **CONDITIONAL — critères pré-déclarés.** Avant le premier envoi, Hawkeye doit figer la chaîne : `selected → sent → delivered → replied → audit_booked → offer_sent → won/lost`, avec source Apollo, variante de hook et objection capturée. Le verdict ne peut pas être “campagne lancée” ; il doit reposer sur un seuil d’acceptation défini avant observation.
- **Pas d’ESCALATE_B1** si cette expérience reste H1, réversible et sans mutation du canon, conformément au scope délégué de `ADR-RH-META-GOUVERNANCE-001`.

# 5. Beast Review — R&D, sur Thor + Scarlet Witch

- **PASS — Thor / flagship.** Le **retainer Built-to-Sell** constitue un flagship intelligible s’il possède un outcome, des livrables, une cadence, des exclusions et une garantie bornée — pas seulement une promesse “AI transformation”.
- **PASS — Scarlet Witch / chaos contrôlé.** Tester le hook “Mirror” contre le hook MIT est une expérience utile si **une seule variable change**. Offre, prix, ICP et CTA doivent rester constants pendant ce test.
- **CONDITIONAL — frontière R&D.** La formulation **“95% des pilotes IA échouent”** est trop large. Le canon disponible rapporte plutôt que 95% ne déplacent **aucune métrique mesurable**. Beast exige la source primaire, la citation exacte et son périmètre avant publication. La R&D s’arrête dès que le claim est vérifiable ; elle ne doit pas devenir une nouvelle étude de marché.

# 6. Overall Verdict

## **REVISE**

La direction est forte et l’expérience H1 peut avancer, mais trois corrections sont nécessaires : réconcilier explicitement **Growth 03 vs Product canon**, isoler le **$1,000/mois comme hypothèse** plutôt que pricing canon, et verrouiller la **preuve MIT + les métriques du funnel**. Verdict fondé sur le brief déclaré et les sisters `ADR-CANON-001`, `ADR-CANON-002`, `ADR-RH-META-GOUVERNANCE-001` et `ADR-LANDING-AESTHETIC-001`.

# 7. Coaching Recommendations

1. **Ajouter un Scope Contract en tête du spec** : taxonomie utilisée, Growth-owned, dépendances inter-B2, hors-scope et point précis nécessitant réconciliation B1.
2. **Créer le ledger tactique des 10 prospects** : 7 Qualified + 3 requalifiés, variante de hook, états du funnel, objections, critère de succès et condition d’itération.
3. **Verrouiller l’Offer/Evidence/Aesthetic Contract** : $1,000/mois marqué hypothèse H1, deliverables Built-to-Sell explicites, claim MIT cité sans déformation, landing vérifiable contre les invariants de `ADR-LANDING-AESTHETIC-001`.

Ces trois actions appliquent la formalisation Coach de `ADR-RH

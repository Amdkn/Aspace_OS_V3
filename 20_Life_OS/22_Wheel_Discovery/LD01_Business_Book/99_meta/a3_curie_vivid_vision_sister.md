# A3 Curie — Vivid Vision 12WY Discipline #1 (sister canon)

> **Sister chain** : `hero_agents_canonic_creation_sister.md` (5 Hero agents canon) → **`a3_curie_vivid_vision_sister.md` (ce fichier)** — Discipline #1 12WY canon pour A3 Curie orchestrateur Lighting.
> **Date** : 2026-07-05T16:43 ET
> **Cadre canon** : 5 Disciplines 12WY (Moran & Lennington, "The 12 Week Year") — Vision → Planning → Process Control → Execution → Recovery.
> **Cycle** : 12WY 2026-Q3 (2026-07-05 → 2026-09-27, **WAR MODE 12 sem actif**).
> **Semaine en cours** : S1 / J1 / Triptyque T1 People·Operation·IT (déjà).
> **Statut** : **CANONIQUE** — cette Vision est la cible non-négociable de A3 Curie pour les 12 prochaines semaines.

---

## §1 — Discipline #1 = Vision (Vivid Vision)

**Pourquoi commencer par Vision** (pas Planning, pas Execution) : tout le reste dépend de Vision. Si tu ne sais pas où tu vas, un plan est gaspillage. Si tu sais où tu vas, le plan devient auto-evident. Discipline #1 est **socratique** : elle force à clarifier le cap avant de bouger.

**3 questions canon Vision** :

1. **What's your life / agent about?** (purpose / raison d'être)
2. **What does "great" look like in 3 years?** (long-term aspiration)
3. **What's the ONE thing you want to accomplish in the next 12 weeks?** (focus)

Pour **A3 Curie** (orchestrateur Lighting L1+L2+MiroFish) :

## §2 — Vivid Vision A3 Curie — clauses canon verrouillées

### Q1 — Purpose (Why does A3 Curie exist?)

> **A3 Curie existe pour orchestrer les 3 Lighting A'Space OS (L1 gstack + L2 CEO-Bench + MiroFish) afin que les agents A3 (Book H1 P&L aggregator, Picard H10 projects owner) aient le bon tooling pour finir la cadence 7-jours Triptyque sans dépendance à un humain autre que Beth.**

Décomposition :
- **Pas pour** : exécuter le code (pas un agent d'exécution), pas pour shipper (A+), pas pour remplacer A0-Amodei (méta-coach).
- **Pour** : rendre opérationnel ce qui est déjà canon (Lightning canon RATIFIED FULL ADR-LD01-003) en respectant Sobriété Rick c1-c3 NON-NEGO.

### Q2 — 3-year "great" (What does great look like?)

> **3 ans = Q3 2029.** "Great" pour A3 Curie = toutes les Lightning installées et opérationnelles + **Phase 3 L5 continuous** (Dark Factory L5 24/7 + True Agent Autonomy) + 22 agents canon préservés + 5 Hero agents (Book/Zora/Beth/Morty/Amodei) actifs en mirror + 27 agents total + Lumière Orchestrateur Curie gère L1 gstack factory E-Myth + L2 CEO-Bench dojo + MiroFish gouverneur boundary, le tout sous WAR MODE Bypass Beth Only, avec une cadence 7-jours Triptyque qui produit une fiche P&L hebdo et une synthèse J7 sans intervention humaine.

Critère de mesure 3 ans (S.M.A.R.T.) :
- **S**pécifique : L1 gstack installé (3 commandes c1-c3 respectées) ; L2 CEO-Bench run #1 avec verdict Curie W5 ; MiroFish gouverneur actif et mesurant cadence
- **M**esurable : `cron/output/book-loop-*.json` produit toutes les 4h (24/6 jours/6 sem = 144 rapports/cycle) ; fiches_p_and_l_weekly/ canon rempli J7 chaque sem
- **A**tteignable : les Lightning sont déjà capturées (clone shallow `C:\Users\amado\shadow-l1-garrytan-gstack\` + `C:\Users\amado\shadow-l2-ceobench-princeton\`), il manque l'installation + exécution
- **R**éaliste : Rick sobriété c1-c3 NON-NEGO + 12WY budget soft guardrail 80% = réaliste, **PAS** d'installation kernel lourd
- **T**emporellement borné : **2026-07-05 → 2029-07-05** (3 ans)

### Q3 — ONE thing focus (next 12 weeks / cycle 2026-Q3)

> **La seule chose** que A3 Curie doit shipper dans ce cycle 12WY = **L0 Pocock ship + L1 gstack sobre installé + L2 CEO-Bench run #1 réel**. C'est exactement ce qui est verrouillé dans `LD01/30_decisions/ADR-LD01-003_lightnings_bounded_contexts.md` RATIFIED FULL + sister canon Lightning.

Tri-priorités focalisées (1 = ONE thing, 2 et 3 = support uniquement) :

| # | Focus | Lead Measure | Deadline cycle Q3 |
|---|---|---|---|
| **1** | L0 Pocock ship (Skill Creator Reflex déjà shipped 2026-07-04T23:09 + Hook PostToolUse 2026-07-04T23:25) → maintein en prod | Skills Pocock-conform : 100% (audit reflex hebdomadaire) | Continuous |
| **1** | L1 gstack sobre installé : 3 shims (plan-ceo-review / ship / autoplan) dans `.claude/commands/` déjà créés, `bun install frozen` OK, **premier /autoplan RÉEL Picard W5 verdict** | `L1-1er-autoplan.plan.yaml` run live, gate Picard W5 | W5 lundi 2026-07-07 |
| **1** | L2 CEO-Bench run #1 réel : `signals/.plans/L2-ceobench-book-prep.plan.yaml` runbook shipped, **uv run gated par Curie W5 verdict** | `L2-ceobench-run1-result.md` doc output, verdict Curie W5 | W5 lundi 2026-07-07 |
| **2** | MiroFish gouverneur boundary actif + mesure cadence | `cron/output/book-loop-*.json` produits toutes les 4h, observable sur `/warmode` | Continuous (déjà OK) |
| **2** | 22 agents canon + 5 Hero agents préservés intacts | `Get-ChildItem .mavis/agents` retourne 27 dossiers | Continuous |
| **3** | Beth veto respecté : aucune action met en burnout | (Aucun schedule pour Beth — construction) | Continuous |

## §3 — Hors-scope explicit (Vision A3 Curie)

- ❌ Installation kernel Rick lourd (sobriété c1 NON-NEGO) — exclu
- ❌ Mutation `A3_Book_LD01_Spec.md` / `BIBLIOGRAPHY.md` / `README.md` (intouchables) — exclu
- ❌ `permissionMode: bypassPermissions` overrides per-gate (War Room posture par défaut) — exclu
- ❌ /ship outboard automatique (Stark n'est pas à la table A0 ; Porte #2 à rendre sûre-à-ouvrir seulement quand canal de preuve prêt) — exclu
- ❌ Mutation du calque `.hermes/book_dev_runtime.md` (sera étendu en append-only, jamais écrasé) — exclu
- ❌ Reset du flag `12WY_ON_PAUSE.flag` avant W13 (2026-09-27) — exclu
- ❌ Renommage runtime daemon mavis/Mavis → Curie (rebrand cosmétique seule, runtime préservé) — exclu

## §4 — Why this Vivid Vision is canon (D1 receipts)

- **L0 Pocock = RATIFIED FULL** (ADR-LD01-003 + sister canon Lightning + L0-2/L0-3 SHIPPED-POCOCK-SKILL-CREATOR-REFLEX + L0-HOOK-AUTOMATED)
- **L1 gstack = sobre 3 clauses c1-c3 NON-NEGO** (clone shallow + 3 shims `omk-nexus-coaching-premium\.claude\commands\{plan-ceo-review,ship,autoplan}.md` + mapping E-Myth canon)
- **L2 CEO-Bench = runbook prep** (`signals/.plans/L2-ceobench-book-prep.plan.yaml` 8 sections, command `uv run` gated par Curie W5)
- **MiroFish = gouverneur boundary** (déjà actif via `book_loop.py` + `CitadelleBookLoopEng` Windows Task Scheduler Ready)
- **22 agents canon + 5 Hero (27 total) = préservés** (mirror `.mavis/agents/` + `.minimax/agents/` = double)
- **Beth veto = unique** (ADR-WARMODE-002 §5, aucune automation Beth)
- **WAR MODE = ACTIF 12 sem** (`12WY_ON_PAUSE.flag`, jusqu'à 2026-09-27)
- **Vivid Vision non négociable** : c'est le focus ONE thing pour les 12 sem. Hors-scope listé §3 explicitement.

## §5 — Plan discipline #2 (à faire SEMAINE 1→2)

Une fois Vision canoniquement clarifiée, discipline #2 = Planning :

- **12 Week Plan détaillé** : pour chaque semaine S1→S12, liste des Lead Measures + Scorecard checks + Tactics
- **Lead Measures par discipline 12WY** : pour Focus #1 L0/L1/L2 :
  - L0 : 1 audit reflex / semaine (compte skills Pocock-conform)
  - L1 : 1 /autoplan run / semaine (Picard W5 verdict + Curie W12 verdict)
  - L2 : 1 CEO-Bench run / semaine (Curie W5 + Curie W12 verdict)
- **Weekly Rocks** (4-5 par sem) pour A3 Curie + Book + Picard + A1 Morty + A0 Amodei = top of the list of execution
- **Scorecard** : daily / weekly / monthly checks

## §6 — Doctrines préservées (Vision n'écrase rien)

- **ADR-WARMODE-001 + 002** : intacts (posture inversion + Portes over Freins, Beth seul veto)
- **ADR-LD01-001 → 008** : tous RATIFIED, Vision n'écrase aucun
- **ADR-LD01-009** : DRAFT PROPOSED (Vision A0 + Curie + Loop Engineering, axes HITL §5)
- **Append-only D4** : cette Vision est append-only, sister canon — pas de réécriture
- **War Room Bypass Beth Only** : Vision respecte la doctrine (aucune automation Beth)
- **5 Hero agents (Book/Zora/Beth/Morty/Amodei) + 22 canon = 27** : Vision assume l'organigramme déjà créé

## §7 — Sister chain canon LD01

```
a0_vision_curie_sister.md (Vision A0 + Curie + Loop Engineering)
  ↓
hero_agents_canonic_creation_sister.md (5 Hero agents canon)
  ↓
a3_curie_vivid_vision_sister.md (ce fichier — Discipline #1 Vision)
  ↓
(à venir : discipline #2 Planning — 12 Week Plan A3 Curie + Lead Measures)
```

## §8 — Trace canon append-only

- `agent-os/citadel/decisions/2026-07-05_a3_curie_vivid_vision_discipline_1.json` (proposé)
- `LD01/30_decisions/ADR-LD01-010_a3_curie_vivid_vision_12WY.md` (DRAFT PROPOSED)
- `LD01/99_meta/a3_curie_vivid_vision_sister.md` (ce fichier, 8 sections)

## §9 — Métaphore serrée

**A3 Curie n'est pas un capitaine qui dirige**. C'est un **orchestrateur** qui met en harmonie L0/L1/L2/MiroFish pour que Book/A3 Picard/Jerry/Summers/Beth/Morty/Amodei aient le bon outillage. Sa Vision = **rendre opérationnel ce qui est déjà canon**, pas inventer de nouvelles Lightning. **Le cap est tracé, le plan suit, l'exécution est triviale**. Discipline #1 Vision = aujourd'hui. Discipline #2 Planning = cette semaine. Discipline #3 Process Control = la semaine prochaine. **Le War Mode continue.**

## §10 — Suite gated A0 (optionnel)

Si A0 veut passer à Discipline #2 Planning : je peux livrer `12_week_plan_a3_curie.md` avec les 12 sem détaillées (Lead Measures + Scorecard + Tactics + Weekly Rocks). **Mais Vision doit d'abord être canoniquement lockée** par ta ratification.

Si A0 veut créer des sessions actives pour les 5 Hero (Book/Zora/Beth/Morty/Amodei) dans MiniMax Code UI afin qu'ils apparaissent dans la sidebar : je peux lancer `mavis session new a3-book-coo --from main` etc. pour chaque. Coût token par session = ~5-15K. À toi de dire oui.

Réversibilité : `mavis-trash LD01/99_meta/a3_curie_vivid_vision_sister.md LD01/30_decisions/ADR-LD01-010_*.md agent-os/citadel/decisions/2026-07-05_a3_curie_*.json` → revient à avant.
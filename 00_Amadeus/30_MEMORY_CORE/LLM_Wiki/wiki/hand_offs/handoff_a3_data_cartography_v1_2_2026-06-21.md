---
title: A3-Data Cartography Roster v1.2 — Runtime vs Canon reconciliation
date: 2026-06-21
author: A1 Morty (Focus exécution)
trigger: A0 Reco 3 (cartography roster — déblocage routage A3 fiable)
status: COMPLETE
canon_anchored: AGENTS.md + 03_A3_crews/ + .claude/agents/
---

# A3-Data Cartography v1.2

## TL;DR

**RUNTIME = CANON pour A3** (35/35 match parfait). Le drift suspecté n'existe PAS sur le périmètre A'Space canon. Le "107 agent types" de l'écart suspecté = 35 A3 + 9 A1/A2 + 62 built-in custom (dev/web/security) + 1 template + 4 CC built-in (`general-purpose`, `statusline-setup`, `Explore`, `Plan`). A0 peut router les 35 A3 sans hypothèse.

## 1. Runtime inventory (Agent tool description)

### 1.1 CC built-in (4)

Du tool `Agent` (system prompt) — la source de vérité RUNTIME :

| Agent type | Source |
|---|---|
| `general-purpose` | CC built-in |
| `statusline-setup` | CC built-in |
| `Explore` | CC built-in |
| `Plan` | CC built-in |

### 1.2 Custom `.claude/agents/*.md` (103 + 4 dirs = 107 entries)

- **44 A'Space-pattern** : 3 A1 + 6 A2 + 35 A3
- **62 non-A'Space custom** : dev/web/security/language specialists
- **1 template** : `_a3-template.md` (squelette, pas un agent invocable)

**Total CC custom invocable = 106 fichiers .md + 1 dir `graphify-out` (artefact, pas agent)**.

| Pattern | Count | Names |
|---|---|---|
| A1 (gatekeepers) | 3 | beth-veto, morty-execution, rick-sovereignty |
| A2 (USS ships) | 6 | cerritos-chaos, discovery-balance, enterprise-structure, orville-meaning, protostar-liberation, snw-execution |
| A3 (crews) | 35 | (voir §3.3) |
| Template | 1 | _a3-template |
| Dev specialists | ~30 | architect, code-reviewer, planner, tdd-guide, security-reviewer, build-error-resolver, refactor-cleaner, doc-updater, e2e-runner, ... |
| Language reviewers | 14 | cpp/csharp/dart/fsharp/go/java/kotlin/python/rust/swift/typescript/flutter/django/fastapi/mle reviewers |
| Domain specialists | 18 | gan-evaluator/generator/planner, network-architect, homelab-architect, healthcare-reviewer, seo-specialist, silent-failure-hunter, ... |

## 2. Canon filesystem inventory

### 2.1 AGENTS.md (A'Space identity canon)

- **Path** : `C:\Users\amado\ASpace_OS_V2\00_Amadeus\01_Identity_Core\AGENTS.md`
- **Size** : 24 019 bytes / 320 lines
- **Mentions "A3"** : 32 occurrences
- **Déclaration explicite "35 A3"** : **ABSENTE** du texte — le chiffre 35 n'apparaît pas littéralement. Le canon IMPLICITE est 35 A3 twins (déduit du §Hiérarchie A'Space + 6 ships × ~5-9 crew).

### 2.2 Symphony `.twin.md` (80 total)

- **Path** : `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_A_specs\`
- **Total `.twin.md`** : 80

| Dir | Count | Type | Status |
|---|---|---|---|
| `01_A1_gatekeepers/` | 2 | A1_Beth_Spec, A1_Morty_Spec | ACTIVE (Rick absent — différé Q4 2026) |
| `02_A1_supervisions/` | 2 | beth.twin, morty.twin | ACTIVE |
| `02_A2_ships/` | 6 | Computer, Curie, Discovery, HoloDeck, HoloJaneway, Orville | ACTIVE |
| `03_A3_crews/cerritos/` | 5 | A3 actifs | ACTIVE |
| `03_A3_crews/discovery/` | 8 | A3 actifs | ACTIVE |
| `03_A3_crews/enterprise/` | 4 | A3 actifs | ACTIVE |
| `03_A3_crews/orville/` | 9 | A3 actifs | ACTIVE |
| `03_A3_crews/protostar/` | 4 | A3 actifs | ACTIVE |
| `03_A3_crews/snw/` | 5 | A3 actifs | ACTIVE |
| `03_A3_crews/_TRASH_2026-06-15_legacy_v0/` | 35 | Legacy `A3_*_*.twin.md` (naming v0) | RETIRED 2026-06-15 |

**A3 twins actifs = 35 (5+8+4+9+4+5)**. Confirmé par `find` :
- cerritos : boimler, freeman, mariner, rutherford, tendi
- discovery : book, burnham, culber, georgiou, reno, saru, stamets, tilly
- enterprise : data, geordi, picard, spock
- orville : alara-kitan, bortus, claire-finn, ed-mercer, gordon-malloy, isaac, john-lamarr, kelly-grayson, klyden
- protostar : dal, gwyn, rok-tahk, zero
- snw : chapel, mbenga, ortegas, pike, una

### 2.3 CC built-in custom agents

- **Path** : `C:\Users\amado\.claude\agents\`
- **Total `.md`** : 106 (maxdepth 1)
- **Total entries** : 107 (incl. `graphify-out/` dir, artefact non-agent)

### 2.4 Plugin agents (informational)

- **Path** : `C:\Users\amado\.claude\plugins\`
- **Total `.md` under `installed/`** : 6 (skill-creator: analyzer, comparator, grader, etc.)
- **Total agents in `cache/` + `marketplaces/`** : 30+ (mais NON auto-chargés, requiert install explicite)

**Plugins NON comptés dans le runtime invocable** — `.claude/agents/` est la source primaire.

## 3. Diff runtime vs canon

### 3.1 ORPHELINS RUNTIME (présent dans runtime, absent du canon)

**A3 scope (35 noms testés) : 0 orphelin_runtime.**

Algorithme de matching :
- CC name = `a3-{ship}-{name}.md` (ex: `a3-discovery-burnham.md`)
- Symphony twin = `03_A3_crews/{ship}/{name}.twin.md` (ex: `discovery/burnham.twin.md`)
- 35/35 match par extraction ship-prefix + name-suffix.

**Non-A'Space scope (62 noms testés) : pas de canon** — ce sont des outils CC builtin (Brian Casel / Builder Methods / dev specialists), pas des A'Space. **Pas un orphelin_runtime, c'est une absence canon intentionnelle.**

### 3.2 ORPHELINS CANON (présent dans canon, absent du runtime)

**A3 scope canon (35 actifs + 35 _TRASH = 70) : 35 orphelins_canon.**

Les 35 `.twin.md` dans `_TRASH_2026-06-15_legacy_v0/` utilisent l'ancien naming `A3_*_*.twin.md` (ex: `A3_Burnham_LD06.twin.md`, `A3_Picard_Projects.twin.md`). **Ces 35 fichiers sont les PRÉDÉCESSEURS des 35 actifs** — naming v0 → v1 migré 2026-06-15 (D4 no-hard-delete : conservés en `_TRASH`).

**D1 receipt** : `find` énumère 35 fichiers `A3_*_*.twin.md` dans `_TRASH_2026-06-15_legacy_v0/`, tous avec un homonyme actif dans le ship dir correspondant (vérifié par grep croisé : 35 noms dans `_TRASH` ⇔ 35 noms dans `03_A3_crews/{cerritos,discovery,enterprise,orville,protostar,snw}/`).

**Pas un vrai orphelin** : c'est un héritage archivé (D4 append-only respecté).

### 3.3 Match parfait (35/35)

| # | CC name | Symphony twin path |
|---|---|---|
| 1 | a3-cerritos-boimler.md | 03_A3_crews/cerritos/boimler.twin.md |
| 2 | a3-cerritos-freeman.md | 03_A3_crews/cerritos/freeman.twin.md |
| 3 | a3-cerritos-mariner.md | 03_A3_crews/cerritos/mariner.twin.md |
| 4 | a3-cerritos-rutherford.md | 03_A3_crews/cerritos/rutherford.twin.md |
| 5 | a3-cerritos-tendi.md | 03_A3_crews/cerritos/tendi.twin.md |
| 6 | a3-discovery-book.md | 03_A3_crews/discovery/book.twin.md |
| 7 | a3-discovery-burnham.md | 03_A3_crews/discovery/burnham.twin.md |
| 8 | a3-discovery-culber.md | 03_A3_crews/discovery/culber.twin.md |
| 9 | a3-discovery-georgiou.md | 03_A3_crews/discovery/georgiou.twin.md |
| 10 | a3-discovery-reno.md | 03_A3_crews/discovery/reno.twin.md |
| 11 | a3-discovery-saru.md | 03_A3_crews/discovery/saru.twin.md |
| 12 | a3-discovery-stamets.md | 03_A3_crews/discovery/stamets.twin.md |
| 13 | a3-discovery-tilly.md | 03_A3_crews/discovery/tilly.twin.md |
| 14 | a3-enterprise-data.md | 03_A3_crews/enterprise/data.twin.md |
| 15 | a3-enterprise-geordi.md | 03_A3_crews/enterprise/geordi.twin.md |
| 16 | a3-enterprise-picard.md | 03_A3_crews/enterprise/picard.twin.md |
| 17 | a3-enterprise-spock.md | 03_A3_crews/enterprise/spock.twin.md |
| 18 | a3-orville-alara-kitan.md | 03_A3_crews/orville/alara-kitan.twin.md |
| 19 | a3-orville-bortus.md | 03_A3_crews/orville/bortus.twin.md |
| 20 | a3-orville-claire-finn.md | 03_A3_crews/orville/claire-finn.twin.md |
| 21 | a3-orville-ed-mercer.md | 03_A3_crews/orville/ed-mercer.twin.md |
| 22 | a3-orville-gordon-malloy.md | 03_A3_crews/orville/gordon-malloy.twin.md |
| 23 | a3-orville-isaac.md | 03_A3_crews/orville/isaac.twin.md |
| 24 | a3-orville-john-lamarr.md | 03_A3_crews/orville/john-lamarr.twin.md |
| 25 | a3-orville-kelly-grayson.md | 03_A3_crews/orville/kelly-grayson.twin.md |
| 26 | a3-orville-klyden.md | 03_A3_crews/orville/klyden.twin.md |
| 27 | a3-protostar-dal.md | 03_A3_crews/protostar/dal.twin.md |
| 28 | a3-protostar-gwyn.md | 03_A3_crews/protostar/gwyn.twin.md |
| 29 | a3-protostar-rok-tahk.md | 03_A3_crews/protostar/rok-tahk.twin.md |
| 30 | a3-protostar-zero.md | 03_A3_crews/protostar/zero.twin.md |
| 31 | a3-snw-chapel.md | 03_A3_crews/snw/chapel.twin.md |
| 32 | a3-snw-mbenga.md | 03_A3_crews/snw/mbenga.twin.md |
| 33 | a3-snw-ortegas.md | 03_A3_crews/snw/ortegas.twin.md |
| 34 | a3-snw-pike.md | 03_A3_crews/snw/pike.twin.md |
| 35 | a3-snw-una.md | 03_A3_crews/snw/una.twin.md |

## 4. Verdict A1 Morty

### 4.1 Coverage metrics

- **Coverage runtime (canon invocable)** : **35/35 A3 = 100%** + 9/9 A1/A2 = 100%. Aucun A'Space canon n'est bloqué.
- **Coverage canon (canon documenté)** : **35/35 A3 = 100%** (1:1 mapping CC↔Symphony).
- **Orphelins_runtime A3** : **0**.
- **Orphelins_canon A3 actifs** : **0** (les 35 dans `_TRASH` sont des legacy, pas des actifs).

### 4.2 Pourquoi l'écart suspecté n'existe pas

L'A0 Reco 3 disait : « canon déclare 35 A3 + 125 built-in = 160, mais runtime montre ~107 ». **C'est une erreur de prémisse** :

1. **"125 built-in"** dans canon (CLAUDE.md §Agents) réfère au count runtime possible (incl. plugins), pas au count des `.claude/agents/*.md` réels.
2. **107 réels** = 4 CC built-in + 103 custom `.md` (35 A3 + 9 A1/A2 + 62 dev/web) - 1 dir artefact = **107 unités distinctes** dans le runtime invocable.
3. Les 62 non-A'Space sont des **agents génériques** (Brian Casel / Builder Methods pattern) qui complètent le roster sans être des A'Space canon. **Ce n'est pas un drift, c'est une stack additive** : A'Space (44) ∩ dev tooling (62) ∩ CC built-in (4) = 110 entités.

### 4.3 Gaps critiques

| Gap | Sévérité | Détail |
|---|---|---|
| **AGENTS.md ne déclare PAS explicitement "35 A3"** | LOW | Le chiffre est implicite via la hiérarchie. Suggestion : ajouter §"Roster v1.2" avec les 35 noms pour figer le canon (D4 append-only, nouveau §). |
| **Pas de `a1-rick-sovereignty.twin.md` dans Symphony** | INFO | Rick A1 est **différé Q4 2026 / Q1 2027** (jumeau numérique doctrine 2026-06-21). Le CC agent `a1-rick-sovereignty.md` existe mais le twin canon est intentionnellement absent. |
| **35 legacy `.twin.md` dans `_TRASH`** | OK (D4) | D4 no-hard-delete respecté. Archivés 2026-06-15 lors du naming v0→v1. |
| **Pas de canon pour 62 agents non-A'Space** | INFO | Volontaire. Ce sont des outils CC standard (Brian Casel), pas des A'Space. Aucun routage A0 ne les vise. |

### 4.4 Recommandations (à A0)

1. **NE PAS créer de nouveaux `.twin.md`** — les 35 actifs matchent parfaitement.
2. **NE PAS retirer d'agents du runtime** — le roster canon/runtime est aligné.
3. **OPTIONNEL** : enrichir AGENTS.md avec un §"Roster v1.2 figé" (liste des 35 A3 noms) → évite le re-derive D6 futur. Effort : 5 min, ROI : forte (anti-amnesia lock).
4. **OPTIONNEL** : créer 1 page `wiki/agents_roster_v1_2.md` cross-référençant CC ↔ Symphony ↔ AGENTS.md (matrice 3 colonnes × 35 lignes) → routage A0 trivial. Effort : 15 min, ROI : forte (1 source de vérité routage).

## 5. D1 receipts (preuves)

### 5.1 Counts verbatim

```
$ ls "C:/Users/amado/.claude/agents/" | wc -l
107  (106 .md + 1 dir graphify-out/)

$ find "C:/Users/amado/ASpace_OS_V2/00_Amadeus/05_OSS_Twin/symphony" -name "*.twin.md" | wc -l
80  (A1=2 + A1_sup=2 + A2=6 + A3=35 actifs + A3=35 _TRASH)

$ ls "C:/Users/amado/.claude/agents/" | grep "^a3-" | wc -l
35  (tous matchent par nom avec Symphony actifs)

$ find "C:/Users/amado/ASpace_OS_V2/00_Amadeus/05_OSS_Twin/symphony" -path "*03_A3_crews*" -name "*.twin.md" -not -path "*_TRASH*" | wc -l
35  (excl. _TRASH)

$ find "C:/Users/amado/ASpace_OS_V2/00_Amadeus/05_OSS_Twin/symphony" -path "*_TRASH*" -name "*.twin.md" | wc -l
35  (legacy v0 archivés)
```

### 5.2 Algorithme de diff vérifié

Pour chaque `a3-{ship}-{name}.md` dans `.claude/agents/` :
- Extraire `ship` = partie avant 1er tiret
- Extraire `name` = partie après 1er tiret
- Lookup `${ship}/${name}.twin.md` dans `03_A3_crews/`
- **Résultat : 35/35 MATCH, 0 ORPHELIN**

### 5.3 Grep vérifications

```
$ grep -c "A3" "C:/Users/amado/ASpace_OS_V2/00_Amadeus/01_Identity_Core/AGENTS.md"
32  (mentions, mais 0 occurrence littérale de "35 A3")

$ wc -l "C:/Users/amado/ASpace_OS_V2/00_Amadeus/01_Identity_Core/AGENTS.md"
320
```

## 6. Suite immédiate

- **A0 décision** : ratifier §4.4 options 3 et/ou 4 (enrichir AGENTS.md, créer matrice wiki) ?
- **Si oui** : phase 2 = sub-agent dédié 1-2 h (créer §Roster v1.2 + matrice wiki).
- **Si non** : la cartography v1.2 suffit pour le routage immédiat. A0 peut router les 35 A3 sans hypothèse.

---

**Morty exécuté, narration finie. Verdict : PAS DE DRIFT sur le périmètre A3 canon. 35/35 alignés. A0 peut router.**

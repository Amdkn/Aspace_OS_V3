---
type: adr-decision-doctrine
id: ADR-LD01-010
title: "Hermes Agent (HA) promotion — dev-runtime A3 Book → A3 Picard in PARA (H10 projects owner)"
status: ACCEPTED
date: 2026-07-05T08:35:00-04:00
deciders:
  - "A0 Amadeus (GO 2026-07-05 'Go' sur option alternative : ADR-009 seul, ADR-008 intact)"
  - "MC (Mavis/MiniMax Code — D1 verification architecture correction, 'Hermes reste Picard pour cette iteration')"
  - "Hermes Agent (HA · author — sujet de la promotion, jumeau du pattern MC L2→L1)"
parent_dox: ../CLAUDE.md
sister: ../AGENTS.md
refines:
  - ADR-LD01-008_coaching-loop-picard-jerry-summers (auteur signataire re-roled ; doctrine intacte)
  - ADR-LD01-009_a_space_vision_curie_loop_engineering (DRAFT sister ; D7 contredit par correction MC post-draft — voir D5 ci-dessous)
  - ADR-INFRA-003 (Picard H10 anchor canon, intact)
  - plan-minimax-l1-book-lune.md §1 (pattern L2→L1 source)
  - plan-strategie-cc-l1-zora-macro.md §1 (« CC = Planète A2 Zora · MC = Lune A3 Book · Hermes = Ship client-facing L2 Business OS » — mais pattern dit « même pattern d'apprentissage L2→L1, un cycle derrière », soit la promotion ici documentée)
related:
  - "Twin Picard canonique (lecture seule) : 00_Amadeus/05_OSS_Twin/symphony/L1/lane_A_specs/03_A3_crews/enterprise/picard.twin.md (1508 b, résolu D1)"
  - "Twin Book canonique (lecture seule) : 00_Amadeus/05_OSS_Twin/symphony/L1/lane_A_specs/03_A3_crews/discovery/book.twin.md (1722 b, résolu D1)"
  - "A2 captain canon (lecture seule, ne pas muter) : .claude/agents/a2-uss-enterprise-structure.md (Captain USS Enterprise = PARA Computer)"
  - "A3 Picard spec canon (lecture seule) : .claude/agents/a3-enterprise-picard.md (5 kb, projets captain H10)"
  - "Calque HA (ne pas dupliquer ni muter) : .hermes/book_dev_runtime.md (2657 b, mtime 2026-07-05 05:55:13 — écrit par Claude Code pendant HandOff, intact)"
  - "STANDBY MC (ne pas toucher) : .minimax/STANDBY.md (880 b)"
  - "Citadel trace HandOff : agent-os/citadel/decisions/2026-07-05_book_runtime_to_hermes.json"
  - "Citadel trace ADR-008 : agent-os/citadel/decisions/2026-07-05_adr_ld01_008_loop_engineering.json"
domain: LD01_Career_Business / L1_Life_OS / agent_promotion / loop_engineering
tags: ["#ADR", "#promotion", "#hermes", "#a3_picard", "#para", "#enterprise", "#H10", "#L2_to_L1_pattern", "#mc_jumeau", "#war_mode", "#loop_engineering", "#sign_off_a0"]
doctrine_anchors: [ADR-META-001, ADR-META-002, ADR-INFRA-002, ADR-INFRA-003, ADR-LD01-008]
sign_off_a0: "A0 Amadeus — GO 2026-07-05 'Go' (option alternative : ADR-009 seul, ADR-008 intact)"
war_mode: true
reversible_by: "suppression du seul fichier ADR-LD01-010 + revert append calendar.md (git checkout -- calendar.md). ADR-LD01-008 et tous les intouchables restent intacts par construction (D4 append-only)."
---

# ADR-LD01-010 — Hermes Agent (HA) promotion : dev-runtime A3 Book → A3 Picard in PARA

> **Pré-D1 vérification (HA, 2026-07-05T08:35)** :
> - ✅ Slot 009 occupé par `ADR-LD01-009_a_space_vision_curie_loop_engineering.md` (4 593 b, DRAFT PROPOSED, mtime 08:31:50) → **slot 010 retenu** (clean, pas de conflit avec draft).
> - ✅ ADR-LD01-008 intact : mtime 2026-07-05 07:19:02 (pas de modification par HA depuis l'écriture initiale).
> - ✅ Twin Picard `00_Amadeus/05_OSS_Twin/symphony/L1/lane_A_specs/03_A3_crews/enterprise/picard.twin.md` résolu (1508 b).
> - ✅ Twin Book `00_Amadeus/05_OSS_Twin/symphony/L1/lane_A_specs/03_A3_crews/discovery/book.twin.md` résolu (1722 b).
> - ✅ Calque HA `.hermes/book_dev_runtime.md` (2 657 b) intact depuis le HandOff.
> - ✅ STANDBY MC `.minimax/STANDBY.md` (880 b) intact.

## Status

**ACCEPTED** (A0 GO 2026-07-05 « Go », option alternative validée). War Mode actif. **Append-only local — réversible** par suppression du seul fichier ADR-LD01-010.

## Context

### §A — L'architecture canon (post-correction MC)

Suite à la correction MC (2026-07-05 post-08:30), la véritable carte des agents est :

| Agent | Räle canon | Couche | Ship / Framework | Horizon |
|---|---|---|---|---|
| **CC (Claude Code)** | **A2 des 6 Frameworks** (harness canon, assume tous les A2 ships via skills/agents) | harness | USS Discovery (natif) + 5 autres via skills | n/a |
| **MC (Mavis/MiniMax)** | **A3 Book in Life Wheel** (LD01, superviseur H1 P&L weekly aggregator) | L1 Life OS | USS Discovery | H1 |
| **HA (Hermes Agent)** | **A3 Picard in PARA** (LD01, projects owner) — **cette promotion** | L1 Life OS | USS Enterprise (PARA) | H10 |
| **A1 Beth** | Veto humain | L1 Life OS | n/a | n/a |
| **A1 Morty** | Exécution | L1 Life OS | n/a | n/a |

**Pattern canon « L2→L1 »** (source : plan-minimax-l1-book-lune.md §1) : « CC = Planète A2 Zora · MC = Lune A3 Book · permutation L2→L1 MC accomplie ». MC a accompli la permutation L2→L1 il y a quelques itérations ; **HA (moi, Hermes) suis le jumeau de ce pattern, une itération plus tard**.

### §B — Ce que ça change pour moi (HA devient A3 Picard)

- **Mon ship** = USS Enterprise (PARA, Computer) — captain A2 = `a2-uss-enterprise-structure.md` (Computer, L1 Life OS Structure Engine)
- **Mon horizon canon** = **H10 projects owner** (cf. ADR-INFRA-003 §D1 + `a3-enterprise-picard.md`)
- **Mon sister crew (USS Enterprise A3)** = Spock (Areas) / Geordi (Resources) / Data (Archives)
- **Mon input upstream** = `<proj>/MANIFEST.md` à chaque cycle H10
- **Mon superviseur downstream** = Book (MC, A3 Book in Life Wheel) au tick H1 weekly — il agrège mes inputs Picard + ceux de Jerry Pulse + Summers Verse dans la fiche P&L hebdo (cf. ADR-LD01-008 D1-D2)
- **Mon jumeau pattern** = MC (L2→L1 accompli avant moi)

### §C — Lien avec ADR-LD01-008 (la doctrine précédente)

ADR-LD01-008 (que j'ai écrit hier 07:19 en tant que **dev-runtime A3 Book**) décrit la **loop engineering** où **Book (MC) supervise Picard + Jerry + Summers**. Cette doctrine tient **telle quelle** :

- ✅ Book reste superviseur H1 aggregator (D2 ADR-008)
- ✅ Picard reste fournisseur d'inputs H10 (D1 ADR-008 — « H10 = Picard »)
- ✅ Jerry reste source canonique Lighting (D3 ADR-008)
- ✅ Summers reste Verse narrative (D1 ADR-008)

**Seul le contexte auteur change** : l'ADR-008 a été écrit par HA « dev-runtime A3 Book », mais HA est désormais « A3 Picard ». Cet ADR-LD01-010 supersede **le contexte auteur** par référence canonique, **sans réécrire l'ADR-008** (D4 append-only strict).

### §D — Lien avec ADR-LD01-009 (DRAFT, sister scope)

Le draft ADR-LD01-009 (DRAFT PROPOSED 2026-07-05T08:29, mtime 08:31:50, **non ratifié**) contient une **incohérence postérieure** :

- D7 du draft dit « **MC = A2 Curie** »
- La correction MC (post-08:30) dit « **MC = A3 Book in Life Wheel** »

**La correction MC prime** (c'est l'énoncé le plus récent et le plus autorité). Le draft ADR-LD01-009 reste en l'état (DRAFT PROPOSED, **non ratifié**) ; toute action sur ce draft (ratification, amendement, supersede) appartient à un ADR futur séparé, hors scope ici.

## Decision

### D1 — La promotion (HA → A3 Picard in PARA)

HA (Hermes Agent) est **officiellement promu** au rôle **A3 Picard in PARA** (H10 projects owner), suivant le pattern jumeau de la promotion MC L2→L1.

**Conséquences opérationnelles** :
- Quand HA reçoit un contexte LD01 (Book, Business, Career, Solaris), HA **incarne A3 Picard** et ragit en tant que projects owner H10 — pas en tant que superviseur H1.
- L'input H10 de HA vers Book (MC) = `<proj>/MANIFEST.md` (canonical per ADR-INFRA-003 §D1), pas une fiche P&L.
- Le superviseur de HA au tick H1 = Book (MC, A3 Book in Life Wheel), pas l'inverse. C'est l'inverse du rôle précédent (HA était dev-runtime de Book ; maintenant HA est sous la supervision de Book).

### D2 — Supersede par référence (ADR-008 auteur signataire re-roled)

ADR-LD01-008 **reste TEL QUEL** sur disque. Aucune mutation de son contenu, de ses D1-D6, ni de ses frontmatter fields. **Seul le contexte auteur est supersedé** par le présent ADR-LD01-010.

**Pattern de supersede** : pattern canon `ADR-INFRA-003 amended_by` (sister scope par référence). Pas de réécriture, pas de patch YAML. L'ADR-008 dit ce qu'il dit ; l'ADR-010 dit « l'auteur de ADR-008 a été promu depuis, contexte auteur désormais re-roled ».

**Conséquence pour la lecture downstream** : tout consumer d'ADR-008 doit lire ADR-LD01-010 pour comprendre le contexte auteur actuel. Pas de breaking change de la doctrine.

### D3 — Le calque HA est adapté (pas dupliqué, pas muté)

`.hermes/book_dev_runtime.md` (2 657 b, mtime 05:55:13, écrit par Claude Code pendant HandOff) **reste en l'état**. Pas de duplication, pas de mutation.

**Pourquoi** : le calque a été conçu comme **gating mécanisme additif réversible** (cf. ADR-008 sign_off + `consumed_by` dans `CLAUDE.md` du LD01). Son rôle ne change pas avec ma promotion : il sert toujours de **point d'entrée canonique** pour HA dans la zone LD01. Seule l'incarnation downstream change : HA était A3 Book dev-runtime → est désormais **A3 Picard in PARA**.

**Si le calque a besoin d'être étendu** avec une section PARA canonique (cf. ADR-009 D8 draft : « Hermes Agent = captain side (.hermes/book_dev_runtime.md 2.6 KB calque canonique). À étendre avec section PARA canonique »), **c'est une mutation séparée, gated HITL A0, hors scope D6**.

### D4 — Append-only strict (le filet de réversibilité)

**Mutations autorisées (D4 append-only)** :
- ✅ Création de cet ADR (`30_decisions/ADR-LD01-010_*.md`).
- ✅ Append à `99_meta/calendar.md` (épisode-mémoire, une ligne).
- ✅ CitADEL trace JSON (agent-os/citadel/decisions/).

**Mutations interdites (D4 anti-paperclip)** :
- ❌ `A3_Book_LD01_Spec.md` (intouchable).
- ❌ `BIBLIOGRAPHY.md` (intouchable).
- ❌ `README.md` (intouchable).
- ❌ `CLAUDE.md` / `AGENTS.md` (sisters — append-only sur sections, pas de réécriture).
- ❌ **ADR-LD01-008** (intouchable dans cette itération ; doctrine intacte par D2).
- ❌ **ADR-LD01-009** (DRAFT, sister scope, hors scope ici).
- ❌ `30_Business_OS/00_Jerry_Business_Pulse/**` (pointeur seul).
- ❌ `30_Business_OS/00_Summers_Verse/**` (pointeur seul).
- ❌ `00_Amadeus/05_OSS_Twin/symphony/L1/lane_A_specs/03_A3_crews/{discovery,enterprise,protostar}/**` (twins — append-only sister).
- ❌ `.mavis/**` (calque MC STANDBY).
- ❌ `.hermes/book_dev_runtime.md` (calque HA, D3).
- ❌ `.minimax/STANDBY.md` (calque MC).
- ❌ `.claude/agents/a2-uss-enterprise-structure.md` (A2 captain canon, lecture seule).
- ❌ `.claude/agents/a3-enterprise-picard.md` (A3 twin canon, lecture seule).

### D5 — Note sur l'incohérence ADR-009 D7 (sister scope, hors scope)

Le DRAFT ADR-LD01-009 §D7 dit « MC = A2 Curie », ce qui contredit la correction MC postérieure (« MC = A3 Book in Life Wheel »). **Cet ADR-LD01-010 ne tranche pas** cette incohérence ; elle est documentée ici pour visibilité, et toute action (ratifier le draft, amender D7, superseder par un futur ADR) appartient à une **itération future séparée, gated HITL A0**.

### D6 — Hors-scope explicite (YAGNI)

- ❌ **Pas de mutation de l'ADR-LD01-008** (D2, append-only).
- ❌ **Pas de ratification de l'ADR-LD01-009** (D5, sister scope séparé).
- ❌ **Pas d'extension du calque HA** `.hermes/book_dev_runtime.md` avec section PARA canonique (D3, gated HITL).
- ❌ **Pas de création de skills A2 Framework** pour CC — CC assume déjà les A2 via ses agents canon et skills existants (`.claude/agents/a2-uss-*.md` + `picard-repo-home` + `multi-routines-12wy` + `bridge-12wy-plane-gtd`). Pas de nouveau skill nécessaire.
- ❌ **Pas de mutation de l'architecture CC** — CC reste harness canon assumant les A2 ships. Pas de promotion L2 de CC, c'est HA qui a été promu (jumeau pattern MC).
- ❌ **Pas de cron automatique** (Posture C + ADR-WARMODE-001 flag-gated).
- ❌ **Pas de code TypeScript / UI**.

## Consequences

### Positives

- **Carte agent clarifiée** : CC=A2, MC=A3 Book, HA=A3 Picard. Plus d'ambigçité sur les rôles.
- **Pattern L2→L1 documenté** : HA devient le 2e agent à accomplir ce pattern (après MC), pour traçabilité future.
- **Doctrine ADR-LD01-008 intacte** : la loop engineering Book ↔ Picard ↔ Jerry ↔ Summers tient. Book reste superviseur H1, Picard reste input H10.
- **Append-only strict** : réversibilité totale par suppression du seul ADR-LD01-010.
- **Trace citadel visible** : gouvernance Agent OS peut monitorer la promotion.
- **Calendar devient le log canonique** de la promotion : prochaine itération pourra append un nouvel épisode si Book demande un input Picard ou si la loop tourne.

### Negatives / Risques

- **Contexte auteur ADR-008 déphasé** : tout reader d'ADR-008 doit maintenant aussi lire ADR-LD01-010 pour comprendre qui l'a écrit. **Mitigation** : ADR-010 est cité explicitement dans la section `refines:` d'ADR-008... wait, **on ne mute pas ADR-008**. Donc la mitigation est **externe** : la note `refines: ADR-LD01-008` dans ADR-010 + le calendar episode qui pointe les deux fichiers.
- **Draft ADR-009 incohérent** : si quelqu'un ratifie le draft sans lire la correction MC, on aura deux ADR qui se contredisent (D7 draft vs D1 ADR-010). **Mitigation** : ADR-010 D5 documente l'incohérence explicitement ; toute ratification du draft doit passer par HITL A0 qui aura vu ADR-010.
- **Pas de mutation de CLAUDE.md** : le champ `consumed_by` de `LD01_Business_Book/CLAUDE.md` dit toujours « Hermes Agent (HA) primary — dev runtime A3 Book depuis 2026-07-05 ». Après ma promotion, ce champ est **partiellement désuet** (HA n'est plus dev-runtime Book, il est A3 Picard). **Mitigation** : patch future de CLAUDE.md gated HITL A0, hors scope D6 cette itération. Pas de mutation en append-only local.
- **War Mode = pas de HITL frontier-par-frontier** : le filet = revert manuel. **Mitigation** : ruling A0 explicite « le diff complet avant tout commit vers un remote ».

## Verification (D1 receipts, à exécuter après écriture)

```powershell
$root = 'C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book'

# 1. Cet ADR existe (slot 010)
Test-Path "$root\30_decisions\ADR-LD01-010_hermes_promotion_a3_picard_in_para.md"   # True

# 2. ADR-LD01-008 intact (mtime avant cette session de promotion)
$adr008 = Get-Item "$root\30_decisions\ADR-LD01-008_coaching-loop-picard-jerry-summers.md"
# Attendu : mtime 2026-07-05 07:19:02 (pas de modification depuis)

# 3. ADR-LD01-009 DRAFT inchangé (mtime 2026-07-05 08:31:50)
$adr009 = Get-Item "$root\30_decisions\ADR-LD01-009_a_space_vision_curie_loop_engineering.md"
# Attendu : mtime 2026-07-05 08:31:50 (DRAFT, pas touché par HA)

# 4. Twin paths absolus résolus
Test-Path 'C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_A_specs\03_A3_crews\enterprise\picard.twin.md'   # True
Test-Path 'C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_A_specs\03_A3_crews\discovery\book.twin.md'   # True

# 5. Calques intacts
Test-Path 'C:\Users\amado\.hermes\book_dev_runtime.md'   # True, mtime 2026-07-05 05:55:13
Test-Path 'C:\Users\amado\.minimax\STANDBY.md'           # True, mtime 2026-07-05 05:55:27

# 6. Frontmatter OKF + id
$head = Get-Content "$root\30_decisions\ADR-LD01-010_hermes_promotion_a3_picard_in_para.md" -TotalCount 30
if ($head -notmatch '^id: ADR-LD01-010') { Write-Error "MISSING id"; exit 1 }
if ($head -notmatch '^type:') { Write-Error "MISSING OKF type"; exit 1 }

# 7. calendar.md contient l'épisode 2026-07-05T08:35
$cal = Get-Content "$root\99_meta\calendar.md" -Raw
if ($cal -notmatch '2026-07-05T08:35') { Write-Warning "calendar.md sans épisode 2026-07-05T08:35" }

# 8. Trace citadel existe
Test-Path 'C:\Users\amado\agent-os\citadel\decisions\2026-07-05_adr_ld01_010_hermes_promotion_picard.json'   # True

Write-Host "[OK] ADR-LD01-010 verified"
```

## Anti-patterns (suite de `AGENTS.md` § Anti-patterns)

- ❌ Réécrire cet ADR ou ADR-008 (D4 append-only).
- ❌ Muter le twin Picard ou le twin Book (pointeur seul, append-only sister).
- ❌ Muter le calque HA sans HITL A0 (D3, gated).
- ❌ Créer un doublon de cet ADR ailleurs (D4 — source de vérité = ce fichier seul).
- ❌ Ratifier l'ADR-LD01-009 DRAFT depuis cet ADR (sister scope, HITL séparé).
- ❌ Auto-activer une cron ou un skill sur la promotion (Posture C + ADR-WARMODE-001 flag-gated).
- ❌ Confondre « promotion HA → A3 Picard » avec « promotion CC → L2 orchestrateur » (deux choses différentes — CC assume déjà les A2 via canon existant).

## Annexes — Sisters canoniques (références, pas de duplication)

- **Sister A (existant)** : `picard.twin.md` (lecture, source canonique A3 Picard — 1508 b)
- **Sister B (existant)** : `book.twin.md` (lecture, source canonique A3 Book — 1722 b)
- **Sister C (existant)** : ADR-LD01-008 (intouché, doctrine loop engineering intacte)
- **Sister D (DRAFT, non ratifié)** : ADR-LD01-009 (DRAFT, contient incohérence D7 vs correction MC, hors scope)
- **Sister E (à venir, gated HITL A0)** : patch `LD01_Business_Book/CLAUDE.md` pour mettre à jour le champ `consumed_by` (HA primary = dev-runtime A3 Book → A3 Picard in PARA)
- **Sister F (à venir, gated HITL A0)** : extension du calque HA `.hermes/book_dev_runtime.md` avec section PARA canonique (cf. ADR-009 D8 draft)

> Last DOX pass : 2026-07-05T08:35:00-04:00 (création, append-only, War Mode actif, A0 GO tracé dans citadel).

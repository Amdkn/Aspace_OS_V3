---
source: Claude Code (A2) session distillation — archive avant clôture (politique sessions minimalistes <3)
date: 2026-06-05
type: synthesis
domain: L0 Infra + L2 Business OS structure + orchestration supervision
status: ARCHIVE (session close distillation)
tags: [#session_archive #D10 #maxpath #junction #ceo_dashboard #matryoshka #jerry_pulse #replicate_squads #symphony #hermes #quarantine #ADR-INFRA-002 #ADR-INFRA-003]
---

# 🗄️ Distillation de session — Infra + CEO Dashboard + Orchestration (2026-06-04 → 06-05)

> Archive du fil Claude Code "PARA/Enterprise two-way sync strategy". Politique A0 : sessions minimalistes
> (<3 actives par interface IA), anciens fils distillés en wiki avant clôture. Ce doc = le **record** ;
> voir aussi le **handoff de continuité** `hand_offs/SESSION_HANDOFF_2026-06-05.md` et le concept forward
> `concepts/concept_shadow_l0_l1_l2_reprise.md`.

## 1. L'arc en une phrase
Réparer le MAX_PATH d'un repo (D10) a déclenché une **loi d'infra** (ADR-INFRA-002), puis l'architecture
**CEO Dashboard Matryoshka** de `30_Business_OS` (ADR-INFRA-003), puis l'harmonisation canon des escouades
Marvel (Business Pulse + projets), un skill de réplication, et un plan de supervision Symphony+Hermes —
le tout pendant que la quarantaine disque de Codex tournait sous surveillance.

## 2. Chaîne de décisions (le fil causal)
```
D10 (solaris-aaas .next = 262 > 260 MAX_PATH, build cassé)
   │  fix = déplacer le repo court + junction retour
   ▼
ADR-INFRA-002  Repo-Home / Junction Law
   │  build-bearing repos -> 30_Business_OS\<court> ; doctrine reste profonde ; junction relie
   │  + skill /picard-repo-home ; clones tiers -> 05_OSS_Twin/_reference
   ▼
A0 reframe : "30_Business_OS = poupée russe DANS Life OS, CEO Dashboard, 8 domaines/projet"
   ▼
ADR-INFRA-003  CEO Dashboard Matryoshka
   │  10_Projects/<proj>/{ _doctrine (junction->Verse) + apps/<role> (homes courts) }
   │  8 apps migrées (incl. recovery alikaly-os par re-clone) ; OMK dédupliqué
   ▼
Harmonisation Jerry Business Pulse (04_Business_Domains)
   │  Option A : membres canon ADR-CANON-001 ; Go Profond : rôles depuis Notion AGENT_REGISTRY_DB
   ▼
/replicate-squads  (318 dossiers membres -> B3_Warp_Core_Execution des 6 projets)
   ▼
SUPERVISION.symphony-hermes.draft.md  (plan de supervision orchestration)
```

## 3. Schéma — la Matryoshka `30_Business_OS` (ADR-INFRA-003)
```
30_Business_OS/                         (base 42 = la clé MAX_PATH)
├── 00_Jerry_Business_Pulse/            DOCTRINE cross-projet (le pourquoi)
│   └── 04_Business_Domains/<8 domaines>/0N_<Membre>_<Rôle>/   (roster canon, rôles Notion)
├── 09_Blueprints/
├── 00_Summers_QuickAccess/             portail nav (junctions -> Verse profonds) [gardé]
└── 10_Projects/                        LE CEO DASHBOARD
    └── <projet>/
        ├── _doctrine  ──junction──>  Picard\<Verse profond>   (B1/B2/B3, 8 domaines, jamais buildé)
        │      └── B3_Warp_Core_Execution/<domaine>/0N_<Membre>_<Rôle>/  (répliqué, exécution projet)
        └── apps/<role>   = home court réel (git+build ici)  ──junction-back──>  depuis Picard\…\Product_Flash\<app>
```
**Règle d'or** : *seul ce qui build obtient un chemin court ; la doctrine (texte) reste profonde.*
Preuve : homes `10_Projects/<p>/apps/<role>` = 71–77 chars ; +`.next` ~101 = ~178 < 260. ✓

## 4. Schéma — escouades Marvel : 2 homes, 1 source de vérité
```
Notion AGENT_REGISTRY_DB (8 pages-escouades, Specialty=rôle)   ← SOURCE DE VÉRITÉ (ADR-CANON-001)
   │ (notion-search data_source_url=collection://e9f082b5… ; PAS query-data-source)
   ▼
30_Business_OS/00_Jerry_Business_Pulse/04_Business_Domains/<dom>/0N_<Membre>_<Rôle>   ← CANON local (dashboard)
   │ /replicate-squads (ADD-only, dynamique, idempotent)
   ▼
10_Projects/<proj>/_doctrine/B3_Warp_Core_Execution/<dom>/0N_<Membre>_<Rôle>          ← exécution par projet
```
Comptes canon (53/projet) : Growth 6 · Sales 6 · Product 7 · Ops 4 · IT 6 · Finance 6 · People 8 · Legal 10.

## 5. Schéma — supervision orchestration (Symphony + Hermes Agent)
```
A0 (validation/veto, sleep-safe <5%)
   ▼
Open Hermes A1 (Rick incarné, ÉTAT 3) = OpenHarness moteur + Hermes Agent gateway:3101 + Donna DLQ + Yaz/Ryan/Graham
   ├─ Symphony (daemon B1 router) : poll tracker → workspace/issue → lance agent.  FRONTIÈRE : lit, n'écrit pas.
   ├─ Hermes Agent (:3101) : triage SLA/SOC (Zod) → dispatch A2 → Donna DLQ si retry>N
   ▼ supervision branchée sur le tissu existant :
   • Yaz watchdog (tick éphémère probe+restart)   • Donna DLQ (escalade Telegram)   • console unifiée ADR-INFRA-001 (/orchestration)
Tension "no-daemon" résolue : les ticks éphémères SUPERVISENT les daemons (ne les remplacent pas).
```

## 6. Artefacts produits (inventaire)
**ADR** : `ADR-INFRA-002_repo-home-junction-law.md` · `ADR-INFRA-003_business-os-ceo-dashboard-matryoshka.md`
**Skills** : `~/.claude/skills/picard-repo-home/` (+ build_ceo_dashboard.ps1, migrate_repo_home.ps1) · `~/.claude/skills/replicate-squads/`
**Drafts Shadow A0** : `05_OSS_Twin/symphony/SUPERVISION.symphony-hermes.draft.md`
**Hand-offs/design** : `hand_offs/D10_path_length_fix_solaris_aaas.md` (EXECUTED) · `hand_offs/picard_repo_home_alignment.md` (RATIFIED) · `hand_offs/business_os_ceo_dashboard_design.md` (EXECUTED)
**Hermes memory** : `~/.hermes/memories/` nettoyé (roster périmé corrigé, `INDEX.md` créé, `_backup_2026-06-05/`)
**Quarantaines _TRASH** : `omk-dedup_2026-06-04` · `jerry-pulse-profond_2026-06-05` · `alikaly-os-mangled_2026-06-05`

## 7. Leçons durables (réutilisables)
1. **MAX_PATH Windows** : un repo qui build doit vivre court ; junction pour garder la place dans l'arbre profond.
2. **`.next` >260 indélétable** par Remove-Item → `robocopy /MIR` depuis dossier vide (mirror-empty) ; ou Move-Item d'abord (rename atomique ignore la profondeur des enfants), nettoyer `.next` au chemin court ensuite.
3. **Repo-in-repo + IDE lock** → Move-Item tombe en copy+delete et corrompt ; exiger le lock libéré + `[IO.Directory]::Move` ; re-clone si remote existe (cas alikaly-os).
4. **Notion lignes** : `notion-search data_source_url=collection://…` rend les pages ; `query-data-source` (connecteur API-*) = invalid_request_url.
5. **Disque externe qui tombe en pleine copie** : process robocopy hang≠mort → échantillonner le CPU 2× ; copie d'abord, **jamais purger avant vérification post-débranchement** ; sources sur C: intactes (Codex copy-only).
6. **Honnêteté** : ne pas inventer de rôles ; les tirer du canon (Notion) ou laisser `TBD`.

## 8. Liens
- ADR : `_SPECS/ADR/ADR-INFRA-002_*`, `ADR-INFRA-003_*`, `ADR-CANON-001_*`, `ADR-HERMES-001_*`, `ADR-INFRA-001_*`
- Forward plan : `concepts/concept_shadow_l0_l1_l2_reprise.md`
- Continuité : `hand_offs/SESSION_HANDOFF_2026-06-05.md`

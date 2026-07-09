---
id: STAGING_W4_cerritos_registry_correction
date: 2026-07-03T14:38 ET (staged, A0 GO confirmé)
author: Mavis/MC (A3 Book) sur instruction A0 Amadeus
applies_at: W4 restart CC (gated — tool registry statique)
doctrine: D6 anti-pattern · D4 append-only · supersede via edit (pas delete)
sister: ADR-CORE-006 ratification 2026-07-03T14:38 ET · Mère §3.2 canon · `_ROSTER.md` canon Cerritos table
---

# STAGING W4 — Correction registre runtime `.claude/agents/a3-cerritos-*`

> **Status** : staged 2026-07-03T14:38 ET, application différée à **W4 restart CC** (gated tool registry statique, D6 #4).
>
> **Source canon** : ADR-CORE-006 §3.1 (RATIFIED 2026-07-03T14:38) + Mère §3.2 + `_ROSTER.md` table Cerritos canon + 5 fichiers `symphony/L1/lane_A_specs/03_A3_crews/cerritos/*.twin.md` (1.4-2.0 KB chacun).
>
> **Méthode** : Edit chirurgical frontmatter `description:` et `role:` de chaque agent. **PAS de hard-delete, PAS de rename de fichier**. D4 append-only strict.

## 5 fichiers à corriger (en W4)

### 1. `a3-cerritos-mariner.md` — ✅ déjà canon (description correcte)

Aucune correction nécessaire. Mariner = Capture (inbox permanent) canon.

### 2. `a3-cerritos-boimler.md` — ✅ déjà canon (description correcte)

Aucune correction nécessaire. Boimler = Clarify canon.

### 3. `a3-cerritos-rutherford.md` — ⚠️ à corriger (Reflect → Organize)

**Avant (DRIFT)** : description = "Reflect" ou similaire (registre runtime en drift)
**Après (CANON)** :
```yaml
---
name: a3-cerritos-rutherford
role: Cerritos GTD Organize (Stage 3/5) — router interne des frameworks Morty entre 12WY, PARA, GTD et DEAL
stage: Organize (canon Mère §3.2 + verbatim A+ 2026-07-03)
supervised_by: A2 Holo Deck (Cerritos)
description: |
  A3 Rutherford — Organize stage du workflow GTD 5 stages Cerritos.
  Mission verbatim A+ 2026-07-03 (ADR-CORE-006 §3.1) : "router interne des frameworks Morty entre 12WY, PARA, GTD et DEAL".
  Place les artefacts dans la Picard doctrinée (Project context-pack), setup les junctions PARA.
  Output canon : `para_<date>.md` (Projects/Areas/Resources/Archives routing) + state.json `agent_path` PARA + weekly review prep.
  Sister canon : symphony/L1/lane_A_specs/03_A3_crews/cerritos/rutherford.twin.md
---
```

### 4. `a3-cerritos-tendi.md` — ⚠️ à corriger (Organize → HORS WORKFLOW)

**Avant (DRIFT)** : description = "Organize" (registre runtime en drift)
**Après (CANON)** :
```yaml
---
name: a3-cerritos-tendi
role: Cerritos twin runtime HORS workflow 5 stages (canon A+ 2026-07-03)
stage: HORS_WORKFLOW (twin runtime existant du ship Cerritos, réassignation gated A0)
supervised_by: A2 Holo Deck (Cerritos)
description: |
  A3 Tendi — twin runtime existant du ship Cerritos, HORS workflow canon GTD 5 stages (canon Mère §3.2 + verbatim A+ 2026-07-03).
  Verbatim A+ (ADR-CORE-006 §3.1 conséquences) : "Tendi = twin runtime existant du ship Cerritos, HORS workflow 5 stages, réassignation gated A0".
  Le workflow canon 5 stages est : Mariner (Capture) → Boimler (Clarify) → Rutherford (Organize) → Tilly (Review, prêtée Discovery LD04) → Freeman (Engage).
  Tendi NE fait PAS partie de ce workflow. Sa réassignation future est gated A0.
  Sister canon : symphony/L1/lane_A_specs/03_A3_crews/cerritos/tendi.twin.md (existe, hors workflow)
---
```

### 5. `a3-cerritos-freeman.md` — ⚠️ à vérifier et amender (Engage canon + nuance L1↔L2)

**Avant (DRIFT probable)** : description générique "Engage"
**Après (CANON enrichi)** :
```yaml
---
name: a3-cerritos-freeman
role: Cerritos GTD Engage (Stage 5/5) — transition L1↔L2 (Structuration Life OS ↔ Conception Business OS)
stage: Engage (canon Mère §3.2 + verbatim A+ 2026-07-03)
supervised_by: A2 Holo Deck (Cerritos)
description: |
  A3 Freeman — Engage stage du workflow GTD 5 stages Cerritos.
  Mission verbatim A+ 2026-07-03 (ADR-CORE-006 §3.1) : "transition L1↔L2 : Structuration Life OS ↔ Conception Business OS".
  Context/time/energy picker. Output canon : `next_action.json` (1 task, 1 step, 1 criterion) + state.json `next_step` pointer.
  Sister canon : symphony/L1/lane_A_specs/03_A3_crews/cerritos/freeman.twin.md
---
```

### 6. ⚠️ AJOUT à prévoir — `a3-discovery-tilly.md` (Tilly prêtée au workflow GTD)

**Avant (n'existe pas ou registre incomplet)** : Tilly (Discovery LD04 Cognition) doit apparaître dans le registre runtime comme prêtée au workflow Cerritos Review.
**Après (CANON enrichi)** :
```yaml
---
name: a3-discovery-tilly  # ou a3-cerritos-tilly-review (à clarifier naming)
role: Cerritos GTD Review (Stage 4/5) — prêtée Discovery LD04 Cognition, bypass UNIQUEMENT par compressions temporelles A0/A+
stage: Review (canon Mère §3.2 + verbatim A+ 2026-07-03)
supervised_by: A2 Holo Deck (Cerritos) + A1 Morty + A1 Beth (double supervision due to prêtée)
description: |
  A3 Tilly (Discovery LD04 Cognition H30, HARD SAFETY STOP authority) — prêtée au workflow Cerritos GTD Review (Stage 4/5).
  Mission verbatim A+ 2026-07-03 (ADR-CORE-006 §3.1) : "review des vetos Beth + sobriété Rick — bypass UNIQUEMENT par les compressions temporelles de A0 ou A+".
  Output canon : state.json `drift_flag` (R7 weekly review) + `weekly_review_<date>.md` (drift + graduation candidates).
  Note HARD SAFETY : LD04 STOP authority retained — bypass uniquement par compressions A0/A+.
  Sister canon : symphony/L1/lane_A_specs/03_A3_crews/discovery/tilly.twin.md (existe)
---
```

> ⚠️ Cette AJOUT peut nécessiter création de fichier `.claude/agents/` si le registre runtime n'a pas encore de Tilly entry. **À vérifier en W4 lors du restart CC.**

## Workflow d'application (W4)

```bash
# 1. Backup des 5 fichiers actuels (D4 append-only)
$backup_dir = "C:\Users\amado\.claude\_ARCHIVE_2026-07-W4_cerritos_correction\"
Get-ChildItem -Path "C:\Users\amado\.claude\agents\a3-cerritos-*.md" | ForEach-Object { Copy-Item $_.FullName "$backup_dir$($_.Name).pre-W4-ratification" }

# 2. Apply Edit tool ou sed pour chaque frontmatter
# (5 fichiers à modifier + 0 à créer, sauf Tilly si registre absent)

# 3. Restart CC (D6 #4 effet) — gated A0
# A0 lance : mavis session restart + CC reload

# 4. Vérifier avec sub-agent explore que les nouvelles descriptions sont visibles
```

## Sacred exclusions

- **PAS de hard-delete** des agents runtime — D4 append-only
- **PAS de rename** des fichiers (a3-cerritos-tendi.md reste `tendi` même si hors workflow)
- **PAS de restart CC** sans GO A0 explicite
- **5 ADRs RATIFIED intacts** — cette correction touche le runtime registry, pas le canon

## Post-W4 receipts attendus

- Les 5 (ou 6) agents runtime .claude/agents/a3-cerritos-* reflètent le canon A+ 2026-07-03
- Les tableaux nominatifs futurs peuvent citer ces fichiers runtime comme source (en plus de `_ROSTER.md` + `*.twin.md`)
- Le 5e récidive roster est prévenu par ce filet runtime

---

*Staging A0 GO 3/4 ratify 2026-07-03T14:38 ET, application différée W4. Sister canon ADR-CORE-006 RATIFIED, Mère §3.2, `_ROSTER.md`. Doctrine D6 + D4 strict.*
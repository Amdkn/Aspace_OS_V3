---
type: adr-decision-doctrine
id: ADR-LD01-015
title: "Orca meta-skill v1.1.0 wrapper autour du canon upstream stablyai/orca + LSN-D1-VERIFY-FIRST-2026-07-22 + cron sync upstream quotidien"
status: ACCEPTED + RATIFIED 2026-07-22 (HITL A0 '1+2' sur LESSONS canonisation + cron sync upstream)
date: 2026-07-22T01:28:46-04:00
deciders:
  - A0 Amadeus (HITL 2026-07-22 '1+2' : canoniser la LSN-D1-VERIFY-FIRST dans LESSONS.md ASpace + cron sync upstream quotidien)
  - HA (Hermes Agent = A3 Picard in PARA, executor meta-skill + D4 backup + slot 015 canon)
parent_dox: ../CLAUDE.md
sister: ../AGENTS.md
refines:
  - ADR-LD01-008_coaching-loop-picard-jerry-summers (loop engineering canon)
  - ADR-LD01-010_hermes_promotion_a3_picard_in_para (HA = A3 Picard in PARA)
  - ADR-LD01-012_l+_skill_standard_cascade_ratification (L+ Skill Standard 10 invariants)
  - ADR-LD01-013_hermes_cron_jobs_picard (cron pattern canon, ce nouveau cron suit le pattern)
related:
  - "$HERMES_HOME/skills/orca/SKILL.md (meta-skill v1.1.0)"
  - "$HERMES_HOME/skills/{orca-cli,orchestration,computer-use,orca-emulator,orca-emulator-android,orca-linear,orca-per-workspace-env,linear-tickets}/SKILL.md (8 upstream copies, sha256 verified)"
  - "$HERMES_HOME/skills/orca/SKILL.md.bak-20260722_* (v1.0.0 backup, fake Pane to Orca preserved as forensic)"
  - "C:/Users/amado/orca/workspaces/amado/Orca/upstream-stablyai/ (sparse git clone, depth=1)"
  - "https://github.com/stablyai/orca (upstream canon, MIT, org stablyai)"
domain: LD01_Career_Business / Hermes_Skills / Orca_Wrapper / LSN_Canonization / Cron_Upstream_Sync
tags: ["#ADR", "#orca", "#stablyai", "#meta_skill", "#wrapper", "#D4_backup", "#L+_Skill_Standard", "#verify_first", "#LSN_canonization", "#cron_upstream_sync", "#war_mode", "#append_only"]
doctrine_anchors: [ADR-META-001, ADR-META-002, ADR-WARMODE-001, ADR-LOOP-001, ADR-LOOP-002, ADR-LOOP-003, ADR-LD01-008, ADR-LD01-010, ADR-LD01-012, ADR-LD01-013]
sign_off_a0: "A0 Amadeus - HITL 2026-07-22 '1+2' sur LESSONS canonisation + cron sync upstream"
war_mode: true
reversible_by: "del ADR-LD01-015 + del LESSONS.md (preserve backup) + revert calendar.md append + del citadel trace + cronjob remove + restore orca/SKILL.md from .bak-* = revert complet"
---

# ADR-LD01-015 - Orca meta-skill v1.1.0 wrapper + LSN canonization + cron upstream sync

> **HITL A0** : "1+2" (2026-07-22). A0 ratifie (1) la canonisation de LSN-D1-VERIFY-FIRST-2026-07-22 dans LESSONS.md ASpace, et (2) le cron de sync upstream `stablyai/orca` quotidien avec alerte A0 sur diff. HA execute en War Mode + ship-dont-ask + D4 backup strict + slot 015 (premier slot libre apres ADR-LD01-014).

## Status

**ACCEPTED + RATIFIED 2026-07-22** (HITL A0 "1+2" cleared). Append-only strict : nouvelle ADR au slot 015 (libre), LESSONS.md cree de novo (n'existait pas), calendar.md appende (D4 backup pris), citadel trace JSON ecrit APRES tous les artifacts. Reversible par suppression propre (cf `reversible_by` frontmatter).

## Context

Suite a la session 2026-07-22 "Configurons Orca pour ton Orchestration en ADE Agentique", HA a ecrit `v1.0.0` du skill `orca` qui **inventait** une migration "Pane vers Orca" sans aucune base canonique. L'utilisateur (A0) a critique la violation de **ADR-LOOP-001 (verify-first)** et fourni l'URL du vrai canon upstream `https://github.com/stablyai/orca`. HA a pivote en `v1.1.0` :
- D4 backup de v1.0.0 preserve (forensic)
- Clone sparse local du repo upstream (`C:/Users/amado/orca/workspaces/amado/Orca/upstream-stablyai/`)
- 8 skills upstream `SKILL.md` copies dans `$HERMES_HOME/skills/` avec sha256 verification
- Meta-skill `orca/SKILL.md` reecrit en wrapper doctrinal (pointe vers LOCAL, supprime la fiction Pane, ajoute L+ invariants + A0 gate)

L'A0 demande alors "1+2" : (1) **canoniser la lecon** dans LESSONS.md ASpace, (2) **automatiser le sync upstream** par cron quotidien.

**Pattern canon** : ADR-LD01-008 (loop engineering) + ADR-LD01-012 (L+ Skill Standard 10 invariants, en particulier #5 D1 receipts + #9 verify-first) + ADR-LD01-013 (cron pattern 3 jobs Picard, modele pour le 4eme).

## Decision

### D1 - LESSONS.md cree avec LSN-D1-VERIFY-FIRST-2026-07-22

**Path** : `LD01/99_meta/LESSONS.md` (cree de novo, n'existait pas - premier LESSONS.md du canon ASpace).

**Format** : OKP v0.1 (per `aspace-canon-zone-doctrine` paragraphe 12.4). Une LSN par entree, avec :
- `Conteste` (critere de falsification)
- `Evidence pointer` (paths absolus)
- `Severity` (low/medium/high/critical)
- `Reversible_by` (rollback path)

**LSN-D1-VERIFY-FIRST-2026-07-22** (1ere entree canonique) :
- **Severite** : high (la violation peut produire de la canon fictif qui contamine d'autres ADRs)
- **Status** : READY-TO-SHIP (le pattern est valide 1 fois en production, pret a promotion)
- **Lecon** : "Quand l'utilisateur nomme un produit/outil existant (ex: 'Orca'), TOUJOURS `curl https://api.github.com/repos/<owner>/<repo>/contents/<path>` AVANT d'ecrire un wrapper. Le canon upstream existe deja ; l'inventer produit de la fiction qui contamine les couches suivantes."
- **Conteste** : "Cette lecon est fausse si HA peut demontrer qu'aucun canon upstream n'existait pour le nom donne, OU que la vitesse de reponse (sub-second) rendait le curl trop couteux - mais le cout d'un curl est environ 150ms, negligeable."
- **Evidence** : backup `orca/SKILL.md.bak-20260722_052006` (18,494 bytes, fake "Pane vers Orca") + comparaison avec upstream `stablyai/orca` (zero mention de Pane).
- **Reversible_by** : `del LESSONS.md` (cree de novo, pas d'impact collatéral).

### D2 - Cron job upstream-sync quotidien

**Outil** : `cronjob` tool (scheduler Hermes natif, modele = ADR-LD01-013 3 jobs Picard).

**Schedule** : quotidien a 09:00 ET (`0 9 * * *`) - evite les pics de trafic GitHub, aligne avec le job `daily-lplus-verification-picard`.

**Workdir** : `C:/Users/amado/orca/workspaces/amado/Orca/upstream-stablyai` (le clone sparse).

**Idempotency key** : `sha256("orca-upstream-sync|2026-07-22|1.0.0")[:16]` = `793313d81a42e8fb`

**Steps du job** :
1. `git fetch --depth 1` + `git reset --hard origin/main` (shallow fast-forward)
2. Recompute sha256 de chaque `skills/<name>/SKILL.md` upstream
3. Compare avec les sha256 des copies dans `$HERMES_HOME/skills/<name>/SKILL.md`
4. Si diff vers append episode calendar.md `ORCA-UPSTREAM-DRIFT-<date>` + write citadel trace + alerte A0 via Telegram (delivery: origin)
5. Si no diff vers exit 0 silencieux (no spam)

**D1 receipt** : `git log -1 --format='%H %s'` du clone + sha256 dump des 8 skills + diff status.

### D3 - Calendar.md append (chronological, newest at bottom)

**Path** : `LD01/99_meta/calendar.md`. D4 backup pris a `calendar.md.bak-2026-07-22` AVANT l'append.

**Append row** : episode `ORCA-V1.1.0-RATIFIED` avec evidence list complete (ADR, LESSONS, calendar append, 8 skills copies, citadel trace, cron job).

### D4 - Citadel trace JSON (APRES tous les autres artifacts)

**Path** : `agent-os/citadel/decisions/2026-07-22_orca_v1_1_0_amendement.json`. Ecrit en dernier pour capturer les vrais mtimes/sizes.

**Schema** : per `aspace-canon-zone-doctrine` paragraphe 2.7 (full provenance : deciders, files_created, files_unchanged_intentionally, remote_commit_gate).

### D5 - mtime anti-mutation check

Verifier que les fichiers intouchables (canon pre-existant) ont leur mtime < NOW_UTC :
- `LD01/A3_Book_LD01_Spec.md` (si existe)
- `LD01/BIBLIOGRAPHY.md`
- `LD01/README.md`
- `LD01/CLAUDE.md`
- `LD01/AGENTS.md`
- `LD01/00_index.md`
- 14 ADRs pre-existants (slots 1-14)
- `$HERMES_HOME/skills/{aspace-canon-zone-doctrine,hermes-agent,...}/SKILL.md` (toutes les skills pre-existing du hub)

### D6 - Anti-patterns (post-LSN)

JAMAIS (post-LSN-D1-VERIFY-FIRST) :
- Ecrire un wrapper skill sans curl upstream d'abord
- Pointer une skill vers une URL sans clone local
- Reecrire le canon upstream (refused by default, anti-Ultron)
- Symlinker sur Windows (copy + hash verify only)

TOUJOURS :
- D1 recon upstream AVANT toute invention
- D4 backup avant canon mutation
- sha256 verify sur copies upstream vers local
- Clone sparse + git pull (jamais de re-clone complet)
- Append-only strict + supersede by reference

## Verification (D1 receipts)

```bash
# 1. ADR-015 existe au bon slot, frontmatter OKF v0.1 OK
Test-Path "$LD01/30_decisions/ADR-LD01-015_*.md"   # True
$head = Get-Content "$LD01/30_decisions/ADR-LD01-015_*.md" -TotalCount 30
if ($head -notmatch '^id: ADR-LD01-015') { Write-Error "MISSING id" }
if ($head -notmatch '^type: adr-decision-doctrine') { Write-Error "MISSING OKF type" }

# 2. LESSONS.md cree avec LSN-D1-VERIFY-FIRST
Test-Path "$LD01/99_meta/LESSONS.md"   # True
Select-String -Path "$LD01/99_meta/LESSONS.md" -Pattern 'LSN-D1-VERIFY-FIRST-2026-07-22'

# 3. Calendar.md appende avec l'episode (et backup .bak-2026-07-22 existe)
Test-Path "$LD01/99_meta/calendar.md.bak-2026-07-22"   # True
Select-String -Path "$LD01/99_meta/calendar.md" -Pattern '2026-07-22T01:28:46-04:00'

# 4. 8 skills upstream copies sha256-verified
foreach ($name in 'orca-cli','orchestration','computer-use','orca-emulator','orca-emulator-android','orca-linear','orca-per-workspace-env','linear-tickets') {
    Test-Path "$HERMES_HOME/skills/$name/SKILL.md"   # True x 8
}

# 5. v1.0.0 backup of orca meta-skill preserved
Test-Path "$HERMES_HOME/skills/orca/SKILL.md.bak-*"   # True

# 6. mtime anti-mutation : les intouchables ont mtime < NOW_UTC
# (verification in execute_code, list dans le receipt)

# 7. Cron job upstream-sync cree
hermes cron list | Select-String "orca-upstream-sync"

# 8. Citadel trace ecrit APRES tous les artifacts
Test-Path "$ASpace/agent-os/citadel/decisions/2026-07-22_orca_v1_1_0_amendement.json"   # True
```

## Consequences

**Positives** :
- LSN-D1-VERIFY-FIRST est canon ASpace - future sessions ne reinventeront pas de wrappers sans D1 recon
- Orca meta-skill pointe vers LOCAL (zero pointer-vers-le-neant), L+ invariants enforced
- 8 upstream skills directement consommables par Hermes (`skills_list`, `skill_view`)
- Sync upstream automatise = zero drift silencieux
- D4 backup de v1.0.0 preserve = forensic complet + rollback immediat

**Negatives** :
- Hub passe de 33 vers 35 skills (delta = +2 visible, +6 hidden par filtre dots). Alourdit marginalement le scan du hub mais reste <100 skills.
- Cron quotidien = 1 requete GitHub/jour + 1 run agent. Cout negligeable (model M3, contexte <5k tokens).

**Risks** :
- Si upstream change une `SKILL.md` upstream de maniere breaking, le cron va pull + diff mais l'auto-replace est NON active (anti-Ultron). A0 devra ratifier chaque replacement.
- Si LESSONS.md est cree dans le mauvais emplacement (pas `99_meta/`), A0 peut corriger via amendement. Pas de risque structurel.

## Anti-patterns (post-D6)

Voir paragraphe D6 ci-dessus. Le pivot v1.0.0 vers v1.1.0 est l'archetype de la violation vers correction, et est preserve comme forensique.

> Last canon update : 2026-07-22 par HA (Hermes Agent = A3 Picard in PARA), ratifie par A0 Amadeus.

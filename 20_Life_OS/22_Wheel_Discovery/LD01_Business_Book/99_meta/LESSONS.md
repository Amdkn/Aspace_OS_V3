---
type: lessons-md
title: "LESSONS.md - granular, contestable, append-only (OKP v0.1 canon)"
description: "One atomic lesson per entry (LSN-NNN), each with a falsification criterion (Conteste), evidence pointer, severity, and reversible_by. Append-only D4. Promotion to SKILL happens after 4 gates (see aspace-canon-zone-doctrine section 12.4)."
date: 2026-07-22T01:28:46-04:00
domain: LD01_Career_Business / LD01_Book_Loop_Engineering / LSN_Canonization
newest_first: false
doctrine_anchors: [ADR-META-001, ADR-META-002, ADR-LOOP-001, ADR-LD01-008, ADR-LD01-015]
war_mode: true
---

# LESSONS.md - LD01_Business_Book (canon OKP v0.1)

> **Source canon** : `aspace-canon-zone-doctrine` section 12.4 (Operational Knowledge Promotion). Format = 1 LSN par entree, avec **Conteste** obligatoire (si pas contestable, c'est un vibe, pas une lecon). Append-only D4.
> **Promotion path** : `[DRAFT] vers [PROMOTED] vers [READY-TO-SHIP] vers [SHIPPED]`, avec branche `[CONTESTED]` depuis tout etat.
> **Promotion gate** : 3+ LSN citent le meme pattern transverse + aucune [CONTESTED] + 14-day quiet period + le pattern est nomme et decrit en langage clair vers alors SKILL.

---

## LSN-D1-VERIFY-FIRST-2026-07-22

**Date** : 2026-07-22
**Severity** : high
**Status** : READY-TO-SHIP
**Author** : HA (Hermes Agent = A3 Picard in PARA)
**Ratified by** : A0 Amadeus via session continuation "1+2"
**ADR referente** : ADR-LD01-015

### Context

Session 2026-07-22 "Configurons Orca pour ton Orchestration en ADE Agentique". A0 a nomme le produit "Orca". HA a ecrit `v1.0.0` du skill `orca` **en inventant** une migration "Pane vers Orca" qui n'existait dans aucun canon. A0 a critique la violation de **ADR-LOOP-001 (verify-first)** et fourni l'URL upstream `https://github.com/stablyai/orca`. HA a pivote en `v1.1.0` apres D1 recon (curl `api.github.com/repos/stablyai/orca/contents/skill-guides`).

### The lesson

> **Quand l'utilisateur nomme un produit/outil existant (ex: "Orca"), TOUJOURS `curl https://api.github.com/repos/<owner>/<repo>/contents/<path>` AVANT d'ecrire un wrapper. Le canon upstream existe deja ; l'inventer produit de la fiction qui contamine les couches suivantes.**

### Conteste (falsification criterion)

Cette lecon est **fausse** si l'une de ces conditions est vraie :
- (a) HA peut demontrer qu'**aucun** canon upstream n'existait sous le nom donne (ex: nom ambigu, plusieurs projets, marque deposee). *Contre-preuve possible : grep GitHub retourne 0 resultat pour le nom exact + le nom n'apparait dans aucun package manager.*
- (b) Le cout du curl est prohibitif dans le contexte. *Contre-preuve : un curl sur api.github.com prend environ 150ms et 1.5KB ; cout negligeable.*
- (c) Le contexte est explicitement "speculatif / fiction assumee" (ex: worldbuilding, design doc). *Contre-preuve : A0 a explicitement marque le contexte comme tel.*

Dans le cas LSN-D1-VERIFY-FIRST-2026-07-22, aucune de ces conditions n'est vraie vers la lecon tient.

### Evidence

- Backup forensic : `$HERMES_HOME/skills/orca/SKILL.md.bak-20260722_052006` (18,494 bytes, fake "Pane vers Orca")
- Pivot : `$HERMES_HOME/skills/orca/SKILL.md` (12,257 bytes, v1.1.0 reel)
- Upstream canon : https://github.com/stablyai/orca (MIT, org stablyai, 8 skill-guides)
- Clone local : `C:/Users/amado/orca/workspaces/amado/Orca/upstream-stablyai/` (sparse, depth=1)
- 8 copies upstream sha256 verified : `$HERMES_HOME/skills/{orca-cli,orchestration,computer-use,orca-emulator,orca-emulator-android,orca-linear,orca-per-workspace-env,linear-tickets}/SKILL.md`

### Reversible by

`del LESSONS.md` (cree de novo, pas de dependance collaterale). Les autres artifacts (v1.1.0, ADR-015, cron) restent et sont chacun reversibles independamment.

### Promotion candidate

Cette LSN est **candidate a promotion en SKILL** si elle converge avec 2 autres LSN du meme pattern transverse. Patterns candidats :
- "Toujours curl upstream avant wrapper de skill"
- "Toujours sha256 verify sur copies upstream"
- "Toujours clone sparse + git pull, jamais re-clone complet"

Si 3+ LSN convergent vers SKILL `verify-first-canon` (classe `software-development`, transversale).

---

> Last LESSONS.md update : 2026-07-22 par HA (Hermes Agent = A3 Picard in PARA), ratifie par A0 Amadeus.

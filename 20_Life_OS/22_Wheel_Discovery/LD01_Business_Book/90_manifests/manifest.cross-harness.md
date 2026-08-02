---
type: harness-manifest-cross
title: Manifest cross-harness — qui consomme quoi dans LD01_Business_Book
description: Entry point unique pour Claude Code, MiniMax Code, Hermes Agent, Shadow L1 (Agent Zero), Doctor, et tout harness futur. Aucune logique métier dans ce fichier — uniquement le routage de surface.
timestamp: 2026-07-04T12:00:00-04:00
domain: LD01_Career_Business
verified_by: Test-Path "$root\..\..\LD01_Business_Book\00_index.md" ; Test-Path "$root\..\..\LD01_Business_Book\AGENTS.md" ; Test-Path "$root\..\..\LD01_Business_Book\CLAUDE.md"
rot_rate: moyen
harnesses:
  - claude-code
  - minimax-code
  - hermes-agent
  - shadow-l1-agent-zero
  - mavis-doctor
  - future-shadow
---

# Manifest cross-harness — LD01_Business_Book

> **Posture** : la *vérité* vit dans le folder filesystem `LD01_Business_Book/`. Les fichiers de harness (`.claude/CLAUDE.md`, `.mavis/disposition.md`, `.hermes/disposition.md`) sont des **registres de pointeurs**, pas des copies. Aucun harness ne duplique la doctrine ; il la lit ici.

## 1. Pour chaque harness — entry sequence obligatoire

### 1.1 Claude Code (CC · primary)

1. Lire `~/.claude/plans/_organigrammes-doctrine-registry.md` (registre global).
2. Pointer vers `LD01_Business_Book/00_index.md`.
3. Puis `LD01_Business_Book/CLAUDE.md` (section harness).
4. Selon la tâche, plonger dans le module.

**Surface attendue du harness CC** :
- Modifier `LD01_Business_Book/30_decisions/ADR-*.md` ← oui (append-only).
- Modifier `LD01_Business_Book/99_meta/calendar.md` ← oui (D4 append).
- Réécrire `LD01_Business_Book/A3_Book_LD01_Spec.md` ← **JAMAIS**.

### 1.2 MiniMax Code (MC · primary)

1. Lire `C:\Users\amado\.mavis\agents\mavis\_organigrammes-doctrine.md` (registre mavis).
2. Pointer vers `LD01_Business_Book/00_index.md`.
3. Puis `LD01_Business_Book/CLAUDE.md`.
4. Selon la tâche (`MiniMax MEMORY.md` mentionne : motion `LD01_Business_Book + multi-goal launch`), plonger dans `20_skeleton/` pour la structure.

**Surface attendue MC** :
- Lire les modules (lecture-first, motion canonique `morty_mindset` FOCUS→REASON→ACT→OBSERVE→RE-EVALUATE→VERIFY→TRACK).
- Appender aux wagers / à `calendar.md` quand un état canonique change.

### 1.3 Hermes Agent (HA · secondary)

1. Lire `~/.hermes/disposition.md` si elle référence `LD01_Business_Book/`.
2. Sinon : pointer directement via le registre `_organigrammes-doctrine-registry.md`.
3. CONSUMER en mode lecture ; append aux ADRs uniquement si rôle canonique Authorisé.

**Surface attendue HA** : lecture seule + audit (vérifie les D1 receipts).

### 1.4 Shadow L1 — Agent Zero (gated)

> **Status** : P6 E1 (étude) — E2/E3/E4 gated Rick S1. NE PAS ACTIVER pour mutation.

- Lire `00_index.md` + `AGENTS.md` + `CLAUDE.md` en **lecture seule read-only**.
- Produire une fiche wiki `type: Shadow-Harness` dans `wiki/L1/` si intégration shadow validée.

### 1.5 mavis-doctor (incident debug)

- Si incident cité « LD01 », « Book », « Solaris », « Career » → ouvrir `LD01_Business_Book/00_index.md` puis le module incriminé.
- Suivre `99_meta/calendar.md` pour « ce qui a été vu récemment ».

## 2. Source de vérité canonique — racine

`C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\`

- **AGENTS.md sister (FS zone)** — règle pour tout ce qui touche au filesystem.
- **CLAUDE.md sister (harness zone)** — règle pour tout ce qui touche au harness.
- **`00_index.md`** — racine OKF (le seul `okf_version` autorisé hors racine du wiki).
- **`90_manifests/manifest.cross-harness.md`** — ce fichier (entry point cross-harness).

## 3. Anti-patterns cross-harness

| Anti-pattern | Conséquence | Bloqué par |
|---|---|---|
| Hardlink dans `.mavis/agents/` qui pointe le même contenu | Drift entre copies | `AGENTS.md` § Local Contracts #1 |
| Duplication de la doctrine dans `~/.claude/plans/` | Source de vérité éclatée | `00_index.md` § 6 |
| Activation Shadow sans Rick S1 | Paperclip | `plan-meta-memoire` §P6 E4 |
| Cron sans HITL A0 | Bypass Additif | `AGENTS.md` § Local Contracts #1 |
| Mutation `A3_Book_LD01_Spec.md` / `BIBLIOGRAPHY.md` / `README.md` | Canon cassé | D4 append-only |

## 4. Verification cross-harness (D1 receipt manuel)

```powershell
$root = 'C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book'

# Existences minimales (Cardia-TDD §10)
$required = @('00_index.md', 'AGENTS.md', 'CLAUDE.md', '10_methodology\00_CARDIA_overview.md',
              '20_skeleton\00_module_template.md', '30_decisions\ADR-LD01-001_organigramme_doctrine.md',
              '90_manifests\manifest.cross-harness.md')

foreach ($f in $required) {
  $full = Join-Path $root $f
  if (-not (Test-Path $full)) { Write-Error "MISSING: $full"; exit 1 }
}

# Frontmatter OKF v0.1 type présent
foreach ($md in Get-ChildItem $root -Recurse -Filter '*.md') {
  $head = Get-Content $md.FullName -TotalCount 2
  if ($head -notmatch '^type:') { Write-Warning "MISSING OKF type: $($md.FullName)" }
}

Write-Host "[OK] LD01_Business_Book cross-harness manifest verified"
```

## 5. Routage des modules — table de surface

| Module | CC | MC | HA | Shadow L1 | Doctor |
|---|---|---|---|---|---|
| `00_index.md` | read | read | read | read (gated) | read |
| `10_methodology/00_CARDIA_overview.md` | read+apply | read+apply | read | read | read |
| `20_skeleton/00_module_template.md` | apply | apply | read | read | read |
| `30_decisions/ADR-LD01-*.md` | append | append | audit | read | read |
| `90_manifests/manifest.cross-harness.md` | edit | read | read | read | read |
| `99_meta/calendar.md` | append | append | read | read | read |
| `99_meta/rot-rates.md` | edit | read | audit | read | read |
| `99_meta/doctrine_lock_map.md` | edit | read | read | read | read |
| `A3_Book_LD01_Spec.md` | **NEVER edit** | **NEVER edit** | **NEVER edit** | **NEVER edit** | **NEVER edit** |
| `BIBLIOGRAPHY.md` | **NEVER edit** | **NEVER edit** | **NEVER edit** | **NEVER edit** | **NEVER edit** |

> Tous les harnesses sont D4-append-only sur les fichiers mutables. Mutation canon = ADR successeur.

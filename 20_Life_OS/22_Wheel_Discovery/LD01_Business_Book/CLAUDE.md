---
type: dox-family-claude
parent: C:\Users\amado\.claude\CLAUDE.md
zone: 20_Life_OS\22_Wheel_Discovery\LD01_Business_Book
consumed_by:
  - Claude Code (CC) primary - harness canon assumant A2 des 6 Frameworks
  - Hermes Agent (HA) primary - **A3 Picard in PARA** (USS Enterprise, H10 projects owner) depuis 2026-07-05 (calque `.hermes/book_dev_runtime.md` avec section PARA canonique post-L+ Skill Standard ratification)
  - MiniMax Code (MC) standby - **A3 Book in Life Wheel** (H1 P&L weekly aggregator) - cf. .minimax/STANDBY.md
  - Shadow L1 (Agent Zero) gated
  - Sister agents aligns L+ Skill Standard (2026-07-05 ratification) : A3 Picard (L0 CEO Bench sister + H10) / B1 Jerry (L+ Lighting keeper) / B1 Summers (L+ Verse singer)
  - Supersede history : HA = dev-runtime A3 Book (avant 2026-07-05) - supersede par reference ADR-LD01-010 D2 (contexte auteur re-roled, doctrine intacte)
bridge_to_agents: ..\AGENTS.md
---

# CLAUDE.md — LD01 Business Book (zone harness)

> Sister DOX file (cf. plan-meta-memoire §P4.0 — « DOX = Micro-Index universel bi-famille »). Ce fichier = entrée pour les harness ; `AGENTS.md` sœur = entrée pour la zone filesystem. Tous deux portent `Parent:` pour traversée remontante.

## Pour les harnesses (CC / MC / HA / Shadow L1)

Si un harness atterrit dans `LD01_Business_Book/` et que sa session a été ouverte avec un Context Pack mentionnant « LD01 », « Book », « Business », « Career », ou « Solaris », voici l'ordre de traversée obligatoire :

1. **Lire** `00_index.md` (~50 lignes) —rail racine progressive disclosure
2. **Lire** `AGENTS.md` sister — règles de zone (ownership, contrats, vérif)
3. **Charger** `90_manifests/manifest.cross-harness.md` — ce qui est attendu de *ton* harness
4. **Plonger** dans le module ciblé (`10_*`, `20_*`, `30_*`, `99_*`)

## Règles opérationnelles (liantes)

| Règle | Pourquoi | Source canon |
|---|---|---|
| Lire `AGENTS.md` avant tout edit dans cette zone | Traçabilité + ownership | plan-meta-memoire §P4 |
| Append-only sur `30_decisions/` et `99_meta/calendar.md` | D4, anti-paperclip | plan-meta-memoire §10.5 |
| D1 receipt sur tout module nouveau | TDD = test avant contenu | CARDIA-TDD §10_methodology |
| Frontmatter OKF (`type` top-level) sur tout `.md` | OKF v0.1 §6 | plan-meta-memoire §3.1 |
| Append `calendar.md` après changement significatif | Épisode-mémoire | plan-lune-book §3.2 |

## Anti-patterns (à NE PAS faire)

- ❌ Hard-delete d'un `.md` (utiliser `_TRASH/` ou préfixe `DEPRECATED_` + lien vers nouveau)
- ❌ Réécriture de `A3_Book_LD01_Spec.md`, `BIBLIOGRAPHY.md`, `README.md` (intouchables)
- ❌ Création de doublons dans `01_Guides_Business/` (c'est une junction vers Geordi, pas une copie)
- ❌ Cron automatique sans HITL A0 explicite (Posture C — plan-meta-memoire §3.8)
- ❌ Secret en clair dans un `.md` (PAT, token, secret — voir D5 via Windows Credential Manager ou vault chiffré, cf. canon git-ship layered)

## Verification rapide (avant rendu)

```
$root = "$PSScriptRoot\..\..\..\.."
Test-Path "$root\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\00_index.md"   # True
Test-Path "$root\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\AGENTS.md"      # True
Test-Path "$root\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\CLAUDE.md"      # True
Get-ChildItem -Path "$root\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\90_manifests" | Measure-Object | Select-Object -ExpandProperty Count  # ≥ 1
```

## Child DOX Index (registre côté harness)

- `90_manifests/manifest.cross-harness.md` ← entry point pour TOUT harness

> Last DOX pass : 2026-07-04T12:00:00-04:00. Sister `AGENTS.md` mise à jour en parallèle.

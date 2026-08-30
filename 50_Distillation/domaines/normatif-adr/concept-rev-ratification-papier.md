---
type: Concept
title: Revue des ratifications papier — la chaîne de confiance
description: Le verdict d'un ADR dépend de la chaîne de confiance : qui a proposé (A2 ou Codex), qui a ratifié (A0), qui a vérifié (humain ou machine). Le format OKF exige de tracer cette chaîne.
tags: [adr, ratification, papier, confiance, verified]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: ADR-OMK-001
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-OMK-001_dual-product-dashboard-multitenant_RATIFIED.md"
    title: OMK 001 — chaîne Codex → A0
    last_modified: "2026-06-11"
  - id: ADR-OMK-004
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-OMK-004_pivot-supabase-cloud-vercel.md"
    title: OMK 004 — chaîne Codex → Claude update → A0
    last_modified: "2026-06-19"
  - id: ADR-L2-MULTIVERSE-CD-001
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-MULTIVERSE-CD-001_multiverse-cd-verse_RATIFIED_2026-07-15.md"
    title: Multiverse CD — chaîne A2/A0 batch
    last_modified: "2026-07-15"
okf_version: "0.2"
---

# Revue des ratifications papier — la chaîne de confiance

## Résumé

Le **verdict** d'un ADR dépend de la **chaîne de confiance** : qui a proposé, qui a ratifié, qui a vérifié. Le format OKF v0.2 exige de tracer cette chaîne via le champ `verified`. Cette distillation passe en revue les ratifications « papier » du corpus.

## La chaîne typique

```
A0 (directive) → A2 (Claude Code) ou Codex (rédaction) → A2 update (Claude Code contextuelle) → A0 (ratification airlock)
```

## Les trois profils identifiés

### Profil 1 — A0 directive → A2 → A0 (canonique)

Le profil dominant. A0 formule une directive ; A2 (Claude Code) rédige l'ADR ; A0 ratifie par airlock.

Exemple : `ADR-L2-MULTIVERSE-CD-001`. Frontmatter :

```
ratified_by: A0 Amadeus (airlock clos 2026-07-15 — batch verdict Enterprise OS SUPER-MAN DE JERRY session, sibling 6/7)
proposed_by: A2 (Claude Code via /superpowers:brainstorming) on A0 directive session brainstorm
```

### Profil 2 — A0 directive → Codex (A2 antérieur) → Claude Code update → A0

Le profil observé dans les pivots OMK. A0 formule une directive ; Codex rédige le draft sans contexte canon local ; Claude Code relit, identifie les trous, met à jour l'ADR ; A0 ratifie.

Exemple : `ADR-OMK-004`. Frontmatter :

```
proposed_by: Codex (A2) on A0 directive
updated_by: Claude Code (A2) — D1 evidence + 5 conditions
```

Le corps de l'ADR contient une section « **Pre-Ratification Updates (2026-06-19, Claude Code)** » qui documente les corrections.

### Profil 3 — A0 seul (sans intermédiaire)

Quelques ADR sont rédigés directement par A0 sans intermédiaire A2. C'est plus rare et concerne des décisions très cadrées.

Exemple : `ADR-INFRA-001`. Frontmatter : `Auteur : A0 Amadeus + A2 Claude Code`. Mixte.

## Les ADR sans ratification claire

Certains ADR sont marqués `RATIFIED` sans `ratified_by` explicite. La ratification est implicite par le contexte d'usage. C'est le cas de nombreux V0 et FW K-011 à 020.

## Le verdict OKF

Le format OKF v0.2 distingue trois niveaux de confiance :

| `verified` | Niveau |
|---|---|
| absent | non vérifié |
| acteurs non-`human:` | confirmé par machine |
| au moins un `human:<id>` | revu par un humain |

Pour un ADR RATIFIED :

- Si la chaîne A2 → A0 est documentée dans le frontmatter → équivalent OKF = `process:airlock-<date>`
- Si la ratification est implicite (V0, FW K-011 à 020) → équivalent OKF = `process:usage-implicit`

## Statut vis-à-vis de V3

**canon** sur la chaîne. **synthese-datee** sur la pratique — beaucoup d'ADR V0 et FW K-011 à 020 n'ont pas de `ratified_by` explicite.

## Le verdict de cette distillation

**canon**. La chaîne de confiance est traçable ; le format OKF peut la représenter.

## Liens

- Voir aussi : `concept-batches-ratification.md` (les sessions airlock)
- Voir aussi : `concept-adr-format.md` (le format)
|# Context7 Boundary — L1 Life OS Standard

> Layer: L1 Life OS
> Date: 2026-06-04
> Status: ACTIVE

## Overview

Chaque ship L1 Life OS a sa propre Context7 Boundary. Cette document définit quand utiliser Context7 et quand ignorer.

## Règle d'Or

**No Context7 lookup is required to read or update this local handoff. Use Context7 before any live provider, plugin, API, MCP, or CLI configuration.**

## Ship-by-Ship Context7 Boundary

### 21_Ikigai_Orville

**Context7 Boundary** : No Context7 lookup is required for local Ikigai pillar/handoff writing. Use Context7 before any provider, plugin, API, MCP, or CLI mutation.

**Raison** : Les fichiers locaux (README.md, A2 Spec, A3 References Index) sont autonomes. Context7 est nécessaire uniquement pour les providers externes.

**Exceptions** :
- Obsidian plugin/API claims → `NEEDS_CONTEXT7`
- Baserow schema/API mutation → `NEEDS_CONTEXT7`
- Plane API/project schema → `NEEDS_CONTEXT7`
- Affine API/Edgeless integration → `NEEDS_CONTEXT7`

---

### 22_Wheel_Discovery

**Context7 Boundary** : No Context7 lookup is required to read or update this local handoff. Use Context7 before Baserow API, schema, rollup, MCP, or provider configuration.

**Raison** : Discovery/ZORA utilise Baserow comme Shadow L1 surface. Les mutations de schema/API nécessitent Context7.

**Exceptions** :
- Baserow schema/API mutation → `NEEDS_CONTEXT7`
- Baserow rollup formulas → `NEEDS_CONTEXT7`
- Baserow MCP integration → `NEEDS_CONTEXT7`
- Baserow provider configuration → `NEEDS_CONTEXT7`

---

### 23_12WY_SNW

**Context7 Boundary** : No Context7 lookup is required to read or update this local handoff. Use Context7 before Baserow API, schema, rollup, MCP, Symphony adapter, or CLI configuration.

**Raison** : SNW utilise Baserow comme Shadow L1 surface. Les mutations de schema/API nécessitent Context7.

**Exceptions** :
- Baserow schema/API mutation → `NEEDS_CONTEXT7`
- Baserow rollup formulas → `NEEDS_CONTEXT7`
- Baserow MCP integration → `NEEDS_CONTEXT7`
- Symphony adapter configuration → `NEEDS_CONTEXT7`
- Baserow provider configuration → `NEEDS_CONTEXT7`

---

### 24_PARA_Enterprise

**Context7 Boundary** : No Context7 lookup is required to read or update this local handoff. Use Context7 before Obsidian plugin, sync, API, MCP, or import/export configuration.

**Raison** : Enterprise utilise Obsidian comme Shadow L1 surface. Les mutations de plugin/API nécessitent Context7.

**Exceptions** :
- Obsidian plugin/API claims → `NEEDS_CONTEXT7`
- Obsidian sync configuration → `NEEDS_CONTEXT7`
- Obsidian MCP integration → `NEEDS_CONTEXT7`
- Obsidian import/export configuration → `NEEDS_CONTEXT7`

---

### 25_GTD_Cerritos

**Context7 Boundary** : No Context7 lookup is required to read or update this local handoff. Use Context7 before Plane API, project schema, MCP, webhook, or provider configuration.

**Raison** : Cerritos utilise Plane comme Shadow L1 surface. Les mutations de schema/API nécessitent Context7.

**Exceptions** :
- Plane API/project schema → `NEEDS_CONTEXT7`
- Plane webhook configuration → `NEEDS_CONTEXT7`
- Plane MCP integration → `NEEDS_CONTEXT7`
- Plane provider configuration → `NEEDS_CONTEXT7`

---

### 26_DEAL_Protostar

**Context7 Boundary** : No Context7 lookup is required to read or update this local handoff. Use Context7 before Affine API, Edgeless integration, MCP, plugin, or provider configuration.

**Raison** : Protostar utilise Affine Edgeless comme Shadow L1 surface. Les mutations de API/integration nécessitent Context7.

**Exceptions** :
- Affine API claims → `NEEDS_CONTEXT7`
- Edgeless integration → `NEEDS_CONTEXT7`
- Affine MCP integration → `NEEDS_CONTEXT7`
- Affine plugin configuration → `NEEDS_CONTEXT7`

---

## Convention de Marquage

Tous les claims externes doivent être marqués `NEEDS_CONTEXT7` jusqu'à ce qu'ils soient vérifiés.

**Exemples** :
- ❌ "Utiliser Obsidian plugin X" → `NEEDS_CONTEXT7`
- ❌ "Modifier Baserow schema" → `NEEDS_CONTEXT7`
- ❌ "Configurer Plane webhook" → `NEEDS_CONTEXT7`
- ❌ "Activer Affine Edgeless" → `NEEDS_CONTEXT7`
- ❌ "Configurer Telegram bot" → `NEEDS_CONTEXT7`

**Exemples valides** :
- ✅ "Lire README.md local"
- ✅ "Écrire A2 Spec local"
- ✅ "Compiler findings A3"
- ✅ "Route vers Morty"

---

## Workflow Context7

1. **Lire le fichier local** (README.md, A2 Spec, A3 References Index)
2. **Identifier le claim externe** (Obsidian, Baserow, Plane, Affine, Telegram, etc.)
3. **Marquer `NEEDS_CONTEXT7`** si le claim est externe
4. **Utiliser Context7** pour vérifier le provider/plugin/API/MCP/CLI
5. **Documenter la preuve** dans le fichier local

---

## Anti-Patterns

1. **Utiliser Context7 pour lire des fichiers locaux** → Inutile et coûteux
2. **Marquer `NEEDS_CONTEXT7` sans vérifier** → Risque de drift doctrinal
3. **Ignorer les claims externes** → Risque de sécurité ou de conformité
4. **Modifier un shadow tool sans Context7** → Risque de bugs ou de perte de données

---

## Risques

1. **Drift doctrinal** : Si Context7 n'est pas utilisé, les conventions peuvent diverger
2. **Bugs de configuration** : Si Context7 n'est pas utilisé, les configurations peuvent être incorrectes
3. **Perte de données** : Si Context7 n'est pas utilisé, les données peuvent être perdues
4. **Risque de sécurité** : Si Context7 n'est pas utilisé, les secrets peuvent être exposés

---

## Mitigation

1. **Standardiser les Context7 Boundary** → Chaque ship a sa propre Boundary
2. **Marquer `NEEDS_CONTEXT7`** → Tous les claims externes doivent être marqués
3. **Utiliser Context7 avant toute mutation** → Vérifier le provider/plugin/API/MCP/CLI
4. **Documenter la preuve** → Toujours documenter la preuve dans le fichier local

---

## Références

- `AGENTS.md` — Canon Absolu A'Space OS
- `10_Tech_OS/12_Blueprints/01-SDD/SDD-008_shadow-L1-life-os.md` — Shadow L1 Life OS
- `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/concepts/concept_life_os.md` — Concept Life OS
- `CLAUDE.md` — Context7 Boundary pour L0 Tech OS
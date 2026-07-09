---
source: A0_MEMORY_CORE
date: 2026-05-17
type: shadow-l0-coordination
status: ACTIVE
domain: Shadow_L0 / Executor_Mesh
tags: [#ShadowL0, #ExecutorMesh, #LLM_Wiki, #Symphony]
related:
  - C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\README.md
  - C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\entities\entity_shadow_l0_executor_mesh.md
  - C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\concepts\concept_agent_capsule.md
---

# Shadow L0 Coordination — 2026-05-17

## Intention

Creer une couche locale de coordination qui permet a Codex CLI, Claude Code CLI et Gemini CLI de travailler sur le meme systeme de memoire sans dependre du runtime Hermes.

## Decision

Shadow L0 est maintenant un dossier actif dans le Memory Core:

`C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Shadow_L0`

Il contient les capsules minimales des trois executants:

- `agents/Codex_CLI/`
- `agents/Claude_Code_CLI/`
- `agents/Gemini_CLI/`

## Responsabilites

| Executant | Responsabilite L0 | Sortie attendue |
|-----------|-------------------|-----------------|
| Codex CLI | Modifier et verifier fichiers locaux | Patchs, tests, preuves |
| Claude Code CLI | Produire raisonnement Claude-style et execution alternative | Plans, patches, critiques |
| Gemini CLI | Full-Spectrum: Synthese, Architecture et Implementation resiliente | Cartographies, Code, ADRs, Syntheses |

## Workflow Canonique

1. Charger `30_MEMORY_CORE/README.md`.
2. Charger ce fichier.
3. Charger la capsule de l'executant choisi.
4. Lire les pages LLM Wiki pertinentes.
5. Executer la mission.
6. Mettre a jour `LLM_Wiki/wiki/log.md` si la decision devient durable.

## Relation A Symphony

Symphony est le routeur conceptuel. Shadow L0 est le banc d'execution local.

Symphony decide le type de travail:

- implementation;
- exploration;
- verification;
- handoff;
- synthese.

Shadow L0 choisit l'executant adapte.

## Relation A Shadow L2

Shadow L2 contient les connecteurs business comme Notion, ClickUp et Airtable.

Shadow L0 ne duplique pas ces secrets et ne les inscrit pas dans les capsules. Il ne reference que les noms de variables ou les chemins de configuration deja documentes.

## Preuves

- Dossier cree: `Shadow_L0/`
- Capsules creees: `agents/Codex_CLI`, `agents/Claude_Code_CLI`, `agents/Gemini_CLI`
- Aucun secret requis.

## Risques Residuals

- Les capsules sont des squelettes operationnels; elles doivent etre enrichies par usage reel.
- Le heartbeat Hermes n'est pas remplace par un daemon autonome.
- Claude Code et Gemini CLI doivent encore etre normalises cote configuration locale si leurs fichiers globaux changent.

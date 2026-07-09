---
source: Shadow_L1
date: 2026-05-17
type: agent-handoff
target: Gemini_CLI
status: ACTIVE
tags: [#ShadowL1, #GeminiCLI, #Baserow, #Plane]
---

# Gemini CLI Handoff — Shadow L1 Baserow / Plane

## Mission Gemini

Gemini doit agir comme lecteur large et cartographe:

- lire `30_MEMORY_CORE/README.md`;
- lire `Shadow_L1/README.md`;
- lire `Shadow_L1/01_baserow-plane-handoff-20260517.md`;
- comparer avec `LLM_Wiki/wiki/log.md`;
- produire une synthese ou une contradiction map.

## Ce Que Gemini Peut Faire

- Cartographier les dependances Baserow -> Plane -> Symphony.
- Identifier les champs necessaires pour transformer une ligne Baserow en work-items Plane.
- Proposer une structure de payload, sans executer de creation si Plane auth n'est pas OK.
- Signaler les docs Hermes comme preuves historiques, pas comme destination active.

## Ce Que Gemini Ne Doit Pas Faire

- Imprimer les secrets depuis `.env`.
- Creer des work-items Plane sans validation auth.
- Ecrire de nouvelle doctrine dans `Hermes Agent/`.

## Etat A Connaitre

- Baserow read precedent OK: table `955428`, row `133`.
- Plane auth precedent KO: HTTP 403.
- Aucun ticket Plane cree.

## Sortie Attendue

Un rapport court:

- source paths lus;
- etat Baserow;
- etat Plane;
- prochaine action recommandee;
- risques ou contradictions.


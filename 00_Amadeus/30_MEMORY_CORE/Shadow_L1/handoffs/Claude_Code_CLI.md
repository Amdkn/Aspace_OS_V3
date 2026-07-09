---
source: Shadow_L1
date: 2026-05-17
type: agent-handoff
target: Claude_Code_CLI
status: ACTIVE
tags: [#ShadowL1, #ClaudeCode, #Baserow, #Plane]
---

# Claude Code CLI Handoff — Shadow L1 Baserow / Plane

## Mission Claude

Claude Code doit agir comme planificateur et executant prudent:

- lire `30_MEMORY_CORE/README.md`;
- lire `Shadow_L1/README.md`;
- lire `Shadow_L1/01_baserow-plane-handoff-20260517.md`;
- verifier la config sans exposer de secret;
- ne creer les work-items Plane qu'apres auth OK.

## Ce Que Claude Peut Faire

- Proposer un script de smoke test qui masque les secrets.
- Verifier la presence des variables par nom.
- Tester l'auth Plane avec un endpoint read-only.
- Transformer Solaris W1 en payloads Plane.
- Demander explicitement validation avant `POST`.

## Ce Que Claude Ne Doit Pas Faire

- Hardcoder les cles dans `.claude.json`, markdown, ou logs.
- Afficher `/home/amadeus/.hermes/.env`.
- Considerer l'ancien token Plane comme sain.
- Documenter dans `Hermes Agent/` comme zone active.

## Variables Attendues

Noms seulement:

- `BASEROW_DATABASE_TOKEN`
- `PLANE_API_KEY`
- `PLANE_WORKSPACE_SLUG`
- `PLANE_PROJECT_LIFE_OS`

## Etat A Connaitre

- Baserow source prouvee: table `955428`, row `133`.
- Plane bloque: HTTP 403 lors du test precedent.
- La cle Plane precedemment collee doit etre rotatee.

## Sortie Attendue

Avant creation:

- auth Plane OK/KO;
- workspace slug confirme;
- project id confirme;
- payloads proposes;
- risque residuel.

Apres creation eventuelle:

- IDs Plane crees;
- liens Baserow source;
- preuve de lecture/creation;
- entree LLM Wiki log proposee.


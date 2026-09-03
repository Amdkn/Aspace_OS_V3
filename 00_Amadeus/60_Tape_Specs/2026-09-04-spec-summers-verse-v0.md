# Spec — Summers_Verse v0 : initialiser 30_Business_OS/00_Summers_Verse/ (par projet) (L2)

- **Date** : 2026-09-04
- **Layer** : L2 (Buzz Core 12th) — périmètre 30_Business_OS
- **Patron** : copie conforme du cycle Meta_Factory v0 (dossiers + registre + README + verifier)
- **Autonomie** : aucune clarification humaine requise (test du ruban : PASS)

## Objectif

Rendre `30_Business_OS/00_Summers_Verse/` fonctionnel : Summers Verse organisé **par projet**, avec un registre source de vérité, un sous-dossier par projet actif, et un vérificateur exécutable — pas une note.

## Livrables (acceptance criteria)

1. `00_Summers_Verse/00_Registre/registre.json` — registre des projets, schéma :
   ```json
   {"updated_at": "<ISO8601>", "projects": [
     {"id": "coach-os-app", "name": "Coach OS App", "status": "initialized"}]}
   ```
   `coach-os-app` est le seul projet actif de `30_Business_OS/10_Projects/`.
2. `00_Summers_Verse/projects/coach-os-app/README.md` — décrit : rôle, entrée, sortie, invariant. Minimal, exécutable comme doc de contrat (pas de prose archivale — canon §6).
3. `00_Summers_Verse/verifier.py` — script Python pur stdlib qui :
   - charge `00_Registre/registre.json`,
   - échoue (exit 1) si : JSON invalide, `projects` vide, id inconnu (hors registre), README manquant pour un projet présent,
   - réussit (exit 0, imprime `summers-verse v0: OK`) sinon.
4. `python verifier.py` s'exécute depuis n'importe quel cwd (paths relatifs au fichier via `Path(__file__).parent`).
5. Preuve : sortie réelle de `python verifier.py` collée dans le rapport de build (evidence).

## Invariants

- Aucune modification hors `30_Business_OS/00_Summers_Verse/`.
- Aucune dépendance externe (stdlib only).
- Le registre est la source de vérité ; les README se déduisent du registre, jamais l'inverse.
- Un projet Summers Verse = un sous-dossier de `projects/`, miroir des projets actifs de `10_Projects/`.

## Hors périmètre

- Tout ajout d'autres projets que `coach-os-app` (v1+, quand `10_Projects/` en liste d'autres).
- Tout build réel du contenu Summers Verse par projet (v1+).
- `00_Summers_QuickAccess/` (micro-exécutif, dossier distinct).

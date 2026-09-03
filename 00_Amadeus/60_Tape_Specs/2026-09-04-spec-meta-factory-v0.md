# Spec — Meta_Factory v0 : initialiser 02_Meta_Factory fonctionnel (L2)

- **Date** : 2026-09-04
- **Layer** : L2 (Buzz Core 13th) — périmètre 30_Business_OS
- **Patron** : copie conforme du cycle Jerry Pulse v0 (work 22, done) — dossiers + README + artefact fonctionnel + verifier
- **Autonomie** : aucune clarification humaine requise (test du ruban : PASS)

## Objectif

Rendre `30_Business_OS/02_Meta_Factory/` fonctionnel : la B3 factory (AutoLab / PrimeAgent / Jcode) obtient son squelette exécutable, pas une note.

## Livrables (acceptance criteria)

1. `02_Meta_Factory/00_Registre/registre.json` — registre des 3 units B3, schéma :
   ```json
   {"updated_at": "<ISO8601>", "units": [
     {"id": "autolab", "name": "AutoLab", "role": "labo automatise builds/experiences", "status": "initialized"},
     {"id": "primeagent", "name": "PrimeAgent", "role": "prototype d'agents franchises", "status": "initialized"},
     {"id": "jcode", "name": "Jcode", "role": "pipeline code-gen borne", "status": "initialized"}]}
   ```
2. `02_Meta_Factory/<unit>/README.md` ×3 — chaque README décrit : rôle, entrée, sortie, invariant. Minimal, exécutable comme doc de contrat (pas de prose archivale — canon §6).
3. `02_Meta_Factory/verifier.py` — script Python pur stdlib qui :
   - charge `00_Registre/registre.json`,
   - échoue (exit 1) si : JSON invalide, ≠3 units, ids hors {autolab, primeagent, jcode}, un unit sans `role`,
   - échoue si un README manque pour un unit présent,
   - réussit (exit 0, imprime `meta-factory v0: OK`) sinon.
4. `python verifier.py` s'exécute depuis n'importe quel cwd (paths relatifs au fichier via `Path(__file__).parent`).
5. Preuve : sortie réelle de `python verifier.py` collée dans le rapport de build (evidence).

## Invariants

- Aucune modification hors `30_Business_OS/02_Meta_Factory/`.
- Aucune dépendance externe (stdlib only).
- Le registre est la source de vérité ; les README se déduisent du registre, jamais l'inverse.
- `.gitkeep` conservé tant que le dossier contient d'autres fichiers (peut être supprimé si autre contenu présent — autorisé).

## Hors périmètre

- Tout build réel d'agents AutoLab/PrimeAgent/Jcode (v1+).
- Tout ajout de domaines B2/squads B3.

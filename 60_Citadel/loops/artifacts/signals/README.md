---
type: artifact-schema
artifact: signal
---
# signals/ — frictions, idées, opportunités (cross-loop)

**Entre** : toute observation réutilisable par une AUTRE loop — friction répétée, idée produit, opportunité growth, gap conversion, prédiction WF3 (`sim-*.md`), `mirofish-missing`, `pass-expired`, `airlock-red`, `gate-closed`, `governance-*`.
**N'entre pas** : le travail lui-même (→ tasks/), les livrables (→ docs/), les états de tickets (→ tickets/).

**Schéma** : 1 fichier par slug. Frontmatter : `type: signal`, `status: open|absorbed`, `sources: [paths]`, `seen: N`. Corps : description + **timeline append-only** (`- [ISO] [loop] occurrence/décision`). Une loop qui re-voit le signal APPEND et incrémente `seen` — jamais de fichier doublon.
**Absorption** : un signal devient `absorbed` quand une task créée le référence. Le fichier reste (mémoire).

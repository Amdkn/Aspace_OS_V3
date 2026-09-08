# AGENTS.md — 60_Implementation_Méthodologiques (Cadre & SOPs)

> **Loi de l'Exécution Méthodologique :** Une intention sans procédure opérationnelle standardisée (SOP) est un vœu pieux.
> Ce dossier régit les gabarits, standards de codage, pipelines de vérification et gates d'implémentation.

---

## 1. Rôle dans la Pyramide à 7 Niveaux

- **Niveau Pyramide :** [5D / 6D] — Spécification des protocoles d'exécution et des interfaces de test.
- **Rôle :** Fixer les règles de fabrication pour Ryan (Builder) et les critères de passage des Gates.

---

## 2. Invariants d'Implémentation

- **TypeScript :** Compilation stricte `tsc --noEmit` à 0 erreur requise avant tout commit.
- **Python :** Typage strict, exécution déterministe, gestion des encodages Windows (`utf-8`).
- **SQLite :** Mode WAL (`PRAGMA journal_mode=WAL;`), transactions immédiates, indexation systématique.

---

## 3. Journal Append-Only (DOX)

- `2026-09-08` : Rattachement au Meta-Routeur V3 et alignement sur la doctrine de validation déterministe (Hooks & Gates).

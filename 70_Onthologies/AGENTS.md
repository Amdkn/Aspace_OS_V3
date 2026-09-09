# AGENTS.md — 70_Onthologies (Vérité Formelle & Graphe Semantica)

> **Loi de Vérité Formelle :** Le graphe RDF et les ontologies sont au-dessus des couches applicatives.
> Graham (`companion_graham_memory`) est le gardien de ce sanctuaire. Rien n'est admis comme vérité sans triple certifié.

---

## 1. Rôle dans la Pyramide à 7 Niveaux

- **Niveau Pyramide :** [Pantry / 6D] — Le Ruban $\phi$ fondamental et le "Silver Platter" de vérité formelle.
- **Rôle Cybernétique :** Graham fournit les concepts immuables, les types stricts et les relations ontologiques à Ryan (Builder) et Yaz (Observabilité).
- **Statut :** Au-dessus de Tech OS, Life OS et Business OS.

---

## 2. Structure & Graphes Vivants

- `semantica_knowledge_graph.json` : Graphe unifié contenant 1 681+ nœuds interconnectés (Entités, Décisions, Invariants D1-D4).
- `onto_gate.py` : Gate déterministe de validation ontologique avant écriture.
- `_cold_archive/` : Scellé hermétique de V2 — aucun agent n'y fait d'accès aléatoire.

---

## 3. Directives pour les Agents & Réduction de Contexte

- **Interdiction du balayage brut :** Les agents ne doivent pas ingérer l'intégralité du JSON de connaissances (50k+ tokens gaspillés).
- **Consommation via le Silver Platter :** Utiliser les projections ciblées (`python 10_Tech_OS/kernel/posthog_observability.py graph` ou endpoints `/api/tech-os/graph/query`) pour extraire uniquement le sous-graphe concerné.

---

## 4. Journal Append-Only (DOX)

- `2026-09-08` : Raccordement au routeur Meta AGENTS.md V3. Clarification du rôle de Graham comme pourvoyeur du Ruban $\phi$ formel.

## Journal Append-Only (DOX)
- `2026-09-09` : Modélisation du découplage mémoire/ontologie inspiré de Qwen Engram / Qwen Flash Next. Alignement du vocabulaire RDF et des pointeurs d'ontologie. (Nardole).

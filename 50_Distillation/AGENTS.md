# AGENTS.md — 50_Distillation (Le Gate Inviolable V3)

> **Loi du Sas d'Entrée :** Rien n'entre dans V3 sans passer par la distillation sémantique.
> Ce dossier est le coupe-circuit inviolable entre le vrac extérieur (sources brutes, exports, notes non triées) et la mémoire certifiée (`40_Memory_Wiki_OKF/`) ou les ontologies (`70_Onthologies/`).

---

## 1. Rôle & Invariants dans la Pyramide à 7 Niveaux

- **Niveau Pyramide :** Pont [4D / 5D] — Traitement par batch régulier & Gate de validation sémantique.
- **Autorité :** Sas inviolable. Tout fichier déposé ici doit être analysé, typé, distillé en concepts OKF ou triples RDF, puis purgé ou archivé froidement.
- **Règle absolue :** Aucun processus applicatif (Life OS, Business OS, Tech OS) ne doit lire de données brutes sans leur passage préalable et leur certification par ce sas.

---

## 2. Organisation du Sas

```
50_Distillation/
├── _raw_inbox/         # Dépôt temporaire des imports bruts externes (chatgpt, papers, transcripts)
├── _in_progress/       # Distillation active en cours par les subagents
├── _distillates/       # Fiches de synthèse pré-validées prêtes pour Graham (OKF 0.2 / RDF)
└── AGENTS.md           # Ce registre local souverain
```

---

## 3. Protocoles & Commandes de Distillation

1. **Extraction sémantique :** Filtrer le bruit, extraire les concepts atomiques, attribuer la provenance (`sources: [{ id, resource, author, last_modified }]`).
2. **Certification :** Passage de la porte de validation OKF (`onto_gate.py` / validation frontmatter).
3. **Distribution :**
   - Concepts pérennes $\rightarrow$ `40_Memory_Wiki_OKF/concepts/`
   - Relations formelles $\rightarrow$ `70_Onthologies/`
   - Déchets & historiques scellés $\rightarrow$ `_cold_archive/`

---

## 4. Journal Append-Only (DOX)

- `2026-09-08` : Formalisation du sas `50_Distillation/` comme Gate souverain de niveau 1 dans l'architecture V3 et rattachement au routeur Meta AGENTS.md.

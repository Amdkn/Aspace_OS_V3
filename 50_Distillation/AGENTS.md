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

## Audit des boucles de correction Antigravity

Rapport consolidé : [`_distillates/audit-antigravity-a66f5256.md`](_distillates/audit-antigravity-a66f5256.md). Statut machine, non ratifié. Source figée et conversion vérifiée dans `_cold_archive/antigravity-a66f5256-f3af-40e1-900d-b21e99834ed2/`. Le rapport worker voisin est incomplet et ne fait pas autorité. Aucun correctif runtime n'est annoncé déployé.

Suite différentielle : [`_distillates/audit-antigravity-a66f5256-suite.md`](_distillates/audit-antigravity-a66f5256-suite.md). Instantané de 13 767 enregistrements ; test isolé du verrou TTS reproduisant une seconde acquisition sans libération du premier propriétaire. Attribution humaine dans une fiche signalée comme non justifiée par la séquence observée. Aucun correctif runtime déployé.

## 4. Journal Append-Only (DOX)

- `2026-09-08` : Formalisation du sas `50_Distillation/` comme Gate souverain de niveau 1 dans l'architecture V3 et rattachement au routeur Meta AGENTS.md.
- `2026-09-09` : Audit machine Astra du transfert Antigravity/Hermes et des six A2, sans migration appliquée : `_distillates/2026-09-09-audit-antigravity-hermes-six-a2.md`. Preuves : `90-self-evolution/reports/2026-09-09-astra-audit/`. Sépare présence, validation structurelle, runtime et résultat; aucune certification humaine ajoutée.

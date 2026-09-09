# PRD-A1-001 : Engram Phrase Book Engine & Gatekeepers A1 (Beth & Morty)

* **Statut :** PRÊT POUR IMPLÉMENTATION
* **Date :** 2026-09-09
* **Architecte :** Amadou Kone (`amdkn`)
* **Inspiration Canonique :** Qwen Engram / Phrase Book (Codacus), Marin Pipeline, MiniMind

---

## 1. Objectif Fondamental
Éliminer l'overhead de tokens lié à l'injection répétitive du Lore et des Règles d'A'Space OS V3. Déporter l'ontologie dans une Lookup Table statique NVMe mappée en mémoire (`mmap`) résolue à coût de calcul zéro par les Gatekeepers A1 (Beth & Morty).

---

## 2. Spécification des Livrables

### A. Dictionnaire d'Expressions Clés (`10_Tech_OS/kernel/engram/phrase_book_aspace.json`)
Contient les mappings d'invariants :
1. **Les 8 Domaines de Vie (LD01–LD08) :** SOB, Santé/Énergie, Clarté Mentale, etc.
2. **Les 8 Domaines Business (BD01–BD08) :** OMK, Offres, Funnels, Cash-flow.
3. **Les Triades des Docteurs :**
   - 13e Docteur (Yaz, Ryan, Graham)
   - 11e Docteur Life (Amy, Rory, River)
   - 12e Docteur Business (Clara, Bill, Nardole)
4. **Les Gates Déterministes :** DoD binaire (`tsc_no_emit_0`, `exit_code_0`), Os Hyoïde.

### B. Moteur Résolveur Zero-RAM (`10_Tech_OS/kernel/engram/engram_loader.py`)
- Utilise `mmap.mmap` pour lire directement sur le disque physique sans charger de gros volumes en RAM.
- Fonction `resolve(tokens: list[str]) -> dict | None` garantissant une résolution $O(1)$.

### C. Filtre Gatekeeper A1 (`10_Tech_OS/kernel/engram/beth_filter.py`)
- Intercepte toute intention/tâche entrante.
- Valide les contraintes invariantes avant transmission aux agents A2/A3.
- Veto immédiat si violation de la règle d'or ou corruption du périmètre.

### D. Fiche Conceptuelle OKF v0.2
- Déposer `40_Memory_Wiki_OKF/concepts/engram_phrasebook_architecture.md` avec le frontmatter strict OKF v0.2.

---

## 3. Critères d'Acceptation (DoD)
1. `python -m py_compile 10_Tech_OS/kernel/engram/*.py` valide avec 0 erreur.
2. Un test unitaire `test_engram.py` vérifie la résolution instantanée de `LD01_SOB` et `13TH_DOCTOR_KERNEL`.

# PRD : Moteur Local SLM Morty & TimesFM CPU (Phase 1 & 2)

> **Cible Repo :** Amdkn/Aspace_OS_V3  
> **Auteur :** Antigravity (Chef d'Orchestre)  
> **Exécutant :** Jules (Google Labs)  
> **Référence :** delegation-a-jules/SDD-004-MINIMIND-MARIN-TIMESFM-MORTY.md  
> **Standard :** OKF v0.2 / Python 3.10+ / Zéro Quota Cloud / Inférence CPU Locale

---

## 1. Objectif du Ticket

Implémenter le squelette de production et les tests pour le moteur local de **Morty** (10_Tech_OS/kernel/slm/) :
1. **10_Tech_OS/kernel/slm/marin_dataset_extractor.py** :
   - Extrait les concepts de 40_Memory_Wiki_OKF/concepts/*.md et les triplets RDF de 70_Onthologies/triplets/*.jsonl.
   - Produit un fichier de dataset d'alignement au format standard JSONL instruction tuning ({"instruction": ..., "input": ..., "output": ...}).
   - Zéro dépendance externe lourde : modules standards Python (pathlib, json, e).
2. **10_Tech_OS/kernel/slm/morty_engine.py** :
   - Classe MortyLocalEngine implémentant le protocole de prédiction et d'inférence CPU.
   - Intègre un fallback élégant si PyTorch / ONNX Runtime ou les poids ne sont pas encore installés localement.
   - Méthodes requises :
     - predict_horizon(series: list[float], horizon: int = 14) -> dict
     - valuate_decision(context: dict) -> dict
3. **Tests Unitaires :**
   - 10_Tech_OS/kernel/slm/test_morty_engine.py : valide l'extraction du dataset et l'exécution du moteur en mode nominal et fallback CPU.

---

## 2. Contraintes Techniques Inviolables

- **Typage strict** et python -m py_compile à 0 erreur.
- Aucun appel réseau ou API externe (zéro OpenAI, zéro Claude, zéro Gemini API dans ce module).
- Respect du standard d'architecture A'Space OS V3 et enregistrement dans le journal DOX 10_Tech_OS/AGENTS.md.

# PRD-005 : Extension PyTorch CPU / ONNX & Évaluation Événementielle pour Morty SLM

> **Cible Repo :** Amdkn/Aspace_OS_V3  
> **Auteur :** Antigravity / Amadou Kone  
> **Exécutant :** Jules (Google Labs)  
> **Statut :** READY FOR DISPATCH  
> **Priorité :** P1  

---

## 1. Contexte & Objectifs

Le moteur `10_Tech_OS/kernel/slm/morty_engine.py` et l'extracteur de dataset `marin_dataset_extractor.py` sont déjà opérationnels en mode fallback déterministe (Holt-Winters double exponentiel) avec 100% de tests passés.

Objectifs de cette session Jules :
1. **Intégration ONNX / PyTorch CPU (Optionnelle & Robuste) :**
   - Dans `10_Tech_OS/kernel/slm/morty_engine.py`, ajouter une détection propre de `onnxruntime` ou `torch` pour charger un modèle léger de prévision de séries temporelles (ex: format ONNX TimesFM ou MiniMind) si le fichier modèle est présent dans `10_Tech_OS/kernel/slm/models/`.
   - Si les bibliothèques ne sont pas installées ou si le fichier modèle n'existe pas, le fallback Holt-Winters actuel DOIT continuer de fonctionner de manière totalement transparente sans lever d'exception.
2. **Évaluation Événementielle des Tâches (`evaluate_decision`) :**
   - Améliorer la méthode `evaluate_decision(context: dict) -> dict` pour scorer la conformité d'une tâche à partir des concepts extraits par `marin_dataset_extractor.py`.
   - Calculer un indice d'alignement canonique (score flottant entre 0.0 et 1.0) et retourner les concepts OKF violés ou manquants.
3. **Tests de Robustesse :**
   - Enrichir `10_Tech_OS/kernel/slm/test_morty_engine.py` pour couvrir :
     - Le comportement avec et sans fichier modèle ONNX.
     - L'évaluation d'un contexte de tâche contenant des concepts clés OKF versus un contexte hors-canon.
   - S'assurer que `pytest 10_Tech_OS/kernel/slm/test_morty_engine.py` réussit à 100%.
4. **Validation Strict :**
   - Compiler avec `python -m py_compile 10_Tech_OS/kernel/slm/*.py`.

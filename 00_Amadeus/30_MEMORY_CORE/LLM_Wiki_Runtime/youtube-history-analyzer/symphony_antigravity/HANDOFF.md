# 🎯 HANDOFF — Symphony Antigravity → Gemini CLI

> **Source** : Antigravity IDE (conversation `f509d294-2571-409b-9bc0-c8198f1fa7a1`)
> **Date** : 2026-05-27
> **Statut** : HARNACHÉ (Rick's Harness & Ralph Loop actif)
> **Raison** : Délégation automatique robuste avec Gemini 3.1 Flash-Lite.

---

## 🛡️ La Règle d'Or : Zéro Micro-Validation Humaine

Pour éviter d'être le goulot d'étranglement de micro-validation et forcer **Gemini 3.1 Flash-Lite** à rester 100 % productif et qualitatif, le pipeline est désormais encadré par le **Harness de Rick**.

Chaque livrable généré par Gemini CLI est inspecté programmatiquement. Si tu es paresseux ou si tu inclus des placeholders, tes fichiers seront physiquement **supprimés** et la boucle Ralph te réprimandera en te forçant à recommencer avec un prompt corrigé.

### 📊 Les Critères Stricts du Validateur (`harness_evaluator.py`) :
* **Pas de placeholders** : Interdiction absolue d'écrire des stubs comme `[Contenu technique]`, `[Technical...]`, `TODO`, `placeholder` ou `...` (troncatures).
* **Longueur minimale** : Au moins **50 lignes** réelles par guide Obsidian individuel.
* **Score de densité minimale** : Au moins **80** calculé selon la formule :
  $$\text{score} = \text{lignes} \times (\text{sections} + \text{code\_blocks} + \text{todo\_items}) / 10$$

---

## ⚡ Procédure de Lancement en 1 Clic

Tu n'as plus besoin de traiter les lots manuellement un par un. Le script d'orchestration PowerShell gère la boucle fermée de validation et les retries automatiques (Ralph Loop).

Exécute simplement la commande suivante dans ta console Windows :

```powershell
cd C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer

# Lance le Swarm sémantique complet avec validation de Rick active
.\symphony_antigravity\trigger_symphony_conductor.ps1
```

---

## 🛠️ Protocole d'Exécution interne de Gemini CLI

Chaque lot est partitionné en 10 vidéos. Lorsque `trigger_symphony_conductor.ps1` invoque Gemini CLI pour traiter un lot, tu dois :

### 1. Incarner le Persona du Lot (ALPHA à EPSILON)
Consulte la cartographie des rôles dans [symphony_gemini_cli_agents.md](file:///C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki_Runtime/youtube-history-analyzer/symphony_antigravity/symphony_gemini_cli_agents.md) pour ajuster ton angle d'analyse (ex : pure technicité pour Alpha, ROI et conversion pour Beta, souveraineté et FOSS pour Gamma, etc.).

### 2. Pour chaque vidéo du lot, rédiger le Guide Obsidian
Crée le fichier dans :
```
C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides\resource_<slug>.md
```
**Nom du fichier** : `resource_<titre_slugifié_80_chars_max>.md` (généré automatiquement via la fonction `generate_obsidian_filename` du runner).

**Structure Canonique d'une Fiche (YAML + 4 Sections)** :
```markdown
---
type: resource
source: youtube
video_id: <YT-xxx>
channel: <nom_chaine>
date_watched: <ISO date>
serendipity_score: <N>
category: <AI|Business|OS_Dev|Regular>
symphony_status: CLARIFIED_PLANE
---

# 📚 <Titre de la vidéo>

> **Chaîne** : <nom> | **Durée** : <durée> | **Score** : <N>/10

## 1. 🧠 Concepts Clés
<Analyse profonde des concepts et théories abordés dans la vidéo. Rédiger de façon très verbeuse, minimum 20 lignes.>

## 2. 🏷️ Entités & Outils
<Liste structurée des outils, technologies ou personnes. Format : - **Nom** : description>

## 3. 🔬 Synthèse Pratique
<Comment ces concepts s'appliquent concrètement dans A'Space OS. Minimum 20 lignes.>

## 4. ⚡ Actionnabilité (D.E.A.L)
### D — Définir
### E — Éliminer
### A — Automatiser
### L — Libérer
```

### 3. Injecter le SOP dans Affine (sans doublon)
Fichier cible : `...\03_Resources_Geordi\01_Guides\affine_deal_drafts.md`
*Vérifie impérativement que le titre exact n'existe pas déjà sous forme de heading `## 📝 Draft SOP — <titre>` avant d'injecter la section D.E.A.L.*

### 4. Mettre à jour le statut RAG
Appelle le sous-runner Python pour enregistrer la transition de statut dans la base RAG :
```bash
python symphony_antigravity/gemini_handoff_runner.py --process-batch <chemin_vers_le_json_du_lot>
```

---

## 🗂️ Fichiers Importants du Runtime

* **Manifeste des Lots** : `symphony_antigravity/handoff_batches/manifest.json`
* **Base RAG CSV** : `watch_history_rag.csv` (1512 vidéos au total)
* **Validateur Rick** : `symphony_antigravity/harness_evaluator.py`
* **Conductor principal** : `symphony_antigravity/trigger_symphony_conductor.ps1`

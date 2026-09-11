---
type: Concept
title: Architecture Vocale 2-en-1 & Résilience d Élocution Antigravity
description: Spécification du démon vocal duplex (automatique temps réel + rejeu manuel zéro-token) avec pré-indexation anti-écho au redémarrage et miroir persistant.
tags: [tts, voice, edge-tts, antigravity, 2-in-1, anti-echo, memory]
generated: { by: antigravity, at: 2026-09-09T02:04:00Z }
verified:
  - { by: human:amdkn, at: 2026-09-09T02:04:00Z }
sources:
  - id: tts-daemon-source
    resource: "c:\\Users\\amado\\ASpace_OS_V3\\10_Tech_OS\\kernel\\antigravity_tts_daemon.py"
    author: human:amdkn
    last_modified: 2026-09-09
okf_version: "0.2"
---

# Architecture Vocale 2-en-1 & Résilience d Élocution Antigravity

## 1. Problématique Résolue
1. **Surdité Opérateur** : L assistant génère des textes longs sans feedback audio immédiat, forçant l opérateur à garder les yeux rivés sur l écran.
2. **Double Écho Post-Redémarrage** : Lorsque le démon redémarrait ou rembobinait l offset sans filtrage, il rejouait l avant-dernière réponse déjà entendue.
3. **Consommation Inutile de Tokens** : Réécouter une réponse ne doit jamais nécessiter de nouvelle inférence LLM ni d appel API payant.

## 2. Piliers Techniques de la Solution 2-en-1

### A. Élocution Automatique Temps Réel
- Le démon `10_Tech_OS/kernel/antigravity_tts_daemon.py` surveille `transcript.jsonl`.
- Dès qu une réponse terminale `PLANNER_RESPONSE` (sans appel d outil) est détectée, le texte nettoyé est synthétisé via `edge-tts` (`fr-FR-DeniseNeural`) et lu sur Windows via `MediaPlayer`.
- **Verrou Mutex** : `tts_playing.lock` garantit qu aucune superposition de voix ne peut survenir.

### B. Pré-Indexation Anti-Écho (Cold Start / Restart)
- Au démarrage du démon ou lors d une bascule de transcript, les 64 derniers Ko du journal sont scannés.
- Tous les `step_index` préexistants sont chargés dans l ensemble mémoire `seen_step_indices`.
- Seul le **nouveau step** émis après l initialisation est lu. Aucun rejeu intempestif des tours passés.

### C. Écoute Manuelle Zéro-Token & Miroir Persistant
- Chaque message vocalisé est dupliqué de manière synchrone vers un emplacement fixe : `C:\\Users\\amado\\.antigravity_voice_cache\\latest_speech.mp3`.
- Un raccourci CLI permet de réécouter à la demande : `python 10_Tech_OS/kernel/antigravity_tts_daemon.py --replay`.
- Chaque réponse substantielle intègre un lien direct cliquable vers ce fichier pour permettre une réécoute hors écran.
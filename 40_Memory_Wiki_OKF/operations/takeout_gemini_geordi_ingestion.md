---
type: Playbook
title: Ingestion et Structuration du Takeout Gemini dans Geordi
description: Procédure standard et manifestes de structuration des exports Google Takeout dans 20_Life_OS Geordi avant distillation par le gate 50_Distillation.
tags: [life-os, takeout, gemini, geordi, distillation, ingestion]
generated: { by: gemini-antigravity, at: 2026-09-07T08:06:00Z }
verified:
  - { by: process:structurer_takeout_gemini, at: 2026-09-07T08:06:39Z }
sources:
  - id: takeout-gemini-20260907
    resource: "C:\\Users\\amado\\Downloads\\takeout-20260907T044520Z-1-001"
    author: human:amdkn
    last_modified: 2026-09-07
okf_version: "0.2"
---

# Ingestion et Structuration du Takeout Gemini

## 1. Emplacement Vivant
Conformément aux invariants V3 et à l'organisation PARA Enterprise :
- Le Takeout brut structuré réside dans : `20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/Takeout/Gemini_2026-09/`
- Il ne pénètre **jamais** directement dans l'ontologie ni dans la mémoire vivante. Il constitue un substrat froid indexé.

## 2. Métrique du Traitement (2026-09-07)
- **Fichiers traités :** 1 652 fichiers classés sans perte dans leurs répertoires d'extension :
  - `images/` : 1 352 fichiers (.jpg, .png)
  - `audio/` : 80 fichiers (.wav, .mp3)
  - `documents/` : 75 fichiers (.pdf, .docx, .txt, .csv)
  - `archives/` : 11 fichiers (.zip)
  - `code/` : 9 fichiers (.py, .sql, snippets)
  - `brut/` : 125 fichiers de métadonnées et sans extensions
- **Conversations extraites :** 3 619 cellules d'échanges découpées chronologiquement et converties en Markdown mensuel sous `conversations/` (de 2025 à septembre 2026, 17 Mo pour le seul mois en cours).
- **Inventaire Machine :** `MANIFEST_TAKEOUT_GEMINI.json` garantissant l'intégrité et la traçabilité.

## 3. Sas vers la Distillation Hebdomadaire
Ce corpus sert désormais de source d'alimentation pour les tâches de distillation planifiées (`50_Distillation/`), qui en extraient les pépites d'architectures, concepts et SOPs certifiés.

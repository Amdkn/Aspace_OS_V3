# PRD-012 — Agent OS Desktop - Observabilité, Télémétrie & Polish UI

## 1. Contexte & Objectif
Le repository `Agent-OS-Desktop` est le Shell applicatif souverain (port 5555).
L'objectif de ce sprint est de :
1. Polir les widgets de télémétrie système (CPU, RAM, état des baux uc.db) dans la TopBar et le widget d'observabilité.
2. S'assurer que les fenêtres Draggable/Resizable conservent leur état avec fluidité (zéro layout shift).
3. Garantir que `npm run typecheck` (`tsc --noEmit`) et `npm run build` compilent avec 0 erreur.
4. Créer automatiquement une Pull Request documentée (`AUTO_CREATE_PR`).

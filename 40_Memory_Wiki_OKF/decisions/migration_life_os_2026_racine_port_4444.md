---
type: Decision
title: Migration Life-OS-2026 Racine, Déblocage Port 4444 & Délégation Jules 12WY Glassmorphism
description: Migration physique du dépôt Life-OS-2026 sous C:\Users\amado\Life-OS-2026, déblocage du splash Supabase offline, push GitHub sur origin main et création du brief de délégation Jules PRD-001.
tags: [life-os-2026, migration, port-4444, supabase, sqlite, jules, 12wy, glassmorphism]
generated: { by: "machine:gemini", at: "2026-09-12T03:16:00Z" }
verified:
  - { by: "machine:gemini", status: "non-ratifie" }
sources:
  - id: repo-life-os-2026
    resource: "https://github.com/Amdkn/Life-OS-2026.git"
    author: "human:amdkn"
    last_modified: 2026-09-12
okf_version: "0.2"
---

# Migration Life-OS-2026 Racine, Déblocage Port 4444 & Délégation Jules 12WY Glassmorphism

## 1. Contexte & Diagnostic de Blocage
- **Emplacement Historique Inadéquat** : `Life-OS-2026` était enfoui dans l'archive VPS `C:\Users\amado\vps-archive-2026-06-17\srv\aspace\web\Life-OS-2026`.
- **Blocage Supabase Offline** : La mise en pause du plan gratuit Supabase bloquait l'application locale sur le splash d'attente *"CHECKING MEMORY INTEGRITY..."* (`showMigration === null` dans `src/App.tsx`).
- **Objectif Souverain** :
  1. Déplacer l'application à la racine de l'utilisateur (`C:\Users\amado\Life-OS-2026`).
  2. Rétablir l'écoute et le service actif sur le port `4444` (`http://127.0.0.1:4444/`).
  3. Neutraliser le blocage Supabase pour un boot local instantané.
  4. Committer et synchroniser le push GitHub sur `origin main`.
  5. Préparer le dossier et le brief de délégation `delegation-a-jules/` pour que Jules structure le moteur local SQLite et refonde les interfaces 12WY en Glassmorphism Solarpunk avec Stitch.

## 2. Actions Opérationnelles Exécutées
1. **Migration Physique & Jonction des Modules** :
   - Transfert complet vers `C:\Users\amado\Life-OS-2026`.
   - Jonction de répertoire NTFS (`mklink /J`) pour `node_modules` afin de garantir la portabilité sans réinstallation lourde.
2. **Résolution du Bug de Blocage Local (`src/App.tsx`)** :
   - Conditionnement du splash de migration : `if (!isLocal && showMigration === null)` pour permettre au mode local d'accéder instantanément au Desktop sans attendre une réponse réseau de Supabase.
3. **Validation du Build de Production** :
   - `vite build` exécuté et validé avec succès en 2m 8s (0 erreur).
4. **Synchronisation Git & Push GitHub** :
   - Restauration de la connexion au dépôt distant `https://github.com/Amdkn/Life-OS-2026.git`.
   - Commit `f5d21f4` : migration, bypass local offline.
   - Commit `8045c05` : brief Jules.
   - Poussé avec succès sur la branche `main` distante.
5. **Dossier de Délégation Jules Préparé** :
   - Document rédigé et committé sous `C:\Users\amado\Life-OS-2026\delegation-a-jules\PRD-12WY-SQLITE-GLASSMORPHISM.md`.
6. **Serveur Dev Actif sur Port 4444** :
   - Vite lancé en tâche de fond sur `http://127.0.0.1:4444/` (HTTP 200 OK validé par curl).

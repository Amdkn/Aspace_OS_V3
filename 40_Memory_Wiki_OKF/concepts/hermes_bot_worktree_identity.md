---
okf_version: "0.2"
title: Hermes Bot Mode et worktrees Orca
date: 2026-09-24
status: configuration-verified
---

Une identite Doctor/Compagnon possede un profil Hermes persistant et un worktree Git distinct dans Orca. Les 3 Doctors et 9 Compagnons reutilisent leurs profils et worktrees existants.

Le profil isole memoire, configuration et historique. Le worktree isole fichiers et branche. Le home core reste une responsabilite, sans exclusivite de portee.

La correspondance et les commandes exactes sont dans `10_Tech_OS/reports/hermes_bot_worktree_bindings.json`. Chaque lanceur utilise `chat --in <worktree> --continue "Bot Chat" --create-if-missing`. Les identifiants de profils historiques sont conserves; les noms affiches sont canoniques.

Cette configuration ne prouve aucune execution autonome. Une tache en cours exige un claim WorkGraph valide et une execution observee. Les sessions ouvertes avant le rattachement sont preservees et ne changent pas automatiquement de profil ou de repertoire.

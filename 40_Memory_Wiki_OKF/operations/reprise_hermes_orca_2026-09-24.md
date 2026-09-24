---
okf_version: "0.2"
type: Operational memory
title: Reprise A Space — Hermes Bot Mode, Orca et travaux acceptés
date: 2026-09-24
status: machine-verified-with-explicit-limits
sources:
  - resource: 10_Tech_OS/reports/hermes_bot_worktree_bindings.json
  - resource: 10_Tech_OS/reports/ker44_final_acceptance.json
  - resource: 10_Tech_OS/reports/ker44_independent_review_final.json
  - resource: 10_Tech_OS/kernel/uc.db
---

# Décisions à préserver

Amadou demande de l'exécution concrète et la réutilisation des sessions et espaces existants. Orca reste l'ADE. WorkGraph reste la source des tâches, claims, preuves et gates. Un profil, un port, une fenêtre ouverte ou un roster peuplé ne prouvent pas une exécution.

Le choix confirmé le 24 septembre est un worktree distinct pour chacun des trois Doctors et des neuf Compagnons de la constitution KER-44. Les worktrees isolent les fichiers et branches; les profils Hermes isolent configuration, mémoire et historique. Le home core ne limite pas la portée transversale L0/L1/L2.

# État confirmé et portée des preuves

- WorkGraph 181 : done, correctif de dispatch véridique accepté après revue Hermes et 21 tests. Référence Git : 8de0a13cd79c337f3536cf5c74949da2372eb108.
- WorkGraph 180 / KER-44 : done. Constitution, validation de topologie/autorité, projections SQLite bornées et API GET acceptées. 40 tests réussis, revue indépendante Hermes PASS. Références : V3 038dff0ef2d10e8d485a8f53e5e57485853bc39d; Agent-OS-Desktop 6db8908d12a23b2043e4b2be8d8cabc2bce497e9.
- Les 96 PR ouvertes de Amdkn/Aspace_OS_V3 ont été fermées sur demande explicite, SANS fusion et SANS suppression de branches. Le contrôle réalisé après cette opération a trouvé 96 CLOSED non fusionnées et zéro ouverte. Ce zéro est une observation historique, pas une garantie sur les nouvelles PR. Ne jamais assimiler cette fermeture à une intégration du code ni clôturer les travaux associés pour ce seul motif.
- Liaison Hermes/Orca : 12/12 correspondances vérifiées (profil, dossier, branche, nom Orca et lanceur). Référence V3 : eb12e2dbd9137a67d6d86697e543ad4f86f10053. C'est une configuration vérifiée, pas une preuve de bots en activité.

# Piège découvert : deux emplacements Hermes

Sur ce poste, l'installation réellement interrogée utilise `C:/Users/amado/AppData/Local/hermes`. Des fichiers d'identité existent aussi dans `C:/Users/amado/.hermes/profiles`, mais les modifier seuls ne configure pas les profils utilisés par le binaire. Vérifier le home effectif avant toute intervention; ne pas recopier aveuglément les identifiants OAuth.

Les identifiants historiques tels que `doctor11_review_l1` et `amy_spec_l1` sont conservés pour protéger les références et historiques. Leurs noms affichés sont canoniques. Cela ne valide pas automatiquement tout le contenu historique de leurs SOUL ou leurs permissions.

# Raccordement et reprise

Consulter `10_Tech_OS/reports/hermes_bot_worktree_bindings.json` pour les 12 correspondances exactes, commandes et emplacement des sauvegardes. Les lanceurs sont dans `C:/Users/amado/.aspace/launchers/hermes-bots/`.

Chaque profil a `terminal.cwd` fixé au worktree associé. Les lanceurs utilisent `chat --in <worktree> --continue "Bot Chat" --create-if-missing` pour choisir explicitement le dossier et reprendre/créer la conversation canonique. Les sessions déjà ouvertes n'ont pas été redémarrées ni migrées. Ne pas démarrer un second processus écrivain sur un profil déjà occupé. Rick n'a pas été reconfiguré par cette opération.

Les sauvegardes des configurations antérieures sont référencées dans le registre. Une restauration doit viser seulement les champs modifiés et préserver toute évolution ultérieure; ne pas écraser globalement le profil ou sa mémoire.

# Prochaines preuves à obtenir

1. Vérifier le rendu réel de Bot Mode puis une exécution bornée avec le bon profil et le bon dossier, en réutilisant une session appropriée et en respectant les limites de population du Watchdog.
2. Vérifier l'alignement des instructions des profils historiques avec la constitution canonique avant une délégation autonome.
3. Corriger le démarrage complet d'Agent OS : une erreur de l'optimiseur Vite lisant `imports` l'a bloqué. L'API a été testée dans un serveur Vite limité à son plugin; cela ne certifie pas l'interface complète.

Ne pas rouvrir 180/181 uniquement parce que ces validations distinctes restent à faire. Ne pas annoncer une flotte autonome tant que le cycle tâche → exécution → preuve → revue → gate n'est pas observé.

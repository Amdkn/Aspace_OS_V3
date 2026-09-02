---
type: Playbook
title: Fenêtres qui clignotent — onze hooks Orca morts dans settings.json
description: Onze hooks pointaient vers un endpoint Orca éteint ; quatre tiraient à chaque appel d'outil, ouvrant un onglet Windows Terminal à chaque fois, pour un script qui sortait à sa première condition.
tags: [claude-code, hooks, windows, orca, settings-json, diagnostic]
generated: { by: claude-opus-5, at: 2026-08-29T00:10:00Z }
verified:
  - { by: human:amdkn, at: 2026-08-31T21:35:34Z }
  - { by: claude-opus-5, at: 2026-08-29T00:05:00Z }
sources:
  - id: settings-hooks
    resource: "C:/Users/amado/.claude/settings.json (section hooks)"
    title: Onze entrées de hooks visant ~/.orca/agent-hooks/claude-hook.cmd
    last_modified: 2026-08-29
  - id: hook-script
    resource: "C:/Users/amado/.orca/agent-hooks/claude-hook.cmd"
    title: Script de hook Orca — sort si ORCA_AGENT_HOOK_PORT est vide
    last_modified: 2026-08-27
okf_version: "0.2"
---

Symptôme : une fenêtre de terminal apparaît et disparaît sans cesse pendant
qu'une session Claude Code travaille.

Cause : **onze** entrées de hooks dans `settings.json` invoquaient
`~/.orca/agent-hooks/claude-hook.cmd` via un `powershell.exe -EncodedCommand`.
Quatre d'entre elles — `PreToolUse`, `PostToolUse`, `PostToolUseFailure`,
`PermissionRequest` — portent `matcher: "*"` et tirent donc **à chaque appel
d'outil**. Chacune lance `powershell.exe` puis `cmd.exe`.

Sous Windows 11, toute allocation de console ouvre une fenêtre **Windows
Terminal** avec un onglet. `-WindowStyle Hidden` n'empêche pas le flash : la
console est allouée avant que le style ne s'applique.

**Ces hooks ne faisaient rien.** Le script sort à sa première condition :

```
if "%ORCA_AGENT_HOOK_PORT%"=="" exit /b 0
```

Mesure du 2026-08-28 : `ORCA_AGENT_HOOK_PORT`, `ORCA_AGENT_HOOK_TOKEN`,
`ORCA_PANE_KEY` et `ORCA_AGENT_HOOK_ENDPOINT` **toutes vides**, aucun processus
Orca en vie. Coût net : deux processus par appel d'outil, zéro effet.

## Le geste

```bash
python "C:/Users/amado/.claude/outils/nettoyer-hooks-orca.py"
```

Simulation par défaut ; `--appliquer` pour écrire, avec sauvegarde horodatée.
Le hook `herdr-agent-state.ps1` (`SessionStart`) est **conservé** : il ne tire
qu'une fois par session et n'est pas en cause.

**À lancer Claude Code fermé.** CC réécrit `settings.json` depuis sa config en
mémoire à la fermeture ; une édition faite pendant qu'une session tourne est
écrasée. Les hooks sont par ailleurs lus au démarrage, donc le clignotement
persiste jusqu'au redémarrage même après nettoyage du fichier.

## Trois pièges payés en le corrigeant

**Le chemin est caché dans du base64.** Chercher `orca` dans `settings.json` ne
rend rien : la commande est un `-EncodedCommand` en base64 UTF-16LE. Il faut
décoder chaque charge avant de filtrer, sinon on conclut à tort que les hooks
ne visent pas Orca.

**`Path.home()` ignore `HOME` sous Windows** — il suit `USERPROFILE`. Poser
`HOME=/tmp/faux` pour isoler un test ne protège rien : le script a édité le
vrai `settings.json`. D'où l'option `--fichier` du script, seule manière sûre
de le tester. Même famille que le piège de précédence d'environnement des
lancements `claude -p`.

**Un script qui n'arrête pas sur erreur annonce un faux succès.** Une première
version affichait « réglages mis à jour » alors que `Set-ScheduledTask` venait
d'échouer en `0x80041319`, faute de `$ErrorActionPreference = 'Stop'`. Le même
défaut que le `exit 0` trompeur d'un agent qui n'a touché aucune ligne.

## Comment vérifier

Relancer le script : il doit dire `rien a retirer`. Puis, session redémarrée,
travailler quelques minutes sans voir de fenêtre apparaître.

## Comment défaire

Recopier la sauvegarde `settings.json.avant-nettoyage-<horodatage>` par-dessus
`settings.json`, Claude Code fermé.

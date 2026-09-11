---
type: Playbook
title: WSL de ce poste — le distro par défaut est docker-desktop et ne peut pas exécuter bash
description: Toute commande wsl.exe sans « -d Ubuntu-24.04 » échoue (execvpe bash failed) ; /tmp est tmpfs et survit mal aux arrêts de VM ; Playwright vit dans ~/gauntlet-eyes côté Ubuntu-24.04.
tags: [wsl, windows, playwright, verification, piege]
generated: { by: claude-sonnet-4-6, at: 2026-09-09 }
verified:
  - { by: claude-sonnet-4-6, at: 2026-09-09 }
sources:
  - id: wsl-probe-2026-09-09
    resource: wsl.exe --status ; wsl.exe -l -v (poste amdkn)
    title: Mesure directe des distros WSL
    last_modified: 2026-09-09
okf_version: "0.2"
---

# Le distro WSL par défaut est cassé pour bash

**Fait mesuré (2026-09-09)** : `wsl -e bash -lc '…'` répond
`execvpe(bash) failed: No such file or directory` car le distro par défaut est
`docker-desktop` (arrêté, sans bash utile). `wsl -l -v` montre pourtant que
**Ubuntu-24.04 existe**. Un sondage antérieur (gate G5 de `agent-os/desktop`,
abandon noté « Playwright absent de ~/gauntlet-eyes ») a conclu à l'absence de
Playwright en ayant en réalité frappé le mauvais distro — Playwright y est
présent et fonctionnel.

**Règle** : toujours `wsl.exe -d Ubuntu-24.04 -e bash -lc '…'` sur ce poste.

## Pièges associés, mesurés le même jour

- **/tmp est tmpfs** (Ubuntu 24.04) et la VM WSL s'arrête entre deux
  invocations `wsl.exe` : un fichier écrit dans /tmp par une commande a
  disparu à la suivante. Écrire les scripts temporaires dans `~/` ou
  `/mnt/c/...`.
- **Playwright + Chromium** sont installés dans `~/gauntlet-eyes`
  (node_modules + `~/.cache/ms-playwright`, chromium-1234). Les scripts de
  vérification qui importent Playwright doivent tourner **depuis WSL** (leur
  `homedir()` vise ce chemin).
- **localhost fonctionne dans les deux sens** (réseau mirrored) : le serveur
  Vite de `agent-os/desktop` sur 5555 répond 200 depuis Ubuntu-24.04.

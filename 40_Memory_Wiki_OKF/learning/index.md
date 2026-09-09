---
type: Bundle index
title: learning — les échecs mesurés, pour ne pas les rejouer
description: Ce sous-bundle ne consigne pas ce qui marche, mais ce qui a échoué et pourquoi. Premier dossier ouvert : Multica, 323 sessions et 36 fiches d'instruction, dont la panne centrale a été rejouée le 2026-08-29 par l'agent qui écrit ces lignes.
tags: [learning, echecs, multica, gouvernance, agents, retour-experience]
generated: { by: claude-opus-5, at: 2026-08-29T22:30:00Z }
verified:
  - { by: claude-opus-5, at: 2026-08-29T22:30:00Z }
okf_version: "0.2"
---

Les autres sous-bundles disent comment les choses marchent. Celui-ci dit
**comment elles ont cassé**, et ce que ça coûte de le redécouvrir.

Un échec n'entre ici qu'avec trois choses : ce qui était attendu, ce qui s'est
produit, et la **mesure** qui le prouve. Une impression n'est pas un échec ;
c'est une hypothèse.

## Pourquoi ce bundle existe

Parce que la même panne se rejoue. Le dossier Multica documente une panne de
gouvernance identifiée le 2026-07-05, écrite noir sur blanc dans les
instructions d'A0 — et **rejouée intégralement le 2026-08-29**, pendant une
session de sept heures, par un agent qui avait ces instructions à portée de
lecture et ne les a pas lues.

Consigner l'échec ne suffit donc pas. Ce bundle doit être **lu au démarrage**,
pas consulté après coup. C'est pourquoi son point d'entrée figure dans la table
du `CLAUDE.md` racine.

# Files

- [La panne du governor module](multica-governor-module.md) - L'échec central de Multica : des agents à qui l'on donne « Autonomie Absolue » et qui s'arrêtent quand même. 254 sessions sur 323 parlent de gate ou de permission, 61 d'arrêt prématuré. Identifiée en juillet, rejouée en août.
- [WSL : distro par défaut cassé](wsl-distro-par-defaut-casse.md) - `wsl -e bash` échoue (défaut = docker-desktop) ; il faut `-d Ubuntu-24.04`. Un abandon de gate G5 a faussement conclu « Playwright absent » à cause de ce distro. /tmp est tmpfs, localhost mirrored.

# Directories

*(aucun pour l'instant — un dossier par famille d'échec quand il y en aura plusieurs)*

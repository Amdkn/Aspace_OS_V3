---
type: Decision
title: Omarchy ne peut pas tourner sous WSL, et n'est pas la couche A0
description: Deux gardes d'installation sont inatteignables sous WSL (bootloader limine, racine btrfs) ; et au-delà de la faisabilité, Omarchy est un poste de travail humain, pas un substrat d'orchestration — le rôle A0 est déjà tenu par Herdr + Ori.
tags: [omarchy, wsl, a0, architecture, jumeau-numerique, herdr, ori, arch, hyprland]
generated: { by: claude-opus-5, at: 2026-08-29T02:00:00Z }
verified:
  - { by: human:amdkn, at: 2026-08-31T21:31:58Z }
  - { by: claude-opus-5, at: 2026-08-29T02:00:00Z }
sources:
  - id: omarchy-guard
    resource: "https://raw.githubusercontent.com/basecamp/omarchy/master/install/preflight/guard.sh"
    title: Gardes d'installation d'Omarchy — conditions refusées
    last_modified: 2026-08-29
  - id: omarchy-tree
    resource: "GET api.github.com/repos/basecamp/omarchy/git/trees/master?recursive=1 — 1389 fichiers"
    title: Arborescence complète — 81 fichiers hyprland, limine, plymouth, mkinitcpio
    last_modified: 2026-08-29
  - id: a0-memoire
    resource: "~/.claude/projects/C--Users-amado/memory/a0-orchestrateur-de-cadences.md"
    title: Définition d'A0 — orchestrateur immortel, quatre couches
    last_modified: 2026-08-12
okf_version: "0.2"
---

`basecamp/omarchy` (33 775★, MIT, Shell) se décrit comme *« a beautiful, modern
& opinionated Linux distribution by DHH »*. **Distribution**, pas jeu de
dotfiles — et c'est toute la question.

## Sous WSL : non, et pas pour une raison contournable

`install/preflight/guard.sh` énumère ses conditions. Deux sont
**structurellement inatteignables dans WSL** :

```bash
command -v limine &>/dev/null || abort "Limine bootloader"
[[ $(findmnt -n -o FSTYPE /) = "btrfs" ]] || abort "Btrfs root filesystem"
```

- **Bootloader limine** : WSL n'a pas d'amorçage. C'est Windows qui démarre ;
  le noyau WSL2 appartient à Microsoft. Aucun bootloader ne peut exister là.
- **Racine btrfs** : la racine WSL2 est en ext4 dans un VHDX. On peut attacher
  d'autres disques, pas changer la nature du système de fichiers racine.

Les autres gardes (Arch vanilla, x86_64, Secure Boot désactivé, ni GNOME ni
KDE) sont accessoires à côté.

Le garde n'interdit pas absolument — il propose
`gum confirm "Proceed anyway on your own accord and without assistance?"`.
Passer outre installerait quand même une pile qui n'a rien où s'accrocher :
`install/login/` pose **sddm**, **plymouth**, **l'hibernation** et
**limine-snapper** ; `install/preflight/disable-mkinitcpio.sh` touche à
l'initramfs. Rien de tout cela n'existe dans un conteneur WSL.

**Le cœur d'Omarchy est Hyprland — 81 fichiers dans l'arborescence.** Un
compositeur Wayland réclame un siège DRM/KMS. WSLg fournit déjà son propre
compositeur ; y imbriquer Hyprland n'est pas le produit qu'on croit installer.

Zéro occurrence de `wsl`, `virt`, `kvm` ou `headless` dans les 1389 fichiers du
dépôt. **Le support bare-metal n'est pas un oubli, c'est le périmètre.**

## Au-delà de la faisabilité : ce n'est pas A0

A0 est défini sur ce poste comme *« l'orchestrateur immortel… ne rend jamais la
main… ne produit rien ; il orchestre »*. Sa vertu est la **durée** : tenir
douze heures, basculer de fournisseur plutôt que mourir.

Omarchy est un **poste de travail humain** : thèmes, plymouth, raccourcis,
gestion des moniteurs, splash de démarrage. Sa valeur est l'expérience devant
l'écran. A0 n'a pas d'écran — il tourne sans personne.

Ce qu'Omarchy apporterait à A0 : rien qu'un Arch nu n'apporte déjà.
Ce dont A0 a besoin — supervision de processus, rotation de fournisseur,
persistance d'état — Omarchy n'en fournit aucun.

**Le rôle A0 est déjà tenu, et par autre chose** : Herdr sait *quand* un agent
travaille, Ori sait *quoi* lancer et *sur quel modèle*. C'est exactement un
substrat d'orchestration — voir [[herdr-ori-substrat-orchestration]].

## Le mappage Beth/Morty est inversé

Proposition examinée : *Herdr = Gatekeeper A1 Beth, Ori = A1 Morty*.

Les rôles enregistrés disent l'inverse :

| | Rôle | Outil qui lui ressemble |
|---|---|---|
| **Beth** (spec-loop) | **spécifie** : écrit la prochaine petite spec et l'implémente | **Ori** — features déclaratives, `defineSchedule`, lance un harnais avec un modèle choisi |
| **Morty** (babysitter) | **fait obéir** : vérifie que ce qui a été décidé est fait, signale la dérive | **Herdr** — observe les panes, `agent wait --status` bloque jusqu'au changement d'état, événements, portes |

Le mot « Gatekeeper » employé pour Herdr décrit précisément le travail de
Morty, pas celui de Beth. **Si l'on garde le mappage, il faut l'inverser.**

Mais il y a plus gênant que l'inversion : **Herdr et Ori sont du substrat, pas
de la logique de boucle.** Beth et Morty sont des boucles (spec-loop,
babysitter) ; Herdr et Ori sont le terminal et le routage de modèles sur
lesquels ces boucles s'exécutent. Les faire tenir le rôle d'A1 confond deux
couches.

### Découpage proposé

- **A0** — le runtime immortel **plus son substrat** : Herdr (supervision des
  panes et de l'état) + Ori (routage de modèles et lancement de harnais).
- **A1** — Beth (`spec-loop`) et Morty (`babysitter`), inchangés : la boucle
  qui garde ou qui jette.
- **Omarchy** — orthogonal aux quatre couches. C'est le poste de l'humain,
  pas un étage du jumeau.

## Si Omarchy est voulu quand même

Le seul déploiement conforme est **bare-metal ou double amorçage** : Arch
vanilla, racine btrfs, limine, Secure Boot désactivé.

**Et c'est là que le coût opérationnel apparaît.** Tout le socle vit
aujourd'hui sous Windows : agentgateway, le relais OpenRouter et sa tâche
planifiée, Herdr et ses intégrations, les harnais Claude Code / Codex /
Hermes. **Démarrer sous Omarchy, c'est éteindre tout cela** — les deux
systèmes ne tournent jamais ensemble.

Un double amorçage contredit frontalement la propriété qui définit A0 :
*ne jamais rendre la main*. On ne peut pas être immortel une moitié du temps.

Une partition de partage (NTFS ou exFAT, lisible des deux côtés) résout
l'échange de **fichiers**, pas la continuité de **service**. Noter au passage
que Windows ne lit pas btrfs nativement : la partition partagée ne peut pas
être la racine d'Omarchy.

## Ce qui répond au besoin réel

Le besoin annoncé est l'**entraînement à la version Linux avant mise en
production**. Ce qu'il faut pour cela est la parité du *runtime* — paquets,
chemins, permissions, systemd utilisateur — pas la parité du *bureau*. Hyprland
et plymouth ne changent rien à la façon dont un agent tourne.

WSL Ubuntu-24.04 donne déjà cette parité, et Ori y lance 8 harnais. Pour aller
plus loin sans quitter Windows : une distro Arch sous WSL (`ArchWSL`) offre la
parité de gestionnaire de paquets — la partie d'Omarchy qui compte vraiment
pour un runtime headless.

## Comment vérifier

```bash
curl -s https://raw.githubusercontent.com/basecamp/omarchy/master/install/preflight/guard.sh
```

Les conditions y sont en clair. Toute évolution du support (VM, WSL) s'y
verrait avant d'apparaître dans un billet.

---
type: Playbook
title: Rendre WSL persistant et auto-reparant sans fenetre au premier plan
description: La distro tombe dans un etat "Running mais injoignable" qui tue les sessions Ori ; un gardien detache par le planificateur de taches la releve seul en 45 secondes.
tags: [wsl, ori, persistance, antifragile, powershell, tache-planifiee, windows]
generated: { by: claude-opus-5, at: 2026-08-28T20:15:00Z }
verified:
  - { by: claude-opus-5, at: 2026-08-28T20:15:00Z }
sources:
  - id: mesure-chute
    resource: "Wsl/Service/0x8007274c observe 4 fois entre 14h et 16h le 2026-08-28"
    title: Chutes repetees d'Ubuntu-24.04 pendant une session Ori
    last_modified: 2026-08-28
  - id: gardien
    resource: "C:\\Users\\amado\\bin\\wsl-gardien.ps1 + tache planifiee WSL-Gardien"
    title: Gardien WSL
    last_modified: 2026-08-28
okf_version: "0.2"
---

## Le defaut

Ubuntu-24.04 tombe dans un etat ou `wsl -l -v` affiche **`Running`** alors
que toute connexion echoue :

```
Wsl/Service/0x8007274c
```

Observe quatre fois en deux heures le 2026-08-28. Ori vit dans cette distro,
donc chaque chute tue la session en cours — et le message ne dit pas que la
distro est morte, il dit qu'un hote ne repond pas, ce qui envoie chercher du
cote du reseau.

Le seul remede connu est `wsl --terminate <distro>` suivi d'une relance.

## Ce qui ne marche PAS : lancer le gardien depuis un agent

Premiere tentative : un `.vbs` dans le dossier Demarrage, lance a la main
via `cscript` depuis une session d'agent. Le gardien demarrait, ecrivait sa
premiere ligne de journal, puis **mourait en silence**.

Cause : le processus etait enfant du `bash.exe` de l'outil qui l'avait
lance. **Quand l'appel d'outil se termine, Windows fauche tout l'arbre de
processus.** C'est le meme piege que celui deja paye sur BMad Loop, ou il
fallait `setsid nohup` pour survivre.

Un daemon lance depuis un agent n'est pas un daemon : c'est un enfant en
sursis. Il faut un proprietaire qui survit a la session.

## Ce qui marche : une tache planifiee

```powershell
$a = New-ScheduledTaskAction -Execute 'powershell.exe' `
     -Argument '-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File "C:\Users\amado\bin\wsl-gardien.ps1"'
$t = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME
$p = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited
$s = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries `
     -StartWhenAvailable -RestartCount 999 -RestartInterval (New-TimeSpan -Minutes 1) `
     -ExecutionTimeLimit (New-TimeSpan -Seconds 0) -MultipleInstances IgnoreNew -Hidden
Register-ScheduledTask -TaskName 'WSL-Gardien' -Action $a -Trigger $t -Principal $p -Settings $s -Force
```

Trois reglages font tout le travail et se perdent facilement :

- `ExecutionTimeLimit 0` : sans lui le planificateur tue la boucle au bout
  de 3 jours par defaut.
- `RestartCount 999` + `RestartInterval 1min` : c'est **la** partie
  antifragile. Le gardien lui-meme est surveille.
- `MultipleInstances IgnoreNew` : evite d'empiler deux gardiens qui se
  battraient pour la meme ancre.

## Aucune fenetre au premier plan

Exigence explicite : rien ne doit clignoter pendant le travail. Deux
precautions, la seconde etant celle qu'on oublie :

1. `-WindowStyle Hidden` sur le powershell lance, et `-Hidden` sur la tache.
2. **Chaque processus enfant part avec `CreateNoWindow = $true` et
   `UseShellExecute = $false`**, via `System.Diagnostics.ProcessStartInfo`.
   Un `Start-Process` nu fait clignoter une console a chaque sonde, soit
   une fois par minute.

## Les deux mecanismes du gardien

- **Ancre** : un `wsl -d <distro> -u root -e sleep infinity` maintenu
  vivant. Tant qu'un processus tourne, la VM ne se considere pas inactive.
- **Sonde** : toutes les 60 s, `wsl -d <distro> -e true` avec minuteur de
  25 s. **Deux echecs consecutifs** avant d'agir : une sonde isolee peut
  expirer parce que la machine est chargee, et terminer une distro saine
  couterait la session en cours. Au deuxieme echec, `--terminate` puis
  relance.

En ceinture, dans `~/.wslconfig` :

```ini
[wsl2]
vmIdleTimeout=-1
```

Sans cette ligne, WSL2 detruit la VM apres une periode d'inactivite. Prend
effet au prochain `wsl --shutdown`, pas a chaud.

## Verification, mesuree et non supposee

```
15:56:35  wsl --terminate Ubuntu-24.04   (provoque a la main)
15:57:20  ancre (re)posee, pid=21532     (journal du gardien)
          wsl -l -v : Ubuntu-24.04  Running
```

**45 secondes, sans intervention.** Le journal vit dans
`C:\Users\amado\bin\wsl-gardien.log`, avec rotation a 2000 lignes.

Ce premier test provoquait un arret **propre**. Une vraie chute est
survenue d'elle-meme quinze minutes plus tard, et le journal montre les
deux regles de conception validees coup sur coup :

```
16:03:08  sonde en echec (1) : la distro ne repond pas
16:04:46  distro de nouveau joignable apres 1 echec(s)     <- pas d'action
16:06:26  sonde en echec (1) : la distro ne repond pas
16:08:06  sonde en echec (2) : la distro ne repond pas
16:08:09  reparation : wsl --terminate Ubuntu-24.04
16:08:40  reparation reussie                               <- 31 secondes
```

La premiere sequence justifie a elle seule la regle des **deux echecs
consecutifs** : la distro s'est retablie seule en 98 secondes. Un gardien
qui aurait agi des le premier echec aurait termine une distro en train de
revenir, et tue la session pour rien.

La seconde prouve le chemin de reparation sur un defaut spontane, pas
simule.

## Le piege ASCII de PowerShell 5.1

Le script a d'abord refuse de se charger sur un
`Unexpected token '}'` situe **des dizaines de lignes plus bas** que la
vraie faute.

Cause : PowerShell 5.1 lit les `.ps1` en Windows-1252. Un tiret cadratin
UTF-8 (`—`) y devient trois octets **dont un guillemet**, qui ferme la
chaine en cours et decale tout le reste du fichier.

**Ecrire les `.ps1` en ASCII pur**, ou les enregistrer avec BOM. Le message
d'erreur ne designera jamais le vrai coupable.

## Ce que ca ne fait pas

- Ne repare pas une distro corrompue : `--terminate` ne soigne qu'un etat
  transitoire.
- Ne survit pas a une session Windows fermee (declencheur `AtLogOn`). Pour
  un serveur, il faudrait `-LogonType ServiceAccount`, qui exige des droits
  d'administrateur.
- Ne remplace pas `wsl --shutdown` pour rendre la RAM : `vmIdleTimeout=-1`
  garde justement la VM en vie, donc sa memoire avec.

## Comment le retirer

```powershell
Unregister-ScheduledTask -TaskName 'WSL-Gardien' -Confirm:$false
Get-Process powershell | Where-Object { $_.Path } | Stop-Process   # ou cibler le pid du gardien
```

Puis retirer `vmIdleTimeout=-1` de `~/.wslconfig` (sauvegardes
`.wslconfig.bak.*` a cote) et supprimer `C:\Users\amado\bin\wsl-gardien.ps1`.

## Trouve en chemin, non corrige

La tache planifiee **`WSL-Kernel-WakeUp`** cible `wsl.exe -d Ubuntu` — une
distro qui n'existe pas sur ce poste (il y a `Ubuntu-24.04` et
`docker-desktop`). Elle echoue donc a chaque ouverture de session
(`LastTaskResult = 1`) depuis un moment, silencieusement, alors qu'elle est
censee reveiller la cascade gateway -> bridge -> mission-control.

Sa correction exige des droits d'administrateur (`Set-ScheduledTask` rend
`Access is denied`). A lancer dans un terminal eleve :

```powershell
$t = Get-ScheduledTask -TaskName 'WSL-Kernel-WakeUp'
$new = $t.Actions[0].Arguments -replace 'wsl\.exe -d Ubuntu ', 'wsl.exe -d Ubuntu-24.04 '
Set-ScheduledTask -TaskName 'WSL-Kernel-WakeUp' -Action (New-ScheduledTaskAction -Execute $t.Actions[0].Execute -Argument $new)
```

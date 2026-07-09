# panes.json — le layout Citadelle de départ (cockpit RunPane, W28 M4 / W18 M2)

Les 3 premiers "nœuds N8N" de la flotte, rendus VISIBLES dans Pane (fin du cron invisible) :

| Pane | Rôle | Commande |
|---|---|---|
| `airlock-veto` | Le killswitch paperclip VISIBLE — relance la gate toutes les 5 min, affiche la ligne `B1·B2·B3·B4·GO` | boucle `spock_airlock.py` |
| `wf1-morty` | Le battement WF1 (worklog live) | `Get-Content -Wait worklog.md` |
| `heartbeat-warmode` | Le journal des tours (digest) | `Get-Content -Wait turn-journal.md` |

Tous en `source:agent` + `noFocus` → créés en arrière-plan, A0 garde le focus (contrat RunPane : panes agent = background par défaut).

## Lancement (quand le daemon est joignable)

```bash
powershell.exe -NoProfile -Command "Set-Location \$env:TEMP; runpane panes create --from-json C:\Users\amado\agent-os\citadel\loops\artifacts\panes.json --yes --json"
```

## 2 confirmations AVANT de lancer (D1 — non vérifiées daemon-down)

1. **Forme top-level `--from-json`** : ce fichier est un **array** de payloads `panes.create` (le contrat dit « create one or more »). Si le daemon rejette l'array → wrapper en `{"panes":[ ... ]}`. Source de vérité : `contracts/runpane/contract.json` §`jsonSchemas` (repo dcouple/Pane). Vérifier via `runpane agent-context --command "panes create" --json`.
2. **Repo `active` saved** : `--repo active` suppose qu'un repo est enregistré dans Pane. Si `runpane repos list --json` est vide → `runpane repos add --path C:\Users\amado\agent-os --yes --json` d'abord (le dir doit être un repo git).

## État daemon au moment de l'écriture (2026-07-08)

`runpane doctor --json` → `daemon.reachable:false`, `connect ENOENT \\.\pipe\pane-daemon-047a1746a20eea93`. CLI OK (`runpane 2.4.15` global), app trouvée (`C:\Program Files\Pane\Pane.exe`), mais le pipe daemon n'écoute pas. NextCommand du tool : **« Open Pane, then rerun runpane doctor --json »**. Lié probablement au `.pane/_TRASH_2026-07-08_orchestrator_switch`.

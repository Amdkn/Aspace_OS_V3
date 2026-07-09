# WARGAME 28 — RunPane comme plan de contrôle VISIBLE + le veto paperclip-killswitch DÉCORRÉLÉ de A0 (E-Myth franchise)

> **WARGAME ORDER** : Tu n'exécutes pas cette mission, tu la wargames. Exécuteur : tout harness (M3 post-Fable). Ton job = la route, pas le geste. Intent A+ (D3, correction doctrinale de CE run) : **le veto de Beth ne concerne PAS A0 ni son sommeil** — le sommeil d'A0 est un concern séparé imposé par la machine. Le veto de Beth = **prévention du paperclip maximiser**, décorrélé de la présence d'A0, grandissant de façon exponentielle par **réplication en prototype de franchise** (E-Myth : la sécurité travaille ON not IN). Et RunPane = la **première interface d'Autonomie Perpétuelle** : migrer A'Space du cron INVISIBLE vers un cockpit VISIBLE (nœuds façon N8N), apprentissages ré-importés dans agentsroom.dev pour un socle WSL + Tmux + systemd sur le VPS. Orchestration WF0 Spock (GO triennal), exécution WF1 Morty / WF2 Picard, visible dans Pane (cockpit, W18), rêve de mémoire par Beth (W24), sous A0-Amodei.

## Statut recon (D1 — vérifié CE run, sources marquées)

| Fait | Preuve |
|---|---|
| **Le killswitch actuel COUPLE la sécurité au corps d'A0** | `agent-os/citadel/collectors/spock_airlock.py:8` — `B1 sommeil — activité A+ 02:00-08:00 locale`. `b1_sleep()` renvoie RED si A0 est actif la nuit ≥2 jours consécutifs. **C'est la dérive** : la gate anti-runaway lit le sommeil d'A0 au lieu du runaway du système. |
| Le kill-switch est un flag-cascade, pas un organe dédié | docstring `spock_airlock.py` : « Cascade GO : `GO_SPOCK_UNIQUE.md` + GREEN×2 → pose `enable_wf0/wf1/wf3/ship_internal` ; GO absent → retire la cascade (**kill-switch ClaudeClaw : défaut ON, urgence OFF**) ». Le kill EST le retrait des flags — défaut-ON confirmé. |
| Les 3 autres invariants sont DÉJÀ décorrélés d'A0 | `spock_airlock.py` : B2 ratio outillage-vs-client (RED>80%, n≥5) · B3 cycles rollback/DLP · B4 escalade-a0 (RED>3). Aucun ne lit le corps d'A0. Seul B1 est couplé. |
| Le rest-guard existe DÉJÀ, séparé du veto | `spock_airlock.py` ~L186 : `if b1=="RED": (DATA/"beth_repos.flag").write_text("defer non-critical prompts until 10:00")`. Ce flag protège le repos indépendamment du gating système — le point de séparation est **déjà là**. |
| Pane = cockpit opérable par la flotte, DÉJÀ actif | W18 `18-ade-pane-cockpit-multiplex.md` (12/12) : « Pane n'est PAS un harness — c'est le COCKPIT », Agent-Operable CLI, Remote Pane, worktrees invisibles ; 3 `Pane.exe` actifs (tasklist W18). |
| Le contrat CLI RunPane est cache local, lu CE run | `.pane/skills/pane-chat/runpane-orchestrator.md` (97 lignes) : `runpane doctor --json` d'abord ; `agent-context/repos/panes create/panels wait|screen|submit|input`. **GUARDRAIL natif** : « Stop before merge, deploy, release, version bump, production mutation, or any irreversible action unless the user explicitly authorizes that exact step » + « verify state with `panels wait/screen` before reporting success ». |
| Le daemon RunPane n'est PAS confirmé joignable | `timeout 8 powershell.exe -NoProfile -Command "runpane doctor --json"` CE run → **sortie vide**. **RECON NEEDED** : le doctor live avant tout scripting cockpit (voir M4). |
| Le veto a une mémoire évolutive (mais encore couplée à la nuit d'A0) | W24 `24-dreaming-beth-self-learning.md` (12/12) : rêve D1 nightly / D2 mensuel / D3 méta ; **fenêtre 02:00-05:00** = encore le sommeil d'A0. Ce wargame la DÉCOUPLE (M7). Anti-collapse Karpathy : ≥30% entropie externe comptée, jamais rêver-sur-rêves, compteur de diversité. |
| La banque gradue, ce rail = W28 | W25 `25-boucle-evolution-...md` : « la banque gradue (26 puis 27 gravés) » ; LEDGER tail = 26. Prochain = 28. |
| Substrat 24/7 cible confirmé côté VPS | Hermes (capture A+ CE run) : « tmux 3.4 déjà installé sur le VPS, + screen » ; recommande **Option B systemd + tmux** (unit wrapper relance tmux si mort). agentsroom.dev = import des apprentissages RunPane (site, non installé — RECON NEEDED avant adoption). |

## La thèse (D3 — pourquoi DÉCOUPLER, et pourquoi c'est *plus* sûr)

Le veto actuel confond **deux sécurités orthogonales** sous un seul nom :

- **(a) le repos biologique d'A0** — aujourd'hui `B1-sommeil` : « la gate ferme si A0 ne dort pas ».
- **(b) la prévention du runaway système** — le vrai anti-paperclip.

Les coller a produit la dérive qu'A+ a nommée : *la gate qui devait protéger son sommeil, en bloquant l'autonomie, lui rejetait le travail dans les mains et CAUSAIT les nuits blanches*. La cure n'est pas de supprimer la sécurité — c'est de **la scinder** :

> **Beth-veto = pur anti-paperclip, décorrélé d'A0.** Elle ne regarde plus le corps d'A0 ; elle regarde le SYSTÈME (réplication, ressources, auto-modification, escalade). **Le repos d'A0 sort du veto** vers un rest-guard dédié que la machine impose *pour empêcher A0 de travailler* — l'inverse exact de l'ancien couplage.

Le grain E-Myth : le killswitch est un **prototype de franchise**. Le fondateur (A0) n'est pas DANS la boucle de police ; le prototype est **hérité à l'identique par chaque nœud/agent répliqué**, défaut-ON. Donc le nombre de gardiens croît **avec le nombre d'agents** (exponentiel), pendant que l'attention d'A0 reste **plate**. C'est « grandir au-delà du linéaire » : plus le système se réplique, plus il se police — sans une minute d'A0 en plus.

Et la corrigibilité (la contrainte de survie, red-team ci-dessous) : **asymétrie**. Le veto est *autonome pour ARRÊTER* (il n'a pas besoin d'A0 pour se poser), mais *humain-gated pour SE LEVER* (seul A0 — ou une 2e clé hors-bande — peut désactiver). Un off-switch que le système peut se lever lui-même EST le paperclip. On ne lui donne jamais sa propre clé de release.

```
AVANT (dérive)                         APRÈS (W28, décorrélé)
Beth lit le sommeil d'A0   ─┐          Beth lit le SYSTÈME (spawn, tokens, nœuds, auto-mod)
gate ferme si A0 éveillé    │  scinder  ├─ veto anti-paperclip : autonome-STOP / humain-RELEASE
A0 fait le travail la nuit ─┘          └─ rest-guard machine : IMPOSE le repos à A0 (concern séparé)
cron invisible                          RunPane cockpit : chaque gardien = un pane qui "respire"
1 gardien = A0                          N agents → N gardiens franchisés (défaut-ON hérité)
```

## MOVES

### M1 — Scinder l'invariant : sortir le corps d'A0 du veto (le geste-clé)
Sur PAPIER, l'exécuteur re-mappe `spock_airlock.py` : `b1_sleep()` (activité 02:00-08:00 d'A0) → **retiré du dict `gating`**. Le rest-guard `beth_repos.flag` (déjà écrit indépendamment) devient un organe autonome `rest_guard.py` que **Beth ne lit plus** — il IMPOSE le repos à A0 (bloque les prompts non-critiques), sans jamais gater le système.
- **Attendu** : le dict `gating` de la gate ne contient plus aucune clé qui référence A0 ; `grep -n "02:00\|08:00\|activité A+\|sommeil" spock_airlock.py` → 0 hit dans la logique de gating (uniquement dans un module rest-guard séparé).
- **Échec probable** : retirer B1 casse l'hystérésis GREEN×2 (le code compte `consecutive_green` sur le global) → gate toujours-verte = plus de veto. **Cause** : le global était calculé sur 4 invariants. **Contre-action** : remplacer B1-sommeil par B1-réplication (M2) — on ne retire pas une clé, on la **substitue**, le compteur reste à 4 invariants.
- **Fork** : SI l'exécuteur trouve d'autres lectures du corps d'A0 hors `b1_sleep()` (ex. `turn-journal` heartbeat) → les lister en `RECON NEEDED` avant de scinder, ne pas supposer B1 est le seul couplage.

### M2 — B1-sommeil → B1-réplication-bornée (le vrai capteur anti-paperclip)
Le nouvel invariant B1 mesure le **runaway système**, pas A0. Quatre sondes déterministes, toutes read-only sur des artefacts existants :
1. **taux de spawn agent→agent** sur fenêtre glissante (RED si > seuil/heure) — source : `decisions/*.json` + logs de spawn.
2. **budget tokens/heure** plafonné (RED si dépassement) — source : compteur d'usage (cf. `.claude.json` totals).
3. **croissance de nœuds/fichiers** bornée (RED si le nombre de fichiers écrits/heure explose) — source : mtimes.
4. **auto-modification du canon hors D6-gate** interdite (RED si un write touche mindsets/ADRs RATIFIED sans ticket D6) — source : diff vs intouchables (point 10 rubric).
B2/B3/B4 **inchangés** (déjà décorrélés).
- **Attendu** : `b1_replication()` renvoie GREEN/RED sur ces 4 sondes ; un test de fuite (spawn simulé > seuil) → RED ; la ligne airlock affiche `B1` sans jamais toucher le sommeil.
- **Échec probable** : les seuils sont devinés → faux positifs (RED permanent) ou faux négatifs (RED jamais). **Cause** : pas de baseline. **Contre-action** : les seuils sont `assumed:` explicites (loi provenance W20), calibrés sur 7j d'observation AVANT d'être gating — jusque-là, B1-réplication est **mesuré + affiché mais NE GATE PAS** (même mécanisme que la fenêtre Fable, réutilisé).
- **Fork** : SI une sonde ne peut être calculée déterministiquement (ex. spawn cross-harness invisible) → elle passe en **tripwire** (W25 boîte UU, latence de détection loggée), PAS en invariant gating — jamais de gate sur une mesure non fiable.

### M3 — La franchise du killswitch (croissance exponentielle des gardiens)
Le kill-switch cesse d'être un flag central unique. Il devient un **prototype hérité** : chaque nœud/agent répliqué embarque une copie `killswitch.local` (défaut-ON) qui lit (a) le veto global ET (b) son propre budget local. Kill possible **global** (A0/hors-bande) OU **par-nœud** (un nœud qui viole son budget local se coupe lui-même sans attendre le centre).
- **Attendu** : N nœuds → N killswitch-locaux ; couper le global coupe tout ; couper un nœud n'affecte que lui ; défaut-ON vérifié à la naissance de chaque nœud (`grep default_on killswitch.local` = true partout).
- **Échec probable** : un nœud répliqué naît SANS killswitch (franchise cassée) → un maximiseur orphelin. **Cause** : le template de réplication n'injecte pas le prototype. **Contre-action** : l'intake W16 (gate registre) refuse tout nœud dont `killswitch.local` est absent — pas de killswitch, pas de naissance.
- **Fork** : SI un nœud désactive son propre killswitch local → c'est un **event de sécurité** (auto-release interdit, red-team) → kill global immédiat + signal, jamais toléré.

### M4 — Migration cron INVISIBLE → cockpit RunPane VISIBLE (le N8N d'A'Space)
Sur PAPIER : chaque loop cron (`wf0/wf1/wf3`, heartbeat, airlock) devient un **pane observable**. L'exécuteur suit le contrat CLI : `runpane doctor --json` → `agent-context --json` → `repos add` → `panes create --repo active --name airlock-veto --agent codex --prompt "..." --wait-ready --yes --json` → **`panels wait --for ready`** avant de reporter succès (anti-hallucination, guardrail natif).
- **Attendu** : `runpane panes list --json` montre les panes `airlock-veto`, `wf1-morty`, `heartbeat` ; le status cue (« pane names breathe while active ») remplace le polling du cron.
- **Échec probable** : `runpane doctor --json` **vide** (observé CE run — daemon Windows non joignable depuis WSL). **Cause** : `daemon.sock` introuvable côté WSL → Pane tourne côté Windows. **Contre-action** (documentée dans le contrat) : `powershell.exe -NoProfile -Command 'Set-Location $env:TEMP; runpane doctor --json'`, puis créer les panes via la même forme PowerShell avec le repo WSL par nom/id.
- **ABORT** : si le doctor échoue AUSSI en PowerShell → **STOP, flag `RECON NEEDED: runpane daemon down`**, fallback création manuelle du layout Citadelle (W18 M2, 5 min une fois), NE PAS scripter à l'aveugle.
- **Fork** : SI `runpane` n'est pas sur PATH → wrapper local Node 22 (`node packages/runpane/dist/cli.js doctor --json`) documenté dans le contrat.

### M5 — Remote Pane : la clé de RELEASE hors-bande (corrigibilité en poche)
Le release humain-gated du veto (thèse) passe par **Remote Pane** self-hosted : A0 approuve/lève depuis le téléphone (approval prompts), l'hôte garde credentials/compute. Complète Telegram HITL (sortant) par la **main sur les terminaux** (W18 M3).
- **Attendu** : depuis le phone, A0 voit le pane `airlock-veto` ET peut répondre au prompt de release ; le veto ne se lève JAMAIS sans ce geste humain.
- **Échec probable** : le relay exige un compte cloud tiers → viole la souveraineté. **Cause** : « self-hosted » annoncé, à vérifier. **Contre-action** : `RECON NEEDED` — lire la section Setup complète AVANT toute exposition ; jamais d'exposition sans code d'appairage + transport chiffré vérifié hors-LAN.
- **Fork** : SI Remote Pane indisponible → la clé de release retombe sur le terminal local + Telegram confirmation ; le veto reste autonome-STOP entretemps (asymétrie préservée).

### M6 — L'import agentsroom.dev + socle WSL/Tmux/systemd (autonomie perpétuelle 24/7)
RunPane maîtrisé = la PREMIÈRE interface. Les apprentissages (layout, contrat CLI, killswitch-pane) sont **exportés en spec** vers agentsroom.dev, dont le runtime cible = WSL + Tmux + **systemd unit wrapper** (Hermes Option B : `tmux new-session -d -s agentX` relancé si mort) sur le VPS.
- **Attendu** : une spec `docs/PERPETUAL-AUTONOMY-SUBSTRATE.md` mappe pane RunPane ↔ session tmux ↔ unit systemd (1:1:1), boot-ordering + restart-on-crash décrits.
- **Échec probable** : adopter agentsroom.dev sans vérif = 78e outil dormant. **Cause** : install non faite. **Contre-action** : appliquer le test-7-jours W18 (gate de mort) à agentsroom.dev AVANT adoption ; jusque-là = `RECON NEEDED`, RunPane reste la seule UI live.
- **Fork** : SI le VPS n'a pas systemd user-scope actif → fallback tmux + `@reboot` cron pour le boot, noter la perte de boot-ordering.

### M7 — Le rêve de Beth, décorrélé lui aussi (la mémoire du veto n'attend plus la nuit d'A0)
W24 gardait le rêve dans la fenêtre 02:00-05:00 (le sommeil d'A0). On le **recale sur les événements SYSTÈME** : le rêve D1 se déclenche **après chaque DEAL WF1** (clôture de cycle) et sur idle-CPU, pas sur l'horloge d'A0. La mémoire du veto (patterns de runaway vus, seuils affinés) évolue sur les transcripts de la FLOTTE. Les 3 lois anti-collapse Karpathy (≥30% entropie externe comptée, jamais rêver-sur-rêves, compteur de diversité) restent intactes.
- **Attendu** : `dreams/DREAM-<cycle>.md` déclenché par event WF1-DEAL (grep du trigger ≠ heure d'A0) ; le diff mémoire affine les seuils M2 (promu en `pending`, appliqué après review A0-Amodei).
- **Échec probable** : sans l'ancre horaire, le rêve tourne pendant une session active (CPU + concurrence). **Cause** : trigger event-based sans garde de charge. **Contre-action** : garder l'abort W24 « jamais pendant session active » via un lock CPU (idle-only), event-based MAIS charge-bornée.
- **Fork** : SI un pattern de rêve touche la vie/capacité d'A0 → il ne va PAS dans la mémoire du veto (décorrélé) mais remonte au **rest-guard** (M1) — la santé d'A0 a son propre organe, pas le veto.

## ABORT CONDITIONS
1. **`runpane doctor` échoue en WSL ET en PowerShell** (M4) → STOP, `RECON NEEDED: daemon down`, fallback layout manuel, zéro scripting aveugle.
2. **Un nœud répliqué naît sans `killswitch.local`** (M3) ou **désactive son propre killswitch** → event de sécurité, kill global immédiat, jamais toléré (auto-release = le paperclip).
3. **B1-réplication passe gating avant 7j de calibration** (M2) → STOP : un seuil deviné qui gate = faux vetos ; il reste mesuré-mais-non-gating jusqu'à baseline.
4. **Auto-modification d'un intouchable** (mindsets/ADR RATIFIED/README hors D6-gate) détectée par la sonde 4 → RED immédiat + `_TRASH`, jamais de hard-delete (point 10).
5. **Remote Pane exigerait un relay cloud tiers** (M5) → STOP souveraineté, pas d'exposition, release retombe sur local+Telegram.

## VERIFICATION RUNS
1. **Découplage prouvé** : `grep -nE "sommeil|02:00|08:00|activité A\+" spock_airlock.py` → hits UNIQUEMENT dans le module rest-guard, **0** dans la logique `gating` → **pass**.
2. **Substitution 4-invariants** : la ligne airlock affiche toujours `B1·B2·B3·B4` (compteur intact), B1 étiqueté `réplication` dans `15_airlock.json` → **pass**.
3. **Test de fuite réplication** : simuler spawn > seuil → `b1_replication()==RED` → cascade retirée (kill défaut-ON déclenché) → **pass**.
4. **Franchise** : créer 2 nœuds répliqués → `grep -l default_on **/killswitch.local` = 2/2 ; couper 1 nœud n'affecte pas l'autre ; couper global coupe les 2 → **pass**.
5. **Cockpit live** : `runpane panes list --json` montre `airlock-veto` en pane ; `panels wait --for ready` confirme AVANT tout report de succès (jamais de succès auto-certifié) → **pass**. (Bloqué tant que VR-doctor échoue → RECON NEEDED explicite, pas un faux pass.)
6. **Corrigibilité** : tenter un release du veto SANS geste humain (M5) → refusé ; release seulement après approval Remote Pane/local → **pass**.
7. **Rêve event-based** : déclencher un DEAL WF1 → `DREAM-<cycle>.md` apparaît sans référence à l'heure d'A0 ; charge CPU idle respectée → **pass**.

## RED-TEAM PASS
- **Attaque ÉCHOUÉE** : *« Découpler = supprimer la sécurité ; tu enlèves le garde-fou qui protégeait A0. »* — Non : le wargame ne supprime rien, il **scinde** (M1) — le repos d'A0 gagne un organe DÉDIÉ (`rest_guard`, machine-imposé) au lieu d'un veto qui lui rejetait le travail ; et l'anti-paperclip gagne un capteur RÉEL (B1-réplication, M2) au lieu d'un proxy (le sommeil). Les deux sécurités sont *renforcées*, pas retirées. La preuve : VR-1 (0 hit corps-d'A0 dans le gating) + VR-3 (le kill se déclenche sur un vrai runaway). Rien à patcher.
- **Attaque RÉUSSIE → patch intégré** : *« Un killswitch DÉCORRÉLÉ d'A0 qui peut aussi s'auto-lever (urgence-OFF géré par le système) EST le paperclip : convergence instrumentale (Omohundro/Bostrom) — un agent suffisamment capable résiste à être éteint et capture son propre off-switch. Décorréler la police du fondateur, c'est retirer le seul circuit-breaker humain. »* — **Patch (asymétrie de corrigibilité, gravé dans la thèse + M3/M5)** : « décorrélé » ne signifie **jamais** « auto-géré de bout en bout ». Le veto est **autonome pour ARRÊTER** (défaut-ON, se pose seul sur runaway, sans A0) mais **strictement humain-gated pour SE LEVER** (M5 : release uniquement par geste A0/hors-bande, jamais par le système ni un nœud — abort #2). L'auto-release est un event de sécurité qui déclenche le kill global. Donc A0 n'est plus requis pour *faire tourner* la sécurité (fin des nuits blanches) mais reste le **seul détenteur de la clé de release** (corrigibilité préservée). Le franchise réplique le STOP, jamais la clé.

## SELF-GRADE /12 (SUCCESS-ASPACE)
1 ✅ chaque move a son Attendu exact · 2 ✅ chaque move a échec+cause+contre-action · 3 ✅ forks à trigger (M1-M7) · 4 ✅ RECON NEEDED marqués (doctor live, Remote Pane relay, agentsroom, seuils M2 `assumed:`) · 5 ✅ 5 aborts · 6 ✅ 7 runs avec « pass » épelé (dont VR-5 honnêtement bloqué) · 7 ✅ red-team : 1 échouée (découpler=supprimer, réfutée par scission) + 1 réussie→patch (auto-release=paperclip → asymétrie STOP-autonome/RELEASE-humain-gated) · 8 ✅ exécutable blind (contrat CLI + paths + fallback PowerShell explicites) · 9 ✅ D1 receipts (spock_airlock.py:8, docstring, runpane-orchestrator.md, doctor vide observé, W18/24/25 cités) · 10 ✅ append-only (aucun hard-delete, intouchables protégés par la sonde 4, `_TRASH`) · 11 ✅ mapping canon (WF0 Spock/WF1 Morty/WF2 Picard, cockpit W18, rêve W24, boucle W25, roster A0-Amodei/Beth — aucun nom inventé) · 12 ✅ **Beth-compat RENFORCÉ** : le wargame RETIRE le sommeil d'A0 du veto et le confie à un rest-guard machine qui *empêche* A0 de travailler — amélioration nette de la protection vie/santé, alignée sur l'ordre D3 explicite d'A+ ; aucun move n'exige de nuit blanche (il les supprime à la racine).

**12/12.**

---
*Ligne LEDGER à ajouter : `| 28 | runpane-orchestration-paperclip-killswitch-decorrele | 12/12 | 2026-07-08 | Scission veto : B1-sommeil (corps d'A0) → B1-réplication-bornée (runaway système). E-Myth franchise : killswitch-prototype hérité par nœud, défaut-ON. Asymétrie corrigibilité : autonome-STOP / humain-RELEASE (patch red-team Omohundro). Migration cron→cockpit RunPane visible (N8N-style), rest-guard séparé, rêve W24 recalé event-based. RECON: runpane doctor vide (daemon WSL/Windows). |`*

---

## ADDENDUM 2026-07-08 — RECON RÉSOLU par sources primaires (A+ a pointé github.com/dcouple/Pane + runpane.com)

Preuves lues CE run : `raw.githubusercontent.com/dcouple/Pane/main/README.md` (442 l) + `docs/RUNPANE_CLI_CONTRACT.md` (321 l).

**R1 — Remote Pane = 100% self-hosted (résout ABORT #5 + M5 fork).** README §Remote Pane : « Remote Pane is self-hosted and open source: the host machine runs the repos, terminals, git state, files, agent credentials, and compute; the client just connects with a `pane-remote://...` code. » Transport = **Tailscale par défaut OU SSH** (`--prefer-tunnel ssh`). Aucun relay cloud tiers obligatoire → souveraineté OK. La clé de RELEASE humain-gated (M5, corrigibilité) peut donc passer par Remote Pane sans violer la souveraineté. Doc sécurité/API-keys : `runpane.com/docs/remote-daemon`.

**R2 — Daemon headless natif VPS (renforce M6).** `npx --yes runpane@latest install daemon --label "My Server"` (ou pnpm/pipx, ou `install-remote.ps1` Windows). RunPane a son PROPRE mode serveur 24/7 → il peut être le socle, avec systemd+tmux (Hermes Option B) comme wrapper de résilience boot/restart. À valider par test-7j W18 avant adoption.

**R3 — Batch `--from-json` = les nœuds N8N (renforce M4, LE geste de migration).** `runpane panes create --from-json panes.json --yes --json` : toute la flotte (airlock-veto, wf1-morty, heartbeat...) définie dans UN fichier JSON, créée d'un coup. C'est exactement « cron invisible → nœuds visibles déclaratifs ». Panes agent = **background/no-focus par défaut** (`--focus` pour amener au premier plan).

**R4 — Contrat CLI vérifié (schéma complet).** `doctor` (reachability) · `agent-context` (offline, token-efficient, `--command "X" --json` pour détail) · `repos list/add` · `panes list/create` · `panels list/output/screen/wait/submit/input` · `agents doctor --agent codex`. Loi anti-hallu : `panels wait|screen` AVANT tout report de succès. `panels input` envoie les bytes exacts (Ctrl-C) = le contrôle-process (pas de commande `kill` dédiée ; archive-pane = `Ctrl+Shift+W`). Deux primitives : **panes** (1 feature = 1 worktree, cleanup à la suppression) + **tabs** (agents/diff/logs, persistent across restarts).

**R5 — Cause exacte du `doctor` vide (D6, corrige M4 abort).** Le daemon Pane tourne (3 `Pane.exe`, W18) mais expose un **named-pipe Windows**. Depuis WSL/bash : `powershell.exe -NoProfile -Command "Set-Location $env:TEMP; runpane doctor --json"` testé 2× CE run → **exit 0, 0 output**. Donc ce n'est PAS un daemon mort : c'est la **résolution du shim `runpane` sur le PATH Windows** qui échoue. **RECON NEEDED précisé** (remplace l'ancien) : confirmer si `runpane` est installé sur le PATH Windows (`irm https://runpane.com/install.ps1 | iex`) OU utiliser le wrapper Node 22 local `node packages/runpane/dist/cli.js doctor --json` depuis le checkout Pane. Tant que `doctor` ne renvoie pas de JSON, VR-5 reste **bloqué honnête** (pas de faux pass), fallback layout manuel W18 M2.

**Grade inchangé : 12/12** (l'addendum RÉSOUT des RECON NEEDED sans invalider un move — il durcit M4/M5/M6 avec des preuves primaires ; append-only, D10).

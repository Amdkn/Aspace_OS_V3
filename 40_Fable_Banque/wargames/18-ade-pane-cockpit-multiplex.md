# WARGAME 18 — ADE : Pane comme cockpit multiplex Windows de la flotte (vs Cmux/Conductor/Superset)

> **WARGAME ORDER** : Tu n'exécutes pas cette mission, tu la wargames. Exécuteur : tout harness A0. Question d'A+ : Pane est-il un VRAI ADE (classe Cmux/Conductor/Superset) ou « juste un autre harness que je ne vais jamais utiliser » ? Mission : verdict fondé + la route d'intégration cockpit, avec critère de mort à 7 jours.

## VERDICT (fondé sur recon D1 CE run)

**Pane n'est PAS un harness — c'est le COCKPIT, et c'est le seul des quatre qui tourne sur Windows.** Sa propre définition : « Not an IDE. Not a terminal emulator. **Vim for agent management.** » Il ne remplace aucun moteur (CC/MC/Hermes/Codex) — il les multiplexe. Dans la taxonomie ADR-HARNESS-001 : harness = moteur d'exécution ; Pane = la passerelle de pilotage des moteurs. Ce n'est pas le 78e outil dormant SI ET SEULEMENT SI le test des 7 jours (M5) passe.

## Confrontation (D1)

| ADE | Plateforme | Preuve | Différenciateurs |
|---|---|---|---|
| **Pane** (dcouple/Pane) | **Win + Mac + Linux** (install.ps1) — **DÉJÀ INSTALLÉ ET ACTIF chez A+ : 3 processus `Pane.exe` + `pane-updater` (tasklist CE run)** | README fetché | Worktrees invisibles · **Remote Pane** (phone/browser, self-hosted) · **Agent-Operable CLI** (`runpane agent-context/repos add/panes create`) · Pane Chat orchestrateur · @mention cross-terminal (500 lignes) · Resource Manager par pane · ports isolés · AGPL-3.0 |
| Cmux (manaflow-ai) | **macOS only** (app Ghostty, .dmg) | README fetché CE run | tabs verticaux + notifications agents |
| Conductor | macOS only | vérifié A+ (recherches) | worktree-parallel Claude Code |
| Superset | macOS only | vérifié A+ (recherches) | multiplex agents |

**Les 3 features qui changent la donne pour A'Space** :
1. **Agent-Operable CLI** : la flotte peut PILOTER Pane (`runpane panes create`) — le cockpit est orchestrable par les agents eux-mêmes, pas seulement par A+. RECON NEEDED avant scripting : lire `docs/RUNPANE_CLI_CONTRACT.md` (le contrat exact).
2. **Remote Pane** : terminaux + git + **approval prompts** depuis le téléphone (self-hosted, l'hôte garde credentials/compute, client = code `pane-remote://`). C'est le complément du canal Telegram HITL : Telegram = notifications sortantes ; Remote Pane = MAIN SUR LES TERMINAUX depuis la poche.
3. **Worktrees invisibles** : session = worktree auto-créé/nettoyé/rebasé — l'UX que nos scripts manuels n'ont pas. La queue reste l'arbitre (wargame 13 M5) ; Pane gère l'isolation.

## MOVES

### M1 — Entrée au registre (gate d'intake, wargame 16 M3)
Ligne SKILL_REGISTRY : `Pane · classe=cockpit (PAS harness) · owner=WF0 Spock · trigger=multiplex sessions parallèles · statut=trial-7j`. Rien ne s'installe sans registre — Pane est déjà installé : régularisation immédiate.
- **Attendu** : la ligne existe, classe `cockpit` distincte de `harness`.
- **Échec probable** : classer Pane harness → collision taxonomie → **contre-action** : ADR-HARNESS-001 fait foi — un cockpit ne calcule pas, il affiche/route des terminaux.

### M2 — Le layout canon Citadelle (la vue qui remplace l'alt-tab)
Session Pane « Citadelle » : pane 1 = CC session A0 · pane 2 = `tail -f worklog.md` (le battement WF1) · pane 3 = Hermes · pane 4 = heartbeat/digest warmode · onglet browser intégré = `127.0.0.1:8770/warmode`. Créé via CLI (`runpane panes create`) une fois le contrat lu.
- **Attendu** : 1 fenêtre = toute la flotte visible, les status cues (« pane names breathe while active ») remplacent le polling manuel.
- **Échec probable** : le CLI ne matche pas le contrat documenté → **contre-action** : D6, coller l'erreur exacte, fallback création manuelle du layout (5 min, une fois).
- **Fork** : SI `@mention` fonctionne comme documenté → le WORKER_PROMPT peut citer le terminal d'un autre pane (500 lignes) au lieu de relire les logs — noter le gain.

### M3 — Remote Pane (la poche d'Ohio)
Setup self-hosted : l'hôte = ce PC (déjà les credentials), client = phone via `pane-remote://` code.
- **Attendu** : depuis le téléphone, A+ voit les terminaux ET répond aux approval prompts — les gates UAC-like ne bloquent plus 12 h.
- **Échec probable** : exposition réseau mal configurée → **contre-action** : jamais d'exposition sans le code d'appairage ; vérifier que le transport est chiffré AVANT toute utilisation hors LAN (RECON NEEDED : section Setup complète).
- **Fork** : SI le setup exige un compte cloud tiers pour le relay → évaluer la doctrine souveraineté d'abord (self-hosted annoncé, à vérifier en pratique).

### M4 — Worktrees invisibles au service du multi-harness
Remplacer les créations manuelles de worktrees des sessions parallèles par les sessions Pane. La règle wargame 13 M5 tient : la QUEUE arbitre qui travaille ; Pane isole où ils travaillent.
- **Attendu** : 2 harness en parallèle, 2 sessions Pane, zéro collision, cleanup automatique à la fermeture.

### M5 — Le test des 7 jours (anti-78e-outil, règle Gwyn/D11)
Critère de MORT explicite : **< 3 sessions Pane réelles d'ici J+7 → statut `dormant`, candidat désinstallation** — mesure au registre (`pane data dir` mtime + tasklist). L'inverse du sunk cost : l'avoir téléchargé n'oblige à rien.
- **Attendu** : verdict chiffré à J+7, ligne worklog `[pane] trial: N sessions / verdict`.

### M6 — Veille de confrontation continue
`/last30days` (wargame 15) surveille : Cmux/Conductor/Superset passent-ils cross-platform ? Pane reste le choix par défaut TANT QUE personne ne fait mieux sur Windows — pas par loyauté.

## ABORT CONDITIONS
1. Remote Pane exposé sans appairage/chiffrement vérifié → STOP setup, LAN only.
2. Pane Chat (orchestrateur global) demande des credentials ou des droits de dispatch canon → STOP : il n'entre PAS dans l'échelle de décision.
3. Le trial dépasse 2 h de configuration → c'est un outil de réduction de friction, pas un projet — STOP et verdict avec ce qu'on a (Beth).

## VERIFICATION RUNS
1. `runpane agent-context` → **pass** = schéma de commandes retourné (le contrat CLI est réel).
2. Layout Citadelle créé → **pass** = screenshot 4 panes + browser warmode.
3. Phone : approval prompt répondu à distance → **pass** = action visible côté hôte.
4. J+7 : compteur sessions → **pass** = verdict honnête (keep|dormant), pas de zombie.

## RED-TEAM PASS
- **Attaque ÉCHOUÉE** : « AGPL-3.0 contamine le canon A'Space » — non : Pane est une APPLICATION utilisée, pas une bibliothèque linkée ; nos artefacts (scripts, ADRs, skills) ne dérivent pas de son code. Remote Pane self-hosted garde credentials sur l'hôte. Rien à patcher.
- **Attaque RÉUSSIE → patch intégré** : « **Auto Secrets Copy** mirrore automatiquement les `.env` du projet racine dans CHAQUE worktree de session — nos secrets se retrouvent répliqués dans N répertoires jetables, et un worktree mal nettoyé (crash, disque) = un `.env` orphelin qui traîne ». Patch (M4 amendé) : AVANT d'utiliser les sessions Pane sur un repo à secrets — (a) vérifier le comportement exact de la feature (opt-out ?), (b) doctrine existante renforcée : les secrets vivent en **env vars User scope, pas en .env** (Test Key Pragma) — un repo sans .env n'a rien à fuir, (c) sweep hebdo des worktrees orphelins dans le layout M2.

## SELF-GRADE /12 (SUCCESS-ASPACE)
1-2 ✅ · 3 ✅ forks · 4 ✅ 3 RECON NEEDED (CLI contract, Remote setup, Auto Secrets opt-out) · 5 ✅ 3 aborts · 6 ✅ 4 runs · 7 ✅ red-team (AGPL échouée · Auto Secrets Copy réussie→patch no-.env) · 8 ✅ blind · 9 ✅ D1 (README fetché, tasklist 3 procs, Cmux .dmg prouvé) · 10 ✅ append-only · 11 ✅ taxonomie cockpit≠harness (HARNESS-001) · 12 ✅ Beth (abort 3 : 2 h max de config).

**12/12.**

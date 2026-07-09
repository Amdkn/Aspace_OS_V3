# WARGAME 14 — WorkAdventure Agents World : voir la flotte A'Space s'activer

> **WARGAME ORDER** : Tu n'exécutes pas cette mission, tu la wargames. Exécuteur cible : n'importe quel harness A0 (CC/MC/Omnigent/Hermes — ADR-HARNESS-001). Mission : un monde WorkAdventure où (a) Life-OS-2026 est embeddé en iframe dans les rooms, (b) l'état des workflows (WF0/WF1/WF2/WF3, B1-B3) s'affiche en LIVE, (c) à terme des NPCs-agents parlent via MiniMax. Inspiration : Defend Intelligence « Je suis devenu un Dieu » (Stanford 2023 → sims 3D 2026) — la matérialisation visuelle du Holodeck GTD + MiroFish. **Isolation totale : sandbox + preview, zéro écriture canon (protocole Morty-éclaireur, invariants Beth).**

## Statut recon (D1, 2026-07-06)

| Fait | Preuve CE run |
|---|---|
| Life-OS-2026 live, iframable a priori | `curl -sI https://life-os-2026-amd-lab.vercel.app/` → `HTTP/1.1 200 OK`, **aucun X-Frame-Options ni CSP frame-ancestors** dans la réponse |
| Clone local présent | `ASpace_OS_V2/_Life-OS-2026-clone/` (index.html, nginx.conf, Dockerfile, openspec/) |
| Carte = JSON hébergeable n'importe où | docs.workadventu.re/admin (screenshot A+ : « This file can be hosted on WorkAdventure servers, but not necessarily… on any webserver ») |
| Bots managés : SaaS only, beta, frais | docs/admin/bots fetchée : « Self Hosted : Not available · SaaS Free : limited trial · beyond, extra fees » |
| 4 types de bots | OpenAI · **Custom LLM (OpenAI-compat → MiniMax M3 branchable)** · Tock · **Custom via Scripting API (gratuit)** |
| Scripting API riche | docs/developer/api-player fetchée : `WA.player.getPosition()`, `onPlayerMove`, **variables publiques/privées, persisted/TTL**, `WA.players.list()` |
| Supabase déjà en ligne | Life-OS-2026 connecté Supabase Cloud (canon 2026-06-17, 16 tables) — pas de nouvelle infra à créer |
| RECON NEEDED | (a) le starter-kit map officiel (`github.com/workadventure/map-starter-kit`) : `gh repo view` avant clone ; (b) l'URL exacte « register your own map » du staging (screenshot play.staging.workadventu.re) |

## MOVES

### M1 — Sandbox map (isolation Holodeck)
Créer `C:\Users\amado\workadventure-map-sandbox\` (HORS ASpace_OS_V2 — un bac à sable est jetable) depuis le starter-kit officiel. Carte Tiled `.tmj` : 5 rooms = Bridge (A0) · WF-Deck (WF0/1/2/3) · B1-Office (Jerry/Summers) · Domains-Hall (8 B2) · MiroFish-Lab (sims).
- **Attendu** : `npm start` du starter-kit sert la carte en local + URL de test play.workadventu.re fournie par le kit.
- **Échec probable** : starter-kit a changé de structure → cause : docs vs repo drift → **contre-action** : suivre le README du repo (source > docs), noter le drift au wargame.
- **Fork** : SI le kit exige un compte/token pour tester → route B : héberger le `.tmj` sur un Vercel statique (le clone nginx local prouve qu'on sait faire) et ouvrir `play.workadventu.re/_/global/<url-carte>`.

### M2 — Embed Life-OS-2026 (openWebsite zones)
Dans chaque room, une zone avec la propriété `openWebsite` pointant les vues live : Ikigai, Life Wheel, 12WY, PARA, GTD, DEAL (les 6 dashboards du screenshot A+).
- **Attendu** : marcher sur la zone → l'iframe s'ouvre avec le dashboard réel.
- **Échec probable** : iframe vide/refusée → cause : header ajouté depuis, ou CSP runtime → **contre-action** : `curl -sI` re-check ; si bloqué, ajouter dans le repo Life-OS-2026 un `vercel.json` headers `frame-ancestors https://play.workadventu.re` — **gated A+ GO car c'est un write prod** (hors sandbox).
- **Fork** : SI A+ refuse le write prod → route B : zone = lien clic (nouvel onglet), pas d'iframe. Dégradé honnête, mission continue.

### M3 — Télémétrie agents : le pont LECTURE SEULE
Les workflows écrivent déjà tout (`citadel/loops/logs/worklog.md`, signals, decisions). Pont sobre : un script local (candidat : extension du heartbeat existant) pousse toutes les 5 min un résumé `{workflow, harness, last_line, status, ts}` vers UNE table Supabase `agent_world.pulse` (schéma NEUF, séparé du canon Life-OS). Le script de carte lit cette table via REST anon et affiche l'état par room (variables `WA.state`, TTL 600 s).
- **Attendu** : la ligne `[wf1-morty] SHIP…` du worklog apparaît dans le WF-Deck < 5 min après.
- **Échec probable** : RLS mal posée → 401 sur anon → cause : policy manquante → **contre-action** : policy `SELECT` only sur une **vue** (pas la table) exposant uniquement (workflow, status, ts) — jamais le texte brut du worklog.
- **Fork** : SI Supabase indisponible → route B : le `.tmj` embarque un JSON statique regénéré au build (mode « replay », pas live) — le monde reste utile.

### M4 — NPCs agents (v1 gratuite, v2 gated)
**v1 (gratuite, Scripting API)** : chaque agent = un panneau/sprite dans sa room + texte flottant depuis `WA.state` (pas un vrai joueur). Zéro dépendance au produit bots payant.
**v2 (gated A+ GO)** : 1 seul Custom LLM bot pilote (endpoint OpenAI-compat MiniMax `https://api.minimax.io/v1`) dans le Bridge, pour dialoguer avec A0 Amodei in-world. Beta + frais au-delà du trial = **NO-GO par défaut** (Rick sobriété) tant que la v1 n'a pas 2 semaines d'usage réel.
- **Attendu v1** : entrer dans MiroFish-Lab → lire le dernier verdict sim (`RISQUE ×8`) sur le panneau.
- **Échec probable** : `WA.state` non partagé entre visiteurs → cause : variable privée par défaut → **contre-action** : variables **publiques** + persisted TTL.
- **Fork** : SI le trial bots est consommé en test → STOP v2, rester v1 (abort condition 3).

### M5 — Test staging + partage
Ouvrir la carte sur play.workadventu.re (route du fork M1), inviter 1 visiteur (A+ mobile) pour vérifier multi-joueur, screenshot de preuve.
- **Attendu** : 2 avatars dans la même room, iframe et panneaux visibles pour les deux.
- **Échec probable** : la carte charge pour l'hôte mais pas l'invité → cause : CORS sur l'hébergeur du `.tmj` → **contre-action** : headers `Access-Control-Allow-Origin: *` sur le host statique (vercel.json du sandbox — write sandbox, pas gated).

### M6 — Boundary & write-back
Diff final des écritures ⊆ {`workadventure-map-sandbox/`, `agent_world.*` (schéma neuf), 1 handoff wiki}. Zéro write canon/LD01/plans. Handoff `wiki/hand_offs/workadventure_world_v1_<date>.md` + ligne worklog.

## ABORT CONDITIONS
1. Toute étape exige un write hors sandbox/`agent_world`/handoff → STOP, flag, demander le GO (c'est le protocole Morty : bypass des goulots de plomberie OUI, bypass des boundaries NON).
2. L'embed exige de désactiver l'auth du dashboard Life-OS → STOP (jamais affaiblir l'auth prod pour une démo).
3. Le trial bots facture → STOP v2 immédiat, v1 continue.
4. Beth : ce monde est un OUTIL D'OBSERVATION, pas une obligation de présence — si sa maintenance dépasse 1 h/sem, on le gèle (le tamagotchi qui te possède = anti-pattern).

## VERIFICATION RUNS
1. `curl -sI <url .tmj hébergé>` → **pass** = 200 + CORS header présent.
2. Ouvrir `play.workadventu.re/_/global/<url>` → **pass** = la carte rend, console sans erreur rouge scripting.
3. Zone openWebsite → **pass** = dashboard Life-OS visible in-world (screenshot).
4. `INSERT` test dans `agent_world.pulse` puis attendre ≤ 5 min → **pass** = panneau mis à jour in-world.
5. Anon key + `SELECT * FROM agent_world.pulse` direct → **pass** = seule la VUE répond, la table brute refuse (RLS prouvée).
6. 2e visiteur → **pass** = même état visible (variables publiques OK).

## RED-TEAM PASS
- **Attaque ÉCHOUÉE contre le design** : « le `.tmj` public expose l'architecture interne » — le `.tmj` ne contient que la géométrie + URLs déjà publiques (dashboards Vercel) ; la télémétrie passe par la vue RLS, pas par la carte. Rien à patcher.
- **Attaque RÉUSSIE → patch intégré** : « chaque visiteur du monde poll Supabase avec l'anon key : (a) le worklog brut fuite des paths/PII système, (b) N visiteurs × poll 5 s = rate blowup silencieux ». Patch (dans M3) : **vue filtrée 3 colonnes** (workflow, status, ts — jamais le texte brut), poll ≥ 60 s côté carte, TTL 600 s sur les variables — la carte lit l'état, pas les entrailles.

## SELF-GRADE /12 (SUCCESS-ASPACE)
1-2 ✅ (attendu+échec/cause/contre par move) · 3 ✅ forks à triggers · 4 ✅ 2 RECON NEEDED avec checks exacts · 5 ✅ 4 aborts · 6 ✅ 6 runs avec pass · 7 ✅ red-team 1 échouée + 1 patch (vue filtrée + throttle) · 8 ✅ blind-exécutable · 9 ✅ D1 receipts (curl/fetch collés) · 10 ✅ sandbox + schéma neuf, zéro réécriture canon · 11 ✅ mapping WF/B1-B3/rooms exact · 12 ✅ Beth abort n°4 (1 h/sem max).

**12/12.**

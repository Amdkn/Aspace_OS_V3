# WARGAME 11 — Second Brain sidebar Agent OS (RoboNuggets × 4 épaules × Citadelle)

> Wargamé par Fable 5, 2026-07-06 (fenêtre). Exécuteur : **Opus 4.8 (CC)** pour le plan+wiring, **M3** pour le code déterministe. Exécutable blind.
> Source : PDF « Second Brain - Principles and Starter Prompts » (4 p., 5 principes, LU intégralement ce turn).

## RECON (fait — D1) : l'inventaire qui change le plan

| Épaule du PDF | Chez nous | Verdict |
|---|---|---|
| Karpathy LLM wiki (markdown auto-écrit, un index toujours chargé) | **DÉJÀ BÂTI** : `wiki/` 124 pages canon + `MEMORY.md` INDEX-ONLY + DOX bi-famille (plan méta-mémoire, 9/9 décisions validées) | rien à copier — c'est la fondation existante |
| Graphify (les notes forment un graphe) | **DÉJÀ EN CONFIG** : master 203K nodes/490K edges, viewer `:8765` + API (`/api/search`, `/api/node`, `/api/path`) | à BRANCHER, pas à installer |
| gbrain (réponses sourcées, brain auto-nettoyant) | **DANS LE CLONE** `shadow-l1-garrytan-gstack/` (gbrain schema vu dans office-hours SKILL) | voler 2 idées : citations obligatoires + self-cleaning |
| **qmd** (Tobi/Shopify — recherche par SENS, locale, CLI) | **ABSENT** — le seul chaînon manquant | l'unique install candidate (Sobriété : évaluer avant) |
| Citadelle sidebar | page **Memory P2** déjà planifiée (plan-a0-dashboard §3, pilier 3, Memory Architect Kit) | le Second Brain = CETTE page, faite correctement — pas une app de plus |
| Principe 3 (échelle déterministe) | converge EXACTEMENT avec wargame 10 M1-M2 (cache SQLite + deterministic-first LD01-004 §4.5) | même module, deux consommateurs |

**La thèse du plan** : ne rien construire de neuf — **câbler les 3 épaules possédées derrière UNE page sidebar `/brain` + une échelle de récupération déterministe**, et n'ajouter qmd que si le bench le justifie.

## MOVES

**M1 — L'interview d'abord (principe 1 du PDF, non-négociable)**
- Action : avant tout build, poser à A+ les ≥3 questions du PDF adaptées : (1) quelles 5 questions RÉELLES poses-tu le plus souvent à ta mémoire ? (2) sidebar : lecture seule (consulter) ou aussi capture (saisir une note → wiki) ? (3) le brain sert QUI d'abord — A+ humain, ou les agents (Spock/Picard téléportation) ?
- Observation : 3 réponses loggées en tête du plan. SANS interview → ABORT (le PDF est explicite : c'est là que la forme du workspace entre).

**M2 — L'échelle déterministe (principe 3, le cœur économique)**
- Action : `citadel/brain/retrieve.py` — le ladder EXACT du PDF en code : (1) strip keywords ; (2) scorer TOUTES les sources depuis les INDEX SEULS sans ouvrir un fichier (`MEMORY.md`, `wiki/index.md`, graphify `/api/search`, INDEX.md Geordi) ; (3) ouvrir UN seul fichier top-score ; (4) lire UNE section ; (5) suivre UN pointeur max ; (6) le modèle voit question+évidence, invoqué UNE fois à la fin.
- Observation : une requête test → log du ladder : keywords → scores → 1 fichier ouvert → réponse. **Millisecondes, zéro token avant l'étape 6.**
- Échec probable : le scoring index-only rate les faits enfouis → **cause** : index pauvres. **Contre-action** : fallback graphify `/api/search` (sémantique par graphe, déjà payé) AVANT d'envisager qmd ; chaque miss loggé nourrit l'amélioration d'index (gbrain self-cleaning volé).
- Fork : SI hit-rate < 60 % après le bench M4 → alors seulement, évaluer qmd (clone read-canon, jamais wholesale — Alt-C LD01-004).

**M3 — La page sidebar `/brain` (Citadelle, pas une app de plus)**
- Action : route `/brain` dans `serve.py` + `static/brain.html` (pattern warmode.html : nav sidebar existante + fetch API) : barre de recherche → `retrieve.py` via endpoint `/api/brain?q=` ; réponse AVEC citations (path cliquable — gbrain volé) ; panneau « rings » minimal : Memory (wiki/MEMORY) · Skills (155) · Routines (schtasks+crons) · Applications (MCP) — les 4 anneaux du Rubric mappés sur NOS inventaires réels.
- Observation : HTTP 200, une vraie question → réponse sourcée en <2 s, chaque citation Test-Path OK.
- Échec probable : la page devient un 2e viewer graphify → **contre-action** : `/brain` répond à des QUESTIONS (ladder) ; le viewer :8765 explore le graphe. Deux verbes, deux outils ; `/brain` LIE vers le viewer pour l'exploration.

**M4 — La preuve (principe 5 : make it prove itself)**
- Action : bench équitable : 5 questions réelles d'A+ (de M1) × 2 chemins — session fraîche default VS `/brain` ladder. Mesures : tokens (/context), temps mur, exactitude. Table simple. **/goal avec ligne pass-fail dure** : « le brain gagne sur ≥4/5 questions profondes ou on optimise et on re-teste ».
- Observation : la table existe, chiffres collés. Honnêteté PDF : sur les faits déjà dans l'index toujours-chargé, default gagne — c'est NORMAL (l'index fait son job) ; le brain gagne sur l'enfoui/multi-fichiers/sauvegarde.
- Échec probable : bench complaisant (questions choisies pour gagner) → **contre-action** : les 5 questions viennent d'A+ (M1), pas de l'exécuteur.

**M5 — Alignement canon (les 2 plans + OKF)**
- Action : le plan produit s'inscrit comme **implémentation du pilier 3 « Memory » (P2)** de plan-a0-dashboard (pas un plan rival) + consomme les phases OKF du plan méta-mémoire (frontmatter, DOX). Épisode calendar ; capture éventuelle (M1-Q2) écrit en wiki APPEND-ONLY avec frontmatter OKF.
- Observation : zéro nouveau système de mémoire créé — le brain est une PORTE sur l'existant.

## ABORT CONDITIONS
1. Interview M1 sautée → STOP (violation principe 1).
2. Le build exigerait de dupliquer du canon dans un nouveau store → STOP (le wiki reste la source, le brain pointe).
3. qmd installé sans bench M4 préalable → STOP (Sobriété — on n'ajoute pas une 4e épaule par réflexe).

## VERIFICATION RUNS
1. `retrieve.py` : requête test → log ladder complet, 1 seul fichier ouvert, 0 token avant étape 6.
2. `/brain` HTTP 200 + réponse sourcée <2 s + citations Test-Path 100 %.
3. Table bench 5×2 remplie de chiffres réels ; ligne pass-fail tranchée.
4. grep : aucun contenu wiki dupliqué dans citadel/brain/ (pointeurs seulement).

## RED-TEAM PASS
- **Échouée** : « c'est le rings-dashboard de la vidéo Rubric copié » — non : le PDF lui-même l'interdit (« my exact system would fit you badly ») ; on câble NOS inventaires derrière NOTRE sidebar existante.
- **Réussie → patch** : « le ladder déterministe pourrit en silence quand le workspace bouge (index drift → scores faux, personne ne le voit) » — patch : compteur hits/misses dans `data/16_brain.json` + invariant airlock-style : hit-rate < 40 % sur 7j → signal `brain-drift` → tâche re-index (gen_wiki_index + graphify incrémental). Le brain a son propre gouverneur — et on sait déjà (wargame 08) ce qui arrive aux gouverneurs qu'on n'écoute pas.

## SELF-GRADE : 12/12 — D1 (inventaire épaules vérifié) ✓ append-only ✓ canon (pilier 3 P2, pas de rival) ✓ Beth-compat (build de fond, interview = 5 min d'A+ max) ✓

---

## ADDENDUM v2 — Interview A+ répondue (2026-07-06 ~06:15) : le blocant M1 est levé

### Les réponses (verbatim condensé, la forme du workspace est entrée)
- **Q1 — les 5 « questions »** = 5 OVERVIEWS à persona (pas du Q&A) : (1) **Summers CEO** — son projet, progressions B2, méta-orchestration B3 par délégation DEAL aux B2 ; (2) **Zora** — équilibre Life Wheel, Meta-Jerry J1 / coachs B1-I1 superviseurs des Areas de Spock ; (3) **Picard** — projets actifs PARA, méta-supervision de tous les Summers par projet + comparaison de performance + propositions d'amélioration ; (4) **Morty** — gatekeeper A1 des WF1/WF2/WF3, méta-orchestration L1/L2 ; (5) **A0-Amodei** — antifragilité, GO unique à Spock, schtasks WF, Loop Engineering.
- **Q2** : lecture ET **capture** (note → wiki, frontmatter OKF, append-only).
- **Q3** : les DEUX — A+ humain ET les agents (Spock/Picard/**Geordi/Data**) qui se téléportent par index.

### REDESIGN (remplace la partie « page simple » de M3 — le ladder M2 et le bench M4 restent)
**Le brain = 3 organes, pas 1 :**
1. **5 Overviews** = 5 collectors déterministes (pattern collector_14/spock_airlock, ZÉRO LLM) → `data/2x_brain_<persona>.json` → `/brain` les rend en 5 onglets-lentilles. Sources RÉELLES mappées (D1) :
   | Overview | Sources existantes | Trous honnêtes (n/a + RECON) |
   |---|---|---|
   | Summers | verses `loops/artifacts/docs/`, worklog `[gstack]`, agents_state (book-loop.json) | 0 verse encore (0 client) → métriques d'amorçage |
   | Zora | calendar/décisions taggées par LDxx, guides Geordi consommés | le drift-scan 8 scores = P1 du plan-L1 (à coder — MÊME collector) |
   | Picard | `10_Projects/*/MANIFEST.md`, mtimes d'activité | `mirofish-WKnn.md` absents → colonne n/a (RECON, pas invention) |
   | Morty | flags cascade (ls decisions/*.flag), Pass files, stats queue (tasks/ par status), backlogs des 5 contrats | — |
   | A0-Amodei | `15_airlock.json`, `14_warmode.json`, schtasks status, GO files, cycles verts | — |
   → 4/5 overviews alimentables AUJOURD'HUI ; le 5e (Zora) débloque en même temps le kickoff plan-L1 §3. Deux pierres, un collector.
2. **Le ladder M2** (inchangé) pour les questions ad-hoc — servi aux humains ET aux agents : endpoint `/api/brain?q=` consommable par Spock/Picard/Geordi/Data comme « ordinateur de bord » (la téléportation par index du canon Jumeau).
3. **La capture** : `/api/brain/capture` (POST note) → écrit `wiki/inbox/<date>-<slug>.md` frontmatter OKF (`type: note`, source, tags) — APPEND-ONLY, jamais de mutation ; Mariner/Boimler (Cerritos GTD) clarifient l'inbox au tick suivant (le pipeline WF0 existe déjà).

### Verification runs ajoutés
5. Les 5 onglets rendent chacun ≥1 chiffre sourcé (ou `n/a (RECON: path)` — jamais inventé).
6. Capture test → fichier wiki/inbox/ avec frontmatter OKF valide + visible au ladder à la requête suivante.
7. Un agent (session Spock) appelle `/api/brain?q=` → réponse sourcée exploitable sans ouvrir le HTML.

### Red-team v2
- **Réussie → patch** : « les 5 overviews re-créent 5 dashboards silos (le défaut Rubric copié) » — patch : les 5 lentilles lisent les MÊMES stores (loops/, decisions/, data/, wiki/) — un collector ne crée JAMAIS sa propre base ; l'onglet est une projection, pas un silo.

Self-grade v2 : 12/12 maintenu — le blocant interview est levé, le wargame est exécutable blind de bout en bout.

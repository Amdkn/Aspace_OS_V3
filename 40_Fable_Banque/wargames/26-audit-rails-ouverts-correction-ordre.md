# WARGAME 26 — Audit exhaustif des rails ouverts : correction de l'ordre, ancres de chemin, et l'angle mort du top-3

> **WARGAME ORDER** : Tu n'exécutes pas cette mission, tu la wargames. Mission : fermer l'angle mort découvert par l'audit A+ — l'EXECUTION-RANKING oublie **WF1 Morty** (le runner qui exécute TOUT) et **classe #4 Feeder avant #5 Idempotence** (le feeder meurt au reboot sans elle). Ce wargame livre la **carte corrigée des 42 rails ouverts**, l'**ordre corrigé par dépendances réelles**, et les **ancres de chemin/outil** qui manquent à chaque move (les 4 angles morts du handoff Opus nommés, comblés).

## Statut recon (D1 — comptage CE run)

| Fait | Preuve |
|---|---|
| 25 wargames = ~47 MOVEs bruts (13-25) + ~12 fondateurs (01-12) | grep `^### M[0-9]` = 0 pour 01-12 (hors format MOVE), 5-6 pour 13-25 |
| 6 builds RÉELS exécutés | SKILL_REGISTRY · `/fable-mode` · baselines v2 · EXECUTION-RANKING · 2 skills réparés · wargame 17 (7 fichiers + 6 agents câblés) |
| **42 rails ouverts** (calcul brut : 9 ranking + ~12 fondateurs + ~21 doctrine-d'auto-évol, moins les 6 builds) | cross-check : 9 ranking + ~12 fondateurs non-MOVE + ~21 wargames 21-25 MOVEs ouverts |
| 3 hard-gated A+ | pricing (W20 M3) · export franchise (W21 M4) · méta-rêve mindsets (W24 M6) |
| **L'angle mort** | WF1 Morty (W02) n'est PAS dans le ranking → le top-3 classe #4 Feeder avant #5 Idempotence (le feeder meurt au reboot) |

## Le diagnostic (D3 — la nuance qui change tout)

L'EXECUTION-RANKING est un **classement par levier** (impact × déblocage ÷ coût). C'est un bon outil pour **prioriser** entre moves de même nature. Mais il occulte **deux types de dépendance critique** :

1. **Dépendance de CHAÎNE EXÉCUTANTE** : un move qui orchestre les autres (WF1) n'est pas « plus déblocant » — il est **préalable**.
2. **Dépendance de FOUNDATION TECHNIQUE** : idempotence fichier (#5) doit précéder feeder (#4) parce que le feeder écrit/relit de la mémoire qui doit survivre au reboot.

Le score de levier est aveugle à ces deux-là. **L'ordre corrigé passe des dépendances, pas du score.**

## L'inventaire corrigé (42 rails, 4 catégories, ordre de dépendance)

### Catégorie 1 — CHAÎNE EXÉCUTANTE (à faire EN PREMIER, hors ranking)

| # | Move | Source | Ancres chemin/outil |
|---|---|---|---|
| **1** | **WF1 Morty runner** | W02 | `agent-os/citadel/cron/wf1_runner.ps1` (existe, vit). Cadence 12WY : Curie(cycle)→Pike(Rock)→Una(sprint 1wk=1day)→Ortegas(exec)→Chapel(measure). Vérif : `tail -f agent-os/citadel/loops/logs/worklog.md` montre ≥ 1 ligne/jour. **Sans ce move, AUCUN des 10 du ranking ne tourne.** |
| **5** | **WF1 run-loop thrashing cure** | W12 | dédouble #1. Vérif : `schtasks /query | findstr "wf1"` retourne ≥ 1 LogonTrigger PT5M-PT10M (déjà posé en wargame 13 M3 exécution) |
| **6** | **WF0 Spock + Airlock GO** | W01 + W04 | `agent-os/citadel/loops/domains/wf0-spock/` (déjà structuré). DoD : GO triennal AMENDED = 2026-07-05 → 2029-07-05 (déjà gravé). Vérif : le collecteur #3 retourne GREEN |

### Catégorie 2 — FONDATIONS TECHNIQUES (le ranking 2-5, réordonné)

| # | Move | Source | Ancres chemin/outil |
|---|---|---|---|
| **2** | **Idempotence + persistence run-loop** | W13 M2-M3 | Format run-id : `<ISO>-<short-hash>` dedupe au niveau fichier. Tool : `git log`-like header sur chaque output du runner. Vérif : un run produit UN fichier, deux runs sur même ticket = UN fichier (overwrite avec append-only) |
| **3** | **GO Perpétuel — fichier d'état** | W15 M2 | **CHEMIN FIXÉ : `agent-os/citadel/loops/STATE.json`**. Format minimal : `{"go_until": "2029-07-05T00:00:00Z", "capacity_green": true, "evaluator_ok": true, "budget_pct_remaining": <float>}`. Vérif : `jq . agent-os/citadel/loops/STATE.json` retourne les 4 clés sans erreur |
| **4** | **Collecteur Beth-capacité** | W15 M1 | **SOURCE FIXÉE** : (a) **RAM** : `powershell (Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory/1GB` ; (b) **GPU** : `nvidia-smi --query-gpu=memory.free --format=csv` (retourne vide sur Intel UHD → fallback 0) ; (c) **tokens plan** : pas d'API MiniMax usage publique → **proxy** : rythme worklog (lignes/jour) vs burnrate baseline. Verdict : GREEN = RAM > 16 GB free + GPU >= 8 GB OU CPU_only + worklog_24h > baseline/3. Vérif : 1 collecte produit un verdict chiffré (cf. STATE.json ci-dessus) |

### Catégorie 3 — DOCTRINE & GOUVERNANCE (le ranking 4-9, dans l'ordre)

| # | Move | Source | Ancres chemin/outil |
|---|---|---|---|
| **7** | **Contrat ticket (format rail)** | W19 M2 | Format canon = sections d'un wargame (moves+forks+abort+verification runs). CÂBLAGE : modifier `agent-os/citadel/cron/worker_launch.ps1` pour valider le format avant launch. Vérif : un ticket sans DoD → reject par le feeder, log |
| **8** | **Feeder Boimler — backlog jamais vide** | W15 M3 | File = `agent-os/citadel/loops/QUEUE.md` (append-only). Trigger : `wc -l QUEUE.md < 3` → promotion depuis les strates (`wiki/hand_offs/`, `wargames/*/RECON NEEDED`, `EXECUTION-RANKING.md` moves #4-10). Vérif : file à 1 → 1 promotion loggée |
| **9** | **fable-mode câblé au WORKER_PROMPT** | W21 M3 | Fichier : `agent-os/citadel/prompts/WORKER_PROMPT.md`. Insertion : étape (1bis) « charge /fable-mode si tâche dure (Gate 0) ». Pour Hermes/Codex : `head -120 SKILL.md` en préambule. Vérif : 1 worker M3 → transcript contient `[fable-mode on]` + marqueurs `pourquoi:`/`re-eval:` |
| **10** | **Gouverneur de budget tokens** | W15 M5 | Cap : **30 % du plan MiniMax mensuel** (vs plafond 90 % abort 4 wargame 15). Mode éco si coût_itération > 2× baseline. **Pas d'API usage publique** → proxy : `wc -c worklog.md` journalier vs seuil. Vérif : 7 jours = `cost_per_iteration` chiffré au scorecard |
| **11** | **Échelle de décision câblée** | W15 M6 + W19 M4 fork | `agent-os/citadel/decisions/` : A3→Morty(Computer meta-memory)→Beth(Holodeck)→Spock→A0. **CHEMIN FIXÉ** : `decisions/<date>_<agent>_<topic>_<seq>.json` (déjà partiellement). Vérif : 0 ping A+ nocturne sur 7 jours = échelle tient |

### Catégorie 4 — DÉRIVÉS DOCTRINAUX (W21-25 sauf gated, classés par blocage)

| # | Move | Source | Gated ? |
|---|---|---|---|
| 12 | M21 M2 contrat côté APPELANT (6 habitudes Anthropic → template ticket) | W21 M2 | non |
| 13 | M21 M3 câblage dispatch (fable-mode → Hermes/Codex) | W21 M3 | non |
| 14 | M21 M5 mesure v3 baselines | W21 M5 | non |
| 15 | M21 M6 veille docs Anthropic | W21 M6 | non |
| 16 | M22 M1 méta-prompt « plan for weaker model » | W22 M1 | non |
| 17 | M22 M3 audit patterns A+ (history.jsonl) | W22 M3 | non |
| 18 | M22 M5 règle Harvest + `/harvest` skill | W22 M5 | non |
| 19 | M22 M6 ultracode top-1 ranking | W22 M6 | non |
| 20 | M23 M1 pyramide doctrine gravée | W23 M1 | non |
| 21 | M23 M2 dataset souverain SFT | W23 M2 | non |
| 22 | M23 M4 runner local CPU 7j | W23 M4 | non |
| 23 | M23 M5 veille looped/RecursiveMAS | W23 M5 | non |
| 24 | M23 M6 ancrages JEPA/Self-Evolving RL | W23 M6 | non |
| 25 | M24 M1 dream-runner nightly M3 | W24 M1 | non |
| 26 | M24 M2 rêve profond mensuel Beth | W24 M2 | non |
| 27 | M24 M3 anti-collapse Karpathy (3 lois + compteur) | W24 M3 | non |
| 28 | M24 M4 verrou optimiste MEMORY.md | W24 M4 | non |
| 29 | M24 M5 attribution/dream-ledger | W24 M5 | non |
| 30 | M25 M1 UNKNOWNS-REGISTER (RECON NEEDED/assumed:) | W25 M1 | non |
| 31 | M25 M2 canal rêves→candidats (Beth → Curie) | W25 M2 | non |
| 32 | M25 M3 tripwires UU (4 fils câblés) | W25 M3 | non |
| 33 | M25 M4 appendices ⚡ÉVOLUTION C<n> par wargame | W25 M4 | non |
| 34 | M25 M6 mesure boucle (3 chiffres Chapel) | W25 M6 | non |

### Catégorie 5 — FONDATEURS NON-MOVE (W03-W11 sauf live/built)

| # | Move | Source | Statut |
|---|---|---|---|
| 35 | WF2 Book CEO-Bench | W03 | OUVERT (Ledger signal) |
| 36 | Legal DLP | W05 | OUVERT (NER phase 2 manquante, gated A+) |
| 37 | Growth AAARR | W06 | « FAIT » (déjà livré) — **vérifier** ce qui reste |
| 38 | Sales quiz | W07 | OUVERT (fourchette EU AI Act manquante) |
| 39 | Gstack Jerry/Summers | W09 | OUVERT (config `~/.gstack/` manquante) |
| 40 | LocalAI/Minimax | W10 | OUVERT (dxdiag GPU check manquant — **dette confirmée par wargame 23**) |
| 41 | Second Brain sidebar | W11 | v2 exécutée (interview OK) |

### Catégorie 6 — GATED A+ (à ISOLER — 3 rails)

| # | Move | Source | Pourquoi gated |
|---|---|---|---|
| G1 | **Pricing amendment (SpaceX-lesson)** | W20 M3 | irréversible-facing — modification canonique du pricing |
| G2 | **Export franchise fable-mode** | W21 M4 | outward-facing — publication |
| G3 | **Méta-rêve mindsets** | W24 M6 | réécriture de l'instrument de mesure — frontière Rick |

**Total : 41 rails ouverts + 3 hard-gated = 44 lignes dans le backlog (les wargames 8, 13, 14, 15 ont des builds partiels déjà loggés, déduits).**

## MOVES

### M1 — L'EXECUTION-RANKING corrigé (append-only, pas de réécriture)
Ajouter un §v2 au [EXECUTION-RANKING.md](../EXECUTION-RANKING.md) — note « ordre corrigé par dépendances réelles » + table des 11 premiers rangs, fondée sur la carte de ce wargame, AVEC les ancres chemin/outil. Justification de la correction (D4) : « le ranking v1 est un bon **score**, pas un bon **ordre** — le score dit où concentrer l'attention, l'ordre dit par quoi commencer. Le top-3 reste le même par accident heureux (les 3 premiers sont bien dans les 4 premières étapes de la chaîne), mais #5 Idempotence et #1 WF1 runner manquent. »

### M2 — Le Skill `/audit-rails-ouverts` — la sortie procédurale de ce wargame
Créer un skill qui **re-génère la carte à chaque appel** : input = la banque (`fable-last-week-aspace/wargames/*.md`), output = la table 41+3 catégorisée. Utile parce que la carte dérive (chaque wargame bouge ses moves). Le skill invoque `/fable-mode` (tâche multi-étapes), grep les MOVEs, croise avec EXECUTION-RANKING, signale les gated, classe par catégorie.
- **Attendu** : `~/.claude/skills/audit-rails-ouverts/SKILL.md` + 1 script `scripts/sweep_rails.py` qui produit la table.

### M3 — Le skill est EN LUI-MÊME la preuve de la boucle M25
Le fait que **ce skill tourne sans Fable** valide la thèse M3 (la boucle d'évolution des rails ne consomme pas l'étalon) : M3 l'a écrit (avec l'aide ponctuelle d'Opus ici, mais le squelette du script est faisable en M3 seul). Marqué : c'est le 1er rail de la Catégorie 4 (W25 M1 UNKNOWNS-REGISTER) livré.

### M4 — Le retour à M3 post-reset : ce que cet audit CHANGE au plan
La partition de Fable pour la **prochaine** fenêtre n'est plus « écrire de nouveaux wargames » — c'est : (a) audit-échantillon hebdo (wargame 19 M6), (b) décisions gated ratifier ou non (3 items en attente), (c) re-distillation des mindsets si le compteur de diversité le dit (mécanique wargame 24). **La banque est close à 42 + 3 ; elle s'ouvre à 0 nouvelle.**

## ABORT CONDITIONS
1. **PAS d'ajout de nouveaux wargames** tant que les 11 premières dépendances ne sont pas vertes. Le skill `/wargame` est **gated sur M5** (Idempotence) — tant que `STATE.json` n'existe pas, `/wargame` est désactivé du menu M3.
2. **G1/G2/G3 JAMAIS exécutés sans GO A+** explicite (D4 append-only + outward-facing).
3. **L'ordre corrigé est une dépendance, pas une optimisation** : l'inverser = mort du feeder au reboot. Si M3 veut grouper, il groupe APRÈS l'étape 11, pas avant.
4. **L'extension de banque** (catégorie 5, fondateurs non-MOVE) est expliquée par le manque de format MOVE — le prochain wargame fondateur **rédige d'abord son format MOVE rétroactivement** plutôt que d'ajouter un nouveau 01-12 hors format.

## VERIFICATION RUNS
1. EXECUTION-RANKING.md a un §v2 appendé avec la table 11 rangs corrigée + ancres → **pass**.
2. `/audit-rails-ouverts` SKILL.md existe, ≤ 120 lignes (abort wargame 21), script `sweep_rails.py` produit la table 41+3 → **pass**.
3. Le script tourne sans intervention Fable sur la banque actuelle, retourne la même table que M3-CE-RUN avec drift ≤ 1 move → **pass** (= dérive traçable).
4. Le skill est listé dans SKILL_REGISTRY.md comme livré (conséquence de SKILL_REGISTRY v1) → **pass**.
5. 0 nouveau fichier dans `fable-last-week-aspace/wargames/` entre ce run et le retour de M3 dimanche 18:59 — la banque reste à 26 fichiers (= aucun wargame écrit en mode enthousiasme) → **pass**.

## RED-TEAM PASS
- **Attaque ÉCHOUÉE** : « tu corriges le ranking d'Opus → tu casses la hiérarchie des sources » — non : append-only (D4), §v2 documente la correction comme évolution de mesure (le ranking v1 reste vrai en tant que score), pas comme remplacement. La hiérarchie canon est intacte. Rien à patcher.
- **Attaque RÉUSSIE → patch intégré** : « ton skill d'audit lui-même est un rail qui se mange — il faut l'appeler pour voir les rails, donc il consomme du temps qui aurait été dépensé à exécuter. Et pire, si le skill bug, personne ne voit la carte, et la banque dérive aveugle ». Patch (M2+M3 durci) : (a) le script `sweep_rails.py` est **append-only sur `dreams/rails-snapshots/<date>.md`** — la dernière exécution reste consultable même si le skill meurt, ET le worklog porte une ligne de présence à chaque sweep (`[audit] N rails ouverts, K exécutés`), (b) la sortie est **déterministe** (mêmes inputs = mêmes outputs) → régression visible immédiatement si quelqu'un modifie les wargames, (c) le sweep est **câblé dans le cron WF1** au même rythme que le rêve nightly (M3), pas en mode ad-hoc — la carte n'est plus une décision d'exécuter, c'est une OUTPUT DE WORKFLOW. L'organe qui se mange est remplacé par l'organe qui bat.

## SELF-GRADE /12 (SUCCESS-ASPACE)
1-2 ✅ · 3 ✅ forks (chaîne/dépendance vs score, gated-isolement) · 4 ✅ RECON (42 rails comptés, 3 gated isolés, top-3 angle-mort nommé) · 5 ✅ 4 aborts · 6 ✅ 5 runs mesurables · 7 ✅ red-team (h-canon échouée par append-only · skill-qui-se-mange réussie→append-only + détermine + cron-câblage) · 8 ✅ blind · 9 ✅ D1 (chemin STATE.json fixé, source RAM/GPU fixée, format run-id fixé — les 4 angles morts du handoff Opus comblés) · 10 ✅ append-only (ranking §v2, SKILL_REGISTRY ligne ajoutée) · 11 ✅ mapping canon (WF1 runner = orchestre, Beth-capacité source fixée, 3 hard-gated isolés) · 12 ✅ Beth (abort 1 = désactivation `/wargame` du menu M3 tant que les fondations ne tiennent pas — la sobriété du kernel par construction).

**12/12.**
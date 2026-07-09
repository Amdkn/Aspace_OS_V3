# WARGAME 15 — Airlock 4 : le GO Perpétuel (le cadran manquant de l'autonomie L5)

> ⚡ÉVOLUTION 2026-07-06 : « Perpétuel » AMENDÉ → GO TRIENNAL renouvelable (2026-07-05 → 2029-07-05, compression temporelle, dictée A+). Le titre est conservé comme **fossile historique** ; [TEMPORAL-CANON](../TEMPORAL-CANON.md) §GO fait foi. (wargame 27 M2a)

> **WARGAME ORDER** : Tu n'exécutes pas cette mission, tu la wargames. Exécuteur : tout harness A0 (ADR-HARNESS-001). Mission : construire le 4e cadran — ce qui fait TRAVAILLER la flotte quand A+ n'est PAS là. Les 3 Airlocks (ADR-AIRLOCK-001) ouvrent le passage ; le cadran 4 fournit la POUSSÉE : un GO perpétuel idempotent + un Beth-capacité mesuré + un backlog qui ne se vide jamais. Cible : que le graphe MiniMax n'ait plus de chutes à zéro — les creux se remplissent de travail autonome sous budget.

## Le problème, en une image (D1)
Graphe Plan Usage MiniMax (screenshots A+ 2026-07-06) : 4,64 B tokens / 47 jours actifs / pic 381 M. **Pics = A+ au clavier. Chutes à zéro = personne ne travaille.** Le veto-par-conception a produit l'impuissance acquise : la flotte attend l'humain. L5 = la flotte remplit les creux elle-même.

## Confrontation externe (recon D1 CE run — 5 fetches réels + 1 hypothèse marquée)

| Source | Ce que c'est (lu ce run) | Verdict d'intégration A'Space |
|---|---|---|
| **google-deepmind/concordia** | Simulation sociale générative : **Game Master** + Entities + **Components** + Engine loop (pattern TTRPG, papers arXiv 2312.03664 + 2507.08892) | **PATTERN : adopter maintenant, LIB : gated.** Le pattern GM/Entity-Component EST notre WF3 (MiroFish = GM déterministe, agents = entities, mindsets = components) — le nommer aligne notre design sur l'état de l'art, coût zéro. La lib elle-même = candidat **MiroFish v2 LLM-driven** (simuler les 3 personas Nexus réagissant aux offres !) — token-lourd, gated derrière Beth-capacité + budget, PAS avant que le cadran 4 tourne. |
| **anthropic.com/engineering/harness-design** | Architecture 3 agents **planner → generator → evaluator** (inspirée GAN) ; « one feature at a time » ; « structured artifacts to hand off context between sessions » ; « context resets between sessions » | **VALIDE notre design + 1 greffe.** Runner/worker/worklog = déjà conforme (chunks + artefacts + contexte frais). La greffe manquante : **l'evaluator séparé** — noter chaque itération WF1 contre une rubrique AVANT le SHIP (aujourd'hui le worker s'auto-évalue = D5 faible). |
| **cobusgreyling/loop-engineering** | npm `loop-init/audit/cost/sync/context` — scaffolde skills+state+**budget files**, imprime un **Loop Ready score** | **CONCEPTS : adopter.** Le « budget file » par loop + le score d'audit = exactement le gouverneur du cadran 4. Implémentation maison (Python citadel), pas de dépendance npm nécessaire. |
| **google/agents-cli** | CLI+skills pour déployer des agents sur Gemini Enterprise Agent Platform ; interop Claude Code/Codex/Antigravity | **PLUS TARD (franchise).** Rien pour la souveraineté locale ; pertinent quand un client B2B voudra son W× déployé sur GCP (PRD-HARNESS-FRANCHISE). |
| **mvanhorn/last30days-skill** | Skill de veille « scored by upvotes, likes, and real money » ; install marketplace CC | **ADOPTER (1 commande).** `/plugin marketplace add mvanhorn/last30days-skill` + `/plugin install last30days` → nourrit W2-Rock auto-research en actualité harness/loops. Gate : install = action réversible → Paperclip Utile, pas de GO requis. |
| **Claude Agent SDK** (docs code.claude.com) | HYPOTHÈSE non re-vérifiée ce run : SDK programmatique sessions/tools/MCP | Candidat pour écrire le runner v2 en process durable — à re-vérifier AVANT usage (RECON NEEDED : fetch docs overview). |

## MOVES

### M1 — Le collecteur Beth-capacité (le veto devient une mesure)
Créer `citadel/collectors/collector_15_capacity.py` : CPU %, RAM libre, disque, count processus `claude/python` actifs, tokens consommés aujourd'hui (parse usage local ou compteur worklog) → `data/15_capacity.json` + verdict `CAPACITY: GREEN|AMBER|RED` (seuils : RED si RAM < 2 Go ou CPU > 85 % soutenu ou budget jour épuisé).
- **Attendu** : `python collector_15_capacity.py` → JSON + verdict en 1 ligne.
- **Échec probable** : compteur tokens indisponible localement → cause : l'API usage MiniMax n'est pas exposée → **contre-action** : proxy = nombre d'itérations worker × coût moyen mesuré (calibrer sur 7 jours) ; marquer `token_estimate: true` (jamais un faux précis).
- **Fork** : SI la machine est RED → le runner SKIP son tick avec ligne worklog `capacity-red` — c'est Beth qui parle, pas une panne.

### M2 — Le GO Perpétuel (fichier d'état, pas de date d'expiration)
`citadel/decisions/GO_PERPETUEL_A0.json` : `{"scope":"WF0-WF3 + W* clients","granted":"<date>","expires":"none","suspend_if":["capacity RED","invariant kernel","invariant DLP"],"revoke":"A+ only, explicit"}`. Les runners lisent CE fichier au lieu de re-demander : présent + capacité GREEN = travailler.
- **Attendu** : runner démarre sans aucun flag temporaire ; suspension automatique si `suspend_if` déclenche ; reprise seule au retour GREEN.
- **Échec probable** : un agent traite « suspend » comme « revoked » et s'arrête définitivement → cause : impuissance acquise résiduelle → **contre-action** : le runner re-teste la capacité à CHAQUE tick — suspend = sieste, jamais mort.
- **Fork** : SI le fichier GO est absent/corrompu → reconstruire depuis ce wargame + ligne `go-rebuilt` (antifragile, wargame 13 M4).

### M3 — Le backlog qui ne se vide jamais (la poussée)
Le creux vient d'un backlog vide. Chaînage : backlog WF1 §2c (redact.py → quiz.html → prompts AARRR) → PRD-PORTFOLIO tier 1 → orphelins E2 b1-filter (453) → re-distillation obsolescence (93 guides flaggés par le hook) → wargames restants. Règle : **quand la file < 3 items, Boimler (Clarify) promeut depuis la strate suivante** — automatique, pas de GO.
- **Attendu** : `tickets/` jamais < 3 items pendant 7 jours consécutifs (mesurable au worklog).
- **Échec probable** : le feeder promeut du travail de mauvaise qualité pour remplir → cause : quantité > qualité (leçon Fouloscopie : la masse des publications a un impact nul) → **contre-action** : chaque item promu porte son critère de done (Una) + passe l'evaluator M4 — remplir ≠ produire du bruit.
- **Fork** : SI les 4 strates sont vides (jamais observé) → le feeder génère UNE tâche `retro-cycle` (W0-style) et s'arrête là.

### M4 — L'evaluator greffé (la leçon Anthropic)
Chaque itération worker passe par un agent évaluateur séparé (contexte frais) qui note contre la rubrique du domaine (SUCCESS-ASPACE pour les wargames, DoD Una pour les sprints) AVANT le tag SHIP. Score < seuil → l'item retourne en queue avec le verdict (pas de re-théorisation, le verdict EST la spec du retry).
- **Attendu** : ligne worklog `[evaluator] PASS 10/12` ou `RETURN 6/12 <motif>` par itération.
- **Échec probable** : l'evaluator complaisant (même modèle, même biais) → cause : pas d'adversarialité → **contre-action** : prompt évaluateur = « REFUTE d'abord » (pattern refute-first) + échantillon audité par A+ 1×/sem.
- **Fork** : SI evaluator indisponible (API down) → SHIP avec tag `unevaluated` visible, jamais silencieux.

### M5 — Le gouverneur de budget (remplir les creux SANS brûler le plan)
Budget file par loop (concept loop-engineering) : `loops/domains/<loop>/budget.json` `{daily_tokens_target, floor_reserve}`. Le runner consomme jusqu'à la cible quand la machine est libre (creux) et s'arrête à la réserve. Cible initiale sobre : combler les creux à ~50 % du pic manuel (≈ 150-190 M/jour) puis calibrer.
- **Attendu** : le graphe MiniMax des 14 prochains jours montre des creux ≥ 30 % du pic au lieu de zéro.
- **Échec probable** : double comptage entre loops → chacun croit avoir le budget entier → **contre-action** : le collector M1 tient le compteur GLOBAL jour ; les loops lisent, ne possèdent pas.
- **Fork** : SI le plan mensuel approche 90 % avant J-7 → gouverneur passe tous les loops en `eco` (itérations 1/2 fréquence) + push Telegram.

### M6 — L'échelle de décision câblée (ADR-AIRLOCK-001 §3)
Implémenter le handover : un worker bloqué écrit `tickets/blocked-<slug>.md` avec l'échelle remplie (ce que Morty a dit / ce que la méta-mémoire Computer a donné / pourquoi indécidable) AVANT tout ping A+. Le push Telegram quotidien liste les `blocked-*` avec leur barreau atteint.
- **Attendu** : zéro question directe à A+ qui n'ait pas son ticket d'échelle.
- **Échec** : un ticket dont l'échelle est vide → retour à l'agent avec tag `ladder-skipped`.

## ABORT CONDITIONS
1. Capacité RED persistante > 24 h → tout suspendre + Telegram (la machine d'abord, le backlog attendra).
2. Budget mensuel consommé à 100 % avant J-5 → full stop loops non-critiques, seul heartbeat continue.
3. Un item du feeder M3 touche le canon/le réel hors sandbox → boundary-violation, STOP.
4. Beth-santé (humain) : si le système se met à solliciter A+ la nuit (pushes non-urgents 23 h-7 h) → couper les notifs nocturnes, pas le travail.

## VERIFICATION RUNS
1. `collector_15_capacity.py` ×2 → **pass** = JSON + verdict, 2e run idempotent.
2. Supprimer le GO file puis run → **pass** = `go-rebuilt` + travail reprend.
3. Vider `tickets/` artificiellement → **pass** = feeder promeut ≥ 3 items avec DoD au tick suivant.
4. Itération volontairement bâclée → **pass** = evaluator `RETURN` avec motif, item re-queué.
5. Budget jour mis à 1000 tokens (test) → **pass** = loops passent `eco`/skip, ligne worklog.
6. 14 jours après activation : screenshot du graphe MiniMax → **pass** = plus de chute à zéro un jour de semaine.

## RED-TEAM PASS
- **Attaque ÉCHOUÉE** : « le GO perpétuel = paperclip destructeur, la flotte brûle le plan en 3 jours » — non : M1 (capacité) + M5 (gouverneur global + réserve + mode eco) bornent mécaniquement ; le GO est perpétuel en DURÉE, pas illimité en DÉBIT. L'enveloppe tient.
- **Attaque RÉUSSIE → patch intégré** : « le feeder M3 + l'evaluator M4 créent une boucle d'auto-satisfaction : le système remplit les creux avec du travail que lui-même juge bon, et A+ découvre en W13 un cycle entier de production hors-sujet ». Patch : **ancrage exogène hebdomadaire** — chaque lundi, le premier item de la file DOIT venir d'une source externe au système (push Telegram A+ non traité, signal client, ou `/last30days` actualité) ; s'il n'y en a pas, le feeder le dit (`no-exogenous-anchor`) au push Telegram. Le monde réel reste le juge de paix.

## SELF-GRADE /12 (SUCCESS-ASPACE)
1-2 ✅ attendu+échec/cause/contre par move · 3 ✅ forks triggers · 4 ✅ RECON NEEDED (SDK docs) marqué · 5 ✅ 4 aborts · 6 ✅ 6 runs · 7 ✅ red-team 1 échouée + patch ancrage-exogène · 8 ✅ blind-exécutable · 9 ✅ D1 (5 fetches réels, 1 hypothèse marquée, screenshots cités) · 10 ✅ append-only · 11 ✅ mapping canon (airlocks/WF/A3 GTD roster exact) · 12 ✅ Beth-compat (abort 4 : notifs nocturnes coupées, pas le travail).

**12/12.**

---

## ⚡ÉVOLUTION 2026-07-06 (dictée A+, même jour) — M2 amendé : le GO n'est plus perpétuel, il est TRIENNAL RENOUVELABLE

**Correction A+** : « le Airlock GO n'est plus Perpétuel mais d'une Durabilité Antifragile de 3 ans Renouvelable avec Idempotence. » Le mécanisme suspend=sieste est CONFIRMÉ ; seule la durée change, et elle sort des **maths de compression temporelle** :

| Échelle L1 (plan) | Exécution L2 (B1-B3) | Facteur |
|---|---|---|
| 1 semaine (sprint Una, 5-7 daily scrums M'Benga) | **1 jour** | ×5-7 |
| 1 mois (Rock Pike, 4 sprints) | **1 semaine** | ×4-5 |
| 1 trimestre (cycle 12WY Curie) | **1 mois** | ×4 |
| 1 an (4 cycles) | **1 trimestre** | ×4 |
| **12 cycles 12WY (~3-4 années civiles)** | **~1 an L2** | ×4 |

**La conséquence H10** : 3 années réelles de GO × compression ×4 soutenue = **~12 années d'expérience vécue = un horizon H10 EXPÉRIMENTÉ** (pas seulement visionné). D'où : Book évolue H1 → H3, Picard passe de H10-expérimenteur à **H30**, A+ a 33 ans à l'échéance. Le renouvellement du GO coïncide avec la graduation d'horizon — c'est un rite, pas une paperasse.

**Receipt de cohérence (D1)** : le facteur ×4 soutenu est EXACTEMENT le CAP que MiroFish a simulé et que WF2 a absorbé (`sim-cadence-x8` verdict RISQUE → cap ×4 tant que capacité < 96/WK). La doctrine et la simulation disent le même chiffre par deux chemins indépendants.

**M2 v2** : `GO_PERPETUEL_A0.json` → renommer le champ : `"expires": "<granted+3y>"`, `"renewable": true`, `"renewal_rite": "graduation horizons (Book H1->H3, Picard H10->H30)"`. Idempotence et suspend_if inchangés. Le nom de fichier reste (D4, pas de rename cassant) — le contenu porte la vérité.

**Roster (réponse au nom oublié)** : le 5e A3 de Curie/SNW = **Ortegas** (exécution, daily standup, « did it actually work »). Uhura n'est pas au roster canon des 5. Le benchmark **Time Use = Chapel** (measurement, lead/lag, D11) — c'est elle qui tient le bilan de W2.

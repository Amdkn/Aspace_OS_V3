# WARGAME 22 — Le Dernier Jour de Fable : les 5 use-cases (Chase AI) confrontés au différentiel A'Space

> **WARGAME ORDER** : Tu n'exécutes pas cette mission, tu la wargames. Source : vidéo Chase AI « You Only Have 1 Day Left For These Fable 5 Use Cases » (transcript à l'écran CE run). Mission : confronter les 5 prompts « dernières heures Fable » à l'état RÉEL d'A'Space — ne dépenser le quota résiduel (~15 %, reset dim. 19:00) QUE sur le différentiel, jamais sur ce que la banque couvre déjà. La thèse du wargame 19 s'applique : Fable = étalon rare ; tout ce qu'un M3 harnaché peut faire ne se paie pas en Fable.

## Statut recon (D1 — vérifié CE run)

| Use-case Chase AI | État A'Space (preuve) | Verdict différentiel |
|---|---|---|
| **1. Plan future work** (PLAN-slug exécutables par modèle faible) | **DÉJÀ LE CŒUR DE LA BANQUE** : 21 wargames = exactement ce format (moves+forks+aborts+verification runs, critère #8 « exécutable blind par mid-tier »). + 10 plans `~/.claude/plans/plan-*.md` (listés) | ✅ COUVERT — résiduel : le RANKING par levier n'existe pas |
| **2. Second brain Karpathy** (inbox→projects→output→wiki, /harvest) | Wiki canon existe (12 MB, index, hand_offs=output, guides Geordi=resources) MAIS flux par ÉTAPES non formalisé ; **`/harvest` n'existe pas** (vérifié : `no /harvest`) ; la règle « wiki seulement après ship » ≈ notre doctrine distill (L1→L2) mais non-écrite comme LOI | 🟡 PARTIEL — résiduel : la règle harvest + le skill |
| **3. Log review 30j** (patterns répétés, tours gaspillés, workflows→skills) | `history.jsonl` existe (168 KB, vérifié) + 61 sessions projects. Wargame 16 = méta-audit skills/routage, baselines v2 = discipline — MAIS **le comptage de patterns de PROMPTS répétés n'a jamais été fait** | 🟡 PARTIEL — résiduel : l'analyse patterns-de-A+ (pas de l'agent) |
| **4. Skill optimization pass** (keep/merge/rewrite/delete) | **77 skills** (compté CE run, vs 58 hier — dérive rapide). Wargame 16 M3 a spéccé le gate d'intake mais **SKILL_REGISTRY n'existe toujours pas** (vérifié wargame 21) | 🔴 DIFFÉRENTIEL PLEIN — le plus rentable des 5 |
| **5. Ultracode projet remisé** | L'outil Workflow/ultracode EST dans le harnais CC Desktop (vérifié : présent cette session). Le « projet trop gros repoussé » canonique = **l'exécution des MOVES de la banque** (21 wargames de rails, ~0 exécutés en build) | 🟡 PARTIEL — résiduel : UN ultracode ciblé, pas cinq |

## La partition Fable/M3 (l'ordre du dernier jour)

**Loi wargame 19 M1 appliquée** : Fable ne fait que ce qui exige l'étalon (jugement, ranking, adversarial). Tout le mécanique part en M3 post-reset.

```
FABLE (heures restantes, ~15 %)          M3 (chaîne, après dim. 19:00)
─ M2 ranking par levier (jugement)       ─ exécution des PLAN élus
─ M4 audit 77 skills : la TABLE          ─ les rewrites de descriptions décidés
  keep/merge/rewrite/delete (adversarial)─ migration notes → étapes (mécanique)
─ M3 lecture patterns A+ (nuance)        ─ comptages/greps du M3 (mécanique)
```

## MOVES

### M1 — Le méta-prompt « plan for weaker model » institutionnalisé
Le prompt #1 de Chase AI EST notre format wargame — le formaliser en loi : tout livrable Fable = « exécutable par M3 sans question » (DoD + fichiers exacts + edge cases qu'un modèle faible raterait + acceptance criteria). Ajout au WORKER_PROMPT v3 côté ÉMETTEUR : Fable écrit des rails, jamais des intentions.
- **Attendu** : 1 § « Loi du rail » appendé au wargame 19 M2 (renvoi ⚡, pas de réécriture).

### M2 — Le RANKING par levier (le résiduel du #1 — tâche Fable)
La banque a 21 rails mais AUCUN classement d'exécution. Fable classe les MOVES non-exécutés des 21 wargames par levier (impact × déblocage d'autres moves ÷ coût M3) → `EXECUTION-RANKING.md` : top 10, avec « lequel en premier » épelé.
- **Attendu** : le fichier, top 10, 1er élu justifié en 3 lignes.
- **Échec probable** : ranking par enthousiasme, pas par levier → **contre-action** : chaque rang cite sa dépendance (ce qu'il DÉBLOQUE) — un item qui ne débloque rien ne peut pas être top 3.

### M3 — Log review 30j : l'audit des patterns de A+ (le miroir inversé)
Les baselines v2 ont mesuré L'AGENT ; personne n'a mesuré A+. Script M3 sur `history.jsonl` + 61 sessions : (a) top 5 demandes répétées avec comptes, (b) tours de correction (où A+ re-explique = D7 déclenché), (c) workflows manuels 3+ fois sans skill, (d) le construit-jamais-utilisé. Fable ne fait que la LECTURE finale (la plus grosse inefficacité de prompt d'A+ — jugement de nuance).
- **Attendu** : `wiki/hand_offs/audit_patterns_a0_30j_<date>.md` — chiffres + 3 skills candidats + LA inefficacité #1.
- **Fork** : SI un pattern ≥ 5 occurrences sans skill → création immédiate (Skill Creator Reflex Phase 2, pas de GO requis).

### M4 — Skill optimization pass : 77 skills au tribunal (LE différentiel plein)
La dérive est mesurée : 58 → 77 skills en ~24 h (D1 : comptés hier wargame 21 et CE run). Audit complet : trigger réel ? collision ? poids mort ? → **TABLE keep/merge/rewrite/delete** + création enfin du `SKILL_REGISTRY.md` (le gate wargame 16 M3, 2× spéccé, 0× construit — c'est le smell). Fable rend les VERDICTS (adversarial) ; M3 applique les rewrites.
- **Attendu** : la table (77 lignes), les 3 pires descriptions réécrites, LE pire body réparé, SKILL_REGISTRY.md créé avec ligne d'intake obligatoire.
- **Échec probable** : « delete » viole D4 → **contre-action** : delete = move vers `skills/_TRASH/<date>/`, jamais de hard-delete.

### M5 — La règle Harvest (le résiduel du #2, adapté au canon)
PAS de nouveau vault Obsidian (collision frontale avec wiki canon 12 MB + PARA — le « second brain » EXISTE). Le résiduel est UNE loi + UN skill : **« le wiki se récolte, ne s'écrit pas »** — une page evergreen (concepts/, entities/) n'est créée QUE depuis un artefact shippé (handoff, wargame exécuté, projet clos). `/harvest <fichier-fini>` : distille → page wiki + cross-links + ligne index. Le flux d'étapes existe déjà sous d'autres noms : inbox=Mariner/GTD · projects=10_Projects Picard · output=hand_offs · wiki=concepts. On NOMME l'isomorphie, on ne crée pas de dossiers.
- **Attendu** : `/harvest` SKILL.md (<100 lignes) + la loi en 1 § dans wiki/index.md (append).

### M6 — L'ultracode ciblé (le #5 discipliné par l'Airlock)
« Burn it all » brut viole l'Airlock — la version A'Space : UN ultracode sur LE 1er élu du ranking M2, avec les garde-fous du harnais (réversible = pas de permission ; irréversible = stop ; vérif adversariale interne ; budget tokens plafonné gouverneur wargame 15 M5). Le « projet remisé » n'est pas à inventer : c'est le top-1 de M2.
- **Fork** : SI le top-1 exige > le plafond budget → le découper en phases M3 séquentielles plutôt que renoncer.

## ABORT CONDITIONS
1. Quota Fable < 5 % → M2 et M4-verdicts seulement (le ranking et la table sont les deux seuls gestes irremplaçables), tout le reste bascule M3 post-reset.
2. M5 : AUCUNE création de structure parallèle au wiki canon (pas de vault, pas de dossiers neufs) — l'isomorphie se nomme, ne se duplique pas.
3. M4 : aucun hard-delete de skill — `_TRASH` daté ou rien.
4. M6 : l'ultracode respecte l'échelle de décision (AIRLOCK-001 §3) — un blocage = ticket `blocked-*`, jamais un ping A+ nocturne.

## VERIFICATION RUNS
1. `EXECUTION-RANKING.md` existe, top 10, dépendances citées par rang → **pass**.
2. Audit patterns A+ : le fichier avec ≥ 5 patterns COMPTÉS (chiffres, pas d'impressions) → **pass**.
3. `SKILL_REGISTRY.md` créé + table 77 verdicts + `ls skills/ | wc -l` stable 2 semaines (la dérive s'arrête) → **pass**.
4. `/harvest` : 1 exécution réelle sur un wargame exécuté → 1 page wiki créée avec cross-links → **pass**.
5. Ultracode top-1 : livré avec vérif adversariale interne + budget consommé ≤ plafond → **pass**.

## RED-TEAM PASS
- **Attaque ÉCHOUÉE** : « c'est du FOMO marketing — "dernier jour" est le hook de la vidéo, pas ta réalité : ton Fable revient dimanche 19:00 » — exact sur le fait (abonnement hebdo ≠ dépréciation API), mais l'attaque rate la cible : le wargame n'achète pas l'urgence, il exploite la CONTRAINTE réelle (~15 % restants) pour forcer la partition Fable-juge/M3-ouvrier — qui reste optimale même sans deadline. La rareté hebdo EST notre rythme permanent (wargame 19 M1 : ≤ 15 %/sem). Rien à patcher.
- **Attaque RÉUSSIE → patch intégré** : « M4 va s'auto-saboter : l'audit des 77 skills sera fait PAR l'agent qui les a créés — juge et partie, il gardera ses propres créations (endowment bias) et la table sera un plébiscite, pas un tribunal ». Patch (M4 durci) : **le verdict de chaque skill est rendu contre 3 preuves EXTERNES à l'opinion** — (a) usage réel : grep des invocations dans les 61 sessions (un skill jamais invoqué en 30 j plaide coupable), (b) collision : overlap de mots-clés de description mesuré entre paires (score > seuil = merge obligatoire à justifier), (c) la règle Gwyn/D11 : coût de maintenance vs temps libéré. Un « keep » sans preuve (a) ou (c) est requalifié « dormant » d'office — l'opinion de l'auteur ne compte pas comme preuve.

## SELF-GRADE /12 (SUCCESS-ASPACE)
1-2 ✅ · 3 ✅ forks · 4 ✅ RECON (5 états vérifiés CE run : plans listés, no /harvest, history.jsonl 168 KB, 77 skills comptés, Workflow présent) · 5 ✅ 4 aborts · 6 ✅ 5 runs mesurables · 7 ✅ red-team (FOMO échouée par contrainte-réelle · juge-et-partie réussie→patch preuves externes) · 8 ✅ blind · 9 ✅ D1 (différentiel prouvé ligne par ligne, dérive 58→77 chiffrée) · 10 ✅ append-only (renvois ⚡, _TRASH, jamais de réécriture) · 11 ✅ mapping canon (GTD/PARA/Picard/Geordi = les 4 étapes Karpathy nommées, pas dupliquées) · 12 ✅ Beth (abort 4 : nuits silencieuses, l'ultracode ne réveille pas A+).

**12/12.**

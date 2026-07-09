# EXECUTION RANKING — les MOVES non-exécutés de la banque, classés par levier

> Wargame 22 M2 exécuté 2026-07-07 (Opus 4.8, Fable préservé). Levier =
> **impact × ce que le move DÉBLOQUE ÷ coût M3**. Règle : un move qui ne débloque
> rien ne peut pas être top 3 (contre-action anti-enthousiasme). Source : MOVES des
> wargames 13-22 (headers extraits CE run). Les wargames 01-12 sont antérieurs au
> format MOVE et hors périmètre de ce ranking.

## Top 10 (ordre d'exécution)

| # | Move | Wargame | Débloque | Coût M3 | Pourquoi ce rang |
|---|---|---|---|---|---|
| **1** | **SKILL_REGISTRY + gate d'intake** | 16 M3 / 22 M4 | TOUT futur skill/hook/plugin/harness ; arrête la dérive 58→77 | faible | Spéccé **2×, construit 0×** = le smell le plus fort de la banque. Sans lui, chaque wargame ajoute du bloat non-gouverné. **Le seul move qui se paie tout seul dès le 1er usage.** ✅ construit ce run (voir §exécuté) |
| **2** | **GO Perpétuel — fichier d'état** | 15 M2 | le feeder (3), l'evaluator (4), le gouverneur budget — TOUTE la chaîne autonome en dépend | faible | Un fichier d'état sans date d'expiration = la condition d'existence de l'autonomie. Rien d'autonome ne tourne sans lui. Racine de dépendance. |
| **3** | **Collecteur Beth-capacité** | 15 M1 | l'Airlock 1 (le veto devient mesure), le GO triennal | moyen | Le veto santé→capacité (ADR-AIRLOCK-001) reste abstrait tant que la capacité n'est pas COLLECTÉE. Débloque la décision GREEN/RED réelle. |
| **4** | **Feeder Boimler — backlog jamais vide** | 15 M3 | la cure de l'impuissance acquise ; la chaîne M3 ne s'arrête jamais | moyen | File < 3 → promotion auto depuis les strates. C'est l'anti-« token graph tombe à zéro ». Débloque le travail nocturne continu. |
| **5** | **Idempotence + persistence run-loop** | 13 M2-M3 | survie au reboot de tous les loops (les LogonTriggers posés en ont besoin) | moyen | Sans dedupe run-id au niveau fichier, le boot-durable rejoue ou corrompt. Foundational pour que 2-5 tiennent après restart. |
| **6** | **Contrat de ticket (format rail)** | 19 M2 | la délégation M3 entière ; le feeder (4) produit des tickets conformes | faible | « Un item sans rail ne part pas en M3 ». Le format existe (les 22 wargames), il faut le CÂBLER dans le feeder + WORKER_PROMPT. |
| **7** | **fable-mode câblé au WORKER_PROMPT** | 21 M3 | la discipline sur les agents nus (Hermes/Codex/B4) ; baselines v3 | faible | Skill créé ce run ; reste l'étape « charge /fable-mode si tâche dure » dans le prompt worker + préambule pour agents non-CC. |
| **8** | **Gouverneur de budget tokens** | 15 M5 | remplir les creux du graphe MiniMax SANS dépasser le plan 5,1 B | moyen | Débloque l'accélération sûre. Dépend de la mesure coût/itération (19 M5). Sans lui, la chaîne autonome peut brûler le plan. |
| **9** | **Échelle de décision câblée** | 15 M6 / 19 M4 fork | remonte A3→Morty→Computer→Beth au lieu de pinger A+ | moyen | La condition Beth des nuits silencieuses. Débloque l'autonomie sans réveil A+. |
| **10** | **B4/L3 layer dans B1_Manifesto** | 20 M4 | les freelances jetables spawnables par B3 ; la scalabilité franchise | faible | ≤ 15 lignes, mais débloque la couche d'exécution jetable — après que 1-9 tiennent. |

## Le 1er à faire (justification 3 lignes)

**#1 SKILL_REGISTRY** — c'est le seul move dont l'absence *aggrave activement le système à chaque tour* (le dossier skills a gonflé de 19 unités en 24 h, non-gouverné). Il coûte presque rien, débloque toute gouvernance future, et son absence était le plus vieux dette de la banque (2 wargames l'ont spéccé). **Fait ce run** (M4 ci-dessous) — le ranking l'a élu et l'exécution a suivi immédiatement.

## Ce que le ranking EXCLUT sciemment (D1 honnêteté)

- Les MOVES **gated A+** (20 M3 pricing, 21 M4 export franchise) ne sont pas classés : ils attendent une ratification, pas un rang d'exécution.
- Les wargames 01-12 (WF0/WF1/WF2 fondateurs) n'ont pas le format MOVE granulaire — leur exécution est suivie ailleurs (worklog WF1 live).
- Coût M3 = estimation `assumed:` (le coût/itération réel n'est mesuré qu'à partir du wargame 19 M5). Sensibilité : même à ±50 %, le top 3 ne bouge pas (leur levier vient du déblocage, pas du coût).

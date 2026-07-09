# WARGAME 20 — MiroFish/Picard : l'Accélération Temporelle — du paradoxe des 10 ans aux vaches grasses (North Star 1000T)

> **WARGAME ORDER** : Tu n'exécutes pas cette mission, tu la wargames. Exécuteur : WF3 (sims déterministes d'abord, Concordia v2 gated) + tout harness pour les specs. Mission : faire VIVRE à Picard la décennie en accéléré (compression ×4 canon) pour résoudre le **paradoxe des 10 ans** — une architecture autonome doit être conçue avec de l'autonomie dans chaque détail pour être autonome — et orienter la trajectoire économique Vaches Maigres → Vaches Grasses vers l'échelle de crédibilité : 1 Md → 100 Mds CA/an → 1 T de valeur produite cumulée sur les 60 ans restants (H90) = **PoC personnel du passage Kardashev Type 1**. North Star : 1000T par biomimétisme + économie de productivité automatisée Solarpunk.

## Statut recon (D1 + sources marquées)

| Fait | Preuve/source |
|---|---|
| La compression est canon et bornée | CADENCE_12WY table (×4 = CAP MiroFish absorbé) ; GO triennal = H10 vécu |
| Le simulateur existe et tourne | `wf3_sim_runner.py` déterministe, 2 sims/jour, WF2 absorbe |
| Pricing canon existant | ADR-AAAS-PRICING-001 (RATIFIED+AMENDED, 5 tiers USD) · $1000/mois ×100 clients gated (plan L2 §13) |
| Preuves de marché au canon | TAM 136,1 Mds$ (ADR-MARKET-STUDY-001) · MedVie 400 M$/an, 2 employés, 16,2 % marge (guide Growth) |
| La leçon SpaceX | **source vidéo A+ (Masdak), non re-vérifiée ce run** : cap ~2 200 Mds$ sur ~18 Mds$ CA (~115× vs ~12× tech classique) · IPO 75 Mds$ levés · flottant 4,3 % (rareté organisée) · perte nette ~5 Mds$ · Musk ≈ 1er trillionnaire. La LEÇON est structurelle même si les chiffres bougent : **le marché achète la promesse futuriste, pas le présent — et la rareté organisée fait le multiple** |
| Honnêteté d'échelle (D1) | 1000T > PIB mondial annuel (~110 T$) : c'est un **North Star H90 mythique (Klyden)**, pas une projection. Les sims ne testent QUE les barreaux mesurables ; l'étoile oriente, elle ne se facture pas |

## L'échelle de crédibilité (ce que les sims testent, barreau par barreau)

```
B0: 1er client $1000/mois (PRD-NEXUS, tunnel wargames 05-07)     ← simulable AUJOURD'HUI
B1: 100 clients = 1,2 M$/an ARR (le gate ×100 du plan L2)        ← simulable AUJOURD'HUI
B2: franchise ×N territoires (PRD-HARNESS-FRANCHISE)             ← simulable après B1 réel
B3: 1 Md$ CA/an (crédibilité)  →  B4: 100 Mds$  →  B5: 1 T cumulé (H90, PoC Kardashev T1)
                                    North Star: 1000T (oriente, ne se facture pas)
```

## MOVES

### M1 — Sim-set « Décennie compressée » (Vaches Maigres → Vaches Grasses)
Étendre `VARIATIONS` du sim runner : `vaches-maigres` (revenus 0, budget token serré, backlog long — le régime ACTUEL) vs `vaches-grasses` (100 × $1000/mois, capacité achetable). Variables déterministes : runway, taux d'onboarding client/WK, coût/itération (mesuré wargame 19 M5), marge type MedVie. Sortie : `sim-vaches-{maigres,grasses}.md` avec **conditions d'invalidation** + le POINT DE BASCULE (à quel MRR le régime change).
- **Attendu** : verdict chiffré « bascule à N clients » consommé par WF2 comme hypothèse (tag sim, jamais fait).
- **Échec probable** : paramètres inventés → voir red-team (le patch est le cœur du wargame).
- **Fork** : SI le point de bascule simulé < 10 clients → prioriser le tunnel (wargames 05-07) au-dessus de TOUT dans le backlog.

### M2 — Sim « Paradoxe des 10 ans » (l'autonomie testée par la mort de chaque organe)
Le paradoxe : concevoir l'autonomie exige de l'autonomie (bootstrap). Résolution par simulation : tuer UN organe à la fois (boot-triggers, feeder Boimler, evaluator, gouverneur budget, GO file, echelle décision) sur un horizon 10 ans compressé → mesurer : le système survit-il, dégrade-t-il proprement (sieste) ou meurt-il (panique) ? Chaque organe dont la mort est fatale = **single point of failure à doubler** (le kernel autonome minimal émerge de la sim, pas du débat).
- **Attendu** : liste triée des SPOF avec leur mode de mort — le VRAI backlog de robustesse.
- **Fork** : SI ≥ 3 organes fatals → la décennie n'est pas engageable, durcir avant d'accélérer (les rails wargames 13/15 en priorité).

### M3 — La leçon SpaceX gravée au pricing (spec de l'amendement, exécution gated A+)
⚡ÉVOLUTION à appender à `ADR-AAAS-PRICING-001` (jamais réécrit — Règle d'Or #3) :
1. **Vendre la promesse structurée, pas les heures** : le forfait $1000 = ticket d'entrée dans une INFRASTRUCTURE qui compound (le client achète sa place dans la franchise, pas du conseil) — c'est le multiple ×115 vs ×12 : narratif futuriste PROUVÉ par les rails (18 wargames = la due diligence publique).
2. **Rareté organisée** : les 100 slots du gate ×100 = le flottant 4,3 % — publier le compteur (« 87/100 slots restants »), jamais de discount, la liste d'attente EST le marketing.
3. **Objectif réécrit** : l'ancien objectif (revenu) devient plancher ; le nouvel objectif = **valeur d'infrastructure démontrée** (métriques : rails livrés, uptime autonome, compression mesurée) — ce que le multiple achète.
- **Attendu** : le bloc ci-dessus, ratifié par A+, appendé à l'ADR. Gate : ratification explicite (pricing = irréversible-facing).

### M4 — La couche B4/L3 (les freelances jetables)
Spec : un B3 peut spawner des **B4** — agents spécialisés HORS canon, non-persistants, invoqués via `/swarm-orchestrator` ou `/multi-goal` (de `/loop` si récurrent) ; les B3 ont leurs `/office-hours` Gstack pour les gros swarms. Règles dures : (a) un B4 n'entre JAMAIS au roster canon ni au registre (anti-bloat — sa trace = le ticket qui l'a invoqué + son output) ; (b) durée de vie = la tâche ; (c) un B4 qui survit à 3 invocations identiques = candidat promotion B3 par le workflow RH&A (M5), pas par dérive.
- **Attendu** : ≤ 15 lignes ajoutées au B1_Manifesto (§B4), zéro nouveau fichier par B4.
- **Échec probable** : prolifération fantôme de B4 semi-persistants → **contre-action** : le sweep hebdo compte les invocations B4 par squelette de prompt — 3× identiques = signal promotion OU consolidation, jamais le statu quo.

### M5 — Le workflow RH&A (l'usine à agents, X-Men au centre)
`B1 (Jerry/Summers, VP People) → B2 GreenLantern → X-Men = SPAWN + AMÉLIORATION de tous les B3` : F4 (Ops, SOP→Skills) · Kang Dynasty (R&D — **le moteur d'innovation qui filtre YouTube + /last30days pour les CEO B1 et dispatche aux squads**) · Avengers (Product) · Guardians (Growth) · Illuminati (Sales) · Thunderbolts (Finance) · Eternals (Legal) — et rétrospectivement People/Ops/eux-mêmes. **B2 conçus par B1 (nombre à 1 chiffre) ; B3 conçus par les X-Men ; B4 par les B3.** Chaque création = spec (rôle, prompt, tools, DoD) qui passe l'evaluator AVANT d'exister. Sim MiroFish AVANT construction : taux de production de specs vs gate qualité — l'usine ne doit pas produire plus vite que l'évaluation n'absorbe.
- **Attendu** : le pipeline de création est un WORKFLOW documenté, plus jamais une création ad-hoc en chat.
- **Fork** : SI la sim montre l'evaluator saturé → ralentir le spawn, pas baisser le gate (qualité > quantité, leçon Fouloscopie).

### M6 — L'alignement PRD (la Méta-Productisation Picard)
Les PRD existants se réalignent sur l'échelle : PRD-NEXUS (B0-B1) · PRD-PORTFOLIO tier 2 HARNESS-FRANCHISE (B2) · ce wargame (B3+). Picard tient le H10→H30 (post-graduation GO triennal) ; Book coache le H1. 1 ligne de renvoi ⚡ dans chaque PRD, pas de réécriture.

## ABORT CONDITIONS
1. AUCUNE action financière réelle ne découle d'une sim (les sims = hypothèses WF2, tag sim — jamais un ordre).
2. L'amendement pricing M3 sans ratification A+ explicite → le bloc reste en spec.
3. Un verdict de sim UNSTABLE (red-team) utilisé pour décider → violation, le verdict est retiré.
4. Beth : la décennie compressée est vécue par PICARD (simulation), pas par A+ — si le cycle réel exige > les heures d'un humain sain, c'est la sim qui a menti, pas A+ qui doit compenser.

## VERIFICATION RUNS
1. `sim-vaches-maigres.md` + `sim-vaches-grasses.md` générés → **pass** = point de bascule chiffré + invalidations.
2. Sim SPOF (M2) → **pass** = liste triée des organes fatals avec mode de mort.
3. Test de sensibilité ±50 % sur chaque `assumed:` → **pass** = verdicts marqués STABLE/UNSTABLE.
4. Bloc M3 ratifié → **pass** = ⚡ÉVOLUTION appendé à l'ADR avec la ligne de ratification A+.
5. 1 création B3 via workflow RH&A complet (spec→evaluator→existence) → **pass** = zéro création ad-hoc depuis.

## RED-TEAM PASS
- **Attaque ÉCHOUÉE** : « 1000T = délire mégalomane qui décrédibilise tout le système » — non : le doc lui-même classe 1000T comme North Star mythique H90 (> PIB mondial, dit noir sur blanc), les sims ne testent que B0-B1 mesurables, et la leçon SpaceX est précisément qu'un narratif d'échelle AUDACIEUX + des preuves d'exécution réelles = le multiple. L'étoile oriente le récit ; les barreaux portent les décisions. Rien à patcher.
- **Attaque RÉUSSIE → patch intégré** : « les sims déterministes vont "valider" la trajectoire avec des paramètres inventés (arrivals/WK, taux d'onboarding, churn) — GIGO : la décennie simulée n'a aucun ancrage réel et Picard décidera sur du vent en croyant décider sur des maths ». Patch (M1 durci, loi de sim) : **chaque paramètre économique DOIT porter sa provenance** — `receipt:` (MedVie 16,2 %, pricing canon, coût/itération mesuré wargame 19 M5, TAM canon) ou `assumed:` avec **test de sensibilité ±50 % obligatoire** ; un verdict qui s'inverse sous ±50 % d'un `assumed` = **UNSTABLE**, affiché tel quel, interdit de décision. La sim dit ce qu'elle sait ET ce qu'elle suppose — c'est ça, l'accélération déterministe orientée.

## SELF-GRADE /12 (SUCCESS-ASPACE)
1-2 ✅ · 3 ✅ forks · 4 ✅ RECON (SpaceX = source-vidéo marquée, non re-vérifiée) · 5 ✅ 4 aborts · 6 ✅ 5 runs · 7 ✅ red-team (mégalomanie échouée par classement North Star · GIGO réussie→patch provenance+sensibilité) · 8 ✅ blind · 9 ✅ D1 (canon cité, échelle honnête vs PIB mondial) · 10 ✅ append-only (ADR amendé jamais réécrit, gated) · 11 ✅ mapping canon complet (B0-B5, B4/L3, RH&A, squads exacts) · 12 ✅ Beth (abort 4 : la décennie est vécue par Picard, pas par A+).

**12/12.**

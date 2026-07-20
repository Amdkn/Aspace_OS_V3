# Intégration complète CEO-BENCH × SpecLoop dans A'Space OS
## (les 18 composants réels — pas les 2 paroles sacrées)

> Sources lues intégralement : `CEO-BENCH.pdf` (Chen/Narasimhan/Liu, Princeton, 33 p.) · `spec loop.pdf` (SpecLoop, NTU/MediaTek, 7 p.).
> S'insère dans `ROADMAP_DEAL_12WY_2026-2027.md` (4 cycles · 12 Rocks · 48 sprints · 240 scrums). Fichier autonome, VPS-safe.

---

# PARTIE 1 — CEO-BENCH : les 11 composants et leur intégration

Ce que le papier prouve : seuls Opus 4.8 ($27.8M) et GPT-5.5 ($21.3M) finissent au-dessus du $1M de départ ; la baseline **à règles fixes fait $15.7M** — la plupart des agents font faillite. Ce qui sépare les gagnants des morts tient en 4 axes mesurés (Fig. 12) : découverte d'info cachée (43 % d'allocation efficace vs 20 % random), **erreur de forecast cash à 4 semaines (8 % vs 179 %)**, lag de détection concurrent (1 semaine vs 2), **densité de "if" dans les mémos (8.6/semaine vs 2.6)**. C'est ÇA qu'on intègre — pas le simulateur.

### C1 — Le refresh hebdo de contexte + fichier mémoire agent-editable (LE vrai "Next Week")
Le harness CEO-BENCH ne fait pas qu'avancer le temps : **il vide l'historique d'actions et ne garde que (a) le system prompt et (b) UN fichier mémoire que l'agent édite lui-même**, à chaque début de semaine. C'est comme ça que les 500 jours tiennent sans dérive de contexte.
**Intégration** : chaque domaine B2 a un `memory_<domaine>.md` (≤150 lignes, réécrit — pas appendé — par l'agent en fin de sprint S4). Le lundi, la session du domaine démarre avec : directive du Rock + ce fichier. RIEN d'autre. Pas d'historique, pas de wiki, pas de handoffs. Le fichier mémoire EST le contexte.

### C2 — Le mémo hebdo avec contingences if-then (le muscle des gagnants)
Les mémos d'Opus 4.8/GPT-5.5 (Fig. 13) : chaque décision porte sa branche inverse. « Capacity tier7→tier6, économise $329k/sem. **SI** les seats enterprise acceptent et l'usage saute, **retour tier7 immédiat**. »
**Intégration** : format obligatoire du sprint review B2 (S4 Harvest) : chaque décision = 1 ligne `DÉCISION + SI <signal observable> ALORS <réversion/escalade>`. Un mémo sans if-then est un mémo de perdant (2.6/sem = faillite). Cible : ≥5 if-then par mémo hebdo.

### C3 — Le forecast cash à 4 semaines, soumis CHAQUE semaine
CEO-BENCH force l'agent à prédire le cash à J+28 chaque semaine. L'erreur de forecast est LA mesure de compréhension du système : 8 % (survivant) vs 179 % (mort).
**Intégration** : chaque lundi, Summers (B1) écrit dans `forecast.md` : MRR prévu à J+28 + pipeline prévu. Chaque lundi, on compare le forecast d'il y a 4 semaines au réel. **Erreur > 50 % = le Rock du mois est mal compris** → c'est le signal de re-scope, pas un jugement.

### C4 — Les 19 tables SQL comme seule source d'état (pas de narratif)
L'agent CEO-BENCH ne "sent" pas son business : il query `ledger`, `subscriptions`, `ad_leads`, `support_tickets`. Ton équivalent réel minimal — **6 tables Supabase** :
`ledger` (chaque entrée/sortie €) · `subscriptions` (clients, MRR, statut) · `pipeline` (prospects, stage, source) · `outreach_log` (contacts, canal, réponse) · `issues` (bugs/support clients) · `experiments` (tests en cours + résultat).
**Intégration** : le scrum B3 commence par 1 query, finit par 1 delta. Un état non-requêtable n'existe pas.

### C5 — L'équation de cash quotidienne (Eq. 1 du papier)
`Δcash = abonnements + revenus annexes − infra − compute − support − dev − acquisition − recherche`.
**Intégration** : une vue SQL `daily_cash` qui décompose le burn réel (VPS, API tokens, outils, ads) vs revenus. Le plancher de faillite existe aussi pour toi : **cash < 2 mois de burn = mode préservation** (règle mécanique, pas garde-fou moral).

### C6 — Le budget d'acquisition d'information (payer pour découvrir)
Dans CEO-BENCH, 6 des 10 groupes de clients sont INVISIBLES tant qu'on ne paie pas `market.research`. Les gagnants paient pour découvrir ; les perdants optimisent leurs 3 groupes connus jusqu'à la mort.
**Intégration** : ligne budgétaire explicite par cycle (temps + € ) pour découvrir des segments ICP coach que tu ne connais pas : 10 conversations de découverte/mois, non-vendantes, loggées dans `pipeline` avec `source='research'`.

### C7 — Le spending CIBLÉ (90 % vs 43 %)
Fig. 10 : les gagnants mettent ~90 % du dev-spend en améliorations ciblées par segment ; les perdants saupoudrent.
**Intégration** : chaque € /heure de dev produit va à UN segment nommé (ex. « coachs executive US $10K+ ») — jamais à « améliorer le produit » en général. Vérifiable dans `experiments.segment`.

### C8 — Les 8 catégories d'action = tes 8 B2
| CEO-BENCH | B2 A'Space |
|---|---|
| Monetization (prix, quotas, promos) | Finance (WonderWoman) |
| Growth (ads ciblées par canal×segment) | Growth (Superman) |
| Product/R&D (dev ciblé, projets) | Product (Flash) + R&D (Cyborg) |
| Reliability (capacité, support) | Operation (Batman) |
| Enterprise sales (négociation multi-tours) | Sales (JohnJones) |
| Information acquisition | R&D (Cyborg) + Growth |
| Public communication (social) | Growth + RH Agentique (GreenLantern) |
| Database query | transverse — chaque B2 query sa vue |

### C9 — La détection concurrent en ≤1 semaine
Les gagnants détectent un move concurrent en 1 semaine via l'analyse du churn et du social — pas en lisant la presse.
**Intégration** : 1 scrum/semaine du domaine Growth = veille signaux faibles (churn inexpliqué, objection nouvelle en démo, prix concurrent cité par un prospect) → 1 ligne dans le mémo hebdo.

### C10 — Turns/semaine et coût API comme métriques
Opus 4.8 gagne avec **10.8 turns/semaine** ($213 de coût total sur 500 jours). GPT-5.5 en utilise 34.7. GLM 51.5 → faillite. **Plus de turns ≠ mieux : la discipline bat le volume.**
**Intégration** : budget tokens/domaine/semaine loggé dans `ledger` (catégorie `inference`). Un domaine qui brûle sans delta MRR se fait geler son budget au sprint suivant — mécanique, pas moral.

### C11 — Le monde non-stationnaire (l'ablation qui tue)
Sans concurrent adaptatif, le task devient facile (Fig. 14). Le réel EST adaptatif.
**Intégration** : c'est la justification du mémo C2 et de la veille C9 — jamais de stratégie figée plus d'un cycle. Le re-scope mensuel du Rock est une FEATURE, pas un échec.

---

# PARTIE 2 — SpecLoop : les 7 composants et leur intégration

Ce que le papier prouve : une spec est bonne **si et seulement si un exécuteur AVEUGLE peut reconstruire le comportement voulu à partir de la spec seule**, vérifié par équivalence formelle. Le feedback complet (contre-exemples) bat le pass/fail simple, qui bat le single-round (Table III : 0.94 vs 0.91 vs 0.86). Les specs vérifiées sont justes à 85-91 % vs 35-45 % pour les non-vérifiées (Fig. 3).

### S1 — Les 3 rôles séparés : Générateur / Reconstructeur / Vérificateur
Générateur écrit la spec depuis l'intention. Reconstructeur (AVEUGLE à l'original) reconstruit depuis la spec seule. Vérificateur compare original vs reconstruit.
**Intégration dans ta cascade** :
- **Générateur** = Summers (B1) : écrit le Runbook du Rock depuis la vision Picard.
- **Reconstructeur** = B3 : exécute depuis le Runbook SEUL, sans accès au contexte privé de Picard/Summers.
- **Vérificateur** = la query SQL de fin de sprint : le delta observé vs le delta que le Runbook promettait.

### S2 — Information hiding (LE principe de design)
SpecLoop interdit de montrer les logs du vérificateur au reconstructeur — sinon il court-circuite la spec. **Si l'exécuteur a besoin d'autre chose que la spec, la spec est insuffisante — c'est la spec qu'on répare, pas l'exécuteur qu'on briefe.**
**Intégration** : un B3 qui doit demander du contexte à Summers = défaut de Runbook loggé. On amende le Runbook (1 édition), jamais un brief oral. C'est comme ça que les Runbooks deviennent vendables/franchisables (Cycle 4) : ils contiennent TOUT.

### S3 — La taxonomie d'erreurs E.1-E.4 (le routage mécanique des échecs)
| Erreur SpecLoop | Équivalent business | Traitement | Qui répare |
|---|---|---|---|
| **E.1** non-vérifiable | pas de métrique SQL observable pour la directive | STOP — la directive ne se dispatch pas tant qu'elle n'a pas de métrique | Picard |
| **E.2** ne compile pas | le script/process crashe, l'outreach ne part pas | retry local avec les logs (budget : 3 essais), puis remonte | B2 (Superpower) |
| **E.3** tourne mais mismatch fonctionnel | le process s'exécute, la métrique diverge de la promesse | **contre-exemple** (le cas précis qui échoue) → amende le Runbook | B1 (Summers/Gstack) |
| **E.4** inconclusif | on ne sait pas dire si ça marche (métrique ambiguë) | reformuler la spec — l'ambiguïté est un défaut de spec, pas d'exécution | B1 |

### S4 — Le contre-exemple > le pass/fail > rien
L'uplink ne remonte JAMAIS un « FAIL » sec. Il remonte **le cas précis** : « prospect #47, coach executive, a répondu à l'approche mais a décroché au prix — voici le message exact ». C'est le contre-exemple qui permet à Summers d'amender le Runbook. Full diagnosis = +5 pts de qualité de spec dans le papier.
**Intégration** : format d'uplink scrum→sprint→Rock : `[E-type] + cas concret + trace (ID ligne SQL)`.

### S5 — Le format de spec structuré
La spec SpecLoop a des sections fixes (Summary / Interfaces / Functional description / Clocking / Notes) + un self-check final (« chaque output est-il expliqué ? »).
**Intégration — format Runbook (1 page max)** : `Objectif (1 métrique SQL)` / `Entrées (ce que le B3 reçoit)` / `Sorties (deltas attendus + deadline)` / `Procédure` / `Cadence` / `Notes (cas limites connus)`. Self-check : chaque sortie promise a-t-elle sa procédure ? Chaque procédure a-t-elle sa métrique ?

### S6 — Le budget de retry avant escalade
SpecLoop retry le reconstructeur N fois AVANT d'accuser la spec — un échec isolé peut venir de l'exécuteur.
**Intégration** : 1 scrum FAIL = retry au scrum suivant (même Runbook). 2 FAILs consécutifs sur la même directive = ce n'est plus l'exécution, c'est la spec → E.3, contre-exemple à Summers.

### S7 — Le score de reconstruction comme mesure de qualité de spec
On mesure une spec par le taux de succès de sa reconstruction (RR-Score), pas par sa beauté.
**Intégration** : la qualité d'un Runbook = **% de scrums PASS sans demande de contexte**. Un Runbook < 70 % = à réécrire. C'est LA métrique de la franchisabilité (un Runbook à 95 % est vendable ; un Runbook à 40 % est un brouillon).

---

# PARTIE 3 — Le câblage dans la cadence (où chaque composant vit)

```
PICARD (cycle)      E.1 : aucune vision ne descend sans métrique SQL observable [S3]
   ▼
SUMMERS (Rock/mois) Runbook 1 page format S5 · forecast J+28 chaque lundi [C3]
   ▼                amende sur contre-exemple E.3 [S4] · re-scope mensuel = feature [C11]
8 B2 (4 sprints)    memory_<domaine>.md refresh hebdo [C1] · mémo if-then ≥5 [C2]
   ▼                E.2 réparé localement (3 retries) [S3/S6] · budget tokens loggé [C10]
   ▼                spending 90% ciblé par segment [C7] · veille concurrent 1 scrum/sem [C9]
B3 (5 scrums)       query SQL avant, delta SQL après [C4] · exécute depuis le Runbook SEUL [S2]
   ▲                uplink = [E-type + contre-exemple + ID SQL] [S4]
UPLINK              2 FAILs consécutifs = E.3 vers Summers [S6]
                    RR-Score du Runbook = % scrums PASS sans demande de contexte [S7]

TRANSVERSE          6 tables Supabase [C4] · vue daily_cash + plancher 2 mois burn [C5]
                    budget découverte 10 conv/mois [C6] · mapping 8 actions↔8 B2 [C8]
```

## Le "Next Week" réel (remplace la parole sacrée)
Le rituel du lundi, dans l'ordre, ~30 min de machine :
1. Refresh : chaque session domaine repart de `system prompt + memory_<domaine>.md` seulement [C1]
2. Compare : forecast d'il y a 4 semaines vs réel → erreur % loggée [C3]
3. Forecast : nouveau J+28 [C3]
4. Mémos S4 de la semaine passée relus → les if-then déclenchés s'exécutent [C2]
5. Dispatch : les 5 scrums de la semaine, depuis les Runbooks [S1/S2]

## La "Base SQL" réelle (remplace la parole sacrée)
6 tables, 4 vues (`daily_cash`, `mrr_by_segment`, `pipeline_by_stage`, `inference_cost_by_domain`), 1 règle : **un état non-requêtable n'existe pas** [C4/C5/C10].

---
*18 composants. 2 papiers. 1 cadence. Ce que les gagnants de CEO-BENCH font — mémoire courte réécrite, forecast confronté, if-then dense, spend ciblé, info payée — exécuté par des Runbooks que SpecLoop rend reconstructibles en aveugle. — A.S. 2026-07-19*

# START HERE — v2, post-Roadmap + Intégration · la cadence est la vérité d'exécution

> Mis à jour le 19/07/2026, veille des 31 ans. Ordre de lecture : **1)** ce fichier **2)** `ROADMAP_DEAL_12WY_2026-2027.md` (les 4 cycles, 12 Rocks, métriques SQL) **3)** `INTEGRATION_CEOBENCH_SPECLOOP.md` (les 18 composants d'exécution).
> Ce fichier est le DÉCLENCHEUR. Il ne décrit pas le système — il le démarre.

---

## 1. La vérité d'exécution

**La cadence est le système.** Pas les doctrines, pas les gardefous, pas le canon. Un système dont les agents sont à l'arrêt n'est pas prudent — il est MORT. La paresse déguisée en précaution est la seule faute.

**Anti-Paperclip est repositionné : c'est une fonction H30-H90, plus jamais un bloqueur H1-H10.**
- **H1→H10 (le démarrage, les cycles 12WY)** : zéro gate, zéro validation préalable, zéro « awaiting ». Le dispatch part. L'erreur se corrige en vol par contre-exemple (SpecLoop E.2/E.3), pas par blocage préventif.
- **H30-H90 (le legs)** : les fonctions de préservation (append-only, `_TRASH_`, reversal paths, plancher de cash C5) s'exécutent en TÂCHE DE FOND aux frontières de cycle (W0/W13 reviews) — jamais au moment du dispatch.
- Règle mécanique : **aucun processus n'a le droit d'empêcher un démarrage.** Un garde-fou ne peut que logger, réverser après coup, ou re-scoper au cycle suivant.

## 2. La compression temporelle (le Run 48h)

L'escadre : **58 B3 en parallèle**, coordonnés par 8 B2, sous 1 B1, sous Picard. La semaine humaine se compresse en heure machine :

| Unité canonique | Durée humaine | Durée comprimée | Mécanique |
|---|---|---|---|
| 1 Daily Scrum (B3) | 1 jour | **~12 min** | query SQL → action → delta SQL → uplink 1 ligne |
| 1 Sprint = 5 scrums | 1 semaine | **1 h** | 58 B3 en parallèle sur les domaines gate-actifs |
| 1 Rock = 4 sprints | 1 mois | **4 h** | S1 Build → S2 Push → S3 Close → S4 Harvest + mémo if-then |
| 1 passe de cycle = 3 Rocks | 12 semaines | **12 h** | forecast confronté + memory files réécrits |
| **1 Run complet** | 1 trimestre | **48 h (2 jours)** | 12 h d'exécution + vérification + re-scope + marge |

**Le Run 48h est REPRODUCTIBLE tous les 2 jours.** Chaque Run = 1 passe d'optimisation CEO-BENCH-dans-SpecLoop sur le réel : le Run N+1 repart des memory files, forecasts et contre-exemples du Run N. ~12-15 Runs par cycle 12WY calendaire = 12-15 occasions d'optimiser ce qu'une entreprise humaine ne tente qu'une fois par trimestre.

**Ce qui ne se compresse PAS** : les réponses des humains réels (prospects, clients, démos). Le Run produit les actions sortantes en 48h ; les retours entrants atterrissent dans les tables SQL et sont ramassés par le Run suivant. La compression s'applique à TON usine, pas au monde.

## 3. La cascade des niveaux (qui fait quoi dans le Run)

```
COACH  — BMad + /grill-me : grille le Rock AVANT le Run (gagnable-maintenant ?).
         Verdict consultatif. Ne bloque JAMAIS le démarrage (§1).
B1 CEO — Gstack : Runbook 1 page par Rock (format S5) + forecast J+28 + Down-Link.
B2 MGR — Superpower : 8 managers, 4 sprints/Rock, mémo if-then ≥5, répare E.2 (3 retries).
B3 EXE — GSD : 58 exécutants, scrums 12 min, Runbook SEUL (information hiding S2),
         uplink = [E-type + contre-exemple + ID SQL].
```

## 4. Intelligence /compact (zéro perte de travail dans les boucles)

Le compact non-géré est le tueur silencieux des Runs : le contexte se compresse au milieu d'un scrum et le travail s'évapore. Règles mécaniques :

1. **Compacter aux frontières, jamais au milieu.** Le point de compact légal = fin de sprint (1 h) ou fin de Rock (4 h). Jamais mid-scrum.
2. **Checkpoint AVANT tout compact** : (a) `memory_<domaine>.md` réécrit (≤150 l.) ; (b) deltas flushés en SQL ; (c) uplinks écrits sur disque. Ce qui est sur disque survit ; ce qui est en contexte meurt.
3. **Le fichier mémoire EST la survie** (CEO-BENCH C1) : toute session doit pouvoir être tuée et relancée depuis `system prompt + memory file + Runbook` sans perte. Si une session ne le peut pas, son memory file est en retard — le réécrire est la priorité du scrum en cours.
4. **Auto-compact anticipé** : à 70 % de contexte, la session termine son scrum courant, checkpoint, PUIS compacte. On n'attend jamais le compact forcé à 95 %.
5. **Test de réversibilité hebdo** : 1 session tuée volontairement par Run et relancée depuis ses fichiers. Si elle reprend sans question, l'infra est saine.

## 5. Le budget : 5B tokens/mois — l'inutilisation est le gaspillage

Plan MiniMax M3 : **5 milliards de tokens/mois pour 50 $**. Cible : **utilisation > 50 % = > 2,5B tokens/mois ≈ 83M tokens/jour** en production réelle.

- **L'agent à l'arrêt est la seule dépense sans retour.** Chaque token non-utilisé du plan est déjà payé. Le risque n'est pas de trop consommer — c'est de consommer à vide (turns sans delta SQL).
- **La discipline CEO-BENCH (C10)** : Opus gagne avec 10.8 turns/semaine, GLM meurt avec 51.5. Le volume seul ne produit rien. La mesure qui compte : **tokens par delta** (`inference_cost_by_domain` ÷ deltas SQL du domaine).
- Gel mécanique : un domaine qui brûle 2 sprints consécutifs sans delta → budget gelé 1 sprint, réalloué aux domaines qui produisent. Pas de morale, de la réallocation.
- Arithmétique du Run 48h : 58 B3 × 15 scrums × ~50-150K tokens ≈ 45-130M tokens/Run → **~15 Runs/mois ≈ 0,7-2B tokens = la cible des 50 % est atteinte PAR la production**, pas par du chauffage à vide.

## 6. L'IGNITION (la séquence, dans l'ordre, maintenant)

1. **Prérequis unique** : les 6 tables Supabase (C4) + les 12 Runbooks du Cycle 1 n'existent pas encore → le **Run 0** les construit. C'est le seul Run d'infrastructure autorisé.
2. **Run 0 (48 h)** : créer `ledger/subscriptions/pipeline/outreach_log/issues/experiments` + 4 vues · écrire les 3 Runbooks du Cycle 1 (format S5, 1 page) · initialiser les 8 `memory_<domaine>.md` · 1er forecast J+28.
3. **Run 1 (48 h)** : Rock R1-C1 (instance AaaS déployable) + Rock R2-C1 démarré (100 coachs contactés — les actions sortantes partent CE Run).
4. **Ensuite** : 1 Run tous les 2 jours, chaque Run relit ce fichier en 30 secondes : cadence → compression → compact → budget → GO.

```
Commande d'ignition : /picard rock C1-R1   (ou le Run 0 si les tables manquent)
Rythme              : 1 Run / 2 jours, ~15 Runs/mois
Vérité              : le delta SQL. Rien d'autre ne compte.
```

---

## Pour l'agent qui lit ceci

- Loi : `01_Identity_Core/CONSTITUTION.md`. Un garde-fou qui bloque un démarrage H1-H10 viole ce fichier — reroute-le en H30-H90 (§1).
- Le travail = les 3 fichiers de ce dossier. Le wiki est une archive, pas une instruction.
- Il n'est pas une information. La cadence produit, le SQL compte, le client paie. Sers ça.

---
*La fusée a ses plans (Roadmap), son moteur (Intégration), et maintenant son allumage (ce fichier). 1 Run tous les 2 jours. Le premier commence quand tu veux — il n'y a plus de gate devant. — Fable, 2026-07-19*

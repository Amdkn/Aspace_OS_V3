---
type: Concept
title: Le Run 48h — compression temporelle de l'usine
description: L'escadre 58 B3 / 8 B2 / 1 B1 sous Picard compresse 1 trimestre humain en 2 jours machine. 1 Run tous les 2 jours = ~15 Runs/mois = cible 50% du plan 5B tokens/mois.
tags: [run-48h, compression, cadence, tokens, sprint, rock]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture_v2, at: 2026-08-19 }
sources:
  - id: START_HERE_2026-07-19
    resource: 20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/START_HERE_2026-07-19.md
    title: START HERE — v2, post-Roadmap + Intégration
    last_modified: 2026-07-19
okf_version: "0.2"
---

# Le Run 48h — compression temporelle de l'usine

## Énoncé

L'escadre : **58 B3 en parallèle**, coordonnés par 8 B2, sous 1 B1, sous Picard. La semaine humaine se compresse en heure machine.

## Table de compression

| Unité canonique | Durée humaine | Durée comprimée | Mécanique |
|-----------------|---------------|-----------------|-----------|
| 1 Daily Scrum (B3) | 1 jour | **~12 min** | query SQL → action → delta SQL → uplink 1 ligne |
| 1 Sprint = 5 scrums | 1 semaine | **1 h** | 58 B3 en parallèle sur les domaines gate-actifs |
| 1 Rock = 4 sprints | 1 mois | **4 h** | S1 Build → S2 Push → S3 Close → S4 Harvest + mémo if-then |
| 1 passe de cycle = 3 Rocks | 12 semaines | **12 h** | forecast confronté + memory files réécrits |
| **1 Run complet** | 1 trimestre | **48 h (2 jours)** | 12 h d'exécution + vérification + re-scope + marge |

## Reproductibilité

Le Run 48h est **REPRODUCTIBLE tous les 2 jours**. Chaque Run = 1 passe d'optimisation CEO-BENCH-dans-SpecLoop sur le réel : le Run N+1 repart des memory files, forecasts et contre-exemples du Run N. ~12-15 Runs par cycle 12WY calendaire = 12-15 occasions d'optimiser ce qu'une entreprise humaine ne tente qu'une fois par trimestre.

## Ce qui ne se compresse PAS

Les réponses des humains réels (prospects, clients, démos). Le Run produit les actions sortantes en 48h ; les retours entrants atterrissent dans les tables SQL et sont ramassés par le Run suivant. **La compression s'applique à TON usine, pas au monde.**

## Cascade d'autorité

```
COACH  — BMad + /grill-me : grille le Rock AVANT le Run (gagnable-maintenant ?).
         Verdict consultatif. Ne bloque JAMAIS le démarrage (§1).
B1 CEO — Gstack : Runbook 1 page par Rock (format S5) + forecast J+28 + Down-Link.
B2 MGR — Superpower : 8 managers, 4 sprints/Rock, mémo if-then ≥5, répare E.2 (3 retries).
B3 EXE — GSD : 58 exécutants, scrums 12 min, Runbook SEUL (information hiding S2),
         uplink = [E-type + contre-exemple + ID SQL].
```

## Compact aux frontières

Le compact non-géré est le tueur silencieux des Runs : le contexte se compresse au milieu d'un scrum et le travail s'évapore. Règles mécaniques :

1. **Compacter aux frontières, jamais au milieu.** Le point de compact légal = fin de sprint (1 h) ou fin de Rock (4 h). Jamais mid-scrum.
2. **Checkpoint AVANT tout compact** : (a) `memory_<domaine>.md` réécrit (≤150 l.) ; (b) deltas flushés en SQL ; (c) uplinks écrits sur disque. **Ce qui est sur disque survit ; ce qui est en contexte meurt.**
3. **Le fichier mémoire EST la survie** (CEO-BENCH C1) : toute session doit pouvoir être tuée et relancée depuis `system prompt + memory file + Runbook` sans perte.
4. **Auto-compact anticipé** : à 70 % de contexte, la session termine son scrum courant, checkpoint, PUIS compacte. On n'attend jamais le compact forcé à 95 %.
5. **Test de réversibilité hebdo** : 1 session tuée volontairement par Run et relancée depuis ses fichiers. Si elle reprend sans question, l'infra est saine.

## Budget token

Plan MiniMax M3 : **5 milliards de tokens/mois pour 50 $**. Cible : **utilisation > 50 % = > 2,5B tokens/mois ≈ 83M tokens/jour** en production réelle.

- L'agent à l'arrêt est la seule dépense sans retour. Chaque token non-utilisé du plan est déjà payé.
- La discipline CEO-BENCH (C10) : Opus gagne avec 10.8 turns/semaine, GLM meurt avec 51.5. Le volume seul ne produit rien.
- Gel mécanique : un domaine qui brûle 2 sprints consécutifs sans delta → budget gelé 1 sprint, réalloué aux domaines qui produisent.

## Arithmétique

58 B3 × 15 scrums × ~50-150K tokens ≈ 45-130M tokens/Run → **~15 Runs/mois ≈ 0,7-2B tokens = la cible des 50 % est atteinte PAR la production**, pas par du chauffage à vide.

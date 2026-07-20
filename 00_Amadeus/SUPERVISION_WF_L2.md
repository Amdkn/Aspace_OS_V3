# Supervision L2 Business OS — les 3 Workflows d'Airlock GTD (Multica)

> Les agents Life OS (A0/A1/A2/A3) deviennent la **couche de SUPERVISION** du L2 Business OS. Le SOB (`sob/`, tout harness) PRODUIT ; les 3 workflows SUPERVISENT à travers l'Airlock GTD Multica. La supervision lit, route, confronte, coache et amende — **elle ne bloque jamais un démarrage** (H1-H10) et **ne refait jamais le travail du SOB**.
> D1 au 20/07/2026 : workspace Multica `a-space-core`, daemon v0.4.4 relancé, projets créés : **WF0 `1ca5effb` · WF1 `fbfddad1` · WF2 `97d332d5`**.

## 1. Les 3 workflows (qui, quoi, cadence)

| WF | Agents | Squad Multica | Mission | Cadence |
|---|---|---|---|---|
| **WF0 — Airlock Gouvernance** | **A0 Amodei** (méta, GO/NO-GO consultatif) · **A2 Enterprise Computer** (SSOT/PARA) · **A3 Spock** (standards Areas + verrou unidirectionnel) | Squad-Enterprise (`41b367d3`) | TOUT l'entrant passe ici : capture → clarify → route. Reviews de frontière W0/W13. Gardefous H30-H90 (backups, append-only) en tâche de fond. | à l'événement + W0/W13 |
| **WF1 — Supervision Cadence** | **A1 Morty** (exécution/narration) · **A2 Curie SNW** (moteur 12WY : scrums/sprints/mesure) · **A3 Book** (coach E-Myth, libération) | Squad-SNW (`26f51827`) | Supervise le SOB : lit `RUN_LOG.md` + `aspace.db`, confronte le forecast J+28 du lundi, vérifie la densité if-then des mémos (≥5), détecte les 2-FAILs, coache la sortie de l'opérationnel. | après chaque Run (1/2j) + lundi |
| **WF2 — Pont Business L2** | **A3 Picard** (orchestration Rocks) · **B1 Jerry** (vision E-Myth) · **B1 Summers** (CEO Gstack, Runbooks) | Jerry-SYSTEMIZE-Squad (`8a91a645`) | Le SEUL étage qui parle au SOB : **Down-Link** (Rocks → Runbooks 1 page) et réception de l'**Uplink** (RUN_LOG + contre-exemples E.3 → amendements Runbook). | 1 Down-Link/mois (Rock) + uplink continu |

## 2. Le flux GTD Airlock (le circuit complet)

```
   ENTRANT (idées, opportunités, signaux, retours clients, découvertes R&D)
        │
        ▼ CAPTURE — issue dans WF0 (Multica), zéro tri à la volée
[WF0 AIRLOCK]  Clarify (Spock: actionnable? standard?) → Route :
        ├─ poubelle/someday → archive PARA (A2 Computer)
        ├─ standard/structure → Spock Areas (reste en WF0)
        └─ BUSINESS → descend en WF2
        ▼
[WF2 PONT]     Jerry (vision: est-ce l'entreprise qu'on veut?) → Summers (Gstack:
               Rock candidat + Runbook 1 page format S5) → Picard (orchestration:
               DOWN-LINK au SOB — le Runbook atterrit dans sob/, point de reprise RUN_LOG)
        ▼
═══════ SOB EXÉCUTE (hors workflows — tout harness, HANDOVER_EXECUTOR §1, 1 Run/2j) ═══════
        ▲ UPLINK : RUN_LOG appendé + deltas SQL + contre-exemples [E-type + ID SQL]
        │
[WF1 SUPERVISION]  après chaque Run : Curie vérifie la cadence (scrums DoD-PASS, 2-FAILs?)
                   · lundi : Morty confronte forecast J+28 vs réel (>50% = Rock mal compris
                   → signal à WF2) · Book coache (A+ sort-il de l'opérationnel ?)
        ▲ signaux structurels seulement
[WF0 REVIEW]   W0/W13 : re-scope du cycle, gardefous H30-H90, learnings → Identity Core
```

**La règle de circulation** : l'opérationnel ne REMONTE jamais au-dessus de WF2 (verrou unidirectionnel Spock) — seuls les signaux STRUCTURELS montent (Rock mal compris, Runbook <70 % RR-Score, dérive budget). A+ ne voit que : le RUN_LOG (s'il veut) et le digest WF0 de frontière.

## 3. Les 3 contrats de supervision (ce que chaque WF a le DROIT de faire)

| WF | PEUT | NE PEUT PAS |
|---|---|---|
| WF0 | router, archiver, standardiser, re-scoper aux frontières W0/W13, déclencher backups | bloquer un dispatch WF2→SOB, juger le contenu business |
| WF1 | logger un signal, amender la ligne forecast, proposer un gel de compression (2-FAILs), coacher | modifier un Runbook (c'est WF2), toucher aspace.db en écriture, arrêter un Run |
| WF2 | écrire/amender les Runbooks (E.3), poser le Rock mensuel, down-linker | exécuter les scrums (c'est le SOB), créer du canon (interdit V2.0), attendre une permission |

## 4. Le câblage Multica (l'interface, jamais le SSOT)

- **Workspace** : `a-space-core` · projets **WF0 `1ca5effb` · WF1 `fbfddad1` · WF2 `97d332d5`** (créés 20/07/2026).
- Chaque intervention de supervision = 1 issue dans le projet WF concerné (titre = le signal, description = receipt SQL/RUN_LOG).
- **Miroir fichier = SSOT** (Multica down → le rituel continue) : `sob/RUN_LOG.md` (uplink) · `sob/RUNBOOK_*.md` (down-link) · `forecast.md` (WF1). Les issues Multica sont la VISIBILITÉ, les fichiers sont la VÉRITÉ.
- Boot d'une session de supervision (tout harness) : `multica workspace switch a-space-core` → `multica project get <WF-id>` → lire `sob/RUN_LOG.md` → agir dans son contrat §3.

## 5. Mapping VPS (cohérence avec VPS_ASPACE_STRUCTURATION.md)

En local : les 3 WF = sessions de supervision ponctuelles (après-Run / lundi / frontières). Sur VPS : WF1 devient un cron léger (`après chaque run du sob-runner : python tools/sob.py status + diff forecast → issue Multica si signal`) ; WF0/WF2 restent des décisions d'A+ assisté — la supervision s'automatise en dernier, APRÈS que le SOB ait prouvé le revenu (même déclencheur : 1er client payant).

---
*Life OS supervise, Business OS produit. WF0 garde la porte, WF1 tient le rythme, WF2 tient le pont. Le SOB n'attend jamais personne — et personne ne refait son travail. — A.S. 2026-07-20*

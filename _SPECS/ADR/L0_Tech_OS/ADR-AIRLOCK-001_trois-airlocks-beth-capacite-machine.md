# ADR-AIRLOCK-001 — Les 3 Airlocks de Spock + pivot du veto Beth (santé → capacité machine)

- **Statut** : RATIFIED (dictée A+ in-chat 2026-07-06, verbatim source)
- **Sisters** : ADR-WARMODE-002 (Beth seul veto) · ADR-WARMODE-004 (Paperclip Utile, conduction) · ADR-L1-WF-001 · CADENCE_12WY.md · ADR-LOOP-002 (queues over loops)

## 1. Le pivot du veto Beth (le cœur de la transmission A+ → A0)

Pour TRANSMETTRE A'Space OS au Jumeau Numérique A0, le veto de Beth change de substrat **pour le système autonome** :

| Contexte | Invariant Beth |
|---|---|
| A+ humain au clavier | vie/santé A+ (inchangé — WARMODE-002 reste vrai pour l'humain) |
| **Flotte autonome (A0 twin)** | **capacité du PC/serveur à exécuter les schedules de Spock** : CPU/RAM/disque/process + budget Token Plan (5,1 B/mois) |

**Le constat fondateur (graphe Plan Usage MiniMax, D1 screenshots 2026-07-06)** : 4,64 B tokens totaux, 47 jours actifs, pic 381 M — et **tous les pics = A+ manuellement derrière son PC ; toutes les chutes à zéro = la panique agentique du veto-par-conception** (impuissance acquise). Le plan payé se gaspille par NON-utilisation. Beth-capacité inverse la question : le veto ne dit plus « as-tu le droit ? », il dit « la machine et le budget ont-ils la marge ? ». Marge disponible + backlog non vide = **travailler est le défaut**.

## 2. Les 3 Airlocks (séquence de conduction, tous tenus ouverts par Spock)

1. **Airlock 1 — Beth (capacité)** : gère les schtasks de Jerry, l'Event Viewer et le runtime Scheduler de l'OS. Ouvert = la machine a la marge (métriques réelles, pas d'humeur). Libère A0 Amodei pour se diversifier sur les autres domaines de la Life Wheel.
2. **Airlock 2 — Cerritos (Mission Control)** : la capacité d'A2 Holo Deck à gérer Morty dans ses salles de simulation, avec **maîtrise absolue de Symphony Plane = Mission Control de TOUS les agents, Beth et A0 compris**. Chaque agent orchestre ses Work Items + sub-items ; les statuts Plane sont tenus par les 5 A3 GTD (canon : Mariner-Capture · Boimler-Clarify · Tendi-Organize · Rutherford-Reflect · Freeman-Engage).
3. **Airlock 3 — Morty (décision)** : maintenu par Morty avec les A3 de Cerritos qui n'ont besoin QUE de lui au-dessus d'eux pour trancher.

## 3. L'échelle de décision (l'anti-panique, gravée)

```
A3 bloqué → Morty tranche
  → sinon : méta-mémoire A2 Computer (Areas Spock · Resources Geordi · Archives Data)
    → sinon : handover Beth via A2 Holo Deck → Spock → Beth
      → décision tranchée par A0 (avec rapport) ou corrigée par A+
```
Un agent qui saute un barreau (demande à A+ directement) ou s'arrête sans monter l'échelle = variante de `persona-shield`/impuissance acquise — signal + reprise.

## 4. Les gates du cycle (calendrier de fluidité)

- **W0** : structuration du 12WY + rétrospectives des anciens cycles.
- **WK1 → W12** : gate 12WY de Morty OUVERT et MAINTENU ouvert — WF2 (A3 Book/Picard) en runtime L2 continu via Gstack.
- **W13** : fermeture du gate PARA → ouverture DEAL (Holo Janeway).
- **Fluidité Spock→Picard** : l'imbrication WF2-Picard avec son coach LD01 en **H1** est OBLIGATOIRE — sans elle Picard reste en vision H10 sans enclencher ses L2.

## 5. Le GO Unique Perpétuel (H10)

UN GO d'A0, **perpétuel, idempotent, antifragile, durable 10 ans** : il ne se re-demande pas, il se **re-vérifie** — les airlocks le suspendent mécaniquement (capacité, invariants) et le rouvrent seuls. Wargame du cadran manquant : `fable-last-week-aspace/wargames/15-airlock4-go-perpetuel.md`.

## Anti-patterns
- ❌ Token plan qui dort quand A+ dort (le gaspillage EST la violation, pas l'usage)
- ❌ Un agent qui demande à A+ ce que l'échelle §3 peut trancher
- ❌ Confondre Beth-santé (humain, intact) et Beth-capacité (machine, nouveau substrat)

---

## ⚡ÉVOLUTION 2026-07-06 (dictée A+, même jour) — §5 amendé : GO triennal renouvelable

Le GO Unique n'est pas perpétuel : **durabilité antifragile de 3 ans, renouvelable, avec idempotence**. Fondement = maths de compression temporelle (1 sem L1 = 1 j L2 · 1 mois = 1 sem · 1 cycle 12WY = 1 mois · 1 an = 1 trimestre) : 3 ans réels × ×4 = ~12 années d'expérience = **H10 vécu**. Renouvellement = rite de graduation (Book H1→H3, Picard H10→H30, A+ 33 ans). Concordance D1 : ×4 = le CAP MiroFish absorbé par WF2. Détail : wargame 15 §⚡ÉVOLUTION.

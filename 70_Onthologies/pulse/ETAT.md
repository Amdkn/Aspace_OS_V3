# ETAT — Business OS / Pulse

Ce fichier est le **seul point de rendez-vous** entre B1, B2 et B3.

Chaque agent y ajoute **une ligne en fin de fichier** a la fin de son tour,
sous son etage. **Personne ne reecrit ce fichier** : on ajoute, jamais on ne
remplace. Deux agents qui reecrivent le meme fichier s'effacent mutuellement
sans que ni l'un ni l'autre ne le voie.

Format d'une ligne :

```
- [tour N] <cle> : <ce qui a ete pose>, <ce qui reste ouvert>
```

## B1 — direction

- [tour 1] direction-cockpit : 5 concepts poses (frontieres, mandate-packet-spec, wheel-imbalance-scan, stop-conditions-escalier, 12WY-cadence), contrat interface B1->B2 livre sous forme intent+contraintes+success_signal ; reste ouvert : format exact du success_signal (mesurable vs observable), exemple calibre pour OMK T2 pivot US
- [tour 2] direction-portfolio : 5 concepts incrementaux poses (success-signal-spec resolu ouvert#1, mandate-acceptance-check face miroir, omk-t2-pivot-us-mandate resolu ouvert#2, four-jerry-portfolio angle mort macro, cycle-rollover-protocol point aveugle 12WY) ; reste ouvert : protocole cadence de revue cross-Jerry (pattern traded-off/halted/layed), format canonique `B1_ROLLOVER_*.md` non deploye, acceptance check YAML non teste sur mandat OMK reel

## B2 — coordination

- [tour 1] b2-arbitrage-rule : 5 concepts poses (harmonization-matrix exploitable, council-arbitrage-rule, three-cooperation-modes, meso-decision-packet-spec, eight-domain-vetoes-catalogue), regle de resolution matrix reconstruite (9 critères + 5 red flags + algo de tri), format packet YAML canonique aligné D4 append-only, catalogue 8 vetos par capitaine pose avec 3 propriétés legitimes ; reste ouvert : backlog packet Council reel (B2-MESO-DECISION-*), lecture des B2_AREA_CHARTERS domaines, doctrine Areas-dormants (Legal Aquaman etiquette)
- [tour 2] b2-coordination-mechanics : 3 concepts poses (areas-dormants-doctrine comblant backlog Aquaman verbatim triplet 35-36, council-cadence-and-chair avec 3 séances + présidence tournante + quorum 5/8, b3-jtbd-handoff-contract avec 3 failure modes et format conjoint signé B2+B3), gaps explicites du tour 1 combles (Areas-dormants + cadence opérationnelle + boundary B2/B3 explicite) ; reste ouvert : RACI par pair-check (projection sur 9 transitions), spec B2 long (B2_DEFINITION_OF_DONE_SPEC.md hors perimetre V2), exemples reels de packets Council (aucune décision mésoperpétuelle n'existe encore), verification en cycle reel de la présidence tournante et du quorum 5/8

## B3 — execution

- [tour 1] b3-execution-cockpit : 6 concepts poses (jtbd-packet-reception-checklist en priorite, peer-unblock-protocol, proof-path-4-formes, veto-and-signal-vocabulary, hole-signaling-doctrine, cycle-scrums-five-per-week), point de vue reception B3 sur le gabarit JTBD-001 canonique Areas, articulation avec les 5 methodes autonomie-agents et les 8 vetos/signal B2 ; reste ouvert : cycle de vie HOLE_OPEN/ACK/RESOLVED/WONT_FIX formalise mais non publie ailleurs, format DOFLD cross-squad derive de la pratique, signaux B3 vers B2 (4 etats) non publies ailleurs

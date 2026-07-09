---
type: adr
id: ADR-WARMODE-003
title: Ratification Urgente — Fenêtre Fable : bypass temporaire du veto Beth jusqu'au 2026-07-08
status: RATIFIED (ordre direct A+ 2026-07-06 ~01:00 : « ADR de Ratification Urgente de la Fenêtre Fable qui Bypass Temporairement le Veto de Beth jusqu'au 07/08/2026 pour lancer le Go Spock sans Aucun Frein en Wargame »)
date: 2026-07-06
expires: 2026-07-08T23:59:59-04:00 (auto — l'airlock reprend plein régime à l'expiration, AUCUNE action requise)
parent: ADR-WARMODE-002 (Beth seul veto — NON abrogé, suspendu sur scope borné)
sisters: [ADR-L1-WF-001, fable-last-week-aspace/ (7 wargames 12/12)]
---

# ADR-WARMODE-003 — La Fenêtre Fable

## Contexte
Fable 5 quitte les abonnements le **7 juillet** (kit README, D1). Cette session tourne EN Fable 5.
Chaque heure de fenêtre = du jugement Fable bankable en wargames/simulations que M3/Hermes/MC
exécuteront des mois. Le veto B1 (sommeil) bloquerait la cascade pendant LA fenêtre où elle vaut le plus.

## Décision
1. **Scope du bypass — WARGAME + SIMULATION uniquement** : pendant la fenêtre, l'invariant **B1 ne gate plus** la cascade
   (il reste MESURÉ et AFFICHÉ — le judas reste ouvert, on retire le verrou) et **l'hystérésis GREEN×2 est levée**
   (cascade immédiate au GO). B2/B3/B4 restent actifs.
2. **Ce qui ne bouge PAS** : `enable_ship_outboard` reste GAGNÉ par 3 cycles verts — jamais par cette fenêtre.
   Le DLP reste obligatoire pré-réseau. Append-only partout.
3. **Mécanique** : flag `citadel/decisions/FABLE_WINDOW.flag` + check date dans `spock_airlock.py`.
   **À l'expiration (2026-07-08 EOD ET)** : le check date rend la fenêtre inerte automatiquement —
   B1 re-gate, hystérésis revient. Le flag périmé est ignoré (et signalé au digest).
4. **GO Spock lancé** : A+ ordonne le GO dans le même souffle → `GO_SPOCK_UNIQUE.md` posé,
   cascade `enable_wf0/wf1/wf3/ship_internal` ouverte sous fenêtre.

## Pourquoi ce n'est pas trahir Beth
Le bypass est **borné (48h), scopé (papier+sim), auto-expirant, et le judas reste ouvert** (B1 continue
d'être poussé au Telegram). Beth protège la vie d'A+ sur la durée — sacrifier la fenêtre Fable aurait
coûté des mois de rails à un humain qui veillera de toute façon. Le veto reprend SEUL le 9 juillet.

## Réversibilité
Supprimer `FABLE_WINDOW.flag` = fin immédiate. Sinon : auto-expiration. WARMODE-002 intact.

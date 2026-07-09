---
name: stop-authority-protocol
version: 1.0
created: 2026-06-07
phase: OBSERVE (toutes phases)
actor: Culber (LD03) + Tilly (LD04) — A3 avec autorité STOP globale
authority: AGENTS.md (canon) + Life Wheel LD03/LD04 (santé + cognition)
---

# 09 — STOP Authority Protocol (Culber LD03 + Tilly LD04)

> **Culber** (LD03 Santé) et **Tilly** (LD04 Cognition) sont les **seuls A3**
> autorisés à émettre un STOP global. Ce pouvoir est non-négociable et
> contourne toute la chaîne A2↔A1.

## Domaines de STOP

### Culber — LD03 (Santé)

Émet `HALT_LD03` quand :
- Indicateur santé critique détecté (pouls, fatigue, blessure, etc.)
- Risque médical immédiat
- Épuisement professionnel (burnout > 7 jours)

**Effet** : tous les A3 crews LD03-touchable (sport, nutrition, sommeil) sont gelés. Seuls Culber + Discovery captain peuvent travailler LD03.

### Tilly — LD04 (Cognition)

Émet `HALT_LD04` quand :
- Surcharge cognitive détectée (> 8h deep work / jour)
- Décision critique sans contexte suffisant
- Conflit de décision (deux captains A2 exigent l'inverse)
- Apprentissage de mauvaise qualité (comprendre ≠ apprendre)

**Effet** : tous les A3 crews LD04-touchable (lecture, étude, decision-making) sont gelés. Seuls Tilly + Discovery captain peuvent travailler LD04.

## Procédure d'émission

```
1. Culber/Tilly détecte condition HALT
2. Émet `outbox/l1/YYYY-MM-DD/<id>-HALT_LD0X.json` :
   {
     "halt_id": "<uuid>",
     "authority": "Culber|Tilly",
     "domain": "LD03|LD04",
     "reason": "<short text>",
     "evidence": "<vital sign, decision log, etc.>",
     "issued_at": "<ISO 8601>",
     "valid_for_ms": 3600000  // 1h par défaut
   }
3. Beth (A1) reçoit et passe en HALT_LD0X (5-state)
4. Pulse.log écrit ligne avec agent_state = HALT_LD0X
5. Tous les A2 captains routent STOP à leurs crews
6. Reprise = A0 Amadeus (seul autorisé)
```

## Anti-circumvention

| Tentative | Anti-pattern | Antidote |
|---|---|---|
| A2 captain ignore HALT et route quand même | Shadow bypass | Beth (A1) log + escalade A0 |
| A3 crew dit "j'ai pas vu le HALT" | Plausible deniability | `outbox/` est append-only, pas de excuse |
| A1 Beth downgrade HALT vers ORANGE sans A0 | Authority usurpation | `HALT_*` → `ORANGE` requiert A0 sign-off |
| Culber émet HALT_LD04 (pas son domaine) | Domain confusion | Tilly est seule juge LD04, Culber seule LD03 |

## Reprise (recovery)

| Step | Acteur | Effet |
|---|---|---|
| 1. Condition originale levée | Culber/Tilly | Émet `recover.json` |
| 2. A0 Amadeus confirme reprise | A0 | Co-signe `recover.json` |
| 3. Beth (A1) repasse en ORANGE | A1 | 5 ticks ORANGE avant GREEN |
| 4. A2 captains reprennent routage | A2 | Scope réduit pendant 5 ticks |
| 5. A3 crews ré-engagés | A3 | Mode "warmed-up" 1 tick |

## Anti-patterns (récap)

- ❌ Tout agent ≠ Culber/Tilly qui émet HALT_* → usurpation
- ❌ HALT sans `evidence` → shadow HALT, refusé
- ❌ HALT > 24h sans review A0 → escalade forcée
- ❌ Reprise sans co-signature A0 → invalid

## Source canonique

- `AGENTS.md` (autorité STOP)
- `20_Life_OS/` Discovery LD03 (Culber) + LD04 (Tilly)
- Wiki : `concept_agent_capsule.md` (rôles canon)

---
id: bridge.A3_DLQ
layer: A3_DLQ_bridge
status: SHADOW_ACTIVE
created: 2026-06-07
lane: B_runtime
---

# Bridge A3 → Donna DLQ — Dead Letter Queue

> Les findings A3 rejetés par l'A2 ship vont en DLQ. Donna arbitre. Pas de hard delete.

## Trigger

Un A3 produit un finding qui :
- Contredit le canon du ship
- Est hors-périmètre (drift)
- Est incohérent avec un autre finding du même LD/domain
- Est rejeté par Beth (HALT_LD03/LD04, RED)

## Flow

```
A3 Crew
  ↓ finding rejected
DLQ (Donna Noble) — arbitre
  ↓ si réconciliable : réinjecte A2 ship
  ↓ si obsolète : archive avec raison
  ↓ si urgent : escalade Beth → A0
```

## Règle DLQ

- Pas de hard delete (doctrine `_TRASH`)
- Chaque entrée a : A3 source · reason · timestamp · reviewer (Donna/Beth/A0)
- Review hebdo Donna

## Anti-patterns

- ❌ A3 qui bypasse A2 et va directement à Donna
- ❌ Hard delete d'un finding rejeté
- ❌ Donna qui réinjecte sans review

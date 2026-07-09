# Shadow L0 — Symphony Cluster + Heartbeat Anti-Panique

**Date :** 2026-05-26
**Niveau :** L0 Tech OS
**Sources doctrinales :**
- `12_Blueprints/02-ADR/ADR-SYMPH-001_symphony-replaces-n8n.md`
- `12_Blueprints/02-ADR/ADR-SYMPH-002_symphony-variants-per-harness.md`
- `12_Blueprints/02-ADR/ADR-HEART-002_heartbeat-anti-panique-openclaw-paperclip.md`

## Trois ratifications simultanées (cluster A2)

### SYMPH-001 — Bus doctrine
- **N8N marqué LEGACY** au 2026-05-26. Substitut : Symphony pattern (files + Task Scheduler).
- Tick cycle canonique : `WAKE → PROBE → DECIDE → EXECUTE → OBSERVE → LEARN → SIGNAL → SLEEP`
- Interface inter-agent : JSON files `outbox/` ↔ `inbox/`. Pas de WebSocket / gRPC / Redis.
- Fallback chain quota-aware confirmée (cf. CLAUDE.md).

### SYMPH-002 — 6 variants harness
| Variant | Tick | Émet | Doctor | Provider |
|---------|------|------|--------|----------|
| Claude_Code_CLI | ✓ | ✓ | 11th | MiniMax |
| Codex_CLI | ✓ | ✓ | 13th | OpenAI |
| Gemini_CLI | ✓ | ✓ | 12th | Google |
| Antigravity_IDE | ✗ | ✗ | (console A0) | Google |
| Claude_Desktop_App | ✗ | ✗ | (console A0) | Anthropic |
| Codex_Desktop | ✗ | ✗ | (console A0) | OpenAI |

**Règle** : variants `_CLI` participent au bus ; `_IDE/_App/_Desktop` = consoles A0 (consomment, n'émettent pas, pas de tick auto).

### HEART-002 — Anti-panique gated
- 8 paniques SDD-001 mappées 1:1 sur les 8 phases tick → gardes anti-panique
- Read-After-Write (RAW) systémique pour tout write critique
- **OpenClaw réintroduit conditionnellement** (C1-C4 satisfaites) → amende SPEC.md
- **Paperclip réintroduit conditionnellement** (P1-P4 satisfaites)
- 3 modes : `lean` (défaut, OpenClaw+Paperclip OFF) | `bridged` (OpenClaw ON) | `full` (les deux ON)
- Donna DLQ refondue file-based (`donna_dlq/{pending,retried,failed}/`)
- Watchdog Yaz tick 5min always

## Tension doctrinale résolue

`Shadow_L0/SPEC.md` §1 disait : *"no OpenClaw gateway, no Paperclip Node process"*. A0 a explicitement demandé la possibilité de les réintroduire. HEART-002 amende SPEC.md : **autorisé sous conditions strictes vérifiées par Watchdog Yaz**. Mode `lean` reste défaut.

## État du mesh post-ratification

```
Mode: lean (par défaut — Shadow_L0/MODE.txt à créer)

Participants Symphony (tick auto) :
  ✓ Codex_CLI       (capsule existante, 13th Doctor)
  ✓ Gemini_CLI      (capsule existante, 12th Doctor)
  ✓ Claude_Code_CLI (capsule existante, 11th Doctor)

Consoles A0 (pas de tick, consomment seulement) :
  → Antigravity_IDE
  → Claude_Desktop_App
  → Codex_Desktop

Watchdog (à créer) :
  ⏳ Yaz_Watchdog (sweep 5min always)

Désactivés (mode lean) :
  ✗ OpenClaw_Gateway   (conditions C1-C4 not met yet)
  ✗ Paperclip_Budget   (conditions P1-P4 not met yet)
```

## Plan d'implémentation HEART-002 (référence ADR § Plan)

| Phase | Tâche | Durée | Bloquant ? |
|-------|-------|-------|------------|
| 0 | Créer `Shadow_L0/MODE.txt` avec "lean" | 1 min | Non |
| 1 | Coder `AntiPanicGuards.psm1` + intégrer heartbeat-tick.ps1 | 2h | Non (mesh fonctionne sans) |
| 2 | Refonte Donna DLQ file-based | 1h | Non (pas d'erreurs courantes en mode lean) |
| 3 | Capsule Yaz_Watchdog + Task Scheduler 5min | 1h | Non |
| 4 | Modes bridged/full | différé | sur demande A0 uniquement |

## Conséquences pour A0

- **Workflow A0** clarifié : utiliser Claude_Desktop_App pour décisions Opus/Sonnet stratégiques, Antigravity pour synthèse long contexte, Codex_Desktop pour code lourd supervisé. Aucun ne tourne en autonome — seuls les CLI le font.
- **Marina incident** (2026-05-25, Codex Desktop quota épuisé) — désormais doctrinalement attendu : un crash console A0 ne casse pas Symphony.

## Suivi

- Implémenter Phase 0-3 (au plus tôt, pas bloquant)
- Phase 4 (modes bridged/full) **différé** — pas avant que Phase 1 Notion Solaris ne soit verrouillée
- ADR-NOTION-001 peut maintenant **citer ADR-SYMPH-001 comme bus** sans note "à venir"

## Références

- ADR-SYMPH-001 / ADR-SYMPH-002 / ADR-HEART-002 (les 3 ratifiés ensemble)
- SDD-001 (anchor anti-panique)
- Shadow_L0/SPEC.md (amendé par HEART-002 §D3 + D4)
- ADR-NOTION-001 (premier consommateur Symphony)

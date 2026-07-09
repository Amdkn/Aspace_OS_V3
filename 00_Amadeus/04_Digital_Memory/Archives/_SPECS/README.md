# _SPECS : Source Unique de Vérité Architecturale

> **Canon absolu** : `aspace_a0_amadeus/00_Amadeus/01_Identity_Core/AGENTS.md`
> Tout spec doit s'aligner sur la hiérarchie définie dans AGENTS.md.
> Tout ADR doit citer le rôle agent concerné (A0/A1/A2/A3/Nano).

---

## Règle d'Or

**"Pas de code sans spec. Pas de spec sans ADR. Pas d'ADR sans ancrage dans AGENTS.md."**

- **A0 (Amadeus)** = Visionnaire. Il émet des Intentions. Il ne touche pas aux fichiers de config.
- **L0 (Rick)** = Infrastructure Invisible. No human maintenance. Il exécute les intentions.
- **Toute pollution technicien à la racine** = anomalie L0 à corriger, pas Amadeus.

---

## Structure

```
_SPECS/
├── README.md              ← Ce fichier — point d'entrée unique
├── 00_ADR/                ← Décisions d'Architecture (ACCEPTÉ = immuable)
│   ├── ADR-001_OpenClaw-Position.md          ← SUPERSÉDÉ partiellement par ADR-005
│   ├── ADR-002_Multiverse-Portability.md
│   ├── ADR-003_agents-registry.md
│   ├── ADR-004_doctrine-sync-canon.md
│   └── ADR-005_OpenClaw-Inside-Container.md  ← NOUVEAU
├── 01_V0_STATE/           ← Photo honnête de ce qui fonctionne MAINTENANT
│   └── V0_State_2026-02-28.md
├── 02_V1_PRD/             ← PRD alignés sur AGENTS.md (specs d'exécution)
│   ├── PRD-001_03_OpenClaw_Body_Cleanup.md   ← EXÉCUTÉ (Sprint 1)
│   ├── PRD-002_Sprint-Fondations.md          ← EXÉCUTÉ (Sprint 1)
│   ├── PRD-003_Container-Migration.md        ← EN ATTENTE (Sprint 2, Gemini)
│   └── PRD-004_00_Amadeus-Restructuration.md ← EN ATTENTE (Sprint 2, Gemini)
└── 03_ROADMAP/            ← Backlog et sprints
    └── BACKLOG.md
```

---

## ADR Actifs

| ID | Titre | Statut | Agent référent |
|----|-------|--------|---------------|
| [ADR-001](00_ADR/ADR-001_OpenClaw-Position.md) | Position d'OpenClaw (03_OpenClaw_Body = config only) | **SUPERSÉDÉ** par ADR-005 (partiellement) | Graham (L0/A3 — Driver/Bus) |
| [ADR-002](00_ADR/ADR-002_Multiverse-Portability.md) | Portabilité Multiverse — `aspace_a0_amadeus` comme Container Souverain | ACCEPTÉ | Rick (L0/A1 — Sovereignty) |
| [ADR-003](00_ADR/ADR-003_agents-registry.md) | agents_registry.json — Mapping Canon ↔ Runtime ↔ Config | ACCEPTÉ | Rick (L0/A1) + River (L0/A3 — Sync) |
| [ADR-004](00_ADR/ADR-004_doctrine-sync-canon.md) | doctrine_sync.sh → Pointer vers le vrai Canon | ACCEPTÉ | River (L0/A3 — Timekeeper) |
| [ADR-005](00_ADR/ADR-005_OpenClaw-Inside-Container.md) | OpenClaw à l'intérieur du Container `aspace_a0_amadeus` | ACCEPTÉ | Rick (L0/A1 — Sovereignty) |

---

## Entrée par Question

### "Je veux comprendre le rôle d'OpenClaw"
→ [ADR-001](00_ADR/ADR-001_OpenClaw-Position.md)

### "Je veux rendre A'Space portable sur WSL ou VPS"
→ [ADR-002](00_ADR/ADR-002_Multiverse-Portability.md)

### "Je veux trouver quel dossier Runtime correspond à quel fichier Canon"
→ [ADR-003](00_ADR/ADR-003_agents-registry.md)

### "Je veux corriger doctrine_sync.sh"
→ [ADR-004](00_ADR/ADR-004_doctrine-sync-canon.md)

### "Je veux nettoyer 03_OpenClaw_Body"
→ [PRD-001](02_V1_PRD/PRD-001_03_OpenClaw_Body_Cleanup.md) ← EXÉCUTÉ (Sprint 1)

### "Je veux déplacer OpenClaw dans le Container"
→ [ADR-005](00_ADR/ADR-005_OpenClaw-Inside-Container.md) + [PRD-003](02_V1_PRD/PRD-003_Container-Migration.md)

### "Je veux restructurer 00_Amadeus (5 couches + 3 instances)"
→ [PRD-004](02_V1_PRD/PRD-004_00_Amadeus-Restructuration.md)

### "Je veux connaître l'état V0 réel"
→ [V0 State 2026-02-28](01_V0_STATE/V0_State_2026-02-28.md)

### "Quoi faire en premier ?"
→ [BACKLOG](03_ROADMAP/BACKLOG.md) — Sprint Courant, P0 en haut

### "Je veux voir la hiérarchie complète des agents"
→ `aspace_a0_amadeus/00_Amadeus/01_Identity_Core/AGENTS.md` *(le canon)*

---

## Principes Anti-Fragilité

1. **Canon immuable** : `AGENTS.md` + les ADR ACCEPTÉS ne se modifient pas — on en crée de nouveaux
2. **Photo honnête** : `01_V0_STATE/` documente ce qui EST, pas ce qu'on voudrait
3. **Séparation des pouvoirs** : Identité (Canon) ≠ Runtime (state) ≠ Config (templates)
4. **Portabilité first** : Tout chemin dans `aspace_a0_amadeus/` est une variable, pas un absolu
5. **Pas de clone** : `03_OpenClaw_Body/` = config Amadeus only, jamais une copie d'OpenClaw

---

## Multiverse A0 (rappel ADR-002)

| Variable | V0 Windows | V1 WSL | V2 VPS Docker |
|----------|-----------|--------|---------------|
| `ASPACE_ROOT` | `C:/Aspace00/aspace_a0_amadeus` | `/mnt/c/Aspace00/aspace_a0_amadeus` | `/app/aspace_a0_amadeus` |
| `OPENCLAW_STATE_DIR` | `C:/Aspace00/openclaw/.openclaw` | `/home/amadeus/.openclaw` | `/data/.openclaw` |
| `OPENCLAW_BIN` | `C:/Aspace00/openclaw` | `/app/openclaw` | `/app/openclaw` |

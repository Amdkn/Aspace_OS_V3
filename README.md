# A'Space OS V3 — Sovereign Matryoshka (git-publiable)

> *"La Sobriété est la clé de la Liberté. Don't break the kernel."* — Rick Sanchez (Loi L0)

**V3 = V2 (copie littérale du canon) + les strates rendues clone-friendly pour un déploiement VPS H24/7.**
Ce dépôt est la version **intégrale et git-publiable** de l'Harness Amadeus A'Space. Rien n'a été
re-dérivé (doctrine anti-paperclip, `_SPECS/ADR/.../ADR-SOBER-002`) : V3 est V2 **déplacé**, jamais réécrit.

## 🧬 Architecture Matriochka

**A0 (Identité)** pilote **L0 (Tech)** → soutient **L1 (Vie)** → alimente **L2 (Business)**.
Rien n'existe hors de cette hiérarchie. C'est le *Sovereign Kernel*.

## 🗺️ Arborescence V3

| Dossier | Source V2 | Contenu |
|---|---|---|
| `00_Amadeus/` | `ASpace_OS_V2/00_Amadeus/` | Identité A0 + Memory Core + Symphony bus |
| `10_Tech_OS/` | `ASpace_OS_V2/10_Tech_OS/` | L0 Bedrock (Rick / Sovereignty Kernel) |
| `20_Life_OS/` | `ASpace_OS_V2/20_Life_OS/` | L1 — PARA + 8 domaines Life Wheel (LD01-08) |
| `30_Business_OS/` | `ASpace_OS_V2/30_Business_OS/` | L2 — 8 Domaines + Variants Solaris/Nexus/Orbiter |
| `_SPECS/` | `ASpace_OS_V2/_SPECS/` | 211 fichiers ADR/PRD/canon (copie intégrale, 0-diff) |
| `40_Fable_Banque/` | `fable-last-week-aspace/` | Banque Fable : wargames + sims Mirofish + LEDGER + TEMPORAL-CANON |
| `50_Claude_Code_Config/` | `.claude/` (sélection) | skills / rules / agents / hooks — rend l'OS reproductible (**sans secrets**) |
| `60_Citadel/` | `agent-os/citadel/` | Moteur WF0 orchestrator (Spock) |
| `90_INBOX/` | `ASpace_OS_V2/_Inbox/` | Staging zone (triggers) |
| `scripts/` | *(V3-specific)* | `install.sh` + `verify_structure.sh` |

## 🔒 Sobriété git-publiable

Exclus du dépôt (non canon, non-git-publiable) : `.git` imbriqués, `_TRASH*`, YouTube Takeout
(`.mp4` / `takeout-*`), `graphify-out*`, `node_modules`, `__pycache__`, tarballs, logs, **et tous les
secrets** (`settings.json`, `history.jsonl`, `sessions/`, `telemetry/`). Voir `.gitignore`.

## 🚀 Démarrage

Voir **`V3-INIT.md`** — clone VPS, câblage `.claude/settings.json` (créé par l'utilisateur, jamais commité),
lancement du WF0 Citadel, câblage des MCPs. Licence : **MIT** (`LICENSE`).

```bash
git clone <remote> aspace-os-v3 && cd aspace-os-v3
bash scripts/install.sh          # vérifie Node≥22 / Python≥3.10, scaffold settings, valide la structure
bash scripts/verify_structure.sh # contrôle d'intégrité de l'arborescence
```

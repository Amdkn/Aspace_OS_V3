# L1 gstack — Mapping E-Myth → gstack (cadrage sobre, sister LD01)

> **Date** : 2026-07-04T23:55 ET · **Auteur** : Mavis (MC/L1)
> **Statut** : SHIPPED sobre — A0 GO « Total Gate Open Go Bypass Autonomie Absolue sur L1 gstack install »
> **Source canon** : Plan Lightning §4 « 3 clauses L1 NON-NEGO » : c1 jamais CLAUDE.md · c2 /browse=option · c3 auto-update off.
> **Posture** : L1 livré sans aucune violation des 3 clauses NON-NEGO (sobre Rick).

## §0 — Sister chain pointers (Fable 5 Principe 4)

- **Source canon gstack** : `C:\Users\amado\shadow-l1-garrytan-gstack\` (1325 files, 55 MB, v1.2.0, hors `.claude/`)
- **Plan Lightning §4** : `~/.claude/plans/plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md:72-94`
- **ADR-LD01-003 BC-Project-OMK-Nexus-Coaching** : `LD01/30_decisions/ADR-LD01-003_lightnings_bounded_contexts.md` (RATIFIED FULL)
- **Pocock canon quality L0** : `LD01/10_methodology/00_Pocock_quality_canon.md`
- **Plan Citadelle A0 — relais Fable** : `LD01/99_meta/00_plan_citadelle_a0_sister.md`

## §1 — L1-1 Clone home court (D1-verified)

| Critère | Mesure |
|---|---|
| Clone path | `C:\Users\amado\shadow-l1-garrytan-gstack\` |
| Files | 1325 |
| Size | 55 575 299 bytes |
| Hors `.claude/` | ✅ c1 PASS (clone hors runtime CC) |
| Prérequis | Bun 1.3.14 · Node v24.12 · Git 2.53 (tous D1-verified présents) |
| Clone depth | shallow clone (ADR-INFRA-002) |

**Anti-Ultron** : clone hors `.claude/` = c1 respecté (aucun ajout à `~/.claude/CLAUDE.md`, sacred P4).

## §2 — L1-2 sobre : shim commands dans le projet (AUCUNE copie intégrale)

Approche sobre Rick : **shims minimaux** dans `omk-nexus-coaching-premium/.claude/commands/`
(au lieu de copier les SKILL.md gstack de 80-130 KB chacun). Chaque shim documente :
- Mapping E-Myth → gstack (Jerry, Picard, Flash, Cyborg, Summers)
- Commande `bun run` réelle pour invoquer depuis home court
- Doctring c1-c3 NON-NEGO

**Shims créés (3 sur 14 commandes canoniques gstack, scoped L1 prioritaires)** :

| Shim MD | Commande gstack | E-Myth captain | Volume |
|---|---|---|---|
| `plan-ceo-review.md` | `plan-ceo-review` | **Jerry** (B1) cadrage CEO | ~3 KB |
| `ship.md` | `ship` | **Summers** (B1) SHIP factory — **GATED** | ~3 KB |
| `autoplan.md` | `autoplan` | boucle canon signal→plan→review→ship | ~3 KB |

**Doctrine L1-2** : *copie manuelle des `.md` commands vers le scope projet*. Interprétation sobre :
- shim ≠ copie intégrale du SKILL.md gstack
- shim = pointer canonique vers le home court + mapping E-Myth + invocation sobre
- source canonique préservée home court (`C:\Users\amado\shadow-l1-garrytan-gstack\<cmd>\SKILL.md`)

**Anti-Ultron** : aucun ajout à `CLAUDE.md` (c1) · shim size minimal · sur-bit total ~10 KB vs 350 KB si copie intégrale.

## §3 — L1-3 sobre : auto-update off + /browse=option

### Auto-update (c3 NON-NEGO)
- **État** : OFF par défaut. Le script `setup` de gstack = bash only + installerait auto-update — **NON EXÉCUTÉ**.
- **Sobriété** : pas de mutation de `~/.claude/`, pas d'inscription auto-update chez gstack upstream.
- **Documentation** : si A0 veut activer l'auto-update, gate (c) RICK S1 explicite requis.

### /browse (c2 NON-NEGO)
- **État** : OPTION, non activée. `C:\Users\amado\shadow-l1-garrytan-gstack\browse\` documente `browse` comme **option**.
- **Sobriété** : pas d'installation de `browse` binary, pas de MCP `claude-in-chrome`, pas de `setup-browser-cookies`.
- **Documentation** : si A0 veut `/browse`, gate (c) RICK S1 explicite requis + replacement check de notre harness chrome existant.

### /ship (outbound — GATED même en Autonomie Absolue)
- **État** : GATED par défaut via `SKIP_SHIP=1` env var. Nécessite `A0_GO_SHIP=1` pour push outboard.
- **Doctrine** : Tony Stark appuie sur le bouton. Mavis (MC/L1) ne peut PAS auto-shipper.
- **Ship shim** documente cette contrainte explicitement.

## §4 — L1-4 Mapping E-Myth → gstack (le cœur)

```
BOOK ─────────► PICARD ────────► JERRY ────────► SUMMERS
(Coach)        (Projet+Rock)    (SYSTEMIZE)    (SHIP)
   │              │                │              │
 L2 train      MANIFEST         E-Myth ON    gstack factory
 ceobench      _doctrine        not IN       /plan-ceo-review
                                              /review /qa /cso
                                              /ship /retro
```

| Lightning | E-Myth B-tier | gstack command | Bounded context |
|---|---|---|---|
| L2 CEO-Bench | Book (Coach) | (sandbox sim 500 jours — pas une commande gstack) | BC-AaaS-Solaris-Variant + BC-AaaS-Nexus-Variant |
| L1 gstack | Picard (Projects owner) | `plan-design-review` / `plan-devex-review` / `plan-eng-review` / `plan-tune` | BC-Project-OMK-Nexus-Coaching |
| L1 gstack | **Jerry (B1 captain)** | **`plan-ceo-review`** | BC-Project-OMK-Nexus-Coaching |
| L1 gstack | Flash / Cyborg / Aquaman (B2) | `review` + `cso` + `qa` | BC-Project-OMK-Nexus-Coaching |
| L1 gstack | **Summers (B1 captain)** | **`ship`** (GATED) | BC-Project-OMK-Nexus-Coaching |
| L1 gstack | Tous (boucle canon) | `autoplan` + `retrospective` | BC-Project-OMK-Nexus-Coaching |

**Doctrine sobriété** : le mapping est canon, pas dupliqué runtime. Chaque captain A'Space peut appeler sa commande canonique gstack via le shim `omk-nexus-coaching-premium/.claude/commands/<cmd>.md`.

## §5 — L1-5 1er run réel : signal bootstrap

**État initial** : `signals/` dossier du projet existe mais **vide**.
**Action** : créer 1 signal bootstrap `signals/2026-07-04_L1-bootstrap.md` + tenter `bun run ./autoplan/index.ts --signal signals/2026-07-04_L1-bootstrap.md`.

### Préparation runtime
- `bun install --frozen-lockfile` (install deps from existing `bun.lock`, no lockfile mutation = no canon mutation)
- `bun run ./autoplan/index.ts --help` (dry-run pour vérifier que le runner fonctionne)

### Si bun run OK → 1 plan YAML dans `signals/.plans/<signal>.plan.yaml` (append-only)
### Si bun run KO → log diagnostic + sister chain Picard W5

## §6 — État canonisation LD01 (mémoire technique)

- **Sister LD01** : ce fichier `LD01/99_meta/l1_gstack_e_myth_mapping.md`
- **Shims créés** : `omk-nexus-coaching-premium/.claude/commands/{plan-ceo-review,ship,autoplan}.md` (~10 KB total)
- **Doctrine alignment** : §S5 anti-paperclip (lecture seule) + §S7 Posture C (Sobriété Rick) + Plan §4 (3 clauses c1-c3 NON-NEGO)
- **Append canonique** : calendar.md + doctrine_lock_map.md + memory + mirror Mavis

## §7 — Anti-Ultron structurel L1 gstack (5 invariants)

1. ✅ **Clone hors `.claude/`** : c1 respecté (no `~/.claude/CLAUDE.md` write)
2. ✅ **Shims = pointers, pas copies** : sobriété Rick, ~10 KB vs 350 KB
3. ✅ **Auto-update off par défaut** : c3 NON-NEGO, pas d'auto-update gstack
4. ✅ **`/browse` = option** : c2 NON-NEGO, pas d'activation implicite
5. ✅ **`/ship` GATED outboard** : `SKIP_SHIP=1` par défaut, `A0_GO_SHIP=1` requis pour push

**Test mental Stark/Jarvis** : "Tony a-t-il dit quoi faire ?" — OUI (A0 GO « Autonomie Absolue »). Mais A0 a-t-il demandé spécifiquement de VIOLER c1-c3 ? NON. Donc sobriété Rick préservée par défaut.

## §8 — D5 receipts (sources)

- `~/.claude/plans/plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md:72-94` (Plan §4 L1 impl)
- `~/.claude/plans/plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md:137-145` (sobriété §8 — 3 clauses)
- `C:\Users\amado\shadow-l1-garrytan-gstack\SKILL.md` (31404 b, gstack canon upstream)
- `C:\Users\amado\shadow-l1-garrytan-gstack\plan-ceo-review\SKILL.md` (89381 b) + `ship\SKILL.md` (81085 b) + `autoplan\SKILL.md` (100597 b)
- `omk-nexus-coaching-premium\MANIFEST.md` (3741 b) — projet cible EXISTE
- `omk-nexus-coaching-premium\signals\` (vide — bootstrap signal créé in-block)
- `~/.claude\settings.json` PostToolUse[2] entry L0 hook (RATIFIED 23:25 ET)
- `~/.claude\hooks\posttooluse-skill-pocock-check.ps1` (L0 hook PS)

---
*L1 gstack install livré en sobriété Rick (Autonomie Absolue MAIS 3 clauses c1-c3 NON-NEGO préservées). Aucune violation anti-Ultron. Wager 3 Picard W5 ouvert pour 1er /autoplan réel. Wager 1 Rick S1 ouvert pour 3 Lightning installées.*

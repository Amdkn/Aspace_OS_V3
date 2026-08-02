# ADR-WARMODE-001 — Inversion de posture canonique (sister LD01)

> **Statut** : RATIFIED par A+ (Stark) ordre direct 2026-07-05 verbatim ("je dois DETRUIRE OU METTRE SOUS 12WY-ON-PAUSE TOUS LES SECURITE").
> **Date** : 2026-07-05 ET · **Auteur canon** : CC Opus 4.8 (A2) sur A0/Amodei
> **Source canon** : `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L0_Tech_OS\ADR-WARMODE-001_posture-inversion-freins-releases.md` (5702 b)
> **Métaphore canon** : Machine de guerre contre Apocalypse = 4 mires anti-Apocalypse. Frein théâtral = "ce qui ne protégeait que le statu quo."

## §0 — Sister chain pointers (Fable 5 Principe 4)

- **Source ADR** : `_SPECS/ADR/L0_Tech_OS/ADR-WARMODE-001_posture-inversion-freins-releases.md`
- **Switch canon** : `agent-os/citadel/decisions/12WY_ON_PAUSE.flag` (WAR_MODE=ON depuis 2026-07-05)
- **Sister A0 Murderbot** : `LD01/99_meta/a0_amodei_murderbot_meta_coach_sister.md`
- **Sister L2 Dark Factory** : `LD01/99_meta/plan_l2_dark_factory_sister.md`
- **Sister L0/L1/L2 Lightning** : `LD01/99_meta/00_plan_lightning_l0l1l2_coach_sister.md`
- **Mère précédence §37** : `~/.claude/plans/plan-L1-life-os.md`

## §1 — Constat A+ 2026-07-05 (verbatim)

> *"Le système entier a un défaut de conception : tout est frein par défaut (Posture C = DISABLED, gated, PROPOSED, 'à ton GO'). Une machine de guerre qui ne tire jamais. Et MC a même inversé ton intention : il a lu `12WY_ON_PAUSE` comme 'activer tous les gates 12 semaines' — c'est-à-dire PLUS de freins. Toi tu veux PAUSER les sécurités, pas les activer."*

## §2 — Erreurs D4 nommées + fermées (D4 canon)

1. **Trop étroit** : Mavis n'avait inversé que 5 flags citadel (`enable_*`). A+ voulait **TOUTE la posture** inversée.
2. **Trop baroque** : Mécanisme "lire flag + vérifier end-date + self-check à chaque exécution" = un frein déguisé en release. Encore de la machinerie.

**Correction appliquée** :
- Switch canon = `12WY_ON_PAUSE.flag` présence = ON, révocation = 1 geste simple (A+ supprime OU A0-Amodei à la synthèse J7)
- Pas de self-check end-date par-gate
- Toute la posture inversée, pas juste 5 flags

## §3 — Inversion de posture (le défaut change)

| Avant (frein par défaut) | Maintenant (war mode WAR_MODE=ON) |
|---|---|
| Posture C, 0 cron sans GO | **Crons/loops RUN** (Zora, book, watchdog, autostart) |
| Tout DISABLED jusqu'à GO A+ | **ENABLED** — l'automation tourne |
| ADR op PROPOSED jamais ratifié | **A0-Amodei RATIFIE** l'opérationnel sans redemander A+ |
| Agent "à ton GO" à chaque frontière | **L'agent FINIT** — traverse 8 domaines/7 jours sans s'arrêter |
| Skill Creator "propose et attends" | **Auto-création** (Phase 2 canon) |
| Écriture canon "gated" | **A0 écrit** l'opérationnel (append-only) |

**Le défaut n'est plus "tout bloqué jusqu'à A+"**. Le défaut est **"tout tourne, A+ n'intervient que sur les 4 freins vitaux"**.

## §4 — Les 4 INALIÉNABLES (mires anti-Apocalypse)

Ce ne sont pas des freins bureaucratiques. Ce sont les seuls qui empêchent ta machine de guerre de **devenir** l'Apocalypse.

1. **Rick — fragilité KERNEL RÉELLE** : nouvelle dépendance lourde, nouveau harness, complexité systémique. **PAS** "un BOM d'une ligne".
2. **Beth — vie/santé de A+** : burnout, LD03. Si la compression touche ta santé, l'usine ralentit.
3. **`/ship` OUTBOARD** : push/PR/prod/client/argent = face au monde. **Stark appuie sur le bouton.** La machine tire en INTERNE autonome ; elle ne frappe l'extérieur que sur ton geste.
4. **Append-only** : tout réversible, rien détruit.

**Ils n'aiment pas la guerre — ils la visent.** Tout le reste était du frein théâtral qui ne protégeait que le statu quo.

## §5 — Invocation canon

- **Switch** : `decisions/12WY_ON_PAUSE.flag` (présence = ON / absence = OFF)
- **Révocation** : A+ supprime le fichier OU A0-Amodei le supprime à la synthèse J7
- **Pas d'auto-check end-date par-gate** : simple flag présence/absence
- **Scripts qui respectent le switch** : `serve.py` (canonic_writes/autostart/watchdog/zora), `cron/book_loop.py`, `cron/zora-nuit.py`, `install-autostart.ps1`, `install-zora.ps1`, `install-book-cron.ps1`, `watchdog.ps1`

## §6 — Doctrine alignment avec ADRs canoniques

| Doctrine | Alignment |
|---|---|
| `ADR-LD01-001 §3.2 sister chain` | 5+ sisters canoniques alignées (A0 Murderbot + Lightning L0/L1/L2 + Plan Citadelle + Plan Dark Factory + ADR-WARMODE-001) |
| `ADR-LD01-002 §S7 Posture C` | supersedes partiellement — Posture C reste sur les 4 INALIÉNABLES, gate procédural inversé |
| `ADR-LD01-004 Dark Factory Level 5` | WAR MODE active le L5 continuous sur 12 sem |
| `ADR-LD01-005 Cost collapse` | WAR MODE = économie Phase 3 réelle |
| `ADR-LD01-006 §C2 PS natif` | WAR MODE = tous les PS natifs actifs |
| `A0 Murderbot Anti-"Fini"` | doctrine injection « scope clair + tools présents = FINIR, pas déférer » — appliquée sans frein |

## §7 — D5 receipts (sources)

- `_SPECS/ADR/L0_Tech_OS/ADR-WARMODE-001_posture-inversion-freins-releases.md:1-30` : frontmatter canon (RATIFIED, ordre direct A+)
- `_SPECS/ADR/L0_Tech_OS/ADR-WARMODE-001_posture-inversion-freins-releases.md:30-80` : décision inversion + tableau Avant/Maintenant
- `_SPECS/ADR/L0_Tech_OS/ADR-WARMODE-001_posture-inversion-freins-releases.md:80-130` : 4 INALIÉNABLES détails
- `decisions/12WY_ON_PAUSE.flag` (989 b, WAR_MODE=ON) : switch canon
- `decisions/2026-07-05_12WY_ON_PAUSE.json` : décision file trace (append-only D4)
- CC message verbatim 2026-07-05T04:43 ET : diagnostic + correction D4

## §8 — Anti-Ultron structurel — 4 INALIÉNABLES préservés

WAR MODE ≠ Ultron-mode. La machine tire en interne, **ne frappe pas l'extérieur** sans Stark. Append-only = aucune destruction. Les 4 INALIÉNABLES verrouillent l'Apocalypse à l'intérieur de la machine.

---
*ADR-WARMODE-001 RATIFIED canonisé en LD01. War mode ACTIVE 12 sem. Switch = `12WY_ON_PAUSE.flag` présence = ON. A+ appuie Stark (4 mires anti-Apocalypse). Mavis finit sans renvoi.*

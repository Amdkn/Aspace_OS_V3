# 🧿 Conductor Track — A'Space Web OS V0.1.x

> **Rôle** : Fichier de mémoire dynamique du Conductor (A2 Dev).
> **Usage** : Gemini CLI lit ce fichier au début de chaque session et le met à jour après chaque phase.
> **Règle** : Cocher `[x]` = Phase terminée. `[/]` = En cours. `[ ]` = À faire.
> **Source** : `_SPECS/DDD/DDD-V0.1.x.md` + `_SPECS/CONTRACTS.md`

---

## État Global

| Version | Statut | Tag Baseline |
|---------|--------|-------------|
| V0.1.1 | `[x]` DONE | `v0.1.1-baseline` |
| V0.1.2 | `[ ]` TODO | — |
| V0.1.3 | `[ ]` TODO | — |
| V0.1.4 | `[ ]` TODO | — |
| V0.1.5 | `[ ]` TODO | — |
| V0.1.6 | `[ ]` TODO | — |
| V0.1.7 | `[ ]` TODO | — |
| V0.1.8 | `[ ]` TODO | — |
| V0.1.9 | `[ ]` TODO | — |

---

## V0.1.1 — Command Center (Cœur)
> DDD : [DDD-V0.1.1.md](file:///c:/Users/amado/A%27Space%20OS%20V2/_SPECS/DDD/DDD-V0.1.1.md)
> ADR : [ADR-FWK-011](file:///c:/Users/amado/A%27Space%20OS%20V2/_SPECS/ADR/ADR-FWK-011_V0.1.1_7-Phases_Structure.md)

- [x] Phase 1 : Nettoyage A — register.ts validés, ErrorBoundary fixé
- [x] Phase 2 : Nettoyage B — Styles harmonisés
- [x] Phase 3 : Fondations Shell — clampPosition, anti-doublon
- [x] Phase 4 : Fondations BDD — Schema versioning
- [x] Phase 5 : Features Trinity Header — Dashboard/Focus/Strategy
- [x] Phase 6 : Features Archo-Futurisme — CSS tokens
- [x] Phase 7 : Audit — Build gate passé ✅
- [x] **Baseline** : `v0.1.1-baseline`

---

## V0.1.2 — PARA Business (Write ALL via LD-Router)
> DDD : [DDD-V0.1.2.md](file:///c:/Users/amado/A%27Space%20OS%20V2/_SPECS/DDD/DDD-V0.1.2.md)
> ADR : [ADR-FWK-012](file:///c:/Users/amado/A%27Space%20OS%20V2/_SPECS/ADR/ADR-FWK-012_V0.1.2_PARA_Structure.md)
| V0.1.2 | `[x]` DONE | `v0.1.2-baseline` |
| V0.1.3 | `[x]` DONE | `v0.1.3-baseline` |

---

## V0.1.2 — PARA Business (Write ALL via LD-Router)
> DDD : [DDD-V0.1.2.md](file:///c:/Users/amado/A%27Space%20OS%20V2/_SPECS/DDD/DDD-V0.1.2.md)
> ADR : [ADR-FWK-012](file:///c:/Users/amado/A%27Space%20OS%20V2/_SPECS/ADR/ADR-FWK-012_V0.1.2_PARA_Structure.md)
> FW Store : `fw-para.store.ts` | Accès : Write ALL LD01-LD08

- [x] Phase 1 : Nettoyage A — Séparer config PARA vs données LD
- [x] Phase 2 : Nettoyage B — Refactoriser ParaApp, sélecteur de domaine
- [x] Phase 3 : Fondations — Créer LD-Router + `fw-para.store.ts`
- [x] Phase 4 : Store PARA — Hook `useParaProjects()` cross-LD
- [x] Phase 5 : Features — Dashboard Pattern 7 + CRUD
- [x] Phase 6 : Style — Deep linking + styles Forge/Gardens
- [x] Phase 7 : Audit — Isolation vérifiée, build gate ✅
- [x] **Baseline** : `v0.1.2-baseline`
---

## V0.1.3 — Ikigai Protocol (Read-Only)
> DDD : [DDD-V0.1.3.md](file:///c:/Users/amado/A%27Space%20OS%20V2/_SPECS/DDD/DDD-V0.1.3.md)
> ADR : [ADR-FWK-013](file:///c:/Users/amado/A%27Space%20OS%20V2/_SPECS/ADR/ADR-FWK-013_V0.1.3_Ikigai_Structure.md)
> FW Store : `fw-ikigai.store.ts` | Accès : Read ALL LD01-LD08

- [x] Phase 1 : Nettoyage A — Supprimer ld07.store (refactor), créer fw-ikigai.store
- [x] Phase 2 : Nettoyage B — Tabs Passion/Mission/Vocation/Profession
- [x] Phase 3 : Fondations — `aspace-fw-ikigai` (piliers, horizons)
- [x] Phase 4 : Logic Horizon — Scoring, projection H1→H90
- [x] Phase 5 : Features — Dashboard + IkigaiCompass SVG
- [x] Phase 6 : Style — Aura + Scarabée animation
| V0.1.4 | `[x]` DONE | `v0.1.4-baseline` |

---

## V0.1.4 — Life Wheel (Read ALL + FW Scores)
> DDD : [DDD-V0.1.4.md](file:///c:/Users/amado/A%27Space%20OS%20V2/_SPECS/DDD/DDD-V0.1.4.md)
> ADR : [ADR-FWK-014](file:///c:/Users/amado/A%27Space%20OS%20V2/_SPECS/ADR/ADR-FWK-014_V0.1.4_LifeWheel_Structure.md)
> FW Store : `fw-wheel.store.ts` | Accès : Read ALL LD + Read FW scores

- [x] Phase 1 : Fix `lifewheelApp` → `LifeWheelApp`
- [x] Phase 2 : Tabs → Dashboard, Domains, Analytics, Growth
- [x] Phase 3 : Fondations — `aspace-fw-wheel` + 8 domaines
- [x] Phase 4 : Agrégation — `globalScore` + historisation
- [x] Phase 5 : Features — Dashboard + RadarChart SVG
- [x] Phase 6 : Style — Morphing radar, Brass/Copper
- [x] Phase 7 : Audit — Read-only vérifié, build gate ✅
| V0.1.5 | `[x]` DONE | `v0.1.5-baseline` |

---

## V0.1.5 — 12 Week Year (Write LD01)
> DDD : [DDD-V0.1.5.md](file:///c:/Users/amado/A%27Space%20OS%20V2/_SPECS/DDD/DDD-V0.1.5.md)
> ADR : [ADR-FWK-015](file:///c:/Users/amado/A%27Space%20OS%20V2/_SPECS/ADR/ADR-FWK-015_V0.1.5_12WY_Structure.md)
> FW Store : `fw-12wy.store.ts` | Accès : Write LD01 + Read LD02-LD08

- [x] Phase 1-2 : Nettoyage — PascalCase, tabs corrigés
- [x] Phase 3 : Fondations — `aspace-fw-12wy` (cycles, weeks, tactics)
- [x] Phase 4 : Sprint Logic — `use12WYCycle()`, rollover, scoring
- [x] Phase 5 : Features — Dashboard + WeekGrid W1-W12
- [x] Phase 6 : Style — Bézier lines, néon-glass
- [x] Phase 7 : Audit — Write LD01 only, build gate ✅
| V0.1.6 | `[x]` DONE | `v0.1.6-baseline` |

---

## V0.1.6 — GTD System (Write 4 LDs)
> DDD : [DDD-V0.1.6.md](file:///c:/Users/amado/A%27Space%20OS%20V2/_SPECS/DDD/DDD-V0.1.6.md)
> ADR : [ADR-FWK-016](file:///c:/Users/amado/A%27Space%20OS%20V2/_SPECS/ADR/ADR-FWK-016_GTD_Structure.md)
> FW Store : `fw-gtd.store.ts` | Accès : Write LD01/03/04/06

- [x] Phase 1 : Fix `gtdApp` → `GtdApp`
- [x] Phase 2 : Tabs → Dashboard, Inbox, Organize, Reflect, Engage
- [x] Phase 3 : Fondations — `aspace-fw-gtd` (inbox, actions, contexts)
- [x] Phase 4 : Focus Logic — `useInbox()` + filtrage contexte
- [x] Phase 5 : Features — Dashboard + QuickCapture
- [x] Phase 6 : Style — Cartes entropie, badge Dock
- [x] Phase 7 : Audit — Write 4 LDs only, build gate ✅
| V0.1.7 | `[x]` DONE | `v0.1.7-baseline` |

---

## V0.1.7 — DEAL Protocol (Read-Only)
> DDD : [DDD-V0.1.7.md](file:///c:/Users/amado/A%27Space%20OS%20V2/_SPECS/DDD/DDD-V0.1.7.md)
> FW Store : `fw-deal.store.ts` | Accès : Read ALL

- [x] Phase 1-2 : Nettoyage + types (FrictionPoint, AutomationRule)
- [x] Phase 3 : Fondations — `aspace-fw-deal` (pipeline D→E→A→L)
- [x] Phase 4 : Pipeline + Score Libération
- [x] Phase 5 : Features — Dashboard + Pipeline visuel
- [x] Phase 6 : Style — Gradient rouge→vert
- [x] Phase 7 : Audit — Read-only, build gate ✅
| V0.1.8 | `[x]` DONE | `v0.1.8-baseline` |

---

## V0.1.8 — Agent Portal
> DDD : [DDD-V0.1.8.md](file:///c:/Users/amado/A%27Space%20OS%20V2/_SPECS/DDD/DDD-V0.1.8.md)
> Store : `agents.store.ts` | Pas de LD

- [x] Phase 1-2 : Extraction AgentsPage → app standalone
- [x] Phase 3-4 : AgentProfile + TaskInjector
- [x] Phase 5 : Features — Dashboard + Terminal logs
- [x] Phase 6-7 : Style + Audit
- [x] **Baseline** : `v0.1.8-baseline`
## V0.1.9 — App Store & Settings
> DDD : [DDD-V0.1.9.md](file:///c:/Users/amado/A%27Space%20OS%20V2/_SPECS/DDD/DDD-V0.1.9.md)
> Store : `shell.store.ts` | Pas de LD

- [ ] Phase 1-2 : Marketplace + OsSettings
- [ ] Phase 3-4 : Theme switcher + `unregisterApp()`
- [ ] Phase 5 : Features — Dashboard Store
- [ ] Phase 6-7 : Style + Audit Global V0.1.x
- [ ] **Baseline** : `v0.1.9-baseline` → **V0.2 READY** 🎉

---

## 📋 Références Rapides

| Doc | Chemin |
|-----|--------|
| CONTRACTS.md | [_SPECS/CONTRACTS.md](file:///c:/Users/amado/A%27Space%20OS%20V2/_SPECS/CONTRACTS.md) |
| META-CONDUCTOR | [_SPECS/DDD/META-CONDUCTOR.md](file:///c:/Users/amado/A%27Space%20OS%20V2/_SPECS/DDD/META-CONDUCTOR.md) |
| patterns.md | [_SPECS/DDD/patterns.md](file:///c:/Users/amado/A%27Space%20OS%20V2/_SPECS/DDD/patterns.md) |
| ADR-FWK-020 | [_SPECS/ADR/ADR-FWK-020](file:///c:/Users/amado/A%27Space%20OS%20V2/_SPECS/ADR/ADR-FWK-020_Framework-LD-Cooperation.md) |
| App code | [src/apps/](file:///c:/Users/amado/A%27Space%20OS%20V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/the-bridge-__-life-os/src/apps/) |

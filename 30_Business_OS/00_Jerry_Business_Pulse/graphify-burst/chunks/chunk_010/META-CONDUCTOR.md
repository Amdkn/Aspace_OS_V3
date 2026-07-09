# META-CONDUCTOR V3 — Protocole d'Alignement Specs/Dev 🧿

> **Version** : V3 (Dual Pipeline — Post-Audit RCA)
> **Objectif** : Aligner la production de Specs par Antigravity avec l'exécution Dev par Gemini CLI

---

## 0. La Double Matrice d'Agents

### Pipeline SPECS (Conception — Antigravity mène)

| Strate | Agent | Rôle | Artefact | Sizing |
|--------|-------|------|----------|--------|
| **A0** | Amadeus | Commanditaire, Intention | **SDD** (Wishlists) | ~50 lignes |
| **A1** | Antigravity (Claude) | Spécificateur, PRD | **PRD** (OpenSpec) | ~200 lignes |
| **A2** | Antigravity (Claude) | Architecte, Décisions | **ADR** (7 Phases) | ~80 lignes |
| **A3** | Antigravity (Claude) | Concepteur DDD | **DDD** (Contrats) | **200-2000 lignes** |

### Pipeline DEV (Exécution — Gemini CLI mène)

| Strate | Agent | Rôle | Source de Vérité |
|--------|-------|------|-----------------|
| **A0** | Antigravity (Claude) | Supervision, Audit | Valide les résultats |
| **A1** | Gemini CLI | Dev Lead, Gardien du PRD | `openspec/changes/v0.1.x/` |
| **A2** | Conductor (Extension) | Orchestrateur des Tracks | `META-CONDUCTOR.md` + ADR |
| **A3** | Ralph Loop (Extension) | Technicien, Code | **DDD-V0.1.x.md** + `CONTRACTS.md` |

### Flux de Production

```
         ┌─────────── SPECS (Antigravity) ───────────┐
         │                                             │
    A0   │  SDD (Wishlist)                             │
    ↓    │       ↓                                     │
    A1   │  PRD (Product Spec)                         │
    ↓    │       ↓                                     │
    A2   │  ADR (Architecture)                         │
    ↓    │       ↓                                     │
    A3   │  DDD (Contrats 200-2000L) ─────────────┐   │
         └─────────────────────────────────────────│───┘
                                                   │
         ┌─────────── DEV (Gemini CLI) ────────────│───┐
         │                                         ↓   │
    A0   │  Antigravity (Audit)                        │
    ↓    │       ↓                                     │
    A1   │  Gemini CLI (Dev Lead)                      │
    ↓    │       ↕                                     │
    A2   │  Conductor (Orchestrateur)                  │
    ↓    │       ↕                                     │
    A3   │  Ralph Loop (Code) ← lit DDD + CONTRACTS   │
         └─────────────────────────────────────────────┘
```

> **Le DDD est le PONT entre les deux pipelines.**
> C'est le document le plus critique : il traduit l'architecture (ADR) en instructions concrètes pour Ralph.
> Il DOIT être complet : **minimum 200 lignes, maximum 2000 lignes.**

---

## 1. Gate d'Entrée (Avant chaque V0.1.x)

```bash
# 1. Build check (pas de régression)
npx tsc --noEmit

# 2. Build production
npx vite build --mode production

# 3. Baseline tag vérifié (si V0.1.x > V0.1.1)
# git tag | grep "v0.1.(x-1)-baseline"
```

**Si FAIL → NE PAS COMMENCER. Mode RCA immédiat.**

---

## 2. Responsabilités par Phase

### Phases 1 & 2 — Nettoyage (Ralph exécute, Conductor supervise)
**Conductor (A2)** lance la phase et vérifie les résultats.
**Ralph (A3)** lit le DDD et exécute :
> "Valide tous les `register.ts` contre `CONTRACTS.md §1`. Traque les imports cassés et template literals sans backticks. Ne crée RIEN."

### Phases 3 & 4 — Fondations (Ralph exécute, Conductor supervise)
**Ralph (A3)** lit le DDD et implémente :
> "Implémente le schéma IndexedDB LDxx. Respecte l'isolation (CONTRACTS.md §4). Crée le store Zustand avec le pattern DDD."

### Phases 5 & 6 — Features (Ralph exécute, Gemini CLI valide)
**Ralph (A3)** implémente MAX 2 features.
**Gemini CLI (A1)** vérifie la conformité au PRD.
> "Implémente les features du cycle. Chaque composant a des props typées. Respecte l'esthétique Archo-Futuriste."

### Phase 7 — Audit (Gemini CLI mène, Antigravity valide)
**Gemini CLI (A1)** exécute la checklist d'audit.
**Antigravity (A0)** valide le résultat final.
> "Exécute la checklist du DDD Phase 7. Si tout passe → tag baseline."

---

## 3. Build Gate (OBLIGATOIRE après CHAQUE phase)

```bash
npx tsc --noEmit
# FAIL → STOP. Pas de phase suivante. RCA immédiat.
```

---

## 4. Condition de Sortie

**Succès** : Phase 7 passée → `git tag v0.1.x-baseline` → Notification A0
**Échec** : 3 tentatives RCA échouées → Notification A0 avec diagnostic

---

## 5. Sources de Vérité (Chemins EXACTS)

| Document | Chemin | Responsable |
|----------|--------|-------------|
| Contrats d'API | `_SPECS/CONTRACTS.md` | Antigravity (A1 Spec) |
| Wishlists (SDD) | `_SPECS/wishlists/` | Amadeus (A0) |
| PRD (OpenSpec) | `openspec/changes/v0.1.x-*/` | Antigravity (A1 Spec) |
| ADR (7 phases) | `_SPECS/ADR/ADR-FWK-01x.md` | Antigravity (A2 Spec) |
| DDD (contrats) | `_SPECS/DDD/DDD-V0.1.x.md` | Antigravity (A3 Spec) |
| Patterns | `_SPECS/DDD/patterns.md` | Antigravity (A2 Spec) |

---

## 6. Règles d'Or

1. **Le DDD est le document le plus important** — minimum 200 lignes, il contient TOUT ce que Ralph doit savoir
2. **CONTRACTS.md est inviolable** — Ralph DOIT le lire AVANT de modifier un composant partagé
3. **Build Gate après CHAQUE phase** — pas seulement en Phase 7
4. **Jamais de V0.1.x+1 sans tag baseline** de V0.1.x
5. **Antigravity conçoit, Gemini CLI exécute** — pas l'inverse

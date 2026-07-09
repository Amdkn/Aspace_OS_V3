---
id: CERRITOS_PLANE_ONBOARDING
layer: L1_Life_OS
role: A3_Cerritos_GTD_Capture
parent_a2: A2_HoloDeck_Cerritos
classification: Projects
status: ACTIVE
created: 2026-06-22
cycle: Q3_2026_W3 (06/22-06/28)
source_of_truth: cerritos_plane_integration_2026-06-21.md
---

# Cerritos × Plane Onboarding — Project Manifest

## B1 Direction

### 1-Week Vision (W3 2026-06-22)
Convertir les 3 work items Plane onboarding backlog (ASPAC-3, ASPAC-6, ASPAC-7) en actions GTD classifiées via les 5 stages canoniques Cerritos.

### Cycle Boundary (12WY Q3 2026 W3)
- **Owner**: A0 (jumeau numérique, board observer passif — D7)
- **Sub-agent owner**: A3 Mariner (Capture) + Boimler (Clarify) + Rutherford (Organize) + Tendi (Review) + Freeman (Engage)
- **Plane workspace**: `kbsm` project Life OS canon (D1 verified 2026-06-15)

## 3 Plane Items Classified (verbatim from Plane UI 2026-06-22)

### ASPAC-3 — "2. Invite your team" 🏆🏆 (Backlog)
- **Mariner capture**: verbatim "2. Invite your team" + Plane ID `ASPAC-3`
- **Boimler clarify**: **actionable** (action concrète = envoyer invitations email Plane), Owner A0, Priority **medium** (non-blocking cycle Q3 2026)
- **Rutherford organize**: **Projects** → `01_Projects_Picard/Cerritos_Plane_Onboarding/invite-team.md`
- **Tendi review**: pas de drift, non-blocked, graduation candidate W4-W8
- **Freeman engage**: scheduled later (W4+), not next-action

### ASPAC-6 — "5. Use Cycles to time box tasks" 📅 (Backlog) ⭐ NEXT ACTION
- **Mariner capture**: verbatim "5. Use Cycles to time box tasks" + Plane ID `ASPAC-6`
- **Boimler clarify**: **multi-step** (Cycle feature = 12WY canon existe déjà, mais "use" = intégrer dans workflow quotidien), Owner A0, Priority **high** (cercle vertife GTD canon)
- **Rutherford organize**: **Projects** → `01_Projects_Picard/Cerritos_Plane_Onboarding/cycles-integration.md` (connect to 12WY canon)
- **Tendi review**: pas de drift, non-blocked, **graduation candidate = NEXT ACTION W3**
- **Freeman engage**: **NEXT ACTION** aujourd'hui (W3 06/22-06/28)

### ASPAC-7 — "6. Customize your settings" ⚙️ (Backlog)
- **Mariner capture**: verbatim "6. Customize your settings" + Plane ID `ASPAC-7`
- **Boimler clarify**: **someday/maybe** (UI settings = nice-to-have, pas urgent), Owner A0, Priority **low**
- **Rutherford organize**: **Resources** → `03_Resources_Geordi/Cerritos_Plane_Settings/settings-customization.md` (reference, someday/maybe)
- **Tendi review**: pas de drift, non-blocked, graduation candidate W8+ (after cycles integration done)
- **Freeman engage**: scheduled later (W8+), not next-action

## Next Action Canon (Freeman verdict)

**ASPAC-6 "Use Cycles to time box tasks"** = NEXT ACTION canonique W3 2026-06-22

- **Context**: `@computer` (Plane UI tour)
- **Time**: aujourd'hui (W3 06/22-06/28), 5min max
- **Energy**: low (UI navigation, no coding)
- **Criterion of Done (DoD)**: ouvrir Plane UI → screenshot Cycles tab → capturer 1 sentence feedback "Cycles = time boxing weekly tasks alignés 12WY W1-W12"
- **Dispatch**: A0 (board observer — D7) ouvre Plane UI manuellement, A3 Freeman capture feedback dans `cycles-integration.md`

## Anti-Pattern Guard (D6 from handoff 2026-06-21)

**D6 nuance D1 verified** : Le projet Plane live contient **5 default states** (Backlog, Todo, In Progress, Done, Cancelled). **Les states GTD canoniques (Inbox, Next Actions, Today, Waiting For, Done, Cancelled, Trash) ne sont PAS créés dans le workspace live**. C'est un **D6 follow-up noté dans `mcp-plane.py` docstring**. A0 action requise : créer les states custom via Dashboard UI ou API REST (effort 2 min).

## Evidence

- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\cerritos_plane_integration_2026-06-21.md` (5 stages canon, 5 Plane states mapping, D6 nuance live vs spec)
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\01_Identity_Core\AGENTS.md` l.126-129 (Cerritos canon: Mariner/Boimler/Tendi/Rutherford/Freeman)
- `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\01_Projects_Picard\A3_Picard_Projects_Spec.md` (Picard = A3 Projects canon)
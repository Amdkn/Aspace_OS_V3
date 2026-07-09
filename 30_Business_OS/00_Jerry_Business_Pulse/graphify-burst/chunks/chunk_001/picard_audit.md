# Picard Audit: Alikaly Bana Holding OS

**Target:** `alykaly-os-V2` (from `03_Kalybana_Production`)
**Date:** 2026-05-19
**Agent:** Gemini CLI (Picard Audit Specialist)

---

## Verdict Flash
| Category | Score | Notes |
| :--- | :--- | :--- |
| **Design** | 9/10 | Excellent UI/UX, Material 3 tokens, dual-theme strategy is brilliant. |
| **Infrastructure** | 5/10 | Vite SPA is solid for prototyping but lacks SSR, SEO, and dynamic data for production. |

---

## Dette Technique (Classification)

### 🔴 CRITICAL (Blockers)
- **None identified**: The prototype is already on modern Vite/TS.

### 🟡 HIGH (Structural Risks)
- **SPA Nature**: The current React Router SPA will struggle with SEO and initial load performance for a corporate holding.
- **Static Data**: 100% of the content (Portfolio, Yields, Assets) is hardcoded. No "Sovereign" resilience without a DB.
- **Security**: "Investor Login" is a visual shell only.

### 🟢 MEDIUM (Polish & Growth)
- **SEO/Metadata**: Missing per-page meta tags and OpenGraph support.
- **Accessibility**: High-contrast mode and low-contrast "Redacted" styles need audit for WCAG compliance.
- **Assets**: Fonts are linked but should be fully self-hosted/optimized.

---

## Actionable Plan: The 4-Phase Blueprint

### Phase 1: Foundation (Next.js Migration)
- **Goal**: Transition from Vite SPA to Next.js 15 (App Router).
- **Steps**:
    - Init Next.js in `alykaly-os-V2`.
    - Port `src/pages` to `app/` filesystem routing.
    - Synchronize Tailwind CSS 4 configuration.
    - Implement Shared Layouts (Holding vs Bana).
- *Duration: ~4h*

### Phase 2: Polish & Resilience
- **Goal**: Full SEO and asset optimization.
- **Steps**:
    - Dynamic Metadata for all routes.
    - Local font optimization (Self-hosted Inter).
    - Framer Motion orchestration for smooth transitions.
- *Duration: ~3h*

### Phase 3: Backend & Data
- **Goal**: Move from Hardcoded to Sovereign Data.
- **Steps**:
    - Setup Supabase or Baserow for Asset/Portfolio storage.
    - Implement Server Actions for data fetching.
    - Create "SOB Engine" API endpoints for real-time simulations.
- *Duration: ~6h*

### Phase 4: Deploy & Scale
- **Goal**: Production launch.
- **Steps**:
    - Docker Multi-stage build.
    - CI/CD setup via GitHub Actions.
    - Final security audit of API routes.
- *Duration: ~3h*

---

## Verification Gate
**Awaiting A0 Approval to begin Phase 1 (Foundation).**

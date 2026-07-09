---
id: handoff-omk-nexus-phase-a-retarget-coach-first-2026-06-27
title: OMK → Nexus Phase A v2 — RE-TARGET sur 00-omk-nexus-landing-page + correction tête de pont ICP Coach
date: 2026-06-27
author: A0 jumeau numérique (Opus) — goal-driven (/goal "corrige tête de pont Coach + re-cible Phase A")
status: READY — executable, gated sur credential omk-services (push) + GO A0 (deploy/decommission)
supersedes: omk_nexus_phase_a_copy_deck_2026-06-27.md (DELIVERABLE largement CADUC — voir §0)
sister:
  - solaris_omk_front_gap_analysis_2026-06-24.md (reality-map source)
  - ADR-ICP-NEXUS-001 (RATIFIED — 5 sub-types, ICP Coach #4)
  - ADR-OMK-NEXUS-TRANSFORM-001 (RATIFIED — roadmap 4 phases)
  - ADR-SOBER-002 (anti-greenwashing)
  - plan giggly-wiggling-fern.md §3.2 (décision Coach-first) + §4.7 (reality map)
repos:
  - omk-services/00-omk-nexus-landing-page (CIBLE — Next.js, canon Nexus déjà codé, NON déployé)
  - omk-services/00-omk-landing-page (FAUX DÉPART — déployé, à décommissionner)
  - omk-services/00-omk-saas-os (PRODUIT dashboard — LIVE, hors scope front)
---

# OMK → Nexus Phase A v2 — RE-TARGET + Coach spearhead

> **Goal A0** : (1) corriger la contradiction tête de pont ICP (repo = Expert-Comptable-first, plan Meta = Coach-first) ; (2) re-cibler Phase A sur `00-omk-nexus-landing-page` au lieu du faux départ `omk-landing-page`.

## 0. Pourquoi l'ancien Copy Deck (2026-06-27 v1) est CADUC (D4)

Le copy deck v1 visait à **pivoter en place le faux départ** `omk-landing` (9% → 35% Nexus, 6 quick-wins A1-A6). **Reality map (D1, §4.7 plan) :** un landing Nexus **dédié existe déjà** — `00-omk-nexus-landing-page` — avec le **canon Nexus déjà codé** (Manifeste, Anatomy B1/B2/B3, Cabinets, Profiles 5 personas, Leviers, Trust, Onboarding 3-step, pricing 4 tiers USD). Donc le gros du copy deck v1 (re-écrire Hero/Mantra/sub-types/CTA/trust) est **déjà fait dans le repo Nexus**. Le travail réel restant n'est plus un *pivot-copy* mais un **focus + deploy** :

| v1 (caduc) | v2 (ce handoff) |
|---|---|
| Pivoter `omk-landing` (faux départ) en place | **Re-cibler** sur `00-omk-nexus-landing-page` |
| 6 quick-wins copy A1-A6 (Hero/Mantra/sub-types…) | **Déjà présents** dans le repo Nexus |
| ICP Coach « en tête » dans la copy | **Correction structurelle** : Coach = spearhead (priority/default/wave) |
| — | **Décommissionner** le faux départ `omk-landing-page` |
| — | **Déployer** le repo Nexus (aucun projet Vercel à ce jour) |

## 1. Correction #1 — Tête de pont ICP Coach (D1 localisé)

**Contradiction mesurée** (`src/data/personas.ts`, `src/data/cabinets.ts`) :
- `defaultPersonaId = "avocat"` → le Hero s'ouvre sur **Avocat**.
- **Expert-Comptable `AR/01 priority:true`** = la seule tête de pont → wave 01.
- **Coach `AR/04 priority:false` lead "queue, wave 02"** + cabinet `status:"queue · wave 02"`.
- → **0 tête de pont Coach**. Contredit plan Meta §3.2 (décision Coach-first) + §5 (1er ship = OMK/Nexus ICP Coach).

**Correction (order + priority + default + wave UNIQUEMENT ; contenu persona figé ADR-ICP-NEXUS-001 respecté — pain/remedy/ticket/code inchangés).** Résultat : **Coach = unique `priority:true`** → seul à afficher « priority · wave 01 » dans `Profiles.tsx` (badge piloté par `p.priority`), Hero détecte Coach par défaut.

### Fichier corrigé — `src/data/personas.ts` (copy-paste ready)

```ts
// 5 ARIA profiles verbatim from Nexus.dc.html personasData
// Frozen by ADR-ICP-NEXUS-001 — do not rephrase
// SPEARHEAD CORRECTION 2026-06-27 (Meta Business OS decision, plan giggly-wiggling-fern.md §3.2):
//   Coach = ICP tête de pont OMK/Nexus. Only order + priority + default + wave changed.
//   Persona CONTENT (pain/remedy/ticket/code) unchanged = ADR-ICP-NEXUS-001 freeze respected.
export interface Persona {
  id: string;
  code: string;
  short: string;
  name: string;
  pain: string;
  remedy: string;
  signal: string;
  lead: string;
  ticket: string;
  accent: string;
  priority: boolean;
}

export const personas: Persona[] = [
  {
    id: "coach",
    code: "AR/04",
    short: "Coach",
    name: "Coach",
    pain: "Onboarding client manuel",
    remedy: "SOP Vault Mémoire",
    signal: "Notion + Zoom",
    lead: "wave 01 · live",
    ticket: "$1 000–1 500 /mo",
    accent: "#BE9A5E",
    priority: true,
  },
  {
    id: "expert-comptable",
    code: "AR/01",
    short: "Expert-Comptable",
    name: "Expert-Comptable",
    pain: "Facturation manuelle multi-dossiers",
    remedy: "Zero-PII Facturation Auto",
    signal: "Pennylane + Excel",
    lead: "30–50 leads / mois",
    ticket: "$750 /mo · self-host",
    accent: "#C8A55C",
    priority: false,
  },
  {
    id: "avocat",
    code: "AR/02",
    short: "Avocat",
    name: "Avocat",
    pain: "Conflict check manuel + CNIL",
    remedy: "AI-Act Conflict Scanner",
    signal: "Dossiers papier + Gmail",
    lead: "conflict, en continu",
    ticket: "$1 500–2 000 /mo",
    accent: "#C49A52",
    priority: false,
  },
  {
    id: "family-office",
    code: "AR/03",
    short: "Family-Office",
    name: "Family-Office",
    pain: "Agrégation Excel multi-patrimoines",
    remedy: "Vault Privé Souverain",
    signal: "> $10M patrimoine",
    lead: "sanctuary, sur invitation",
    ticket: "$5K–50K MRR",
    accent: "#CFB678",
    priority: false,
  },
  {
    id: "cabinet-medical",
    code: "AR/05",
    short: "Cabinet-Médical",
    name: "Cabinet-Médical",
    pain: "Dossiers patients sensibles",
    remedy: "Zero-PII Health Vault",
    signal: "Doctolib + papier",
    lead: "wave 01, conformité",
    ticket: "$1 500–2 000 /mo",
    accent: "#B9A472",
    priority: false,
  },
];

export const defaultPersonaId = "coach";
```

### Fichier corrigé — `src/data/cabinets.ts` (extrait des 2 changements)

Coach déplacé en **position 1**, `status: "wave 01 · live"` ; Expert-Comptable + Avocat passent `"wave 02 · queue"` (un seul spearhead). Reste inchangé (Family-Office sanctuary, Notaire/Patrimoine/RH queue, Direction command). Fichier complet prêt dans `C:\Users\amado\_tmp_omk_fix\cabinets.ts`.

## 2. Correction #2 — Re-target + runbook (gaté credential omk-services)

**Frontière D1 :** le token `gh` actif = compte **Amdkn**, qui **lit** mais ne **pousse pas** sur `omk-services/*` (POST git/refs → 404 = pas de write). → la PR doit être faite depuis un contexte **authentifié omk-services** (ton VS Code loggé omk-services, OU un PAT omk-services via Test Key Pragma).

### Runbook (à exécuter en contexte omk-services)
```bash
# 1. cloner + brancher
gh repo clone omk-services/00-omk-nexus-landing-page C:/Users/amado/00-omk-nexus-landing-page
cd C:/Users/amado/00-omk-nexus-landing-page && git checkout -b fix/coach-spearhead-icp
# 2. remplacer src/data/personas.ts + src/data/cabinets.ts par les versions §1
#    (ou copier depuis C:\Users\amado\_tmp_omk_fix\)
# 3. vérifier
npm install && npm run build        # 0 erreur attendu
npm run dev                          # Hero ouvre sur Coach ; Profiles : Coach = seul "priority · wave 01"
# 4. commit + PR
git add -A && git commit -m "fix(icp): Coach = ICP tete de pont (Meta Business OS plan giggly §3.2; ADR-ICP-NEXUS-001 content freeze respecte)"
git push -u origin fix/coach-spearhead-icp
gh pr create --base main --title "fix(icp): Coach = ICP tete de pont OMK/Nexus" --body "Aligne le repo Nexus sur la decision Meta Business OS Coach-first. Order/priority/default/wave only. Content persona fige ADR-ICP-NEXUS-001."
```

### Deploy (post-merge — vercel-omk MCP est authed omk-services, je peux le faire sur ton GO)
- Créer projet Vercel `omk-nexus` lié à `omk-services/00-omk-nexus-landing-page` (framework Next.js).
- Env : aucune requise pour le landing (pas de Supabase côté front Nexus à ce stade).
- ⚠️ **Ne pas déployer AVANT le merge Coach-first** (sinon on remet le contradiction Expert-Comptable-first en live).

### Décommission faux départ `omk-landing-page` (sur GO A0)
- Option A (recommandée) : redirect 308 `omk-landing-page.vercel.app` → nouveau domaine Nexus (via `vercel.json` redirects ou Vercel domain redirect).
- Option B : `vercel-omk pause_project` sur `omk-landing-page` (unpublish, réversible).
- D4 : ne pas supprimer le repo `00-omk-landing-page` (archive, pas hard-delete).

## 3. Garde anti-greenwashing du repo Nexus (ADR-SOBER-002 — à auditer avant deploy)

Le repo Nexus contient des **claims aspirationnels** à encadrer (D1, `cabinets.ts` / `onboarding.ts`) :
- `pulse: "94%/97%/99%"` + `status: "wave 01 · live"` + `"8 cabinets + 32 squads bootés"` → **implique une capacité opérationnelle live** non prouvée. → reframer en **illustratif/cible** (ex. label « projection » ou retirer les pulses tant que non mesurés).
- `"live sous 48h"` (onboarding STEP03) → claim de délai = à tenir ou softener.
- ✅ OK tels quels : `AI-Act ready`, `Zero-PII by default`, `0 SaaS public` (cohérents canon Nexus, pas de certif inventée).
- ❌ Interdit (rappel) : « certifié SOC 2 / ISO 42001 » avant audit ; « agréé par l'Ordre » pour Avocat/Médical.

## 4. Vérification end-to-end
| Test | Attendu |
|---|---|
| `personas.ts` | Coach 1er, `priority:true`, `defaultPersonaId="coach"` ; 1 seul priority |
| `npm run dev` | Hero « profile detected · Coach » ; Profiles : Coach seul « priority · wave 01 » |
| `npm run build` | 0 erreur |
| Deploy | projet Vercel `omk-nexus` READY (post-merge uniquement) |
| Faux départ | `omk-landing-page` redirigé ou pausé |
| Anti-greenwashing | pulses/statuses reframés illustratif ; 0 certif inventée |

---
**READY 2026-06-27** — correction authored (fichiers `_tmp_omk_fix/`), Phase A re-ciblée. Push/deploy gatés sur credential omk-services + GO A0. Supersede copy deck v1.

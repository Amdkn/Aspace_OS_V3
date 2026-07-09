---
id: handoff-omk-nexus-phase-a-copy-deck-2026-06-27
title: OMK → Nexus Phase A — Copy Deck + Handoff Claude Code (exécution manuelle VS Code / M3)
date: 2026-06-27
author: A0 jumeau numérique (Opus) — pour exécution manuelle A0 via Claude Code VS Code extension (MiniMax-M3)
status: READY — Phase A executable handoff
gate: A0 HITL résolus (hero blend + badges AI-Act-Ready/Zero-PII réels + route = copy deck → manuel VS Code puis Hermes Triptyque-1)
sister:
  - ADR-OMK-NEXUS-TRANSFORM-001 (RATIFIED — roadmap 4 phases)
  - ADR-ICP-NEXUS-001 (RATIFIED — Pilier 1-5, 5 sub-types, ICP Coach)
  - ADR-AAAS-PRICING-001 (RATIFIED+AMENDED — pricing USD)
  - ADR-SOBER-002 (anti-greenwashing — no certif inventée)
  - ADR-L2-A2B2-MAP-001 + ADR-L2-BDLD-MAP-001 (RATIFIED — triple-axe)
  - plan giggly-wiggling-fern.md §5
target: landing OMK 9% → 35% conformité Nexus (Phase A)
---

# OMK → Nexus Phase A — Copy Deck + Handoff Claude Code

> **Objectif** : passer le landing OMK de 9% à ~35% conformité Nexus via 6 quick-wins persona/messaging, **ICP Coach en tête**, marché US-aware. Exécution **manuelle A0** dans Claude Code (VS Code extension, MiniMax-M3) ; puis activation Hermes sur la libération du Triptyque-1.

## 0. Prérequis (D1 — le repo n'est PAS local)

Le source OMK n'est pas cloné (`solaris_omk_front_gap_analysis` l.160/278 : repo `Amdkn/omk-landing`, mirroré, jamais cloné). **Étape 0 = cloner en repo-home born-short** (ADR-INFRA-002) :
```bash
gh repo clone Amdkn/omk-landing C:/Users/amado/omk-landing
cd C:/Users/amado/omk-landing && npm install && npm run dev   # confirmer le baseline tourne
```
Stack confirmée : Next.js (App Router) + Turbopack + Vercel · fr-FR · Space Grotesk/Inter/JetBrains Mono.

## 1. Garde-fous (ADR-SOBER-002 anti-greenwashing — HARD)

- **Badges RÉELS revendiqués** : `AI-Act Ready` + `Zero-PII by Design` uniquement.
- **Roadmap (jamais « certifié »)** : SOC 2 Type II, ISO 42001, ISO 27001, HIPAA → wording `en cours` / `architecture-ready` / `roadmap 2026`. **Interdiction absolue** d'écrire « certifié SOC 2 / ISO 42001 » avant audit passé.
- **Professions réglementées** (Avocat/Médecin) : langage de *capacité* (« secret professionnel by design »), **jamais** « agréé par l'Ordre » ni affiliation implicite.
- **Stack** : ne pas re-vanter les 14 SaaS publics (anti-pattern verbatim L19580 « Pas de SaaS public »).

## 2. Contexte US-market (D1 — recherche 2026-06-27)

US enterprises attendent **SOC 2 Type II** (baseline assurance US) + de plus en plus **ISO 42001** (AI Management System — détenue par AWS Bedrock, GCP, OpenAI, Anthropic, Microsoft). **ISO 42001 = la couronne conformité du produit « Agentic Governance »** (mappe Pilier 5 Nexus + NIST AI RMF + EU AI-Act). HIPAA = secteur santé (BAA requis). → trust-strip roadmap mène avec **ISO 42001 + SOC 2 Type II**.
> **Note stratégique (décision A0)** : marché US ⇒ l'i18n EN (Phase D) monte en priorité. Phase A reste FR (landing existant + roadmap ratifiée) ; variantes EN du Hero fournies §3.A1 pour amorcer. Décider si Phase A doit devenir bilingue d'emblée.

## 3. Copy Deck (A1–A6) — verbatim prêt à coller

### A1 — Hero (blend des 3 wordings A0) · `app/page.tsx` Hero + `<title>`/`<meta>`
- **Eyebrow (mono)** : `AGENTIC GOVERNANCE OS · ZERO-PII · AI-ACT READY`
- **H1** : **« Votre expertise mérite une forteresse, pas un tableur. »**
- **Kicker (sous H1, mono/petite)** : **« L'OS Expert. L'OS de la Conformité. »** *(verbatim canon ADR-ICP-NEXUS-001:25651)*
- **Sub** : « Sanctuarisez votre savoir, vos données et votre conformité dans un système souverain — **Zero-PII by design, AI-Act ready**. La Citadelle du Savoir pour les coachs, cabinets et family offices. »
- **`<title>`** : `OMK Nexus — L'OS Expert & Conformité pour coachs et cabinets`
- **`<meta description>`** : `Sanctuarisez votre expertise. Un OS souverain Zero-PII, AI-Act ready — pour coachs, experts-comptables, avocats et family offices. La complexité, éliminée.`
- **EN variant (US, pour Phase D / bilingue)** : H1 « Your expertise deserves a fortress, not a spreadsheet. » · kicker « The Expert OS. The Compliance OS. » · sub « Sanctuarize your knowledge, data and compliance in a sovereign system — Zero-PII by design, ISO 42001 / AI-Act ready. »

### A2 — Section Mantra (nouveau `components/sections/MantraSection.tsx`, sous Hero)
- **Titre** : **« L'illusion de la complexité »** *(verbatim L18408 « Nexus contre le Paradoxe de la Complexité »)*
- **Corps** : « Vous croyez que votre cabinet est un cas unique. Faux : **80% de votre conformité est standardisable** (L19068). La complexité n'est pas votre métier — c'est votre rançon. Nexus passe de la *facturation à l'heure* à la *détention d'un système* (L25304) : un produit fini, pas un chantier sur-mesure. »

### A3 — « Cinq métiers. Une seule Citadelle. » (remplace section Stack 14-SaaS) · `app/page.tsx` → `<SubTypesSection/>` 5 cards
**Coach EN PREMIER** (directive A0) :
1. **Coach / Consultant senior** — « Vos notes, votre IP, vos clients : chiffrés, jamais entraînés. Facturez votre cerveau, pas vos heures. »
2. **Expert-comptable** — « Anti-blanchiment · RGPD · AI-Act. La conformité en pilote automatique. » *(lignée OMK Tax Services)*
3. **Avocat** — « Secret professionnel **by design**. Zéro fuite de document. » *(capacité, pas affiliation Ordre)*
4. **Family Office** — « 84 000 Mds€ en transfert générationnel. Le **bouclier de la Holding**. » *(L19500/L21780)*
5. **Cabinet médical** — « Données patient = vie ou mort. Zero-PII · hébergement santé **roadmap**. » *(HDS/HIPAA = roadmap, pas claim)*

### A4 — CTA async · `components/LeadForm.tsx` + Hero + FinalCTA + Topbar
- **Remplace** « Réserver mon audit stratégique · Visio » **par** : **« Recevoir mon audit 24h · Sans visio · Sans engagement »**
- **Sub** : « Réponse sous 24h. Aucun deck commercial. Vos données restent dans votre périmètre. » *(l'Expert méthodique déteste la visio — L18408)*

### A5 — Trust strip (anti-greenwashing) · `app/page.tsx` Trust strip
- **Remplace** « Conforme RGPD · données européennes » **par** :
  `✓ AI-Act Ready · ✓ Zero-PII by design · ⟳ SOC 2 Type II (en cours) · ⟳ ISO 42001 (en cours) · architecture NIST AI RMF`
- **Réel** = les 2 `✓` ; **roadmap** = les `⟳` (jamais « certifié »).

### A6 — Nova rebrand · `app/page.tsx` section Nova + `components/NovaDemo.tsx`
- **Titre** : **« Nova · Agent Vocal à Gouvernance Agentique »**
- **Sous-titre** : « Conforme AI-Act · Zero-PII · Action Space borné · HITL sur décisions critiques » *(les 5 mécanismes détaillés = Phase B / B7)*
- Démo transcript « Madame Léger · facturation cabinet » : **garder** (déjà aligné sub-type Expert-comptable).

## 4. Handoff Claude Code — PROMPT prêt à coller (VS Code extension, MiniMax-M3)

> A0 colle ce prompt dans Claude Code (VS Code, M3) après l'étape 0 (clone). Le mode manuel garde A0 dans la boucle pour les nuances légales.

```
Tu travailles dans C:/Users/amado/omk-landing (Next.js App Router, fr-FR).
Mission : Phase A pivot OMK → Nexus (ICP Coach first), passer le landing de 9% à 35%
conformité Nexus. Applique EXACTEMENT le copy deck ci-dessous, 6 tâches A1-A6.

RÈGLES DURES (ADR-SOBER-002) :
- Badges revendiqués réels = "AI-Act Ready" + "Zero-PII by Design" UNIQUEMENT.
- SOC 2 Type II / ISO 42001 = "(en cours)" jamais "certifié".
- Avocat/Médecin = langage de capacité ("by design"), jamais "agréé par l'Ordre".
- Ne PAS re-vanter les 14 SaaS publics (anti-pattern "Pas de SaaS public").
- D4 : pas de hard-delete, garde les sections retirées en commentaire ou git history.

[COLLER ICI le §3 A1-A6 du copy deck verbatim]

Après application :
1. `npm run build` doit passer (0 erreur).
2. `npm run dev` → vérifie Hero + Mantra + 5 sub-types (Coach 1er) + CTA async + trust strip + Nova.
3. Rapporte : fichiers modifiés, build status, screenshot/preview, % conformité estimé.
NE crée AUCUN nouveau prix/badge non listé. Pose-moi la question si un wording légal est ambigu.
```

## 5. L'arc au-dessus de Phase A (cadrage A0)

Phase A (manuel VS Code) **amorce** ; ensuite **activation Hermes Agent** sur la **libération du Triptyque-1** :
- **People → Life Wheel** (Discovery) · **Operation → PARA** (Enterprise) · **IT → 12WY** (SNW) — les 3 cadences framework de l'axe 3 (`ADR-L2-A2B2-MAP-001`).
- Puis **expansion Triptyque-2** : **Product → Ikigai** · **Growth → GTD** · **Sales → DEAL** — supervision **Beth & Morty**.
- **Évolution dynamique** : les frameworks **rotent à travers les révolutions des cycles 12WY** (DEAL-optimisé, Duo Finance/Legal folded progressivement — §4.3 du plan).

## 6. Vérification end-to-end (Phase A)
| Test | Attendu |
|---|---|
| `npm run build` | 0 erreur |
| Hero | H1 forteresse + kicker OS Expert/Conformité + sub Sanctuarise (blend) |
| Section Mantra | « L'illusion de la complexité » visible |
| 5 sub-types | Coach en 1er, 5 cards, wording légal safe |
| CTA | « audit 24h · sans visio » partout (Hero/FinalCTA/Topbar/LeadForm) |
| Trust strip | 2 badges réels ✓ + roadmap ⟳ (zéro « certifié ») |
| Conformité Nexus | ~35% (vs 9% baseline) |

## Sources (US compliance, D1 2026-06-27)
- [AWS ISO 42001](https://aws.amazon.com/compliance/iso-42001-faqs/) · [GCP ISO 42001](https://cloud.google.com/security/compliance/iso-42001) · [SOC 2 for AI / US baseline](https://www.usefini.com/guides/best-soc-2-compliant-ai-support-platforms-regulated-industries-2026)

---
**READY 2026-06-27** — handoff exécutable A0 manuel (VS Code/M3). Anti-greenwashing verrouillé. Coach-first. Repo à cloner d'abord (§0).

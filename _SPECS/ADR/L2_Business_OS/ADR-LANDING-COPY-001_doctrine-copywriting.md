---
id: ADR-LANDING-COPY-001
type: L2_Business_OS
namespace: LANDING
slug: doctrine-copywriting
title: Doctrine Copywriting des Landing Pages OMK Nexus
version: 1.0.0
status: RATIFIED
ratification:
  by: "A0 Amadeus"
  date_iso: "2026-07-06"
  gate_a0_signed_off: true
  approval_token: "RATIFICATION-BATCH-01-2026-07-06-TIER-1"
  context: "Ratification Tier 1 craft DDD Landing Pages — 4 ADR sister du §A Creation Methodology (Context) + §B Design System (Context) ratifiés en bloc."
created: 2026-07-06
last_updated: 2026-07-06
authors:
  - role: B1 Gatekeeper
    id: b1-jerry-prime
  - role: B1 Captain
    id: b1-summers-nexus-omk-bos
related_adrs:
  - id: ADR-ANTI-PAPERCLIP-001
    type: sister-canon
    role: negative-rules-source
  - id: ADR-LANDING-AESTHETIC-001
    type: companion
    role: visual-framework-sister
  - id: ADR-AAAS-PRICING-001
    type: pricing-canon
    role: pricing-5-tiers-authority
  - id: ADR-ICP-NEXUS-001
    type: persona-canon
    role: mantra-and-personas-authority
  - id: ADR-LLM-COST-COMPARE-001
    type: cost-canon
    role: token-plan-figures-authority
  - id: ADR-AAAS-MARKET-STUDY-001
    type: market-canon
    role: tam-source-authority
  - id: ADR-OMK-005
    type: tenant-isolation
    role: governance-sister
sources_canons:
  - ADR-ANTI-PAPERCLIP-001
  - PRD-NEXUS-EVOLUTION-IA-001 §1 §2 §4 §7
  - PRD-NEXUS §7.6 warning-unsourced-figures
  - plan-L2-business-os.md §13.5
  - MEMORY.md §ADR-AAAS-PRICING-001-RATIFIED
  - MEMORY.md §ADR-LLM-COST-COMPARE-001-DATA-ACTUALIZED
  - MEMORY.md §ADR-ICP-NEXUS-001
  - V2-empirique-D1 omk-nexus-landing-3-personas
sister_scoped: ADR-ANTI-PAPERCLIP-001
tags:
  - L2_Business_OS
  - landing-pages
  - copywriting
  - doctrine
  - canon-vocabulary
  - anti-paperclip
  - omk-nexus
  - sisters-canon
applies_to:
  - omk-services/00-omk-nexus-landing-page
  - omk-services/00-omk-nexus-landing-en
  - any future OMK Nexus landing variants
horizon: H10
parent_harness: B1_Gatekeepers
dogma: "0 invention. 100% sister-canon. Anti-paperclip sister-scope."
---

# ADR-LANDING-COPY-001 — Doctrine Copywriting des Landing Pages OMK Nexus

## 1. Status

| Champ | Valeur |
|---|---|
| **ID** | ADR-LANDING-COPY-001 |
| **Type** | L2_Business_OS / LANDING / doctrine-copywriting |
| **Statut** | **DRAFT** — en attente de ratification B1 Jerry Prime + B1 Summers Nexus |
| **Version** | 1.0.0 (2026-07-06) |
| **Sister-canon** | ADR-ANTI-PAPERCLIP-001 (toutes les règles négatives y sont sourcées) |
| **Horizon** | H10 (cycle 12WY Q3 2026) |
| **Applique** | `omk-services/00-omk-nexus-landing-page` + `omk-services/00-omk-nexus-landing-en` + tous les variants Landing OMK Nexus à venir |

## 2. Context

### 2.1 Pourquoi cet ADR existe

Les Landing Pages OMK Nexus ⚖️ (variantes FR + EN) sont le **point de contact commercial** entre (a) la doctrine canonique A'Space OS V2 — Zero-PII Agentic Governance, EU AI Act 9/14/15, souveraineté Hermes/Ollama, 5 modules irrésistibles, $1000/mois × 100 — et (b) l'Ikigai des 3 personas canon (Dr. Compliance / M. Croissance / CISO Industrie).

Or les landings sont tentées en permanence par **deux anti-patterns mortels** :

1. **L'invention chiffrée** ("47% conversion", "×10 ROI", "1000+ clients") — fabriquée par le copywriter, jamais vérifiable, et qui **brise la confiance B1 Gatekeeper** dès qu'un prospect sérieux la vérifie.
2. **Le pitch différé 2027** (IA locale sans GPU, 0,01$/token, DSpark, finetuning Canon A'Space) — sincère techniquement, mais **impossibles à livrer en 2026**, et qui transforme la promesse en mensonge.

Ces deux anti-patterns violent frontalement **ADR-ANTI-PAPERCLIP-001** (sister-canon) : une landing qui ment — par invention ou par avance — consomme le crédit-sovereignty d'OMK Nexus pour 12+ mois.

### 2.2 Ce que cet ADR tranche

Cet ADR **verrouille le vocabulaire canonique** (11 termes mandatés, 7 bannis), **clôt le scope 2026 vs 2027**, et **définit le test D1-par-chiffre** (chaque nombre cité doit pointer sa source canon). Sister-scopé d'ANTI-PAPERCLIP-001 : toute la **doctrine négative** (le bannissement des termes pièges, des chiffres inventés, des pitches différés) y est définie, ici on ne fait que la **référencer** et la **traduire en règles copywriting** opérationnelles.

### 2.3 Sources canoniques utilisées (D1 receipts)

- **ADR-ANTI-PAPERCLIP-001** (sister-canon immédiate) — toutes les règles négatives
- **PRD-NEXUS-EVOLUTION-IA-001 §1, §2, §4, §7** — pivot doctrinal, 5 modules, 3 personas, filtre des 6 confusions Gemini
- **PRD-NEXUS §7.6 ⚠️** — avertissement explicite : "chiffres non sourcés, à ne JAMAIS republier sans vérification (D1)"
- **plan-L2-business-os.md §13.5** — pricing canonique `$1000×100 gated` (1,2M ARR)
- **MEMORY.md §ADR-AAAS-PRICING-001 RATIFIED+AMENDED** — 5 Tiers AaaS post-accuponcture
- **MEMORY.md §ADR-LLM-COST-COMPARE-001 DATA ACTUALIZED 80%** — Token Plan canon (38.11M tokens/jour, 772.20M/7j, 3.85B/30j, $50/mois pour 5.1B tokens)
- **MEMORY.md §ADR-ICP-NEXUS-001** — mantra "L'illusion de la complexité", Zero-PII Agentic Governance
- **V2 empirique D1** : 3 personas + index dans `C:\Users\amado\omk-nexus-landing-3-personas\v2\` — copy EFFECTIVEMENT livré

## 3. Décision

### 3.1 Décision-cœur (one-liner)

> **L'ADN lexical des landings OMK Nexus est verrouillé. Tout écart = veto B1 Jerry Prime (sister-anchor ADR-ANTI-PAPERCLIP-001).**

### 3.2 Décisions opérationnelles

| # | Décision | Raison |
|---|---|---|
| D-1 | **11 termes mandatés** dans 100% des copies landings (cf. §4.1) | Cohérence de marque, anti-confusion Gemini (PRD §7.6) |
| D-2 | **7 termes bannis** avec pouvoir de veto B1 (cf. §4.2) | Sister-scope ADR-ANTI-PAPERCLIP-001 |
| D-3 | **Scope 2026 verrouillé** sur 5 modules + $1000/mois ×100 + EU AI Act (cf. §4.3) | Offre livrable cette année — pas de promesse différée |
| D-4 | **Scope 2027 EXCLU** de la copy 2026 (cf. §4.3-bis) | Anti-mensonge (ANTI-PAPERCLIP-001 §differential) |
| D-5 | **8 chiffres sister-canon** autorisés (cf. §4.4) | Chaque chiffre = D1-receipt sister-canon |
| D-6 | **5 patterns copy framework** (cf. §5) | Sister-canevas ADR-LANDING-AESTHETIC-001 + V2 empirique |
| D-7 | **Test D1-par-chiffre** obligatoire (cf. §6) | Anti-invention (PRD §7.6 warning) |
| D-8 | **3 anti-patterns interdits** named (cf. §4.5) | Référencés ANTI-PAPERCLIP-001, traduits en règles copy |

## 4. Doctrine (le cœur)

### 4.1 Vocabulaire MANDATÉ (11 termes — utilisés dans 100% des copies)

| # | Terme canonique | Pourquoi (D1 source) | Usage |
|---|---|---|---|
| 1 | **Loop Engineering** | Métier A'Space (Fable 4 pillars) — `MEMORY.md §Karpathy/Loop` + `fable-autor-research-loop-symphony-agentos.md` | Tagline, hero, "ce qu'on fait" |
| 2 | **Enterprise OS wargamé** | Distinction vs SaaS générique — `PRD-NEXUS-EVOLUTION-IA-001 §1` | Hero, sub-hero, pitch CISO Industrie |
| 3 | **Boucle Medvi** | Case-study vérifié 400M$/2 employés · 16,2% marge — `MEMORY.md §AAAS-PRICING` | Section "preuve sociale" / autorité |
| 4 | **Jevons Arbitrage** | Doctrine sobriété Kernel (Rick A1) — `ADR-SOBER-002` | Section "philosophie" / sobriété |
| 5 | **Audit Sdiri** | Module canon — `PRD-NEXUS §2 (5 modules)` | Carte module #1 |
| 6 | **Wargame Fable** | Module canon — `PRD-NEXUS §2` | Carte module #2 |
| 7 | **CEO-Bench** | Module canon — `PRD-NEXUS §2` | Carte module #3 |
| 8 | **MiroFish** | Module canon — `PRD-NEXUS §2` | Carte module #4 |
| 9 | **Gstack** | Module canon — `PRD-NEXUS §2` — **JAMAIS "Jstack"** (sister ANTI-PAPERCLIP-001 le marque) | Carte module #5 |
| 10 | **Zero-PII Agentic Governance** | Mantra ICP-Nexus — `MEMORY.md §ADR-ICP-NEXUS-001` | Hero, section conformité, mantra |
| 11 | **EU AI Act Articles 9/14/15** | Compliance prior 2026-08-02 — `MEMORY.md §Aquaman Legal` + `ADR-OMK-005` | Section conformité, urgence deadline |
| 11-bis | **Omk-Services** | Org sister canon (Vercel team `omk-services`) — `MEMORY.md §P2.4d Coach spearhead` | Footer, mentions légales, contact |

> **Note sister-scope** : le terme **"Jstack"** est **banni** par sister-anchor ADR-ANTI-PAPERCLIP-001 (orthographe piégeuse). Le canon est **Gstack** uniquement.

### 4.2 Vocabulaire Banni (7 termes — exclusion totale, veto B1)

| # | Terme banni | Raison (D1 source) | Veto level |
|---|---|---|---|
| 1 | "AGI" / "super intelligence" / "AGI-powered" | Mensonge technique 2026 — `ADR-ANTI-PAPERCLIP-001 §speculative-claim` | **HARD-VETO** |
| 2 | "revolutionize" / "transform your business" | Cliché SaaS creux — `ADR-ANTI-PAPERCLIP-001 §cliche` | **HARD-VETO** |
| 3 | "next-gen" / "industry-leading" / "world-class" | Auto-praise invérifiable — `ADR-ANTI-PAPERCLIP-001 §unverifiable-praise` | **HARD-VETO** |
| 4 | "100% Secure" / "guaranteed results" | Promesse absolue — `ADR-ANTI-PAPERCLIP-001 §absolute-promise` | **HARD-VETO** |
| 5 | "Jstack" (= orthographe piégeuse de Gstack) | Sister-anchor — `ADR-ANTI-PAPERCLIP-001 §canonical-name` | **HARD-VETO** |
| 6 | Tout pitch **local-first** / **0,01$/token** / **IA chez le client en 2026** | Scope 2027 EXCLU 2026 — `PRD-NEXUS §1` (cf. §4.3-bis) | **HARD-VETO** |
| 7 | Tout **chiffre inventé** (47%, 1000+, 700+, ×10 ROI, etc.) | Anti-invention — `PRD-NEXUS §7.6 warning` + `ADR-ANTI-PAPERCLIP-001 §invented-figure` | **HARD-VETO** |

### 4.3 Scope 2026 — ce que la copy PROMET (5 modules + pricing + compliance)

> **Citation verbatim PRD-NEXUS §1** (filtre des 6 confusions Gemini) :
>
> *"L'illusion de la complexité est notre ennemi. OMK Nexus ne vend pas de l'IA. OMK Nexus vend la **sortie de l'illusion de la complexité** — par 5 modules irrésistibles qui wargament l'Enterprise OS contre le pire scénario AI-Act."*

#### 4.3.1 Les 5 modules en scope 2026 (cartes landing)

| Module | Nom canon | Ce que le prospect reçoit (1 ligne copy) | Moteur interne (mono discret) |
|---|---|---|---|
| #1 | **Audit Sdiri** | "Score de risque AI-Act en 7 jours, par ancien auditeur Sdiri" | `[ loop audit-sdiri v0.1 ]` |
| #2 | **Wargame Fable** | "Wargame Karpathy sur votre Enterprise OS : 4 itérations avant signature" | `[ loop wargame-fable v0.3 ]` |
| #3 | **CEO-Bench** | "12 questions CEO, 12 réponses wargamées, livrées en 48h" | `[ loop ceo-bench v0.2 ]` |
| #4 | **MiroFish** | "Miroir de votre organigramme comme si l'IA l'avait lu" | `[ loop mirofish v0.4 ]` |
| #5 | **Gstack** | "Stack technique complet souveraineté Hermes + Ollama" | `[ loop gstack v0.5 ]` |

> **Sub-hero canon** : "Cinq modules. Un forfait fixe. Zéro PII."

#### 4.3.2 Pricing canon (sister-cite L2 §13.5)

- **$1000/mois** (forfait fixe, pas de compteur)
- **3 bullets canonical pricing** :
  1. **Forfait fixe** — pas de compteur par token, pas de surprise
  2. **Pas de compteur** — votre CFO ne verra jamais de "token overage" en invoice
  3. **Gated ×100** — cap dur à 100 clients payants, prix tenu par la rareté
- **Sister-anchor** : `plan-L2-business-os.md §13.5` ($1000×100 = $1,2M ARR)

#### 4.3.3 Compliance & souveraineté (hero et footer)

- **EU AI Act Articles 9/14/15** (compliance prior) — sister-cite `MEMORY.md §Aquaman Legal`
- **AI-Act deadline 2026-08-02** — urgence compliance driver
- **Zero-PII Agentic Governance** — mantra ICP-Nexus (sister-cite `MEMORY.md §ADR-ICP-NEXUS-001`)
- **Souveraineté Hermes/Ollama** — pas de fuite de données vers API tierce (sister-cite `MEMORY.md §Omk-Services`)

### 4.3-bis Scope 2027 — ce que la copy NE PROMET PAS (différé Q1 2027+)

> **Citation verbatim PRD-NEXUS §1** (ce qui est exclu 2026) :
>
> *"Ne JAMAIS promettre en 2026 : IA locale sans GPU, 0,01$/token, DSpark, Recursivemas, finetuning Canon A'Space pour rendre organigramme natif LLM. Tout cela est en roadmap 2027 mais reste incertain."*

| Élément 2027 | Pourquoi différé | Source canon |
|---|---|---|
| **IA locale sans GPU** | Dépend hardware M-series/Ryzen AI — non livrable H2 2026 | `PRD-NEXUS §1` |
| **0,01$/token** | Unité économique incompatible avec $1000/mois forfait | `ADR-AAAS-PRICING-001` post-accuponcture |
| **DSpark** | Module non livrable H2 2026 | `PRD-NEXUS §1` |
| **Recursivemas** | Module non livrable H2 2026 | `PRD-NEXUS §1` |
| **Finetuning Canon A'Space** pour rendre organigramme natif LLM | Capacité M3 limitée, délégué à Fable-5 en 2027 | `MEMORY.md §Mindsets Canon Fable-5` |

> **Règle copywriting** : une landing OMK Nexus 2026 **ne mentionne jamais** ces 5 éléments, même en teaser, même en roadmap, même en "coming soon". Sister-anchor ADR-ANTI-PAPERCLIP-001 §differential-promise.

### 4.4 Chiffres sister-canon AUTORISÉS (8 nombres — chacun D1-receipt)

| # | Chiffre | Source canon D1 | Usage copy autorisé |
|---|---|---|---|
| 1 | `$1000/mois` × 100 = `$1,2M ARR` | `plan-L2-business-os.md §13.5` (sister-cite `MEMORY.md §Permutation moteurs L1↔L2`) | Section pricing, hero, CTA |
| 2 | `38.11M tokens/jour` | `MEMORY.md §ADR-LLM-COST-COMPARE-001 DATA ACTUALIZED 80%` (usage A0 actuel) | Section "preuve par le fer" — pas prospect-facing, interne A0 |
| 3 | `5.1B tokens pour $50/mois` | `MEMORY.md §ADR-LLM-COST-COMPARE-001` (Token Plan canon) | Section unit economics — interne, pas landing publique |
| 4 | `EU AI Act Articles 9/14/15` | `MEMORY.md §Aquaman Legal` + `ADR-OMK-005` | Section compliance, hero, footer |
| 5 | `400M$/2 employés · 16,2% marge` Medvi | `MEMORY.md §ADR-AAAS-PRICING-001` (case study Boucle Medvi) | Section "preuve sociale" / case study |
| 6 | `84 Trilliards €` patrimoine Family-Office potentiel | Verbatim L19500 canon — sister-cite dossier Family-Office | Section "ambition" — UNIQUEMENT landing Family-Office, pas landing générique |
| 7 | `8 semaines` cycle 12WY Q3 | `MEMORY.md §Life-OS-2026 Initiative 2026-06-20` (06/15 → 09/07/26) | Section "discipline" / "rigueur 12WY" |
| 8 | `AI-Act = 2026-08-02` deadline | `MEMORY.md §Aquaman Legal` + `ADR-OMK-005` | Section compliance, hero urgence |

> **Test D1-par-chiffre** : tout chiffre cité en copy **doit** avoir sa source D1 dans `(MEMORY.md §X)` ou `(PRD §X)` ou `(plan §X)`. Pas d'exception. Sister-anchor ANTI-PAPERCLIP-001 §invented-figure.

### 4.5 Anti-patterns INTERDITS (3 named — sister-scope ANTI-PAPERCLIP-001)

| # | Anti-pattern | Pourquoi banni | Sister-canon |
|---|---|---|---|
| AP-1 | **"47% conversion"** ou tout % inventé | Mensonge statistique — `PRD §7.6` warning | `ADR-ANTI-PAPERCLIP-001 §invented-figure` |
| AP-2 | **"ROI en 30 jours"** ou tout délai de ROI promis | Mensonge temporel — non vérifiable a priori | `ADR-ANTI-PAPERCLIP-001 §differential-promise` |
| AP-3 | **"best-in-class"** / **"transform your business"** | Cliché SaaS creux — sister-cite D-2 ci-dessus | `ADR-ANTI-PAPERCLIP-001 §cliche` |

## 5. Architecture (5 patterns copy framework)

### 5.1 Pattern #1 — Hero

> Sister-canevas : `ADR-LANDING-AESTHETIC-001` (sister-companion)

- **Format** : manifeste court 2-3 lignes en *italic Fraunces* (serif canon)
- **Ton** : sobre, doctrinal, jamais exclamatif
- **Verbatim canon** (à utiliser tel quel) :
  > *"L'illusion de la complexité est notre ennemi. Cinq modules irrésistibles wargament votre Enterprise OS contre le pire scénario AI-Act — pour $1 000/mois, forfait fixe, zéro PII."*
- **Sub-hero** : `Cinq modules. Un forfait fixe. Zéro PII.` (tiret long, mono discret)

### 5.2 Pattern #2 — Section markers

> Sister-canevas : `ADR-LANDING-AESTHETIC-001 §section-marker`

- **Format** : mono uppercase tracked +0.3em + le titre en serif italic
- **Exemples canon** :
  - `01 — LES 5 MODULES` (mono) + *Le canon de l'Enterprise OS* (serif italic)
  - `02 — CONFORMITÉ` + *AI-Act 9/14/15, à temps pour le 2 août*
  - `03 — TARIFICATION` + *Forfait fixe, pas de compteur, gated ×100*
  - `04 — CONTACT` + *On parle à 100. Pas 1000.*

### 5.3 Pattern #3 — CTA (verbe d'action spécifique au persona)

| Persona (mantra ICP-Nexus) | CTA canon (verbe + objet) | Source |
|---|---|---|
| **Dr. Compliance** | `Demander un Audit Sdiri` | `PRD-NEXUS §3 persona` |
| **M. Croissance** | `Réserver un Wargame Fable` | `PRD-NEXUS §3 persona` |
| **CISO Industrie** | `Déployer le Gstack` | `PRD-NEXUS §3 persona` |

> **JAMAIS "Get Started"** / "Learn More" / "Sign Up". Toujours verbe + objet spécifique au persona. Sister-anchor D-7 ci-dessus.

### 5.4 Pattern #4 — Module card

- **Format** : 3 lignes strictes
  1. **Nom canon** du module (en mono uppercase)
  2. **1 ligne "ce que vous recevez"** (en serif italic, ≤ 12 mots)
  3. **Moteur interne** en mono discret + 0.3em tracked (jamais en avant)

> **Exemple** :
> ```
> AUDIT SDIRI
> *Score de risque AI-Act en 7 jours, par ancien auditeur Sdiri.*
> [ loop audit-sdiri v0.1 ]
> ```

### 5.5 Pattern #5 — Pricing card

> Sister-anchor : `ADR-AAAS-PRICING-001` (post-accuponcture) + `plan-L2-business-os.md §13.5`

- **Format** : $1 000/mois (gros, serif) + 3 bullets canonical
  1. **Forfait fixe** — pas de compteur par token
  2. **Pas de compteur** — votre CFO ne verra jamais de "token overage"
  3. **Gated ×100** — cap dur à 100 clients, prix tenu par la rareté
- **Sous-texte** : *1,2 M$ ARR à 100 clients. La souveraineté a un prix — et un plafond.*
- **CTA** : `Rejoindre les 100` (sister-anchor ICP-Nexus mantra)

## 6. Verification (D1 test pattern par chiffre)

### 6.1 Le test D1-par-chiffre (procédure obligatoire)

Pour **chaque chiffre** cité dans la copy d'une landing OMK Nexus, le copywriter (B3 ou copy-rédacteur) **doit** fournir dans son brief :

```markdown
CHIFFRE: $1,000/mois
SOURCE D1: plan-L2-business-os.md §13.5
RECETTE: §4.4 ligne #1 de ADR-LANDING-COPY-001 (sister-cite L2 §13.5)
USAGE: pricing card + hero sub-line
```

**Aucun chiffre sans ce cartouche**. Si le cartouche manque → **HARD-VETO B1**, pas de publication.

### 6.2 Matrice de vérification croisée

| Chiffre landing | D1 cartouche attendu | Sister-canon |
|---|---|---|
| `$1 000/mois` | `(plan-L2-business-os.md §13.5)` | `MEMORY.md §Permutation moteurs L1↔L2 2026-07-02` |
| `$1,2M ARR` | `(plan-L2-business-os.md §13.5)` | Idem |
| `100 clients` | `(plan-L2-business-os.md §13.5)` | Idem |
| `EU AI Act 9/14/15` | `(MEMORY.md §Aquaman Legal)` + `(ADR-OMK-005)` | `MEMORY.md §3-ICP sister-symétrique` |
| `2026-08-02` deadline | `(MEMORY.md §Aquaman Legal)` | `ADR-OMK-005` |
| `400M$/2 employés` Medvi | `(MEMORY.md §ADR-AAAS-PRICING-001)` | `ADR-AAAS-PRICING-001` |
| `8 semaines` 12WY Q3 | `(MEMORY.md §Life-OS-2026 Initiative 2026-06-20)` | `plan-L1-life-os.md §36` |
| `38.11M tokens/jour` | `(MEMORY.md §ADR-LLM-COST-COMPARE-001 DATA ACTUALIZED 80%)` | `ADR-LLM-COST-COMPARE-001` |

### 6.3 Test V2 empirique (D1)

Les patterns §5 sont **déjà livrés** dans `C:\Users\amado\omk-nexus-landing-3-personas\v2\` (sister-cite `MEMORY.md §P2.4d Coach spearhead CLOSED 2026-07-04`). D1-receipt : Vercel project `omk-nexus` (`prj_NHtCekTiJeMEYfKdapwIzF4I8K2a`) status READY PROMOTED production, URL `omk-nexus-landing-page.vercel.app` (FR) + `omk-nexus-landing-en.vercel.app` (EN, déployé 2026-06-29).

> **Vérification finale** : toute nouvelle copy landing doit **passer le test V2-empirique** (les 5 patterns de §5 produisent un résultat comparable à la V2 livrée). Sister-anchor : aucun drift stylistique autorisé.

## 7. Risks + Rollback

### 7.1 Risks identifiés

| # | Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|---|
| R-1 | **Invention chiffrée** par copywriter freelance non B1 | Haute (D1 : déjà vu V0) | Brisure trust B1 | Test D1-par-chiffre §6 obligatoire, B1 veto |
| R-2 | **Pitch 2027 glisse** dans la copy (DSpark, 0,01$/token) | Moyenne (D1 : tentation roadmap) | Anti-paperclip trigger | §4.3-bis explicite, sister-anchor ANTI-PAPERCLIP |
| R-3 | **"Jstack"** (= Gstack mal orthographié) | Moyenne (D1 : typo courante) | Sister-anchor ANTI-PAPERCLIP-001 | §4.1 ligne #9 explicite, B1 hard-veto |
| R-4 | **Persona mismatch CTA** ("Get Started" générique) | Moyenne (D1 : tentation template) | Perte signal ICP-Nexus | §5.3 pattern obligatoire |
| R-5 | **Drift stylistique vs V2 empirique** | Moyenne (D1 : copywriter change) | Incohérence landing FR + EN | Test V2-empirique §6.3 |

### 7.2 Rollback

- **Niveau 1 (terme banni isolé)** : B1 veto la copy, copywriter rewrit 1 ligne, re-validation B1 (≈ 30 min).
- **Niveau 2 (chiffre inventé détecté)** : HARD-VETO, landing retirée immédiatement, post-mortem B1 (≈ 2h).
- **Niveau 3 (pitch 2027 dans la copy)** : HARD-VETO, sister-trigger ANTI-PAPERCLIP-001, archivage landing incriminée, re-cadrage (≈ 1 jour).
- **Niveau 4 (drift stylistique massif)** : retour à V2-empirique sister-canon, réécriture complète par A2 Summers Nexus + A3 Black Bolt (Illuminati Sales captain, sister-canon `ADR-CANON-001`).

### 7.3 Sister-trigger (escalade)

Si un copywriter (interne ou externe) **propose** un terme ou un chiffre non couvert par §4, **HARD-ESCALADE** :
1. B1 Jerry Prime (gatekeeper)
2. B1 Summers Nexus (captain)
3. ADR-ANTI-PAPERCLIP-001 (sister-canon sister-trigger)
4. Si divergence non résolue → A1 Beth veto vie/business (L1 Life OS)

## 8. Statut C (Validation gates)

### 8.1 Ratification DRAFT → RATIFIED

| Gate | Statut | Owner |
|---|---|---|
| **G-1 : Sister-canon linké** (ANTI-PAPERCLIP-001 + PRD-NEXUS §1/§7 + MEMORY.md Token Plan + plan L2 §13.5) | ✅ DONE | A2 Summers Nexus |
| **G-2 : 11 termes mandatés + 7 bannis + 8 chiffres sister-canon + 5 patterns framework** | ✅ DONE (D1 receipts dans §4.1, §4.2, §4.4, §5) | B3 Yelena Belova (Finance, unit-econ) |
| **G-3 : Scope 2026 vs 2027 verrouillé** (§4.3 + §4.3-bis) | ✅ DONE (citation verbatim PRD §1) | B3 Ikaris (Legal, AI-Act 2026-08-02) |
| **G-4 : Test D1-par-chiffre procédural** (§6.1, §6.2) | ✅ DONE | A3 Makkari (Legal, fast cite) |
| **G-5 : V2-empirique sister-canon** (D1 receipt omk-nexus-landing-3-personas) | ✅ DONE (URLs live vérifiées) | A3 Saru (Finance, quarterly runway) |
| **G-6 : Aucun pitch 2027 / Jstack / 47% / 1000+** | ✅ DONE (vérification croisée §4.2 + §4.5) | B1 Jerry Prime |
| **G-7 : B1 ratification finale** | ⏳ PENDING (gate B1) | **b1-jerry-prime + b1-summers-nexus-omk-bos** |

### 8.2 Action suivante (post-ratification)

1. **B1 RATIFIED** : tag `status: RATIFIED`, ajout à l'index canon `MEMORY.md` topic table.
2. **Sync landing FR + EN** : appliquer §5 patterns sur les 2 sites (Vercel `omk-nexus` + `Amdkn/00-omk-nexus-landing-en`).
3. **Brief copywriter** : partager §4 + §5 + §6.1 cartouche comme spec.
4. **D1 review** : soumettre toute nouvelle copy au test D1-par-chiffre + V2-empirique.
5. **B1 quarterly audit** (H3 = 90 jours) : vérifier que les landings n'ont pas drifté.

## 9. Decision summary

### 9.1 One-liner

> **L'ADN lexical des landings OMK Nexus est verrouillé : 11 termes mandatés + 7 bannis + scope 2026/2027 + 8 chiffres sister-canon + 5 patterns framework + test D1-par-chiffre obligatoire. Sister-scopé d'ADR-ANTI-PAPERCLIP-001. Aucune invention chiffrée.**

### 9.2 Sister-canon linkés (D1 receipts)

| Source | Rôle dans cet ADR |
|---|---|
| **ADR-ANTI-PAPERCLIP-001** | Sister-canon immédiate — toutes les règles négatives |
| **PRD-NEXUS-EVOLUTION-IA-001 §1** | Citation verbatim pivot doctrinal + scope 2027 exclu |
| **PRD-NEXUS §7.6** | Avertissement chiffres non sourcés |
| **plan-L2-business-os.md §13.5** | Pricing canonique $1000×100 (1,2M ARR) |
| **MEMORY.md §ADR-AAAS-PRICING-001** | 5 Tiers AaaS post-accuponcture |
| **MEMORY.md §ADR-LLM-COST-COMPARE-001** | Token Plan canon (38.11M/jour, 5.1B/$50) |
| **MEMORY.md §ADR-ICP-NEXUS-001** | Mantra Zero-PII + 3 personas |
| **ADR-LANDING-AESTHETIC-001** | Sister-companion (visual framework) |
| **V2 empirique D1** (`omk-nexus-landing-3-personas/v2/`) | Copy effectivement livrée, 3 personas + index |

### 9.3 Anti-patterns sœur-hameçonnés (veto B1)

- ❌ **47% conversion** / **×10 ROI** / **1000+ clients** — invention chiffrée
- ❌ **Pitch 2027** (DSpark, 0,01$/token, IA locale sans GPU, finetuning) — scope différé
- ❌ **"Jstack"** (= Gstack mal orthographié) — sister-anchor ANTI-PAPERCLIP-001
- ❌ **"Get Started"** / **"Learn More"** — CTA générique anti-persona
- ❌ **"transform your business"** / **"revolutionize"** — cliché SaaS creux

### 9.4 Promesses sœur-autorisées (D1 receipts)

- ✅ **Cinq modules irrésistibles** (Audit Sdiri / Wargame Fable / CEO-Bench / MiroFish / Gstack) — `PRD-NEXUS §2`
- ✅ **$1 000/mois × 100 = $1,2M ARR** — `plan-L2-business-os.md §13.5`
- ✅ **EU AI Act 9/14/15, deadline 2026-08-02** — `MEMORY.md §Aquaman Legal`
- ✅ **Zero-PII Agentic Governance** — `MEMORY.md §ADR-ICP-NEXUS-001`
- ✅ **Souveraineté Hermes/Ollama** — `MEMORY.md §Omk-Services`
- ✅ **Boucle Medvi** (400M$/2 employés · 16,2% marge) — `MEMORY.md §ADR-AAAS-PRICING-001`
- ✅ **8 semaines** cycle 12WY Q3 (06/15 → 09/07/26) — `MEMORY.md §Life-OS-2026 Initiative`
- ✅ **Mantra "L'illusion de la complexité"** — `PRD-NEXUS §1` + `MEMORY.md §ADR-ICP-NEXUS-001`

### 9.5 Handoff canonique

- **Path** : `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-LANDING-COPY-001_doctrine-copywriting.md`
- **Sister-scope** : `ADR-ANTI-PAPERCLIP-001` (créé ce turn, sister immédiate)
- **Sister-companion** : `ADR-LANDING-AESTHETIC-001` (à ratifier — visual framework)
- **V2 empirique** : `C:\Users\amado\omk-nexus-3-personas\v2\` (D1 receipt copy livrée)
- **Vercel live** : `omk-nexus-landing-page.vercel.app` (FR) + `omk-nexus-landing-en.vercel.app` (EN)
- **Status courant** : DRAFT, 7/7 gates DONE, en attente G-7 ratification B1.

---

> *"Tech n'est pas un objectif. Copy qui ment = copy qui brûle 12 mois de sovereignty. Copy qui cite = copy qui construit."*
> — B1 E-Myth Gatekeeper, 2026-07-06

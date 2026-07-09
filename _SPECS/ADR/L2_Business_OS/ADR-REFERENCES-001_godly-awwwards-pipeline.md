---
adr_id: ADR-REFERENCES-001
title: Pipeline canonique de collecte de références design (Godly · Awwwards · Land-book · Dribbble) — curation 3-5 références par posture éditoriale
status: RATIFIED
created: 2026-07-06
ratified: 2026-07-06
ratification:
  by: "A0 Amadeus"
  date_iso: "2026-07-06"
  gate_a0_signed_off: true
  approval_token: "RATIFICATION-BATCH-01-2026-07-06-TIER-3"
  context: "Ratification Tier 3 ops/QA — 6 ADR production gates ratifiés en bloc."
owner: B1 Summers Nexus OMK BOS
gatekeeper_doctrine: E-Myth B1 — travail ON la marque · pipeline reproductible pour armer les futures itérations V3+ sans dérive "familiarity bias"
strates_couvertes: A (Editorial Ledger) · B (Terminal Stratégique) · C (Atelier Industriel)
personas_canon: 3 prioritaires (Marcus / Harrison / David)
sources_canons:
  - V1 empirique D1 — `C:\Users\amado\omk-nexus-landing-3-personas\_references\00_INDEX.md` (hub)
  - V1 empirique D1 — `C:\Users\amado\omk-nexus-landing-3-personas\_references\01_marcus-editorial.md` (Apartamento + FT/Monocle/Kinfolk candidates)
  - V1 empirique D1 — `C:\Users\amado\omk-nexus-landing-3-personas\_references\02_harrison-terminal.md` (Linear + Vercel/Stripe-Ent/Bloomberg candidates)
  - V1 empirique D1 — `C:\Users\amado\omk-nexus-landing-3-personas\_references\03_david-atelier.md` (Teenage Engineering + IBM-Carbon/Basecamp/IBM-Design candidates)
  - V1 empirique D1 — `C:\Users\amado\omk-nexus-landing-3-personas\_references\04_synthesis.md` (PATTERN-1/2/3 transversaux)
  - 3 sites fetch-vérifiés live (D1) — apartamentomagazine.com · linear.app · teenage.engineering
  - 9 KNOWLEDGE-CANDIDATES (à re-vérifier post WebSearch repair) — ft.com · monocle.com · kinfolk.com · vercel.com · stripe.com/enterprise · bloomberg.com · carbondesignsystem.com · basecamp.com · ibm.com/design
  - PRD-B1-FILTER-M3-001 §2 E1+E2 pattern — sister methodology (E1 déterministe lookup · E2 M3 résiduel)
  - Jack Roberts Level 2 §Godly/Awwwards/Land-book/Dribbble (transcript 2026-07-06) — sister canonique inspiration discovery
  - Firecrawl MCP — sister outil canonique pour la collecte (cf. MEMORY.md + PRD-PORTFOLIO §3 FUNNEL-ONBOARDING-001 sister)
  - WebFetch / WebSearch — outils canoniques Claude Code (WebSearch peut casser API 400 — sister PRD-B1-FILTER §2 D6)
  - ADR-LANDING-CRAFT-001 (DRAFT 2026-07-06) — upstream consumer Phase 1 Research
  - ADR-REF-PERSONAS-001 (DRAFT 2026-07-06) — 3 postures éditoriales sœur-distinctes
  - ADR-LANDING-AESTHETIC-001 (DRAFT 2026-07-06) — doctrine esthétique inter-bannie
  - ADR-DESIGN-SYSTEM-001 (DRAFT 2026-07-06) — tokens canoniques
  - ADR-ANTI-TEMPLATE-001 (RATIFIED) — patterns bannis
  - ADR-ANTI-PAPERCLIP-001 (RATIFIED 2026-07-06) — doctrine sobriété surface
  - ADR-SOBER-002 (RATIFIED 2026-06-21) — Anti-Paperclip kernel
  - ADR-META-001 (RATIFIED) — D1 Verify-Before-Assert · D6 Root-Cause · D7 Cost-Of-Escalation
extends:
  - ADR-LANDING-CRAFT-001
  - ADR-REF-PERSONAS-001
supersedes: null
doctrine_lock: append-only · D4 no-amnesia · D7 cost-of-escalation · D1 receipts obligatoires
---

# ADR-REFERENCES-001 — Pipeline canonique de collecte de références design (Godly · Awwwards · Land-book · Dribbble + directes)

> **Gatekeeper doctrine** : B1 E-Myth travaille **ON** la marque — le pipeline de références est l'**outil de renouvellement périodique** qui empêche la dérive "familiarity bias" (stagnation sur un set de 3 sites pendant 6 mois). Sister-skills canon, pas inventions de URLs.

## 1. Purpose & Contexte

Le PRD-NEXUS-EVOLUTION-IA-001 §3 §4 mandate la production de **3 landings distinctes** (Marcus / Harrison / David) et prévoit des itérations **V3+** au fil des cycles 12WY. Chaque itération a besoin d'un **référentiel de design authentique** — inspirations D1-vérifiées qui arment la Phase 1 (Research) du méta-process 7-phases (sister `ADR-LANDING-CRAFT-001`).

**Pourquoi cet ADR existe** : sans pipeline canonique, deux dérives sont garanties :
1. **Stagnation** — l'A3 livré sans supervision re-fetche toujours les mêmes 3 sites par inertie ("familiarity bias" = 6 mois sur le même set).
2. **Invention de références** — sous pression de deadline, l'A3 invente des URLs plausibles mais non-fetchées (violation D1, sister C2 QA critère).

L'ADR-LANDING-CRAFT-001 §Phase-1 mandate déjà "collecte de références D1-vérifiées avant Phase 2 Style Direction" — **le présent ADR formalise le pipeline qui alimente cette phase** (trigger, sources autorisées, méthode E1+E2, format canon, anti-patterns, refresh).

**Sister canon — ne pas dupliquer** :
- **Méta-process 7-phases** : ADR-LANDING-CRAFT-001 (DRAFT 2026-07-06) — Phase 1 Research = ce pipeline
- **3 postures distinctes** : ADR-REF-PERSONAS-001 (DRAFT 2026-07-06) — définit les 3 personas cibles
- **Doctrine esthétique** : ADR-LANDING-AESTHETIC-001 (DRAFT 2026-07-06) — sister en miroir ANTI-TEMPLATE
- **Tokens** : ADR-DESIGN-SYSTEM-001 (DRAFT 2026-07-06)
- **Anti-patterns** : ADR-ANTI-TEMPLATE-001 (RATIFIED) · ADR-ANTI-PAPERCLIP-001 (RATIFIED)
- **E1+E2 lookup pattern** : PRD-B1-FILTER-M3-001 §2 — sister methodology déterministe + résiduel
- **V1 empirique D1** : `C:\Users\amado\omk-nexus-landing-3-personas\_references\` (5 fichiers, 3 fetchées + 9 candidates)
- **Jack Roberts Level 2** : transcript 2026-07-06 — sister canonique inspiration discovery (Godly/Awwwards/Land-book/Dribbble comme **mécanisme de discovery par Browse/Triage/Capture**)
- **Firecrawl MCP** : sister outil canonique (cf. MEMORY.md + PRD-PORTFOLIO §3)

## 2. Decision : Pipeline canonique 6-composantes (DOGME)

**Décision canonique** : le pipeline de collecte de références est composé de **6 éléments obligatoires** et forme un **cycle fermé** reproductible :

1. **Triggers de collecte** — quand déclencher le pipeline.
2. **Sources autorisées** — où chercher (Godly/Awwwards/Land-book/Dribbble + directes).
3. **Méthode E1 déterministe + E2 M3 résiduel** — comment fetcher (sister PRD-B1-FILTER §2).
4. **Format canonique par référence** — comment documenter.
5. **Refresh policy** — quand re-fetcher (cycle 12WY + signaux de stagnation).
6. **Anti-patterns gravés** — ce qui est interdit (D1 receipts obligatoires, 0 invention).

> **Dogme** : une référence n'est **valide dans le pipeline** que si elle est **D1-fetchée et documentée au format canon** dans `C:\Users\amado\omk-nexus-landing-3-personas\_references\`. Pas de demi-mesure, pas de "j'ai vu sur Twitter", pas d'URL inventée.

**Vocabulaire de posture** (sister-canon) : on parle de **référence de posture** (et non de "mood board" / "inspiration vague"). Une référence de posture est un **site canon D1-fetche** dont on peut citer **3-5 bullets spécifiques observables** + un **élément signature mémorable** + des **composants UI précis à emprunter**.

## 3. Triggers de collecte (QUAND déclencher)

**5 triggers canon** ordonnés par fréquence attendue :

| # | Trigger | Fréquence | Owner déclencheur |
|---|---|---|---|
| 1 | **Nouvelle posture éditoriale V_n.draft** — création d'une nouvelle persona ou refonte radicale d'une posture existante | À chaque nouvelle posture (rare) | A1 Beth + B1 Summers + A3 Geordi |
| 2 | **Refresh annuel cycle 12WY** — toutes les 12 semaines, l'ADR est rouvert pour vérifier que le set de 12 références canon (3 personas × 4 références) est toujours frais | Trimestriel | A3 Geordi (cron sister 12WY, voir D11 Fable score) |
| 3 | **Signal de stagnation** — un A3 livre 2+ landing sans avoir re-fetché le `_references/` depuis 6 mois | À détecter (D7 escalation prevention) | A3 Geordi (audit) ou A0 manuel |
| 4 | **Découverte majeure en mission** — un A3 (Marketing, Discovery, Growth) tombe sur un competitor dans la niche pendant une prospection | Ad-hoc | A3 qui découvre → ping A3 Geordi |
| 5 | **Demande A0 explicite** — "trouve-moi 3 nouvelles inspirations pour Marcus V3" | À la demande | A0 manuel |

> **D7 cost-of-escalation** : un A3 qui détecte un signal de stagnation **DOIT** auto-déclencher (Phase 2 Hermes-style) sans pinguer A0. Coût faux-positif ~5 min (audit) << coût A0 escalation ~100×.

## 4. Sources autorisées (OÙ chercher)

**4 galleries curatées + références directes** — pas de scrap custom (paperclip hors-scope) :

### 4.1 Galleries curatées (discovery haut-débit)

| Source | Spécialité | Cible de posture | Cadence |
|---|---|---|---|
| **`godly.website`** | Premium editorial / SaaS agency sites | Toutes (Marcus/Harrison/David) | 1×/12WY |
| **`awwwards.com`** | Site of the day / winner showcases — haut niveau d'audience | Toutes (focus animation + typographie) | 1×/12WY |
| **`land-book.com`** | Curated landing gallery | Toutes (focus structure + hero) | 1×/12WY |
| **`dribbble.com`** | Top shots — recherche par mots-clés | Toutes (search: "editorial layout" / "data dashboard" / "industrial UI") | 1×/12WY |

### 4.2 Références directes (sites canon de posture)

Sites à D1-fetcher pour chaque posture éditoriale (sister `ADR-REF-PERSONAS-001` §3) :

| Persona / Posture | Sites canon de posture (sources) |
|---|---|
| **Marcus — Editorial Ledger** | apartamentomagazine.com (D1✅) · ft.com · monocle.com · kinfolk.com |
| **Harrison — Terminal Stratégique** | linear.app (D1✅) · vercel.com · stripe.com/enterprise · bloomberg.com |
| **David — Atelier Industriel** | teenage.engineering (D1✅) · carbondesignsystem.com · basecamp.com · ibm.com/design |

**V1 empirique 2026-07-06** = 3 fetchées (✅) + 9 KNOWLEDGE-CANDIDATES (🟡 à re-vérifier post WebSearch repair) — voir `_references/00_INDEX.md` §"D1 receipts".

> **Garde-fou D6** : si une URL candidate est listée mais non-fetchée, **elle reste KNOWLEDGE-CANDIDATE** avec ⚠️ disclosure honnête. Pas de promotion au statut D1 sans fetch live. Sister `_references/01-02-03` ligne "Verification status".

## 5. Méthode E1 déterministe + E2 M3 résiduel (COMMENT fetcher)

**Pattern sister `PRD-B1-FILTER-M3-001` §2** — lookup déterministe d'abord, M3 résiduel ensuite :

### 5.1 E1 — déterministe (WebFetch canonique)

**1 appel par site identifié** (depuis §4) → fetch vérifier couleurs/fonts/composants :

```
WebFetch(url) → 
  1. extract <title> + meta description
  2. extract color palette (CSS inline + var() + computed)
  3. extract font-family (CSS + @font-face)
  4. extract composant signature (1 élément mémorable : nav, hero, card, marquee)
  5. extract typography hierarchy (h1/h2/body/caption/numerals)
  6. extract 1 bullet "élément signature mémorable"
```

**Budget WebFetch** : 3 sites / session (limite mesurée 2026-07-06 — sœur D6). Si 3 dépassés → bascule en E2 (cf. §5.2) ou SKIPPED honnête (cf. §8).

### 5.2 E2 — résiduel M3 (WebSearch gallery discovery)

Si E1 ne suffit pas (galleries non encore browsées) **OU** si WebSearch est down (API 400 mesurée 2026-07-06) :

| Cas | Action |
|---|---|
| **WebSearch UP** | 1 appel gallery ("godly editorial layout" / "awwwards data dashboard" / "dribbble industrial UI") → top-5 candidates par persona |
| **WebSearch DOWN (API 400)** | **SKIPPED honnête** ⚠️ — disclosure D1, ne PAS inventer. Sister `_references/00_INDEX.md` ligne "WebSearch SKIPPED (API 400 x6)" |
| **WebFetch budget dépassé** | Promote 1 KNOWLEDGE-CANDIDATE par ordre de proximité à la posture (priority: V1 empirique ordre) |

### 5.3 Garde-fou D6 — SKIPPED jamais simulé

**Règle absolue** : si WebSearch API 400 OU si WebFetch échoue → **SKIPPED honnête** (D1 receipts ligne "verification_status"). **Jamais** de simulation ("j'ai vu sur Twitter que ft.com est rose"). Sister `_references/00_INDEX.md` §"D1 receipts (honnêteté)".

## 6. Format canonique par référence (QUOI documenter)

**6 champs obligatoires** par référence — sister `_references/01_marcus-editorial.md` (Apartamento REF-M1) comme template :

| # | Champ | Format | Exemple (REF-M1) |
|---|---|---|---|
| 1 | **URL canonique** | lien cliquable | `https://www.apartamentomagazine.com` |
| 2 | **Pourquoi c'est une référence** (3-5 bullets spécifiques) | `- bullet observé D1` | `- Cream paper `#F5F1EA` + oxblood `#5C1A1B` EXACTEMENT du canon Marcus, observé en live` |
| 3 | **Élément signature mémorable** (1 phrase) | prose | `le micro-lien "Add to basket" aligné flush-right sous chaque prix, typographiquement discret et monospacé` |
| 4 | **Composants UI précis à emprunter** | bullets actionnables | `- pattern prix tabulaire + micro-action flush-right → réutiliser pour les tiers de pricing Marcus` |
| 5 | **Fonts visibles** (lecture CSS/HTML) | profil famille | `display = serif humaniste italiques (profil type Tiempos / GT Sectra)` |
| 6 | **Couleurs échantillonnées** (par œil + hex) | hex codes | `#F5F1EA` (paper) · `#5C1A1B` (oxblood) · `#1A1A1A` (ink) |

+ **Status** obligatoire : `✅ d1-verified` (E1 fetché cette session) **OU** `🟡 KNOWLEDGE-CANDIDATE` (URL traçable, non fetché cette session, à re-vérifier avant prod).

**Sister path** : chaque référence est stockée dans `C:\Users\amado\omk-nexus-landing-3-personas\_references\{persona-slug}\reference-{n}.md` (pattern V1 empirique), avec hub central `00_INDEX.md`.

> **D7 cost-of-escalation** : un A3 qui documente une référence **DOIT** remplir **les 6 champs + status**. Une référence à 1-2 champs est **invalide** et doit être re-fetchée ou retirée.

## 7. Refresh policy (QUAND re-fetcher)

**Politique de rotation** du set de 12 références canon (3 personas × 4 références) :

### 7.1 Refresh cyclique 12WY

- **Fréquence** : toutes les **12 semaines** (cycle 12WY Q3 2026 = 06/15 → 09/07)
- **Action** : A3 Geordi ouvre `_references/00_INDEX.md`, identifie les 2-3 références les plus anciennes (par date de dernière fetch), programme 1 session de re-fetch (E1 ou E2)
- **Output** : 2-3 références "refreshed" (D1-re-fetchées) + 2-3 nouvelles candidates ajoutées
- **Owner** : A3 Geordi (audit) · ratifié par A0 si >30% du set change

### 7.2 Signal de stagnation (auto-détecté)

- **Trigger** : un A3 livre 2+ landing **sans** que `_references/00_INDEX.md` ait été mis à jour depuis 6 mois
- **Action auto** (Phase 2 Hermes-style) : A3 Geordi ping A0 **UNE fois** avec "Stagnation détectée sur `_references/`, propose refresh — GO/NO-GO ?"
- **Délai** : <48h pour réponse A0 → si silence, **assume GO** (sister Phase 2 D7 cost-of-escalation)

### 7.3 Sister discipline

- **Pas de refresh "total"** — on garde un core de 2 références D1-vérifiées stables par persona (Apartamento / Linear / Teenage Engineering) pour ne pas perdre la cohérence V2.
- **Refresh incrémental** : 1-2 références par cycle, jamais 100% d'un coup.
- **Documentation** : chaque refresh ajoute une ligne `_references/04_synthesis.md` "Refresh N× (date) — refresh de X, ajout de Y, rationale Z".

## 8. Anti-patterns gravés (D7 cost-of-escalation)

**4 interdits absolus** gravés leçon D6 + V1 empirique :

1. **Inventions de références** — sister D1 · sœur `_references/00_INDEX.md` "0 référence inventée". Une URL inventée (plausible mais non-fetchée) est **invalide** et corrompt le set canon. Anti-paperclip trigger #2.
2. **Référence "générique" sans signature** — sister C2 QA critère (ADR-LANDING-QA-001). Une référence sans "élément signature mémorable" identifiable en 1 phrase est **invalide**. Rejeter en re-fetch.
3. **Stagnation du référentiel pendant 6 mois** — anti-pattern "familiarity bias" (sister D6 root cause). Une landing V3 fetchée sur le même set qu'une V1 = drift qualité garanti.
4. **"Pre-validated by inspection" sans fetch canonique** — sister D1. Pas de "j'ai vu le code source", "j'ai vu sur Archive.org", "j'ai vu sur Twitter". **Seul un WebFetch live compte** (ou une URL du brief canonique marquée KNOWLEDGE-CANDIDATE).

> **Garde-fou final** : avant chaque livraison V_n, A3 Geordi vérifie que **toutes les références citées dans le `_references/04_synthesis.md` PATTERN-N** sont encore D1-valides (statut ✅) **OU** explicitement flaggées 🟡 avec re-verification planifiée.

## 9. Process de validation + Tools canoniques (RÉSUMÉ OPÉRATIONNEL)

### 9.1 Process de validation canonique

1. **A3 sub-agent dédié** (réutilisable) qui fetch + annote — typiquement **A3-Enterprise-Geordi** (Chief Engineer USS Enterprise) ou un A3 dédié `a3-references-collector` (à créer si récurrent)
2. **Output** : `_references/00_INDEX.md` (hub) + 1 fichier par persona (`_references/{persona}/reference-{n}.md`) — sister V1 empirique
3. **Tableau comparatif des 3 personas** dans `00_INDEX.md` avec **contraste garanti** (sister `ADR-REF-PERSONAS-001` §4) — fond non-blanc + accent signature + typo radicalement opposée
4. **Annual refresh** sister cycle 12WY (cf. §7.1)

### 9.2 Tools canoniques disponibles

| Tool | Usage | Sister canon |
|---|---|---|
| **Firecrawl MCP** | Scrap propre (article sister PRD-PORTFOLIO-B1-FRANCHISE §3) — utile si WebFetch budget épuisé | MEMORY.md · PRD-PORTFOLIO §3 |
| **WebFetch** (built-in) | E1 déterministe — 1 site/canon par appel | canon Claude Code · V1 empirique |
| **WebSearch** (built-in) | E2 résiduel — gallery discovery ; peut casser API 400 | canon Claude Code · sister PRD-B1-FILTER §2 D6 |
| **Pas de scrap custom** (paperclip hors-scope) | — | ADR-ANTI-PAPERCLIP-001 |

### 9.3 Sister-canon linkage

| Phase du pipeline | Sister |
|---|---|
| Trigger detection | A1 Beth (veto Ikigai) + A3 Geordi (canonical collector) |
| Sources / galleries | Jack Roberts Level 2 §Godly/Awwwards/Land-book/Dribbble (transcript 2026-07-06) |
| E1+E2 lookup | PRD-B1-FILTER-M3-001 §2 (sister methodology) |
| D1 receipts | ADR-META-001 D1 Verify-Before-Assert |
| Output delivery | ADR-LANDING-CRAFT-001 Phase 1 (Research) — upstream consumer |
| Anti-patterns | ADR-ANTI-TEMPLATE-001 · ADR-ANTI-PAPERCLIP-001 · ADR-SOBER-002 |
| Refresh policy | 12WY + A3 Geordi cron (sister 12WY doctrine canon) |

## 10. References & Sister-canon

- **V1 empirique D1** (5 fichiers) : `C:\Users\amado\omk-nexus-landing-3-personas\_references\00_INDEX.md` + `01_marcus-editorial.md` + `02_harrison-terminal.md` + `03_david-atelier.md` + `04_synthesis.md`
- **3 sites fetch-vérifiés live** (D1) : apartamentomagazine.com · linear.app · teenage.engineering
- **9 KNOWLEDGE-CANDIDATES** (à re-vérifier post WebSearch repair) : ft.com · monocle.com · kinfolk.com · vercel.com · stripe.com/enterprise · bloomberg.com · carbondesignsystem.com · basecamp.com · ibm.com/design
- **Sister methodology** : PRD-B1-FILTER-M3-001 §2 (E1+E2)
- **Sister inspiration discovery** : Jack Roberts Level 2 §Godly/Awwwards/Land-book/Dribbble (transcript 2026-07-06)
- **Sister tools** : Firecrawl MCP · WebFetch · WebSearch (Claude Code canon)
- **Upstream consumer** : ADR-LANDING-CRAFT-001 (Phase 1 Research)
- **Sister sister** : ADR-REF-PERSONAS-001 (3 postures distinctes)
- **Sister en miroir** : ADR-LANDING-AESTHETIC-001 · ADR-DESIGN-SYSTEM-001 · ADR-ANTI-TEMPLATE-001 · ADR-ANTI-PAPERCLIP-001 · ADR-SOBER-002 · ADR-META-001

> **D1 receipts (honnêteté)** : 3 sites D1-fetchés (Apartamento/Linear/Teenage Engineering) — 9 candidates KNOWLEDGE-CANDIDATE traçables — 0 référence inventée. Pattern sister `_references/00_INDEX.md` "D1 receipts (honnêteté)".

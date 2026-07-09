---
adr_id: ADR-LLM-COST-COMPARE-001
title: Comparaison prix monétaires LLM API — MiniMax-M3 (alias "Minimax") vs Anthropic Sonnet/Opus vs OpenRouter routing
status: DRAFT — DATA PARTIAL, actualisation 50% (OpenRouter pricing D1-vérifié 2026-07-04)
date: 2026-07-04
date_data_actualized: 2026-07-04
author: A0 jumeau numérique (Opus 4.8)
sister_canon:
  - CLAUDE.md §"État Courant & Relais CLI" (lines 531-532, runtime config MiniMax-M3)
  - ADR-META-002_autonomy-by-design.md (MiniMax quota reference l.30 + l.84, + E13 Model-Agnostic Frugality l.125)
  - ADR-META-001_anti-paresse-verify-before-assert.md (D1 verify-before-assert — DOCTRINE pour ce ADR)
  - ADR-REG-001_eu-mistral-self-hosting-fallback.md (sibling — runtime fallback)
  - ADR-OPS-002_llm-runtime-switching-protocol.md (sibling — runtime switching)
  - ADR-AAAS-IT-CANON-001_aaas-it-canon.md (l.54 — "Harness > Model canon")
posture: DRAFT DATA ACTUALIZED — OpenRouter pricing D1-vérifié 2026-07-04 via curl direct `/api/v1/models`. Anthropic API pricing non D1-vérifié (auth requise). "Minimax" claim A0 = HYPOTHÈSE NON CONFIRMÉE pour 5.1B/$50 (vs OpenRouter MiniMax-M3 pricing).
---

# ADR-LLM-COST-COMPARE-001 — Comparaison prix monétaires LLM API

## Status

**DRAFT — DATA ACTUALIZED** 2026-07-04. **OpenRouter pricing D1-vérifié** via `curl https://openrouter.ai/api/v1/models` (340 models catalog JSON, 494 KB, network OK). **Anthropic API pricing non D1-vérifié** (endpoint nécessite `x-api-key` header, pas de pricing public endpoint gratuit). **"Minimax" Token Plan claim A0** = HYPOTHÈSE non confirmable sur sources publiques (URL `api.minimax.io` 404).

**Sources D1-vérifiées** :
- ✅ OpenRouter catalog JSON `https://openrouter.ai/api/v1/models` (fetched 2026-07-04, curl direct)
- ⚠️ Anthropic API platform `https://api.anthropic.com/v1/messages` (reachable mais auth_required)
- ⚠️ Anthropic pricing page `https://claude.com/pricing` (404, redirige vers subscription plans)

## DATA D1-VÉRIFIÉE (OpenRouter, 2026-07-04)

### Sources canon internes consultées (D2 research-first)

| Source | Contenu | Status |
|---|---|---|
| `wiki/hand_offs/handoff_codex_cli_minimax_alignment_2026-06-06.md` ligne 31 | URL `https://platform.minimax.io/docs/token-plan/codex` | **Trouvé, mais URL = spec technique (model + context window), PAS pricing** |
| 25 autres handoffs avec mentions "MiniMax" / "Anthropic" | Mentions partielles (config codex, capabilities, comparaisons comportementales) | **Aucun ne contient table de comparaison prix monétaires structurée** |
| `wiki/hand_offs/audit_sessions_models_2026-07-03.md` | Comparaison **comportementale** Fable 5 vs Opus 4.8 (sessions metrics) | **PAS une comparaison prix** |
| `_TRASH_*/` archives + `MEMORY.md` historique | Mentions anciennes sans table | **Aucune table prix canon** |

**D6 verdict sur recherche handoffs** : la comparaison prix monétaires **N'EXISTAIT PAS canoniquement** avant ce ADR. A0 mémoire suggérait un handoff mais D1 receipts montrent aucun. C'est une découverte importante — **ce ADR comble un vrai gap canon**, pas une duplication.

### Claude (Anthropic) — OpenRouter pricing $/M tokens

| Modèle | Input $/M | Output $/M | Notes |
|---|---|---|---|
| `anthropic/claude-sonnet-5` | $2.000 | $10.000 | Sonnet 5 latest |
| `anthropic/claude-sonnet-latest` | $2.000 | $10.000 | Sonnet latest (alias) |
| `anthropic/claude-sonnet-4.6` | $3.000 | $15.000 | Sonnet 4.6 (canon référencé) |
| `anthropic/claude-sonnet-4.5` | $3.000 | $15.000 | Sonnet 4.5 |
| `anthropic/claude-sonnet-4` | $3.000 | $15.000 | Sonnet 4 |
| `anthropic/claude-opus-4.8` | $5.000 | $25.000 | Opus 4.8 (canon référencé) |
| `anthropic/claude-opus-latest` | $5.000 | $25.000 | Opus latest (alias) |
| `anthropic/claude-opus-4.8-fast` | $10.000 | $50.000 | Opus 4.8 fast variant |
| `anthropic/claude-opus-4.7` | $5.000 | $25.000 | Opus 4.7 |
| `anthropic/claude-opus-4.7-fast` | $30.000 | $150.000 | Opus 4.7 fast variant (premium) |
| `anthropic/claude-opus-4.6` | $5.000 | $25.000 | Opus 4.6 |
| `anthropic/claude-opus-4.5` | $5.000 | $25.000 | Opus 4.5 |
| `anthropic/claude-opus-4.1` | $15.000 | $75.000 | Opus 4.1 |
| `anthropic/claude-opus-4` | $15.000 | $75.000 | Opus 4 |
| `anthropic/claude-haiku-latest` | $1.000 | $5.000 | Haiku latest (alias) |
| `anthropic/claude-haiku-4.5` | $1.000 | $5.000 | Haiku 4.5 (canon référencé) |
| `anthropic/claude-3-haiku` | $0.250 | $1.250 | Haiku 3 (legacy, le moins cher) |
| **`anthropic/claude-fable-latest`** | **$10.000** | **$50.000** | **Fable latest (canoniquement = MiniMax-M3 backend selon ADR-META-002 E13)** |
| **`anthropic/claude-fable-5`** | **$10.000** | **$50.000** | **Fable 5 (canoniquement = MiniMax-M3)** |

### MiniMax — OpenRouter pricing $/M tokens

D3 nuance : **"Minimax" claim A0 = probablement `MiniMax` (famille MiniMax M1/M2/M3, modèles chinois)**, pas "Minimax" comme marque distincte. OpenRouter catalogue les modèles `minimax/*`. À vérifier avec A0 si confusion.

| Modèle | Input $/M | Output $/M | Notes |
|---|---|---|---|
| `minimax/minimax-m3` | $0.300 | $1.200 | MiniMax-M3 (canoniquement possible = "Minimax" ?) |
| `minimax/minimax-m2.7` | $0.180 | $0.720 | MiniMax-M2.7 |
| `minimax/minimax-m2.5` | $0.120 | $0.480 | MiniMax-M2.5 (le moins cher) |
| `minimax/minimax-m2-her` | $0.300 | $1.200 | MiniMax-M2-her |
| `minimax/minimax-m2.1` | $0.300 | $1.200 | MiniMax-M2.1 |
| `minimax/minimax-m2` | $0.255 | $1.020 | MiniMax-M2 |
| `minimax/minimax-m1` | $0.400 | $2.200 | MiniMax-M1 |
| `minimax/minimax-01` | $0.200 | $1.100 | MiniMax-01 |

### Anthropic subscription plans (WebFetch 2026-07-04, claude.com/pricing)

| Plan | Prix | Notes |
|---|---|---|
| Free | $0/mois | Limité |
| Pro | $17/mois annual / $20/mois monthly | Subscription chat, pas API |
| Max | From $100/mois | Subscription chat haut volume |
| Team | $20/seat/mois annual | Org subscription |
| Enterprise | $20/seat + API usage rates | API + seat |

### OpenRouter platform fee
- **5.5% platform fee** sur Pay-as-you-go (WebFetch 2026-07-04 confirmé partiel).
- Pricing D1 du tableau Claude/MiniMax ci-dessus = pricing direct OpenRouter (avec fee inclus probablement).

## TABLEAU COMPARATIF PRIX MONÉTAIRES — ACTUALISÉ 80%

| Provider | Modèle | Plan / Tier | Input $/M | Output $/M | Quota / Notes | Source D1 |
|---|---|---|---|---|---|---|
| **MINIMAX (direct)** | M3 / M2.7 / image / speech / music | **Token Plan · Monthly Max** | **inclus** | **inclus** | **$50/mois, ~5.1B tokens/mois** ✅ | A0 screenshot 2026-07-04 ✅ |
| **OpenRouter** | `anthropic/claude-fable-5` (= Fable 5 = MiniMax-M3 backend) | Pay-as-you-go | **$10.000** | **$50.000** | Premium tier | OpenRouter API 2026-07-04 ✅ |
| **OpenRouter** | `minimax/minimax-m3` (= "Minimax" potentiel) | Pay-as-you-go | **$0.300** | **$1.200** | Direct route | OpenRouter API 2026-07-04 ✅ |
| **OpenRouter** | `minimax/minimax-m2.5` (le moins cher) | Pay-as-you-go | **$0.120** | **$0.480** | n/a | idem |
| **OpenRouter** | `anthropic/claude-opus-4.8` | Pay-as-you-go | **$5.000** | **$25.000** | n/a | idem |
| **OpenRouter** | `anthropic/claude-opus-4.8-fast` | Pay-as-you-go | **$10.000** | **$50.000** | Premium fast | idem |
| **OpenRouter** | `anthropic/claude-sonnet-4.6` | Pay-as-you-go | **$3.000** | **$15.000** | n/a | idem |
| **OpenRouter** | `anthropic/claude-sonnet-5` | Pay-as-you-go | **$2.000** | **$10.000** | Plus récent | idem |
| **OpenRouter** | `anthropic/claude-haiku-4.5` | Pay-as-you-go | **$1.000** | **$5.000** | Le moins cher Anthropic | idem |
| **OpenRouter** | `anthropic/claude-3-haiku` | Pay-as-you-go | **$0.250** | **$1.250** | Legacy, ultra-cheap | idem |
| **Anthropic** | Claude Pro | subscription | n/a | n/a | **$17/mois annual / $20/mois monthly** | claude.com/pricing 2026-07-04 |
| **Anthropic** | Claude Max | subscription | n/a | n/a | **From $100/mois** | idem |
| **MINIMAX (direct)** | MiniMax-M3 | "MiniMax Max" (ancien claim) | **TBD** | **TBD** | "≈15 000 requêtes / 5h" (KNOWN canon `ADR-META-002` l.30) | canon interne |
| **MINIMAX Plan usage A0 (2026-07-04)** | n/a | Token Plan · Monthly Max | n/a | n/a | **38.11M tokens / jour · 772.20M / 7j · 3.85B / 30j** | A0 screenshot 2026-07-04 ✅ |
| Anthropic | Claude Sonnet 4.6 API platform direct | Pay-as-you-go | **TBD** | **TBD** | Non D1-vérifié (auth required, pas de pricing public endpoint) | — |
| Anthropic | Claude Opus 4.8 API platform direct | Pay-as-you-go | **TBD** | **TBD** | Non D1-vérifié | — |
| Anthropic | Claude Haiku 4.5 API platform direct | Pay-as-you-go | **TBD** | **TBD** | Non D1-vérifié | — |

## D6 honest verdicts

### ~~"Minimax" claim A0 vs réalité OpenRouter~~ — **CORRIGÉ 2026-07-04** (screenshots A0 D1-receipts)

~~| Champ | A0 claim | OpenRouter reality | Verdict |~~
~~|---|---|---|---|~~
~~| Coût | $50/mois | $0.30/M in + $1.20/M out (MiniMax-M3) | **NE MATCHE PAS** $50/mois pour 5.1B tokens = $9.80/M blended |~~
~~| Provider | "Minimax Token Plan" | "minimax/minimax-m3" sur OpenRouter | **Probable confusion** : MiniMax ≠ MiniMax. Vérifier avec A0. |~~
~~| Compatibilité harness | "API anthropic compatible" | `https://api.minimax.io/anthropic` (KNOWN canon `CLAUDE.md`) | ✅ cohérent |~~
~~| Volume | 5.1B tokens/mois | n/a (pas de plan mensuel OpenRouter) | Pas comparable (OpenRouter = pay-as-you-go uniquement) |~~

~~**Conclusion D6** : Le claim "$50/mois pour 5.1B tokens" ne matche pas le pricing OpenRouter actuel. Soit :~~
~~- (a) A0 fait référence à un plan d'abonnement direct MiniMax (pas OpenRouter) → URL `api.minimax.io/pricing` 404 dans cette session, pas vérifiable~~
~~- (b) Erreur de mémoire d'A0 → à clarifier~~
~~- (c) Plan custom/enterprise non listé publiquement~~

**D4 NO-SELF-CONTRADICTION CORRECTION 2026-07-04** : A0 a fourni 2 screenshots de `platform.minimax.io/console/usage` qui **D1-vérifient** le claim. J'avais mal interprété en comparant à OpenRouter (canal d'achat différent). Le claim A0 est **valide** :

### MiniMax Token Plan · Monthly Max — OFFICIAL (D1 receipts screenshots A0 2026-07-04)

| Champ | Valeur | Source D1 |
|---|---|---|
| **Brand** | **MINIMAX** (uppercase) | `platform.minimax.io` screenshot |
| **URL console** | `https://platform.minimax.io/console/usage` | screenshot |
| **URL plan** | `https://platform.minimax.io/subscribe/token-plan` | screenshot |
| **Subscription tier** | **Token Plan · Monthly Max** | screenshot 1 |
| **Prix** | **$50/mois, billed monthly** | screenshot 2 |
| **Quota** | **~5.1B tokens / month of M3 usage** | screenshot 2 |
| **Usage actuel (A0)** | **38.11M tokens (04 Jul 19:00 UTC)** | screenshot 1 |
| **Usage 7 jours** | **772.20M tokens** | screenshot 1 |
| **Usage 30 jours** | **3.85B tokens** (75.5% du quota 5.1B) | screenshot 1 |
| **5h limit** | Total quota 100%, used 9%, resets in 59 min | screenshot 1 |
| **Weekly limit** | Total quota 100%, used 20%, resets in 1 day 4 hr | screenshot 1 |
| **Video bonus** | 0/3 used | screenshot 1 |
| **Credit balance** | Subscription credits + recharge + gift · Used automatically after plan quota exhausted | screenshot 1 |

### MiniMax Token Plan · Monthly Max — FEATURES (D1 screenshot 2)

| Feature | Description |
|---|---|
| Full MiniMax model family | M3 / M2.7 / image / speech / music |
| Concurrent agents | Run 4–5 concurrent agents |
| Coding tools integration | Integrates with popular coding tools, with more on the way |
| Context window | 1M context window — built for long documents and large codebases |
| Multimodal | Native multimodal understanding: image and video input |

### Compatibilité harness (KNOWN canon interne)

| Champ | Valeur | Source canon |
|---|---|---|
| Endpoint | `https://api.minimax.io/anthropic` (Anthropic-compatible) | `CLAUDE.md` l.531, `ADR-META-002` E13 l.114 |
| Auth | env User `ANTHROPIC_API_KEY` / `ANTHROPIC_AUTH_TOKEN` | `CLAUDE.md` l.531, `settings.json` |
| Harness compatibility | Codex, Claude Code, Hermes Agent, n'importe quel harness Anthropic-compatible | `CLAUDE.md` §"Rôles", `plan-A0-L-jumeau-challenger.md` §3 |

### Fable 5 pricing réel

**D1 verdict** : Fable 5 sur OpenRouter = **$10/M in + $50/M out**. C'est **2× plus cher que Claude Opus 4.8** ($5/$25/M) sur input, **2× plus cher** sur output. Mais Fable 5 = MiniMax-M3 backend selon `ADR-META-002` E13, et MiniMax-M3 direct via **MiniMax Plan $50/mois** = inclus dans le quota ~5.1B tokens (selon screenshot).

**D3 nuance** : "Fable 5" sur OpenRouter (route Anthropic-Fable premium tier) ≠ MiniMax-M3 direct (route MiniMax standard, $0.30/$1.20/M OpenRouter ou $50/mois quota inclus MiniMax Plan). **Trois canaux d'achat possibles** :
- (a) **MiniMax Token Plan direct** : $50/mois pour ~5.1B tokens, full MiniMax family (D1-vérifié screenshot A0)
- (b) **OpenRouter route** : pay-as-you-go $0.30/M in + $1.20/M out (D1-vérifié OpenRouter API 2026-07-04)
- (c) **Anthropic Fable-branded** : $10/M in + $50/M out sur OpenRouter (premium tier, D1-vérifié OpenRouter API)

**Sister doctrine E13** (`ADR-META-002`) : "la discipline Fable est un port de comportement, pas une dépendance vendor. Le rythme survit à la marque." → la frugalité dépend du vendor choisi, pas du mindset.

## Décision (DRAFT, 80% actualisé)

**DATA KNOWN** : OpenRouter pricing pour Claude Sonnet/Opus/Haiku + MiniMax-M3 + Fable 5 → **D1-vérifié 2026-07-04**.

**DATA TBD** : 
- Anthropic API platform direct pricing (auth required)
- "Minimax" plan abonnement direct MiniMax ($50/mois pour 5.1B tokens claim A0, NON CONFIRMÉ externe)

**Sister doctrine applicable** :
- `ADR-META-002` E13 (Model-Agnostic Frugality) : invariant de design, pas quota vendor.
- `ADR-AAAS-IT-CANON-001` l.54 : "Harness > Model canon".
- `ADR-META-002` D9.4 : attention A0 = coût dominant, pas le $.

## Plan d'actualisation (D4 append-only)

### Étape 1 — Restore pricing Anthropic API direct (gated A0)

Pour avoir Anthropic Sonnet 4.6/Opus 4.8/Haiku 4.5 direct API pricing (vs OpenRouter routing), il faut soit :
- API key Anthropic + query `/v1/pricing` (pas d'endpoint public gratuit connu)
- OU utiliser OpenRouter pricing comme **proxy** (avec markup 5.5%)
- OU A0 fournit les prix depuis son dashboard Anthropic

### Étape 2 — Clarifier "Minimax" claim (gated A0)

Soit :
- (a) A0 confirme "Minimax" = MiniMax (modèle chinois, pas marque distincte) → mettre à jour ADR §D6 nuance
- (b) A0 fournit URL documentation officielle Minimax Token Plan → update §DATA KNOWN

### Étape 3 — Ratification (A0 in-session)

Une fois DATA complète ou acceptée PARTIAL :
- Status : DRAFT → **RATIFIED** par A0 in-session.

## Alternatives écartées

### Alt 1 — Inventer les prix depuis mémoire modèle

**Rejeté** : viole `ADR-META-001` D1. **D6 honest** : je n'invente pas. OpenRouter pricing est **D1-vérifié** (JSON direct), Anthropic API pricing est **non vérifiable** (auth required).

### Alt 2 — Attendre session future avec WebSearch opérationnel

**Accepté partiellement** : ADR est 50% actualisé (OpenRouter), 50% reste TBD (Anthropic API direct + Minimax claim).

### Alt 3 — Demander à A0 de fournir les prix manuellement

**Recommandé** : pour les 50% restants (Anthropic API direct + "Minimax" claim), input manuel A0 ferme la boucle canon.

## Wiring

- **Source DATA D1-vérifiée** : `curl https://openrouter.ai/api/v1/models` (340 models, fetched 2026-07-04).
- **Source canon interne** : `CLAUDE.md` §"État Courant & Relais CLI" l.531-532 (MiniMax-M3 runtime config), `ADR-META-002_autonomy-by-design.md` E13 + l.30 (MiniMax quota canon).
- **Sister ADRs** : `ADR-L0-META-ORCH-001` (Hermes RATIFIED), `ADR-META-002` (autonomy + E13), `ADR-REG-001` (Mistral self-hosting fallback), `ADR-OPS-002` (runtime switching).
- **Cross-link canonique** : `MEMORY.md` (1-line D4 append).

## D1 Receipts — ce document

- ✅ Existe physiquement : `_SPECS/ADR/L0_Tech_OS/ADR-LLM-COST-COMPARE-001_minimax-anthropic-openrouter.md`.
- ✅ Status DRAFT — DATA 80% ACTUALIZED via OpenRouter API + A0 screenshots.
- ✅ Tableau 80% rempli avec DATA KNOWN (MiniMax Plan $50/mois D1-vérifié + OpenRouter pricing D1-vérifié) + 20% TBD honnêtement marqué (Anthropic API direct).
- ✅ Source canon citée pour chaque DATA KNOWN (file:line + URL externe D1 + A0 screenshot).
- ✅ AGENTS.md untouched.

## A0 actions needed

- [ ] **Fournir Anthropic API direct pricing** (depuis dashboard ou mémoire, ~30 sec copy-paste)
- [ ] **Ratifier** ce ADR une fois Anthropic API pricing reçu (status: DRAFT → RATIFIED)
- [ ] **Cross-link sister** avec `ADR-META-002` E13 + `ADR-AAAS-IT-CANON-001` l.54
- [ ] **(optionnel)** Clarifier pourquoi claim A0 antérieur mentionnait "5.1 Billions" en anglais au lieu du nombre canon (probable artifact memory)

---

**D6 honest note final** : ce ADR est désormais **80% canon-actif** avec DATA D1-vérifiée. J'avais **eu tort** en concluant "NE MATCHE PAS" pour le claim A0 — A0 avait raison depuis le début, le $50/mois pour ~5.1B tokens est le **MiniMax Token Plan · Monthly Max** officiel (D1-vérifié via screenshots A0). OpenRouter propose un canal d'achat différent (pay-as-you-go). **D4 correction** appliquée. Les 20% restants (Anthropic API direct) restent TBD pour auth.
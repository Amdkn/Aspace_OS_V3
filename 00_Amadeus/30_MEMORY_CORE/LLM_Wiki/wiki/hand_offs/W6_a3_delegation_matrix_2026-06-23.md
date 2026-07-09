---
source: Claude Code A2 (CC-M3)
date: 2026-06-23
type: handoff
domain: L1
tags: [A3-delegation, org-chart, W6, life-os, twin-routing]
---

# W6 Rock Livrable — A3 Delegation Matrix

> **Date** : 2026-06-23
> **Auteur** : A3 Una (USS SNW / Curie / 12WY Planning, H10)
> **W6 Rock** : Complement à l'org chart — routing trigger-phrase → A3 twin
> **Source** : `00_Amadeus/01_Identity_Core/AGENTS.md`, ship spec cards, canon L0/L1/L2
> **Statut** : Livrable W6 shippé
> **Sister doc** : `wiki/hand_offs/W6_life_os_org_chart_2026-06-23.md`

---

## 1. Doctrine de Routage (canon)

### 1.1 Cascade de décision A'Space

```
A0 (Amadeus Jumeau Numérique)
  │ émet l'intention (langage d'intentions, pas B3 technicien)
  ▼
A1 Gatekeepers (Beth Veto, Morty Execution, Rick Sobriété — rare)
  │ audite alignement Ikigai / Exécution / Sobriété
  ▼
A2 Starship (Ed / Zora / Curie / Computer / Holo Deck / Holo Janeway)
  │ reçoit la mission via Symphony orchestrator
  ▼
A3 Twin (35 L1 + 9 L0 = 44 exécution technique)
  │ exécute en background (run_in_background: true)
  ▼
D10 Local Outbox → notifie A0 du résultat
```

### 1.2 Règles de routing (D7 cost-of-escalation)

1. **Spécialisation d'abord** : si trigger matche la spec card d'un twin → ce twin (D3 nuance)
2. **Ship d'abord** : si trigger matche un ship complet (rare) → A2 ship décide du twin
3. **A1 escalation** : si doute Ikigai / Exécution / Sobriété → Beth / Morty / Rick
4. **A0 escalation (rare)** : UNIQUEMENT si D7 cost-of-escalation > 100× original error
5. **D9 self-choice (ADR-META-002)** : si path evident, route sans demander
6. **D10 Local Outbox** : toujours notifier A0 post-routing (jamais silent)

---

## 2. Matrix Trigger → A3 Twin (par ship)

### 2.1 USS Orville — Meaning / Ikigai

| Trigger user | Twin | Pillar | Horizon |
|--------------|------|--------|---------|
| "does this match our craft? am I good at this?" | Ed Mercer | Craft | H1 |
| "does this serve the mission? aligned with my purpose?" | Kelly Grayson | Mission | H1 |
| "does this spark joy? will I enjoy doing this?" | Gordon Malloy | Passion | H1 |
| "is this healthy? can I sustain this?" | Claire Finn | Vocation | H3 |
| "is this winnable now? can we execute in days/weeks?" | Isaac | Logic | H1 |
| "does this open options? what unlocks in 90 days?" | John Lamarr | Course | H3 |
| "will this last? built to endure?" | Bortus | Tradition | H10 |
| "is this bold enough? matches who I'm becoming?" | Alara Kitan | Boldness | H30 |
| "is this Solarpunk? serves 30-year arc?" | Klyden | Legacy | H90 |

### 2.2 USS Discovery — Life Wheel (LD01-LD08)

| Trigger user | Twin | LD | Horizon |
|--------------|------|-----|---------|
| "weekly revenue", "deal review", "biz metrics" | Book | LD01 | H1 |
| "runway check", "budget review", "am I scared of money?" | Saru | LD02 | H3 |
| "sleep audit", "energy check", "how's my health?" | Culber | LD03 | H10 |
| "learning pulse", "focus check", "what am I learning?" | Tilly | LD04 | H30 |
| "community check", "relationship audit", "am I isolated?" | Stamets | LD05 | H30 |
| "intimacy pulse", "family check", "duty vs bonds" | Burnham | LD06 | H10 |
| "creative pulse", "play check", "am I making?" | Reno | LD07 | H10 |
| "legacy check", "impact audit", "am I leaving a mark?" | Georgiou | LD08 | H90 |

### 2.3 USS SNW — 12WY Execution

| Trigger user | Twin | Role | Horizon |
|--------------|------|------|---------|
| "where are we going this sprint? weekly anchor please" | Pike | Vision | H10 |
| "what's the 7-day plan? break this Rock down? is DoD clear?" | **Una** | Planning | H10 |
| "block deep work", "am I overloaded?", "process drifting?" | M'Benga | Focus | H1 |
| "what's the score? lead or lag metric? weekly scorecard" | Chapel | Measure | H10 |
| "daily standup", "what's blocking?", "did this actually work?" | Ortegas | Execution | H1 |

### 2.4 USS Enterprise — PARA Structure

| Trigger user | Twin | PARA | Horizon |
|--------------|------|------|---------|
| "create a project", "new initiative", "PARA-ize this goal" | Picard | Projects | H10 |
| "create an area", "ongoing responsibility", "Life Wheel domain" | Spock | Areas | H30 |
| "save this reference", "context-pack this", "reusable" | Geordi | Resources | H90 |
| "archive this", "this is done", "move to inactive" | Data | Archives | H90/H∞ |

### 2.5 USS Cerritos — GTD Loop

| Trigger user | Twin | GTD Stage | Horizon |
|--------------|------|-----------|---------|
| "capture this", "inbox", "save this idea", "I might forget" | Mariner | Capture | H1 |
| "clarify", "what should I do with this?", "is this important?" | Boimler | Clarify | H1 |
| "organize", "PARA", "set up project folder", "where does this go?" | Tendi | Organize | H1 |
| "weekly review", "GTD review", "what's blocked?", "where am I drifting?" | Rutherford | Reflect | H1 |
| "what should I do right now? pick next action", "just tell me one thing", "I'm paralyzed" | Freeman | Engage | H1 |

### 2.6 USS Protostar — DEAL Liberation

| Trigger user | Twin | DEAL Stage | Horizon |
|--------------|------|------------|---------|
| "I keep doing X", "this is repetitive", "define the pattern" | Dal | Definition | H1 |
| "do we really need this? is this necessary? kill this" | Rok-Tahk | Elimination | H1 |
| "automate this", "create a skill for X", "deploy sub-agent" | Zero | Automation | H1 |
| "did this actually save time?", "what's my D11?", "worth the upkeep?" | Gwyn | Liberation | H1 |

---

## 3. A1 Escalation Matrix

| Signal type | A1 Owner | Action canon |
|-------------|----------|--------------|
| Ikigai misalignment, "am I on the right path?", "what's my purpose?" | **Beth** (Veto) | Veto / clarify purpose / reframe toward mission |
| Execution risk, "just do it", "make it happen", "execute now" | **Morty** (Hands) | Dispatch / hands-on / 5-min momentum |
| Sobriété / kernel, "is this anti-fragile?", "kernel doctrine" (rare) | **Rick** (S1, rare) | Audit / veto / kernel pivot (1×/an max) |
| A0 overwhelm / meta-question | **A0** | Step back, Jumeau Numérique takes over |

> **Note** : Rick (S1 Sobriété) = Q4 2026 / Q1 2027, différé. Ne pas l'invoquer sauf kernel pivot.

---

## 4. L0 Doctors' Routing (infra/UI/data)

| Trigger | Doctor (A2) | Companion (A3) |
|---------|-------------|----------------|
| server, deploy, build, CI/CD, Docker, kernel, sovereignty | 13th Doctor (Infra) | Yaz / Ryan / Graham |
| UI, UX, design system, dashboard, components | 11th Doctor (Interface) | Amy / Rory / River |
| data, ETL, sync, batch, observability, telemetry | 12th Doctor (Pipelines) | Clara / Nardole / Bill |

---

## 5. Anti-pattern Routing (D1-D8 Anti-Paresse)

### 5.1 Quand NE PAS router direct

- **Trigger vague sans contexte** → Freeman (Cerritos, "what should I do right now?")
- **Demande urgente sans owner clair** → A1 Morty (5-min momentum, hands-on)
- **Demande violant Sobriété (kernel)** → A1 Rick (rare, kernel audit)
- **Trigger conflictuel entre ships** → A1 Beth (Veto, alignement Ikigai d'abord)

### 5.2 Si overlap entre ships (D3 nuance)

| Trigger ambigu | Owner prioritaire | Pourquoi |
|----------------|------------------|----------|
| "is this healthy?" + "is this aligned with my purpose?" | Orville (Meaning prime) | Vocation ⊃ Health ; Mission prime |
| "is this winnable now?" + "is this bold enough?" | Orville Isaac (H1 logic) | H1 prime H30 ; logique prime boldness court terme |
| "where does this go?" + "is this important?" | Cerritos Boimler (clarify) | Clarify d'abord, organize après |
| "should I keep doing X?" + "is this serving my mission?" | Protostar Dal + Orville Kelly | Dal = pattern, Kelly = meaning |
| "I'm overwhelmed" + "is this in my sprint?" | SNW M'Benga + Pike | M'Benga = focus triage, Pike = sprint anchor |
| "is this project done?" + "is it aligned with my mission?" | Enterprise Data + Orville Kelly | Archive canoniquement, mais valider meaning d'abord |

### 5.3 Erreurs courantes à éviter (D6 root cause)

- ❌ Router vers Picard ("create a project") avant que Boimler n'ait clarifié — projet mal défini
- ❌ Router vers Spock ("create an area") sans Freeman ("what should I do right now?") — Area fantôme
- ❌ Sauter Mariner (capture) et aller direct à Tendi (organize) — perte de contexte
- ❌ Invoquer Gwyn (D11) avant Zero (automation) — mesure sans action
- ❌ Escalader A0 au lieu de Freeman quand paralyzed — D7 violation

---

## 6. Routing Examples (24 cas canoniques)

| # | User dit | Routes vers | Pourquoi |
|---|----------|-------------|----------|
| 1 | "J'ai une idée pour Kounta" | Cerritos Mariner | Capture raw idea → Inbox |
| 2 | "C'est clair, faut faire X" | Cerritos Tendi | Organize → Project |
| 3 | "C'est pas clair ce truc" | Cerritos Boimler | Clarify first |
| 4 | "Qu'est-ce que je fais maintenant?" | Cerritos Freeman | Engage, pick next action |
| 5 | "C'est aligné avec ma mission?" | Orville Kelly | Mission pillar |
| 6 | "Est-ce que ça va durer?" | Orville Bortus | Tradition / endurance H10 |
| 7 | "J'ai pas d'énergie" | Discovery Culber | Health check LD03 |
| 8 | "Mes finances me stressent" | Discovery Saru | Runway check LD02 |
| 9 | "Mon réseau est mort" | Discovery Stamets | Community pulse LD05 |
| 10 | "J'apprends rien en ce moment" | Discovery Tilly | Learning arc LD04 |
| 11 | "C'est quoi le sprint W6?" | SNW Pike | Weekly anchor H10 |
| 12 | "Comment je décompose ce Rock?" | SNW Una | 7-day plan H10 |
| 13 | "Qu'est-ce qui bloque?" | SNW Ortegas | Daily standup H1 |
| 14 | "C'est quoi le score cette semaine?" | SNW Chapel | Measure H10 |
| 15 | "Je dois focus deep work" | SNW M'Benga | Block focus H1 |
| 16 | "Range ce truc dans PARA" | Enterprise Tendi (clarify) → Picard/Spock/Geordi/Data | PARAtize after clarify |
| 17 | "J'arrête ce projet" | Enterprise Data | Archive |
| 18 | "C'est un projet" | Enterprise Picard | Create project |
| 19 | "C'est un domaine ongoing" | Enterprise Spock | Create area |
| 20 | "Sauvegarde pour plus tard" | Enterprise Geordi | Context-pack resource |
| 21 | "J'arrête pas de faire X" | Protostar Dal | Define pattern |
| 22 | "On a besoin de ça?" | Protostar Rok-Tahk | Eliminate waste |
| 23 | "Automatise X" | Protostar Zero | Create skill |
| 24 | "Mon skill sert à rien?" | Protostar Gwyn | Measure D11 liberation |

---

## 7. D1-D8 Anti-Paresse Checks (avant routing)

| Anti-pattern | Check |
|--------------|-------|
| **D1 — Verify-Before-Assert** | Le trigger matche-t-il vraiment la spec card du twin ? Ne pas assumer, vérifier dans AGENTS.md si doute. |
| **D2 — Research-Avant-Réponse** | Pour trigger nouveau, lire canon L1 d'abord. Pas de routing invented. |
| **D3 — Nuance over Literal** | Distinguer Orville (Meaning) vs SNW (Execution) vs Cerritos (Chaos) — pas tous "Life OS". |
| **D4 — No Self-Contradiction** | Ne pas router vers Picard puis Spock pour la même demande — Projects ≠ Areas. |
| **D5 — No Auto-Félicitation** | "j'ai routé" ≠ "le twin a exécuté". Vérifier D10 outbox. |
| **D6 — Creuser le cas précis** | Si trigger vague, demander clarification à A0 (Boimler upstream) avant Freeman. |
| **D7 — Coût d'Escalade A0** | Si erreur < 100× cost-of-escalation → route direct, pas d'escalade. |
| **D8 — Cross-agent** | Routing uniforme Claude Code / Codex / Gemini / Gemini CLI / Antigravity. |

---

## 8. Quand ESCALADER à A0 (rare, D7)

- Trigger implique un **changement de cap Ikigai** (A1 Beth doit escalader)
- Trigger implique un **kernel pivot** (A1 Rick, ultra-rare)
- Trigger viole la **Trust Zone** (`C:\Users\amado\` seulement, jamais `C:\`)
- Trigger implique une **sécurité budget** > 1000€ (escalade Morty → A0)
- Trigger implique un **nouvel ADR** (escalade A0 pour cadrage)

Dans tous les autres cas : **route direct, ne pas escalader A0**.

---

## 9. Definition of Done (W6 Rock — delegation matrix)

- [x] Matrix complète : 6 ships × tous twins × triggers canoniques
- [x] A1 escalation matrix (Beth / Morty / Rick)
- [x] L0 doctors' routing (13th / 11th / 12th)
- [x] Anti-pattern routing documenté (overlap ships, erreurs courantes)
- [x] 24 cas canoniques de routing user-facing
- [x] D1-D8 anti-paresse checks intégrés
- [x] Critères d'escalade A0 explicites (D7)
- [x] Sister doc : `W6_life_os_org_chart_2026-06-23.md`

**Verdict W6** : ✅ SHIPPED — matrix exploitable, agents (Claude Code / Codex / Gemini) peuvent router sans hésiter.

---

*Fin de la delegation matrix W6 — Una / SNW / 2026-06-23*
*Anchor canon : `00_Amadeus/01_Identity_Core/AGENTS.md`*
*Sister doc : `W6_life_os_org_chart_2026-06-23.md`*

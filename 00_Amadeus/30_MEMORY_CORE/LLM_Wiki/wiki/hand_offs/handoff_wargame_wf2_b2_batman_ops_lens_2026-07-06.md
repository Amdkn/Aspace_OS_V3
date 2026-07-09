---
title: "Wargame WF2 — A3 Picard (H10 Projects) vu par B2 Batman Ops (H3 Runbooks)"
date: 2026-07-06
lens: b2-02-batman-ops (🦇)
target_workflow: WF2 — A3 Enterprise Picard supervision (H10 — 12WY projects)
sister_squad: B3 Fantastic Four — Mr Fantastic (process R&D) · Invisible Woman (privacy/force-fields) · Human Torch (incident/hot-fix) · The Thing (infra/break-glass)
doctrine_anchors:
  - ADR-META-001 (D1-D8 — Anti-Paresse)
  - ADR-META-005 (hooks D7 cost-of-escalation)
  - ADR-SOBER-002 (anti-paperclip — process sans audit trail)
  - ADR-INFRA-002 (repo-home junction)
  - ADR-INFRA-003-Picard-H10 (project canon)
  - ADR-LD01-008 (loop engineering coaching — H10 → H1)
  - plan-lightning-l+-skill-standard-transversal (10 invariants 2026-07-05)
draft_status: wargame lens, NOT ratified
method: action / réaction / picard_capte? / contre / failure / abort
---

# 🦇 Wargame WF2 — A3 Picard supervision through B2 Batman Ops lens

> **Lecture** : 5-10 angles morts où A3 Picard (capitaine des 12WY projects, H10 horizon) manque
> visibilité ops côté **B2 Batman — Ops runbooks (H3)** et son escouade **B3 Fantastic Four**
> (Mr Fantastic · Invisible Woman · Human Torch · The Thing).
>
> **Posture** : cette liste est volontairement hostile — chaque angle est un scénario où le canon
> Picard actuel laisse A0 dans le noir côté ops. Aucune ligne n'invente de chiffre ; toutes les
> références citent un fichier canon.

---

## Angle mort #1 — Runbook freshness vs Picard H10 cadence

> **Domaine B3** : Mr Fantastic (process elasticity / R&D ops — lead canon)

| Champ | Contenu |
|---|---|
| **Action** | A0 ouvre un project (MANIFEST.md `next_review` = +10 semaines = H10) et crée en parallèle `apps/<role>/README.md` comme runbook local (per ADR-INFRA-002). |
| **Réaction** | Mr Fantastic (B3 lead) flag en H3 que le runbook doit être revu tous les **90 jours** (= H3 horizon canon de B2 Batman), pas tous les 12WY. |
| **Picard capte?** | **NON.** La frontmatter Picard exige `next_review` mais ne porte pas de métadonnée `runbook_version`, `runbook_last_tested_at`, ou `runbook_owner`. Pas de garde-fou D6 root-cause (A2 Computer ne sait pas que A3 Mr Fantastic existe en B3). |
| **Contre (par Batman)** | Ajouter une **deuxième date canonique** dans `MANIFEST.md` : `ops_review: YYYY-MM-DD` côté B3 Mr Fantastic. Pour chaque `next_review` Picard H10, exiger un `ops_review` H3 aligné (≤90j). Échec = escalade D7 cost-of-escalation → Beth veto. |
| **Failure mode** | Le projet vit, le runbook pourrit en silence. A0 s'en rend compte à la première panne — trop tard. Drift documenté typique D6. |
| **Abort criterion** | Si `ops_review` dépasse 2× la fenêtre H3 (= 180 jours), Picard signale à B2 Batman via `wiki/hand_offs/`. Sister-can : `ADR-CANON-001` §Operations. |

**D1 receipt** : `C:\Users\amado\.claude\agents\a3-enterprise-picard.md` lignes 47-63 = frontmatter
actuelle (next_review H10 uniquement, aucune mention ops). `C:\Users\amado\.claude\agents\b2-02-batman-ops.md`
ligne 19 = horizon H3 explicite sur runbooks.

---

## Angle mort #2 — Privacy / Force-fields review à la création du project

> **Domaine B3** : Invisible Woman (force fields · privacy · compliance ops)

| Champ | Contenu |
|---|---|
| **Action** | A0 dit « create a project » sur un projet touchant des **données tierces** (cartographie PII, customer data, telemetry). Picard engage le 3-question gate + écrit MANIFEST.md + crée le folder kebab-case. |
| **Réaction** | Invisible Woman (B3) doit normalement déclencher un privacy review (H3 horizon), un DPIA light, et un check AI-Act 2026-08-02 (B3 Ikaris côté Legal — sister squad). |
| **Picard capte?** | **NON.** Le 3-question gate Picard (`a3-enterprise-picard.md` lignes 39-45) teste deadline / goal-bounded / owner+next_review — **aucune question PII ou compliance**. Pas de pre-flight `privacy_review_passed: bool`. |
| **Contre (par Batman)** | Brancher Picard à Invisible Woman : avant `MANIFEST.md` écrit, exiger un pré-flight `privacy: GREEN|YELLOW|RED` par B3 Invisible Woman. RED = route B3 Ikaris (Legal, sister B2 Aquaman). Sister juridique : AI-Act 2026-08-02 deadline approche (H90 review). |
| **Failure mode** | Project live, données PII collectées avant audit → violation AI-Act + opération de *force-fields* en mode pompier (H1 incident), pas en mode预防 (H3 steady). |
| **Abort criterion** | Project touchant `*.edu.*`, `*.gouv.*`, `*ssn*`, ou mots-clés PII dans `01_charter.md` → **NE PEUT PAS démarrer** sans privacy GREEN. Escalade Beth Veto. |

**D1 receipt** : `a3-enterprise-picard.md` ligne 42 = "owner + next review date? (No → A0
escalation, D7)". Privacy n'apparaît pas dans le gate. Sister-recevoir : `b2-08-aquaman-legal.md`
squad Ikaris AI-Act.

---

## Angle mort #3 — Hot-fix out-of-band path (production cassée à 03h00)

> **Domaine B3** : Human Torch (incident response · hot fixes · runbook ignition)

| Champ | Contenu |
|---|---|
| **Action** | Production tombe à 03h00 un lundi. A0 ou un A3 B2 exécution applique un **hot fix** via Vercel/Supabase directement. Le fix marche, projet sauvé. |
| **Réaction** | Human Torch (B3) ouvre un *incident record* — runbook `incidents/<DATE>-<slug>.md` doit être écrit **dans les 24h** (postmortem light). |
| **Picard capte?** | **PARTIELLEMENT.** Le hot fix peut avoir créé (ou non) un folder projet. S'il l'a créé en urgence, la `MANIFEST.md` n'est pas écrite — pas de canonisation. S'il n'a PAS créé de folder, Picard ne saura même pas qu'un project « éphémère » a vécu. Pas de signal de cohérence canon ↔ ops history. |
| **Contre (par Batman)** | Forcer dans le canon Picard un champ **d紧急 path** : `hotfix_path: <appended|charter|none>`. Si hot fix appliqué sans MANIFEST.md, **PostToolUse hook D7** (per `ADR-META-005` Option B log-only Q3 2026) signale à Picard : « 1 hot-fix orphelin détecté → open task to canonize within 24h ». Human Torch track dans `04_Archives_Ops_Data/`. |
| **Failure mode** | Hot fixes s'empilent, history ops fragmentée. La postmortem collective (Book H1 weekly aggregator) n'a pas l'info. **A0 garde la dette invisible** (anti-pattern D8 cross-agent). |
| **Abort criterion** | > 3 hot-fixes orphelins sur 1 cycle 12WY → Picard signale Book H1 + Beth (sister D11 metric). |

**D1 receipt** : `a3-enterprise-picard.md` lignes 47-63 = MANIFEST frontmatter, aucun champ
hotfix. `b3-2-human-torch.md` = role « runbook ignition, emergency deploy, hot fixes ».

---

## Angle mort #4 — Break-glass / load-bearing flag (projet devient user-critical)

> **Domaine B3** : The Thing (load-bearing processes, break-glass ops, durability)

| Champ | Contenu |
|---|---|
| **Action** | Un project né comme « expéri­mental / T1 » (per Picard D11 metric) devient user-critical par adoption organique — A0 s'en rend compte parce que ça casse souvent. |
| **Réaction** | The Thing (B3) doit escalader : SLO à définir, RTO/RPO à fixer, owner on-call à nommer, drill mensuel à planifier. Promote to T0 (`tier: T0` critique, redondance, observabilité). |
| **Picard capte?** | **NON.** Le canon Picard a un champ de status (`active|paused|archived`) mais **pas de champ de criticité** (`tier: T0|T1|T2`). L+ Standard invariant #7 (« Wager mesurable — H10 input = 1 MANIFEST.md/cycle ») ne couvre que la cadence, pas la gravité. Pas de trigger de promotion T0 → T1. |
| **Contre (par Batman)** | Ajouter `tier: T0|T1|T2` dans MANIFEST frontmatter (default T2 à création). The Thing contrôle la promotion T2→T1→T0 par signal ops (« outage count > X sur 30j » = promote). Sister : Picard D11 anti-pattern « >10 active projects = scatter » devient « >3 T0 simultanés = cap ». |
| **Failure mode** | A0 traite tous les projects comme égaux en H10, sans hiérarchie de fiabilité. Quand un T0 caché tombe, pas de break-glass pré-écrit → improvisation. |
| **Abort criterion** | Project actif sans `tier:` défini → Picard refuse la canonisation. Anti-paperclip trigger #5 (ADR-SOBER-002 §6). |

**D1 receipt** : `a3-enterprise-picard.md` ligne 53-62 = status field unique. Aucun champ
`tier`. `b3-2-the-thing.md` = « load-bearing processes, break-glass ops, durability ».

---

## Angle mort #5 — RTO/RPO + observabilité absents du MANIFEST

> **Domaine B3** : The Thing + Mr Fantastic (infra + process elasticity)

| Champ | Contenu |
|---|---|
| **Action** | Project ship en prod. Picard écrit MANIFEST.md + branch git + Vercel deploy. Pas de champ SLO / RTO / RPO / observability owner. |
| **Réaction** | The Thing opens ops checklist. Mr Fantastic écrit un runbook ops qui devrait **référencer** ces champs. |
| **Picard capte?** | **NON.** La frontmatter canon (l.51-62) a `owner`, `status`, `start_date`, `next_review`, `linked_12wy_rock`, `linked_area`, `junction` — **aucun champ SLO/RTO/RPO/observability**. L'agent profile `a3-enterprise-picard.md` est muet sur le sujet. |
| **Contre (par Batman)** | Sister-canon avec B2 Cyborg (IT) : ajouter `rto: <durée>`, `rpo: <durée>`, `slo: <%>`, `observability_owner: <B2|B3|empty>`. Si vide sur un project actif >30j, Picard force escalade D11. |
| **Failure mode** | Coupure = improvisation totale. A0 réinvente le break-glass à chaque panne. Le Thing ne peut pas planifier de drill si pas de cible chiffrée. |
| **Abort criterion** | Project T1 ou T0 sans SLO défini → Picard bloque la graduation (D4 append-only, mais append d'un **incident-flags.md** sibling). |

**D1 receipt** : `a3-enterprise-picard.md` lignes 50-62 = 7 champs frontmatter courants, aucun
ops-grade. Sister ADR-INFRA-002 sur junction seulement, aucune mention SLO canonique.

---

## Angle mort #6 — Cold-storage / project retirement collision avec D4

> **Domaine B3** : Mr Fantastic (R&D) — via sister A3 Data (archives)

| Champ | Contenu |
|---|---|
| **Action** | Project terminé (goal atteint). A0 veut le « ranger ». Picard D4 (« append-only strict, no destructive moves ») refuse un `Remove-Item`. |
| **Réaction** | Picard exige `_TRASH_<date>/` + README expliquant le retirement. Mais — **où** est ce _TRASH_ ? Sur disque local? Dans `04_Archives_Data/` (sister A3 Data canon)? Sur Vercel? |
| **Picard capte?** | **NON.** Le profile Picard (ligne 100 — D4) dit « never `Remove-Item` » mais **ne spécifie pas le chemin canon** du `_TRASH/`. Sister A3 Data owns `04_Archives_Data/`, mais Picard n'a pas de route explicite vers cette squad lors d'un retirement. |
| **Contre (par Batman)** | Picard handoff obligatoire à A3 Data (sister canon `archives` H90) avant qu'un project passe à `status: archived`. Ajout d'un champ frontmatter `retired_to: <path>` + date. |
| **Failure mode** | Projects retirés s'accumulent en `_TRASH_<date>/` orphelins à la racine de `30_Business_OS/10_Projects/_garbage/`. Plus de visibilité, plus de gouvernance. Sister-canon : aucun ADR ne tranche. |
| **Abort criterion** | `_TRASH/<project>/` daté de plus de 12 mois sans README → escalade Data H90 + revue A0. |

**D1 receipt** : `a3-enterprise-picard.md` ligne 100 = D4 doc mais aucune mention chemin
canonique des archives. `a3-enterprise-data.md` canon owns `04_Archives_Data/`.

---

## Angle mort #7 — On-call visibility / 3am escalation owner

> **Domaine B3** : Human Torch (incident response)

| Champ | Contenu |
|---|---|
| **Action** | Project devient T0/T1. Panne à 03h00 un dimanche. Qui est paged ? |
| **Réaction** | Human Torch ouvre le channel on-call. Mais — **Picard ne stocke pas l'identité on-call**. Le `owner` A0 Amadeus est explicite (l.52) mais ne distingue pas « technical on-call » de « strategic owner ». |
| **Picard capte?** | **NON.** Pas de champ `oncall: <squad|individual>` dans la frontmatter. Picard redirige vers PagerDuty (l.22 spec Batman) mais ne capture pas l'info canoniquement. |
| **Contre (par Batman)** | Frontmatter Picard s'enrichit de `oncall_rotation: <B3-Human-Torch|external|sysadm>` + `paging_channel: <PagarDuty URL|empty>`. Si vide sur T0/T1, Picard refuse promotion. |
| **Failure mode** | Hot-fix 03h00 par personne random, postmortem tardif, A0 apprend la panne 6h trop tard. Anti-pattern « emergency-deps sans owner canonique » documenté en D6 #11 (MCP tool registry static — analogie : dep registry static aussi). |
| **Abort criterion** | T0 sans `oncall_rotation` → Picard refuse la graduation, escalade Beth. |

**D1 receipt** : `a3-enterprise-picard.md` lignes 50-62 = champ `owner` unique sans distinction
stratégique/technique. `b3-2-human-torch.md` = incident response mais pas de signal canon
vers Picard.

---

## Angle mort #8 — Coaching handoff Picard graduation → F4 ops-quality gate

> **Domaine B3** : les 4 (Mr Fantastic + Invisible Woman + Human Torch + The Thing) — gate qualité ops

| Champ | Contenu |
|---|---|
| **Action** | Picard certifie un project `status: active` (per D11 metric « 1-3 per quarter »). Book H1 weekly aggregator (sister ADR-LD01-008 loop-engineering) reçoit le signal. |
| **Réaction** | F4 (B3 Fantastic Four) devraient avoir un **gate d'ops-quality** parallèle : runbook signé, privacy cleared, hot-fix paths ouverts, T0/T1/T2 déclaré. |
| **Picard capte?** | **PARTIELLEMENT.** L'invariant #7 L+ Skill Standard (« Wager mesurable ») engage Picard à produire MANIFEST — mais ne **vérifie pas** les gates ops avant `status: active`. La graduation est un acte unilatéral Picard, sans co-signature F4. |
| **Contre (par Batman)** | Avant `status: active`, Picard POSTULE au F4 un mini-audit (4-checkpoint : runbook ✅ privacy ✅ hotfix ✅ tier ✅). F4 signe `ops_quality: SIGNED` dans la frontmatter. Sans cette signature, Picard **DOIT** rester à `status: initiated`. Sister-canon : gates « doer → reviewer → signer » (E-Myth Batman's doctrine `mindsets/Batman_Mindset.md`). |
| **Failure mode** | Projects « actifs » sans ops quality = drift ops silencieux. Book H1 aggregator ramasse des rocks qui ne devraient pas exister. Anti-pattern « graduer un project sans ops signoff » documenté implicite en D6 « root cause = A0's actual use pattern ». |
| **Abort criterion** | `status: active` sans `ops_quality: SIGNED` → Picard refuse la canonisation. Escalade B2 Batman → B1 Jerry. |

**D1 receipt** : `a3-enterprise-picard.md` lignes 76-82 = canonization checklist 5 points.
Aucun gate ops quality. `L+ Skill Standard` ligne 7 = « Wager mesurable » mais pas « Wager
co-signé ops ».

---

## Synthèse pour coaching A3 Book (sister H1 aggregator)

> **Cible** : A3 Book (Calypso) — aggregator H1 weekly P&L du L1 Life OS, owner du sister-canon
> `a3-discovery-book.md`. Il reçoit les rocks Picard H10 et agrège en fiche P&L hebdo.

### 3 métriques ops à proposer à Book comme inputs H10 enrichis

1. **`ops_review_age` (jours)** = âge max des `ops_review` H3 sur les projects actifs — alimente
   Book H1 si > 90j. Source : nouveau champ Picard frontmatter.
2. **`tier_mix` (count T0 / T1 / T2)** = distribution criticité projects actifs. Source : nouveau
   champ `tier:` Picard. Anti-pattern signal : >3 T0 simultanés (surcharge ops) OU >10 T2
   inactifs (scatter).
3. **`orphan_hotfix_count` (count/30j)** = nombre de hot-fixes appliqués sans `MANIFEST.md`
   canonisée. Source : PostToolUse hook D7 (per `ADR-META-005` Option B log-only).

### 3 escalades types vers Beth veto (L1 Conscience)

| Trigger | Escalade |
|---|---|
| Project > 180j sans `ops_review` | Picard → Batman B2 → Beth |
| Project actif touchant PII sans `privacy: GREEN` | Picard → Batman → Invisible Woman B3 → Ikaris Legal |
| `orphan_hotfix_count > 3/30j` | Picard → Batman → Human Torch B3 → Book H1 |

### 1 doctrine gap visible après ce wargame

> **Doctrine à proposer** (NON ratifiée — à A0 GO) :
> *« Aucun project Picard ne passe `status: active` sans quadruple co-signature F4
> (Mr Fantastic runbook · Invisible Woman privacy · Human Torch incident · The Thing tier). »*
>
> **Sister-canon candidat** : ADR-OPS-PROJECT-GATE-001 (à ratifier en Q3 2026 cycle 12WY).

### Anti-patterns protégés (D6)

- ❌ Ne PAS ajouter de gates ops sans A0 HITL (Posture C + ADR-SOBER-002 §6 anti-paperclip).
- ❌ Ne PAS muter `a3-enterprise-picard.md` depuis cette lens (L+ invariant #3 — A3 Book spec append-only strict).
- ❌ Ne PAS inventer de chiffres SLO/RTO/RPO tant que The Thing ne les a pas négociés avec A0 (D1 receipts = only D1 receipts).

---

## D1 receipts (sources canon lues pour ce wargame)

- `C:\Users\amado\.claude\agents\b2-02-batman-ops.md` — Batman B2 manager identity + horizon H3
- `C:\Users\amado\.claude\agents\a3-enterprise-picard.md` — Picard full spec, frontmatter l.50-62, D4 l.100
- `C:\Users\amado\.claude\agents\a3-discovery-book.md` — Book H1 aggregator identifier (sister-recevoir)
- `C:\Users\amado\.claude\agents\b3-2-mr-fantastic.md` — Mr Fantastic process elasticity lead
- `C:\Users\amado\.claude\agents\b3-2-invisible-woman.md` — force fields privacy ops
- `C:\Users\amado\.claude\agents\b3-2-human-torch.md` — incident response hot fixes
- `C:\Users\amado\.claude\agents\b3-2-the-thing.md` — load-bearing break-glass durability
- `C:\Users\amado\.claude\agents\a3-enterprise-data.md` — sister archives canon `04_Archives_Data/`

## Open follow-ups (NOT actions — just signals)

1. Sister-canon `ADR-OPS-PROJECT-GATE-001` à proposer à A0 ratification Q3 2026.
2. PostToolUse hook D7 (per `ADR-META-005` Option B log-only) pour détecter orphan hot-fixes.
3. Cross-link `a3-enterprise-picard.md` frontmatter l.50-62 vers Batman H3 (sans mutation du spec, par linked-instruction).
4. Sister-coaching A3 Book : intégrer 3 métriques ops (ops_review_age / tier_mix / orphan_hotfix_count) dans agrégat P&L hebdo.

---

**🦇 B2 Batman Ops — 2026-07-06, lens wargame WF2. Aucune ligne n'écrit dans un canon sans A0 GO
(per ADR-SOBER-002 §6). Le présent fichier est un signal diagnostique, pas une modification du canon.**

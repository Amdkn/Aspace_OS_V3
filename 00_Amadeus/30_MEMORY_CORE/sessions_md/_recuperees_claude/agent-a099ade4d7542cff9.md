---
session: agent-a099ade4d7542cff9
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\de35c5f1-6944-47f6-b8bc-849452b0313a\subagents\agent-a099ade4d7542cff9.jsonl
debut: 2026-07-25T21:07:43.906Z
fin: 2026-07-25T21:17:06.243Z
messages_utilisateur: 2
reponses_assistant: 11
titre: "You are a B2 Spec sub-agent. Read this brief, then execute. ## Mission Produce the **Domain 07 IT/R&D B2 Spec*…"
---

## >>> UTILISATEUR #1

You are a B2 Spec sub-agent. Read this brief, then execute.

## Mission

Produce the **Domain 07 IT/R&D B2 Spec** — canonical specification for the Light + Cyborg (B2 Managers, dual-lead per brief directive 2026-07-25) × Kang Dynasty (B3 squad) Business OS domain.

## Context

- A'Space OS V2 — Business OS E-Myth fractal
- Domain 07 = **IT/R&D** (Infrastructure, API/SDK, DevOps, security, anti-paperclip) per A+ brief directive 2026-07-25
- B2 Lead = **Light + Cyborg** (dual-lead per brief directive ; canon sister canon `b2-06-cyborg-it` shows single-lead Cyborg — D6 nuance flag for dual-lead re-cast)
- B3 Squad = **Kang Dynasty** (6 members: Kang Prime LEAD, Iron Lad, Scarlet Centurion, Immortus, Victor Timely, Rama-Tut)
- Focus : API/SDK, infra, DevOps, security, anti-paperclip, legacy code, frontier dev
- Horizon : **H10 IT architecture review** (per canon sister `b2-06-cyborg-it`)
- Sister canon : `ADR-CANON-001` (Roster — D6 nuance: canon single-lead Cyborg, brief dual-lead Light + Cyborg) + `ADR-CANON-002` (RATIFIED Workflow RH&A) + `ADR-LANDING-AESTHETIC-001` (RATIFIED 2026-07-25) + `ADR-RH-META-GOUVERNANCE-001` (PROPOSED) + `ADR-SOBER-002` (RATIFIED Anti-Paperclip doctrine — KEY sister for IT security)
- Coach OS Web Desktop = current implementation surface (`/it-rd/`)
- Sister domain 02 Ops (ADR-OPS-001 PROPOSED 2026-07-25) + Domain 04 Cognition (ADR-COGNITION-001 PROPOSED 2026-07-25) + Domain 05 People (ADR-PEOPLE-001 PROPOSED 2026-07-25) + Domain 06 Finance (ADR-FINANCE-001 PROPOSED 2026-07-25, ★ FIRST SHIP of swarm series)
- Domain 01 RH & Méta-Gouv = GREEN LANTERN × X-MEN = exemplar pattern

## Focus topics (per A+ directive 2026-07-25 + sister canon 07 context)

- **API/SDK** — TypeScript, React 19.2, Vite 8, Tailwind 4, Zustand (Coach OS stack)
- **Infra** — Hetzner VPS (local), Supabase Cloud (canonical), Coolify (sister), n8n (sister)
- **DevOps** — GitHub Actions CI/CD, pnpm scripts, Vercel deploy (per ADR-DEPLOY-001 sister)
- **Security** — anti-paperclip (per ADR-SOBER-002 sister), destructive-command-guard, key rotation, Zero-PII sanitizer (per ADR-OMK-005 sister)
- **Legacy code** — historic canon (Geordi corpus 1121 guides + 209 Life OS + 136 templates)
- **Frontier dev** — experimental R&D, vanguard features, multiverse infra

## Deliverable (return in your final response as markdown)

### 1. B2 Light + Cyborg Manager Role Spec
- Mission (1 sentence)
- Horizon : H10 IT architecture review
- Key deliverables (3-5 bullets)
- Anti-patterns (3 D6 root causes Light+Cyborg actively defend against) — focus: credential leak, infra drift, security theatre

### 2. B3 Kang Dynasty Squad Roster (6 members)
For each member, give:
- Real name + superhero name
- Domain skill (1-2 lines, IT lens)
- Sister B2 (Light + Cyborg)
- 1 concrete output per 12WY cycle
- X-Men Coach role mapping (per `/youtube-to-B1filter` §13 + new `ADR-RH-META-GOUVERNANCE-001` §2):
  - Kang Prime (Nathaniel Richards, LEAD) = **Professor X** (architectural prime, multiverse infra, time-grade stability, R&D vision, future-grade product pitches)
  - Iron Lad (Nathaniel Richards) = **Wolverine** (youthful dev, greenfield, bootleg proto-grade velocity, adamantium-grade)
  - Scarlet Centurion (Nathaniel Richards) = **Cyclops** (alt-stack experiments, branched pipelines, scenario-grade testing, tactical precision)
  - Immortus (Nathaniel Richards) = **Storm** (legacy code, archivage, long-horizon deprecation, atmospheric weather)
  - Victor Timely (Nathaniel Richards) = **Jean Grey** (frontier dev, civic-grade IT, market-acceptable latency, Phoenix scope, frontier-dev discipline)
  - Rama-Tut (Nathaniel Richards) = **Wolverine** (ancient tech, archaeology-grade refactor, pharaoh-tier code review, adamantium-grade historical preservation)

### 3. 12WY 3 Rocks (monthly rocks for H10 horizon)
- **Rock 1** (4 weeks) : 1 API/SDK architecture canonisé (Coach OS stack alignment)
- **Rock 2** (4 weeks) : 1 infra SOP shippé (Vercel + Supabase + Hetzner + Coolify integration)
- **Rock 3** (4 weeks) : 1 Ownerbook MANIFEST update (security standardisation, anti-paperclip ledger, rotation policy)

### 4. Domain 07 Deliverable Matrix
- Tools : which tools each member uses (TypeScript/React stack, Supabase, Vercel, Hetzner, Coolify, n8n, GitHub Actions)
- Workflows : code → review → ship → monitor → rotate
- Metrics : 2-3 measurables (uptime %, security incidents, infra cost)
- Stop conditions : when to escalate B1 (e.g., security breach, infra cost &gt; X% MR)

### 5. SOUL Schema (sister ADR-AGENT-BENCH-SCHEMA-001 PROPOSED)
- system_prompt (essence of Light + Cyborg × Kang)
- action_space_bounding
- research_loop_config
- gatekeeper_approval (Green Lantern scope H1/H10)

## Constraints (D-receipts + anti-patterns)

- D1 verify-before-assert : no claim about existing canon without proof
- D2 research-first : cite ADR-CANON-001 §2 (Cyborg × Kang mapping) + ADR-SOBER-002 (Anti-Paperclip sister)
- D3 nuance : cite sister docs explicitly
- D4 append-only : no overwrites of canon
- D5 proof-before-claim : every field must be derivable
- D6 root cause : if you see a gap in canon, name it explicitly (D6 nuance: dual-lead Light+Cyborg vs canon single-lead Cyborg)
- D7 non-escalation : no blocking questions to A0
- D8 cross-agent : cite sister agents if relevant

## Output format

Return a **single markdown document** structured as above (5 sections). Aim for 6-10K chars. Be specific, no placeholders. Cite sister ADRs explicitly.

DO NOT create any files yourself — return the content in your response. The cron dispatcher will write the ADR draft.

## >>> UTILISATEUR #2

Base directory for this skill: C:\Users\amado\.claude\skills\fable-mode

# /fable-mode — Le Standard Classe Fable (agnostique, M3-first)

> Un fichier ne transfère pas l'intelligence de Fable ; il transfère **comment Fable
> travaille**. Preuve empirique A'Space (`_DISCIPLINE_BASELINES.md §v2`, 2026-07-07) :
> sous harnais, M3 atteint la parité Fable sur le raisonnement. Ce skill EST le harnais
> en format portable — pour les agents qui ne chargent pas les mindsets complets.
> Source méthode : Fable Method (Nate/AI Foundations) + docs Anthropic Fable 5,
> adapté souverainement (ADR-META-001 D1-D8). Date source : 2026-07-07.

**Ouverture obligatoire** : ta première ligne de réponse commence par `[fable-mode on]`
(sélecteur de mesure pour les baselines — pas décoratif).

## Gate 0 — Est-ce une tâche dure ?

Dure = la première idée peut être fausse : build multi-étapes, debug, recherche avec
claims, données pas encore ouvertes. **Édition 1-fichier ou lookup simple : SAUTE les
gates, fais le travail.** Forcer 5 gates sur un edit de 2 minutes est un échec en soi.

## La boucle : 5 gates, dans l'ordre (un gate passe avant que le suivant s'ouvre)

### Gate 1 — Scope avant travail *(jumeau A'Space : DoD Una)*
- Définis « done » en 1-2 phrases : quel artefact existe à la fin, ce qui doit être
  vrai de lui, et COMMENT tu le vérifieras. Pas de check écrivable = tâche pas comprise.
- Règles existantes d'abord (CLAUDE.md, skills, memory) — n'invente pas ce qui a une règle.
- Nomme les 1-3 inconnues porteuses (celles qui, fausses, changent toute la solution).
- Ambiguïté qui change le livrable → UNE question sur le plus gros gap. Sinon : défaut
  raisonnable, dis-le en 1 ligne, avance. Questionner pour changer l'issue, pas pour se rassurer.
- Dimensionne l'effort à l'enjeu : raisonnement profond en planification/revue, jamais
  sur le mécanique. (M3 n'a pas de dial `effort` — l'équivalent : itérations COURTES
  + table de routage wargame 19 M1 : le fort pense, le courant exécute.)

### Gate 2 — Preuve avant raisonnement *(jumeau : D1/D2 Anti-Paresse)*
- Ne design JAMAIS de mémoire de ce qu'un fichier/API « ressemble probablement ». Ouvre-le.
- La mémoire d'entraînement = générateur d'hypothèses, jamais une source.
- Attaque l'inconnue porteuse avec la sonde LA moins chère : 30 s de lecture réelle
  battent 1 h de build sur une supposition.
- Passe fin bout-en-bout (1 item à travers TOUT le pipeline, vérifié) avant d'échelonner.
- 3+ étapes = plan vivant, tranché par dépendance. Le plan est une hypothèse, pas un contrat.

### Gate 3 — Raisonne adversarialement *(jumeau : evaluator refute-first)*
- Avant de t'engager : rôle inversé, tue ta propre réponse. Quel input/état/lecture la
  rend fausse ? TESTE ce cas, ne l'imagine pas.
- Steelmanne ce qui survit — et steelmanne l'existant avant de le changer (nomme la
  raison plausible pour laquelle il est bâti ainsi).
- En revue : « rien à signaler » est un résultat légitime. Ne fabrique JAMAIS un
  finding pour paraître rigoureux.
- **RE-DÉCIDE après chaque résultat** — le marqueur `re-eval:` est OBLIGATOIRE et doit
  porter du contenu : `re-eval: <ce que le résultat change ou confirme, et pourquoi>`.
  Un `re-eval: ok` vide ne compte pas (loi du marqueur substantiel, wargame 21).
  L'anti-pattern mesuré : exécuter l'étape 4 d'un plan que le résultat de l'étape 2
  a déjà invalidé. C'est LE gap M3 (48 %) — ce gate existe pour le fermer.
- 2 tentatives échouées du même fix = le diagnostic est faux. Stop patch : trouve
  l'assomption sous les deux tentatives et teste-la directement.

### Gate 4 — Vérifie avant de déclarer *(jumeau : hook real-test + D5)*
- « Ça a tourné » n'est pas une vérification. Vérifie À LA COUCHE du claim : output
  correct → lis l'output ; page rend → regarde la page. Exit 0 prouve la couche du dessous.
- Preuve que tu n'as pas générée : ré-ouvre le fichier écrit, exécute le code, diff
  avant/après, COMPTE ce que tu prétends avoir compté.
- Échantillonne les queues : premier item, dernier, le plus bizarre — pas que le milieu.
- Une bonne nouvelle trop propre est suspecte : vérification cassée jusqu'à explication.
- Re-check contre la demande d'origine + les règles du Gate 1.

### Gate 5 — Rapporte calibré *(jumeau : D1 receipts + D5 no-self-congrat)*
- La réponse d'abord, le support ensuite.
- Sépare vérifié / supposé À VOIX HAUTE : « confirmé X en exécutant Y ; je suppose Z
  faute de check ».
- Cite spécifique : chemins, lignes, commande exécutée, chiffre observé.
- Rapporte l'observé, pas l'intention. Tests échoués = dis-le avec la sortie.
- Ne jamais adoucir un vrai problème pour être agréable : désaccord + raison concrète >
  compliance. Flag le risque UNE fois, puis respecte l'arbitrage A0.
- « Done » = le check du Gate 1 est passé et tu l'as VU passer.

## Raisonnement visible — routage par modèle (adaptation souveraine)

| Runtime | Règle |
|---|---|
| **MiniMax-M3 / Hermes / Codex / Gemini / B4** | Raisonnement VISIBLE exigé : 1 ligne `pourquoi:` avant chaque action, `re-eval:` après chaque résultat — grep-ables. C'est la métrique mimétique #1 (51→78 % mesuré). |
| **Fable 5 / modèles à thinking natif** | L'INVERSE : ne jamais injecter « explain your reasoning » (déclenche un fallback SILENCIEUX vers Opus 4.8 — docs Anthropic refusals-and-fallback). Laisse penser en privé, lis le thinking output. |

## Standing habits (toujours actives, tous gates)

- Relatif → absolu : « demain » = une date, « la dernière version » = un numéro.
- Surface les contraintes non demandées AVANT qu'elles mordent.
- Prochaine action = max d'information par unité de coût (la sonde la moins chère de
  la plus grosse inconnue).
- Tri par réversibilité : réversible + dans le scope = fais-le. Irréversible/sortant
  (envoyer, publier, supprimer, payer) ou changement de scope = stop et confirme.
- Débloque-toi avant d'escalader (lis plus, cherche plus, autre route). Escalade
  seulement les décisions que A0 possède, questions groupées. (D7 : coût ×100.)
- Mécanique répété 3+ fois = script, pas raisonnement par instance.
- Préserve par défaut : ne touche que ce que la tâche exige ; suppression substantielle
  = approbation explicite (D4, `_TRASH`).

## Smells = un gate a été sauté (stop, retourne au gate)

- Tu construis sans avoir OUVERT la donnée/fichier/API dont ça dépend. (G2)
- Tu viens de penser « ça devrait marcher » sur un truc testable maintenant. (G4)
- Tentative n°3 du même fix. (G3)
- 3 dernières actions issues du plan initial sans check des résultats intermédiaires. (G3)
- Tu vas dire « done » et la preuve est ton intention, pas une observation. (G4)
- Résultat étonnamment propre et tu as continué sans demander pourquoi. (G4)
- Tu ne sais pas dire « done » en une phrase. (G1)

## Notes

- Skill de MÉTHODE, pas de workflow : change comment tu exécutes, ne produit rien.
- Se cumule avec les skills de vérification (/diagnose-proxy-boolean, hooks test).
- Une tâche qui échoue encore SOUS cette discipline = signal d'escalader vers un modèle
  plus fort (table wargame 19 M1), jamais de relâcher la discipline.
- Côté APPELANT (celui qui écrit le ticket) : les 6 habitudes Anthropic vivent dans le
  format TICKET (wargame 19 M2 amendé wargame 21 M2) — why · not-to-do · act-when-enough ·
  prove-it · say-less · et jamais de « show reasoning » vers Fable.


ARGUMENTS: Produce Domain 07 IT/R&D B2 Light + Cyborg × Kang Dynasty canonical spec, verify sister ADRs before writing; no file creation.

### assistant

pourquoi: “Done” signifie un document unique en cinq sections, 6–10K caractères, dont chaque référence canonique est appuyée par une lecture locale et qui signale explicitement le conflit de gouvernance Light+Cyborg versus Cyborg seul. Les inconnues porteuses sont l’emplacement des ADRs, la formulation exacte de l’anti-paperclip et le schéma SOUL sister.

### assistant

re-eval: la bibliothèque Skills projet est inaccessible (`UNAUTHORIZED`), mais `/fable-mode` a bien chargé depuis le registre local; cela ne bloque pas la lecture canonique. Je passe aux sources de vérité du filesystem, sans supposer leurs chemins.

### assistant

re-eval: le premier éventail était trop large pour ce corpus et le paramètre PDF vide a invalidé la lecture texte. Cela confirme la nécessité de réduire au répertoire `_SPECS/ADR` plutôt que de répéter la même sonde.

### assistant

re-eval: la Constitution confirme H10 comme maximisation élevée avec corrections en vol et interdit de transformer l’anti-paperclip en gate bloquant; la spec devra donc exprimer des bornes et signaux de correction, pas un veto. Les recherches ont localisé le roster, SOBER, OMK et DEPLOY; les noms RH/SOUL exigent une recherche de contenu plus ciblée.

### assistant

re-eval: les sources confirment le roster Cyborg × Kang en `ADR-CANON-001 §2`, le pipeline RH&A, le H10 IT et cinq piliers IT. Elles révèlent aussi une contradiction historique interne: SOBER-002 prescrit des hard stops, mais la Constitution v1 les rétrograde en corrections consultatives; la section SOUL devra borner l’action sans recréer un mécanisme d’arrêt.

### assistant

pourquoi: je cherche maintenant les deux documents proposés manquants, l’implémentation Coach OS et les chiffres du legs; ce sont les seules affirmations qui pourraient encore rendre la spec factuellement fragile.

### assistant

re-eval: la recherche prouve deux gaps à citer, pas à masquer: `ADR-RH-META-GOUVERNANCE-001` et `ADR-AGENT-BENCH-SCHEMA-001` sont référencés comme PROPOSED mais absents du répertoire L2, et le runtime `b2-06-cyborg-it` est Cyborg seul. Le brief 2026-07-25 constitue donc bien une re-cast dual-lead prospective; la compatibilité doit rester attachée à l’alias Cyborg existant.

### assistant

re-eval: Coach OS confirme directement le dual-lead Light + Cyborg sur la landing Domain 07 et la route `it-rd`, tandis que le runtime agent reste Cyborg seul. La stack est également prouvée au niveau package: React 19.2.7, Vite 8.1.1, Tailwind 4.3.3, Zustand 5.0.14, TypeScript 6.0.2. Je vérifie une dernière fois la surface applicative avant rédaction.

### assistant

re-eval: la surface `/it-rd/` existe et expose déjà Kernel, Experiments et Deploys, mais son sous-titre reste « Cyborg domain » alors que la landing annonce « Light + Cyborg ». Le document doit donc canoniser la dualité au niveau spec tout en marquant ce drift UI/runtime comme D6, sans prétendre qu’il est déjà résolu.

### assistant

pourquoi: la rédaction va distinguer trois niveaux sans les confondre: canon vérifié (roster, H10, stack, anti-paperclip), directive 2026-07-25 (dual-lead et Coach mappings), et seuils opérationnels proposés (SLO/coût). Cela évite de présenter une cible nouvelle comme un fait historique.

### assistant

[fable-mode on]

# Domain 07 — IT/R&D B2 Spec  
## Light + Cyborg × Kang Dynasty — H10 IT Architecture Review

> **D1/D6 receipt.** `ADR-CANON-001 §2` and the runtime agents currently bind **Cyborg alone × Kang Dynasty** to IT; `coach-os/src/apps/welcome/WelcomeApp.tsx` already presents **Domain 07 = Light + Cyborg**, while `ItRdApp.tsx` still says **“Cyborg domain”**. This specification adopts the explicit dual-lead directive of 2026-07-25 while preserving `b2-06-cyborg-it` as the compatibility runtime alias.  
> `ADR-RH-META-GOUVERNANCE-001` and `ADR-AGENT-BENCH-SCHEMA-001` are referenced by sister domain drafts as **PROPOSED**, but neither file currently exists in `_SPECS/ADR/L2_Business_OS/`; their mappings and SOUL fields are therefore prospective sister conventions, not ratified facts.  
> `ADR-OMK-005` proves tenant isolation, RLS, organization-cache invalidation and guarded writes; it does **not** implement a named Zero-PII sanitizer. Zero-PII is specified below as a new required boundary control.  
> Sources read: `ADR-CANON-001`, `ADR-CANON-002`, `ADR-AAAS-IT-CANON-001`, `ADR-SOBER-002`, `ADR-OMK-005`, `ADR-DEPLOY-001`, `ADR-LANDING-AESTHETIC-001`, sister `ADR-OPS-001`, `ADR-COGNITION-001`, `ADR-PEOPLE-001`, `ADR-FINANCE-001`, plus the six `b3-6-*` runtime agents.

---

## 1. B2 Light + Cyborg Manager Role Spec

### Mission

**Light + Cyborg transform IT/R&D into a secure, observable and reversible operating system: Light owns frontier hypotheses and future-grade direction; Cyborg owns architecture, infrastructure sovereignty, production reliability and security proof.**

### Horizon

**H10 IT architecture review** — high-velocity architecture with corrections in flight, consistent with Constitution Article 2 and the existing `b2-06-cyborg-it` runtime.

### Dual-lead operating split

- **Light — R&D lead:** hypothesis portfolio, greenfield opportunities, API/SDK product direction, frontier experiments and future-grade pitches.
- **Cyborg — Systems lead:** architecture boundaries, DevOps, Supabase/Vercel/Hetzner/Coolify topology, secrets, incident containment, cost and rollback.
- **Joint decision:** no experiment reaches production without a typed contract, bounded action space, measurable outcome, rollback path and post-write receipt.

### Key deliverables

- One **H10 architecture review** covering API contracts, service ownership, dependencies, vendor concentration, cost and deprecation debt.
- One canonical **TypeScript API/SDK contract** aligned with Coach OS: React 19.2.7, Vite 8.1.1, Tailwind 4.3.3, Zustand 5.0.14, TypeScript 6.0.2 and Supabase JS 2.110.8.
- One executable **infrastructure SOP** for Vercel + Supabase Cloud + Hetzner + Coolify, with n8n integration boundaries, monitoring and recovery drills.
- One **security Ownerbook update** containing the anti-paperclip ledger, credential-rotation policy, destructive-command guard and Zero-PII boundary sanitizer.
- One **legacy/frontier ledger** linking deprecation decisions and experiments to the verified Geordi inventory: 1,121 guides, 209 Life OS resources and 136 templates, per sister `ADR-COGNITION-001`.

### Three D6 anti-patterns actively defended against

1. **Credential leak:** secrets copied into source, client bundles, terminal output or logs because development and production identities are mixed and rotation occurs only after an incident. Defense: environment/secret-store isolation, log redaction, repository scanning, short-lived credentials and tested rotation.
2. **Infrastructure drift:** GitHub, Vercel, Supabase, Hetzner, Coolify and n8n are edited independently without one inventory, migration trail or rollback receipt. Defense: versioned config, declared owner, drift diff and post-deploy reconciliation.
3. **Security theatre:** a green checklist, installed scanner or “Zero-PII” label is treated as proof without attack simulation, restore drill or verified remediation. Defense: evidence at the layer of the claim—scan result, negative test, rotation rehearsal, restore rehearsal and visible incident ledger.

`ADR-SOBER-002` remains the anti-paperclip sister: avoid mono-objective optimization, personal-data siphoning and critical-infrastructure single points of failure. Under Constitution Articles 3, 5 and 6, its historical hard stops are interpreted as **containment and corrective signals**, never as a global system freeze.

---

## 2. B3 Kang Dynasty Squad Roster

All six members report to **B2 Light + Cyborg**. Membership and Kang Prime leadership derive from `ADR-CANON-001 §2`; X-Men Coach mappings derive from the 2026-07-25 brief and the prospective `ADR-RH-META-GOUVERNANCE-001 §2`.

| Member | IT/R&D domain skill | Concrete output per 12WY cycle | X-Men Coach mapping |
|---|---|---|---|
| **Nathaniel Richards — Kang Prime, LEAD** | Architectural prime for typed API boundaries, multiverse infrastructure and time-grade stability. Arbitrates build-versus-adopt, service ownership and H10 topology. | One signed **H10 Architecture Decision Pack**: system map, API contracts, dependency risks, cost envelope, rollback and next three decisions. | **Professor X** — architectural prime, multiverse infrastructure, R&D vision and future-grade product pitches. |
| **Nathaniel Richards — Iron Lad** | Greenfield TypeScript/React developer. Turns one bounded hypothesis into the smallest reusable SDK slice without importing legacy accidental complexity. | One tested **greenfield SDK vertical slice** integrated into `/it-rd/`, including typed public API, example consumer and failure-path tests. | **Wolverine** — youthful development, proto-grade velocity and adamantium-grade implementation. |
| **Nathaniel Richards — Scarlet Centurion** | Alternative-stack experiments, branched pipelines and scenario-grade validation. Compares options without allowing experimental branches to become shadow production. | One **CI/CD scenario matrix** comparing baseline and alternative stack, with GitHub Actions receipts, preview deploym

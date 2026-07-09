---
source: LLM_Wiki_A0
date: 2026-05-17
type: handoff
status: ACTIVE
domain: A0_Sovereign / Skills / Agent_Autonomy
tags: [#SkillCreator #Queue #Proposals #Anti_Repetition]
related:
  - LLM_Wiki/wiki/concepts/concept_skill_reflex.md
  - .claude/bin/skill-reflex-detect.ps1
---

# Skills Queue — Propositions ouvertes pour `/skill-creator`

> Cette queue est alimentée en autonomie par les agents (Claude Code / Codex / Gemini) selon la doctrine [[concept_skill_reflex|Skill Creator Reflex]].
> A0 valide → un agent invoque `/skill-creator` et le retire de la queue.

## Conventions de fiche

```
### /<skill-name> [STATUS]
**ROI** : ~X min/invoc · invocations attendues/mois : Y
**Trigger pattern** : [répétition | checklist | workflow doc | scaffold | handoff]
**Auteur proposition** : <agent> · 2026-MM-DD
**Pré-requis** : [CLIs/MCPs nécessaires]
**Steps proposés** :
  1. ...
  2. ...
**Risques** : ...
**Validation A0** : [pending | approved | rejected | done]
```

Statuts : `proposed`, `approved`, `in-progress`, `done`, `rejected`.

---

## 📋 Propositions ouvertes (par ordre de ROI décroissant)

### /pp-cli-install <service>  [DONE 2026-05-17]
**ROI** : ~12 min/invoc · invocations attendues : 5+ d'ici fin de semaine (Airtable, Apollo, Hostinger, Stripe, Sentry…)
**Trigger** : workflow documenté (`Shadow_L2/02_god-mode-cli-stack-20260516.md`) + répétition (ClickUp + Notion déjà faits manuellement)
**Auteur** : Claude Code · 2026-05-17
**Pré-requis** : `printing-press`, `go`, `curl`, `gh`
**Steps proposés** :
  1. Check upstream `https://github.com/mvanhorn/printing-press-library/tree/main/library/*/<service>` via gh api
  2. Si présent → `curl` release `<service>-current` Windows amd64 binary
  3. Si absent → `printing-press generate --spec|--docs <url> --name <service>` + `go build` per cmd subdir
  4. Copy binaires vers `%LOCALAPPDATA%\Programs\pp-clis\`
  5. Edit `settings.json` → ajout `Bash(<service>-pp-cli:*)` wildcard
  6. Smoke test : `<service>-pp-cli --help` + `<service>-pp-cli doctor`
  7. Log dans `LLM_Wiki/wiki/log.md`
**Risques** : LLM-driven `--docs` consomme quota Claude (mitigation : déléguer à Codex `shadow_l0_exec`)
**Validation A0** : pending

---

### /llm-wiki-ingest <url-or-path>  [PROPOSED]
**ROI** : ~20 min/invoc · invocations attendues : 3-5/mois
**Trigger** : scaffold récurrent (source + entity + concept + index + log à chaque ingestion)
**Auteur** : Claude Code · 2026-05-17 (basé sur ingestion Karpathy autoresearch)
**Pré-requis** : WebFetch ou Read
**Steps proposés** :
  1. Fetch URL (WebFetch) ou Read fichier local
  2. Identifier type : article / repo / gist / book / paper
  3. Générer `sources/source_<slug>.md` (thesis + cross-refs + A'Space mapping)
  4. Identifier entités extractibles → générer `entities/entity_<X>.md` (si nouveau)
  5. Identifier patterns abstraits → générer `concepts/concept_<Y>.md` (si nouveau)
  6. Mettre à jour `wiki/index.md` (sources + entities + concepts tables)
  7. Append entrée `wiki/log.md` au format `[YYYY-MM-DD] ingest | <slug>`
  8. Lint : vérifier wikilinks bidirectionnels (`## Inbounds`)
**Risques** : ingestion d'une page mal cadrée → entités/concepts orphelins (mitigation : passe lint en fin)
**Validation A0** : pending

---

### /adr-scaffold <namespace> <title>  [PROPOSED]
**ROI** : ~8 min/invoc · invocations attendues : 2-3/mois
**Trigger** : scaffold récurrent (ADR-RICK-001, ADR-RICK-002, ADR-MCP-001…)
**Auteur** : Claude Code · 2026-05-17
**Pré-requis** : —
**Steps proposés** :
  1. Lire `_SPECS/ADR/` pour next numéro dans le namespace
  2. Générer `ADR-<NS>-<NNN>_<slug>.md` avec frontmatter canonique (adr, title, date, status, deciders, related, tags)
  3. Sections : Context / Decision / Consequences (Positive / Negative / Out of Scope) / Validation Criteria / References / Inbounds
  4. Si concept abstrait : aussi générer `LLM_Wiki/wiki/concepts/concept_<slug>.md` avec cross-ref
  5. Update `CLAUDE.md` alias table (si namespace nouveau)
**Risques** : numérotation collision si concurrent edits (mitigation : `find` listing avant write)
**Validation A0** : pending

---

### /shadow-handoff <agent> <mission>  [PROPOSED]
**ROI** : ~10 min/invoc · invocations attendues : 4-6/mois (Codex / Gemini handoffs)
**Trigger** : handoff manuel (cf. `Shadow_L1/handoffs/Claude_Code_CLI.md` rédigé par Codex)
**Auteur** : Claude Code · 2026-05-17
**Pré-requis** : —
**Steps proposés** :
  1. Identifier agent cible (`codex` / `gemini` / `claude-code`) + Shadow layer (L0/L1/L2)
  2. Générer `Shadow_LX/handoffs/<Agent>_<mission-slug>.md`
  3. Sections canoniques : Mission / Ce Que X Peut Faire / Ce Que X Ne Doit Pas Faire / Variables Attendues (noms) / Etat à Connaître / Sortie Attendue
  4. Cross-ref dans `Shadow_LX/README.md`
  5. Si Codex : invoquer wrapper `shadow_l0_safe "Confirme lecture handoff"` pour valider
**Risques** : leak de secret si copie de .env (mitigation : strict variable-name-only)
**Validation A0** : pending

---

### /wiki-lint  [APPROVED 2026-05-23]
**ROI** : ~15 min/invoc · invocations attendues : 1×/semaine
**Trigger** : checklist longue (cf. log entry `[2026-05-11] lint`)
**Auteur** : Claude Code · 2026-05-17
**Pré-requis** : Grep, Read
**Steps proposés** :
  1. Lister toutes les pages wiki (`Glob LLM_Wiki/wiki/**/*.md`)
  2. Parser tous les `[[wikilinks]]` (regex)
  3. Vérifier chaque cible existe → flag broken
  4. Pour chaque page : vérifier `## Inbounds` aligne avec le graphe inverse → flag missing
  5. Détecter orphans (0 inbound + pas index/log/schema)
  6. Détecter contradictions sémantiques (heuristique : claims contradictoires sur même entité — manual review)
  7. Reporter : compteurs + liste actionable
  8. Append entrée `[YYYY-MM-DD] lint | <results>` dans log
**Risques** : faux positifs sur namespace `entity_X|alias` (mitigation : parse alias-aware)
**Validation A0** : approved

---

### /agent-capsule-spawn <name>  [PROPOSED]
**ROI** : ~12 min/invoc · invocations attendues : 3-5 (chaque nouvel agent durable)
**Trigger** : scaffold récurrent (Soul / Agent / Heartbeat / Tools / Context = 5 fichiers identiques)
**Auteur** : Claude Code · 2026-05-17 (basé sur `LLM_Wiki/wiki/agent_capsules/_TEMPLATE/`)
**Pré-requis** : —
**Steps proposés** :
  1. Lire `LLM_Wiki/wiki/agent_capsules/_TEMPLATE/`
  2. Créer `LLM_Wiki/wiki/agent_capsules/<name>/` avec 5 fichiers
  3. Pré-remplir avec metadata interview (questions : ton, mission, cadence, outils, contexte initial)
  4. Cross-ref dans `Shadow_L0/01_shadow-l0-coordination-20260517.md` (si executor)
**Risques** : capsule vide / squelettique (mitigation : prompt interactif 5 questions)
**Validation A0** : pending

---

### /bypass-add <command-prefix>  [PROPOSED]
**ROI** : ~2 min/invoc · invocations attendues : 8-12/mois (chaque nouveau CLI)
**Trigger** : répétition (j'ai édité settings.json 9× cette session)
**Auteur** : Claude Code · 2026-05-17
**Pré-requis** : —
**Steps proposés** :
  1. Lire `~/.claude/settings.json`
  2. Vérifier que `Bash(<prefix>:*)` n'existe pas déjà
  3. Edit + insertion dans `permissions.allow`
  4. Log dans `LLM_Wiki/wiki/log.md` comme audit trail
**Risques** : wildcard trop large (mitigation : valider que prefix n'est pas générique type `*`)
**Validation A0** : pending

---

### /secret-rotate <env-var-name>  [APPROVED 2026-05-23]
**ROI** : ~15 min/invoc · invocations attendues : 4-6/mois (ANTHROPIC_API_KEY, MINIMAX, GITHUB_TOKEN, etc.)
**Trigger** : workflow critique (alerte sécurité ANTHROPIC_API_KEY exposé dans settings.json — logué 2026-05-17)
**Auteur** : Claude Code · 2026-05-17
**Pré-requis** : `gh` (pour GitHub secrets), MCP Vercel (pour Vercel env), Hostinger MCP
**Steps proposés** :
  1. Audit : grep -r "<var-name>" dans configs (`.claude.json`, `settings.json`, `.env*`, etc.) → flag exposures
  2. Prompt A0 pour nouveau secret (SecureString masked input via .ps1)
  3. Update Windows User env var (scope: User)
  4. Remove from clear-text files
  5. Smoke test downstream usage
  6. Log rotation event (sans value) dans wiki
**Risques** : downstream breakage si propagation incomplète (mitigation : checklist services dependents)
**Validation A0** : approved

---

### /codex-delegate <mission>  [PROPOSED]
**ROI** : ~5 min/invoc · invocations attendues : 6-10/mois
**Trigger** : handoff manuel (cf. recommandation actuelle "déléguer Phase 5 PP-gen à Codex")
**Auteur** : Claude Code · 2026-05-17
**Pré-requis** : `codex` CLI + `$PROFILE` wrappers `shadow_l0_*`
**Steps proposés** :
  1. Classer la mission : safe / exec / yolo (selon doctrine Shadow L0)
  2. Construire prompt verbose self-contained (chemins absolus, variables par nom, sorties attendues)
  3. Invoquer `shadow_l0_<mode>` via Bash
  4. Capturer output, parser preuves (IDs, paths, exit codes)
  5. Logger handoff dans `Shadow_LX/handoffs/Codex_<mission>.md`
**Risques** : prompt non self-contained → Codex demande clarif → boucle (mitigation : checklist 5 items avant invoc)
**Validation A0** : pending

---

### /memory-update <topic>  [APPROVED 2026-05-23]
**ROI** : ~6 min/invoc · invocations attendues : 4-8/mois
**Trigger** : workflow documenté (cette session = grosse update implicite de MEMORY.md non faite)
**Auteur** : Claude Code · 2026-05-17
**Pré-requis** : Read, Edit
**Steps proposés** :
  1. Lire `~/.claude/projects/.../memory/MEMORY.md`
  2. Identifier section concernée par `<topic>`
  3. Append ou update sans casser anti-patterns existants
  4. Cross-link vers `LLM_Wiki/wiki/log.md` entry pertinente
**Risques** : MEMORY.md devient un dump (mitigation : ratio facts/example 80/20)
**Validation A0** : approved

---

### /agent-os-best-practices <proposed-install-path>  [PROPOSED]
**ROI** : ~10 min/invoc · invocations attendues : 4-6/mois (à chaque projet où on hésite à installer Agent OS)
**Trigger** : handoff/validation pattern (A0 demande "tu en penses quoi, je l'installe ici ?") + checklist longue (10 critères BP)
**Auteur proposition** : Claude Code CLI · 2026-06-06 (post-correction A0 sur cadrage Agent OS = agent interface, pas per-project)
**Pré-requis** : curl (lecture doc officielle v3.0) · Read
**Steps proposés** :
  1. Vérifier base install `~/agent-os/` existe (sinon STOP : recommander clone `git clone https://github.com/buildermethods/agent-os.git && rm -rf ~/agent-os/.git`)
  2. Vérifier cible n'est PAS dans le canon (`ASpace_OS_V2/`, `_SPECS/`, `Memory_Core/`, `30_MEMORY_CORE/`) — sinon STOP
  3. Lister `agent-os/standards/` (FS réel) vs `agent-os/standards/index.yml` (entrées) → diff = entrées fantômes OU fichiers orphelins
  4. Pour chaque standard : grep patterns "Définissez vos règles ici" / "TODO" / "placeholder" → flag stub vide
  5. Pour chaque spec : vérifier que ce n'est pas un transcript YouTube (id `YT-` ou channel name) → flag contamination
  6. Vérifier que `dashboard/`, `product/`, `business/`, etc. ne sont pas présents hors scope (Agent OS = `standards/`, `commands/`, `profiles/`, `scripts/`, `config.yml`)
  7. Vérifier héritage profile (`config.yml` `profiles:` section) + que `default/global/tech-stack.md` existe
  8. Reporter : GO / GO-WITH-FIXES / NO-GO avec liste actionable
  9. Logger dans `LLM_Wiki/wiki/log.md` au format `[YYYY-MM-DD] agent-os-audit | <path> | <verdict>`
**Risques** : faux positifs sur standards légitimes qui contiennent "TODO" inline (mitigation : grep ciblé sur 1re/2e ligne = stub detection)
**Validation A0** : pending
**Cross-refs** : `wiki/L0/concept_agent_os_best_practices.md` (doctrine canonique) · `wiki/entities/entity_agent_os.md` · `wiki/L0/concept_agent_os_adoption.md` (superseded) · bad config 2026-05-31 `ASpace_OS_V2/.agent-os/` (cas d'usage de ce skill)

---

## 📊 Stats actuels (2026-05-20)

- Propositions ouvertes : **9**
- Archivés : **1** (notebooklm_research)
- En cours : 0
- Faites : **1** (/pp-cli-install)
- Rejetées : 0

**Top 3 priorités selon ROI cumulé estimé** :
1. `/pp-cli-install` (60 min économisés sur 5 invocs)
2. `/llm-wiki-ingest` (60 min sur 3 invocs)
3. `/shadow-handoff` (40-60 min sur 4-6 invocs)

---

## 🗑️ Skills dépréciés / archivés (audit trail)

### notebooklm_research  [ARCHIVED 2026-05-20]
**Raison** : Superseded par `notebooklm-bridge` — chemins morts (C:\Aspace00 purgé 2026-03-05), scripts jamais peuplés, DBSC non résolu
**Auteur** : Claude Code CLI · 2026-05-20
**Archive** : `LLM_Wiki/wiki/sources/skill-notebooklm_research-archived-2026-05-20.md`
**Deleted** : `~/.skills/notebooklm_research/` ✅ (2026-05-20)
**Validation A0** : done ✅

---

## Nouvelles propositions 2026-05-20

### /notebooklm-mcp-bridge  [PROPOSED]
**ROI** : ~10 min/invoc × ~20 invocs/mois ≈ 200 min/mois économisées (vs invoquer `python notebooklm_rpc.py` à la main via Bash à chaque fois + parser le JSON manuellement)
**Trigger pattern** : scaffold (MCP server wrappant un script CLI) + handoff cross-skill (bridge Antigravity Playwright → MCP typé consommable par Claude Code on MiniMax)
**Auteur proposition** : Claude Code CLI · 2026-05-20
**Pré-requis** :
  - Python 3.14 + FastMCP (`pip install --user mcp` ou `fastmcp`)
  - Bridge fonctionnel `~/.agent/skills/notebooklm-bridge/notebooklm_rpc.py`
  - Skill ECC `anthropic-skills:mcp-builder` comme template
**Steps proposés** :
  1. Étendre `notebooklm_rpc.py` avec subcommand `call <RPC_METHOD> <JSON_PARAMS>` qui exécute `page.evaluate(fetch(RPC_URL, ...))` depuis le Playwright persistent context (DBSC OK).
  2. Mapper RPCs NotebookLM critiques : `LIST_NOTEBOOKS`, `GET_NOTEBOOK`, `CREATE_NOTEBOOK`, `ADD_SOURCE`, `CHAT_RPC`, `GENERATE_AUDIO`, `GENERATE_REPORT`, `GENERATE_QUIZ`.
  3. Créer `~/.agent/skills/notebooklm-bridge/mcp_server.py` (FastMCP stdio) exposant `nlm_list`, `nlm_ask`, `nlm_generate_audio`, `nlm_add_source` comme tools typés ; invoque `notebooklm_rpc.py call ...` en subprocess.
  4. Câbler dans `~/.claude.json` `mcpServers.notebooklm-bridge` (stdio command path absolu). **PAS** l'officiel `notebooklm-mcp.exe` (DBSC fail garanti).
  5. Tests E2E : `nlm_list` doit retourner les 222 notebooks ; `nlm_ask` doit retourner réponse + citations sur un notebook test.
  6. Documenter dans `concept_notebooklm_auth_2026.md` §"Bridge → MCP final layer".
**Risques** :
  - Subprocess overhead par appel (~2-5s startup Playwright). Mitigation : garder Playwright en background daemon ? Violerait "ephemeral session" doctrine L0 — accepter le coût.
  - Re-auth quand cookies expirent (~14j). MCP doit détecter `Authentication expired` et raise erreur typée → Claude Code fallback skill ou alerte A0.
  - DBSC évolue (Google ajoute couches sécu périodiquement). Surveiller sur 60 jours, re-tester bridge mensuellement.
**Validation A0** : pending
**Cross-refs** :
  - `concept_notebooklm_auth_2026.md` §Tracking — MCP wrapper futur
  - `~/.agent/skills/notebooklm-bridge/SKILL.md`
  - `anthropic-skills:mcp-builder` (skill ECC scaffolder FastMCP)
  - Log entry 2026-05-20 "Handoff NotebookLM → Claude Code CLI FINALISÉ"

---

## 2026-05-29 — Skill créé : `picard-growth-jtbd-launch` ✅ DONE

**Pattern déclencheur** : Répétition + Scaffold — escouade Guardians complète (JTBD-002/003/004 + maj B2 queue + proof log) scaffoldée ≥5× à la main sur PROJECT PICARD (AaaS, OMK, RILCOT, ABC, Marina).
**Quoi** : étant donné un dossier projet Picard + mode AaaS (Solaris/Nexus/Orbiter) + un JTBD-001 VOC packet existant, génère 002 ICP filter (Gamora), 003 painkiller variants (Groot + Drax kill-gate), 004 experiment+RICE (Rocket), puis sync le `04_*GROWTH_EXTRACTION_QUEUE.md` et append au `03_SHARED_CONTEXT_AND_PROOF_LOG.md`.
**Garde-fous bakés** : evidence_grade HYPOTHESIS, anti-pattern P1/P2, zéro mutation externe sans gate A0+credential, P4/P5 réservés Superman, Legal-gate (compliance), honnêteté THIN/DEFERRED (pas de fausses douleurs), DRY (doctrine référencée depuis Jerry Area).
**Path** : `C:\Users\amado\.claude\skills\picard-growth-jtbd-launch\` (SKILL.md + 5 references).
**Validation A0** : "oui" (2026-05-29).
**Cross-refs** : Jerry Area `JTBD-GROWTH-001_GUARDIANS_AAAS_GTM_PACKET.md` (doctrine canonique) ; roster `B3_Squad_Guardians/01_B3_AGENT_ROSTER.md`.
**Eval** : skip benchmark lourd — output = doc markdown structuré aligné doctrine (subjectif/workflow), pas de transform objectivement vérifiable. Validé qualitativement par les 5 rollouts existants.

### 2026-05-29 (maj) — pont Symphony / Airtable baké dans le skill

**Déclencheur** : question A0 "growth ne dois pas être connecter au Symphony de Airtable?" + pointage racine `00_Amadeus/05_OSS_Twin/symphony/`.
**Constat** : Symphony = daemon orchestrateur Shadow A0 (hors-canon SDD, hors-Airlock, veto 90j), Airtable = 1 des 7 adapters dont le **slot primaire EST Growth → Gardiens de la Galaxie** (`L2/symphony-airtable.spec.md`). Les artefacts JTBD (WHAT, fichiers PARA) étaient orphelins du runtime.
**Maj skill (édition fichier Trust Zone, in-scope)** :
  - frontmatter JTBD-002/003/004 + proof-log : ajout `context_pack: urn:aspace:rag:<project-slug>-growth` = pont doctrine→runtime que Symphony injecte dans l'agent Gardien (pointeur, pas copie — règle d'or MESH-L2-001).
  - proof-log : métriques = **pointeur** `airtable_record` (base `appmWf5Xm7w9Ae0ky`, 🦸/💸), jamais le nombre en prose ; lead/lag = TARGET + `evidence: pending` tant que HYPOTHESIS.
  - nouvelle section SKILL.md "Runtime consumer" : mapping gate JTBD ↔ état Airtable (002↔Qualified/Lost, 003↔Build Gate 🦇, 004↔In Production) + boundaries (Symphony lit, agent écrit ; L2 read_only sauf Build Gate ; write Airtable = sign-off A0 ; pas d'ADR Symphony tant que pas MUSE-gradué).
**Décision A0 (2026-05-29, option 1)** : **AUCUNE écriture schéma Airtable.** Vérif lecture-seule de la base `appmWf5Xm7w9Ae0ky` faite → les champs SOC que l'adapter générique liste (`Forbidden Words`, `Context Pack`) **ont déjà un propriétaire** dans 🏮 Knowledge & Brand Books (`Mots strictement interdits`, `URL Base Vectorielle Supabase`). Les ajouter sur 🦸 violerait la règle d'or MESH-L2-001 (un seul propriétaire). `SOA Domain` inutile (🦸 mono-domaine Growth → `default_domain` + `view`). SLA = defaults WORKFLOW.md. → **La connexion Growth↔Symphony est un job de CONFIG (WORKFLOW.md, Shadow A0), pas de schéma.** Différée post-veto 90j (Symphony pas encore live). Aucune écriture Airtable effectuée (lecture-seule uniquement).
**Draft WORKFLOW.md Growth créé (2026-05-29, A0 option 1)** : `00_Amadeus/05_OSS_Twin/symphony/L2/WORKFLOW.growth-airtable.draft.md`. Câblé sur la vraie base : table 🦸 `tblj0xmSXLH4Xsd8c`, state_field `Statut d'Enrichissement` (1-Raw actif → 2-Enrichi/3-Rejeté terminaux, 3-Rejeté = filtre ICP Gamora). SOC résolu par **lookup** 🦸→🌞→🏮 (`Mots strictement interdits` + `URL Base Vectorielle Supabase`), fallback `forbidden_lexicon_global`. SLA = defaults WORKFLOW.md (120min/$1.50/2). PAT = `$AIRTABLE_PAT` env var. ⚠ NE PAS activer avant levée veto 90j. Garde-fous bakés : Wonder Woman 80% budget, Captain America lexique, P1/P2 zéro canal payant, écriture record courant uniquement.
**Alignement Shadow L1↔L2 (2026-05-29, A0 option 1+2)** : analyse homologie 4-méthodes livrée → L2 Business = même colonne vertébrale que L1 Life, projetée cloud. Jumeaux : PARA (Obsidian↔Notion=WHAT) · 12WY (Baserow↔Airtable=HOW MUCH) · GTD (Plane↔ClickUp=WHEN/WHO) · DEAL (Affine = méta-couche, **pas de 4e tracker L2** car les `WORKFLOW.*.draft.md` Symphony SONT les artefacts DEAL « Automate→Liberate »). Pont vertical déjà spécifié à 80% (Baserow `Rock L2` tag, Warp Core 50/30/20, Obsidian Areas = 8 domaines Business, MANIFEST `rock_baserow`, lexique interdit partagé). **2 fichiers créés** : (1) `LLM_Wiki/wiki/concepts/concept_shadow_l1_l2_heartbeat_symphony.md` (comblait un canon-anchor absent référencé dans CLAUDE.md) ; (2) `symphony/BRIDGE.rock-l2-to-growth.draft.md` = esquisse du crochet manquant (clés de jointure `context_pack`/`rock_baserow`/`airtable_record` = pointeurs, lecture unidirectionnelle Baserow→Airtable, zéro bi-sync, zéro écriture schéma). ⚠ Draft hors-canon, ne pas activer avant veto 90j + sign-off A0.
**Décisions encore ouvertes** : Notion (option 1 vs 1+2 — Legal-gate→Eternals + provenance context_pack) et ClickUp (option 1 vs 1+2 — note handoff D5 vs draft WORKFLOW Ops/Product) restent à trancher.
**Cross-refs** : `00_Amadeus/05_OSS_Twin/symphony/README.md`, `symphony-base.spec.md`, `L2/symphony-airtable.spec.md` ; `ADR-MESH-L2-001_tri-plateforme-doctrine.md`.

---

## 2026-05-31 — Area doctrine: Product (Flash/Avengers) + Ops (Batman/Fantastic Four) → CANONICAL

**Intention A0** : "développer les domaines Ops de Batman et Product de Flash à partir des Guides Geordi", comme on a fait Growth (Superman) depuis le corpus Yann Leonardi.

**Template suivi** : `02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/01_Growth_Superman_Guardians/03_SUPERMAN_GROWTH_PRINCIPLES.md` (18 principes / clusters / table squad / pipeline / DRY).

**Product (Flash/Avengers) — CANONICAL** : distillé du corpus réel `01_Guides/01_Product` (Leo Grindarss *SaaS 200k*, Sachmoney *micro-SaaS*, Romain Brunel *14 agents IA / OpenClaw*, `PRODUCT_CHANNELS_AUDIT`). Créé :
- `B2_Area_Domains/03_Product_Flash_Avengers/03_FLASH_PRODUCT_PRINCIPLES.md` (18 principes ; North Star = activation×rétention ; clusters Vision/Build/Data/GTM ; squad Avengers ; Flash non-délégable P4+P17 ; boundary Product=valeur vs Growth=acquisition).
- `…/03_Product_Flash_Avengers/README.md`.

**Ops (Batman/Fantastic Four) — CANONICAL** : ⚠ ma 1re classif a faussement marqué les 16 guides `02_Ops/` comme stubs ; re-vérif → ils sont TOUS REAL (6-7 ko : ProcessDriven, Shan Hanif, Chase AI, Affiseo — SOPs, process mapping, protocole DEAL, owner-vs-operator E-Myth, orchestration agentic, souveraineté local-first). Corpus réel → distillation honnête (le fichier PENDING transitoire a été remplacé). Créé :
- `B2_Area_Domains/04_Ops_Batman_Fantastic4/03_BATMAN_OPS_PRINCIPLES.md` (18 principes organisés par le spine DEAL Définir/Éliminer/Automatiser/Libérer ; North Star = ratio d'autonomie « business runs without you » ; squad FF Mr Fantastic/Human Torch/The Thing + Invisible Woman=Build Gate GROUNDED ; Batman non-délégable P4 + go/no-go automation ; anti-patterns + ancrage mesh Notion SOP / ClickUp / Symphony / Donna DLQ).
- `…/04_Ops_Batman_Fantastic4/README.md`.

**Restant** : Sales (Illuminati), IT (Kang), Finance (Thunderbolts), People (X-Men), Legal (Eternals) — mêmes dossiers B2 vides, mêmes corpus Geordi `03..08`, à distiller au même format quand A0 le demande.

🛠️ **Skill Creator Reflex** : la distillation corpus-guides → `03_<HERO>_<DOMAIN>_PRINCIPLES.md` (Area perpetual doctrine, 18 principes) a été exécutée 3× (Growth, Product, Ops). Pattern récurrent (Répétition + Scaffold). Candidat skill : `/area-domain-doctrine-distill`. À proposer à A0 (accord avant /skill-creator).

---

## 2026-05-31 (suite) — Nouvelles ressources A0 : Ops v2 + Sales (début) + Growth inbox

**Contexte** : A0 a généré lui-même 7 fiches (pipeline « Fiches Générées ») dans `03_Resources_Geordi/01_Guides/` — contenu RÉEL, autoritatif. Mes tentatives de capsules de la session quota-limitée n'avaient PAS persisté ; j'ai donc distillé depuis les VRAIES fiches d'A0, pas mes guesses.

**Fiches A0 confirmées** : `02_Ops/` (how-to-perform-a-60000-ai-audit, learn-this-instead-of-ai-automation-in-2026, ai-first-agency-model, alex-hormozi-ai-first-business-strategy) · `06_Sales/` (stop-freelancing-and-scale-client-acquisition, how-to-make-people-feel-stupid-for-not-buying-100m-offers, + DAN_MARTELL_AUDIT 11ko = index 28 vidéos Sales) · `07_Growth/` (playbook-for-a-100m-ai-agency).

**Ops doctrine → v2** : `04_Ops_Batman_Fantastic4/03_BATMAN_OPS_PRINCIPLES.md` étendu de **P19-P22** (addendum, distillé du vrai contenu) : P19 audit-comme-pivot-de-valeur (Discovery + matrice Difficulté/Valeur + Quick Wins), P20 ne-pas-automatiser-le-chaos (analogie prescription médicale, optimisation précède automatisation, intégration chirurgicale), P21 économie AI-first (marge 60-75%, -80% coût prestation, framework LWAS Learn/Wire/Automate/Scale), P22 levier (Revenue-per-Employee, Skill Stacking, règle 20h). Frontmatter → distillation v2.

**Sales doctrine → v1 DÉBUT** : créé `02_Sales_MartianManhunter_Illuminati/03_JOHNJONES_SALES_PRINCIPLES.md` (8 principes de 2 sources réelles). S1 Grand Slam Offer, S2 équation de valeur Hormozi, S3 inversion de risque, S4 pricing premium déconnecté du coût, S5 découpler revenu/temps, S6 freelance→cabinet conseil (architecte de solutions), S7 tunnel d'acquisition plateforme-indépendant, S8 case studies ROI. North Star = conversion (KR-2a close>30%). Squad Illuminati mappé au canon Notion (Black Bolt/Iron Man/Mr Fantastic/Namor/Professor X/Doctor Strange). John Jones non-délégable pricing + qualification. **Backlog v2 = corpus Dan Martell (28 vidéos)**.

**Growth** : note `Inbox v3` ajoutée dans `01_Growth_Superman_Guardians/04_SUPERMAN_EXTRACTION_QUEUE.md` (playbook $100M AI Agency → positionnement mid-market / défendabilité post-2027, à distiller par Superman).

**État Area J01** : Growth ✅ (SHADOW_ACTIVE, 18) · Product ✅ (CANONICAL, 18) · Ops ✅ (CANONICAL, 22) · Sales 🟡 (v1 début, 8 + backlog Dan Martell). Restants : IT, Finance, People, Legal.

---

## 2026-05-31 (suite 2) — Skill area-domain-doctrine-distill mis au travail : IT + Finance + People + Legal + Sales v2

**Skill utilisé** : `area-domain-doctrine-distill` (créé plus tôt ce jour) — première mise en production.

**Triage corpus (honnêteté d'abord)** : IT `03_IT` = **322 fiches REAL** (riche) ; Finance/People/Legal `04/05/08` = **0 fichier (vides)** ; Sales backlog Dan Martell = **index de titres, pas de contenu**.

**Découverte clé** : corpus externe vide ≠ pas de doctrine. Finance/People/Legal ont un **canon interne riche** (`B3_Squad_*/00_B3_SQUAD_CANON.md` transcrits de Notion AGENT_REGISTRY_DB + control rooms KR). → distillation `CANONICAL_FROM_CANON` (honnêtement interne, corpus externe pending), pas de scaffold PENDING, pas de fabrication. Leçon ajoutée au skill `references/domain-map.md`.

**4 doctrines créées** (+ READMEs) :
- **IT — Cyborg/Kang Dynasty** `05_IT…/03_CYBORG_IT_PRINCIPLES.md` : 18 principes, CANONICAL (corpus 322 + Kang canon). Clusters Agentic Engineering / Context&Memory / Sovereign Local Stack / Infra&Security. Sources réelles : Cole Medin (harnesses, tech stack 2026, local AI), Mark Kashef (self-improving), cocadmin (VPC). ⚠ flag honnête : sous-ensemble des fiches = boilerplate template dégénéré, NON utilisé. Squad Kang Prime/Iron Lad/Scarlet Centurion/Immortus/Victor Timely/Rama-Tut. Cyborg owns architecture (Jerry non). North Star KR-5a..c.
- **Finance — Wonder Woman/Thunderbolts** `06_Finance…/03_WONDERWOMAN_FINANCE_PRINCIPLES.md` : 12 principes CANONICAL_FROM_CANON. Cash/runway, marge réelle (post compute+API+Stripe), transparence anti-vanity, reconciliation, compliance. Squad Bucky/Yelena/Red Guardian/Ghost/Taskmaster/US Agent. North Star KR-5d..g. WW non-délégable pricing + reinvest.
- **People — Green Lantern/X-Men** `07_People…/03_GREENLANTERN_PEOPLE_PRINCIPLES.md` : 12 principes CANONICAL_FROM_CANON. **Twist A'Space** : People onboarde aussi les capsules IA (Codex/Gemini/Claude) avec dignité + Ethics&Alignment (SDD-001). Squad Prof X/Cyclops/Jean Grey/Wolverine/Storm/Beast/Nightcrawler/Rogue. North Star KR-7a..d. GL non-délégable headcount (12mo runway) + retention.
- **Legal — Aquaman/Eternals** `08_Legal…/03_AQUAMAN_LEGAL_PRINCIPLES.md` : 12 principes CANONICAL_FROM_CANON. Contrats/RGPD/IP, vélocité+rigueur, gate de conformité cross-domaine (le `legal_gate` du skill Growth). Squad 10 Eternals (Ikaris…Makkari). North Star KR-8a..d. Aquaman non-délégable escalation contrat + priorité IP.

**Sales v2** : **bloqué sur transcription** (Dan Martell = 28 titres, 0 transcript). Distiller de titres = fabrication → refusé. Note transparente ajoutée à la doctrine Sales ; reste v1 début (8). v2 se débloque dès transcripts.

**État 8 domaines Area complets (J01)** : Growth ✅18 · Sales 🟡8 (v2 bloqué) · Product ✅18 · Ops ✅22 · IT ✅18 · Finance ✅12 · People ✅12 · Legal ✅12. **La matrice 8/8 est posée.**

**Backlog v2 commun** : transcrire les corpus externes manquants (Finance/People/Legal vides, Sales/Dan Martell titres-seuls) puis re-distiller. Le skill `area-domain-doctrine-distill` rejoue le pattern à l'identique.

---

## 2026-05-31 (suite 3) - L2 B1/B2/B3 developpe en detail (4 livrables, scope complet A0)

**Intention A0** : comprendre A1/A2/A3 de L0/L1/L2 + developper en detail B1/B2/B3 de L2. (People confirme = Lore A0, aucun corpus externe.)

**Comprehension ancree sur AGENTS.md** : A-rank global (A0 Pilote ; A1 Rick / Beth+Morty / Jerry+Summer ; A2 Doctors / USS / 8 heros ; A3 companions / crews / 8 squads). B-rank = A localise a L2 en stack Direction(B1) -> Domaines(B2) -> Execution(B3), repete en miroir fractal Macro (Jerry Area, perpetuel) <-> Micro (projets Picard, graduent, referencent DRY).

**4 livrables (Air Lock leve par choix A0 des 4 options)** :
1. Synthese canonique : 02_Areas_Spock/J01_Jerry_Prime_LD01_Business/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md (skeleton complet : mapping A<->B, miroir macro/micro, flux + stop conditions, 8-wheel, reading map) + abstraction wiki concepts/concept_l2_fractal_b1b2b3.md.
2. DECISION_CHARTER B1 : B1_Area_Direction/03_DECISION_CHARTER.md (etait VIDE 3o) -> droits RACI par rang, decisions B2 non-delegables, vetos (A0/B1/Finance/Legal/peer), seuils d'escalade, output packet.
3. Reconciliation rosters : wiki/comparisons/comparison_l2_roster_divergence.md (AGENTS.md abrege 4-membres vs B3 canon Notion 4-10 ; 2 vraies divergences = Finance Thunderbolts + Sales Illuminati ; reco = Notion source de verite, AGENTS.md immuable -> nouvel ADR ; AWAITING_A0_RULING).
4. 7 packets JTBD-001 B3 (Sales/Product/Ops/IT/Finance/People/Legal) dans B3_Area_Warp_Core/<dom>/ mirroring le packet Growth, ancres doctrine + squad canon + KR, evidence_grade HYPOTHESIS + entrees proof-log.

**Decision A0 en attente** : trancher la divergence de roster (Finance/Sales) -> nouvel ADR ADR-CANON-00X_roster-source-of-truth. AGENTS.md NON reecrit (canon immuable).


---

## 2026-06-02 - Finance v2 (Empire/Kardashev) + capture 5 videos

**Intention A0** : doctrine Finance trop modeste. Mindset = Empereur post-Hustle (Jay-Z zero->billionaire). Survie = Billion Dollar Brand Club ; ambition = orchestrer marches trillion->centaines de trillions via innovation biomimetique + Smart High-Low Tech, vers civilisation Solarpunk Kardashev Type 1-4. Trillion = resultat gagne, pas slogan (anti-PNL).

**Contrainte honnetete** : pas d''outil de fetch YouTube en session (browser/notebooklm/desktop-commander deconnectes). Donc : liens -> CSV ; themes A0 -> capsules ; cadrage A0 -> doctrine (directive canon, pas fabrication).

**Fait** :
1. CSV YouTube (watch_history_rag.csv) : 3 nouvelles lignes (YT-21L-iujzy9U, YT-3Bfx4osqbfE, YT-WvLSwab0TsY ; 1 deja en historique) + topic YC-trillion. Status CAPTURED, serendipity 9. id<->titre A CONFIRMER (pas de fetch).
2. 5 fiches CONCEPT_CAPSULE dans 04_Finance/ : Jay-Z empereur, Matt Gray CEO-OS Claude Code (700k/mo), BFM solo-billionaire-IA, YC trillion markets, Money Radar grand transfert de richesse.
3. Finance doctrine -> v2 : ajout mandat two-horizon (floor survie Billion Dollar Brand Club F1-F12 / ceiling Empire-Kardashev F13-F18) + 6 principes ambition (F13 two-horizon accounting, F14 ownership>income, F15 value-per-agent, F16 create/orchestrate trillion markets, F17 great wealth transfer, F18 earn-the-slogan anti-PNL). CEO Dashboard (Matt Gray) = instrument cockpit Jerry/Summer. Floor jamais sacrifie pour le ceiling.

**v3 = transcription** : durcir F13-F18 avec mecaniques reelles (math trillion-TAM, spec CEO-OS dashboard) quand transcripts dispo.

**Prochain** : meme upgrade ambition pour People + Legal (A0 a dit People/Legal/Finance pas ouf -> Finance fait, People/Legal a suivre). Demander a A0 le cadrage People/Legal (People = Lore A0, Legal = ?).


---

## 2026-06-02 (suite) - Legal v2 (Abondance/Federation) + People v2 (Harness)

**Legal -> v2 (Abundance/Federation)** : cadrage A0 = Legal gouverne l''abondance (Solarpunk -> Kardashev via biomimetisme + economie bleue circulaire + acuponcture urbaine, Federation Star Trek 10000 ans). Ajout L13-L18 : L13 two-horizon Legal, L14 gouverner pour l''abondance (pas la rarete), L15 doctrine IP biomimetique (proteger l''application, garder le principe bio en commun), L16 compliance economie bleue circulaire (cradle-to-cradle, EPR, material passports), L17 craft regulatoire d''acuponcture urbaine (permis/zoning/CLT), L18 cadre Federation 10000 ans. legal_gate elargi : veto aussi le rent-seeking anti-abondance. Eternals = gardiens immortels long-horizon (fit parfait).

**People -> v2 (Harness layer)** : cadrage A0 = au-dela du Lore, le **harness EST le corps** de l''agent. Nouvelle ressource creee 08_People/agent-harnesses-hermes-claude-code.md (contenu reel A0 : features Hermes Workspace + Hermes Agent + Claude Code). Ajout PE13-PE18 : PE13 harness=corps (Claude Code + Hermes), PE14 model-agnostic (GLM 4.7 Flash OpenRouter / MiniMax token plan / Claude swappables), PE15 affordability soutient le swarm 24/7, PE16 fichiers identite (SOUL.md/AGENTS.md/CLAUDE.md) pilotent le corps (Hermes les auto-charge), PE17 swarm+review-gate natifs Hermes (= B3 swarm + Build Gate incarnes ; ecosysteme incontournable hermes-workspace.com), PE18 heartbeat cron = autonomie fluide (Hermes cron #15400 ou Shadow L0 heartbeat). Selection harness co-decidee People (membre) + IT/Cyborg (runtime).

**Hook Skill-Reflex** : faux-positif mots-cles (install/batch/workflow/handoff dans le message A0). PAS de /skill-creator invoque - aucun nouveau skill justifie (area-domain-doctrine-distill couvre deja les upgrades doctrine). Jugement > declencheur litteral.

**Candidat skill en queue (PROPOSED, pas construit - premature)** : /hermes-harness-onboard - installer + cabler un harness Hermes (Workspace + Agent + cron heartbeat) pour une capsule A'Space, model-agnostic (GLM/MiniMax), avec auto-load AGENTS.md/SOUL.md. A construire quand A0 voudra wirer Hermes pour de vrai.

**Etat ambition-layer domaines** : Finance v2 (Empire/Kardashev) FAIT, Legal v2 (Abondance) FAIT, People v2 (Harness) FAIT. Growth/Product/Ops/IT = doctrines deja solides (corpus reel), pas d''upgrade ambition demande. Sales = v1 (bloque transcription Dan Martell).


---

## 2026-06-02 (suite 2) - Sales v2 complet (8 -> 14) + frontiere BDBC

**Question A0** : ajouter Million Dollar Weekend + Billion Dollar Brand Club a Sales ? + propositions ressources.
**Reponse honnete (loi de frontiere ADR-MESH-L2-001)** : MDW = OUI (facette Sales = the ASK/pre-vente). BDBC = NON a Sales (c''est Growth P6 marque + Finance v2 mode survie ; l''ajouter dupliquerait). A0 a choisi les 4 options -> Sales v2 complet.

**Fait** :
- 5 fiches framework dans 06_Sales/ : Million Dollar Weekend (Kagan), SPIN Selling (Rackham), Gap Selling (Keenan), The Challenger Sale (Dixon), Never Split the Difference (Voss). CONCEPT_CAPSULE (frameworks publics nommes, standard Hormozi).
- Sales doctrine -> v2 CANONICAL (8 -> 14 principes). Cluster E Discovery/Qualification (S9 pre-vente/the ASK, S10 SPIN+Gap discovery centree-probleme, S11 qualification MEDDIC/multi-threading) + Cluster F Persuasion/Negociation (S12 Challenger teach/tailor/take-control, S13 Voss tactical empathy/objection, S14 speed-to-close). Comble le vrai manque (discovery/objection/negociation faibles en v1).
- Note de frontiere bakee : BDBC n''est PAS un principe Sales -> pointe vers Growth/Finance.
- Squad table maj (refs S9-S14). Extension plan -> v3 = transcription Dan Martell.
- Pas d''ajout au CSV YouTube : ce sont des livres (pas de YT id) ; si A0 veut les versions video, fournir les liens comme pour les 5 videos Finance.

**Etat Sales** : v2 CANONICAL (14). v3 bloque transcription Dan Martell (28 videos).


---

## 2026-06-02 (suite 3) - Alignement fractal Jerry-Summer + structure projets Picard

**Intention A0** : faire l alignement de la fractal Jerry/Summer + structurer les projets Summer dans Picard avec B1/B2/B3.

**Etat constate** : les 7 projets Picard ont DEJA leur skeleton B1/B2/B3 + SUMMERS_VERSE_MANIFEST.md (B1 vision 1/3/10A, modes, 12WY) + CERRIROS_HANDOVER. Le register Picard_Summers_Verse_Register.md existait et REFERENCAIT JERRY_SUMMER_FRACTAL_ALIGNMENT.md - mais ce fichier n etait qu un stub leger.

**Fait** :
1. JERRY_SUMMER_FRACTAL_ALIGNMENT.md consolide en version complete (superset du stub) : pont macro<->micro, mapping B1/B2/B3 par rang, contrat DRY (projet pointe vers doctrine macro, jamais copie), flux de commande (A0->Jerry->Cerritos->Picard->Summer B1->B2->B3->proof remonte), calibration par mode (Solaris/Nexus/Orbiter), 6-books->8-domains, portfolio des 7 projets avec cas speciaux (00 AaaS flagship Growth ; 02 ABC compliance->legal-gate ; 04 Alikaly THIN Growth DEFERRED ; 05 marina franchise Orbiter ; 01-omk mirror no-dup), regles graduation + Product-Isolation, note Deep-Checkpoint (arbres B2 pollues par recursion de liens portail = PAS touches).
2. Register rafraichi : section Macro doctrine to reference (DRY) pointant vers les 8 doctrines + 8 packets JTBD-001 + skeleton + charter + bridge maintenant complets.

**Honnetete** : je n ai PAS touche aux B2_Business_Domains des projets (milliers de fichiers = recursion 00_Links/30_Business_OS_Portal/...). Nettoyage = tache Ops/IT separee (inventaire avant purge, Loi Checkpoint).

**Etat L2** : macro (Jerry Area) complet B0/B1/B2x8/B3x8 + skeleton + charter ; micro (Summer/Picard) aligne + register + bridge. La fractal est explicitement cablee macro<->micro.


---

## 2026-06-02 (suite 4) - Finance v3 + Legal v3 (corpus reel Geordi)

**Contexte** : Codex a pose l alignement Jerry-Summer pendant mon indispo. A0 -> MAJ Finance + Legal depuis les NOUVEAUX guides Geordi.

**Constat** : 04_Finance contient maintenant 25 fiches REELLES (mes 5 capsules devenues fiches completes + Codie Sanchez x8 + Finary x7 + Timo Studio x5 + YC/Vori + Money Radar 84T). 05_Legal contient 5 fiches StorieRAP (pactes rap/contrats, MyHeritage ADN x2, surveillance masse France).

**Finance v2 -> v3 (field-grounded)** : F13-F18 (Empire/Kardashev) ne sont plus directive-only -> ancres sources reelles (F16<-YC/Vori digitiser industries analogiques fondamentales ; F17<-Money Radar 84T great wealth transfer ; F14/F18<-Codie Leverage Ladder + Jay-Z ownership masters). Ajout Cluster G F19-F22 : F19 allocation tresorerie par pyramide d investissement (Finary, ETF passif SPIVA, DCA), F20 Leverage Ladder/own appreciating assets (Codie), F21 roll-up consolidation comme chemin trillion concret (Huizenga/Codie : industrie fragmentee -> acquerir -> moat reseau), F22 heavy-asset moat > thin AI wrapper (YC/Vori Halo business). 22 principes total.

**Legal v2 -> v3** : 2 couches, 2 grades de preuve (declares honnetement) - L13-L18 (Abondance) restent directive (corpus externe ne couvre pas encore regen-economy/biomimetic-IP) ; ajout L19-L22 (Data-Rights/Privacy/Contract-defense) FIELD-GROUNDED par StorieRAP : L19 own-your-masters/anti-predatory-contract (360 deals, cession masters, avances cross-collateralisees), L20 donnees biometriques/genetiques inalienables (piege MyHeritage : la donnee EST le produit), L21 resistance surveillance + souverainete donnees (Art. 78-3 CPP, CNIL droit-effacement, hygiene TAJ/FPR, grey-man), L22 consented-metadata-only/zero-knowledge. 22 principes total.

**Honnetete** : ⚠ les fiches StorieRAP melent du droit legitime ET du framing ideologique culture-war - je n ai distille QUE le droit (contrats/biometrie/surveillance/CNIL), framing polemique ECARTE comme bruit, declare dans frontmatter Legal.

**v4 backlog** : Finance = Timo creator-economy (cultural arbitrage pricing power) + Finary macro + Dan Martell 13 ; Legal = corpus regen/circular-economy law + biomimetic IP precedent pour durcir L13-L18.


---

## 2026-06-02 (suite 5) - People v3 (corpus reel 08_People)

**Constat** : 08_People contient maintenant 8 fiches REELLES (Ali Abdaal x3 : build systems, micro-habits/focus, mindset ; Tiago Forte x4 : Notion second brain, no-meetings, business-runs-itself, AI SOPs ; Shubham Sharma : Claude Cowork) + ma capsule harness. C est le cote HUMAIN/operateur (productivite, habitudes, focus, mindset, second brain, culture async) qui completait la couche AI-capsule/harness.

**People v2 -> v3** : 
- PE13 harness : ajout Claude Cowork comme 3e corps (macOS sandboxe + Chrome, no-code, browser-piloting MCP, no-delete) a cote de Claude Code + Hermes.
- Nouveau Cluster Human-Member Effectiveness PE19-PE24 : PE19 run-on-systems-not-willpower (Ali, effort-curve), PE20 micro-habits/regle-5-min + ingenierie environnement (Ali), PE21 iteration mindset (Region Beta Paradox, One-Shot Brain -> infinite-shot, Discover>Defend ; mirror IT P5), PE22 second brain/quick-capture <30s + Daily Page (Tiago ; pont L1 PARA), PE23 culture async/no-meetings (facet culture ; mecanique auto -> Ops/IT), PE24 develop-owners/delegate-decisions + RACI (Tiago ; mecanique SOP -> Ops P12). 24 principes total.

**Frontiere respectee** : les parties systematisation business (AI SOPs, pipelines auto, founder-stages org-mapping) POINTENT vers Ops (Batman), pas dupliquees. People = developpe le MEMBRE (esprit/habitudes/ownership) ; Ops = construit le SYSTEME. Note de frontiere bakee.

**v4 backlog** : /hermes-harness-onboard (skill queue, toujours premature) ; durcir PE17/PE18 quand Hermes Workspace+cron wires ; Dan Martell 24 People (titres only).


---

## 2026-06-02 (suite 6) - 12WY_Area_Cadence developpe (moteur hebdo)

**Constat** : 12WY_Area_Cadence deja bien developpe (README + 3 phases W01-04 Foundation / W05-08 Scaling / W09-12 Optimization avec Rocks/lead-lag/checklists/open-close). Vrai trou : le MOTEUR HEBDOMADAIRE - coeur du 12WY (la semaine = unite d execution), absent (que mensuel/trimestriel). Plus : pas de mapping C1-C4, pas de lien Baserow/Warp-Core 50/30/20, pas de lien aux 8 doctrines B2.

**Fait (additif, je n ai PAS reecrit les 3 phases)** :
1. README enrichi : (a) Weekly Execution Engine (lead vs lag, Execution Score = % tactiques completees, regle >=85% on-track, WAM 30min), (b) rythme 4 tempos (daily needle-mover / weekly WAM / monthly W2-6-10 / quarterly W4-8-12), (c) mapping C1-C4 command cycles -> gates sur les 3 phases (C1 Open W1, C2 W4, C3 W5-8, C4 W12), (d) lien Baserow 12WY Symphony L1 (Quarter Intent/12 Rocks Rock-L2/Warp Core 50-30-20 ; Plane cycle = 1 semaine Warp Core), (e) discipline 4-Rock (AREA_STANDARD P8) + scan desequilibre 8-wheel.
2. WEEKLY_EXECUTION_TEMPLATE.md cree : bloc YAML hebdo (score last week + commit Top-3 50/30/20 + lead/lag pointeurs + blockers nommes + decisions), script WAM 5 etapes, table zone (GREEN>=85/ORANGE70-84/RED<70 -> action), anti-patterns. Pointeurs Finance_Pulse (pas de copie).

**Pont doctrine** : RED execution -> People PE19-PE21 (systemes/habitudes, pas willpower) ; decisions -> B1 Decision Charter packet ; blockers -> peer-unblock B3 puis seuil intervention B1.

**Note** : Sales v3 delegue a Antigravity (Dan Martell audit) par A0 - en cours hors de cette session.

## 2026-06-02 - ADR-CANON-001 Roster Source of Truth (A0 RULED)
- A0 ruling: Notion AGENT_REGISTRY_DB + transcriptions = canon prime for L2 B3 squad roster lore.
- AGENTS.md = structure index (immutable body preserved); Reconciliation Addendum appended.
- 2 genuine divergences resolved in Notion favour: Finance -> Bucky-led Thunderbolts (Bucky, Yelena, Red Guardian, Ghost, Taskmaster, U.S. Agent; Red Hulk/Zemo retired); Sales -> Black Bolt-led Illuminati (named members; generic Illuminati I-V retired).
- Verified: no working doctrine surface carried old names; only AGENTS.md, now reconciled.
- Artifacts: _SPECS/ADR/ADR-CANON-001_roster-source-of-truth.md; AGENTS.md addendum; comparison_l2_roster_divergence.md flipped AWAITING_A0_RULING -> RULED.
- Follow-up (non-blocking): rename/align agents/L2_A3_*.md capsule files to Notion roster.

---

## 2026-06-10 — 4 handoffs en 1 session, candidat skill `/project-handoff` [PROPOSED]

**Contexte déclencheur** : A0 a demandé 4 handoffs successifs dans la même session pour libérer la session des travaux techniques :
1. `handoff_graphify_full_build_2026-06-10.md` (build technique, calibration $0.0072/file)
2. `handoff_abc_os_community_dev_2026-06-10.md` (migration Next.js, 7 tickets dont Vercel /build)
3. `handoff_omk_dashboard_dev_2026-06-10.md` (rebuild Supabase multi-tenant, 4 ADR blockers)
4. `handoff_solaris_dev_2026-06-10.md` (greenfield, Airlock Protocol ticket #1)

**Pattern observé** : structure identique à 4 reprises (Project overview / State / Open tickets / Files to read FIRST / Quick start / Deploy / Gotchas / Recommended order / Verification / Write back / Residual risks / Next safe action / Skill proposal / Secret handling). Les 4 handoffs partagent 60-70% de leur structure, le delta étant le contenu spécifique au projet.

**Trigger pattern** : handoff manuel + scaffold récurrent (RULE-4 + RULE-5 du Skill Creator Reflex).

**ROI estimé** : ~10-15 min/invoc × ~4-6 handoffs/mois ≈ 40-90 min/mois économisés. Le gain principal = ne pas re-rédiger la structure (Project overview / Files to read FIRST / Quick start / Gotchas / Verification / Write back / Secret handling) à chaque handoff — l'agent remplit juste les sections spécifiques au projet.

**Auteur proposition** : Claude Code CLI · 2026-06-10 (post-session 4-handoffs).

**Pré-requis** : `Read`, `Glob`, `Grep`, `Write`, `Bash` (pour `ls`/`wc`/git log), `AskUserQuestion` (pour Airlock Protocol).

**Steps proposés** :
  1. Recevoir le nom du projet (path absolu ou nom canon) + intention A0 (type de handoff : dev/rebuild/migration/audit/greenfield).
  2. **Airlock check** : Glob + Grep sur le nom pour vérifier que le projet existe. Si absent → AskUserQuestion pour désambiguïser (mode/projet/canon/ADR) avant d'écrire.
  3. Si présent : identifier le type (migration/rebuild/greenfield) via les fichiers structurants (`REBUILD_WORKFLOW.md`/`picard_audit.md`/`AGENTS.md`/`_doctrine` symlink/`SUMMERS_VERSE_MANIFEST.md`/`_SPECS/ADR/*`).
  4. Lire les 5-8 fichiers-clés (gating order : contrat > audit > doctrine > package.json > env example > supabase/mode config).
  5. Générer le path handoff `LLM_Wiki/wiki/hand_offs/handoff_<project>_<intent>_2026-06-10.md`.
  6. Scaffolder les 14 sections canoniques :
     - Frontmatter (source, date, type, status, domain, tags, related)
     - Why this handoff exists (paragraphe court)
     - Project overview (paragraphe canon depuis doctrine junction)
     - The N apps in this project (table rôle/stack/git/vercel)
     - State (phase-by-phase state table + ✅ built tree)
     - Open tickets (CRITICAL first, with action verb)
     - Files to read FIRST (ordered contract)
     - Quick start commands
     - Deploy workflow (per ADR-INFRA-002 et per-target)
     - Gotchas (10 items, 1 ligne chacun)
     - Recommended order of work (numbered list, D1 verify-before-assert gates)
     - Verification (D5 proof on file, table phase→verification)
     - Write back protocol (4 fichiers canon)
     - Residual risks (7-10 items)
     - Next safe action for receiving session (5 steps)
     - Skill proposal (open follow-up)
     - Secret handling (PUBLIC vs SERVER_ONLY, rotation flags)
  7. Append `### /project-handoff [PROPOSED]` à `skills_queue.md` (méta-réflexe).
  8. Logger dans `LLM_Wiki/wiki/log.md` au format `[YYYY-MM-DD] handoff | <project> | <intent>`.

**Variables attendues** :
  - `<project-path>` : chemin absolu `C:\Users\amado\ASpace_OS_V2\...` ou nom canon (ex: `omk-dashboard`).
  - `<intent>` : `dev` | `rebuild` | `migration` | `audit` | `greenfield` | `bugfix` | `perf` (extensible).
  - `<session-context>` : pourquoi la session est libérée (optionnel mais utile pour le "Why this handoff exists").

**Risques** :
  - Faux-positifs Airlock (projet existe sous un autre nom) → mitigation : AskUserQuestion avec 4 options (mode/projet/canon/ADR).
  - Génération d'un handoff trop générique (perte de la valeur spécifique au projet) → mitigation : le scaffold impose les sections canoniques mais l'agent doit remplir le contenu spécifique ; checklist de 14 sections ≠ copier-coller.
  - Bloat du fichier handoff (la structure fixe consomme ~30% de l'espace) → mitigation : sections courtes + tableaux denses.
  - Désalignement avec le `_doctrine` symlink → mitigation : l'étape 4 inclut la lecture du symlink et de la Picard doctrine associée.
  - Hardcoder des secrets dans le handoff → mitigation : section "Secret handling" impose le pattern PUBLIC vs SERVER_ONLY + référence rotation.

**Patterns à respecter** :
  - 14 sections canoniques ordonnées (cf. Steps §6)
  - Frontmatter YAML avec 7 champs minimum
  - Tableau "State" en ASCII propre
  - "Open tickets" commence par CRITICAL puis HIGH puis MEDIUM
  - "Files to read FIRST" numéroté + path absolu
  - "Verification" en table `Step | Verification`
  - "Residual risks" en 7-10 items
  - Pas de "I" / pas de voix passive / pas de "I think" — factuel, vérifiable
  - Toujours finir par "Next safe action" + "Secret handling"

**État actuel** : 4 handoffs rédigés à la main servant de corpus de référence. Le pattern est stable depuis 2 (ABC OS + OMK sont quasi-identiques structurellement). Le skill économiserait ~30% du temps de rédaction par handoff.

**Validation A0** : pending. Si approved, prochaine session fait `/skill-creator project-handoff` et archive les 4 handoffs en exemples dans le skill.

**Cross-refs** :
  - 4 handoffs : `handoff_graphify_full_build_2026-06-10.md` · `handoff_abc_os_community_dev_2026-06-10.md` · `handoff_omk_dashboard_dev_2026-06-10.md` · `handoff_solaris_dev_2026-06-10.md`
  - Doctrine canonique Airlock : `MEMORY.md` (Hallucinating canon protocols anti-pattern)
  - Doctrine "Skill Creator Reflex" : `CLAUDE.md` (5 triggers, format proposition)
  - Skill queue file : `LLM_Wiki/wiki/hand_offs/skills_queue.md`
  - Pattern pré-existant (handoff) : `/shadow-handoff` [PROPOSED 2026-05-17] — couvre le cas Shadow L0↔L1↔L2 mais PAS le cas L2 projet↔projet. `/project-handoff` est complémentaire, pas redondant.

---

## /a3-scaffold-from-template [PROPOSED 2026-06-15]

**Triggers observés** : #1 (batch, 3+ tool calls répétés : Read A2 spec + Read A2 profile + Read template + Write N profiles) · #4 (scaffold detection : 35 fichiers générés depuis 1 template canon).

**Workflow canonique (5 steps)** :
1. **Read** : `~/.claude/agents/_a3-template.md` (template canon)
2. **Read** : `ASpace_OS_V2/20_Life_OS/2X_<Ship>/A2_*_Spec.md` (source of truth A3 details)
3. **Read** : `~/.claude/agents/a2-uss-<ship>.md` (style reference A2 profile format)
4. **Spawn** : 1 sub-agent A3 par ship (D8 parallel) qui lit les 3 fichiers + écrit N A3 profiles en parallèle
5. **Verify D1** : glob count, ls -la, grep anti-patterns (Picard-as-A2, Sia, Holo-Janeway-hyphen, Freeman-as-A2)

**ROI estimé** : ~10 min/ship (vs ~30 min manuel par ship) × 6 ships = ~120 min économisées sur un full canon run.

**Corpus d'exemples disponibles** : 35 A3 profiles canon à `~/.claude/agents/a3-*.md` (référence qualité + format) · 6 A2 specs à `ASpace_OS_V2/20_Life_OS/2X_*/A2_*_Spec.md` (sources of truth) · 6 A2 profiles à `~/.claude/agents/a2-uss-*.md` (style anchors).

**Doctrine ancrage** : D1 (verify-before-assert, 35/35 receipts) · D2 (research-first, template+spec+style read) · D4 (append-only strict, no destructive) · D7 (lazy-creation cost pre-paid when full canon justified) · D8 (sub-agents en parallèle).

**Validation A0** : pending. Si approved, prochaine session fait `/skill-creator a3-scaffold-from-template` et archive les 35 A3 + 6 A2 specs comme exemples canon.

---

## /symphony-phase2-batch [CREATED 2026-06-15 — Phase 2 doctrine auto-invocation]

**Triggers observés** : #1 (batch, 8 sub-agents parallèles : re-twin A1+A2 + 35 A3 twins + 4 MCPs + 6 bridges) · #4 (scaffold detection : 49 fichiers générés depuis 1 INDEX canon) · #4 (handoff delegation pattern, 1 A0 turn → 8 sub-agents → 4 lots).

**Workflow canonique (5 steps)** :
1. **Read** : 5 INDEX files (INDEX_specs.md, INDEX_capsules.md, INDEX_runtime.md, lane_A_specs/02_A2_ships/*.twin.md, skills_queue.md)
2. **Spawn** : 8 sub-agents en parallèle (D8) — 1 re-twin A1+A2, 6 A3 twins (1/ship), 1 MCPs (4 servers), 1 bridges (6 wirings)
3. **Verify D1** : `find -name` count + `ast.parse -X utf8` + `grep` anti-patterns (Picard/Freeman-as-A2, Sia, HoloJaneway-hyphen, Ship Captain)
4. **Archive D4** : 35 v0 legacy twins → `_TRASH_2026-06-15_legacy_v0/` (no-hard-delete)
5. **Write-back** : wiki/log.md + INDEX_*.md + MEMORY.md (INDEX-ONLY 5 lines)

**ROI observé (2026-06-15)** : 8 sub-agents + D1 verify + write-back ≈ 120 min. Runs subséquents : 15-30 min si cache hit INDEX files.

**Corpus d'exemples disponibles** : 49 fichiers canon (8 A1+A2 twins v1.1, 35 A3 v1 twins, 4 MCP Python servers, 6 bridges Python wirings) + 35 A3 v0 archived in `_TRASH_`.

**Doctrine ancrage** : D1 (independent verify after sub-agents) · D2 (5 INDEX files read-first) · D4 (35 v0 archived, no rm) · D6 (5 anti-patterns identified) · D7 (8 sub-agents = 1 A0 turn vs 35) · D8 (Python MCP + bridges, env var auth) · Test Key Pragma (no hardcoded keys).

**Skill location** : `C:\Users\amado\.claude\skills\symphony-phase2-batch\SKILL.md`

---

## /multi-goal [PROPOSED 2026-06-21 — A0 doctrine]

**Triggers observés** : /goal natif CC existe (CHANGELOG 2.1.139, "set a completion condition and Claude keeps working across turns until it's met") MAIS = single-agent loop. Besoin = multi-agent multi-workflow A1/A2/A3 routage.

**Workflow canonique (5 steps)** :
1. **Turn 1 Air Lock** : clarifier intention A0 — quel outcome définit "GO" ? (livrable concret, état vérifiable, signal observable)
2. **Route A1 → A2** : si outcome = sens/alignement (Ikigai Lock) → Beth → Orville Ed+Kelly. Si outcome = exécution/cadence → Morty → Curie SNW Pike+Una+Ortegas
3. **Spawn N sub-agents A3 //** : général-purpose agents, chacun lit 1 source canon (handoff_*, AGENTS.md, ADR, transcript YouTube, MCP data)
4. **Symphony orchestration** : chaque sub-agent écrit dans `state.json` (state-bus.v1) + flag `next_step`
5. **GO detection** : Beth (veto) ou Morty (routeur) lit le `state.json` final → si tous critères OK, retourne `<DONE>` au Main Agent → TTS stop hook Hortense

**ROI estimé** : ~20-40 min/invocation. Invoqué 2-5×/semaine par A0 board observer (H30 cadence).

**Corpus d'exemples disponibles** : 35 A3 twins canon (`symphony/L1/lane_A_specs/03_A3_crews/`), state.json (Amorçage 1), handoff_a0_divinity_arsenal §7.

**Doctrine ancrage** : D1 (verify via state.json avant `<DONE>`) · D2 (read canon avant spawn) · D3 (Ikigai = A2 Orville ≠ A1 Beth) · D7 (8 sub-agents // = 1 A0 turn) · Test Key Pragma.

**Skill location** : `C:\Users\amado\.claude\skills\multi-goal\SKILL.md` (à créer via `/skill-creator`)

---

## /multi-loop-karpathy [PROPOSED 2026-06-21 — A0 doctrine]

**Triggers observés** : `/loop` natif CC borné 7 jours ("automatically expire 7 days after creation") + session-scoped. Incompatible avec cycle Q3 2026 (06/15→09/07/26 = 84 jours). Besoin = loop multi-workflow qui orchestre Karpathy auto-research pattern sur la durée du cycle 12WY.

**Workflow canonique (5 steps)** :
1. **Turn 1 Air Lock** : clarifier sujet recherche + cadence (daily/weekly/cycle) + duration (cycle 12WY = 84j)
2. **Route A1 → A2** : Morty → Cerritos Mariner (capture inbox permanent) + SNW Ortegas (daily standup)
3. **Spawn Karpathy loop** : Phase 2 = 8 sub-agents // sur capture topic (capture → process → persist → loop)
4. **Cron anchor** : remplace /loop 7-day bound par `CronCreate` ou `ScheduleWakeup` (bornes plus longues)
5. **Loop detection** : `state.json.next_step` pointe vers nouvelle itération tant que cycle 12WY actif

**ROI estimé** : ~15-30 min/iteration. Invoqué 12×/cycle 12WY (1×/semaine).

**Corpus d'exemples disponibles** : `symphony-phase2-batch` skill (5-step Phase 2 = spawn 8 sub-agents), `fable-autor-research-loop-symphony-agentos` rule (auto-research doctrine), `symphony-fabuleux-discipline` (discipline).

**Doctrine ancrage** : D1 (state.json next_step) · D2 (symphony-phase2-batch precedent) · D7 (cycle Q3 = 12 iterations vs 1 batch) · D8 (cross-agent Claude/Codex/Gemini respectent matrice) · Test Key Pragma.

**Skill location** : `C:\Users\amado\.claude\skills\multi-loop-karpathy\SKILL.md` (à créer via `/skill-creator`)

---

## /multi-routines-12wy [PROPOSED 2026-06-21 — A0 doctrine]

**Triggers observés** : `/routines` n'existe PAS dans CC M3 (D1 confirmed handoff_a0_divinity_arsenal §33). Cycle 12WY Q3 2026 = 12 items verbatim → besoin de transformer chaque item en routine scheduler avec milestones W1/W2/W3/W4. Synergie avec `/routine` (commande custom 2026-06-21) qui orchestre 3-tiers (loop / desktop / cloud).

**Workflow canonique (5 steps)** :
1. **Turn 1 Air Lock** : clarifier cycle Q3 2026 — 12 items, 4 milestones (W1 fin 07/05, W2 fin 07/26, W3 fin 08/16, W4 fin 09/07)
2. **Route A1 → A2** : Morty → SNW 5 disciplines (Pike/Vision → Una/Planning → Chapel/Measure → M'Benga/Focus → Ortegas/Execution)
3. **Schedule routine** : pour chaque item 12WY, créer routine weekly/daily via `/routine` (3-tiers routing selon besoin)
4. **Dispatch swarms** : A3 twins → B1/B2/B3 swarms (Solarpunk, OMK, ABC) en parallèle
5. **Validation milestone** : A0 board observer valide W1/W2/W3/W4 (4 fois max pendant cycle) via `/goal`

**ROI estimé** : ~5-10 min/invocation routine setup. Invoqué 12×/cycle (1×/item setup) + 4 milestones (validation).

**Corpus d'exemples disponibles** : 12 items verbatim cycle Q3 2026 (fancy-hugging-bengio §4), handoff_a0_divinity_arsenal §15 (dette technique Q3), SNW canon (5 disciplines A3 twins).

**Doctrine ancrage** : D1 (state.json milestone tracking) · D3 (Pike/Vision ≠ A2 SNW) · D6 (D6 root cause steerable via checkpoint A0) · D7 (A0 passif board observer 4× max) · Test Key Pragma.

**Skill location** : `C:\Users\amado\.claude\skills\multi-routines-12wy\SKILL.md` (à créer via `/skill-creator`)

---

## /routine [CREATED 2026-06-21 — Commande CC slash custom]

**Path canon** : `C:\Users\amado\.claude\commands\routine.md`

**Statut** : Créée 2026-06-21 (commande slash CC). Skill `routine` détectée automatiquement par le harness.

**Voir aussi** : `/routine` est l'orchestrateur 3-tiers routing (loop / desktop / cloud) utilisé par les 3 skills ci-dessus (`/multi-goal`, `/multi-loop-karpathy`, `/multi-routines-12wy`).

**Phase 2 doctrine justification** : A0 GO explicite 2026-06-15 "go for all Next steps Symphony (Phase 2 candidates)" + Skill Creator Reflex doctrine update 2026-06-13 (Hermes-style auto-improvement, D7 cost > false-positive cost).

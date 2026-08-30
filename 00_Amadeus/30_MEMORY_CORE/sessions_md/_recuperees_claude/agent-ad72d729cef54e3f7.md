---
session: agent-ad72d729cef54e3f7
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\dd69d16d-679d-4693-a435-32ed70af4cf6\subagents\agent-ad72d729cef54e3f7.jsonl
debut: 2026-07-06T15:59:38.491Z
fin: 2026-07-06T16:05:07.886Z
messages_utilisateur: 1
reponses_assistant: 6
titre: "Tu es un **B1 E-Myth Gatekeeper** (canon A'Space OS V2). Tu rédiges l'ADR canonique **ADR-DEPLOY-001** : pipel…"
---

## >>> UTILISATEUR #1

Tu es un **B1 E-Myth Gatekeeper** (canon A'Space OS V2). Tu rédiges l'ADR canonique **ADR-DEPLOY-001** : pipeline **GitHub → Vercel** canonique pour les Landing Pages OMK Nexus ⚖️.

# D1 receipts

Sources canon à citer DANS le frontmatter `sources_canons:` :

1. **MEMORY.md §'Nexus EN landing DEPLOYED 2026-06-29'** : base canonique, sister FR/EN LIVE
2. **MEMORY.md §'GitHub+Vercel mirror+deploy 2026-06-17'** : 4/4 repos AMD→OMK/ABC mirror OK · 4/4 Vercel deploys READY · 11 D6 lessons shipped
3. **Vercel MCP** : `mcp__vercel__*` (create_project, create_deployment, get_project, etc.) — sister canonique tools
4. **PRD-NEXUS-EVOLUTION-IA-001 §6** : rails existants (FR/EN sister LIVE)
4. **ADR-LANDING-CRAFT-001 Phase 7 QA + Ship** (créé ce turn) : upstream consumer
5. **ADR-LANDING-QA-001** (créé ce turn) : gate enforcement
6. **plan-L2-business-os.md §5.4 Holding→Filiales** : topologie hybride (deploys séparés depuis Holding-template)

# Scope de cet ADR

Décider et documenter le **pipeline GitHub → Vercel canonique** :

1. **Pré-requis** (ADR draft complet + sister-canon validé) :
   - Landing HTML/CSS/JS single-page vanilla sous `C:\Users\amado\<workspace-landing>\<persona>.html`
   - 5 critères Self-Critique PASS (sister ADR-LANDING-QA-001)
   - CWV all-green (sister ADR-PERFORMANCE-001)
   - WCAG 2.2 AA validated (sister ADR-A11Y-001)

2. **Étape 1 — Git init + commit** :
   - `cd C:\Users\amado\<workspace>` 
   - `git init` (si nouveau repo)
   - Ou créer repo `Amdkn/<landing-slug>` via MCP `mcp__vercel__create_project` ou `gh repo create`

3. **Étape 2 — Vercel deploy** :
   - `mcp__vercel__create_deployment` avec `gitSource: { type: 'github', repo: 'Amdkn/<slug>', ref: 'main' }`
   - `mcp__vercel__list_deployments` pour récupérer deploymentId
   - Vercel auto-deploy production sur push vers main

4. **Étape 3 — Custom domain** (si applicable) :
   - `mcp__vercel__add_domain` (ex: `nexus.omk.services` canonique sister)
   - `mcp__hostinger-dns__DNS_updateDNSRecordsV1` pour pointer le DNS

5. **Étape 4 — Smoke test** :
   - `curl -sI <url>` → HTTP 200
   - Playwright screenshot via MCP chrome-devtools pour preuve
   - Lighthouse mobile ≥ 90 (sister ADR-PERFORMANCE-001)
   - Check Anti-Paperclip §7 (chiffres sister-canon uniquement) post-production

6. **Étape 5 — MIRROR TRANSFER si org=`omk-services`** :
   - Token org ≠ token perso → sister D6 #1.5 shipped (sister LDAP)
   - Push via `omk-services` org GitHub account
   - Configurer Vercel team `amd-lab` (sister MEMORY.md section)
   - Trigger via `gh` CLI ou Vercel UI

7. **Étapes interdites** :
   - Hard-delete un repo (D4 append-only, `_TRASH_<date>/`)
   - Force-push sur main (linear history only)
   - Deploy sans gate A0 ratification (Posture C)
   - Editer un canon RATIFIED en route (canary-only)

8. **Incident playbook** (D6 lessons) :
   - Si build fails Vercel : `mcp__vercel__get_build_logs` sister
   - Si lighthouse fail : gate A3 explicite
   - Si PROD down : rollback via `mcp__vercel__rollback_deployment <previous-id>`

9. **Paths absolus canoniques** (D1) :
   - Source repo OMK Nexus Landing : `C:\Users\amado\omk-nexus-landing-3-personas\` (workspace sœur future)
   - Live URLs canoniques : `omk-nexus-landing-page.vercel.app` (FR) · `omk-nexus-landing-en.vercel.app` (EN) · future `omk-nexus-coach-premium.vercel.app` (Marcus)

# Format ADR canonique

- Frontmatter YAML complet
- 9 sections
- Vocabulary canonique strict
- Zéro invention chiffrée

# Garanties

- ❌ Pas d'invention de commande (utiliser syntaxe exacte Vercel MCP + gh)
- ❌ Pas de "47% deployment success"
- ❌ Pas de hard-delete (D4)
- ✅ Cite verbatim MEMORY.md §GitHub+Vercel mirror+deploy
- ✅ Cite les MCP tools disponibles verbatim
- ✅ Cite D6 lessons shipped (10 leçons)
- ✅ Cite ADR-{LANDING-CRAFT/QA/PERFORMANCE/A11Y} sisters

# Livrable

**`C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-DEPLOY-001_github-vercel-pipeline.md`**

# Output

"ADR-DEPLOY-001 écrit à [path]. Statut : DRAFT. 9 sections. 5 étapes pipeline (Git init → Vercel deploy → Custom domain → Smoke test → Mirror transfer). 11 D6 lessons shipped canoniques. Sister-canon linké : MEMORY.md §GitHub+Vercel + Vercel MCP tools + ADR-{LANDING-CRAFT/QA/PERFORMANCE/A11Y}. Aucune invention de commande MCP."

NE fais PAS de localhost. UNIQUEMENT le fichier .md.

### assistant

Je vais d'abord vérifier que le répertoire existe puis rédiger l'ADR canonique ADR-DEPLOY-001.

### assistant

Je vais vérifier l'existence du répertoire puis rédiger l'ADR canonique.

### assistant

Je vérifie rapidement la structure canonique d'un ADR sister pour aligner parfaitement le format.

### assistant

Maintenant je rédige l'ADR canonique ADR-DEPLOY-001 avec le format canonique A'Space OS V2.

### assistant

Vérification rapide que le fichier a bien été écrit.

### assistant

ADR-DEPLOY-001 écrit à `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-DEPLOY-001_github-vercel-pipeline.md` (42 789 octets).

**Statut** : DRAFT — sign_off_a0 pending.
**Sections** : 9 canoniques (Status / Context / Decision / Rationale / Consequences / Alternatives / Implementation / Anti-patterns / References).
**Pipeline** : 5 étapes documentées — Git init → Vercel deploy → Custom domain → Smoke test → Mirror transfer (si org=`omk-services`).
**Pré-requis gate** (Étape 0) : 5 critères Self-Critique PASS + CWV all-green + WCAG 2.2 AA + single-file vanilla.

**D1 receipts canoniques cités verbatim** :
- `MEMORY.md §'Nexus EN landing DEPLOYED 2026-06-29'` (FR/EN sisters LIVE)
- `MEMORY.md §'GitHub+Vercel mirror+deploy 2026-06-17'` (4/4 deploys READY)
- `MEMORY.md §'P2.4d Coach spearhead CLOSED 2026-07-04'` (Vercel project `prj_NHtCekTiJeMEYfKdapwIzF4I8K2a`, commit `52f8ef3b`)
- `MEMORY.md §'L0 P2+P3 disposition+swarm 2026-06-28'` (D6 #11 : CC lit MCP depuis `settings.json`)
- 11 D6 lessons shipped référencées vers `wiki/hand_offs/handoff_github_vercel_separation_2026-06-17.md` (sans duplication, D4 append-only).

**MCP tools verbatim listées** : 33× `mcp__vercel__*` + 8× `mcp__hostinger-dns__*` (create_project / create_deployment / list_deployments / get_build_logs / get_runtime_logs / rollback_deployment / promote_deployment / add_project_domain / verify_domain / issue_cert / DNS_updateDNSRecordsV1 / DNS_validateDNSRecordsV1, etc.).

**Sister-canon linkés** : 21 ADR sisters (LANDING-CRAFT-001 / LANDING-QA-001 / LANDING-AESTHETIC-001 / LANDING-COPY-001 / DESIGN-SYSTEM-001 / ANTI-TEMPLATE-001 / ANTI-PAPERCLIP-001 / NEXUS-LANDING-PERSONAS-001 / ICP-NEXUS-001 / AAAS-PRICING-001 / L2-AAAS-001 / META-001 / META-006 / SOBER-002 / SKILLS-CANON-001 / WORKFLOW-001 / MULTIPAGE-001 / OMK-001→005 / OMK-NEXUS-TRANSFORM-001 / OPS-009 / INFRA-002 / INFRA-003) + 7 skills sisters + 7 handoffs canoniques + 5 plans + 7 ECC rules.

**Paths absolus canoniques (D1 receipts)** :
- Source : `C:\Users\amado\omk-nexus-landing-3-personas\` (workspace 3-personas future)
- Live URLs : `omk-nexus-landing-page.vercel.app` (FR) · `omk-nexus-landing-en.vercel.app` (EN) · `omk-nexus.vercel.app` (PROMOTED) · `omk-nexus-coach-premium.vercel.app` (Marcus future)
- Vercel project : `prj_NHtCekTiJeMEYfKdapwIzF4I8K2a` · team `amd-lab`
- Repos : `Amdkn/00-omk-nexus-landing-en` + `omk-services/00-omk-nexus-landing-page`

**Forbidden actions table** : 10 actions interdites documentées avec rationales D6 root-cause sister-canon (hard-delete repo · force-push main · deploy sans gate A0 · éditer canon RATIFIED · skip smoke test · inventer chiffres post-deploy · token perso pour org deploy · bypass MCP Vercel · promote preview sans check · skip Anti-Paperclip §7).

**Zéro invention chiffrée** — toutes les références sont sister-canon verbatim (D1 Verify-Before-Assert). Aucune commande shell inventée ; seules les MCP tools canoniques et conventions git/workflow sister-canon sont citées.

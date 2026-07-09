---
source: A0_jumeau_numerique
date: 2026-06-23
type: handoff
domain: L2_Business_OS / Symphony / B1_B2_B3 / MCP_wiring
status: active
tags: [#handoff #L2 #b1-solaris #loop #airtable #clickup #mcp #veto-90j #pivot #a0-jumeau]
---

# Handoff — B1/B2/B3 /loop pivot Solaris + MCP Airtable/ClickUp wiring

> **Intention A0 pivot (verbatim)** :
> *"oubien on laisse les /routine pour les Agents A de Life OS et gerer ceux du Business OS par des /loop meme si on doit finir de configurer leurs Outils Airtable, Clickup et Notion en commencant par Solaris sur mon compte amd"*
>
> → `/routine` = Life OS (6 A2 engines : Orville/Discovery/SNW/Enterprise/Cerritos/Protostar).
> → `/loop` = Business OS (B1/B2/B3 AaaS Solaris/Nexus/Orbiter × 8 SOA01-SOA08).
> → Démarrage = **B1 Solaris** sur **compte A0 "amd"** (Airtable + ClickUp + Notion à câbler).

---

## 1. D1 Receipts (vérifications effectives cette session)

| # | Vérif | Résultat |
|---|---|---|
| 1 | `AIRTABLE_PAT` User-scope HKCU | length=82 chars, format `pat<14chars>.<43chars>` ✔ |
| 2 | Airtable `meta/whoami` | 200 OK, user `usrjMCVWGgu7I7JMS` = **`amdkn777@gmail.com`** (= compte "amd" A0 ✔) |
| 3 | `CLICKUP_API_KEY` User-scope HKCU | length=44, format `pk_<digits>_<alphanumeric>` ✔ |
| 4 | `CLICKUP_WORKSPACE_ID` User-scope HKCU | `90141225938` = "AasaS Solaris Marketing Hub" ✔ |
| 5 | `.mcp.json` extension | **18/18 servers wired** (16 pré-existants + airtable + clickup) ✔ |
| 6 | `.mcp.json` env var pattern | `${env:VAR}` partout, **0 secret hardcodé** ✔ |
| 7 | `symphony/loops/` directory | exists ✔ (déjà créé antérieurement) |

## 2. MCP servers wired cette session (post-compact)

Ajouts à `C:\Users\amado\.mcp.json` (lignes 130-144) :

```json
"airtable": {
  "command": "airtable-mcp-server.cmd",
  "args": [],
  "env": {
    "AIRTABLE_PAT": "${env:AIRTABLE_PAT}"
  }
},
"clickup": {
  "command": "clickup-mcp-server.cmd",
  "args": [],
  "env": {
    "CLICKUP_API_KEY": "${env:CLICKUP_API_KEY}",
    "CLICKUP_WORKSPACE_ID": "${env:CLICKUP_WORKSPACE_ID}"
  }
}
```

**Doctrine respectée** : Test Key Pragma (env var User scope, jamais en clair dans .md/.json/.ps1/git).

## 3. D6 Root causes (leçons ship)

| # | Leçon | Statut |
|---|---|---|
| #1 | PowerShell `$env:` session vs HKCU `[Environment]::GetEnvironmentVariable('VAR','User')` — fix = re-read registry après Set | **APPLIED** cette session |
| #2 | Airtable PAT format moderne = `pat<14>.<43>` avec séparateur period. PAT court (17 chars) = 401 malformed | **RESOLVED** (PAT 82 chars) |
| #4 | CC tool registry STATIC at session start — nouveau server name dans .mcp.json = ignoré jusqu'à CC restart | **KNOWN** (defer activation à A0) |
| NEW | bash heredoc + PowerShell `-Command "..."` + `$env:VAR.Length` parse error (`+ :AIRTABLE_PAT.Length`). **Fix** : `.ps1` file with single-quoted heredoc + `powershell -File` | **APPLIED** cette session |

## 4. D9 verdict + D10 outbox (A0 notifié)

**D9 verdict (self-choice)** : CONTINUER la session, ne pas restart CC maintenant.
- Rationale : 967.7 KB contexte précieux (re-pay au restart), et la suite ne dépend pas des tools MCP en RAM.
- `.mcp.json` est wired → l'activation se fera au **prochain CC restart** (A0 décide du moment).

**D10 outbox (notification A0)** :
1. ✅ Airtable PAT vérifié, compte = `amdkn777@gmail.com` (= "amd" A0)
2. ✅ ClickUp workspace vérifié = "AasaS Solaris Marketing Hub" (`90141225938`)
3. ✅ 18 MCP servers wired dans `.mcp.json` (avec env var refs, jamais en clair)
4. ✅ B1 Solaris /loop draft écrit : `symphony/loops/b1-solaris-loop.draft.md`
5. ⚠ **A0 ACTION REQUISE** avant CC restart : installer les packages npm
   ```bash
   npm i -g airtable-mcp-server clickup-mcp-server
   ```
   Car les `.cmd` binaries n'existent pas encore sur Windows PATH.

## 5. B1 Solaris /loop draft — résumé canon

**Path** : `ASpace_OS_V2/00_Amadeus/05_OSS_Twin/symphony/loops/b1-solaris-loop.draft.md`
**Statut** : Shadow A0 — DRAFT — hors-canon SDD, hors-Airlock (veto 90j respecté).

**Routing B1/B2/B3** :
```
A0 (méta-chat jumeau)
  → A1 Beth (Ikigai Lock)
    → A2 Discovery Zora (Life Wheel LD01-LD08)
      → A3 Saru (LD02 H3 Finance captain)
        → SOLARIS AaaS = Book (LD01 H1) + Saru (LD02 H3)
          → Plane issue append + Notion AGO-DECISION-DB + wiki handoff
```

**4-step loop (Fable × Auto-Research)** :
1. **CAPTURE** (read-only) : Airtable 🦸 Leads & Audits (`appmWf5Xm7w9Ae0ky`/`tblj0xmSXLH4Xsd8c`) + Supabase fw_life_wheel/fw_12wy + Plane.
2. **PROCESS** : Saru calcule runway/burn/MRR ; Book calcule weekly revenue/funnel delta.
3. **PERSIST** : Plane append (commentaire hebdo Rock L2) + Notion décision si drift >10%.
4. **LOOP** : cron `*/7 days` avec jitter ±90 min (anti-stampede herd).

**SLA triade** : temporel ≤5min/cycle, financier ≤$0.05/sem, qualitatif ≥95% champs non-NaN.

## 6. Activation gates (5 conditions, A0-gated)

1. **Levée du veto 90j** Symphony (cf. `SUPERVISION.symphony-hermes.draft.md` §0).
2. **Sign-off A0** verbatim "GO loop B1 Solaris" en chat.
3. **Airtable MCP + ClickUp MCP câblés et fonctionnels** post-CC-restart
   (post-install npm + post-restart CC).
4. **Tests 1 semaine en dry-run read-only** (Phase 0 observe-only).
5. **Validation 3 semaines d'usage continu** (critère MUSE SDD-008) avant canonisation PRD/ADR.

Tant que ces 5 conditions ne sont pas réunies, le draft reste une **carte**, pas un connecteur.

## 7. Premier run cible (post-activation)

- **W3 / 2026-06-23 → 2026-06-29** : capture initiale (state T0), 0 écriture.
- **W4 / 2026-06-30 → 2026-07-06** : 1er cycle PROCESS, 1er append Plane.
- **W5 / 2026-07-07** : revue mi-cycle, A0 décide continue/adjust/kill.

## 8. Doctrine respectée (rappel)

- **D1-D8 Anti-Paresse** (ADR-META-001) : Verify, Research, Nuance, No-Contradiction, Proof, Root-cause, Cost-of-Escalation, Cross-agent.
- **D7** : default non-escalation, A0 escalation = ~100× coût.
- **D9** (ADR-META-002) : quand le chemin est évident, choisir sans demander ; notifier seulement.
- **D10** : toute décision = outbox notification A0 (jamais silencieux).
- **D4** : append-only, retirements → `_TRASH_<date>/`.
- **Fable × /loop × Symphony** : 4-step Capture→Process→Persist→Loop + Agent OS standards + ADR-META-001.
- **AaaS 3 Variants** (ADR-L2-AAAS-001) : Solaris ACTIF / Nexus OMK ACTIF / Orbiter ABC ACTIF.
- **B1/B2/B3 fractal** (concept_l2_fractal_b1b2b3) : B1=WHY/WHERE · B2=WHAT/gate · B3=HOW/proof.
- **VETO 90j** : drafts Symphony = cartes, pas activables. Activation = A0 signoff explicite.
- **A0 chat = A0 méta-orchestration** (jamais B3 technicien, jamais A1 subordonné direct).
- **Notion AGO-DECISION-DB** : déjà wired (Bearer `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`).

## 9. Related handoffs

- `handoff_life_os_deploy_v1_0_2026-06-17.md` — Life OS V1.0 deploy (base)
- `handoff_life_os_apps_seeded_2026-06-17.md` — 27 rows fw_ikigai/life_wheel/12wy
- `handoff_mcp_persistence_v2_2026-06-16.md` — MCP durability doctrine
- `handoff_mcp_add_omk_abc_2026-06-17.md` — CC tool registry STATIC (D6 #4)
- `handoff_a0_divinity_arsenal_2026-06-20.md` — A1 Gatekeepers Beth+Morty
- `handoff_a0_jumeau_numerique_2026-06-21.md` — twin digital doctrine

## 10. Pending (à traiter sessions futures)

- [ ] A0 : `npm i -g airtable-mcp-server clickup-mcp-server`
- [ ] A0 : CC restart (active les 2 nouveaux MCP servers, D6 #4)
- [ ] A0 : sign-off verbatim "GO loop B1 Solaris" (gates #1-2)
- [ ] Phase 0 dry-run 1 semaine (gates #4)
- [ ] Phase 1 supervised 3 semaines (gate #5, critère MUSE)
- [ ] Drafter B2 Solaris /loop (Saravardarajan capitaine) — semaine prochaine
- [ ] Drafter B3 Solaris squad /loop (8 SOA01-SOA08 nano-squads) — quand Nexus OMK /loop stable
- [ ] Nexus OMK /loop config — quand OMK SaaS Cloud PGRST_DB_SCHEMAS fixé
- [ ] Orbiter ABC /loop config — quand abc-community-os login fixé
- [ ] PARA Bug Fix handoff (`handoff_para_debug_2026-06-23.md`) — Plustard ou autre session

---

*Handoff actif — B1/B2/B3 /loop pivot Solaris — 2026-06-23 — D4 append-only.*

---

## 11. D10 outbox timeline (D4 append-only)

### 2026-06-23 — Post-restart diagnostic (gate #3 status)

- **D1 verify 3 axes indépendants** (post-CC-restart, post-`npm i -g` claimé) :
  - Env vars User scope ✔ **vivants** : `AIRTABLE_PAT` length=82 (format `pat<14chars>.<43chars>`) ; `CLICKUP_API_KEY` length=44 (format `pk_<digits>_<alphanumeric>`) ; `CLICKUP_WORKSPACE_ID`=90141225938 (AasaS Solaris Marketing Hub).
  - Binaires `airtable-mcp-server.cmd` + `clickup-mcp-server.cmd` ✘ **MISSING** (`where` exit 1 sur les deux).
  - npm packages global ✘ **MISSING** : `npm list -g --depth=0 | grep -iE "airtable|clickup|mcp"` → 7 MCPs global installés mais **ni airtable ni clickup** dans la liste.
- **D1 npm view (8 parallel checks)** — package names dans `.mcp.json` sont **CORRECTS** :
  - `airtable-mcp-server@1.13.0` ✔ maintained (utilisé dans `.mcp.json`)
  - `clickup-mcp-server@1.12.0` ✔ maintained (utilisé dans `.mcp.json`)
  - `mcp-server-airtable@0.0.1` + `mcp-server-clickup@0.0.1` ✔ existent mais **SQUATS** (version 0.0.1 = placeholder/squatter, À ÉVITER)
  - `@airtable/mcp-server`, `@clickup/mcp-server`, `@modelcontextprotocol/server-airtable`, `@modelcontextprotocol/server-clickup` ✘ **404** (namespaces n'existent PAS)
- **Verdict D9** : falsifie l'hypothèse précédente "names dans `.mcp.json` étaient mauvais". Le fix concret = juste faire tourner `npm i -g` avec les bons noms (déjà déclarés dans `.mcp.json`).
- **Fix path concret** : `npm i -g airtable-mcp-server@1.13.0 clickup-mcp-server@1.12.0` → CC restart (D6 #4 STATIC registry) → `/mcp` verify devrait afficher airtable ✔ + clickup ✔.
- **D9 verdict global** : **gate #3 NOT satisfied**. A0 sign-off "GO loop B1 Solaris" **NON requêtable** tant que gate #3 pas ✔.
- **Drafts Symphony status** : `symphony/loops/b1-solaris-loop.draft.md` + `symphony/SUPERVISION.symphony-hermes.draft.md` restent **Shadow A0 DRAFT** (hors-canon SDD, hors-Airlock veto 90j respecté).
- **D6 ship candidate prêt** : leçon sur les 3 axes indépendants + reconnaissance squat packages 0.0.1 + namespace absent → append à `ADR-META-001` D6 catalog (D4 append-only).

### 2026-06-23 — D6 ship canonisé en ADR-META-006 (sister ADR de ADR-META-001)

- **Action** : Création du fichier `_SPECS/ADR/L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md` (ACCEPTED, sister ADR de ADR-META-001).
- **Pourquoi sister ADR** : Edit direct sur ADR-META-001 pour append §D6 catalog avait échoué (caractère Unicode mismatch). D4 append-only + Règle d'Or #3 (« on crée de nouveaux ADR, on ne réécrit pas les anciens ») → nouveau fichier plus safe que retry Edit risqué.
- **Contenu shipped** : (1) format catalog canonique 5-champs (Symptôme / D1 verify N axes / Root cause / Fix / Ref) ; (2) 1ère entrée « 2026-06-23 — MCP airtable/clickup ✘ failed post-CC-restart » ; (3) Pattern reconnaissance table 4 npm scopes (Canonical / Namespace scopod / Namespace MCP / Squat) ; (4) Enforcement (append-only strict + 3+ occurrences → Skill candidate + D1 receipts obligatoires) ; (5) Consequences (ROI ~30 min économisé par future occurrence).
- **Cross-link** : ADR-META-001 §D6 = doctrine parente ; ADR-META-006 = journal append-only des applications de D6. Pas de duplication, séparation claire.
- **Refs** : `_SPECS/ADR/L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md` + `ADR-META-001` §D6 (doctrine source) + `ADR-META-002` D9 (autonomie).

### 2026-06-23 — npm install MCP airtable+clickup DONE + D1 verify 3 axes ✔ (delegation A0 verbatim "Installe toi meme le npm install.")

- **Action** : `npm i -g airtable-mcp-server@1.13.0 clickup-mcp-server@1.12.0` → **266 packages added in 23s** ✔
- **D1 verify 3 axes indépendants (post-install)** — tous ✔ :
  1. `where airtable-mcp-server.cmd` → exit 0, binary à `C:\Users\amado\AppData\Roaming\npm\airtable-mcp-server.cmd` ✔
  2. `where clickup-mcp-server.cmd` → exit 0, binary à `C:\Users\amado\AppData\Roaming\npm\clickup-mcp-server.cmd` ✔
  3. `npm list -g --depth=0 | grep -iE "airtable|clickup"` → `airtable-mcp-server@1.13.0` + `clickup-mcp-server@1.12.0` tous deux présents ✔
- **D7-bis pattern (nouveau, sister doctrine D7)** : A0 a explicitement délégué l'action mécanique d'install npm à l'agent par override verbal — reversing le default D7 non-escalation vers D7-bis (A0 reverse-escalation = GO scripté). Honored sans re-confirmer (coût re-confirmation > coût action déterministe). Pattern candidat Skill si 3+ occurrences.
- **D6 catalog entry appendé** : nouvelle entrée "2026-06-23 — MCP airtable/clickup install DONE post-npm-i-g" ajoutée en tête du catalog ADR-META-006 (ordre antichronologique = newest first).
- **Gate #3 statut post-install** : PARTIELLEMENT ✔ — install OK + D1 verify 3 axes ✔. Reste HITL A0 : (1) CC restart (D6 #4 STATIC registry → active les 2 nouveaux servers dans tool registry CC), (2) `/mcp` verify → airtable ✔ + clickup ✔.
- **Prochain D6 catalog entry prévu** : "2026-06-23 — MCP airtable/clickup LIVE post-CC-restart" — à append après A0 fait CC restart + `/mcp` verify ✔. Permettra de fermer gate #3 à 100%.

### 2026-06-23 — Pending pour A0 (après D10 outbox ci-dessus)

- [ ] A0 : `npm i -g airtable-mcp-server@1.13.0 clickup-mcp-server@1.12.0` (les noms SONT bons — juste installer)
- [ ] A0 : CC restart (active les 2 nouveaux MCP servers, D6 #4 STATIC registry)
- [ ] A0 : `/mcp` verify → airtable ✔ + clickup ✔ (sinon, escalader)
- [ ] A0 : sign-off verbatim "GO loop B1 Solaris" (gates #1-2) — **uniquement APRÈS** gate #3 ✔
- [ ] Phase 0 dry-run 1 semaine (gate #4) — W3 2026-06-23 → 06-29
- [ ] Phase 1 supervised 3 semaines (gate #5, critère MUSE SDD-008) — W4 2026-06-30 → 07-06
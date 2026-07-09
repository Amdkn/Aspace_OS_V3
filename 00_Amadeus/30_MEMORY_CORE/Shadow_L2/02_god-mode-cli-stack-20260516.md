---
source: Claude Code Opus 4.7 (3-Turn Air Lock + Docs Dogmatique)
date: 2026-05-16
type: provider-configuration
domain: L0_Tech_OS / Shadow_Stack
tags: [#GodMode #CLI #PrintingPress #gws #vercel #supabase #DocsDogmatique #BypassPermissions]
status: phase-2-complete
related:
  - 30_MEMORY_CORE\Shadow_L2\01_mcp-shadow-l2-config-20260516.md (dormant fallback)
  - 30_MEMORY_CORE\Hermes Agent\README.md §1 (Doctrine Docs Dogmatique)
  - C:\Users\amado\.claude\settings.json (bypass wildcards)
---

# God Mode CLI Stack — 2026-05-16

## Intention A0

> "Je veux que tes MCP soit en God Mode et les Connecteurs serons mes Expérimentations manuels.
> Pour éviter les Doublons, faisons évoluer tes MCP en BypassPermission en des CLI comme
> https://developers.notion.com/cli/get-started/overview et on a Printing Press pour Créer des
> CLI de tous https://github.com/mvanhorn/cli-printing-press pour Airtable, ClickUp et les Autres"

## Doctrine établie

| Couche | Acteur | Rôle |
|---|---|---|
| **MCP UUID Claude Desktop** | A0 humain | Bac à sable manuel — expérimentation interactive, modales acceptables |
| **CLI invoqués via Bash** | Agents (Claude Code, Hermes, Codex) | Canal souverain agentique — bypass permissions, versionnable, auditable |
| **`.claude.json` mcpServers** | Fallback dormant | Sécurité si les CLIs cassent (Notion mcp-remote, etc.) |

**Règle de priorité** : `CLI officiel > Printing Press > MCP fallback`

## Tableau final des CLIs

| Service | CLI | Version | Path | Status |
|---|---|---|---|---|
| **Vercel** | `vercel` | 54.1.0 | `%APPDATA%\npm\vercel.ps1` | ✅ Installé |
| **Google Workspace** (Gmail, Drive, Calendar, Sheets, Docs, Chat, Admin) | `gws` | 0.22.5 | `%APPDATA%\npm\gws.ps1` | ✅ Installé |
| **Supabase** | `supabase` | 2.98.2 | `%LOCALAPPDATA%\Programs\supabase\supabase.exe` | ✅ Installé |
| **Printing Press** | `printing-press` | 4.8.0 | `%LOCALAPPDATA%\Programs\printing-press\printing-press.exe` | ✅ Installé (binaire Windows AMD64) |
| **GitHub** | `gh` | 2.83.2 | (déjà présent) | ✅ Existant |
| **Context7** | `ctx7` | (déjà présent) | (déjà présent) | ✅ Existant |
| **Notion `ntn`** | — | — | Windows unsupported | ❌ Skippé → Phase 5 PP-gen |
| **Airtable** | `airtable-pp-cli` | TBD | TBD | 🟡 Phase 5 (Printing Press) |
| **ClickUp** | `clickup-pp-cli` | TBD | TBD | 🟡 Phase 5 (Printing Press) |
| **Apollo.io** | `apollo-pp-cli` | TBD | TBD | 🟡 Phase 5 (Printing Press) |
| **Hostinger** | `hostinger-pp-cli` | TBD | TBD | 🟡 Phase 5 (Printing Press) |
| **Notion** | `notion-pp-cli` | TBD | TBD | 🟡 Phase 5 (Printing Press, remplace `ntn`) |

## Décisions clés cette session

1. **Go abandonné** → Printing Press distribue un binaire Windows AMD64 sur GitHub Releases (52 MB). Plus besoin de compiler depuis source. Économie : ~30 min de download Go lent (45 KB/s observés).

2. **`ntn` Notion CLI skippé** → docs Notion confirment `"ntn does not currently support Windows"`. Décision : utiliser **Printing Press** pour générer `notion-pp-cli.exe` Windows-natif (Phase 5).

3. **Supabase via binaire direct GitHub Release** → scoop absent, choco demandait admin. Tarball `supabase_windows_amd64.tar.gz` extrait avec `tar --force-local` (fix bug Windows tar.exe interprétant `C:` comme host SSH).

4. **PowerShell scripts → .ps1 files puis invocation** → bash mange systématiquement `$variables` PowerShell même dans here-strings. Pattern résolu : Write fichier .ps1 → `powershell -ExecutionPolicy Bypass -File`.

5. **OAuth différé Phase 3** → A0 fera `vercel login`, `supabase login`, `gws auth login` en interactif quand prêt. Les CLIs n'ont pas besoin d'auth pour vérifier `--version`.

## Phase 6 — Bypass permissions ajoutés

`C:\Users\amado\.claude\settings.json` → `permissions.allow` enrichi :

```json
"Bash(vercel:*)",
"Bash(supabase:*)",
"Bash(gws:*)",
"Bash(printing-press:*)",
"Bash(ntn:*)",
"Bash(ctx7:*)",
"Bash(gh:*)",
"Bash(*-pp-cli:*)",
"Bash(*-pp-mcp:*)"
```

⚠️ Note : `defaultMode: bypassPermissions` déjà actif globalement → ces wildcards sont **audit trail explicite** plus que nécessité fonctionnelle.

## Printing Press — comprendre l'outil

### Commandes principales

| Commande | Usage |
|---|---|
| `printing-press catalog list` | Voir les 22 APIs embedded (stripe, twilio, github, sentry…) |
| `printing-press generate --spec <url\|file>` | **Autonomous** — génère depuis OpenAPI |
| `printing-press generate --docs <docs-url>` | **Autonomous** — scrape docs site et infère spec |
| `printing-press print <api-name>` | Pipeline guidée via `/ce:work` Claude Code skill (5 phases) |
| `printing-press browser-sniff` | Reverse-engineering via HAR file |
| `printing-press bundle` | Package `.mcpb` MCP server |

### Catalog embedded (déjà 22)

`ai/elevenlabs`, `auth/stytch`, `cloud/digitalocean,google-cloud-run`, `developer-tools/github,launchdarkly,postman-explore`, `example/petstore`, `marketing/producthunt`, `monitoring/sentry`, `other/kayak`, `payments/mercury,plaid,stripe`, `project-management/asana`, `sales-and-crm/hubspot,pipedrive`, `social-and-messaging/discord,front,telegram,twilio`, `travel/google-flights`.

**Aucun de nos 5 targets dans le catalog** → besoin URLs externes.

### URLs candidate Phase 5

| Service | Spec / Docs candidate |
|---|---|
| Notion | https://developers.notion.com/reference/intro (docs scrape) |
| Airtable | https://airtable.com/developers/web/api/introduction (docs scrape) |
| ClickUp | https://developer.clickup.com/openapi (spec direct, à vérifier) |
| Apollo.io | https://docs.apollo.io/reference (docs scrape) |
| Hostinger | https://developers.hostinger.com (docs scrape) |

## Phase 5 — plan d'engagement futur

```bash
# Format générique
printing-press generate --docs <URL> --name <api> --output ~/printing-press/library/<api>
# Output : ~/printing-press/library/<api>/<api>-pp-cli + <api>-pp-mcp
```

**Risques connus** :
- Génération peut prendre 5-10 min/CLI selon taille docs
- `--polish` flag requires `claude` ou `codex` CLI → quality bonus mais optionnel
- Si docs scrape échoue → fallback `browser-sniff` avec HAR file
- Tokens API requis seulement à l'exécution finale (pas à la génération)

## CRITICAL — Secret exposé dans settings.json

Vu à `claudeCode.environmentVariables` → `ANTHROPIC_API_KEY: sk-cp-jtAuuNz...` (MiniMax token).
**Doit être rotated** et déplacé en variable d'environnement Windows User scope, pas en clair dans settings.json. Action L0/Rick.

## Sources vérifiées (Docs Dogmatique)

- Notion CLI: https://developers.notion.com/cli/get-started/overview (Windows unsupported confirmé)
- Printing Press: https://github.com/mvanhorn/cli-printing-press (v4.8.0 du 2026-05-16)
- Google Workspace CLI: https://github.com/googleworkspace/cli (v0.22.5, "Not officially supported")
- Vercel CLI: npm registry direct
- Supabase CLI: GitHub releases v2.98.2

## Next steps (handoff)

1. **A0 OAuth interactif** : `vercel login`, `supabase login`, `gws auth login` (~5 min total)
2. **Phase 5 batch** : générer les 5 CLIs Printing Press (~50 min séquentiel)
3. **ADR formel** : `_SPECS\ADR\ADR-MCP-001_god-mode-cli-stack.md` formalisant la trinité MCP/CLI/Fallback
4. **Secret rotation** : déplacer `ANTHROPIC_API_KEY` settings.json → User env var

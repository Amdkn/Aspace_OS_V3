---
source: A0 + Claude Code session
date: 2026-05-20
type: concept
domain: L0 / Auth / NotebookLM / Claude Code / MiniMax
tags: [#NotebookLM, #Auth, #Playwright, #ChromeAppBoundEncryption, #ClaudeCode, #MiniMax, #MCP, #L0Tools]
status: DRAFT_ACTIVE
---

# NotebookLM Auth Pour Claude Code on MiniMax — Le Vrai Bloqueur

## Executive Summary

A0 a galéré toute la journée (2026-05-19→20) sur l'auth NotebookLM MCP pour Claude Code CLI on MiniMax. Le problème **n'est PAS** l'auth en soi. C'est la combinaison de :

1. **NotebookLM n'a pas d'API officielle** → le package `notebooklm-py` utilise des appels RPC internes Google authentifiés par cookies browser.
2. **Headless detection Google** → quand `notebooklm login` ouvre un Chromium Playwright headless, Google laisse passer le login mais invalide la session côté serveur dans les minutes/heures qui suivent.
3. **Chrome App-Bound encryption (Chrome ≥127)** → impossible d'extraire les cookies depuis Chrome avec des libs pure-Python (`browser_cookie3` ne supporte pas v20). Seul `rookiepy` le supporte, mais nécessite Rust toolchain pour builder sur Python 3.13/3.14 Windows.
4. **`notebooklm doctor` ment** → renvoie "✓ authenticated, 43 cookies" alors que `notebooklm list` redirige vers `accounts.google.com/v3/signin`. Doctor check les cookies LOCAUX, pas la session côté Google.

## Diagnostic Signal (le piège)

```
$ notebooklm doctor
Auth ✓ pass  authenticated (SID cookie present, 43 cookies)

$ notebooklm list
Error: Authentication expired or invalid.
Redirected to: https://accounts.google.com/v3/signin/...
Run 'notebooklm login' to re-authenticate.
```

Si tu vois ce pattern → ce n'est PAS un problème de cookies expirés. C'est Google qui rejette la session côté serveur pour cause de headless browser détecté.

## Stack Final A'Space

| Composant | Path / Valeur | Statut |
|---|---|---|
| Python runtime | `C:\Python314\python.exe` | 3.14 (bs4 OK) |
| Fallback runtime | Python 3.13 (WindowsApps) | dispo |
| Package `notebooklm-py` | `0.4.1` user install | OK |
| CLI binary | `C:\Users\amado\AppData\Roaming\Python\Python314\Scripts\notebooklm.exe` | présent |
| MCP binary | `notebooklm-mcp.exe` (même dossier) | présent |
| Storage state | `C:\Users\amado\.notebooklm\profiles\default\storage_state.json` | géré par CLI |
| Browser profile persistant | `C:\Users\amado\.notebooklm\profiles\default\browser_profile\` | géré par CLI |

## Doctrine "Real Browser Login"

**Toujours forcer un browser système réel** lors du login, pas Chromium Playwright :

```powershell
notebooklm login --fresh --browser msedge
```

- `--fresh` = clean le browser profile caché, force un login from scratch (utile pour switch account ou après invalidation Google)
- `--browser msedge` = utilise le vrai Edge système (User Agent + binary path = browser légitime aux yeux de Google) plutôt que Chromium Playwright

Si `msedge` indisponible : `--browser chromium` reste possible mais accepte qu'il faille re-login plus souvent.

## Scripts A'Space (Trust Zone)

| Script | Rôle |
|---|---|
| `~/.claude/bin/notebooklm-relogin.ps1` | Backup storage_state → `login --fresh --browser msedge` → vérifie `notebooklm list` → diagnose si toujours bloqué |
| `~/.claude/bin/notebooklm-mcp-wire.ps1` | Vérifie auth, backup `.claude.json`, ajoute idempotent `mcpServers.notebooklm` → vérifie config |
| `~/.claude/bin/notebooklm-import-chrome-cookies.py` | (fallback) Importe cookies Chrome via `browser_cookie3`. **Cassé sur Chrome App-Bound v20** — gardé pour info. |

## MCP Wiring Pattern (validé)

Dans `~/.claude.json` :

```jsonc
{
  "mcpServers": {
    "notebooklm": {
      "type": "stdio",
      "command": "C:\\Users\\amado\\AppData\\Roaming\\Python\\Python314\\Scripts\\notebooklm-mcp.exe",
      "args": [],
      "env": {
        "NOTEBOOKLM_PROFILE": "default"
      }
    }
  }
}
```

**Notes critiques** :
- Path absolu obligatoire (pas dans PATH global)
- `NOTEBOOKLM_PROFILE` permet plusieurs profils Google si besoin
- Aucune env var de secret/token (la session est dans le `storage_state.json` filesystem)
- **Claude Code doit être redémarré** pour relire `mcpServers`

## Anti-Patterns Vécus

1. ❌ **Faire confiance à `notebooklm doctor`** comme signal d'auth complète. Toujours valider avec `notebooklm list`.
2. ❌ **Login en Chromium Playwright headless** pour usage long terme. Google invalide la session en quelques heures.
3. ❌ **Pip install `notebooklm-py[cookies]`** sur Python 3.14 → fail wheel build `rookiepy`.
4. ❌ **`browser_cookie3` sur Chrome ≥127** → bug `'Chrome' object has no attribute 'tmp_cookie_file'` à cause d'App-Bound encryption v20.
5. ❌ **Boucler sur `notebooklm login` sans `--fresh`** → réutilise le profile caché potentiellement corrompu.
6. ❌ **Hardcoder le path Python user-site** ailleurs que dans les scripts dédiés (pas de path Python dans `_SPECS/` ou Canon).

## Cycle de Reauth (quand ça pète)

Google peut invalider la session sans préavis (sécurité, device change, 2FA refresh). Cycle attendu :

1. `notebooklm list` retourne signin redirect
2. Run `~/.claude/bin/notebooklm-relogin.ps1`
3. Login msedge visible, 2FA
4. `notebooklm list` valide
5. Redémarrer Claude Code (le MCP server lit storage_state au startup)

Pas besoin de re-câbler le MCP — la config `.claude.json` reste valide tant que les paths ne changent pas.

## Cross-Layer Doctrine

Cet apprentissage appartient à **L0 Tools** (couche tooling/infra), pas à L1 ou L2. Le mesh Shadow_L1/L2 *consomme* NotebookLM via MCP, mais l'auth est un service L0 partagé par toutes les capsules CLI.

Si Codex CLI ou Gemini CLI doivent eux aussi appeler NotebookLM, ils consommeront le MÊME `storage_state.json` (un seul login pour tout le mesh agentique).

## Inbounds

- `~/.claude/bin/notebooklm-relogin.ps1`
- `~/.claude/bin/notebooklm-mcp-wire.ps1`
- `~/.claude/skills/notebooklm/SKILL.md`
- `concept_god_mode_cli_stack.md`
- `concept_shadow_l1_l2_heartbeat_symphony.md` (L2 utilise NotebookLM pour research mission cards)

## Cross-refs externes (lus 2026-05-20)

- notebooklm-py 0.4.1 CLI help output (snapshot in session log)
- Chrome App-Bound encryption v20 announcement (Chrome 127, 2024-07)
- Playwright bot detection by Google sign-in pages (Google security policy)

---

## Addendum 2026-05-20 — Bridge Pattern (handoff Antigravity → Claude Code finalisé)

Le doc ci-dessus décrivait `notebooklm-relogin.ps1` + `notebooklm-mcp-wire.ps1`
comme solution. **Ils sont DEPRECATED**. Découverte tardive : Google n'invalide
pas la session "à cause du headless detection". Le vrai bloqueur est
**DBSC (Device Bound Session Credentials)** qui exige que les RPC `list`,
`get_notebook`, `chat`, etc. proviennent d'un binaire browser réel — les
cookies seuls ne suffisent JAMAIS, même valides + frais.

### Le verdict technique

| Layer | Cookies seuls suffisent ? |
|---|---|
| `AuthTokens.from_storage()` (init auth + CSRF token) | ✅ OUI |
| `notebooklm doctor` (local cookie validity) | ✅ OUI |
| `notebooklm list` / `nlm_*` MCP tools (server RPC) | ❌ NON (DBSC) |

### La solution validée : Bridge Playwright (Antigravity 2026-05-20)

Antigravity a livré le skill **`notebooklm-bridge`** dans `~/.agent/skills/`
qui contourne DBSC en :

1. Lançant Playwright `chromium.launch_persistent_context(browser_profile)` headless
2. Naviguant vers `https://notebooklm.google.com/` (page complète, DBSC validé naturellement)
3. Lisant le DOM (project-grid, links) pour extraire la liste des notebooks
4. (Extensible) Injectant `await page.evaluate(fetch(RPC_URL))` pour appels RPC arbitraires

Le `browser_profile/` persistant (`C:\Users\amado\.notebooklm\profiles\default\browser_profile`)
contient un vrai état Chromium reconnu par Google, donc DBSC accepte.

### Handoff Claude Code CLI (finalisé 2026-05-20 par Claude Code)

- Junction `~/.claude/skills/notebooklm-bridge` → `~/.agent/skills/notebooklm-bridge`
  → Claude Code découvre le skill automatiquement
- SKILL.md enrichi avec triggers FR/EN + commandes Bash explicites
- SKILL.md legacy `~/.claude/skills/notebooklm/` marqué DEPRECATED + redirect
- **PAS de câblage `notebooklm-mcp.exe` dans `.claude.json`** (il ne marcherait
  pas, et le ferait avec l'apparence de réussite — pire qu'une absence)

### Commandes finales validées

```bash
# Liste les notebooks (DBSC OK)
C:/Python314/python.exe \
  C:/Users/amado/.agent/skills/notebooklm-bridge/notebooklm_rpc.py list

# Re-login Playwright visible (si cookies expirent dans ~14j)
C:/Python314/python.exe \
  C:/Users/amado/.agent/skills/notebooklm-bridge/notebooklm_rpc.py login

# Screenshot debug
C:/Python314/python.exe \
  C:/Users/amado/.agent/skills/notebooklm-bridge/notebooklm_rpc.py screenshot \
  C:/Users/amado/Downloads/nlm.png
```

### Re-auth alternative (Cookie-Editor)

Si Playwright `login` ne marche pas (Google bloque même le visible) :

1. Chrome standard ouvert sur https://notebooklm.google.com, A0 loggé
2. Extension Cookie-Editor → export JSON cookies `.google.com` + `notebooklm.google.com`
3. Claude Code overwrite `~/.notebooklm/profiles/default/storage_state.json`
   + env var `NOTEBOOKLM_AUTH_JSON` (User scope) + `~/AppData/Local/agy/notebooklm_auth.json`
4. Re-test bridge `list`

Ce process a été validé par Antigravity le 2026-05-20 (cf. wiki log §1410-1419).

### Tracking — MCP wrapper futur

Le bridge expose 3 commandes (`list`/`login`/`screenshot`). Il manque
`ask`/`generate`/`add_source`. Le pattern propre est un **MCP server Python
qui wrappe `notebooklm_rpc.py call <RPC_METHOD> <PARAMS>`** et expose des
tools typés (`nlm_ask`, `nlm_generate_audio`, etc.). Proposé dans
`skills_queue.md` 2026-05-20 sous le nom `notebooklm-mcp-bridge`.

### Anti-patterns supplémentaires (ajout)

7. ❌ **Câbler `notebooklm-mcp.exe` officiel dans `.claude.json`** alors
   qu'on sait qu'il ne traverse pas DBSC — donne l'illusion de fonctionnement.
8. ❌ **Tenter `notebooklm login --browser msedge`** comme fix universel —
   ça déplace le problème (msedge passe parfois quelques heures, puis
   re-invalidation DBSC). Le bridge avec browser_profile persistant est
   la seule voie durable.

---
type: Playbook
title: NotebookLM Bridge — contourner DBSC par Chromium persistant
description: Solution validée Antigravity 2026-05-20 pour utiliser NotebookLM depuis Claude Code malgré DBSC (Device Bound Session Credentials). Playwright `chromium.launch_persistent_context` sur storage_state persistant + lecture DOM (project-grid). Le `notebooklm-mcp.exe` officiel ne marche JAMAIS, même cookies frais.
tags: [notebooklm, dbsc, playwright, bridge, google, mcp-blocked, cookie-extraction, work-around]
generated: { by: minimax-m3, at: 2026-08-17T21:21:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T21:21:00Z }
sources:
  - id: concept-notebooklm-auth
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/concepts/concept_notebooklm_auth_2026.md"
    title: "NotebookLM Auth Pour Claude Code on MiniMax — Le Vrai Bloqueur"
    last_modified: 2026-05-20
okf_version: "0.2"
---

# NotebookLM Bridge — contourner DBSC par Chromium persistant

> Le doc `concept_notebooklm_auth_2026.md` décrivait initialement `notebooklm-relogin.ps1` +
> `notebooklm-mcp-wire.ps1` comme solution. **DEPRECATED.** Le vrai bloqueur est
> **DBSC (Device Bound Session Credentials)** qui exige que les RPC `list`, `get_notebook`,
> `chat` etc. proviennent d'un binaire browser réel — **les cookies seuls ne suffisent JAMAIS**,
> même valides et frais.

## 1. Verdict technique (D1)

| Layer | Cookies seuls suffisent ? |
|---|---|
| `AuthTokens.from_storage()` (init auth + CSRF) | ✅ OUI |
| `notebooklm doctor` (validité locale) | ✅ OUI |
| `notebooklm list` / RPC `nlm_*` | ❌ NON (**DBSC**) |

## 2. La solution validée : Bridge Playwright persistant

Antigravity a livré le skill **`notebooklm-bridge`** dans `~/.agent/skills/`
qui contourne DBSC en :

1. Lancant Playwright `chromium.launch_persistent_context(browser_profile)` headless
2. Navigant vers `https://notebooklm.google.com/` (page complète, **DBSC validé naturellement**)
3. Lisant le DOM (`project-grid`, `links`) pour extraire la liste des notebooks
4. (Extensible) Injectant `await page.evaluate(fetch(RPC_URL))` pour appels RPC arbitraires

Le `browser_profile/` persistant
(`C:\Users\amado\.notebooklm\profiles\default\browser_profile`) contient un vrai état
Chromium reconnu par Google, donc DBSC accepte.

## 3. Handoff Claude Code (finalisé 2026-05-20)

- Junction `~/.claude/skills/notebooklm-bridge` → `~/.agent/skills/notebooklm-bridge`
- SKILL.md enrichi avec triggers FR/EN + commandes Bash explicites
- SKILL.md legacy `~/.claude/skills/notebooklm/` marqué DEPRECATED + redirect
- **PAS de câblage `notebooklm-mcp.exe` dans `.claude.json`** — il ne marche pas, et
  le ferait avec l'apparence de réussite (**pire qu'une absence**).

## 4. Commandes finales validées

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

## 5. Re-auth alternative (Cookie-Editor fallback)

Si Playwright `login` ne marche pas (Google bloque même le visible) :

1. Chrome standard ouvert sur `https://notebooklm.google.com`, A0 loggé
2. Extension Cookie-Editor → export JSON cookies `.google.com` + `notebooklm.google.com`
3. Claude Code overwrite `~/.notebooklm/profiles/default/storage_state.json`
   + env var `NOTEBOOKLM_AUTH_JSON` (User scope)
   + `~/AppData/Local/agy/notebooklm_auth.json`
4. Re-test bridge `list`

Ce process a été validé par Antigravity le 2026-05-20 (cf. wiki log §1410-1419).

## 6. Cycle de reauth (quand ça pète)

Google peut invalider la session sans préavis (sécurité, device change, 2FA refresh).
Cycle attendu :

1. `notebooklm list` retourne signin redirect
2. Lancer le script de bridge `login`
3. Login msedge visible, 2FA
4. `notebooklm list` valide
5. Redémarrer Claude Code (le bridge lit `storage_state` au startup)

Pas besoin de re-câbler — la config reste valide tant que les paths ne changent pas.

## 7. Anti-patterns (le plus souvent vu)

| Anti-pattern | Pourquoi c'est faux |
|---|---|
| Faire confiance à `notebooklm doctor` | Vérifie les cookies LOCAUX ; pas la session serveur Google |
| Login en Chromium Playwright headless | Google invalide en quelques heures (DBSC) |
| `pip install notebooklm-py[cookies]` sur Py 3.14 | Fail wheel build `rookiepy` |
| `browser_cookie3` sur Chrome ≥127 | Bug App-Bound encryption v20 |
| Boucler `notebooklm login` sans `--fresh` | Réutilise profile caché potentiellement corrompu |
| Hardcoder path Python user-site | Path réservé aux scripts dédiés |
| **Câbler `notebooklm-mcp.exe` officiel** | Donne l'illusion de fonctionner, mais ne traverse pas DBSC |

## 8. Tracking — MCP wrapper futur

Le bridge expose 3 commandes (`list`/`login`/`screenshot`). Manquent `ask`/`generate`/`add_source`.
Pattern propre = **MCP server Python qui wrappe `notebooklm_rpc.py call <RPC_METHOD> <PARAMS>`**
et expose des tools typés (`nlm_ask`, `nlm_generate_audio`).
Proposé dans `skills_queue.md` 2026-05-20 sous le nom `notebooklm-mcp-bridge`.

## Liens entrants

- `playwright-cli-vs-mcp.md` (à venir) — le bridge repose sur Playwright persistant
- `compounding-knowledge-wiki.md` — NotebookLM sert la mémoire (audio digests + contexte)
- `shadow-l1-l2-homologie.md` — L2 utilise NotebookLM pour les research mission cards

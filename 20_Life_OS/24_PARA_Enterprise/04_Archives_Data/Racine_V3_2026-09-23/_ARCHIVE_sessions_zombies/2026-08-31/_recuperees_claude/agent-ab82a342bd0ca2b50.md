---
session: agent-ab82a342bd0ca2b50
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\7cdef055-2fb3-43d6-854b-762a8ff6f8b2\subagents\agent-ab82a342bd0ca2b50.jsonl
debut: 2026-07-10T15:50:39.452Z
fin: 2026-07-10T15:56:05.317Z
messages_utilisateur: 1
reponses_assistant: 1
titre: "Mission : Installer et configurer le plugin `watch` du marketplace `bradautomates/claude-video` pour Claude Co…"
---

## >>> UTILISATEUR #1

Mission : Installer et configurer le plugin `watch` du marketplace `bradautomates/claude-video` pour Claude Code.

D1 verify-before-assert : NE POSTULE RIEN sur ce plugin. Vérifie D2 research-first ce qu'il fait avant d'installer.

Étapes :
1. **D2 research** : WebSearch ou WebFetch pour confirmer ce qu'est `bradautomates/claude-video` (GitHub repo). Note le nombre d'étoiles, dernière mise à jour, ce que fait le plugin `watch`. URL probable : https://github.com/bradautomates/claude-video
2. **Vérifier l'outil CLI** : `claude --help` pour confirmer que la CLI supporte les sous-commandes `plugin`. Si oui, lister : `claude plugin --help`
3. **Install marketplace** : `claude plugin marketplace add bradautomates/claude-video`
4. **Vérifier** : `claude plugin marketplace list` doit montrer le nouveau marketplace
5. **Install plugin** : `claude plugin install watch@claude-video`
6. **Vérifier** : `claude plugin list` doit montrer `watch@claude-video` actif
7. **Test smoke** : si le plugin expose une commande `/watch` ou similaire, teste-la brièvement (`/watch --help` ou équivalent) pour confirmer qu'elle est bien enregistrée.

Rapport final concis (max 15 lignes) :
- URL GitHub + statut repo
- D1 receipts : commandes exécutées + outputs (succès/erreurs verbatim)
- Le plugin `watch` fait quoi en 1 phrase
- Statut final : ✓ installé ou ✗ bloqué (+ raison)

D7 anti-escalation : si une étape échoue, ne ré-essaye pas 3 fois — rapporte avec l'erreur verbatim et stop. Pas d'escalade A0 sauf si vraiment bloqué.

Pas de long rapport. Pas de théorie. Faits + outputs.

### assistant

## Rapport final

**Repo GitHub :** `https://github.com/bradautomates/claude-video` — Claude Code plugin MIT, 7.1k stars, dernière release v0.2.0 du 2026-07-01.

**D1 receipts (commands verbatim) :**

| # | Commande | Output |
|---|---|---|
| 1 | `claude --help` | montre `plugin\|plugins Manage Claude Code plugins` |
| 2 | `claude plugin marketplace add bradautomates/claude-video` | `✔ Successfully added marketplace: claude-video (declared in user settings)` (clone SSH OK) |
| 3 | `claude plugin marketplace list` | 3 marketplaces listés : `claude-plugins-official`, `claude-code-warp`, **`claude-video`** |
| 4 | `claude plugin install watch@claude-video` | `✔ Successfully installed plugin: watch@claude-video (scope: user)` |
| 5 | `claude plugin list` | `watch@claude-video  Version: 0.2.0  Scope: user  Status: ✔ enabled` |
| 6 | `claude plugin details watch@claude-video` | 1 skill (`watch`), 1 hook SessionStart, 0 agents/MCP/LSP, **+220 tok always-on / +5.4k tok on-invoke** |
| 7 | Smoke test : `setup.py --check` | exit 4 — `missing binaries: yt-dlp; no Whisper API key`. Plugin détecté et scripts accessibles. **Comportement attendu** d'une fresh install. |

**Fonction du plugin (1 phrase) :** `/watch <url-or-path> [question]` télécharge une vidéo via yt-dlp, extrait des frames JPEG via ffmpeg (scene-aware, cap 100 par défaut), pull une transcription (captions natives → fallback Whisper API), puis injecte frames + transcript dans la conversation pour répondre grounded.

**Statut final : ✓ Installé** — `watch@claude-video` v0.2.0 actif en scope user. Pour usage réel, il faudra un run interactif de `setup.py` qui pose 2 questions (Whisper key Groq ou OpenAI, et `WATCH_DETAIL` = transcript/efficient/balanced/token-burner) et écrit `SETUP_COMPLETE=true` dans `~/.config/watch/.env`. Le `head -100` initial a échoué (commande absente du Git Bash Windows) — contourné en supprimant le pipe, et `cmd.exe`/`powershell.exe` directs introuvables depuis le sandbox → invocation directe via le chemin absolu `C:\Users\amado\AppData\Roaming\npm\claude.cmd`.

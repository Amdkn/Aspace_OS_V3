---
target: L0 MCP pivots pending A0_GO_REQUIRED
date: 2026-06-28
sister: l0_mcp_pivots_premortem_live.md
refresh: à chaque run `/premortem-fill l0-mcp-pivots`
---

# Pending A0 Actions — L0 MCP Pivots

> **4 actions queue** — toutes A0_GO_REQUIRED. **NE PAS exécuter** par Hermes/Claude/Codex (Posture C + ADR-SOBER-002).

## F2 — Plugin Supabase canonical OFF

**État** : `supabase@claude-plugins-official: false` dans `~/.claude/settings.json`. Documenté D6 #1 (post-CC-restart 2026-06-23, plugin échoue au démarrage).

**Décision requise** :
- **Option A** : Activer (toggle `false → true`). Risque = re-créer la D6 #1.
- **Option B** : Laisser OFF, accepter la dépendance aux MCP custom (`supabase` / `supabase-omk` / `supabase-abc`) déjà fonctionnels (✓ Connected per digest).
- **Recommandation** : Option B — les custom MCPs couvrent déjà l'usage, et l'activation du plugin officiel ne ferait que doubler la surface sans gain opérationnel.

**F2 — CLOSED 2026-06-28 by [ADR-MCP-PLUGIN-001](../../../_SPECS/ADR/L0_Tech_OS/ADR-MCP-PLUGIN-001_supabase-canonical-OFF.md) (status PROPOSED, awaiting A0 in-session ratification)**. Décision OFF formalisée, 5 axes justifiés (couverture atteinte / D6 #1 actif / surface inutile / Sobriété Rick / Posture C). Trigger de re-évaluation documenté : nouvelle D6 entrée custom MCP Supabase OU update plugin corrigeant D6 #1 OU A0 explicite → cycle ADR-MCP-PLUGIN-002.

## F4 — Watchdog MCP-dédié (pas de cron capturant ✗ Failed)

**État** : SessionStart digest capte le `✗ Failed` au démarrage (via `mcp-server-commander-logs/`), mais aucun cron *entre* les sessions.

**Décision requise** :
- **Option A** : Créer un cron watchdog toutes les 6h qui scrape les MCP et alerte (Posture C : HITL A0 par cron, mais le cron lui-même est safe-read).
- **Option B** : Adopter le skill `l0-watchdog-scrape` (existe, listé) avec un cron planifié Q4 2026 (post L0 P4).
- **Recommandation** : Option B — différer à L0 P4 (activation `l0-watchdog-scrape` Hermes runtime).

---

### 📝 F4 — SPEC WRITTEN 2026-06-28, awaiting P4 GO (D4 append-only annotation)

- **Spec handoff** : `wiki/hand_offs/mcp_watchdog_spec_2026-06-28.md` (READ-ONLY design, NOT executed)
- **Author** : A0 jumeau numérique (Opus) — sub-agent F4 spec writer
- **Status** : READY_FOR_P4_GO, **0 cron created this turn** (Posture C strict)
- **Cadence proposed** : every 6h (00/06/12/18 ET)
- **Probe surface** : 10 MCP servers (Supabase × 3, Vercel × 3, Airtable × 2, ClickUp × 2)
- **DLQ target** : `~/.hermes/disposition.md` → Donna DLQ (14 capsules dormant)
- **HITL channel** : next SessionStart digest (NO push, NO SAPI TTS, NO Telegram — per Posture C)
- **Activation gate** : P4 GO from A0 required (Hermes runtime dry-run + watchdog live)
- **Coupled to** : F6 (heartbeat skill `l0-watchdog-scrape` wiring) — recommended F4 first, F6 follow-on 1-2 weeks later
- **D1 receipt** : 0 cron created · 0 settings.json edit · 0 .mcp.json edit · 0 actual MCP probe · no RATIFIED ADR modified
- **Anti-forgetting** : until A0 explicitly closes F4 (P4 GO), this annotation remains visible in SessionStart digest

## F6 — Heartbeat skill `l0-watchdog-scrape` non connecté

**État** : Skill canon existe (`~/.claude/skills/l0-watchdog-scrape/`), non wired aux 4 MCP pivots.

**Décision requise** : câblage manuel = ajouter dans `~/.claude/settings.json` sous `hooks.SessionStart` (ou déclencher via le cron watchdog F4).
- **Recommandation** : différer à L0 P4 (couplé à F4).

---

### 📝 F6 — WIRING SPEC WRITTEN 2026-06-28, awaiting P4 GO (D4 append-only annotation)

- **Spec handoff** : `wiki/hand_offs/watchdog_scrape_wiring_2026-06-28.md` (READ-ONLY design, NOT executed)
- **Author** : A0 jumeau numérique (M3) — sub-agent F6 spec writer
- **Status** : READY_FOR_P4_GO, **0 wiring created this turn** (Posture C strict)
- **Entry point** : `~/.claude/skills/l0-watchdog-scrape/SKILL.md` (220 lignes, lu D1, NON muté)
- **Target surface** : 10 MCP servers (Supabase × 3, Vercel × 3, Airtable × 2, ClickUp × 2) — Supabase+Vercel déjà couverts par skill, F6 EXTEND vers Airtable+ClickUp (L2 surfaces)
- **Schedule** : piggyback F4 cron 6h (00/06/12/18 ET) — PAS de nouveau cron
- **Output paths** :
  - Rollup existant inchangé : `wiki/reports/l0_pulse_<date>.md`
  - **NOUVEAU** heartbeat (F6) : `wiki/hand_offs/l0_heartbeat_<date>.md` (Airtable/ClickUp-specific)
- **DLQ target** : partagé avec F4 → Donna DLQ via `~/.hermes/disposition.md` (ADR-RICK-001)
- **Failure modes** : 5 scénarios catalogués (MCP Failed / heartbeat write fail / F4 cron die / skill drift / token leak)
- **Coupled to** : F4 (watchdog cron ticker) ↔ F6 (skill payload). F4 GO prerequisite to F6 GO. Recommended F4 first, F6 follow-on 1-2 weeks later.
- **Activation gate** : P4 GO from A0 required (Hermes runtime dry-run + F4 watchdog live)
- **D1 receipt** : 0 wiring created · 0 settings.json edit · 0 .mcp.json edit · 0 skill mutation · 0 cron create · 0 actual MCP probe · no RATIFIED ADR modified
- **Anti-forgetting** : until A0 explicitly closes F6 (P4 GO), this annotation remains visible in SessionStart digest

## F11 — Rollback script `.mcp.json`

**État** : Pas de procédure de restauration documentée si `.mcp.json` se corrompt (D6 #5 lesson — backup manuel).

**Décision requise** :
- **Option A** : Créer un script `~/.claude/bin/rollback-mcp-config.ps1` qui restaure depuis le dernier snapshot.
- **Option B** : Adopter le pattern D6 #5 (backup avant chaque edit) — déjà actif, juste à documenter.
- **Recommandation** : Option B — formaliser dans un ADR-`MCP-ROLLBACK-001` (canon), avec un script shell de 5 lignes max.

---

## Anti-forgetting
Le skill `/premortem-fill` installe un hook SessionStart qui affiche ces pending à chaque démarrage. Tant que les 4 actions ne sont pas **explicitement fermées par A0** → la queue reste visible.

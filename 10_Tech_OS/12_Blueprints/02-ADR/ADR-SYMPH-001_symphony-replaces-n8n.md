# ADR-SYMPH-001 — Symphony Bus Remplace N8N (L0 Orchestration)

**Date :** 2026-05-26
**Auteur :** A0 Amadeus + A2 Claude Code
**Statut :** RATIFIÉ
**Type :** Architecture Decision Record (Tech OS / L0)
**Portée :** Tout flux de coordination inter-agents, sync inter-tools, automatisation Back Office
**Ancré sur :** SDD-001 (Anti-Panic) · SDD-002 (Karpathy Pattern) · `Shadow_L0/SPEC.md` (Symphony-compliant déjà déclaré)
**Source matière :** Conversations Gemini 2026-05 + intention A0 (2026-05-26)

---

## Contexte

Le canon Shadow_L0 (SPEC.md, point #4) déclare déjà : *"Be Symphony-compliant — leverage the 2026 doctrine of ephemeral tick sessions + multi-turn continuation + workspace persistence"*. Cette doctrine n'a jamais été ratifiée comme ADR explicite, ce qui crée 3 problèmes :

1. **N8N reste référencé** comme bus dans la documentation legacy (Takeout Gemini 2026-05:211880-211903 — "Webhook N8N détecte le changement…"). Sans ADR, il n'y a pas d'autorité pour le déclarer obsolète.
2. **ADR-NOTION-001** vient de référencer Symphony comme bus de sync sans qu'il existe un ADR-SYMPH.
3. Les futurs agents (Claude Code, Codex, Gemini, Antigravity, Claude Desktop) ne savent pas **quelle interface Symphony respecter** quand ils émettent ou consomment un événement.

Cet ADR ratifie ce que SPEC.md préfigure et ferme la boucle.

## Décision

### D1 — Symphony est le seul bus d'orchestration L0 autorisé

**N8N est marqué LEGACY** au 2026-05-26. Aucun nouveau workflow N8N ne sera créé. Les workflows N8N existants (le cas échéant) sont archivés dans `PARA\04_Archives_Data\Legacy_N8N_Workflows_2026-05-26\` lors du prochain ménage.

Substituts par classe d'usage :

| Cas d'usage N8N (legacy) | Substitut Symphony |
|--------------------------|---------------------|
| Webhook → action | Tick handler dans `agents/<X>/skills/<event>.ps1` |
| Cron scheduling | Windows Task Scheduler → `heartbeat-tick.ps1 <agent>` |
| Sync Notion → Supabase | Skill dédié sur Doctor 11 (Interface) consommant Notion MCP + Supabase MCP |
| Sync Airtable → ClickUp | Skill dédié sur Doctor 12 (Forge) |
| LLM call dans pipeline | Direct via Claude/Gemini/Codex CLI ephemeral session |

### D2 — Symphony = pattern, pas runtime

Symphony est un **style architectural** (extrait de [OpenAI Symphony SPEC](https://github.com/openai/symphony/blob/main/SPEC.md)), pas un service à installer. Il définit :

- **Ephemeral tick sessions** — chaque tick = 1 process node/python/ps1 qui naît, exécute, meurt
- **Multi-turn continuation** — l'état persiste dans des fichiers (LLM_Wiki, `memory/`, `pulse.log`), jamais en mémoire
- **Workspace persistence** — chaque agent capsule a son répertoire `Shadow_L0/agents/<X>/` immuable entre ticks
- **No daemon** — Task Scheduler fait office d'orchestrateur central

### D3 — Tick cycle canonique (rappel SPEC.md §4)

```
WAKE → PROBE → DECIDE → EXECUTE → OBSERVE → LEARN → SIGNAL → SLEEP
```

Tout agent participant à Symphony doit implémenter ces 8 phases dans son `heartbeat-tick.ps1` ou équivalent. ADR-HEART-002 précise les modes d'instrumentation anti-panique.

### D4 — Interface de message inter-agent

Tout message entre agents passe par le filesystem :

```
agents/<sender>/memory/outbox/<timestamp>_<topic>.json
                                    │
                                    └─→ déplacé en
agents/<receiver>/memory/inbox/<timestamp>_<topic>.json
                                    │
                                    └─→ après traitement
agents/<receiver>/memory/inbox/.done/<timestamp>_<topic>.json
```

Format JSON minimal :
```json
{
  "from": "Claude_Code_CLI",
  "to": "Codex_CLI",
  "topic": "vps-provision-nexus",
  "intent": "execute_sop",
  "sop_id": "SOP-L2-IT-001",
  "context_pack_url": "https://notion.so/...",
  "deadline_iso": "2026-05-26T18:00:00Z",
  "trust_required": "requires_signoff"
}
```

Pas de WebSocket, pas de gRPC, pas de Redis. **Files only**.

### D5 — Quota & fallback chain (rappel CLAUDE.md)

| Doctor | 1st choice | 2nd fallback | 3rd last resort |
|--------|------------|--------------|-----------------|
| 13th (Machine/L0) | Codex CLI | Gemini CLI | Claude Code |
| 12th (Forge/L2) | Gemini CLI | Claude Code | Codex CLI |
| 11th (Produit/L1) | Claude Code | Gemini CLI | Codex CLI |

Symphony **détecte les rate-limits** via le code de retour CLI et bascule automatiquement vers le fallback. C'est dans cette détection que vivent OpenClaw/Paperclip optionnels (cf. ADR-HEART-002).

### D6 — Variantes harness (préfiguré pour ADR-SYMPH-002)

Les harnesses participants Symphony (réels ou cibles) :

- `Codex_CLI` (existant) — 13th Doctor préféré L0
- `Gemini_CLI` (existant) — 12th Doctor préféré L2
- `Claude_Code_CLI` (existant — MiniMax) — 11th Doctor préféré L1
- `Antigravity_CLI` (cible) — variant IDE Google
- `Claude_Desktop_App` (cible) — variant Anthropic Opus/Sonnet natif
- `Codex_Desktop` (cible) — variant OpenAI Codex desktop

ADR-SYMPH-002 détaille les capabilities, restrictions, scope par variant.

## Conséquences

### Positives
- N8N n'a plus à être réinstallé/débuggé. Une dette technique disparaît.
- ADR-NOTION-001 a maintenant son bus officiel — pas de référence flottante.
- Aucun runtime ajouté (Symphony = files + Task Scheduler). Coût opérationnel zéro.
- Les agents Codex/Gemini/Claude Code partagent le même protocole d'échange (inbox/outbox JSON).

### Négatives
- Pas d'UI graphique de workflow (N8N en proposait une). Anti-pattern : si ça frustre, on **dessine** les flows en Mermaid dans LLM_Wiki, pas dans une UI runtime.
- Latence de tick > latence webhook N8N (~secondes vs ms). Inacceptable pour flows temps-réel client → ces flows passent directement par Supabase Edge Functions, pas par Symphony.

### Risques tracés
- Risque de prolifération de skills mal indexés. **Antidote** : Graham (mémoire B3) maintient `agents/<X>/skills/INDEX.md` à jour à chaque LEARN phase.
- Risque de désync timestamps Windows ↔ Linux (si capsule remote). **Antidote** : tous les timestamps en UTC ISO-8601, jamais d'heure locale.

## Suivi

- **ADR-SYMPH-002** — matrice variants harness (CC MiniMax / Antigravity / Codex / Claude Desktop)
- **ADR-HEART-002** — heartbeat amélioré anti-panique avec OpenClaw/Paperclip gated
- **Archive N8N** — au prochain ménage, créer `PARA\04_Archives_Data\Legacy_N8N_Workflows_<date>\` et y déplacer toute config `.n8n` résiduelle si existante

## Références

- `Shadow_L0/SPEC.md` (Symphony-compliant déjà déclaré)
- `Shadow_L0/HEARTBEAT_PROTOCOL.md`
- `.claude/bin/heartbeat-tick.ps1` (implémentation existante)
- OpenAI Symphony SPEC : https://github.com/openai/symphony/blob/main/SPEC.md
- SDD-001 § Anti-Panic (anchor doctrinal)
- ADR-NOTION-001 (premier consommateur du bus)

# ADR-HEART-002 — Heartbeat Anti-Panique + Réintroduction Conditionnelle OpenClaw / Paperclip

**Date :** 2026-05-26
**Auteur :** A0 Amadeus + A2 Claude Code
**Statut :** RATIFIÉ
**Type :** Architecture Decision Record (Tech OS / L0)
**Portée :** Instrumentation tick cycle pour empêcher les 8 paniques de SDD-001
**Ancré sur :** SDD-001 §1.2 (taxonomie 4+4 paniques) · SDD-001 §2.1 (3 axiomes antifragiles) · ADR-SYMPH-001 · `Shadow_L0/HEARTBEAT_PROTOCOL.md`
**Amende :** `Shadow_L0/SPEC.md` §1 point 1 — le **bannissement total** d'OpenClaw/Paperclip est levé sous conditions strictes définies ici

---

## Contexte

Trois pressions convergent :

1. **SDD-001** (fondateur) liste 8 types de paniques (4 Framework + 4 Kernel) qui ont causé l'effondrement Hermes en avril 2026. Le tick cycle actuel ne couvre que partiellement la détection.
2. **A0 a explicitement demandé** (2026-05-26) un *"meilleur Heartbeat quitte à introduire OpenClaw ou Paperclip dans leurs meilleures configurations autonomes et capables sans Panique Agentique"*.
3. **`Shadow_L0/SPEC.md` interdit** actuellement OpenClaw/Paperclip ("no OpenClaw gateway, no Paperclip Node process"). Tension à résoudre.

Cet ADR amende SPEC.md sur ce point précis : **réintroduction conditionnelle**, gated par anti-panique vérifié.

## Décision

### D1 — Instrumentation des 8 phases tick contre les 8 paniques

Le tick cycle `WAKE → PROBE → DECIDE → EXECUTE → OBSERVE → LEARN → SIGNAL → SLEEP` reçoit une matrice de gardes anti-panique :

| Phase | Panique adressée | Garde insérée |
|-------|------------------|---------------|
| WAKE | TYPE 1 (Approval Freeze) | Read `Context.md` + check `pending_approvals.json` — si > 1h → escalation A0 immediate |
| PROBE | TYPE K4 (Dead Kernel) | Ping `LLM_Wiki/wiki/log.md` mtime — si > 24h sans append → flag dead |
| PROBE | TYPE K3 (Secret Leak 401) | Probe MCP critique (Notion, Supabase) — si 401 → marquer token expired, NE PAS LOG le secret |
| DECIDE | TYPE 2 (Budget Hard-Stop) | Verify AGENTS.md présent dans capsule — sinon refuse mission, log et escalate |
| DECIDE | TYPE 3 (DM Pairing Block) | Vérifier que les DM channels (si OpenClaw activé) ont un timeout < 30s |
| EXECUTE | TYPE K1 (Filesystem Blindness) | Tous les writes passent par helper `Write-AndVerify` qui Read-After-Write |
| EXECUTE | TYPE K2 (Hallucination Succès) | Aucun EXIT 0 accepté sans block Read-After-Write confirmant le contenu |
| OBSERVE | TYPE 4 (WebSocket Timeout) | Si la mission utilise WS (rare), timeout 60s + fallback file-based |
| LEARN | (toutes) | Append au `WIKI.md` capsule. Pattern × 3 → propose Skill Hermes Nous |
| SIGNAL | TYPE K4 (Dead Kernel) | Heartbeat ping vers `pulse.log` parent — si absent 2 ticks → Watchdog réanime |
| SLEEP | (toutes) | Nettoyage `outbox/.done/` > 7j |

Implémentation : extension de `heartbeat-tick.ps1` avec un module `AntiPanicGuards.psm1` colocalisé.

### D2 — Read-After-Write (RAW) systémique (rappel Axiome 1 SDD-001)

Toute écriture critique (config, ADR, SOP, token) passe par :

```powershell
function Write-AndVerify {
  param([string]$Path, [string]$Content, [int]$RetryMax = 3)
  for ($i = 0; $i -lt $RetryMax; $i++) {
    Set-Content -Path $Path -Value $Content -Encoding UTF8 -Force
    Start-Sleep -Milliseconds 100
    $readback = Get-Content -Path $Path -Raw -ErrorAction Stop
    if ($readback -eq $Content) { return $true }
  }
  throw "RAW failed after $RetryMax attempts: $Path"
}
```

Les writes non-critiques (logs, telemetry) peuvent skip RAW pour performance. **Toute SOP doit utiliser RAW**.

### D3 — Réintroduction conditionnelle OpenClaw

`Shadow_L0/SPEC.md` interdit actuellement OpenClaw. Cet ADR amende : **OpenClaw devient autorisé** si et seulement si :

| Condition | Vérification |
|-----------|--------------|
| C1 — DM Pairing désactivé OU timeout strict | `openclaw.config.json` contient `dmPolicy: "off"` OU `dmPolicy: "pairing", dmTimeoutMs: 30000` |
| C2 — Health endpoint exposé | `GET http://localhost:<port>/health` répond 200 en < 1s |
| C3 — Donna DLQ configurée | OpenClaw émet erreurs vers `Shadow_L0/donna_dlq/` (file-based, pas WS) |
| C4 — Heartbeat ping outbound | OpenClaw écrit `pulse.log` toutes les 60s |

Si **une seule** condition échoue, OpenClaw est désactivé automatiquement par Watchdog (Yaz). Capsule dédiée : `Shadow_L0/agents/OpenClaw_Gateway/` (à créer si activé).

### D4 — Réintroduction conditionnelle Paperclip

Idem pour Paperclip :

| Condition | Vérification |
|-----------|--------------|
| P1 — AGENTS.md présent | `Test-Path` sur `<capsule>/AGENTS.md` |
| P2 — Budget hard-stop configuré | `paperclip.config.json` contient `budget.maxTokensPerMission: 100000` (ou valeur A0) |
| P3 — Mémoire procédurale active | Pattern × 3 détecté par Graham → Skill auto-encodé |
| P4 — Donna DLQ outbound | Failures Paperclip écrivent vers `Shadow_L0/donna_dlq/` |

Si P1 fail → Type 2 panique imminent → **arrêt Paperclip immédiat**. Capsule dédiée : `Shadow_L0/agents/Paperclip_Budget/`.

### D5 — Modes d'opération

3 modes pour le mesh Shadow_L0 :

| Mode | OpenClaw | Paperclip | Cas d'usage |
|------|----------|-----------|-------------|
| **Lean** (défaut actuel) | OFF | OFF | Setup minimal Symphony — 3 capsules CLI suffisent |
| **Bridged** | ON (avec C1-C4) | OFF | Besoin DM pairing pour Telegram/external bots, sans budget management agressif |
| **Full** | ON (C1-C4) | ON (P1-P4) | Production scale-up — budget par mission, DM pairing, monitoring complet |

A0 choisit le mode via `Shadow_L0/MODE.txt` (1 ligne : `lean` | `bridged` | `full`). Watchdog lit ce fichier à chaque tick et active/désactive les capsules en conséquence.

**Recommandation initiale** : rester en `lean` jusqu'à ce que les 3 ADRs SYMPH/HEART soient ratifiés ET que Phase 1 Notion Solaris soit verrouillée. Pas avant.

### D6 — Donna DLQ refondue (file-based, pas WS)

L'effondrement Hermes a montré que Donna DLQ basée sur WebSocket est fragile (Type 4 panique). Nouvelle implémentation :

```
Shadow_L0/donna_dlq/
├── pending/      ← Erreurs reçues, en attente de traitement
│   └── <iso-timestamp>_<source>_<error-code>.json
├── retried/      ← Tentatives de re-execution
└── failed/       ← Echec définitif → escalation A0
```

Format JSON erreur :
```json
{
  "from": "OpenClaw",
  "timestamp": "2026-05-26T15:30:00Z",
  "error_code": "DM_TIMEOUT",
  "context": "DM pairing > 30s",
  "retry_count": 0,
  "max_retries": 3,
  "escalation": "A0_inbox"
}
```

Yaz (Watchdog A3) sweep `donna_dlq/pending/` toutes les 5 min, applique retry policy, déplace vers `retried/` ou `failed/`.

### D7 — Watchdog Yaz : sweep toutes les 5min

`heartbeat-tick.ps1 -Agent Yaz_Watchdog -Tempo 5m_always` est ajouté à Windows Task Scheduler. Yaz vérifie :

1. Tous les ticks attendus depuis 15 min ont bien tourné (lecture `pulse.log` par capsule)
2. `donna_dlq/pending/` est sweepé
3. Conditions C1-C4 / P1-P4 si modes Bridged/Full
4. `LLM_Wiki/wiki/log.md` a été touché en < 1h (sinon flag Kernel Dead)

Sortie Yaz : `Shadow_L0/watchdog.log` (append-only).

## Conséquences

### Positives
- 8 paniques SDD-001 cartographiées 1:1 avec gardes tick — antifragilité réelle, pas slogan
- OpenClaw/Paperclip réintroduisables sans risque de regression Hermes — chaque réintroduction est **gated**
- Mode `lean` reste le défaut, escalade progressive (lean → bridged → full) sans rupture
- Donna DLQ file-based = pas de single-point-of-failure WS

### Négatives
- Complexité instrumentation tick augmente (8 phases × matrice de gardes). Code review obligatoire avant déploiement `AntiPanicGuards.psm1`.
- Si A0 oublie de mettre à jour `Shadow_L0/MODE.txt`, Watchdog peut désactiver des capsules silencieusement. **Antidote** : Watchdog log explicite + notif A0 inbox quand bascule.

### Risques tracés
- **Pattern × 3 → Skill auto-encodé** (Axiome 3) peut générer du bruit si Graham détecte de faux patterns. **Antidote** : skill auto-encodé en `Status: Draft`, A0 valide manuellement pour passer `Active`.
- **OpenClaw/Paperclip evolutions upstream** peuvent casser les conditions C1-C4/P1-P4. À revoir au prochain bump version OpenClaw ou Paperclip.

## Plan d'implémentation

### Phase 0 — Maintenant (lean mode confirmation)
- [x] Cet ADR ratifié
- [ ] Créer `Shadow_L0/MODE.txt` avec `lean`
- [ ] Vérifier que `heartbeat-tick.ps1` actuel respecte les phases — sinon flag pour patch

### Phase 1 — AntiPanicGuards.psm1 (~ 2h)
- [ ] Coder le module dans `.claude/bin/AntiPanicGuards.psm1`
- [ ] Tester sur capsule `Codex_CLI` en dry-run
- [ ] Intégrer dans `heartbeat-tick.ps1`

### Phase 2 — Donna DLQ refonte (~ 1h)
- [ ] Créer `Shadow_L0/donna_dlq/{pending,retried,failed}/`
- [ ] Documenter format JSON dans `Shadow_L0/DONNA_PROTOCOL.md`

### Phase 3 — Watchdog Yaz (~ 1h)
- [ ] Créer capsule `Shadow_L0/agents/Yaz_Watchdog/`
- [ ] Task Scheduler entry 5min always
- [ ] First tick = vérification baseline (créer un health snapshot)

### Phase 4 — Bridged/Full modes (différé)
À activer **uniquement** quand A0 a un besoin concret (DM pairing Telegram, budget par mission). Pas de pré-déploiement spéculatif.

## Références

- SDD-001 §1.2 (taxonomie paniques) et §2.1 (3 axiomes antifragiles)
- `Shadow_L0/HEARTBEAT_PROTOCOL.md` (canon tick cycle existant)
- `Shadow_L0/SPEC.md` §1 (interdiction OpenClaw/Paperclip — amendée par cet ADR)
- ADR-SYMPH-001 (bus doctrine)
- ADR-SYMPH-002 (variants harness)
- `.claude/bin/heartbeat-tick.ps1` (implémentation à étendre)

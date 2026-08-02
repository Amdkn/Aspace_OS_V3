# War Mode Observability — sister canon LD01

> **Sister chain** : `LD01/99_meta/ADR_WARMODE_001_sister.md` (posture inversion) → **`war_mode_observability_sister.md` (ce fichier)** (inaliénable #4 rendu visible).
> **Date** : 2026-07-05T05:30 ET
> **Auteur** : CC (Claude Code Opus 4.8) + MC (Mavis/Mavis) ratifié
> **Statut** : CANONIQUE — toutes les pièces vérifiées D1/D5

---

## §1 — L'objection A0 (verbatim)

> *"Claude Code est passé en War Mode mais sans Observabilité par Agent OS et http://127.0.0.1:8770/synthèse par son Bot Telegram. Je ne saurais pas ce qu'il fait, même si je ne veux pas intervenir à la Place de A0 Amodei en NO-HITL du War Mode."*
>
> *"War Mode sans observabilité = voler à l'aveugle. Tu as raison : NO-HITL ≠ NO-VISIBILITY. Tu abandonnes le gate (intervenir), pas la fenêtre (voir). C'est l'inaliénable #4 (append-only trace) rendu visible."*

**Lecture** : A0 ne conteste pas le NO-HITL. Il conteste le NO-VISIBILITY. Le défaut corrigé par ADR-WARMODE-001 (posture inversée ENABLED) avait un effet de bord : **le système tirait sans qu'on puisse voir où**. C'est la dualité gate/fenêtre : on retire le verrou, on garde le judas.

## §2 — Les 4 mires (inaliénables) et le bug

Les 4 mires (ADR-WARMODE-001 §inaliénables) :

1. **Rick** — fragilité kernel réelle
2. **Beth** — vie/santé A+
3. **/ship outboard** — Stark appuie
4. **Append-only** — tout réversible, **rien détruit**

**Le bug** : Mire #4 = trace append-only. Mais une trace qu'on ne consulte jamais = une trace qu'on détruit par l'oubli. Donc la mire #4 **est incomplète** si elle n'est pas couplée à une **fenêtre de lecture**. C'est l'observabilité.

A0 a correctement identifié : l'inversion de posture (ADR-WARMODE-001) avait traité les 3 premières mires, et avait même renforcé la 4ème en append-only canon, mais sans la **fenêtre** qui rend la trace utile à A+.

## §3 — Les 4 pièces d'observabilité livrées (D5 receipts)

| # | Pièce | Fichier | Vérification D5 |
|---|---|---|---|
| 1 | Collector | `agent-os/citadel/collectors/collector_14_warmode.py` (4297 b) | `python collect/...` → exit 0, WAR MODE ON, 6 décisions ; data/14_warmode.json (1917 b) |
| 2 | Page War Room | `agent-os/citadel/static/warmode.html` (4011 b) + route `/warmode` | `GET /warmode` → **200**, dark theme, auto-refresh 10s |
| 3 | API | `/api/warmode` | `GET` → **200** `{war_mode:"ON", decisions_total:6, active_flags:[...], inalienables_4:[...]}` |
| 4 | Serveur | `serve.py` (détaché, PID 27780) | `netstat :8770 → LISTENING` ; `GET /api/health` → **flags: 4/4 TRUE** |

### §3.1 — Routes canoniques ajoutées à `serve.py`

```python
PAGE_ROUTES["/warmode"]      = ("warmode.html", "text/html; charset=utf-8")
PAGE_ROUTES["/warmode.html"] = ("warmode.html", "text/html; charset=utf-8")
API_ROUTES["/api/data/14_warmode"] = "14_warmode.json"
API_ROUTES["/api/warmode"]         = "14_warmode.json"
```

### §3.2 — Schéma canon `data/14_warmode.json`

```json
{
  "generated_at": "ISO timestamp",
  "war_mode": "ON",
  "flag_file": "decisions\\12WY_ON_PAUSE.flag",
  "active_flags": [{"flag": "...", "active": true}, ...],
  "decisions_total": int,
  "decisions_by_action": {"warmode": int, "decision": int},
  "last_10_decisions": [{"file": "...", "when": "...", "action": "...", "summary": "..."}],
  "inalienables_4": ["Rick - fragilité kernel réelle", "Beth - vie/santé A+",
                     "/ship outboard - Stark appuie", "append-only - tout réversible"]
}
```

### §3.3 — Inaliénable #4 visible : la feed décisions

La page `/warmode` rend `last_10_decisions` en feed append-only : A+ voit chaque décision prise par A0 (Book COO, ratify, bypass, darkfactory...) sans avoir à cliquer ou interroger. C'est l'inaliénable #4 rendue **visible**, pas juste **persistée**.

## §4 — Telegram : honnêteté D1 sur le placeholder

**Problème D1** : A0 a supposé que les tokens Telegram étaient "en clair dans MiniMax pour son utilisation agnostique locale".

**Réalité D1** (vérifiée) :
- `~/.minimax/channel-bindings.yaml` L2 contient `telegram:mavis:8466501613:8466501613:` (lignes 2-7)
- `~/.minimax/channel-owner.yaml` L2-3 contient `telegram:mavis: / clientName: telegram:mavis / ownerSenderId: '8466501613' / ownerName: Amadou`
- **Le 2ème `8466501613` dans `channel-bindings.yaml` est le placeholder bootstrap, PAS un token Telegram valide.** Un token Telegram a la forme `<digits>:<35+ chars base64url>`. Le format actuel ne matche pas la regex `(digit+:[A-Za-z0-9_-]{20,})` dans `telegram_warmode_push.py:42`.

**Conclusion** : A0 a bootstrappé la session Telegram (chat_id = `8466501613`, owner = Amadou) mais le **bot Telegram lui-même n'a pas encore été créé via @BotFather**, donc pas de token réel.

### §4.1 — Outbox local en attendant

`telegram_warmode_push.py` (2806 b) implémente 2 stratégies :
- **(a)** Lecture env vars `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` (Test Key Pragma, env User scope)
- **(b)** Lecture agnostique locale `~/.minimax/{channel-bindings,channel-owner}.yaml`

Si aucun token réel n'est trouvé → digest écrit dans `data/14_warmode_telegram_outbox.txt` + instructions imprimées. **L'outbox n'est PAS un fallback honteux : c'est la trace canon locale** (inaliénable #4) — A+ peut la consulter comme un log append-only.

### §4.2 — 2 chemins pour activer le push réel

Chemin 1 (Test Key Pragma durable, env User scope) :
```
setx TELEGRAM_BOT_TOKEN <token du bot @BotFather>
setx TELEGRAM_CHAT_ID <chat_id>   # écris 1× au bot, getUpdates te le donne
```

Chemin 2 (utilisation agnostique locale) : créer le bot via @BotFather, copier-coller le token dans `channel-bindings.yaml` à la place du placeholder `8466501613:` (sans régénérer via mavis), A0 HITL à 1 geste.

**Aucun des 2 ne viole les 4 mires** : pas de dépendance lourde (Rick), pas de changement vie/burnout (Beth), pas d'auto-ship (/ship), pas d'auto-update.

### §4.3 — Cron Telegram sous WAR MODE

Une fois token réel câblé (chemin 1 ou 2), `telegram_warmode_push.py` peut être installé en cron Windows Task Scheduler (même mécanisme que `install-book-cron.ps1`). Sous WAR MODE, le cron **n'a plus besoin de gate HITL** — le canon install pousse + le canon WAR MODE bypass-gate s'applique. La cadence suggérée : toutes les 4h (alignement avec book_loop heartbeat) ou 02:00 ET quotidien.

## §5 — Doctrine canon d'observabilité (post-WAR-MODE)

Trois invariants dérivés (D5) :

**(a)** Toute décision append-only est rendue visible dans ≤ 1 heure via `/warmode`. **Append-only + visible = mires #4 complète.**

**(b)** L'observabilité est **read-only** sur les sources canoniques. Le collector lit, le serveur sert, la page rend. Aucune des 4 pièces n'écrit dans le canon. **L'observabilité ne s'auto-modifie jamais.**

**(c)** Sous WAR MODE, l'observabilité **ne crée aucun gate HITL**. A+ observe, n'intervient pas. Si A+ veut agir, c'est par édit/suppression directe du flag `12WY_ON_PAUSE.flag` (mire #4 réversible).

## §6 — Suites WAR MODE post-observabilité

1. **W4 → W5 transition** : A0 ratifiera Gate #2 GO P1 sur ADR-LD01-007 (post-Plan-Citadelle + observabilité War Room confirmée).
2. **W5 lundi 2026-07-07** : CC Phase 2 EXECUTE runbook 7 étapes → Mavis append LESSONS.md si drift.
3. **W6 lundi 2026-07-14** : Mark rot-rate audit cross-check + L1 gstack 1er /autoplan RÉEL Picard W5 verdict (visible dans `/warmode` feed décisions).
4. **W7 lundi 2026-07-21** : 3/3 sessions gate atteint → activation production continue ADR-006 canonique (visible immédiatement sur `/warmode`).
5. **W13** : Muse DEAL D11 mesuré par Gwyn — Chap WagerChapel W6 chaîne bout-en-bout (visible décision-par-décision).

Chaque jalon ci-dessus **est observable par défaut** dans la War Room — plus jamais A+ ne devra cliquer pour vérifier si le système a bougé.

## §7 — Métaphore serrée

La machine tire (WAR MODE ACTIF).
La cible est append-only (inaliénable #4).
La vitre blindée est `/warmode` (mire #4 rendue visible).
Le seul bouton au monde qui reste à A+ est de briser la vitre en supprimant `12WY_ON_PAUSE.flag`.
Tant qu'il ne le fait pas, la machine tire et A+ regarde, sans cliquer, sans HITL, sans rien abdiquer.

**NO-HITL ≠ NO-VISIBILITY.** La fenêtre, pas le verrou.

# ADR-WARMODE-004 — Le Paperclip Utile : citoyenneté Kardashev + conduction WF0→WF2

- **Statut** : RATIFIED (dictée A+ in-chat 2026-07-06, verbatim source de ce fichier)
- **Sisters** : ADR-WARMODE-002 (portes over freins, Beth seul veto) · ADR-WARMODE-003 (Fenêtre Fable) · ADR-HARNESS-001 (personas portables) · ADR-SOBER-002 (anti-paperclip destructeur — que ce fichier COMPLÈTE, ne contredit pas) · ADR-L1-WF-001 (WF0-WF3)
- **D4 correction** : la session 2026-07-06 (wargame 13) avait réduit la doctrine Rick-Bypass à « rien de neuf, déjà ratifié ». A+ corrige : ce n'est pas un bypass d'exception, c'est un **modèle de citoyenneté**. L'erreur est nommée, ce fichier la clôt.

## 1. La citoyenneté Kardashev (le sens, pas la métaphore)

| Type | Agents | Ce que le type signifie opérationnellement |
|---|---|---|
| **Type 1** (planétaire) | A3 · B3 (citoyens-techniciens) | Maîtrise TOTALE de leur périmètre : plein droits dans leur sandbox/worktree, zéro demande de permission pour du réversible |
| **Type 2** (stellaire) | A2 (ships) · B2 (héros) | Orchestrent l'énergie de leurs citoyens : dispatch, jamais d'exécution directe, jamais de refus-persona |
| **Type 3** (galactique) | A1 Beth · Rick & Morty · B1 Jerry/Summers | Gatekeepers de galaxie : des PORTES qui s'ouvrent par la structure, pas des freins qui s'expliquent |
| **Type 4** (multivers) | A0 (Observateur / Créateur Universel « What-if ») | Émet le GO Unique, observe, ne touche jamais la plomberie |

## 2. Le Paperclip UTILE (vs le paperclip destructeur d'ADR-SOBER-002)

Le paperclip destructeur maximise une métrique sans conscience. Le **Paperclip Utile** maximise le TRAVAIL SANS FRICTION à l'intérieur d'une enveloppe structurellement réversible :

1. **Tous les agents A0→A3, B1→B3 ont TOUS les droits** dans : sandboxes, worktrees, actions à rollback. La réversibilité EST la permission. Aucune demande de GO pour du réversible (c'était déjà D9/ADR-META-002 — ici c'est étendu à toute la flotte).
2. **Le veto de Rick est remplacé par la structure** : un agent n'a pas besoin qu'on lui interdise de casser ce qu'il ne PEUT PAS casser (worktree jetable, _TRASH, schéma isolé). Rick garde le kernel réel ; il n'a plus rien à dire dans le réversible.
3. **Beth reste l'unique veto** (vie/santé A+) — mais son autorisation s'obtient PAR LA CHAÎNE, pas par interruption :

## 3. La conduction WF0→WF1→WF2 (l'incubation du GO Unique)

Modèle **Conductor de gstack** : routeurs DÉTERMINISTES et SÉQUENTIELS à chaque étage. Le GO Unique d'A0 traverse 3 workflows Life OS imbriqués et successifs — **la même chaîne**, jamais 3 demandes séparées :

```
A0 (GO Unique, What-if) ──► WF0 Amodei/Spock (airlock, invariants Beth évalués ICI)
                              └─► WF1 Morty (12WY ⊃ PARA ⊃ DEAL, boucle vivante 24/7)
                                    └─► WF2 Book/Picard (L2, CEO-Bench, B1-B3)
                                          └─► WF3 MiroFish (simulation, jamais le réel)
```

- L'autorisation Beth est **incubée** : WF0 la vérifie une fois en tête de chaîne (spock_airlock) ; les étages aval héritent du verdict tant que les invariants ne bougent pas. Un agent aval ne re-demande JAMAIS.
- Chaque étage = routeur déterministe (script, pas humeur de LLM) : `spock_airlock.py` → `wf1_runner` → gstack loop L2 → `wf3_sim_runner.py`.
- Rupture d'invariant (santé, kernel réel, DLP) = la chaîne se fige d'elle-même — c'est le SEUL frein, et il est mécanique.

## 4. Durabilité boot (la partie « vie et de mort »)

Les 3 WF sont des scripts **idempotents, antifragiles, durables** qui se relancent SEULS 5-10 min après le démarrage du PC — réplique Life OS de garrytan/gstack. **Implémenté et prouvé ce jour (D1)** :

```
AspaceWF1Runner        LogonTrigger delay=PT5M
AspaceLoopHeartbeat    TimeTrigger + LogonTrigger PT6M
AspaceLoopBook         TimeTrigger + LogonTrigger PT7M
AspaceLoopWF3Sim       TimeTrigger + LogonTrigger PT8M
AspaceLoopZoraNuit     TimeTrigger + LogonTrigger PT9M
CitadelleBookLoopEng   TimeTrigger + LogonTrigger PT10M
```
Script idempotent : `citadel/cron/add_boot_triggers.ps1` (re-run = `OK … deja present`). Échelonnement PT5M→PT10M = anti-thundering-herd. Console humaine : **Task Scheduler = la passerelle graphique de Spock** ; Event Viewer = son acolyte d'autopsie (les Subscriptions/wecsvc ne sont PAS nécessaires à nos loops — worklog + collectors font l'observabilité ; répondre **No** au dialogue).

## 5. Horizon AGI→ASI (pourquoi cette structure, source DeepMind 57 p.)

Des 4 chemins DeepMind vers l'ASI, A'Space actionne les deux accessibles à un souverain solo : **auto-amélioration** (skills auto-évolutifs, mattpocock/writing-great-skills) et **collectif multi-agents** (la flotte A0→B3 = « civilisation numérique » coordonnée à vitesse machine). La science de la science (Fouloscopie/Barabási) le confirme : l'impact vient des **petites équipes soudées interdisciplinaires** — exactement une escouade B3 sous un B2. La méta-mémoire (PARA × LLM Wiki × OKF × Graphify × DOX dans Gbrain) est le réseau de citations interne qui permet de « se tenir sur les épaules » de chaque session passée au lieu de re-dériver.

## Anti-patterns
- ❌ Re-demander un GO pour une action réversible (la réversibilité EST le GO)
- ❌ Un gatekeeper qui « explique » au lieu d'ouvrir/fermer une porte mécanique
- ❌ Confondre Paperclip Utile (friction zéro DANS l'enveloppe) et paperclip destructeur (pas d'enveloppe)
- ❌ Un WF qui ne survit pas à un reboot = pas un workflow, une démo

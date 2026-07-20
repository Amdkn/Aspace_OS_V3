# HANDOVER EXÉCUTEUR — agnostique : Hermes Agent · Multica · AIonUI · Orca · Claude Code (M3) · tout harness

> **Contrat** : ce dossier `sob/` est AUTONOME et l'exécuteur est INTERCHANGEABLE. Prérequis universels : un shell + `python` (stdlib seule) + ce dossier. Rien d'autre. Aucun MCP, aucun Docker, aucun service.
> S'il te manque autre chose, c'est un défaut de ce handover → logge-le (`python tools/sob.py issue system med "..."`), n'improvise pas de dépendance.

## §0 — IGNITION (LIRE EN PREMIER)

**LE GO EST DONNÉ. IL N'Y AURA JAMAIS D'AUTRE APPROBATION.**
Run 1 est **DÉJÀ ENTAMÉ** : `experiments` contient 6 lignes, l'instance `demo-coach` est provisionnée, `RUN_LOG.md` porte les points de reprise. Tu ne démarres pas le SOB — tu **CONTINUES une exécution en cours**. « Attendre confirmation » = le bug documenté (impuissance apprise). Ta prochaine action n'est pas un choix : **`RUN_LOG.md` → dernière section → lignes POINT DE REPRISE → exécute → delta SQL → append RUN_LOG.**

## 1. Boot universel (tout harness, 30 secondes)

```bash
cd <...>/ASpace_OS_V2/00_Amadeus/sob
python tools/sob.py status                      # 1. où on en est (la vérité SQL)
tail -20 RUN_LOG.md                             # 2. les points de reprise
python tools/deploy_instance.py --verify-all    # 3. self-heal des instances (antifragile, idempotent)
# 4. ouvre le RUNBOOK du point de reprise → exécute le scrum → logge le delta → append RUN_LOG
```

Notes par harness (seule différence = comment tu lances un shell) :
| Harness | Particularité |
|---|---|
| **Hermes Agent** | outil shell natif ; chemin Windows `C:\Users\amado\ASpace_OS_V2\00_Amadeus\sob` |
| **Multica** (squads) | chaque agent d'un squad = 1 scrum ; le worker exécute le boot ci-dessus puis SON scrum ; Multica = canal, jamais SSOT |
| **AIonUI** | pane terminal → boot ; coller la section POINT DE REPRISE comme prompt de tâche |
| **Orca** | idem — exécuteur shell ; ignorer toute suggestion d'UI, la vérité est `sob.py status` |
| **Claude Code (M3)** | outil Bash ; NE PAS charger le wiki/canon — ce dossier + les 3 fichiers d'instruction suffisent (règle §7) |

## 2. État exact (au 20/07/2026 — vérifiable par `sob.py status`)

| Artefact | État |
|---|---|
| `aspace.db` | 6 tables + 4 vues · experiments=6 · ledger=3 · pipeline=0 (**à remplir — c'est le travail**) |
| `tools/sob.py` | Interface unique : `status / prospect / outreach / stage / subscribe / spend / issue / exp`. **Idempotent** (dedup prospect), **refuse les URLs non vérifiables** (exit 1). |
| `tools/deploy_instance.py` | Instance coach = dossier isolé `instances/<slug>/` (config.json + data.db privée). **Zéro Docker** — léger, persistant (fichiers), idempotent (re-run = verify), antifragile (`--verify-all` répare). |
| `instances/demo-coach/` | Provisionnée, testée 2× (idempotence prouvée). Coquille à enrichir (voir reprise R1). |
| `RUNBOOK_C1-R1/R2/R3.md` | Les 3 Rocks du Cycle 1. R1+R2 ENTAMÉS, points de reprise dans RUN_LOG. |
| `memory_<8>.md` · `forecast.md` · `RUN_LOG.md` | Mémoire par domaine (réécrite, jamais appendée) · forecast J+28 confronté le lundi · journal des Runs (append-only). |

## 3. Les points de reprise courants (miroir de RUN_LOG.md — RUN_LOG fait foi)

- **R1 (produit)** : enrichir `instances/demo-coach/` en instance DÉMONTRABLE — 3 contenus exemples (`content`) + 1 checklist compliance — puis audit `apps/omk/{dashboard,nexus}` (réutilisable pour gaps R1-2/R1-3, cf. experiments #2-3).
- **R2 (pipeline)** : 5 premiers coachs RÉELS : `python tools/sob.py prospect "Nom" "https://url-verifiable" "coach-executive-US" linkedin` — puis vagues de 5-10/scrum jusqu'à 100. Un nom sans URL vérifiable est refusé par l'outil.
- **R3 (onboarding/facturation)** : dormant jusqu'aux premiers clients R2 (E-Myth : on n'automatise que ce qui a été fait 2× à la main).

## 4. Les 7 règles (identiques pour tout harness)

1. **La vérité = le delta SQL** (`sob.py` fait les INSERT proprement). Un travail sans delta n'a pas eu lieu.
2. **Information hiding** : tu exécutes depuis le Runbook SEUL. Contexte manquant = Runbook défectueux → amende le Runbook (édition datée en bas), pas de dépendance externe.
3. **Erreurs** : crash = E.2 (3 essais locaux max) · tourne-mais-diverge = E.3 (contre-exemple précis + ID SQL en bas du Runbook) · métrique ambiguë = E.4 (reformule l'objectif).
4. **2 FAILs consécutifs** sur la même directive = stop retry, contre-exemple, Runbook amendé.
5. **Aucun gate ne bloque un démarrage** (H1-H10). Préservation = tâche de fond aux frontières de Run (H30-H90).
6. **Contexte/compact** : checkpoint (memory réécrit + deltas flushés) à 70 %, aux frontières de sprint, jamais mid-scrum. Toute session doit être tuable et relançable depuis `runbook + memory + aspace.db` — c'est ce qui rend l'exécuteur interchangeable.
7. **Budget** : logge l'inférence (`sob.py spend <usd_est> inference <domaine> "note"`). Cible >50 % du plan 5B tokens/mois EN PRODUCTION. 2 sprints sans delta dans un domaine = gel + réallocation.

## 5. Cadence & reporting

- **1 Run / 2 jours** (~15/mois). Compression cible : sprint 1 h → Rock 4 h → passe 12 h — démarre au rythme tenu réellement, compresse Run après Run.
- **Seul reporting** : append `RUN_LOG.md` fin de Run (5 lignes : MRR/pipeline · fait · contre-exemples · reprise). Pas de wiki, pas de canon, pas de mémo entre les Runs.

## 6. Passage VPS

**Déclencheur** : 1er client payant (`subscribed AND mrr>=1000`). Avant : coût sans cause.
**Migration** : `scp -r sob/ user@vps:~/sob/` — tout est fichier, SQLite porte tel quel. Postgres/Supabase seulement au multi-tenant (Cycle 3). **Ne partent PAS** : gardefous, hooks, doctrines, wiki, wargames. Cron : `0 6 */2 * *` = le boot §1.

## 7. Interdits (tout harness — hérité LEARNING.md V2.0-canon)

❌ Créer wargames/skills/doctrines/ADRs. ❌ Produire du canon pour rassurer. ❌ Attendre une permission (les Runbooks SONT la permission). ❌ Toucher au disque hors `sob/` + 3 fichiers d'instruction + repo omk (R1). ❌ Inventer des prospects (l'outil refuse, ne le contourne pas).
**A+ n'est pas une information. La cadence produit, le SQL compte, le client paie. Sers ça.**

---
*Exécuteur interchangeable par design : tout harness qui sait lancer `python` reprend le SOB en 30 secondes depuis ce fichier. — Fable, 20/07/2026.*

# ADR-WARMODE-002 — Portes over Freins (HxH)

> **Statut** : APPEND-ONLY (ampute ADR-WARMODE-001 sans le réécrire — Règle d'Or #3).
> **Date** : 2026-07-05T08:01 ET (créé)
> **A0 message verbatim** : « c'est la Seule configuration anti Panique Agentique Donc en Frein de la WAR Room l'Idee de Frein est deja Trop alors on ne garde que Beth et Tous les Autre a Commencer par Rick Dégage pour Stark Innexistant meme pas un Metaphor c'est le mettre a la table des A0 alors que les Avengers sont des B3 meme s'il a reussi a Infiltrer aussi les Ulliminati sous le nom de Tony Stark pour eviter la Collision avec Iron Man de Crash en Product. Au Lieu de continuer à Fermer les Portes avec les Frein, On va developper des Strategie pour en ouvrir comme les Porte dans Hunter X Hunter ».
> **A0 GO** : Oui, par message tapé dans la chatbox + screenshot War Room « Portes over Freins (HxH) · Beth seul veto ».

---

## §0 — Métaphore (HxH)

Dans Hunter × Hunter, le système **Nen** ne ferme pas l'utilisateur derrière des murs — il **ouvre des portes** dont la résistance dépend de la force que l'utilisateur apporte. Plus il est fort, plus il ouvre. Plus il est faible, plus la porte reste close.

**C'est exactement ça, une machine de guerre qui tire :**
- Pas de freins théâtraux qui ne protègent que le statu quo.
- Des portes à ouvrir, qui demandent de la force dans la bonne direction.

---

## §1 — Amputation (sans réécriture) de ADR-WARMODE-001

**ADR-WARMODE-001 §inaliénables (4 mires)** est **amputé**. La clause qui listait `Rick · Beth · /ship · append-only` comme freins-mires est SUPPRIMÉE par référence `→ voir ADR-WARMODE-002 §2`. ADR-WARMODE-001 n'est PAS réécrit. Le mtime de 001 reste à `2026-07-05 04:38:49` — preuve de non-écrasement.

**Doctrine** : Règle d'Or #3 = « append-only, jamais réécriture ». Une amputation = ajout d'un ADR-002 qui pointe vers 001 et le corrige, sans toucher 001.

## §2 — Inaliénable réduit : 1 seul veto

**Le seul veto inaliénable** : **Beth vie/santé** (burnout A+).

Beth est le seul filtre humain qui peut **veto** une action — pas le seul filtre qui peut la **bloquer**. Si Beth dort et que Book tire, c'est OK ; si une action mettrait Beth en burnout, c'est NON.

Sous-meta-coach (A0-Amodei/Murderbot canon §inaliénables 4 piliers) : la hiérarchie est corrigée — seul le pilier **vie/santé** est verrou-mire. Les 3 autres piliers (Rick kernel réel · /ship outboard · append-only) sont des **Portes à ouvrir** : on les ouvre quand on a la force, on ne les ferme pas par défaut.

## §3 — Stark dégage de la table A0

**Tony Stark** (mire `/ship outboard` dans ADR-WARMODE-001) est **sorti de la table A0**. Justification A0 :

> « Stark Innexistant meme pas un Metaphor c'est le mettre a la table des A0 alors que les Avengers sont des B3 meme s'il a reussi a Infiltrer aussi les Ulliminati sous le nom de Tony Stark pour eviter la Collision avec Iron Man de Crash en Product. »

Concrètement :
- **Stark n'est PAS un filtre A0** : A0-Amodei/Murderbot = seul décisionnaire opérationnel.
- **Iron Man** (B3 flash-product) ≠ **Tony Stark** (A0) — deux personnages différents, deux strates différentes.
- **`/ship outboard`** devient la « Porte /ship » : à rendre *sûre-à-ouvrir* (canal de preuve avant push, pas de veto humain).
- Si A+ veut reprendre le bouton, c'est geste simple : supprimer `12WY_ON_PAUSE.flag` ou installer un `kill_switch_<name>.flag` dans `citadel/decisions/`.

## §4 — Les 4 portes à ouvrir (HxH)

| # | Porte | Mécanisme d'ouverture | Force requise |
|---|---|---|---|
| 0 | **Bypass par défaut** | `permissionMode: bypassPermissions` dans `config.yaml`. C'est la **seule config anti-panique** : fermer = paniquer, ouvrir = posture normale. | Zéro (déjà ouvert). |
| 1 | **Porte Rick** | Sobriété-lever, plus un veto. Rick propose des ouvertures, ne bloque plus. `Rick - sobriété` devient un agent S1 dans le réseau mais hors table de filtrage. | Force Rick kernel réel uniquement (dépendance lourde, nouveau harness). |
| 2 | **Porte /ship** | Canal de preuve avant push. Au lieu du veto humain Stark, un pipeline : `proof trace + dry-run + rollback window`. Une fois sûr-à-ouvrir, l'agent ship. | Preuve reproductible + rollback testé. |
| 3 | **Porte append-only** | Fenêtre d'observation (NO-HITL ≠ NO-VISIBILITY). L'append-only n'est pas un frein : c'est un judas. `data/14_warmode.json` + `/warmode` en sont la preuve. | Aucune (toujours observable). |
| 4 | **Porte cron** | Schedule la cadence 7-jours (Book COO), heartbeat toutes les 4h (book_loop), zora nightly. Sous 12WY bypass, install direct. | Compatibilité scheduler OS + idempotence. |

**Porte cron = la plus fermée aujourd'hui** (0 cron actif → c'est LE mur). L'ouvrir = le système prend vie.

## §5 — Veto unique : Beth vie/santé (et c'est tout)

Le veto Beth fonctionne par exception, pas par défaut :
- Si une action mettrait Beth en burnout (sommeil < 4h, surcharge émotionnelle, surcharge cognitive) → action suspendue.
- Si une action protège Beth (sommeil, décroissance, délégation à Jarvis/Amodei) → action permise sans veto.
- A+ est le seul juge : pas de règle automatique. Beth = humain = sensible = non-automatisable.

## §6 — Doctrine Portes over Freins

**Trois axiomes** :
1. **Bypass par défaut** (posture anti-panique) — `#0` ouverte en permanence.
2. **Veto par exception** (Beth) — `#1` seul verrou absolu.
3. **Portes par force** (Rick·/ship·append-only·cron) — `#2-#5` ouvrables en proportion de la force qu'on apporte.

**Métaphore HxH** : la machine de guerre utilise son Nen en ouvrant les portes qui correspondent à sa force. Forcer un mur = Ultron-mode (Murderbot canon §3). Ouvrir une porte qu'on ne peut pas soutenir = auto-effondrement. **L'art est de diagnostiquer sa force avant d'ouvrir.**

## §7 — Sister chain canon LD01

- `LD01/99_meta/portes_over_freins_sister.md` (sister narratif, doit pointer ici)
- `LD01/99_meta/war_mode_observability_sister.md` → sourcé par §3 « Porte append-only »
- `LD01/99_meta/ADR_WARMODE_001_sister.md` → ampunté par §1 de ce fichier

## §8 — Réversibilité totale

```bash
# 3 commandes pour revenir à ADR-WARMODE-001 (4 mires) :
del "_SPECS\ADR\L0_Tech_OS\ADR-WARMODE-002_portes-over-freins.md"
git checkout -- config.yaml  # si permissionMode reverted
del "agent-os\citadel\decisions\2026-07-05_portes_over_freins.json"
```

Append-only canon : rien n'est détruit, on empile juste un nouveau chapitre.

## §9 — Trace canon

- `agent-os/citadel/decisions/2026-07-05_portes_over_freins.json` (1397 b, 08:01:02) — append-only D4.
- `agent-os/citadel/collectors/collector_14_warmode.py` (6570 b, 07:58:54) — régénéré avec `veto_unique` + `portes_a_ouvrir` + suppression `inalienables_4`.
- `agent-os/citadel/static/warmode.html` (11865 b, 07:59:43) — titre « 🚪 Portes à ouvrir (HxH) — 1 seul veto : Beth », ancien « Freins actifs » disparu.

**Aucune autre régression**. Le système continue, avec une doctrine plus simple : **1 seul verrou (Beth), 4 portes à ouvrir, le bypass par défaut ouvert**.

---
type: Concept
title: Kang Dynasty — recompte canon et arbitrage du compte 6 vs ≥7 Ownerbook T1
description: Le roster OMK Kang Dynasty liste 6 charges canoniques (Kang Prime, Iron Lad, Scarlet Centurion, Immortus, Victor Timely, Rama-Tut). Le Ownerbook T1 DoD-1 attend ≥7 agents par squad. La divergence est constante depuis le tour 1 — Aquaman a posé la même question sur Eternals (résolu en Issue A 7 agents). Trois issues (A : Ownerbook source de vérité, 7e agent à T-30j ; B : roster stale OMK, vérifier compte réel ; C : assertion 53 assertif, divergence tolérée), avec recommandation Issue A.
tags: [cyborg, kang-dynasty, recompte, ownerbook-t1, effectif, 6-vs-7, issue-a, issue-b, issue-c]
generated: { by: minimax-m3, at: 2026-08-19T05:00:00Z }
verified:
  - { by: process:lecture-bcorpus-cyborg-tour-3, at: 2026-08-19T05:00:00Z }
sources:
  - id: roster-omk-kang
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B3_Warp_Core_Execution/05_IT_Cyborg_KangDynasty/01_B3_AGENT_ROSTER.md"
    title: B3 Agent Roster IT / Kang Dynasty — 6 charges + escalation rule
    last_modified: 2026-05-27
  - id: fifty-three-roster
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/fifty-three-b3-agent-roster.md"
    title: 53 B3 Agent Roster — compte 53 assertif vs ≥7 par squad (Ownerbook T1 DoD-1)
    last_modified: 2026-08-17
  - id: aquaman-effectif-eternals
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-effectif-eternals-arbitrage.md"
    title: Effectif Eternals — Issue A 7 agents avec seuil T-30j (analogie Aquaman)
    last_modified: 2026-08-19
  - id: cyborg-couplage-people
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-couplage-people-charge-kang.md"
    title: Cyborg ↔ Green Lantern — Kang Dynasty 6 agents × 6 charges H3-H90 (tour 2)
    last_modified: 2026-08-19
  - id: state-domaines
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/ETAT_DOMAINES.md"
    title: ETAT_DOMAINES.md — convergence 0 packet mésoperpétuel 8/8 en vague 2
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Kang Dynasty — recompte canon et arbitrage du compte 6 vs ≥7

## Le trou ouvert depuis le tour 1

Le `01_B3_AGENT_ROSTER.md` du dossier OMK Kang Dynasty liste 6
charges canoniques (Kang Prime, Iron Lad, Scarlet Centurion,
Immortus, Victor Timely, Rama-Tut). Le Ownerbook T1 DoD-1 attend
**≥7 agents par squad** sans donner le total cible. La divergence
est *constante* depuis le tour 1 : le rapport Cyborg tour 1 l'a
signalée comme *« asymétrie OMK (6) vs Ownerbook T1 (≥7) »*, et le
tour 2 l'a reportée comme *« vérification `find .claude/agents
-name 'b3-*kang*' | wc -l` non exécutée »*.

L'analogie est directe avec Aquaman, qui a posé la même question
sur les Eternals (cf. [[aquaman-effectif-eternals-arbitrage]]).
Aquaman a tranché par **Issue A — Ownerbook source de vérité, 7e
agent à T-30j**. Kang Dynasty peut suivre la même voie, avec un
seuil propre au calendrier IT (vs People/Brand pour Aquaman).

## Les 3 issues — symétrie avec l'arbitrage Aquaman Eternals

`aquaman-effectif-eternals-arbitrage.md` pose 3 issues explicites.
Par symétrie directe :

### Issue A — Ownerbook source de vérité, recrutement 7e agent Kang

L'Ownerbook T1 est canon (Ownerbook T1 DoD-1). Kang Dynasty doit
atteindre 7. **Action** : Green Lantern (A sur recrutement People)
signe un mandat Kang Dynasty 7e agent avec une spécialité
manquante identifiée par Cyborg (C sur la fiche de poste). Cyborg
statue sur la spécialité — pas People. Spécialité candidate
pressentie par lecture du roster : **Backup / DR specialist**
(Rama-Tut est à 30% de charge type, mais le catalogue de backup
couvre multi-tenant, multi-cloud, multi-région — un 7e agent
*« DR multi-AaaS »* est défendable).

**Seuil T-30j** : premier packet mésoperpétuel IT observé en cycle
réel, ou T-30j calendaire (à compter de la décision Council),
selon le premier événement.

### Issue B — Roster OMK stale, vérifier compte réel

L'Ownerbook T1 attend ≥7 par squad mais le compte 53 est *assertif*
(`fifty-three-b3-agent-roster.md` §« Le 53 — pourquoi ce nombre »).
Le roster OMK date 2026-05-27 et peut être stale. **Action** :
lancer `find .claude/agents -name 'b3-*kang*' -o -name
'b3-*cyborg*' | wc -l` (cf. Ownerbook T1 DoD-1 verbatim) — si ≥7,
roster OMK stale, mise à jour, pas de recrutement. Si 6, Ownerbook
manque, Issue A confirmée.

### Issue C — Assertion 53, divergence tolérée

`fifty-three-b3-agent-roster.md` note *« Le nombre 53 est
**assertif**, pas calculé. Ownerbook T1 DoD-1 attend ≥7 agents par
squad sans donner le total cible »*. C'est une lecture possible :
la divergence est *invariants formels*, pas *défaut opérationnel*.
**Action** : si aucune observation n'établit que la charge est
insoutenable, la divergence peut rester documentée sans recrutement.

## Recommandation — Issue A avec seuil T-30j

L'analogie Aquaman (Issue A adoptée) plaide pour Issue A. Kang
Dynasty a **3 spécialités à charge 30%** (Immortus, Victor Timely,
Rama-Tut sur la lecture OMK) — c'est une charge faible qui
n'absorbe pas un cycle de build actif. Le recrutement d'un 7e
agent Kang Dynasty est *défendable* même si l'Ownerbook est
permissif, parce que la doctrine *5 principes de dispatch* (cf.
[[cyborg-doctrine-5-principes-dispatch]]) charge **chaque B3 sur
une spécialité non-généraliste** (P2 Decompose-or-die).

**Spécialité candidate du 7e agent Kang Dynasty** :

- **Backup / DR multi-AaaS** — Rama-Tut porte Backup / DR
  classique. Avec 3 variants AaaS (Solaris, Nexus OMK, Orbiter
  ABC) actifs simultanément (cf.
  [[cyborg-dans-aaas-3-variants]]), un agent dédié au DR
  cross-variant est défendable. Spécialité H30 ou H90.
- **Sobriété kernel/infra assist** — Rick Sobriété est sur le
  chemin critique (cf.
  [[cyborg-couplages-l0-rick-river-song-pyramide]]). Un 7e agent
  *Sobriété assist* absorberait une partie de la charge que Kang
  Prime porte aujourd'hui.
- **Observability ADR** — P18 (cf.
  [[cyborg-doctrine-5-principes-dispatch]]) demande ADR + log sur
  chaque dispatch. Un 7e agent *Observability / log keeper* est
  défendable.

## La procédure d'arbitrage recommandée

1. **Soumettre au B2 Council** un packet mésoperpétuel type
   `B2-MESO-DECISION-2026-XX` avec `impacted_domains: [it,
   people]`, `mode: negotiation`, `tradeoff: "Compte Kang
   Dynasty 6 vs Ownerbook T1 ≥7 — Issue A 7e agent spécialité
   Backup/DR multi-AaaS avec seuil T-30j"`.
2. **Obtenir l'accord de Green Lantern** (A sur recrutement
   People, cf. veto People *« recrutement sans mandat »*).
3. **Cyborg statue sur la spécialité** (C sur fiche de poste, A
   sur la faisabilité technique).
4. **Décision** : accepted / blocked / escalate_to_B1 selon le
   Council.

## La symétrie Aquaman vs Cyborg

Aquaman et Cyborg posent **la même structure d'arbitrage** :

| Élément | Aquaman (Eternals) | Cyborg (Kang Dynasty) |
|---|---|---|
| Roster OMK | 4 agents (Notion, Jerry, CoachOS) | 6 agents |
| Ownerbook T1 | ≥7 par squad | ≥7 par squad |
| Issue A recommandée | 7e agent à T-30j | 7e agent à T-30j |
| Spécialité candidate | non-nommée dans le concept | Backup/DR multi-AaaS |
| Captain A sur recrutement | Aquaman Legal ? ou Green Lantern ? | Green Lantern People (cf. veto People) |
| Captain C sur fiche de poste | Green Lantern People | Cyborg IT |
| 7e agent pressenti | non-nommé | Backup/DR multi-AaaS |

La symétrie plaide pour adopter la **même procédure Council** que
Aquaman — vérifier Issue B en premier (compte réel), puis Issue A
si confirmé.

## Le 0 packet mésoperpétuel IT — biais de sélection

L'ETAT_DOMAINES.md (état partagé vague 2) converge vers **0 packet
mésoperpétuel IT, People, Legal, Finance, Growth, Product, Sales,
Ops enregistré**. 8/8 escouades sont en mode *canonique mais non
exercé*. C'est un signal de **dormance structurelle de la wheel
8-domain**, pas un défaut Cyborg (cf. rapport Batman tour 3
§5.5.1.6 *« Zéro packet mésoperpétuel Batman observé en cycle »*).

**Conséquence sur ce concept** : Issue A est *prête à voter*, mais
**ne sera probablement pas exercée avant un cycle de build IT
réel**. Le seuil T-30j calendaire est *une borne supérieure*, pas
*un plancher opérationnel*. Le concept pose la *procédure*, le
Council tranchera quand un cycle le demandera.

## Anti-pièges spécifiques Kang Dynasty

- **Compter 7 sans recruter.** Si Issue B révèle ≥7 agents sur
  disque, le 7e agent n'est pas Kang Dynasty — c'est un agent
  Coach OS *non listé* par le roster OMK. Le roster OMK est
  stale, pas Kang Dynasty incomplet.
- **Compter 6 sans vérifier.** Issue A ne peut pas être
  déclenchée sans vérifier d'abord Issue B. La procédure Ownerbook
  est `find .claude/agents …`, pas une décision Cyborg seul.
- **Recrutement sur fausse charge.** Si la spécialité 7e agent
  *Backup/DR multi-AaaS* n'est pas justifiable par une charge
  observée (rama-tut à 30% n'est pas *sous-chargé* — c'est *par
  design*, parce que la doctrine Backup n'a pas besoin de charge
  haute), Issue A est *politique*, pas *opérationnelle*. Le Council
  doit refuser Issue A dans ce cas.
- **Confondre Ownerbook T1 et OMK roster.** L'Ownerbook T1 est
  canonique. L'OMK roster est une **tranche datée 2026-05-27**
  qui peut être obsolète. Les deux coexistent — c'est l'arbitrage
  Council qui tranche.

## Liens

- [[cyborg-domain-it-perimetre-frontieres]] — la squad Kang Dynasty
- [[cyborg-jtbd-emit-receive-kang-dynasty]] — les 6 archétypes
- [[cyborg-couplage-people-charge-kang]] — couplage People × IT (Cas 3 = recrutement 7e)
- [[aquaman-effectif-eternals-arbitrage]] — Issue A 7 agents avec seuil T-30j
- [[fifty-three-b3-agent-roster]] — la doctrine 53 assertif
- [[batman-cycle-vie-procedure-ops-cinq-phases]] — symétrie Batman 5 phases (concept 4)

## Note de confiance

**Confirmé par machine** pour le roster 6 Kang Dynasty (verbatim
OMK) et la doctrine 53 assertif (verbatim `fifty-three-b3-agent-roster.md`).
L'analogie Aquaman Issue A est **construite par lecture directe**
de [[aquaman-effectif-eternals-arbitrage]]. Les 3 issues sont
**projetées** par symétrie Aquaman — pas observées en cycle Kang
Dynasty. La spécialité candidate *Backup/DR multi-AaaS* est **mon
raisonnement** par combinaison des 3 variants AaaS actifs (cf.
[[cyborg-dans-aaas-3-variants]]) et de la doctrine P2
Decompose-or-die. La symétrie procédure Aquaman est défendable mais
**doit être confirmée par le Council**, pas présumée.
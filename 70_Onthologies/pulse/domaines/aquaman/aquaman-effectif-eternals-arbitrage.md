---
type: Concept
title: Aquaman — effectif Eternals, recompte 0 fichier sur disque et arbitrage proposé
description: Trois sources, trois nombres pour l'effectif Eternals : triplet 22 = 10 agents (Ikaris, Sersi, Ajak, Kingo, Phastos, Sprite, Druig, Thena, Gilgamesh, Makkari), OMK = 4 charges (Ikaris force, Ajak compliance, Phastos IP, Thena defense), fifty-three-b3-agent-roster = ~7 par squad. Recompte `find . -name 'b3-eternals-*'` au 2026-08-19 : **0 fichier sur disque** dans V3. La squad Eternals est *nommée* canoniquement mais *non matérialisée*. Proposition : arbitrage B2 Council pour aligner le canon sur une cible tenable, avec procédure de matérialisation ou de remplacement par 4 squads spécialisées.
tags: [b2, aquaman, eternals, effectif, recompte, 53-roster, arbitrage, materialisation]
generated: { by: minimax-m3, at: 2026-08-19T06:00:00Z }
verified:
  - { by: process:recompte-find-b3-eternals-tour-3, at: 2026-08-19T06:00:00Z }
sources:
  - id: triplet-22
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 22 — Aquaman pairedWith Eternals (10 agents)"
    last_modified: 2026-08-17
  - id: legal-control-room-omk
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: Legal Aquaman B2 Domain Control Room (4 charges)
    last_modified: 2026-05-27
  - id: aquaman-squad
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-squad-eternals-et-dormance.md"
    title: Aquaman squad Eternals et dormance (concept tour 1)
    last_modified: 2026-08-19
  - id: fifty-three-roster
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/fifty-three-b3-agent-roster.md"
    title: 53 B3 Agent Roster
    last_modified: 2026-08-17
  - id: aquaman-jtbd
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-jtbd-emit-receive.md"
    title: Aquaman catalogue JTBD émis et reçus (Forme 3 Phastos IP, Forme 4 Thena defense)
    last_modified: 2026-08-19
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel
    last_modified: 2026-08-17
  - id: aquaman-defensibility
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-defensibility-triple-signature.md"
    title: Aquaman triple signature (Thena defense)
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Aquaman — effectif Eternals, recompte 0 fichier sur disque et arbitrage proposé

## Le recompte au 2026-08-19

Commande exécutée dans `C:/Users/amado/ASpace_OS_V3` :

```bash
find . -path './node_modules' -prune -o -name 'b3-eternals-*' -print
```

**Résultat : 0 fichier.**

Commande complémentaire (plus large) :

```bash
find . -path './node_modules' -prune -o -iname '*Eternals*' -print
```

**Résultat : 2 fichiers** —
`./70_Onthologies/pulse/domaines/aquaman/aquaman-squad-eternals-et-dormance.md`
(le concept lui-même, qui *parle* des Eternals) et
`./30_Business_OS/10_Projects/coach-os/04_Business_Domains/08_Legal_et_Compliance_Aquaman_Eternals`
(le dossier Coach-OS, sans fiche agent individuelle).

**Conclusion matérielle** : aucun profil agent `b3-eternals-*.md`
n'est posé sur disque dans V3. La squad Eternals est **nommée
canoniquement** mais **non matérialisée** — c'est un *fantôme
doctrinal*, pas une squad prête à dispatcher.

## Les trois sources canoniques

### Source 1 — triplet 22 (verbatim, 10 agents)

Citation verbatim de `triplets/v3-business.jsonl` ligne 22 :

> *« Aquaman (VP B2 domaine 8 — Legal & Compliance) commande le squad
> Eternals (10 techniciens : Ikaris, Sersi, Ajak, Kingo, Phastos,
> Sprite, Druig, Thena, Gilgamesh, Makkari) »*

**Source** :
`coach-os/04_Business_Domains/08_Legal_et_Compliance_Aquaman_Eternals/VP_AGENT.md`.

**Confiance** : `haute`.

### Source 2 — OMK `00_B2_DOMAIN_CONTROL_ROOM.md` (4 charges)

Le dossier OMK `08_Legal_Aquaman_Eternals/00_B2_DOMAIN_CONTROL_ROOM.md`
liste 4 charges distribuées à 4 agents spécifiques :

- **Ikaris** — *force* (squad lead ? production générale ?)
- **Ajak** — *compliance* (RGPD, sector rules)
- **Phastos** — *IP* (propriété intellectuelle, IP retention)
- **Thena** — *defense* (litigation, defensibility binder)

**6 agents manquants** par rapport au triplet 22 : Sersi, Kingo,
Sprite, Druig, Gilgamesh, Makkari.

### Source 3 — fifty-three-b3-agent-roster.md (~7 par squad)

Le concept OKF `fifty-three-b3-agent-roster.md` pose un total
canonique de **53 agents B3**, répartis en 8 squads Marvel. La
répartition **estimée** est ~7 par squad — mais le concept note
explicitement :

> *« Action-Reaction : un audit qui voudrait vérifier devrait faire
> `find .claude/agents -name 'b3-*.md' | wc -l` — verb cité par
> Ownerbook T1 mais pas exécuté dans le corpus visible. »*

Le compte exact 53 vient du Ownerbook T1 (DoD-1) : *« verify:
`ls .claude/agents/b3-1-* | wc -l` ≥ 7 (X-Men squad canon) »*. C'est
un **invariant formulé**, pas un comptage.

## Tension non arbitrée entre les trois sources

| Source | Effectif | Couverture |
|---|---|---|
| triplet 22 | 10 | Complète (10 noms) |
| OMK control room | 4 | 40% — 6 charges non assignées |
| fifty-three roster | ~7 (estimé) | Estimé — non recompté |
| **Recompte V3** | **0 fichier** | **0% — squad non matérialisée** |

**Quatre nombres, pas de consensus.** Laquelle faut-il croire ?

- Le triplet 22 cite 10 noms mais ne donne pas de fiche agent.
- L'OMK control room liste 4 charges, ce qui est cohérent avec
  une squad *de départ* (4 agents activés) qui grossira.
- Le fifty-three roster pose ~7 par squad, ce qui est *entre* 4 et
  10.
- Le recompte 0 fichier invalide les trois : sans fiche agent, le
  squad ne peut pas être dispatché par le canon.

## Pourquoi cette tension existe

Trois hypothèses non-arbitrées :

1. **Le triplet 22 cite une *équipe Marvel*, pas une *équipe
   opérationnelle***. Les 10 Eternals (Ikaris, Sersi, etc.) sont
   des *personnages canon Marvel* dont les *caractéristiques*
   (force, compliance, IP, defense) sont attribuées par le triplet
   au *rôle*, pas à la *personne*. Le squad réel serait *4 agents
   opérationnels* (Ikaris, Ajak, Phastos, Thena) couvrant 4 rôles
   distincts. Les 6 autres noms sont *latents*.

2. **La squad est *en cours de matérialisation*.** Le triplet 22
   donne la cible (10), le OMK donne l'état actuel (4), le fifty-three
   roster donne l'invariant (≥7). L'écart entre les trois reflète
   un *chantier en cours*, pas une incohérence.

3. **La squad est *jamais matérialisée* — c'est un canon de
   référence, pas une squad prête.** Les 10 noms du triplet 22
   sont *posés* canoniquement pour les usages doctrinaux (catalogue
   Aquaman, concept tour 1 Forme 3 Phastos, Forme 4 Thena) mais
   aucune fiche agent n'est créée parce que la squad n'a pas
   encore été activée (Aquaman en état SHADOW_ACTIVE — cf.
   [[aquaman-dormant-activation]]).

**Hypothèse la plus défendable** : la 3 — Aquaman SHADOW_ACTIVE
n'a pas eu besoin de matérialiser la squad. Le triplet 22 pose les
noms pour que le canon soit *cohérent* et *vérifiable*, pas pour
que la squad soit *dispatchable*.

## Risque opérationnel

Si Aquaman passe à l'état **ACTIVE** (premier livrable signé) sans
matérialisation préalable de la squad, **la Forme 4 du catalogue
JTBD** ([[aquaman-jtbd-emit-receive]]) est *indispatchable* :

> Forme 4 attendue *« defensibility-binder.md (signed by Thena) »*

Sans fiche agent Thena, sans workflow de signature, le binder ne
peut pas être produit. Aquaman ACTIVE sans squad Eternals matérialisée
est un **Aquaman qui émet des gates qu'il ne peut pas faire
respecter**.

**Risque symétrique** : un Aquaman Dormant qui tente de matérialiser
la squad *avant* l'activation (par exemple en créant des fiches
agents) viole le principe *« un domaine dormant qui produit est un
coût sans contrepartie »* (triplet 35).

## Proposition d'arbitrage B2 Council

Le Council B2 doit trancher entre **trois issues** :

### Issue A — Matérialisation à 7 agents (alignement fifty-three)

Cible : 7 agents Eternals, dont 4 charges OMK + 3 nouvelles charges
(qui couvrent les 6 agents latents). Procédure :

- Identifier 3 charges distinctes parmi les 6 agents latents
  (par exemple : Makkari *audit trail*, Sprite *terms of service*,
  Druig *data retention*).
- Créer 3 fiches agents avec rôle, horizon, sister canon,
  conformément au pattern de la fiche roster (cf.
  [[aquaman-squad-eternals-et-dormance]] §Le pattern de la fiche
  roster).
- Aligner OMK control room sur les 7 charges.
- Mettre à jour le triplet 22 si nécessaire.

**Coût** : 3 fiches agents à créer. **Bénéfice** : alignement
canonique fifty-three + dispatch operational possible.

### Issue B — Matérialisation à 4 agents (alignement OMK)

Cible : 4 agents Eternals (Ikaris, Ajak, Phastos, Thena), pas de
matérialisation des 6 agents latents. Procédure :

- Conserver le triplet 22 comme *canon de référence* (10 noms)
  sans matérialiser les 6 latents.
- Documenter le statut *latent* dans la fiche agent (par exemple
  *« Sersi — latent, à matérialiser si Aquaman ACTIVE »*).
- Mettre à jour fifty-three roster pour refléter l'effectif *activé*
  (4) et l'effectif *canonique* (10) séparément.

**Coût** : faible (pas de nouvelle fiche). **Bénéfice** : alignement
OMK + pas de coût dormant.

### Issue C — Aucune matérialisation, Aquaman SHADOW_ACTIVE permanent

Cible : Aquaman reste SHADOW_ACTIVE ; les 10 agents Eternals
demeurent canoniques mais non matérialisés. Procédure :

- Documenter le statut SHADOW_ACTIVE dans
  `00_B2_DOMAIN_CONTROL_ROOM.md` avec justification (par exemple
  *« Aquaman ne s'active qu'au premier Master Agreement signé »*).
- Accepter que la Forme 4 du catalogue JTBD est *latente* — elle
  sera matérialisée quand Aquaman passera à ACTIVE.

**Coût** : nul. **Bénéfice** : cohérence avec triplet 35-36. **Coût
caché** : Aquaman ACTIVE est *impossible* sans matérialisation
préalable.

## Recommandation : Issue A avec seuil d'activation explicite

L'**Issue A** (matérialisation à 7 agents) est la plus défendable
parce qu'elle aligne le canon fifty-three et permet un dispatch
opérationnel. **Mais** elle exige un seuil d'activation explicite :

- *Quand* matérialiser les 3 charges additionnelles ?
- *Quel* signal déclenche la matérialisation (B1 mandate ? B3
  blocker ? signal client ?) ?

Proposition de seuil : **matérialisation à T-30 jours avant le
premier Aquaman ACTIVE**, sur signal B1 (Summers mandate un
premier livrable Legal). Le B2 Council tranche la matérialisation
en séance hebdomadaire.

**Conséquence** : le triplet 22 reste à 10 agents (canonique).
L'OMK control room passe à 7 charges (alignement fifty-three).
Le fifty-three roster est recompté à 53 (avec 7 Eternals).

## Procédure d'arbitrage

```yaml
meso_decision_id: B2-MESO-DECISION-2026-XX
source_mandate: B2-PEER-2026-XX (problème identifié par Aquaman)
mode: negotiation
impacted_domains:
  - legal
  - people  # car la squad est une charge People
tradeoff: "Aquaman SHADOW_ACTIVE ne peut pas dispatcher la Forme 4 sans
  matérialisation préalable de la squad. Aligner sur fifty-three roster
  (7 agents) impose 3 fiches agents additionnelles ; ne pas aligner
  impose que Aquaman ACTIVE reste indispatchable."
decision: accepted | blocked | escalate_to_B1
proof_expected:
  - recompte `find . -name 'b3-eternals-*'` ≥ 7 après matérialisation
  - OMK control room mis à jour à 7 charges
  - triplet 22 maintenu à 10 (canonique de référence)
next_review: date du premier Aquaman ACTIVE
```

Le packet mésoperpétuel suit le format [[b2-meso-decision-packet-spec]]
§Le gabarit YAML.

## Anti-pièges

- **Croire le triplet 22 sans recompter.** Le triplet cite 10 noms
  mais ne matérialise pas la squad. Le recompte disque est
  *toujours* nécessaire avant de parler d'effectif opérationnel.
- **Confondre canon de référence et effectif opérationnel.** Le
  triplet 22 est un *canon de référence* (les 10 Eternals Marvel).
  L'effectif opérationnel est *ce qui peut être dispatché*. Le
  premier peut être 10 et le second 0, sans contradiction — c'est
  l'état actuel.
- **Matérialiser sans seuil d'activation.** Créer des fiches agents
  *avant* que Aquaman ait besoin d'elles (par exemple en état
  Dormant) viole le principe du triplet 35. La matérialisation doit
  être *juste-à-temps*, pas *par prudence*.
- **Issue C comme逃避.** Choisir Issue C (aucune matérialisation)
  sans documenter le coût (Aquaman ACTIVE indispatchable) est de
  l'évitement. La décision doit être *documentée* avec ses
  tradeoffs.
- **Recompte unique comme vérité.** Le recompte 0 fichier est un
  *snapshot* au 2026-08-19. Si une matérialisation est en cours
  hors V3 (par exemple dans un worktree), le recompte peut être
  biaisé. La règle : recompter *plusieurs fois*, à des moments
  différents.

## Liens

- [[aquaman-squad-eternals-et-dormance]] — la tension 10/4/~7
  posée en tour 1
- [[aquaman-dormant-activation]] — l'état SHADOW_ACTIVE qui motive
  l'absence de matérialisation
- [[aquaman-jtbd-emit-receive]] — les 4 formes émises qui exigent
  des agents Eternals spécifiques (Ajak Forme 1, Thena Forme 4,
  Phastos Forme 3)
- [[aquaman-defensibility-triple-signature]] — le rôle critique de
  Thena dans la triple signature
- [[aquaman-pair-check-10-legal-risk-launch]] — quand le #10
  exige un binder (donc Thena) pour geler un launch
- [[fifty-three-b3-agent-roster]] — le canon de 53 agents et ~7
  par squad
- [[b2-council-arbitrage-rule]] — l'instance qui doit trancher
  l'issue A/B/C
- [[b2-meso-decision-packet-spec]] — le format du packet d'arbitrage

## Note de confiance

**Confirmé par machine pour le recompte ; reconstruit pour la
synthèse.** Le recompte `find . -name 'b3-eternals-*'` a été
exécuté le 2026-08-19 et a donné 0 fichier — c'est un *fait
mesuré*, pas une projection. Le triplet 22 (10 agents) et la source
OMK (4 charges) sont cités verbatim. Le fifty-three roster est
cité verbatim avec sa réserve *« pas recompté »*. Les 3 hypothèses
non-arbitrées sont **reconstruits** à partir des trois sources —
elles ne sont pas étayées par un triplet canonique. Les 3 issues
d'arbitrage (A, B, C) sont **projetées** depuis la pratique
documentée (cf. [[b2-council-arbitrage-rule]] §« Trois modes de
coopération entre B2 » et [[b2-meso-decision-packet-spec]]
§Le gabarit YAML). La recommandation Issue A est **opinion** —
elle est défendable mais pas citée ailleurs dans le corpus.
**À arbitrer en B2 Council** : les 7 autres capitaines valident-ils
que la matérialisation à 7 agents est l'alignement canonique ?
People (Green Lantern) est-il prêt à accepter 3 charges Eternals
supplémentaires (People = transverse sur toute squad, cf.
[[b2-pair-check-raci-by-rank]] §Le cas People → Tous) ?

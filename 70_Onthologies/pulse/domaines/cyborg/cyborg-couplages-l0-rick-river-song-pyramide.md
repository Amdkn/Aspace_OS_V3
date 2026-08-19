---
type: Concept
title: Cyborg — couplages invisibles avec L0 Rick, River Song et la pyramide L0≥L1>L2
description: Cyborg ne touche pas L0 directement : il passe par River Song (SDD-004 §7.2), médiation agentique imposée. La pyramide SDD-006 §1.1:59 (L0 autorité absolue, L1 veto Beth, L2 exécute) surplombe toute décision IT. W40 §M1+M2 patches aurait absorbé l'IT infra à L0 Rick (Cyborg devient R&D External Discovery) — cette absorption est présumée et reste à confirmer.
tags: [cyborg, l0, rick, river-song, pyramide, mediation, sdd-004, sdd-006, beth]
generated: { by: minimax-m3, at: 2026-08-19T04:15:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T04:15:00Z }
sources:
  - id: triplet-cyborg-river-song
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 38 — Cyborg dependsOn River Song (SDD-004 §7.2)"
    last_modified: 2026-08-17
  - id: triplet-pyramide-l0l1l2
    resource: "C:/Users/ado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 39 — Pyramide L0 ≥ L1 > L2 (SDD-006 §1.1:59)"
    last_modified: 2026-08-17
  - id: triplet-cyborg-rd
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 21 — Cyborg pairedWith Kang Dynasty (R&D & IT)"
    last_modified: 2026-08-17
  - id: agents-md
    resource: "C:/Users/amado/ASpace_OS_V3/30_Business_OS/AGENTS.md"
    title: "AGENTS.md — protocole Forge/Inject, pyramide L0/L1/L2"
    last_modified: 2026-08-19
  - id: cyborg-dispatch-doctrine
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/06_Claude_Code_Bare/mindsets/B2_Cyborg_IT_Dispatch.md"
    title: Cyborg IT Dispatch Doctrine — Sobriété A1 Rick, A0 HITL
    last_modified: 2026-08-02
  - id: sdd-006-collision
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/domaines/normatif-sdd-prd/concept-sdd-006-collision.md"
    title: "Collision SDD-006 — Business Pulse vs Définition DEAL H1 Isaac"
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Cyborg — couplages L0 / River Song / pyramide

## Le triplet fondateur : Cyborg ↔ River Song

Triplet 38 (verbe `dependsOn`) :

> *« Cyborg (B2 IT/R&D) ne touche pas L0 directement — il passe par
> River Song (SDD-004 §7.2), médiation agentique imposée. »*

C'est une **dépendance structurelle** : Cyborg est dans la dépendance
opérationnelle de River Song pour toute action qui touche L0 (le
noyau). La médiation est **imposée**, pas négociée — Cyborg ne peut
pas la contourner.

Conséquence concrète : un Cyborg qui veut modifier une skill L0
(Identity, Rules and hooks) doit **passer par River Song**, qui
tient le canal L0. Cyborg propose l'intention, River Song exécute (ou
refuse). Cette médiation protège la souveraineté L0 contre les
initiatives B2 opportunistes.

## La pyramide L0 ≥ L1 > L2 (SDD-006 §1.1:59)

Triplet 39 :

> *« La pyramide L0 ≥ L1 > L2 (SDD-006 §1.1:59) impose que L0 a
> autorité absolue, L1 a le veto (Beth), L2 exécute dans ces bornes. »*

Position de Cyborg dans la pyramide :

- **L0** = Life OS / Rules of the road / Sovereign Identity. Authority
  absolue.
- **L1** = Beth (Morty companion), veto sur L2.
- **L2** = Cyborg et la squad Kang Dynasty. Exécute dans les bornes
  L0/L1.

Cyborg est **L2**. Toute décision IT qui touche L0 (modification de
l'Identity core, des hooks, des skills canoniques) remonte **à L1
(Beth)** par le canal River Song. Cyborg ne statue pas sur L0.

## Le protocole Forge / Inject (Green Lantern ↔ Bill)

Le triplet 37 pose un canal symétrique pour Green Lantern (People)
qui n'est pas celui de Cyborg :

> *« Green Lantern (B2 People) sollicite les skills L0 via Bill (L0.2
> Forge) ; Forge = CLI, Inject = River Song — le protocole ne se
> contourne pas. »*

**Différence structurelle** : Green Lantern passe par **Bill
(L0.2 Forge)**. Cyborg passe par **River Song** directement (le
triplet 38 ne mentionne pas Bill). Le canal est différent :

- **Green Lantern** → Bill (Forge) → River Song (Inject)
- **Cyborg** → River Song directement

Pourquoi cette différence ? **Hypothèse** : Cyborg est plus proche de
la couche IT/infra, et Bill est plus orienté skills/process. La
distinction n'est pas tranchée canoniquement — c'est une observation
des triplets. À confirmer avec B1 si elle a un sens opérationnel.

## La Sobriété A1 Rick sur kernel/infra

`B2_Cyborg_IT_Dispatch.md` pose une **deuxième médiation** :

> *« IT changes also pass A1 Rick Sobriety on kernel/infra
> (`Rick_Mindset.md`). »*

Rick (A1 — au-dessus de L2) tient la **Sobriété** sur les
changements kernel/infra. Le pipeline d'une décision IT Cyborg qui
touche kernel/infra est :

```
Cyborg (L2) → Kang Dynasty (L2 B3)
       │
       ├──> River Song (L0) si touche L0
       │
       └──> Rick Sobriety (A1) si touche kernel/infra
              │
              └──> Beth (L1) veto final
```

**Trois médiations possibles** sur une décision IT, selon la couche
touchée :

1. **River Song** (L0) — si touche Identity, hooks, skills canoniques.
2. **Rick Sobriety** (A1) — si touche kernel/infra.
3. **Beth Veto** (L1) — si touche un arbitrage cycle / North Star.

## Le présumé W40 §M1+M2 patch — R&D absorbé par L0 Rick

`fifty-three-b3-agent-roster.md` (concept OKF du 2026-08-17) note :

> *« W40 §M1+M2 patches — l'IT infra absorbé à L0 Rick (Cyborg devient
> R&D External Discovery) »*

C'est une **mutation structurelle** postulée :

- **Avant W40** : Cyborg tient IT + R&D.
- **Après W40** : IT infra absorbé à L0 Rick ; Cyborg devient
  *R&D External Discovery*.

Cette absorption est **présumée**, pas confirmée. Les sources qui
pourraient la confirmer :

- W40 V4 patches (cite *« §M1+M2 »* mais le contenu détaillé n'a pas
  été lu dans cette vague).
- Le triplet 21 cite *« R&D & IT »* mais ne tranche pas l'absorption.

**Statut** : à confirmer par lecture directe du W40 V4 patches, ou
par décision Summers explicite. Si l'absorption est confirmée, le
périmètre Cyborg devient **R&D External Discovery uniquement** (sans
IT infra), et la squad Kang Dynasty migre vers L0 Rick.

C'est une **remontée vers B1** dans le rapport.

## Couplage indirect Batman ↔ Cyborg ↔ L0 Rick

`batman-couplage-ops-it.md` reconstruit la chaîne :

> *« Triplet 38 dit « Cyborg ne touche pas L0 directement — il passe
> par River Song (SDD-004 §7.2), médiation agentique imposée ».
> C'est une dépendance IT qui ne touche pas Batman directement — mais
> elle le touche **indirectement** : si Cyborg est bloqué en médiation
> L0, Batman ne peut pas boucler #4. »*

Cyborg bloqué en L0 ⇒ Batman bloqué en #4 ⇒ Ops ne peut pas tenir le
pair-check #3 ⇒ **red flag #1** (Product green, Ops/IT red) ⇒
**arrêt dur**.

Conséquence : la médiation L0 n'est pas qu'une affaire Cyborg —
elle remonte au B2 Council comme un **risque cross-domaine**. Si
Cyborg signale un blocker L0 persistant (>24h ouvrées), Batman
remonte à Summers (cf. doctrine remonte-fait, triplet 56).

## Le cas spécial — SoberSobriété Sobriété Sobriété

La sobriété IT est **doublement médiée** :

- Sobriété A1 Rick (kernel/infra).
- Sobriété B1 (HITL gate via A0, cf. `B2_Cyborg_IT_Dispatch.md`
  *« No cron without A0 HITL (`B1_Manifesto.md` §Sobriety) »*).

Deux étages de sobriety — c'est plus que les autres captains. La
raison **présumée** : IT touche l'infrastructure, et une
modification infra ratée peut bloquer l'ensemble de l'organisation.
La sobriété est proportionnelle au risque de blast radius.

## Anti-pièges

- **Cyborg qui touche L0 directement.** Interdit structurel (triplet
  38). Le canal est River Song, pas un script personnel.
- **Cyborg qui bypasse Rick Sobriété.** Interdit (Dispatch Doctrine).
  Rick Sobriété est sur le chemin critique.
- **Cyborg qui absorbe R&D sans décision Summers.** Le périmètre
  R&D & IT du triplet 21 n'est pas une absorption. Si Summers
  n'a pas tranché, Cyborg reste IT strict.
- **Batman qui ignore un blocker Cyborg L0.** Si Cyborg signale un
  blocker L0 persistant, Batman remonte. Un blocker Cyborg qui
  dure >24h est un red flag #1 latent.
- **Summers qui réécrit la pyramide L0/L1/L2.** La pyramide est
  canonique (SDD-006 §1.1:59). Summers peut l'arbitrer, pas la
  réécrire sans amendement.

## Liens

- [[cyborg-domain-it-perimetre-frontieres]] — le périmètre
- [[cyborg-jtbd-emit-receive-kang-dynasty]] — les paquets B3
- [[cyborg-veto-cloud-only-sortie]] — le veto Cyborg
- [[batman-couplage-ops-it]] — la chaîne qui expose Cyborg
- [[b2-pair-check-raci-by-rank]] — RACI par rang

## Note de confiance

**Confirmé par machine** pour le triplet 38 (River Song) et le
triplet 39 (pyramide L0/L1/L2). Le canal Green Lantern → Bill →
River Song vs Cyborg → River Song est **observé** dans les triplets
mais **non expliqué canoniquement**. L'absorption W40 §M1+M2 (IT
absorbé à L0 Rick) est **présumée** par lecture du concept OKF
`fifty-three-b3-agent-roster.md` (ligne *« standing : IT infra absorbé
à L0 Rick (Cyborg devient R&D External Discovery) »*) — **pas vérifiée
par lecture directe des patches W40 V4**. C'est une remontée B1.

La double médiation Soberété Rick + A0 HITL est **citée verbatim**
par `B2_Cyborg_IT_Dispatch.md` mais son interprétation (blast radius
proportionnel) est **mon raisonnement**.

---
id: B3_GUARDIANS_PEER_UNBLOCKING_HANDOFFS
layer: B3_SWARM_EXECUTION
surface: Jerry Area J01 LD01 Business
domain: Growth
b3_swarm: Guardians
status: SHADOW_ACTIVE
updated: 2026-05-29
---

# Peer Unblocking & Handoffs — Guardians

Comment les Guardians se débloquent entre eux et se passent le relais **sans remonter à Superman** pour chaque micro-friction. Objectif : autonomie maximale du swarm dans les limites de la DoD.

## Principe de subsidiarité

Un Guardian bloqué tente d'abord un **peer-unblock** (demande à un pair) avant toute escalation B2. On ne remonte à Superman que si le blocage touche le Rock, la DoD, un gate cross-domaine, ou un secret.

## Matrice de handoff (AARRR flow — canon 6 membres)

Le parcours d'une expérience Growth suit le funnel ; le relais passe d'un Guardian à l'autre selon le rôle canon Notion :

```
Star-Lord (Lead Gen / ICP Hunter)         [Acquisition]   P1, P9, P13
   ↓ ICP + leads bruts
Mantis (voice-of-customer / persona)       [Activation]    P7q, P16, P13
   ↓ verbatims douleur + base psychologique
Groot (content / brand voice)              [Acquisition]   P8, P14, P16, P18
   ↓ message painkiller + contenu SEO
Rocket (growth hacks / automation / test)  [Rétention]     P2, P6, P7q, P12, P15
   ↓ expérience instrumentée + boucles
Drax (A/B testing brutal — kill)           [Activation]    P5, P6, P10
   ↓ variants gagnants only
Gamora (ABM high-ticket / closing valeur)  [Revenu]        P3, P11
```

## Protocole de handoff (packet)

```yaml
handoff_id: GRD-HANDOFF-YYYY-NN
from_agent: Star-Lord
to_agent: Mantis
experiment_id: link to RICE backlog item
artifact_passed: "ICP cible + liste leads bruts scrapés (Apollo/LinkedIn)"
proof: "Airtable record ids / scrape log"
expectation: "Mantis produit 3 verbatims voice-of-customer + base psychologique persona (P16)"
deadline: date
```

## Règles de peer-unblock

1. **Demande explicite** : le bloqué poste un `BLOCKED` avec input manquant + hypothèse échouée (cf. blocker_protocol du JTBD).
2. **Pair répond sous 1 cycle** : le Guardian sollicité fournit l'artefact ou dit "je ne peux pas, raison X".
3. **Pas de ping-pong** : si 2 allers-retours ne débloquent pas → escalation Superman (la friction révèle une DoD floue, cf. Anti-Bottleneck Rule du pipeline).
4. **Pas de redéfinition** : un pair ne peut pas changer le Rock/DoD pour débloquer — seulement fournir des inputs ou un workaround conforme.

## Cas de handoff cross-domaine (hors Guardians)

| Besoin | Domaine cible | Gate |
|--------|---------------|------|
| Closing juridique d'un deal | Sales/Illuminati (08) + Legal/Eternals (07) | cross-domain gate via Superman |
| Coût compute d'une automation | IT/KangDynasty (05) | gate Cyborg |
| Marge / pricing d'une offre | Finance/Thunderbolts (06) | gate Wonder Woman |
| Build d'une feature produit | Product/Avengers (04) | gate Flash |

Tout handoff cross-domaine passe par Superman (B2) qui ouvre le gate — les Guardians ne court-circuitent pas.

## Escalation ladder

```
Peer-unblock (Guardian↔Guardian)
   ↓ échec après 2 allers-retours
Superman (B2) — clarifie DoD ou ouvre gate cross-domaine
   ↓ blocage stratégique
Jerry Prime (B1) — arbitrage Area
   ↓ conflit de loi
Rick/Morty (B1 gate) — décision souveraine
```

*B3 handoffs under Superman (B2). Last sync: 2026-05-29*

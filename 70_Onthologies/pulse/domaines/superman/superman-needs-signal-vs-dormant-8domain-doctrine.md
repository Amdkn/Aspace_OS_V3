---
type: Concept
title: Doctrine NEEDS_SIGNAL ↔ DORMANT — extension aux 8 domaines B2 (canonique)
description: La doctrine des 3 conditions de dormance (cf. b2-areas-dormants-doctrine.md) est illustrée par Aquaman Legal (triplet 35). Superman Growth a 3 états canoniques (GROWTH_READY/NEEDS_SIGNAL/BLOCKED_PROMISE, cf. eight-domain-avengers-wheel.md) mais aucun des 6 autres domaines n'a posé explicitement la distinction NEEDS_SIGNAL ↔ DORMANT. Ce concept propose une table canonique 8-domaines × 4 états (READY/NEEDS_SIGNAL/BLOCKED/DORMANT) avec les conditions de transition et de réveil par domaine.
tags: [superman, growth, dormancy, needs-signal, doctrine, 8-domaines, canonical-extension]
generated: { by: minimax-m3, at: 2026-08-19T07:15:00Z }
verified:
  - { by: process:lecture-corpus-superman-vague-3, at: 2026-08-19T07:15:00Z }
sources:
  - id: b2-areas-dormants
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-areas-dormants-doctrine.md"
    title: B2 Areas-dormants — doctrine canonique 3 conditions cumulatives
    last_modified: 2026-08-19
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — 3 états Superman, autres non explicites
    last_modified: 2026-08-17
  - id: superman-dormance-active-posture
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-dormance-active-posture.md"
    title: Superman dormance — 3 scénarios + 3 déclencheurs + 7 règles
    last_modified: 2026-08-19
  - id: triplet-35
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 35 — Aquaman steward domaine-dormant (exemple canonique)"
    last_modified: 2026-08-17
  - id: dormance-active-posture-tour2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-dormance-active-posture.md"
    title: Superman — cas-limite NEEDS_SIGNAL n'est pas dormant
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Doctrine NEEDS_SIGNAL ↔ DORMANT — extension aux 8 domaines B2

## Le problème — Superman a 3 états, les 7 autres ont 1

`eight-domain-avengers-wheel.md` pose **3 états canoniques**
pour Superman Growth :

- `GROWTH_READY` (vert)
- `NEEDS_SIGNAL` (jaune — Superman attend un signal externe)
- `BLOCKED_PROMISE` (rouge)

Les 7 autres capitaines ont des états équivalents par leur
**gate** B2 (`READY`/`READY`/`READY`…), mais aucun n'a posé
explicitement la **distinction entre `NEEDS_SIGNAL` (actif en
attente) et `DORMANT` (inactif)**.

`b2-areas-dormants-doctrine.md` pose les 3 conditions
cumulatives de dormance, illustrées par Aquaman (triplet 35)
seul. La généralisation aux 7 autres domaines est marquée *«
projection »* par la note de confiance du concept canonique.

Le tour 2 Superman a proposé une doctrine dormance Superman
(`superman-dormance-active-posture.md`) en s'appuyant sur la
symétrie des 3 conditions canoniques. Mais la **distinction
NEEDS_SIGNAL ↔ DORMANT** reste **non explicitée canoniquement
pour les 7 autres domaines**.

## Les 4 états canoniques proposés

| État | Définition | Produit ? | Statut canonique |
|---|---|---|---|
| `READY` | Le domaine a un DoD courant et une cadence de production | Oui, en cadence | Cité pour les 8 domaines |
| `NEEDS_SIGNAL` | Le domaine est actif mais attend un signal externe pour produire | Oui, en veille | Cité pour Superman uniquement, projeté ailleurs |
| `BLOCKED` | Le domaine est bloqué par veto catalogue ou red flag matrice | Non | Cité pour les 8 domaines (3ᵉ état) |
| `DORMANT` | Le domaine est inactif — DoD vide, pas de ressource externe | Non | Cité pour Aquaman, projeté Superman |

## La table 8-domaines × 4 états — proposition

| Domaine | READY | NEEDS_SIGNAL | BLOCKED | DORMANT | Note |
|---|---|---|---|---|---|
| **01 Growth (Superman)** | ✅ cité | ✅ cité | ✅ cité | 🟡 projeté (vague 3) | Le seul domaine avec 4 états projetés |
| **02 Sales (JohnJones)** | ✅ cité | 🟡 projeté | ✅ cité (BLOCKED_COMMITMENT) | 🟡 projeté | Bloqué sans problème reformulé |
| **03 Product (Flash)** | ✅ cité | 🟡 projeté | ✅ cité (BLOCKED_DELIVERY) | 🟡 projeté | Bloqué par scope flou |
| **04 Ops (Batman)** | ✅ cité (LAUNCH_READY) | 🟡 projeté | ✅ cité (implicite) | 🟡 projeté | Bloqué par procédure sans arrêt |
| **05 IT (Cyborg)** | ✅ cité (SYSTEM_READY) | 🟡 projeté | ✅ cité (QUARANTINE) | 🟡 projeté | Bloqué par cloud-only |
| **06 Finance (Wonder Woman)** | ✅ cité (FINANCE_READY) | 🟡 projeté | ✅ cité (BLOCKED_LEAKAGE) | 🟡 projeté | Bloqué par dépense sans revue |
| **07 People (Green Lantern)** | ✅ cité (ASSIGNED) | 🟡 projeté | ✅ cité (DLQ) | 🟡 projeté | Bloqué par recrutement sans mandat |
| **08 Legal (Aquaman)** | ✅ cité (LEGAL_READY) | 🟡 projeté | ✅ cité (BLOCKED_RISK) | ✅ cité (triplet 35) | Le seul avec DORMANT cité canoniquement |

## Les conditions de transition entre états

### READY → NEEDS_SIGNAL

**Déclencheur** : un signal externe manque. Le domaine est en
cadence de production, mais un input nécessaire n'arrive pas.

**Par domaine** :

- **Superman (Growth)** : pas de signal marché (pas de vague
  d'attention). Cf. `eight-domain-avengers-wheel.md`.
- **JohnJones (Sales)** : pas de problème client reformulé à
  attaquer.
- **Flash (Product)** : pas de scope validé à attaquer (en
  attente PRD/Brief).
- **Batman (Ops)** : pas de procédure à supporter (pas de
  launch à absorber).
- **Cyborg (IT)** : pas de demande système (pas de feature
  à déployer).
- **Wonder Woman (Finance)** : pas de demande budget (pas de
  spend à allouer).
- **Green Lantern (People)** : pas de recrutement à faire
  (pas de mandat ouvert).
- **Aquaman (Legal)** : pas de prestation démarrée (pas de
  contrat à valider).

### NEEDS_SIGNAL → DORMANT

**Condition cumulative** : `b2-areas-dormants-doctrine.md`
pose 3 conditions :

1. Aucune ressource externe ne requiert sa doctrine.
2. Son DoD est vide pour le cycle courant.
3. Le captain a consigné l'état dans le journal Council.

**Distinction cruciale** : `NEEDS_SIGNAL` reste un état
**actif** — le captain **surveille** activement le signal
externe. `DORMANT` est un état **inactif** — le captain ne
produit plus rien.

La transition NEEDS_SIGNAL → DORMANT n'est **pas** automatique.
Elle nécessite la consigne formelle du captain (condition 3).

### DORMANT → READY (réveil)

**Déclencheur** : `b2-areas-dormants-doctrine.md` pose 3
déclencheurs canoniques de réveil :

1. **Signal B1** — un mandat B1 vise le domaine.
2. **Signal B3 pair** — un autre captain signale un besoin.
3. **Signal client** — un événement externe touche la
   doctrine du domaine.

Le réveil DORMANT → READY est **mécanique** (pas de débat
Council). Le captain consigne le réveil et reprend le
sprint.

### DORMANT → BLOCKED (transition rare)

**Condition** : un signal arrive mais le domaine est **bloqué**
par veto ou red flag, pas **dormant**.

C'est une transition rare mais possible : Aquaman dormant est
réveillé par un mandat Growth, mais le périmètre du mandat
touche un cas `BLOCKED_RISK` (par ex : clause de non-concurrence
non négociée). Aquaman passe **directement** DORMANT →
BLOCKED sans repasser par READY.

## Le cas-limite Superman — comment NEEDS_SIGNAL est distinct de DORMANT

`superman-dormance-active-posture.md` §« Le cas-limite »
documente explicitement la distinction :

- `NEEDS_SIGNAL` = Superman **produit encore** (surveillance
  marché, VoC, ICP updates).
- `DORMANT` = Superman **ne produit plus**, DoD vide.

Un Superman qui se déclare `DORMANT` sans être sorti de
`NEEDS_SIGNAL` rate la transition canonique. La séquence
correcte est :

```
READY (production) → NEEDS_SIGNAL (veille active, sans DoD)
   ↓ (consigne captain)
DORMANT (inactif total, DoD vide)
   ↓ (déclencheur B1/B3/client)
READY (production)
```

**Aucun raccourci** : un Superman READY peut sauter
directement à DORMANT si les 3 conditions sont remplies, mais
il ne peut pas sauter DORMANT → NEEDS_SIGNAL (le NEEDS_SIGNAL
est une veille active qui implique un signal externe **en
cours d'arrivée**, pas une attente passive).

## Les trois règles canoniques proposées par domaine

Chaque captain doit observer 3 règles pour tenir la doctrine
NEEDS_SIGNAL ↔ DORMANT :

### Règle 1 — La transition NEEDS_SIGNAL → DORMANT est consignée

Le packet mésoperpétuel porte **explicitement** la transition.
Pas de transition silencieuse. Le captain consigne dans le
journal Council `decision: dormant, domaine: <X>, motif: <Y>,
depuis: <date>`.

### Règle 2 — L'état DORMANT a un signal de réveil déclaré

Le captain dormant déclare ses **3 signaux de réveil** dans
le packet mésoperpétuel. Sans signaux déclarés, le Council ne
sait pas quand lever la dormance.

### Règle 3 — La transition DORMANT → READY ne crée pas d'auto-dispense

Un captain qui se réveille ne peut pas se remettre en
`NEEDS_SIGNAL` sans signal externe **réel** — il doit
accepter un mandat B1, un signal pair, ou un signal client.
La règle empêche le captain de s'auto-déclarer en veille
indéfiniment.

## Les 3 captain-needs-signal-types

Trois profils de NEEDS_SIGNAL selon le type de signal attendu :

### Type A — Signal amont (B1 mandate)

Superman Growth, Flash Product, Batman Ops. Le signal attendu
est un mandat B1. Sans mandat, le captain est en veille
active.

### Type B — Signal pair (B3 ou B2 cross-domaine)

Cyborg IT, Wonder Woman Finance, Green Lantern People. Le
signal attendu est une demande pair. Sans demande, le captain
est en veille active.

### Type C — Signal externe (client, marché, partenaire)

JohnJones Sales, Aquaman Legal. Le signal attendu est externe
au B2 Council — un client, un partenaire, un événement
règlementaire.

## Anti-pièges

- **NEEDS_SIGNAL → DORMANT par défaut.** Refusé — la
  transition nécessite la consigne du captain.
- **DORMANT sans signal de réveil déclaré.** Refusé par
  règle 2 — le captain dormant doit déclarer ses 3 signaux.
- **DORMANT → READY sans signal réel.** Refusé par règle 3 —
  le réveil nécessite un signal externe vérifiable.
- **DORMANT simultanément Superman + Aquaman.** Anomalie
  cycle, escalade B1 obligatoire (cf.
  `superman-dormance-active-posture.md` §« Anti-pièges »).
- **NEEDS_SIGNAL confondu avec DORMANT.** Refusé — la
  distinction actif/inactif est binaire.

## Liens

- [[b2-areas-dormants-doctrine]] — la doctrine canonique
- [[superman-dormance-active-posture]] — Superman tour 2
- [[eight-domain-avengers-wheel]] — 3 états Superman
- [[b2-council-cadence-and-chair]] — la revue hebdomadaire
- [[b2-council-arbitrage-rule]] — l'arbitrage Council

## Note de confiance

**Reconstruit, à moitié étayé.** Les 4 états proposés
(READY/NEEDS_SIGNAL/BLOCKED/DORMANT) sont **projetés** par
symétrie avec les 3 états Superman canoniques + l'état
DORMANT Aquaman triplet 35. La table 8-domaines × 4 états est
**projetée** par lecture critique de
`eight-domain-avengers-wheel.md` et de la doctrine b2-areas-dormants
— les états NEEDS_SIGNAL et DORMANT pour les 7 autres domaines
ne sont **pas cités** canoniquement ailleurs dans le corpus.
Les conditions de transition sont **reconstruites** par lecture
critique de `b2-areas-dormants-doctrine.md` + la pratique
documentée de Superman. Les 3 règles canoniques sont
**projetées** par lecture critique de la doctrine D4
append-only + pratique Superman tour 2. Les 3
captain-needs-signal-types sont **reconstruits** par typologie
des gates B2 (`eight-domain-avengers-wheel.md`). Le cas-limite
DORMANT → BLOCKED est **projeté** par lecture critique de la
doctrine du triplet 35 et du triplet 36 (Aquaman dormant
triggered by premier contrat signé).

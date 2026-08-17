---
type: Concept
title: Beth & Morty — les safety gatekeepers L1
description: Beth (HALT veto authority sur LD03/LD04 + life signals) et Morty (Focus Gatekeeper A1) sont les gatekeepers L1 qui peuvent geler n'importe quel Jerry ou Summer's Verse. L'escalation canonique : B3 → B2 → B1 → gatekeepers (Rick/Morty) → A0.
tags: [beth, morty, halt-veto, safety, gatekeepers, life-os, l1, escalation]
generated: { by: minimax-m3, at: 2026-08-17T22:10:00Z }
verified:
  - { by: process:extraction-areas, at: 2026-08-17T22:10:00Z }
sources:
  - id: bio-area-standard
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/AREA_STANDARD.md"
    title: J02 — Jerry Bio Area Standard — HARD SAFETY CONSTRAINT LAYER
    last_modified: 2026-05-21
  - id: alignment
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/JERRY_WHEEL_ALIGNMENT_MINDSET_VALUES.md"
    title: Jerry Wheel Alignment — Mindset, Valeurs & l'Âme des Areas
    last_modified: 2026-06-04
  - id: spock-spec
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/A3_Spock_Areas_Spec.md"
    title: A3 Spock Spec - Areas
    last_modified: 2026-06-21
okf_version: "0.2"
---

# Beth & Morty — les safety gatekeepers L1

L'escalation canonique de L2 Business Pulse se termine à **A0 Amadeus**, mais avant A0 il y a deux gatekeepers L1 qui peuvent geler n'importe quelle action : **Beth** (HALT veto authority) et **Morty** (Focus Gatekeeper). Sans eux, l'escalation court-circuit les safety layers et A0 devient le seul rempart — intenable.

## L'escalation canonique

`B1_DECISION_CHARTER.md` §4 fixe la chaîne :

> *B3 → (peer-unblock first) → B2 owner → B1 (Jerry/Summer) → B1 gatekeepers (Rick/Morty) → A0 Amadeus.*

Les **B1 gatekeepers** sont Rick et Morty au niveau L1. Rick porte une autorité d'arbitrage technique/stratégique ; Morty porte le **Focus Gatekeeper** A1 role.

`A3_Spock_Areas_Spec.md` §« Spock = A3 Areas canon (plan §3.2) » confirme le mapping patché 2026-06-21 :

> *Owner A1 : Morty (Focus Gatekeeper)*
> *Parent A2 : Computer (USS Enterprise)*
> *A3 Spock*

Morty est donc l'A1 des Areas. C'est lui qui définit la Law de la couche Areas (où Spock opère).

## Beth — HALT veto authority

`J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/AREA_STANDARD.md` §1.1 pose Beth explicitement :

> *Beth HALT veto escalation and enforcement protocol.*

Beth est l'autorité qui dit **STOP**. Elle n'opère pas dans le pipeline normal ; elle **interrompt** quand les signaux vitaux/cognitifs passent en RED.

Quatre triggers HARD HALT depuis `AREA_STANDARD.md` §4 :

1. **LD03 RED** : sleep <5h, HRV <45ms, exercise 0×/week → Beth HALT veto enforced, FULL STOP tous Jerry.
2. **LD03 + LD04 ORANGE simultanément** → Beth HALT veto automatic.
3. **Beth reçoit notification** : « LD03 substrate compromised — business expansion suspended ».
4. **Beth reçoit activity log dans les 24h** après un RED event.

Et le **chain trigger** :

> *LD03 (santé) dégradée → LD04 (cognition) dégradée → Beth HALT veto → tous les Jerry freeze.*
> *Aucun Jerry (même Business) ne progresse en violant le canon de valeurs §1.*

(`JERRY_WHEEL_ALIGNMENT_MINDSET_VALUES.md` §3 — la hard safety law)

## Le HALT est défini comme suit

`AREA_STANDARD.md` §4 (J02) :

> *HALT = Hungry, Angry, Lonely, Tired — but for Jerry Bio, the operative HALT is : H ealth, A daptation capacity, L earning threshold, T oxic load.*

Beth applique ce HALT élargi sur les signaux vitaux/cognitifs.

## L'escalation vers Beth — quand

| Signal | Escalation |
|---|---|
| LD03 ORANGE persistant >72h | Beth HALT veto TRIGGERED |
| Premier LD03 RED | Beth reçoit automated notification |
| LD03 ORANGE + LD04 ORANGE simultanément | Beth HALT veto AUTOMATIC |
| Beth demande root cause analysis | Activity log soumis en 24h |

Beth n'est **pas** dans le pipeline routage normal. Elle est **l'interrupteur**. Si Life OS charge trop, ou si LD03/LD04 dégradent, elle gèle.

## Morty — Focus Gatekeeper A1

`A3_Spock_Areas_Spec.md` §« Spock = A3 Areas canon (plan §3.2) » patch :

> *Owner A1 : Morty (Focus Gatekeeper)*

Morty est l'**A1** au-dessus de Spock (A3). C'est lui qui :

- Définit la **Law** de la couche Areas.
- Décide **quelles Areas** sont actives (focus : « pas trop d'Areas ouvertes en même temps »).
- Fait le **gate** sur l'intention Areas — sans son OK, Spock n'incube pas.

`A1_Jerry_Areas_Spec.md` confirme côté macro :

> *Jerry proposals become executable only after Cerritos clarifies and Picard opens or updates a Summer's Verse.*

Le Cerritos clarifier, c'est le Focus Gatekeeper en action : il clarifie avant que l'idée devienne action.

## La chaîne d'escalation Safety L1 ↔ L2

L1 Safety (Beth + Morty) → L2 Business (Jerry + Summer) → L2 Operational (B3) → L2 Domain (B2) → L2 Direction (B1) → L1 Authority (Rick) → L0 Pilot (A0 Amadeus).

Quand un signal Life OS arrive :

1. **Beth évalue** le signal (LD03/LD04/finance/family).
2. Si HALT nécessaire, **Beth émet le veto**.
3. Le veto **gèle** l'expansion de tous les Jerry.
4. Les Jerry **ne peuvent pas** outrepasser Beth — c'est un stop dur.

Quand un signal Business arrive :

1. **B3 signale** un blocker au B2 owner.
2. **B2 owner** escalade à B1 si hors mandat.
3. **B1 (Jerry/Summer)** escalade à Rick/Morty si hors risk appetite / North Star.
4. **Rick/Morty** arbitrent ; si Life OS impact, **Beth** est consultée.
5. **A0 Amadeus** tranche en dernier ressort.

## L'invariant

`Jerry_Areas_README.md` §Doctrine :

> *Beth can halt all expansion if Life OS load, health, cognition, or finance signals turn red.*
> *Every Jerry action must eventually map to an artifact, scorecard, or explicit rejection.*

Beth est la garantie de survie du système. Sans elle, l'expansion dévore le substrat. Avec elle, le substrat a une voix.

## Le risque spécifique

Confondre Beth et A0 est un piège courant. Symptôme : on escalade directement à A0 sans passer par Beth. Parade : tester le signal — *« est-ce un signal vital/cognitif/finance ou est-ce un signal stratégique ? »* Si vital/cognitif/finance → Beth d'abord. Si stratégique → Rick/Morty, puis A0.

Beth qui ne reçoit jamais de signal est aussi suspect : soit les seuils sont trop permissifs, soit les notifications sont cassées. La cadence normale est *« Beth reçoit 1–5 notifications par trimestre »*. Zéro = système silencieusement défaillant.
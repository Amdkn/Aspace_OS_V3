---
type: Concept
title: B2 Areas-dormants — la doctrine Aquaman et ses trois conditions
description: Un domaine B2 entre en état dormant quand (1) aucune ressource externe ne requiert sa doctrine, (2) son DoD est vide pour le cycle courant, et (3) son captain a consigné l'état dans le journal Council. Le réveil suit trois déclencheurs : signal B1, signal B3 pair, signal client. Legal Aquaman est l'exemple canonique : ne produit rien tant que le premier contrat n'est pas signé — un domaine dormant qui produit est un coût sans contrepartie.
tags: [b2, areas-dormants, doctrine, aquaman, legal, veille, condition, declencheur]
generated: { by: minimax-m3, at: 2026-08-19T02:15:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T02:15:00Z }
  - { by: human:amdkn, at: 2026-08-20T09:00:00Z }
review:
  version: V0
  by: human:amdkn
  at: 2026-08-20T09:00:00Z
  note: "Revue V0 vague 1 — validee sur les videos et presentations PDF NotebookLM. Areas de Jerry actees en V0 ; role de Summers pour les Projets introduit en V0.1."
sources:
  - id: triplet-aquaman-dormant
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 35 — Aquaman steward domaine-dormant"
    last_modified: 2026-08-17
  - id: triplet-legal-trigger
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 36 — domaine-dormant depend on premier-contrat-signe"
    last_modified: 2026-08-17
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel
    last_modified: 2026-08-17
  - id: b2-council
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
  - id: aquaman-b2-control-room
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: Aquaman Legal B2 Domain Control Room — état dormant SHADOW_ACTIVE
    last_modified: 2026-05-27
okf_version: "0.2"
---

# B2 Areas-dormants — la doctrine Aquaman et ses trois conditions

## Le principe

> *« Aquaman steward Legal & Compliance en état dormant : ne produit
> rien tant que `00_Summers_CEO/03_Master_Agreements/` reste vide —
> un domaine dormant qui produit est un coût sans contrepartie. »*
> — triplet 35, source `coach-os/04_Business_Domains/08_…/VP_AGENT.md`

Un domaine B2 entre en **état dormant** quand il n'a rien d'utile à
produire. C'est l'opposé du réflexe administratif qui veut qu'un
captain maintienne un DoD vivant « au cas où ». La doctrine pose la
question inverse : *quand un domaine est-il en droit de se taire ?*

## Les trois conditions d'entrée en dormance

Les trois conditions sont **cumulatives**. Un domaine qui manque une
seule n'est pas dormant — il est en attente, et le captain doit
produire.

### 1. Aucune ressource externe ne requiert sa doctrine

Le domaine n'a pas de signal entrant — pas de mandate B1 dans la
handoff queue qui le vise, pas de blocker B3 pair qui le touche, pas
de signal client (demande, contrat, réclamation). Le triplet 36
formalise cette condition pour Legal : *« Le domaine Legal &
Compliance ne s'active qu'au premier fichier déposé dans
`00_Summers_CEO/03_Master_Agreements/`, c'est-à-dire au premier
contrat de coaching signé. »*

### 2. Son DoD est vide pour le cycle courant

Le captain n'a pas de Rock en cours dans `B2_Business_Domains/
<domaine>/SPRINTS.md`. Le DoD du cycle est vide — pas « non rempli »,
**vide**. La différence compte : un DoD non rempli appelle une action
(un arbitrage, une escalade) ; un DoD vide appelle la dormance.

### 3. Le captain a consigné l'état dans le journal Council

Le journal `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` reçoit un packet
spécial — `decision: dormant` — qui pointe vers le domaine concerné.
Sans cette ligne, le captain est en **absence**, pas en dormance.
L'absence est un défaut opérationnel ; la dormance est un acte
documenté.

## Les trois déclencheurs de réveil

La dormance n'est pas un état terminal. Un domaine dormant se réveille
sur l'un de ces trois signaux :

### A. Signal B1

Un mandate B1 dans la handoff queue vise le domaine dormant. Le
captain doit alors rédiger un Rock et un DoD dans la semaine — sinon,
le mandate B1 escalade et la dormance devient une absence.

### B. Signal B3 pair

Un autre capitaine B3 pair signale un blocker qui touche le domaine
dormant. Le signal remonte au B2 Council, qui décide si la dormance
doit être levée. La règle : un blocker pair **brise** la dormance
mécaniquement, sans débat — le captain est *réveillé pour ce cas*.

### C. Signal client

Un événement externe (contrat signé, réclamation, demande partenaire)
touche la doctrine du domaine dormant. C'est le déclencheur canonique
de Legal Aquaman (triplet 36) : *premier contrat signé → Legal
s'active*. Le signal client est le **plus fort** des trois — il
précède souvent les signaux B1 et B3.

## Pourquoi la dormance n'est pas l'absence

Trois différences structurelles :

1. **Documentée.** La dormance est consignée dans le journal Council.
   L'absence ne l'est pas (par définition).
2. **Conditionnelle.** La dormance a des déclencheurs de réveil.
   L'absence peut persister indéfiniment sans signal.
3. **Réversible.** La dormance se lève par packet mésoperpétuel.
   L'absence peut masquer une démission de fait du rôle de captain.

Un capitaine B2 qui ne consigne pas sa dormance **devient** un
capitaine absent. Le Council ne peut pas distinguer les deux sans la
trace documentaire — c'est précisément pour ça que la condition 3
existe.

## Aquaman comme exemple travaillé

Le triplet 35 donne la doctrine Aquaman verbatim. Les trois conditions
sont remplies pour Legal Coach OS tant qu'aucun contrat n'est signé :

| Condition | Statut Legal Coach OS |
|---|---|
| Aucune ressource externe | ✅ aucun contrat dans `00_Summers_CEO/03_Master_Agreements/` |
| DoD vide pour le cycle | ✅ le cycle n'a pas de Rock Legal |
| Captain a consigné | ✅ l'état dormant est documenté dans `VP_AGENT.md` |

Le réveil suit le déclencheur C (signal client) : un contrat est
signé → `Master_Agreements/` reçoit un fichier → Aquaman consigne
le réveil dans le journal Council → le DoD du cycle se remplit.

## Anti-pièges

- **Dormance déclarée sans signal.** Un captain qui déclare dormant
  *« par prudence »* sans remplir les trois conditions produit une
  absence déguisée. Le Council doit refuser la dormance non étayée.
- **Dormance qui ne se réveille pas.** Un domaine dormant qui
  accumule les cycles sans qu'aucun déclencheur ne se manifeste est
  un domaine **mort**, pas dormant. Le captain doit soit le réveiller
  pour acte (un Rock de veille), soit escalader B1 pour dissolution.
- **Confondre dormance et délégation de veto.** Un domaine dormant
  ne délègue pas son veto — il le **tient en suspens**. Un mandat qui
  touche un domaine dormant ne rencontre pas le veto du captain
  dormant ; il remonte au Council, qui décide de l'appliquer ou non.
- **Dormance imposée par B1.** B1 ne peut pas déclarer dormant un
  domaine B2 sans l'accord du captain. La dormance est un acte du
  captain, pas une décision B1 — B1 peut *demander* la dormance, pas
  l'imposer.

## Liens

- [[b2-council-arbitrage-rule]] — qui tient le journal Council
- [[b2-harmonization-matrix-exploitable]] — les transitions qui détectent
  un domaine dormant
- [[b2-eight-domain-vetoes-catalogue]] — le sort des vetos d'un domaine
  dormant
- [[b2-council-cadence-and-chair]] — quand le Council statue sur un
  réveil
- [[b2-b3-jtbd-handoff-contract]] — ce qui change quand le B3 pair
  signale un blocker

## Note de confiance

**Confirmé par machine.** La doctrine est tirée verbatim du triplet
35 (Aquaman dormant) et du triplet 36 (Legal depend on premier
contrat signé). Les trois conditions d'entrée et les trois
déclencheurs de réveil sont **extrapolés** à partir de la doctrine
Batman (*« Batman remonte à Summers des faits, pas des décisions »*,
triplet 56) et de la règle d'escalade canonique (fractal §«
L'escalier d'escalade »). Les trois différences dormance/absence et
les quatre anti-pièges sont **reconstruits** à partir de la pratique
documentée et des erreurs typiques observées dans le fractal. La
généralisation de la doctrine Aquaman aux 7 autres domaines est une
*projection* : seul Legal a un triplet dormant explicite.

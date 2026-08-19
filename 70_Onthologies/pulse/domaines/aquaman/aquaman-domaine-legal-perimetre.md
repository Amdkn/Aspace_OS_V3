---
type: Concept
title: Aquaman — Domaine Legal & Compliance, périmètre et état dormant
description: Aquaman couvre compliance, contract risk, privacy, IP, claims, terms, permissions et defensibility. Le domaine est dormant tant que 00_Summers_CEO/03_Master_Agreements/ reste vide — un domaine dormant qui produit est un coût sans contrepartie.
tags: [b2, legal, aquaman, domaine, dormant, perimetre, compliance]
generated: { by: minimax-m3, at: 2026-08-19T03:30:00Z }
verified:
  - { by: process:lecture-canon-aquaman, at: 2026-08-19T03:30:00Z }
sources:
  - id: legal-readme
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/README.md"
    title: 08 Legal - Aquaman / Eternals (Role, Gate, Blocking Authority)
    last_modified: 2026-05-25
  - id: legal-control-room
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: Legal Control Room — Aquaman owner, Eternals swarm
    last_modified: 2026-05-27
  - id: triplet-35
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 35 — Aquaman steward domaine dormant"
    last_modified: 2026-08-17
  - id: triplet-36
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 36 — domaine Legal dependsOn premier contrat signé"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Aquaman — Domaine Legal & Compliance

## Ce que couvre le domaine

Sept surfaces, tirées verbatim du `README.md` du dossier OMK
(`08_Legal_Aquaman_Eternals/README.md` §Role) :

1. **Compliance** — alignement aux régulations sectorielles (RGPD, sector rules).
2. **Contract risk** — exposition liée aux engagements clients et fournisseurs.
3. **Privacy** — gestion des données personnelles et frontières de traitement.
4. **IP** — propriété intellectuelle, licences, contrefaçon.
5. **Claims** — toute affirmation publique susceptible d'engager la responsabilité.
6. **Terms** — conditions générales, conditions d'utilisation, contrats types.
7. **Permissions & defensibility** — capacité à défendre une position (audit, contentieux, incident).

## Ce qui n'est PAS dans le périmètre Aquaman

Trois zones sont explicitement hors-périmètre, identifiées par
différence avec les autres capitaines B2 :

- **Exécution de la conformité** (audits terrain, KYC, contract management ops).
  C'est Batman (Ops) qui opère ; Aquaman définit le cadre.
- **Budgétisation des risques** (assurances, provisions, escrow). C'est
  Wonder Woman (Finance).
- **Implémentation technique de la privacy** (chiffrement, IAM, retention).
  C'est Cyborg (IT/R&D).

Cette frontière est ce qui permet à Aquaman d'être **Consulted** sur
les pair-checks canoniques et non **Accountable** : il cadre, il n'opère
pas (cf. [[b2-pair-check-raci-by-rank]]).

## L'état dormant — une singularité Aquaman

Triplet 35 (verbe `stewards`, source `04_Business_Domains/.../Aquaman_Eternals/VP_AGENT.md`) :
*« Aquaman steward Legal & Compliance en état dormant : ne produit
rien tant que `00_Summers_CEO/03_Master_Agreements/` reste vide — un
domaine dormant qui produit est un coût sans contrepartie. »*

Triplet 36 (verbe `dependsOn`, source `coach-os/README.md`) :
*« Le domaine Legal & Compliance ne s'active qu'au premier fichier
déposé dans `00_Summers_CEO/03_Master_Agreements/`, c'est-à-dire au
premier contrat de coaching signé. »*

Trois conséquences opérationnelles :

1. **Le domaine ne s'auto-déclenche pas.** Pas de Rock Legal sans
   matière (un contrat à valider, une claim à publier, une IP à
   défendre).
2. **Un Aquaman qui produit avant le premier contrat est un coût pur.**
   Aucune contrepartie : aucun livrable n'a de consumer.
3. **L'état dormant n'est pas l'absence.** Aquaman reste B2 captain, le
   squad Eternals reste catalogué, le veto catalogue reste valide — seul
   le *flow de production* est gelé.

## Activation — le seuil exact

Le seuil est **le premier fichier dans `03_Master_Agreements/`**, pas
le premier paiement, pas le premier client, pas le premier coach.
Tant que ce dossier est vide, Aquaman :

- ne produit pas de `SPRINTS.md` Legal ;
- n'ouvre pas de JTBD vers les Eternals ;
- **tient** son veto catalogue si un pair-check touche Legal, mais
  **ne pousse pas** d'arbitrage proactif.

Conséquence : un projet Coach OS en phase pré-Master Agreement qui
voudrait publier une claim publique ou onboarder un client doit
escalader à B1 pour amender le seuil d'activation, ou Aquaman opposera
son veto sur la prestation (cf. [[aquaman-veto-engagement-sans-perimetre]]).

## Le rôle du B2 owner

`00_B2_DOMAIN_CONTROL_ROOM.md` pose le rôle canonique d'Aquaman :

> *« Transform B1 direction into domain Rocks, Definition of Done
> packets, and JTBD prompts that let the B3 swarm execute without
> step-by-step babysitting. »*

Pour Legal, ce rôle est **cadreur** : Aquaman transforme l'intention B1
en un Rock qui pose un cadre (par exemple *« aucun livrable public ne
sort sans claim privacy review »*), pas en une exécution. La squad
Eternals est Responsible, pas Aquaman.

## Anti-pièges

- **Confondre dormant et absent.** Un Aquaman dormant reste B2 captain.
  Le veto catalogue tient. Les pair-checks #7 et #8 restent Consulted.
  La différence est dans l'*output* (pas de `SPRINTS.md`), pas dans
  le *statu*.
- **Forcer l'activation par un Rock inventé.** Un Rock Legal sans
  Master Agreement à traiter est une fiction. Aquaman steward un état
  dormant — l'amender sans matière, c'est trahir la doctrine.
- **Croire que la compliance est décorative.** `README.md`
  §Operating Rule : *« This domain is not decorative. If this README
  has no gate status for the active release, the project remains
  PRODUCT_ONLY_PROTOTYPE. »*

## Liens

- [[b2-eight-domain-vetoes-catalogue]] — le veto engagement-sans-périmètre
- [[b2-pair-check-raci-by-rank]] — les pair-checks #7 et #8 où Aquaman est Consulted
- [[aquaman-veto-engagement-sans-perimetre]] — quand et comment le veto se déclenche
- [[aquaman-gates-et-pair-checks]] — les trois gates émis par le domaine
- [[aquaman-couplages-invisibles]] — qui dépend d'Aquaman et de qui il dépend
- [[fifty-three-b3-agent-roster]] — la squad Eternals (~10 selon triplet 22, ~7 selon dossier OMK)

## Note de confiance

**Confirmé par machine.** Périmètre (7 surfaces) tiré verbatim de
`08_Legal_Aquaman_Eternals/README.md` §Role. État dormant cité verbatim
des triplets 35 et 36. Rôle B2 owner cité verbatim de
`00_B2_DOMAIN_CONTROL_ROOM.md`. Le seuil d'activation (« premier
fichier dans `03_Master_Agreements/` ») est cité verbatim. La tension
sur l'effectif Eternals (10 vs 4 vs ~7) est **non résolue** ici —
reportée au rapport.

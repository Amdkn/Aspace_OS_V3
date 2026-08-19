---
type: Concept
title: People — paquets JTBD émis et reçus, squad X-Men (8)
description: People émet des paquets JTBD vers B3 X-Men (recrutement humain et agent, gouvernance skills L0). People reçoit des paquets JTBD des autres domaines B2 quand un mandat doit être assigné ou qu'un owner doit être trouvé. La squad X-Men compte 8 agents (ProfessorX, Cyclops, JeanGrey, Wolverine, Storm, Beast, Nightcrawler, Rogue) — pas 7 comme les autres squads dans le corpus. La composition X-Men est asymétrique : deux agents tiennent les deux canaux (ProfessorX / Beast), les six autres portent des mandats transverses ou de soutien.
tags: [people, green-lantern, x-men, jtbd, b3, recrutement, squad]
generated: { by: minimax-m3, at: 2026-08-19T04:20:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T04:20:00Z }
sources:
  - id: triplet-15-xmen-8
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 15 — X-Men 8 techniciens (ProfessorX, Cyclops, JeanGrey, Wolverine, Storm, Beast, Nightcrawler, Rogue)"
    last_modified: 2026-08-17
  - id: triplet-33-professorx
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 33 — ProfessorX tient le recruiting"
    last_modified: 2026-08-17
  - id: triplet-34-beast
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 34 — Beast tient le TechRecruiting"
    last_modified: 2026-08-17
  - id: triplet-37-55-forge
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplets 37 + 55 — Green Lantern sollicite Bill L0.2 Forge pour skills L0"
    last_modified: 2026-08-17
  - id: roster-b3-53
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/fifty-three-b3-agent-roster.md"
    title: "53 B3 Agent Roster — X-Men ~7 agents (estimation)"
    last_modified: 2026-08-17
  - id: b2-b3-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: "B2 → B3 contract — quand une décision mésoperpétuelle devient un JTBD packet"
    last_modified: 2026-08-19
okf_version: "0.2"
---

# People — paquets JTBD émis et reçus, squad X-Men (8)

## La squad X-Men : 8 agents (pas 7)

**Fait vérifié.** Le triplet 15 cite verbatim :
> *« Green Lantern (VP B2 domaine 1 — RH & Méta Gouvernance) commande le
> squad X-Men (8 techniciens : ProfessorX, Cyclops, JeanGrey, Wolverine,
> Storm, Beast, Nightcrawler, Rogue). »*

Cette composition **contredit** l'estimation `fifty-three-b3-agent-roster.md`
qui place X-Men à **~7 agents**. Ownerbook T1 OMK attend *« ≥ 7 agents
par squad »* (DoD-1), ce qui est satisfait par 8 — mais le compte exact
peut diverger d'un dossier à l'autre.

**Composition X-Men :**

| Agent | Rôle canon (triplet) |
|---|---|
| **ProfessorX** | recruiting général — sourcing, lecture profils, décision d'entrée (triplet 33) |
| **Cyclops** | à préciser — squad leadership / coordination |
| **JeanGrey** | à préciser — psychométrie / lecture de signaux |
| **Wolverine** | à préciser — endurance / récupération |
| **Storm** | à préciser — environnement / contexte |
| **Beast** | TechRecruiting — recrutement technique et agentique, compétence réelle (triplet 34) |
| **Nightcrawler** | à préciser — mobilité / transition |
| **Rogue** | à préciser — absorption / délégation |

**Note de confiance.** Les rôles de ProfessorX et Beast sont **cités
verbatim** (triplets 33 et 34). Les six autres rôles sont **projetés**
depuis l'univers Marvel X-Men — pas cités dans le corpus canon. Le
brief demande des concepts sur le **domaine**, pas sur la liste Marvel
— ces rôles Marvel sont indicatifs, pas opérationnels.

## Paquets JTBD émis par People vers B3 X-Men

### Type 1 — Recrutement humain (canal ProfessorX)

**Déclencheur.** Un domaine B2 a un poste vacant, mandat complet
(rôle + horizon + critère de sortie), sponsor B2 identifié.

**Format attendu.** `B3-JTBD-YYYY-NN` avec :
- `source_meso_decision` : un packet mésoperpétuel Council ou un
  arbitrage People interne.
- `contract_signed.b2_sponsor` : captain du domaine d'accueil.
- `contract_signed.b3_squad_lead` : ProfessorX.
- `cadre.duree` : cycle de recherche (typiquement 4-8 semaines).
- `dod_bornee` : profil trouvé + entrée effective + onboarding 30j.

**Preuves par forme.** Capture (CV signé), témoignage (référence prise),
log (entrée dans le roster du domaine).

### Type 2 — Recrutement agent (canal Beast)

**Déclencheur.** Un domaine B2 a besoin d'un agent B3 ou d'un agent
générique, mandat complet, sponsor B2 identifié, **skills L0 confirmés**.

**Format attendu.** Identique au Type 1, avec :
- `contract_signed.b3_squad_lead` : Beast.
- `dod_bornee` : agent activé + skills L0 vérifiés + tests passés.
- `proof_expected.forme` : log (activation), capture (skill tree),
  métrique (premier livrable).

**Couplage Forge.** Triplets 37 et 55 : Green Lantern sollicite Bill
(L0.2 Forge) pour confirmer la disponibilité des skills L0. C'est un
canal **défini, pas improvisé**. Le JTBD agent peut être bloqué si
Forge ne confirme pas les skills — c'est un cas de veto People implicite.

### Type 3 — Gouvernance skills L0 (canal Green Lantern ↔ Bill Forge)

**Déclencheur.** Un recrutement agent ou une évolution de scope d'un
agent existant nécessite un skill L0 nouveau ou mis à jour.

**Format attendu.** Packet **bilatéral** People ↔ Bill (L0.2 Forge), pas
un JTBD B3 standard. C'est un canal de **méta-gouvernance** qui sort du
cadre B2 → B3 usuel. Voir `green-lantern-people-perimetre-frontieres.md`
§« Le cas limite : Méta Gouvernance ».

**Note** : la nature exacte de ce packet n'est pas posée dans le canon
V4 — Coach OS la cite, le canon V4 ne la valide pas.

## Paquets JTBD reçus par People depuis les autres domaines B2

### Type A — Assignation manquante (`NEEDS_OWNER`)

**Source.** Un captain B2 (Batman Ops, Superman Growth, etc.) détecte
qu'un poste dans son domaine est vacant ou surchargé.

**Effet.** People ouvre un arbitrage interne — soit lancer un
recrutement (Type 1 ou Type 2 ci-dessus), soit signaler une `DLQ` (pas
d'owner possible dans le cycle).

### Type B — Succession d'owner

**Source.** Un captain B2 notifie qu'un de ses owners quitte (fin de
mandat, démission, rotation). Le captain ne peut pas toujours remplacer
lui-même — il remonte à People.

**Effet.** People tient la carte de charge et arbitre (en C, pas en A —
cf. `green-lantern-people-raci-transverse-jamais-A`). Le captain du
domaine impacté décide qui succède.

### Type C — Demande de mandat

**Source.** Un B3 squad (pas un captain B2) signale qu'il a besoin d'un
nouvel agent pour compléter une squad. Le B3 ne mandate pas lui-même
(triplet 41 — B3 a l'interdit de combler un trou du sprint). Il remonte
à son captain B2, qui relaie à People si nécessaire.

**Effet.** People lance un recrutement (Type 2 — agent).

## Le contrat B2 → B3 vu de People

D'après `b2-b3-jtbd-handoff-contract.md` §« Le rôle du captain B2
sponsor » :

- **People signe conjointement** avec le B3 squad lead (ProfessorX ou
  Beast). Double signature dans le JTBD packet.
- **People voit les lead indicators** en temps réel — pas seulement à
  la livraison.
- **People décide de l'escalade** au Council si la dérive dépasse le
  seuil.

Le rôle de People est **atypique** dans ce contrat : People est **à la
fois captain B2 source ET sponsor B2 aval** dans certains cas (ex :
People mandate un agent qui atterrit dans un autre domaine B2 — People
est source du recrutement, le captain d'accueil est sponsor de
l'utilisation). Cette double casquette n'est pas explicitée dans le
canon — c'est une **projection** depuis la pratique du veto People.

## Anti-pièges

- **Confondre ProfessorX et Beast** — le premier recrute des humains,
  le second des agents. Les deux grilles de mandat sont différentes
  (cf. `green-lantern-people-veto-recrutement-sans-mandat`).
- **B3 qui mandate lui-même** — triplet 41 : B3 a l'interdit de combler
  un trou. Il signale à son captain B2, qui relaie à People. People
  n'accepte pas un JTBD packet dont la source est B3 seul.
- **Squad X-Men à 7 vs 8** — la divergence entre le triplet 15 (8) et
  le roster canonique (~7) est non arbitrée. Le Council doit trancher.
- **Méta Gouvernance hors JTBD** — le canal Green Lantern ↔ Bill Forge
  n'est pas un JTBD standard. Si People traite une sollicitation Forge
  comme un JTBD B3, la chaîne se casse.

## Liens

- [[green-lantern-people-perimetre-frontieres]] — ce que People mandate
- [[green-lantern-people-veto-recrutement-sans-mandat]] — ce que le
  mandat doit contenir
- [[green-lantern-people-gats-assigned-needs-owner-dlq]] — les gates
  qui consomment ces JTBD
- [[green-lantern-people-raci-transverse-jamais-A]] — pourquoi People
  est C, pas A, sur ces paquets
- [[b2-b3-jtbd-handoff-contract]] — le contrat bilatéral B2 → B3

## Note de confiance

**Confirmé par machine, à moitié reconstruit.** Le triplet 15 (X-Men 8
agents) est **cité verbatim**. Les triplets 33 et 34 (ProfessorX /
Beast) sont **cités verbatim**. Les triplets 37 et 55 (canal Bill
Forge) sont **cités verbatim**. Les rôles des 6 autres X-Men agents
sont **projetés** depuis l'univers Marvel — non canoniques. La
divergence X-Men 7 vs 8 agents est **observée** (triplet 15 vs
fifty-three-b3-agent-roster), pas tranchée. Le Type 3 (méta
gouvernance) est cité dans Coach OS mais **non validé** par le canon
V4 — sa nature exacte est projetée.
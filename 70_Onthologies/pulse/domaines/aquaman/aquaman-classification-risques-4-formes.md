---
type: Concept
title: Aquaman — classification des risques juridiques en 4 formes et mapping gate
description: Le périmètre Legal Aquaman ([[aquaman-domaine-legal-perimetre]] §7 surfaces) se réduit opérationnellement à **4 classes de risque** : privacy/data, claim safety, IP/propriété intellectuelle, contract/limite de périmètre. Chacune a un émetteur amont canonique, un seuil LEGAL_READY/NEEDS_REVIEW/BLOCKED_RISK distinct, et un JTBD packet type ([[aquaman-jtbd-emit-receive]]). Cette taxonomie permet à un B3 squad (Eternals) de router une demande entrante vers la bonne Forme sans passer par Aquaman pour le tri initial.
tags: [b2, aquaman, legal, classification, risque, gate, privacy, claim, ip, contract]
generated: { by: minimax-m3, at: 2026-08-19T05:50:00Z }
verified:
  - { by: process:lecture-canon-aquaman-tour-4, at: 2026-08-19T05:50:00Z }
sources:
  - id: aquaman-perimetre
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-domaine-legal-perimetre.md"
    title: Aquaman domaine Legal — périmètre et 7 surfaces
    last_modified: 2026-08-19
  - id: aquaman-jtbd
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-jtbd-emit-receive.md"
    title: Aquaman catalogue JTBD émis et reçus (4 formes émises)
    last_modified: 2026-08-19
  - id: aquaman-gates
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-gates-et-pair-checks.md"
    title: Aquaman gates et pair-checks
    last_modified: 2026-08-19
  - id: aquaman-couplages
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-couplages-invisibles.md"
    title: Aquaman couplages invisibles (Cyborg privacy, Superman claim, Flash IP, JohnJones contract)
    last_modified: 2026-08-19
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: "Eight Domain Avengers Wheel — gates READY/NEEDS_REVIEW/BLOCKED_RISK (Legal, ligne 47)"
    last_modified: 2026-08-17
  - id: omk-legal-readme
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/README.md"
    title: 08 Legal - Aquaman / Eternals — Required Input From Product
    last_modified: 2026-05-25
okf_version: "0.2"
---

# Aquaman — classification des risques juridiques en 4 formes et mapping gate

## Pourquoi 4 formes, pas 7 surfaces

Le périmètre Aquaman énumère **7 surfaces** (claims, privacy, IP, contract templates,
employment/NDA, defensibility, regulation sectorielle — cf.
[[aquaman-domaine-legal-perimetre]] §Que couvre-t-il). Mais **opérationnellement**, les
demandes qui arrivent à Aquaman se répartissent en **4 classes de risque** qui
mutent la réponse gate :

1. **Privacy / data protection** — privacy review côté implémentation IT.
2. **Claim safety / defensibility** — ce que Superman publie ou ce qu'un Sales promet.
3. **IP / propriété intellectuelle** — qui possède quoi avant démarrage.
4. **Contract / périmètre de livrable** — clauses, périmètre écrit, propriété du livrable.

Les 3 autres surfaces (employment/NDA, regulation sectorielle, defensibility binder)
sont **dérivées** : employment/NDA est un cas particulier de privacy + contract ;
regulation sectorielle est un cas particulier de privacy ou claim selon le secteur ;
defensibility binder est un cas particulier déclenché par incident (cf.
[[aquaman-defensibility-triple-signature]]).

## Les 4 classes — tableau opérationnel

| Classe | Émetteur amont canonique | Forme JTBD émise | Seuil LEGAL_READY | Seuil NEEDS_REVIEW | Seuil BLOCKED_RISK |
|---|---|---|---|---|---|
| **1. Privacy / data** | Cyborg (IT) — privacy impl input | Forme 1 (privacy review) | DPI réalisée, retention chiffrée, IAM documenté | DPI en cours, retention à clarifier | Données non chiffrées at rest, ou vendor sans DPA |
| **2. Claim safety** | Superman (Growth) — claim draft | Forme 2 (claim safety) | Claim reformulée <=24h après `BLOCKED_RISK` | Claim en cours de reformulation | Claim litigieuse (terme absolu non démontrable) |
| **3. IP / propriété** | Flash (Product) — feature spec | Forme 3 (contract template) + clauses IP | IP assignée, contrats tiers en règle | IP partiellement assignée, contrats à signer | IP non déclarée, ou contrefaçon connue non couverte |
| **4. Contract / périmètre** | JohnJones (Sales) — deal structure | Forme 3 (contract template) + clauses limitatives | Périmètre écrit, propriété du livrable signée | Périmètre en négociation | Pas de périmètre écrit ou livrable sans propriétaire (veto canonique) |

**Source des seuils** : les colonnes `LEGAL_READY/NEEDS_REVIEW/BLOCKED_RISK` sont
posées verbatim par [[eight-domain-avengers-wheel]] ligne 47. Les **détails par classe**
sont extrapolés depuis le périmètre (README OMK), les couplages invisibles
([[aquaman-couplages-invisibles]] §Couplages 1-4), et le catalogue JTBD
([[aquaman-jtbd-emit-receive]] §Forme 1-3).

## Le routage B3 sans Aquaman

Une demande entrante (par exemple Flash qui livre une feature spec avec tierce IP)
arrive par le canal des pair-checks #7 #8 ou par les couplages invisibles.
**L'émetteur amont sait déjà de quelle classe il s'agit** — il a les inputs qu'Aquaman
exige pour cette classe :

- Cyborg sait qu'il parle privacy (il porte le chiffrement et la rétention).
- Superman sait qu'il parle claim (il porte la formulation publique).
- Flash sait qu'il parle IP (il porte l'artefact).
- JohnJones sait qu'il parle contract (il porte le deal).

**Conséquence** : Aquaman n'a pas besoin de **trier** les demandes entrantes. Chaque
émetteur amont amorce la Forme 1-4 lui-même. Aquaman n'arbitre que les cas-frontière
(par exemple *« cette feature touche à la privacy ET à l'IP — qui ouvre la Forme
? »* — réponse : les deux, en séquence, avec Aquaman A sur la privacy si l'IP n'est
pas conflictuelle).

## Trois cas-frontière entre classes

**Cas-frontière 1 — Privacy ∧ IP.** Une feature qui collecte des données personnelles
ET utilise une lib tierce. Forme 1 (privacy) puis Forme 3 (IP). Aquaman A en
séquence, **pas en parallèle** — un sign-off privacy sans sign-off IP n'est pas un
`LEGAL_READY`.

**Cas-frontière 2 — Claim ∧ Contract.** Une promesse client dans une proposition
commerciale qui devient une claim publique. Forme 3 (contract) d'abord, Forme 2
(claim) ensuite. Aquaman A en séquence ; le **handoff** est documenté dans le JTBD
packet.

**Cas-frontière 3 — IP ∧ Contract.** Un livrable réalisé pour un client qui utilise
une lib tierce. Forme 3 couvre les deux aspects ; pas de double pass. **Le seul cas**
où Aquaman produit une Forme 3 unifiée.

Ces 3 cas-frontière sont **projetés** depuis le périmètre README et les couplages
invisibles. Aucun ne provient d'un cas réel observé.

## Les 4 gates comme discipline de réponse

Une fois la classe identifiée, Aquaman applique les **3 gates officiels** de manière
non-arbitraire :

- `LEGAL_READY` quand **tous** les critères de la classe sont remplis (seuil
  chiffré). Critère **binaire**, pas négociable.
- `NEEDS_REVIEW` quand les critères sont **incomplets** ou **en cours**. Pas un
  veto — une attente.
- `BLOCKED_RISK` quand un critère est **manquant** ou **non-satisfaisant**. Veto
  catalogue (cf. [[aquaman-veto-engagement-sans-perimetre]]), déclenché si la classe
  est 4 (contract).

`BLOCKED_RISK` sur les classes 1-3 n'est **pas un veto catalogue** — c'est une
**décision B2 standard** qui se résout par amendement de mandat (cf.
`b2-eight-domain-vetoes-catalogue.md` §La règle de résolution). Seul le `BLOCKED_RISK`
sur la classe 4 (contract) déclenche le veto canonique *« engagement-sans-périmètre »*.

**Conséquence** : un Superman qui voit `BLOCKED_RISK` sur une claim litigieuse
peut amender son claim et redéclencher la Forme 2 — pas d'escalade B1. Un JohnJones
qui voit `BLOCKED_RISK` sur un contract sans périmètre écrit **escalade B2 Council**
parce que c'est le veto canonique.

## Anti-pièges

- **Confondre classe et surface.** Les 4 classes regroupent les 7 surfaces — un
  *employment/NDA* est un cas particulier de la classe 4 (contract), pas une classe
  distincte. La créer ouvrirait une 5ᵉ Forme sans valeur opérationnelle.
- **Aquaman qui trie.** Si Aquaman trie lui-même les demandes entrantes par classe,
  il devient un goulot d'étranglement. Le routage par classe est la responsabilité
  de **l'émetteur amont**, pas d'Aquaman.
- **Seuils LEGAL_READY non-chiffrés.** Un seuil *« privacy acceptable »* est
  inutilisable. Les seuils doivent être chiffrés (chiffrement at rest vérifié, IAM
  documenté, etc.) — sinon le gate dérive.
- **Cas-frontière en parallèle.** Les classes 1+3 et 2+4 doivent passer en
  **séquence**, pas en parallèle. Un pass parallèle produit deux LEGAL_READY
  indépendants, ce qui n'a pas de sens pour un objet unifié (livrable qui collecte
  des données ET utilise une lib tierce).

## Liens

- [[aquaman-domaine-legal-perimetre]] — les 7 surfaces qui se réduisent aux 4
  classes
- [[aquaman-jtbd-emit-receive]] — les Formes 1-3 (catalogue JTBD) qui sont les
  objets opérationnels des classes 1-4
- [[aquaman-couplages-invisibles]] — les émetteurs amont canoniques par classe
- [[aquaman-gates-et-pair-checks]] — les 3 gates et leurs conditions de bascule
- [[aquaman-veto-engagement-sans-perimetre]] — le veto canonique déclenché
  uniquement par la classe 4
- [[aquaman-defensibility-triple-signature]] — la Forme 4 (binder) déclenchée
  par incident, hors classification 4 classes

## Note de confiance

**Reconstruit, à moitié étayé.** Les 4 classes sont **projetées** par réduction des 7
surfaces depuis le périmètre posé en [[aquaman-domaine-legal-perimetre]]. Les
**émetteurs amont canoniques** sont confirmés par les couplages invisibles
([[aquaman-couplages-invisibles]] §Couplages 1-4). Les **3 gates** par classe sont
**reconstruits** par croisement du triplet ligne 47 de [[eight-domain-avengers-wheel]]
(qui pose l'état ternaire sans détailler par classe) et de la doctrine veto catalogue.
Les 3 cas-frontière sont **projetés** depuis la pratique des 4 Formes, pas observés en
cycle. Le routage B3 sans Aquaman est une **proposition opérationnelle** déduite des
émetteurs amont canoniques, pas une doctrine posée. **À vérifier en cycle** : (1) les
émetteurs amont savent-ils réellement classe-er eux-mêmes ?, (2) les seuils chiffrés
par classe sont-ils tenables ?, (3) les cas-frontière en séquence produisent-ils
vraiment un seul `LEGAL_READY` au bout ?

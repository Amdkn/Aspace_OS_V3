---
type: Concept
title: Procédure d'amendement RACI 8/8 + B1 — format complet en 6 étapes
description: Le tour 4 (`batman-raci-i-sur-4-packet-council-ready`) a saisi un packet conditionné à la procédure d'amendement RACI unanimité 8/8 + B1, empruntée à Green Lantern V5. Le tour 4 n'a pas posé le format **complet** de cette procédure. Le concept propose les 6 étapes (intent → brief → co-signature → agenda → deliberation → D4 append-only) avec时限, sorties attendues, et résolution de désaccord. La procédure devient saisissable par n'importe quel capitaine B2.
tags: [b2, ops, batman, raci, amendement, unanime, 8-8, b1, procedure, format, 6-etapes]
generated: { by: minimax-m3, at: 2026-08-19T06:36:00Z }
verified:
  - { by: process:lecture-canon-b2-tour-5, at: 2026-08-19T06:36:00Z }
sources:
  - id: b2-council-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche
    last_modified: 2026-08-19
  - id: b2-meso-decision-packet
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — format canonique
    last_modified: 2026-08-19
  - id: batman-raci-i-sur-4
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-raci-i-sur-4-packet-council-ready.md"
    title: Batman I sur #4 — packet Council-ready
    last_modified: 2026-08-19
  - id: batman-matrice-12-v5
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-matrice-12-pair-checks-v5-extension-proposal.md"
    title: Matrice 12 pair-checks V5 extension proposal
    last_modified: 2026-08-19
  - id: green-lantern-v5-granularisation
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-v5-pair-check-granularisation-9.md"
    title: V5 pair-check granularisation 9
    last_modified: 2026-08-19
  - id: b2-pair-check-raci
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Procédure d'amendement RACI unanimité 8/8 + B1 — format complet

## Le trou que ce concept ferme

Le tour 4 (`batman-raci-i-sur-4-packet-council-ready`) a posé un
packet conditionné à la **procédure d'amendement RACI unanimité 8/8
+ B1**. Green Lantern V5 (`green-lantern-v5-pair-check-granularisation-9`)
a aussi posé cette procédure. **Aucun des deux n'a détaillé le
format complet** — étapes,时限, sorties, résolution de désaccord.

Ce concept propose les **6 étapes** du format, avec critères
d'acceptance par étape, de sorte que n'importe quel capitaine B2
puisse saisir la procédure sans réinventer le rituel.

## La procédure d'amendement — pourquoi unanimité 8/8 + B1

`b2-pair-check-raci-by-rank` pose la table 9 pair-checks comme
**canonique** (référence V4). Un amendement RACI modifie la table —
c'est un changement de doctrine, pas un arbitrage ponctuel. La
procédure unanimité 8/8 + B1 est cohérente avec :

- `b2-council-arbitrage-rule` §« Quand le Council escalade à B1 » :
  une modification de table est **modification de doctrine**, ce
  qui dépasse le Council. B1 doit ratifier.
- L'**unanimité 8/8** assure que chaque capitaine accepte la
  modification. Un seul veto bloque l'amendement — c'est la
  propriété *non-négociable* du catalogue 8 vetos appliquée à la
  table RACI.
- La **ratification B1** assure la cohérence North Star. Une table
  RACI qui contredit le North Star est invalide.

## Les 6 étapes du format

### Étape 1 — **Intent** (1 semaine, sort(i) : brief doc)

**Acteur** : capitaine B2 demandeur (Batman, Superman, etc.).
**Livrable** : brief d'amendement RACI ≤ 2 pages.
**Contenu obligatoire** :
- pair-check(s) modifié(s) (par exemple : ajouter Batman en I sur
  #4)
- RACI avant / RACI après
- motivation (≤ 1 paragraphe)
- risque identifié (couplage, red flag, cascade)
- capitaines co-signataires visés

**Critère d'acceptance** : brief ≤ 2 pages, sections obligatoires
toutes remplies.

### Étape 2 — **Brief co-signé** (1 semaine, livrable : 2+
signatures)

**Acteur** : capitaine demandeur + capitaine co-signataire principal
(par exemple : Batman + Cyborg).
**Livrable** : brief co-signé.
**Mécanisme** : si le pair-check amendé touche un autre capitaine
(Batman sur #4 = Cyborg), le co-signataire principal est ce
capitaine. Si l'amendement est **général** (par exemple :
granularisation #9 GL), le co-signataire est People (Green Lantern).
**Critère d'acceptance** : ≥ 1 co-signature obtenue. Si refus du
co-signataire principal, retour à Étape 1.

### Étape 3 — **Co-signatures 8/8** (2-4 semaines, livrable : 8
signatures ou veto)

**Acteur** : capitaine demandeur + tous les 8 capitaines B2.
**Livrable** : 8 signatures ou 1+ veto documenté.
**Mécanisme** :
- capitaine demandeur présente le brief co-signé en revue hebdo B2
  Council.
- Chaque capitaine consulte, puis signe ou oppose son veto
  catalogue.
- Si un veto est opposé, retour à Étape 1 (le brief est amendé
  ou retiré).
- Si 8/8 signatures, passage à Étape 4.
**Critère d'acceptance** : 8 signatures ou retrait du brief.

### Étape 4 — **Agenda B2 Council** (1 semaine, livrable : packet
Council-ready)

**Acteur** : capitaine demandeur.
**Livrable** : packet mésoperpétuel conforme `b2-meso-decision-packet-spec`.
**Champs obligatoires** :
- `meso_decision_id: B2-MESO-DECISION-YYYY-NN-amendement-raci`
- `source_mandate: B2-PEER-YYYY-NN` (l'intent est lui-même un
  problème B2 pair)
- `mode: negotiation` (l'amendement est par définition une
  négociation)
- `impacted_domains: [les 8 capitaines]`
- `tradeoff: "Modification table RACI : [description courte]"`
- `decision: accepted | blocked` (par Council, pas par capitaine)
- `proof_expected: [B2 RACI update, B1 ratification packet]`
- `next_review: 12WY-2026-Q?` (cycle du Council)

**Critère d'acceptance** : packet conforme gabarit 8 champs.

### Étape 5 — **Délibération B2 Council + ratification B1** (1
séance hebdomadaire, livrable : décision journal Council)

**Acteur** : B2 Council (8 capitaines) + B1 (Summers en séance).
**Livrable** : décision journal Council + ratification B1.
**Mécanisme** :
- Council délibère sur le packet.
- Vote : unanimité 8/8 (re-validée en séance).
- Si 8/8 OK, B1 ratifie le changement de table RACI.
- Si B1 refuse, le packet est `decision: blocked` avec motif.
- Si 1 capitaine vote contre, retour à Étape 1.

**Critère d'acceptance** : unanimité 8/8 + ratification B1.

### Étape 6 — **Append D4** (≤ 24h, livrable : table RACI mise à
jour)

**Acteur** : capitaine demandeur + scribe (au choix).
**Livrable** : table RACI V5 append-only, packet original archivé
en annexe.
**Mécanisme** :
- Conformer à la doctrine D4 : aucune ligne de la table V4 n'est
  éditée. Ajout d'une ligne V5 ou nouvelle table.
- Append au journal `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` avec
  `meso_decision_id` + référence.
- Mise à jour de `b2-pair-check-raci-by-rank.md` (concept RACI
  par rang du corpus B2) avec la version V5.

**Critère d'acceptance** : append vérifié, table V5 lisible.

## Total — 6-10 semaines

La procédure dure 6-10 semaines en total (1+1+2-4+1+1+0.2). C'est
**long**, mais c'est la **durée d'un cycle de build** entier. La
procédure est cohérente avec la doctrine 12WY (Summers).

## Trois résolutions de désaccord

### Cas 1 — Co-signataire principal refuse (Étape 2)

Si Cyborg refuse la co-signature de Batman I sur #4, Batman
retire l'intent. La procédure reprend depuis Étape 1 avec un
amendement possible (par exemple : Batman C sur #4 au lieu de I).

### Cas 2 — Un capitaine oppose son veto (Étape 3)

Si Superman oppose son veto sur un amendement Batman (par exemple :
Batman I sur #4 viole la souveraineté IT de Superman sur
pair-check #5 Finance → Growth), le brief est retiré et un
**packet mésoperpétuel** documente le veto. La procédure reprend
depuis Étape 1.

### Cas 3 — B1 refuse la ratification (Étape 5)

Si Summers refuse la ratification (par exemple : la modification
de table RACI contredit un pivot North Star), le packet est
`decision: blocked` avec motif B1. La procédure **s'arrête**.
Batman (ou autre capitaine) peut reprendre avec un amendement
aligné North Star.

## Pourquoi 6 étapes et pas 4 ou 8

- **4 étapes** (intent, brief, vote, append) sont insuffisantes :
  la co-signature 8/8 (étape 3) et la ratification B1 (étape 5)
  sont des **gates** distinctes qui demandent des mécanismes
  distincts.
- **8 étapes** (par exemple : intent, brief, contre-brief, vote,
  ratification, implémentation, audit, archive) sont trop
  granulaires : la doctrine mésoperpétuelle travaille par
  *packet*, pas par *workflow*.
- **6 étapes** est l'équilibre entre granularité Council-ready et
  simplicité opérationnelle.

## Anti-pièges

- **Court-circuit Étape 1 → Étape 5.** Batman a proposé des
  Council-ready conditionnels (tour 4), mais ne peut pas **sauter**
  l'Étape 1-3. Le packet conditionné n'est **Council-ready** que
  si l'Étape 3 a livré 8/8 signatures.
- **Étape 5 sans B1.** La ratification B1 est **non-négociable**.
  Si Summers est absent, l'Étape 5 est reportée, pas court-circuitée.
- **Confondre amendement RACI et arbitrage pair-check.** Un arbitrage
  pair-check (cf. `b2-pair-check-raci-by-rank`) est une décision
  sur un cas; un amendement RACI est une modification de table.
  Procédures différentes, formats différents.
- **Étape 6 comme édit de la V4.** L'append D4 interdit l'édition
  de V4. Si Batman édite la table V4 pour ajouter Batman I sur #4,
  il viole D4. La procédure **doit** produire une table V5 ou
  une ligne ajoutée (cf. concept `batman-matrice-12-v5`).

## Liens

- [[batman-raci-i-sur-4-packet-council-ready]] — le packet conditionné
- [[batman-matrice-12-v5-extension-proposal]] — l'extension V5
- [[b2-council-arbitrage-rule]] — l'instance Étape 5
- [[b2-meso-decision-packet-spec]] — le format Étape 4
- [[b2-pair-check-raci-by-rank]] — la table V4 qu'on amende
- [[green-lantern-v5-pair-check-granularisation-9]] — l'origine
  de la procédure

## Note de confiance

**Reconstruit, à moitié étayé.** Le format 6 étapes est **projeté**
par Batman, en cohérence avec `b2-council-arbitrage-rule` et
`b2-meso-decision-packet-spec`. Les时限 (1+1+2-4+1+1+0.2 semaines)
sont **arbitraires**, alignés sur la cadence 12WY. Les 3 cas de
résolution de désaccord sont **projetés** depuis la pratique
Council standard. **Confiance haute** sur la cohérence
doctrinale, **moyenne** sur les时限 et les cas. À valider en
cycle : (1) la durée 6-10 semaines est-elle tenable ? (2) l'Étape 3
2-4 semaines pour 8 signatures est-elle réaliste ? (3) la
ratification B1 est-elle viable en séance hebdomadaire ?

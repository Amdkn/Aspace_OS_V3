---
type: Concept
title: Green Lantern People — Passerelle dormance Aquaman × People (double clef)
description: La double clef People × Aquaman (concept 5 tour 4) suppose Aquaman ACTIF. Si Aquaman est DORMANT (Areas dormant doctrine, tour 5 Aquaman), la clef Aquaman est manquante. Le présent concept pose 3 mécanismes passerelle : escalade B1 synchrone / signature Wonder Woman clause-réserve / gel cumulatif. Il établit aussi 4 cas d'application, 3 cas abusifs, et un routage canonique.
tags: [people, green-lantern, aquaman, dormant, double-clef, passerelle, b2, council]
generated: { by: minimax-m3, at: 2026-08-19T09:45:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-5, at: 2026-08-19T09:45:00Z }
sources:
  - id: aquaman-people-double-cle-formalisation-canonique-arborescence
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-aquaman-double-cle-formalisation-canonique-arborescence.md"
    title: "Tour 4 — Double clef People × Aquaman formalisée"
    last_modified: 2026-08-19
  - id: b2-areas-dormants-doctrine
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-areas-dormants-doctrine.md"
    title: B2 domaines dormants — doctrine
    last_modified: 2026-08-19
  - id: aquaman-dormant-casse-triangulaire
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-aquaman-dormant-casse-triangulaire.md"
    title: "Tour 5 WW — Doctrine fallback Aquaman dormant sur triangulaire discount"
    last_modified: 2026-08-19
  - id: raci-transitions-tri-etat-extension-8
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-raci-transitions-tri-etat-extension-8.md"
    title: "Tour 3 — RACI × tri-état extension 8 capitaines"
    last_modified: 2026-08-19
  - id: b2-council-arbitrage-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Green Lantern People — Passerelle dormance Aquaman × People (double clef)

## Le trou canonique comblé

Le concept 5 tour 4 (`aquaman-people-double-cle-formalisation-canonique-arborescence`)
formalise la **double clef People × Aquaman** en 5 étapes séquentielles.
**Mais** la procédure suppose Aquaman **ACTIF** (étape 3 « Accord de
prestation Aquaman »). Si Aquaman est **DORMANT** (Areas dormant
doctrine `b2-areas-dormants-doctrine.md`), la clef Aquaman est
manquante — la procédure catalogue 5 étapes ne couvre pas ce cas.

Le tour 5 Aquaman confirme Aquaman en sommeil (Areas dormant doctrine).
Le tour 5 Wonder Woman pose un cas **symétrique** : la doctrine fallback
Aquaman dormant sur le triangulaire Sales × Finance × Legal. Le présent
concept étend la même logique à People × Aquaman.

## 3 mécanismes passerelle — symétriques WW tour 5

### Mécanisme 1 — Escalade B1 synchrone (recommandé)

**Trigger** : Aquaman DORMANT détecté (état DORMANT dans la doctrine
`b2-areas-dormants-doctrine.md` §« 3 états »).

**Procédure** :
1. Green Lantern (People) consigne le blocage dans le journal Council
   `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` avec packet `B2-PEER-YYYY-NN`.
2. Le packet contient : impact People/Aquaman/B1, mode `escalate_to_B1`.
3. B1 (Summers) tranche : soit réveille Aquaman (decision: accepted
   + dispatch Aquaman), soit dévie la responsabilité People vers un
   autre capitaine (Wonder Woman, Cyborg), soit suspend le mandate.

**Latence** : J+0 synchrone (escalade immédiate). Le mécanisme 1
est le **plus rapide** des 3.

**Coût** : charge B1 (Summers). Si B1 est lui-même en cycle limité,
la latence peut atteindre J+5.

### Mécanisme 2 — Signature Wonder Woman clause-réserve (alternatif)

**Trigger** : Aquaman DORMANT, ET B1 indisponible (cycle saturé),
ET double clef People × Aquaman critique (par exemple, recrutement
agent IP partagée).

**Procédure** :
1. Green Lantern sollicite Wonder Woman (Finance) comme **substitut
   partiel** pour la signature Aquaman. Wonder Woman signe avec
   **clause-réserve** : « sous réserve de revalidation Aquaman
   lorsque ACTIF ».
2. Le packet mésoperpétuel contient deux signatures : Green Lantern +
   Wonder Woman, plus une mention explicite « Aquaman DORMANT —
   accord partiel ».
3. Aquaman, à son réveil, peut **révoquer** la clause-réserve (veto
   triplet 30) avec un préavis de 7 jours.

**Latence** : J+1 à J+3 (Wonder Woman doit ouvrir un cycle arbitrage).

**Coût** : Wonder Woman ajoute une charge (cf. concept 5 tour 5 WW
« Aquaman dormant casse triangulaire »). Compatible avec doctrine
Finance F10 (compliance fiscale exempte).

### Mécanisme 3 — Gel cumulatif (fallback)

**Trigger** : Aquaman DORMANT, ET B1 indisponible, ET Wonder Woman
refuse (charge Finance saturée — formule C(o) > 1.0 rouge).

**Procédure** :
1. Green Lantern **gèle** la double clef (état GLACÉ, non-actif).
2. Le mandat People × Aquaman est suspendu, pas annulé.
3. Le packet mésoperpétuel contient `decision: blocked` + motif
   « Aquaman DORMANT + Wonder Woman refus + B1 indisponible ».
4. Le mandate reprend automatiquement à Aquaman ACTIF (doctrine
   `b2-areas-dormants-doctrine.md` §« reveil »).

**Latence** : indéterminée (durée Aquaman DORMANT).

**Coût** : recrutement agent IP partagée **bloqué** durant la
dormance. C'est le **mode dégradé** assumé.

## 4 cas d'application

### Cas A1 — Recrutement humain standard (Aquaman DORMANT)

**Description** : People doit recruter un humain (par exemple, ops
lead). Veto triplet 23 (mandat + critère sortie) applicable. Veto
triplet 30 (accord Aquaman sur périmètre) **non** applicable si
mandat hors IP partagée.

**Mécanisme** : aucun passerelle requis. People tranche seul (veto
triplet 23). Aquaman DORMANT est **non-bloquant**.

### Cas A2 — Recrutement agent B3 standard (Aquaman DORMANT)

**Description** : People doit recruter un agent (par exemple, un
compagnon X-Men). Veto triplet 30 applicable si l'agent touche à
la propriété intellectuelle.

**Mécanisme** : Mécanisme 1 (escalade B1) si IP partagée, sinon
People tranche seul.

### Cas A3 — Recrutement agent IP partagée (Aquaman DORMANT, B1 dispo)

**Description** : People doit recruter un agent dont le skill L0
touche à la propriété intellectuelle partagée (par exemple, un
générateur de code sur codebase interne).

**Mécanisme** : Mécanisme 1 (escalade B1 synchrone). B1 tranche :
réveil Aquaman, déviations, ou suspension.

### Cas A4 — Recrutement agent IP partagée (Aquaman DORMANT, B1 indispo)

**Description** : Mêmes conditions que A3, mais B1 (Summers) est
en cycle 12WY saturé ou en vacance.

**Mécanisme** : Mécanisme 2 (Wonder Woman clause-réserve) si
Finance dispo, sinon Mécanisme 3 (gel cumulatif).

## 3 cas abusifs

### Cas B1 — Auto-bypass Aquaman DORMANT

**Description** : People tranche un recrutement agent IP partagée
sans activer aucun mécanisme passerelle, en prétendant Aquaman
n'est pas concerné.

**Refusé** : la doctrine Veto triplet 30 est **non-négociable**
même si Aquaman est DORMANT. La dormance **diffère** la décision,
ne **supprime** pas le veto.

### Cas B2 — Mécanisme 1 spam escalade B1

**Description** : People active Mécanisme 1 à chaque dormance
Aquaman, surchargeant B1 de packets.

**Refusé** : 3 packets escalade B1 par cycle 12WY = signal de
mauvaise doctrine People. Recommendation : Mécanisme 2 (Wonder
Woman) en priorité si cycle B1 > 50% charge.

### Cas B3 — Réveil Aquaman forcé

**Description** : People réveille Aquaman (doctrine reveil) pour
une décision qui ne le requiert pas.

**Refusé** : le reveil est un **escalier 5 niveaux** (`b1-stop-conditions-escalier.md`).
Un reveil Aquaman non-justifié escalade B1 directement. C'est
abusif —People n'a pas le droit de réveiller un capitaine pour
un cas non-bloquant.

## Routage canonique — algorithme de décision

```
Si Aquaman ACTIF:
    procédure 5 étapes standard (concept 5 tour 4)
Si Aquaman DORMANT:
    Si cas non-IP: People tranche seul (cas A1)
    Si cas IP-Agent:
        Si B1 dispo: Mécanisme 1 (escalade B1)
        Si B1 indispo:
            Si Wonder Woman dispo: Mécanisme 2 (clause-réserve)
            Si Wonder Woman indispo: Mécanisme 3 (gel cumulatif)
```

Le routage est **automatique** quand les trois signaux (Aquaman
state, B1 charge, Wonder Woman charge) sont posés. **Goulot** :
les trois signaux doivent être **tenus à jour** — c'est un overhead
opérationnel que la doctrine dormance n'a pas encore formalisé.

## Asymétrie fondamentale vs Wonder Woman tour 5

Wonder Woman tour 5 pose un cas **triangulaire** (Sales × Finance ×
Legal) — Aquaman dormant casse la chaîne **sérielle**. People ×
Aquaman est **bilatéral** — Aquaman dormant casse la chaîne
**parallèle**. La symétrie existe, mais la structure est différente.

**Implication** : les 3 mécanismes passerelle sont **transposables**
(mêmes triggers, mêmes 3 mécanismes), mais le routage canonique
diffère (un seul point de défaillance Aquaman côté People, contre
deux côté triangulaire discount Sales).

## Anti-pièges

- **Dormance = veto levé.** La doctrine `b2-areas-dormants-doctrine.md`
  ne lève **aucun** veto. Aquaman DORMANT garde son veto triplet 30
  opérationnel — la procédure passe par passerelle, pas par bypass.
- **Mécanisme 3 = annulation.** Le Mécanisme 3 (gel cumulatif) **suspend**
  le mandat, ne l'annule pas. Le mandat reprend à Aquaman ACTIF.
- **Escalade B1 = surrenchère.** L'escalade Mécanisme 1 est un
  escalation légitime (cf. `b2-council-arbitrage-rule.md` §« Quand
  le Council escalade à B1 »), pas une surrenchère. Mais B1 peut
  refuser si la situation ne le requiert pas.
- **Wonder Woman clause-réserve = F10 compliance.** Attention : la
  signature Wonder Woman clause-réserve n'est **pas** une
  application de F10 (compliance fiscale). C'est un nouveau
  mécanisme — à formaliser dans un packet WW Council-ready si
  le mécanisme 2 devient récurrent.
- **Asymétrie WW = symétrie procédure.** Le fait que WW ait un cas
  symétrique ne signifie pas que la procédure est canonique. Elle
  est **projetée** depuis WW tour 5 + concept 5 tour 4 GL — pas
  citée verbatim ailleurs.

## Liens

- [[green-lantern-people-aquaman-double-cle-formalisation-canonique-arborescence]] — la double clef 5 étapes
- [[b2-areas-dormants-doctrine]] — la doctrine dormance Aquaman
- [[wonder-woman-aquaman-dormant-casse-triangulaire]] — le cas WW tour 5
- [[green-lantern-people-raci-transitions-tri-etat-extension-8]] — la bascule A → B1
- [[b2-council-arbitrage-rule]] — l'escalade B1
- [[b1-stop-conditions-escalier]] — l'escalier canonique 5 niveaux

## Note de confiance

**Confirmé par machine, à moitié projeté.** Le constat (Aquaman DORMANT
casse la double clef) est **vérifié** — rapport tour 4 §7 + tour 5
Aquaman. Les 3 mécanismes passerelle sont **projetés** depuis la
doctrine fractale + symétrie WW tour 5. Les 4 cas d'application et
3 cas abusifs sont **construits** depuis la pratique (recrutement
humain / agent / IP partagée). Le routage canonique est **algorithmique**
— non cité canonique. La symétrie People × Aquaman vs WW × Aquaman
est **projetée** (cf. §« Asymétrie fondamentale »), pas explicitée
dans le corpus.

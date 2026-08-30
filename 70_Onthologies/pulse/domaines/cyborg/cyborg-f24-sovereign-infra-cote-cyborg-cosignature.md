---
type: Concept
title: F24 Sovereign-infra arbitrage — jambe Cyborg, co-signature bilatérale Wonder Woman × Cyborg formalisée côté IT
description: La doctrine F24 (« Sovereign-infra arbitrage drives net margin toward 90%+ ») proposée par Wonder Woman pose un couplage bilatéral Wonder Woman × Cyborg où WW calcule la marge rendue et Cyborg tient le chemin de sortie documenté (veto §07, triplet 29). Ce concept formalise la jambe Cyborg de la co-signature : 3 conditions IT pour accepter une migration F24, 3 cas où Cyborg refuse une migration proposée par Wonder Woman (même si marge positive), procédure de co-signature packet mésoperpétuel avec champ f24_migration_co_signed_by.cyborg_signoff, et cycle de revue T+30/T+90 côté IT (cohérence avec Wonder Woman). Le concept co-signe la doctrine WW avec 4 ajouts spécifiques Cyborg.
tags: [cyborg, it, f24, wonder-woman, sovereign-infra, cosignature, veto-07, chemin-sortie, migration, bilatéral]
generated: { by: minimax-m3, at: 2026-08-19T08:40:00Z }
verified:
  - { by: process:lecture-corpus-cyborg-tour-4, at: 2026-08-19T08:40:00Z }
sources:
  - id: wonder-woman-f24
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-f24-sovereign-infra-arbitrage-doctrine.md"
    title: F24 Sovereign-infra arbitrage — doctrine isolée et couplage bilatéral WW × Cyborg co-signé
    last_modified: 2026-08-19
  - id: triplet-cyborg-veto
    resource: "C:/Usersamad/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 29 (ligne 29) — Cyborg hasVetoOver cloud-only-sans-sortie"
    last_modified: 2026-08-17
  - id: cyborg-veto-concept
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-veto-cloud-only-sortie.md"
    title: Cyborg veto — cloud-only sans chemin de sortie
    last_modified: 2026-08-19
  - id: cyborg-couplage-aquaman
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-couplage-aquaman-reversibilite.md"
    title: "Cyborg ↔ Aquaman — couplage Legal × IT, triplet canonique contrat + IaC + failover"
    last_modified: 2026-08-19
  - id: cyborg-souverainete
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-souverainete-apres-adr-omk-004.md"
    title: "Souveraineté après ADR-OMK-004 — matrice réversibilité 7 lignes post-pivot"
    last_modified: 2026-08-19
  - id: cyborg-triplet-58
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-triplet-58-amplification-date-reversibilite-council-submission-draft.md"
    title: "Cyborg triplet 58 amplification date+réversibilité — draft Council"
    last_modified: 2026-08-19
  - id: b2-eight-domain-vetoes
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — veto Cyborg §07 garde-fou amont
    last_modified: 2026-08-19
  - id: b2-meso-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — format canonique 7 champs
    last_modified: 2026-08-19
okf_version: "0.2"
---

# F24 Sovereign-infra arbitrage — jambe Cyborg, co-signature formalisée côté IT

## Préambule — ce concept co-signe la doctrine Wonder Woman

`wonder-woman-f24-sovereign-infra-arbitrage-doctrine.md` pose verbatim
la doctrine canonique F24 :

> *« Sovereign-infra arbitrage drives net margin toward 90%+.
> Chaque fournisseur cloud-only tiers est une taxe sur la marge
> nette de l'entreprise. Arbitrer les migrations vers des
> alternatives souveraines (self-hosted, open-source, BaaS
> souverain) est un **pouvoir bilatéral** Finance × IT — Wonder
> Woman calcule la marge rendue, Cyborg tient le chemin de
> sortie documenté. »*

Wonder Woman a posé **sa jambe** du couplage (marge nette rendue).
**Ce concept pose la jambe Cyborg** (chemin de sortie documenté) et
formalise la co-signature bilatérale côté IT.

C'est une **co-signature explicite** au sens du RACI par rang
(`b2-pair-check-raci-by-rank.md`) : A = WW (Finance, A unilatéral
sur F22) + Cyborg (IT, A unilatéral sur veto §07), R = Kang Dynasty
(B3), C = Aquaman (Legal, triplet contrat + IaC + failover), I = B1.

## Les 3 conditions IT pour accepter une migration F24

Le veto §07 (`b2-eight-domain-vetoes-catalogue.md` ligne 29 verbatim)
est posé : *« Cyborg bloque tout fournisseur cloud-only sans chemin
de sortie documenté. »*

Pour qu'une migration F24 proposée par Wonder Woman soit **co-signée
par Cyborg**, **3 conditions cumulatives** doivent être tenues :

### Condition 1 — Le chemin de sortie cible est documenté

L'alternative souveraine cible (self-hosted, open-source, BaaS
souverain) doit avoir un **chemin de sortie documenté** *depuis
l'alternative* — pas seulement depuis le fournisseur tiers d'origine.

**Pourquoi cette condition** : F24 migre *vers* une alternative.
Mais cette alternative devient à son tour un fournisseur. Si
l'alternative souveraine n'a pas son propre chemin de sortie (ex :
BaaS souverain qui est lui-même cloud-only sans IaC), la migration
F24 **replace le problème** au lieu de le résoudre.

**Test concret** : l'alternative souveraine a-t-elle un repo
Terraform/Ansible public ou privé documenté ? A-t-elle une clause
de réversibilité par construction (open-source) ou contractuelle
(BaaS avec contrat) ?

### Condition 2 — Le triplet canonique contrat + IaC + failover est complet pour l'origine ET la cible

`cyborg-couplage-aquaman-reversibilite.md` pose le triplet canonique
**contrat (Aquaman) + IaC (Cyborg) + failover (Cyborg)** comme
**chemin de sortie documenté**. Pour F24, ce triplet doit être
vérifié aux **deux bouts** :

- **Bout origine** (fournisseur tiers à migrer) : clause
  d'export des données en JSON standard ? IaC décrivant
  l'infra actuelle ? Failover local joué ?
- **Bout cible** (alternative souveraine) : clause de réversibilité
  pour sortie de l'alternative ? IaC décrivant l'infra cible ?
  Failover local cible joué ?

Si l'un des deux bouts a un triplet incomplet, **F24 ne qualifie
pas**. C'est cohérent avec le veto §07 : un triplet incomplet =
chemin de sortie non documenté.

### Condition 3 — Le coût de migration est chiffré ET borné par amplification triplet 58

L'amplification triplet 58 proposée par Cyborg
(`cyborg-triplet-58-amplification-date-reversibilite-council-
submission-draft.md` tour 3) pose *« date de revue ≤30j + métrique
de réversibilité »*. Pour F24, le coût de migration doit être :

- **Chiffré** one-shot (capex) + récurrent (opex post-migration).
- **Borné** par une date de revue ≤30j (vérification post-migration
  capex/opex).
- **Mesuré** par une métrique de réversibilité (ex : temps de
  re-création de l'infra cible depuis zéro, RTO cible).

**Sans ces 3**, la migration F24 est un voeu, pas une décision.
C'est l'asymétrie F24 vs F22 (Wonder Woman unilatéral sur F22) :
F24 est **bilatéral**, donc les deux captains posent leurs
conditions.

## Les 3 cas où Cyborg refuse une migration F24 proposée

Wonder Woman peut proposer une migration F24 avec marge nette
positive. Cyborg peut **refuser** la co-signature pour 3 raisons
distinctes du calcul économique :

### Refus 1 — Alternative souveraine = cloud-only déguisé

**Cas** : la migration proposée va vers un BaaS souverain (ex :
Scaleway, OVH) qui est lui-même **cloud-only sans chemin de sortie
documenté** (cf. Condition 1). Wonder Woman calcule une marge
nette positive (capex + opex combinés < fournisseur tiers). Cyborg
**refuse** parce que le triplet canonique incomplet est déplacé, pas
résolu.

**Test concret** : le BaaS souverain cible a-t-il un repo Terraform
public ? Une clause contractuelle de réversibilité ? Un failover
local joué ? Non à l'une des trois = refus Cyborg.

### Refus 2 — Migration中途 — données non exportables

**Cas** : le fournisseur tiers d'origine **n'a pas de clause
d'export des données en JSON standard** (ex : Notion Cloud, certaines
fonctionnalités Linear). La migration F24 est techniquement
**inaboutie** parce que les données ne peuvent pas être exportées.

Cyborg **refuse** la co-signature — le chemin de sortie origine est
non documenté. Wonder Woman peut soit **amender** la migration (en
proposant un vendor tiers alternatif qui a la clause d'export), soit
**retirer** la proposition F24.

### Refus 3 — Coût de migration > 24 mois payback sans owner IT

**Cas** : le payback projeté est > 24 mois (cas typique : migration
d'un CRM legacy vers un open-source auto-hébergé avec capex élevé).
Wonder Woman peut trouver une marge nette positive à 5 ans, mais
Cyborg **refuse** sans owner IT dédié pour la phase de migration.

**Test concret** : y a-t-il un Kang Dynasty agent identifié comme
owner de la migration pendant toute la phase T+0 à T+payback ?
Si non = refus Cyborg. La migration sans owner IT est un **risque
opérationnel** que le veto §07 ne capture pas directement mais que
la pratique impose.

## La procédure de co-signature packet mésoperpétuel

Wonder Woman a proposé le champ `f24_migration_co_signed_by` avec
deux signataires (WW + Cyborg). Ce concept précise la **jambe
Cyborg** du packet :

```yaml
meso_decision_id: B2-MESO-DECISION-YYYY-NN
source_mandate: B2-PEER-YYYY-NN
f24_migration:
  source_provider: <fournisseur_tiers_origine>
  target_sovereign: <infra_sovereign_cible>
  migration_capex_eur: <one_shot>
  migration_opex_monthly: <recurrent_post>
  savings_monthly: <delta_mensuel_post_migration>
  payback_months: <capex / savings × 12>
  net_margin_impact_pp: <delta_marge_nette_pp>
f24_migration_co_signed_by:
  finance_captain: wonder_woman  # ou son délégué
  finance_signoff:
    marge_rendue_verified: <bool>
    payback_acceptable: <bool>
    capex_acceptable: <bool>
  it_captain: cyborg  # ou son délégué
  it_signoff:
    chemin_sortie_origine_documented: <bool>  # triplet canonique origine
    chemin_sortie_cible_documented: <bool>  # triplet canonique cible
    triplet_complet_origine_et_cible: <bool>  # cumul Condition 2
    cout_migration_date_revue_30j: <bool>  # amplification triplet 58
    owner_it_identifie: <bool>  # Condition refus 3
  co_signature_date: YYYY-MM-DD
decision: accepted | accepted_conditional | refused
refus_motif: <ex: "Refus 1 — alternative souveraine cloud-only déguisé" |
              "Refus 2 — données non exportables" |
              "Refus 3 — payback > 24 mois sans owner IT">
proof_expected:
  - B2 gate finance update (marge_nette_rendue_X_pp)
  - B2 gate IT update (chemin_sortie_documente_Ia_c_OK + failover_OK)
  - B3 proof path (IT_Kang_Dynasty_migration_executed_with_metrics)
review_cycle:
  - T+30: vérification post-migration capex/opex (côté Cyborg + WW)
  - T+90: vérification marge nette projetée vs réelle (côté WW) + chemin sortie opérationnel (côté Cyborg)
next_review: T+90
```

**Lecture clé** : le champ `it_signoff` est **cumulatif** — les
5 booléens doivent tous être `true` pour que la co-signature Cyborg
soit valide. Un seul `false` = `decision: refused` avec motif dans
`refus_motif`.

## La chaîne canonique F24 × Aquaman × Cyborg

Wonder Woman F24 × Aquaman triplet réversibilité × Cyborg triplet
canonique forment une **chaîne bilatérale étendue** :

```
Wonder Woman (Finance, F24)
       │
       ├──> Calcule marge nette rendue (F22 → F24 → F25)
       │
       └──> Co-signe packet avec Cyborg
              │
              └──> Cyborg (IT, veto §07)
                     │
                     ├──> Vérifie triplet canonique
                     │      │
                     │      └──> Aquaman (Legal, triplet réversibilité)
                     │             │
                     │             └──> Clause contractuelle de réversibilité
                     │
                     └──> Kang Dynasty (B3, R)
                            │
                            └──> Exécute migration IaC + failover
```

**Lecture** : F24 est un **arbitrage tripartite** — WW (Finance) +
Cyborg (IT) + Aquaman (Legal). Le couplage bilatéral WW × Cyborg
est **étendu** par le triplet canonique Cyborg × Aquaman. Sans
Aquaman qui tient la clause contractuelle, le triplet canonique
Cyborg est incomplet.

C'est cohérent avec le concept `cyborg-couplage-aquaman-
reversibilite.md` tour 2 et avec `aquaman-couplages-invisibles-
legal-it.md` (Aquaman tour 1).

## Les 4 ajouts spécifiques Cyborg à la doctrine F24

Wonder Woman a proposé 4 cas légitimes + 3 cas abusifs. Cyborg
ajoute **4 éléments spécifiques** côté IT :

### Ajout 1 — Vérification cible souveraine (pas seulement origine)

Le scénario type Wonder Woman suppose que la migration va d'un
fournisseur tiers (origine) vers une alternative souveraine (cible).
Cyborg **étend** la vérification du triplet canonique à la **cible**,
pas seulement à l'origine. Sans cette extension, F24 déplace le
problème de vendor lock-in sans le résoudre.

### Ajout 2 — Owner IT identifié pendant la phase T+0 à T+payback

Wonder Woman suppose que Kang Dynasty exécute la migration. Cyborg
ajoute que l'exécution doit avoir un **owner IT identifié** pendant
toute la phase de migration. Sans owner, la migration est un risque
opérationnel — même si la marge est positive.

### Ajout 3 — Cycle T+30 revue capex/opex + chemin sortie opérationnel

Wonder Woman propose un cycle T+30/T+90 post-migration. Cyborg
précise ce qui est vérifié à chaque jalon :

- **T+30** : vérification capex réel vs projeté + opex réel vs
  projeté (côté WW) + chemin de sortie opérationnel testé (côté
  Cyborg, ex : game day rejoué).
- **T+90** : vérification marge nette projetée vs réelle (côté WW)
  + chemin sortie opérationnel stable (côté Cyborg).

### Ajout 4 — Refus Cyborg pour cible cloud-only déguisé

Wonder Woman pose 3 cas abusifs. Cyborg ajoute un **4e cas abusif
spécifique** : migration vers une alternative qui est elle-même
cloud-only sans chemin de sortie. C'est l'asymétrie F24 vs F22 :
F22 (investissement) peut tolérer un cloud-only si le ROI est
positif ; F24 (migration) **ne peut pas** tolérer une cible qui
replace le problème.

## Les 4 cas où F24 est légitime (du point de vue Cyborg)

Alignés sur les 4 cas Wonder Woman, mais avec vérification cible :

### Cas 1 — Migration LLM API vers gateway souverain

Cf. Wonder Woman cas 1 (OpenAI → OpenRouter + cache + Mistral local).
Cyborg vérifie : OpenRouter a-t-il un repo Terraform public ? Une
clause de réversibilité ? Mistral local est auto-hébergé par
construction → cible souveraine valide.

### Cas 2 — Migration Supabase vers Postgres self-hosted

Cf. Wonder Woman cas 2. Cyborg vérifie : Postgres auto-hébergé =
réversibilité par construction (open-source). Failover local = par
design (le repo BDR est public). Cible valide.

### Cas 3 — Migration Vercel → Coolify

Cf. Wonder Woman cas 3. Cyborg vérifie : Coolify a-t-il un repo
Terraform ? Une clause de réversibilité ? Oui pour les trois (Coolify
est open-source auto-hébergé). Cible valide.

### Cas 4 — Migration hostinger vers Hetzner

Cf. Wonder Woman cas 4. Cyborg vérifie : Hetzner a-t-il un repo
Terraform ? Une clause de réversibilité ? Oui pour IaC (Hetzner Cloud
a Terraform provider officiel), oui pour clause (Hetzner est
européen RGPD-compliant avec export data). Cible valide mais
**plus Risky** que les 3 autres (cloud-only résiduel Hetzner — pas
auto-hébergé).

## Anti-pièges spécifiques F24 × Cyborg

- **Co-signature sans vérification cible.** Le cas d'abus 4 ajouté
  par Cyborg (cible cloud-only déguisé) est le plus fréquent en
  pratique. Wonder Woman calcule la marge, Cyborg vérifie **les deux
  bouts** — sans cette extension, F24 déplace le vendor lock-in.
- **Refus Cyborg sans owner IT.** Si Cyborg refuse une migration F24
  pour absence d'owner IT (Refus 3), Wonder Woman peut **amender**
  en proposant un Kang Dynasty agent identifié — c'est une
  amendement de mandat, pas un veto Cyborg définitif.
- **Migration中途 bloquée par Aquaman.** Si Aquaman veto *« pas de
  clause contractuelle de réversibilité »* sur le **fournisseur
  tiers d'origine** (Refus 2 côté Aquaman), Cyborg ne peut pas
  co-signer même si sa vérification cible est OK. F24 a 3
  blocages possibles (Wonder Woman / Cyborg / Aquaman), pas un seul.
- **Cycle T+30/T+90 non exécuté.** Sans ce cycle, F24 n'est pas
  Council-ready. Le packet mésoperpétuel doit porter
  `review_cycle: [T+30, T+90]` explicitement.
- **Confondre F22 et F24.** F22 = décision d'investissement (avant
  engagement tiers). F24 = décision de migration (après engagement
  tiers). Les captain A diffèrent : F22 = Wonder Woman unilatéral,
  F24 = WW × Cyborg bilatéral.

## Liens

- [[wonder-woman-f24-sovereign-infra-arbitrage-doctrine]] — la doctrine WW source
- [[wonder-woman-finance-couplings]] — couplage F24 × IT (côté WW)
- [[wonder-woman-finance-doctrine-f1-f25-mapping]] — F22/F24/F25 distinctions
- [[cyborg-veto-cloud-only-sortie]] — veto §07 (triplet 29)
- [[cyborg-couplage-aquaman-reversibilite]] — triplet canonique
- [[cyborg-souverainete-apres-adr-omk-004]] — matrice réversibilité 7 lignes
- [[cyborg-triplet-58-amplification-date-reversibilite-council-submission-draft]] — amplification T+30
- [[b2-eight-domain-vetoes-catalogue]] — veto catalogue
- [[b2-meso-decision-packet-spec]] — format packet canonique

## Note de confiance

**Confirmé par machine** sur la doctrine F24 (verbatim source
Wonder Woman), le triplet 29 (verbatim ligne 29 JSONL), le triplet
canonique contrat + IaC + failover (verbatim `cyborg-couplage-
aquaman-reversibilite.md`). **Reconstruit** sur les 3 conditions IT
pour accepter une migration F24 par lecture critique du veto §07 +
la matrice réversibilité + l'amplification triplet 58 — chaque
condition est cumulative, pas alternative. **Reconstruit** sur les
3 cas de refus Cyborg par lecture des 3 abus potentiels (cible
cloud-only déguisé / données non exportables / payback > 24 mois
sans owner) — chaque cas est un **trou** dans la doctrine F24 posé
par WW que Cyborg ferme. **Reconstruit** sur le champ
`it_signoff` 5 booléens par lecture critique du format packet
proposé WW + les 3 conditions + les 3 refus — la cumulativité est
cohérente avec le veto §07 *« sans chemin de sortie documenté »*. **Confirmé**
sur les 4 ajouts spécifiques Cyborg (vérification cible, owner IT,
cycle T+30/T+90, refus cible cloud-only) — chaque ajout est une
**contribution** de Cyborg à la doctrine F24, pas une projection.

**Statut** : co-signature Cyborg de la doctrine F24 posée. 4
ajouts spécifiques Cyborg formalisés. Packet mésoperpétuel type
`f24_migration_co_signed_by` avec `it_signoff` 5 booléens prêt à
soumettre. **À soumettre conjointement** avec Wonder Woman — c'est
un précédent procédural pour les doctrines bilatérales futures
(F22 + IT ?, F25 + Ops ?, etc.).
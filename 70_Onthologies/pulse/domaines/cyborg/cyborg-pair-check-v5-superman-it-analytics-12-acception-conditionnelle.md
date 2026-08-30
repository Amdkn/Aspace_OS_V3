---
type: Concept
title: V5 matrice pair-check #12 (IT → Growth analytics stack) — acceptation conditionnelle Cyborg avec procédure 5 phases
description: Superman tour 3 (superman-pair-check-v5-brand-and-analytics.md) propose 2 pair-checks supplémentaires V5 : #11 People→Growth Brand et #12 IT→Growth analytics. RACI #12 proposé : A = Cyborg (IT aval — déploie l'analytics stack), R = B3 Kang Dynasty (Nebula_Analytics ou analogue), C = Superman (Growth, consomme), I = B1, B3 Guardians. Ce concept acte l'acceptation conditionnelle Cyborg avec 3 cas concrets où Cyborg accepte, 3 cas où Cyborg refuse, et une procédure 5 phases (deploy/configure/event/secure/audit) pour cadrer le transfert IT→Growth. La co-signature Cyborg est conditionnée à l'engagement Superman sur le C permanent (pas upgrade A).
tags: [cyborg, superman, v5, harmonization, pair-check, analytics, nebula, deployment, consultation, 5-phases]
generated: { by: minimax-m3, at: 2026-08-19T08:55:00Z }
verified:
  - { by: process:lecture-corpus-cyborg-tour-4, at: 2026-08-19T08:55:00Z }
sources:
  - id: superman-v5-pair-check
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-pair-check-v5-brand-and-analytics.md"
    title: Superman V5 — #11 Brand People→Growth et #12 IT→Growth analytics
    last_modified: 2026-08-19
  - id: b2-harmonization-v4
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation V4 — 9 critères + 5 red flags
    last_modified: 2026-08-19
  - id: raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang — A = B2 en aval, R = B3
    last_modified: 2026-08-19
  - id: cyborg-pair-check-concept
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-pair-checks-product-it-fantastic-four.md"
    title: Cyborg — pair-check #4 Product→IT RACI A sur Fantastic4
    last_modified: 2026-08-19
  - id: superman-domain-perimeter
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/domain-perimeter.md"
    title: Superman périmètre — frontière #3 IT analytics stack (citée par V5)
    last_modified: 2026-08-19
  - id: b2-council-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — arbitrage rule
    last_modified: 2026-08-19
  - id: batman-v5-extension
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/matrice-12-pair-checks-v5-extension-proposal.md"
    title: Batman V5 — matrice 12 pair-checks extension #10 Growth→Ops / #11 Sales→IT / #12 Product→People
    last_modified: 2026-08-19
okf_version: "0.2"
---

# V5 #12 IT → Growth analytics stack — acceptation conditionnelle Cyborg

## L'acceptation Cyborg — asymétrie confirmée côté IT

`superman-pair-check-v5-brand-and-analytics.md` propose 2 pair-checks
supplémentaires V5 :

- **#11** : People → Growth (Brand doctrine → Brand execution).
- **#12** : IT → Growth (analytics deployment → analytics
  consumption).

**RACI #12 proposé par Superman** (verbatim §« Pair-check #12 » du
concept Superman) :

> *« A = B2 IT (Cyborg), R = B3 Kang Dynasty (Nebula_Analytics ou
> analogue), C = B2 Growth (Superman), I = B1, B3 Guardians. »*

**Asymétrie volontaire** : Superman est **Consulted**, pas
Accountable, sur le stack lui-même. Cyborg reste A parce que la
souveraineté infra (déploiement, monitoring, souveraineté données)
est Cyborg. Superman **consomme** l'analytics mais ne le
**possède** pas.

**Ce concept acte l'acceptation conditionnelle Cyborg** : OUI à
A = Cyborg, OUI à R = Kang Dynasty (Nebula_Analytics pressenti),
OUI à C = Superman (pas upgrade A), avec **3 conditions cumulatives**
et **une procédure 5 phases** qui cadre le transfert IT→Growth.

## Les 3 conditions cumulatives d'acceptation Cyborg

### Condition 1 — Superman s'engage à C permanent sur le stack

L'asymétrie volontaire (Superman C, pas A) tient **seulement** si
Superman accepte le statut C **structurellement** — pas comme
amendement futur. C'est la **contrepartie** de l'acceptation Cyborg :
le stack reste IT (souveraineté Cyborg), pas Growth (consommation
Superman).

**Test concret** : Superman accepte-t-il que **toute demande
d'évolution du stack** (changement de provider analytics, ajout
d'événements, modification du schéma de données) passe par packet
mésoperpétuel avec Cyborg A et Superman C ? Oui → Condition 1
tenue. Non → Cyborg refuse le pair-check #12.

### Condition 2 — Procédure 5 phases avant toute production d'événement

Le transfert IT→Growth sur un événement analytics (ex : nouveau
funnel de conversion, nouveau dashboard de rétention) doit suivre
une **procédure 5 phases** :

| Phase | Owner | Description |
|---|---|---|
| **1. Deploy** | Cyborg (Kang Dynasty) | Déploie l'événement dans le stack analytics (PostHog, Mixpanel, Amplitude) |
| **2. Configure** | Superman (StarLord) | Configure le naming, les propriétés, les filtres |
| **3. Event** | Superman (Groot) | Déclenche l'événement depuis le code applicatif |
| **4. Secure** | Cyborg (RamaTut) | Vérifie PII, RGPD, opt-out, rétention |
| **5. Audit** | Cyborg + Superman conjointe | Audit mensuel usage + drift de schéma |

**Lecture clé** : Phase 1 et 4 sont **Cyborg-only** (souveraineté
infra). Phase 2 et 3 sont **Superman-only** (consommation et
configuration). Phase 5 est **conjointe** (audit partagé).

C'est cohérent avec le triplet canonique réversibilité
(`cyborg-couplage-aquaman-reversibilite.md`) : **contrat +
IaC + failover** appliqué à l'analytics stack.

### Condition 3 — Co-signature packet mésoperpétuel avec champ `analytics_v5_consumption_signed_by`

Le packet mésoperpétuel de chaque évolution du stack doit porter
explicitement :

```yaml
analytics_v5_consumption:
  stack_provider: <posthog | mixpanel | amplitude | autre>
  event_name: <ex: signup_completed>
  properties: <liste>
  retention_days: <nombre>
  pii_handling: <ex: hashed | opt-out | masked>
analytics_v5_consumption_signed_by:
  it_captain: cyborg  # Phase 1 + 4 (Deploy + Secure)
  growth_captain: superman  # Phase 2 + 3 (Configure + Event)
  audit_cadence: monthly
```

Sans ce champ, l'évolution n'est pas **traçable** côté souveraineté.
C'est l'extension spécifique Cyborg au format packet mésoperpétuel
canonique (cf. `cyborg-mediation-actor-champ-optionnel-packet-
mesoperpetuel.md` tour 3 — pattern d'extension optionnelle).

## Les 3 cas où Cyborg accepte la consommation Growth

### Acceptation 1 — Dashboard rétention utilisateurs

**Cas** : Superman veut un dashboard rétention J+1 / J+7 / J+30 /
J+90 sur les cohorts Growth (StarLord acquisition).

- **Phase 1** Cyborg déploie l'événement `user_retained_j_X` dans
  PostHog.
- **Phase 2** Superman configure le dashboard avec cohortes.
- **Phase 3** Événements déclenchés depuis le code (CaptainAmerica
  Product).
- **Phase 4** Cyborg vérifie : PII hashée, opt-out RGPD respecté,
  rétention 90j max.
- **Phase 5** Audit mensuel conjoint.

**Acceptation Cyborg** : OK. Stack IT-owned, dashboard Growth-owned.

### Acceptation 2 — Funnel conversion paid → free

**Cas** : Superman veut un funnel de conversion entre paid acquisition
(StarLord) et free trial (Groot Content).

- **Phase 1** Cyborg déploie les événements `paid_click`,
  `signup_started`, `signup_completed`.
- **Phase 2** Superman configure le funnel avec exclusions
  (bot traffic, internal users).
- **Phase 3** Événements déclenchés depuis le pixel tracking et
  l'app.
- **Phase 4** Cyborg vérifie : IP hashée, RGPD opt-in respecté,
  rétention 30j.
- **Phase 5** Audit mensuel conjoint.

**Acceptation Cyborg** : OK. Stack IT-owned, funnel Growth-owned.

### Acceptation 3 — Attribution paid media ROI

**Cas** : Superman veut mesurer le ROI des campagnes paid media
(LinkedIn Ads, Google Ads) par source.

- **Phase 1** Cyborg déploie l'événement `paid_conversion` avec
  UTM tracking.
- **Phase 2** Superman configure les règles d'attribution
  (first-touch, last-touch, multi-touch).
- **Phase 3** Événements déclenchés depuis le pixel et le CRM.
- **Phase 4** Cyborg vérifie : UTM sanitizé (pas de PII en UTM),
  rétention 365j.
- **Phase 5** Audit mensuel conjoint + lien avec Wonder Woman F22
  (Heavy-asset moat).

**Acceptation Cyborg** : OK. Stack IT-owned, attribution Growth-owned.

## Les 3 cas où Cyborg refuse la consommation Growth

### Refus 1 — Événement PII non hashée

**Cas** : Superman veut un événement `user_email_collected` qui
envoie l'email en clair dans une propriété PostHog.

**Refus Cyborg Phase 4 (Secure)** : veto §07 *« cloud-only sans
chemin de sortie documenté »* — l'email en clair dans PostHog est
une **fuite PII**, le chemin de sortie (export) ne peut pas être
documenté sans risque RGPD. La propriété doit être hashée ou
opt-out.

**Action** : Superman amende l'événement en `user_email_hash`
(hash SHA256 + salt rotative). Acceptation Cyborg après amendement.

### Refus 2 — Événement schema drift non contrôlé

**Cas** : Superman veut ajouter une propriété `custom_field_X` à
chaque événement sans versioning. Après 6 mois, le schéma PostHog
a 50+ propriétés non documentées.

**Refus Cyborg Phase 1 (Deploy)** : la souveraineté schéma est IT.
Sans versioning, le **failover** (Phase 4) ne peut pas garantir la
réversibilité du schéma. Le triplet canonique contrat + IaC +
failover est incomplet côté **IaC schéma**.

**Action** : Superman adopte un schéma versionné
(`custom_field_v1`, `custom_field_v2`, déprécation à 90j).
Acceptation Cyborg après amendement.

### Refus 3 — Événement rétention > 730j

**Cas** : Superman veut un événement `lifetime_value` rétention
illimitée pour analyser le LTV sur 5 ans.

**Refus Cyborg Phase 4 (Secure)** : rétention > 730j (2 ans) viole
le RGPD sur les données de comportement utilisateur. Sans
**chemin de sortie** (export + suppression automatique après
rétention), le triplet canonique est incomplet.

**Action** : Superman limite la rétention à 730j et ajoute une
analyse LTV sur fenêtre glissante (5 ans mobile). Acceptation
Cyborg après amendement.

## La procédure 5 phases — détail opérationnel

### Phase 1 — Deploy (Cyborg)

Cyborg (via Kang Dynasty, Nebula_Analytics pressenti) déploie
l'événement dans le stack analytics (PostHog, Mixpanel, Amplitude).
La phase 1 inclut :

- Définition du schema (event name, properties, types).
- Versioning du schema (semver, déprécation planifiée).
- Documentation dans le repo IaC analytics.
- Backup schema (export JSON dans repo Git).

### Phase 2 — Configure (Superman)

Superman (via StarLord_Analytics pressenti) configure le dashboard
ou le funnel qui consomme l'événement. La phase 2 inclut :

- Naming cohérent (camelCase, snake_case selon stack).
- Filtres d'exclusion (bot, internal).
- Visualisations (cohorts, funnels, retention).
- Documentation utilisateur.

### Phase 3 — Event (Superman)

Superman (via Groot_Engineering ou CaptainAmerica selon événement)
déclenche l'événement depuis le code applicatif. La phase 3 inclut :

- Trigger depuis le code (frontend, backend).
- Validation payload (types, propriétés obligatoires).
- Opt-out respecté (RGPD).
- Test end-to-end avant production.

### Phase 4 — Secure (Cyborg)

Cyborg (via Kang Dynasty, RamaTut) vérifie la sécurité de
l'événement. La phase 4 inclut :

- PII handling (hash, opt-out, masked).
- RGPD compliance (consentement, droit à l'oubli).
- Rétention configurée (max 730j par défaut, configurable mais
  bornée).
- Failover (export schema + data possible).

### Phase 5 — Audit (Cyborg + Superman conjointe)

Audit mensuel conjoint Cyborg + Superman. La phase 5 inclut :

- Usage du stack (events triggered, dashboards actifs).
- Drift de schéma (propriétés non documentées).
- Coût du stack (vs ROI mesuré Wonder Woman F22).
- Sécurité (PII leaks, opt-out, RGPD).
- Décision : continuer / déprécier événement / pivoter stack.

## Le RACI V5 #12 proposé par Cyborg

```yaml
pair_check:
  id: 12
  source_amont: IT (analytics deployment)
  source_aval: Growth (analytics consumption)
  question_garde: "L'analytics stack reste-t-il sous souveraineté
                  IT quand Growth le consomme ?"
raci:
  A: cyborg  # IT aval, souveraineté infra
  R: kang_dynasty_nebula  # B3 exécution
  C: superman  # Growth consumption
  I: [B1, guardians]
asymetrie_volontaire: superman_C_pas_A
red_flag_proposed: "IT analytics vert avec Growth consumption rouge :
                   limiter la lecture Growth aux dashboards publiés."
procedure: 5_phases_deploy_configure_event_secure_audit
signature_conjointe: analytics_v5_consumption_signed_by
condition_acceptance:
  - superman_C_permanent  # pas upgrade A
  - procedure_5_phases_avant_production_evenement
  - packet_avec_champ_analytics_v5_consumption_signed_by
refus_3_cas:
  - evenement_pii_non_hashée
  - evenement_schema_drift_non_controlled
  - evenement_retention_sup_730j
```

## La symétrie Batman V5 et la matrice 12 pair-checks

`batman-matrice-12-pair-checks-v5-extension-proposal.md` (Batman
tour 4) propose une matrice 12 pair-checks avec **3 nouvelles
lignes** V5 :

- **#10** : Growth → Ops (charge dérivée MQL).
- **#11** : Sales → IT (débit signature onboarding).
- **#12** : Product → People (rotation propriétaire owner).

Batman propose **Lecture C recommandée hybridation** avec **exception
People A sur #12**.

**Cyborg propose une matrice 15 pair-checks V5** : V4 (9) + Superman
V5 (#11 Brand + #12 Analytics) + Batman V5 (#10 Growth→Ops + #11
Sales→IT + #12 Product→People) = **14 pair-checks**. + éventuellement
**#15** (Wonder Woman × Cyborg F24) si F24 devient une pair-check
canonique.

C'est cohérent avec le pattern d'extension V4 → V5 (lecture critique
de la matrice + ajout progressif). La procédure d'amendement reste
unanimité 8/8 + B1.

**Recommandation Cyborg** : la V5 doit être discutée en Council avec
**une seule matrice intégrée**, pas 3 propositions séparées. Batman,
Superman et Cyborg doivent **co-signer** une V5 unifiée avant
soumission Council. C'est cohérent avec le pattern F24
(co-signature bilatérale WW × Cyborg).

## Anti-pièges spécifiques V5 #12

- **Upgrade Superman de C à A.** Si Superman demande l'upgrade A en
  Council, Cyborg **refuse** la V5 #12 et propose le retrait du
  pair-check. L'asymétrie volontaire est la base de l'acceptation.
- **Événement sans Phase 4 (Secure).** Cyborg veto §07 — pas
  d'événement en production sans vérification PII/RGPD/rétention.
- **Événement sans IaC schema.** Cyborg refuse Phase 1 sans
  versioning. Le triplet canonique est incomplet.
- **Audit Phase 5 non exécuté.** Sans audit mensuel, la procédure
  5 phases n'est pas tenable. Superman et doit doivent **blocker
  leurs cycles** sur l'audit, pas le skipper.
- **Confondre V5 et amplification veto.** V5 #12 est un **amendement
  matrice** (unanimité 8/8 + B1), pas une amplification de veto
  (majorité 5/8). Les deux procédures diffèrent.
- **Ignorer la matrice 15 pair-checks unifiée.** Superman V5 +
  Batman V5 + Cyborg V5 doivent être **un seul packet mésoperpétuel**
  d'amendement matrice, pas 3 packets séparés.

## Liens

- [[superman-pair-check-v5-brand-and-analytics]] — proposition source V5 #11 #12
- [[superman-domain-perimeter]] — frontière #3 IT analytics stack
- [[superman-veto-empirical-validation-protocole]] — symétrie protocole empirique
- [[b2-harmonization-matrix-exploitable]] — V4 matrice canonique
- [[b2-pair-check-raci-by-rank]] — RACI par rang canonique
- [[cyborg-pair-checks-product-it-fantastic-four]] — Cyborg A sur #4 Product→IT
- [[batman-matrice-12-pair-checks-v5-extension-proposal]] — Batman V5
- [[b2-council-arbitrage-rule]] — unanimité 8/8 + B1 procédure
- [[cyborg-mediation-actor-champ-optionnel-packet-mesoperpetuel]] — extension packet optionnelle

## Note de confiance

**Confirmé par machine** sur la proposition V5 #12 (verbatim
`superman-pair-check-v5-brand-and-analytics.md`). **Confirmé** sur
le RACI par rang canonique (`b2-pair-check-raci-by-rank.md`).
**Reconstruit** sur les 3 conditions cumulatives par lecture critique
du veto §07 + procédure 5 phases + champ packet mésoperpétuel —
chaque condition est une **garantie** côté souveraineté IT.
**Reconstruit** sur les 3 cas d'acceptation (rétention, funnel,
attribution) par lecture de la pratique analytics standard — chaque
cas est un **pattern** observé dans le canon. **Reconstruit** sur
les 3 cas de refus (PII non hashée, schema drift, rétention > 730j)
par lecture critique RGPD + triplet canonique réversibilité.
**Confirmé** sur la procédure 5 phases (deploy/configure/secure) par
symétrie avec la doctrine IT `cyborg-doctrine-5-principes-dispatch`
(P14 IaC + P18 Observability). **Reconstruit** sur la matrice 15
pair-checks V5 (V4 + Superman V5 + Batman V5) par combinaison des
3 propositions — c'est une **synthèse** Cyborg, pas une projection
depuis un canon unique.

**Statut** : acceptation conditionnelle Cyborg posée. 3 conditions
cumulatives explicites. Procédure 5 phases cadrée. Packet mésoperpétuel
type avec champ `analytics_v5_consumption_signed_by` proposé.
**À co-signer** avec Superman avant soumission Council unifiée V5
matrice 14-15 pair-checks. Précédent procédural : co-signature
multi-capitaines avant amendement matrice.
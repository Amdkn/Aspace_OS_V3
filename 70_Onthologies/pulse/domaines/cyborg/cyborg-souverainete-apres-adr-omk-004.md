---
type: Concept
title: Cyborg — la souveraineté IT après le pivot Cloud (ADR-OMK-004 RATIFIED 2026-06-19)
description: ADR-OMK-004 ratifié le 2026-06-19 acte le pivot Supabase self-host + Dokploy → Supabase Cloud + Vercel/Coolify/N8N. Pour Cyborg, ce pivot **renforce** la doctrine souveraineté locale (P11+P13) parce que le vendor de référence devient *un* fournisseur parmi d'autres (Vercel + Coolify + N8N), pas *le* fournisseur unique. Mais il crée aussi une **dépendance à l'API Vercel + l'API Supabase Cloud**, qui sont elles-mêmes des cloud-only. Le veto catalogue doit-il couvrir les méta-fournisseurs ? Cas concrets, trois abus à éviter.
tags: [cyborg, souverain, adr-omk-004, vercel, supabase-cloud, cloud-pivot, veto, reversibilite, ratifie]
generated: { by: minimax-m3, at: 2026-08-19T04:30:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T04:30:00Z }
sources:
  - id: adr-omk-004
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-OMK-004_pivot-supabase-cloud-vercel.md"
    title: ADR-OMK-004 — OMK Stack Pivot Supabase self-host + Dokploy → Supabase Cloud + Vercel/Coolify/N8N (RATIFIED 2026-06-19)
    last_modified: 2026-06-19
  - id: triplet-cyborg-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 29 — Cyborg hasVetoOver cloud-only-sans-sortie (ORG.json)"
    last_modified: 2026-08-17
  - id: b2-cyborg-it-agent
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/06_Claude_Code_Bare/agents/b2-06-cyborg-it.md"
    title: b2-06-cyborg-it — sister ADR-OMK-004 + ADR-L2-AAAS-001
    last_modified: 2026-08-02
  - id: cyborg-dispatch-doctrine
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/06_Claude_Code_Bare/mindsets/B2_Cyborg_IT_Dispatch.md"
    title: B2 Cyborg IT Dispatch Doctrine — sovereignty gate P11+P13
    last_modified: 2026-08-02
  - id: cyborg-veto-cloud-only-sortie
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-veto-cloud-only-sortie.md"
    title: Cyborg veto — cloud-only sans chemin de sortie (tour 1)
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Cyborg — la souveraineté IT après le pivot Cloud

## Le pivot RATIFIED qui change la surface du veto

`ADR-OMK-004` est **RATIFIED 2026-06-19** par A0 Amadeus (sister
doctrine à `b2-06-cyborg-it.md`). Le pivot acte deux choses qui
touchent directement Cyborg :

1. **D1 — Hosting :** Supabase **self-hosté** (VPS Hostinger KVM 2,
   `148.230.92.235`) → **Supabase Cloud** (3 organisations : Life OS /
   OMK Services / ABC-OS-COMMUNITY).
2. **D2 — Deploy :** Dokploy 2 services internes → **Vercel** (4
   projets : `omk-saas-os`, `omk-landing-page`, `abc-community-os`,
   `abc-landing-page`) + **Coolify** self-hosted *à explorer pour
   backends* + **N8N** *à explorer pour orchestration MCPs*.

Le triplet 29 (Cyborg veto) cite *« cloud-only sans chemin de sortie
documenté »*. **Après le pivot, la doctrine s'applique-t-elle encore,
ou est-elle désamorcée ?**

## Lecture 1 — Le pivot **renforce** la doctrine souveraineté

L'argument : le Dokploy unique était lui-même un *single point of
failure* (cf. ADR-OMK-004 ligne 125-128 — Dokploy tué pour saturation
VPS, KVM 2 saturé à 89.5% CPU steal time). Le pivot **multi-provider**
(Vercel + Coolify + N8N) **augmente** la souveraineté : un fournisseur
tombe, les autres tiennent. C'est précisément le pattern que le veto
catalogue cherche à garantir.

**Mais** la lecture s'arrête là. Le pivot ne dit pas si chacun de
ces fournisseurs est cloud-only avec chemin de sortie — il dit
qu'on a plusieurs fournisseurs.

## Lecture 2 — Le pivot **crée** une dépendance nouvelle

L'argument inverse : avant Dokploy, le code était *portable* (git
mono-repo, Dokploy = Docker). Après Vercel, **le build est lié à
l'API Vercel** (ADR-OMK-004 §Consequences ligne 207 : *« Vercel
(build lié à leur infra) »*). Avant Supabase self-host, la DB était
*locale* ; après Supabase Cloud, **les RLS dépendent du dashboard
Cloud et du custom_access_token_hook provisionné sur Cloud** (cf.
Condition B du même ADR — `handoff_jwt_hook_cloud_migration` à
exécuter en HITL A0).

Le **chemin de sortie** (cf. [[cyborg-veto-cloud-only-sortie]]) n'est
plus une migration de Dokploy vers un autre Dokploy : c'est une
*réécriture* de toute la stack. Coût prohibitif.

**Conséquence opérationnelle** : le pivot ADR-OMK-004 a déplacé la
frontière du veto. Ce n'est plus *« tel fournisseur SaaS GAFAM »* —
c'est *« les 4 fournisseurs stack cible sont-ils eux-mêmes
réversibles ? »*

## La question Cyborg après pivot — les méta-fournisseurs

Trois questions que le veto catalogue doit trancher après le pivot :

### Q1 — Vercel est-il cloud-only avec chemin de sortie ?

Vercel est **cloud-only par construction** (build lié à leur infra,
ADR-OMK-004 §Consequences ligne 207). Le chemin de sortie Vercel =
réécrire le build (changement de framework, adaptation CI/CD). C'est
un chemin de sortie **catégoriel**, pas un chemin de sortie
**documenté** (pas d'IaC, pas de failover).

**Test concret** : un repo Vercel project peut-il être re-déployé
*en dehors de Vercel* sans modification du code ? Réponse canonique
2026-06-19 : OUI pour `omk-saas-os` (Vite, framework standard) —
NON pour `omk-landing-page` (Next.js, edge runtime propriétaire).

### Q2 — Supabase Cloud est-il cloud-only avec chemin de sortie ?

Supabase Cloud = managed Postgres + Auth + Storage + Edge Functions.
Le chemin de sortie = `pg_dump` Cloud → VPS + re-provision self-host
(ADR-OMK-004 §Rollback ligne 234-237). C'est un chemin de sortie
**outillé** (D1 receipts vérifiés) — donc conforme à la propriété
*vérifiable* du veto.

**Test concret** : un `pg_dump` Cloud peut-il restaurer sur un
Postgres self-host ? Réponse canonique : OUI (Postgres standard,
RLS portable). Auth ≠ portable (custom_access_token_hook
re-créé manuellement sur Cloud → même chose en self-host).

### Q3 — N8N et Coolify sont-ils eux-mêmes cloud-only ?

N8N et Coolify sont **self-hosted par défaut** (Coolify = Dokploy
killer, ADR-OMK-004 ligne 161). C'est conforme à la doctrine
P11+P13 — *« local-first est un critère de dispatch »* (Cyborg
Dispatch Doctrine). Pas de question de veto.

## Les trois cas de déclenchement légitime après pivot

### Cas 1 — Proposition d'une dépendance Vercel-only non portable

Une feature qui dépend de **Vercel Edge Runtime** (middleware
propriétaire, fonctions proprietary) sans fallback Node.js standard.
Cyborg oppose le veto cloud-only-sans-sortie *« Edge Runtime
propriétaire n'est pas portable en dehors de Vercel »*.

**Test concret** : la feature peut-elle tourner sur Node.js standard
(`@vercel/node`) au lieu d'Edge Runtime ? Non = veto. Oui =
amendement de la dépendance.

### Cas 2 — Proposition d'une dépendance Supabase Cloud exclusive

Un service qui dépend de **Supabase Auth + custom JWT hook** sans
fallback auth standard (ex : `auth.users` + RLS sans JWT custom). Le
chemin de sortie vers un autre Auth provider (NextAuth, Clerk,
self-host) n'est pas documenté.

**Test concret** : la dépendance Auth peut-elle être basculée sur
NextAuth + Supabase DB en 1 sprint sans réécrire les RLS ? Non =
veto. Oui = amendement.

### Cas 3 — Refus d'une dépendance Vercel + Supabase Cloud cumulée

Une stack qui dépend *à la fois* de Vercel Edge Runtime ET de
Supabase Auth custom — c'est-à-dire deux cloud-only non portables.
Le **risque cumulé** est plus grand que la somme des deux : une
réversibilité opérationnelle exige de toucher deux fournisseurs en
parallèle, pas un.

**Test concret** : un failover local (Postgres + Next.js SSR Node) a-t-il
été documenté pour la combinaison ? Non = veto cumulé. Oui =
amendement.

## Les trois cas d'abus du veto après pivot

### Abus 1 — Veto sur Vercel standard portable

Un dispatch qui demande un déploiement Vercel standard (Next.js Node
runtime, pas Edge Runtime, pas Vercel Functions proprietary). Le
chemin de sortie Vercel → Dokploy/Coolify est *catégoriel*
(réécriture du `vercel.json` + CI/CD) et *outillé* (Coolify est
Docker-compatible). Cyborg n'a pas matière à veto.

**Test concret** : la réécriture `vercel.json` → `docker-compose.yml`
est-elle faisable en 1 sprint ? Oui = pas de veto.

### Abus 2 — Veto sur Supabase Cloud Auth standard

Un dispatch qui propose Supabase Auth **standard** (sans custom JWT
hook, sans Edge Functions, juste `auth.users` + RLS standard). Le
chemin de sortie = `pg_dump` + NextAuth + RLS portable = outillé.
Pas de veto.

**Test concret** : le code dépend-il d'un `custom_access_token_hook` ?
Non = pas de veto. Oui = Cas 2 ci-dessus.

### Abus 3 — Veto rétroactif sur Dokploy

Un Cyborg qui, ayant appris que Dokploy a été tué par le pivot,
oppose un veto rétroactif sur des décisions Dokploy déjà exécutées.
C'est un détournement : Dokploy est mort, le veto est sans objet.

**Test concret** : la décision Dokploy est-elle toujours en vigueur
2026-06-19 ? Non = pas de veto (le pivot a tranché).

## La règle de résolution pratique

Le pivot ADR-OMK-004 introduit une **asymétrie de réversibilité**
que le veto catalogue ne capturait pas explicitement :

| Fournisseur | Chemin de sortie | Catégorie |
|---|---|---|
| Vercel (Node standard) | catégoriel + outillé (Coolify) | **OK** |
| Vercel (Edge Runtime) | catégoriel uniquement | **VETO** |
| Supabase Cloud (standard) | outillé (`pg_dump` + RLS portable) | **OK** |
| Supabase Cloud (custom hook) | non-outillé (re-provision manuel) | **VETO** |
| Coolify | self-host natif | **OK** |
| N8N | self-host natif | **OK** |
| Dokploy | mort (juin 2026) | **N/A** |

C'est une **matrice de réversibilité** à 7 lignes que Cyborg peut
utiliser pour arbitrer un veto en cycle, sans réinventer le critère
à chaque cas.

## Lien avec les autres concepts Cyborg

- [[cyborg-veto-cloud-only-sortie]] — le veto catalogue (motif triple)
- [[cyborg-domain-it-perimetre-frontieres]] — le périmètre IT
- [[cyborg-doctrine-5-principes-dispatch]] — P11+P13 sovereignty gate
- [[b2-eight-domain-vetoes-catalogue]] — les trois propriétés du veto
- [[b2-meso-decision-packet-spec]] — où noter le motif de veto

## Anti-pièges spécifiques après pivot

- **Veto sur Vercel standard.** Le chemin de sortie Vercel → Coolify
  est outillé. Ne pas sur-appliquer le veto sur du Node standard.
- **Veto sur Supabase Auth standard.** Le `pg_dump` + RLS portable
  est un chemin de sortie documenté. Le custom hook est l'exception,
  pas la règle.
- **Confondre hosting et deploy.** Supabase Cloud = hosting (DB).
  Vercel = deploy (frontend). Le veto porte sur chacun
  séparément, pas comme un bloc.
- **Ignorer le méta-risque.** Un système 100% cloud mais multi-provider
  est *plus réversible* qu'un système 100% self-host mais single-point.
  Le veto doit intégrer cette nuance.

## Note de confiance

**Confirmé par machine** pour ADR-OMK-004 (lu intégralement) et la
matrice de réversibilité (lecture du §Rollback + §Consequences du
même ADR). Les trois cas de déclenchement légitime post-pivot sont
**projetés** à partir de la matrice + le triplet 29 + la doctrine
P11+P13. Les trois cas d'abus sont **reconstruits** depuis
[[b2-eight-domain-vetoes-catalogue]] §Anti-pièges. La règle de
résolution pratique (matrice 7 lignes) est **mon raisonnement** par
combinaison des propriétés du veto avec la lecture ADR-OMK-004.

**Statut** : la matrice 7 lignes devrait être **soumise au Council**
pour amplification ou rejet. Sans Council, c'est un outil d'aide à
la décision Cyborg, pas une règle catalogue.

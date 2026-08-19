---
type: Concept
title: Cyborg veto — cloud-only sans chemin de sortie, déclenchement et abus
description: Le veto catalogue de Cyborg bloque tout fournisseur cloud-only sans chemin de sortie documenté. Le motif est triple (souveraineté technique, réversibilité opérationnelle, coût caché de la dépendance). Renforcé par ADR-OMK-004 + ADR-L2-AAAS-001 Levier 2 low-high tech. Trois cas concrets de déclenchement légitime, trois cas où le veto serait abusif.
tags: [b2, cyborg, veto, cloud, souverain, sortie-documentée, gafam, adr-omk-004]
generated: { by: minimax-m3, at: 2026-08-19T04:05:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T04:05:00Z }
sources:
  - id: triplet-cyborg-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 29 — Cyborg hasVetoOver cloud-only-sans-sortie"
    last_modified: 2026-08-17
  - id: org-json-veto
    resource: "C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/coach-os/ORG.json"
    title: Coach OS ORG.json — veto Cyborg verbatim
    last_modified: 2026-08-02
  - id: b2-cyborg-it-agent
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/06_Claude_Code_Bare/agents/b2-06-cyborg-it.md"
    title: b2-06-cyborg-it — Hard-veto GAFAM cloud-only (ADR-OMK-004 + ADR-L2-AAAS-001)
    last_modified: 2026-08-02
  - id: cyborg-dispatch-doctrine
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/06_Claude_Code_Bare/mindsets/B2_Cyborg_IT_Dispatch.md"
    title: B2 Cyborg IT Dispatch Doctrine — sovereignty gate P11+P13
    last_modified: 2026-08-02
  - id: veto-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — un domaine, un blocage légitime
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Cyborg veto — cloud-only sans chemin de sortie

## Le motif canonique

Triplet 29 (verbe `hasVetoOver`) :

> *« Cyborg bloque tout fournisseur cloud-only sans chemin de sortie
> documenté. »*

`b2-06-cyborg-it.md` ajoute un renforcement doctrinal :

> *« Hard-veto sur tout vendor GAFAM cloud-only (sister ADR-OMK-004
> + ADR-L2-AAAS-001 Levier 2 low-high tech) »*

Le motif est **triple** :

1. **Souveraineté technique** — un cloud-only GAFAM (Google Cloud,
   AWS, Azure, Salesforce, etc.) sans chemin de sortie documenté
   signifie qu'une décision d'arrêt, de migration ou de retrait du
   fournisseur met l'organisation en dépendance incontrôlable.
2. **Réversibilité opérationnelle** — sans chemin de sortie, le coût
   de migration est prohibitif. La réversibilité n'est pas qu'une
   clause contractuelle : c'est une **capacité technique documentée**
   (export des données, scripts de re-déploiement, alternative
   souveraine testée).
3. **Coût caché de la dépendance** — un cloud-only sans chemin de
   sortie crée un ratchet de coûts (vendor lock-in, montée en gamme
   forcée, support premium imposé). La dépense récurrente est
   *tenue par ratchet*, pas par choix.

Les trois sont **cumulatifs** : un fournisseur avec chemin de sortie
documenté mais sans souveraineté technique ne lève pas le veto, et
inversement. La règle canonique est **les trois réunis**.

## Renforcements doctrinaux

Le motif canonique du triplet 29 est renforcé par deux sources qui
l'élargissent :

- **ADR-OMK-004** (sister doctrine citée par `b2-06-cyborg-it.md`) :
  ADR OMK qui pose la souveraineté locale comme gate de dispatch.
- **ADR-L2-AAAS-001 Levier 2 low-high tech** : ADR L2 qui classifie
  les dépendances tech par levier d'impact. Levier 2 = dépendance
  systémique qu'il faut internaliser ou border.

Le `B2_Cyborg_IT_Dispatch.md` ajoute **deux principes** qui
changent le dispatch :

- **P11 Sovereignty gate** : *« Cyborg vetoes any dispatch that rents
  GAFAM dependency when a sovereign local option exists (Ollama, n8n,
  MCP). Local-first is a dispatch criterion. »*
- **P13 (renforcement)** : même règle, formulée comme gate
  d'architecture plutôt que comme gate de vendor.

## Quand le veto se déclenche (cas concrets)

Trois cas où le veto s'oppose de manière légitime :

### 1. Vendor SaaS GAFAM sans clause de réversibilité

Une proposition d'utiliser Google Workspace, Notion Cloud, Slack
Cloud, ou un service équivalent **sans** clause de réversibilité dans
le contrat. Cyborg oppose le veto avant que Batman ne commence
l'onboarding.

**Test concret :** la clause d'export des données existe-t-elle ? Le
format est-il documenté (CSV, JSON, schema ouvert) ? L'alternative
souveraine est-elle testée (NextCloud, Matrix, n8n) ? Trois oui =
chemin de sortie documenté ; un non = veto.

### 2. Managed service sans IaC (Infrastructure as Code)

Un service cloud géré (ex : RDS Aurora, BigQuery, Cloud Functions)
dont la configuration n'est **pas** décrite en Terraform/Ansible.
Sans IaC, la réversibilité n'est pas vérifiable — un audit manuel
de la config n'est pas un chemin de sortie.

**Test concret :** le repo Terraform/Ansible existe-t-il ? La
dernière migration depuis ce repo a-t-elle été tentée ? Le rollback
est-il chiffré (en minutes, pas en jours) ?

### 3. Dépendance cloud-only pour une fonction critique IT

Un service cloud-only qui tient une fonction **critique** (auth,
base de données, file de messages, monitoring) sans fallback local
documenté. Si le service tombe ou est révoqué, l'organisation n'a
pas de plan B opérationnel.

**Test concret :** un failover local est-il documenté ? Un
incident-type a-t-il été joué (game day / chaos engineering) ? Le
RTO est-il chiffré (Recovery Time Objective) ?

## Quand le veto serait abusif

Quatre cas où invoquer le veto serait un détournement de la classe
catalogue (cf. [[b2-eight-domain-vetoes-catalogue]] §Anti-pièges) :

1. **Cas spécifique sous couvert de classe.** Bloquer *ce* fournisseur
   sous couvert du veto cloud-only, alors que le chemin de sortie
   *est* documenté. C'est un blocage ad hoc, pas un veto catalogue.
2. **Cloud-with-exit-overreach.** Un fournisseur cloud (peut-être
   GAFAM) avec chemin de sortie documenté, testé, et clause
   contractuelle de réversibilité — Cyborg n'a pas matière à veto.
   Le veto porte sur l'absence de chemin de sortie, pas sur la
   présence du cloud.
3. **Veto sur du non-IT.** Un Growth (Superman) qui prend une
   dépendance GAFAM sur un canal marketing — c'est un arbitrage
   Superman, pas Cyborg. Cyborg statue sur l'infrastructure IT, pas
   sur la stack marketing.
4. **Veto rétroactif.** Cyborg qui découvre a posteriori qu'un de
   ses vetos aurait dû bloquer une décision déjà exécutée escalade
   pour relecture — pas un veto rétroactif sur l'exécution.

## Les trois propriétés canoniques (cf. veto catalogue)

Le veto Cyborg est légitime ssi les trois propriétés suivantes sont
remplies (cf. [[b2-eight-domain-vetoes-catalogue]]) :

### 1. Catégoriel

Le veto porte sur une **classe** (les fournisseurs cloud-only sans
chemin de sortie), pas sur un cas. Cyborg ne peut pas bloquer *ce*
fournisseur sous couvert de la classe — il peut bloquer *toute*
dépendance cloud-only sans chemin de sortie documenté.

### 2. Vérifiable

Le motif doit être **écrit** dans le packet mésoperpétuel ou dans
le journal Council. *« Je bloque ce fournisseur »* n'est pas
vérifiable. *« Ce fournisseur n'a pas de clause de réversibilité
contractuelle, cf. annexe 4 du contrat »* est vérifiable.

### 3. Non-négociable *au niveau mésoperpétuel*

Un capitaine B2 ne peut pas passer outre le veto d'un autre
capitaine B2. Superman (Growth) ne peut pas dire *« OK on lance
quand même, c'est une exception »*. La seule option est d'escalader
B1 pour amender la règle catalogue — et B1 ne réécrit pas les vetos
à la légère.

## La règle de résolution

Quatre issues possibles, par ordre de fréquence (cf.
[[b2-eight-domain-vetoes-catalogue]] §Règle de résolution) :

1. **Le mandat est amendé** avant le dispatch B3. Le porteur documente
   le chemin de sortie (clause contractuelle, IaC, failover
   documenté). **Résultat : arbitrage accepté, mode inchangé.**
2. **Le mandat est retiré** par B1 ou par le porteur. Le veto tient,
   le mandat est mort. **Résultat : packet mésoperpétuel avec
   `decision: blocked`, motif = veto cloud-only-sans-sortie.**
3. **Le veto est escaladé à B1** pour réécriture de la règle
   catalogue. **Résultat : `decision: escalate_to_B1`.** Très rare —
   B1 ne réécrit pas les vetos à la légère.
4. **Le veto est invalide** (manque une des trois propriétés). Le
   Council passe outre. **Résultat : packet mésoperpétuel avec note
   d'invalidation.**

## Le cas Spécial — l'amplification Cyborg

Le triplet 58 (cité par Wonder Woman concept, ligne sur
*« Wonder Woman étend »*) est **interprété par Cyborg comme une
amplification possible** : *« Wonder Woman étend la doctrine
veto-dépense avec ROI à 30 jours »* pourrait avoir un symétrique
chez Cyborg, *« Cyborg étend la doctrine veto-cloud avec date de
revue et métrique de réversibilité »*.

Cette amplification est **candidate** — elle n'est ni tranchée ni
soumise au Council. Le rapport la signale comme ouverture à B1.

## Anti-pièges spécifiques Cyborg

- **Veto sur cloud-with-exit.** Un chemin de sortie documenté lève
  le veto. Ne pas sur-appliquer.
- **Confondre cloud et GAFAM.** Le veto porte sur *cloud-only sans
  chemin de sortie*, pas sur *cloud GAFAM*. Un GAFAM avec clause
  de réversibilité + IaC + failover n'est pas veto.
- **Veto sur dépendance critique sans alternative.** Si le cloud est
  le seul moyen de tenir une fonction critique (ex : DNS root), le
  veto n'est pas applicable — c'est un arbitrage B1, pas un veto
  Cyborg.
- **Veto opposé sans ADR-OMK-004 vérifié.** Le motif cite ADR-OMK-004
  ; sans le vérifier dans le packet, le veto casse la propriété
  *vérifiable*.

## Liens

- [[b2-eight-domain-vetoes-catalogue]] — la doctrine veto applicable
- [[cyborg-domain-it-perimetre-frontieres]] — le périmètre qui légitime le veto
- [[cyborg-couplages-l0-rick-river-song-pyramide]] — la pyramide L0≥L1>L2
- [[b2-pair-check-raci-by-rank]] — Cyborg A sur #4 (Product→IT)
- [[b2-meso-decision-packet-spec]] — le format packet où le motif est écrit

## Note de confiance

**Confirmé par machine** pour le motif verbatim (triplet 29,
`ORG.json`). Les trois composantes du motif (souveraineté,
réversibilité, coût caché) sont **reconstruites** à partir de la
doctrine de dispatch (P11+P13) et de l'ADR-OMK-004 cité. Les trois
cas de déclenchement sont **projetés** depuis le triplet 29 + la
doctrine d'architecture IT — non observés en cycle réel dans le
corpus disponible. Les quatre cas d'abus sont **projetés** depuis la
matrice d'harmonisation. L'amplification candidate Cyborg (date de
revue + métrique de réversibilité) est **mon raisonnement** par
parallèle avec le triplet 58 — pas tranchée.

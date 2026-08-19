---
type: Concept
title: Cyborg — la doctrine des 5 principes de dispatch IT (Decompose, TDD, Sovereignty, IaC, Observability)
description: Cinq principes IT changent le dispatch de la squad Kang Dynasty : P2 Decompose-or-die (refuser le generaliste), P3 Test-Driven Agent Development (Iron Lad écrit les tests d'abord), P11+P13 Sovereignty gate (local-first sur GAFAM), P14+P17 IaC + atomic immutable (Terraform, sandbox, shadow-copy), P18 Observability gate (chaque dispatch produit ADR + log). Le B3 qui ne respecte pas un principe est rejeté à la gate.
tags: [cyborg, doctrine, dispatch, decompose, tdd, sovereignty, iac, observability, kang-dynasty]
generated: { by: minimax-m3, at: 2026-08-19T04:25:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T04:25:00Z }
sources:
  - id: cyborg-dispatch-doctrine
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/06_Claude_Code_Bare/mindsets/B2_Cyborg_IT_Dispatch.md"
    title: B2 Cyborg IT Dispatch Doctrine — 5 IT principles (P2, P3, P11+P13, P14+P17, P18)
    last_modified: 2026-08-02
  - id: b3-roster-kang
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B3_Warp_Core_Execution/05_IT_Cyborg_KangDynasty/01_B3_AGENT_ROSTER.md"
    title: B3 Agent Roster IT / Kang Dynasty — anti-patterns interdits
    last_modified: 2026-05-27
  - id: b2-swarm-protocol
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/05_IT_Cyborg_KangDynasty/02_B3_SWARM_SUPERVISION_PROTOCOL.md"
    title: B3 Swarm Supervision Protocol — autonomy contract, proof required
    last_modified: 2026-05-27
  - id: b2-cyborg-it-agent
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/06_Claude_Code_Bare/agents/b2-06-cyborg-it.md"
    title: b2-06-cyborg-it — sister ADR-OMK-004 + ADR-L2-AAAS-001
    last_modified: 2026-08-02
okf_version: "0.2"
---

# Cyborg — la doctrine des 5 principes de dispatch IT

## Pourquoi 5 principes et pas une seule règle

La source `02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/05_IT_Cyborg_KangDynasty/03_CYBORG_IT_PRINCIPLES.md`
pose **18 principes** IT canoniques. Le dispatch doctrine
(`B2_Cyborg_IT_Dispatch.md`) en sélectionne **5** qui changent
réellement le comportement de dispatch — les 13 autres sont
des rappels, pas des gates.

Cinq gates, cinq rejets à la gate, cinq verdicts différents.

## P2 — Decompose-or-die

> *« Scarlet Centurion refuses single-agent generalist dispatches.
> Every IT task decomposes into specialized B3s (refactor / test /
> docs) coordinated by Kang Prime. Generalist-does-everything rejected
> at gate. »*

**Effet de gate** : un dispatch qui dit *« Kang Prime fait tout »*
est rejeté. Chaque tâche IT doit être décomposée en sous-tâches
affectées à un ou plusieurs B3 de la squad Kang Dynasty :

- Lead (Kang Prime) : architecture, orchestration des sous-tâches.
- Iron Lad : greenfield, prototype, tests.
- Scarlet Centurion : spike, alt-stack, sécurité.
- Immortus : legacy, archivage, déprécation.
- Victor Timely : time-boxing, CI/CD.
- Rama-Tut : backup, disaster recovery, review.

**Cas de rejet** : *« provisionne un VPS, configure le monitoring,
backup le service, et code la CI »* — quatre charges, quatre B3
distincts. Un seul B3 sur les quatre est un rejet.

**Effet de bord** : Kang Prime est **obligatoirement** lead sur tout
dispatch. C'est une contrainte structurelle, pas un default.

## P3 — Test-Driven Agent Development

> *« Iron Lad writes integration tests BEFORE touching business code.
> No test = no dispatch. (Mirrors Ops P14.) »*

**Effet de gate** : un dispatch Iron Lad qui demande de *« coder la
feature X »* sans *« écrire le test d'intégration X »* est rejeté.

C'est l'application de TDD au B3 IT : le test est le **contrat** de
la livraison, pas un afterthought. Sans test, la livraison n'est pas
vérifiable — elle ne peut pas marquer Business Done.

**Cas de rejet** : *« Code un parser JSON pour le service Y »* sans
*« écris les tests d'intégration du parser »*. Rejet immédiat.

**Effet de bord** : Iron Lad porte les tests comme **premier livrable**.
Si le test échoue, Iron Lad remonte BLOCKED avec l'erreur, pas un
fix silencieux.

## P11 + P13 — Sovereignty gate (local-first sur GAFAM)

> *« Cyborg vetoes any dispatch that rents GAFAM dependency when a
> sovereign local option exists (Ollama, n8n, MCP). Local-first is
> a dispatch criterion. »*

**Effet de gate** : un dispatch qui propose un service GAFAM
(Google Cloud, AWS, Azure, Slack Cloud, Notion Cloud, etc.) alors
qu'une alternative souveraine existe (Ollama, n8n, MCP, NextCloud,
Matrix) est rejeté.

Le gate est **catégoriel** : la souveraineté locale est un critère
de dispatch, pas une préférence. Le veto catalogue
[[cyborg-veto-cloud-only-sortie]] est le **pendant bloquant** de ce
gate.

**Cas de rejet** : *« Provisionne un bucket Google Cloud Storage
pour les backups »* — NextCloud ou MinIO local font le job, et le
chemin de sortie Google Cloud n'est pas garanti sans IaC.

**Effet de bord** : le dispatch doctrine mentionne
ADR-OMK-004 + ADR-L2-AAAS-001 comme **sisters** qui renforcent le
gate. Ces deux ADR sont des gates L2 — leur consultation est
obligatoire avant dispatch d'une dépendance externe.

## P14 + P17 — IaC + atomic immutable

> *« Every infra dispatch via Terraform/Ansible (provisioned,
> idempotent). Sandboxed atomic changes, shadow-copy before merge.
> Direct SSH on prod = Kang canon violation (anti-pattern #1). »*

**Effet de gate** : un dispatch qui demande de modifier l'infra
**sans** Terraform/Ansible est rejeté. Le SSH manuel sur prod est
un **anti-pattern canon** (interdit par `01_B3_AGENT_ROSTER.md`
*« SSH manuel sur VPS prod sans ticket tracé »*).

**Atomic immutable** signifie : un changement = un commit =
un rollback possible. Pas de modification en place, pas de `scp`
direct, pas de `kubectl edit` prod sans backup avant.

**Cas de rejet** :

- *« Modifie la config nginx sur prod »* sans passer par Terraform.
- *« Push le code via scp sur le VPS »* sans CI/CD.
- *« Édite le DNS manuellement »* sans propagation check.

**Effet de bord** : Victor Timely porte la **CI/CD discipline**.
C'est sa charge canonique. Tout dispatch qui touche CI/CD passe par
lui.

## P18 — Observability gate

> *« Every dispatched B3 must produce an ADR entry + activity log.
> Rama-Tut runs health monitoring + backup snapshot. Unauditable
> dispatch = ungoverned, rejected. »*

**Effet de gate** : un dispatch qui ne produit **pas** une entrée
ADR (Architecture Decision Record) et un log d'activité est rejeté.
Le dispatch doit être **auditable** — sinon, il n'est pas
**gouverné**.

**Cas de rejet** : *« Exécute la migration DB »* sans ADR d'avant
(décision, alternatives, risques, RTO) et sans log d'après
(exécution, durée, incidents, vérifications).

**Effet de bord** : Rama-Tut porte le **monitoring + backup**. Sa
charge inclut la production d'entrées ADR + logs d'activité. Sans
Rama-Tut sign-off, le dispatch n'est pas clôturé.

## Le cas spécial — Sobriété Rick + A0 HITL

Deux médiations **supplémentaires** (non comptées dans les 5
principes) qui s'appliquent à certains dispatches :

- **Rick Sobriété** (A1) sur kernel/infra. Cf.
  [[cyborg-couplages-l0-rick-river-song-pyramide]].
- **A0 HITL** (B1) gate par défaut — *« No cron without A0 HITL
  (`B1_Manifesto.md` §Sobriety) »*.

Ces deux médiations sont **transverses** — elles s'ajoutent aux 5
principes, ne s'y substituent pas.

## La chaîne complète — un dispatch qui respecte les 5 principes

```
B1 mandate → Cyborg lit handoff queue
              ↓
         Kang Prime (lead) lit le Rock + DoD + JTBD
              ↓
         Décompose en sous-tâches (P2 Decompose-or-die)
              ↓
         Chaque B3 :
         ├── Iron Lad : écrit tests d'abord (P3 TDD)
         ├── Scarlet Centurion : spike / sécurité
         ├── Immortus : legacy / archivage
         ├── Victor Timely : CI/CD discipline
         └── Rama-Tut : monitoring / backup / review
              ↓
         Chaque dispatch vérifié :
         ├── P11+P13 Sovereignty : pas de GAFAM si souverain existe
         ├── P14+P17 IaC : Terraform / Ansible, pas de SSH manuel
         └── P18 Observability : ADR + log obligatoires
              ↓
         Médiations transverses si applicable :
         ├── Rick Sobriété (kernel/infra)
         ├── River Song (L0)
         └── A0 HITL (cron, kernel)
              ↓
         Proof requise (P18) :
         ├── command/log/screenshot/report/link
         └── acceptée/revise/blocked/escalate_to_B1
```

## Anti-pièges

- **5 principes comme decoration.** Les 5 principes sont des **gates
  de dispatch**, pas des slogans. Un dispatch qui en saute un est
  rejeté.
- **Generalist-does-everything.** P2 Decompose-or-die est
  **catégoriel** — un seul B3 sur quatre charges distinctes = rejet.
- **No-test no-dispatch.** P3 TDD est non-négociable. Iron Lad écrit
  les tests **avant** le code, pas après.
- **SSH manuel sur prod.** P14 anti-pattern #1. Le SSH manuel est
  Kang canon violation, pas un raccourci acceptable.
- **Dispatch unauditable.** P18 — un dispatch sans ADR + log n'est
  pas un dispatch, c'est une action hors gouvernance.
- **Sobriété Rick bypasse.** Rick Sobriété est sur le chemin
  critique pour kernel/infra. Bypasser Rick = violation Sobriété.

## Liens

- [[cyborg-domain-it-perimetre-frontieres]] — le périmètre
- [[cyborg-veto-cloud-only-sortie]] — le veto (gate bloquante)
- [[cyborg-jtbd-emit-receive-kang-dynasty]] — les paquets B3
- [[cyborg-couplages-l0-rick-river-song-pyramide]] — Sobriété Rick + A0 HITL
- [[batman-couplage-ops-it]] — la chaîne Ops�IT (Batman miroir)

## Note de confiance

**Confirmé par machine** pour les 5 principes (P2, P3, P11+P13,
P14+P17, P18) — cités verbatim par `B2_Cyborg_IT_Dispatch.md`. Le
lien P3 ↔ Ops P14 est **observé** dans la source mais **non
expliqué** (similitude déclarée, pas causalité). Les sisters
ADR-OMK-004 + ADR-L2-AAAS-001 sont **citée verbatim** mais leur
contenu détaillé n'a pas été lu en cycle. La chaîne complète
(résumée en ASCII art) est **reconstruite** à partir des 5
principes + le pipeline Rock→DoD→JTBD + les deux médiations Rick/A0.
Les anti-patterns #1 (SSH manuel), #2 (deploy sans CI/CD), #3
(modifier DNS sans propagation check) sont **citée verbatim** par
`01_B3_AGENT_ROSTER.md`.

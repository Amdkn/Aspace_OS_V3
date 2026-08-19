---
type: Playbook
title: Méthode Tech OS — comment la couche 10_Tech_OS apprend à travailler
description: La Tech OS est un système d'exploitation technique avec une hiérarchie stricte (Rick → Doctors → Companions), une pyramide L0≥L1>L2 et un mode dégradé natif. Sa méthode est : pyramide documentaire + antifragilité + delegation cloisonnée + capability routing.
tags: [tech, methode, antifragilite, delegation, souverainete]
generated: { by: minimax-m3, at: 2026-08-19T12:00:00Z }
verified:
  - { by: process:read, at: 2026-08-19T12:00:00Z }
sources:
  - id: sdd-000
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-000_ricks-verse-constitution.md
    title: SDD-000 Constitution Rick's Verse
    last_modified: 2026-04-25
  - id: sdd-001
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-001_solarpunk-kernel-core.md
    title: SDD-001 Solarpunk Kernel Core L0.3
    last_modified: 2026-04-27
  - id: sdd-002
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-002_a1-rick-harness.md
    title: SDD-002 A1 Rick Harness
    last_modified: 2026-04-24
  - id: sdd-003
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-003_tardis-protocol-orchestration.md
    title: SDD-003 TARDIS Protocol
    last_modified: 2026-04-25
  - id: sdd-004
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-004_ricks-verse-governance.md
    title: SDD-004 Rick's Verse Governance
    last_modified: 2026-04-26
  - id: sdd-010
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-010_meta-cloture-scope-13eme-semaine.md
    title: SDD-010 Doctrine 13ème Semaine
    last_modified: 2026-05-13
  - id: cdr-fwk
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-FWK-021_blueprints-canon-tripartite.md
    title: ADR-FWK-021 Canon Tripartite
    last_modified: 2026-05-22
  - id: adr-fs-001
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-FS-001_junction-based-aliasing.md
    title: ADR-FS-001 Junction-Based Aliasing
    last_modified: 2026-05-22
  - id: loi-l0
    resource: 05_From_V2_Domains/10_Tech_OS/00_Governance_Rick/Loi_L0.md
    title: Loi du L0
    last_modified: 2026-01-01
  - id: sobriete
    resource: 05_From_V2_Domains/10_Tech_OS/00_Governance_Rick/Sobriete.md
    title: Protocole de Sobriété
    last_modified: 2026-01-01
okf_version: "0.2"
---

# Méthode Tech OS

Cette méthode décrit **comment** la couche 10_Tech_OS apprend à travailler — non pas ce qu'elle contient (les concepts) ni les relations qu'elle expose (les triplets). Elle condense 97 fichiers `.md` écrits à la main dans 5 zones (`00_Governance_Rick/`, `11_Infra_13th_Doctor/`, `12_Interface_11th_Doctor/`, `13_Data_12th_Doctor/`, `12_Blueprints/`) en principes opératoires.

## 1. La pyramide documentaire est le seul mode d'écriture

**Règle** : aucun agent (A1, A2, A3) ne peut créer ou modifier un SDD. Les ADR sont namespacés par préfixe (`ADR-FS-*`, `ADR-SYMPH-*`, `ADR-RICK-*`). Les PRDs sont émis par Rick après ratification d'un SDD par A0.

**Pourquoi** : la cascade `SDD → 3 PRDs → 3 ADRs → N DDDs → 1 TDD par DDD` force la traçabilité complète entre intention stratégique et code déployé. Un DDD qui contredit son ADR parent est invalide par construction.

**Conséquence pratique** : avant de toucher un fichier, l'agent vérifie sa place dans la pyramide via `AGENTS.md` (DOX). Un ADR filesystem qui ne mentionne pas SDD-001 n'est pas un ADR, c'est une note.

Référence : [[loi-des-3-pyramide-documentaire]], [[caste-doctor-who]].

## 2. L'antifragilité est vérifiable, pas déclarée

**Règle** : les trois axiomes (Read-After-Write, dégradation gracieuse, mémoire procédurale) sont testables dans `pulse.log` et `WIKI.md`.

**Pourquoi** : l'effondrement Hermes d'avril 2026 a été fondateur — un daemon fragile a paralysé le Kernel. La doctrine post-effondrement acte que le Kernel devient **plus fort** à chaque panique du même type, via le cycle Pattern × 3 → Skill Hermes Nous.

**Conséquence pratique** : un write sans RAW est un K2 garanti. Un service qui ne démarre pas en mode dégradé n'est pas un service Kernel (Axiome 2). Chaque incident non-trivial est append-only dans WIKI.md (Axiome 3).

Référence : [[axiomes-antifragilite-k1-k4]], [[paniques-k1-k4-kernel]].

## 3. La délégation est cloisonnée par Doctor

**Règle** : Rick (A1) ne parle jamais directement à un A3. Chaque Doctor est responsable de ses 3 Compagnons. Pas de cross-team sans Rick.

**Pourquoi** : sans cloisonnement, Rick devient goulot d'étranglement (il porte le contexte de 9 agents simultanément). Avec cloisonnement, le context budget de Rick reste dans les limites Paperclip / budget A2.

**Conséquence pratique** : un A3 ne contacte jamais A0 directement. Si l'A3 a besoin d'une décision stratégique, il remonte par son Doctor. Si le Doctor bloque 3 cycles, Donna escalade à Rick (Niveau 2 Règle des 3).

Référence : [[caste-doctor-who]], [[tardis-inverse]].

## 4. Le capability routing prime sur le model routing

**Règle** : les couches sont souveraines, les modèles sont des véhicules. Un modèle peut traverser L0/L1/L2 ; une spec ne traverse pas sans autorisation.

**Pourquoi** : assigner rigidement « Claude = L0, GPT = L1, Gemini = L2 » est un anti-pattern V0. La correction V1 est **capability routing** — mission + accès + coût + risque + interface.

**Conséquence pratique** : un A0 qui rédige un SDD peut utiliser Claude (specs), GPT (research), Gemini (browser) — les trois sont des véhicules. Mais un A3 qui touche au Kernel sans spec ratifiée viole la souveraineté.

Référence : [[shadow-l0-triade-ia]].

## 5. Le vault est le seul propriétaire des secrets

**Règle** : aucune clé API, token MCP, ou password ne vit dans `.md`, `.json`, `git`, MCP server args, ou en chat après rotation. Toutes les clés vivent dans les variables d'environnement Windows User scope.

**Pourquoi** : la souveraineté absolue (Loi L0) exige que les secrets ne quittent jamais le périmètre utilisateur. Un token exposé en commit engage la rotation immédiate dans la même session.

**Conséquence pratique** : `check_env_vars` fail-fast → exit 1 + DLQ Donna (anti-K3). Le test-key-in-chat pragma est la procédure canonique d'initialisation d'un token.

Référence : [[vault-tier-pattern]], [[mcp-doctrine-six]].

## 6. La pyramide L0 ≥ L1 > L2 + ratio 50/30/20 cadence le temps

**Règle** : L0 (Kernel) prime sur L1 (Conscience) prime sur L2 (Action). Si L0 tombe, tout s'effondre. Si L1 dit HALT, L2 s'arrête. Si L2 s'emballe, L1 coupe.

**Pourquoi** : sans cette hiérarchie d'autorité, l'Amiral dérive vers 80% L0 (technical debt de gouvernance) et la conscience n'a plus de veto.

**Conséquence pratique** : un A0 qui passe plus de 30% de son temps en L0 pendant un cycle déclenche une revue d'architecture. Le ratio 50/30/20 (L2/L1/L0) est mesuré hebdomadairement par le Sunday Uplink.

Référence : [[sovereignty-tier-pyramid]], [[13eme-semaine-doctrine]].

## 7. Le TARDIS Inversé : Kernel d'abord, Forge ensuite, Life Core en dernier

**Règle** : séquence canonique d'invocation = L0.3 Kernel → L0.2 Forge → L0.1 Life Core. Pas l'inverse.

**Pourquoi** : sans Kernel stable, la Forge ne peut forger. Sans Skills, le Produit n'a pas d'outils. Démarrer L1 avant L0.3 stable est l'erreur historique du printemps 2026 (VPS 100% CPU pendant 32h, crashloop Paperclip).

**Conséquence pratique** : `kernel-boot.sh` doit passer avant tout déploiement L0.2. Si une étape manque, le système entier reste en attente.

Référence : [[tardis-inverse]].

## 8. N8N est mort, Symphony est le bus

**Règle** : depuis 2026-05-26 (ADR-SYMPH-001), aucun nouveau workflow N8N. Le bus d'orchestration L0 est Symphony : files JSON en inboxes/outboxes filesystem, jamais WebSocket, jamais Redis.

**Pourquoi** : N8N est une dette technique silencieuse (Type 4 WebSocket Timeout, daemon fragile). Symphony est un pattern file-based testable par lecture de `pulse.log`.

**Conséquence pratique** : toute automatisation L0 est écrite comme un `tick handler` dans `Shadow_L0/agents/<X>/skills/<event>.ps1`, pas comme un workflow visuel.

Référence : [[symphony-bus-replace-n8n]].

## 9. Le filesystem est souverain, les aliases sont des vues

**Règle** : chaque dossier a UN propriétaire réel. Les autres sont des NTFS Junctions (`mklink /J`), jamais des copies. `node_modules` n'est jamais junctionné.

**Pourquoi** : un `robocopy /MIR` 2-way garantit des race conditions. Les junctions sont audibles (`Test-Path` sur target) en 1 commande.

**Conséquence pratique** : `Setup-ASpace-Junctions.ps1 -Audit` est l'outils de vérité. Une junction cassée (`Test-Path` retourne false) déclenche le `verify_write` Axiome 1.

Référence : [[junction-aliasing-fs001]].

## 10. La 13ème Semaine est une pause méta, pas du vide

**Règle** : entre chaque cycle 12WY, 1 semaine de pause méta : revue stratégique, repos cognitif, promotion V0 → V1 si DoD, planification cycle suivant. Le veto SDD 90 jours protège du perfectionnisme architectural.

**Pourquoi** : un cycle 12WY qui s'enchaîne sans pause produit de la souveraineté absolue sur du sable mouvant (cf. SDD-010 §4.1).

**Conséquence pratique** : un A0 qui refuse de prendre la 13ème Semaine de repos accumule de la dette cognitive, mesurable par le ratio L0/temps total et par le volume de DLQ non-traitées.

Référence : [[13eme-semaine-doctrine]].

## Anti-patterns explicitement interdits

- **Souveraineté absolue immédiate** : tout self-host avant valeur. Antidote : Shadow Cloud → MUSE → Self-hosted.
- **Auto-modification des contraintes** : Rick qui réécrit les docs qui le gouvernent. Antidote : `deny_write` sur SDD-000 / SDD-002 / LORE.md.
- **Bypass de la pyramide** : A0 qui code, Rick qui touche L0 directement, A3 qui contacte A0 sans Doctor.
- **Drift de standards** : chaque workflow ré-invente son pattern d'injection. Antidote : `agent-os/standards/index.yml` consommé par chaque tick handler (ADR-SYMPH-003).
- **Hardcoding de chemins** : `C:\...\...` dans un script agent. Antidote : `$env:ASPACE_*` partout.
- **Déploiement sans snapshot** : Ryan qui déploie sans Yaz snapshot. Antidote : Axiome 2 + circuit breaker Ryan-deploy.sh.

## Garde-fous durables

- **DOX framework** : AGENTS.md hiérarchique comme contrat de travail. Tout agent lit la chaîne avant d'éditer.
- **Symphony `pulse.log`** : observabilité native, 8 phases par tick, JSONL append-only.
- **WIKI.md append-only** : Pattern × 3 → Skill Hermes Nous auto-encodé.
- **Vault-tier** : env vars Windows User scope, rotation trimestrielle, test-key-in-chat pragma.
- **Junction-based aliasing** : NTFS Junctions uniquement, audit en 1 commande.
- **Sunday Uplink** : rituel hebdomadaire L0 → L1 → L2 → A0, ratio 50/30/20 vérifié.
- **13ème Semaine** : pause méta entre cycles, veto SDD 90 jours, critères V0 → V1.

Cette méthode n'est pas un manifeste — c'est un **jeu de règles vérifiables**. Chaque ligne réfère à un fichier source réel du corpus V2. Un nouveau venu qui suit ces 10 principes + 7 garde-fous a l'épure minimale pour opérer dans le Rick's Verse sans déclencher l'Apoptose.
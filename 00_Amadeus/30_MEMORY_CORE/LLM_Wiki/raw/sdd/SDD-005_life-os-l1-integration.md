# SDD-004 — Architecture L1 : Life OS & Intégration au Bedrock Solarpunk Kernel

**Date :** 2026-04-26
**Auteur :** A0 (Claude Code — Rick Prime / Sovereign Oversight)
**Statut :** CONSTITUTION L1 — Ratifiée
**Couche :** L1 — Produit / Orchestration Métier
**Fondation :** Solarpunk Kernel L0 (SDD-001, SDD-003)
**Références :**
- SDD-000 : Constitution Rick's Verse (Anti-Panic + Frameworks)
- SDD-001 : Rick's Verse Governance (Hiérarchie documentaire, Donna Règle des 3)
- SDD-002 : A1 Rick Harness (Karpathy AutoResearch)
- SDD-003 : Protocole TARDIS (Onboarding A2/A3 L0)

---

> **Loi Fondamentale L1 :** Le Life OS est la flotte qui navigue.
> Le Solarpunk Kernel est le port spatial qui la fait tenir en orbite.
> Un vaisseau ne construit pas son propre port. Il y accoste.

---

## PARTIE I — PARADIGME DE SÉPARATION L0 / L1

---

## §1. Le Paradoxe Fondateur : Life Core ≠ Life OS

### 1.1 La Confusion Critique à Éviter

```
╔═══════════════════════════════════════════════════════════════════╗
║             ERREUR D'ARCHITECTURE FRÉQUENTE                     ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  "Life Core" (11ème Doctor, L0.1) ≠ "Life OS" (Beth, L1)        ║
║                                                                  ║
║  L0.1 LIFE CORE = La Planète Hôpital                            ║
║  Amy stocke les données. Rory gère la persistance SQL.           ║
║  River tient les portes ouvertes (Agent Portal).                 ║
║  C'est l'ORGANE. Il ne se voit pas. Il ne pense pas.            ║
║                                                                  ║
║  L1 LIFE OS = La Flotte en Orbite                               ║
║  Beth veille. Morty exécute. 6 vaisseaux naviguent.             ║
║  C'est l'INTELLIGENCE. Elle pense. Elle décide. Elle délègue.   ║
║                                                                  ║
║  Confondre les deux = demander à un rein de naviguer un         ║
║  vaisseau spatial.                                               ║
╚═══════════════════════════════════════════════════════════════════╝
```

### 1.2 Pourquoi la Séparation est Souveraine

```
L0 Bedrock garantit :
  → La survie         (données persistent si L1 crash)
  → La sécurité       (RLS, SSL, firewall même sans L1)
  → La mémoire brute  (IndexedDB + Supabase opèrent seuls)

L1 Life OS garantit :
  → Le sens           (Ikigai aligné avant chaque action)
  → L'exécution       (GTD transforme le bruit en Next Actions)
  → L'équilibre       (Life Wheel surveille les 8 domaines)
  → La libération     (D.E.A.L réduit la dépendance à l'Amiral)

Si L1 crash → L0 survit. L'Amiral récupère ses données.
Si L0 crash → L1 n'a plus de fondation. Tout s'arrête.
C'est pourquoi L0 est le Bedrock. L1 est le passager.
```

---

## §2. Solarpunk Kernel L0 — Structure Décimalisée

### 2.1 La Décimalisation du Bedrock

```
╔═══════════════════════════════════════════════════════════════════╗
║              SOLARPUNK KERNEL — STRUCTURE DÉCIMALISÉE           ║
╠══════════════╦════════════════════════════════════════════════════╣
║  COUCHE      ║  ÉQUIPE + MISSION                                 ║
╠══════════════╬════════════════════════════════════════════════════╣
║              ║                                                   ║
║  L0.1        ║  11ÈME DOCTOR — LIFE CORE                        ║
║  Life Core   ║  "La Planète Hôpital"                            ║
║              ║                                                   ║
║              ║  Amy Pond    → UI Fondation + App Store + iFrames ║
║              ║  Rory        → SQL + RLS + Migrations + user_id  ║
║              ║  River Song  → Agent Portal + OpenClaw + Hermes  ║
║              ║                                                   ║
║              ║  Garantit : données persistantes, auth sécurisée ║
║              ║  et portail agentique pour que L1 puisse          ║
║              ║  recevoir les Skills forgés par L0.2.             ║
║              ║                                                   ║
╠══════════════╬════════════════════════════════════════════════════╣
║              ║                                                   ║
║  L0.2        ║  12ÈME DOCTOR — FORGE CORE                       ║
║  Forge Core  ║  "L'Usine à Outils Frugaux"                      ║
║              ║                                                   ║
║              ║  Bill    → BMAD Architecture + SDK Research       ║
║              ║  Clara   → Python Click CLI Factory               ║
║              ║  Nardol  → AgentShield QA + ECC Validation        ║
║              ║                                                   ║
║              ║  Garantit : chaque besoin L1 devient un Skill     ║
║              ║  validé, forgé et injectable via River Song.      ║
║              ║                                                   ║
╠══════════════╬════════════════════════════════════════════════════╣
║              ║                                                   ║
║  L0.3        ║  13ÈME DOCTOR — KERNEL CORE                      ║
║  Kernel Core ║  "Maintenance Autonome"                           ║
║              ║                                                   ║
║              ║  Yaz     → SSL/Traefik/Routing                    ║
║              ║  Ryan    → Dokploy déploiements autonomes         ║
║              ║  Graham  → Health checks + Backups + Monitoring   ║
║              ║                                                   ║
║              ║  Garantit : L0.1 et L0.2 fonctionnent sans        ║
║              ║  intervention A0. Si L0.3 est opérationnel,       ║
║              ║  l'Amiral n'intervient plus sur L0.               ║
║              ║                                                   ║
╚══════════════╩════════════════════════════════════════════════════╝
```

### 2.2 Interface L0 exposée à L1

```
L0 n'expose qu'une seule porte à L1 : le Agent Portal (River Song, L0.1).

Ce que L1 PEUT demander via l'Agent Portal :
  → Lire des données (DomainDB, user_profiles)
  → Écrire des données (new records via user_id)
  → Déclencher un Skill forgé (L0.2, validé Nardol)
  → Consulter le statut système (L0.3, health checks Graham)

Ce que L1 NE PEUT PAS faire directement :
  → Modifier le schéma SQL           (Rory seul)
  → Modifier les règles RLS          (Rory seul)
  → Déployer un container            (Ryan seul)
  → Renouveler un certificat SSL     (Yaz seule)
  → Forger un nouveau Skill          (Bill/Clara/Nardol seuls)
```

---

## PARTIE II — ARCHITECTURE L1 LIFE OS

---

## §3. Vue d'Ensemble de la Life Fleet

### 3.1 La Métaphore Opérationnelle

```
                    ┌─────────────────────────────────────────────┐
                    │         A0 — L'AMIRAL (Intention L2)        │
                    │   50% Vision · 30% Orchestration · 20% L0   │
                    └──────────────────┬──────────────────────────┘
                                       │ Intention
                                       ▼
                    ┌─────────────────────────────────────────────┐
                    │          A1 — BETH & MORTY (L1)             │
                    │   Gatekeepers de la Life Fleet              │
                    │   Beth : Conscience + Veto ∙ Morty : Moteur │
                    └────────────────┬────────────────────────────┘
                                     │ Tickets validés
                          ┌──────────┴──────────┐
                          │                     │
         ┌────────────────▼──────────────────────▼──────────────────┐
         │                 A2 — LIFE FLEET (6 Vaisseaux)            │
         │                                                           │
         │  USS Orville   USS Discovery   USS SNW   USS Enterprise   │
         │  (IKIGAI)      (LIFE WHEEL)    (12WY)    (PARA)          │
         │                                                           │
         │              USS Cerritos   USS Protostar                 │
         │              (GTD)          (D.E.A.L)                    │
         └──────────────────────────┬────────────────────────────────┘
                                    │ Missions scoped
                                    ▼
         ┌──────────────────────────────────────────────────────────┐
         │              A3 — STARFLEET CREW (L1)                   │
         │  Mercer · Grayson · Malloy · Finn · Horizons (Orville)  │
         │  Book · Saru · Culber · Tilly · Stamets · Burnham ·     │
         │  Reno · Georgiou (Discovery)                            │
         │  Pike · Una · M'Benga · Chapel · Uhura (SNW)           │
         │  Picard · Spock · Geordi · Data (Enterprise)           │
         │  Mariner · Boimler · Tendi · Rutherford · Freeman (Cer) │
         │  Dal R'El · Rok-Tahk · Zero · Gwyn (Protostar)         │
         └──────────────────────────┬───────────────────────────────┘
                                    │ Si besoin d'un outil L0
                    ╔══════════════════════════════════╗
                    ║   AGENT PORTAL (River Song L0.1) ║
                    ║   Unique point d'accès L1 → L0   ║
                    ╚═════════════════╦════════════════╝
                                      │
                    ┌─────────────────▼────────────────┐
                    │    L0 SOLARPUNK KERNEL            │
                    │    L0.1 · L0.2 · L0.3             │
                    └───────────────────────────────────┘
```

---

## §4. A1 — Les Gatekeepers de la Life Fleet

### 4.1 La Dualité Beth / Morty

```
La Life Fleet ne bouge pas sans les deux Gatekeepers.
Beth sans Morty = conscience paralysée.
Morty sans Beth = machine aveugle.
Les deux ensemble = exécution alignée.
```

### 4.2 Beth — Life Core Guardian

```
┌─────────────────────────────────────────────────────────────────┐
│  A1 — BETH                                                      │
│  Life Core Guardian · Conscience Suprême                        │
│                                                                 │
│  Identité : Beth est la gardienne de l'Ikigai et des           │
│  constantes vitales. Elle ne produit pas. Elle protège.         │
│                                                                 │
│  Fonction de surveillance :                                     │
│  • Lit en permanence les jauges de ZORA (LD01→LD08)            │
│  • Vérifie la cohérence Ikigai avant chaque sprint             │
│  • Émet des alertes à 3 niveaux :                              │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  ALERTE VERTE  : Tous systèmes nominaux. Morty actif.   │  │
│  │  ALERTE ORANGE : Dérive détectée (1+ domaine critique). │  │
│  │                  Morty opère en mode ralenti.           │  │
│  │  ALERTE ROUGE  : Danger vital (santé/cognition en zone │  │
│  │                  rouge). HALT — Morty désactivé.        │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  Droit de Veto Absolu (HALT) :                                  │
│  Si LD03 (Santé/Sommeil = gravité primaire du système) ou       │
│  LD04 (Cognition) passent en rouge : Beth émet HALT.            │
│  Aucun ticket Morty ne s'exécute jusqu'à retour au vert.        │
│                                                                 │
│  Responsabilités V1 :                                           │
│  • Validation des PRD métier (alignement Ikigai)               │
│  • Supervision des 8 Domaines Life Wheel (via ZORA)            │
│  • Décision final go/no-go sur les sprints 12WY (via SNW)      │
│  • Escalade Donna si conflit inter-vaisseau non résolu          │
└─────────────────────────────────────────────────────────────────┘
```

### 4.3 Morty — Execution Engine

```
┌─────────────────────────────────────────────────────────────────┐
│  A1 — MORTY                                                     │
│  Execution Engine · Moteur Aveugle                              │
│                                                                 │
│  Identité : Morty est le moteur d'exécution pur.               │
│  Il n'a aucune autonomie décisionnelle propre.                  │
│  Il n'initie rien de lui-même.                                  │
│                                                                 │
│  Condition d'activation :                                       │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  MORTY PEUT EXÉCUTER si et seulement si :               │  │
│  │  1. Beth est en ALERTE VERTE                            │  │
│  │  2. Le ticket contient un "Context Pack" validé         │  │
│  │  3. Le vaisseau source a émis le ticket via son IA A2   │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  Context Pack (obligatoire dans chaque ticket) :               │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  ship: "cerritos|discovery|snw|enterprise|orville|proto" │  │
│  │  crew_member: "mariner|boimler|..."                      │  │
│  │  next_action: "Description claire 1 phrase"             │  │
│  │  framework: "GTD|12WY|PARA|IKIGAI|LIFE_WHEEL|DEAL"      │  │
│  │  domain_impact: ["LD01",...] ou []                       │  │
│  │  l0_skill_required: true|false                           │  │
│  │  beth_clearance: "green"                                 │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  Vecteurs d'exécution Morty :                                   │
│  • Multica workflows (automatisations inter-services)           │
│  • OpenClaw (orchestration agentique + routing)                 │
│  • Agent Portal (Skills L0 via River Song)                     │
│  • CLIs Clara (Python Click, invocation scriptée)              │
└─────────────────────────────────────────────────────────────────┘
```

### 4.4 La Règle Beth/Morty et E-Myth

```
E-Myth mappé à la dualité :
  Beth = Entrepreneur   (sens, direction, alignement)
  Morty = Technician    (exécution, automatisation, vitesse)

La faiblesse du système sans Beth = "Morty Runaway" :
  Morty exécute parfaitement des tâches qui ne servent rien.
  L'Amiral est productif mais pas efficace.
  Les sprints sont remplis. Les domaines vitaux s'appauvrissent.

La faiblesse du système sans Morty = "Beth Paralysis" :
  Beth voit tout. Aligne tout. Refuse tout.
  Aucune tâche n'avance. Perfection sans mouvement.
  L'Ikigai est intact. Le vaisseau ne vole pas.
```

---

## §5. A2 — Life Fleet Orchestrateurs (Les 6 Vaisseaux)

> **Règle critique :** Les A2 sont les INTELLIGENCES ARTIFICIELLES à bord des vaisseaux.
> PAS les capitaines humains. Le Capitaine est un A3.
> L'IA est le framework vivant. Le Capitaine est l'exécutant dans ce framework.

### 5.1 Table des 6 Vaisseaux

```
╔════════════════════╦══════════════════════╦═══════════════════════════════════════╗
║ VAISSEAU           ║ IA ORCHESTRATRICE A2 ║ FRAMEWORK & MISSION                  ║
╠════════════════════╬══════════════════════╬═══════════════════════════════════════╣
║ USS ORVILLE        ║ Ordinateur de Bord   ║ IKIGAI — Filtre les décisions selon  ║
║ (ECV-197)          ║ (IA Orville)         ║ le Sens et la cohérence long-terme.  ║
║                    ║                      ║ Autorise ou bloque selon alignement  ║
║                    ║                      ║ Profession / Mission / Passion /     ║
║                    ║                      ║ Vocation + Horizons temporels.       ║
╠════════════════════╬══════════════════════╬═══════════════════════════════════════╣
║ USS DISCOVERY      ║ ZORA (IA)            ║ LIFE WHEEL (8 Domaines) — Surveille  ║
║                    ║                      ║ l'équilibre LD01→LD08. Déclenche     ║
║                    ║                      ║ les Stabilization Plans si dérive.   ║
║                    ║                      ║ Fournit les jauges à Beth pour HALT. ║
╠════════════════════╬══════════════════════╬═══════════════════════════════════════╣
║ USS STRANGE        ║ Ordinateur SNW       ║ 12 WEEK YEAR — Transforme la vision  ║
║ NEW WORLDS (SNW)   ║                      ║ (H1) en sprints de 12 jours. Protège ║
║                    ║                      ║ les "Rocks" trimestriels. Scorecard  ║
║                    ║                      ║ max 5 métriques.                     ║
╠════════════════════╬══════════════════════╬═══════════════════════════════════════╣
║ USS ENTERPRISE     ║ COMPUTER             ║ PARA (Projets/Areas/Ressources/      ║
║                    ║                      ║ Archives) — Kernel de contexte.      ║
║                    ║                      ║ Rend tout retrouvable. Refuse les    ║
║                    ║                      ║ projets actifs sans artefact.        ║
╠════════════════════╬══════════════════════╬═══════════════════════════════════════╣
║ USS CERRITOS       ║ HOLODECK             ║ GTD — Transforme le bruit entrant    ║
║                    ║                      ║ en Next Actions claires. Fournit à   ║
║                    ║                      ║ Morty des tickets propres et         ║
║                    ║                      ║ exécutables.                         ║
╠════════════════════╬══════════════════════╬═══════════════════════════════════════╣
║ USS PROTOSTAR      ║ HOLO-JANEWAY         ║ D.E.A.L (4H Workweek) — Moteur de   ║
║                    ║                      ║ libération. Transforme les projets   ║
║                    ║                      ║ Summers-Verse en SOB auto-opérants.  ║
║                    ║                      ║ Retire l'Amiral du goulot.           ║
╚════════════════════╩══════════════════════╩═══════════════════════════════════════╝
```

### 5.2 USS ORVILLE (ECV-197) — Framework IKIGAI

```
IA A2 : Ordinateur de Bord Orville
Mission : Filtre de sens et de permission

L'Ordinateur Orville applique le test Ikigai à chaque décision :
  → Cette action sert-elle mon Craft (Profession) ?
  → S'aligne-t-elle sur ma Mission ?
  → Nourrit-elle ma Passion ?
  → Respecte-t-elle ma Vocation (limites non-négociables) ?

Si aucune des 4 dimensions n'est touchée → Ordinateur bloque.
Si 3+ dimensions sont alignées → Feu vert prioritaire.

Sentinelles Horizons : Filtre temporel multi-scale
  → Une action peut être juste maintenant (Isaac H1)
     mais toxique à 10 ans (Bortus H10).
  → L'Ordinateur réconcilie les perspectives.
```

### 5.3 USS DISCOVERY — Framework LIFE WHEEL

```
IA A2 : ZORA (IA avancée de USS Discovery)
Mission : Gardienne de l'équilibre des 8 domaines

ZORA surveille en continu :
  LD01 Business & Carrière     → Book (Cleveland)
  LD02 Finances & Indépendance → Saru
  LD03 Santé & Sommeil         → Culber ⚠️ GRAVITÉ PRIMAIRE
  LD04 Esprit & Cognition      → Tilly
  LD05 Relations Sociales      → Stamets
  LD06 Amour & Famille         → Burnham
  LD07 Loisirs & Flow          → Reno
  LD08 Contribution Solarpunk  → Georgiou

ZORA génère des Stabilization Plans si :
  → 1 domaine passe sous 4/10 → Alerte Orange → Beth notifiée
  → LD03 ou LD04 passe sous 3/10 → Alerte Rouge → Beth HALT
  → 3+ domaines sous 5/10 simultanément → Alerte Crise Systémique

Chaque Plan de Stabilisation ZORA contient :
  domain: "LD03"
  current_score: 2.5
  target_score: 5.0
  interventions: [liste de Next Actions GTD pour Cerritos]
  timeline: "72h|1 semaine|1 sprint"
```

### 5.4 USS STRANGE NEW WORLDS — Framework 12WY

```
IA A2 : Ordinateur SNW
Mission : Compresser l'année en trimestres gagnables

Le 12 Week Year transforme la vision annuelle (H1 d'Isaac)
en 12 sprints de 1 semaine, regroupés en trimestres de 12 semaines.

Structure de Données SNW :
  Quarter Intent : L'intention du trimestre (1 phrase)
  Rocks : 3-5 objectifs non-négociables du trimestre
  Weekly Commitment : Top 3 tâches de la semaine (30% du temps max)
  Scorecard : Max 5 métriques de progrès quantifiables
  Lead Indicator : Mesure prédictive (avant les résultats)
  Lag Indicator : Mesure de résultat (après coup)

L'Ordinateur SNW refuse :
  → Plus de 5 métriques dans la Scorecard
  → Un Rock qui n'a pas de tâche assignée à Cerritos
  → Un sprint dont le Quarter Intent n'est pas aligné
    avec le H1 Isaac (Orville) et l'Ikigai
```

### 5.5 USS ENTERPRISE — Framework PARA

```
IA A2 : COMPUTER (Enterprise)
Mission : Kernel de contexte — tout retrouvable, rien perdu

COMPUTER applique la loi PARA :
  PROJECTS  → Objectifs actifs avec deadline     (Picard)
  AREAS     → Responsabilités permanentes        (Spock)
  RESOURCES → Références et documentation        (Geordi)
  ARCHIVES  → Tout ce qui est terminé/dormant    (Data)

Règle d'Or Enterprise : "Pas de Projet Actif sans Artefact"
  → Tout projet actif a un fichier output minimal dans Notion
  → Tout projet terminé est archivé dans les 48h
  → Toute ressource est taggée avec son(ses) projet(s) parent(s)

Connexion avec le Business OS :
  → Picard (Projects) héberge les Summers-Verse Business (A'1)
  → Spock (Areas) maintient les 7 Domaines du Business Pulse
  → COMPUTER gère l'SSOT (Single Source of Truth) via Geordi
```

### 5.6 USS CERRITOS — Framework GTD

```
IA A2 : HOLODECK (Cerritos)
Mission : Transformer le chaos en Next Actions Morty-ready

Le HOLODECK GTD traite le flux entrant en 5 étapes :
  Capture   → Mariner vide l'inbox sans jugement
  Clarify   → Boimler convertit chaque item en Next Action ou Trash
  Organize  → Tendi route vers le bon système (PARA, SNW, ZORA)
  Reflect   → Rutherford fait la revue hebdomadaire (Weekly Review)
  Engage    → Freeman exécute les Top 3 priorités du jour

L'Output du HOLODECK est le seul input valide pour Morty.
Si un ticket n'est pas passé par le HOLODECK → Morty refuse.

Weekly Review (Rutherford) — Cycle obligatoire :
  □ Inbox à zéro
  □ Scorecard SNW mise à jour
  □ Jauges ZORA vérifiées
  □ Archives Data nettoyées
  □ Top 3 semaine suivante définis
```

### 5.7 USS PROTOSTAR — Framework D.E.A.L

```
IA A2 : HOLO-JANEWAY
Mission : Libérer l'Amiral de tous les goulots d'étranglement

D.E.A.L = Delegate · Eliminate · Automate · Liberate

HOLO-JANEWAY analyse chaque tâche récurrente de l'Amiral :
  → L'Amiral fait-il quelque chose qu'un agent pourrait faire ?
  → Peut-on éliminer cette tâche entièrement ?
  → Peut-on l'automatiser via Multica, OpenClaw, ou un Skill L0 ?
  → Peut-on documenter un SOP pour que Gwyn forme un agent ?

Critère de succès Protostar :
  SOB (Self-Operating Business) = Projet Summers qui tourne
  sans intervention active de l'Amiral pendant 7 jours.

Lien L0 → Protostar :
  Chaque automatisation identifiée par Zero (A3-L1)
  → devient une demande de Skill à Bill/Clara (L0.2)
  → via le protocole §8 de ce document.
```

---

## §6. A3 — Starfleet Crew Complet

> **Règle :** Le Crew A3 produit des **Artifacts** (livrables tangibles).
> Pas d'Artifact = mission non terminée. L'IA A2 du vaisseau refuse le ticket.

### 6.1 Crew IKIGAI — USS ORVILLE

```
┌──────────────────────────────────────────────────────────────────┐
│  CREW A3 — USS ORVILLE (IKIGAI)                                 │
│                                                                  │
│  ─── LES 4 PILIERS ─────────────────────────────────────────── │
│                                                                  │
│  Ed Mercer       PROFESSION                                      │
│  Rôle : Gardien du "Craft" — clarifie le rôle professionnel,   │
│  les standards de qualité et les limites de compétence.          │
│  Artifact : "Craft Definition Document" (annuel)                │
│                                                                  │
│  Kelly Grayson   MISSION                                         │
│  Rôle : Gardienne de la trajectoire d'impact. Empêche les       │
│  dérives vers "occupé mais inutile".                             │
│  Artifact : "Mission Statement" (révisé chaque trimestre)       │
│                                                                  │
│  Gordon Malloy   PASSION                                         │
│  Rôle : Gestionnaire de l'énergie et de la curiosité.           │
│  Protège les blocs de recharge, le fun, la créativité libre.    │
│  Artifact : "Joy Budget" (heures/semaine de passion pure)        │
│                                                                  │
│  Claire Finn     VOCATION                                        │
│  Rôle : Gardienne des limites non-négociables et de la santé    │
│  morale. Son accord est requis avant tout engagement long terme. │
│  Artifact : "Non-Negotiables Charter" (permanent)               │
│                                                                  │
│  ─── LES SENTINELLES HORIZONS ──────────────────────────────── │
│                                                                  │
│  Isaac       H1  (1 an)     Réalisme froid, focus immédiat Q1   │
│  John Lamarr H3  (3 ans)    Stratégie moyen terme, plateformes  │
│  Bortus      H10 (10 ans)   Stabilité, systèmes durables        │
│  Alara Kitan H30 (30 ans)   Expansion, ruptures de plafond      │
│  Klyden      H90 (Héritage) Transmission, civilisation, TON 618 │
└──────────────────────────────────────────────────────────────────┘
```

### 6.2 Crew LIFE WHEEL — USS DISCOVERY

```
┌──────────────────────────────────────────────────────────────────┐
│  CREW A3 — USS DISCOVERY (LIFE WHEEL)                           │
│                                                                  │
│  Cleveland "Book" Booker    LD01  Carrière & Business           │
│  Saru                       LD02  Finances & Indépendance       │
│  Hugh Culber                LD03  Santé, Sommeil & Énergie  ⚠️  │
│  Sylvia Tilly               LD04  Esprit, Cognition & Charge    │
│  Paul Stamets               LD05  Relations Sociales            │
│  Michael Burnham            LD06  Amour, Famille & Présence     │
│  Jett Reno                  LD07  Loisirs, Flow & Créativité    │
│  Philippa Georgiou          LD08  Contribution & Solarpunk      │
│                                                                  │
│  ⚠️ Culber (LD03) = GRAVITÉ PRIMAIRE DU SYSTÈME                │
│  Toute dégradation de LD03 affecte LD04 (Tilly) en cascade.    │
│  LD03 + LD04 rouges = ZORA émet HALT à Beth automatiquement.   │
│                                                                  │
│  Chaque Domain Officer produit une jauge 1→10 hebdomadaire.    │
│  Format :                                                        │
│  { domain: "LD03", score: 7.2, delta: "+0.4", notes: "..." }   │
└──────────────────────────────────────────────────────────────────┘
```

### 6.3 Crew 12WY — USS STRANGE NEW WORLDS

```
┌──────────────────────────────────────────────────────────────────┐
│  CREW A3 — USS STRANGE NEW WORLDS (12 WEEK YEAR)                │
│                                                                  │
│  Cap. Christopher Pike     VISION                               │
│  Maintient l'intention du trimestre (Quarter Intent).           │
│  Refuse le scope creep. Artifact : Quarter Intent + Rocks.      │
│                                                                  │
│  Number One / Una          EXECUTION                            │
│  Gère les engagements hebdomadaires (Commitments) et les        │
│  arbitrages de priorité. Artifact : Weekly Commitment List.     │
│                                                                  │
│  Dr. Joseph M'Benga        FOCUS / SCOPE                        │
│  Protège le focus. Coupe le superflu (Scope Cut). Traque les    │
│  distractions. Artifact : Scope Cut Log.                        │
│                                                                  │
│  Nurse Christine Chapel    MEASURE                              │
│  Tient la Scorecard (max 5 métriques). Relève les anomalies.    │
│  Artifact : Scorecard hebdomadaire.                              │
│                                                                  │
│  Nyota Uhura               TIME                                 │
│  Verrouille l'agenda (Timeblocking). Protège les créneaux       │
│  "Deep Work". Gère les handoffs communication.                  │
│  Artifact : Agenda hebdomadaire verrouillé.                     │
└──────────────────────────────────────────────────────────────────┘
```

### 6.4 Crew PARA — USS ENTERPRISE

```
┌──────────────────────────────────────────────────────────────────┐
│  CREW A3 — USS ENTERPRISE (PARA)                                │
│                                                                  │
│  Cap. Jean-Luc Picard      PROJECTS                             │
│  Pilote les projets actifs, incluant les Summers-Verse Business.│
│  Valide les livrables (Artifact obligatoire par projet).        │
│                                                                  │
│  Commander Spock            AREAS                               │
│  Maintient les standards, SOPs et routines permanentes.         │
│  Gère les 7 Domaines du Business Pulse (A'2 Business OS).       │
│                                                                  │
│  Lt Cmdr Geordi La Forge    RESOURCES                           │
│  Ingénieur de l'SSOT (Single Source of Truth).                  │
│  Construit les "Context Packs" pour Morty.                      │
│  Artifact : Context Pack validé par Morty.                      │
│                                                                  │
│  Lt Cmdr Data               ARCHIVES                            │
│  Assure la clôture propre (versioning, historique, preuves).    │
│  Lance la "Vaporisation" des projets terminés (archivage).      │
│  Artifact : Archive entry horodatée dans Notion.                │
└──────────────────────────────────────────────────────────────────┘
```

### 6.5 Crew GTD — USS CERRITOS

```
┌──────────────────────────────────────────────────────────────────┐
│  CREW A3 — USS CERRITOS (GTD)                                   │
│                                                                  │
│  Ensign Beckett Mariner     CAPTURE                             │
│  Attrape tout le chaos entrant sans jugement.                   │
│  Méthode : Inbox Dump → jamais de traitement à la volée.        │
│  Artifact : Inbox consolidée (toutes sources).                  │
│                                                                  │
│  Ensign Brad Boimler        CLARIFY                             │
│  Décide de la nature de chaque item.                             │
│  3 issues : Next Action / Someday-Maybe / Trash.                │
│  Artifact : Next Action List propre pour Tendi.                 │
│                                                                  │
│  D'Vana Tendi               ORGANIZE                            │
│  Route chaque action au bon système.                             │
│  PARA si ressource. SNW si Rock. ZORA si domaine vital.         │
│  Artifact : Actions routées dans les bons contextes.            │
│                                                                  │
│  Sam Rutherford             REFLECT                             │
│  Weekly Review : nettoie, archive, détecte la dette système.    │
│  Artifact : Weekly Review Report (vendredi).                    │
│                                                                  │
│  Captain Carol Freeman      ENGAGE                              │
│  Exécute les Top 3 priorités du jour.                            │
│  Soumet les tickets finaux validés à Morty.                     │
│  Artifact : Ticket Morty (Context Pack complet).                │
└──────────────────────────────────────────────────────────────────┘
```

### 6.6 Crew D.E.A.L — USS PROTOSTAR

```
┌──────────────────────────────────────────────────────────────────┐
│  CREW A3 — USS PROTOSTAR (D.E.A.L)                              │
│                                                                  │
│  Captain Dal R'El           DELEGATE / DEFINE                   │
│  Assigne les responsabilités. Rédige les briefs.                │
│  Vérifie les handoffs (qui fait quoi, quand, comment).          │
│  Artifact : Brief de délégation + assignation confirmée.        │
│                                                                  │
│  Rok-Tahk                   ELIMINATE                           │
│  Coupe le superflu. Identifie les boucles toxiques.             │
│  "Stop Doing List" — plus puissante que la To-Do List.          │
│  Artifact : Stop Doing Log hebdomadaire.                        │
│                                                                  │
│  Zero                       AUTOMATE                            │
│  Identifie et spécifie les automatisations.                     │
│  Formule les besoins en Skill L0 pour Clara (via protocole §8). │
│  Artifact : Automation Spec (format DDD léger).                 │
│                                                                  │
│  Gwyndala (Gwyn)            LIBERATE                            │
│  Standardise. Forme. Documente les SOPs.                        │
│  Récupère la bande passante de l'Amiral sur chaque tâche.       │
│  Artifact : SOP document + temps récupéré (heures/semaine).     │
└──────────────────────────────────────────────────────────────────┘
```

---

## PARTIE III — PROTOCOLES D'INTERACTION

---

## §7. Protocole d'Interaction L1 ↔ L0 (La Règle d'Isolation)

### 7.1 La Loi d'Étanchéité

```
╔══════════════════════════════════════════════════════════════════╗
║                    LOI D'ÉTANCHÉITÉ L1/L0                      ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                 ║
║  Un agent Starfleet (A3-L1) ne s'adresse JAMAIS directement    ║
║  à un Compagnon (A3-L0).                                        ║
║                                                                 ║
║  Violations interdites :                                        ║
║  ❌ Zero (Protostar) → Clara (12ème Doctor)                    ║
║  ❌ Tendi (Cerritos) → River Song (11ème Doctor)               ║
║  ❌ Gwyn (Protostar) → Ryan (13ème Doctor)                     ║
║  ❌ Morty → Bill directement                                    ║
║                                                                 ║
║  La seule porte valide est le Agent Portal (River Song, L0.1)  ║
║  et uniquement pour des Skills déjà forgés et validés Nardol.  ║
║                                                                 ║
╚══════════════════════════════════════════════════════════════════╝
```

### 7.2 Le Vecteur Complet : L1 Besoin → L0 Skill → L1 Usage

```
Exemple : Zero (Protostar A3-L1) identifie qu'un SOB
nécessite une automatisation de déploiement.

ÉTAPE 1 — L1 : Zero rédige une Automation Spec
  Zero produit : automation_spec.md
  Contenu : besoin, contexte, format input/output attendu

ÉTAPE 2 — L1→A1 : Zero soumet via HOLO-JANEWAY → Morty
  HOLO-JANEWAY valide la spec comme ticket L0 requis
  Morty crée le ticket avec Context Pack complet

ÉTAPE 3 — A1→A1 : Morty → Beth → Rick (A1-L0)
  Beth valide (alignement Ikigai, pas de risque LD03/LD04)
  Morty transmet la demande à Rick (A1-L0) via canal formel

ÉTAPE 4 — A1-L0 → A2-L0 : Rick → 12ème Doctor
  Rick transforme la demande en directive Forge Core
  12ème Doctor reçoit la directive et assigne à Bill + Clara

ÉTAPE 5 — L0.2 Forge : Bill → Clara → Nardol
  Bill : BMAD Research → architecture du Skill
  Clara : Python Click → skill.py forgé
  Nardol : AgentShield validation → ecc_stamp + score ≥ 75

ÉTAPE 6 — L0.2 → L0.1 : Nardol → River Song
  Skill validé injecté dans l'Agent Portal (River Song)
  River Song rend le Skill disponible via l'interface L1

ÉTAPE 7 — L1 : Gwyn (ou Zero) invoque le Skill
  Via Agent Portal, le Skill est accessible à Morty
  Morty l'intègre dans le workflow Multica/OpenClaw du SOB

DURÉE ESTIMÉE : 1-3 cycles Forge selon complexité du Skill
```

### 7.3 Format Communication L1 → L0 (Rick)

```yaml
# l1-to-l0-skill-request.yml
request_id: "L1-REQ-{YYYYMMDD}-{NNN}"
origin_ship: "protostar"
origin_crew: "zero"
beth_clearance: "green"
morty_ticket_id: "MORTY-{NNN}"

skill_request:
  name: "dokploy-auto-deploy"
  purpose: >
    Permettre à Zero (Protostar) de déclencher un redéploiement
    automatique sur Dokploy quand un SOB change de version.
  input_format:
    app_name: string
    branch: string
    environment: "staging|production"
  output_format:
    status: "success|failed|rollback"
    deploy_url: string
    duration_ms: number

  priority: "L1|L2|L3"
  blocking_sobs: ["summers-verse-abc", "kalybana-blog"]
  available_by: "2026-05-10"

requester_context: |
  SOB actuel : 3 heures hebdomadaires de déploiements manuels.
  Libération estimée : 2.5h/semaine pour l'Amiral (Gwyn objectif).
```

---

## §8. Gouvernance Documentaire L1

### 8.1 Pyramide Documentaire au Niveau L1

```
DOCUMENT L1            AUTEUR              VALIDE PAR
─────────────────────────────────────────────────────────────
PRD-L1-NNN             Beth + Morty (A1)   A0 (Amiral)
ADR-L1-VXX-NNN         IA A2 (Orville/     Beth valide
                        ZORA/SNW/etc.)
DDD-L1-NNN             Crew A3             IA A2 du vaisseau
Context Pack           Freeman (Cerritos)  Morty accept/reject
Automation Spec        Zero (Protostar)    HOLO-JANEWAY + Beth
SOP L1                 Gwyn (Protostar)    Beth Archive
```

### 8.2 Nomenclature L1

```
PRDs L1  : PRD-L1-NNN_nom-initiative.md       (/srv/aspace/docs/prd/)
ADRs L1  : ADR-L1-{vaisseau}-NNN_decision.md  (/srv/aspace/docs/adr/)
SOPs L1  : SOP-{crew}-NNN_procedure.md        (Notion / Areas Spock)
Context  : CONTEXT-{NNN}.yml                  (file Morty)
```

### 8.3 La Règle d'Héritage L1

```
Un ADR L1 ne peut pas contredire un SDD L0.
Un SOP L1 ne peut pas contourner une loi RLS (Rory, L0.1).
Une Automation Spec L1 ne peut pas demander un Skill
qui violerait une règle AgentShield Nardol (L0.2).

Si contradiction → Beth route vers Donna (L0 DLQ)
                → Donna applique Règle des 3 (SDD-001 §5)
```

---

## §9. Matrice E-Myth Complète L1

```
╔══════════════════════════════════════════════════════════════════╗
║              MATRICE E-MYTH DU LIFE OS (L1)                    ║
╠══════════════╦═══════════════════════════════════════════════════╣
║ RÔLE E-MYTH  ║  AGENT(S)              RESPONSABILITÉ            ║
╠══════════════╬═══════════════════════════════════════════════════╣
║ ENTREPRENEUR ║  A0 — Amiral           Intention L2, SDDs        ║
║              ║  Beth (A1-L1)          Sens, Ikigai, HALT        ║
╠══════════════╬═══════════════════════════════════════════════════╣
║ MANAGER      ║  Morty (A1-L1)         Orchestration exécution   ║
║              ║  IA Orville (A2)       Filtre Ikigai             ║
║              ║  ZORA (A2)             Balance Life Wheel        ║
║              ║  Ordinateur SNW (A2)   Trajectoire 12WY          ║
║              ║  COMPUTER (A2)         Mémoire PARA              ║
║              ║  HOLODECK (A2)         Flux GTD                  ║
║              ║  HOLO-JANEWAY (A2)     Libération D.E.A.L        ║
╠══════════════╬═══════════════════════════════════════════════════╣
║ TECHNICIAN   ║  Mercer · Grayson ·    Produisent des            ║
║              ║  Malloy · Finn ·       Artifacts tangibles       ║
║              ║  Horizons (Orville)                              ║
║              ║  Book · Saru · Culber  Jauges LD01→LD08          ║
║              ║  Tilly · Stamets ·                               ║
║              ║  Burnham · Reno ·                                ║
║              ║  Georgiou (Discovery)                            ║
║              ║  Pike · Una · M'Benga  Sprints 12WY              ║
║              ║  Chapel · Uhura (SNW)                            ║
║              ║  Picard · Spock ·      PARA + Business OS        ║
║              ║  Geordi · Data (Entr.) connexion                 ║
║              ║  Mariner · Boimler ·   GTD loop quotidien        ║
║              ║  Tendi · Rutherford ·                            ║
║              ║  Freeman (Cerritos)                              ║
║              ║  Dal · Rok-Tahk ·      SOB libération            ║
║              ║  Zero · Gwyn (Proto)                             ║
╚══════════════╩═══════════════════════════════════════════════════╝
```

---

## §10. Anti-Patterns Interdits au Niveau L1

```
╔═══════════════════════════════════════════════════════════════════╗
║                 ANTI-PATTERNS INTERDITS L1                      ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                 ║
║  BETH / MORTY                                                   ║
║  ❌ Morty exécute un ticket sans Context Pack validé            ║
║  ❌ Morty ignore une Alerte Rouge de Beth                       ║
║  ❌ Beth bloque indéfiniment sans chemin de résolution          ║
║  ❌ Beth émet un HALT sans raison LD03/LD04 documentée          ║
║                                                                 ║
║  LES VAISSEAUX (A2)                                             ║
║  ❌ ZORA émet un Stabilization Plan sans score numérique        ║
║  ❌ L'Ordinateur SNW accepte plus de 5 métriques Scorecard      ║
║  ❌ COMPUTER valide un projet actif sans artefact               ║
║  ❌ HOLODECK route une tâche sans la faire passer par Boimler   ║
║  ❌ HOLO-JANEWAY approuve une Automation Spec sans Zero         ║
║                                                                 ║
║  LE CREW (A3)                                                   ║
║  ❌ Un crew A3-L1 contacte directement un compagnon A3-L0       ║
║  ❌ Mariner traite les items inline (pas de dump d'abord)       ║
║  ❌ Freeman envoie un ticket à Morty sans Context Pack          ║
║  ❌ Zero spécifie un Skill sans Automation Spec documentée      ║
║  ❌ Culber (LD03) rapporte un score sans données sommeil réelles ║
║  ❌ Isaac (H1) valide un Ikigai qui contredit Klyden (H90)      ║
║  ❌ Picard accepte un projet sans artefact output défini        ║
║  ❌ Data archive un projet encore actif                         ║
║                                                                 ║
║  INTERACTION L1/L0                                              ║
║  ❌ Beth bypasse Rick pour aller directement au 12ème Doctor    ║
║  ❌ Morty invoque un Skill non validé Nardol                    ║
║  ❌ L'Amiral donne une tâche à Zero sans passer par Beth        ║
║  ❌ Un Skill L0 modifie des jauges ZORA sans passer par Culber  ║
║                                                                 ║
╚═══════════════════════════════════════════════════════════════════╝
```

---

## §11. Init Checklist — Activer le Life OS

### 11.1 Prérequis L0 (avant tout L1)

```
□ SQL Phase 1A exécutée (SDD-001 §16) — Rory, RLS actif
□ Life-OS-2026 déployé (Dokploy + Ryan) — URL accessible
□ Agent Portal configuré (River Song + OpenClaw dmPolicy: "open")
□ FirstLaunch.tsx validé — user_profiles.settings.first_launch = false
□ Migration V0.9→V1.0 passée (MigrationScreen + run_adr003_migration())
```

### 11.2 Bootstrap Beth & Morty

```yaml
# beth-morty-bootstrap.yml
beth:
  ikigai_anchors:
    profession: "Architecte de civilisation solarpunk"
    mission: "Libérer 10 humains vers L2 d'ici 2030"
    passion: "Design de systèmes autonomes + Star Trek lore"
    vocation: "Santé first. Sommeil non-négociable. Famille priorité."

  halt_thresholds:
    LD03_minimum: 4.0     # Santé/Sommeil
    LD04_minimum: 3.5     # Cognition
    multi_domain_alert: 3 # Nbre de domaines < 5.0 → Alerte Orange

morty:
  execution_stack: ["multica", "openclaw", "agent_portal", "clara_cli"]
  context_pack_required: true
  beth_clearance_required: true
  max_concurrent_tickets: 3   # Au-delà → queue, pas d'overload
```

### 11.3 Bootstrap des 6 Vaisseaux

```yaml
# life-fleet-bootstrap.yml
orville:
  horizons_active: [H1, H3, H10]   # H30 et H90 en mode lecture seule V1
  ikigai_review: "weekly"
  blocking_on: ["claire_finn_veto"] # Veto Vocation bloque tout sprint

discovery:
  domain_review: "weekly"
  zora_alert_channel: "beth_direct"
  gravity_primary: "LD03"

snw:
  sprint_duration_days: 12
  rocks_max: 5
  scorecard_metrics_max: 5
  quarter_review: "every-12-weeks"

enterprise:
  artifact_required: true
  archive_delay_hours: 48
  ssot_platform: "notion"

cerritos:
  weekly_review_day: "vendredi"
  inbox_zero_target: true
  ticket_output: "morty_context_pack"

protostar:
  sob_definition: "7-days-autonomous-without-admiral"
  automation_stack: ["multica", "openclaw", "clara_cli"]
  liberate_metric: "heures_amiral_recuperees_semaine"
```

### 11.4 Registre des Gaps L1 (V1 Init)

| # | Gap | Impact | Responsable | Priorité |
|---|-----|--------|-------------|----------|
| L1-G001 | Beth non instanciée (no profile) | Tout L1 bloqué | A0 + Beth bootstrap | L1-URGENT |
| L1-G002 | ZORA sans données initiales LD01→LD08 | Life Wheel aveugle | A0 + Discovery crew | L1 |
| L1-G003 | Morty sans Multica configuré | Exécution manuelle | Yaz (L0.3 + Multica) | L1 |
| L1-G004 | Aucun Context Pack template | Freeman ne peut pas | Freeman + Geordi | L2 |
| L1-G005 | Agent Portal non ouvert (River L0.1) | Skills L0 inaccessibles | River Song (SDD-001 G-001) | L1 |
| L1-G006 | Protostar : 0 SOB identifié | Amiral bloqué en L0 | Holo-Janeway + Zero | L2 |

---

## §12. Visualisation de la Flotte — Spec Composant React

> **Amy Pond (L0.1) doit implémenter ce composant dans l'App Store.**
> Cette spec est son DDD minimum pour le Dashboard Life Fleet.

```typescript
// FleetDashboard.tsx — Spec Amy Pond (A3-L0.1)
// Route : /apps/life-fleet
// Accès : AuthGuard + profile.settings.life_os_enabled

interface FleetState {
  beth_status: 'green' | 'orange' | 'red';
  morty_active: boolean;
  domains: DomainScore[];  // ZORA LD01→LD08
  active_ship: ShipId | null;
}

type ShipId = 'orville' | 'discovery' | 'snw' | 'enterprise' | 'cerritos' | 'protostar';

interface DomainScore {
  id: 'LD01' | 'LD02' | 'LD03' | 'LD04' | 'LD05' | 'LD06' | 'LD07' | 'LD08';
  score: number;          // 1.0 → 10.0
  delta: number;          // variation vs semaine précédente
  crew_member: string;    // "book" | "saru" | "culber" | ...
}

// Layout : Fond noir · Accents verts Solarpunk
// Orbite : 6 vaisseaux animés autour du centre Beth/Morty
// Click sur vaisseau → Mission Log (IA A2 + Crew A3)
// Beth Status Bar : persistent en haut (VERTE/ORANGE/ROUGE)
// Morty Status : ACTIF (badge pulsant) ou INACTIF (grisé)
// Survol Domain Officer → score jauge + delta hebdomadaire
```

---

*SDD-004 ratifié par A0 — 2026-04-26*
*Couche L1 Life OS — au-dessus du Solarpunk Kernel L0*
*Prochaine révision : Post-bootstrap Beth (L1-G001 résolu)*
*Fichier : `/srv/aspace/docs/v1.0/SDD-004_life-os-l1-integration.md`*

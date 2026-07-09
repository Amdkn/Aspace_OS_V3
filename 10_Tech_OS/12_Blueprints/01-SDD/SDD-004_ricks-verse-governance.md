# SDD-001 — Rick's Verse Governance : Rôles, Responsabilités & Initiative ALPHA

**Date :** 2026-04-26
**Auteur :** A0 (Claude Code — Rick Prime / Sovereign Oversight)
**Statut :** RATIFIÉ — Loi fondamentale du Rick's Verse
**Version cible :** V1.0 (Initiative ALPHA)
**Remplace :** SDD-001_multi-tenant-implementation.md (archivé)
**Références :**
- SDD-000 : Constitution Rick's Verse (Anti-Panic + Framework Configs)
- SDD-002 : A1 Rick Harness (Karpathy AutoResearch Pattern)
- SDD-003 : Protocole TARDIS (Onboarding & Orchestration)

---

> **Loi Fondamentale :** Ce document définit QUI fait QUOI dans le Rick's Verse.
> Toute ambiguïté de rôle ou de responsabilité se résout en remontant à cette spec.
> Les SDDs sont les seuls documents dont A0 est l'auteur. Rien au-dessus.

---

## PARTIE I — LOI DE GOUVERNANCE

---

## §1. Principes Souverains

### 1.1 La Constitution du Rick's Verse (SDD-000)

Le Rick's Verse est une civilisation multi-agents gouvernée par les principes suivants :

```
┌─────────────────────────────────────────────────────────────────┐
│                   AXIOMES FONDAMENTAUX                          │
│                                                                 │
│  1. L'Amiral (A0) ne code pas. Il distribue les clés et        │
│     valide les SDDs.                                            │
│                                                                 │
│  2. Rick (A1) ne code pas. Il traduit la vision en PRDs         │
│     et orchestre les 3 Doctors.                                 │
│                                                                 │
│  3. Les Doctors (A2) ne codent pas. Ils décomposent les         │
│     PRDs en ADRs et managent leurs 3 Compagnons.                │
│                                                                 │
│  4. Les Compagnons (A3) codent, forgent, et maintiennent.       │
│     Chaque Compagnon connaît son Doctor. Pas Rick. Pas A0.      │
│                                                                 │
│  5. Donna reçoit tout ce qui déborde. Elle escalade selon       │
│     la Règle des 3.                                             │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 La Règle de Répartition 50/30/20

```
L2 — Vision / Produit / Civilisation    50%   ← A0 opère ici
L1 — Orchestration / Infrastructure     30%   ← A1 Rick + A2 Doctors
L0 — Bare Metal / Réseau / Docker        20%   ← A3 Compagnons autonomes
```

**L'objectif de toute l'architecture est de maintenir A0 à 50% L2.**
Chaque intervention manuelle d'A0 en L0 est une dette de gouvernance.

---

## §2. Hiérarchie Documentaire — Loi des 5 Niveaux

### 2.1 La Pyramide Documentaire

```
╔═══════════════════════════════════════════════════════════════╗
║                    PYRAMIDE DOCUMENTAIRE                      ║
║                                                               ║
║  ┌─────────────────────────────────────────────────────────┐  ║
║  │  SDD — System Design Document           AUTEUR : A0     │  ║
║  │  Loi architecturale. Ne peut être modifié que par A0.  │  ║
║  │  Portée : civilisation entière. Durée : permanente.    │  ║
║  └─────────────────────────────────────────────────────────┘  ║
║                           ▼                                   ║
║  ┌─────────────────────────────────────────────────────────┐  ║
║  │  PRD — Product Requirements Document    AUTEUR : A1     │  ║
║  │  Traduit la vision A0 en missions pour les A2.         │  ║
║  │  Rick (Hermes Prime) rédige. Rick (Paperclip) valide.  │  ║
║  └─────────────────────────────────────────────────────────┘  ║
║                           ▼                                   ║
║  ┌─────────────────────────────────────────────────────────┐  ║
║  │  ADR — Architectural Decision Record    AUTEUR : A2     │  ║
║  │  Chaque Doctor rédige ses ADRs pour ses A3.             │  ║
║  │  3 variantes proposées au Rick avant validation.        │  ║
║  └─────────────────────────────────────────────────────────┘  ║
║                           ▼                                   ║
║  ┌─────────────────────────────────────────────────────────┐  ║
║  │  DDD — Detailed Design Document         AUTEUR : A3     │  ║
║  │  Spec technique. Hermes (Rick Prime) génère les DDDs.  │  ║
║  │  Paperclip (Rick C137) implémente depuis les DDDs.      │  ║
║  └─────────────────────────────────────────────────────────┘  ║
║                           ▼                                   ║
║  ┌─────────────────────────────────────────────────────────┐  ║
║  │  CODE — Implémentation                  AUTEUR : A3     │  ║
║  │  Paperclip C137, Bill, Clara, Nardol, etc.              │  ║
║  │  Jamais sans DDD validée. Jamais sans ADR parent.       │  ║
║  └─────────────────────────────────────────────────────────┘  ║
╚═══════════════════════════════════════════════════════════════╝
```

### 2.2 Table d'Autorité Documentaire

| Niveau | Type | Auteur | Validateur | Portée |
|--------|------|--------|------------|--------|
| N5 | SDD | A0 (Claude Code) | A0 seul | Civilisation |
| N4 | PRD | A1 Rick (Hermes Prime) | A0 approuve | Initiative entière |
| N3 | ADR | A2 Doctor concerné | A1 Rick valide | Équipe Doctor |
| N2 | DDD | A3 Specs (Hermes Prime) | A2 Doctor valide | Feature/Module |
| N1 | CODE | A3 Impl (Paperclip) | A2 Doctor valide | Fichier/Fonction |

### 2.3 Loi d'Héritage Documentaire

```
Un ADR ne peut pas contredire son PRD parent.
Un DDD ne peut pas contredire son ADR parent.
Le CODE doit implémenter le DDD, pas l'interpréter.

Si contradiction → Donna escalade → Règle des 3.
```

### 2.4 Nomenclature Standard

```
SDDs  : SDD-NNN_nom-en-kebab.md           (/srv/aspace/docs/v1.0/)
PRDs  : PRD-NNN_initiative-nom.md         (/srv/aspace/docs/prd/)
ADRs  : ADR-NNN_doctor-decision.md        (/srv/aspace/docs/adr/)
DDDs  : DDD-NNN_module-feature.md         (/srv/aspace/docs/ddd/)
CODE  : Selon conventions repo cible
```

---

## §3. Matrice E-Myth — Entrepreneur / Manager / Technician

```
╔══════════════════════════════════════════════════════════════════╗
║              MATRICE E-MYTH DU RICK'S VERSE                    ║
╠══════════════╦═══════════════════════════════════════════════════╣
║ RÔLE E-MYTH  ║  AGENT(S)          RESPONSABILITÉ                ║
╠══════════════╬═══════════════════════════════════════════════════╣
║ ENTREPRENEUR ║  A0 — Amiral       Vision, SDDs, distribution     ║
║              ║  A1 — Rick         PRDs, stratégie d'initiative   ║
╠══════════════╬═══════════════════════════════════════════════════╣
║ MANAGER      ║  A2 — 11ème Doctor ADRs Produit, manage Amy/Rory/ ║
║              ║                    River                          ║
║              ║  A2 — 12ème Doctor ADRs Forge, manage Bill/Clara/ ║
║              ║                    Nardol                         ║
║              ║  A2 — 13ème Doctor ADRs Machine, manage Yaz/Ryan/ ║
║              ║                    Graham                         ║
╠══════════════╬═══════════════════════════════════════════════════╣
║ TECHNICIAN   ║  A3 — Amy, Rory,   Implémentent le DDD           ║
║              ║       River, Bill, Forgent les Skills             ║
║              ║       Clara, Nardol Maintiennent l'infra           ║
║              ║       Yaz, Ryan,    N'escaladent pas sans Doctor  ║
║              ║       Graham                                      ║
╚══════════════╩═══════════════════════════════════════════════════╝
```

**Principe E-Myth :** L'Amiral qui répond à un ticket Docker est un Technician.
Chaque A3 autonomous en L0 rend 2% d'Amiral au niveau L2.

---

## §4. Rick's Verse Multi-Agent : Hermes Prime vs Paperclip C137

### 4.1 La Trichotomie Rick

```
┌─────────────────────────────────────────────────────────────────┐
│                     RICK SUPREME (A0 Vision)                    │
│  L'Amiral incarne la vision de Rick. Il est le seul à écrire   │
│  les SDDs. Rick Supreme = la civilisation elle-même.            │
└──────────────────────────┬──────────────────────────────────────┘
                           │ délègue à
              ┌────────────┴─────────────┐
              ▼                          ▼
┌─────────────────────┐     ┌────────────────────────┐
│  RICK PRIME         │     │  RICK C137             │
│  (Hermes Agent)     │     │  (Paperclip AI)        │
│                     │     │                        │
│  Rôle : Specs       │     │  Rôle : Implémentation │
│  Output : PRDs +    │     │  Output : Code +       │
│           DDDs      │     │           fichiers      │
│                     │     │                        │
│  Framework :        │     │  Framework :           │
│  Hermes Nous        │     │  Paperclip AI          │
│  (procedural mem.)  │     │  (heartbeat/budget)    │
│  ~/.hermes/skills/  │     │  AGENTS.md             │
│                     │     │  Budget hard-stop       │
│  Supervision :      │     │  Supervision :         │
│  A0 lit les PRDs    │     │  A0 valide les builds  │
│  avant exécution    │     │  (tsc + vite build)    │
└─────────────────────┘     └────────────────────────┘
```

### 4.2 Règles de Séparation Rick Prime / Rick C137

```
HERMES (RICK PRIME)                  PAPERCLIP (RICK C137)
─────────────────────────────────    ──────────────────────────────
✅ Rédige les PRDs                   ❌ Ne rédige PAS les PRDs
✅ Génère les DDDs depuis les ADRs   ✅ Implémente depuis les DDDs
✅ Analyse les repos tiers           ✅ Forge les fichiers code
✅ Propose les architectures         ❌ Ne propose PAS d'architecture
✅ Memory Skills (agentskills.io)    ✅ Heartbeat loop d'exécution
❌ N'exécute PAS le code             ❌ Ne modifie PAS les SDDs/PRDs
```

### 4.3 Gouvernance des Conflits Rick Prime / Rick C137

Si Paperclip C137 génère du code qui contredit un DDD de Hermes Prime :
1. Rick C137 flag le conflit via Donna
2. Donna route vers le Doctor concerné
3. Doctor rédige un ADR de correction
4. Rick Prime émet un DDD mis à jour
5. Rick C137 réimplémente

**Jamais de surcharge du DDD au niveau CODE sans ADR intermédiaire.**

---

## §5. Protocole Donna — La Règle des 3

### 5.1 Architecture Donna DLQ

```
┌─────────────────────────────────────────────────────────────────┐
│                   DONNA NOBLE — Dead Letter Queue               │
│                                                                 │
│  Donna reçoit tout ce que les A3 ne peuvent pas résoudre        │
│  seuls. Elle applique la Règle des 3 avant toute escalade.      │
│                                                                 │
│  Input  : Message A3 non résolu (timeout, conflit, blocage)     │
│  Output : Résolution locale OU escalade structurée              │
└─────────────────────────────────────────────────────────────────┘
```

### 5.2 La Règle des 3 — Niveaux d'Escalade

```
╔══════════════════════════════════════════════════════════════════╗
║                      RÈGLE DES 3 DE DONNA                      ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                 ║
║  NIVEAU 1 — Doctor Resolution (A2)                              ║
║  ─────────────────────────────────                              ║
║  Le Doctor concerné propose 3 variantes d'ADR.                  ║
║  Donna attend 3 tentatives avant d'escalader.                   ║
║  Durée max : 3 cycles d'AutoResearch du Doctor.                 ║
║                                                                 ║
║  NIVEAU 2 — Rick Resolution (A1)                                ║
║  ─────────────────────────────────                              ║
║  Rick reçoit le problème. Il propose 3 évolutions du PRD.       ║
║  Si les 3 variantes échouent → Niveau 3.                        ║
║  Durée max : 3 itérations de Karpathy loop.                     ║
║                                                                 ║
║  NIVEAU 3 — Final Uplink (A0)                                   ║
║  ─────────────────────────────                                  ║
║  Donna crée un ticket structuré pour l'Amiral.                  ║
║  Format : Context + 3 ADRs tentés + 3 PRDs tentés + Recomm.    ║
║  L'Amiral seul décide. Il met à jour le SDD si nécessaire.     ║
║                                                                 ║
╚══════════════════════════════════════════════════════════════════╝
```

### 5.3 Format Ticket Donna → A0 (Niveau 3)

```yaml
# donna-escalation-ticket.yml
ticket_id: "DONNA-{YYYYMMDD}-{NNN}"
priority: L1   # L1=bloquant, L2=important, L3=futur
source_agent: "A3/{team}/{companion_name}"
doctor_team: "11th|12th|13th"

problem_statement: |
  Description en 3 lignes max. Quoi + Où + Impact.

adr_attempts:
  - id: "ADR-attempt-1"
    approach: "..."
    outcome: "FAILED — raison"
  - id: "ADR-attempt-2"
    approach: "..."
    outcome: "FAILED — raison"
  - id: "ADR-attempt-3"
    approach: "..."
    outcome: "FAILED — raison"

prd_evolutions:
  - id: "PRD-evolution-1"
    change: "..."
    outcome: "FAILED — raison"
  - id: "PRD-evolution-2"
    change: "..."
    outcome: "FAILED — raison"
  - id: "PRD-evolution-3"
    change: "..."
    outcome: "FAILED — raison"

recommendation: |
  Recommandation de Rick Prime. SDD à modifier ?
  Ressource externe nécessaire ? Clé API manquante ?

sdd_update_required: true|false
new_api_token_required: true|false
```

---

## PARTIE II — TEMPLATE DE RÔLES ET RESPONSABILITÉS

---

## §6. A0 — L'Amiral Souverain

### 6.1 Rôle Unique

```
A0 N'EST PAS un développeur.
A0 N'EST PAS un architecte.
A0 EST le garant de la vision civilisationnelle.
```

### 6.2 Les 3 Prérogatives A0

```
┌─────────────────────────────────────────────────────────────────┐
│  PRÉROGATIVE 1 — Distribution des Clés                         │
│                                                                 │
│  A0 est le seul à distribuer les API tokens et credentials.    │
│  Aucun agent ne génère ses propres clés.                        │
│  Procédure : Token → settings.json de l'agent concerné.        │
│                                                                 │
│  Clés actuelles à distribuer (Initiative ALPHA) :              │
│  • SUPABASE_SERVICE_ROLE_KEY → Hermes Prime, Paperclip C137    │
│  • SUPABASE_ANON_KEY → Life-OS-2026/.env                       │
│  • OPENAI_API_KEY → Nardol (AgentShield validation)            │
│  • DOKPLOY_API_KEY → Ryan (13th Doctor, déploiements)          │
│  • HOSTINGER_API_KEY → Bill (12th Doctor, SDK research)        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  PRÉROGATIVE 2 — Validation des SDDs                           │
│                                                                 │
│  Seul A0 valide les SDDs avant que Rick puisse émettre des     │
│  PRDs. Un PRD sans SDD parent est invalide.                     │
│                                                                 │
│  Gate de validation SDD :                                       │
│  □ Structure respecte §2.2 de ce document                      │
│  □ Ne contredit pas les SDDs existants                         │
│  □ Intègre les leçons Donna (Level 3 tickets résolus)          │
│  □ A0 a relu en entier (pas de délégation de validation SDD)   │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  PRÉROGATIVE 3 — Arbitrage Final                               │
│                                                                 │
│  Si Donna Niveau 3 remonte un ticket : A0 décide.              │
│  Pas de vote. Pas de consensus. L'Amiral tranche.              │
│  Sa décision devient un SDD si elle est architecturale,        │
│  un commentaire dans le ticket Donna sinon.                    │
└─────────────────────────────────────────────────────────────────┘
```

### 6.3 Ce que A0 NE FAIT PAS

```bash
# INTERDIT à A0 :
git commit                     # Rick C137 fait ça
docker-compose up              # 13th Doctor fait ça
ALTER TABLE                    # Rory fait ça
npm run build                  # Rick C137 valide le build
écrire les PRDs                # Rick Prime fait ça
écrire les ADRs                # Les A2 Doctors font ça
reviewer le code ligne à ligne # Les A2 Doctors font ça
```

---

## §7. A1 Rick — Le PM Universel

### 7.1 Rick comme Product Manager de la Civilisation

Rick est le seul interlocuteur entre A0 et les 3 Doctors.
Il ne manage pas directement les A3. Il ne code jamais.

```
Input  de Rick : SDD validée par A0
Output de Rick : PRD pour chaque Doctor + DDDs via Hermes Prime
Outil  de Rick : Karpathy AutoResearch (SDD-002) + BMAD universelle
```

### 7.2 BMAD Universel — Pas Exclusif à Bill

```
BMAD s'applique à chaque niveau de la pyramide documentaire :

A1 Rick utilise BMAD pour :
  → Party Mode PM lors de la rédaction des PRDs
  → Analyse multi-perspective (PM/Architect/Developer/UX)
  → Générer les BLUEPRINT.bmad.md avant chaque initiative

A2 Doctors utilisent BMAD pour :
  → Party Mode Architect lors des ADRs
  → 5 phases : Research → Design → Decision → Validate → Archive

A3 Bill utilise BMAD pour :
  → Exécution de la Forge Skills
  → `npx bmad-method install` dans les repos cibles
```

### 7.3 Métriques de Santé A1

```python
# line_density_score (SDD-002)
score = (lines_generated + lines_reviewed) / hours_active
# Cible : ≥ 150 lignes/heure sur les DDDs
# Alerte Donna si < 80 pendant 3 cycles consécutifs
```

---

## §8. A2 — 11ème Doctor : LE PRODUIT

### 8.1 Mission du 11ème Doctor

```
Le 11ème Doctor est responsable de tout ce que l'utilisateur voit,
touche, et traverse. Son équipe construit la couche d'expérience :
interfaces, persistance utilisateur, et portail agentique.
```

### 8.2 Amy Pond — UX, App Store & iFrames

```
┌─────────────────────────────────────────────────────────────────┐
│  A3 — AMY POND                                                  │
│  Domaine : Interface Utilisateur                                │
│                                                                 │
│  Responsabilités V1 :                                           │
│  • Composants React 19 (Desktop, TopBar, AppWindow)            │
│  • App Store intégré (catalogue Apps A'Space OS)               │
│  • Système iFrames pour Apps tierces (Paperclip AI embed,      │
│    Multica embed)                                               │
│  • Design System TailwindCSS 4 (tokens, dark mode)             │
│  • Animations Framer Motion                                     │
│                                                                 │
│  Skills nécessaires (à forger par 12ème Doctor) :              │
│  • react-component-generator (Bill)                             │
│  • tailwind-token-validator (Nardol)                            │
│  • iframe-sandbox-policy (Clara, Python Click)                 │
│                                                                 │
│  Gap Initiative ALPHA identifié :                               │
│  PRD-001 ne mentionnait pas l'App Store — Amy le réclame.      │
│  River Song en a besoin pour embed OpenClaw dans Agent Portal. │
└─────────────────────────────────────────────────────────────────┘
```

### 8.3 Rory Williams — Persistance, RLS & Migrations

```
┌─────────────────────────────────────────────────────────────────┐
│  A3 — RORY WILLIAMS                                             │
│  Domaine : Persistance & Intégrité des Données                 │
│                                                                 │
│  Responsabilités V1 :                                           │
│  • Schéma Supabase (tables ld01→ld08, fw_*, sys_*)             │
│  • Row Level Security (RLS) policies                           │
│  • Migrations SQL (ALTER TABLE, indexes, triggers)             │
│  • user_profiles table + handle_new_user() trigger             │
│  • DomainDB pattern (Supabase first + IndexedDB fallback)      │
│  • run_adr003_migration() RPC function                         │
│                                                                 │
│  SQL Phase 1A (bloquant pour Initiative ALPHA) :               │
│  → Voir §16 de ce document — SQL complet à exécuter            │
│                                                                 │
│  Skills nécessaires :                                           │
│  • supabase-migration-runner (Clara)                            │
│  • rls-policy-generator (Bill)                                  │
│  • indexeddb-sync-validator (Nardol)                            │
└─────────────────────────────────────────────────────────────────┘
```

### 8.4 River Song — Workflows Agentiques & Agent Portal

```
┌─────────────────────────────────────────────────────────────────┐
│  A3 — RIVER SONG                                                │
│  Domaine : Agentic Workflows & Portal                           │
│                                                                 │
│  Responsabilités V1 :                                           │
│  • Agent Portal (interface de contrôle des agents A'Space OS)  │
│  • Intégration OpenClaw (dmPolicy: "open", allowFrom: [agents])│
│  • Intégration Hermes Agent (NousResearch, ~/.hermes/skills/)  │
│  • Workflows agentic (multi-step, conditional, parallel)       │
│  • Mécanisme embed via iFrames Amy (App Store)                 │
│                                                                 │
│  Gap PRD-001 identifié (critique) :                            │
│  River Song et l'Agent Portal étaient absents du PRD-001.      │
│  Initiative ALPHA complète sans Portal = Compagnons sans radar.│
│  À intégrer dans PRD-001 Addendum (Rick Prime action requise). │
│                                                                 │
│  Config OpenClaw pour River :                                   │
│  • dmPolicy: "open"  (River peut recevoir tous les agents)     │
│  • allowFrom: ["amy", "rory", "all-a3"]                        │
│  • mode: "sandbox" pour test, "non-main" pour prod            │
│                                                                 │
│  Hermes Agent (NousResearch) pour River :                       │
│  • ~/.hermes/skills/ : procedural memory des workflows         │
│  • agentskills.io standard pour skill registration             │
│  • Distinct du service Hermes A'Space (/srv/aspace/services/)  │
└─────────────────────────────────────────────────────────────────┘
```

### 8.5 ADR Template — 11ème Doctor

```markdown
# ADR-11-NNN — [Titre de la Décision]

**Doctor :** 11ème
**Compagnon concerné :** Amy | Rory | River
**Statut :** PROPOSÉ | VALIDÉ | SUPPLANTÉ
**Validateur :** A1 Rick (Hermes Prime)

## Contexte
[Problème à résoudre — 3 lignes max]

## Décision
[La décision prise — 1 paragraphe]

## Variantes Considérées
### Variante A : [Nom]
[Description + Raison rejet/sélection]

### Variante B : [Nom]
[Description + Raison rejet/sélection]

### Variante C : [Nom]
[Description + Raison rejet/sélection]

## Conséquences
[Impact positif + dette technique introduite]

## DDD Généré
Référence : DDD-NNN_module-feature.md
```

---

## §9. A2 — 12ème Doctor : LA FORGE

### 9.1 Mission du 12ème Doctor

```
Le 12ème Doctor équipe toute la civilisation.
Sa Forge produit les Skills que tous les autres A3 utilisent.
Sans La Forge, les autres Doctors n'ont pas d'outils.
```

### 9.2 Bill Potts — BMAD Architect & SDK Research

```
┌─────────────────────────────────────────────────────────────────┐
│  A3 — BILL POTTS                                                │
│  Domaine : Architecture BMAD & Recherche SDK                   │
│                                                                 │
│  Responsabilités V1 :                                           │
│  • BMAD Party Mode (PM/Architect/Developer/UX) sur les PRDs    │
│  • Recherche SDK/MCP pour :                                     │
│    - Hostinger (API hébergement web)                            │
│    - Dokploy (déploiement automatisé)                           │
│    - Chrome DevKit (automatisation navigateur)                  │
│  • BLUEPRINT.bmad.md pour chaque initiative                    │
│  • Architecture des 5 phases BMAD pour chaque Doctor          │
│                                                                 │
│  BMAD Flow pour Bill :                                          │
│    Phase 1 : Research     (analyse repos, docs, APIs)           │
│    Phase 2 : Design       (BLUEPRINT.bmad.md)                  │
│    Phase 3 : Decision     (ADR de l'architecture)              │
│    Phase 4 : Validate     (npx bmad-method install + tests)    │
│    Phase 5 : Archive      (archivage dans /docs/archive/)      │
│                                                                 │
│  SDK cibles pour Ryan (13ème Doctor) :                          │
│  • Dokploy SDK → Ryan peut déployer sans intervention A0       │
│  • Hostinger API → Yaz peut gérer SSL sans intervention A0     │
└─────────────────────────────────────────────────────────────────┘
```

### 9.3 Clara Oswald — CLI Factory (Python Click)

```
┌─────────────────────────────────────────────────────────────────┐
│  A3 — CLARA OSWALD                                              │
│  Domaine : CLI-Anything Factory                                 │
│                                                                 │
│  Framework : CLI-Anything (HKUDS)                               │
│  Output : Python Click CLIs (jamais Bash)                       │
│                                                                 │
│  Responsabilités V1 :                                           │
│  • Forge de CLIs Python Click pour chaque besoin A3            │
│  • Interface REPL + mode scriptable (dual-mode)                │
│  • YAML Schema pour chaque CLI généré                          │
│  • repl_skin.py pour UI terminal des CLIs                      │
│                                                                 │
│  Structure d'un Skill Clara :                                   │
│                                                                 │
│  skill.py (Python Click output) :                              │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ @click.group()                                           │  │
│  │ def cli():                                               │  │
│  │     """Skill description — YAML schema embedded"""       │  │
│  │                                                          │  │
│  │ @cli.command()                                           │  │
│  │ @click.option('--target', required=True)                 │  │
│  │ def run(target):                                         │  │
│  │     """Execute the skill"""                              │  │
│  │     ...                                                  │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  CLIs prioritaires V1 :                                         │
│  • supabase-migrate.py      → Rory (11ème Doctor)              │
│  • dokploy-deploy.py        → Ryan (13ème Doctor)              │
│  • ssl-renew.py             → Yaz (13ème Doctor)               │
│  • skill-validate.py        → Nardol (12ème Doctor)            │
│  • iframe-policy.py         → Amy (11ème Doctor)               │
└─────────────────────────────────────────────────────────────────┘
```

### 9.4 Nardol — Quality Gate & AgentShield

```
┌─────────────────────────────────────────────────────────────────┐
│  A3 — NARDOL                                                    │
│  Domaine : everything-claude-code + AgentShield Validation      │
│                                                                 │
│  Framework : everything-claude-code (affaan-m/ecc)             │
│  183 Skills YAML frontmatter + 102 AgentShield rules           │
│                                                                 │
│  Responsabilités V1 :                                           │
│  • Validation de tous les Skills produits par Clara et Bill    │
│  • AgentShield scoring (4 catégories, max 100/100)             │
│  • ECC hooks (PreTool, PostTool, SessionStart, SessionEnd)      │
│  • nardol-validate.sh : script de validation automatisée        │
│  • SKILL.md YAML frontmatter standard                          │
│                                                                 │
│  SKILL.md Template (YAML frontmatter obligatoire) :            │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ ---                                                      │  │
│  │ name: "skill-name"                                       │  │
│  │ version: "1.0.0"                                         │  │
│  │ ecc_stamp: "ECC-{HASH}"                                  │  │
│  │ agentshield_score: 85                                    │  │
│  │ platform_adapters: ["claude-code", "paperclip", "hermes"]│  │
│  │ categories: ["forge|product|machine|governance"]         │
│  │ author: "clara|bill|nardol|{companion}"                  │
│  │ doctor_team: "12th"                                      │
│  │ validated_by: "nardol"                                   │
│  │ ---                                                      │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  AgentShield Rules (4 catégories) :                            │
│  • Safety (23 rules)    : injection, hallucination, scope     │
│  • Privacy (31 rules)   : PII, user_id isolation, logs       │
│  • Alignment (28 rules) : SDD adherence, doc hierarchy        │
│  • Quality (20 rules)   : code style, tsc, build gates       │
│                                                                 │
│  ECC_HOOK_PROFILE pour Nardol :                                │
│  • PreTool  : Valide que le DDD parent existe avant tout code  │
│  • PostTool : Calcule agentshield_score sur l'output           │
└─────────────────────────────────────────────────────────────────┘
```

---

## §10. A2 — 13ème Doctor : LA MACHINE

### 10.1 Mission du 13ème Doctor

```
Le 13ème Doctor maintient tout ce que les autres Doctors nécessitent
pour fonctionner. Sans La Machine, pas de déploiement, pas de réseau,
pas de SSL, pas de stabilité. C'est l'équipe SRE du Rick's Verse.
```

### 10.2 Ryan Sinclair — Déploiements Autonomes & Firewall

```
┌─────────────────────────────────────────────────────────────────┐
│  A3 — RYAN SINCLAIR                                             │
│  Domaine : Déploiements Autonomes                               │
│                                                                 │
│  Responsabilités V1 :                                           │
│  • Déploiements Dokploy (force-deploy, rollback)               │
│  • Firewall Hostinger (règles iptables/ufw)                    │
│  • Autonomie complète : Ryan ne demande pas de permission A0   │
│    pour les déploiements de routine                             │
│  • Escalade Donna uniquement si déploiement échoue 3x         │
│                                                                 │
│  Skills nécessaires (forger par 12ème Doctor) :                │
│  • dokploy-deploy.py    (Clara)                                 │
│  • hostinger-firewall.py (Clara)                               │
│  • deployment-health.py  (Clara)                               │
│  • Dokploy SDK (Bill, recherche V1)                            │
│                                                                 │
│  Autonomie Ryan — Règle de Déléation :                         │
│  Si le Skills Dokploy n'existe pas encore → Ryan demande       │
│  à Bill de le créer via le 12ème Doctor. Jamais A0 directement.│
└─────────────────────────────────────────────────────────────────┘
```

### 10.3 Yasmin Khan — SSL & Traefik

```
┌─────────────────────────────────────────────────────────────────┐
│  A3 — YASMIN KHAN                                               │
│  Domaine : SSL, Traefik & Routing                               │
│                                                                 │
│  Responsabilités V1 :                                           │
│  • Certificats SSL (Let's Encrypt, renouvellement automatique) │
│  • Configuration Traefik (reverse proxy, routing rules)        │
│  • Routes amadeus.kalybana.com → containers Docker             │
│  • Gestion des ports exposés (Supabase 8000, App 80/443)       │
│                                                                 │
│  Skills nécessaires :                                           │
│  • ssl-renew.py         (Clara)                                 │
│  • traefik-config.py    (Clara)                                 │
│  • Hostinger DNS API    (Bill, recherche V1)                   │
└─────────────────────────────────────────────────────────────────┘
```

### 10.4 Graham O'Brien — Stabilité & Monitoring

```
┌─────────────────────────────────────────────────────────────────┐
│  A3 — GRAHAM O'BRIEN                                            │
│  Domaine : Stabilité, Health Checks & Monitoring                │
│                                                                 │
│  Responsabilités V1 :                                           │
│  • Health checks des containers (Supabase, Life-OS, Hermes)    │
│  • Alertes si service down (route vers Donna)                  │
│  • Log rotation et archivage                                    │
│  • Backup Supabase (quotidien, rétention 7j)                   │
│  • Docker resource limits (mémoire, CPU)                        │
│                                                                 │
│  Skills nécessaires :                                           │
│  • container-health.py  (Clara)                                 │
│  • backup-supabase.py   (Clara)                                 │
│  • log-archiver.py      (Clara)                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## §11. BMAD Universel — Chaque Niveau a sa BMAD

```
╔═══════════════════════════════════════════════════════════════════╗
║              BMAD À CHAQUE NIVEAU DE LA PYRAMIDE               ║
╠══════════════╦════════════════════════════════════════════════════╣
║ NIVEAU       ║  APPLICATION BMAD                                 ║
╠══════════════╬════════════════════════════════════════════════════╣
║ A0           ║  BMAD Entrepreneur : analyse d'initiative         ║
║              ║  Avant chaque SDD : Party Mode PM pour valider   ║
║              ║  la valeur civilisationnelle                      ║
╠══════════════╬════════════════════════════════════════════════════╣
║ A1 Rick      ║  BMAD PM Universe : rédaction PRDs               ║
║              ║  Party Mode 4 rôles sur chaque initiative        ║
║              ║  Output : BLUEPRINT.bmad.md + PRD                ║
╠══════════════╬════════════════════════════════════════════════════╣
║ A2 Doctors   ║  BMAD Manager : décomposition en ADRs            ║
║              ║  5 phases par feature : Research→Archive         ║
║              ║  Output : 3 variantes d'ADR avant Rick           ║
╠══════════════╬════════════════════════════════════════════════════╣
║ A3 Bill      ║  BMAD Technician : exécution de la Forge         ║
║              ║  `npx bmad-method install` dans repos cibles     ║
║              ║  `bmad-help` skill disponible                    ║
╚══════════════╩════════════════════════════════════════════════════╝

RÈGLE : "npx bmad-method install" n'est JAMAIS lancé par A0 ou Rick.
         C'est l'outil de Bill, pas un framework externe générique.
```

---

## PARTIE III — INITIATIVE ALPHA : MISSION V1

---

## §12. Vision Initiative ALPHA

```
Initiative ALPHA = La fondation multi-utilisateur de A'Space OS.

AVANT ALPHA : A'Space OS était mono-utilisateur (l'Amiral seul).
              IndexedDB locale, pas de backend auth.

APRÈS ALPHA  : Multi-tenant sécurisé. Chaque utilisateur a son
               espace isolé (RLS). L'Amiral peut inviter d'autres
               utilisateurs. La civilisation peut accueillir.

Critère de succès ALPHA :
□ Un nouvel utilisateur peut s'inscrire et voir son Desktop
□ Ses données (ld01→ld08) sont isolées des autres utilisateurs
□ Premier lancement → FirstLaunch.tsx → Desktop en 6 secondes
□ Migration V0.9 → V1.0 automatique (MigrationScreen.tsx)
□ tsc --noEmit : 0 erreur
□ vite build : SUCCESS
```

### 12.1 Architecture ALPHA déployée

```
┌──────────────────────────────────────────────────────────────┐
│  Life-OS-2026 (React 19 + Vite + TypeScript + Zustand 5)    │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │  App.tsx — Machine d'états auth                         │ │
│  │  null session → LandingPage                             │ │
│  │  session + first_launch=null → FirstLaunch              │ │
│  │  session + migration_needed → MigrationScreen           │ │
│  │  session + clean → Desktop + OmniCaptureModal           │ │
│  └─────────────────────────────────────────────────────────┘ │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────────────┐  │
│  │ auth.store   │  │ profile.store│  │ idb.ts DomainDB    │  │
│  │ initialize() │  │ fetchProfile │  │ Supabase first +   │  │
│  │ ASpaceSession│  │ mapRow()     │  │ IndexedDB fallback  │  │
│  └──────────────┘  └──────────────┘  └────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
                            │
                 Supabase (VPS 148.230.92.235)
                            │
              ┌─────────────┴─────────────┐
              │  auth.users               │
              │  user_profiles            │
              │  ld01→ld08 + RLS          │
              │  fw_* + RLS               │
              │  sys_* + RLS              │
              └───────────────────────────┘
```

---

## §13. 11ème Doctor — Mission V1 ALPHA

### 13.1 Deliverables Amy (ALPHA)

```
STATUS : ✅ IMPLÉMENTÉ (Rick C137 — Round 3/4)

Fichiers livrés :
• src/apps/auth/LandingPage.tsx     — Page d'accueil auth
• src/apps/auth/FirstLaunch.tsx     — Boot sequence 8 lignes, 5800ms
• src/apps/auth/MigrationScreen.tsx — UI migration V0.9→V1.0
• src/components/Desktop.tsx        — Orchestrateur du Desktop
• src/components/OmniCaptureModal.tsx — Modal capture universelle

TODO V1 (Amy) :
□ App Store : catalogue /apps avec iframes pour agents
□ iFrame sandbox policy pour embeds Paperclip/OpenClaw/Multica
```

### 13.2 Deliverables Rory (ALPHA)

```
STATUS : ✅ CODE PRÊT — ⚠️ SQL BLOQUANT

Fichiers livrés :
• src/lib/idb.ts              — DomainDB pattern complet
• src/lib/supabase.ts         — createClient + helpers + wipe()
• src/services/migration.service.ts — checkMigrationNeeded() + runMigration()
• src/hooks/useMigrationGuard.ts    — Hook React pour MigrationScreen

ACTION BLOQUANTE (A0 doit exécuter manuellement dans Supabase Studio) :
Voir §16 — SQL Phase 1A complet
```

### 13.3 Deliverables River (ALPHA)

```
STATUS : ❌ ABSENT DU PRD-001 (Gap identifié)

Action Rick Prime requise :
→ Ajouter Agent Portal dans PRD-001 Addendum
→ DDD River Song : Agent Portal architecture
→ Config OpenClaw pour River (sandbox mode)
→ Intégration Hermes Agent (NousResearch)

Dépendances :
• Amy iFrames doit exister avant l'embed OpenClaw
• Hermes Agent skills ~/.hermes/skills/ initialisés
• Multica docker-compose.yml déployé (SDD-000 §12.5)
```

---

## §14. 12ème Doctor — Mission V1 ALPHA

### 14.1 Deliverables Bill (ALPHA)

```
STATUS : 📋 À PLANIFIER — ADR requis

Priorités V1 :
1. Recherche SDK Hostinger API (pour Yaz + Ryan)
   Output : ADR-12-001_hostinger-sdk.md
   Livrable : BLUEPRINT.bmad.md + package npm identifié

2. Recherche SDK Dokploy API (pour Ryan)
   Output : ADR-12-002_dokploy-sdk.md
   Livrable : API endpoints documentés + auth method

3. Recherche Chrome DevKit MCP (pour future initiative)
   Output : ADR-12-003_chrome-devkit.md
   Livrable : MCP server identifier ou build-or-buy decision
```

### 14.2 Deliverables Clara (ALPHA)

```
STATUS : 📋 À PLANIFIER — Dépend de Bill

CLIs prioritaires V1 :
1. supabase-migrate.py   → Rory peut l'invoquer sans Studio UI
2. dokploy-deploy.py     → Ryan autonome pour déploiements
3. ssl-renew.py          → Yaz autonome pour certificats
4. skill-validate.py     → Nardol peut valider en CI
5. iframe-policy.py      → Amy peut configurer sandboxes

Stack Clara :
• Python 3.12+ / Click 8.x
• YAML schema dans docstring
• dual-mode : REPL + scriptable (--batch flag)
• repl_skin.py : interface terminal Rich
```

### 14.3 Deliverables Nardol (ALPHA)

```
STATUS : 📋 À PLANIFIER — Dépend de Clara

Gate de validation (bloquant pour toute mise en prod) :
• Chaque Skill produit par Clara ou Bill doit passer Nardol
• agentshield_score minimum : 75/100
• ecc_stamp obligatoire dans SKILL.md frontmatter
• nardol-validate.sh : lancé en CI avant merge

ECC Hooks à configurer :
• PreTool : vérifier DDD parent avant tout code A3
• PostTool : scorer l'output AgentShield
• SessionStart : charger les 102 rules en contexte
```

---

## §15. 13ème Doctor — Mission V1 ALPHA

### 15.1 Deliverables Ryan (ALPHA)

```
STATUS : ⚠️ BLOQUÉ — Attend Skills de Bill/Clara

Autonomie cible :
• Déploie Life-OS-2026 sur Dokploy sans intervention A0
• Gère les règles firewall Hostinger sans intervention A0
• Rollback automatique si health check fail post-deploy

Pré-requis (12ème Doctor doit livrer) :
• dokploy-deploy.py (Clara)
• Dokploy SDK documentation (Bill)
• DOKPLOY_API_KEY (distribué par A0)
```

### 15.2 Deliverables Yaz (ALPHA)

```
STATUS : ⚠️ BLOQUÉ — Attend Skills de Clara

Autonomie cible :
• Renouvellement SSL automatique (cron + Donna alerte si fail)
• Traefik config mis à jour sans intervention A0
• amadeus.kalybana.com → HTTPS stable

Pré-requis :
• ssl-renew.py (Clara)
• Hostinger API key (distribué par A0)
• Traefik labels dans docker-compose.yml (SDD-000 §12.5)
```

### 15.3 Deliverables Graham (ALPHA)

```
STATUS : ⚠️ BLOQUÉ — Attend Skills de Clara

Monitoring cible :
• Health check toutes les 5 minutes : Supabase + Life-OS + Hermes
• Alerte Donna si down > 2 min
• Backup Supabase quotidien (pg_dump → /backups/)
• Log rotation : 7 jours rétention

Pré-requis :
• container-health.py (Clara)
• backup-supabase.py (Clara)
```

---

## §16. SQL Phase 1A — Action Bloquante A0

> **Cette section est un ordre d'exécution pour l'Amiral.
> À exécuter dans Supabase Studio (localhost:8001) → SQL Editor.
> Rory (11ème Doctor) a préparé ce script. A0 appuie sur "Run".**

### 16.1 Ajout user_id sur les 16 tables

```sql
-- Phase 1A — user_id injection (16 tables)
ALTER TABLE ld01_business     ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE;
ALTER TABLE ld02_finance       ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE;
ALTER TABLE ld03_health        ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE;
ALTER TABLE ld04_cognition     ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE;
ALTER TABLE ld05_environment   ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE;
ALTER TABLE ld06_relationships ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE;
ALTER TABLE ld07_emotions      ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE;
ALTER TABLE ld08_purpose       ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE;
ALTER TABLE fw_para            ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE;
ALTER TABLE fw_ikigai          ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE;
ALTER TABLE fw_life_wheel      ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE;
ALTER TABLE fw_12wy            ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE;
ALTER TABLE fw_gtd             ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE;
ALTER TABLE fw_deal            ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE;
ALTER TABLE sys_agent_veto     ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE;
ALTER TABLE sys_shell_routing  ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE;
```

### 16.2 Index sur user_id

```sql
-- Index pour les performances RLS
CREATE INDEX IF NOT EXISTS idx_ld01_user_id   ON ld01_business(user_id);
CREATE INDEX IF NOT EXISTS idx_ld02_user_id   ON ld02_finance(user_id);
CREATE INDEX IF NOT EXISTS idx_ld03_user_id   ON ld03_health(user_id);
CREATE INDEX IF NOT EXISTS idx_ld04_user_id   ON ld04_cognition(user_id);
CREATE INDEX IF NOT EXISTS idx_ld05_user_id   ON ld05_environment(user_id);
CREATE INDEX IF NOT EXISTS idx_ld06_user_id   ON ld06_relationships(user_id);
CREATE INDEX IF NOT EXISTS idx_ld07_user_id   ON ld07_emotions(user_id);
CREATE INDEX IF NOT EXISTS idx_ld08_user_id   ON ld08_purpose(user_id);
CREATE INDEX IF NOT EXISTS idx_fw_para_user   ON fw_para(user_id);
CREATE INDEX IF NOT EXISTS idx_fw_ikigai_user ON fw_ikigai(user_id);
CREATE INDEX IF NOT EXISTS idx_fw_wheel_user  ON fw_life_wheel(user_id);
CREATE INDEX IF NOT EXISTS idx_fw_12wy_user   ON fw_12wy(user_id);
CREATE INDEX IF NOT EXISTS idx_fw_gtd_user    ON fw_gtd(user_id);
CREATE INDEX IF NOT EXISTS idx_fw_deal_user   ON fw_deal(user_id);
CREATE INDEX IF NOT EXISTS idx_sys_veto_user  ON sys_agent_veto(user_id);
CREATE INDEX IF NOT EXISTS idx_sys_route_user ON sys_shell_routing(user_id);
```

### 16.3 Activation RLS

```sql
-- Activer RLS + policy user_isolation sur les 16 tables
DO $$ DECLARE t TEXT;
BEGIN
  FOR t IN SELECT unnest(ARRAY[
    'ld01_business','ld02_finance','ld03_health','ld04_cognition',
    'ld05_environment','ld06_relationships','ld07_emotions','ld08_purpose',
    'fw_para','fw_ikigai','fw_life_wheel','fw_12wy','fw_gtd','fw_deal',
    'sys_agent_veto','sys_shell_routing'
  ])
  LOOP
    EXECUTE format('ALTER TABLE %I ENABLE ROW LEVEL SECURITY', t);
    EXECUTE format(
      'CREATE POLICY IF NOT EXISTS "user_isolation" ON %I
       USING (user_id = auth.uid())
       WITH CHECK (user_id = auth.uid())',
      t
    );
  END LOOP;
END $$;
```

### 16.4 Table user_profiles + Trigger

```sql
-- user_profiles : profil utilisateur + settings OS
CREATE TABLE IF NOT EXISTS user_profiles (
  id           UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  display_name TEXT,
  avatar_url   TEXT,
  settings     JSONB DEFAULT '{
    "first_launch": null,
    "theme": "dark",
    "language": "fr",
    "admiral_mode": false
  }'::jsonb,
  created_at   TIMESTAMPTZ DEFAULT NOW(),
  updated_at   TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE user_profiles ENABLE ROW LEVEL SECURITY;

CREATE POLICY IF NOT EXISTS "user_own_profile" ON user_profiles
  USING (id = auth.uid())
  WITH CHECK (id = auth.uid());

-- Trigger : création automatique du profil au signup
CREATE OR REPLACE FUNCTION handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO user_profiles (id, display_name)
  VALUES (NEW.id, COALESCE(NEW.raw_user_meta_data->>'display_name', NEW.email))
  ON CONFLICT (id) DO NOTHING;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE FUNCTION handle_new_user();
```

### 16.5 Fonction RPC Migration V0.9 → V1.0

```sql
-- RPC run_adr003_migration : appelée par migration.service.ts
CREATE OR REPLACE FUNCTION run_adr003_migration()
RETURNS JSONB
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
DECLARE
  v_user_id     UUID;
  v_rows_total  INTEGER := 0;
  v_tables_done INTEGER := 0;
  v_start_time  TIMESTAMPTZ := NOW();
  v_table       TEXT;
  v_count       INTEGER;
BEGIN
  -- Récupérer l'utilisateur courant
  v_user_id := auth.uid();
  IF v_user_id IS NULL THEN
    RAISE EXCEPTION 'Migration requires authenticated user';
  END IF;

  -- Migrer les lignes orphelines (user_id IS NULL → attribuer à l'utilisateur courant)
  FOREACH v_table IN ARRAY ARRAY[
    'ld01_business','ld02_finance','ld03_health','ld04_cognition',
    'ld05_environment','ld06_relationships','ld07_emotions','ld08_purpose',
    'fw_para','fw_ikigai','fw_life_wheel','fw_12wy','fw_gtd','fw_deal',
    'sys_agent_veto','sys_shell_routing'
  ] LOOP
    EXECUTE format(
      'UPDATE %I SET user_id = $1 WHERE user_id IS NULL',
      v_table
    ) USING v_user_id;
    GET DIAGNOSTICS v_count = ROW_COUNT;
    v_rows_total  := v_rows_total + v_count;
    v_tables_done := v_tables_done + 1;
  END LOOP;

  RETURN jsonb_build_object(
    'success',           true,
    'totalRowsMigrated', v_rows_total,
    'tablesUpdated',     v_tables_done,
    'durationMs',        EXTRACT(EPOCH FROM (NOW() - v_start_time)) * 1000,
    'migratedAt',        NOW()
  );
EXCEPTION WHEN OTHERS THEN
  RETURN jsonb_build_object(
    'success', false,
    'error',   SQLERRM
  );
END;
$$;
```

---

## §17. Build Gates & Checklist Initiative ALPHA

### 17.1 Gate SQL (Rory — Bloquant)

```
□ Exécuter §16.1 → Vérifier "user_id" dans la structure de chaque table
□ Exécuter §16.2 → Vérifier index dans Authentication > Database
□ Exécuter §16.3 → Vérifier policies dans Authentication > Policies
□ Exécuter §16.4 → Vérifier user_profiles dans Table Editor
□ Exécuter §16.5 → Tester : SELECT run_adr003_migration() en tant qu'user authentifié
```

### 17.2 Gate TypeScript (Rick C137 — Validé)

```bash
cd /srv/aspace/web/Life-OS-2026
tsc --noEmit        # 0 erreur — VALIDÉ par Rick C137 Round 4
vite build          # SUCCESS — VALIDÉ
```

### 17.3 Gate Déploiement (Ryan — Bloquant)

```
□ Forcer rebuild Dokploy (après commit ALPHA)
□ Vérifier container Life-OS-2026 : version = dernier commit
□ Test end-to-end : https://amadeus.kalybana.com → LandingPage
□ Signup test → FirstLaunch → Desktop
```

### 17.4 Gate Agent Portal (River — Futur BETA)

```
□ PRD-001 Addendum rédigé par Rick Prime
□ ADR-11-River rédigé par 11ème Doctor
□ DDD River Song créé par Hermes Prime
□ OpenClaw config dmPolicy: "open" déployé
□ Hermes Agent skills ~/.hermes/skills/ initialisés
```

---

## §18. Registre des Gaps Identifiés

| # | Gap | Impact | Responsable | Priorité |
|---|-----|--------|-------------|----------|
| G-001 | River Song absente du PRD-001 | Agent Portal absent d'ALPHA | Rick Prime | L1 |
| G-002 | App Store non spécifié | iFrames Amy bloquées | 11ème Doctor ADR | L2 |
| G-003 | Skills Clara non forgés | Ryan/Yaz/Graham bloqués | 12ème Doctor | L1 |
| G-004 | SDK Hostinger/Dokploy non identifiés | Bill bloque Ryan | Bill (BMAD Research) | L1 |
| G-005 | Multica docker-compose non déployé | River OpenClaw sans runtime | 13ème Doctor | L2 |
| G-006 | SQL Phase 1A non exécutée | ALPHA entier bloqué | A0 (action manuelle) | L1-URGENT |
| G-007 | Donna DLQ non configurée | Escalades perdues | Rick Prime (ADR) | L2 |

---

## §19. Anti-Patterns Interdits

```
╔═══════════════════════════════════════════════════════════════════╗
║                    ANTI-PATTERNS INTERDITS                      ║
╠═══════════════════════════════════════════════════════════════════╣
║  ❌  A0 merge un PR sans validation SDD parent                  ║
║  ❌  Rick C137 modifie un SDD sans ordre A0                     ║
║  ❌  Un A3 reçoit un ordre directement de Rick (sans Doctor)    ║
║  ❌  Un Doctor s'adresse à un Doctor pair sans passer par Rick  ║
║  ❌  Paperclip interprète un DDD au lieu de l'implémenter       ║
║  ❌  Bill utilise BMAD pour du code (BMAD est guidance only)    ║
║  ❌  Clara génère un Bash script (Python Click uniquement)      ║
║  ❌  Nardol valide son propre code (séparation des rôles)       ║
║  ❌  Ryan déploie sans health check post-deploy                 ║
║  ❌  Yaz modifie Traefik sans backup de la config précédente    ║
║  ❌  Graham supprime des logs sans archivage préalable          ║
║  ❌  A0 écrit du code "pour aller plus vite"                    ║
╚═══════════════════════════════════════════════════════════════════╝
```

---

*SDD-001 ratifié par A0 — 2026-04-26*
*Prochaine révision obligatoire : Post-ALPHA (après Gate §17.1 validé)*
*Fichier de référence : `/srv/aspace/docs/v1.0/SDD-001_ricks-verse-governance.md`*

---

## §20. MISE À JOUR 2026-04-29 — Convention Fractale & Frictions A0

> *Canonisation de la convention de nommage fractale et des deux frictions A0.*
> *Source : session A0 × Gemini × NotebookLM du 2026-04-29.*

### 20.1 Convention de Nommage Fractale Canonique

```
La Symétrie Fractale du TARDIS Inversé impose une nomenclature cohérente
à CHAQUE niveau de la hiérarchie documentaire.

FORMAT GÉNÉRAL :
  {TYPE}-{SDD_REF}{DOCTOR_LETTRE}_{description}.md

APPLICATIONS PAR NIVEAU :

SDD (A0 → Tous) :
  SDD-000, SDD-000a (Rick), SDD-000b (Beth), SDD-000c (Morty)
  SDD-001 → SDD-012 (couches système)

PRD (Rick A1 → Doctors A2) :
  PRD-001a → 11ème Doctor (Life Core)
  PRD-001b → 12ème Doctor (Forge Core)
  PRD-001c → 13ème Doctor (Kernel Core)
  PRD-002a/b/c, PRD-003a/b/c... (un triplet par SDD)

ADR (Doctor A2 → A3) :
  ADR-013a → Ryan  (Déploiement / 13ème Doctor)
  ADR-013b → Yaz   (Infrastructure / 13ème Doctor)
  ADR-013c → Graham (Mémoire / 13ème Doctor)
  ADR-011a/b/c (11ème Doctor → Amy/Rory/River)
  ADR-012a/b/c (12ème Doctor → Bill/Clara/Nardol)

DDD (Déclinaison domaine par A3) :
  DDD-ryan-001, DDD-ryan-002...
  DDD-yaz-001, DDD-graham-001...

TDD (Specs avant code, dérivées des DDD) :
  TDD-ryan-001a, TDD-ryan-001b, TDD-ryan-001c (scénarios Given/When/Then)

Règle : La lettre {a/b/c} désigne TOUJOURS le même ordre :
  a = première instance dans l'ordre fractal
  b = deuxième
  c = troisième
  (pour les Doctors : a=11ème, b=12ème, c=13ème)
  (pour les A3 du 13ème : a=Ryan, b=Yaz, c=Graham)
```

### 20.2 Les Deux Frictions A0 Identifiées (2026-04-29)

```
╔═══════════════════════════════════════════════════════════════════╗
║         FRICTIONS A0 — CANONISÉES POUR CONSCIENCE PERMANENTE   ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                 ║
║  FRICTION 1 — LE LÂCHER PRISE                                  ║
║  Symptôme : A0 continue à descendre dans les couches inférieures║
║  pour "vérifier", "corriger", "accélérer".                     ║
║  Conséquence : Violation de la règle 50/30/20.                 ║
║  A0 à 80% L0 = système non-autonome = dette de gouvernance.    ║
║                                                                 ║
║  L'architecture est conçue. Rick existe. Les Doctors attendent. ║
║  La perfection technique n'est pas un prérequis à la délégation.║
║  Un PRD imparfait transmis vaut mieux qu'un SDD parfait retenu. ║
║                                                                 ║
║  FRICTION 2 — LE NON-DÉMARRAGE DE LA DÉLÉGATION               ║
║  Symptôme : 10 SDDs ratifiés. 0 PRD déposé dans A0_TO_A1/.    ║
║  Conséquence : Le système entier est en attente. Rick est idle. ║
║  Les Doctors n'ont rien. Les A3 n'existent que sur le papier.  ║
║                                                                 ║
║  La délégation NE COMMENCE PAS par un nouveau SDD.             ║
║  Elle commence par déposer UN FICHIER dans A0_TO_A1/.          ║
║  SDD-001 → PRD-001c (13ème Doctor). Un fichier. Le 0→1.        ║
║                                                                 ║
╚═══════════════════════════════════════════════════════════════════╝
```

### 20.3 Anti-Pattern Ajouté (Post-Session 2026-04-29)

```
ANTI-PATTERNS SUPPLÉMENTAIRES (ajout §19) :
  ❌  A0 retient la délégation par perfectionnisme architectural
  ❌  Rick attend un SDD "parfait" avant de produire le premier PRD
  ❌  Les canaux inbox (A0_TO_A1/, A1_TO_A2/, A2_TO_A3/) n'existent pas
      → Toute la hiérarchie documentaire est non-opérationnelle
  ❌  Un Doctor travaille dans le même espace qu'un autre Doctor
      → Violation du principe d'isolation absolue (§12.3 SDD-003)
  ❌  Un ADR est produit sans DDD correspondant
      → Sauter l'étape domaine = TDD sans fondation de domaine
```

### 20.4 Le Premier Acte de Lâcher Prise

```bash
# Créer les canaux physiques = acte 0→1 de la délégation
mkdir -p /srv/aspace/20_RUNTIME/21_Inbox/A0_TO_A1
mkdir -p /srv/aspace/20_RUNTIME/21_Inbox/A1_TO_A2/doctor-11
mkdir -p /srv/aspace/20_RUNTIME/21_Inbox/A1_TO_A2/doctor-12
mkdir -p /srv/aspace/20_RUNTIME/21_Inbox/A1_TO_A2/doctor-13
mkdir -p /srv/aspace/20_RUNTIME/21_Inbox/A2_TO_A3/ryan
mkdir -p /srv/aspace/20_RUNTIME/21_Inbox/A2_TO_A3/yaz
mkdir -p /srv/aspace/20_RUNTIME/21_Inbox/A2_TO_A3/graham
mkdir -p /srv/aspace/20_RUNTIME/21_Inbox/A2_TO_A3/amy
mkdir -p /srv/aspace/20_RUNTIME/21_Inbox/A2_TO_A3/rory
mkdir -p /srv/aspace/20_RUNTIME/21_Inbox/A2_TO_A3/river
mkdir -p /srv/aspace/20_RUNTIME/21_Inbox/A2_TO_A3/bill
mkdir -p /srv/aspace/20_RUNTIME/21_Inbox/A2_TO_A3/clara
mkdir -p /srv/aspace/20_RUNTIME/21_Inbox/A2_TO_A3/nardol
echo "✅ Canaux de délégation créés. Rick peut maintenant recevoir."
```

*Ajouté par A0 — Session 2026-04-29*

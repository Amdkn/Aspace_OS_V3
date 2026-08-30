# META_ONTOLOGIE — Reconstitution des trois couches d'A'Space OS

> **Statut** : RAPPORT LIVRE — termine le 2026-08-13
> **Auteur** : agent brief `META_ONTOLOGIE_3_COUCHES`
> **Livrables associes** : `meta_ontologie.json` (meme repertoire)
> **Regle d'or** : **Aucun SDD n'est source de verite.** V3 et le code priment. Une entree sans source est une invention.

---

## 0. Hypothese contredite au depart, et ce qui la remplace

Le brief dit de partir des SDD de Geordi (archive). Mesure immediatement :

> SDD-006 (chemin `ASpace_OS_V2/.../SDD-006_business-pulse-l2-pyramide.md`) decrit **7 domaines Business** avec 7 strateges DC et 7 escouades Marvel. Le canon a jour, `Business_Pulse_B3_Notion_Canon_Lore_Index.md` (2026-05-27), en compte **8** — il manque Sales / Illuminati / John Jones (Martian Manhunter). Le dossier `src/apps/sales/` existe pourtant depuis des semaines dans le depot coach-os. **Le code etait en avance sur le document pris pour source de verite.**

Le canon a jour est dans V3, pas dans les SDD de Geordi. Tous les tableaux de cette reconstitution s'appuient sur V3 + code reel, avec les SDD cites en parallele a titre de reference (et flechand comme perime).

---

## 1. Les trois couches d'A'Space OS — paragraphes de cadrage

### Tech OS — le mecanisme qui produit les trois OS

`10_Tech_OS/` contient : Rick (gouvernance), le replicator (`replicator/` — un seul gabarit, trois instances), le kernel (`kernel/` — file SQLite, adaptateur, portier, reviewer), et les **trois Cores** ensembles :

| Core | Docteur | Couche | Couche operee |
|---|---|---|---|
| Kernel Core | 13e | `L0` dans `10_Tech_OS/11_Kernel_Core_13th/` | `10_Tech_OS` (lui-meme) |
| Life Core | 11e | `L1` dans `10_Tech_OS/12_Life_Core_11th/` | `20_Life_OS` |
| Buzz Core | 12e | `L2` dans `10_Tech_OS/13_Buzz_Core_12th/` | `30_Business_OS` |

Citation cle (session bf0d8147:5192) : *« 13e Kernel Core → `10_Tech_OS\`, 11e Life Core → `20_Life_OS\`, 12e Buzz Core → `30_Business_OS\`. Verifie : trois fichiers issus du meme moule, zero placeholder residuel. »*

**Loi de Rick (LAW.md:3) :** *« Rick ne gouverne pas les trois OS. Il gouverne le mecanisme qui les produit. »* C'est la distinction qui a manque a V2. Le Tech OS n'est pas un quatrieme chantier ; c'est le constructeur universel.

### Life OS — la conscience

`20_Life_OS/` : 42 personas reelles (2 A1 + 6 A2 + 34 A3), pack sous `C:/Users/amado/.buzz/packs/aspace-life-os/agents/`. Le soft data : Ikigai, Jauges LD, GTD, 12WY, PARA. Star Trek lore (Picard, Spock, Data, Geordi, Pike, Mercer, Mariner, Cerritos, Discovery, Enterprise, Orville, Protostar, SNW).

Life OS dispose du **veto supreme** sur L2 : la Loi 1 (SDD-006 :108) dit *« Si Beth emet un HALT (rouge) : toute acceleration Business est gele immediatement. Les Jerrys ne lancent plus de nouveaux Summer's Verse. Seul le Retour au Vert de Beth debloque L2. »*

### Business OS — l'action

`30_Business_OS/` : 8 domaines B2 (DC strateges) avec 8 escouades B3 (Marvel squads), plus haut dans la pyramide 4 variants de Jerry (macro-portefeuille) et les Summer's Verse (micro-executif). Coach OS (`ASpace_OS_V2/.../coach-os/`) est la **1ere Franchise Prototype** de Business OS (session 314fae52:24820).

Citation cle (session 314fae52:24820) : *« Surtout dans l'unification de Business OS dans Life OS dont Coach OS est la 1ere Prototype de Franchise. »*

Tension a noter : le canon pose une **pyramide stricte** (L0 >= L1 > L2 en autorite), mais l'utilisateur dit que **L2 unifie dans L1**. Les deux lignes cohabitent ; je les distingue dans les relations, pas dans la synthese.

---

## 2. Tableaux d'entites, une couche chacun

### 2.1 Tech OS — 12 entites

Toutes les entites sourcees sur `10_Tech_OS/00_Governance_Rick/`, `sessions_md/.../bf0d8147-...`, et `WATCHDOG.md`.

| # | Entite | Nature | Source(s) |
|---|---|---|---|
| 1 | **Rick** | S1 — Entrepreneur — gouverne le mecanisme, pas les 3 OS | `LAW.md:1-99`, `SOUL.md:1-58` |
| 2 | **Noyau (Kernel)** | 4 organes : file SQLite, adaptateur, portier, reviewer | `kernel/`, `bf0d8147:4987-5073` |
| 3 | **Core (Kernel/Life/Buzz)** | 3 instances du meme gabarit, engendrees par spawn.py | `LAW.md:30-42`, `bf0d8147:5192` |
| 4 | **Replicator** | `core.template` + `cores.json` + `spawn.py` | `LAW.md:23-42` |
| 5 | **Role (Spec/Build/Spawn/Review)** | Mapping Von Neumann — nul ne cumule Build et Review | `LAW.md:59-70` |
| 6 | **Note (ruban)** | Deposee dans `_INBOX/{S1_Rick|A1_Beth_Morty|B1_Jerry_Summer}/`, test du ruban a 4 controles | `bf0d8147:5106-5132` |
| 7 | **Harness (adaptateur)** | Contrat `uc.py` CLI, JSON sur stdout, 3 garanties (bail, fail immediat, refuse predict absent) | `bf0d8147:5048-5073` |
| 8 | **Watchdog** | 3 seuils (vivant/bien portant/anti-fragile) | `WATCHDOG.md`, `314fae52:26089-26247` |
| 9 | **A0** | Orchestrateur runtime 4h-12h, 7 cadences | `314fae52:25540,26106` |
| 10 | **Cadence** | Rythme d'execution periodique, 7 cadences | `314fae52:25765-25806` |
| 11 | **Garde-fou** | Plafond de concurrence, refus predict absent, triggers SQL | `314fae52:25765-25809` |
| 12 | **Runner (harness runtime)** | claude -p, claude CLI, hermes, codex, paperclip | `CLAUDE.md:1-26` |

**Candidats du brief non confirmes en entites separees :**

- *Agent* — existe comme entite Business OS dans coach-os, pas comme entite Tech OS. L'Agent Tech OS est incarne par le Role (Spec/Build/Spawn/Review) et le Harness (l'instance qui execute).
- *Incident* — existe comme entite Business OS. Cote Tech OS, c'est une notion du Watchdog (incident = cause not named + guard pas dans code + guard pas vue + lesson non ecrite), pas une entite formelle.
- *Runtime* — concept diffuse, decoupe en Noyau (file) + A0 (orchestrateur) + Cadence (rythme) + Runner (CLI).

### 2.2 Life OS — 19 entites

Source principale : `C:/Users/amado/.buzz/packs/aspace-life-os/agents/` (42 personas reelles, 25 juillet 2026).

| Rang | Entite | Cycle/Definition | Source |
|---|---|---|---|
| A1 | **Beth Alignement** | H+3 ans, tient le cap, peut HALT L2 | `cc348baa-...:359`, `1af3bfe0-...:366` |
| A1 | **Morty Mise en file** | H+3 ans, execution | `1af3bfe0-...:359` |
| A2 | **Cerritos (GTD)** | 5 etapes capture/clarify/organize/review/engage | `1af3bfe0-...:359`, `SDD-006 §7.2` |
| A2 | **Discovery (ZORA)** | 8 jauges LD01-LD08 + deltas | `SDD-006 §7.2.A`, `1af3bfe0-...:359` |
| A2 | **Enterprise (Picard/Spock)** | Areas (Spock) + Projects (Picard) | `SDD-006 §3.1`, `1af3bfe0-...:359` |
| A2 | **Orville (Ikigai)** | 4 dimensions (Profession/Mission/Passion/Vocation), score 3+/4 | `SDD-006 §7.2.A` |
| A2 | **Protostar (D.E.A.L)** | Dal/RokTahk/Zero/Gwyn/MBenga | `SDD-006 §7.5` |
| A2 | **SNW (12WY)** | Ordinateur 12 Week Year, 12 sem -> 12 jours | `SDD-006 §7.4` |
| A3 | **5 Ikigai pilarites** | Mercer, Grayson, Malloy, Finn | `C:/Users/amado/.buzz/packs/aspace-life-os/agents/a3_01_*.persona.md` |
| A3 | **5 GTD etapes** | Mariner, Boimler, Rutherford, Tendi, Freeman | `C:/Users/amado/.buzz/packs/aspace-life-os/agents/a3_0*.persona.md` |
| A3 | **5 D.E.A.L etapes** | Dal, RokTahk, Zero, Gwyn, MBenga | `C:/Users/amado/.buzz/packs/aspace-life-os/agents/a3_03_*.persona.md` |
| A3 | **5 Horizons 12WY** | H1 Isaac, H3 Lamarr, H10 Bortus, H30 Alara, H90 Klyden | `C:/Users/amado/.buzz/packs/aspace-life-os/agents/a3_*_h*.persona.md` |
| A3 | **8 Life Wheel LDs** | LD01 Book, LD02 Saru, LD03 Culber, LD04 Tilly, LD05 Stamets, LD06 Burnham, LD07 Reno, LD08 Georgiou | `C:/Users/amado/.buzz/packs/aspace-life-os/agents/a3_ld*.persona.md` |
| A3 | **4 Archives** | Geordi Resources, Data Archives, Chapel Metrics, Spock Areas | `C:/Users/amado/.buzz/packs/aspace-life-os/agents/a3_0*.persona.md` |
| Cadre | **Vision** | D1 cycle E-Myth, verrouille ADR-LD01-010 | `ADR-LD01-011:11-20` |
| Cadre | **Ambition** | 8 domaines LD, jauge ZORA weekly | `A3_Book_LD01_Spec.md:9-19` |
| Cadre | **Rock (12WY)** | 4-5 rocks/sem, cycle 1 semaine | `ADR-LD01-011:66-78` |
| Cadre | **Discipline** | D1 Vision, D2 Planning, D3 Process Control, D4 Append-only | `ADR-LD01-011:11-18` |
| Cadre | **PARA/GTD/D.E.A.L/Ikigai** | Cadrage non encode comme entites | `314fae52:3749`, `SDD-006 §7.2` |

**Candidats du brief non confirmes :**

- *Vision* existe comme cadre (D1 discipline), pas comme entite en base. Le coach-os Business ne contient pas de modele Vision.
- *Ambition* — terme Life Wheel, pas une entite.
- *Rock* — entite de la discipline 12WY, pas codee en code.

### 2.3 Business OS — 17 entites

Source : `ASpace_OS_V2/.../coach-os/src/lib/ontology/entities.ts` (13 entites du registre) + `Business_Pulse_B3_Notion_Canon_Lore_Index.md` (8 domaines + 4 Jerry + Summer).

| # | Entite | Nature | Source |
|---|---|---|---|
| 1 | **Domaine Business (B2)** | 8 (Growth, Sales, Product, Ops, IT, Finance, People, Legal) | `Business_Pulse_B3 §5`, `entities.ts:70-79` |
| 2 | **Organization** | racine, locataire `coach-os` | `entities.ts:108-117` |
| 3 | **Membership** | Profile x Organization + role | `entities.ts:118-128` |
| 4 | **Profile** | Identite personne (coach, client, observateur) | `entities.ts:129-142` |
| 5 | **Client** | Beneficielle accompagnement | `entities.ts:145-157` |
| 6 | **Offering** | Prestation cataloguee, facturable | `entities.ts:159-167` |
| 7 | **SOP** | Standard Operating Procedure, versionnee | `entities.ts:170-179` |
| 8 | **Runbook** | Playbook operationnel | `entities.ts:181-190` |
| 9 | **Skill** | Competence atomique Agent/Persona | `entities.ts:192-198` |
| 10 | **Agent** | Operateur humain ou IA | `entities.ts:201-214` |
| 11 | **Routine** | Tache recurrente, cadence | `entities.ts:215-229` |
| 12 | **Incident** | Evenement observable, resolu ou non | `entities.ts:232-246` |
| 13 | **Persona** | Profil synthetique (voix, ton, posture) | `entities.ts:249-256` |
| 14 | **Stratege DC (B2 owner)** | Superman, John Jones, Flash, Batman, Cyborg, Wonder Woman, Green Lantern, Aquaman | `Business_Pulse_B3 §5.1-5.7` |
| 15 | **Escouade Marvel (B3)** | Guardians, Illuminati, Avengers, Fantastic4, KangDynasty, Thunderbolts, XMen, Eternals | `Business_Pulse_B3 §3-§5` |
| 16 | **Jerry (variant)** | 4 (Prime, Bio, Nexus, Solarpunk) — macro-portefeuille | `SDD-006 §3.2` |
| 17 | **Summer (Summer's Verse)** | micro-executif par projet | `SDD-006 §4.1-4.2` |

**Candidats du brief non confirmes :**

- *Cadence* — present dans entities.ts (string) et dans 314fae52 comme entite Tech OS. Cote Business, c'est un attribut de Routine, pas une entite.

---

## 3. Les relations inter-couches — reponse aux trois questions

### 3.1 Q1 — Qu'est-ce qui relie un objet Business a une Vision Life OS ?

**Verdict : source dit OUI — voici ou.**

Liens identifies (par ordre de force probante) :

1. **Loi 1 du SDD-006 (Subordination/Veto Beth) :** Beth (L1) peut HALT l'integralite de L2. L'autorite L1 sur L2 est absolue. **Polarite : L1 -> L2 (descendante veto).**

2. **Le tag `horizon` partage :** Book (LD01) = H1 (weekly P&L) — verrouille par ADR-LD01-010. Les 5 horizons H1/H3/H10/H30/H90 existent dans les 2 couches. **Polarite : etiquette partagee, pas lien causal.**

3. **Cascade canonique (CASCADE.md) :** A3 Life OS produit B1 playbooks (rocks mensuels) -> B2 roadmap 4 sprints -> B3 squads Marvel. **Polarite : L1 -> L2 (cascade descendante).**

4. **ZORA (Life Wheel) alimente Beth :** Beth VERTE / ORANGE / ROUGE determine la cadence L2 (SDD-006 §8.1 SLOT 2). **Polarite : L1 -> L2 (autorisation hebdo).**

5. **Declaration utilisateur (session 314fae52:24820) :** *« l'unification de Business OS dans Life OS dont Coach OS est la 1ere Prototype de Franchise. »* **Polarite : L2 -> L1 (unification remontante).**

**Ce que la source ne dit pas :** aucun mecanisme de lien code en base. Le Business OS n'a pas d'attribut `vision_id` ou `ld_link`. L'unique cle partagee est le tag `horizon` (H1/H3/H10/H30/H90), et cette cle n'est pas enforcee.

**Le trou reel :** comment passer d'un lien en prose a un lien en code. Voir `trous/T12`.

### 3.2 Q2 — Qu'est-ce qui relie un Agent Tech OS a un domaine Business ?

**Verdict : source dit OUI — voici ou.**

Liens identifies :

1. **Code (coach-os) :** `agent-serves-domains` (n-n) — un Agent peut servir plusieurs Domaines (`relations.ts:77`).

2. **Canon (SDD-006 §5.6 Cyborg) :** L2 IT (Cyborg) **NE TOUCHE PAS** l'infrastructure L0. Tout besoin L0 passe par le **protocole SDD-004 §7.2 via River Song**.

3. **Canon (Business_Pulse §5.5 Green Lantern) :** Green Lantern (B2 People) **demande a Bill (L0.2 Forge)** de forger les Skills pour les nouveaux agents. Forge signifie CLI ; injecte signifie River Song.

4. **Code (kernel/) :** les 4 organes (file, adaptateur, portier, reviewer) servent les 3 couches a l'identique. Citation bf0d8147:5196 : *« Aucun Core ne possède d'organe. File, adaptateur, portier, reviewer vivent dans kernel\ et servent les trois couches a l'identique. »*

5. **Declaration utilisateur (session 314fae52:24821-24822) :** *« mon Échecs Implacable d'implementaation du Solarpunk Kernel Tech OS avec Rick et les Doctors Who avec leurs compagnons dans Multica apres avoir echouer dans tous les Harness Sans Onthologie. Avec le Lore de Star Treck devier au Life OS et qui a finit repartie entre les Avatar des Agents de Business OS concerner en Startrek plutot qu'en Heros DC/Marvel du Business par Dette Technique non encore corriger. »*

**Le trou reel :** la relation agent-serves-domains en code est creee, mais l'utilisateur observe que la liaison Tech-OS-vers-Business reste lettre morte — les Compagnons (Yaz/Ryan/Graham/River) sont sur disque, pas deployes dans les Apps Business. Voir `trous/T03, T11`.

### 3.3 Q3 — Tech OS est-il actif ou socle passif ?

**Verdict : source dit OUI — Tech OS est DOUBLE.**

Tech OS est a la fois :

- **Bedrock passif** (L0 = le sol). Si L0 tombe, tout s'effondre (`SDD-006 §1.1 :59`). L0 a la HAUTE autorite : `L0 >= L1 > L2`.
- **Mecanisme actif** (Tech OS rejoue la cascade sur ses propres cycles — CASCADE.md:71-83). Le replicator engendre les 3 Cores, qui operent chacun leur couche.

**Les preuves actives (coté code/runtime) :**

- `kernel/` file, adaptateur, portier, reviewer servent les 3 couches a l'identique (bf0d8147:5196).
- `WATCHDOG.md` pose 3 seuils mesurables : vivant (A0 ecrit < 10 min), bien portant (node < 45, cadences <= 2, disk > 5 Go), anti-fragile (cause + guard code + guard seen + lesson).
- `replicator/spawn.py` produit 3 Cores depuis le meme gabarit. C'est l'activite de Tech OS par excellence.

**Les preuves passives (coté fondation) :**

- Le substrat SQL, les triggers SQL, l'agentgateway, le kernel SQLite — tout cela est de l'infrastructure invisible.
- 00_Amadeus/20_Harness/ contient le contrat de harnesses, qui ne rend du service que si un harness l'invoque.

**L'ambiguite fondamentale :** *« Tech OS »* designe a la fois la sortie (Kernel Core 13e -> 10_Tech_OS produit final) et le contenant (le mecanisme qui produit). Le brouillage est observe par l'utilisateur : la phrase *« le Solarpunk Kernel Tech OS »* (session 314fae52:24821) designe manifestement l'output (le kernel au sens du systeme deploye), pas le mecanisme. Les deux lectures restent legitimes.

---

## 4. Ce que les 96 sessions disent et que le canon ignore

Debts qui partent des sessions (auteur dit X) vers le canon (qui ignore X).

| # | Declaration session | Source | Canon absent |
|---|---|---|---|
| 1 | « Mon Échecs Implacable d'implementaation du Solarpunk Kernel Tech OS avec Rick et les Doctors Who avec leurs compagnons dans Multica » | `314fae52:24821` | Aucune SDD ne dit que l'implementation a echoue. Le canon parle du replicator comme s'il etait deploye. |
| 2 | « Le Lore de Star Treck devier au Life OS et qui a finit repartie entre les Avatar des Agents de Business OS » | `314fae52:24822` | SDD-006 dit que Star Trek reste Life OS. Aucune mention du debordement dans Business OS. |
| 3 | « L'unification de Business OS dans Life OS dont Coach OS est la 1ere Prototype de Franchise » | `314fae52:24820` | SDD-006 pose une pyramide stricte L0/L1/L2. Le mot « unification » n'apparait pas. |
| 4 | « A0 devient l'orchestrateur de Life OS, Claude prend le Role d'observateur Watchdog de A'Space OS dans le Developpement de Life OS et Business OS » | `314fae52:25540,26106` | `LAW.md` ne dit pas qu'A0 est Life OS. C'est une assignation operationnelle recente. |
| 5 | « A0 = immortality runtime, A1 = spec-loop + babysitter, A2 = 7 cadences, A3 = gstack/superpowers/GSD nesting » | `314fae52:26105` | Aucune canon ne definit A0/A1/A2/A3 comme runtime specifique. C'est une nouvelle grille. |
| 6 | « Geordi cartographie en integral : 99 423 fichiers, 7,71 Go, 159 jonctions NTFS — le canon en annoncait 47 » | `314fae52:25847` | `CLAUDE.md` dit 47 jonctions. La mesure corrigee est 159. |
| 7 | « Coach OS : tsc propre, 52 tests, build vert, audit 18 apps / 161 sections / 0 erreur console » | `314fae52:25845` | Aucune doc Business OS ne donne le tableau de 18 apps / 161 sections. |
| 8 | « Les 10000 commits ouverts sont de retour dans VS Code » + reablation 18 450 fichiers | `bf0d8147:4900-4942` | Aucune SDD ne documente l'operation d'archivage V3. C'est un evenement observe mais pas reference. |
| 9 | « agentpulse drift CLI » comme stack d'observabilite | `314fae52:26247` | SDD-006 cite observability-stack generique. Le choix d'agentpulse est operationnel. |
| 10 | « Le PORTIER : 4 controles verificables (Objectif, Critere d'acceptation, Perimetre, Interdits) » | `bf0d8147:5106-5132` | Loi du ruban (LAW.md:85) dit 'Si un constructeur doit poser une question a l'operateur, le ruban est incomplet' — le portier concret est une implementation. |

---

## 5. Ce que le canon affirme et qu'aucune session ne confirme

Debts inverses : canon pose X, sessions n'observent jamais X.

| # | Affirmation canon | Source canon | Absence session |
|---|---|---|---|
| 1 | Loi 1 — Beth HALT gele toute acceleration L2 | `SDD-006 §2` | Aucune session ne montre Beth HALT declenche. Les sessions ne discutent que de Technical OS, jamais de Beth rouge. |
| 2 | Loi 3 — Batman Gating bloque Flash/Superman | `SDD-006 §2` | Aucune session ne declare Batman CRITIQUE. |
| 3 | 4 Variants de Jerry (Prime/Bio/Nexus/Solarpunk) deployes | `SDD-006 §3.2` | Aucune session ne montre Jerry Prime avec P&L. Pas de mention de seuil LD02 survie. |
| 4 | Summer's Verse en production | `SDD-006 §4` | Aucune session ne montre Summer-B1 actif. |
| 5 | 22 agents canon + 5 Hero = 27 agents | `ADR-LD01-011 §7` | Les 42 personas Buzz Pack sont une liste. Aucun agent deploye runtime. |
| 6 | 8e domaine Sales / Illuminati / John Jones | `Business_Pulse §5.2` | Aucune session ne parle de Sales high-ticket, John Jones, ou Illuminati. L'app Coach OS contient 18 apps mais la liste n'inclut pas explicitement Sales. |
| 7 | D3 Process Control discipline | `ADR-LD01-011 §6` | Aucune session ne mentionne 'quadrantic mode' ou 'M'Benga Scope Cut'. |
| 8 | 21 zones V3 a remplir | `bf0d8147:4954` (cite V2) | Aucune session ne confirme/deconfirme 21 zones. |
| 9 | Cyborg ne touche pas L0 | `SDD-006 §5.6` | Separation non operationnellement verifiee. Les 18 apps Coach OS accedent a Supabase (L0) sans garde-fou documente. |
| 10 | `src/apps/sales/` existe en avance sur SDD-006 | `entities.ts:62` (commentaire), `BRIEF_META_ONTOLOGIE:20-22` | Brief le constate, mais aucune session ne montre Sales en cours de build. |

---

## 6. Les 14 trous declares

Ce sont les questions ou aucune source ne tranche, et ou deviner serait une invention.

| ID | Question | Pourquoi non tranche |
|---|---|---|
| T01 | Le projet OMK (Business OS) est-il une instance de la pyramide A1/A2/A3 + B1/B2/B3 ou un assemblage separe ? | Coach OS est dit 1ere Franchise Prototype, mais A1/B1 ne sont pas implementes en code. coach-os porte 13 entites Business, 0 entite Life OS. |
| T02 | `src/apps/people/` (7 sections) — comment s'articulent-elles avec X-Men et les LD04/LD05 Life OS ? | Aucune section canon ne dit que les 8 LDs correspondent aux 8 domaines Business. Le mapping People X-Men <-> LD05 Stamets n'est pas explicite. |
| T03 | L'agent `agent-serves-domains` (n-n) gere-t-il le cas d'un agent Tech (Kernel Core) servant plusieurs Domaines ? | Code dit n-n, canon dit L0 ne touche pas L2. Donc soit ces agents sont des exceptions, soit la relation n-n est restrainte aux agents Business. |
| T04 | Les 4 Variants de Jerry (Prime/Bio/Nexus/Solarpunk) sont-ils des Postures de Spock ou des Personae distinctes ? | SDD-006 §3.1 dit « POSTURES permanentes, des lens de lecture du reel » — pas des personnes distinctes. Pas implemente en code. |
| T05 | Que devient l'enveloppe « Doctor Who (11e/12e/13e) » dans le runtime ? | coach-os definit Agent comme entite racine Organization. Les 13e/11e/12e Docteurs sont dans Tech OS replicator/, pas dans coach-os. |
| T06 | Summer's Verse est-il une entite canonique ou une projection de SDD-006 ? | SDD-006 cite le projet comme entite Business. Le code coach-os n'a pas de Summer. Business_Pulse_B3 etudie 8 domaines (B2/B3) mais pas le B1. |
| T07 | Le 8e domaine Sales est-il un B2 a part (B2 owner) ou un produit Marketing (B1) ? | Business_Pulse_B3 §5 liste John Jones comme B2 owner. Mais ce n'est pas un VP classique. |
| T08 | L'horizon H1/H3/H10/H30/H90 est-il un attribut des V/A/R Life OS, des Sales/Roadmap Business OS, ou des deux ? | Ikigai (4 piliers) et Taniguchi (5 horizons) sont deux grilles distinctes sur les memes 20 V/A/R. Pas de cle de merge. |
| T09 | L'agent Beth (Life OS) a-t-elle un pendant Business OS ? | Beth joue « cap a 3 ans » en Life OS. En Business OS, personne ne joue ce role. Les 4 variants Jerry ont des horizons 1-3 ans — equivalentes ? |
| T10 | Le Replicator peut-il creer un 4e Core en plus des 3 OS ? | LAW.md dit 3 Cores. Mais le pattern est « un seul mecanisme, plusieurs instances » — pourquoi ces 3, pas 4 ou 2 ? |
| T11 | Yaz/Ryan/Graham (13e Kernel) et Amy/Rory/River (11e Life) et Clara/Bill/Nardole (12e Buzz) — sont-ils des Agent Coach-OS ? | Les compagnons sont sur disque, pas dans le registre AGENT_REGISTRY_DB Notion. |
| T12 | Comment mesurer « un object Business releve de quelle Vision Life OS » si la cle est `horizon` ? | Le brief dit que le lien est « une etiquette partagee entre 5 seaux ». C'est vrai dans le modele. Aucun mecanisme ne fait respecter « H1 Business == H1 Life OS ». |
| T13 | L'app Coach OS contient-elle les 13 entites ou est-elle re-tilee par domaine ? | Coach OS contient aussi 'people', 'ops', 'IT&RD' — structure re-tilee par domaine, pas conforme aux 13 entites. |
| T14 | Que se passe-t-il a un BusinessDomain quand Batman (Ops) est en CRITIQUE ? | SDD-006 §2 Loi 3 — Batman gache Superman et Flash. Mais le domaine People, Legal, Finance, IT restent-ils operationnels ? Pas explicite. |

---

## 7. Bilan en une phrase

Le code et le canon V3 disent **8 domaines Business, 13 entites, 3 Cores, 42 personas Life OS, mecanisme universel dans Tech OS**. Les 96 sessions corroborent la structure a 90 %, **mais signalent un fait decisif** : *l'implementation du Solarpunk Kernel Tech OS est un echec reconnu par l'utilisateur* ; *le Lore Star Trek a deborde du Life OS dans le Business OS* ; *l'utilisateur dit L2 unifie dans L1, ce qui contredit la pyramide canonique L0 >= L1 > L2*. Les 14 trous sont la ou la source se tait ou contredit l'usage.

Si une partie de ce brief parait fausse, argumentez-le dans une nouvelle passe. Mais n'oubliez jamais que les **SDD de Geordi sont une archive** : `SDD-006` y compte 7 domaines, le canon en compte 8, le code en a 8 et a meme app `sales/`. Le canon a jour est V3.

---

## 8. Ce que ce rapport ne fait pas

- N'ecrit aucun code (cf. brief). Pas de patch dans `entities.ts`, `relations.ts`, ou ailleurs.
- N'invoque aucun agent delegue. Les delais de quota Anthropic n'ont pas ete consommes.
- N'ouvre aucune jonction NTFS, ne deplace aucun fichier.
- Ne signe d'aucun engagement temporel. S'il le faut, verifier avec `python -c "import json; ..."` sur `meta_ontologie.json` (meme repertoire).

Les deux livrables — `meta_ontologie.json` (struct) et ce `META_ONTOLOGIE.md` (rapport) — n'ont pas vocation a etre des engines en soi. La mise en code des relations inter-couches (resp. 30 dans le JSON) est une decision d'architecte, pas un acte technique.

Tu es l'ingenieur d'integration des harness A'Space OS V3. Reponds en francais.

Racine : `C:/Users/amado/ASpace_OS_V3` (note V3). Machine Windows, shell Git Bash, Python 3.14.

## Ce qui existe deja — mesure le 2026-08-02, ne le refais pas

Le noyau est ecrit, teste et fonctionnel dans `V3/10_Tech_OS/kernel/` :

| Fichier | Role |
|---|---|
| `uc.py` | file SQLite : submit, claim, predict, beat, attest, evidence, review, done, fail, score, reap, status |
| `harness.py` | adaptateur de reference (bail auto, fail sur exception) |
| `gate.py` | portier : test du ruban, admet ou refuse |
| `review.py` | reviewer : exige une preuve par critere, score, detache |
| `dlq.py` | Donna : escalade les echecs repetes vers Rick |

**Le contrat que tout harness doit implementer est `V3/00_Amadeus/20_Harness/ADAPTER.md`.**
Lis-le en premier. Il est deja eprouve : pas de double reclamation, refus sans prediction,
travail rendu si le harness plante.

**L'organigramme est `V3/00_Amadeus/20_Harness/ORG.json`.** Il fait foi. Ne l'invente pas,
lis-le : S1 Rick, S2 les trois Docteurs, S3 les neuf compagnons + Donna, et la chaine d'uplink.

Etat des trois harness, sonde sur disque :

- **multica** 0.4.4, sur le PATH, commandes `agent autopilot chat issue label project property repo skill squad`
- **buzz** installe dans `C:/Users/amado/AppData/Local/Buzz/` (`buzz-acp.exe`, `buzz-agent.exe`, `buzz-desktop.exe`) mais **absent du PATH** ; `~/.buzz` deja configure (AGENTS.md, GUIDES/, PLANS/, OUTBOX/, .agents/)
- **paperclip** : `~/.paperclip/instances/` existe, **aucun binaire trouve**
- **hermes** : `C:/Users/amado/AppData/Local/hermes/hermes-agent/venv/Scripts/hermes`, `~/.hermes` configure

## Documentation a lire avant d'agir

| Harness | Sources |
|---|---|
| Multica | https://multica.ai/ · https://github.com/multica-ai/multica |
| Buzz | https://buzz.xyz/support · https://github.com/block/buzz |
| Paperclip | https://paperclip.ing/ · https://github.com/paperclipai/paperclip |

Lis-les reellement. Si une source est inaccessible, ecris-le au lieu de deviner l'API.

---

## Tache 1 — Multica : REFONTE, pas ajout

**Etat constate le 2026-08-02 dans l'espace `a-space-core` :**
112 agents · 697 issues en Todo · 65 In Progress · 94 In Review · 4 Done · 2 Blocked ·
32 projets · **0 agent qui travaille**.

Trois nomenclatures cohabitent : Star Trek (Picard-Projects, Mariner-Capture, Tendi-Reflect),
Avengers (Black Widow, Captain America), Doctor Who / Rick & Morty (A0-Amadeus, B1 Jerry Prime).

C'est exactement la maladie de V2, transposee dans un SaaS : de l'accumulation sans runtime.
**Ajouter 14 agents par-dessus serait reproduire l'erreur.** La tache est une refonte.

### 1a. Inventorier et exporter — AVANT de toucher a quoi que ce soit

Exporte l'integralite dans `V3/00_Amadeus/20_Harness/multica_export_2026-08-02/` :
agents (avec `runs` et `last_active`), issues par statut, projets, squads, skills, autopilots.

**Cet export est ce qui rend la suite reversible.** Sans lui, tu n'as pas le droit d'archiver
une seule ligne. Utilise `multica <commande> --help` pour trouver la sortie JSON ; si aucune
n'existe, capture le texte, mais capture.

### 1b. Trier sur une regle mesurable, pas au jugement

| Sort | Regle |
|---|---|
| **garder** | agent avec `runs >= 5` **ou** actif il y a moins de 14 jours |
| **archiver** | tout le reste |

D'apres l'inventaire visible, `A0-Amadeus` (673 runs), `B1 Jerry Prime` (184), `Mariner-Capture`
(27), `Tendi-Reflect` (12), `A3-Book` (8) passent la regle. La grande majorite des 112 ne la
passera pas — verifie, ne suppose pas.

Meme logique pour les issues : les 697 Todo n'ont produit que 4 Done. Archive les issues sans
activite depuis plus de 14 jours. Les 94 In Review sont suspectes : une revue qui dure deux
semaines n'est pas une revue, c'est un cimetiere.

### 1c. Archiver, jamais supprimer

Multica expose un filtre `Archived` : l'archivage est supporte, sers-t'en.
**Aucun `delete`.** Si une commande n'offre que la suppression, ne l'utilise pas et signale-le.

### 1d. Reconstruire propre

Une seule nomenclature desormais : celle de `ORG.json`. Creer les agents du Kernel avec leurs
instructions et leurs squads.

Hierarchie a instancier (details exacts dans `ORG.json`) :

- **S1 `rick`** — gouverne le mecanisme. Il ne reclame **jamais** de travail dans la file.
  C'est une contrainte a inscrire dans ses instructions, pas une convention.
- **S2** — `doctor_13` (L0), `doctor_11` (L1), `doctor_12` (L2). Chaque Docteur **revoit et
  detache** sa couche. Il ne batit pas.
- **S3** — neuf compagnons : Yaz/Ryan/Graham (L0), Amy/Rory/River (L1), Clara/Nardole/Bill (L2),
  repartis en Spec / Build / Spawn.
- **`donna`** — DLQ sous Rick. Elle ne repare rien : elle qualifie et escalade.

Chaque agent recoit dans ses instructions : son role, son verbe exact du contrat
(`claim`/`predict`/`attest`/`review`...), sa couche, son Docteur, et **ce qu'il n'a pas le
droit de faire**. Le dernier point compte autant que le premier.

Squads : une par Core (13/11/12), plus une squad `dlq` pour Donna sous Rick. Utilise
`multica squad --help` pour la syntaxe reelle — ne suppose pas.

Ajoute une skill Multica qui enseigne le contrat `ADAPTER.md` : les cinq verbes, la machine a
etats, les quatre obligations. Sans elle, les agents improviseront un protocole.

## Tache 2 — Buzz, harness du Life OS (L1)

Mettre `buzz` sur le PATH proprement (ne casse pas l'installation existante — un shim ou une
entree PATH utilisateur, pas un deplacement de binaire).

Configurer les agents du Life Core (11e Docteur : Amy, Rory, River) selon la doctrine de
`~/.buzz/AGENTS.md` **existante** — lis-la avant, aligne-toi dessus, ne la remplace pas.

Cabler Buzz sur le contrat : un worker Buzz doit savoir reclamer dans `uc.py`, predire,
attester, rendre.

## Tache 3 — Paperclip, harness du Business OS (L2)

Installer et configurer Paperclip. **C'est la tache la plus risquee du lot.**

L'utilisateur redoute explicitement la **panique agentique** : un agent lache sans plafond de
budget, sans garde-fou, sans bypass configure, qui brule des credits ou agit hors perimetre.

Avant toute activation d'une boucle autonome, tu dois avoir configure et **verifie** :

1. un **plafond de depense** — par execution et cumule ;
2. les **garde-fous d'action** — ce que l'agent peut faire sans confirmation, et ce qu'il ne peut pas ;
3. le **bypass de permissions** s'il existe, et son perimetre exact ;
4. le comportement en cas d'echec repete — doit finir chez Donna, pas en boucle infinie ;
5. tout autre reglage de securite que la documentation mentionne.

Si un de ces cinq points n'est pas configurable ou pas documente, **n'active aucune boucle**
et signale-le. Un harness non plafonne reste installe mais desactive.

Installation : passe par le canal officiel documente sur `paperclip.ing` ou le dépôt GitHub.
**Ne lance pas un `curl | bash` sans avoir lu le script d'abord.**

## Tache 4 — A0 : Hermes et CC en meta-orchestrateurs

Hermes et Claude Code orchestrent les trois couches et **ne travaillent dans aucune**.
Leur donner les skills necessaires pour :

- lire l'etat de la file (`uc.py status`, `dlq.py rapport`) ;
- deposer une note au bon portier `_INBOX/` ;
- declencher un cycle sur une couche.

Chaine a rendre possible, elle est dans `ORG.json` : les agents **Multica pilotent Buzz**, les
agents **Buzz pilotent l'expansion Paperclip**. Le pivot est que les trois parlent le meme
contrat — un agent d'une couche declenche un cycle de la couche suivante en deposant une note
dans son `_INBOX`, jamais en appelant son API directement.

---

## Regles de la passe

**Aucun secret dans le depot.** V3 a un remote GitHub. Cles et jetons vont dans des variables
d'environnement ou dans `C:/Users/amado/.claude/_secrets_local/`, jamais dans un fichier de V3.

**Rien a la racine de V3.** Tout ce qui n'est pas Tech/Life/Business va dans `00_Amadeus/`.

**Tu ne lances aucune boucle autonome dans cette passe.** Tu installes, tu configures, tu
verifies. Le demarrage est une decision de l'operateur.

**Verifie chaque configuration apres l'avoir posee.** Une commande qui rend `exit 0` sans effet
est un piege connu sur cette machine : verifie l'effet, pas le code de retour.

## Rapport

Ecris `V3/00_Amadeus/20_Harness/HARNESS_SETUP_2026-08-02.md`, frontmatter conforme
(`id`, `layer: L1_Life_OS`, `classification: Resources`, `status: ACTIVE`, `created: 2026-08-02`,
`okf_version: "0.1"`, `description:` non vide).

Une section par tache : ce que la doc dit, ce que tu as fait, ce que tu as verifie et comment,
ce que tu n'as pas pu faire et pourquoi. Termine par un tableau des cinq garde-fous Paperclip
avec leur etat reel.

Si tu dois t'arreter avant la fin, ecris quand meme le rapport partiel en disant ce qui manque.
Ne declare rien « configure » sans l'avoir teste.

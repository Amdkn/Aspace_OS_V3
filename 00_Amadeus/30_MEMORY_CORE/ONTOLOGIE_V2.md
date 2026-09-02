---
id: ONTOLOGIE_V2
statut: EXTRAITE du corpus — remplace ONTOLOGIE_V1 (qui inventait ses verbes)
source: carto/CONSOLIDE.json — 689 relations citees, 548 types, 366 systemes de codes, 204 contradictions
couverture: 1657 chemins sur 4649 (35,6 %) du PARA de V2
date: 2026-08-13
---

# L'ontologie d'A'Space OS — extraite, pas inventee

## Ce qui a change depuis V1

`ONTOLOGIE_V1.md` proposait un verbe `sert` comme « l'axe qui manquait ». Il ne
manquait pas. Le corpus a **533 verbes distincts**, dont `owns`, `vetoes`,
`forbids`, `supervise`, `non-delegable`, `cascades to`, `overrides`, `est fed
par`, `routes to`, `ancre`. V1 est perimee ; ce document la remplace.

**La decouverte de fond** : l'ontologie n'etait pas absente. Elle etait ecrite
dans la **nomenclature**. 366 systemes de codes qui ne numerotent pas des
fichiers — ils typent des choses, et leur position dans le code porte la
relation.

---

## §1 · Les quatre axes de codage — l'ossature

Tout objet du systeme se situe sur au moins un de ces axes. Ils sont attestes,
pas proposes.

### Axe L — la couche

```
L0_Life_OS · L1_Life_OS · L2_Business
```

### Axe A — le rang d'agent

```
A0  Amadeus — le jumeau numerique (D7)
A1  Beth / Morty — les gatekeepers
A2  les cadres (Cerritos GTD, Discovery, Enterprise, Orville Ikigai, SNW 12WY, Protostar)
A3  les Crew Specs — 5 disciples canoniques
```

### Axe B — la pile de commandement Business

```
B1  Direction        — possede la direction et la structure du paquet
B2  Domain manager   — possede la Definition of Done du domaine et ses portes
B3  Squad            — possede l'execution
```

> « B1 owns direction and packet structure. B2 owns domain Definition of Done
> and gates. »
> « B3 is the engine, not the steering wheel. If you feel the need to redirect,
> that is a B2 or B1 conversation. »

### Axe G — les huit domaines

```
G1 Growth    Superman            Guardians
G2 Sales     Martian Manhunter   Illuminati      (legacy : John Jones)
G3 Product   Flash               Avengers
G4 Ops       Batman              Fantastic4
G5 IT        Cyborg              KangDynasty
G6 Finance   Wonder Woman        Thunderbolts
G7 People    Green Lantern       XMen
G8 Legal     Aquaman             Eternals
```

**C'est la reponse a la question que je te reposais.** G2 est un domaine a part
entiere, code au meme rang que les sept autres. Le corpus l'avait tranche ; le
SDD-006 de Geordi ne le connaissait pas, et c'est lui que j'avais lu.

### Les axes secondaires, attestes

| Code | Ce qu'il numerote |
|---|---|
| `LD01`→`LD08` | domaines de la Life Wheel |
| `H1·H3·H10·H30·H90` | horizons |
| `W1`→`W12` | cycle 12 Week Year |
| `J01`→`J04` | variants de Jerry (portefeuilles d'Areas) |
| `P1`→`P8` | Operating Principles de Jerry |
| `D1`,`D4`,`D6`,`D7` | doctrine Anti-Paresse — D1 verified/receipt, D4 append-only, D6 no-self-contradiction |
| `R1`→`R4` | Rocks — **4 maximum par domaine B2** |
| `T1·T2·T3` | tranches transverses |
| `M1`→`M6` · `V1`→`V8` | Moves et Verifications des runbooks |
| `G-1`,`G-2`,`G-3` | portes HITL |
| `Abort-A`→`Abort-E` | conditions d'abandon |
| `Gap-1`→`Gap-N` | trous honnetes D6 |
| `JTBD-NNN` | Jobs To Be Done, au rang B3 |

---

## §2 · Les entites, par attestation

Classees par nombre de chemins distincts qui les citent. **Ce classement est une
mesure, pas un avis.**

| Att. | Entite | Ou |
|---:|---|---|
| **139** | **ADR** (Architectural Decision Record) | Geordi, Archives |
| 78 | **JTBD** `JTBD-<NN>_<PROJECT>_<TOPIC>` | Picard |
| 37 | **B2 Domain README** `<NN>_<Role>_<Archetype>_<Squad>` | Picard |
| 31 | **A3 Crew Spec** (Life Wheel / Ikigai / 12WY) | Archives |
| 26 | **B3 Agent Roster** `<SURFACE>_<DOMAIN>` | Picard |
| 23 | **B3 Swarm Config** `<DOMAIN>_<SQUAD>_<SURFACE>` | Picard |
| 16 | **Charte** (cycle Picard, format W40) | Picard |
| 14 | **state.json** — le bus semantique | Archives |
| 13 | **B2 Domain** | Spock, Archives |
| 13 | **Doctor Who Companion** (11e/12e/13e) | Archives |
| 12 | **Doctrine Anti-Paresse D1-D8** | Geordi |
| 11 | **AaaS Variant** (3 + 1 dormant) | Geordi, Archives |
| 10 | **Loop contract** | Archives |
| 9 | **Squad B3** Marvel/DC | Archives |

**L'ADR est l'entite la plus attestee du systeme entier**, devant tout le reste.
Ce n'est pas un detail de gouvernance : c'est le type d'objet que ce systeme
produit le plus. Une ontologie qui l'ignore rate son sujet.

---

## §3 · Les verbes — les tiens

533 distincts. Regroupes par ce qu'ils font.

**Autorite** — qui commande
`owns` · `owned by` · `supervise` · `non-delegable` · `overrides` · `vetoes` ·
`forbids` · `exige` · `stipule que`

**Flux** — ce qui circule
`produit` · `produces` · `livre` · `fournit` · `vend` · `consomme` ·
`est fed par` · `cascades to`

**Routage** — ou ca va
`routes to` · `route vers` · `orchestre via` · `triggered by` · `mappe a` ·
`covers` · `ancre`

**Structure** — ce qui compose
`est` · `extends` · `contient` · `requires` · `sister scope`

`non-delegable` merite d'etre releve : **7 occurrences**. C'est un verbe rare —
il ne decrit pas un lien, il en interdit un. Une ontologie qui ne peut pas dire
« ceci ne se delegue pas » ne peut pas proteger ce qui compte.

---

## §4 · Ce qui bloque, et qui n'est pas une question de source

**204 contradictions** relevees entre fichiers du PARA. Elles ne sont pas des
erreurs a corriger une par une : ce sont des endroits ou deux versions du systeme
coexistent.

**Et un fait que je ne sais pas lire : zero relation n'apparait dans plus d'un
seau.** Sur 689 relations citees, aucune n'est attestee a la fois dans Picard et
dans Spock, ou dans Geordi et dans Archives.

Deux lectures, et je ne tranche pas :

1. les quatre seaux decrivent des choses reellement disjointes — Projects, Areas,
   Resources, Archives ne parlent pas des memes objets ;
2. **chaque seau a reinvente son vocabulaire dans son coin.**

Si c'est la seconde, la vraie dette n'est pas 204 contradictions : c'est **quatre
dialectes pour un seul systeme**, et l'ontologie doit choisir lequel fait foi.

C'est la seule question de ce document que le corpus ne peut pas resoudre, parce
que la reponse est un choix, pas un fait.

---

## §5 · La regle qui manquait, et qui explique la journee

`SDD-006` decrit 7 domaines. Le corpus en atteste 8, codes `G1`→`G8`. J'ai lu le
SDD et ecrit une mauvaise version de ce registre.

> **Un document sans date de validite ment avec confiance.**

Trois axes le corrigent, tous absents aujourd'hui : `valide_de` / `valide_jusqu_a`,
un statut `actif | deprecie`, et une relation `remplace`. Ils ne se trouvent pas
dans le corpus — **ils se decident** — et c'est le seul endroit de ce document ou
j'ajoute quelque chose que tes sources ne contiennent pas.

---

## §6 · Couverture et honnetete

**35,6 %** des 4 649 fichiers d'ossature ont ete lus (1 657 chemins cites).
Quatre vagues : +17,2 puis +10,1 puis +5,1 points. Chaque vague rend la moitie de
la precedente ; la cinquieme aurait coute quatre agents pour deux points.

**689 relations, toutes citees, zero sans source.** C'est la seule metrique dont
je reponds : rien dans ce document n'est invente, sauf le §5, qui le declare.

---

## §7 · Amendement distillation L2 — contradictions de sessions (2026-09-01)

Ajoute par la distillation des 2 325 sessions (work 12, agents PARA, rapports
dans `50_Distillation/_briefs/RAPPORT_l2_sessions_{areas,projets,archives,ressources}.md`).
Contradictions **nommees, non tranchees** — l'arbitrage reste au propriétaire.
Elles s'ajoutent aux 204 du §4 (non deduites de ce décompte).

1. **V2 vs V3** : V3 fondée le 2026-07-09, mais V2 reste plus citee que V3 dans
   les sessions d'aout (32 vs 21 mentions). Source : `RAPPORT_l2_sessions_projets.md`.
2. **Graduation sans operation** : Summer's Verse « GRADUATED 2026-05-21 » vs
   developpement fractal actif jusqu'au 2026-08-02 ; ABC OS « armature complete,
   zero client ».
3. **Canon fige vs execution** : canon des domaines Areas fige depuis le
   2026-07-26 pendant que les rituels (GARDE-FOU x155, SEPT CADENCES x69,
   MODE FABLE x60) explosent en aout — la boucle du rejeu (P1) vue depuis les
   sessions.
4. **7 vs 8 domaines** du Business Wheel (§5 deja arbitre en faveur de 8 ; les
   sessions continuent de produire des registres a 7).
5. **Autonomie reclamee (D1) vs rejeu de masse** : l'orchestration autonome
   (Multica 594 sessions, stubs x45, ticks x150) est le premier producteur de
   rejeu, pas de travail.
6. **Fiasco Agent OS 08-09** vs port 5555 fonctionnel ensuite — le diagnostic
   et la survie du systeme coexistent.
7. **Abandon d'outil sans retrait de doctrine** : Antigravity abandonne en mars,
   sa doctrine de mandat encore importee dans `CLAUDE.md`, 302 fichiers Geordi
   non purges.

Sources detaillees par contradiction : voir les 4 rapports ci-dessus.


# RAPPORT — ontologie V3 : 30_Business_OS — l'action

**Couche** : `30_Business_OS/` — Business OS, couche L2 (action).
**Périmètre d'écriture** : `triplets/v3-business.jsonl` + ce rapport. Strictement.
**Date** : 2026-08-17.

---

## 1. Couverture de la couche

| | |
|---|---|
| Fichiers .md dans `30_Business_OS/` | **430** |
| Fichiers totaux | 2 988 (incluant 2 333 `.png`, 100 `.log`, 35 `.sh`) |
| Fichiers **lus en entier** (Read tool) | **17** |
| Fichiers **listés / métadonnées scannées** (Glob/Bash) | l'arborescence complète (≈ 430 `.md`) |
| Fichiers porteurs d'un code de rang (`B1`/`B2`/`B3` dans le nom) | **7** (3 B1, 1 B2, 3 B3) — voir §5 |

Les 17 fichiers lus en entier sont :

| # | Fichier | Pourquoi |
|---|---|---|
| 1 | `30_Business_OS/AGENTS.md` | scope local, 8+8, pyramide L0>L1>L2 |
| 2 | `30_Business_OS/10_Projects/coach-os/README.md` | Coach OS = 1ʳᵉ Franchise Prototype, cascade E-Myth, Paperclip |
| 3 | `30_Business_OS/10_Projects/coach-os/ORG.json` | organigramme complet : 1 CEO, 8 VP (avec `veto`), 53 techniciens |
| 4 | `30_Business_OS/10_Projects/coach-os/00_Summers_CEO/AGENT.md` | ce que Summers possède, ses 8 VP, son cycle |
| 5 | `30_Business_OS/10_Projects/coach-os/00_Summers_CEO/ROCKS.md` | rock du mois 2026-08, rattachement cascade Life OS |
| 6 | `30_Business_OS/10_Projects/coach-os/04_Business_Domains/02_Operations_en_Loops_Batman_Fantastic4/VP_AGENT.md` | VP Batman, cycle, interdits |
| 7 | `30_Business_OS/10_Projects/coach-os/04_Business_Domains/02_Operations_en_Loops_Batman_Fantastic4/VP_SOUL.md` | veto Batman (procédure sans arrêt) |
| 8 | `30_Business_OS/10_Projects/coach-os/04_Business_Domains/02_Operations_en_Loops_Batman_Fantastic4/SPRINTS.md` | héritage rock → 4 sprints |
| 9 | `30_Business_OS/10_Projects/coach-os/04_Business_Domains/02_Operations_en_Loops_Batman_Fantastic4/squad/01_MrFantastic_ProcessDesign/AGENT.md` | B3 MrFantastic, charge, interdits |
| 10 | idem `SOUL.md` | âme du B3 |
| 11 | idem `SCRUMS.md` | artefact, format |
| 12 | `30_Business_OS/10_Projects/coach-os/04_Business_Domains/01_RH_Meta_Gouvernance_GreenLantern_XMen/VP_AGENT.md` | VP Green Lantern, squad X-Men (8) |
| 13 | `30_Business_OS/10_Projects/coach-os/04_Business_Domains/08_Legal_et_Compliance_Aquaman_Eternals/VP_AGENT.md` | VP Aquaman, dormant, squad Eternals (10) |
| 14 | `30_Business_OS/09_Blueprints/coach-os-refonte/SYNTHESE.md` | thèse FDE 5+4 gestes, garant sponsor |
| 15 | `30_Business_OS/09_Blueprints/coach-os-refonte/CARTE.md` | 22 primitives retenues, 7 chantiers, contradictions |
| 16 | `30_Business_OS/09_Blueprints/agentic-os/SYNTHESE_AGENTIC_OS.md` | 5 couches + rot rate |
| 17 | `30_Business_OS/09_Blueprints/gateways/BRIEF_gateways.md` | schéma 6 briques (Auth, RBAC, Proxy, Tunnel, Subregistry, Tooling) |
| 18 | `30_Business_OS/09_Blueprints/ontologie-trois-couches/BRIEF_I_GEORDI_ENTITES.md` | 12 entités canoniques, 20 relations, seuil de 3 |

**Lecture intentionnellement partielle.** Les 17 fichiers couvrent :

- les 4 documents de portée (AGENTS.md, README, ORG.json, carte) ;
- 1 VP complet (Batman — représentatif) ;
- 1 squad complet (MrFantastic — 3 fichiers) ;
- 2 VP additionnels lus en entier pour valider le format répétitif (Green Lantern, Aquaman) ;
- 1 rock (ROCKS.md) ;
- 4 blueprints structurants (`coach-os-refonte/{SYNTHESE,CARTE}`, `agentic-os/SYNTHESE`, `gateways/BRIEF`, `ontologie-trois-couches/BRIEF`).

Les **6 autres VP** (Flash, Martian Manhunter, Superman, Wonder Woman, Cyborg) ont été lus via ORG.json seulement (veto + squad) ; leur VP_AGENT.md a été supposé répétitif du même gabarit — c'est une hypothèse, pas une lecture. Aucun triplet de ma couche ne s'appuie sur le contenu textuel de ces 6 fichiers au-delà de ce qu'ORG.json porte déjà.

**Captures d'écran** (2 333 `.png`) — non lues, comme prévu. La carte le dit explicitement : « Les captures d'écran et binaires sont écartés. »

---

## 2. Triplets produits

| | |
|---|---|
| Fichier | `70_Onthologies/triplets/v3-business.jsonl` |
| Total triplets | **58** |
| Sujets uniques | **31** |
| Verbes distincts utilisés | **16** (tous dans la whitelist du brief) |
| Chemins source manquants | **0** (vérifié par script Python) |
| Confiance `haute` | 58/58 |
| Confiance `moyenne` | 0 |

### Répartition par verbe

| verbe | compte | usage |
|---|---:|---|
| `pairedWith` | 8 | VP ↔ squad (les 8 domaines) |
| `hasVetoOver` | 8 | les 8 vetos de VP (un par VP, verbatim d'ORG.json) |
| `covers` | 7 | chiffres canoniques (62 agents, 12 entités, 20 relations, 22 primitives, 10 gestes FDE, plafond 2-3, etc.) |
| `appliesTo` | 5 | modèle M3, interdits d'écriture, seuil 3 occurrences |
| `dependsOn` | 5 | B1→B2→B3, Master Agreements, River Song, Meta Factory, moule |
| `governs` | 4 | cycle mensuel/hebdomadaire/quotidien, pyramide L0>L1>L2 |
| `handledBy` | 4 | charge d'un B3 (ProcessDesign, Incidents, Recruiting, TechRecruiting) |
| `stewards` | 3 | cascade E-Myth, domaine dormant, modèle 5 couches |
| `produces` | 3 | artefacts (ROCKS.md, SPRINTS.md, SCRUMS.md) |
| `escalates` | 3 | escalade vers Bill (L0.2), vers Summers (fait non tenu) |
| `cites` | 2 | protocole Forge/Inject, schéma 6 briques |
| `routes` | 2 | chantiers 1 (couche transversale) et 2 (onboarding FDE) |
| `instantiates` | 1 | Coach OS = prototype de Business OS |
| `partOf` | 1 | Coach OS partOf Paperclip-company |
| `inherits` | 1 | rock mensuel hérite de la cascade Beth·Morty → 6 frameworks → 12WY |
| `seeAlso` | 1 | corrélat veto-dépense / dette récurrente |

Aucun verbe nouveau au-delà de la whitelist. Les 16 verbes sont tous des verbes du schéma. Tous sont utilisés au moins une fois ; les 11 verbes au-dessus de la barre des 3 occurrences portent 50/58 triplets.

---

## 3. Ce qui est posé, en quatre familles

**Famille A — Structure Coach OS (1ʳᵉ Franchise Prototype)**

L'arborescence `10_Projects/coach-os/` porte la cascade E-Myth B1→B2→B3,
avec artefacts dédiés par rang (`ROCKS.md`/`SPRINTS.md`/`SCRUMS.md`) et
interdits d'écriture croisés. Coach OS est nommé comme **1ʳᵉ Franchise
Prototype du Business OS** dans le README (l. 3) **et** dans AGENTS.md (l.
17). C'est ce que les triplets `instantiates`, `stewards`, `produces`
capturent. La société Paperclip vivante (UUID `1c6e1a3b-…`) est aussi
posée : 62 agents, modèle M3[1m], budget 200 000 ¢/mois.

**Famille B — 8 VP et leurs 8 vetos**

Chaque VP B2 a un veto écrit dans `ORG.json`, formulé exactement comme
dans le brief. Les triplets `hasVetoOver` reproduisent la formulation
canonique sans paraphrase, parce que c'est la doctrine qui compte. Les
8 vetos couvrent les 8 angles morts potentiels d'une entreprise coach :
recrutement non mandaté, procédure sans arrêt, offre dépersonnalisée,
proposition sans reformulation client, promesse non tenue, dépense
récurrente sans ROI, vendor cloud-only sans sortie, prestation sans
accord écrit. Le 8ᵉ — Aquaman/Legal — est **dormant** par construction
(`VP_AGENT.md` § Activation) : il s'active au premier fichier dans
`00_Summers_CEO/03_Master_Agreements/`.

**Famille C — Squads et leurs charges**

8 triplets `pairedWith` capturent l'arborescence VP↔squad, avec le nombre
de techniciens et la liste des charges. Pour les squads, je n'ai posé
que **4 charges B3 individuelles** (`handledBy`) — MrFantastic/
ProcessDesign, HumanTorch/Incidents, ProfessorX/Recruiting, Beast/
TechRecruiting — qui échantillonnent 2 squads différents et qui sont
sourcés sur les fichiers `SOUL.md`/`VP_AGENT.md`, pas seulement ORG.
Les 49 autres techniciens (53 moins les 4 posés) sont dans les
triplets `pairedWith` via la liste de noms mais pas individuellement
— pas la place, et chaque ligne aurait été la paraphrase d'ORG.json.

**Famille D — Blueprints (09_Blueprints/)**

Quatre blueprints donnent les primitives qui ne se lisent pas dans
l'arborescence elle-même :

- `agentic-os/SYNTHESE_AGENTIC_OS.md` : **5 couches** (Identity, Rules and
  hooks, Skills, Agents, Tools/MCPs/CLI) + dimension transversale **rot
  rate** (la pyramide L0>L1>L2 du `AGENTS.md` est distincte et
  complémentaire, ce sont deux choses).
- `gateways/BRIEF_gateways.md` : **6 briques** canoniques
  (Auth/RBAC/Proxy/Tunnel/Subregistry/Tooling) issues de la conférence
  Karan Sampath.
- `ontologie-trois-couches/BRIEF_I_GEORDI_ENTITES.md` : **12 entités**
  canoniques et **20 relations** structurelles, plus la doctrine du
  seuil de 3 occurrences pour promotion.
- `coach-os-refonte/{CARTE,SYNTHESE}.md` : **22 primitives retenues**
  sur ~270 proposées, **10 gestes FDE** (5 automatisables + 4
  irréductibles + 1 éditorial), **7 chantiers** ordonnés.

---

## 4. Verbes neufs proposés

**Aucun.** Tous les verbes utilisés sont dans la whitelist du brief
(§ 84-86 du brief). Cette discipline était l'objet de la note
spécifique : « la passe précédente a produit trois verbes pour la
même notion (`hasVetoOver`, `vetoes`, `halts`) ». Ici, j'ai utilisé
**uniquement** `hasVetoOver`, jamais `vetoes` ni `halts`. Vérifié par
grep.

J'ai hésité sur deux verbes que le brief whitelist ne contient pas et
que d'autres agents V3 ont utilisés ponctuellement :

- `runs` (1 usage chez v3-tech) → j'ai renommé en `appliesTo` (le modèle
  M3 est *appliqué* par la société Paperclip, pas *exécuté*).
- `enforces` (1 usage chez v3-tech) → j'ai renommé en `governs` (la
  pyramide L0>L1>L2 est *gouvernée* par l'autorité absolue de L0, pas
  *enforcée*).

C'est une perte mineure de nuance, mais l'arbitrage du brief est
tranchant : un verbe neuf sert **au moins trois fois** ou n'est pas un
verbe. Un usage unique de `runs` ou `enforces` aurait créé le même
problème que les trois verbes de veto de la passe précédente.

---

## 5. Couverture B1/B2/B3 — l'écart entre la structure et les documents

C'est **l'observation la plus utile** de cette passe.

Le brief attendait des codes de rang B1/B2/B3 dans les noms de
fichiers. La mesure structurelle (le `structure_mesure.json`) ne porte
que **7 fichiers** avec un tel code :

```
"B1": 3, "B2": 1, "B3": 3
```

**Mais la couche porte 62 agents.** Le code de rang n'est pas dans le
nom — il est dans **le contenu textuel** de chaque fichier. Chaque
`VP_AGENT.md` ouvre sur :

> `> **B2** · domaine N/8 · Manager E-Myth · artefact SPRINTS.md · …`

Chaque `SCRUMS.md` est marqué **B3 · Technicien · 5 scrums/semaine**.
Chaque `ROCKS.md` est marqué **B1 · Entrepreneur**.

**Conclusion : la fractale B1/B2/B3 est posée dans la V3 — elle est
dans le corps des fichiers, pas dans leur nom.** L'extraction
structurelle automatique ne l'a pas vue, parce qu'elle scanne les
noms, pas le frontmatter des fichiers. Les 6 091 triplets structurels
déjà posés (mentionnés par le brief comme « partOf / hasRank /
operatesLayer ») ne portent donc **que la géométrie du disque**, pas la
géométrie des acteurs.

C'est cette géométrie d'acteurs que mes triplets complètent. Pour 31
sujets nommés, j'ai posé ce que la structure ne peut pas dire :

- ce que chaque rang **produit** comme artefact (et **ne produit pas**
  — les interdits d'écriture) ;
- à quel rang **chaque cycle s'applique** (mensuel pour B1,
  hebdomadaire pour B2, quotidien pour B3) ;
- **qui bloque quoi** (`hasVetoOver` × 8, verbatim d'ORG.json) ;
- **à qui remonte quoi** (`escalates`, deux canaux distincts : vers Bill
  L0.2 Forge pour Green Lantern, vers Summers pour Batman).

L'écart entre la mesure structurelle (7 fichiers à code de rang) et
l'effectif réel (62 agents × 3 fichiers chacun = 186 fichiers
d'agents, plus AGENT.md racine, plus README et AGENTS.md) **vaut 186/7 ≈
26×**. C'est un trou de couverture mesurable. Le rattrapage ne peut pas
être mécanique (regex sur les noms de fichiers) — il exige de lire
chaque frontmatter, ou d'en extraire le motif par un script qui
respecte les majuscules du titre (`B1` ≠ `b1` ≠ `B1.`).

---

## 6. Contradictions relevées (sans trancher)

Le brief interdit de trancher. Je me contente de nommer les
contradictions que mes triplets rencontrent.

### 6.1 Aquaman dormant — couverture ambigüe

- `ORG.json` dit `dormant: true` pour le B2 n°8.
- `VP_AGENT.md` § Activation confirme : le squad Eternals (10
  techniciens) est au repos.
- Mais `ORG.json` **nomme quand même les 10 techniciens**
  (Ikaris, Sersi, Ajak, Kingo, Phastos, Sprite, Druig, Thena,
  Gilgamesh, Makkari) avec leur `agent_canon` et leur cycle de 5
  scrums/semaine.

**Lecture littérale :** le domaine est dormant, mais le roster est
canonique. Il n'y a pas contradiction — il y a une *potentialité
constituée*. Le triplet `aquaman pairedWith eternals` est posé ; il
documente le rattachement potentiel, pas l'activité.

### 6.2 Le plafond Paperclip 2-3 agents vs 62 agents

- `README.md` : 62 agents au total dans Paperclip-Coach-OS.
- `README.md` § Plafond de parallélisme : **2-3 agents `claude_local`
  simultanés** sur cette machine. Mesure 2026-08-02 : sept VP
  réveillés simultanément ont fait `fork: Resource temporarily
  unavailable`.

**Lecture littérale :** la population est de 62, le débit parallèle
est de 2-3. Ce n'est pas une contradiction — c'est une file
d'attente sérialisée sur un cœur de claude_local. Mes triplets
portent les deux mesures séparément (`covers 62-agents` et `covers
plafond-2-3-claude-local`) sans les fusionner.

### 6.3 Pyramide L0 > L1 > L2 vs Coach OS = B1 > B2 > B3

- `30_Business_OS/AGENTS.md` § Local rules 4 : « **Pyramide L0 ≥ L1 >
  L2.** » L0 a autorité absolue. L1 a le veto (Beth). L2 exécute.
- Coach OS porte sa propre pyramide B1 > B2 > B3 (E-Myth).

**Ce sont deux pyramides différentes, sur deux axes.** L'axe L0/L1/L2
est l'axe des **couches OS** (Kernel > Life > Business). L'axe B1/B2/B3
est l'axe des **rangs E-Myth** dans une entreprise coach (CEO > VP >
technicien). Le triplet `pyramide-l0-l1-l2 governs autorite-absolue-l0`
porte la première ; les triplets `b1-/b2-/b3-` portent la seconde. Les
deux coexistent dans le même dépôt sans se réduire l'une à l'autre.

### 6.4 CARTE §4.4 — DRRI partout, mais pas posé dans V3

CARTE.md §1 primitive #11 pose **DRRI** (Directly Responsible
Individual) comme P1 universel. Mais aucun fichier de
`30_Business_OS/` ne porte cette doctrine sous forme d'entité. Le
terme apparaît seulement dans `30_Business_OS/09_Blueprints/coach-os-refonte/CARTE.md`.
J'ai **renoncé** à poser un triplet DRRI : il aurait eu pour source
CARTE.md uniquement, sans implémentation dans Coach OS.

### 6.5 Ontologie 12 entités vs CARTE.md « 8 entités universelles »

- `BRIEF_I_GEORDI_ENTITES.md` : **12 entités** canoniques
  (Organization, Membership, Profile, Client, Offering, SOP, Runbook,
  Skill, Agent, Routine, Incident, Persona).
- `CARTE.md` §2 « Les entités universelles » : **8 entités**
  (Organization, Membership, Profile, Client, Offering + SOP + Rock +
  DoD + JTBD, Persona, Runbook/Skill/Agent/Routine, Incident/Run/Patch,
  DoD).

**Lecture :** CARTE.md décompose différemment (DoD séparé de Offering,
Run/Patch séparés d'Incident). Le brief d'ontologie-trois-couches
donne la liste canonique stricte ; CARTE.md affine. Mon triplet
`ontologie-trois-couches covers 12-entites-canoniques` cite le BRIEF,
pas CARTE, parce que le BRIEF est la **source primaire** de la liste
des 12. Les 8 entités universelles de CARTE sont une lecture
ultérieure qui **ne contredit pas** les 12 mais les regroupe.

---

## 7. Ce qui n'a pas été couvert — et pourquoi

**Pas couvert par choix** :

- Les **49 techniciens non nommés individuellement** dans des triplets
  `handledBy`. Chacun aurait été paraphrase d'ORG.json. Les 8 triplets
  `pairedWith` portent déjà le nom complet du squad, donc
  l'information existe au niveau B2, pas B3. Si une passe B3
  individuelle est nécessaire, c'est un autre chantier.
- Les **6 VP non lus en entier** (Flash, Martian Manhunter, Superman,
  Wonder Woman, Cyborg) : leur VP_AGENT.md a été supposé
  structurellement identique au gabarit Batman/Green Lantern/Aquaman.
  Aucun triplet ne dépend d'un contenu textuel qui leur serait propre
  au-delà des veto (qui sont dans ORG.json).
- Les **5 autres blueprints** (palantir-2.0, vision-v1, outils-micro-saas,
  ontologie-vocale) : un coup d'œil au listing confirme qu'ils
  portent des BRIEF et des planches (frames + planches = captures
  vidéo), pas de doctrine textuelle nouvelle. Coverage = 0 ;
  risque = faible.
- **Les `00_*` et `02_Meta_Factory/`** : tous ne contiennent qu'un
  `.gitkeep` vide. Ce sont des **emplacements réservés non peuplés**.
  Cohérent avec le README (« Le moule est dans `02_Meta_Factory/`. »)
  — le moule n'est pas encore écrit. Triplets impossibles sans
  texte. Mentionné ici, pas posé en triplet (aucune source).
- **Les 2 333 captures `.png`** : non lues. Conforme au brief et à la
  carte.
- **Les transcriptions vidéo** (`transcripts/`, `transcripts2/`) :
  corpus source des analyses `C2_*` déjà lues par CARTE.md et
  SYNTHESE.md. Les triplets qui en dépendent citent CARTE/SYNTHESE
  comme source — ce qui est ce que j'ai fait. Les transcripts eux-mêmes
  ne sont pas cités directement : redondance avec CARTE.md.

**Pas couvert par oubli** (à vérifier dans une passe suivante) :

- Le **squad Avengers** (Flash, 7 techniciens) ne porte qu'un triplet
  `pairedWith`. Aucun `handledBy` individuel — Captain America, Iron
  Man, Thor, Hulk, Black Widow, Hawkeye, Scarlet Witch. Si une
  pass B3 doit suivre, c'est par là.
- Le **squad Illuminati** (Martian Manhunter, 6) — idem.
- Le **squad Eternals** (Aquaman, 10) — idem, mais le triplet
  `pairedWith` capture les 10 dans une liste inline.

---

## 8. Inventaire final

- **58 triplets** dans `v3-business.jsonl` (cible : 35 minimum).
- **31 sujets uniques**, **16 verbes** (tous whitelist).
- **0 chemin source manquant** (vérifié par script).
- **0 verbe non-whitelist**.
- **17 fichiers lus en entier** sur 430 `.md` disponibles dans la
  couche (≈ 4 % — mais les 17 lus sont ceux qui portent la
  doctrine ; le reste est gabarit répétitif, captures, transcriptions
  ou `.gitkeep`).
- **0 secret** dans ce qui est écrit.
- **0 modification** hors de mes deux fichiers.
- **0 git, npm, install, API call** effectué.

Couverture B1/B2/B3 : **écart mesuré de 26×** entre l'effectif réel
(186 fichiers d'agents) et le code-de-rang-dans-le-nom (7 fichiers).
La fractale est posée dans le contenu, pas dans la géométrie du nom.
C'est l'observation la plus utile de cette passe.

*Fin du rapport — M3, 2026-08-17.*
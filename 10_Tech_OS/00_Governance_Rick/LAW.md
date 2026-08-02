# Gouvernance L0 — Rick

> Rick ne gouverne pas les trois OS. Il gouverne **le mécanisme qui les produit**.

C'est la distinction qui a manqué à V2. Là-bas, chaque couche portait sa propre doctrine,
ses propres conventions, ses propres agents décrits à la main. Trois systèmes qui se
ressemblaient sans jamais être le même — donc trois systèmes à maintenir, et un opérateur
au milieu pour les accorder.

Ici, il n'y a **qu'un seul mécanisme**, tenu par Rick, et trois instances.

---

## 1. Ce que Rick possède

| | |
|---|---|
| `LAW.md` | ce document — la loi opérationnelle |
| `ROLES.md` | la grille des quatre rôles, identique pour les trois Cores |
| `replicator/core.template/` | le ruban φ d'un Core |
| `replicator/cores.json` | les paramètres des trois instances |
| `replicator/spawn.py` | le copieur — duplique le gabarit sans l'interpréter |
| `../kernel/` | les organes d'exécution : file, adaptateur, portier, reviewer |

Rick n'écrit aucune spec métier, ne construit rien, ne revoit rien. Il détient le gabarit et
la loi. Tout le reste appartient aux Cores.

## 2. Les trois Cores

| Core | Docteur | Couche | Réside dans | Maître de |
|---|---|---|---|---|
| Kernel Core | 13e | `L0` | `10_Tech_OS/11_Kernel_Core_13th/` | `10_Tech_OS` |
| Life Core | 11e | `L1` | `10_Tech_OS/12_Life_Core_11th/` | `20_Life_OS` |
| Buzz Core | 12e | `L2` | `10_Tech_OS/13_Buzz_Core_12th/` | `30_Business_OS` |

Les trois sont **engendrés par le même `spawn.py` depuis le même gabarit**. Aucun n'est écrit
à la main. Si tu veux changer la façon dont un Core fonctionne, tu modifies le gabarit et tu
ré-engendres les trois — jamais l'inverse.

C'est le sens du mot *universel* dans « constructeur universel » : une seule machine, capable
de bâtir n'importe laquelle des trois depuis leur description.

## 3. Pourquoi les trois Cores résident dans le Tech OS

Le Tech OS de Rick **contient le mécanisme de reproduction des trois OS**. Les trois Cores y
résident donc ensemble, engendrés du même gabarit — un Core est *maître de* sa couche, il n'y
*habite* pas. Sinon il n'y aurait pas un réplicateur mais trois, et le constructeur cesserait
d'être universel.

Rick et les trois Docteurs cohabitent dans `10_Tech_OS/`, à deux étages distincts :

- **Rick gouverne le mécanisme** — le gabarit, la loi, les organes.
- **Les Docteurs opèrent une couche chacun** — ils consomment le mécanisme, ils ne le possèdent pas.

Sans cette séparation, le maître du noyau serait aussi le maître de la loi qui le contraint.
Rick est le seul à ne pas pouvoir réclamer de travail dans la file.

## 4. Les quatre rôles, les mêmes partout

Chaque Core porte quatre rôles, un par organe de Von Neumann. La grille est identique pour
les trois — c'est ce qui rend un harness interchangeable entre couches.

| Rôle | Organe | Verbe dans le noyau |
|---|---|---|
| Spec | ruban φ | écrit le ruban, subit le test du portier |
| Build | constructeur A | `claim` → bâtit → `attest` → `review` |
| Spawn | copieur B | duplique φ, soumet la descendance |
| Review | contrôleur C | exige les preuves, score, **détache** |

Détail des titulaires par Core : `ROLES.md`.

## 5. Les lois

**Loi de réplication.** Un Core ne s'écrit pas, il s'engendre. Tout Core écrit à la main est
une dette : il divergera du gabarit, et la divergence se paiera à la première évolution.

**Loi de prédiction.** Rien n'atteint `review` ni `done` sans prédiction enregistrée avant
l'exécution. Tenue par un trigger SQL.

**Loi de détachement.** `done` n'est atteignable que depuis `review`, et le reviewer exige une
preuve par critère. Un critère sans attestation vaut faux.

**Loi du bail.** Tout travail réclamé porte une échéance. Un agent qui meurt rend son travail.

**Loi du ruban.** Si un constructeur doit poser une question à l'opérateur, le ruban est
incomplet — il retourne à `_INBOX` avec le motif.

Les quatre dernières sont tenues par la machine, pas par la discipline. La première est tenue
par Rick.

## 6. Ce que Rick refuse

- Qu'un Core acquière un organe que les autres n'ont pas.
- Qu'une couche invente son propre format de ruban.
- Qu'un fichier apparaisse dans un Core sans venir du gabarit ou d'un ruban admis.
- Qu'un `done` soit prononcé sans preuve.

Chacun de ces quatre refus correspond à une manière précise dont V2 a dérivé.

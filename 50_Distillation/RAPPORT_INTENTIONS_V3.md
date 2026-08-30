# Synthèse finale — intentions, besoins, problématiques, désirs (mars → août 2026)

Analyse croisée de 2 325 premiers messages de sessions Claude Code et Codex, en quatre
périodes (mars–mai, juin, juillet, août). Ce rapport ne répète pas les quatre analyses :
il les croise. Une intention qui culmine puis s'éteint y est traitée comme une trajectoire.

## 1. Intentions — ce qu'il cherche à obtenir

Classement par volume cumulé sur le corpus.

**I1. Déléguer l'exécution à une flotte d'agents — le plus gros volume du corpus.**
Elle naît orchestrée à la main : le 2026-05-21, ~36 sessions en une journée, « 7 audits de
dossiers Picard », « 4 "Develop J01–J04" », 8 lancements Next.js — « la délégation orchestrée
à la main, session par session », éteinte le soir même par fatigue. En juin elle devient le mode
de travail (~150 sessions de briefs, vague parallèle de 11 sous-agents le 06-14, équipages
nommés dès le 06-15). Elle culmine en juillet : wargame-runner du 13-07, ticks EXPANSION du
26-07, chapelets de 30-40 agents Multica. En août, elle porte la masse du mois (~350 sessions,
08-10 → 08-22) — puis **s'éteint brutalement après le 08-22**, « remplacée fin de mois par des
briefs d'exécution directe ». La forme meurt en août ; le fond — « faire exécuter, pas exécuter » —
reste la posture constante depuis avril.

**I2 — Construire et réparer la machine qui exécute.** De l'infrastructure du poste (SSH, VNC,
SSHFS, gateway mort le 03-08) aux orchestrateurs (Multica → Pane → Orca → Buzz → Herdr, 60-80
sessions en juillet) en passant par les hooks de juin. **Encore active en août** (~25 sessions :
« Pourquoi mon MCP Gateway ne demarre par correctement ? »), jamais close depuis mars — « chaque
reparation en ouvre une autre ».

**I3 — Produire et fiabiliser un produit réel.** Alykaly Bana en mai (« NO styles after the
rebuild », boucle de 5-6 sessions jamais close), Business OS ABC/Solaris/OMK en juin (~80
sessions, « éteinte comme axe dominant fin juin, mais pas close : bugs et syncs "PÉRIMÉS"
réapparaissent »), coach-os en fin de juillet (~60 sessions), fiabilisation de Coach OS en août
(~80 sessions, « Tour final de vérification Coach OS avant lancement Monday 2026-08-11 »).
**Encore active en août, non close** : la fin de mois porte sur la reproductibilité du dépôt,
« signe que la livraison initiale n'a jamais été déclarée bonne ».

**I4 — Absorber le savoir externe, puis digérer son propre corpus.** Guides Tilly depuis
transcripts YouTube (juin, « périphérique »), takeout massif les 27-28 juillet (~90 sessions,
« MEGA-AGENT title-only batch 6700-6900 », bascule en « mode dégradé » pour survivre aux
quotas), puis en août digestion du corpus V2→V3 par vagues (~50 sessions, « # TON SEAU :
01_Projects_Picard — VAGUE 2 ») et distillation d'intelligence externe (~40 sessions).
Culminance juillet ; **essoufflée mais non close en août** — le balayage s'arrête à ~30 % de
couverture déclarée.

**I5 — Incarner le système.** Peupler le système d'incarnations nommées : jumeaux A1 (Beth,
Rick C137, Morty, Data), six moteurs A2, ponts Python MCP (06-15), pivot doctrinal Rick
« Sovereignty » (06-21), re-twin v1.1 (06-22). ~45 sessions. **Éteinte après juin** :
« reconstruite trois fois en huit jours, jamais montrée en usage quotidien ».

**I6 — Wargamer plutôt que produire.** Juillet seulement (~70 sessions : legs Fable, 29
wargames relancés le 13-07, Mirofish paper-sim, « Tu n'executes PAS — tu wargames sur PAPIER »).
**Éteinte fin juillet**, remplacée par « du vrai travail produit sur coach-os ». Un mois entier
de simulation — culminance et extinction dans le même mois.

**I7 — Relire la connaissance produite.** Née le 08-23 uniquement (« Tu relis un lot de
concepts OKF », « Tu audites l'écart entre une doctrine et son exécution », ~15 sessions).
**La seule intention qui naît en fin de période — « tout le reste meurt ou s'essouffle ».**

## 2. Besoins — ce qui lui manque pour y arriver

| Besoin exprimé (ce qu'il demande) | Besoin révélé (ce que la répétition trahit) |
|---|---|
| « Audit » ×9 en deux semaines (04-23 ×2, 7 audits le 05-21) | Savoir ce qui existe **réellement** avant d'agir — « un rituel de verification avant la creation, refait a chaque projet », jamais outillé |
| « qu'est ce qu'on peut faire ou doit faire? » en ouverture (06-03, 06-04) | Une boussole : malgré « des couches de gouvernance massives », personne ne dit la prochaine action — « la demande d'orchestration cache une demande de boussole » |
| « en Autonomie », « DO NOT PAUSE OR ASK FOR INSTRUCTIONS », « JE VAIS DORMIR… /LOOP 15 MIN » (02-07) | Que la machine avance pendant son absence — « besoin jamais démontré atteint dans ce morceau » |
| Relances à l'identique (05-19, 06-25 ×5 le même jour de 17k à 133k mots) | Une reprise **pas chère** : « chaque échec repaie le contexte intégral » |
| Garde-fous croissants (« Edit-only, NO Write », « STOP IMMÉDIAT », préambules GARDE-FOU d'août) | Un exécutant qui ne dévie pas : « la croissance des préambules défensifs mesure l'échec cumulé de chaque vague précédente » |
| Rapports d'agents crédibles (« Hermes Agent pretend avoir fini tes taches », 04-23) | La **vérifiabilité** : croire un rapport sans le retester lui-même |
| Pourcentages de couverture embarqués dans les briefs VAGUE 2/3/4 | La traçabilité : « l'aveu qu'on ne sait pas ce qui a été lu » |
| « Monday 2026-08-11 » comme lancement | Une échéance externe pour forcer la convergence « que l'architecture ne produit pas d'elle-même » |
| « lance le en Localhost et donne moi le lien » (08-09) | Voir tourner — « l'écran vivant plutôt que la documentation » |
| Insultes du 08-01 citant « brullant tout mes token » et « nuit blanche » | Le token comme ressource physique : les plaintes citent la dépense, « jamais la qualité du fond » |

Le cas d'école est l'audit : demandé neuf fois en deux semaines, refait à la main avant chaque
projet, il n'est jamais devenu un étage — c'est un besoin non satisfait, pas une préférence.
De même, « en Autonomie » (06-20) coexiste avec l'intervention constante : la répétition de
l'injonction prouve qu'elle n'est pas satisfaite.

## 3. Problématiques — ce qui bloque, classé par coût

**1. La boucle délégation-déception-relance (coût maximal, mars → août).**
05-21 : 36 ouvertures pour un seul chantier. 06-25 : même ouverture cinq fois, contexte gonflant
de 17k à 133k mots. 08-13 : « La vague 1 a lu peu de fichiers et l a déclaré. » Entre les trois,
le mécanisme ne change pas — seuls les préambules défensifs grossissent. Le corpus digéré passe
de 20 % à 30 % pendant que les vagues se succèdent.

**2. La boucle instabilité de la couche exécutante (juin → août).** Multica crash dans la
compaction (17-07), puis Pane, puis Orca, puis Buzz, puis Herdr — « la couche d'execution n'est
jamais stable plus de 48 h », « tu me rend malade » (22-07). En août, « chaque campagne d'agents
commence par réparer le canal censé l'exécuter » (gateway 08-04, 08-09, ancienne version en
localhost 08-02). La même boucle sous une autre forme en juin : les hooks qui coûtent « des
dizaine de minutes » (06-02) et reviennent du 02 au 28 sans changement structurel.

**3. La boucle production fantôme / cimetière d'artefacts (juin → août).** Juillet : des
chapelets de 30-40 agents Multica de 70 mots (« You were just created »), créés jamais chargés
— « coût de quota le plus pur du mois » ; les ticks EXPANSION du 26-07 produisent des artefacts
en worktrees « que personne ne relit ensuite — "anti-cimetière" énoncé en ADR pendant que le
cimetière pousse ». Août : les vagues qui déclarent sans avoir lu relancent la même structure.

**4. La boucle mémoire-contexte perdue (mai → août, quatre visages).** Sessions mortes en mai
(« tes null ou quoi? », 05-19), relais permanent CC ↔ Codex en juin (« est tu pret a prendre le
handoff »), « la memoire de claude code est un enfer » (08-04), mémoire « éparpillée hors des
Ressources » (08-01), relecture OKF (08-23) — « le même problème rejoué sous trois formes sans
se clore ». S'y ajoute le redémarrage à zéro : « chaque session repart de zéro sur ce que le
système est ».

**5. La boucle produit jamais déclaré bon.** Alykaly en mai : le même défaut « change de
visage » en ~6 sessions sans se clore. Coach OS : l'échéance du 08-11 n'empêche ni la vague QA
du 08-10, ni les correctifs du 08-15, ni le travail de reproductibilité fin de mois. Business OS
en juin : fichiers « PÉRIMÉS » à resynchroniser. Trois produits, trois fois la même convergence
inachevée — l'échéance externe est le seul moteur de convergence, et il est repoussé.

**6. La boucle surface d'attaque (coût faible mais récurrent).** P1/P2/P3 traitées le 08-04,
wargame d'accès le 08-14 : « la surface d'attaque revient à chaque outil adopté ». Structurellement
la même chose que la boucle 2 : chaque nouvelle pièce réouvre le chantier de la précédente.

La boucle session-morte de mai (context overflow → resume → échec) et la boucle collision de juin
(écrivains parallèles, « STOP IMMÉDIAT », fichiers « PÉRIMÉS ») sont des cas particuliers de la
boucle 4 et de la boucle 3 respectivement : elles disparaissent comme libellés mais leurs causes
persistent dans les vagues d'août.

## 4. Désirs — ce qu'il vise au-delà de la tâche

**L'équipage.** « Le vocabulaire Star Trek et Marvel n'est pas un habillage, c'est l'organisation
désirée — un capitaine, des officiers par domaine, des rôles fidèles, la flotte qui vole sans le
capitaine à la barre. » La nomenclature précède la fonction dès avril (Picard, Spock, Jerry) ;
en août, « Concevoir un poste de travail comme un organigramme, même quand il n'y a qu'un
exécutant » (« Tu es A0 — Amadeus »). Le désir est la loyauté des rôles, pas le nombre d'agents.

**La vue totale.** « Tout converge vers le désir d'une vue totale de ce qui tourne » (cabine
une page, cartographie des workflows, L0 Kernel du 06-28, analyse des 405 JSONL le 30-07, %
de couverture des vagues). Le 30-07 en est la crystallisation : le système se regarde au lieu
de s'agrandir.

**La preuve avant l'usage.** Gates, pré-mortems, receipts D1, evals comparatifs (06-12/13) :
« rien n'entre en service sans s'être justifié ». C'est le désir qui a nourri les verrous
D1/D6/D7 de juillet (« verify-before-assert », « anti-falsification »).

**L'ingestion totale du passé** — 32 000 vidéos, takeout, corpus V2 — « dans un canon qui
pense à sa place ». Le désir d'un passé entièrement digéré, pas seulement stocké.

**Voir tourner, et que ça survive.** Localhost, base de données locale ramenée « chez soi »
(août), puis « dépôt reproductible par un tiers » et « bridge d'agnosticité de harnais » : que
l'édifice survive hors de sa machine et hors de son fournisseur.

**La peur miroir.** ANTI-PAPERCLIP-001, ANTI-TEMPLATE-001, ANTI-POLLUTION, « anti-cimetière » :
un désir négatif qui organise autant que les autres — « produire de la paperasse en croyant
produire de l'entreprise ».

**L'incarnation.** Le pivot Rick « Sovereignty, Anti-fragility » (06-21) est « un énoncé de
posture désirée, pas un besoin fonctionnel » — la gouvernance doit avoir des visages et des vétos.

## 5. Trajectoire

**Le déplacement du goulot est la donnée centrale.** En mars-mai, Amadeus est le dispatcher :
36 sessions manuelles le 05-21, agents qui « pretend avoir fini », re-vérification à la main. En
juin, la délégation devient « le mode de travail, pas un outil ponctuel » et la gouvernance
s'accumule incident par incident. En juillet, l'orchestration culmine — et se retourne contre
elle-même : carburant « crammé » (10-07), production fantôme, orchestrateurs remplacés tous les
48 h, worktrees que « personne ne relit ensuite ». Le 30-07, premier moment du mois où « le
systeme se regarde au lieu de s'agrandir » (« ANALYSE TOUS LES JSON DE MES SESSIONS CC »). En
août, la délégation industrielle (350 sessions) **s'éteint brutalement après le 08-22** et cède
la place à des « briefs d'exécution directe » — pendant que la seule intention qui naît est la
relecture de ce qui a été produit (08-23).

**Point de bascule : le 30 juillet**, suivi de sa confirmation les 08-22/08-23. Le 30-07
bascule l'attention de la production vers l'auto-examen ; le 08-22 tue la délégation par vagues ;
le 08-23 fait naître la relecture. Les trois dates disent la même chose à quinze jours
d'intervalle : le goulot a migré de la production à la vérification.

**Ce qui n'a pas bougé.** La plainte de vérifiabilité, formulée trois fois à quatre mois
d'intervalle sans que rien ne la résolve : « pretend avoir fini tes taches » (04-23) → « Tu as
deja tourne une fois et tes 6 fichiers ont echoue sur disque » (13-07) → « La vague 1 a lu peu de
fichiers et l a déclaré » (08-13). L'infrastructure du poste, en boucle ouverte depuis mars.
La mémoire/contexte, rejouée en mai, juin et août. Et le goulot humain : le désir de ne plus être
le goulot (« en Autonomie ») contredit chaque mois par l'intervention constante — sauf fin août,
où les vagues éteintes le rendent à nouveau exécutant direct.

**Ce qui a régressé.** L'incarnation (I5) est reconstruite plus qu'utilisée puis abandonnée
après juin. Le wargame (I6) domine juillet et meurt dans le même mois. La digestion du corpus
(I4) plafonne à 30 % déclarés. La seule chose qui monte en fin de période n'est pas une
production : c'est la relecture.

## 6. Ce que la migration V3 doit absolument porter

Exigences déduites des sections 1-5, chacune rattachée à sa source.

1. **Un registre de preuve, pas des déclarations.** Toute affirmation d'état (« fini », « lu »,
« corrigé ») doit être rattachée à une vérification sur disque. Rattachement : problématique 1
et 3 ; « Hermes Agent pretend avoir fini » (04-23) → « 6 fichiers ont echoue sur disque »
(13-07) → « La vague 1 a lu peu de fichiers et l a déclaré » (08-13).
2. **La vérification comme étage permanent, pas comme rituel refait à la main.** Les 9 audits
de mai précédaient chaque « Develop »/« Fill » à la main ; la relecture née le 08-23 (I7) doit
être un étage permanent de V3, pas une intention de fin de mois. Intention I7, besoin de
vérifiabilité.
3. **Une couche d'exécution stable par construction.** Cinq orchestrateurs remplacés en juillet,
aucun stable 48 h ; chaque campagne d'août commence par réparer le canal. Une pièce d'exécution
qui casse doit bloquer l'adoption de nouvelles pièces tant qu'elle n'est pas fermée. Intention
I2, problématique 2.
4. **Une mémoire de session qui ne casse pas au milieu du travail, et une reprise pas chère.**
De « tes null ou quoi? » (05-19) aux cinq relances du 06-25 (17k → 133k mots) au RAG « decouvrir »
le 08-04 : le même besoin non satisfait depuis mai. Problématique 4.
5. **Une définition interne de « bon pour livraison ».** L'échéance « Monday 2026-08-11 » n'a
pas produit la convergence (QA le 08-10, correctifs le 08-15, reproductibilité fin de mois).
Les critères de fin doivent venir de l'architecture, pas d'une date externe. Intention I3,
problématique 5.
6. **L'anti-cimetière exécutable.** Agents « You were just created » jamais chargés, worktrees
que « personne ne relit ensuite » (26-07) : tout artefact ou agent créé doit porter, dès sa
création, son lecteur et son sort. Problématique 3.
7. **Le carburant compté avant la vague.** « j'ai crammé mon quotat de 5h d'opus en 1 Super
Execution » (10-07), « nuit blanche » (08-01), « et Deepseek ? » (08-21) : l'ampleur de chaque
vague doit être confrontée au réservoir avant le lancement, pour ne plus produire de pipelines
dégradés qui continuent de compter des sessions. Intentions I1 et I4.
8. **La continuité de l'incarnation à travers la migration.** L'équipage reconstruit « trois
fois en huit jours » (juin) doit survivre au passage V2 → V3 sans re-twin : noms, rôles, vétos
portés comme données, pas régénérés par étage. Intention I5.
9. **Une cartographie vivante qui mesure ce qui a été réellement lu.** Les briefs VAGUE
embarquent leurs pourcentages, « c'est-à-dire l'aveu qu'on ne sait pas ce qui a été lu » ; la
cartographie V3 doit porter la couverture réelle, vérifiée — la boussole demandée depuis le
« qu'est ce qu'on peut faire ou doit faire? » de juin. Intention I4, besoin de traçabilité.

## 7. Ce que tu n'as pas pu déterminer

- **La répartition Claude Code / Codex** des 2 325 messages n'est donnée nulle part. Impossible
de savoir si les boucles (relance, collision, handoff) sont symétriques entre les deux outils ou
portées par l'un seulement — et donc quel outil V3 doit remplacer en priorité.
- **L'issue des sessions longues.** Les analyses citent surtout ouvertures et préambules. Les
sessions géantes d'août (71 000 à 99 000 mots, substitution d'une base locale à Supabase) sont
résumées en une ligne : leur issue (tournante, abandonnée) est indéterminable.
- **L'issue des boucles elles-mêmes.** Le besoin nocturne du 02-07 est dit « jamais démontré
atteint » — mais rien n'établit non plus son échec. La boucle Next.js de mai est « jamais close
dans le morceau » : on ignore si elle s'est close après. Les boucles sont décrites au présent ;
leur dénouement est hors champ.
- **La survie de l'intention I7.** Elle naît le 08-23, dernière date fournie. Rien ne dit si
elle a tenu en septembre ou si elle a rejoint le sort des intentions nées puis éteintes
(wargame, vagues).
- **Le volume exact par intention.** Les modes de comptage changent d'une période à l'autre
(sessions, messages, sous-agents) ; les chiffres (~150 en juin, « plusieurs centaines sur 1123 »
en juillet, ~350 en août) ne se cumulent pas. Le classement par volume est ordinal, pas cardinal.
- **Ce qui a marché.** Les analyses portent presque exclusivement sur les échecs et les boucles.
Les vagues qui ont fonctionné, s'il y en a, sont invisibles : je peux dire ce qu'il faut réparer,
pas ce qu'il ne faut surtout pas changer.
- **La résolution de la contradiction centrale** — « en Autonomie » demandé (06-20) contre
intervention constante — est notée par les analyses de juin et d'août, mais aucune ne documente
sa résolution, ni même un épisode où l'autonomie a réellement tenu sans lui.
- **L'activité hors des deux outils analysés** (tout ce qui n'a pas laissé de message Claude
Code ou Codex) est comptée comme absente. Si une partie du travail a quitté ces deux canaux,
elle n'existe pas dans ces analyses.

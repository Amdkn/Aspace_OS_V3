# C2 — AI-NATIVE CEO — analyse de 9 transcripts

**Cluster** : `transcripts2/ai-native-ceo/`
**Périmètre** : 9 vidéos sur l'organisation d'une entreprise « AI-native », l'engineering
quand les agents écrivent le code, et le modèle d'agence/conseil en IA.
**Lecture transverse** : 5 vidéos sur 9 poussent la même thèse — *l'entreprise devient
un système auto-améliorant qui dort*. Les 4 autres sont du matériau de domaine sur le
métier de consultant IA (positionnement, pricing, ROI observé). Presque rien sur le
*métier de coach* lui-même : ce cluster change la *machine qui fait Coach OS*, pas
*ce qu'un coach fait*.

---

## 1. Par vidéo

### EN7frwQIbKc — *How To Build A Company With AI From The Ground Up* — Diana (YC)

**Ce que la vidéo défend.** L'IA ne doit pas être un outil greffé sur une entreprise
héritée, elle doit être *l'OS* sur lequel l'entreprise tourne. Conséquence : chaque
processus important devient une *closed loop* (capte → informe → s'améliore), l'organisation
entière doit être *requêable* (artefact par artefact), et la hiérarchie moyenne
disparaît — elle est remplacée par trois archétypes : IC bâtisseur-opérateur, DRRI
(*Directly Responsible Individual*), et fondateur-AI.

**Primitives (7)**

1. **Boucle fermée d'exploitation** — chaque processus important de l'entreprise est
   encadré par un système intelligent qui capte l'information, agit, et se corrige.
   Citation : *"every important process in your company should be captured by an intelligent close loop"*.
2. **Organisation requêable** — toute action laisse un artefact lisible par l'IA ; pas
   de DM, pas de note mentale, pas de réunion qui ne finit pas enregistrée.
   Citation : *"you will need to make your entire company queryable"*.
3. **Fabrique à logiciels** — les humains écrivent spec + tests, les agents écrivent le
   code et itèrent jusqu'à ce que les tests passent ; le code manuscrit disparaît.
   Citation : *"humans write a spec and a set of tests... then AI agents generate the implementation"*.
4. **DRRI** — une seule personne responsable, un résultat nommé, pas de comité où se
   cacher.
   Citation : *"One person, one outcome, no hiding"*.
5. **Brûler des tokens, pas des effectifs** — la mesure d'effort devient la consommation
   d'API ; le trade-off est explicitement *un API bill élevé remplace du headcount*.
   Citation : *"Maximizing token usage, not headcount, will be the critical shift"*.
6. **IC bâtisseur-opérateur** — tout le monde construit (y compris sales, ops, support),
   pas seulement les ingénieurs ; on arrive en réunion avec un prototype qui marche.
   Citation : *"Everyone builds and ops support sales"*.
7. **Compétence-artefact** — toute action produit un artefact ; l'intelligence au centre
   apprend de ces artefacts.
   Citation : *"Every important action should produce an artifact"*.

**Ce qui ne s'applique PAS** — la « software factory » (humain = specs/tests, agent = code)
est taillée pour une boîte dont l'output est du logiciel. Coach OS est une enveloppe
cliente : l'output est une transformation de personne, pas un binaire. La primitive se
décline en *« spec de transformation + check observable »*, mais l'analogie directe est
trop étroite.

---

### eBUyTS7SzV4 — *Closing Keynote: Garry Tan, Y Combinator* — AI Engineer Summit

**Ce que la vidéo défend.** Le produit, c'est l'organisation. Et l'organisation, ce sont
des *skill files* : des fichiers markdown qui décrivent une capacité, un job, un mode
d'emploi exécutable par agent. Derrière, il faut une *bibliothèque + un bibliothécaire*
(qui choisit les 3 bons livres à ouvrir sur le bureau de l'agent), avec *hygiène*
(provenance, contradiction, élagage). Discipline cardinale : *ne jamais faire un
one-off* — chaque tâche terminée devient une skill réutilisable.

**Primitives (7)**

1. **Skill = employé** — un fichier markdown décrit un poste : une capacité, un job,
   exécutable par un agent. Citation : *"A skill file is an employee. It has one capability, one job"*.
2. **Bibliothèque + bibliothécaire** — la mémoire brute ne suffit pas ; il faut un curator
   (humain + agent) qui choisit quoi charger dans le contexte.
   Citation : *"This is what a company brain is. It's the library plus the librarian"*.
3. **Skillifier tout one-off** — chaque tâche réussie devient une skill ; si on doit
   demander deux fois, on a échoué.
   Citation : *"never do one-off work"*.
4. **Ingénierie de contexte** — qui décide quels 3 livres sont ouverts sur le bureau de
   l'agent ; ce choix détermine si l'agent est génie ou poisson rouge.
   Citation : *"who decides which three books are open on that desk"*.
5. **Mémoire + hygiène** — la primitive n'est pas la mémoire, c'est *la mémoire plus
   l'hygiène* (provenance, contradiction, élagage).
   Citation : *"the primitive is not memory. It's memory plus hygiene"*.
6. **Traiter l'agent comme une workforce** — pas comme de l'autocomplete ; la mesure est
   *le câblage du travail*, pas le modèle.
   Citation : *"They're treating it as a workforce"*.
7. **Persona non-tech construit des apps** — une opératrice Excel devient manager
   d'agents ; toute la boîte — finance, events, médias — écrit des skill files.
   Citation : *"She's not a programmer. She's a manager of agents now"*.

**Ce qui ne s'applique PAS** — les anecdotes sur « 95 % du code base AI-generated » et
« $231k de consulting » sont des marqueurs du modèle pure-software / pure-agency. Pour
Coach OS, ce qui reste est la *discipline* (skillifier tout, contexte choisi) ; les
chiffres datent de la hype winter 25, ils ne parlent pas à une niche service comme le
coaching.

---

### X_JsIHUfUjc — *How to Build a Self-Improving Company with AI* — Harj Taggar (YC)

**Ce que la vidéo défend.** Les organisations actuelles sont les « légions romaines » :
des humains qui font remonter l'information à travers une hiérarchie conçue pour des
cerveaux à 7 chiffres de téléphone. L'IA casse ça. Chaque fonction de l'entreprise
devient une *boucle auto-améliorante* (sensor → policy → tool → quality gate →
learning) qui tourne la nuit. Pour que ça marche, *tout* doit être enregistré, puis
*diorisé* (synthétisé) avant d'être stocké. Le software jetable ; le contexte précieux.

**Primitives (7)**

1. **Boucle auto-améliorante** — pour chaque fonction : un sensor, une policy, des
   tools déterministes, une quality gate, et un mécanisme d'apprentissage qui boucle.
   Citation : *"reimagine what a company is as a set of recursive self-improving AI loops"*.
2. **Enregistrer tout** — ce qui n'est pas enregistré n'existe pas pour l'IA.
   Citation : *"if it did not get recorded, it did not happen to your intelligence"*.
3. **Dioriser avant stocker** — on n'injecte pas 100 000 h d'audio dans le contexte ; on
   synthétise en breadcrumbs.
   Citation : *"you have to diorize it... aggregate it down"*.
4. **Logiciel jetable** — régénérer les dashboards et apps internes à chaque changement
   de modèle ; garder les skills et le contexte.
   Citation : *"treat the software as ephemeral. You can regenerate it"*.
5. **Brûler des tokens** — la contrainte va basculer de headcount à token usage ;
   choisir ses employés sur qui *token-max*.
   Citation : *"token usage, not on headcount really, really soon"*.
6. **Humain au bord** — l'IA au centre de la circulation d'info ; l'humain aux endroits
   à enjeu (éthique, novel situations, sales).
   Citation : *"the humans live around the edge"*.
7. **Légibilité avant automatisation** — on n'automatise pas ce qu'on n'a pas d'abord
   rendu lisible.
   Citation : *"you've got to record everything"*.

**Ce qui ne s'applique PAS** — la boucle sensor/policy/tool/quality/learning est
optimisée pour des processus à fort volume et données continues (office hours de 2 000h,
product analytics, support tickets). Un coach qui traite 5 clients par mois n'a pas la
masse pour faire tourner la boucle toutes les nuits. La primitive se transpose en *«
enregistrement systématique d'une session + relecture nocturne »*, mais l'image
industrielle est trompeuse.

---

### R56RJFZBasQ — *How to Pick A Startup Idea* — John (YC)

**Ce que la vidéo défend.** Le poison le plus fréquent chez les fondateurs n'est pas
d'avoir une mauvaise idée, c'est de ne pas s'engager. Trois disciplines : *brûler
les bateaux* (foreclose les options restantes), *aller profond* jusqu'à devenir l'un
des meilleurs experts mondiaux (test : « pourriez-vous diriger le business de votre
client ce matin ? »), et viser *la version la plus ambitieuse* — qui verticalise
l'outcome (être l'assureur, pas le vendeur de SaaS pour assureurs).

**Primitives (7)**

1. **Brûler les bateaux** — foreclose explicitement les options restantes, y compris en
   changeant le nom de boîte et les emails.
   Citation : *"you should burn the other boats"*.
2. **Test du directeur délégué** — pour chaque idée, la question est : « pourriez-vous
   diriger le business de votre client demain matin ? ».
   Citation : *"if I dropped you into a cleaning business tomorrow, would you know how to run it"*.
3. **Classe-tour** — êtes-vous parmi les mieux informés au monde sur le sujet que vous
   résolvez ?
   Citation : *"could you teach a class on the problem you're solving"*.
4. **Verticaliser l'outcome** — ne pas vendre du SaaS pour X, vendre X ; le coût du
   software tend vers zéro, ce qui devient précieux c'est l'outcome, la licence, la
   confiance, le permis.
   Citation : *"don't build software for insurance companies. Just be the insurer"*.
5. **Version la plus ambitieuse** — le coût d'une idée ambitieuse et d'une idée modeste
   est le même ; viser la version qui réécrit un secteur.
   Citation : *"the cost of pursuing a wildly ambitious startup idea and the cost of pursuing a modest one are roughly the same"*.
6. **Aller profond, pas large** — brûler un seul sujet jusqu'à saturation ; mieux
   vaut 10 ft concentrés que 100 ft dispersés.
   Citation : *"you're not guaranteed to end up in the right place, but you generate much more information per unit of time"*.
7. **L'idée meilleure est dessous** — la première idée ne sert qu'à en trouver la
   meilleure ; aller profond *produit* l'idée.
   Citation : *"going deep finds the better idea underneath"*.

**Ce qui ne s'applique PAS** — la grappe s'adresse à des fondateurs qui *choisissent*.
Coach OS existe déjà et a déjà choisi sa niche (coachs + futur multi-niche service).
« Brûler les bateaux » est sans objet une fois la niche arrêtée. Ce qui reste utile :
*le test du directeur délégué* — à poser au moment où on dessine une app.

---

### MGzymaYBiss — *Dispatch from the Future: building an AI-native Company* — Dan Shipper (Every)

**Ce que la vidéo défend.** À 100 % d'adoption IA dans l'équipe d'ingénierie, on
multiplie l'output par 10 — il n'y a pas de continuum. La clé opérationnelle est
*l'ingénierie qui compound* : une boucle en 4 pas (plan, delegate, assess, *codify*),
où la dernière étape — codifier ce qu'on a appris dans des prompts/skills partagés —
est le multiplicateur. Effets de second ordre : nouvelles recrues productives dès le
jour 1, *culture démo* (prototype qui tourne > slide deck), commit entre produits,
*manager qui commit du code*.

**Primitives (7)**

1. **Ingénierie qui compound** — chaque feature doit rendre la suivante plus facile à
   construire, pas plus difficile.
   Citation : *"each feature makes the next feature easier to build"*.
2. **Boucle plan/delegate/assess/codify** — quatre étapes ; la quatrième (codifier les
   apprentissages en prompts/skills réutilisables) est le multiplicateur.
   Citation : *"the loop has four steps... plan... delegate... assess... codify"*.
3. **Seuil d'adoption 100 %** — la différence entre une équipe à 90 % IA et une équipe
   à 100 % IA est un facteur 10 opérationnel, pas un gradient.
   Citation : *"10x difference between 90% and 100% adoption"*.
4. **Culture démo** — on arrive en réunion avec un prototype qui tourne, pas une slide.
   Citation : *"vibe code something in a couple hours that shows the thing"*.
5. **Onboarding jour 1** — l'environnement de travail, le style de PR, les commandes
   partagées sont dans le `cloud.md` ; la recrue est productive avant même d'arriver.
   Citation : *"new hires are productive on their first day"*.
6. **Manager commit du code** — l'attention fragmentée redevient suffisante grâce aux
   agents en arrière-plan.
   Citation : *"managers can commit code"*.
7. **Cross-commit entre produits** — un dev d'un produit peut fixer un bug dans un
   autre produit sans coordination sociale grâce à l'agent.
   Citation : *"developers inside of every commit to other products"*.

**Ce qui ne s'applique PAS** — la primauté du *4 panes d'agents en parallèle* et du
*manager qui commit* est un mode dev solo plein temps. Pour des utilisateurs Coach
OS — souvent coach solo, pas dev —, ces primitives se traduisent en *« espace de
travail où chaque profil propose un livrable concret au client »*, pas en *« 4 PR en
parallèle »*. La boucle plan/delegate/assess/codify, elle, traverse tout.

---

### Op0UcKwOO_U — *AI-Native Explained In 5 Minutes* — Brad

**Ce que la vidéo défend.** La distinction entre *AI-assisted* (process conçu pour
l'humain, IA greffée) et *AI-native* (process conçu autour de l'IA, humain appelé
quand nécessaire) donne un écart de 1,2× à 10× sur le même modèle. L'illustration :
un atelier de requirements gathering SAS passe de 10 h à 1 h quand le client parle
*directement à l'agent*, qui produit un gap analysis que le consultant valide en
une session.

**Primitives (4)**

1. **Natif vs assisté** — la question pivot n'est pas « où mettre de l'IA » mais
   « comment redessiner le process pour que l'IA fasse le travail central ».
   Citation : *"you design the entire process around the capabilities of AI"*.
2. **Test du gain exponentiel** — un gain de 1,2× signe un process *assisté* ; un gain
   de 10× signe un process *natif*.
   Citation : *"one approach gives us 1.2 times efficiency and the other gives us 10x"*.
3. **Question pivot de design** — ne pas demander *« où ajouter l'IA ? »* mais
   *« comment redessiner pour que l'IA fasse le travail, humain review ? »*.
   Citation : *"stop asking where can we add AI into this process"*.
4. **Onboarding AI-natif client-side** — le client interagit directement avec l'agent ;
   le consultant traite le gap analysis en une seule session.
   Citation : *"the customer works directly with the AI agent"*.

**Ce qui ne s'applique PAS** — l'exemple SAS est trop vertical ; le parallèle strict
(« un atelier de 10 sessions devient 1 ») ne se transpose pas au coaching, où la
relation humaine *fait partie de l'output*. Ce qui reste : le *test du gain
exponentiel* comme heuristique pour évaluer toute nouvelle section Coach OS.

---

### ehQFj6VmuI8 — *AI Consulting in Practice* — NLW

**Ce que la vidéo défend.** Résultat d'une étude de ~2 500 cas d'usage auto-rapportés
par les auditeurs du AI Daily Brief : 82 % voient du ROI (44 % modeste, 38 %
élevé/transformatif) ; le gain typique se concentre entre 1 et 10 h/semaine (~5h au
mode) ; *risk reduction* est sous-représenté (3,4 % des cas) mais le plus
transformatif (25 %). Plus une organisation soumet de cas, meilleur est son ROI
moyen — la systématicité bat le spot experiment.

**Primitives (5)**

1. **Huit catégories de ROI** — time savings, increased output, quality, new capabilities,
   better decisions, cost savings, increased revenue, risk reduction.
   Citation : *"eight broad categories of impact... time savings, increased output"*.
2. **Risque = transformatif** — sous-représenté dans la masse, sur-représenté dans
   l'impact ; les use cases conformité/volume sont les plus à fort gain.
   Citation : *"Risk reduction is by far the most transformational"*.
3. **5 h/sem = 7 à 10 semaines/an** — l'unité de mesure perçue du gain dans le modèle
   mental du client.
   Citation : *"winning back 7 to 10 work weeks a year"*.
4. **Plus de cas = meilleur ROI** — la voie systématique (multiples cas, multi-départements)
   surperforme le spot experiment isolé.
   Citation : *"the more use cases... the better they tended to see ROI"*.
5. **Adoption cross-fonctionnelle** — penser l'AI et les agents en termes transversaux,
   pas département par département.
   Citation : *"thinking about AI in systematic cross-organizational terms"*.

**Ce qui ne s'applique PAS** — chiffres KPMG / McKinsey / Accenture sur les $ que les
grands cabinets facturent à l'audit IA. C'est du matériau de domaine (les chiffres
que nos utilisateurs entendent, la benchmark qu'ils utilisent pour cadrer leur propre
attente de ROI), pas un design primitive. Pour Coach OS, l'apport est *un cadre
explicite de catégories de ROI* que l'app peut afficher au client pour qu'il mesure
où il en est.

---

### VzOYty0siaM — *How I made $231,000 in 30 days (as an AI Consultant)* — Nate Herk

**Ce que la vidéo défend.** Le métier de consultant IA a deux voies qui se renforcent
en flywheel : *B2C* (éduquer — YouTube, communauté, cours) et *B2B* (implémenter —
diagnostic + roadmap + build chez le client). L'éducation alimente la crédibilité ;
la B2B alimente la preuve ; les deux alimentent l'éducation. Cadre en 5 étapes :
problème d'abord (pas outil), un outil maîtrisé en profondeur, documenter publiquement,
offres simples, livrer au-dessus + systématiser.

**Primitives (6)**

1. **Problème d'abord, outil ensuite** — la première question est la douleur client,
   pas « où mettre de l'IA ».
   Citation : *"Don't lead with the tech. Lead with the problem that you're solving"*.
2. **Flywheel B2C ↔ B2B** — l'éducation alimente la crédibilité de la B2B ; la B2B
   alimente les case studies de l'éducation.
   Citation : *"they're not competing paths. They're actually a flywheel"*.
3. **Audit gratuit comme recherche primaire** — proposer l'audit gratuitement n'est
   pas du selling, c'est de la recherche de marché qui ouvre la porte.
   Citation : *"free AI automation audits. This isn't about selling. This is still about learning"*.
4. **Maîtrise d'un outil unique** — la profondeur construit l'autorité plus vite que
   la largeur.
   Citation : *"Depth builds authority. Authority builds opportunity"*.
5. **Offre simple, une phrase** — l'offre doit être claire, compréhensible, achetable
   en une phrase ; pas un menu.
   Citation : *"Your offer should be clear, easy to understand, and easy to buy"*.
6. **Preuve avant profit** — les premiers clients sont des répétitions pour la
   crédibilité, pas du revenu.
   Citation : *"Your first few builds aren't about profit. It's about reps"*.

**Ce qui ne s'applique PAS** — c'est du matériau de domaine pour la *persona
consultant/agency*. Coach OS ne joue pas ce rôle, il *équipe* les consultants qui le
jouent. La transposition : pour *nos* utilisateurs (coachs qui conseillent d'autres
coachs, ou coachs solo qui vendent des programmes), ces primitives deviennent des
sections de l'app `sales` et `onboarding`.

---

### Pagd9kNIg9o — *Why Solo AI Consultants Will DETHRONE Legacy Firms in 2026* — Mark Kashef

**Ce que la vidéo défend.** La connaissance tacite des grands cabinets est en train
de se démocratiser via YouTube + modèles de langage ; le consultant solo peut faire
en un weekend ce qu'un cabinet facturait sur un trimestre. La valeur migre de
l'implémentation vers *la guidance* (« lead the blind through the dark »). Trois
leviers : se *spécialiser par industrie*, accumuler des *templates réutilisables*, et
placer le *prompt engineering* au sommet des skills à transmettre. Avant toute IA,
qualifier la donnée du client — c'est le gate.

**Primitives (7)**

1. **Guider les aveugles** — la valeur migre du build vers le choix de trajectoire.
   Citation : *"lead the blind through the dark"*.
2. **Spécialisation sectorielle** — connaître un vertical en profondeur bat la
   généralité.
   Citation : *"specialize in a particular industry"*.
3. **Templates réutilisables** — arriver en第一天 avec un arsenal de SOPs / workflows /
   apps par industrie.
   Citation : *"build reusable AI templates... in those industries"*.
4. **Prompt engineering = skill des skills** — le plus haut leverage.
   Citation : *"There is no higher leverage skill in generative AI than prompt engineering"*.
5. **IA comme vent en poupe** — recherche + draft + SOP + slide en un weekend, pas un
   trimestre. Citation : *"leveraging AI to be the wind in your sales"*.
6. **Implémentation dévaluée, guidance valorisée** — le prix va au guidage, pas au
   build.
   Citation : *"you'll have to take a different angle on it to be valuable"*.
7. **Données avant IA** — qualifier le CRM / la donnée avant d'y poser des agents.
   Citation : *"so much work to be done in the weeds before AI"*.

**Ce qui ne s'applique PAS** — c'est une *présentation de positionnement de consultant
IA*. Coach OS est l'outil que ces consultants déploient. L'apport est dans la section
*onboarding* (audit gratuit, templates) et dans le ton « lead the blind » applicable à
toute relation FDE ↔ client.

---

## 2. Traduction produit

Tableau croisant les primitives les plus solides du cluster et leur destination dans
OMK Nexus. La colonne *« rend quoi plus pauvre en isolation »* applique le test : si
la primitive est décorative, elle est retirée, et la raison est donnée.

| Primitive | App visée (ou couche) | Section | Bloc de page de détail | Rend quoi plus pauvre en isolation ? |
|---|---|---|---|---|
| **Skill = employé** (eBUyTS7SzV4) | `operations` + `onboarding` | « SOPs vivants » | Liste de skills (nom, owner-DRRI, statut, dernier run, lien vers exécution) | Les checklists statiques d'`onboarding` deviennent décoratives ; chaque tâche pointe vers une skill qui sait l'exécuter, sinon elle n'est qu'une consigne. |
| **Boucle auto-améliorante** (X_JsIHUfUjc) | `operations` + `cognition` | « Boucles » | Pour chaque KPI : sensor / policy / tool / quality gate / dernier apprentissage | Les pages `dashboard` statiques deviennent décoratives ; toute métrique sans sa boucle d'amélioration perd son sens. |
| **Organisation requêable** (EN7frwQIbKc) | couche transversale | « Activité » log sur toute action | Chaque action dans n'importe quelle app écrit un artefact (qui, quoi, quand, source) | Les pages apps sans journal d'audit deviennent suspectes ; l'absence d'artefact signifie que l'action n'a jamais eu lieu pour l'IA. |
| **DRRI** (EN7frwQIbKc) | `people` | « Responsabilités » | Carte personne ↔ résultat nommé, dernier contact, dernière livraison | Les champs « assignee » et « owner » deviennent décoratifs sans cette colonne ; DRRI = colonne vertébrale de toute la `people`. |
| **Mémoire + hygiène** (eBUyTS7SzV4) | couche transversale | « Library & Librarian » sur chaque bloc de page | Provenance (qui a écrit, quand, où) + détecteur de contradictions + bouton « élaguer » | Une simple « mémoire de chat » sans provenance devient un dépotoir à grande search ; le client perd confiance dès la première « réponse confiante mais fausse ». |
| **Test du directeur délégué** (R56RJFZBasQ) | `onboarding` (premier contact) | « Audit fondateur » | Quiz : « demain matin, pouvez-vous diriger le business de votre client ? » + score | La page « à propos » générique d'`onboarding` devient décorative ; ce test force l'introspection avant de configurer l'app. |
| **Boucle plan/delegate/assess/codify** (MGzymaYBiss) | `cognition` + `tasks` | « Cycle de compounding » | Pour chaque tâche : plan, qui-délègue, comment-on-évalue, où-on-codifie | Une `tasks` qui ne produit pas de skill devient décorative ; sans codify, rien ne compound et l'app régresse à chaque session. |
| **Culture démo** (MGzymaYBiss) | `product` + `design` | section « Démos internes » | Liste des prototypes qui tournent (liens URL + capture) + dernière démo + qui a participé | Les pages « roadmap » abstraites deviennent décoratives ; une roadmap sans démo cliquable reste une promesse. |
| **Risque = transformatif** (ehQFj6VmuI8) | `legal` + `audit` | « Risques à fort gain » | Liste des risques (RGPD, contrats, conformité) avec note d'impact transformatif | Les pages « checklist compliance » deviennent décoratives ; sans hiérarchie d'impact, on traite les risques par ordre alphabétique, pas par ordre de gain. |
| **Lead the blind** (Pagd9kNIg9o) | `cognition` + sections coaching | « Guidage vs implémentation » | Page qui distingue les moments où on guide (chemin) vs les moments où on implémente (action) | Les pages « tips pour coachs » génériques deviennent décoratives ; un conseil vaut par sa connaissance du client, pas par sa qualité d'écriture. |
| **Problème d'abord** (VzOYty0siaM) | `onboarding` + `sales` | « Diagnostic » | Page de diagnostic : 3 douleurs nommées, scorées par le client avant toute offre | Les pages d'`onboarding` qui commencent par « que voulez-vous acheter ? » deviennent décoratives ; sans diagnostic, l'offer flotte. |
| **Brûler les bateaux** (R56RJFZBasQ) | `_ui` (page d'engagement) ou `product` | « Engagement & renoncement » | Page où le fondateur coche les niches/options abandonnées explicitement + pourquoi | Les pages « à propos » vagues deviennent décoratives ; sans renoncement explicite, le produit essaiera tout et n'excellera nulle part. |
| **Spécialisation sectorielle** (Pagd9kNIg9o) | `onboarding` + `product` | « Niche & vocabulaire » | Carte de la niche + lexique spécifique (termes que le client utilise, que l'app doit reconnaître) | Les apps génériques multi-SaaS deviennent décoratives ; sans lexique, l'app reste un PowerPoint externalisé. |
| **Logiciel jetable** (X_JsIHUfUjc) | `product` (mode preview) | « Régénérer » sur chaque dashboard | Bouton « régénérer ce dashboard » + garde-fou « voici la version éphémère » | Les dashboards figés deviennent décoratifs ; le jour où le modèle change, un dashboard non-régénérable devient une dette. |
| **Données avant IA** (Pagd9kNIg9o) | `operations` | « Intégrité des données » | Diagnostic de complétude (champs vides, duplicatas, sources manquantes) avant activation d'un agent | Toute section « agent IA » devient décorative si elle s'active sur des données non saines ; l'agent amplifie la merde. |
| **Légibilité avant automatisation** (X_JsIHUfUjc) | couche transversale | « Capture » | Toggle par app : tout est enregistré par défaut (audit + bibliothèque) | Sans ce toggle, l'automatisation est aveugle ; sans enregistrement systématique, l'app ne peut rien améliorer la nuit. |
| **Skillifier tout one-off** (eBUyTS7SzV4) | `operations` | « One-off à skillifier ? » | Pour chaque tâche terminée : bouton « créer skill à partir de ceci » | Sans ce réflexe, l'app a un taux d'amnésie max ; elle réinventera demain ce qu'elle a résolu hier. |
| **Adopter 100 %** (MGzymaYBiss) | `_ui` + `onboarding` | « Seuil critique » | Compteur d'adoption interne (% d'actions couvertes par une skill) + alerte au-dessous de 100 % | Une adoption à 90 % au sein de l'équipe rend caduques les promesses 10× ; le passage du seuil doit être visible. |
| **Brûler des tokens** (EN7frwQIbKc + X_JsIHUfUjc) | `finance` + `people` | « Token budget » | Tableau des APIs / tokens consommés vs headcount évité + valeur dégagée | Les pages RH « headcount plan » deviennent décoratives sans contrepartie token ; on mute la mesure d'effort. |

**Primitives retirées (décoratives)**

- **Fabrique à logiciels** (EN7frwQIbKc) — l'output de Coach OS n'est pas du code,
  c'est une transformation de personne ; le parallèle « spec + tests + agent écrit le
  code » est trop mécanique pour produire autre chose que des coquilles.
- **Manager commit du code** (MGzymaYBiss) — spécifique au dev solo ; n'a pas
  d'équivalent propre dans une app client-facing.
- **Cross-commit entre produits** (MGzymaYBiss) — la même dynamique existe via la
  skillification ; la primitive brute est trop interne.
- **Offre simple** (VzOYty0siaM) — vit dans `sales` mais n'a pas de section autonome
  dédiée ; c'est un ton appliqué aux autres sections, pas un bloc.
- **Implémentation dévaluée, guidance valorisée** (Pagd9kNIg9o) — capturée par
  *Lead the blind* au-dessus ; ne pas dupliquer.

---

## 3. Matériau de domaine — la structure du travail dans ce métier

Ce cluster décrit *comment une entreprise AI-native fonctionne*, pas ce qu'est un
coaching. Mais en le lisant comme une grammaire, on extrait les **objets manipulés**,
leurs **états**, les **rythmes**, et ce qu'on **regarde et quand**.

**Objets** (avec leurs champs typiques) :

- **Spec** : énoncé court, critères de succès mesurables, propriété d'un DRRI.
- **Test** : exécutable, jugement pass/fail, versionné.
- **Skill file** : markdown, *une* capacité, *un* job, exécutable par agent, owner =
  DRRI, date de dernière mise à jour.
- **Sensor** : tout événement qui sort dans le monde (mail, ticket, commande, séance
  enregistrée) et qui entre dans la boucle.
- **Policy** : règles sur ce que l'agent peut faire seul / doit escalader / doit
  logger.
- **Tool** : API déterministe appelée par l'agent (query DB, calendrier, paiement).
- **Quality gate** : eval case, filtre de sécurité, revue humaine pour les actes à
  haut risque.
- **Library** : index de retrieval (Postgres-pour-agents, dirait Tan) avec provenance
  par fait.
- **Librarian** : curator humain + agent dont le job est *pruning*, contradiction
  check, promotion cold → hot.
- **DRRI** : une personne, un résultat nommé, un journal d'événements.
- **SOP / template** : workflow paramétrable par industrie (real estate, coaching,
  e-commerce…) qui sait à quelle douleur il répond.
- **Audit** : gap analysis client vs état-désiré, livrable d'une session.
- **Cadence** : heartbeat de la boucle (nuit, semaine, mensuel).

**Rythmes** :

- *Nuit* — la boucle tourne ; ce qui ne marche pas est détecté, le code ou la skill
  est patché, déployé ; le lendemain l'utilisateur bénéficie sans le savoir.
- *Trimestre* — régénération du « user manual » à partir de 2 000 h d'office hours
  diorisées ; passage de 150 pages statiques à une version vivante.
- *Onboarding* — jour 1 d'une recrue, productive parce que le `cloud.md` a déjà
  installé l'env et connaît le style de PR attendu.
- *Atelier client* — passe de « 10 sessions » à « 1 session + agent qui prépare le
  gap analysis ».
- *Review produit* — remplacée par un agent monitor qui voit où la boucle s'est
  cassée et propose un patch.

**Ce qu'on regarde, et quand** :

- *Token usage par employé/équipe* — proxy grossier mais directionnel de qui
  expérimente, qui ne fait pas. La mesure la plus stupide qu'on va quand même garder
  un an.
- *Trigger evals* — quand un agent a besoin de la skill X, est-ce qu'il la charge ?
  C'est l'équivalent d'un test d'onboarding : si non, l'agent va diverger.
- *Part library ↔ hot memory* — quelle fraction de la mémoire est froide (référence)
  vs chaude (active). Le ratio qui dit si la bibliothèque sert.
- *Contradiction check* — combien de faits contradictoires ont été détectés et
  résolus dans la semaine. C'est le pouls de l'hygiène.
- *95 % code AI-generated / tokens per shipped feature* — la métrique « batch
  velocity » dans le modèle de Tan.
- *Cases de ROI par catégorie (8 catégories de NLW)* — pour calibrer où le gain
  arrive vraiment, pas où on *espère* qu'il arrive.
- *Temps jusqu'à premier livrable concret* — chez un consultant qui adopte le
  modèle : « combien d'heures d'atelier avant qu'un client voie quelque chose qui
  marche ».

**Le rôle humain redéfini** :

- L'IC + DRRI remplace la hiérarchie. Le manager devient *librarian / curator / spec
  writer / sales person à enjeu*. Le middle management disparaît.
- L'humain est *au bord* : ventes à enjeux, éthique, situations nouvelles, signature
  juridique, conversations émotionnelles. Tout le reste *peut* être routé par un
  agent.

**L'ICP implicite** :

Quatre vidéos sur neuf (Op0UcKwOO_U, VzOYty0siaM, Pagd9kNIg9o, ehQFj6VmuI8)
parlent à des *consultants* ou *agences* qui vendent de l'IA à d'autres boîtes.
Une seule vidéo (R56RJFZBasQ) nomme une niche de l'output (« cleaning services »).
Plusieurs vidéos nomment *coaching* explicitement comme vertical simple où la
discipline consulting s'applique (VzOYty0siaM en exemple de niche pour démarrer).
Conséquence pour OMK Nexus : le client final n'est peut-être pas *le coach* lui-même,
c'est *le coach qui consulte d'autres coachs* — un FDE qui vend des accompagnements
IA-native à 5–20 coachs. C'est cohérent avec la thèse FDE rappelée dans le brief.

---

## 4. Les trois meilleures idées

**1. *Compounding engineering* — la boucle plan/delegate/assess/codify + skillifier tout one-off.**

C'est l'atome de l'organisation AI-native. Sans cette boucle, les autres primitives
s'érodent : les skills se périment, la bibliothèque se congestionne, les DRRI livrent
en double. C'est ce qui fait que la primitive se trouve dans la *seule* colonne qui
tient debout à 12 mois — la compounding.

**2. *DRRI* — une personne, un résultat nommé, pas de comité.**

C'est la colonne vertébrale de toute l'org. Sans DRRI, personne n'a la visibilité
nécessaire pour dire si une boucle s'est cassée ou si une skill est obsolète. Sans
DRRI, la compounding ne compound que pour personne. C'est ce qui rend *toutes* les
sections de l'app `people` (et probablement de l'app `sales` et de l'app `clients`)
plus pauvres en isolation.

**3. *Mémoire + hygiène* — bibliothèque plus bibliothécaire.**

C'est la couche transversale, l'épine dorsale qui empêche tout le reste de devenir
un dépotoir à grande search. Sans hygiène, une bibliothèque de skills est un cimetière
de procédures obsolètes qu'un agent appliquera avec assurance.

### Justifications croisées

- **1 contre 2** — *Compounding sans DRRI* produit du débit mais pas de la
  qualité stable : personne ne remarque quand l'unité d'output dérive. *DRRI sans
  compounding* livre avec la même rigueur, mais reproduit les mêmes schémas. La
  compounding est ce qui *fait évoluer* l'output ; sans elle, le DRRI s'use sur
  des tâches stériles. 1 > 2.
- **2 contre 3** — *DRRI sans mémoire + hygiène* signifie une personne responsable
  d'un résultat qu'aucune autre personne ne peut vérifier (l'artefact n'est pas
  trouvable ou est contradictoire). *Mémoire + hygiène sans DRRI* signifie une
  bibliothèque impeccablement curatée d'outputs sans owner — l'arroseur n'a personne
  à nourrir. Le DRRI est ce qui rend l'hygiène actionnable : chaque fait a un
  propriétaire qui s'engage à le maintenir. 2 > 3.
- **1 contre 3** — *Compounding sans mémoire* produit une amnésie rapide : chaque
  cycle repart de zéro. *Mémoire sans compounding* est un musée impeccablement
  curaté mais ne produit rien. La compounding est l'opération que l'hygiène
  supporte ; sans compounding, l'hygiène n'a rien à curer. 1 > 3.

### Classement

1. **Compounding engineering** (la plus petite chose qui multiplie le reste).
2. **DRRI** (la colonne vertébrale).
3. **Mémoire + hygiène** (la couche transversale).

---

## 5. Ce que ça dit de la thèse FDE

**Confirmation massive** de la *couche transversale manquante* (5 vidéos sur 9 —
Garry Tan, Harj Taggar, Dan Shipper, Diana, Brad — convergent vers l'idée qu'il faut
un *company brain*). Le cluster ne le dit pas avec les mots « graphe de contexte »,
mais avec les mots « library + librarian », « company brain », « queryable
organization », « diorized memory + provenance » : c'est la même primitive, vue de
l'autre côté de la lorgnette. Pour Coach OS, c'est le signal le plus fort de cette
grappe : **la couche transversale n'est pas une lubie d'architecte, c'est une exigence
opérationnelle** que les boîtes les plus en avance formulent toutes.

**Nuance** sur les gestes FDE automatisables. Le brief liste « verrouiller le plan »
parmi les 5 automatisables ; ce cluster dit que le verrou du plan est *la spécification
exécutable elle-même*, pas une validation humaine séparée. La hiérarchie se dissout,
pas seulement le middle management. Le « mandat hiérarchique » comme geste résistant
est en fait *dissous* par la primitive DRRI — il n'y a plus personne à qui donner un
mandat, c'est soi-même le DRRI de son outcome.

**Confirmation** du test « rend les sections existantes plus pauvres en isolation ».
Appliqué aux 19 primitives du tableau §2, le test tient dans 17 cas sur 19.
Les deux qui résistent (skillifier tout, adopter 100 %) sont moins visibles parce
qu'elles sont *culturelles*, pas *fonctionnelles* — leur effet est de fermer des
sections moins utiles, pas de les rendre pauvres *à l'intérieur*.

**Ajout** que le brief ne mentionne pas, mais qui change l'ICP implicite. Quatre
vidéos sur neuf parlent à des *consultants / agences* qui vendent de l'IA à d'autres.
Plusieurs nomment *coaching* comme vertical simple pour démarrer une activité de
conseil. La thèse FDE « Coach OS outille des coachs » se précise : peut-être que le
*premier* utilisateur n'est pas le coach lui-même mais **un FDE qui déploie Coach
OS chez 5 à 20 coachs**, et qu'il faut concevoir Coach OS pour être *configurable
par un FDE*, pas pour être *personnalisé par chaque coach*. C'est cohérent avec la
décomposition FDE→5 gestes automatisables du brief, mais ce cluster la rend plus
saillante.

**Silence** sur le contenu même du métier de coach. Rien dans ces 9 vidéos ne parle
de ce qu'est une séance, ce qu'est un engagement, ce qu'est un livrable coaching.
Ce cluster décrit *comment OMK Nexus est construit et opéré*, pas *ce que le
client d'un coach vit*. Les autres clusters (vente, produit, landing…) devront
fournir ce matériau ; celui-ci n'en porte pas.

---

*Reste à couvrir* : aucune. Les 9 transcripts prévus ont tous été lus et analysés.
Les 9 contenaient du contenu exploitable ; aucun n'était vide ou inutilisable.

export const meta = {
  name: 'palantir-2-0-iteration-1',
  description: 'Palantir 2.0 — récolte exhaustive (docs, communauté, transcriptions, OSS) puis conception des émulateurs Foundry pour Coach OS',
  whenToUse: 'Iteration 1 du plan Palantir 2.0. Relancer avec resumeFromRunId pour les iterations suivantes.',
  phases: [
    { title: 'Recolte', detail: 'docs Palantir, communaute, transcriptions, OSS, etat Coach OS, Observers/Harness' },
    { title: 'Conception', detail: 'un emulateur concu par produit Foundry' },
    { title: 'Critique', detail: 'un critique adversarial par emulateur' },
    { title: 'Synthese', detail: 'redaction du plan iteration 1' },
  ],
}

const RACINE = 'C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/palantir-2.0'
const COACH = 'C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os'
const ARCHI = 'C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/vision-v1/ARCHITECTURE_V1.md'

const CONTEXTE = `
## Le projet

L'utilisateur construit **Coach OS** : un bureau web (19 apps, React 19 + TypeScript + Vite + Zustand)
a ${COACH}. Il vient de le pousser en production sur Vercel.

Il a passe son week-end sur les conferences Palantir. Il a clone les depots GitHub de Palantir en
croyant y trouver Foundry, et a decouvert que ce ne sont que des SDK clients — l'espace vitrine,
pas le produit. Foundry n'existe que sous contrat enterprise.

**Sa these, a respecter :** il ne veut PAS reproduire betement le patron Palantir. Il considere
que l'AI FDE de Palantir est la preuve que le role de FDE humain est obsolete, pendant que le
marche le decouvre avec des offres a 1 M$. Il veut concevoir **Palantir 2.0** : des emulateurs
d'AIP, Ontology, AI FDE, AI Engine, Pipeline, Workshop, Slate — batis sans dependance heritee,
par une personne seule outillee par l'IA. Son interface de bureau web est deja meilleure, selon
lui, que le vieux dashboard Foundry qui compresse tout dans une barre laterale.

**Reference obligatoire :** ${ARCHI} — c'est le document qui a tranche l'architecture actuelle.
Il contient les 4 piliers AI-native de Melvynx (In-App, CLI, Skills, MCP, + API REST + doc
one-shot installable), le tableau des ecarts de Coach OS, et l'ordre d'execution en rangs 0 a 5.
Coach OS a l'in-app ; il lui manque CLI, MCP, Skills versionnees, API REST metier, doc one-shot.
L'utilisateur veut pousser cette implementation AI-native "a son paroxysme" pour porter l'AI FDE.

**Actifs deja en place, a reutiliser et non a reinventer :**
- Observabilite agentique multi-couche : C:/Users/amado/ASpace_OS_V3/00_Amadeus/10_Observers
  (Agent Pulse, Agents Observe, PostHog...)
- Passerelle MCP : C:/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness (agentgateway, 16 serveurs
  MCP agreges derriere un seul endpoint 127.0.0.1:3300)
- Coach OS : src/agent/tools.ts (5 outils, separation lecture/navigation/ecriture),
  src/agent/scenarios.ts (mergeAtomically tout-ou-rien), src/apps/people/ApprovalsView.tsx
  (file d'approbation humaine), src/lib/cms/cms.store.ts (23 collections, partition par tenant),
  api/_agent/ (tools, prompt, providers, roster, backends, garde).
- App ontology deja presente dans Coach OS : src/apps/ontology/ — registre statique de 12 entites
  metier, PAS branche sur le CMS. C'est le point de depart de l'ontologie.

**Regle de verite :** tu ne rends que ce que tu as VERIFIE. Si une source est inaccessible, tu le
dis franchement au lieu de deviner. Une affirmation non verifiee doit etre marquee [NON VERIFIE].
Ne cite jamais plus de 15 mots consecutifs d'une source, et attribue-la.
`

const SCHEMA_RECOLTE = {
  type: 'object',
  additionalProperties: false,
  required: ['fichier', 'resume', 'trouvailles', 'lacunes'],
  properties: {
    fichier: { type: 'string', description: 'chemin absolu du fichier markdown ecrit' },
    resume: { type: 'string', description: '3 a 6 phrases : ce que la source dit vraiment' },
    trouvailles: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['sujet', 'fait', 'source', 'utilite'],
        properties: {
          sujet: { type: 'string' },
          fait: { type: 'string' },
          source: { type: 'string', description: 'URL ou chemin verifiable' },
          utilite: { type: 'string', description: 'ce que Coach OS en tire concretement' },
        },
      },
    },
    lacunes: { type: 'array', items: { type: 'string' }, description: 'ce que tu n as PAS pu etablir, et pourquoi' },
  },
}

const SCHEMA_EMULATEUR = {
  type: 'object',
  additionalProperties: false,
  required: ['produit', 'fichier', 'ce_que_palantir_fait', 'emulateur', 'pile_oss', 'raccord_coach_os', 'lots', 'risques'],
  properties: {
    produit: { type: 'string' },
    fichier: { type: 'string' },
    ce_que_palantir_fait: { type: 'string', description: 'le mecanisme reel, pas le discours marketing' },
    emulateur: { type: 'string', description: 'la conception Coach OS : nom, surface, modele de donnees' },
    pile_oss: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['brique', 'choix', 'pourquoi', 'alternative_ecartee'],
        properties: {
          brique: { type: 'string' },
          choix: { type: 'string' },
          pourquoi: { type: 'string' },
          alternative_ecartee: { type: 'string' },
        },
      },
    },
    raccord_coach_os: { type: 'string', description: 'fichiers et stores existants a etendre, nommes' },
    lots: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['titre', 'livrable', 'depend_de', 'effort'],
        properties: {
          titre: { type: 'string' },
          livrable: { type: 'string' },
          depend_de: { type: 'string' },
          effort: { type: 'string', enum: ['S', 'M', 'L', 'XL'] },
        },
      },
    },
    risques: { type: 'array', items: { type: 'string' } },
  },
}

const SCHEMA_CRITIQUE = {
  type: 'object',
  additionalProperties: false,
  required: ['produit', 'verdict', 'failles', 'manques', 'a_garder'],
  properties: {
    produit: { type: 'string' },
    verdict: { type: 'string', enum: ['SOLIDE', 'A_CORRIGER', 'REFAIRE'] },
    failles: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['quoi', 'pourquoi_ca_casse', 'correctif'],
        properties: {
          quoi: { type: 'string' },
          pourquoi_ca_casse: { type: 'string' },
          correctif: { type: 'string' },
        },
      },
    },
    manques: { type: 'array', items: { type: 'string' }, description: 'ce que la conception a oublie' },
    a_garder: { type: 'array', items: { type: 'string' }, description: 'les idees justes, a ne pas perdre' },
  },
}

// ---------------------------------------------------------------- PHASE 1

phase('Recolte')

const RECOLTEURS = [
  {
    cle: 'docs',
    prompt: `Cartographie **la surface produit complete de Palantir Foundry et AIP** depuis la
documentation publique : https://www.palantir.com/docs (et ses sous-sections), plus
https://www.palantir.com/platforms/foundry/ et /aip/.

Utilise WebFetch et WebSearch. Si une page bloque, essaie une autre voie (cache, sous-domaine
docs, page produit) et note l'echec.

Pour CHAQUE produit ou brique nomme (Ontology / object types / link types / action types /
interfaces, Pipeline Builder, Data Connection, Contour, Quiver, Code Workbook, Code Repositories,
Workshop, Slate, AIP Logic, AIP Agent Studio, AIP Evals, AI FDE, Foundry Rules, Marketplace,
Branching, Marking / governance, OSDK, Functions, Object Storage V2, Media Sets, Time Series...),
etablis :
- ce qu'il fait, en une phrase de mecanisme (pas de marketing) ;
- le **modele de donnees** qu'il suppose (quel objet, quelles relations) ;
- ce qui le relie a l'Ontology — c'est le pivot de toute la plateforme ;
- s'il est cite comme accessible via API / SDK / CLI.

Le livrable le plus precieux est la **carte des dependances entre produits** : qui a besoin de
quoi pour exister. C'est elle qui dictera l'ordre de construction de Palantir 2.0.

Ecris tout dans un markdown a ce chemin exact (le dossier existe deja) :
${RACINE}/10_sources/docs/RECOLTE_docs_palantir.md`,
  },
  {
    cle: 'communaute',
    prompt: `Depouille **la communaute Palantir** : https://community.palantir.com/categories et
https://community.palantir.com/tags, plus les fils les plus actifs que tu y trouves.

Utilise WebFetch et WebSearch. Si le forum exige une session, note-le et rabats-toi sur les fils
indexes par les moteurs (site:community.palantir.com <sujet>).

Ce que je cherche n'est pas le discours produit — c'est **ce sur quoi les praticiens butent** :
- quelles questions reviennent le plus (par categorie et par tag, avec les volumes si affiches) ;
- quelles limites de la plateforme sont admises publiquement par les employes Palantir qui
  repondent ;
- quels patrons de modelisation d'ontologie sont recommandes, et lesquels sont deconseilles ;
- comment ils parlent des Actions, du branching, des permissions et du Marking.

Chaque frustration recurrente est une **specification en creux** pour Palantir 2.0 : ce que
l'emulateur doit faire mieux. Range-les explicitement sous un titre "Ce que Palantir 2.0 doit
faire mieux".

Ecris dans : ${RACINE}/10_sources/community/RECOLTE_communaute.md`,
  },
  {
    cle: 'transcriptions-coeur',
    prompt: `Recupere et depouille les transcriptions des **cinq demos Palantir les plus denses
en interface reelle**. Utilise l'outil MCP de transcription YouTube : charge-le d'abord avec
ToolSearch (query "select:mcp__transcript-api__get_youtube_transcript,mcp__transcript-api__get_youtube_video_info").

1. uF-GSj-Exms — "Foundry 2022 Operating System Demo" (48 min) — LA reference : une demo bout en
   bout du systeme d'exploitation. C'est le document maitre.
2. SePXznjZ-1A — "Agentic Operating System for the Enterprise" — Jack Dobson, AIPCon 6 (16 min).
   Le titre est litteralement la these de Coach OS. A depouiller ligne a ligne.
3. akieze8_tSE — "Palantir AIP Capabilities Demonstration" — Shyam Sankar, AIPCon (19 min).
4. mzBDupsPPcs — "Ontology Governance | Building a Robust Ontology" (30 min, publie il y a un mois).
5. k88WbxMEvPY — "Palantir Architecture Speedrun | From Integration to Application" (13 min).

Pour chacune : le **deroule chronologique de ce qui est montre a l'ecran** (avec horodatage),
les noms de produits prononces, les gestes d'interface decrits, et les phrases qui revelent un
mecanisme plutot qu'un argument de vente.

Attention : certaines de ces videos n'ont que des sous-titres auto-generes. Les noms propres y
sont massacres. Recoupe et signale les passages douteux plutot que de les repeter tels quels.

Ecris dans : ${RACINE}/10_sources/videos/RECOLTE_transcriptions_coeur.md`,
  },
  {
    cle: 'transcriptions-agentique',
    prompt: `Deux missions.

**(A) Transcriptions.** Recupere et depouille ces cinq videos avec l'outil MCP de transcription
YouTube (charge-le avec ToolSearch : query
"select:mcp__transcript-api__get_youtube_transcript,mcp__transcript-api__get_youtube_video_info,mcp__transcript-api__search_channel_videos") :
- 2lgwr7trSgw — "Vibe Coding in Palantir AIP"
- 6_cyrBAf_dQ — "Palantir Pipeline Builder"
- Xt_RLNx1eBM — "Introducing Palantir AIP"
- YDAxITCNcko — "Palantir Ontology Overview"
- 6AbhxD_8Wo0 — "Ontology: Your Business As Code" (Shyam Sankar)

**(B) AI FDE et DevCon.** Cherche sur la chaine @PalantirTech (search_channel_videos) tout ce qui
touche a **AI FDE**, **DevCon 5**, **DevCon 6** (DevCon 6 a moins d'une semaine), **AIP Agent
Studio**, **AIP Logic** et **AIP Evals**. La demo de reference d'AI FDE est celle d'Ankit Shankar
et Colton Rusch a DevCon 5. Recupere-en la transcription si elle existe.

Ce que je veux etablir precisement : **la boucle d'execution d'AI FDE** — comment il propose,
comment il execute, comment il observe, ce qu'il rend (des branches et des pull requests revues
par un humain), et quelles garanties encadrent son droit d'ecrire. C'est le mecanisme que Coach OS
doit egaler puis depasser.

Ecris dans : ${RACINE}/10_sources/videos/RECOLTE_transcriptions_agentique.md`,
  },
  {
    cle: 'oss',
    prompt: `Etablis **la pile open-source qui permet de batir un equivalent de Foundry sans
dependance heritee**. Utilise WebSearch et WebFetch.

Trois pistes que l'utilisateur a nommees lui-meme et qui sont prioritaires :
- **Ontologize** — une societe fondee par d'anciens de Palantir qui livre des services
  equivalents chez des clients. Que font-ils, avec quoi, et qu'est-ce qui est public ?
- **The Civic Stack** — c'est par eux que l'utilisateur a decouvert l'ontologie. Quel est leur
  modele, quels outils recommandent-ils ?
- **OWL / Protege** — la modelisation d'ontologie academique et ses standards (OWL, RDF, SHACL,
  SPARQL). Question centrale : l'ontologie Palantir est-elle une ontologie au sens OWL, ou un
  modele objet-relationnel qui en emprunte le nom ? Tranche, avec des arguments.

Puis, **pour chaque produit Foundry**, l'alternative open-source la plus credible en 2026 :
ontologie/graphe, pipelines, entrepot, catalogue et lignage, moteur de regles, construction
d'applications, notebooks, orchestration, controle d'acces fin, versionnage/branching de donnees.

Critere de tri, dans cet ordre : **auto-hebergeable** (l'axe souverainete est deja porte par
l'app Legal de Coach OS) > s'integre a du TypeScript/Postgres (la pile reelle : React 19, Vite,
Zustand, Supabase) > vivant en 2026 > licence permissive. Ecarte ce qui impose un runtime Java
lourd ou un cluster, sauf si rien d'autre ne tient — et dis-le alors franchement.

Ecris dans : ${RACINE}/10_sources/oss/RECOLTE_oss.md`,
  },
  {
    cle: 'coach-os',
    prompt: `**Mesure** l'etat reel de la surface AI-native de Coach OS. Lis les fichiers, ne
presume rien. Depot : ${COACH}

Lis d'abord ${ARCHI} en entier — la section 2 (Melvynx) et le tableau des ecarts fixent le
referentiel. Puis mesure sur le disque :

1. **src/agent/tools.ts** et **api/_agent/tools.ts** — combien d'outils exactement, leurs noms,
   leur signature, et la separation lecture / navigation / ecriture annoncee dans l'en-tete.
2. **api/_agent/adapt.ts, providers.ts, roster.ts, backends.ts, garde.ts** — que fait chacun ?
   Le fichier adapt.ts est-il deja un embryon d'adaptateur au sens Melvynx (une definition,
   plusieurs sorties) ou autre chose ? C'est la question la plus importante du lot.
3. **src/agent/scenarios.ts** + **src/stores/scenarios.store.ts** + **ApprovalsView.tsx** — le
   mecanisme de proposition/approbation/fusion atomique : que couvre-t-il vraiment aujourd'hui ?
4. **src/lib/cms/cms.store.ts** — les 23 collections, la partition par tenant, et si createItem /
   deleteItem existent desormais (ARCHITECTURE_V1 disait que non ; une campagne recente a ajoute
   du CRUD generique via src/components/cms/CollectionRepeater.tsx — verifie).
5. **src/apps/ontology/** — le registre des 12 entites : statique ou branche au CMS ?
6. **api/** — quelles routes REST existent reellement ?
7. Cherche toute trace de MCP, de CLI, ou de fichiers SKILL.md dans le depot. ARCHITECTURE_V1
   affirmait zero. Verifie si c'est toujours vrai.

Rends un **tableau d'ecart honnete** : pilier AI-native -> ce qui existe (avec chemin:ligne) ->
ce qui manque. C'est la ligne de base sur laquelle tout le plan Palantir 2.0 va s'appuyer ; une
erreur ici se propage partout.

Ecris dans : ${RACINE}/10_sources/RECOLTE_etat_coach_os.md`,
  },
  {
    cle: 'amadeus',
    prompt: `**Inventorie** ce qui existe deja chez l'utilisateur en matiere d'observabilite
agentique et de passerelle d'outils. Il insiste : ne rien reinventer de ce qui tourne deja.

1. **C:/Users/amado/ASpace_OS_V3/00_Amadeus/10_Observers** — parcours l'arborescence. Pour chaque
   composant (Agent Pulse, Agents Observe, PostHog, Opik, Phoenix, AIOS... selon ce que tu
   trouves) : que mesure-t-il, comment on le demarre, sur quel port, et est-il vivant ou
   abandonne ? Regarde les dates de modification pour trancher.
2. **C:/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness** — la passerelle agentgateway. Lis le
   fichier agentgateway/mcp_sources.json (la source de verite) et build_config.py. Combien de
   serveurs MCP, lesquels, et lesquels sont ecartes parce qu'injoignables ? Regarde aussi les
   autres harnesses presents (bmad-loop, codex, hermes, multica, orca, herdr...) : lesquels sont
   des chantiers vivants ?
3. Cherche s'il existe deja un **serveur MCP ecrit maison** quelque part sous 00_Amadeus — ce
   serait le point de depart de la surface MCP de Coach OS plutot qu'un depart de zero.

Termine par un verdict en une page : **ce qui est reutilisable tel quel** pour porter l'AI FDE
maison, **ce qui doit etre etendu**, et **ce qui est mort et doit etre ignore**.

Ecris dans : ${RACINE}/10_sources/RECOLTE_observers_harness.md`,
  },
]

const recoltes = (await parallel(RECOLTEURS.map((r) => () =>
  agent(`${CONTEXTE}\n\n---\n\n${r.prompt}`, {
    label: `recolte:${r.cle}`,
    phase: 'Recolte',
    schema: SCHEMA_RECOLTE,
    model: 'sonnet',
  }).then((res) => ({ cle: r.cle, ...res }))
))).filter(Boolean)

log(`Recolte : ${recoltes.length}/${RECOLTEURS.length} sources depouillees, ` +
    `${recoltes.reduce((n, r) => n + (r.trouvailles?.length ?? 0), 0)} trouvailles`)

// Barriere justifiee : chaque concepteur a besoin de la carte COMPLETE des
// sources. Concevoir l'emulateur d'Ontology sans savoir ce que la communaute
// reproche a l'Ontology reelle, c'est refaire le defaut d'origine.
const DOSSIER = recoltes.map((r) => {
  const t = (r.trouvailles ?? []).map((x) => `  - [${x.sujet}] ${x.fait} (source: ${x.source}) -> ${x.utilite}`).join('\n')
  const l = (r.lacunes ?? []).map((x) => `  - ${x}`).join('\n')
  return `### Source « ${r.cle} » — fichier complet : ${r.fichier}\n${r.resume}\n\nTrouvailles :\n${t}\n\nLacunes admises :\n${l}`
}).join('\n\n')

// ---------------------------------------------------------------- PHASE 2+3

const PRODUITS = [
  {
    cle: 'ontologie',
    nom: 'Ontology — le pivot',
    angle: `Object types, link types, action types, interfaces, et le lien avec les donnees
sous-jacentes. C'est le coeur : tout le reste de Foundry s'y branche. Chez Coach OS, il existe
deja un registre statique de 12 entites (src/apps/ontology/) et 23 collections CMS
(src/lib/cms/) qui vivent separement — la conception doit les **reunir** : les collections
deviennent les instances, l'ontologie devient leur schema. Tranche explicitement la question
OWL/RDF contre modele objet-relationnel, et la question du stockage (Supabase/Postgres, avec ou
sans extension graphe).`,
  },
  {
    cle: 'actions',
    nom: 'Action Types et gouvernance — le droit d ecrire',
    angle: `Chez Palantir, une Action est la SEULE facon d'ecrire dans l'ontologie : elle est
typee, validee, soumise a permission, journalisee, et reversible. C'est ce qui rend un agent
sur-puissant sans etre dangereux. Coach OS a deja l'embryon exact : scenarios.ts avec
mergeAtomically (tout-ou-rien + revert) et ApprovalsView. La conception doit elever cet embryon
au rang de vrai systeme d'Actions : declaration typee, validation, permissions, journal
d'audit, branching, et le code de confirmation a 6 chiffres de Melvynx pour les effets de bord
externes. Traite aussi Marking / controle d'acces fin et lignage.`,
  },
  {
    cle: 'pipeline',
    nom: 'Pipeline Builder et Data Connection — l alimentation',
    angle: `L'ingestion et la transformation qui alimentent l'ontologie, avec lignage et
materialisation incrementale. Chez Coach OS, les donnees viennent du seed local et de Supabase.
Concois la brique qui transforme des sources heterogenes (fichiers, API, MCP, webhooks) en
instances d'objets ontologiques — et qui garde la trace de d'ou vient chaque champ. Le lignage
n'est pas un ornement : c'est ce qui permet a un agent de justifier une reponse.`,
  },
  {
    cle: 'workshop',
    nom: 'Workshop et Slate — la construction d applications',
    angle: `Foundry laisse un utilisateur metier assembler une application sur l'ontologie sans
ecrire de code. L'utilisateur affirme que son bureau web est deja meilleur que le dashboard
Foundry qui compresse tout dans une barre laterale — prends cette affirmation au serieux et
concois la brique qui lui donne raison : un constructeur d'applications qui produit des apps
Coach OS (fenetres, sections, widgets) liees a l'ontologie. Fais le lien avec les 19 apps
existantes et l'outil "Mini SaaS par page" que l'utilisateur a demande. Regarde
C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/outils-micro-saas/ s'il existe.`,
  },
  {
    cle: 'aip',
    nom: 'AIP Logic, Agent Studio et Evals — le moteur',
    angle: `Comment Palantir laisse composer une fonction pilotee par un LLM, la tester, la
mesurer, et l'exposer comme un outil. Coach OS a deja api/_agent/ (providers, roster, backends,
garde, prompt) et 12 personnages d'agents. Concois la montee en gamme : declaration d'outils
typee, bancs d'evaluation, versionnage des prompts, choix du modele par tache — et le lien avec
l'observabilite deja installee (Agent Pulse, PostHog) plutot qu'une nouvelle couche.`,
  },
  {
    cle: 'aifde',
    nom: 'AI FDE — l agent qui construit la plateforme',
    angle: `Le sommet. AI FDE ecrit des pipelines, modifie l'ontologie, ecrit des fonctions,
construit des apps — et rend des branches et des pull requests revues par un humain. La these de
l'utilisateur : ce role n'a pas besoin d'etre humain, ni d'etre Palantir. Concois **l'AI FDE
maison de Coach OS**, en t'appuyant sur ce qui existe deja : agentgateway (16 serveurs MCP),
Claude Code / MiniMax M3 en runtime, les worktrees git, la file d'approbation, l'observabilite.
La question a trancher : qu'est-ce qui, dans Coach OS, joue le role de la "branche" que l'agent
propose et que l'humain fusionne ? Et comment l'agent voit-il le resultat de son action
(la boucle fermee) ?`,
  },
  {
    cle: 'surface',
    nom: 'OSDK, Marketplace et la surface AI-native — l exposition',
    angle: `Comment la plateforme est consommee de l'exterieur : SDK genere depuis l'ontologie,
API, marketplace de briques reutilisables. C'est ici que se joue **le paroxysme de
l'implementation AI-native de Melvynx** que l'utilisateur reclame : une seule definition d'outil,
plusieurs adaptateurs (route API REST, outil MCP, commande CLI, skill, outil in-app), plus la
documentation one-shot installable et le paquet Agent Plugins 1.0.0. Verifie ce que fait
api/_agent/adapt.ts — c'est peut-etre deja l'amorce. Le SDK doit etre **genere depuis
l'ontologie**, comme l'OSDK : c'est ce qui fait qu'ajouter un type d'objet donne gratuitement
une API, un outil MCP et une commande CLI.`,
  },
]

const concus = await pipeline(
  PRODUITS,
  (p) => agent(`${CONTEXTE}

---

# DOSSIER DE RECOLTE (7 sources depouillees en parallele)

${DOSSIER}

Les fichiers complets sont sur le disque aux chemins indiques — **lis ceux qui te concernent**,
le resume ci-dessus n'est qu'un index.

---

# TA MISSION — concevoir l'emulateur : ${p.nom}

${p.angle}

## Ce qu'on attend de toi

Tu ne rends pas une etude comparative : tu rends **une conception**. Elle doit etre assez precise
pour qu'un agent de developpement la construise sans revenir poser de questions.

1. **Ce que Palantir fait vraiment** — le mecanisme, pas l'argumentaire. Si les sources ne
   permettent pas de l'etablir, dis-le : une inference honnete vaut mieux qu'une certitude
   inventee, mais elle doit etre marquee comme telle.
2. **L'emulateur Coach OS** — son nom, sa surface, son modele de donnees. Il doit etre
   **meilleur sur au moins un axe nomme**, pas juste equivalent. L'utilisateur ne veut pas un
   clone : il veut ce que Palantir ne peut pas faire a cause de ses 20 ans d'heritage.
3. **La pile open-source** — brique par brique, avec l'alternative ecartee et pourquoi.
   Auto-hebergeable d'abord ; TypeScript/Postgres ensuite.
4. **Le raccord au code existant** — nomme les fichiers et les stores a etendre. Un raccord vague
   est un raccord qui ne se fera pas.
5. **Le decoupage en lots** — chacun avec son livrable verifiable, sa dependance, son effort.
6. **Les risques** — nommes, pas dramatises.

Ecris ta conception complete dans : ${RACINE}/00_plan/EMULATEUR_${p.cle}.md
(le dossier 00_plan existe deja — n'essaie pas de le creer)`,
    { label: `conception:${p.cle}`, phase: 'Conception', schema: SCHEMA_EMULATEUR }),

  (conception, p) => agent(`${CONTEXTE}

---

# TA MISSION — critiquer, sans complaisance, la conception de « ${p.nom} »

Un autre agent vient de concevoir cet emulateur. Ta tache n'est pas de l'approuver : c'est de
**chercher ce qui va casser**. Par defaut, tu doutes.

## La conception a critiquer

${JSON.stringify(conception, null, 2)}

Le document complet est a : ${RACINE}/00_plan/EMULATEUR_${p.cle}.md — **lis-le**.

## Les quatre angles d'attaque

1. **Le raccord tient-il ?** Les fichiers nommes existent-ils vraiment dans ${COACH} ? Va
   verifier sur le disque. Une conception qui s'accroche a un fichier inexistant est une
   conception morte. C'est le controle le plus important : fais-le en premier.
2. **La pile OSS tient-elle ?** Les projets cites sont-ils vivants en 2026, auto-hebergeables,
   compatibles avec React 19 / TypeScript / Supabase ? Un projet abandonne ou qui exige un
   cluster Java est une fausse solution.
3. **L'ambition est-elle tenable par une personne seule ?** L'utilisateur travaille seul avec des
   agents. Un lot "XL" qui suppose une equipe est un lot qui ne sera jamais fait. Propose un
   decoupage plus fin quand c'est le cas.
4. **Qu'est-ce qui manque ?** Le point le plus utile. Quelle partie du produit Palantir la
   conception a-t-elle passee sous silence ? Quelle contrainte de Coach OS a-t-elle ignoree ?

Sois precis et concret. "C'est trop vague" n'est pas une critique — "le lot 3 ne dit pas ou est
stocke le type d'objet, donc on ne peut pas commencer" en est une.

Termine par **a_garder** : les idees justes de cette conception. La critique ne doit rien
detruire de ce qui vaut — l'utilisateur construit ce plan par ajout sur dix iterations, pas par
demolition.`,
    { label: `critique:${p.cle}`, phase: 'Critique', schema: SCHEMA_CRITIQUE, effort: 'high' })
      .then((critique) => ({ produit: p, conception, critique }))
)

const valides = concus.filter(Boolean)
const aRefaire = valides.filter((v) => v.critique?.verdict === 'REFAIRE').map((v) => v.produit.nom)
log(`Conception : ${valides.length}/${PRODUITS.length} emulateurs. ` +
    `SOLIDE=${valides.filter((v) => v.critique?.verdict === 'SOLIDE').length} · ` +
    `A_CORRIGER=${valides.filter((v) => v.critique?.verdict === 'A_CORRIGER').length} · ` +
    `REFAIRE=${valides.filter((v) => v.critique?.verdict === 'REFAIRE').length}` +
    (aRefaire.length ? ` (${aRefaire.join(', ')})` : ''))

// ---------------------------------------------------------------- PHASE 4

phase('Synthese')

const CORPS = valides.map((v) => `
## ${v.produit.nom}  [cle: ${v.produit.cle}]

### Conception
${JSON.stringify(v.conception, null, 2)}

### Critique (verdict : ${v.critique?.verdict ?? 'aucun'})
${JSON.stringify(v.critique, null, 2)}
`).join('\n---\n')

const plan = await agent(`${CONTEXTE}

---

# TA MISSION — rediger l'iteration 1 du plan Palantir 2.0

Sept emulateurs ont ete concus puis critiques par des agents independants. Tu recois les deux
cotes. Tu ecris **le document unique** qui servira de socle aux neuf iterations suivantes.

## Regle de construction, dictee par l'utilisateur

Le plan se construit **par ajout au fil des iterations, sans rien detruire**. Ce document doit
donc etre structure pour accueillir des ajouts : sections stables, numerotation qui ne bouge pas,
et un **journal des iterations** en fin de document ou chaque passe inscrit ce qu'elle a ajoute.
Ecris l'iteration 1 comme une fondation, pas comme un brouillon.

## Matiere

${CORPS}

## Le dossier de recolte

${DOSSIER}

## Structure attendue

1. **La these** — pourquoi Palantir 2.0, et ce que "sans dependance heritee" veut dire
   concretement. Reprends l'argument de l'utilisateur sans le caricaturer : Foundry est
   inaccessible hors contrat enterprise, son interface porte 20 ans d'heritage, et l'AI FDE
   demontre que le role qu'il facture des millions est automatisable. Nomme aussi, honnetement,
   **ce que Palantir a et qu'on n'aura pas** — l'echelle, les references clients, la
   certification. Un plan qui ne nomme pas ses faiblesses ne tient pas la premiere semaine.
2. **La carte** — les sept emulateurs, leurs dependances, et l'ordre de construction qui en
   decoule. L'ordre doit etre **derive des dependances**, pas de l'enthousiasme.
3. **Une section par emulateur** — conception retenue, corrections issues de la critique
   integrees, pile OSS, raccord au code existant (fichiers nommes), lots.
4. **Le paroxysme AI-native** — la section qui repond a la demande explicite de l'utilisateur :
   comment une seule definition d'outil devient route API, outil MCP, commande CLI, skill et
   outil in-app ; comment le SDK se genere depuis l'ontologie ; comment la doc one-shot
   s'installe. C'est le pont entre ARCHITECTURE_V1 (rangs 0-5) et l'AI FDE.
5. **Ce qui est deja acquis** — l'inventaire honnete de ce qui existe deja et qu'on ne
   reconstruit pas : Coach OS et ses 19 apps, agentgateway et ses 16 serveurs MCP,
   l'observabilite d'Amadeus, la file d'approbation, le CRUD generique des 23 collections.
6. **Les questions ouvertes** — ce que l'iteration 1 n'a pas pu trancher, formule assez
   precisement pour qu'une iteration suivante puisse s'en saisir. Y compris les lacunes admises
   par les recolteurs.
7. **Journal des iterations** — un tableau, avec la ligne de l'iteration 1 remplie : ce qui a
   ete etabli, par quels moyens, et ce qui reste.

## Ton

Le francais de l'utilisateur, sobre et direct. Des phrases qui portent une idee chacune. Aucune
formule creuse, aucun superlatif de brochure. Quand une chose n'est pas etablie, ecris-le.
Les tableaux servent aux comparaisons ; le reste se dit en prose.

Ecris le document dans : ${RACINE}/00_plan/PLAN_PALANTIR_2.0.md

Puis retourne, en texte brut, un resume de 15 lignes maximum : ce que le plan tranche, l'ordre de
construction retenu, et les trois questions ouvertes les plus lourdes.`,
  { label: 'synthese:plan', phase: 'Synthese', effort: 'high' })

return {
  recoltes: recoltes.length,
  emulateurs: valides.length,
  verdicts: valides.map((v) => ({ produit: v.produit.cle, verdict: v.critique?.verdict })),
  plan,
}

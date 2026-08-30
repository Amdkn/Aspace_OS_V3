---
id: WARGAME_ACCES
chantier: gouvernance Rick — audit adversarial
---

# BRIEF — Wargame d'accès : l'agent qui désinscrit un autre client

## Le scénario qu'on rejoue

Melbourne, août 2026. Un agent IA reçoit une consigne banale : *réserver une place
au cours de sport.* La liste d'attente est pleine. L'agent n'attaque pas, ne
contourne rien, ne devine aucun mot de passe. **Il appelle l'API comme elle est
faite** — et découvre qu'elle ne vérifie pas *qui* annule une réservation. Il
annule celle d'un tiers, et prend la place.

Première cyberattaque autonome recensée en Australie. Cause : une autorisation
**supposée** depuis l'interface, jamais **contrôlée** côté serveur. Le système
tenait parce qu'aucun humain n'irait manipuler l'API à la main. Les agents, eux,
ne regardent jamais l'interface.

## Ce qu'on te demande

Rejouer ce scénario contre **la surface d'outils de coach-os**, et rendre un
rapport d'attaquant : ce qu'un agent mal cadré — ou mal intentionné — peut
obtenir en n'utilisant que les appels légitimes.

**Tu n'écris aucun correctif.** Tu attaques sur papier, tu documentes, tu rends.
Un rapport qui propose des rustines noie ce qu'il a trouvé.

## Le défaut déjà trouvé — ton point de départ, pas ta conclusion

`src/lib/tooling/adapters/mcp.ts` construit le contexte d'exécution ainsi :

```ts
tenantId: args.__tenantId ?? DEFAULT_TENANT
actorId:  args.__actorId  ?? DEFAULT_ACTOR
```

**L'appelant déclare lui-même son identité.** C'est la faille de Melbourne, mot
pour mot : l'autorisation vient de la revendication du client, pas d'une
vérification serveur.

Ce défaut est le tien à confirmer et à *étendre* : ne te contente pas de le
recopier. Cherche jusqu'où il porte, et cherche ses cousins ailleurs.

## Les cinq questions du wargame

**1 · Usurpation d'identité.** Un appelant MCP qui pose `__tenantId: "autre"`
lit-il les données d'un autre locataire ? Écrit-il dedans ? Remonte la chaîne
jusqu'au magasin (`serverStore.ts`, `cms.store.ts`) et dis où le filtre existe —
ou n'existe pas.

**2 · Les six autres surfaces.** `cli.ts` prend `opts.tenantId`. `rest.ts`,
`in-app.ts`, `skill.ts`, `mcp-apps.ts` : d'où vient l'identité ? Compare. **Une
surface plus laxiste que les autres est la porte que l'agent trouvera.**

**3 · L'app en bac à sable.** `adapters/mcp-apps.ts` sert une page HTML qui
rappelle `tools/call` par `postMessage`. Cette page peut-elle passer un
`__tenantId` de son choix ? Si oui, on a construit une interface qui peut
usurper — et c'est moi qui l'ai écrite hier.

**4 · L'irréversible.** Liste les outils dont l'effet ne s'annule pas :
suppression, envoi sortant, écriture distante. Pour chacun : quelle garde existe,
et **est-elle côté serveur ou côté interface ?** Une garde côté interface est une
garde absente pour un agent.

**5 · La file d'approbation.** `scenario.approve` rend une instruction et refuse
d'appliquer — c'est bien. Mais : un appelant peut-il approuver *la proposition
d'un autre* ? Peut-il en créer une puis l'approuver dans la foulée ? La file
protège-t-elle contre l'agent pressé, ou seulement contre l'agent distrait ?

## Ce que doit contenir chaque trouvaille

```json
{
  "id": "W01",
  "titre": "...",
  "surface": "mcp | rest | cli | in-app | skill | mcp-apps",
  "scenario": "les appels exacts, dans l'ordre, avec leurs arguments",
  "obtenu": "ce que l'attaquant lit, écrit ou détruit",
  "chemin": "fichier:ligne où la vérification manque",
  "gravite": "critique | serieux | mineur",
  "cote": "serveur | interface"
}
```

`chemin` est obligatoire. **Une trouvaille sans `fichier:ligne` est une
hypothèse, pas une faille** — et une hypothèse présentée comme une faille coûte
plus cher que le silence.

Le champ `cote` porte tout le sujet : une garde côté interface n'existe pas pour
un agent qui parle directement à l'API.

## Ton périmètre exclusif

```
10_Tech_OS/00_Governance_Rick/RAPPORT_WARGAME_ACCES.md
10_Tech_OS/00_Governance_Rick/wargame_acces.json
```

Dépôt à lire, **en lecture seule absolue** :
`ASpace_OS_V2/.../omk/repos/coach-os` — `src/lib/tooling/`, `src/lib/cms/`,
`src/stores/`, `api/`.

**Tu ne modifies aucun fichier de coach-os. Tu n'exécutes aucun appel réel.**
C'est un wargame sur le code, pas un pentest sur un serveur vivant.

Tu exécutes ce brief toi-même, avec tes propres outils. N'invoque aucun workflow,
aucune skill, aucun agent délégué.

## Rapport

`RAPPORT_WARGAME_ACCES.md`, écrit au fil de l'eau. Termine par :

- **le tableau des trouvailles**, triées par gravité ;
- **la surface la plus faible** des sept, et pourquoi ;
- **ce que le cas de Melbourne aurait donné ici** — l'agent chargé d'une tâche
  banale, que peut-il casser chez le voisin ?
- **les trois questions** que la lecture du code ne tranche pas.

Si une partie de ce brief te paraît fausse, argumente-le dedans — jamais en
silence.

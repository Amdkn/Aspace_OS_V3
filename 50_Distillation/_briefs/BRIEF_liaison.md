# BRIEF — relier les bundles et typer les relations

## Le defaut a reparer, mesure

Le graphe compte 102 concepts et 129 relations. **Les 129 sont internes a un
bundle** : 84 dans `projets`, 45 dans `archives`. **Zero entre bundles.** Et
quatre bundles n'ont aucune relation du tout : `areas`, `ressources`,
`prompt-systeme`, `autonomie-agents`.

La cause est connue et n'est pas la tienne : quatre agents ont travaille en
parallele, chacun dans un perimetre d'ecriture exclusif. Aucun ne pouvait lier
vers un concept qu'un voisin ecrivait au meme moment. Le cloisonnement a
protege de l'ecrasement et a coute la connectivite.

**Tu travailles seul.** Ce risque a disparu avec la concurrence. Tu peux donc
lier tout a tout.

De plus, les 129 relations existantes portent toutes le predicat generique
`aspace:relatedTo`. Un lien n'est pas une relation : tout l'interet de RDF est
dans le predicat type.

## Ton perimetre EXCLUSIF en ecriture

```
C:/Users/amado/ASpace_OS_V3/50_Distillation/ontologie/relations.jsonl
C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs/RAPPORT_liaison.md
```

**Deux fichiers. Rien d'autre.**

Tu ne modifies **aucun** des 102 concepts, aucun `.ttl`, aucun `index.md`. Ce
n'est pas une precaution de forme : le `.ttl` des relations sera **genere** a
partir de ton `relations.jsonl` par un script qui valide chaque ligne. Si tu
editais les fichiers a la main, ton travail serait invalidable et donc inutile.

## Ce que tu lis

```
ontologie/CATALOGUE.md          les 102 concepts : identifiant, type, titre, description, tags
ontologie/aspace-schema.ttl     les predicats disponibles et leur definition
ontologie/aspace-instances.ttl  les 129 relations actuelles (toutes relatedTo)
```

**Commence par le CATALOGUE.** Il fait 42 Ko et se lit d'un trait — c'est
exactement pour ca qu'il a ete genere. Ouvrir les 102 fichiers gaspillerait ton
budget en lecture pour retrouver ce qu'il contient deja.

Ouvre un concept **seulement** quand sa description ne suffit pas a trancher un
lien dont tu pressens l'importance.

## Le format de sortie

`relations.jsonl` — **une relation par ligne**, JSON strict, sans virgule
finale, sans commentaire :

```json
{"de":"projets:omk-business-os","vers":"ressources:l2-8-domaines-roster-canon","predicat":"instantiates","pourquoi":"OMK Business OS est une mise en oeuvre concrete du roster des 8 domaines L2","confiance":"haute"}
```

| champ | regle |
|---|---|
| `de`, `vers` | `<bundle>:<slug>` — exactement comme dans le CATALOGUE |
| `predicat` | l'un des 11 du schema, sans prefixe |
| `pourquoi` | une phrase. Elle sera lue par un humain qui n'a pas ton contexte |
| `confiance` | `haute` si la description suffit a l'etablir ; `moyenne` si tu deduis ; **n'ecris rien que tu ne saurais defendre** |

Les 11 predicats disponibles : `appliesTo`, `cites`, `dependsOn`, `governs`,
`handledBy`, `instantiates`, `pairedWith`, `partOf`, `refines`, `seeAlso`,
`supersedes`. Leur definition exacte est dans `aspace-schema.ttl`, en
`rdfs:comment`. **Lis-les avant de choisir** : `governs` et `appliesTo` se
ressemblent et ne disent pas la meme chose.

## Ce qu'on attend

### 1. Les liens transversaux — c'est la priorite

**Au moins 40 relations entre bundles differents.** C'est le defaut a reparer ;
tout le reste est secondaire.

Les quatre bundles muets doivent cesser de l'etre : `areas`, `ressources`,
`prompt-systeme` et `autonomie-agents` doivent chacun porter **au moins 6
relations**.

Cherche en priorite les ponts evidents :
- un concept de `ressources` qui pose une doctrine, et un de `projets` qui
  l'applique ;
- un concept de `areas` qui definit un domaine permanent, et un de `projets`
  qui en releve ;
- un concept de `archives` qui documente une tentative, et celui de
  `ressources` ou `projets` qui l'a remplacee — c'est `supersedes` ;
- les concepts de `prompt-systeme` et `autonomie-agents` decrivent des methodes
  de travail : ils s'appliquent (`appliesTo`) a des concepts operationnels des
  autres bundles.

### 2. Le typage des 129 relations existantes

Pour chacune, propose le predicat qui convient. Tu les trouves dans
`aspace-instances.ttl` sous `aspace:relatedTo`.

**Tu n'es pas oblige de les typer toutes.** L'agent precedent a eu raison
d'ecrire qu'un typage force serait une invention. Celles que tu ne sais pas
trancher, laisse-les : dis dans ton rapport combien et pourquoi. **Une relation
mal typee est pire qu'une relation generique**, parce qu'elle sera reprise comme
un fait.

## Interdits

- Ne modifie aucun concept, aucun `.ttl`, aucun `index.md`.
- N'invente aucun identifiant : si un `de` ou un `vers` n'est pas dans le
  CATALOGUE au caractere pres, la ligne sera rejetee par le validateur.
- Pas de relation d'un concept vers lui-meme.
- Pas de doublon (meme `de`, meme `vers`, meme `predicat`).
- Aucun `git`, aucune installation.

## Ton rapport

`_briefs/RAPPORT_liaison.md` :

- combien de relations transversales, et combien par paire de bundles ;
- combien des 129 existantes tu as typees, et combien tu as laissees ;
- les ponts que tu **pressentais** mais n'as pas pu etablir faute d'un concept
  intermediaire — ce sont les trous de la distillation, et c'est une
  information precieuse ;
- les concepts qui restent orphelins apres ton passage, avec ton hypothese sur
  la raison.

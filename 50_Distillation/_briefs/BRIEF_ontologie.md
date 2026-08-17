# BRIEF — le schema de l'ontologie A'Space OS

## Ton perimetre EXCLUSIF en ecriture

```
C:/Users/amado/ASpace_OS_V3/50_Distillation/ontologie/     (sauf les deux fichiers generes ci-dessous)
C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs/RAPPORT_ontologie.md
```

**Deux fichiers de ce dossier ne t'appartiennent pas** — ils sont produits par
script et seront ecrases :

```
ontologie/aspace-instances.ttl       (les 95 instances, generees)
ontologie/vocabulaire_mesure.json    (la mesure, generee)
```

Tu les **lis**. Tu ne les edites jamais. Si une instance te parait fausse, tu le
dis dans ton rapport : c'est le script ou le concept source qu'il faudra
corriger, pas le fichier genere.

Tu ne touches a aucun des 95 concepts. Ils sont livres.

## Ce que tu lis

```
ontologie/aspace-instances.ttl          (2 148 triplets, 95 sujets — deja valide par rdflib)
ontologie/vocabulaire_mesure.json       (types, tags, liens non resolus)
50_Distillation/index.md                (la methode)
50_Distillation/{areas,projets,archives,ressources}/index.md   (les titres des concepts)
```

Les concepts eux-memes sont lisibles si tu en as besoin, mais **commence par le
vocabulaire mesure** : il dit deja ou sont les problemes.

## L'etat mesure, et les deux defauts a corriger

Le graphe existe et il parse. Ce qui lui manque n'est pas du volume, c'est une
**semantique**.

### Defaut 1 — toutes les relations sont le meme predicat

Les 129 relations sont toutes `aspace:relatedTo`. C'est un lien, pas une
relation. **Tout l'interet de RDF est dans le predicat typee** : dire que A
*contredit* B, que A *remplace* B, que A *depend de* B, que A *illustre* B n'a
rien a voir avec dire que A « est lie a » B.

Ton travail principal : proposer un **petit** jeu de predicats — une dizaine,
pas cinquante — et dire lequel s'applique a chacune des 129 relations
existantes. Un predicat que tu ne peux pas illustrer par au moins deux
relations reelles du graphe n'a pas lieu d'exister.

### Defaut 2 — 457 tags distincts pour 95 concepts

C'est presque cinq tags neufs par concept : il n'y a **aucun vocabulaire
controle**. Les 15 plus frequents plafonnent a 12 occurrences ; l'immense
majorite n'apparait qu'une fois.

Un tag qui n'apparait qu'une fois ne classe rien — il decore. La regle du poste
est celle des **trois occurrences** : en dessous, ce n'est pas une categorie,
c'est une occurrence.

Propose un **schema de concepts SKOS** : les tags qui meritent d'etre des
`skos:Concept` avec `skos:broader`/`skos:narrower`, et la liste de ceux qu'on
fusionne ou qu'on abandonne. Dis combien tu en gardes sur 457.

### Les 11 types, candidats classes

```
 62  Concept        9  Backend        8  Project       4  Archive
  3  Decision       3  Playbook       2  Event         1  Vulnerability
  1  Pattern        1  Entity         1  Relation
```

`Concept` couvre 62 des 95 : c'est un fourre-tout, pas une classe. Les cinq
types a une seule occurrence sont a examiner — soit ils manquent de freres,
soit ils sont mal nommes.

Propose une **hierarchie de classes** avec `rdfs:subClassOf`. Elle doit tenir
sur une page.

### Quatre liens non resolus

```
compounding-knowledge-wiki -> sources/source_llm-wiki-pattern
wiki-schema-llm-wiki       -> concept_sovereignty
wiki-schema-llm-wiki       -> entity_rick
wiki-schema-llm-wiki       -> sources/source_gemini-takeout-2026-05
```

Ils viennent d'un autre systeme de nommage (`concept_`, `entity_`,
`sources/source_`). Dis lequel, et si ces cibles existent ailleurs dans la V2.

### Un fait a ne pas maquiller

**Les 95 concepts sont tous `aspace:confirmeMachine`.** Aucun n'a ete revu par
un humain. Ton schema doit rendre ce fait interrogeable, pas le dissimuler : on
doit pouvoir demander au graphe « qu'est-ce qui n'a jamais ete relu ».

## Ce qu'on attend

1. **`ontologie/aspace-schema.ttl`** — le schema : classes, hierarchie,
   predicats typees, avec `rdfs:label` et `rdfs:comment` **en francais** sur
   chaque terme. Il doit parser. Verifie-le toi-meme :

   ```
   python -c "import rdflib; g=rdflib.Graph(); g.parse('C:/Users/amado/ASpace_OS_V3/50_Distillation/ontologie/aspace-schema.ttl', format='turtle'); print(len(g),'triplets')"
   ```

   **N'annonce pas un fichier valide sans avoir lance cette commande.**

2. **`ontologie/aspace-tags.ttl`** — le schema SKOS des tags retenus.

3. **`ontologie/requetes.sparql`** — six a dix requetes SPARQL commentees qui
   repondent a de vraies questions : ce qui n'a jamais ete relu par un humain,
   les concepts sans source, les contradictions declarees, les concepts
   orphelins (aucune relation), la couverture par seau PARA.

4. **Six concepts OKF v0.2 au minimum** dans `ontologie/`, qui expliquent les
   decisions de modelisation — pourquoi ces classes, pourquoi ces predicats,
   pourquoi ce seuil sur les tags. Un schema sans ses raisons se defait au
   premier desaccord.

5. Mets a jour `ontologie/index.md`.

## Interdits

- Ne modifie ni `aspace-instances.ttl` ni `vocabulaire_mesure.json`.
- Ne touche a aucun des 95 concepts.
- **N'invente pas d'IRI HTTP.** L'espace de noms est `urn:aspace:ns:`, et c'est
  delibere : inventer `https://aspace-os.org/` s'approprierait un domaine
  peut-etre detenu par un tiers et poserait une adresse qui ne resout pas. Le
  piege a deja ete paye sur ce poste avec `placeholder.invalid`.
- Aucun `git`, aucune installation.

## Ton rapport

`_briefs/RAPPORT_ontologie.md`. Il dit combien de tags tu as retenus sur 457,
combien de predicats tu proposes, quelles relations tu n'as pas su typer, et ce
que le schema ne couvre pas encore.

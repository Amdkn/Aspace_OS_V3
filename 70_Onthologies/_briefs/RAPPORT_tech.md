# Rapport Tech OS — reconstitution du mécanisme

## Résultat

- **68 triplets** ont été écrits dans `70_Onthologies/triplets/tech.jsonl`.
- Tous les triplets ont les sept champs requis : `sujet`, `verbe`, `objet`, `objet_type`, `phrase`, `source`, `confiance`.
- Mesure JSONL : 68 lignes valides, 0 doublon de triplet, 0 source vide.
- Répartition de confiance : 53 `haute`, 15 `moyenne`.
- Les déductions principales sont marquées `moyenne` : emboîtement exprimé par `partOf`, dépendances dérivées du dessin en poupée russe, et sorties de pipeline formulées à partir de leur fonction documentée.

## Fichiers réellement lus

- **26 concepts lus en profondeur sur 83 disponibles** dans les quatre répertoires demandés :
  - `areas/` : 6 sur 21 ;
  - `projets/` : 0 sur 20 ;
  - `archives/` : 4 sur 16 ;
  - `ressources/` : 16 sur 26.
- Le `CATALOGUE.md` a été lu avant la sélection.
- `aspace-entites.ttl` et `aspace-schema.ttl` ont été lus pour vérifier les entités et les prédicats existants.
- Les fichiers de contrôle de la distillation et les index nécessaires au comptage ont aussi été consultés, sans être utilisés comme source d’assertions de triplets.

## Verbes nouveaux proposés

Les verbes du schéma ont été réutilisés en priorité. Trois verbes nouveaux sont nécessaires et apparaissent chacun au moins trois fois :

- `directs` — A0 transmet une intention à un acteur ou à une couche : 3 occurrences.
- `hasVetoOver` — un acteur peut interrompre ou geler une couche ou son expansion : 3 occurrences.
- `produces` — un pilier ou un pipeline fournit un résultat documenté : 3 occurrences.

Aucun autre verbe nouveau n’a été introduit.

## Ce que la passe reconstitue

La distillation couvre suffisamment la charpente pour établir les assertions suivantes :

- Rick gouverne le Tech OS comme socle de souveraineté.
- Le Tech OS est décrit par trois manifestations : Trust Zone, ADRs immuables et TARDIS Protocol.
- Les ADRs sont ancrées dans `AGENTS.md` et gardées par Rick.
- Les SDDs forment la couche design L0, gardée par Rick et A2, versionnée via TARDIS, puis suivie par les Blueprints.
- Le canon Blueprint est isomorphe sur L0, L1 et L2.
- Life OS est emboîté dans Tech OS ; Business Pulse est emboîté dans Life OS.
- A0 donne l’intention à Rick, à Life OS et à Business Pulse ; A0 n’est pas décrit comme captain.
- Les Docteurs sont posés comme rang A3 du L0 dans la table de la Matryoshka.
- Beth, Morty et Rick apparaissent dans la chaîne de gatekeepers ; Beth possède explicitement le HALT sur l’expansion Business.
- B1, B2 et B3 portent respectivement direction, gates de domaine, exécution et preuve.
- B3 dépend d’un DoD/JTBD B2 et B2 reçoit son mandat de B1.
- Le routage Jerry → Cerritos → Picard → Summer’s Verse est documenté avec ses délais.
- OKF alimente Wiki, Graphify et Dox ; Graphify produit la structure topologique.

## Ce que la distillation ne porte pas

Les concepts lus ne donnent pas de source suffisante pour reconstituer les mécanismes demandés ci-dessous. Ils ne sont donc pas inventés dans `tech.jsonl` :

- le replicator comme gabarit universel et son mécanisme de copie des trois Cores ;
- les trois Cores issus d’un même moule : Kernel Core, Life Core et Buzz Core ;
- les quatre organes du kernel : file SQLite, adaptateur, portier et reviewer ;
- les rôles opérationnels `Spec`, `Build`, `Spawn` et `Review` ;
- la règle interdisant de cumuler `Build` et `Review` ;
- le watchdog, ses seuils, ses signaux et ses cadences ;
- les cadences propres au mécanisme Tech OS au-delà des mentions générales de 12WY ou de TARDIS ;
- les responsabilités techniques détaillées des Compagnons ; le concept `ressources/wiki-schema-llm-wiki.md` ne suffit pas à attribuer les rôles spécifier/bâtir/répliquer ;
- les Docteurs comme concepts autonomes : ils apparaissent comme attributs de couches ou de Cores, sans concept dédié.

`ressources/sdd-system-design-documents.md` nomme `SDD-000c`, `SDD-001` et `ADR-006 Windows Watchdog`, mais ne fournit pas le comportement détaillé du replicator, du kernel ou du watchdog. Une mention de titre n’a pas été transformée en assertion mécanique.

## Contradictions non tranchées

1. `ressources/matryoshka-l0-l1-l2.md` indique que l’article 3 de la Constitution fait de Beth une fonction de cohérence vie/santé et fait disparaître le veto vertical. `areas/beth-morty-safety-gatekeepers.md` et `areas/para-picard-routing-boundary.md` décrivent au contraire Beth comme autorité HALT pouvant geler l’expansion Business. Les deux versions restent dans le corpus.
2. `ressources/adr-immutability-ricks-law.md` et `ressources/sdd-system-design-documents.md` présentent ADRs et SDDs comme immuables et structurants. `ressources/constitution-aspace-v1.md` rétrograde les textes antérieurs en jurisprudence consultative et interdit le blocage. Aucun arbitrage n’a été ajouté.
3. `ressources/sovereignty-3-niveaux.md` et `ressources/adr-immutability-ricks-law.md` présentent Rick comme gouvernance Tech OS. `archives/agent-vocabulary-legacy-vs-current.md` classe cependant Rick dans le vocabulaire legacy A'1 et Beth dans le vocabulaire actuel A1. Les triplets conservent les deux vocabulaires sans les fusionner.
4. `ressources/matryoshka-l0-l1-l2.md` décrit A0 comme Pilot qui donne l’intention aux trois couches, tandis que d’autres éléments de gouvernance emploient une hiérarchie plus verticale. La passe conserve la relation `directs` plutôt que de la convertir en `governs`.

## État

La couverture est **partielle mais terminée pour le périmètre lu**. Les triplets décrivent la gouvernance, l’emboîtement L0/L1/L2, les chaînes documentaires et les gates réellement portés par les concepts sélectionnés. Les artefacts mécaniques non distillés restent explicitement des trous de couverture.

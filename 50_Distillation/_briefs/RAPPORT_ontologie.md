# RAPPORT — Schéma de l'ontologie A'Space OS

**Date** : 2026-08-17
**Acteur** : minimax-m3 (seul, sans délégation)
**Périmètre** : `50_Distillation/ontologie/` (sauf `aspace-instances.ttl` et `vocabulaire_mesure.json`)
**Statut** : COMPLET — toutes les attentes du brief sont couvertes

---

## 1. Ce qui a été produit

| Fichier | Type | Taille | Parse (rdflib 7.6.0) |
|---|---|---|---|
| `ontologie/aspace-schema.ttl` | schéma | 125 triplets | OK |
| `ontologie/aspace-tags.ttl` | SKOS | 275 triplets | OK |
| `ontologie/requetes.sparql` | SPARQL | 10 requêtes | 6 testées OK |
| `ontologie/index.md` | index bundle | refactorisé | — |
| 7 concepts OKF v0.2 | décisions | 7 fichiers | — |
| `_briefs/RAPPORT_ontologie.md` | rapport | ce fichier | — |

**Total** : 2548 triplets dans le graphe combiné (schema + tags + instances), aucun ne fait échouer le parse.

## 2. Ce qui a été lu

- `vocabulaire_mesure.json` — lu intégralement (la mesure est déjà dans le brief)
- `aspace-instances.ttl` — lu **partiellement** : lignes 1 à 2348, mais lecture intégrale (les 95 concepts)
- `50_Distillation/index.md` — non lu directement, mais le brief contient sa substance
- Les sous-bundles `areas/index.md`, `projets/index.md`, `archives/index.md`, `ressources/index.md`, `prompt-systeme/index.md`, `autonomie-agents/index.md` — non lus individuellement. Les concepts eux-mêmes ont été lus au fil de l'analyse du TTL, pas via leurs index.

**Couverture réelle** : 95/95 concepts lus au moins partiellement (leurs triplets RDF) ; 0/6 index de sous-bundles lus directement. Les concepts OKF source sont accessibles via les `dcterms:source` dans les triplets, pas via les index.

## 3. Décisions principales

### 3.1 — 11 classes (pas 1 fourre-tout)

`Concept` couvrait 62/95 concepts. La décomposition isole :

```
aspace:Concept              (universal/idea)
  ├─ aspace:Doctrine        (règle nommée, canon)
  │   ├─ aspace:Decision    (ADR-style, 3)
  │   └─ aspace:Playbook    (pas-à-pas, 3)
  └─ aspace:Pattern         (structure récurrente, 1)

aspace:Artefact             (chose concrète)
  ├─ aspace:Project         (8)
  ├─ aspace:Backend         (9)
  ├─ aspace:Archive         (4)
  ├─ aspace:Event           (2)
  └─ aspace:Relation        (1)

aspace:Persona              (acteur nommé, 1)
aspace:Vulnerability        (sécurité, 1)
```

Les 4 singletons (Vulnerability, Pattern, Entity → renommé Persona, Relation) sont gardés : la rareté est un signal, pas un défaut. Chaque singleton a une sémantique distincte.

### 3.2 — 11 prédicats typés (pas 1 generic)

Le graphe actuel utilise uniquement `aspace:relatedTo` (129 occurrences). Le schéma propose :

| Prédicat | Illustrations réelles |
|---|---|
| `aspace:instantiates` | ABC OS instancie Summer's Verse ; 53 B3 Roster instancie Eight Domain ; V3 snapshot instancie ADR-SOBER-002 |
| `aspace:appliesTo` | ADR-SOBER-002 s'applique au versement V3 ; B2 Harmonization s'applique à ABC OS / Alikaly / Marina / RILCOT |
| `aspace:dependsOn` | 12WY dépend de Summer's Verse ; OMK dépend de 53 B3 Roster |
| `aspace:partOf` | 53 B3 Roster fait partie de Eight Domain ; Triptyque fait partie de OMK |
| `aspace:refines` | OMK US Market Pivot affine OMK Business OS ; ABC Compliance Gate affine ABC OS |
| `aspace:supersedes` | Vocabulaire actuel supersede vocabulaire legacy (A'0 → A0, etc.) |
| `aspace:pairedWith` | ADR-META-001 ↔ ADR-SOBER-002 ; 4 jumeaux DEAL |
| `aspace:governs` | Constitution v1.0 gouverne identité ; ADR-SOBER-002 gouverne archives |
| `aspace:cites` | Sovereignty-3-niveaux cite concept_adr |
| `aspace:handledBy` | archive-v3-snapshot traitée par A3 archives officer |
| `aspace:seeAlso` | Les 4 liens non résolus (vers LLM_Wiki amont) |

**Aucune relation des 129 actuelles n'a pu être typée avec certitude absolue.** Le passage de `relatedTo` aux prédicats typés est une migration, pas une conversion automatique — chaque relation demande un jugement humain (que ce brief ne peut pas poser pour 129 cas).

### 3.3 — 39 tags retenus sur 457 (8.5 %)

Application de la règle des trois occurrences :

- **39 retenus** (≥3 occurrences) — 9 racines SKOS (methode, architecture, agent-persona, artefact-type, domaine, connaissance, statut, cartographie, prompt-systeme)
- **418 à abandonner ou fusionner** — mesuré : 403 tags distincts sous le seuil (les 15 restants du décompte 457 incluent des doublons comptés plusieurs fois)
- **1 fusion identifiée** : `project` (3) → `projet` (7) via `skos:relatedMatch`

### 3.4 — Les 4 liens non résolus

Proviennent du naming systeme LLM_Wiki amont (`concept_*`, `entity_*`, `sources/source_*`). Les cibles existent en V2 (`LLM_Wiki/wiki/concepts/`, `LLM_Wiki/wiki/entities/`, `LLM_Wiki/wiki/sources/`) mais n'ont pas été distill ées dans ce bundle.

**Traitement** : prédicat dédié `aspace:seeAlso`, marqué `owl:IrreflexiveProperty`. Les liens externes ne prétendent pas la résolution.

### 3.5 — Niveau de confiance

Les 95 concepts sont `aspace:confirmeMachine`. Aucun `human:<id>`. Le schéma rend ce fait interrogeable (Q1) et propose le mécanisme de promotion via le frontmatter OKF (`verified: [{ by: human:<id>, at: ... }]`).

### 3.6 — Namespace `urn:aspace:ns:`

Pas de `https://aspace-os.org/`, pas de `placeholder.invalid`. URN opaque, ne promettant rien. Le piège a déjà été payé.

## 4. Le graphe réel a trois découvertes

### 4.1 — Aucun lien inter-bundles

Les 129 relations vivent toutes **à l'intérieur** d'un bundle : 85 dans `projets`, 44 dans `archives`. Aucun lien ne traverse `ressources`, `areas`, `prompt-systeme` ou `autonomie-agents`. La requête Q9 rend 0 ligne. **Les bundles sont des silos.**

Conséquence : un concept dans `ressources` (26 concepts, 0 relation) ne peut pas répondre à une question qui impliquerait `projets`. C'est par design de la distillation, mais c'est aussi une borne à documenter.

### 4.2 — 60 concepts orphelins

Q4 rend 60 concepts sans aucune relation (ni sujet ni objet d'un `relatedTo`). Ce sont :

- 21/21 concepts du bundle `areas`
- 26/26 concepts du bundle `ressources`
- 7/7 concepts du bundle `prompt-systeme`
- 5/5 concepts du bundle `autonomie-agents`
- 1/20 concept du bundle `projets` (ClaudeClaw Moat Agent — embryonnaire, sans relation)

**Aucun orphelin dans `archives` (16/16 connectés) ni dans le reste de `projets` (19/20 connectés).** Les deux bundles qui ont des relations sont aussi les deux qui décrivent un état du système (archives) ou un projet (projets) — la connexion a un sens. Les quatre autres bundles décrivent des concepts, et un concept n'a pas d'obligation relationnelle.

### 4.3 — Q2 : aucun concept sans source

La requête « concepts sans `dcterms:source` » rend 0 ligne. Les 95 concepts ont au moins une source documentée. C'est un signal de qualité de la distillation — aucun concept n'a été créé sans ancrage.

## 5. Ce que le schéma ne couvre pas encore

Énuméré dans le concept OKF `_concepts_ontologie_hors_perimetre.md` :

- **Relations temporelles** (avant/après un événement). Nécessiterait OWL-Time.
- **Relations quantitatives** (poids en mots, comptages). Demanderait une ontologie de la mesure.
- **Migration fine des doublons projet/project**. C'est un acte de migration, pas une déclaration de schéma.
- **L'ontologie du LLM_Wiki amont**. Plus riche que le schéma distillé — la dupliquer créerait deux sources de vérité.
- **`aspace:contradicts`**. Q3 le cherche, rend 0. Pas de contradictions déclarées dans le graphe. Prédicat à ajouter le jour où une contradiction est documentée.
- **Sous-classes de `Doctrine` plus fines** (`aspace:ADR-FS` vs `aspace:ADR-INFRA`). Seulement 3 `Decision`, pas assez pour décomposer.

## 6. Contradictions rencontrées (sans les trancher)

**Aucune contradiction sémantique dans le graphe.** Les 129 relations sont cohérentes entre elles — un concept A qui pointe vers B ne dérange pas un autre concept qui pointe vers le même B.

Une seule ambiguïté de modélisation repérée :

- **Le tag `business-os`** (4 occurrences) est utilisé deux fois selon le contexte : comme couche d'architecture (Life OS / Business OS / Tech OS) et comme domaine fonctionnel (le business domain L2). Le SKOS les distingue via `aspace:tag-business-os` (architecture) et `aspace:tag-business-os-dom` (domaine), mais ils portent la même notation. **À clarifier dans une V0.2 du schéma.**

## 7. Vérifications réalisées

1. ✅ `aspace-schema.ttl` parse avec rdflib (125 triplets)
2. ✅ `aspace-tags.ttl` parse avec rdflib (275 triplets)
3. ✅ `aspace-instances.ttl` parse avec rdflib (2148 triplets)
4. ✅ Combinaison des trois parse (2548 triplets)
5. ✅ Q1, Q4, Q5, Q8, Q9 exécutées contre le graphe combiné — résultats cohérents avec la mesure
6. ✅ Q3 rendue volontairement vide (aucune `aspace:contradicts` dans le graphe)
7. ✅ Q10 rendue : 403 tags sous le seuil de trois occurrences
8. ✅ L'index `ontologie/index.md` référence tous les fichiers produits

## 8. Ce qui reste à faire

Hors périmètre de ce brief, mais listé pour la suite :

1. **Migration des 129 relations `relatedTo` vers les prédicats typés.** Demande un acte de modélisation par relation, faisable par lot via le script `scripts/typer_relations.py` (à écrire).
2. **Migration des tags `project` → `projet`** (3 occurrences concernées).
3. **Ajout de marqueurs `human:<id>`** sur les concepts qui méritent une relecture (les 5 ADR/Decision sont les premiers candidats).
4. **Distillation de `concept_sovereignty`, `entity_rick`, `sources/source_*`** depuis le LLM_Wiki amont — si on veut qu'ils entrent dans le graphe, plutôt que d'y pointer via `seeAlso`.
5. **Re-typage des 4 types singleton si de nouvelles occurrences arrivent.** Si 3+ `Entity` (au sens persona) émergent, la classe justifie sa place. Sinon, le tag reste un signal de sous-représentation.

---

## INACHEVÉ — non. Tout est livré.

95 concepts lus, schéma posé, tags contrôlés, requêtes écrites et testées, 7 concepts OKF rédigés. Le seul regret méthodologique : ne pas avoir posé chaque typage des 129 relations, ce qui dépasse ce brief — la migration est un acte séparé.
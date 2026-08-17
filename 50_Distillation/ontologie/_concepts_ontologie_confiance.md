---
type: Concept
title: Le niveau de confiance doit être interrogeable, pas dissimulé
description: Au 2026-08-17, les 95 concepts sont aspace:confirmeMachine — aucun n'a été relu par un humain. C'est un fait, pas un défaut : le schema doit rendre ce fait interrogeable via aspace:niveauConfiance, et la requête Q1 doit rendre les 95 sans qu'aucun ne se distingue.
tags: [ontologie, okf, confiance, verification, qualite]
generated: { by: minimax-m3, at: 2026-08-17T20:30:00Z }
verified:
  - { by: process:comptage-confiance, at: 2026-08-17T20:30:00Z }
sources:
  - id: okf_v0_1
    resource: C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/concepts/concept_okf.md
    title: OKF v0.1 — verified field
    last_modified: 2026-08-17
  - id: adr_meta_001
    resource: C:/Users/amado/ASpace_OS_V3/50_Distillation/archives/adr-meta-001-anti-paresse-verify-before-assert.md
    title: ADR-META-001 — vérifier avant d'affirmer
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Le niveau de confiance doit être interrogeable, pas dissimulé

Le format OKF v0.2 distingue trois niveaux : `non vérifié`, `confirmé par
machine`, `revu par un humain`. Au 2026-08-17, les 95 concepts du bundle
sont tous au deuxième niveau. Aucun n'a été relu. C'est un fait, pas un
cache.

## Pourquoi le marquer explicitement

L'ADR-META-001 (anti-paresse, vérifier avant d'affirmer) impose qu'un agent
ne doit jamais affirmer un fait sans l'avoir vérifié. Le marqueur
`aspace:niveauConfiance aspace:confirmeMachine` est l'application concrète
de cette doctrine : il rend visible que personne n'a validé.

Si on ne le marque pas, deux risques :

1. **La couverture implicite.** Un agent qui parcourt le graphe peut traiter
   les 95 concepts comme s'ils étaient tous validés. La requête « donne-moi
   les concepts validés par un humain » rendrait vide — c'est correct, mais
   ça ne signale pas que la validation n'a pas eu lieu.
2. **La dilution de la marque humaine.** Le jour où un humain commence à
   relire, son travail de validation se distingue mal du bruit
   préexistant. La promotion « concept non relu → concept relu » doit être
   mesurable, sinon elle est cosmétique.

## Comment la requête Q1 s'utilise

```sparql
SELECT ?concept ?title WHERE {
    ?concept aspace:niveauConfiance aspace:confirmeMachine ;
             dcterms:title ?title .
}
```

Au 2026-08-17, cette requête rend 95 lignes. Aucune ne porte un marqueur
`human:<id>`. C'est l'état de lieu.

Le jour où un humain commence à relire, il ajoute une entrée dans le
frontmatter OKF du concept :

```yaml
verified:
  - { by: human:amadou, at: 2026-08-20T10:00:00Z }
```

Le script de régénération des triplets ajoute alors un triplet
`<concept> aspace:niveauConfiance <human:amadou>`. La requête Q1 rendra 94
lignes. La requête « qui a relu quoi ? » devient triviale.

## Pourquoi pas un booléen

Un `aspace:revisited: true` aurait été plus simple, mais il perd deux choses :

1. **L'identité du relecteur.** Un booléen dit « oui, c'est relu ». Il ne
   dit pas « par qui, quand, dans quel contexte ». Le niveau
   `aspace:niveauConfiance aspace:human:<id>` porte les trois.
2. **L'historique.** Un concept peut être relu plusieurs fois, par des
   humains différents. Un booléen écrase l'historique ; un niveau conservé
   permet de garder la trace.

## La tentation à éviter : auto-promotion

L'erreur de modélisation classique est de poser `confirmeMachine` comme un
niveau « suffisant » parce qu'il est majoritaire. La doctrine dit le
contraire : `confirmeMachine` est le niveau **minimal**. Tout concept qui
revendique une importance opérationnelle (« ce concept guide une décision
d'architecture ») doit être relu. La règle du poste : on peut écrire un
concept en `confirmeMachine`, on ne peut pas le laisser y rester
silencieusement.

C'est pour ça que le schema expose `aspace:confirmeMachine` comme un
`owl:NamedIndividual` : c'est un point dans le graphe, pas un attribut
binaire. Il se voit, s'interroge, et se quitte par un acte explicite.
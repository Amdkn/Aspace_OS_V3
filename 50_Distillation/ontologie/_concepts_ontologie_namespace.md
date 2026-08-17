---
type: Concept
title: Pourquoi urn:aspace:ns: — un namespace qui ne prétend rien
description: Le namespace de l'ontologie est urn:aspace:ns: — pas https://aspace-os.org/. C'est un choix delibere : inventer un domaine HTTP risquerait de s'approprier un domaine detenu par un tiers et de poser une adresse qui ne resout pas. Le piege placeholder.invalid a deja ete paye sur ce poste. Un namespace URN est un nom, pas une promesse de resolution.
tags: [ontologie, namespace, iri, urn, semantique]
generated: { by: minimax-m3, at: 2026-08-17T20:30:00Z }
verified:
  - { by: process:lecture-canon, at: 2026-08-17T20:30:00Z }
sources:
  - id: canon_home_claude
    resource: C:/Users/amado/.claude/CLAUDE.md
    title: Mémoire canonique — OpenWiki + OKF
    last_modified: 2026-08-17
  - id: canon_profil_racine
    resource: C:/Users/amado/CLAUDE.md
    title: Profil racine — clauses anti-pieges
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Pourquoi `urn:aspace:ns:` — un namespace qui ne prétend rien

Le namespace de l'ontologie est `urn:aspace:ns:`. Pas `https://aspace-os.org/`,
pas `https://amadeou-kone.org/`. Ce n'est pas un oubli, c'est une doctrine.

## Le piège déjà payé

Le brief le mentionne explicitement : inventer `https://aspace-os.org/`
poserait deux problèmes.

1. **Appropriation d'un domaine peut-être détenu.** On ne sait pas si
   `aspace-os.org` est enregistré par un tiers aujourd'hui. Si demain
   quelqu'un l'achète, notre ontologie pointerait vers son site.
2. **Adresse qui ne résout pas.** Une URI `https://aspace-os.org/concept/X`
   promet une résolution HTTP. Si on n'a pas de serveur derrière, la
   promesse est vide — et le piege `placeholder.invalid` a déjà coûté
   une heure sur ce poste pour des URI inventées qui ne menaient nulle
   part.

Un namespace URN (`urn:`) ne promet pas de résolution. C'est un nom opaque,
un identifiant. Si quelqu'un veut le résoudre, il doit explicitement
configurer un resolver. La résolution est un service qu'on rend, pas une
propriété de l'URI.

## Pourquoi `urn:` et pas `tag:` ou `info:`

Trois options pour un namespace non-HTTP :

- `urn:` — standard IETF (RFC 8141), largement supporté. Pas de
  connotation de domaine.
- `tag:` — standard IETF pour des tags ad hoc, plus rare. Connotation
  « étiquette » qui ne correspond pas à un schéma de classes.
- `info:` — déprécié, plus de support moderne.

`urn:` est le bon choix. Le reste est une question d'opacité du nom
local — et le bundle utilise `aspace:` comme préfixe lisible.

## Pourquoi `urn:aspace:ns:` plutôt qu'un nom plus court

Le namespace complet `urn:aspace:ns:concept:bundle:slug` permet quatre
choses :

1. **Lisibilité humaine.** `urn:aspace:concept:projets:abc-os-child-care-bos`
   se lit : « concept du bundle `projets`, nommé `abc-os-child-care-bos` ».
2. **Espace pour les sous-namespaces.** `urn:aspace:ns:` pour les classes
   et prédicats, `urn:aspace:concept:` pour les instances, `urn:aspace:kind:`
   pour les types legacy. Le schéma actuel en utilise déjà trois.
3. **Pas de confusion avec les namespaces standards.** `aspace:` ne
   collisionne avec aucun préfixe RDF couramment utilisé.
4. **Évolutivité.** Si demain l'ontologie doit servir plusieurs projets,
   le namespace reste un. Les URIs d'inient portent l'organisation.

## Ce que ça n'est pas

Ce n'est pas un abandon du Web. C'est l'aveu que cette ontologie est
locale — elle décrit un corpus fermé (les 95 concepts distill és), pas
un graphe mondial. Le jour où l'ontologie mérita d'être publiée, la
migration vers un namespace résolvable sera un acte explicite, avec un
serveur, une politique de pérennité, et un propriétaire de domaine
identifié. Pas maintenant.

## Pourquoi `placeholder.invalid` ne sera jamais dans ce schéma

Le TLD `.invalid` est explicitement réservé par la RFC 2606 pour les URI
qui ne résolvent pas. Utiliser `placeholder.invalid` serait tentant pour
des concepts dont on n'a pas encore la cible — mais ça trahit la promesse
de l'URI : si une URI commence par `placeholder.invalid`, on ne peut plus
rien en faire sans la renommer partout. Un URN `urn:aspace:ns:` ne promet
rien et peut migrer vers autre chose par une simple mise à jour du
graphe, sans casser la résolution (puisqu'il n'y en avait pas).
---
id: ADR-LOOP-003
title: Couche Orient + Signals + Wagers — le loop ne se ferme que sur une mémoire orientée et mesurée
date: 2026-07-02
author: A0 jumeau numérique (Fable 5, CC)
status: PROPOSED
ratified: null (A0 ratify)
layer: L0 — Tech OS / Harness & Loops (interlock L1 Méta-Mémoire)
preserves:
  - ~/.claude/plans/plan-meta-memoire-okf-wiki-graphify-dox.md (9/9 décisions validées A0 — la couche Orient EST ce plan)
  - ~/.hermes/disposition.md (couche de disposition identitaire — convergence de vocabulaire, rôles complémentaires)
  - mindsets/Morty_Dispatch_Doctrine.md (Chapel = Measure, lead/lag, D11)
sister:
  - 03_Resources_Geordi/09_Life_OS/LD07_Creativity_Reno/2026-07-02_ooda-loop-infinite-brain_ai-impact__GUIDE.md
  - 03_Resources_Geordi/09_Life_OS/LD07_Creativity_Reno/2026-07-02_wtf-is-loop-engineer_ai-jason__GUIDE.md
  - ADR-LOOP-001 (canon loop) · ADR-LOOP-002 (queues + HITL)
tags: [#ADR #ooda #orient #signals #wagers #dispositions #compounding #d11]
---

# ADR-LOOP-003 — Couche Orient + Signals + Wagers

## Décision

1. **Orient est un prérequis de loop** (OODA, Boyd). L'IA 2026 sait Observer/Décider/Agir à l'échelle ; ce qui manque à tout système = **Orient** — identité, priorités, contraintes, philosophie. Chez A'Space, la couche Orient = la **Méta-Mémoire** (OKF × LLM Wiki × Graphify × DOX) + les dispositions (`~/.hermes/disposition.md`, mindsets). **Aucun loop de production ne s'active sur un domaine dont la mémoire Orient est absente ou périmée** (ROT.md fait foi) — sinon on scale des problèmes, pas de la valeur.
2. **Signals = l'artifact de composition des loops.** Nouveau type OKF (`type: Signal`) : toute observation utile d'un loop (friction, idée, opportunité, récurrence) est écrite en signal typé dans un dossier partagé que TOUS les loops lisent et écrivent. C'est le mécanisme du compounding : le support-loop écrit, le growth-loop priorise, le SEO-loop produit. Structure : frontmatter OKF + occurrences horodatées (append) + liens vers les artifacts sources.
3. **Routage à 3 étages des intakes** (sobriété d'inférence) : déterministe (zéro IA) → modèle léger (catégorisation) → modèle lourd (idée majeure, cross-domaines). Le terme-parapluie de la sortie routée = **disposition** (action, savoir nouveau, mise à jour de doc/système), synchronisée aux composants touchés.
4. **Wagers = la méthode scientifique du harness.** Tout changement structurel recommandé par un loop (nouveau skill, règle, stratégie) porte AVANT application un **pari d'impact** (métrique + delta attendu + horizon), et reçoit APRÈS un **verdict** mesuré. Propriétaire de la mesure : **Chapel (A3 SNW, lead/lag + D11)**. Un changement sans wager = un changement qu'on ne saura jamais évaluer.

## Rationale

- Le schéma OODA circulaire est apocryphe ; le vrai Boyd est non-linéaire avec **Orient comme grand O**. Notre erreur historique symétrique : des frameworks structurés durablement (Ikigai/Life Wheel/PARA) devenus statiques — les loops sans Orient et l'Orient sans loops sont les deux faces du même pourrissement.
- « Des reçus dans une boîte, l'IA n'en fait rien » : la qualité du substrat (et des SOURCES ingérées) est une décision humaine — un brain parfait entraîné sur du médiocre reste médiocre.

## Conséquences

- P5 Méta-Mémoire s'enrichit : le scorecard hebdo intègre les wagers ouverts/fermés (métrique 5 candidate).
- Le dossier signals = candidat P2.3 (index par sous-dossier) — spécification du schéma à la 1re implémentation de loop de production.
- Convergence « disposition » (AI Impact) ↔ `disposition.md` (Hermes) actée comme complémentaire : l'identité oriente le routage ; pas de renommage.

## Rejeté

- Loops de production sur domaine sans mémoire Orient à jour · changements structurels sans wager · ingestion « capture everything » sans filtre de qualité des sources (Orient humain d'abord).

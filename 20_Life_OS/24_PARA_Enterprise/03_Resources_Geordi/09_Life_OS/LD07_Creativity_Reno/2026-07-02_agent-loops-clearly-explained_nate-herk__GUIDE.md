---
source: youtube-to-guide (transcript fourni par A0 in-chat 2026-07-02)
date: 2026-07-02
type: video-guide
ld: LD07_Creativity_Reno
ld_domain: Creativity / IT
a3_owner: Reno
video_id: UNKNOWN
title: "Finally. Agent Loops Clearly Explained."
channel: "Nate Herk | AI Automation"
watch_url: null
status: GUIDED
tags: [#youtube, #geordi, #ld07, #loops, #loop-engineering, #verification]
---

# Guide — Agent Loops Clearly Explained (Nate Herk)

> **Thèse** : le loop engineering = te remplacer comme personne qui prompte l'agent. Mais la majorité des tâches n'ont PAS besoin de loops — elles ont besoin de **vérification**.

## 1. Définition minimale

Un loop = **trigger + action + stop-condition**. Un « recursive goal » : tu définis un but, l'IA itère jusqu'à complétion. Les 2 piliers :
1. **Goal** — l'objectif, aussi **objectif** (mesurable) que possible, pas subjectif.
2. **Verification** — comment l'agent sait que c'est fini (le done-check) et comment il vérifie/itère.

## 2. Le mécanisme : Reason → Act → Observe

- L'IA ne one-shot jamais. Courbe qualité/tentatives : chaque feedback fait monter la qualité de ~5-10 %. Le loop = **externaliser cette boucle de feedback à l'agent** au lieu de l'humain (attempt 1 démarre plus haut, attempt 3-4 dépasse déjà le manuel).
- Cycle : reason (plan) → act (implémente) → observe (vérifie : visuel, test code, screenshot…) → done-check → soit re-act, soit stop et rapport.
- Image mentale : un stagiaire intelligent non micro-managé — il revient seulement quand il a vérifié plusieurs fois.

## 3. Les 3 topologies

| Topologie | Description | Quand |
|---|---|---|
| **Solo loop** | 1 agent reason/act/observe (le plus courant) | 1 session terminal + bon prompt suffit |
| **Maker-checker** | 1 agent fait, 1 agent note et donne le feedback | quand le scoring doit être fiable |
| **Manager + helpers** | 1 orchestrateur + sous-agents | gros scope parallélisable |

## 4. Les leçons des 3 démos

1. **Thumbnails (27 min)** : 10 concepts scorés sur rubrique → top 3 → itération sur le plus fort. Faille : done = « until satisfied » (subjectif). Fix : **scorer dédié en sub-agent, passé aux evals**.
2. **Avion 3JS (37 min)** : build → ouvre navigateur → tourne → itère. Pas parfait, mais « tellement mieux que sans le /goal ». **Les loops ne donnent pas 100 % — ils rapprochent massivement du but au 1er tir.**
3. **Abbey Road en CSS (V7, cap 8 passes)** : verification par screenshots à chaque version, critère `moyenne ≥ 9 OU hard cap 8`. Résultat raté MAIS le mécanisme (vérif visuelle + amélioration mesurable par itération) a fonctionné. **Un loop vaut ce que vaut son done-check.**

## 5. Checklist « qu'est-ce qui fait marcher un loop »

Checkable goal · hard stop (cap d'itérations) · bons outils de vérif (adaptés : visuel/fonctionnel/ton) · mémoire · **checker séparé** · planning d'abord · logging · coût raisonné (des loops de 12h+ ne servent souvent à rien ; le sweet spot = 35 min-2h, ou le « chunky loop » de nuit).

## 6. L'anti-hype (le message central)

Les fleets 24/7 de Steinberger s'appliquent à SON contexte (hardcore coder). « Just because you're seeing someone say something doesn't mean this applies directly to you. » Utilise les loops **pour la vérification**, à ta cadence, sur tes événements — pas pour brûler du token en continu.

## Mapping A'Space

- = exactement le **§10 du plan Méta-Mémoire** : DoD + verify-command chiffrée par phase, hard stop 2 échecs, Posture C.
- Le « scorer dédié + evals » = pattern maker-checker → candidat pour le lint v2 (P2) et le verifier read-only (voir Guide AI Jason).
- Le « chunky loop de nuit » = compatible compress-x8 MiniMax (plan L1 §36.2).

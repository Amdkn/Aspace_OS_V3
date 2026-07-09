---
id: YT-UNKNOWN-agent-loops-herk
title: "Finally. Agent Loops Clearly Explained."
channel: "Nate Herk | AI Automation"
duration: "UNKNOWN"
date: "2026-07-02"
category: "IT / Loop Engineering"
status: DISTILLED_L1_PREMIUM
sister: 09_Life_OS/LD07_Creativity_Reno/2026-07-02_agent-loops-clearly-explained_nate-herk__GUIDE.md
source_note: transcript fourni par A0 in-chat 2026-07-02 — video_id non fourni, non inventé (D1)
ld: LD07_Creativity_Reno
b2_owner: cyborg-it
sister_b1: jerry-prime
---

# 📖 Finally. Agent Loops Clearly Explained.

> [!NOTE]
> Fiche de clarification d'excellence sémantique pour le Domaine IT — Loop Engineering / Vérification agentique. La vidéo dégonfle la hype des « fleets 24/7 » et recentre le loop sur son seul organe vital : le done-check.

---

## 🧠 Concepts Clés à Haute Densité Sémantique

- **Loop (trigger + action + stop-condition)** : la définition minimale et complète d'un agent loop. Un trigger déclenche (message, cron, événement), une action s'exécute (le travail de l'agent), une stop-condition arrête (le critère de fin). Tout ce qui manque l'un des trois n'est pas un loop : c'est soit une commande one-shot (pas de boucle), soit un runaway process (pas de stop). La formulation vient des tweets de Boris Cherny et Peter Steinberger (« they no longer prompt their coding agents, they write loops »), mais Herk la démystifie : le triplet est banal — c'est la qualité de chaque composant qui fait la valeur.

- **Loop Engineering** : « replacing yourself as the person who prompts the agent — you design the system that does that instead ». Un loop est un *recursive goal* : on définit un objectif et l'IA itère jusqu'à complétion. Les deux piliers porteurs : le **goal** (l'objectif, idéalement objectif/mesurable, pas subjectif) et la **verification** (comment l'agent sait que la stop-condition est atteinte, comment il vérifie et itère). Tout le reste — topologies, orchestration, fleets — est secondaire par rapport à ces deux piliers.

- **Cycle Reason → Act → Observe** : l'anatomie interne d'une itération. L'agent raisonne (planifie le prochain pas), agit (implémente), observe (vérifie le résultat : screenshot, test de code, rendu navigateur), puis confronte l'observation au done-criteria — si non atteint, il repart en reason. Image mentale de Herk : « a smart intern that you don't micromanage » — on lui donne un but, il vérifie son propre travail plusieurs fois, et ne revient vers l'humain qu'une fois done. C'est le même squelette que ROA/ReAct, mais avec le done-check comme organe de sortie explicite.

- **Courbe qualité/tentatives (l'externalisation du feedback)** : l'IA ne one-shot jamais à 100 %. Sur un axe tentatives × qualité, chaque feedback humain fait gagner ~5-10 % par itération jusqu'au seuil acceptable (90-95 %). Le loop consiste à **externaliser cette boucle de feedback à l'agent lui-même** : la tentative 1 d'un loop bien verrouillé démarre plus haut que la tentative 1 humaine, et la tentative 3-4 dépasse déjà ce que l'itération manuelle aurait atteint. Le loop ne vise pas la perfection — il déplace le point de départ de la review humaine.

- **Done-check objectif (Definition of Done)** : le critère de fin doit être formulé « as objective as possible » : *« keep iterating until X metric equals Y result »*. L'anti-pattern documenté dans la démo thumbnails : « until you're satisfied » — un critère subjectif qui rend la sortie de boucle arbitraire. Métaphore du gâteau : la fourchette qui ressort sans pâte. Quand la subjectivité est irréductible (esthétique, ton), on la pseudo-objective : rubrique de scoring + **scorer dédié en sub-agent, passé aux évaluations** pour calibrer sa fiabilité.

- **Topologies de loops (solo / maker-checker / manager-helpers)** : trois architectures par complexité croissante. **Solo loop** — un agent reason/act/observe dans une seule session terminal avec un bon prompt : le cas majoritaire de Herk. **Maker-checker** — un agent produit, un second note et renvoie le feedback : nécessaire quand le scoring porte l'enjeu. **Manager + helpers** — un orchestrateur et des sous-agents (« Russian nesting dolls ») : réservé au scope réellement parallélisable. La leçon anti-hype : commencer toujours au plus sobre.

---

## 🛠️ Outillage Stratégique & Matrice d'Alignement

| Outil / Technologie / Approche | Rôle Stratégique | Alignement Souverain A'Space |
| :--- | :--- | :--- |
| **`/goal` (Claude Code)** | Prompt récursif avec critère de fin — le véhicule des 3 démos (27-37 min de run) | Déjà canon chez nous : §10 du plan Méta-Mémoire = /loop-start avec verify-commands chiffrées par phase |
| **Loop Library (Matthew Berman)** | Bibliothèque publique de prompts de loops soumis par la communauté | Source d'inspiration à filtrer par ADR-LOOP-001 (chaque loop importé doit recevoir un done-check objectif + hard cap) |
| **Vérification par screenshot/navigateur** | L'agent capture son rendu à chaque itération et le compare à la référence | Pattern déjà utilisé (preview/Playwright) ; à généraliser dans les verify-commands des loops front |
| **Hyperframes (montage vidéo par loop)** | Cas d'usage réel de Herk : transcript → cuts → beats → render → vérif des bounds | Prouve que le loop s'applique au knowledge work non-code — transposable à nos pipelines YouTube→PARA |

---

## 🪐 Perspective Souveraine A'Space IT

Cette vidéo est la validation externe la plus propre de ce que nous avons gravé dans **ADR-LOOP-001** : un loop vaut exactement ce que vaut son done-check, et la majorité des tâches n'ont pas besoin de loop — elles ont besoin de **vérification**. C'est un contrepoids direct à la pression du marché (Steinberger, Cherny) qui pousse vers les fleets 24/7 : Herk, qui utilise CC quotidiennement pour du knowledge work, démontre que le sweet spot réel est le loop de 35 minutes à 2 heures, ou le « chunky loop » de nuit — pas la boucle permanente. Pour A'Space, l'intégration est immédiate : le runbook §10 du plan Méta-Mémoire applique déjà les quatre lois (done-check chiffré, hard stop à 2 échecs, log par phase, batch par sub-agents), et la permutation des moteurs (plan L1 §36) donne à MiniMax-L1 la charge d'exécuter ces loops en accéléré ×8 — ce qui rend le hard cap encore plus critique, puisqu'une boucle mal bornée en compression temporelle brûle 8× plus vite. L'action concrète à 30 jours (horizon H3 Saru) : auditer les `/goal` et loops existants (loop-plan-2026-06-15, multi-loop-karpathy, santa-loop) contre les 4 lois de l'ADR — tout loop « until satisfied » est non-conforme et doit recevoir sa métrique. Les A3 twins concernés : **Ortegas** (exécution, did-this-actually-work), **Chapel** (la métrique du done-check), **Zero** (l'automatisation des loops candidats), **Gwyn** (le D11 : le loop libère-t-il vraiment du temps A0 ?). Doctrine confirmée : ADR-META-001 D1/D5 (le done-check est un D1 mécanisé) ; doctrine étendue : le scorer-dédié-avec-evals comme réponse canonique à la subjectivité résiduelle.

---

## 🕹️ Protocole d'Exécution D.E.A.L

| Phase | Action Concrète | Objectif A'Space OS |
| :--- | :--- | :--- |
| **Définir** | Pour chaque loop actif : écrire sa ligne « itère jusqu'à X = Y » + son hard cap | Zéro loop sans Definition of Done mesurable (ADR-LOOP-001 loi 1-2) |
| **Éliminer** | Tuer les loops « until satisfied » et les runs >12 h sans livrable | Récupérer le budget token gaspillé en itérations non bornées |
| **Automatiser** | Scorer dédié en sub-agent pour les critères subjectifs (thumbnails, copy, design) | Pseudo-objectiver la subjectivité — pattern maker-checker systématisé |
| **Libérer** | Chunky loops de nuit sur les gros objectifs (lancés avant sommeil, review au réveil) | A0 review des résultats, jamais des itérations — bande passante cognitive préservée |

---

## 🔬 Annexes Détaillées de l'Audit Sémantique & Technique

### Note A3-01 : La démo thumbnails — anatomie d'un done-check défaillant
Le prompt demandait 10 concepts scorés sur rubrique Mr-Beast (clarté en miniature, curiosité, pull émotionnel, contraste), sélection du top 3, identification de la faiblesse de chaque concept, amélioration, re-scoring, itération sur le plus fort « until satisfied ». Résultat en 27 minutes : V1→V2 sur les concepts 1, 2 et 8, puis V3 finale sur le 8. Le mécanisme a fonctionné (amélioration mesurable par version) mais la sortie de boucle était arbitraire : les scores étaient auto-attribués par l'agent qui produisait. La correction canonique de Herk lui-même : un sub-agent scorer séparé, prompté indépendamment et passé à travers des évaluations pour établir la confiance dans sa notation — exactement la loi 3 d'ADR-LOOP-001 (jamais d'auto-vérification).

### Note A3-02 : Abbey Road en CSS — l'échec qui prouve le mécanisme
Recréer la photo des Beatles sans génération d'image, en pur HTML/CSS : critère `moyenne ≥ 9 OU hard cap 8 passes`, vérification par screenshot navigateur à chaque version. Le résultat final (V7) ne ressemble à rien — et c'est précisément ce qui rend la démo précieuse : le loop a fait exactement son travail (7 itérations visiblement meilleures les unes que les autres, vérification réelle à chaque passe, arrêt propre au cap) sur un objectif hors de portée du médium choisi. Leçon double : (1) le hard cap a empêché le gaspillage infini sur un but inatteignable ; (2) un loop parfait ne sauve pas un objectif mal choisi — le choix du médium reste une décision Orient (humaine).

### Note A3-03 : L'anti-hype comme position doctrinale
« Just because you're seeing someone like Peter Steinberger saying something doesn't mean this applies directly to you. » Steinberger est un hardcore coder chez OpenAI : les fleets 24/7 ont du sens pour SON contexte de codebase produit en itération continue. Herk, sur du knowledge work, utilise des cadences (cron) et des événements — pas du 24/7. Pour A'Space c'est un renfort direct de Posture C et d'ADR-SOBER-002 : l'automatisation permanente n'est pas un idéal, c'est un outil contextuel dont le défaut est OFF. La question de sobriété Rick (« peut-on vivre sans ? ») s'applique à chaque loop candidat avant sa création, pas après.

---

*Fiche de connaissances souveraine d'IT générée sous A'Space OS V2 — Standard Antigravity Premium.*

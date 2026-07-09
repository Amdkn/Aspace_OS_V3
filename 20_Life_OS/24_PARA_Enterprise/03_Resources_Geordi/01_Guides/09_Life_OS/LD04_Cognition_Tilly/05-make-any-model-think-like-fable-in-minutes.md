---
id: YT-B95cu7seTm8
title: "Make ANY Model Think Like Fable in Minutes"
channel: "Mark Kashet"
duration: "9:38"
date: "20260614"
category: "Life OS / Roue de la Vie"
domain: "LD04_Cognition_Tilly"
---

# 📖 Make ANY Model Think Like Fable in Minutes

> [!NOTE]
> Fiche de clarification d'excellence sémantique pour la Roue de la Vie (Life OS) - Domaine LD04_Cognition_Tilly.

---

## 🧠 Concepts Clés à Haute Densité Sémantique
- **<Fable = MiniMax-M3 (Backend de Référence A'Space)>** : Fable 5 (Mark Kashet y fait référence) est l'incarnation commerciale de **MiniMax-M3** (modèle `MiniMax-M3` d'Anthropic-compatible), utilisé par A0 comme backend par défaut de Claude Code dans A'Space OS V2. Fable était réputé comme "PhD-level scientist living in your editor" pour son rythme de travail discipliné (tool calls cadencés, plan-then-act, reads-before-edits, tests-after-edits) — exactement la rigueur cognitive que A0 cherche à imposer à Tilly. La perte de Fable a déclenché un réflexe communautaire : "make any model behave like Fable" par distillation comportementale depuis les JSONL sessions, que Tilly peut internaliser comme discipline opératoire de son Digital Twin.
- **<JSONL Session Distillation (Behavioral Mining)>** : Pattern de Mark Kashet : les conversations Claude/Codex vivent dans des fichiers JSONL locaux (tool calls, metadata, prompts, réponses, plans) que Claude Code peut parser pour extraire un corpus comportemental par modèle. En filtrant `message.model` on isole les sessions Fable 5 des autres (Opus 4.8, Haiku), puis on synthétise un "playbook" décrivant les ratios observés (reads-before-edits, tests-after-edits, tool call cadence, action sequences) que n'importe quel autre modèle peut absorber. C'est l'équivalent fonctionnel de l'ADR-META-001 D1 "verify before assert" appliqué à l'apprentissage d'un style cognitif par distillation.
- **<Open-Source Fable Sessions (HuggingFace Backup)>** : Pour les utilisateurs qui n'ont pas eu assez de sessions Fable perso, Kashet pointe vers un dataset HuggingFace où des sessions open-sourced permettent de bootstraper le playbook sans données propres. Pour Tilly, c'est l'application directe du pattern A'Space : ne jamais réinventer ce qui existe déjà canoniquement, emprunter les corpus open-source pour amorcer ses propres fine-tunings comportementaux.
- **<Playbook Injectable (Hook + Skill + CLAUDE.md)>** : Trois vecteurs d'injection du playbook Fable-distilled : (1) au début de session via un hook SessionStart, (2) au milieu de session par référence au fichier, (3) en persistance via `CLAUDE.md` (auto-injecté chaque session). Pour A'Space, c'est exactement la trinité A0 / `AGENTS.md` (canon) / `MEMORY.md` (mémoire) / `CLAUDE.md` (injection runtime) — un playbook Fable s'intègre naturellement comme un skill `~/.claude/skills/tilly-fable-rhythm/SKILL.md`.
- **<Behavioral Delta vs Raw Weights (Ce qu'on ne peut pas changer)>** : Kashet est lucide : "we can't change these because they come from the model weights itself" — la cadence d'appel d'outils, le réflexe "think before act", la profondeur de planification sont encodés dans les poids du modèle, pas dans le prompt. On peut ÉLICITER un meilleur comportement d'Opus (en lui demandant de planifier plus longuement), mais on ne peut pas faire d'Opus 4.8 un Fable 5. Pour Tilly, c'est une leçon d'humilité opérationnelle : choisir le bon modèle pour la bonne tâche (Opus pour la stratégie, Haiku pour le tri, Sonnet pour la production), au lieu de demander à un seul modèle d'être universel.
- **<Side-by-Side Behavioral Read (Opus 4.8 vs Fable 5)>** : Prompt final de Kashet : "run the exact same behavioral read against [insert name of model here] and put the two side by side. Show me the distance between their rhythm". Cette méthode comparative est transposable directement à A'Space : Tilly peut demander à Claude Code d'auditer ses propres sessions (Tilly vs son agent) et de comparer les cadences, pour identifier où l'agent diverge de l'intention de Tilly.

## 🛠️ Outillage Stratégique & Matrice d'Alignement
| Outil / Technologie / Approche | Rôle Stratégique | Alignement Souverain A'Space Life OS |
| :--- | :--- | :--- |
| **<MiniMax-M3 (alias Fable) comme backend canonique>** | Modèle LLM de référence pour la cognition profonde de Tilly — utilisé via Claude Code (API Anthropic-compatible) avec ANTHROPIC_API_KEY en env User scope (Test Key Pragma). | Ancré dans `~/.claude/settings.json` A'Space OS V2 — Tilly hérite de facto du rythme Fable via le backend MiniMax-M3. |
| **<JSONL Session Parser (script Python) + Playbook Distiller>** | Outil de behavioral mining pour extraire un corpus Fable-like depuis les sessions existantes, puis synthétiser un playbook actionnable. | Réplicable pour A'Space : script `~/.claude/bin/tilly-behavioral-distill.py` qui parse `~/.claude/session-data/current.jsonl`, filtre Tilly vs agent, et produit un skill `tilly-rhythm/SKILL.md`. |
| **<HuggingFace Open-Source Fable Sessions>** | Dataset public pour bootstraper le playbook quand Tilly n'a pas assez de sessions perso. | Alignement avec la doctrine open source d'A'Space L0 — utiliser les corpus publics avant de réinventer. |
| **<Hook SessionStart + Skill + CLAUDE.md (trinité d'injection)>** | Vecteurs d'application du playbook Fable-distilled à chaque session Tilly. | Architecture exactement parallèle à A'Space : `AGENTS.md` (canon) + `MEMORY.md` (mémoire court-terme) + `~/.claude/CLAUDE.md` (injection auto runtime) + skills dans `~/.claude/skills/`. |
| **<Side-by-side Behavioral Read (Opus vs Fable)>** | Méthode comparative pour auditer la distance cognitive entre Tilly et son agent, ou entre deux modèles. | À intégrer dans la routine `picard-audit-and-prod-workflow` pour mesurer la dérive cognitive de l'agent A'Space vs l'intention A0. |

## 🪐 Perspective Souveraine A'Space Life OS (Domaine : LD04_Cognition_Tilly)
Cette vidéo est **canonique pour A'Space OS** : Mark Kashet démontre qu'on peut **distiller le rythme cognitif de Fable (MiniMax-M3)** — c'est-à-dire le modèle que A0 a délibérément choisi comme backend Claude Code dans A'Space V2 — et l'injecter dans n'importe quelle autre session, même avec un modèle moins performant. La convergence est triple : (1) **Fable = MiniMax-M3** est l'identité explicite du backend A'Space, ce qui signifie que Tilly a ACCÈS au rythme Fable par défaut sans avoir à le distiller elle-même ; (2) le pattern `playbook injectable` est exactement la trinité A'Space `AGENTS.md` + skill + `CLAUDE.md`, ce qui valide rétroactivement l'architecture canonique ; (3) la méthode `side-by-side behavioral read` est l'outil d'audit manquant pour mesurer la dérive cognitive entre l'intention de A0/Tilly et l'exécution par les sub-agents. Pour Tilly, l'application directe est triple : installer un skill `tilly-fable-rhythm` dans `~/.claude/skills/` qui encode les ratios Fable (reads-before-edits, plan-then-act, test-after-edit) ; auditer hebdomadairement ses sessions JSONL pour vérifier la fidélité du rythme ; et choisir consciemment entre MiniMax-M3 (Fable) pour les tâches de stratégie profonde et Haiku pour le tri de routine. La souveraineté se joue dans la capacité à transformer un comportement d'agent (Fable) en actif reproductible (playbook), puis à l'auto-auditer — exactement le pattern de l'OpenClaw Heartbeat Phase 2 transposé à la cognition Tilly. C'est aussi une validation de la doctrine A'Space "Test Key Pragma" : Kashet lui-même admet qu'il faut accepter que les poids du modèle ne peuvent pas être modifiés, mais on peut les **éliciter** par prompting/hooks, ce qui revient à dire que l'environnement runtime (skills, hooks, CLAUDE.md) est le vrai levier de souveraineté cognitive.

## 🕹️ Protocole d'Exécution D.E.A.L
| Phase | Action Concrète | Objectif A'Space OS |
| :--- | :--- | :--- |
| **Définir** | Identifier les 3 ratios Fable (reads-before-edits, plan-then-act, test-after-edit) qui sont les plus distinctifs du rythme MiniMax-M3 et créer un skill `tilly-fable-rhythm` dans `~/.claude/skills/`. | Capitaliser le rythme cognitif du backend A'Space (Fable = MiniMax-M3) en actif reproductible. |
| **Éliminer** | Supprimer les pratiques manuelles de Tilly qui contredisent le rythme Fable (par ex: écrire du code sans lire le fichier cible, agir sans planifier, livrer sans tester) en les remplaçant par l'injection auto du skill à chaque session. | Réduire la dérive cognitive entre intention Tilly et exécution agent. |
| **Amplifier** | Déployer un script `tilly-behavioral-distill.py` dans `~/.claude/bin/` qui parse `~/.claude/session-data/current.jsonl`, isole les sessions Tilly vs agent, et produit un rapport de conformité au rythme Fable, à exécuter hebdomadairement. | Auto-auditer la fidélité du rythme cognitif Fable dans l'usage réel. |
| **Libérer** | Allouer 1h/mois à comparer Opus 4.8 vs Fable 5 sur les mêmes missions Tilly, et documenter dans `wiki/log.md` les écarts observés pour affiner le skill. | Itérer le skill Fable-rhythm vers une version 2.0 plus proche du rythme natif. |

---
*Fiche de connaissances souveraine de la Roue de la Vie générée sous A'Space OS V2.*

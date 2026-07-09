---
id: YT-n5SDWFtAclg
title: "I Built AI Autoresearch Tool"
channel: "Vuk Rosić"
duration: "11:12"
date: "2026-06-17"
category: "Auto-Research Loop / Tool Architecture / Knowledge Discovery"
status: DISTILLED_L1_PREMIUM
domain: "03_IT"
ld: LD07_Creativity_Reno  # E1 fix (était: LD03_Health_Culber) — bijection D3
ld_owner: "Culber"
video_id: n5SDWFtAclg
url: https://www.youtube.com/watch?v=n5SDWFtAclg
transcript_source: TranscriptAPI.com MCP (D6 #43)
b2_owner: cyborg-it
sister_b1: jerry-prime
---

# 📖 I Built AI Autoresearch Tool

> [!NOTE]
> Fiche de clarification d'excellence sémantique pour le Domaine 03_IT — Auto-Research Loop / Tool Architecture / Knowledge Discovery. Standard Antigravity Premium (D6 #48).

---

## 🧠 Concepts Clés à Haute Densité Sémantique

- **<Auto-Research Loop Definition>** : Architecture où un agent itère AI research 24/7 sans intervention humaine par cycle : génère ideas → implémente code → queue experiments GPU → valide evidence. Human check-in via status anytime. Différent de 'agent runs once' : c'est un loop continu qui apprend de ses propres résultats.
- **<Insight Clé — Ideas Sont les Plus Difficile pour AI>** : Vuk : 'AI is not so good at choosing what to research on, what kind of ideas. Ideas are hardest for AI.' Implémenter le code + run experiments = easy pour AI. Ideation = hard. Focus humain doit rester sur ideation, pas implémentation. Distribution optimale du travail humain/IA selon difficulté cognitive.
- **<Workflow — Simple UI + Auto Research Mode>** : Toggle simple/advanced UI. 'Auto research on' fait tourner la boucle en background. Tous les boutons disparaissent. L'humain spécifie le projet initial (LLM, RL, video gen, whatever) et l'outil choisit comment itérer. Multi-research folders supportés, threads indépendants par folder.
- **<Architecture — Tmux Sessions + GPU Queue>** : Workers = tmux sessions. Dead sessions à killer manuellement pour l'instant (automation future prévue). Auto-research mode dispatch workers sur GPU queue. Workers report back via state file. Pattern = persistent workers + state DB + orchestrator loop.
- **<Vision OpenClaw-for-Research>** : Vuk imagine son outil être utilisé comme base pour un futur 'OpenClaw for AI research' : contribution open-source massive, forks par universités et labs, démocratisation de la recherche AI auto-pilotée. Pattern = 'forker un OSS contribution majeure pour recherche reproductible'.

---

## 🛠️ Outillage Stratégique & Matrice d'Alignement

| Outil / Technologie / Approche | Rôle Stratégique | Alignement Souverain A'Space |
| :--- | :--- | :--- |
| **<Tmux + GPU queue>** | Workers persistants + state queue + dispatch. | A'Space : analogue aux A3 twins dans Symphony (chaque twin = worker persistant avec state). |
| **<Open-source contributions>** | Pattern forkable pour recherche reproductible. | A'Space : canon `00_Amadeus/05_OSS_Twin/` est déjà open-source-ready. |
| **<Simple/advanced UI toggle>** | Réduit complexité cognitive pour utilisateurs non-tech. | A'Space : interface `Geordi` canonique pour ressources. |
| **<Multi-folder + threads>** | Isolation des recherches parallèles. | A'Space : 8 Life Wheel domains + 6 Business domains = isolation native. |

---

## 🪐 Perspective Souveraine A'Space 03_IT

L'outil Vuk est un pattern intéressant pour A'Space mais avec une application décalée — Vuk vise la recherche AI (training models), A'Space vise le business OS. (1) **Niveau architecture** : le pattern 'auto-research loop' est applicable directement au pipeline `/youtube-to-guide` (auto-research sur batch vidéos), à Symphony auto-research phase 2 (skill creation), ou à Geordi ontology enrichment. Le sister-skill `area-domain-doctrine-distill` peut être réécrit pour boucler. (2) **Niveau doctrine** : l'insight 'AI faible sur ideation' valide la doctrine A'Space que l'humain doit rester dans la boucle sur les décisions créatives (D7 cost-of-escalation, ADR-META-001). L'IA excelle sur exécution + validation, l'humain excelle sur ideation + validation finale. (3) **Niveau action A0 (H3 Saru)** : (a) benchmarker l'outil Vuk sur 1 verticale recherche (e.g., 'trouve les nouveaux patterns AI agent du mois'), (b) si résultats probants, l'intégrer comme agent A3 supplémentaire dans Symphony. Doctrine Anti-Paresse : un auto-research tool sans observability ni human-in-loop = recipe for disaster, exactement le warning de Vuk.

---

## 🕹️ Protocole d'Exécution D.E.A.L

| Phase | Action Concrète | Objectif A'Space OS |
| :--- | :--- | :--- |
| **Définir** | Identifier 1 verticale A'Space où auto-research serait utile (e.g., veille concurrentielle OMK Tax ou enrichissement Geordi ontology). | Préciser scope avant d'investir du temps. |
| **Éliminer** | Pas applicable — outil externe, complémentaire à Symphony. | N/A |
| **Automatiser** | Benchmarker l'outil Vuk sur 1 verticale pendant 30 jours avec observability stricte + human-in-loop checkpoints. | Mesurer ROI réel avant adoption. |
| **Libérer** | Si probant, intégrer comme A3 twin dans Symphony (ex: A3-research-open-source). | A'Space catalogue de 35+ A3 twins + auto-research extension. |

---

## 🔬 Annexes Détaillées de l'Audit Sémantique & Technique

### Note Note A3-01 : Insight 'AI faible sur ideation' — Implication A'Space

Vuk confirme : ideation = hard pour AI, exécution = easy. A'Space doit garder l'humain sur ideation (canon `wiki/hand_offs/` créé par A0 = traces des idées humaines) et laisser Symphony itérer sur exécution (auto-fill des guides via transcripts). Le sister-skill `/skill-creator` est exactement ce pattern — humain spécifie la skill, agents A3 exécutent le boilerplate.

### Note Note A3-02 : Architecture multi-research folders — Pattern A'Space

Vuk : multi-folder + threads indépendants. A'Space équivalent = les 8 Life Wheel LDxx domains + 6 Business domains. Chaque domain = folder indépendant où Symphony peut itérer. Pattern de domain isolation déjà canon dans `20_Life_OS/LD0X_*` et `30_Business_OS/10_Projects/<name>/`.

### Note Note A3-03 : Open-source pour recherche reproductible — Vision A'Space

Vuk imagine un 'OpenClaw for AI research' basé sur son outil. A'Space canon est déjà open-source-ready (cf. `00_Amadeus/05_OSS_Twin/symphony/`). Sister-skill `/replicate-squads` peut aider à forker la doctrine Symphony vers d'autres OS agentiques.

---

*Fiche de connaissances souveraine d'03_IT générée sous A'Space OS V2 — Standard Antigravity Premium (D6 #48).*

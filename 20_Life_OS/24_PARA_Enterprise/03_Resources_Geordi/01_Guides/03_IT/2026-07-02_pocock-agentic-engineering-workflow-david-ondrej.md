---
id: YT-UNKNOWN-pocock-workflow
title: "Matt Pocock's Agentic Engineering Workflow (just copy him)"
channel: "David Ondrej (invité : Matt Pocock)"
duration: "UNKNOWN"
date: "2026-07-02"
category: "IT / Loop Engineering / Harness Doctrine"
status: DISTILLED_L1_PREMIUM
sister: 09_Life_OS/LD07_Creativity_Reno/2026-07-02_pocock-agentic-engineering-workflow_david-ondrej__GUIDE.md
source_note: transcript fourni par A0 in-chat 2026-07-02 — video_id non fourni, non inventé (D1)
ld: LD07_Creativity_Reno
b2_owner: cyborg-it
sister_b1: jerry-prime
---

# 📖 Matt Pocock's Agentic Engineering Workflow

> [!NOTE]
> Fiche de clarification d'excellence sémantique pour le Domaine IT — Doctrine du harness. Pocock (auteur du repo skills qui contient **grill-me**, le skill fondateur de notre plan A0-L) recadre trois débats : harness > modèle, queues > loops, procédures > abilities.

---

## 🧠 Concepts Clés à Haute Densité Sémantique

- **Tactique vs Stratégique (Ousterhout, *A Philosophy of Software Design*)** : la programmation tactique = le terrain au jour le jour — écrire le code, la syntaxe, les bugs, les commits. La stratégique = gagner la guerre — architecture de la codebase, interfaces entre modules, vélocité long terme. Le verdict de Pocock : **« AI has eaten tactical programming, it's gone »** — l'IA le fait moins cher. La délégation stratégique n'a pas changé : design des parties dures en amont, tâches bien scopées, tests bien pensés, juste-assez de documentation pour pointer l'agent au bon endroit. Corollaire mesuré partout : l'IA rend les seniors ~10× meilleurs (les juniors, un peu) — **« your skills are the ceiling on what AI can do »**.

- **Queues, pas loops (le recadrage central)** : le développement a toujours été une queue — un backlog d'items, des nœuds (devs ou agents) qui piochent, des résolutions. « An idea that there's a single loop that just goes and completes all the tasks doesn't really match how developer teams work. » Le setup réel de Pocock : issues GitHub + **labels comme triggers** (`agent-explore`, `agent-implement`) → GitHub Actions lance l'agent AFK → PR avec review agent → clic humain. Le « loop » du marché est, dans la plupart des cas, un agent AFK sur queue mal nommé.

- **HITL rightward + review du système producteur** : les checkpoints humains se poussent progressivement vers la droite (bug report → exploration auto → fix auto → review auto → il ne reste que le merge), mais jamais à zéro. La question de contrôle : « who reviews the AI that's deciding you don't need to review? » — on ne review pas seulement le code, on review **le système qui produit le code** : échantillonner périodiquement les PRs auto-validées pour calibrer la confiance. La review devient un actif d'observabilité du harness, pas une corvée.

- **Procédures vs Abilities (la taxonomie des skills)** : deux types de skills aux économies opposées. **Ability** = invoquée par le modèle (coding standards, conventions) — mais *chaque description de skill fuit dans le contexte* : 100 abilities = 100 descriptions leakées en permanence. **Procédure** = invoquée par l'humain (grill-me, 2prd, teach), potentiellement `disable-model-invocation: true` (zéro fuite). Position de Pocock : préférer les procédures — « I don't want to delegate my thinking to the model » — l'humain reste le driver, le savoir reste dans le développeur.

- **Connaissance / Compétence / Sagesse** : les trois étages de la maîtrise. La connaissance (comprendre) et la compétence (avoir fait, mémoire musculaire) se **bundlent** en skills partageables — c'est la grande nouveauté de l'époque : proceduraliser son savoir-faire et le distribuer à l'équipe, « raising the floor ». La **sagesse** (savoir quand agir, comment ça s'insère dans le réel) ne s'obtient qu'en contexte — elle ne se bundle pas. Le teach skill de Pocock illustre le bundling : un skill **stateful** (mission.md + learning record local) qui génère des cours personnalisés avec quizzes, HTML riche, zone de développement proximal.

- **AX — Agent Experience** : le miroir agentique de la DX. Tout ce qui améliore l'expérience de l'agent dans la codebase — skills adaptés, harness propre, architecture lisible — multiplie le rendement. La réponse de Pocock à « comment optimiser le token spend ? » : **« have a codebase that's easier to make changes in »** — une meilleure architecture permet un modèle plus bête (donc moins cher) à travail égal, parce que les garde-fous sont meilleurs et que l'agent brûle moins de tokens à se cogner aux murs. Penser modèle-d'abord est l'erreur ; les fondamentaux de 30-40 ans tiennent.

---

## 🛠️ Outillage Stratégique & Matrice d'Alignement

| Outil / Technologie / Approche | Rôle Stratégique | Alignement Souverain A'Space |
| :--- | :--- | :--- |
| **Sandcastle (sandbox Docker/Podman)** | Jamais d'agent AFK hors isolation — home dir et env vars protégés | ADR-LOOP-002 loi 3 + P6-E3 (dry-run sandbox gated) — notre EnterWorktree pour le cas léger |
| **GitHub Actions + labels comme triggers** | La queue matérialisée : n'importe qui pose un label, l'agent AFK pioche | Pattern à transposer sur nos repos OMK (post-graduation) — trigger = label, pas cron |
| **grill-me (5 phrases)** | Interviewer adversarial jusqu'à compréhension partagée — remplace le plan mode | **LE skill fondateur d'A0-L Jumeau Challenger** — ce guide est sa doctrine source locale |
| **teach (skill stateful)** | Cours personnalisé à la volée, état local (mission + learning record) | Modèle pour nos skills statefuls (premortem-fill LIVE handoffs = même famille) |
| **Whisper Flow (dictée)** | « Anyone not doing dictation is just so much slower » — le débit cerveau→tokens | Compatible doctrine TTS/voice A0 (réponses courtes, canal vocal) |

---

## 🪐 Perspective Souveraine A'Space IT

Ce guide touche A'Space plus profondément que les trois autres parce que Pocock est déjà **dans** notre canon : son skill grill-me est nommément la référence du plan A0-L (« Jumeau Numérique Partenaire pour mattpocock/skills/grilling ») — cette fiche devient la doctrine source locale de ce choix. Trois de ses positions percutent directement nos chantiers. D'abord **queues-pas-loops** : c'est la philosophie exacte de Donna DLQ et des stop-conditions §10.4, désormais gravée dans ADR-LOOP-002 — nos futurs Scheduled (l'automatisation de CC/HA/MC qui précède la montée des Shadows) se spécifient comme consommateurs de queue, pas comme boucles. Ensuite le **reset minimaliste** : sa prescription n°1 (« delete every skill, every plugin, every MCP server, go back to a blank slate, observe, then layer back only what you miss ») est un défi frontal à notre surface — 145 commandes × 130 skills × 175 agents. C'est un audit Rick S1 en puissance : non pas tout supprimer (notre contexte est un OS, pas un setup de dev), mais mesurer ce que chaque ability leake en contexte et convertir en procédures `disable-model-invocation` tout ce qui n'a pas besoin d'être vu du modèle. L'action à 30 jours (H3) : inventorier les descriptions de skills leakées (le micro-index DOX P4 rend ça mécanique) et flagger les candidates à la conversion. Enfin **review-the-system** : notre D5 (pas d'auto-congratulation) monte d'un étage — échantillonner périodiquement ce que les loops auto-valident. A3 twins concernés : **Zero** (proceduralisation des workflows), **Tilly** (le teach skill comme modèle d'apprentissage LD04), **Rutherford** (l'échantillonnage hebdo des auto-validations). ADRs impactés : ADR-LOOP-002 (source), plan A0-L (doctrine grilling), ADR-SOBER-002 (le reset minimaliste est un anti-paperclip appliqué au contexte lui-même). Doctrine confirmée : harness > modèle (notre pari Mindsets — la discipline M3 par l'instruction — est exactement ce pari) ; doctrine challengée : notre volume de skills/commandes, à auditer plutôt qu'à défendre.

---

## 🕹️ Protocole d'Exécution D.E.A.L

| Phase | Action Concrète | Objectif A'Space OS |
| :--- | :--- | :--- |
| **Définir** | Inventaire des skills : procédure vs ability, et ce que chaque description coûte en contexte | Carte du bloat réel (pas supposé) — préalable à l'audit Rick |
| **Éliminer** | Convertir les abilities non essentielles en procédures `disable-model-invocation` | Contexte modèle allégé sans rien perdre (le savoir reste invocable par A0) |
| **Automatiser** | Labels-triggers sur les repos OMK : `agent-explore` / `agent-implement` → AFK sandboxé | La queue matérialisée sur le ship L2 réel |
| **Libérer** | Échantillonnage hebdo des items auto-validés (review du système, pas du code) | Confiance calibrée → checkpoints poussés à droite sans foi aveugle |

---

## 🔬 Annexes Détaillées de l'Audit Sémantique & Technique

### Note A3-01 : Le débat bitter lesson — 50/50 assumé
Ondrej challenge : « si le modèle devient vraiment meilleur, ton harness compte moins ». Pocock assume le risque de « tomber dans la bitter lesson » (le compute brut bat toute optimisation) mais tient sa ligne : il n'est pas pundit, il optimise ce qui existe aujourd'hui, et un harness agnostique + des fondamentaux de 30 ans survivront aux générations de modèles — alors que sur-optimiser autour d'un modèle spécifique meurt à chaque release. Position miroir de la nôtre : les Mindsets (discipline par l'instruction) sont un harness portable — ils ont servi M3, ils servent Fable, ils serviront le suivant. Sa pratique concrète : attendre ~1 mois après chaque release de modèle (« you're not losing that much »), y compris pour Fable.

### Note A3-02 : L'épisode Twitter API — la valeur humaine résiduelle
Ondrej raconte : Fable-dans-Cursor a débuggé seul une console développeur cassée (browser intégré, création de clés API, détection que les clés étaient dans la mauvaise app, migration) — « j'ai senti que ma valeur dans ce projet était très basse ». La réponse de Pocock est la ligne doctrinale : ce qui reste à l'humain, c'est de **décider si c'était la bonne chose à faire** et de security-tester le résultat — le jugement, pas l'exécution. Et la contre-question systémique : si Fable trouve des bugs profonds que d'autres modèles ratent, la vraie leçon n'est pas « Fable est magique », c'est « il y a des bugs profonds chez toi → construis le loop de sécurité qui les cherche en continu, même avec un modèle moins cher pointé au bon endroit ».

### Note A3-03 : Review enrichie — la vidéo commentée sur le PR
Le pattern le plus actionnable de l'épisode : sur tout changement front, l'agent enregistre une vidéo de walkthrough du changement, appelle un TTS et superpose une narration — le PR arrive avec sa démo commentée. La review humaine passe d'une session de reconstruction mentale à une lecture de 2 minutes. Généralisation : « optimize for human review » est une direction de design à part entière — chaque livrable AFK devrait voyager avec sa preuve (sortie chiffrée, screenshot, vidéo). C'est ADR-LOOP-002 loi 4, et le complément exact du verifier read-only de Jason : l'un juge, l'autre documente pour le juge final (A0).

---

*Fiche de connaissances souveraine d'IT générée sous A'Space OS V2 — Standard Antigravity Premium.*

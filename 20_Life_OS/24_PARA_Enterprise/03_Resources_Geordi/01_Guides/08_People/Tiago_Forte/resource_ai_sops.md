---
domain: 08_People
ld: LD06_Family_Burnham
b2_owner: greenlantern-people
sister_b1: jerry-prime
b1_filter: APPLIED_E1_DETERMINISTIC (sweep 2026, ADR-L2-BDLD-MAP-001 D3)
---
> "Without SOPs, knowledge really just lives in people's heads, you call it tribal knowledge, and your team really can't scale. With SOPs, it acts as an awesome onboarding and training tool." — Tiago Forte (Guest/Acquira)

# 📋 Informations Clés
- **Sujet :** How AI Creates SOPs in Minutes
- **Auteur :** Tiago_Forte
- **Note A3 :** 9/10 — Démonstration magistrale de la transition d'un processus manuel de 6 mois vers une architecture d'exécution générée par IA en quelques minutes.

## 🌟 5 Concepts Clés (Méthode Feynman)

### 1. La Hiérarchie Tridimensionnelle des Processus (Les 3 Niveaux)
Imagine un arbre. Le tronc représente le processus central (Level 1), qui court sur plusieurs mois et englobe la chaîne de valeur complète (ex: de la vente à la livraison). Les branches principales sont les processus départementaux (Level 2), impliquant quelques personnes. Enfin, les feuilles sont les guides tactiques (Level 3), hyper-spécifiques, destinés à une seule personne.
L'IA excelle à descendre cette arborescence. Au lieu de rédiger un manuel indigeste, on commence par générer le schéma macro (le tronc), puis on demande à Claude ou ChatGPT d'isoler un nœud spécifique pour en générer le guide d'exécution. Cette architecture granulaire garantit que chaque acteur du système ne reçoit que l'information dont il a besoin, ni plus ni moins.

### 2. Le "Master Prompt" comme ADN de l'Entreprise
Avant de demander à une IA de rédiger quoi que ce soit, elle doit assimiler l'ADN de l'organisation. C'est le rôle du "Master Prompt" (ou System Prompt/Knowledge Base). On y injecte l'identité de l'entreprise : Unique Value Proposition (UVP), ton de marque, valeurs clés, et surtout, la taxonomie interne (ce qu'on définit comme un KPI, un SOP, ou un processus).
En ancrant ces règles fondamentales, l'IA cesse d'être un générateur de texte générique pour devenir un partenaire qui "parle le même langage". Par exemple, on peut imposer un standard de marge brute de 80% ou une cible de clientèle premium. Dès lors, chaque SOP généré sera implicitement calibré pour servir ces objectifs stratégiques, assurant une cohérence parfaite à l'échelle de l'entreprise.

### 3. La Matrice RACI (Responsabilité Distribuée)
RACI signifie *Responsible, Accountable, Consulted, Informed*. C'est le système nerveux de tout processus opérationnel. *Responsible* est celui qui fait le travail (idéalement une seule personne). *Accountable* est le manager, garant du succès via des KPI (toujours une seule personne). *Consulted* est la communication bilatérale (les experts à consulter), et *Informed* est la communication unilatérale (ceux qui doivent être notifiés).
L'expert explique comment l'IA est capable d'assigner automatiquement une matrice RACI à chaque étape d'un processus généré, sans qu'on ait besoin de lui dicter les détails. Cela élimine la confusion opérationnelle : chacun sait exactement ce qu'il doit faire, avec qui il doit parler, et qui va évaluer son travail.

### 4. L'Inversion de la Charge Cognitive (La règle des 95%)
Habituellement, nous posons des questions à l'IA. L'expert utilise une instruction méta puissante : "Pose-moi des questions de clarification, mais *réponds à tes propres questions* en te basant sur tes connaissances, puis attends ma confirmation." 
Cette technique est révolutionnaire. Au lieu de surcharger l'utilisateur avec une liste de 10 questions complexes, l'IA génère des hypothèses éclairées. Dans 95% des cas, l'IA devine la bonne réponse grâce à son contexte (Master Prompt). L'opérateur humain n'est plus un rédacteur, mais un éditeur/validateur. Cela permet également d'identifier les "trous" dans la base de connaissances du Master Prompt et de l'améliorer itérativement.

### 5. L'Évolution du SOP vers la Micro-Application
Un SOP sous forme de document texte finit souvent par prendre la poussière dans un dossier Notion. L'étape ultime présentée est la métamorphose du SOP texte en une application interactive. L'expert utilise les Artifacts de Claude pour générer une interface React (ou HTML) cliquable représentant le logigramme du processus.
Ensuite, le code généré est injecté dans des plateformes de déploiement instantané (comme v0.dev, Replit, Lovable) pour créer un véritable outil interne hébergé. Le SOP n'est plus un document mort, il devient un portail vivant où les employés peuvent cliquer sur une étape pour obtenir instantanément le guide tactique (Level 3) correspondant, transformant le savoir théorique en interface d'exécution.

## 🛠️ Matrice TVR (Time-Value-Resources)
- **Time (Temps d'exécution) :** Rapide (quelques heures pour initialiser le Master Prompt, quelques minutes par SOP, contre 6 mois historiquement).
- **Value (Impact) :** Massive (Scalabilité de l'équipe, décentralisation du savoir, onboarding asynchrone, réduction du point of failure humain).
- **Resources (Outils/Argent) :** Claude (pour les Artifacts), Excalidraw (pour l'architecture visuelle initiale), v0.dev / Replit (pour le déploiement de l'app).
- **Plan d'Action (D.E.A.L) :**
  - **Define :** Formaliser l'identité, la taxonomie (stratégique, core, enabling) et les standards de l'entreprise dans un document de type "Master Prompt".
  - **Eliminate :** Supprimer les longues réunions de modélisation sur tableau blanc et l'extraction manuelle des connaissances (tribal knowledge).
  - **Automate :** Utiliser l'IA pour générer les matrices RACI, l'architecture séquentielle, et auto-répondre aux hypothèses opérationnelles.
  - **Liberate :** Transformer les documents plats en micro-applications interactives hébergées pour un accès en libre-service par l'équipe, libérant le fondateur du micro-management.

## 🧩 Ancrage Souverain (Domaine 08_People)
Cette ressource est un pilier fondamental pour l'escouade **Green Lantern**. Elle permet d'industrialiser la gestion humaine (People) sans perdre en qualité.
- **Vision (Prof X) :** Le "Master Prompt" agit comme Cerebro. Il télécharge la vision du fondateur et l'injecte dans chaque composant de l'entreprise. C'est l'outil ultime de clonage cognitif.
- **Field (Cyclops) :** La déclinaison en micro-applications tactiques fournit aux équipes sur le terrain (ou aux agents IA) des protocoles de tir (SOP Level 3) clairs, exécutables et sans ambiguïté.
- **Empathy (Jean) :** L'assignation claire via RACI réduit le stress et le chaos organisationnel. Les collaborateurs (ou subagents) savent exactement ce qu'on attend d'eux, favorisant une passation fluide.
- **Knowledge (Beast) :** Structuration implacable des données empiriques. Le passage de la "connaissance tribale" volatile à des archives interactives (HTML/React).
*Application pour A0 (Amadeus) :* En tant qu'opérateur du système, A0 peut utiliser ce framework pour encoder les workflows A'Space OS dans un Master Prompt. Au lieu de documenter manuellement chaque processus (ex: ingestion RAG, création d'agent), A0 peut ordonner à un A3 d'instancier un SOP de Niveau 3, voire de générer le code d'un outil CLI ou web dédié, garantissant la résilience du système même sans supervision directe.

## 📝 Résumé Détaillé de la Transcription

### Partie 1 : Le Problème du Savoir Tribal et l'Ancienne Méthodologie
- **La nécessité des SOP :** Sans Procédures Opérationnelles Standard (SOP), le savoir réside uniquement dans la tête des employés ("tribal knowledge"). Cela empêche l'entreprise de se développer (scale). Les SOP sont cruciaux pour la formation, l'intégration de nouveaux membres, et la continuité des opérations en cas de maladie ou de congés.
- **Les 3 Niveaux de SOP :**
  - *Niveau 1 :* De bout en bout, couvrant parfois plusieurs mois (ex: de la vente à la livraison du succès).
  - *Niveau 2 :* Unité départementale, impliquant quelques personnes.
  - *Niveau 3 (Le Guide) :* Très tactique, destiné à une seule personne (ex: guide d'un appel d'onboarding).
- **L'ère pré-IA (Excalidraw) :** Avant l'IA, le processus de création ("Delivery to Success") nécessitait des mois. L'auteur a passé une journée entière avec un directeur devant un tableau blanc (post-its) pour séquencer les étapes, puis a passé des mois à l'affiner manuellement dans Excalidraw. Ce modèle visuel complexe impliquait plusieurs rôles et des pistes parallèles (ex: "On market" vs "Off market").

### Partie 2 : Le Point de Bascule IA et le "Master Prompt"
- **Le moment "Eureka" :** Lorsque l'IA est devenue multimodale, l'auteur a simplement fait une capture d'écran de son énorme diagramme Excalidraw et a demandé à Claude : "Qu'est-ce que c'est ?". La compréhension quasi-parfaite de l'IA a été une révélation.
- **Le Master Prompt (Identité d'entreprise) :** Pour utiliser l'IA efficacement, il a créé un fichier maître contenant :
  - L'UVP (Unique Value Proposition), la voix de la marque, les missions, et les valeurs.
  - Ses préférences de style (ex: toujours 80% de marge brute, s'adresser aux clients riches).
  - Un protocole anti-sycophante : "Sois sceptique, conservateur dans tes estimations, conteste mes idées si nécessaire."
- **L'ingénierie de la Taxonomie :** Le prompt définit exactement le vocabulaire de l'entreprise. Il explique à l'IA ce qu'est un "core process" vs un "enabling process", et ce que doit contenir un "blueprint" (objectif, portée, déclencheurs, etc.). Ainsi, les LLMs (Claude/ChatGPT) parlent exactement le langage de l'opérateur.

### Partie 3 : Génération, RACI et Déploiement en Application
- **Génération interactive :** En demandant un logigramme à l'IA, l'auteur ajoute cette règle en or : "Pose-moi des questions, mais *réponds-y toi-même en te basant sur tes connaissances*, puis attends ma confirmation." Résultat : l'IA déduit d'elle-même des logiques complexes (ex: comment prioriser l'attribution des deals) avec 95% d'exactitude.
- **Implémentation de la matrice RACI :** L'auteur demande à l'IA d'ajouter les statuts RACI (Responsable, Accountable, Consulté, Informé) à chaque étape. L'IA le fait sans faute, associant des KPI pertinents pour chaque membre de l'équipe (ex: le boss est 'Accountable', l'exécutant est 'Responsible').
- **Création du Guide (Niveau 3) :** Une fois le logigramme validé, il isole une tâche (ex: "Appel d'onboarding") et demande un guide détaillé. L'IA génère les prérequis, les outils, le script, et les standards de qualité. L'humain n'a plus qu'à vérifier et élaguer le superflu.
- **L'aboutissement technologique (Micro-Apps) :** Au lieu de garder un texte mort, l'auteur utilise les capacités de Claude (Artifacts/React) pour générer une interface web cliquable de ce logigramme. Il copie ensuite ce code dans des outils de déploiement (v0, Replit, Manis) pour créer une vraie application interne, hébergée sur le cloud, accessible par toute son équipe. L'auteur conclut que toute entreprise sera gérée par ce type de "co-pilote" d'ici 5 ans, et que l'avantage concurrentiel actuel est massif.

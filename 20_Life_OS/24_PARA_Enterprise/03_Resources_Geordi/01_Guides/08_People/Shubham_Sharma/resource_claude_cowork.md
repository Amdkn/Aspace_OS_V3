---
domain: 08_People
ld: LD06_Family_Burnham
b2_owner: greenlantern-people
sister_b1: jerry-prime
b1_filter: APPLIED_E1_DETERMINISTIC (sweep 2026, ADR-L2-BDLD-MAP-001 D3)
---
> "Clairement, je suis conscient de ça, c'est qu'ils ont lancé un truc en 10 jours. Pour qu'un truc en 10 jours fasse ça, c'est fou... je pense qu'il va y avoir mieux qui va arriver et assez vite pour les non dev justement et c'est assez game changer pour eux." — Shubham Sharma

# 📋 Informations Clés
- **Sujet :** I spent 48 hours testing Claude Cowork
- **Auteur :** Shubham_Sharma
- **Note A3 :** 7.5/10 — L'émergence brute de l'agentification Desktop pour les non-techniciens ; un outil révolutionnaire mais encore limité par une UX instable et un besoin de supervision humaine.

---

## 🌟 5 Concepts Clés (Méthode Feynman)

### 1. L'Agentification du Desktop (Cowork vs Code)
Imaginez que vous avez un ingénieur très intelligent mais qui ne parle que le langage "Terminal" (c'est Claude Code). Maintenant, imaginez qu'on donne à cet ingénieur un visage, des mains et un bureau graphique pour qu'il puisse aider le commun des mortels : c'est Claude Cowork. Cowork est une application macOS (sandboxée, donc dans une "bulle de sécurité" virtuelle) couplée à une extension Chrome. Il ne nécessite aucune compétence en développement. Contrairement à Claude Code qui peut exécuter des scripts puissants et dangereux sur votre système de base, Cowork agit dans un environnement restreint. Vous discutez avec lui dans une interface classique, mais il a la capacité "physique" de déplacer vos dossiers, de lire vos fichiers et de contrôler votre navigateur. C'est l'IA qui passe du simple chat à la souris de votre ordinateur.

### 2. Le Protocole d'Organisation Cognitive Automatisé
Si vous donnez une boîte remplie de milliers de papiers en vrac à un humain, il mettra des jours à tout trier. Claude Cowork agit comme un archiviste sur-vitaminé. Dans la vidéo, Shubham lui donne accès à un dossier "Téléchargements" contenant plus de 4300 fichiers hétéroclites (zip, DMG, factures, captures d'écran). L'agent commence par scanner les extensions et les métadonnées pour cartographier le chaos. Ensuite, il propose un "Plan d'Action" clair (créer des dossiers par types de médias, isoler les factures, regrouper les installeurs). Ce qui est brillant, c'est son approche sécuritaire : il ne supprime **rien**. S'il ne peut pas classer un élément, il le place dans un dossier `uncategorized`. L'agent manipule le système de fichiers en tâche de fond (via des commandes bash invisibles pour l'utilisateur).

### 3. "Browser Piloting" et Extraction d'Expertise (MCP)
C'est ici que l'IA devient littéralement vos yeux et vos mains sur internet. Grâce à l'architecture MCP (Model Context Protocol), Claude Cowork peut ouvrir Google Chrome, naviguer de manière autonome, taper dans une barre de recherche ("Shubham Sharma en France") et analyser la page. Il procède par itérations visuelles : il prend une capture d'écran de votre profil LinkedIn, défile (scroll), reprend une capture, et synthétise le tout. Dans l'exemple, il a rédigé un audit d'amélioration de profil LinkedIn (expert en personal branding) et a généré un document Word avec un score global, notant que la description était obsolète et trop "autobiographique". C'est la fin du copier-coller manuel d'informations web vers les LLMs : l'agent vient chercher la donnée directement à la source.

### 4. Synthèse Multi-Modale et Création de Livrables (PPT, Excel)
Transformer des données éparses en un format exécutif (Executive Summary). L'IA est capable d'enchaîner les opérations de traduction de formats. D'abord, on lui demande de lire un audit texte, puis on exige : "Fais-moi des slides PPTX avec une reco de style minimaliste à la Apple". L'agent va écrire des scripts transitoires (Javascript, HTML), installer des navigateurs headless comme Playwright si besoin, compiler le tout et exporter un fichier `.pptx` lisible et correctement structuré. De la même manière, face à 104 factures, l'agent écrit seul un script Python (`script.py`) pour lire les PDF, catégoriser les fournisseurs et les montants, et générer un tableau structuré (pour Google Sheets / Excel). L'IA pallie ses propres limites d'outils par l'écriture de scripts jetables (Disposable Code).

### 5. Résilience par Contournement (Le Hack du "Frame-by-Frame")
C'est le concept le plus impressionnant pour un Technicien A3 : la résilience algorithmique face à l'échec. Lorsqu'on demande à Cowork d'analyser une vidéo mp4 pour en extraire l'audio via Whisper afin de créer un "Lead Magnet", il se heurte à des blocages réseau (modèles bloqués). Au lieu d'abandonner et d'afficher une erreur, l'agent change de paradigme. Il décide de découper visuellement la vidéo frame par frame, d'utiliser l'OCR (Reconnaissance Optique de Caractères) pour lire les sous-titres incrustés sur le visage du créateur, de reconstituer la transcription exacte de la vidéo, puis de générer le code d'une Landing Page parfaite pour capturer des emails. C'est l'essence de l'intelligence agentique : **trouver un chemin alternatif quand le chemin principal est mort.**

---

## 🛠️ Matrice TVR (Time-Value-Resources)

- **Time (Temps d'exécution) :** Élevé pour l'outil (5 à 10 minutes pour des tris de dossiers complexes, des bugs de scroll nécessitant de scroller manuellement pour voir la fin de la réponse). Économie drastique pour l'humain (plusieurs heures économisées).
- **Value (Impact) :** Massive pour les tâches administratives répétitives (tri de factures, rangement de bureau, création de la V0 de présentations ou de landing pages).
- **Resources (Outils/Argent) :** App macOS "Claude" + Extension Chrome. **Attention au Paywall** : Le forfait "Pro" classique est rapidement insuffisant à cause de la consommation massive de tokens (images et scripts générés en boucle). Un plan "Max" (environ 100$/mois) est la réalité pour un usage intensif de ce type d'agents.
- **Plan d'Action (D.E.A.L) :**
  - **Define :** Identifier les "trous noirs" de productivité (dossiers Téléchargements chaotiques, compilation mensuelle des factures, audits de profils manuels).
  - **Eliminate :** Le copier-coller d'informations depuis le navigateur, la transcription manuelle de données PDF vers Excel.
  - **Automate :** Utiliser des agents Desktop pour générer les V0 de livrables (slides, scripts de nettoyage).
  - **Liberate :** Libérer le temps de cerveau disponible de l'A0 et de ses équipes pour l'analyse stratégique plutôt que la compilation mécanique.

---

## 🧩 Ancrage Souverain (Domaine 08_People)

Cette ressource est un pilier stratégique pour la **Green Lantern Squad (08_People)** car elle démontre l'autonomisation des profils "Non-Devs".

- **Vision (Prof X) :** Prof X observe l'avènement des assistants "Sandboxés". L'enjeu n'est plus d'apprendre à coder, mais d'apprendre à diriger un agent technique qui code pour soi (génération de scripts Python à la volée par Cowork). Cela modifie fondamentalement les critères de recrutement et la gestion des talents : l'emphase est mise sur la capacité de "Prompt Engineering" et de supervision.
- **Field (Cyclops) :** Tactique de terrain pure. Cyclops peut déployer ces paradigmes pour "nettoyer le champ de bataille". Des dossiers d'assets désordonnés ou des factures éparpillées sont instantanément restructurés par des directives simples : "Classe-moi le dossier X, ne supprime rien, fais un log Excel". L'exécution est asynchrone (on lance et on laisse tourner pendant 10 minutes).
- **Empathy (Jean) :** L'entropie numérique (le bordel dans les dossiers) crée une forte charge mentale. En déléguant le rangement "ingrat" à l'IA, Jean sécurise la santé mentale et le bien-être numérique de l'A0. Cowork agit comme un tampon entre l'humain et le chaos de la donnée.
- **Knowledge (Beast) :** Beast analyse la méthode de "contournement" de l'IA (lecture OCR frame par frame pour éviter un blocage API). C'est une révélation pour nos propres pipelines d'ingestion (Memory Core). Beast peut utiliser cette logique pour concevoir des systèmes de fallback : si l'API A échoue, passe par une analyse visuelle de la donnée (Vision Model).

**Impact direct pour A0 (Amadeus) :** A0 n'a plus à toucher à ses dossiers locaux (Downloads, factures). Le temps dégagé par cette sous-traitance à la machine permet de scaler l'empire sans recruter de main-d'œuvre administrative. C'est l'essence du *Life OS* : la machine entretient la machine.

---

## 📝 Résumé Détaillé de la Transcription

### 1. La Promesse et l'Écosystème Anthropique (Le Piège du Paywall)
- **Le Contexte :** Anthropic a sorti des outils spécialisés. *Claude* (Chatbot public classique) et *Claude Code* (Agent pour les développeurs s'exécutant dans le terminal, générant plus d'un milliard d'occurrences). Pour toucher le public non-technique, ils ont lancé **Claude Cowork**.
- **Fonctionnement :** C'est une application macOS (non disponible sur Windows) qui s'exécute dans un environnement virtuel restreint (une mini-VM sandboxée). Cela garantit la sécurité : l'IA ne peut pas "casser" l'OS natif. Une extension (*Claude Chrome*) lui sert de pont pour naviguer sur le web.
- **Le modèle économique :** > *"il y a un piège là-dedans, c'est que le plan pro, il est pas du tout suffisant pour pouvoir utiliser [Cowork]... c'est clairement une technique pour pouvoir faire passer les gens sur Cloud Max."* L'outil consomme énormément de contexte et de requêtes, forçant l'upgrade (100$/mois).

### 2. Nettoyage et Organisation du File System (L'Archiviste)
- **Use Case 1 : Le dossier Photos.** L'agent liste les fichiers, repère les extensions, identifie les doublons et les images au nom similaire. Il propose un plan d'action validé par l'utilisateur (le bouton "Go"). L'agent crée des dossiers, déplace les images et place les éléments complexes dans un dossier `uncategorized`. Il refuse de supprimer de la donnée de son propre chef.
- **Use Case 2 : Le dossier Téléchargements (Downloads).** Avec plus de 4300 fichiers, l'IA sépare les factures (Invoices), les images disques (DMG), les archives (ZIP).
- **Problématique UX :** > *"ça prend une plombe. Euh ça prend hyper longtemps pour que Claude navigue, aille regarder vos fichiers, rédige des scripts..."* Le processus est lent et nécessite de scroller manuellement l'interface pour lire les updates de l'agent.

### 3. Navigation Autonome et Extraction de Data (LinkedIn & PPT)
- **Use Case 3 : Audit LinkedIn.** L'IA utilise son connecteur Chrome, ouvre le navigateur, recherche "Shubham Sharma en France" et analyse les expériences professionnelles en scrollant et en prenant des captures d'écran. Elle dresse un audit critique (document DocX) : manque de "Call to Action", description trop autobiographique, etc.
- **Use Case 4 : Génération de Présentation.** Sur la base de l'audit, l'agent reçoit l'ordre de créer un PowerPoint au style minimaliste Apple. Il code dynamiquement des scripts JS/HTML pour générer le design puis le compile en PPTX.
- **Les Limites de l'Interface Système :** Quand l'auteur demande à Cowork d'uploader la présentation sur *Google Slides*, l'agent échoue systématiquement. Il ne parvient pas à interagir avec la boîte de dialogue native du Finder macOS (le pop-up d'upload). L'auteur conclut que l'automatisation totale ("je pars et ça travaille") n'est pas encore là.

### 4. La Résilience Algorithmique (Factures & OCR Vidéo)
- **Use Case 5 : Synthèse Comptable.** L'IA écrit un script Python pour parser 104 factures PDF. Lorsqu'une erreur survient (ex: des fournisseurs mal classés dans la catégorie 'Télécom'), l'agent modifie son propre code de manière itérative jusqu'à produire un tableau de données propre, importable dans Google Sheets.
- **Use Case 6 : Le Lead Magnet (Landing Page).** Le testeur demande à convertir une vidéo Instagram en Lead Magnet. L'agent bloque sur l'extraction audio (modèle Whisper indisponible). Sa solution de contournement est stupéfiante : il découpe la vidéo image par image, utilise un modèle de Vision pour lire les sous-titres incrustés dans la vidéo par le créateur, reconstitue 100% de la transcription texte, et code une landing page HTML/CSS à partir de ce contenu. 
- **Conclusion de l'auteur :** > *"L'artefact [est] impressionnant... on est encore au moment démo. Clairement, je suis conscient de ça, c'est qu'ils ont lancé un truc en 10 jours... c'est assez game changer pour eux."* Le produit transpire l'avenir du travail, mais réclame de la patience vis-à-vis des limitations actuelles (vitesse, bugs UX).

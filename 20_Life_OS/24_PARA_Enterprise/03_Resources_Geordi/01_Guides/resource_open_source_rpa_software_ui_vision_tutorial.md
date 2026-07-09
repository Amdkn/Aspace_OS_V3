# 🧿 Guide Geordi Resource — Open-Source RPA Software - Ui.Vision Web and Desktop Automation Tutorial

## 🧬 Métadonnées
- **ID Vidéo** : YT-yzVc13QdGxw
- **Titre** : Open-Source RPA Software - Ui.Vision Web and Desktop Automation Tutorial
- **Chaîne** : Ui.Vision, AI & OCR
- **Serendipity Score** : 7/10
- **Catégorie** : AI / RPA / Automation / Open Source Software
- **Date de Clarification** : 2026-05-24
- **Statut** : CLARIFIED_PLANE

---

## 1. Concepts Clés (Concepts Clés)

L'automatisation robotique des processus (RPA) par le biais de solutions open-source comme **Ui.Vision** est un pilier de la souveraineté opérationnelle et de l'efficacité administrative des organisations modernes.

### L'Automatisation Robotique des Processus (RPA)
Le RPA désigne la technologie qui permet à un agent logiciel (un "robot") de reproduire à l'identique les actions d'un opérateur humain sur une interface graphique d'ordinateur. Le robot simule les clics de souris, les frappes de clavier, navigue sur des sites web, extrait des données de formulaires et interagit avec des applications de bureau. Contrairement aux intégrations par API, le RPA n'exige aucune modification du système cible ; il agit comme un utilisateur virtuel, ce qui permet d'automatiser des systèmes anciens (legacy) ou des plateformes tierces dépourvues de passerelles de programmation.

### Reconnaissance Visuelle par Ordinateur (Computer Vision & OpenCV)
La force d'Ui.Vision par rapport aux extensions de navigateur classiques (comme Selenium) réside dans son moteur de vision par ordinateur basé sur la bibliothèque **OpenCV**. Au lieu de s'appuyer uniquement sur le code source HTML (les sélecteurs XPath ou CSS) qui peut changer d'un jour à l'autre et briser le script, le robot d'Ui.Vision analyse visuellement l'écran. Il cherche des patterns graphiques (ex: l'image d'un bouton de validation) et clique précisément dessus. Cela lui permet d'automatiser des interfaces de bureau, des animations Flash/Canvas complexes, et de s'affranchir des modifications mineures du code HTML sous-jacent.

### Reconnaissance Optique de Caractère (OCR) par IA
L'intégration de moteurs OCR avancés (locaux ou cloud) permet au robot de lire et d'extraire du texte directement à partir d'images à l'écran. Cette fonctionnalité est cruciale pour automatiser la lecture de factures au format PDF, de reçus numérisés, de captures d'écran, ou pour valider l'affichage correct d'un message système dans des environnements d'applications de bureau non-accessibles par le biais de sélecteurs de code.

### Automatisation Hybride Web & Desktop
Ui.Vision propose un pont transparent entre l'automatisation dans le navigateur web et l'automatisation du système d'exploitation hôte (le bureau Windows/Linux/macOS). Grâce à un module d'intégration natif léger (XModules), le robot peut extraire des données d'un portail web public, ouvrir un classeur Excel local sur la machine, saisir les données extraites, puis lancer un script PowerShell ou Bash système pour sceller l'opération.

---

## 2. Entités & Outils (Entités & Outils)

L'écosystème d'Ui.Vision regroupe plusieurs logiciels, protocoles et structures d'instructions.

### Architecture Matérielle & Logicielle
- **Ui.Vision RPA Core (Extension)** : L'extension officielle disponible pour Google Chrome, Mozilla Firefox et Microsoft Edge, servant d'EDI (Environnement de Développement Intégré) visuel local pour concevoir et tester les macros.
- **XModules** : Composants natifs optionnels mais indispensables pour l'automatisation du bureau. Ils gèrent la simulation de bas niveau de la souris/clavier et la vision par ordinateur locale sans passer par le bac à sable du navigateur.
- **Moteur OpenCV Intégré** : L'algorithme mathématique de détection de formes et de patterns graphiques qui analyse l'écran à la recherche des images cibles fournies par l'utilisateur.

### Structure d'une Macro (JSON Scripting)
- **Commandes (Commands)** : Les verbes d'action du robot (ex: `click`, `type`, `open`, `visualVerify`, `storeText`).
- **Cibles (Targets)** : L'endroit où s'applique l'action. Il peut s'agir d'un sélecteur XPath (`xpath=//*[@id="submit"]`), d'une image de référence enregistrée (`submit_button.png`) ou de coordonnées de pixels précises (`x,y=150,300`).
- **Valeurs (Values)** : Les données d'entrée ou les variables (ex: le texte à saisir dans un champ de texte).

---

## 3. Synthèse Pratique (Synthèse Pratique)

La création d'une macro robuste avec Ui.Vision exige une approche méthodique pour garantir que le robot fonctionne de manière autonome sans planter au moindre imprévu.

### Processus pas à pas de Conception d'un Script RPA
Le concepteur ouvre l'EDI d'Ui.Vision dans son navigateur. Il lance l'enregistreur de macro (Record) et effectue la tâche manuellement sur le site web ou le bureau. Ui.Vision capture automatiquement les actions et génère les lignes de commandes correspondantes. Une fois l'enregistrement brut terminé, le concepteur doit nettoyer le script : remplacer les sélecteurs XPath automatiques trop fragiles par des sélecteurs robustes ou des images de vision par ordinateur pour les boutons critiques.

### Gestion des Attentes (Waits) et des Exceptions
La principale cause d'échec des scripts d'automatisation est la vitesse variable de chargement des pages ou des applications. Si le robot tente de cliquer sur un bouton avant que celui-ci ne soit affiché, le script plante. Ui.Vision résout ce problème en introduisant des instructions d'attente intelligentes. Par exemple, la commande `click` attend implicitement que l'élément cible apparaisse à l'écran pendant un délai maximal configurable (timeout). Pour les étapes hautement sensibles, l'usage de commandes explicites comme `waitForVisible` ou `visualVerify` garantit que le système est dans l'état attendu avant de poursuivre.

### Analyse de Friction et Résolution de Problèmes
1. **Les changements d'échelle d'affichage (DPI)** : La vision par ordinateur d'OpenCV peut échouer si le script a été enregistré sur un écran 4K et est exécuté sur un écran 1080p. Il est crucial de standardiser la résolution d'écran des machines virtuelles de production.
2. **La gestion des cookies et des CAPTCHAs** : Les CAPTCHAs bloquent par définition les robots RPA. Ui.Vision permet d'intégrer des API de résolution de CAPTCHAs tiers ou d'introduire des pauses manuelles dans le script pour laisser un opérateur humain résoudre l'énigme avant que le robot ne reprenne la main automatiquement.

---

## 4. Actionnabilité (D.E.A.L) (Actionnabilité)

Comment exploiter Ui.Vision RPA pour automatiser nos tâches d'infrastructure et de gestion administrative souveraines dans A'Space OS ?

### D — Definition (Définition)
- **Objectif** : Identifier et formaliser les processus manuels répétitifs éligibles au RPA.
- **Actions** :
  1. Lister toutes nos corvées quotidiennes de gestion (ex: se connecter à notre console d'hébergement Hostinger, récupérer la facture mensuelle, la renommer et la téléverser sur notre espace de stockage).
  2. Rédiger le diagramme logique (workflow) précis de chaque étape du processus pour s'assurer qu'il est 100% déterministe.
  3. Déterminer si le processus peut être automatisé par des sélecteurs HTML ou nécessite l'activation de la vision par ordinateur Desktop (via XModules).

### E — Elimination (Élimination)
- **Objectif** : Éliminer la perte de temps humain sur des tâches administratives à faible valeur ajoutée.
- **Actions** :
  1. Éliminer la saisie manuelle de données redondantes en créant des robots Ui.Vision de transfert d'informations entre nos applications.
  2. Supprimer la dépendance à des plateformes RPA cloud payantes et propriétaires extrêmement chères (comme UiPath ou Power Automate Desktop) au profit de la solution open-source locale et souveraine d'Ui.Vision.
  3. Proscrire les scripts d'automatisation fragiles : éliminer les sélecteurs XPath dynamiques instables qui changent à chaque rafraîchissement au profit d'identifiants uniques (IDs) ou de détection visuelle OpenCV stable.

### A — Automation (Automatisation)
- **Objectif** : Automatiser le déclenchement, l'exécution et le reporting de nos macros robotisées.
- **Actions** :
  1. Automatiser l'exécution de nos macros Ui.Vision en les programmant à l'aide de tâches planifiées Windows (Task Scheduler) ou de cron jobs Linux sous WSL, en passant par l'interface en ligne de commande (CLI) de l'extension de navigateur.
  2. Configurer des scripts de récupération automatique après échec : si une macro plante à l'étape 5, le robot doit automatiquement faire une capture d'écran de l'erreur, fermer le navigateur, et envoyer une alerte sur notre canal Telegram.
  3. Automatiser l'OCR pour extraire les données de facturation directement depuis les documents PDF téléchargés mensuellement.

### L — Liberation (Libération)
- **Objectif** : Se libérer complètement des tâches numériques répétitives pour consacrer 100% de notre temps de cerveau à des projets de haute ingénierie stratégique.
- **Actions** :
  1. Gagner plusieurs heures par semaine de liberté opérationnelle en confiant nos flux de paperasse et de rapports de surveillance à notre armée de robots virtuels Ui.Vision.
  2. Assurer la souveraineté totale de nos données en exécutant l'ensemble de nos automatisations en local sur notre machine physique sans qu'aucune donnée d'entreprise ne transite par des serveurs tiers.
  3. Libérer le potentiel fonctionnel de nos anciens outils non dotés d'API en leur fabriquant de manière externe une passerelle d'automatisation intelligente et robuste.

---

## 5. SOP Opérationnelle de Création et de Planification d'une Macro Web RPA

```text
[SOP-UIVISION-MACRO]
1. Préparation de l'Environnement : Ouvrir Google Chrome. Lancer l'extension Ui.Vision RPA en cliquant sur son icône. Créer une nouvelle macro nommée `AUT_HOSTINGER_INVOICES`.
2. Enregistrement Initial : Cliquer sur le bouton "Record" dans l'EDI d'Ui.Vision. Dans le navigateur, effectuer la séquence manuellement : se connecter au portail Hostinger, naviguer vers l'historique de facturation, et cliquer sur le bouton de téléchargement de la dernière facture. Cliquer sur "Stop" dans l'extension.
3. Nettoyage et Consolidation : Parcourir les lignes générées dans l'EDI d'Ui.Vision. Remplacer les sélecteurs de clic fragiles par des cibles robustes de type `id=xxx`. Pour le bouton de téléchargement, capturer une image précise de l'icône de téléchargement et remplacer la cible par le chemin de l'image de référence OpenCV (`download_icon.png`).
4. Intégration de la Gestion d'Erreur : Ajouter en début de macro la commande `store | true | !errorignore` pour s'assurer que le script continue d'autres opérations ou s'arrête proprement en cas d'erreur bloquante. Ajouter des commandes `waitForPageToLoad` aux étapes critiques.
5. Test de Stabilité : Exécuter la macro en boucle 5 fois d'affilée en mode lent (Play Macro) pour s'assurer qu'aucun timing ne pose problème et que la facture est correctement enregistrée dans le dossier des téléchargements locaux.
6. Planification par CLI : Rédiger un script PowerShell local `run_rpa.ps1` qui lance Chrome en ligne de commande avec les arguments requis pour exécuter la macro Ui.Vision de manière invisible et fermer le navigateur à la fin (ex: `start chrome "file:///C:/.../ui.vision.html?macro=AUT_HOSTINGER_INVOICES&direct=1&closeRPA=1"`). Programmer l'exécution de ce script tous les 1ers du mois via le Planificateur de Tâches Windows.
```

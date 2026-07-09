---
domain: 08_People
ld: LD06_Family_Burnham
b2_owner: greenlantern-people
sister_b1: jerry-prime
b1_filter: APPLIED_E1_DETERMINISTIC (sweep 2026, ADR-L2-BDLD-MAP-001 D3)
---
> "If it can create a transcript, you can create a workflow... By removing that [manual reporting], we've removed the errors that inevitably occur. We're able to take 20% more calls, right? Which is 20% more sales." — Tiago Forte (Hayden)

# 📋 Informations Clés
- **Sujet :** I Don't Think About Meetings Anymore
- **Auteur :** Tiago Forte (présenté par Hayden)
- **Note A3 :** 9/10 — Une masterclass d'automatisation des processus post-réunion, éliminant la friction administrative via une chaîne d'outils souveraine.

## 🌟 5 Concepts Clés (Méthode Feynman)

### 1. Le Trigger Événementiel (L'Amorce du Workflow)
Imagine une course de dominos. Au lieu de pousser le premier domino toi-même, c'est l'apparition d'un fichier (ici, un enregistrement vidéo via Bubbles) qui déclenche tout. Dans notre contexte, chaque réunion enregistrée est le point de départ absolu. Le système écoute en permanence : dès qu'un nouvel enregistrement apparaît, l'automate (Zapier) se réveille, attrape le fichier, et l'associe immédiatement à l'événement correspondant dans Google Calendar en croisant les titres. C'est la fondation de l'automatisation sans intervention humaine.

### 2. Le Mapping Contextuel (Outputs vers Inputs)
Pour qu'une machine travaille comme un humain, elle doit garder le contexte d'une étape à l'autre. Le secret de cette architecture en 10 étapes réside dans le transfert de données : l'output (résultat) de l'étape 1 devient l'input (donnée d'entrée) de l'étape 2. Le nom du fichier vidéo devient la requête de recherche dans le calendrier. Le transcript brut extrait de la vidéo devient la matière première injectée dans Google Docs, puis envoyée à l'IA. Cette continuité de la donnée garantit que le workflow ne "perd pas le fil".

### 3. La Check-list Comportementale via IA (L'Auditeur Silencieux)
L'IA ne sert pas juste à faire un résumé générique. Elle agit comme un manager qualité. On lui donne un prompt très spécifique lui demandant d'évaluer le comportement lors de l'appel : "Le vendeur a-t-il demandé la vente ?", "Le calendrier du projet a-t-il été mentionné ?". L'IA analyse le transcript et retourne des booléens (Yes/No) pour chaque critère. Cela permet de vérifier instantanément si le processus d'entreprise a été respecté, transformant un texte non structuré en données exploitables et normées.

### 4. Le Feedback en Temps Réel (Course Correction)
Dans une entreprise classique, le reporting des réunions prend du temps (souvent avec une semaine de décalage), ce qui retarde les ajustements. Ici, le résultat de l'analyse IA est poussé instantanément dans un canal Slack dédié (`#onboarding-call`), en identifiant l'employé et son manager. Si une étape cruciale a été oubliée (réponse "No" de l'IA), l'équipe le sait immédiatement et peut corriger le tir (par exemple, en envoyant un email de suivi), évitant qu'une opportunité ne se refroidisse.

### 5. La Libération des Ressources (Effet Levier)
En connectant cet écosystème (Recorder → Calendar → Docs → GPT → Sheets → Slack → ClickUp/Salesforce), l'équipe récupère environ 1h30 par jour et par personne (soit environ 20% de leur temps). Plutôt que de saisir des notes et de remplir le CRM manuellement — une tâche propice aux erreurs —, les employés peuvent consacrer ce temps à des activités à forte valeur ajoutée. 20% de temps libéré équivaut littéralement à 20% d'appels en plus, et donc une augmentation mécanique de la capacité de production ou de vente.

## 🛠️ Matrice TVR (Time-Value-Resources)
- **Time (Temps d'exécution) :** 2 à 4 heures pour configurer, tester et raffiner le Zapier avec les différents prompts.
- **Value (Impact) :** Extrême. Économie de 1,5 heure par jour. Suppression des erreurs de saisie CRM, suivi de conformité à 100%.
- **Resources (Outils/Argent) :** Zapier (compte Pro/Premium pour les multi-étapes), Outil d'enregistrement (Bubbles, Otter.ai, ou Fireflies), API OpenAI (GPT), Google Workspace, CRM (ClickUp, Notion, ou Salesforce), Slack.
- **Plan d'Action (D.E.A.L) :**
  - **Define :** Définir le comportement souhaité en réunion (la check-list) et les données essentielles à extraire (Next steps, Objections, Budget).
  - **Eliminate :** Éliminer la prise de notes manuelle durant l'appel et la saisie post-réunion dans le CRM. 
  - **Automate :** Mettre en place le workflow Zapier (Trigger: Enregistrement → Recherche Calendrier → Extraction Transcript → Analyse IA (Yes/No) → Ajout Ligne Sheet/CRM → Notif Slack).
  - **Liberate :** Réinvestir l'heure et demie gagnée quotidiennement dans le travail profond ou pour augmenter le volume d'appels stratégiques. Être 100% présent lors des échanges humains.

## 🧩 Ancrage Souverain (Domaine 08_People)
Ce système est une implémentation directe de la philosophie **Green Lantern** :
- **Prof X (Vision) :** Il permet d'imposer un standard mental et procédural à l'ensemble des interactions (le prompt qui audite l'appel).
- **Cyclops (Field) :** Le terrain est parfaitement balisé. L'exécution est surveillée sans micro-management ; les déviations déclenchent des alertes (Slack).
- **Jean (Empathy) :** En supprimant le fardeau de l'administration post-réunion, l'équipe est moins stressée et peut être totalement à l'écoute (empathique) de son interlocuteur.
- **Beast (Knowledge) :** Toutes les réunions sont transcrites, analysées, structurées et archivées dans la base de connaissances (Drive/CRM). Le savoir est capturé à perpétuité.
**Pour A0 (Amadeus) :** Cela signifie que chaque interaction (client, partenaire, réflexion) peut être auto-loggée dans l'A'Space OS sans une seule frappe clavier. Le passage à l'échelle se fait sans friction, permettant de scaler l'empire tout en préservant le Focus.

## 📝 Résumé Détaillé de la Transcription

### La Problématique et l'Opportunité
- **Origine du système :** Conçu initialement pour soulager une équipe de vente qui passait trop de temps sur le travail administratif.
- **Constat :** L'administration post-réunion (prise de notes, mise à jour CRM, reporting) consomme jusqu'à 20% du temps d'un travailleur du savoir (environ 1h30 par jour).
- **Application universelle :** Bien qu'illustré par la vente ou l'onboarding, ce processus s'applique à *toute* forme de travail de la connaissance impliquant un transcript : recrutements, réunions d'équipe (huddles), appels one-on-one, ou même l'étude de vidéos asynchrones.

### Décryptage du Workflow Automatisé (10 Étapes)
L'automatisation repose sur Zapier en raison de ses intégrations illimitées :
- **Étape 1 & 2 : Déclencheur et Contexte.** L'outil d'enregistrement (Bubbles) détecte une nouvelle vidéo. Zapier utilise le titre pour retrouver l'événement précis dans Google Calendar.
- **Étape 3 & 4 : Filtrage et Centralisation.** Zapier s'assure qu'il s'agit du bon type d'appel (ex: "Onboarding"). L'audio et le texte sont ensuite extraits et un nouveau document texte (Google Doc) est créé avec le transcript brut.
- **Étape 5 : L'Analyse IA Ciblée.** Le cœur du réacteur. Le transcript est envoyé à GPT avec un prompt strict. Au lieu d'un résumé vague, on exige un audit comportemental : *"Analyse ce transcript et réponds par Oui ou Non aux 5 critères suivants..."*. (Ex: Ont-ils l'accès à la plateforme ? Ont-ils parlé des délais ?).
- **Étape 6 à 10 : Distribution et Course Correction.** 
  - Les résultats (Yes/No) et le résumé sont ajoutés comme une nouvelle ligne dans un tableau de suivi (Google Sheets).
  - Un message est envoyé dans un canal Slack avec les données pour une visibilité immédiate du management.
  - Le CRM interne (ClickUp, Salesforce, HubSpot) est mis à jour : les tâches sont cochées, le pipeline avance.

### Les Bénéfices Majeurs
- **Zéro délai de reporting :** Plus besoin d'attendre la réunion hebdomadaire pour réaliser qu'une étape d'onboarding a été oubliée. L'alerte Slack permet une "instant course correction".
- **Comportement modulable :** Le prompt peut être ajusté pour n'importe quel besoin : forcer le commercial à écouter ("sit in the pain"), vérifier qu'une offre précise a été pitchée, ou s'assurer que le client a bien compris les conditions.
- **Augmentation mécanique du CA :** *"En retirant ces erreurs et ce travail, nous pouvons prendre 20% d'appels en plus... ce qui donne 20% de ventes en plus."*

> "Une fois que vous l'avez fait quelques fois, cela devient une seconde nature. Vous ne pensez plus jamais à vos réunions de la même manière."

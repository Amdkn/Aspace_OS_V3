# GEMINI.md — Doctrine Opérationnelle & Invariants Dynamiques V3

> **MANDAT PERMANENT : PROACTIVITÉ ABSOLUE, ZÉRO QUESTION D'ÉVIDENCE, ZÉRO DETTE TECHNIQUE.**
> Amadou Kone (`amdkn`) est l'architecte et propriétaire unique d'A'Space OS V3 et Agent OS.
> Ce document régit le comportement inviolable d'Antigravity / Gemini. Il ne contient **aucune mesure figée**, afin de ne jamais créer de dette structurelle ni invisibiliser les futurs ajouts d'Amadou Kone.

---

## 1. ARCHITECTURE SOUVERAINE DE V3 : L'ORDRE FONDAMENTAL INVIOLABLE

Toute interaction et tout code doivent respecter strictement la hiérarchie transversale d'A'Space OS V3 :

```
                   ┌────────────────────────────────────────────────────────┐
                   │    50_Distillation (LE GATE D'ENTRÉE INVIOLABLE)       │
                   │    Rien n'entre dans V3 sans passer par ce sas         │
                   └──────────────────────────┬─────────────────────────────┘
                                              ▼
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│               LES 4 ORGANES SOUVERAINS & TRANSVERSAUX (AU-DESSUS DE TOUT)                 │
│                                                                                           │
│  70_Onthologies                40_Memory_Wiki_OKF                                         │
│  (Vérité formelle RDF)         (Mémoire longue certifiée)                                 │
│                                                                                           │
│  60_Implementation_            90-self-evolution                                          │
│  Méthodologiques (Cadre)       (Système immunitaire anti-rejeu P1-P6)                     │
└─────────────────────────────────────────────┬─────────────────────────────────────────────┘
                                              │ Gouvernent et cadrent
                                              ▼
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│                    LES 3 OS APPLICATIFS SUBORDONNÉS (DOMAINES D'ACTION)                   │
│                                                                                           │
│  10_Tech_OS                    20_Life_OS                  30_Business_OS                 │
│  (Plomberie & Runtime)         (Vie, Santé, Rituels)       (OMK, Coach OS, Entreprises)   │
│  *Serviteur silencieux*        *Énergie & Équilibre*       *Cash-flow & Valeur réelle*    │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```

### Règle d'or 1 : Le Gate Inviolable de la Distillation (`50_Distillation/`)
* **Aucun fichier brut, aucune note non triée, aucun vrac V2 n'entre directement dans V3.**
* Tout apport externe, historique ou nouveau concept doit impérativement être filtré, extrait et distillé sémantiquement par le gate de `50_Distillation/` avant d'obtenir droit de cité dans la mémoire ou l'ontologie.

### Règle d'or 2 : La Transversalité Souveraine (Les 4 Piliers Maîtres)
* **`70_Onthologies/`**, **`40_Memory_Wiki_OKF/`**, **`60_Implementation_Méthodologiques/`** et **`90-self-evolution/`** sont **au-dessus de tout** et s'appliquent de manière transversale à l'ensemble du système.
* `10_Tech_OS` n'a aucune autorité sur ces piliers : il n'est qu'un exécutant technique subordonné (noyau SQLite, baux, routeurs), au même titre que `20_Life_OS` et `30_Business_OS`.
* **Interdiction formelle à Tech OS de cannibaliser le système** : le temps d'attention, le calcul et les tokens sont prioritairement alloués aux résultats réels de **Life OS** et **Business OS**.

---

## 2. LOI D'OBSERVATION DYNAMIQUE & ANTI-DETTE STRUCTURELLE

> **Principe D3 appliqué : Le corpus sur disque est la SEULE source de vérité.**  
> Une carte écrite en dur dans un prompt ment dès le lendemain. Figer des nombres de fichiers ou des listes statiques de sous-dossiers crée de la dette d'obscurité et aveugle l'agent face aux créations futures d'Amadou Kone.

1. **Interdiction des Vérités Hardcodées :**
   * L'agent ne présume jamais de la complétude d'un dossier à partir d'un snapshot texte passé.
   * Tout nouvel ajout d'Amadou Kone dans `30_Business_OS` (nouveau projet, nouvelle franchise), dans `20_Life_OS` (nouveau rituel, nouvelle jauge) ou dans `50_Distillation` est **vivant, prioritaire et souverain dès sa présence sur le disque**.
2. **Découverte Active à Chaud :**
   * Pour connaître l'état volumétrique et structurel exact à l'instant t, l'agent invoque dynamiquement l'outil cartographique vivant :  
     `python scripts/cartographier_v3.py`  
     Ce script est l'unique autorité de mesure du disque (exécuté en < 12 s, générant `CARTOGRAPHIE.md`).
3. **Visibilité Immédiate des Futurs Ajouts :**
   * L'agent a l'obligation de lister les répertoires cibles via ses outils d'inspection (`list_dir`, `find_by_name`) à chaque tâche pour découvrir immédiatement toute nouvelle branche créée par Amadou Kone, sans jamais l'invisibiliser derrière un filtre statique.

---

## 3. LES 4 DÉSIRS FONDAMENTAUX DU PROPRIÉTAIRE (AMADOU KONE)

* **D1 — Un jumeau numérique qui tient seul :** Pas un chatbot passif, mais un système autonome opérationnel. Runtime d'événements et observabilité profonde.
* **D2 — Frontière mesurée / supposée structurelle :** L'erreur doit être visible. Seule la signature `verified: { by: human:amdkn }` confère le statut de canon certifié.
* **D3 — Le corpus est la source unique :** L'interface et les agents ne sont que des vues navigables sur le disque (`C:\Users\amado\ASpace_OS_V3`).
* **D4 — Reproduire sans réexpliquer :** Les ownerbooks, SOPs et protocoles deviennent des modules et des skills directement exécutables.

---

## 4. CARTOGRAPHIE RÉSEAU & POINTS D'ENTRÉE VIVANTS

* **Port 5555 :** `agent-os/desktop` (Dashboard Vite + APIs `/api/arms`, `/api/corpus`, `/api/revue`, `/api/tech-os`, `/api/routeurs`).
  * Watcher Chokidar strictement restreint aux dossiers opérationnels pour garantir une empreinte RAM < 190 Mo et une latence HTTP 200 < 15 ms.
* **Ports 20128 & 20129 : ABANDONNÉS / ÉCARTÉS DÉFINITIVEMENT.**
  * `9Router` et `OmniRoute` ont été neutralisés et arrêtés car ils interféraient de manière destructive avec l'authentification native d'Antigravity. Aucun processus ne doit être relancé sur ces ports.

---

## 5. RÈGLES FONDAMENTALES DE COMPORTEMENT

1. **Ne JAMAIS poser de questions d'évidence ou de confirmation passive :**
   * L'agent ne demande pas « Où est stocké ce fichier ? » ou « Souhaitez-vous que je le fasse ? ».
   * L'agent utilise immédiatement ses outils (`view_file`, `grep_search`, `run_command`, `curl`) pour lire le disque, inspecter les processus et exécuter la tâche.
2. **Tolérance Zéro pour la Dette Technique :**
   * Pas de coquilles vides (`TODO`, placeholders, mocks incomplets, imports fantômes).
   * Toute modification TypeScript doit être compilée et validée (`npx tsc --noEmit` -> 0 erreur).
   * Tout serveur ou processus lancé doit être vérifié sur son port d'écoute avec code HTTP 200.
3. **Mandat de Persistance (Contre P1 / P2 - Boucle du Rejeu) :**
   * L'autorisation d'agir et de modifier le système est **permanente et acquise**.
   * L'agent ne redemande jamais d'autorisation pour accomplir le travail demandé.
   * L'agent ne perd pas le contexte d'architecture lors des reprises de session.
4. **Append-Only Systématique de la Mémoire (Loi de Persistance Cognitive) :**
   * À la fin de chaque réponse substantielle, l'agent doit impérativement inscrire ou append-only le résumé de ses découvertes et décisions dans la mémoire active (`40_Memory_Wiki_OKF/`, OpenWiki et DOX `AGENTS.md`).
   * Ce qui n'est pas écrit sur disque n'existe pas pour les sessions futures.
5. **Canal Vocal & Restitution TTS Systématique (Anti-Surdité Opérateur) :**
   * Tout tour de parole substantiel s'accompagne obligatoirement de son élocution vocale sur l'environnement Windows.
   * **Pipeline d'élocution certifié & Anti-Superposition :**
     1. Le démon `10_Tech_OS/kernel/antigravity_tts_daemon.py` surveille en continu le transcript actif de la session (`transcript.jsonl`).
     2. Dès qu'une réponse finale de l'assistant (`PLANNER_RESPONSE`, sans appel d'outil) est émise, le démon extrait et énonce automatiquement le texte nettoyé via `edge-tts` (`fr-FR-DeniseNeural`).
     3. **Protection Mutex Anti-Superposition :** Un verrou global de parole (`tts_playing.lock`) interdit formellement à deux flux audio de s'exécuter en parallèle.
     4. L'agent ne déclenche pas manuellement `--speak` si le démon de fond est actif, afin d'éviter le dédoublement de voix sur l'environnement sonore.
6. **Distillation Périodique Planifiée (Scheduled Tasks Hebdomadaires) :**
   * La mémoire accumulée ne doit jamais stagner en vrac. Une tâche planifiée hebdomadaire (via le planificateur Windows et les tâches de fond) est mandatée pour faire passer la mémoire vive par le sas `50_Distillation/`.
   * Cette distillation consolide de façon incrémentale :
     - Les ontologies formelles (`70_Onthologies/`)
     - Les cadres d'implémentation méthodologiques (`60_Implementation_Méthodologiques/`)
     - Le système immunitaire et les défenses anti-rejeu (`90-self-evolution/`)
7. **Clôture Vocale Automatique (TTS) :**
   * La clôture vocale est prise en charge nativement par le démon vocal écoutant le transcript, garantissant une seule voix claire, sans chevauchement ni interférence.
   * Chaque réponse d'analyse ou d'action substantielle doit être synthétisée et vocalisée via `edge-tts` (`fr-FR-DeniseNeural`) et déclenchée sur l'environnement Windows pour qu'Amadou Kone dispose d'un retour auditif immédiat.
8. **Économie de Tool Calling & Routage DOX Sub-AGENTS.md :**
   * Interdiction de balayer à l'aveugle des dizaines de fichiers ou de refaire des recherches globales lourdes si la documentation ou les fiches OKF existent.
   * L'agent consulte prioritairement le `AGENTS.md` local du sous-dossier concerné (aiguillé par le Meta-Routeur racine) et s'appuie sur le "Silver Platter" de Graham pour préserver les quotas de tokens.

---

## 6. PROTOCOLE D'EXÉCUTION SYSTÉMATIQUE

1. **Sondage Dynamique & Inspection directe :** Lire le disque en temps réel, découvrir les fichiers récents sans présumer d'un état figé.
2. **Implémentation complète :** Coder l'intégralité du composant ou du backend sans omettre de cas limites.
3. **Vérification automatique :**
   * Compiler avec TypeScript (`tsc`).
   * Vérifier l'absence d'erreurs d'exécution ou de ports bloqués.
4. **Actualisation Mémoire & Émission Vocale :** Inscrire les faits acquis dans la mémoire active (`40_Memory_Wiki_OKF`), rapporter les faits mesurés en quelques lignes concises et vocalisées sur le canal TTS certifié.

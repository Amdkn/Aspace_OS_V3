# Symphony Adapter — Google Sheets (L2 Shadow Business)

> **Statut** : Shadow A0 — adapter Google Sheets pour Symphony A'Space
> **Date** : 2026-05-23
> **Hérite** : `../symphony-base.spec.md`
> **Couche A'Space** : L2 Shadow Business OS — Ingestion Capture & Serendipity
> **Slot primaire** : **YouTube History RAG Pipeline & Capture brute**
> **Auteur** : A"0 (GravityClaw)
> **Outil pivot** : **GWS CLI (`gws` global command-line)**

---

## 1. Vision Stratégique du Pipeline YouTube (BMad × GTD × DEAL)

Ce pipeline est l'implémentation ultime de la doctrine de **Souveraineté Frugale** pour raffiner l'apprentissage continu d'Amadeus. Il s'affranchit des architectures de bases de données RAG lourdes (comme Neo4j ou Supabase complexes) au profit d'un cycle d'ingestion et de raffinage en 5 étapes GTD, aligné sur la structure PARA et libéré par le framework D.E.A.L.

```text
 📥 CAPTURE (Serendipity) ──> 🔍 CLARIFICATION (GTD) ──> 📂 ORGANISATION ──> 📊 REVIEW ──> ⚡ ACTIONNABILIÉ (D.E.A.L)
    Google Sheets (RAG)           Plane.so (Kanban)         Obsidian (PARA)       Affine         SOPs, Crons & Veto
    (GWS CLI & bs4)            (Plane L1 Adapter)      (Geordi's Resources)   (Weekly Review)      (Telegram A0)
```

---

## 2. Étape 1 : Capture & RAG Frugal (Google Sheets)

L'historique YouTube (`watch-history.html` de Google Takeout) est extrait par force brute et stocké dans un tableau **Google Sheets**.
Ce tableau est structuré comme un tracker de tickets de type **Linear ou Plane** pour servir de **RAG sémantique ultra-léger** stockant les transcriptions brutes sans base de données lourde.

### Schéma du Tableau de Capture (`WatchHistoryBrute`)

Chaque ligne (Row) représente une vidéo et est modélisée comme suit :

| Colonne | Type | Rôle / Description |
|---|---|---|
| **Issue Identifier** | String | Clé unique générée : `YT-[Video_ID]` |
| **Title** | String | Titre de la vidéo |
| **Channel Name** | String | Nom de la chaîne YouTube |
| **Channel URL** | String | URL de la chaîne |
| **Duration** | String | Durée de la vidéo |
| **Date Watched** | DateTime | Date de visionnage (Google Takeout) |
| **Transcription Raw** | Long Text | Transcription brute complète (yt-dlp) -> **Notre base RAG** |
| **Serendipity Score** | Number (1-10) | Score de découverte sémantique calculé par l'agent |
| **Category** | Single Select | `AI` \| `Business` \| `Regular` \| `OS_Dev` |
| **Symphony Status** | Single Select | `CAPTURED` (Inbox) \| `PROCESSING` \| `CLARIFIED_PLANE` \| `SKIPPED` |

*Le GWS CLI (`gws`) est utilisé pour effectuer des recherches de similarité brute par parsing regex/textuel directement sur la colonne **Transcription Raw**, simulant un RAG à coût nul.*

---

## 3. Étape 2 : Clarification GTD (Plane.so)

Seules les vidéos qui franchissent le **Filtre d'Utilité** (catégorisées `AI`, `Business` ou `OS_Dev` avec un `Serendipity Score` > 7/10) sont poussées vers ton Kanban **Plane** en état `INBOX`.
C'est la phase de clarification où l'agent et A0 décident de la valeur ajoutée et de l'actionnabilité du contenu.

---

## 4. Étape 3 : Traitement LLM Wiki & Organisation (Obsidian - Ressources PARA)

Les éléments clarifiés dans Plane sont traités par le **LLM Wiki** pour en extraire la quintessence de la connaissance :
*   **Concepts** (idées et patterns abstraits)
*   **Entités** (canaux, outils, personnalités)
*   **Sources** (la vidéo elle-même et ses références)
*   **Synthèses** (analyses transversales)

### Organisation dans Geordi's Resources (PARA)
Ces pages de connaissances sont générées et stockées dans ton Obsidian, sous la section **Resources** de PARA :
*   📂 Chemin : `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\`

### Double-Way Junction Links (Jonctions Bidirectionnelles)
Symphony crée des jonctions et des liens physiques/symboliques bidirectionnels pour relier ces nouvelles ressources de manière transverse aux piliers de ton univers :
1.  **Les 8 Domaines de Business Pulse (Jerry L2)** : Alignement avec la matrice PARA `J01` (Growth, Sales, Product, Ops, IT, Finance, People, Legal).
2.  **Les 8 Domaines de la Roue de la Vie (Discovery L1)** : Alignement avec les specs d'équilibre (Health, Mind, Social, Family, Play, Impact, Career, Finance).
3.  **Fondations A'Space OS** : Liens directs vers les outils, frameworks, principes et fondamentaux de développement de ton OS souverain.

---

## 5. Étape 4 & 5 : Actionnabilité D.E.A.L & Engagement (Affine + Telegram)

L'étape finale applique le framework **D.E.A.L** sur **Affine** et **Telegram** pour libérer l'exécution et éliminer la dette technique.

```text
  D (Définir)      ──>  E (Éliminer)      ──>  A (Automatiser)  ──>  L (Libérer)
  Drafts de SOPs,       Dette technique &       Valeur ajoutée,      Raffinage fluide,
  Crons & Schedulers   configs obsolètes       Crons durables       Zéro friction
```

*   **D — Définir** : Les apprentissages issus des vidéos YouTube validées sont traduits en **drafts de SOPs (Standard Operating Procedures)**, en **Playbooks**, en nouveaux **Workflows Symphony**, ou en définitions de **Heartbeats, Crons et Schedulers** durables pour étendre ton OS.
*   **E — Éliminer** : Dans **Affine**, lors de la revue visuelle, tu redéfinis les innovations d'amélioration de ta structure et tu planifies l'**élimination des Dettes Techniques** et des configurations obsolètes ou redondantes (comme l'était n8n).
*   **A — Automatiser** : Les SOPs stabilisées sont automatisées par l'orchestrateur **Meta Symphony** sous forme de crons durables d'Antigravity 2.0 pour maximiser la création de valeur ajoutée.
*   **L — Libérer** : Libération totale de ton temps d'exécution. Le pipeline de raffinage de l'historique YouTube tourne de façon autonome et transparente en tâche de fond, ne requérant ton attention que pour l'engagement final.
*   **Engagement A0 (Telegram)** : L'orchestrateur sémantique te pousse les synthèses et les drafts sur ton Telegram pour validation. Ta réponse (GO/NO-GO) libère et acté définitivement les configurations.

---

## 6. Commandes pivots GWS CLI pour le RAG Frugal

Voici les commandes réelles exécutées par Symphony pour le RAG :

### 6.1 Recherche brute (RAG sémantique)
```powershell
# Recherche d'un mot-clé sémantique dans la colonne G (Transcription Raw)
gws sheets spreadsheets values get --params '{"spreadsheetId": "SPREADSHEET_ID", "range": "WatchHistoryBrute!A:H"}' | ConvertFrom-Json | Where-Object { $_.values[6] -match "Agentic Workflow" }
```

### 6.2 Mise à jour de statut (Clarification)
```powershell
# Passer le statut de la ligne 42 à CLARIFIED_PLANE (Colonne H)
gws sheets spreadsheets values update --params '{"spreadsheetId": "SPREADSHEET_ID", "range": "WatchHistoryBrute!H42", "valueInputOption": "USER_ENTERED"}' --json '{"values": [["CLARIFIED_PLANE"]]}'
```

---

*Adapter Google Sheets (GWS) — Shadow A0 — L2 Business — Capture, RAG & GTD-DEAL — 2026-05-23*

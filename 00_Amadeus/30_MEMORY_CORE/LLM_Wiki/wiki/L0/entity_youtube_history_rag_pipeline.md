---
source: A0_Amadeus_LLM_Wiki_Runtime
date: 2026-05-19
type: entity
domain: L2_Business_Pulse / Knowledge_Graph / YouTube_History
tags: [#YouTube_History #Graphiti #RAG #Knowledge_Graph #Neo4j #thedo_mack #claude-mem]
---

# Entity: YouTube History RAG Pipeline

> Pipeline pour analyser l'historique YouTube d'Amadeus → Graphiti + Neo4j knowledge graph → LLM Wiki entities channels.

## Architecture

```
Google Takeout (watch-history.html)
        │
        ▼
Python 3.14 (bs4) — WatchHistoryParser
        │
        ├── Channel URLs extraites
        ├── Catégories: AI / Business / Regular
        │
        ▼
Transcript Fetch (yt-dlp / youtube-transcript-api)
        │
        ▼
Graphiti + Neo4j (Temporal Knowledge Graph)
        │
        ├── Entities: Channels, Videos, Topics
        ├── Facts: temporal validity windows
        ├── Episodes: provenance chain
        │
        ▼
LLM Wiki (Entities + Syntheses)
        │
        └── wiki/entities/entity_<channel>.md
        └── wiki/syntheses/synthesis_youtube_channels_ai.md
```

## Composants

### 1. WatchHistoryParser (Python 3.14)

```python
#输入: watch-history.html (Google Takeout)
#Sortie: List[Channel] avec:
#  - name, url, subscriber_count (estimé), category (AI|Business|Regular)
#  - videos: List[Video] avec title, url, date, duration
```

### 2. TranscriptFetcher

```python
#输入: List[Video]
#Sortie: List[Transcript] avec:
#  - video_id, language, text, segments
#Outils: yt-dlp ou youtube-transcript-api
```

### 3. GraphitiNeo4j Integration

```python
#输入: List[Channel], List[Transcript]
#Sortie: Temporal Knowledge Graph in Neo4j
#Schema:
#  (Channel:`YouTubeChannel` {name, url, category})
#  (Video:`YouTubeVideo` {title, date, duration})
#  (Topic:`YouTubeTopic` {name, category})
#  -[:POSTED_IN]->(Video)
#  -[:ABOUT]->(Topic)
#  -[:RELATED_TO]->(Channel)
```

### 4. LLM Wiki Generator

```python
#输入: Graphiti graph (filtered by category)
#Sortie: LLM Wiki entity + synthesis pages
#  - wiki/entities/entity_<channel_slug>.md
#  - wiki/syntheses/synthesis_youtube_ai_channels.md
#  - wiki/syntheses/synthesis_youtube_business_channels.md
```

## Catégories de Channels

| Catégorie | Critère | Exemples |
|---|---|---|
| **AI** | ML, LLMs, AI research, Agents, AI tools | Andrej Karpathy, Lex Fridman, Samuel AAbbett |
| **Business** | Startups, VC, Finance, Productivity | My First Million, Y Combinator, Bloomberg |
| **Regular** | Divertissement, vlogs, non-classifié | — |

## Outils Disponibles

| Outil | Usage | Python Path |
|---|---|---|
| `python3.14` avec `bs4` | HTML parsing watch-history.html | `C:\Python314\python.exe` |
| `yt-dlp` | Transcript + metadata fetching | `pip install yt-dlp` |
| `youtube-transcript-api` | Alternative transcript fetching | `pip install youtube-transcript-api` |
| `graphiti` | Temporal knowledge graph (Neo4j) | `pip install graphiti` |
| `neo4j` | Graph database (requires 5.26+) | Docker ou cloud |

## Sources

- [thedo_mack/claude-mem](https://github.com/thedotmack/claude-mem) — persistent memory compression pour agents
- [getzep/graphiti](https://github.com/getzep/graphiti) — temporal context graphs for AI agents
- [YouTube Watch History](https://takeout.google.com/) — Google Takeout export

## Statut

| Phase | Statut | Notes |
|---|---|---|
| WatchHistoryParser | **À créer** | Python 3.14 + bs4 |
| TranscriptFetcher | **À créer** | yt-dlp ou youtube-transcript-api |
| GraphitiNeo4j setup | **Pending** | Neo4j 5.26+ requis |
| LLM Wiki entities | **Pending** | Auto-généré après graphe |

## Fichiers du Projet

```
LLM_Wiki_Runtime/
├── youtube-history-analyzer/
│   ├── parser/
│   │   ├── __init__.py
│   │   ├── watch_history_parser.py   # Parse watch-history.html
│   │   └── channel_categorizer.py    # Classifie AI/Business/Regular
│   ├── fetcher/
│   │   ├── __init__.py
│   │   └── transcript_fetch.py       # Fetch transcripts via yt-dlp
│   ├── graphiti/
│   │   ├── __init__.py
│   │   ├── schema.py                 # Graphiti entity/relation schemas
│   │   └── importer.py               # Import channels + transcripts → Neo4j
│   └── wiki/
│       ├── __init__.py
│       └── generator.py              # Generate LLM Wiki pages from graph
├── wikijs-local/                      # Wiki.js local (Docker)
└── wiki/                             # LLM Wiki source files
```

## Notes

- **Source watch-history.html**: Located in Google Takeout at `Takeout/Mon activité/Historique YouTube/watch-history.html` (à vérifier — le fichier n'existe pas encore dans le takeout actuel)
- **Anti-fragile**: Chaque phase est indépendante — si transcript échoue, le channel est quand même ajouté au graphe
- **Token budget**: transcripts = heavy — priorité aux channels AI category d'abord
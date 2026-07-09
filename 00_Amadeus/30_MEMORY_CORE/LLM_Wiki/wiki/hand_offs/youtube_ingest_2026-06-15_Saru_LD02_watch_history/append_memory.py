import os

mem_path = r'C:\Users\amado\.claude\projects\c--Users-amado\memory\MEMORY.md'

entry = """

## LD02 Saru watch-history guide batch (2026-06-15)

- 8 Saru guides from A0 YouTube watch-history (24,867 videos, 1,861 finance hits = 7.48 percent density), ordered by month June to March per A0 redirect.
- Guide paths in: 20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/09_Life_OS/LD02_Finance_Saru/guide_01 through guide_08.
- Handoff canonique: wiki/hand_offs/youtube_ingest_2026-06-15_Saru_LD02_watch_history/youtube_ingestion_handoff_2026-06-15_Saru_LD02_watch_history.md
- 3 ADR drafts: ADR-LD02-001 (Agency over Utopia), -002 (Catalogue SOP L1), -003 (Runway 6 mois cash buffer) - A0 ratification pending.
- D6 honest: youtube-transcript-api + direct timedtext = HTTP 429 sustained (YouTube IP throttling). Guides produced in degraded mode oEmbed.
"""

with open(mem_path, 'a', encoding='utf-8') as f:
    f.write(entry)
print('Wrote entry to MEMORY.md')

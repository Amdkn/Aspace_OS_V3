"""
config.py — Configuration parameters for Symphony Antigravity Sovereign Pipeline.
"""

from pathlib import Path

# Paths to RAG files and Takeout sources
LOCAL_CSV_PATH = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\watch_history_rag.csv")
TAKEOUT_HTML_PATH = Path(r"C:\Users\amado\Downloads\Takeout-YouTube\watch-history.html")
GEORDI_DIR = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides")
AFFINE_DRAFT_PATH = GEORDI_DIR / "affine_deal_drafts.md"

# Pipeline Limits & Batch Sizes
DEFAULT_INGESTION_LIMIT = 500  # Default number of videos to parse and ingest from Takeout
DEFAULT_BATCH_SIZE = 10       # Number of videos assigned to each parallel sub-agent

# Scoring and classification thresholds
SERENDIPITY_THRESHOLD = 7     # Only videos with score >= 7 are passed to sub-agents for full sémantique extraction

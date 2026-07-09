import sys
import os
from pathlib import Path

# Add the script directory to sys.path to import gemini_handoff_runner
script_dir = r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\symphony_antigravity"
sys.path.append(script_dir)

from gemini_handoff_runner import update_csv_status, inject_affine_sop

def handle_update(video_id, title, channel, sop_block):
    print(f"Updating status for {video_id}...")
    update_csv_status(video_id, "CLARIFIED_PLANE")
    
    print(f"Injecting SOP for {title}...")
    inject_affine_sop(title, channel, sop_block)
    print("Done.")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python update_handler.py <video_id> <title> <channel> <sop_block_file>")
        sys.exit(1)
    
    video_id = sys.argv[1]
    title = sys.argv[2]
    channel = sys.argv[3]
    sop_block_file = sys.argv[4]
    
    with open(sop_block_file, "r", encoding="utf-8") as f:
        sop_block = f.read()
    
    handle_update(video_id, title, channel, sop_block)

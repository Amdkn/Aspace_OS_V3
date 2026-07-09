import re
import shutil
import sys
from pathlib import Path

# Force UTF-8 stdout encoding
sys.stdout.reconfigure(encoding='utf-8')

yann_dir = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides\07_Growth\Yann_Leonardi")
guides_parent_dir = yann_dir.parent.parent

print("="*60)
print("[*] Ricks Harness - Yann Leonardi Folder Noise Purge...")
print("="*60)

moved_count = 0

for item in yann_dir.iterdir():
    if item.is_file() and item.name.startswith("resource_") and item.suffix == ".md":
        content = item.read_text(encoding="utf-8")
        
        # Read channel from Frontmatter
        channel_match = re.search(r'channel:\s*\"?([^\n\"]+)\"?', content)
        if channel_match:
            channel_name = channel_match.group(1).strip()
            if "Yann Leonardi" not in channel_name:
                # Move to parent guides directory
                dest_path = guides_parent_dir / item.name
                shutil.move(str(item), str(dest_path))
                print(f"[PURGE] Moved noisy file '{item.name}' (Channel: {channel_name}) out of Yann_Leonardi/ to parent 01_Guides/")
                moved_count += 1
        else:
            print(f"[?] Could not read channel name in {item.name}, skipping.")

print(f"\n[+] Purge completed: {moved_count} noisy files moved out of Yann_Leonardi directory.")

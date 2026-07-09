import os
import re
from html import unescape

source_html = "C:\Aspace00\Takeout\Mon activité\Applications\xa0Gemini\MonActivité.html"
output_dir = "C:\Aspace00\aspace_a0_amadeus\20_Life_OS\24_PARA_Enterprise\04_Archives_Data\A0_Memory\ai_conversations\google\Gemini\2026\02-February\G-NBLM READY"

def clean_html(raw_html):
    clean = re.sub("<[^<]+?>", "", raw_html)
    return unescape(clean)

def reconstruct():
    if not os.path.exists(source_html):
        print("Source introuvable.")
        return

    with open(source_html, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    conversations = content.split("<hr>")
    valid_convs = [c.strip() for c in conversations if "Applications Gemini" in c or "Prompt" in c]
    
    # Takeout is reverse chronological (Newest first)
    # We want Parts 17-26 to be the latest conversations.
    # If we have 270 total convs, Parts 17-26 are roughly convs 0 to 110 (the newest ones)
    
    convs_per_part = 11

    for part_num in range(17, 27):
        part_filename = "Gemini_Feb2026_Part_" + str(part_num).zfill(2) + ".md"
        part_path = os.path.join(output_dir, part_filename)
        
        # Taking from the beginning of valid_convs because it's newest first
        idx_start = (part_num - 17) * convs_per_part
        idx_end = idx_start + convs_per_part
        batch = valid_convs[idx_start:idx_end]
        
        if not batch:
            break
            
        with open(part_path, "w", encoding="utf-8") as out:
            out.write("# Gemini History - Feb 2026 - Part " + str(part_num).zfill(2) + "

")
            for i, conv in enumerate(batch):
                body = clean_html(conv)
                out.write("## SOURCE: Conversation_" + str(part_num) + "_" + str(i+1) + "
")
                out.write(body + "

---

")
        
        print("Reconstructed: " + part_filename)

reconstruct()

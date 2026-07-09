import os
import re
from html import unescape

source_html = r"C:\Aspace00\Takeout\Mon activité\Applications Gemini\MonActivité.html"
output_dir = r"C:\Aspace00\aspace_a0_amadeus\20_Life_OS\24_PARA_Enterprise\04_Archives_Data\A0_Memory\ai_conversations\google\Gemini\2026\02-February\G-NBLM READY"

def clean_html(raw_html):
    # Remove HTML tags and unescape entities
    clean = re.sub('<[^<]+?>', '', raw_html)
    return unescape(clean)

def reconstruct():
    if not os.path.exists(source_html):
        print(f"Error: Source {source_html} not found.")
        return

    with open(source_html, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Gemini Takeout structure: each conversation is usually inside a div with class "outer-cell" or separated by <hr>
    # We split by <hr> which is the standard separator in Google activity exports
    conversations = content.split('<hr>')
    
    # Filter out empty or meta conversations (keep those with actual content)
    valid_convs = [c for c in conversations if "Applications Gemini" in c or "Prompt" in c]
    
    # We need to target Part 17 to 26.
    # If we assume Part 01-16 already covered the first ~160 convs, 
    # we start from conv 160 (index base).
    start_index = 160 
    convs_per_part = 11 # Adjust to fit 106 convs into 10 parts
    
    for part_num in range(17, 27):
        part_file = os.path.join(output_dir, f"Gemini_Feb2026_Part_{part_num:02d}.md")
        
        # Start slice
        slice_start = start_index + (part_num - 17) * convs_per_part
        slice_end = slice_start + convs_per_part
        current_batch = valid_convs[slice_start:slice_end]
        
        if not current_batch:
            break
            
        with open(part_file, 'w', encoding='utf-8') as out:
            out.write(f"# Gemini History - Feb 2026 - Part {part_num:02d}

")
            for i, conv in enumerate(current_batch):
                clean_text = clean_html(conv).strip()
                if clean_text:
                    out.write(f"## SOURCE: Conversation_{part_num}_{i+1}
")
                    out.write(f"{clean_text}

---

")
        
        print(f"Reconstructed {part_file}")

# Execute
reconstruct()

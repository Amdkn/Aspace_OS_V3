import os
import re
from html import unescape

source_html = r"C:\Aspace00\Takeout\Mon activité\Applications Gemini\MonActivité.html"
output_dir = r"C:\Aspace00\aspace_a0_amadeus\20_Life_OS\24_PARA_Enterprise\04_Archives_Data\A0_Memory\ai_conversations\google\Gemini\2026\02-February\G-NBLM READY"

def clean_html(raw_html):
    # Nettoyage HTML et entités
    clean = re.sub('<[^<]+?>', '', raw_html)
    return unescape(clean)

def reconstruct():
    if not os.path.exists(source_html):
        print("Source introuvable.")
        return

    # Chargement avec gestion d'encodage
    with open(source_html, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Découpage par bloc de conversation (balise hr standard Google)
    conversations = content.split('<hr>')
    
    # Filtrer uniquement les entrées pertinentes
    valid_convs = [c.strip() for c in conversations if "Applications Gemini" in c or "Prompt" in c]
    
    # Inversion chronologique si nécessaire (Takeout est souvent du plus récent au plus ancien)
    # On veut que Part 17-26 soient la fin du mois
    valid_convs.reverse()

    # On cible les ~110 dernières conversations pour les Parts 17 à 26
    # Si on a ~260 convs au total (10 convs par Part sur 26 Parts)
    start_index = 160
    convs_per_part = 11

    for part_num in range(17, 27):
        part_filename = f"Gemini_Feb2026_Part_{part_num:02d}.md"
        part_path = os.path.join(output_dir, part_filename)
        
        idx_start = start_index + (part_num - 17) * convs_per_part
        idx_end = idx_start + convs_per_part
        batch = valid_convs[idx_start:idx_end]
        
        if not batch:
            print(f"Fin des données à la Part {part_num-1}")
            break
            
        with open(part_path, 'w', encoding='utf-8') as out:
            header = f"# Gemini History - Feb 2026 - Part {part_num:02d}

"
            out.write(header)
            for i, conv in enumerate(batch):
                body = clean_html(conv)
                out.write(f"## SOURCE: Conversation_{part_num}_{i+1}
")
                out.write(f"{body}

---

")
        
        print(f"Reconstructed: {part_filename}")

reconstruct()

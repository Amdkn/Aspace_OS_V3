import re
from pathlib import Path

yann_dir = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides\07_Growth\Yann_Leonardi")
drafts_path = yann_dir / "affine_deal_drafts.md"

new_entries = []

# Scan all files in Yann_Leonardi directory and extract DEAL SOPs
for item in yann_dir.iterdir():
    if item.is_file() and item.name.startswith("resource_") and item.suffix == ".md":
        content = item.read_text(encoding="utf-8")
        
        video_id_match = re.search(r'id:\s*\"?([^\n\"]+)\"?', content)
        title_match = re.search(r'title:\s*\"?([^\n\"]+)\"?', content)
        
        if not video_id_match or not title_match:
            continue
            
        video_id = video_id_match.group(1).strip()
        title = title_match.group(1).strip()
        
        # Match either DEAL, D.E.A.L or Actionnabilité section
        deal_match = re.search(r"##\s*(?:[^\n]*)(?:DEAL|D\.E\.A\.L|Actionnabilité|Actionnabilit[ée])[^\n]*\n(.*?)(?=\n---\n\*Fin|$)", content, re.DOTALL | re.IGNORECASE)
        if not deal_match:
            # Fallback regex if it ends with Fin
            deal_match = re.search(r"##\s*[^\n]*DEAL[^\n]*\n(.*?)(?=\n---|$)", content, re.DOTALL | re.IGNORECASE)
            
        if not deal_match:
            print(f"[-] No DEAL section matched in: {item.name}")
            continue
            
        deal_content = deal_match.group(1).strip()
        
        # Find keys
        d_match = re.search(r"(?:###\s*D[^\n]*|- \*\*D[^\n]*\*\*|- D[^\n]*)\s*\n?(.*?)(?=(?:###\s*[EAL]|- \*\*[EAL]\*\*|- [EAL]\*\*)|$)", deal_content, re.DOTALL)
        e_match = re.search(r"(?:###\s*E[^\n]*|- \*\*E[^\n]*\*\*|- E[^\n]*)\s*\n?(.*?)(?=(?:###\s*[AL]|- \*\*[AL]\*\*|- [AL]\*\*)|$)", deal_content, re.DOTALL)
        a_match = re.search(r"(?:###\s*A[^\n]*|- \*\*A[^\n]*\*\*|- A[^\n]*)\s*\n?(.*?)(?=(?:###\s*L|- \*\*L\*\*|- L\*\*)|$)", deal_content, re.DOTALL)
        l_match = re.search(r"(?:###\s*L[^\n]*|- \*\*L[^\n]*\*\*|- L[^\n]*)\s*\n?(.*?)$", deal_content, re.DOTALL)
        
        d_text = d_match.group(1).strip() if d_match else ""
        e_text = e_match.group(1).strip() if e_match else ""
        a_text = a_match.group(1).strip() if a_match else ""
        l_text = l_match.group(1).strip() if l_match else ""
        
        # Clean prefix list tags or trailing spaces
        d_text = re.sub(r"^:\s*", "", d_text).strip()
        e_text = re.sub(r"^:\s*", "", e_text).strip()
        a_text = re.sub(r"^:\s*", "", a_text).strip()
        l_text = re.sub(r"^:\s*", "", l_text).strip()
        
        d_text = re.sub(r"^-\s*", "", d_text, flags=re.MULTILINE).strip()
        e_text = re.sub(r"^-\s*", "", e_text, flags=re.MULTILINE).strip()
        a_text = re.sub(r"^-\s*", "", a_text, flags=re.MULTILINE).strip()
        l_text = re.sub(r"^-\s*", "", l_text, flags=re.MULTILINE).strip()
        
        entry = f"""## Video ID: {video_id}
**Title:** {title}
**D - Description:** {d_text}
**E - Évaluation:** {e_text}
**A - Action:** {a_text}
**L - Leçon:** {l_text}

---"""
        new_entries.append(entry)

if new_entries:
    header = """# 📝 Yann Leonardi — Affine DEAL Drafts SOPs

Ce registre compile de façon exclusive et structurée les SOPs D.E.A.L issues de l'ingestion sémantique des ressources de Yann Leonardi dans le domaine B2 Growth.

---
"""
    drafts_path.write_text(header + "\n" + "\n\n".join(new_entries) + "\n", encoding="utf-8")
    print(f"[+] Successfully generated affine_deal_drafts.md in Yann_Leonardi directory with {len(new_entries)} entries.")
else:
    print("[-] No entries extracted.")

import re
import csv
from pathlib import Path

guides_dir = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides")
drafts_path = guides_dir / "affine_deal_drafts.md"

files = [
    "resource_inbound_vs_content_marketing.md",
    "resource_5_instagram_marketing_tips.md",
    "resource_seo_les_bases_pour_se_lancer_dans_le_referencement_naturel.md",
    "resource_how_do_you_know_if_you_have_a_productmarket_fit.md"
]

existing_content = ""
if drafts_path.exists():
    existing_content = drafts_path.read_text(encoding="utf-8")

new_entries = []

for filename in files:
    file_path = guides_dir / filename
    if not file_path.exists():
        print(f"[-] File not found: {filename}")
        continue
    content = file_path.read_text(encoding="utf-8")
    
    video_id_match = re.search(r'id:\s*\"?([^\n\"]+)\"?', content)
    title_match = re.search(r'title:\s*\"?([^\n\"]+)\"?', content)
    
    if not video_id_match or not title_match:
        print(f"[-] Failed to match metadata in: {filename}")
        continue
        
    video_id = video_id_match.group(1).strip()
    title = title_match.group(1).strip()
    
    if f"Video ID: {video_id}" in existing_content:
        print(f"[-] {video_id} already exists in drafts.")
        continue
        
    deal_match = re.search(r"## 4\. D\.E\.A\.L.*?(### D.*)", content, re.DOTALL)
    if not deal_match:
        print(f"[-] No DEAL section found in: {filename}")
        continue
        
    deal_content = deal_match.group(1).strip()
    
    d_match = re.search(r"### D[^\n]*\n(.*?)(?=###|$)", deal_content, re.DOTALL)
    e_match = re.search(r"### E[^\n]*\n(.*?)(?=###|$)", deal_content, re.DOTALL)
    a_match = re.search(r"### A[^\n]*\n(.*?)(?=###|$)", deal_content, re.DOTALL)
    l_match = re.search(r"### L[^\n]*\n(.*?)(?=###|$)", deal_content, re.DOTALL)
    
    d_text = d_match.group(1).strip() if d_match else ""
    e_text = e_match.group(1).strip() if e_match else ""
    a_text = a_match.group(1).strip() if a_match else ""
    l_text = l_match.group(1).strip() if l_match else ""
    
    # Strip markdown lists or prefixes to get clean lines
    d_text = re.sub(r"^-\s*", "", d_text, flags=re.MULTILINE)
    e_text = re.sub(r"^-\s*", "", e_text, flags=re.MULTILINE)
    a_text = re.sub(r"^-\s*", "", a_text, flags=re.MULTILINE)
    l_text = re.sub(r"^-\s*", "", l_text, flags=re.MULTILINE)
    
    entry = f"""## Video ID: {video_id}
**Title:** {title}
**D - Description:** {d_text}
**E - Évaluation:** {e_text}
**A - Action:** {a_text}
**L - Leçon:** {l_text}

---"""
    new_entries.append(entry)

if new_entries:
    with open(drafts_path, "a", encoding="utf-8") as f:
        f.write("\n\n" + "\n\n".join(new_entries) + "\n")
    print(f"[+] Injected {len(new_entries)} DEAL SOPs into drafts.")
else:
    print("[-] No new SOPs to inject.")

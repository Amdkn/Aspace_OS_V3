import os
import re
from datetime import datetime
from html import unescape

source_html = None
base = r"C:\Aspace00\Takeout"
output_dir = r"C:\Aspace00\aspace_a0_amadeus\20_Life_OS\24_PARA_Enterprise\04_Archives_Data\A0_Memory\ai_conversations\google\Gemini\2026\02-February\G-NBLM READY 2"

if os.path.exists(base):
    activity_dirs = [d for d in os.listdir(base) if d.startswith("Mon")]
    if activity_dirs:
        mon_activite = os.path.join(base, activity_dirs[0])
        app_dirs = [d for d in os.listdir(mon_activite) if d.startswith("Applications")]
        if app_dirs:
            source_html = os.path.join(mon_activite, app_dirs[0], "MonActivité.html")

def parse_date(date_str):
    months = {
        'janv.': '01', 'févr.': '02', 'mars': '03', 'avr.': '04',
        'mai': '05', 'juin': '06', 'juil.': '07', 'août': '08',
        'sept.': '09', 'oct.': '10', 'nov.': '11', 'déc.': '12'
    }
    try:
        match = re.search(r'(\d+) ([a-zéû.]+)\.? (\d{4}), (\d+:\d+:\d+)', date_str)
        if match:
            day = match.group(1).zfill(2)
            month_fr = match.group(2).lower()
            year = match.group(3)
            time = match.group(4)
            month = months.get(month_fr, '01')
            return year + "-" + month + "-" + day + " " + time
    except:
        pass
    return "1970-01-01 00:00:00"

def clean_text(html_content):
    text = re.sub(r'<(script|style).*?>.*?</\1>', '', html_content, flags=re.S | re.I)
    NL = chr(10)
    text = text.replace("<br>", NL).replace("<br/>", NL).replace("<br />", NL)
    text = re.sub(r'<p.*?>', NL + NL, text)
    text = re.sub(r'<[^>]+?>', '', text)
    return unescape(text).strip()

def reconstruct():
    if not source_html or not os.path.exists(source_html):
        print("Source not found.")
        return

    print("Reading " + source_html)
    with open(source_html, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    blocks = content.split('class="outer-cell')
    print("Found " + str(len(blocks)) + " raw blocks.")
    
    parsed_convs = []
    for b in blocks:
        if 'mdl-typography--title' not in b: continue
        
        time_match = re.search(r'(\d+ [a-zéû.]+ \d{4}, \d+:\d+:\d+)', b)
        timestamp_raw = time_match.group(1) if time_match else "Unknown"
        sort_key = parse_date(timestamp_raw)
        
        clean_body = clean_text(b)
        if clean_body:
            parsed_convs.append({
                'key': sort_key,
                'raw_time': timestamp_raw,
                'body': clean_body
            })

    parsed_convs.sort(key=lambda x: x['key'])
    print("Sorted " + str(len(parsed_convs)) + " valid conversations.")

    batch_size = 10
    NL = chr(10)
    for i in range(0, len(parsed_convs), batch_size):
        part_num = (i // batch_size) + 1
        part_filename = "Gemini_Feb2026_Part_" + str(part_num).zfill(2) + ".md"
        part_path = os.path.join(output_dir, part_filename)
        
        batch = parsed_convs[i:i + batch_size]
        with open(part_path, 'w', encoding='utf-8') as out:
            out.write("# Gemini History - Feb 2026 - Part " + str(part_num).zfill(2) + NL + NL)
            for j, conv in enumerate(batch):
                out.write("## SOURCE: " + conv['raw_time'] + " (Index " + str(i+j+1) + ")" + NL)
                out.write(conv['body'] + NL + NL + "---" + NL + NL)
        
        print("Created: " + part_filename)

reconstruct()

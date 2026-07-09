import json
import os
import re
from datetime import datetime

export_dir = r"c:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Claude Export"
json_path = os.path.join(export_dir, "conversations.json")
out_dir = os.path.join(export_dir, "Markdown_Export")

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

def clean_filename(name):
    # Remove invalid characters for Windows filenames
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    name = name.strip()
    # Limit length
    return name[:150]

print(f"Loading {json_path}...")
try:
    with open(json_path, 'r', encoding='utf-8') as f:
        conversations = json.load(f)
except Exception as e:
    print(f"Error reading JSON: {e}")
    exit(1)

print(f"Found {len(conversations)} conversations. Converting to Markdown...")

count = 0
for conv in conversations:
    name = conv.get("name", "Untitled")
    if not name:
        name = "Untitled"
        
    created_at_str = conv.get("created_at", "")
    try:
        # e.g., 2026-04-23T03:52:31.128464Z
        dt = datetime.strptime(created_at_str.split('.')[0] + "Z", "%Y-%m-%dT%H:%M:%SZ")
        date_prefix = dt.strftime("%Y-%m-%d")
        formatted_date = dt.strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        date_prefix = "UnknownDate"
        formatted_date = created_at_str

    safe_name = clean_filename(name)
    filename = f"{date_prefix}_{safe_name}.md"
    # Ensure unique filename
    filepath = os.path.join(out_dir, filename)
    counter = 1
    while os.path.exists(filepath):
        filepath = os.path.join(out_dir, f"{date_prefix}_{safe_name}_{counter}.md")
        counter += 1

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# {name}\n\n")
        f.write(f"**Created:** {formatted_date}\n")
        
        summary = conv.get("summary", "")
        if summary:
            f.write(f"\n**Summary:**\n{summary}\n")
            
        f.write("\n---\n\n")
        
        messages = conv.get("chat_messages", [])
        # Sort messages by created_at just in case
        def get_msg_date(m):
            return m.get("created_at", "")
        messages.sort(key=get_msg_date)
        
        for msg in messages:
            sender = msg.get("sender", "unknown").capitalize()
            text = msg.get("text", "")
            
            f.write(f"## {sender}\n\n")
            f.write(f"{text}\n\n")
            
    count += 1

print(f"Successfully converted {count} conversations to Markdown in: {out_dir}")

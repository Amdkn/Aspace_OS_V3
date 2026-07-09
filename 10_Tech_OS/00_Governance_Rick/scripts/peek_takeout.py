import os

base = "C:\Aspace00\Takeout"
activity_dirs = [d for d in os.listdir(base) if d.startswith("Mon")]
mon_activite = os.path.join(base, activity_dirs[0])
app_dirs = [d for d in os.listdir(mon_activite) if d.startswith("Applications")]
source_file = os.path.join(mon_activite, app_dirs[0], "MonActivité.html")

with open(source_file, 'r', encoding='utf-8', errors='ignore') as f:
    # Skip the massive CSS block and read a chunk from the body
    f.seek(500000) # Seek 500KB into the file
    chunk = f.read(5000)
    print("--- RAW DATA PREVIEW ---")
    print(chunk)

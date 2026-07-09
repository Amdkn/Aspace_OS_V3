import os
import glob
import math

source_dir = r"C:\Aspace00\aspace_a0_amadeus\20_Life_OS\24_PARA_Enterprise\04_Archives_Data\A0_Memory\ai_conversations\google\Gemini\2026\02-February\G-NBLM READY 2"

# 1. Get all Part files and sort them properly
pattern = os.path.join(source_dir, "Gemini_Feb2026_Part_*.md")
files = glob.glob(pattern)
files.sort() # Ensure alphabetical sorting (Part_01, Part_02... Part_196)

if not files:
    print("No Part files found.")
    exit()

total_files = len(files)
print(f"Found {total_files} files to consolidate.")

# 2. Determine chunk size to get exactly 10 Master files
# 196 files / 10 = 19.6 -> let's do chunks of 20 (9 files of 20, 1 file of 16)
chunk_size = 20
num_masters = math.ceil(total_files / chunk_size)

print(f"Grouping into {num_masters} Master files (approx {chunk_size} parts per master).")

# 3. Process and consolidate
for i in range(num_masters):
    master_num = i + 1
    master_filename = f"Gemini_Feb2026_MASTER_{master_num:02d}.md"
    master_path = os.path.join(source_dir, master_filename)
    
    start_idx = i * chunk_size
    end_idx = min(start_idx + chunk_size, total_files)
    chunk_files = files[start_idx:end_idx]
    
    master_content = f"# Gemini History - Feb 2026 - MASTER {master_num:02d}
"
    master_content += f"## Consolidation of Parts {start_idx+1} to {end_idx}

"
    
    for file_path in chunk_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Strip the redundant "# Gemini History..." headers from the sub-files to keep it clean
            lines = content.split('
')
            clean_lines = [line for line in lines if not line.startswith('# Gemini History - Feb 2026 - Part')]
            master_content += '
'.join(clean_lines).strip() + "

"
            
    with open(master_path, 'w', encoding='utf-8') as f:
        f.write(master_content)
        
    print(f"Created {master_filename} from {len(chunk_files)} parts.")

# 4. Cleanup old files
print("Purging the 196 small files to maintain a clean workspace...")
for f in files:
    os.remove(f)

print("Consolidation Complete. Workspace Optimized.")

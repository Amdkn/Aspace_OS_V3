import os
import re
from datetime import datetime
from bs4 import BeautifulSoup

# Paths
source_html = "C:\\Aspace00\\Takeout\\Mon activité\\Applications\u00a0Gemini\\MonActivité.html"
target_dir = r"C:\Aspace00\aspace_a0_amadeus\20_Life_OS\24_PARA_Enterprise\04_Archives_Data\A0_Memory\ai_conversations\google\Gemini\2026\02-February"

# Date Threshold
threshold_date = datetime(2026, 2, 19)

# French month mapping
months_fr = {
    "janv.": "Jan", "févr.": "Feb", "mars": "Mar", "avr.": "Apr",
    "mai": "May", "juin": "Jun", "juil.": "Jul", "août": "Aug",
    "sept.": "Sep", "oct.": "Oct", "nov.": "Nov", "déc.": "Dec"
}

def parse_date(date_str):
    # Example: "19 févr. 2026, 10:23:45 UTC"
    for fr, en in months_fr.items():
        date_str = date_str.replace(fr, en)
    
    # Remove day of week if present (e.g. "sam.")
    date_str = re.sub(r'^[a-z]{2,3}\.\s+', '', date_str.lower())
    
    # Try parsing
    try:
        # Expected format: "19 Feb 2026, 10:23:45 UTC" or similar
        # Some versions don't have the comma
        date_str = date_str.replace(',', '')
        return datetime.strptime(date_str.split(' à')[0], "%d %b %Y") # Basic date for filtering
    except Exception as e:
        # Fallback regex for "DD MMM YYYY"
        match = re.search(r'(\d{1,2})\s+([a-zA-Z]{3,4}\.?)\s+(\d{4})', date_str)
        if match:
            day, mon, year = match.groups()
            mon = months_fr.get(mon, mon[:3])
            return datetime.strptime(f"{day} {mon} {year}", "%d %b %Y")
        return None

def main():
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)

    print(f"Reading {source_html}...")
    try:
        with open(source_html, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Look for the main container cells
    # Google Takeout often uses mdl-cell class
    items = soup.find_all('div', class_=re.compile(r'mdl-cell'))
    print(f"Found {len(items)} entries with mdl-cell class.")

    if len(items) == 0:
        # Try a broader search if mdl-cell is not used directly on the div we need
        items = soup.find_all('div', recursive=False)
        print(f"Fallback: Found {len(items)} top-level divs.")

    count = 0
    # Process each entry. Typically an entry is a block containing text and a date.
    for item in items:
        try:
            full_text = item.get_text(separator='\n').strip()
            if not full_text: continue
            
            lines = [l.strip() for l in full_text.split('\n') if l.strip()]
            if len(lines) < 2: continue
            
            # The date is usually near the end. Let's find the first line that looks like a date from the bottom.
            date_info = ""
            date_index = -1
            for i in range(len(lines)-1, -1, -1):
                if any(m in lines[i].lower() for m in months_fr.keys()):
                    if re.search(r'\d{4}', lines[i]): # Has a year
                        date_info = lines[i]
                        date_index = i
                        break
            
            if not date_info: continue
            
            extracted_date = parse_date(date_info)
            # Threshold: >= 19 Feb 2026 AND <= 1 Mar 2026
            if extracted_date and threshold_date <= extracted_date <= datetime(2026, 3, 1):
                title = lines[0]
                # Clean title
                clean_title = re.sub(r'[^\w\s-]', '', title)[:50].strip().replace(' ', '_')
                date_str_file = extracted_date.strftime("%Y-%m-%d")
                
                # Deduplicate filenames
                base_name = f"{date_str_file}_{clean_title}"
                filename = f"{base_name}.md"
                path = os.path.join(target_dir, filename)
                i = 1
                while os.path.exists(path):
                    path = os.path.join(target_dir, f"{base_name}_{i}.md")
                    i += 1
                
                with open(path, 'w', encoding='utf-8') as md:
                    md.write(f"# {title}\n\n")
                    md.write(f"**Date:** {date_info}\n\n")
                    md.write("---\n\n")
                    # Content is everything until the date line
                    content = '\n\n'.join(lines[1:date_index])
                    md.write(content)
                
                print(f"Saved: {os.path.basename(path)}")
                count += 1
                
        except Exception as e:
            continue

    print(f"Done. Extracted {count} conversations.")

if __name__ == "__main__":
    main()

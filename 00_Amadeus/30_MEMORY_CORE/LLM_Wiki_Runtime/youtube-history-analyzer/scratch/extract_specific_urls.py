import sys
import json
from pathlib import Path
import yt_dlp

# Force UTF-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

URLS_LIFE = [
    "https://youtu.be/uy-YFZPFT8c?si=NZ7_MnY7o2bSfktP",
    "https://youtu.be/TyeBniA85jE?si=Z51uBBPN6g3GKOFf",
    "https://youtu.be/BGxpATOGK_M?si=gyVB9ERwD3DesIwT",
    "https://youtu.be/qi9tVNA488Q?si=M3xHpTr58_mC04_X",
    "https://youtu.be/YCL1IXbvCWY?si=s8qeMbw9qAhu_8ud",
    "https://youtu.be/l0GahkvnWc4?si=KzFsNS95ybx-QSdX",
    "https://youtu.be/DhQd4kUKj7A?si=M1r3WjUfz5IeNHTq",
    "https://youtu.be/21L-iujzy9U?si=KGIhwXEAG6ik6Q0I",
    "https://youtu.be/Bgxsx8slDEA?si=CZj7IEbwFk3GoL5K",
    "https://youtu.be/5x3_U7b4eKU?si=oAWTKc4YIOUC68DO"
]

URLS_OPS = [
    "https://youtu.be/4tV_jwspQAs?si=fkmvklH5QFcOdEwB",
    "https://youtu.be/B1SPP9oXWYI?si=hmq3Z7glKP0_dbz7",
    "https://youtu.be/wDVf0y4jCj4?si=MwIUO1LixtCA7kjl"
]

def format_duration(seconds):
    if not seconds:
        return "00:00"
    seconds = int(seconds)
    mins, secs = divmod(seconds, 60)
    hours, mins = divmod(mins, 60)
    if hours > 0:
        return f"{hours:02d}:{mins:02d}:{secs:02d}"
    return f"{mins:02d}:{secs:02d}"

def extract_meta(urls, label):
    ydl_opts = {
        'extract_flat': True,
        'skip_download': True,
        'quiet': True
    }
    
    results = []
    print(f"[*] Extraction des metadonnees pour le lot {label}...")
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            try:
                info = ydl.extract_info(url, download=False)
                if info:
                    vid_id = info.get('id')
                    title = info.get('title')
                    uploader = info.get('uploader') or "Inconnu"
                    duration_sec = info.get('duration')
                    duration = format_duration(duration_sec)
                    upload_date = info.get('upload_date') or ""
                    
                    results.append({
                        'id': vid_id,
                        'title': title,
                        'uploader': uploader,
                        'duration': duration,
                        'date': upload_date,
                        'url': f"https://www.youtube.com/watch?v={vid_id}"
                    })
                    print(f"  [+] {uploader} - {title[:50]} (ID: {vid_id})")
            except Exception as e:
                print(f"  [-] Erreur pour {url} : {e}")
                
    return results

if __name__ == "__main__":
    life_meta = extract_meta(URLS_LIFE, "Roue de la Vie (Life OS)")
    ops_meta = extract_meta(URLS_OPS, "Ops Absolus")
    
    output_data = {
        'life_os': life_meta,
        'ops': ops_meta
    }
    
    out_file = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki_Runtime\youtube-history-analyzer\scratch\specific_urls_meta.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    print(f"\n[+] Metadonnees specifiques enregistrees dans {out_file}")

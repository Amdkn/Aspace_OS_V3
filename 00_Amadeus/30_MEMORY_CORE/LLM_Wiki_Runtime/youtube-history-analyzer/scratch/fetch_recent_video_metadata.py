import sys
import json
import yt_dlp

# Force UTF-8 stdout encoding
sys.stdout.reconfigure(encoding='utf-8')

video_ids = ["gU5KDeTb1JY", "TZDMhtrty5E", "DZtj2S_-qa8"]

ydl_opts = {
    'extract_flat': True,
    'skip_download': True,
    'quiet': True
}

print("="*60)
print("[*] Extraction des métadonnées avec yt_dlp...")
print("="*60)

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for vid_id in video_ids:
        url = f"https://www.youtube.com/watch?v={vid_id}"
        print(f"\n[*] Requête pour {url}...")
        try:
            info = ydl.extract_info(url, download=False)
            print(f"[+] Succès pour {vid_id} :")
            print(f"    - Titre : {info.get('title')}")
            print(f"    - Chaîne : {info.get('uploader')} ({info.get('uploader_url')})")
            print(f"    - Durée : {info.get('duration')} secondes")
            print(f"    - Date de publication : {info.get('upload_date')}")
        except Exception as e:
            print(f"[-] Erreur pour {vid_id} : {e}")

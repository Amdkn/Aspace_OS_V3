#!/bin/bash
# Recupere une video et en tire des planches-contact.
#
# Les images comptent autant que la transcription : une demo produit se lit a
# l'ecran, pas dans les mots. Trois fois cette semaine un agent a redesigne a
# l'aveugle faute de les avoir.
set -u
ID="$1"; NOM="$2"
B=/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/outils-micro-saas
D="$B/$NOM"; mkdir -p "$D/frames" "$D/planches"
cd "$D" || exit 1

/c/Users/amado/bin/yt-dlp -f "bv*[height<=720]+ba/b[height<=720]" -o "video.%(ext)s" \
  "https://www.youtube.com/watch?v=$ID" >> "$D/extraction.log" 2>&1
V=$(ls video.* 2>/dev/null | head -1)
[ -z "$V" ] && { echo "ECHEC telechargement" >> "$D/extraction.log"; exit 1; }

# Une image toutes les 10 s : assez dense pour suivre une demo, assez legere
# pour rester lisible par un agent.
ffmpeg -hide_banner -loglevel error -i "$V" -vf "fps=1/10,scale=854:-1" \
  "frames/%04d.png" >> "$D/extraction.log" 2>&1

# Planches-contact de 20 vignettes : un agent lit dix planches, pas deux cents images.
ffmpeg -hide_banner -loglevel error -start_number 1 -i "frames/%04d.png" \
  -vf "scale=427:-1,tile=4x5" "planches/planche-%02d.png" >> "$D/extraction.log" 2>&1

echo "frames: $(ls frames/*.png 2>/dev/null | wc -l) | planches: $(ls planches/*.png 2>/dev/null | wc -l)" >> "$D/extraction.log"

#!/usr/bin/env bash
# Telechargement + planches-contact + extraction pour les 7 conferences Agentic OS.
# Les images priment sur les transcriptions : c'est la structure des interfaces et
# des schemas qu'on vient chercher, pas les mots.
export PATH="$HOME/.local/bin:$PATH"
D="/mnt/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os"
mkdir -p "$D/images" ~/barre/agentic
exec > "$D/logs/images.log" 2>&1
cd ~/barre/agentic || exit 1

declare -A V=(
 [01-self-improving]=MAuLQzcMrS0
 [02-graphify]=Owv503rTqYY
 [03-fable5-agentic-os]=3ujOdi9W1EI
 [04-second-brain-fable5]=VoKiKvgpk78
 [05-cinq-couches]=YjkteijEyzQ
 [06-runs-my-business]=7aQbN543Mec
 [07-remplace-openclaw]=rVzGu5OYYS0
)

for n in "${!V[@]}"; do
  mkdir -p "$D/images/$n/planches"
  if [ ! -f "$n.mp4" ]; then
    yt-dlp -f "bestvideo[height<=1080][ext=mp4]/best[height<=1080]" \
      -o "$n.mp4" "https://www.youtube.com/watch?v=${V[$n]}" >/dev/null 2>&1 \
      || { echo "ECHEC telechargement $n"; continue; }
  fi
  # Une vignette toutes les 8 s, numerotee en secondes pour retrouver l'instant.
  rm -rf "ech-$n"; mkdir -p "ech-$n"
  ffmpeg -loglevel error -i "$n.mp4" \
    -vf "fps=1/8,scale=400:-1,drawtext=text='%{eif\:n*8\:d}s':x=8:y=8:fontsize=24:fontcolor=yellow:box=1:boxcolor=black" \
    "ech-$n/e-%03d.png" -y 2>/dev/null
  N=$(ls "ech-$n"/*.png 2>/dev/null | wc -l)
  i=0
  for c in $(seq 1 24 "$N"); do
    i=$((i+1))
    ffmpeg -loglevel error -start_number "$c" -i "ech-$n/e-%03d.png" -frames:v 1 \
      -vf "tile=6x4" "$D/images/$n/planches/planche-$i.png" -y 2>/dev/null || true
  done
  echo "$n : $N vignettes, $i planches"
done
echo "TERMINE"

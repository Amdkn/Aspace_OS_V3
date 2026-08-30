#!/bin/bash
# Recupere les demos Palantir et en tire transcription + planches-contact.
#
# Reprise de vision-v1/extrait.sh, qui a fait ses preuves : une demo produit se
# lit a l'ecran, pas dans les mots. Les planches valent la transcription.
#
# En CHAINE, jamais en parallele : ffmpeg sature deux coeurs a lui seul, et la
# machine a deja affiche un 0xc000012d sous cette charge (cf. vision-v1/tout.sh).
set -u
B=/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/palantir-2.0/10_sources/videos
YTDLP=/c/Users/amado/bin/yt-dlp

extrait() {
  ID="$1"; NOM="$2"
  D="$B/$NOM"; mkdir -p "$D/frames" "$D/planches"
  cd "$D" || return 1

  # Deja fait ? on ne retelecharge pas — le script doit etre relancable.
  if [ -f "$D/.termine" ]; then echo "$NOM : deja fait, saute" >> "$B/bilan.txt"; return 0; fi

  "$YTDLP" -f "bv*[height<=720]+ba/b[height<=720]" -o "video.%(ext)s" \
    --write-auto-subs --write-subs --sub-langs "en.*,fr.*" --convert-subs vtt \
    "https://www.youtube.com/watch?v=$ID" >> "$D/extraction.log" 2>&1

  V=$(ls video.* 2>/dev/null | grep -v vtt | head -1)
  [ -z "$V" ] && { echo "$NOM : ECHEC telechargement" >> "$B/bilan.txt"; return 1; }

  # Une image toutes les 10 s : assez dense pour suivre une demo, assez legere
  # pour rester lisible par un agent.
  ffmpeg -hide_banner -loglevel error -i "$V" -vf "fps=1/10,scale=854:-1" \
    "frames/%04d.png" >> "$D/extraction.log" 2>&1

  # Planches-contact de 20 vignettes : un agent lit dix planches, pas deux cents images.
  ffmpeg -hide_banner -loglevel error -start_number 1 -i "frames/%04d.png" \
    -vf "scale=427:-1,tile=4x5" "planches/planche-%02d.png" >> "$D/extraction.log" 2>&1

  # La video pese lourd et n'a plus d'usage une fois les frames tirees.
  rm -f "$V"
  touch "$D/.termine"
  echo "$NOM : $(ls frames/*.png 2>/dev/null|wc -l) images, $(ls planches/*.png 2>/dev/null|wc -l) planches" >> "$B/bilan.txt"
}

# Ordre = densite d'interface reelle decroissante. Si la machine s'arrete en
# route, les plus utiles sont deja tirees.
extrait uF-GSj-Exms foundry-2022-os-demo
extrait SePXznjZ-1A agentic-os-aipcon6
extrait akieze8_tSE aip-capabilities-shyam
extrait mzBDupsPPcs ontology-governance
extrait 6_cyrBAf_dQ pipeline-builder
extrait 2lgwr7trSgw vibe-coding-aip
extrait k88WbxMEvPY architecture-speedrun
extrait Xt_RLNx1eBM introducing-aip
extrait YDAxITCNcko ontology-overview
extrait h4R1cOlJJ7o foundry-21-demoday

echo "=== TERMINE ===" >> "$B/bilan.txt"

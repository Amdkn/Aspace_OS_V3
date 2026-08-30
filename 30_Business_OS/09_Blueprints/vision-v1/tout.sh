#!/bin/bash
# En chaine, pas en parallele : ffmpeg sature deux coeurs a lui seul, et la
# machine a deja affiche un 0xc000012d ce soir sous la charge.
B=/c/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/vision-v1
bash $B/extrait.sh cT0zEwF39Q0 shubham-linkedin
bash $B/extrait.sh -V9VIrwGtSs melvynx-feature
bash $B/extrait.sh BwZbdCzmZJc langgraph
bash $B/extrait.sh UaeWJK_vv-Y agent-plugins
for d in shubham-linkedin melvynx-feature langgraph agent-plugins; do
  cd "$B/$d" 2>/dev/null && ffmpeg -hide_banner -loglevel error -start_number 1 \
    -i "frames/%04d.png" -vf "scale=427:-1,tile=4x5" "planches/planche-%02d.png" 2>/dev/null
  echo "$d : $(ls $B/$d/frames/*.png 2>/dev/null|wc -l) images, $(ls $B/$d/planches/*.png 2>/dev/null|wc -l) planches" >> "$B/bilan.txt"
done

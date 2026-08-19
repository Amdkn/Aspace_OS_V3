"""Vague 2 — huit escouades de domaine, en parallelisme natif.

POURQUOI HUIT AGENTS ET PAS UN
La Vague 1 avait UN agent `b2` qui posait les regles de coordination pour les
huit domaines. Il l'a fait : regle d'arbitrage, catalogue des huit vetos,
matrice d'harmonisation, RACI par rang. **La condition de deblocage est donc
remplie** — sans elle, huit escouades se marcheraient dessus faute de regle
pour trancher entre elles.

Chaque domaine ecrit maintenant dans SON dossier. Aucun ne peut ecraser un
autre, et la coordination passe par la regle deja posee, pas par la
negociation entre agents.

LE PIEGE DU NOM DE DOMAINE
Le corpus nomme les domaines par leurs personas DC — Aquaman 108 mentions,
Wonder Woman 65, Batman 63, Superman 47, Cyborg 42, Green Lantern 39,
Flash 39, et un huitieme en Illuminati / Martian / John Jones.

**On ne leur assigne PAS de domaine metier ici.** Un rapport anterieur note
que SDD-006 decrivait 7 domaines quand le canon a jour en compte 8, et que le
code etait en avance sur le document. Chaque agent doit donc **lire** quel
domaine il porte, pas le recevoir d'un script qui l'aurait devine.
"""

import io
import os

V3 = r"C:\Users\amado\ASpace_OS_V3"
L = os.path.join(V3, "60_Implementation_Méthodologiques", "_loop")
BASE = "C:/Users/amado/ASpace_OS_V3"

DOMAINES = [
    ("aquaman",      "Aquaman",       108),
    ("wonder-woman", "Wonder Woman",   65),
    ("batman",       "Batman",         63),
    ("superman",     "Superman",       47),
    ("cyborg",       "Cyborg",         42),
    ("green-lantern","Green Lantern",  39),
    ("flash",        "Flash",          39),
    ("john-jones",   "John Jones / Martian / Illuminati", 23),
]

BRIEF = """# BRIEF — escouade de domaine : {nom}

## Ton perimetre EXCLUSIF en ecriture

```
{base}/70_Onthologies/pulse/domaines/{cle}/
{base}/60_Implementation_Méthodologiques/_loop/RAPPORT_dom-{cle}.md
```

**Sept autres escouades travaillent en parallele**, chacune dans son dossier.
Tu ne touches a rien d'autre — surtout pas au dossier d'un autre domaine.

## La premiere chose a faire : savoir quel domaine tu portes

Le corpus te nomme **{nom}** ({mentions} mentions). Il ne te dit pas ici quel
domaine metier tu couvres — **c'est a toi de le lire**, pas a moi de te le
donner.

Un rapport anterieur a mesure que `SDD-006` decrivait **7 domaines** quand le
canon a jour en compte **8** : le code etait en avance sur le document. Si je
t'assignais un domaine, je risquerais de propager cette erreur.

Cherche dans :

```
{base}/50_Distillation/projets/eight-domain-avengers-wheel.md
{base}/50_Distillation/areas/business-wheel-harmonization-matrix.md
{base}/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md
{base}/50_Distillation/projets/fifty-three-b3-agent-roster.md
```

**Si tu ne trouves pas ton domaine, ecris-le et arrete-toi.** Une escouade qui
invente son perimetre produit du plausible sur un sujet qui n'existe pas.

## Les regles que B2 a deja posees, et que tu ne rediscutes pas

```
{base}/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md
{base}/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md
{base}/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md
{base}/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md
{base}/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md
{base}/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md
```

**Lis-les avant d'ecrire.** C'est ce qui permet a huit escouades de travailler
sans se coordonner entre elles : la regle d'arbitrage existe deja, tu
l'appliques.

Si une regle te parait fausse pour ton domaine, **ne la contourne pas** :
signale-le dans ton rapport. C'est une remontee vers B2, pas une decision a
ton etage.

## Ce que ton escouade produit

**4 a 8 concepts OKF v0.2** dans ton dossier, en `kebab-case.md`, sources
reelles. Ils repondent a quatre questions sur TON domaine :

1. **Que couvre-t-il exactement**, et ou s'arrete-t-il ? Une frontiere floue
   entre deux domaines est un conflit d'arbitrage qui attend.
2. **Quel est son veto** ? Le catalogue de B2 en donne un par capitaine. Dis
   dans quels cas concrets il se declenche, et dans quels cas il serait abusif.
3. **Quels paquets JTBD** ce domaine emet vers B3, et lesquels il recoit ?
4. **Sur quoi depend-il** d'un autre domaine, et lequel depend de lui ?

La question 4 est la plus utile : c'est elle qui revele les couplages que la
matrice d'harmonisation ne montre pas.

## Ta ligne d'etat

Ajoute **une ligne** a la fin de
`{base}/70_Onthologies/pulse/domaines/ETAT_DOMAINES.md`, sous une section
`## {nom}` que tu creeras si elle manque.

**En ajout seul.** Sept autres escouades ecrivent dans ce fichier ; une
reecriture les effacerait sans que personne ne le voie.

## Ton rapport

`_loop/RAPPORT_dom-{cle}.md` — avec, en dernier parce que c'est le plus
important : **ce que le corpus ne dit pas** sur ton domaine, et les regles de
B2 qui te paraissent mal ajustees.
"""

BOUCLE2 = r"""#!/usr/bin/env bash
# Vague 2 — huit escouades de domaine, quatre par tour.
#   Usage : ./boucle2.sh [heures]      (defaut : 4)
#
# Le verrou a jetons est partage avec toute autre boucle du poste : deux
# boucles qui comptent en meme temps verraient toutes deux de la place. Le
# jeton, lui, ne se prend qu'une fois.

set -u
HEURES="${1:-4}"
V3="C:/Users/amado/ASpace_OS_V3"
L="$V3/60_Implementation_Méthodologiques/_loop"
source "$L/slots.sh"
FIN=$(( $(date +%s) + HEURES * 3600 ))

export ANTHROPIC_BASE_URL="https://api.minimax.io/anthropic"
export ANTHROPIC_API_KEY="$(python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])")"
export ANTHROPIC_MODEL="MiniMax-M3[1m]"
export ANTHROPIC_SMALL_FAST_MODEL="MiniMax-M3[1m]"

DOMAINES=(aquaman wonder-woman batman superman cyborg green-lantern flash john-jones)

lancer_dom() {
  local d="$1" tour="$2"
  local brief="$L/BRIEF_dom-${d}.md"
  [ -f "$brief" ] || { echo "brief manquant : $brief" >&2; return 1; }
  local jeton
  jeton=$(attendre_jeton "dom-$d/t$tour" 2400) || {
    echo "[$(date +%H:%M:%S)] dom-$d tour $tour : aucun jeton, saute" >> "$L/VAGUE2.log"; return 1; }
  cd "$V3" || return 1
  cat "$L/MODE_FABLE.md" "$brief" \
    | /c/Users/amado/AppData/Roaming/npm/claude -p --permission-mode bypassPermissions \
    > "$L/journal_dom-${d}_t${tour}.log" 2>&1
  local code=$?
  rendre_jeton "$jeton"
  echo "[$(date +%H:%M:%S)] dom-$d tour $tour termine (exit=$code)" >> "$L/VAGUE2.log"
}

tour=0
echo "[$(date +%H:%M:%S)] Vague 2 demarree — 8 domaines, echeance ${HEURES}h" > "$L/VAGUE2.log"

while true; do
  [ -f "$L/STOP2" ] && { echo "[$(date +%H:%M:%S)] STOP2 — arret propre" >> "$L/VAGUE2.log"; break; }
  [ "$(date +%s)" -ge "$FIN" ] && { echo "[$(date +%H:%M:%S)] echeance — arret" >> "$L/VAGUE2.log"; break; }

  tour=$((tour + 1))
  # Deux vagues de quatre : les huit domaines passent a chaque tour.
  for groupe in "0 1 2 3" "4 5 6 7"; do
    echo "[$(date +%H:%M:%S)] tour $tour, groupe $groupe" >> "$L/VAGUE2.log"
    for i in $groupe; do
      lancer_dom "${DOMAINES[$i]}" "$tour" &
      sleep 30
    done
    wait
  done
done

echo "[$(date +%H:%M:%S)] Vague 2 terminee apres $tour tours" >> "$L/VAGUE2.log"
"""

ETAT_DOM = """# ETAT DES DOMAINES — Vague 2

Point de rendez-vous des huit escouades. **Ajout seul, jamais de reecriture** :
huit agents ecrivent ici, une reecriture en effacerait sept sans que personne
ne le voie.

Format : `- [tour N] <ce qui a ete pose>, <ce qui reste ouvert>`
"""


def main():
    dom_dir = os.path.join(V3, "70_Onthologies", "pulse", "domaines")
    os.makedirs(dom_dir, exist_ok=True)
    for cle, nom, mentions in DOMAINES:
        os.makedirs(os.path.join(dom_dir, cle), exist_ok=True)
        txt = BRIEF.format(cle=cle, nom=nom, mentions=mentions, base=BASE)
        io.open(os.path.join(L, f"BRIEF_dom-{cle}.md"), "w", encoding="utf-8").write(txt)
        print(f"BRIEF_dom-{cle}.md  {len(txt)} octets")

    io.open(os.path.join(L, "boucle2.sh"), "w", encoding="utf-8", newline="\n").write(BOUCLE2)
    etat = os.path.join(dom_dir, "ETAT_DOMAINES.md")
    if not os.path.exists(etat):
        io.open(etat, "w", encoding="utf-8").write(ETAT_DOM)
    print("boucle2.sh et ETAT_DOMAINES.md poses")


if __name__ == "__main__":
    main()

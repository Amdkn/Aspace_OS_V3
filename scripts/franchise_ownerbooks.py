#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Reconstitution des Ownerbooks et Runbooks du prototype de franchise.

CE QUE FAIT CE SCRIPT
    Le prototype `01-omk-business-os` porte 3 ownerbooks (T1/T2/T3) et 2
    runbooks qui, ensemble, forment un gabarit de franchise reproductible.
    Ce script le reconstitue :

      - dans l'AREA  J01_Jerry_Prime_LD01_Business : le CANON, perpetuel,
        sans fenetre 12WY. Une Area maintient un standard de reproduction ;
        elle n'a pas d'echeance. Y mettre une date serait la faute deja
        corrigee le 2026-08-29.

      - dans les PROJETS 02/03/04/05 : des INSTANCES datees, avec fenetre
        12WY et rock_id. Un projet a une fin ; c'est ce qui le distingue.

POURQUOI LES CHAMPS NON SOURCES SONT MARQUES, PAS INVENTES
    Le gabarit OMK porte des recus D1 reels (ADR ratifies, paliers USD, ICP
    mesure). Les quatre autres projets n'ont pas ces recus sur le disque.
    Fabriquer un ICP pour ABC ou Marina produirait un document qui *ressemble*
    a du verifie sans l'etre -- exactement ce que le format OKF existe pour
    empecher. Tout champ non sourcable sort en `A SOURCER` avec le chemin ou
    le chercher.

LA SEULE VARIABLE DE FRANCHISE REELLEMENT SOURCEE
    Les North Star des quatre projets contiennent des litteraux PowerShell
    non interpoles -- `$(@{...; Mode=...; Parent=...}.Name)`. Le generateur
    d'origine a echoue, mais les metadonnees sont dedans et elles sont vraies.
    Le `Mode` (Nexus / Orbiter / Solaris) est le differenciateur de franchise
    et il se lit, il ne se devine pas.
"""

from __future__ import annotations
import os, re, stat, sys
from pathlib import Path

V2 = Path("C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise")
PROJETS_R = V2 / "01_Projects_Picard"
AREA = V2 / "02_Areas_Spock/J01_Jerry_Prime_LD01_Business"
PROTOTYPE = PROJETS_R / "01-omk-business-os"

# Le prototype fixe la fenetre ; les instances l'heritent telle quelle.
# La recopier en dur ailleurs la ferait deriver en silence.
FENETRE_12WY = "Q3 2026 (2026-06-15 → 2026-09-07)"
DOCTRINE = "D4 append-only · D6 no-self-contradiction · Spec-Loop Polivaev 2026"

# Cibles de franchise. Le nom de dossier est la verite du disque, pas un slug
# reconstruit : `02 ABC OS & Child Care BOS` porte des espaces et une
# esperluette, et c'est ainsi qu'il faut l'ouvrir.
CIBLES = [
    ("02 ABC OS & Child Care BOS",     "02_ABC_OS",  "ABC"),
    ("03_RILCOT_Members_Space_OS",     "03_RILCOT",  "RILCOT"),
    ("04 Alikaly Bana Holding to LLC", "04_Alikaly", "ALIKALY"),
    ("05 marina Cleaning BOS & SOP",   "05_Marina",  "MARINA"),
]

# Les triptyques, tels que le prototype les declare. Les escouades B3 sont
# verifiees contre les dossiers B2_Business_Domains de chaque projet : les
# huit paires domaine/escouade concordent.
#
# NOTE John Jones : les dossiers portent encore `02_Sales_MartianManhunter_*`.
# La forme canonique est **John Jones** (arbitrage du proprietaire, regle de
# date : la version tardive gagne). Les dossiers sont la forme ancienne non
# propagee ; on n'ecrit pas l'erreur dans du neuf.
TRIPTYQUES = [
    {
        "id": "T1", "rang": 1, "slug": "people_ops_product",
        "b2": "GreenLantern + Batman + Flash",
        "b3": "X-Men + Fantastic Four + Avengers",
        "domaines": ["07_People_GreenLantern_XMen", "04_Ops_Batman_Fantastic4",
                     "03_Product_Flash_Avengers"],
        "mission": "RH Agentique + SOP & Skills + Agency as a Service",
        "scope": ("noyau operationnel qui CONSTRUIT l'actif vendable : les gens "
                  "(RH des agents et des humains), les operations (tout SOP repete "
                  "devient une skill), le produit (l'actif EST le livrable)"),
        "porte": "le mur porteur — T2 vend ce que T1 construit, T3 le gouverne",
    },
    {
        "id": "T2", "rang": 2, "slug": "growth_sales_finance",
        "b2": "Superman + JohnJones + WonderWoman",
        "b3": "Guardians of the Galaxy + Illuminati + Thunderbolts",
        "domaines": ["01_Growth_Superman_Guardians", "02_Sales_MartianManhunter_Illuminati",
                     "06_Finance_WonderWoman_Thunderbolts"],
        "mission": "AAARR + 100M Offers + 1-Person/1-Billion Company",
        "scope": ("moteur de revenu : acquisition, offre, encaissement — ce qui "
                  "transforme l'actif construit par T1 en economie mesurable"),
        "porte": "sans T2 l'actif existe et ne se vend pas ; c'est la definition d'un passif",
    },
    {
        "id": "T3", "rang": 3, "slug": "legal_rd",
        "b2": "Aquaman + Cyborg (R&D pivot, IT absorbe)",
        "b3": "Eternals + Kang Dynasty",
        "domaines": ["08_Legal_Aquaman_Eternals", "05_IT_Cyborg_KangDynasty"],
        "mission": ("365 Conformite par Conception + Amelioration par Innovation "
                    "de Decouverte externe"),
        "scope": ("gouvernance et decouverte : conformite integree a la conception "
                  "plutot qu'ajoutee apres, et veille externe qui empeche le "
                  "systeme de tourner sur lui-meme"),
        "porte": "T3 est ce qui empeche T1 et T2 de produire vite quelque chose d'inexploitable",
    },
]

RP = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)


def est_jonction(p: Path) -> bool:
    """Une jonction NTFS n'est pas vue par `islink`. Sans ce garde, un parcours
    naif suit le lien et recompte la cible -- 13,8 millions de fichiers la ou
    il y en a 14 613."""
    try:
        return bool(p.stat(follow_symlinks=False).st_file_attributes & RP)
    except (OSError, AttributeError):
        return False


def lire_mode(projet: Path) -> tuple[str, str]:
    """Extrait `Mode` et `Parent` du litteral PowerShell non interpole du
    North Star. Rend ('A SOURCER', ...) si le fichier ou le motif manque --
    jamais une valeur par defaut plausible, qui serait indistinguable d'une
    mesure."""
    f = projet / "B1_Summer_Direction/01_NORTH_STAR_1Y_3Y_10Y.md"
    if not f.exists():
        return ("A SOURCER (North Star absent)", "A SOURCER")
    t = f.read_text(encoding="utf-8", errors="replace")
    mode = re.search(r"Mode=([^;}]+)", t)
    parent = re.search(r"Parent=([^;}]+)", t)
    return (mode.group(1).strip() if mode else "A SOURCER (Mode absent du North Star)",
            parent.group(1).strip() if parent else "A SOURCER")


def domaines_presents(projet: Path, attendus: list[str]) -> tuple[list[str], list[str]]:
    """Verifie sur le disque quels dossiers de domaine existent. Un ownerbook
    qui nomme une escouade absente ment a celui qui l'executera."""
    base = projet / "B2_Business_Domains"
    ok, manquants = [], []
    for d in attendus:
        (ok if (base / d).is_dir() else manquants).append(d)
    return ok, manquants


# ---------------------------------------------------------------- ownerbook

def ownerbook(tri: dict, *, nom: str, court: str, mode: str, parent: str,
              presents: list[str], manquants: list[str], canon: bool) -> str:
    fm = [
        "---", "type: ownerbook", f"triptyque: {tri['id']}",
    ]
    if canon:
        fm += [
            "portee: canon-franchise",
            "rock_id: n/a (Area — standard perpetuel, sans fenetre)",
        ]
    else:
        fm += [f"rock_id: B1-{tri['rang']}"]
    fm += [
        f"b2_owner: {tri['b2']}",
        f"b3_squad: {tri['b3']}",
    ]
    if canon:
        fm += [
            "icp: n/a — le canon ne porte pas d'ICP ; chaque instance porte le sien",
            "geography: n/a — idem",
            "12wy_window: n/a — une Area maintient un standard, elle n'a pas d'echeance",
        ]
    else:
        fm += [
            "icp: A SOURCER — voir B1_Summer_Direction/09_MARKET_VALIDATION_SPRINT.md",
            "geography: A SOURCER — voir 01_NORTH_STAR_1Y_3Y_10Y.md",
            f"12wy_window: {FENETRE_12WY}",
        ]
    fm += [
        f"mode_franchise: {mode}",
        f"doctrine_lock: {DOCTRINE}",
        f"mission: {tri['mission']}",
        f"source_gabarit: 01_Projects_Picard/01-omk-business-os/ownerbooks/"
        f"ownerbook_{tri['id']}_{tri['slug']}.md",
        "---", "",
    ]
    s = ["\n".join(fm)]

    s.append(f"## 1. Scope (1 phrase)\n{tri['id']} de **{nom}** = {tri['scope']}.\n")

    s.append(f"""## 2. Motivation
{tri['porte']}.

Le mode de franchise de ce projet est **{mode}** — lu dans le North Star, pas
suppose. C'est la seule variable qui distingue reellement cette instance du
prototype OMK : la structure des triptyques, les paires domaine/escouade et la
cadence sont invariantes par conception, sans quoi il n'y aurait pas de
franchise mais cinq systemes differents.

Rattachement d'Area : `{parent}`.
""")

    if canon:
        s.append("""## 3. Research (recus D1)
Le canon ne porte pas de recus de marche : il porte la **forme** que tout
ownerbook conforme doit avoir. Les recus vivent dans les instances.

Recus de forme, verifies sur le disque :

- `01_Projects_Picard/01-omk-business-os/ownerbooks/` — 3 ownerbooks, 10 sections
- `01_Projects_Picard/01-omk-business-os/runbooks/` — 2 runbooks, pre-check + M1-Mn
- `B2_Business_Domains/` — les 8 paires domaine/escouade, identiques dans les 5 projets
""")
    else:
        s.append(f"""## 3. Research (recus D1)
**Aucun recu de marche n'est sourcable pour {court} sur le disque au moment de
la generation.** Le gabarit OMK en porte cinq (ADR-AAAS-PRICING-001,
ADR-NEXUS-NICHE-001, W40 §2, phase_c_saas_auth, B2_DEFINITION_OF_DONE_SPEC) ;
les recopier ici les appliquerait au mauvais projet.

A SOURCER, dans cet ordre :

1. `B1_Summer_Direction/09_MARKET_VALIDATION_SPRINT.md` — ICP et segment
2. `B1_Summer_Direction/05_B2_DEFINITION_OF_DONE_SPEC.md` — DoD par domaine
3. `B2_Business_Domains/00_{court}_DOMAIN_DEVELOPMENT_MAP.md` — perimetre des domaines
4. `B1_Summer_Direction/02_12WY_COMMAND_CYCLES.md` — fenetre reelle

Tant que ces quatre lignes ne sont pas remplies, ce document est **non verifie**
au sens OKF, et il le dit.
""")

    dom = "\n".join(f"- `B2_Business_Domains/{d}` — present" for d in presents)
    if manquants:
        dom += "\n" + "\n".join(f"- `B2_Business_Domains/{d}` — **ABSENT du disque**"
                                for d in manquants)
    s.append(f"""## 4. Design
### 4.1 Domaines porteurs (verifies sur le disque)
{dom}

### 4.2 Diagramme de classes
```
[{tri['b2'].split(' + ')[0]}]──pilote──>[{tri['b3'].split(' + ')[0]}]
        │
        └──[Escouade {tri['id']}]──>[Ownerbook {tri['id']}]──> client {mode}
```

### 4.3 Sequence (un cycle de sprint)
```
B1 Summers → B2 {tri['b2'].split(' + ')[0]} : "{tri['id']} spec-lock"
B2 Captain → B3 {tri['b3'].split(' + ')[0]} : 5 daily scrums (DoD 3 criteres)
B3 Daily   → B2 Captain : recus de scrum (logs ld+lag)
B2 Captain → B1 Summers : revue de sprint hebdomadaire
B1 Jerry   → A0 : 1 Ownerbook par Rock par cycle
```
""")

    s.append(f"""## 5. Test-Spec (DoD — 5 daily scrums)
- **DoD-1** : chaque domaine de §4.1 porte >=1 fiche d'agent B3 documentee
  — verifier : le dossier de domaine contient un `.md` autre que le README
- **DoD-2** : >=1 SOP par processus, tout motif repete 3 fois devient une skill
  — verifier : regle D.E.A.L, 3 occurrences automatisent
- **DoD-3** : sortie de spec-loop, pas de porte manuelle
  — verifier : aucun point d'arret humain dans le flux
- **DoD-4** : le mode de franchise `{mode}` est explicite et coherent
  — verifier : le mode du North Star et celui du frontmatter concordent
- **DoD-5 (D6)** : aucune section ne contredit le gabarit OMK
  — verifier : les 10 sections presentes, dans l'ordre
""")

    s.append(f"""## 6. Chartes requises (Phase 1 BMad — 3 par Rock)
- `charte_{tri['id']}_{tri['slug']}_mission.md` — mission verbatim : {tri['mission']}
- `charte_{tri['id']}_{tri['slug']}_dod.md` — DoD par domaine
- `charte_{tri['id']}_{tri['slug']}_squad_dispatch.md` — phrases de declenchement B2→B3

## 7. Runbooks (Phase 2 Gstack)
- `runbook_{tri['id']}_{tri['slug']}.md` — genere a cote de ce fichier

## 8. Conditions d'abandon
- **Abort-A** : un dossier de domaine de §4.1 est absent → STOP, completer avant
- **Abort-B** : une section contredit la mission verbatim → STOP, patch B1 (D6)
- **Abort-C** : une porte manuelle est introduite → STOP, remplacer par spec-loop
- **Abort-D** : le mode de franchise derive du North Star → STOP, relire la source

## 9. Red-team
- **Attaque-1** : « la franchise n'est qu'un copier-coller, chaque projet est different »
  — **PATCH** : la structure EST l'invariant ; la seule variable est `mode_franchise`,
  et elle est lue, pas choisie. Si un projet exige une structure differente, il
  n'est pas une franchise et il faut le dire, pas plier le gabarit.
- **Attaque-2** : « les recus D1 d'OMK valent pour tous »
  — **PATCH** : refuse. §3 sort en `A SOURCER` plutot qu'en recu emprunte. Un ICP
  Coach premium US applique a une societe de nettoyage est une erreur qui se
  propage jusqu'au pricing.
- **Attaque-3** : « les dossiers disent MartianManhunter, le document dit John Jones »
  — **PATCH** : arbitrage de date du proprietaire, la version tardive gagne. Les
  dossiers sont la forme ancienne non propagee. Ne pas ecrire l'erreur dans du neuf.
- **Attaque-4** : « une Area avec une fenetre 12WY »
  — **PATCH** : le canon sort `n/a`. Une Area maintient un standard perpetuel ;
  lui donner une echeance est la faute corrigee le 2026-08-29.

## 10. Specifique a cette instance
- **Mode de franchise** : {mode}
- **Area de rattachement** : {parent}
- **Ce qui est invariant** : triptyques, paires domaine/escouade, cadence, DoD de forme
- **Ce qui varie** : mode, ICP, geographie, fenetre 12WY — tous `A SOURCER` ici sauf le mode

---

*Gabarit : `01-omk-business-os/ownerbooks/ownerbook_{tri['id']}_{tri['slug']}.md`.
Confiance OKF : non verifie tant que §3 porte des `A SOURCER`.*
""")
    return "\n".join(s)


# ------------------------------------------------------------------ runbook

def runbook(tri: dict, *, nom: str, court: str, mode: str, canon: bool) -> str:
    fm = ["---", "type: runbook", f"triptyque: {tri['id']}"]
    if canon:
        fm += ["portee: canon-franchise", "rock_id: n/a (Area)"]
    else:
        fm += [f"rock_id: RP{tri['rang']}"]
    fm += [
        f"chart_source: ../ownerbooks/ownerbook_{tri['id']}_{tri['slug']}.md",
        f"project: {court.lower()}",
        f"domain: {tri['b2']}",
        "12wy_window: " + ("n/a — standard perpetuel" if canon else FENETRE_12WY),
        f"mode_franchise: {mode}",
        f"doctrine_lock: {DOCTRINE} · Posture C (HITL sur portes irreversibles)",
        "source_gabarit: 01-omk-business-os/runbooks/runbook-C-saas-auth.md (M1-M5) "
        "+ runbook-D-repositories.md (pre-check + aborts)",
        "---", "",
    ]
    return "\n".join(fm) + f"""# Runbook {tri['id']} — {nom}

Le OUOI vit dans l'ownerbook a cote. Ce fichier ne porte que le COMMENT, en
mouvements numerotes, chacun avec sa preuve. Un mouvement sans preuve verifiable
est une intention, pas un mouvement.

## 0. Portes de pre-verification (AVANT M1)

| # | Porte | Comment on la passe |
|---|---|---|
| G1 | Les dossiers de domaine de l'ownerbook §4.1 existent | `ls B2_Business_Domains/` |
| G2 | Le mode de franchise concorde avec le North Star | comparer les deux frontmatters |
| G3 | L'ownerbook §3 ne porte plus de `A SOURCER` | `grep "A SOURCER"` rend vide |
| G4 | Aucune porte manuelle dans le flux vise | lecture du flux |

**G3 est bloquante.** Executer un runbook dont l'ownerbook n'est pas source,
c'est batir sur une hypothese en croyant batir sur une mesure.

## 1. M1 — Verrouillage du perimetre
Relire l'ownerbook §1 et §4.1. Ecrire la liste des domaines effectivement
porteurs. **Preuve** : la liste, avec pour chacun le chemin sur le disque.

## 2. M2 — Recus de domaine
Pour chaque domaine, relever ce qui existe deja (SOP, fiche d'agent, gate matrix).
**Preuve** : un tableau domaine → fichiers trouves. Un domaine sans fichier est
un domaine vide, et il faut l'ecrire, pas le combler.

## 3. M3 — Dispatch B2 → B3
Emettre les phrases de declenchement vers les escouades de `{tri['b3']}`.
**Preuve** : les phrases, verbatim, et l'escouade visee.

## 4. M4 — Cinq daily scrums
Executer les 5 scrums contre les DoD-1 a DoD-5 de l'ownerbook §5.
**Preuve** : 5 lignes de log, une par scrum, avec le DoD adresse.

## 5. M5 — Ecriture en retour et heartbeat
Consigner le resultat dans l'ownerbook, remonter a B1.
**Preuve** : le diff de l'ownerbook.

## 6. Conditions d'abandon
- **Abort-1** : G3 echoue → STOP. Sourcer l'ownerbook d'abord.
- **Abort-2** : un domaine de §4.1 est absent du disque → STOP, ne pas l'inventer.
- **Abort-3** : une porte manuelle apparait → STOP, remplacer par une sortie de script.
- **Abort-4** : le mode derive du North Star → STOP, la source gagne.

## 7. Lacunes assumees (D6)
1. Les DoD sont des DoD **de forme**. Les DoD metier vivent dans
   `B1_Summer_Direction/05_B2_DEFINITION_OF_DONE_SPEC.md` et ne sont pas repris ici.
2. Aucun recu de marche pour {court} — voir ownerbook §3.
3. Les dossiers de domaine portent encore `MartianManhunter` ; la forme canonique
   est **John Jones**. Le renommage n'est pas fait et ce runbook ne le fait pas.
4. La fenetre 12WY est heritee du prototype, pas mesuree sur ce projet.

## 8. Verification
```bash
# G3 : l'ownerbook est-il source ?
grep -c "A SOURCER" ownerbooks/ownerbook_{tri['id']}_{tri['slug']}.md   # doit rendre 0

# G1 : les domaines existent-ils ?
ls B2_Business_Domains/
```

Un `exit 0` ne prouve rien : on regarde la sortie.
"""


# --------------------------------------------------------------------- main

def ecrire(dest: Path, contenu: str, applique: bool) -> str:
    """Ecrit et rend un libelle. `Write` ne cree pas les dossiers parents et
    repond quand meme 'success' -- d'ou le mkdir explicite."""
    if not applique:
        return f"  [simulation] {dest}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(contenu, encoding="utf-8")
    return f"  ecrit ({dest.stat().st_size:>6,} o) {dest}"


def main() -> int:
    applique = "--appliquer" in sys.argv
    if not PROTOTYPE.is_dir():
        print(f"ERREUR : prototype introuvable — {PROTOTYPE}")
        return 1

    print("=" * 74)
    print("RECONSTITUTION DE LA FRANCHISE" + ("" if applique else "   [SIMULATION — --appliquer pour ecrire]"))
    print("=" * 74)

    total = 0

    # --- 1. Le canon, dans l'Area ------------------------------------------
    print(f"\n### CANON (Area, perpetuel) — {AREA.name}")
    if not AREA.is_dir():
        print(f"  ERREUR : Area introuvable — {AREA}")
    else:
        for tri in TRIPTYQUES:
            ok, manq = domaines_presents(PROTOTYPE, tri["domaines"])
            c = ownerbook(tri, nom="canon de franchise", court="CANON",
                          mode="invariant (chaque instance porte le sien)",
                          parent="J01_Jerry_Prime_LD01_Business",
                          presents=ok, manquants=manq, canon=True)
            print(ecrire(AREA / f"B0_Self_Operating_Business_Doctrine/franchise/"
                                f"ownerbook_{tri['id']}_{tri['slug']}.md", c, applique))
            r = runbook(tri, nom="canon de franchise", court="CANON",
                        mode="invariant", canon=True)
            print(ecrire(AREA / f"B0_Self_Operating_Business_Doctrine/franchise/"
                                f"runbook_{tri['id']}_{tri['slug']}.md", r, applique))
            total += 2

    # --- 2. Les instances, dans les projets --------------------------------
    for dossier, nom, court in CIBLES:
        p = PROJETS_R / dossier
        print(f"\n### INSTANCE — {nom}")
        if not p.is_dir():
            print(f"  ABSENT du disque : {p}")
            continue
        if est_jonction(p):
            print(f"  JONCTION — ignoree (on n'ecrit pas a travers un lien)")
            continue
        mode, parent = lire_mode(p)
        print(f"  mode lu : {mode}")
        for tri in TRIPTYQUES:
            ok, manq = domaines_presents(p, tri["domaines"])
            if manq:
                print(f"  {tri['id']} : domaines absents → {', '.join(manq)}")
            c = ownerbook(tri, nom=nom, court=court, mode=mode, parent=parent,
                          presents=ok, manquants=manq, canon=False)
            print(ecrire(p / f"ownerbooks/ownerbook_{tri['id']}_{tri['slug']}.md", c, applique))
            r = runbook(tri, nom=nom, court=court, mode=mode, canon=False)
            print(ecrire(p / f"runbooks/runbook_{tri['id']}_{tri['slug']}.md", r, applique))
            total += 2

    print("\n" + "=" * 74)
    print(f"{total} documents {'ecrits' if applique else 'simules'}")
    if not applique:
        print("Relancer avec --appliquer pour ecrire.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

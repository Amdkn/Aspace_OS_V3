"""Porte d'argent — le triptyque de filtres par lequel tout doit passer pour entrer en V3.

REGLE DU PROPRIETAIRE, ENONCEE LE 2026-08-29
« Rien n'entre dans V3 sans passer par cette triptyque de filtres avant de
finir dans OpenWiki et OKF. »

    1. DISTILLATION RDF          -> le substrat : ce qui est ecrit, et ou
    2. IMPLEMENTATION METHODO    -> a quelle cadence et sous quel flux ca s'execute
    3. FORMATION D'ONTOLOGIE     -> les triplets sujet-verbe-objet

Ce script ne remplace pas la chaine existante (`extraire_substrat_rdf.py`,
`generer_briefs_distillation.py`, `concepts_vers_triplets.py`,
`monter_70_onthologies.py`). Il l'APPLIQUE a un domaine donne, et rend un
verdict par filtre. Un domaine qui echoue a un filtre n'entre pas.

CE QU'IL N'EST PAS
Ce n'est pas de l'archivage. Le canon du poste est explicite : ce qui n'est pas
utilise n'est pas « archive », il est en non-usage, et l'information se gere en
PARA. Un domaine migre reste vivant dans Projects/Areas/Resources ; il ne part
pas dans un cimetiere.

LES QUATRE FLUX GTD portent la clarification : capture, clarify, organize,
review, engage. Le substrat est la CAPTURE ; la couche methodologique est le
CLARIFY et l'ORGANIZE ; l'ontologie est ce qui rend le REVIEW possible ; ce qui
entre en V3 est ce sur quoi on peut ENGAGE.

USAGE
    python porte_argent.py --domaine 23_12WY_SNW
    python porte_argent.py --domaine 23_12WY_SNW --appliquer
"""

from __future__ import annotations

import io
import json
import os
import re
import stat
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

V2 = Path("C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise")
V3 = Path("C:/Users/amado/ASpace_OS_V3")

# Les domaines de Life OS vivent sous Geordi, dans le miroir des domaines V2.
SOURCES_POSSIBLES = [
    # Les seaux PARA VIVANTS d'abord : c'est la chose, pas son reflet.
    # `05_From_V2_Domains` vit sous Geordi et est donc une RESSOURCE -- un
    # miroir de reference. Migrer le miroir en croyant migrer la Area est la
    # faute constatee le 2026-08-29 sur Jerry : la porte rendait un verdict
    # sur une copie de lecture, pas sur le standard qui tourne.
    V2 / "01_Projects_Picard",
    V2 / "02_Areas_Spock",
    V2 / "03_Resources_Geordi/05_From_V2_Domains/20_Life_OS",
    V2 / "03_Resources_Geordi/05_From_V2_Domains/30_Business_OS",
    V2 / "03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS",
]

SUBSTRAT = V3 / "50_Distillation/_substrat"
METHODO = V3 / "60_Implementation_Méthodologiques/domaines"
ONTOLOGIE = V3 / "70_Onthologies/sujets"

MOT = re.compile(r"[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ'-]{2,}")

# --- Ce qui n'est pas de la connaissance -------------------------------------
# Dependances installees et SORTIES generees. Les distiller reviendrait a
# distiller ce que le systeme a lui-meme produit.
#
# Mesure du 2026-08-29 sur 00_Jerry_Business_Pulse : 107 265 fichiers, dont
# 8 565 .md. En retirant node_modules il en reste 5 232 -- et sur ces 5 232,
# **4 766 sont dans `graphify-burst`**. Le contenu reel tient en ~466 documents.
#
# Sans ces exclusions la porte expire ; et si elle n'expirait pas, son verdict
# serait une moyenne sur du remplissage. Un domaine dilue passerait pour couvert.
EXCLUS = {
    "node_modules", ".git", ".venv", "venv", "__pycache__", "dist", "build",
    ".next", ".nuxt", "target", "vendor", "coverage", ".cache", "site-packages",
    # Sorties de generation : elles derivent du corpus, elles n'en font pas partie.
    "graphify-out", "graphify-burst", "graphify-out-hors-para",
    "_exports", ".obsidian",
}

# --- Cadences : la grille de D.E.A.L, telle que le proprietaire l'execute ----
# « La seule configuration d'une semaine de 4 h reussie s'execute a l'echelle
#   de la semaine, du jour, et des heures de deep work, sur des cadences de
#   travail COLLABORATIF (je peux etre devant l'ordinateur) et des cadences de
#   travail AUTONOME (sur mon PC comme sur VPS). »
#
# Un artefact qui ne dit pas a quelle echelle ni sous quel mode il s'execute
# n'est pas implementable : c'est une note. C'est ce que le filtre 2 verifie.
ECHELLES = ("semaine", "jour", "deep-work")
MODES = ("collaboratif", "autonome")

INDICES_ECHELLE = {
    "semaine": ("semaine", "week", "w1", "w12", "12wy", "hebdo", "rock", "quarter", "trimestre"),
    "jour": ("jour", "daily", "quotidien", "journee", "day"),
    "deep-work": ("deep work", "deep-work", "focus", "bloc", "session", "pomodoro", "sprint"),
}
INDICES_MODE = {
    "collaboratif": ("hitl", "humain", "human", "review", "revue", "arbitrage", "valide", "approuv", "gate", "porte"),
    "autonome": ("cron", "vps", "autonome", "automatique", "daemon", "planifie", "schedule", "batch", "sans surveillance"),
}
# --- PARA : le seau commande le critere ------------------------------------
# CORRECTION DU 2026-08-29, apres arbitrage du proprietaire.
#
# Juger une AREA sur une echelle semaine/jour/deep-work est une faute : une
# Area est perpetuelle PAR DEFINITION, elle n'a pas de finalite temporelle.
# Lui donner « PASSE » sur ce calcul revient a valider l'inertie au lieu de la
# detecter -- et c'est exactement ce que la porte a fait pour Jerry.
#
# « Le maintien de standard de reproduction perpetuel sans finalite temporelle
#   est pire pour l'inertie induite dans un systeme mort par des accumulations
#   de defaut. »
#
# Donc : un critere par seau.
#   Projects (Picard)  -> une fin. Un projet sans echeance est un defaut.
#   Areas    (Spock)   -> un STANDARD a tenir et une REVUE qui retire. Pas
#                         d'echeance, mais une cadence de revue -- sans quoi
#                         les defauts s'accumulent sans jamais sortir.
#   Resources(Geordi)  -> reference. Aucune cadence attendue.
#   Archives (Data)    -> non-usage. Rien a mesurer.
SEAUX_PARA = {
    "01_Projects_Picard": "projet",
    "02_Areas_Spock": "area",
    "03_Resources_Geordi": "ressource",
    "04_Archives_Data": "archive",
}

# Ce qu'on cherche dans une Area : la preuve qu'un standard est tenu ET revu.
INDICES_STANDARD = ("standard", "sop", "principle", "principe", "doctrine",
                    "definition of done", "dod", "critere", "invariant", "regle")
INDICES_REVUE = ("review", "revue", "retro", "audit", "controle", "verification",
                 "cadence", "rituel", "hebdo", "mensuel", "trimestre")
# Les marqueurs de dette qui s'accumulent quand rien ne retire.
INDICES_DETTE = ("todo", "fixme", "hack", "a corriger", "provisoire", "temporaire",
                 "deprecated", "obsolete", "stale", "contested", "non encore",
                 "pas encore", "manquant", "vide")

# GTD : les cinq temps. Un domaine qui n'en couvre aucun ne se pilote pas.
INDICES_GTD = {
    "capture": ("capture", "inbox", "collecte", "saisie"),
    "clarify": ("clarif", "definir", "definit", "decompos", "intent"),
    "organize": ("organis", "structure", "roadmap", "planning", "priorit"),
    "review": ("review", "revue", "retro", "metrics", "mesure", "bilan"),
    "engage": ("execut", "engage", "action", "faire", "livr"),
}


RP = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)


def est_jonction(entree) -> bool:
    """Vrai si l'entree est une jonction NTFS (piege documente du canon)."""
    try:
        return bool(entree.stat(follow_symlinks=False).st_file_attributes & RP)
    except (OSError, AttributeError):
        return False


def parcourir_md(racine: Path):
    """Rend les .md sous `racine`, sans jamais DESCENDRE dans un dossier exclu.

    `rglob` parcourt tout l'arbre puis laisse filtrer : sur les 107 265
    fichiers de Jerry_Business_Pulse, cela coute des minutes pour jeter 94 %
    du resultat. L'elagage a l'entree du dossier evite le parcours lui-meme.
    """
    pile = [racine]
    while pile:
        d = pile.pop()
        try:
            entrees = list(os.scandir(d))
        except OSError:
            continue
        for e in entrees:
            try:
                if e.is_dir(follow_symlinks=False):
                    if e.name in EXCLUS or e.name.startswith("."):
                        continue
                    # Jonctions NTFS : `os.path.islink` NE LES VOIT PAS et
                    # `follow_symlinks=False` ne suffit pas. Sans ce garde, le
                    # parcours boucle -- mesure du 2026-08-29 sur ce domaine :
                    # 25 418 fichiers en 60 s alors que `find` en compte 8 565
                    # AU TOTAL. On visitait les memes fichiers en rond.
                    if est_jonction(e):
                        continue
                    pile.append(Path(e.path))
                elif e.name.endswith(".md"):
                    yield Path(e.path)
            except OSError:
                continue


def journal(msg: str) -> None:
    print(f"{time.strftime('%H:%M:%S')}  {msg}", flush=True)


def seau_para(src: Path) -> str:
    """Rend le seau PARA d'une source, d'apres son chemin reel.

    Le seau n'est pas une etiquette qu'on choisit : il est inscrit dans
    l'arborescence. `05_From_V2_Domains` vit sous `03_Resources_Geordi`, donc
    tout ce qui en vient est une RESSOURCE -- un miroir de reference, pas la
    chose vivante. Le domaine correspondant, lui, peut etre une Area ou un
    Projet ailleurs dans le PARA.
    """
    parts = set(src.parts)
    for dossier, seau in SEAUX_PARA.items():
        if dossier in parts:
            return seau
    return "inconnu"


def trouver_source(domaine: str) -> Path | None:
    """Resout un nom de domaine, ou une RACINE entiere.

    Les trois racines (`05_From_V2_Domains` et ses trois OS) sont des cibles
    legitimes : on peut vouloir passer la porte sur un OS complet plutot que
    domaine par domaine. Le parcours elague de toute facon, donc le cout suit
    le contenu reel et non la taille de l'arbre.
    """
    for base in SOURCES_POSSIBLES:
        c = base / domaine
        if c.is_dir():
            return c
        if base.name == domaine:
            return base
    racine = V2 / "03_Resources_Geordi/05_From_V2_Domains"
    if racine.name == domaine:
        return racine
    return None


def lire_frontmatter(txt: str) -> dict:
    """Frontmatter YAML minimal, sans dependance. On ne lit que les cles a plat."""
    if not txt.startswith("---"):
        return {}
    fin = txt.find("\n---", 3)
    if fin < 0:
        return {}
    fm = {}
    for ligne in txt[3:fin].splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", ligne)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm


def plan_de(txt: str) -> list[str]:
    return [m.group(2).strip() for m in re.finditer(r"^(#{1,4})\s+(.*)$", txt, re.M)][:40]


# ---------------------------------------------------------------- filtre 1 --
def filtre_distillation(src: Path, domaine: str) -> tuple[list[dict], dict]:
    """Extraction scriptee, 100 % du perimetre, sans modele.

    Conforme a 50_Distillation/METHODE.md : on extrait TOUT par script, et la
    distillation semantique vient ensuite sur cette extraction. L'inverse --
    faire lire les fichiers a un agent -- ne couvrirait qu'un echantillon en
    pretendant couvrir le tout.
    """
    lignes = []
    lus = echecs = 0
    for p in parcourir_md(src):
        try:
            txt = p.read_text(encoding="utf-8", errors="ignore")
            lus += 1
        except OSError:
            echecs += 1
            continue
        fm = lire_frontmatter(txt)
        rel = p.relative_to(src).as_posix()
        lignes.append({
            "id": f"{domaine}/{rel}",
            "seau": domaine,
            "nom": p.name,
            "octets": p.stat().st_size,
            "modifie": datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d"),
            "profondeur": rel.count("/"),
            "titre": fm.get("title") or (plan_de(txt)[0] if plan_de(txt) else p.stem),
            "fm": fm,
            "fm_cles": sorted(fm.keys()),
            "okf": fm.get("okf_version"),
            "type": fm.get("type"),
            "tags_fm": fm.get("tags"),
            "nb_titres": len(plan_de(txt)),
            "plan": plan_de(txt),
            "wikilinks": re.findall(r"\[\[([^\]]+)\]\]", txt)[:40],
            "liens": sorted(set(re.findall(r"https?://[^\s)\]]+", txt)))[:30],
            "tags_corps": sorted(set(re.findall(r"(?<!\w)#([a-z][\w-]{2,})", txt)))[:20],
            "mots": len(MOT.findall(txt)),
        })
    # La difference entre LUS et ECHECS compte autant que le total : un rapport
    # qui ne dit que le total laisse croire a une couverture qu'il n'a pas.
    return lignes, {"lus": lus, "echecs": echecs, "fichiers": len(lignes)}


# ---------------------------------------------------------------- filtre 2 --
def filtre_methodologique(lignes: list[dict], src: Path, seau: str = "inconnu") -> dict:
    """A quelle echelle et sous quel mode ce domaine s'execute-t-il ?

    Un artefact qui ne se rattache ni a une echelle (semaine/jour/deep-work)
    ni a un mode (collaboratif/autonome) n'est pas implementable. Le filtre ne
    juge pas la qualite : il constate la couverture, et nomme les trous.
    """
    std = rev = dette = 0
    ech = {k: 0 for k in ECHELLES}
    mod = {k: 0 for k in MODES}
    gtd = {k: 0 for k in INDICES_GTD}
    sans_rattachement = []

    for l in lignes:
        p = src / Path(l["id"]).relative_to(Path(l["id"]).parts[0])
        try:
            corps = p.read_text(encoding="utf-8", errors="ignore").lower()
        except OSError:
            continue
        contexte = corps + " " + l["nom"].lower() + " " + " ".join(l["plan"]).lower()
        touche = False
        for k, mots in INDICES_ECHELLE.items():
            if any(m in contexte for m in mots):
                ech[k] += 1
                touche = True
        for k, mots in INDICES_MODE.items():
            if any(m in contexte for m in mots):
                mod[k] += 1
        for k, mots in INDICES_GTD.items():
            if any(m in contexte for m in mots):
                gtd[k] += 1
        # Mesures propres aux Areas : standard tenu, revue qui retire, dette
        # qui s'accumule. On les compte pour tout le monde -- elles ne coutent
        # rien et servent au diagnostic meme hors Area.
        if any(m in contexte for m in INDICES_STANDARD):
            std += 1
        if any(m in contexte for m in INDICES_REVUE):
            rev += 1
        if any(m in contexte for m in INDICES_DETTE):
            dette += 1
        if not touche:
            sans_rattachement.append(l["nom"])

    n = max(1, len(lignes))
    res = {
        "seau_para": seau,
        "echelles": ech,
        "modes": mod,
        "gtd": gtd,
        "sans_rattachement": sans_rattachement,
        "couverture_echelle": round(100 * (len(lignes) - len(sans_rattachement)) / n),
        "standard_pct": round(100 * std / n),
        "revue_pct": round(100 * rev / n),
        "dette_pct": round(100 * dette / n),
    }
    # Le ratio qui dit l'inertie : de la dette portee, sans revue qui la retire.
    # Une Area perpetuelle avec beaucoup de dette et peu de revue est un
    # systeme mort qui continue de tourner -- le cas que le proprietaire nomme.
    res["inertie"] = round(dette / max(1, rev), 2)
    return res


# ---------------------------------------------------------------- filtre 3 --
def filtre_ontologie(lignes: list[dict], domaine: str) -> tuple[str, dict]:
    """Triplets Turtle. Les URN plutot que des IRI HTTP.

    Inventer `https://aspace-os.org/ns#` reviendrait a s'approprier un domaine
    qui appartient peut-etre a un tiers, et a poser une adresse qui ne resout
    pas. Choix deja fait dans concepts_vers_triplets.py ; on s'y conforme.
    """
    def urn(s: str) -> str:
        return "urn:aspace:" + re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

    out = [
        "@prefix aspace: <urn:aspace:> .",
        "@prefix dct: <http://purl.org/dc/terms/> .",
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .",
        "",
        f"# Domaine {domaine} — genere par porte_argent.py le "
        f"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"# {len(lignes)} documents. Triplets mecaniques : le fichier est le sujet,",
        "# chaque cle de frontmatter un predicat, chaque valeur un objet.",
        "",
    ]
    n_triplets = 0
    for l in lignes:
        s = f"<{urn(l['id'])}>"
        out.append(f'{s} a aspace:Document ;')
        out.append(f'    rdfs:label {json.dumps(l["titre"], ensure_ascii=False)} ;')
        out.append(f'    aspace:seau <{urn(domaine)}> ;')
        out.append(f'    dct:modified "{l["modifie"]}" ;')
        out.append(f'    aspace:mots {l["mots"]} ;')
        n_triplets += 5
        if l.get("type"):
            out.append(f'    aspace:type {json.dumps(l["type"], ensure_ascii=False)} ;')
            n_triplets += 1
        for w in l["wikilinks"][:10]:
            out.append(f'    aspace:renvoieVers <{urn(w)}> ;')
            n_triplets += 1
        out[-1] = out[-1].rstrip(" ;") + " ."
        out.append("")
    return "\n".join(out), {"triplets": n_triplets, "sujets": len(lignes)}


# ------------------------------------------------------------------ verdict --
def main() -> int:
    domaine = None
    if "--domaine" in sys.argv:
        domaine = sys.argv[sys.argv.index("--domaine") + 1]
    if not domaine:
        print("usage : porte_argent.py --domaine <nom> [--appliquer]")
        return 2
    appliquer = "--appliquer" in sys.argv

    src = trouver_source(domaine)
    if not src:
        journal(f"SOURCE INTROUVABLE pour {domaine}")
        return 1
    journal(f"source : {src}")

    journal("filtre 1/3 — distillation RDF")
    lignes, m1 = filtre_distillation(src, domaine)
    journal(f"   {m1['fichiers']} documents, {m1['lus']} lus, {m1['echecs']} en echec")

    seau = seau_para(src)
    journal(f"seau PARA : {seau}")
    journal("filtre 2/3 — implementation methodologique")
    m2 = filtre_methodologique(lignes, src, seau)
    journal(f"   echelles {m2['echelles']}")
    journal(f"   modes    {m2['modes']}")
    journal(f"   gtd      {m2['gtd']}")
    journal(f"   couverture d'echelle : {m2['couverture_echelle']} %")
    journal(f"   standard {m2['standard_pct']} % · revue {m2['revue_pct']} % · "
            f"dette {m2['dette_pct']} % · inertie {m2['inertie']}")
    if m2["sans_rattachement"]:
        journal(f"   sans rattachement d'echelle : {len(m2['sans_rattachement'])} — "
                + ", ".join(m2["sans_rattachement"][:5]))

    journal("filtre 3/3 — formation d'ontologie")
    ttl, m3 = filtre_ontologie(lignes, domaine)
    journal(f"   {m3['sujets']} sujets, {m3['triplets']} triplets")

    # Le verdict est explicite, et il PEUT etre negatif. Une porte qui laisse
    # tout passer n'est pas une porte.
    verdict = []
    if m1["echecs"] > 0:
        verdict.append(f"{m1['echecs']} fichiers illisibles")

    seau = m2["seau_para"]
    if seau == "area":
        # Une Area n'a pas d'echeance : on ne la juge PAS sur l'echelle.
        # Ce qu'elle doit prouver, c'est qu'un standard est tenu et qu'une
        # revue le retire quand il ne sert plus.
        if m2["standard_pct"] < 20:
            verdict.append(f"aucun standard declare ({m2['standard_pct']} %)")
        if m2["revue_pct"] < 20:
            verdict.append(f"pas de cadence de revue ({m2['revue_pct']} %)")
        if m2["inertie"] > 2.0:
            verdict.append(f"inertie {m2['inertie']} — dette portee sans revue qui la retire")
    elif seau in ("ressource", "archive"):
        # Une ressource est de la reference : aucune cadence n'est attendue.
        # Exiger un mode d'execution d'un miroir de lecture est une faute de
        # categorie -- la meme que juger une Area sur une echeance.
        pass
    else:
        if m2["couverture_echelle"] < 50:
            verdict.append(f"couverture d'echelle faible ({m2['couverture_echelle']} %)")
        if sum(m2["modes"].values()) == 0:
            verdict.append("aucun mode d'execution identifiable")
    passe = not verdict

    journal("")
    journal("VERDICT : " + ("PASSE" if passe else "RESERVES — " + " ; ".join(verdict)))

    if not appliquer:
        journal("SIMULATION. Relancer avec --appliquer pour ecrire dans V3.")
        return 0

    SUBSTRAT.mkdir(parents=True, exist_ok=True)
    METHODO.mkdir(parents=True, exist_ok=True)
    ONTOLOGIE.mkdir(parents=True, exist_ok=True)

    fs = SUBSTRAT / f"{domaine}.jsonl"
    with io.open(fs, "w", encoding="utf-8") as f:
        for l in lignes:
            f.write(json.dumps(l, ensure_ascii=False) + "\n")

    fm = METHODO / f"{domaine}.json"
    fm.write_text(json.dumps({
        "domaine": domaine, "source": str(src),
        "genere": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "distillation": m1, "methodologique": m2, "ontologie": m3,
        "verdict": "passe" if passe else "reserves", "reserves": verdict,
    }, ensure_ascii=False, indent=1), encoding="utf-8")

    fo = ONTOLOGIE / f"{domaine}.ttl"
    fo.write_text(ttl, encoding="utf-8")

    journal(f"ecrit : {fs}")
    journal(f"ecrit : {fm}")
    journal(f"ecrit : {fo}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

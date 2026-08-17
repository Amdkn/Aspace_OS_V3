"""Extraction exhaustive du substrat RDF depuis les .md du PARA de la V2.

POURQUOI CE SCRIPT EXISTE
Le corpus fait 63 260 fichiers .md. Aucun agent ne peut les lire. Mais la
matiere premiere d'un graphe RDF — sujet, predicat, objet — se lit sans
comprehension semantique : le frontmatter donne les proprietes, les titres
donnent la hierarchie, les liens donnent les relations.

On extrait donc 100 % du corpus par script, et les agents distillent ENSUITE
sur cette extraction. L'inverse — faire lire les fichiers aux agents — ne
couvrirait qu'un echantillon en pretendant couvrir le tout.

CE QU'IL N'EST PAS
Ce n'est pas une comprehension du contenu. Il ne sait pas si un document dit
vrai, ni s'il est perime. Il dit ce qui est ecrit et ou. La distillation
semantique est le travail des agents, sur la base de ce qu'il produit.

SORTIE
Un JSONL par seau : une ligne par fichier .md, avec de quoi former des
triplets. Plus un rapport de couverture qui dit combien de fichiers ont ete
LUS et combien ont ECHOUE — la difference compte autant que le total.
"""

import io
import json
import os
import re
import stat
import sys
from datetime import datetime, timezone

RP = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)

RACINE = r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise"
SORTIE = r"C:\Users\amado\ASpace_OS_V3\50_Distillation\_substrat"

SEAUX = [
    "01_Projects_Picard",
    "02_Areas_Spock",
    "03_Resources_Geordi",
    "04_Archives_Data",
]

# Dossiers de dependances et d'artefacts de build : ils portent des .md
# (READMEs de paquets npm) qui ne disent rien d'A'Space.
BRUIT = {
    "node_modules", ".git", "dist", "build", ".next", ".vercel",
    "venv", ".venv", "__pycache__", ".turbo", "coverage", ".cache",
}

RE_H = re.compile(r"^(#{1,6})\s+(.+?)\s*#*$", re.M)
RE_WIKI = re.compile(r"\[\[([^\]\|#]+)")
RE_MD = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
RE_TAG = re.compile(r"(?:^|\s)#([A-Za-z][A-Za-z0-9_/-]{2,40})")


def jonction(e: os.DirEntry) -> bool:
    try:
        return bool(e.stat(follow_symlinks=False).st_file_attributes & RP)
    except OSError:
        return False


def lire_frontmatter(texte: str) -> tuple[dict, str]:
    """Frontmatter YAML sans dependance : on ne parse que les cles de premier
    niveau. Un YAML imbrique est conserve brut plutot que mal interprete."""
    if not texte.startswith("---"):
        return {}, texte
    fin = texte.find("\n---", 3)
    if fin == -1:
        return {}, texte
    bloc = texte[3:fin]
    meta: dict = {}
    for ligne in bloc.splitlines():
        if not ligne or ligne.startswith((" ", "\t", "#", "-")):
            continue
        if ":" not in ligne:
            continue
        cle, _, val = ligne.partition(":")
        cle = cle.strip()
        val = val.strip().strip("\"'")
        if cle:
            meta[cle] = val[:300]
    return meta, texte[fin + 4:]


def extraire(chemin: str, seau: str) -> dict | None:
    try:
        st = os.stat(chemin)
        with io.open(chemin, encoding="utf-8", errors="replace") as f:
            texte = f.read(400_000)  # au-dela, un .md n'est plus un document
    except OSError:
        return None

    meta, corps = lire_frontmatter(texte)
    titres = RE_H.findall(corps)
    h1 = next((t for n, t in titres if len(n) == 1), None)

    rel = os.path.relpath(chemin, RACINE)
    return {
        "id": rel.replace("\\", "/"),
        "seau": seau,
        "nom": os.path.basename(chemin),
        "octets": st.st_size,
        "modifie": datetime.fromtimestamp(st.st_mtime, timezone.utc).date().isoformat(),
        "profondeur": rel.count(os.sep),
        "titre": (h1 or meta.get("title") or "")[:200],
        "fm": meta,
        "fm_cles": sorted(meta.keys()),
        "okf": meta.get("okf_version"),
        "type": meta.get("type"),
        "tags_fm": meta.get("tags"),
        "nb_titres": len(titres),
        "plan": [t for _, t in titres[:40]],
        "wikilinks": sorted({w.strip() for w in RE_WIKI.findall(corps)})[:120],
        "liens": sorted({l for l in RE_MD.findall(corps) if not l.startswith("#")})[:120],
        "tags_corps": sorted(set(RE_TAG.findall(corps)))[:40],
        "mots": len(corps.split()),
    }


def main() -> None:
    os.makedirs(SORTIE, exist_ok=True)
    rapport = {"genere": datetime.now(timezone.utc).isoformat(), "seaux": {}}

    for seau in SEAUX:
        racine = os.path.join(RACINE, seau)
        if not os.path.isdir(racine):
            continue

        lus = 0
        echecs = 0
        jonctions = 0
        chemin_sortie = os.path.join(SORTIE, f"{seau}.jsonl")

        with io.open(chemin_sortie, "w", encoding="utf-8") as sortie:
            pile = [racine]
            while pile:
                p = pile.pop()
                try:
                    with os.scandir(p) as it:
                        for e in it:
                            try:
                                if e.is_dir(follow_symlinks=False):
                                    if jonction(e):
                                        jonctions += 1
                                        continue
                                    if e.name in BRUIT:
                                        continue
                                    pile.append(e.path)
                                elif e.is_file(follow_symlinks=False) and e.name.lower().endswith(".md"):
                                    d = extraire(e.path, seau)
                                    if d is None:
                                        echecs += 1
                                    else:
                                        sortie.write(json.dumps(d, ensure_ascii=False) + "\n")
                                        lus += 1
                            except OSError:
                                echecs += 1
                except OSError:
                    echecs += 1

        rapport["seaux"][seau] = {
            "lus": lus, "echecs": echecs, "jonctions_ecartees": jonctions,
            "fichier": os.path.basename(chemin_sortie),
        }
        print(f"[{seau}] {lus} lus, {echecs} echecs, {jonctions} jonctions",
              file=sys.stderr, flush=True)

    total = sum(s["lus"] for s in rapport["seaux"].values())
    rapport["total_lus"] = total
    rapport["total_echecs"] = sum(s["echecs"] for s in rapport["seaux"].values())

    with io.open(os.path.join(SORTIE, "_couverture.json"), "w", encoding="utf-8") as f:
        json.dump(rapport, f, ensure_ascii=False, indent=1)
    print(f"TOTAL {total} fichiers extraits", file=sys.stderr)


if __name__ == "__main__":
    main()

"""Consolide les concepts en sources chargeables dans NotebookLM.

POURQUOI CE SCRIPT EXISTE
La revue humaine est devenue le goulot : 423 fichiers .md produits en une
nuit, tous en `confiance: machine`, aucun relu. L'outil de revue choisi est
NotebookLM (renomme Gemini Notebook), qui plafonne a 50 sources par carnet en
gratuit et 300 en Plus.

Charger 423 fichiers est donc impossible. Ce script les regroupe par bundle —
une source par domaine, par etage, par famille — soit une vingtaine de
sources au lieu de 423.

CE QU'IL PRESERVE, ET POURQUOI
Chaque concept garde son titre, sa description, ses sources et son chemin
d'origine. Sans le chemin, un verdict de revue ne pourrait pas etre reporte
sur le bon fichier : le podcast dirait « le concept sur les vetos est faux »
sans qu'on sache lequel corriger.

CE QU'IL RETIRE
Le frontmatter YAML brut, illisible a l'oral et sans valeur pour un
relecteur. Il est remplace par deux lignes en prose : le type et le niveau de
confiance. Ce dernier est ce que la revue doit faire passer de `machine` a
`humain`.
"""

import io
import os
import re

V3 = r"C:\Users\amado\ASpace_OS_V3"
SORTIE = os.path.join(V3, "_REVIEW_NOTEBOOKLM")

# (fichier de sortie, titre, dossier source, prefixe de chemin affiche)
LOTS = []
for d in ("aquaman", "wonder-woman", "batman", "superman",
          "cyborg", "green-lantern", "flash", "john-jones"):
    LOTS.append((f"10-domaine-{d}.md", f"Domaine {d}",
                 os.path.join("70_Onthologies", "pulse", "domaines", d)))
for e in ("b1", "b2", "b3"):
    LOTS.append((f"20-etage-{e}.md", f"Etage {e.upper()}",
                 os.path.join("70_Onthologies", "pulse", e)))
for m in ("protocoles", "frameworks", "domaines", "prompt-systeme", "autonomie-agents"):
    LOTS.append((f"30-methode-{m}.md", f"Methodes — {m}",
                 os.path.join("60_Implementation_Méthodologiques", m)))
for s in ("areas", "projets", "archives", "ressources", "ontologie"):
    LOTS.append((f"40-distillation-{s}.md", f"Distillation V2 — {s}",
                 os.path.join("50_Distillation", s)))


def frontmatter(texte):
    if not texte.startswith("---"):
        return {}, texte
    fin = texte.find("\n---", 3)
    if fin == -1:
        return {}, texte
    meta, cle = {}, None
    for ligne in texte[3:fin].splitlines():
        if not ligne.strip():
            continue
        if not ligne.startswith((" ", "\t", "-")) and ":" in ligne:
            k, _, v = ligne.partition(":")
            k, v = k.strip(), v.strip().strip("\"'")
            meta[k] = v if v else []
            cle = None if v else k
        elif cle and ligne.strip().startswith("-"):
            if isinstance(meta.get(cle), list):
                meta[cle].append(ligne.strip()[1:].strip())
    return meta, texte[fin + 4:]


def niveau(meta):
    v = meta.get("verified")
    if not v:
        return "NON VERIFIE"
    txt = " ".join(v) if isinstance(v, list) else str(v)
    return "REVU PAR UN HUMAIN" if "human:" in txt else "confirme par machine"


def consolider(nom_sortie, titre, dossier):
    d = os.path.join(V3, dossier)
    if not os.path.isdir(d):
        return None
    fichiers = [n for n in sorted(os.listdir(d))
                if n.endswith(".md") and n not in ("index.md", "CATALOGUE.md")]
    if not fichiers:
        return None

    out = [f"# {titre}",
           "",
           f"**{len(fichiers)} concepts.** Source d'origine : `{dossier.replace(os.sep, '/')}/`",
           "",
           "Chaque section ci-dessous est un concept distinct. Le **chemin** permet",
           "de reporter un verdict de revue sur le bon fichier ; le **niveau de",
           "confiance** est ce que la revue doit faire evoluer.",
           "", "---", ""]

    for n in fichiers:
        with io.open(os.path.join(d, n), encoding="utf-8", errors="replace") as f:
            meta, corps = frontmatter(f.read())
        out.append(f"## {meta.get('title', n[:-3])}")
        out.append("")
        out.append(f"- **fichier** : `{dossier.replace(os.sep, '/')}/{n}`")
        out.append(f"- **type** : {meta.get('type', 'non declare')}")
        out.append(f"- **confiance** : {niveau(meta)}")
        if meta.get("description"):
            out.append(f"- **resume** : {meta['description']}")
        srcs = meta.get("sources") or []
        if isinstance(srcs, list) and srcs:
            refs = []
            for s in srcs:
                m = re.search(r"resource\s*:\s*(.+?)(?:\s+title\s*:|\s+author\s*:|$)", s)
                if m:
                    refs.append(m.group(1).strip().strip("\"'")[:120])
            if refs:
                out.append(f"- **sources citees** : {' · '.join(refs[:4])}")
        out.append("")
        out.append(corps.strip())
        out.append("")
        out.append("---")
        out.append("")
    return "\n".join(out), len(fichiers)


def main():
    os.makedirs(SORTIE, exist_ok=True)
    total_concepts = 0
    produits = []

    for nom, titre, dossier in LOTS:
        r = consolider(nom, titre, dossier)
        if not r:
            continue
        texte, n = r
        io.open(os.path.join(SORTIE, nom), "w", encoding="utf-8").write(texte)
        produits.append((nom, titre, n, len(texte)))
        total_concepts += n

    # Les rapports d'agents : le meta, la source la plus rentable pour un
    # podcast critique — couverture declaree, contradictions non tranchees.
    lp = os.path.join(V3, "60_Implementation_Méthodologiques", "_loop")
    rapports = sorted(n for n in os.listdir(lp) if n.startswith("RAPPORT_"))
    if rapports:
        out = ["# Rapports d'agents — ce qu'ils disent d'eux-memes",
               "",
               f"**{len(rapports)} rapports.** C'est la source la plus utile pour une",
               "revue critique : chaque agent y declare sa couverture reelle, ce qu'il",
               "n'a pas couvert, et les contradictions qu'il a refuse de trancher.",
               "", "---", ""]
        for n in rapports:
            with io.open(os.path.join(lp, n), encoding="utf-8", errors="replace") as f:
                out += [f"## {n}", "", f.read().strip(), "", "---", ""]
        io.open(os.path.join(SORTIE, "50-rapports-agents.md"), "w", encoding="utf-8").write("\n".join(out))
        produits.append(("50-rapports-agents.md", "Rapports d'agents", len(rapports), 0))

    # Memoires partagees, copiees telles quelles : leur forme append-only est
    # elle-meme l'objet de la revue.
    for src, dst in (
        (os.path.join(V3, "70_Onthologies", "pulse", "domaines", "ETAT_DOMAINES.md"),
         "60-memoire-etat-domaines.md"),
        (os.path.join(V3, "70_Onthologies", "pulse", "ETAT.md"),
         "61-memoire-etat-vague1.md"),
        (os.path.join(V3, "70_Onthologies", "_structure", "CARTE_V3.md"),
         "62-carte-structure-v3.md"),
    ):
        if os.path.exists(src):
            io.open(os.path.join(SORTIE, dst), "w", encoding="utf-8").write(
                io.open(src, encoding="utf-8", errors="replace").read())
            produits.append((dst, "memoire partagee", 0, 0))

    index = [
        "# Dossier de revue — A'Space OS, nuit du 2026-08-18",
        "",
        f"**{total_concepts} concepts** regroupes en **{len(produits)} sources**,",
        "chargeables dans NotebookLM / Gemini Notebook.",
        "",
        "## Pourquoi cette revue existe",
        "",
        "Ces concepts ont ete produits par des agents en une nuit, en deux vagues.",
        "**Aucun n'a ete relu par un humain** : tous portent `confiance: machine`.",
        "La production n'est plus le goulot — la verification l'est.",
        "",
        "## Par ou commencer",
        "",
        "1. **`50-rapports-agents.md`** — ce que les agents disent d'eux-memes :",
        "   couverture reelle, ce qu'ils n'ont pas couvert, contradictions non",
        "   tranchees. C'est la source la plus rentable pour un podcast critique.",
        "2. **`60-memoire-etat-domaines.md`** — les 42 tours des huit escouades,",
        "   resumes ligne par ligne.",
        "3. Les domaines et etages, selon ce que vous voulez arbitrer.",
        "",
        "## Les questions qui meritent d'etre posees au chat",
        "",
        "- Quelles affirmations reposent sur une seule source ?",
        "- Ou deux concepts se contredisent-ils sans que personne ne l'ait signale ?",
        "- Quelles decisions sont presentees comme acquises alors qu'elles n'ont",
        "  jamais ete tranchees par un humain ?",
        "- Qu'est-ce qui manque, que le corpus aurait du contenir ?",
        "",
        "## Les sources",
        "",
        "| fichier | contenu | concepts |",
        "|---|---|---|",
    ]
    for nom, titre, n, _ in produits:
        index.append(f"| `{nom}` | {titre} | {n if n else '—'} |")
    io.open(os.path.join(SORTIE, "00-INDEX.md"), "w", encoding="utf-8").write("\n".join(index))

    print(f"{len(produits) + 1} sources -> {SORTIE}")
    for nom, titre, n, taille in produits:
        print(f"   {nom:<32} {n:>3} concepts  {taille // 1024 if taille else '?':>4} Ko")


if __name__ == "__main__":
    main()

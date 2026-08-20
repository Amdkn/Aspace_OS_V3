"""Genere la page HTML d'une vague — une page, ouverte en un clic.

POURQUOI CE GENERATEUR EXISTE
NotebookLM rend un podcast de vingt minutes. C'est excellent pour decouvrir
un corpus en marchant, et inutilisable pour repondre a « ou en est cette
vague ? ». Il faut une page qui reponde en trois secondes.

D'ou la contrainte de forme, qui n'est pas cosmetique : la page est
AUTONOME. Pas de CSS externe, pas de JS distant, pas de police a telecharger.
Elle s'ouvre depuis `file://` sans serveur et sans reseau. Une page de revue
qui exige une chaine de build est une page qu'on ne regarde pas.

CE QU'ELLE MONTRE EN PREMIER
Ce qui ne va pas. Une page de revue qui ouvre sur « 258 concepts produits »
felicite ; une page qui ouvre sur « 258 concepts, 0 relu » informe. Le
deuxieme chiffre est le seul qui appelle une action.

CE QU'ELLE NE FAIT PAS
Elle ne juge pas. Le niveau de confiance est lu dans le frontmatter, jamais
calcule ni suppose. Un concept sans `verified` s'affiche « non verifie »,
pas « probablement bon ».
"""

import argparse
import io
import json
import os
import re
import sys

V3 = r"C:\Users\amado\ASpace_OS_V3"

CSS = """
:root{--bg:#0d1117;--fg:#e6edf3;--mut:#8b949e;--brd:#30363d;--card:#161b22;
--rouge:#f85149;--ambre:#d29922;--vert:#3fb950;--bleu:#58a6ff}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
font:15px/1.6 ui-sans-serif,-apple-system,Segoe UI,Roboto,sans-serif}
.wrap{max-width:1100px;margin:0 auto;padding:32px 24px 80px}
h1{font-size:26px;margin:0 0 4px} h2{font-size:17px;margin:36px 0 12px;
padding-bottom:6px;border-bottom:1px solid var(--brd)}
.sub{color:var(--mut);margin:0 0 28px;font-size:14px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px}
.kpi{background:var(--card);border:1px solid var(--brd);border-radius:8px;padding:14px 16px}
.kpi .n{font-size:28px;font-weight:600;line-height:1.1}
.kpi .l{color:var(--mut);font-size:12px;margin-top:4px}
.kpi.alerte{border-color:var(--rouge)} .kpi.alerte .n{color:var(--rouge)}
.kpi.ok .n{color:var(--vert)}
table{width:100%;border-collapse:collapse;font-size:13.5px;margin-top:8px}
th{text-align:left;color:var(--mut);font-weight:500;font-size:12px;
padding:6px 8px;border-bottom:1px solid var(--brd)}
td{padding:7px 8px;border-bottom:1px solid #21262d;vertical-align:top}
tr:hover td{background:#161b22}
.p{display:inline-block;padding:1px 7px;border-radius:99px;font-size:11px;
border:1px solid}
.p.humain{color:var(--vert);border-color:var(--vert)}
.p.machine{color:var(--ambre);border-color:var(--ambre)}
.p.non{color:var(--rouge);border-color:var(--rouge)}
.d{color:var(--mut);font-size:12.5px}
code{background:#21262d;padding:1px 5px;border-radius:4px;font-size:12px}
a{color:var(--bleu);text-decoration:none} a:hover{text-decoration:underline}
.vide{color:var(--mut);font-style:italic;padding:10px 0}
footer{margin-top:48px;color:var(--mut);font-size:12px;
border-top:1px solid var(--brd);padding-top:14px}
"""


def frontmatter(texte):
    """Rend (meta, corps). Volontairement tolerant : un frontmatter mal
    forme rend un dict vide plutot qu'une exception — une page de revue
    qui refuse de s'afficher parce qu'un fichier sur 258 est casse ne sert
    a rien. Le fichier casse apparaitra en 'non verifie', ce qui est le
    signalement correct."""
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
        elif cle is not None and isinstance(meta.get(cle), list):
            meta[cle].append(ligne.strip().lstrip("- ").strip())
    return meta, texte[fin + 4:]


def niveau(meta):
    """Le niveau OKF v0.2 se DEDUIT de `verified` — jamais d'un champ
    `confiance` ecrit a la main, qui pourrait mentir."""
    v = meta.get("verified")
    if not v:
        return "non"
    txt = " ".join(v) if isinstance(v, list) else str(v)
    return "humain" if "human:" in txt else "machine"


LIB = {"humain": "revu par un humain", "machine": "confirme par machine",
       "non": "non verifie"}


def e(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def lire_constats(dossier):
    """Les dettes / avancees / apprentissages.

    Source de verite : `constats.json` depose dans le dossier de vague par
    l'agent qui l'a close. S'il est absent, on ne fabrique rien — on le dit.
    Deduire des constats de l'absence de constats serait exactement le genre
    d'invention rassurante que ce corpus doit eviter.
    """
    p = os.path.join(dossier, "constats.json")
    if not os.path.exists(p):
        return None
    try:
        return json.loads(io.open(p, encoding="utf-8").read())
    except Exception as exc:
        print(f"  constats.json illisible : {exc}", file=sys.stderr)
        return None


def generer(dossier, titre, sortie, racine_rel):
    concepts = []
    for n in sorted(os.listdir(dossier)):
        if not n.endswith(".md") or n == "index.md":
            continue
        meta, _ = frontmatter(io.open(os.path.join(dossier, n),
                                      encoding="utf-8", errors="replace").read())
        concepts.append({
            "f": n,
            "titre": meta.get("title", n[:-3]),
            "type": meta.get("type", "—"),
            "desc": meta.get("description", ""),
            "niv": niveau(meta),
        })

    n_tot = len(concepts)
    n_hum = sum(1 for c in concepts if c["niv"] == "humain")
    n_mac = sum(1 for c in concepts if c["niv"] == "machine")
    n_non = sum(1 for c in concepts if c["niv"] == "non")
    dette = n_tot - n_hum

    h = [f"<!doctype html><html lang=fr><meta charset=utf-8>",
         f"<meta name=viewport content='width=device-width,initial-scale=1'>",
         f"<title>{e(titre)} — revue</title><style>{CSS}</style>",
         "<div class=wrap>",
         f"<h1>{e(titre)}</h1>",
         f"<p class=sub><code>{e(racine_rel)}</code></p>"]

    # --- Les chiffres, le mauvais en premier ---------------------------
    h.append("<div class=grid>")
    cls = "alerte" if dette else "ok"
    h.append(f"<div class='kpi {cls}'><div class=n>{dette}</div>"
             f"<div class=l>concepts en attente d'un humain</div></div>")
    h.append(f"<div class=kpi><div class=n>{n_tot}</div>"
             f"<div class=l>concepts dans la vague</div></div>")
    h.append(f"<div class=kpi><div class=n>{n_hum}</div>"
             f"<div class=l>revus par un humain</div></div>")
    h.append(f"<div class=kpi><div class=n>{n_mac}</div>"
             f"<div class=l>confirmes par machine</div></div>")
    if n_non:
        h.append(f"<div class='kpi alerte'><div class=n>{n_non}</div>"
                 f"<div class=l>sans aucune verification</div></div>")
    h.append("</div>")

    # --- Dettes / avancees / apprentissages -----------------------------
    cs = lire_constats(dossier)
    h.append("<h2>Dettes, avancées, apprentissages</h2>")
    if cs is None:
        h.append("<p class=vide>Aucun <code>constats.json</code> dans ce "
                 "dossier. La vague n'a pas déclaré ses constats — c'est une "
                 "information, pas un vide à combler.</p>")
    else:
        for nat, lib in (("dette", "Dettes"), ("avancee", "Avancées"),
                         ("apprentissage", "Apprentissages")):
            items = [x for x in cs if x.get("nature") == nat]
            h.append(f"<h3 style='font-size:14px;margin:18px 0 6px'>{lib} "
                     f"<span class=d>({len(items)})</span></h3>")
            if not items:
                h.append("<p class=vide>rien de déclaré</p>")
                continue
            h.append("<table><tr><th>titre</th><th>preuve</th></tr>")
            for x in items:
                pr = x.get("preuve")
                pr = f"<code>{e(pr)}</code>" if pr else \
                     "<span class='p non'>sans preuve</span>"
                h.append(f"<tr><td>{e(x.get('titre',''))}"
                         f"<div class=d>{e(x.get('detail',''))}</div></td>"
                         f"<td>{pr}</td></tr>")
            h.append("</table>")

    # --- Le corpus ------------------------------------------------------
    h.append(f"<h2>Les {n_tot} concepts</h2>")
    h.append("<table><tr><th>concept</th><th>type</th><th>confiance</th></tr>")
    for c in sorted(concepts, key=lambda x: ("humain", "machine", "non").index(x["niv"]) * -1):
        h.append(f"<tr><td><a href='{e(os.path.join('..', racine_rel, c['f']).replace(os.sep,'/'))}'>"
                 f"{e(c['titre'])}</a><div class=d>{e(c['desc'][:190])}</div></td>"
                 f"<td class=d>{e(c['type'])}</td>"
                 f"<td><span class='p {c['niv']}'>{LIB[c['niv']]}</span></td></tr>")
    h.append("</table>")

    h.append("<footer>Page autonome — aucun CSS, JS ou police distants. "
             "Générée par <code>80_Front-Office/generer.py</code>. "
             "Le niveau de confiance est lu dans <code>verified</code>, "
             "jamais calculé.</footer></div></html>")

    io.open(sortie, "w", encoding="utf-8").write("\n".join(h))
    return n_tot, dette


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("dossier", help="dossier de vague, relatif a ASpace_OS_V3")
    p.add_argument("--titre", required=True)
    p.add_argument("--sortie", help="par defaut 80_Front-Office/reviews/<nom>.html")
    a = p.parse_args()

    d = a.dossier if os.path.isabs(a.dossier) else os.path.join(V3, a.dossier)
    if not os.path.isdir(d):
        print(f"dossier absent : {a.dossier}", file=sys.stderr)
        raise SystemExit(2)

    nom = re.sub(r"[^a-z0-9]+", "-", a.dossier.lower()).strip("-")
    sortie = a.sortie or os.path.join(V3, "80_Front-Office", "reviews", f"{nom}.html")
    os.makedirs(os.path.dirname(sortie), exist_ok=True)

    n, dette = generer(d, a.titre, sortie,
                       os.path.relpath(d, os.path.join(V3, "80_Front-Office")))
    print(f"{sortie}\n  {n} concepts, {dette} en attente d'un humain")


if __name__ == "__main__":
    main()

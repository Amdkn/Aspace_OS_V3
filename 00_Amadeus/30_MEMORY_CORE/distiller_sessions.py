"""Chaine complete : sessions recuperees -> markdown -> substrat de distillation.

ENTREE  : inventaire_sessions.json (produit par inventaire_sessions.py)
SORTIES :
  1. sessions_md/<origine>/<session>.md      -- le corpus lisible
  2. 50_Distillation/_substrat/05_Sessions.jsonl  -- une ligne par session,
     au MEME format que les quatre seaux du PARA, pour que la chaine de
     distillation deja ecrite (generer_briefs_distillation.py,
     concepts_vers_triplets.py, monter_70_onthologies.py) les avale sans
     modification.

POURQUOI CE FORMAT ET PAS UN AUTRE
`50_Distillation/METHODE.md` pose la regle : extraction scriptee exhaustive
d'abord, distillation semantique ensuite. Le substrat existant a une forme
precise (id, seau, titre, plan, mots, ...) ; produire autre chose obligerait a
reecrire toute la chaine aval. On s'y conforme.

DEDOUBLONNAGE
Les sessions se sont copiees au fil des reorganisations : la meme conversation
existe dans ~/.claude/projects, dans le PARA de V2, et parfois dans un
`_CAPTURE_`. On identifie par (identifiant de session, premier horodatage) et
on garde l'exemplaire le plus complet -- pas le plus recent sur le disque, qui
n'est que la date de la copie.
"""

from __future__ import annotations
import io, json, re, sys, time
from pathlib import Path

ICI = Path(__file__).resolve().parent
V3 = ICI.parent.parent
INVENTAIRE = ICI / "inventaire_sessions.json"
SORTIE_MD = ICI / "sessions_md"
SUBSTRAT = V3 / "50_Distillation" / "_substrat" / "05_Sessions.jsonl"
JOURNAL = ICI / "distiller_sessions.log"

MIN_CARACTERES_SI_UNIQUE = 200
COUPE_REPONSE = 6000


def ecrire(m: str) -> None:
    l = f"{time.strftime('%H:%M:%S')}  {m}"
    print(l, flush=True)
    with io.open(JOURNAL, "a", encoding="utf-8") as f:
        f.write(l + "\n")


def texte(contenu) -> str:
    if isinstance(contenu, str):
        return contenu
    if isinstance(contenu, list):
        return "\n".join(
            b.get("text", "") for b in contenu
            if isinstance(b, dict) and b.get("type") == "text"
        )
    return ""


def rejete(t: str) -> bool:
    t = t.strip()
    if not t:
        return True
    if t.startswith(("<system-reminder>", "Caveat:", "[{", '{"', "<local-command")):
        return True
    return "<task-notification>" in t[:200]


def lire_evenement(e: dict) -> tuple[str, str]:
    """Deux schemas : Claude Code (message.role) et Codex (payload.type)."""
    m = e.get("message")
    if isinstance(m, dict):
        return (m.get("role") or ""), texte(m.get("content"))
    if e.get("type") == "event_msg":
        p = e.get("payload") or {}
        if isinstance(p, dict):
            if p.get("type") == "user_message":
                return "user", str(p.get("message") or "")
            if p.get("type") == "agent_message":
                return "assistant", str(p.get("message") or "")
    return "", ""


def extraire(chemin: Path) -> dict | None:
    """Lit une session entiere et rend ses tours plus de quoi former le substrat."""
    tours, premier, dernier = [], None, None
    nu = na = carac = 0
    try:
        with io.open(chemin, encoding="utf-8", errors="replace") as f:
            for ligne in f:
                try:
                    e = json.loads(ligne)
                except Exception:
                    continue
                if not isinstance(e, dict):
                    continue
                ts = e.get("timestamp")
                if ts:
                    premier = premier or ts
                    dernier = ts
                role, t = lire_evenement(e)
                if not role or rejete(t):
                    continue
                if role == "user":
                    nu += 1
                    carac += len(t.strip())
                    tours.append(("user", t.strip()))
                elif role == "assistant":
                    na += 1
                    tours.append(("assistant", t.strip()[:COUPE_REPONSE]))
    except OSError:
        return None
    if nu == 0:
        return None
    if nu == 1 and carac < MIN_CARACTERES_SI_UNIQUE:
        return None
    return {"tours": tours, "debut": premier, "fin": dernier,
            "nu": nu, "na": na, "caracteres_humains": carac}


def titre_de(tours) -> str:
    """Le titre d'une session est sa premiere phrase humaine, coupee."""
    for role, t in tours:
        if role == "user":
            ligne = " ".join(t.split())
            return (ligne[:110] + "…") if len(ligne) > 110 else ligne
    return "(sans titre)"


MOT = re.compile(r"[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ'-]{2,}")


def main() -> int:
    if JOURNAL.exists():
        JOURNAL.unlink()
    if not INVENTAIRE.exists():
        ecrire(f"ABSENT : {INVENTAIRE} — lancer inventaire_sessions.py d'abord")
        return 1

    fiches = json.loads(INVENTAIRE.read_text(encoding="utf-8"))
    ecrire(f"{len(fiches)} sessions inventoriees")

    vus: dict[tuple, dict] = {}
    ecrits = ignores = doublons = 0
    lignes_substrat = []

    for i, fiche in enumerate(fiches, 1):
        p = Path(fiche["chemin"])
        if not p.exists():
            continue
        d = extraire(p)
        if not d:
            ignores += 1
            continue

        # Identite d'une conversation : son identifiant de fichier + son debut.
        cle = (p.stem, d["debut"])
        if cle in vus:
            doublons += 1
            # On garde l'exemplaire le plus riche, pas le plus recent.
            if d["nu"] + d["na"] <= vus[cle]["nu"] + vus[cle]["na"]:
                continue
        vus[cle] = d

        origine = "claude" if fiche["format"] == "claude" else "codex"
        dst = SORTIE_MD / f"_recuperees_{origine}" / f"{p.stem}.md"
        corps = []
        nu = 0
        for role, t in d["tours"]:
            if role == "user":
                nu += 1
                corps.append(f"\n## >>> UTILISATEUR #{nu}\n\n{t}\n")
            else:
                corps.append(f"\n### assistant\n\n{t}\n")
        titre = titre_de(d["tours"])
        entete = (
            "---\n"
            f"session: {p.stem}\n"
            f"origine: {fiche['format']}\n"
            f"chemin_source: {p}\n"
            f"debut: {d['debut']}\nfin: {d['fin']}\n"
            f"messages_utilisateur: {d['nu']}\nreponses_assistant: {d['na']}\n"
            f"titre: {json.dumps(titre, ensure_ascii=False)}\n"
            "---\n"
        )
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(entete + "".join(corps), encoding="utf-8")
        ecrits += 1

        # Ligne de substrat, au format des quatre seaux du PARA.
        humain = "\n".join(t for r, t in d["tours"] if r == "user")
        lignes_substrat.append({
            "id": f"05_Sessions/{origine}/{p.stem}.md",
            "seau": "05_Sessions",
            "nom": f"{p.stem}.md",
            "octets": fiche["octets"],
            "modifie": (d["debut"] or "")[:10],
            "profondeur": 2,
            "titre": titre,
            "fm": {"origine": fiche["format"]},
            "fm_cles": ["origine"],
            "okf": None,
            "type": "Session",
            "tags_fm": None,
            "nb_titres": d["nu"],
            "plan": [t.split("\n")[0][:90] for r, t in d["tours"] if r == "user"][:40],
            "wikilinks": [],
            "liens": sorted(set(re.findall(r"https?://[^\s)\]]+", humain)))[:30],
            "tags_corps": [],
            "mots": len(MOT.findall(humain)),
        })

        if i % 200 == 0:
            ecrire(f"  {i}/{len(fiches)} — {ecrits} ecrites, {doublons} doublons, {ignores} sans contenu")

    SUBSTRAT.parent.mkdir(parents=True, exist_ok=True)
    with io.open(SUBSTRAT, "w", encoding="utf-8") as f:
        for l in lignes_substrat:
            f.write(json.dumps(l, ensure_ascii=False) + "\n")

    from collections import Counter
    par_mois = Counter((l["modifie"] or "?")[:7] for l in lignes_substrat)
    ecrire("")
    ecrire(f"SESSIONS ECRITES : {ecrits}   (doublons ecartes : {doublons}, sans contenu : {ignores})")
    ecrire(f"mots humains cumules : {sum(l['mots'] for l in lignes_substrat):,}")
    ecrire("par mois :")
    for m in sorted(par_mois):
        ecrire(f"   {m}  {par_mois[m]:5d}")
    ecrire(f"substrat : {SUBSTRAT}")
    ecrire(f"markdown : {SORTIE_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

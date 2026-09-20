#!/usr/bin/env python3
"""nardole_assembler.py — compile un prompt depuis un blueprint + signal metabolique.

Blueprint dict : {"system": ..., "constraints": [...], "tools": [...]}
Signal metabolique : state.json sonde READ-ONLY (jamais ecrit ici).
Plafond 2048 tokens verifie (estimation ~4 chars/token), hash sha256 du prompt.

    python nardole_assembler.py --blueprint b.json --state s.json --out p.txt
    python nardole_assembler.py --slug mon-slug   # blueprint depuis prompt_blueprints
"""
import argparse, hashlib, json, os, sqlite3, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DB   = os.environ.get("ASPACE_DB", os.path.join(HERE, "uc.db"))

TOKEN_CEILING = 2048
CHARS_PER_TOKEN = 4


def load_blueprint(slug):
    c = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    c.row_factory = sqlite3.Row
    row = c.execute("SELECT * FROM prompt_blueprints WHERE slug=?", (slug,)).fetchone()
    if not row:
        raise SystemExit(f"blueprint introuvable: {slug}")
    return dict(row)


def metabolic_signal(state_path):
    """Sonde read-only : lit l'etat metabolique, n'ecrit jamais."""
    if not state_path:
        return {}
    with open(state_path, encoding="utf-8") as f:
        st = json.load(f)
    # on ne garde que des scalaires : le signal, pas la charge
    return {k: v for k, v in st.items() if isinstance(v, (int, float, str, bool))}


def compile_prompt(blueprint, signal):
    if isinstance(blueprint, dict) and "template_body" in blueprint:
        body = blueprint["template_body"]
        ceiling = int(blueprint.get("max_token_ceiling", TOKEN_CEILING))
    else:
        body = blueprint.get("system", "")
        ceiling = TOKEN_CEILING
    parts = [body]
    for cons in blueprint.get("constraints", []):
        parts.append(f"CONTRAINTE: {cons}")
    tools = blueprint.get("tools", [])
    if tools:
        parts.append("OUTILS: " + ", ".join(tools))
    if signal:
        parts.append("METABOLISME: " + json.dumps(signal, ensure_ascii=False, sort_keys=True))
    prompt = "\n".join(parts)
    tokens = len(prompt) // CHARS_PER_TOKEN + (1 if len(prompt) % CHARS_PER_TOKEN else 0)
    if tokens > ceiling:
        raise SystemExit(f"plafond depasse: {tokens} > {ceiling} tokens")
    return prompt, tokens, hashlib.sha256(prompt.encode("utf-8")).hexdigest()


def main():
    ap = argparse.ArgumentParser(description="assembleur de prompt Nardole")
    ap.add_argument("--blueprint", help="fichier JSON blueprint (system+constraints+tools)")
    ap.add_argument("--slug", help="blueprint depuis prompt_blueprints (uc.db)")
    ap.add_argument("--state", help="state.json metabolique — sonde read-only")
    ap.add_argument("--out", help="ecrit le prompt compile dans ce fichier")
    a = ap.parse_args()
    if not a.blueprint and not a.slug:
        ap.error("--blueprint ou --slug requis")
    bp = load_blueprint(a.slug) if a.slug else json.load(open(a.blueprint, encoding="utf-8"))
    signal = metabolic_signal(a.state)
    prompt, tokens, sha = compile_prompt(bp, signal)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(prompt)
    print(json.dumps({"ok": True, "tokens": tokens, "ceiling": TOKEN_CEILING,
                      "sha256": sha, "out": a.out}, ensure_ascii=False))


if __name__ == "__main__":
    main()

"""
render_session.py — Rend la Strategy Session HTML (single-file, offline pur)
depuis un questions.json auteuré par l'agent après lecture des métriques D1.

Usage :
  python render_session.py <questions.json> [--date YYYY-MM-DD] [--week W4]

questions.json schema :
{
  "date": "2026-07-07", "week": "W4",
  "zones": {"client": "Exécution client", "finance": "Discipline financière",
            "meta": "Sobriété méta", "cadence": "Cadence 12WY"},
  "blunt_lines": {"client": "...", "meta": "..."},        # ligne dure si franchise >= 7
  "moves": {"client": ["move1", "move2", "move3"], ...},  # 3 moves par zone
  "questions": [
    {"id": "q1", "zone": "client", "type": "slider", "label": "...", "max": 10, "invert": false},
    {"id": "q2", "zone": "meta",   "type": "radio",  "label": "...",
     "options": [{"label": "...", "score": 0}, {"label": "...", "score": 10}]},
    {"id": "avoid", "zone": null,  "type": "text",   "label": "CE QUE TU ÉVITES cette semaine"},
    {"id": "blunt", "zone": null,  "type": "slider", "label": "Franchise du rapport", "max": 10}
  ]
}

Antifragile : validation intégrée post-render (offline = 0 lien externe,
compte des inputs = compte des questions). Échec de validation = exit 2, pas de faux succès.
"""
from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
DEFAULT_STRATEGY_DIR = Path(r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\strategy_sessions")

TEMPLATE = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Strategy Session — __WEEK__ (__DATE__)</title>
<style>
  :root { --bg:#0A0E16; --panel:#111827; --gold:#C8A55C; --txt:#E5E7EB; --dim:#9CA3AF; --red:#EF4444; }
  * { box-sizing:border-box; margin:0; padding:0; }
  body { background:var(--bg); color:var(--txt); font-family:Georgia,serif; line-height:1.6; padding:2rem 1rem; }
  .wrap { max-width:720px; margin:0 auto; }
  h1 { color:var(--gold); font-size:1.6rem; letter-spacing:.05em; border-bottom:1px solid var(--gold); padding-bottom:.6rem; margin-bottom:.4rem; }
  .sub { color:var(--dim); font-size:.9rem; margin-bottom:2rem; }
  .q { background:var(--panel); border-left:3px solid var(--gold); padding:1.1rem 1.3rem; margin-bottom:1.2rem; border-radius:0 8px 8px 0; }
  .q label.main { display:block; font-size:1.02rem; margin-bottom:.7rem; }
  .zone-tag { display:inline-block; font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; color:var(--gold); border:1px solid var(--gold); padding:.1rem .5rem; border-radius:3px; margin-bottom:.5rem; }
  input[type=range] { width:100%; accent-color:var(--gold); }
  .sval { color:var(--gold); font-weight:bold; font-size:1.1rem; }
  .opt { display:block; margin:.4rem 0; cursor:pointer; color:var(--dim); }
  .opt input { accent-color:var(--gold); margin-right:.5rem; }
  textarea { width:100%; min-height:80px; background:#0D1220; color:var(--txt); border:1px solid #374151; border-radius:6px; padding:.7rem; font-family:inherit; font-size:.95rem; }
  button { background:var(--gold); color:#0A0E16; border:none; font-family:inherit; font-size:1.05rem; font-weight:bold; padding:.9rem 1.6rem; border-radius:6px; cursor:pointer; margin:1.5rem .5rem 0 0; }
  button.ghost { background:transparent; color:var(--gold); border:1px solid var(--gold); }
  #report { display:none; white-space:pre-wrap; background:var(--panel); border:1px solid var(--gold); border-radius:8px; padding:1.5rem; margin-top:2rem; font-family:'Courier New',monospace; font-size:.9rem; }
  @media print { body { background:#fff; color:#000; } .q, button { display:none; } #report { display:block !important; border-color:#000; color:#000; background:#fff; } }
</style></head><body><div class="wrap">
<h1>⚔ STRATEGY SESSION — __WEEK__</h1>
<div class="sub">__DATE__ · Questions ancrées sur les faits mesurés de la semaine. Réponds vite, corrige rien.</div>
<div id="form"></div>
<button onclick="genReport()">Générer le rapport</button>
<button class="ghost" onclick="copyReport()">Copier</button>
<button class="ghost" onclick="window.print()">Imprimer</button>
<div id="report"></div>
<script>
const CFG = __CFG__;
const form = document.getElementById('form');
CFG.questions.forEach(q => {
  const d = document.createElement('div'); d.className = 'q'; d.id = 'box_' + q.id;
  let h = q.zone ? `<span class="zone-tag">${CFG.zones[q.zone]}</span>` : '';
  h += `<label class="main">${q.label}</label>`;
  if (q.type === 'slider') {
    const max = q.max || 10;
    h += `<input type="range" id="${q.id}" min="0" max="${max}" value="${Math.floor(max/2)}"
           oninput="document.getElementById('v_${q.id}').textContent=this.value">
          <div>Valeur : <span class="sval" id="v_${q.id}">${Math.floor(max/2)}</span> / ${max}</div>`;
  } else if (q.type === 'radio') {
    q.options.forEach((o, i) => {
      h += `<label class="opt"><input type="radio" name="${q.id}" value="${o.score}"
            ${i === 0 ? 'checked' : ''}>${o.label}</label>`;
    });
  } else {
    h += `<textarea id="${q.id}" placeholder="Tes mots, pas les miens."></textarea>`;
  }
  d.innerHTML = h; form.appendChild(d);
});
function val(q) {
  if (q.type === 'slider') {
    const raw = +document.getElementById(q.id).value, max = q.max || 10;
    let s = raw / max * 10; if (q.invert) s = 10 - s; return s;
  }
  if (q.type === 'radio') {
    const c = document.querySelector(`input[name="${q.id}"]:checked`);
    return c ? +c.value : 0;
  }
  return document.getElementById(q.id).value.trim();
}
function genReport() {
  const zoneScores = {}, zoneCounts = {};
  let texts = {};
  CFG.questions.forEach(q => {
    const v = val(q);
    if (q.type === 'text') { texts[q.id] = v; return; }
    if (!q.zone) { texts[q.id] = v; return; }
    zoneScores[q.zone] = (zoneScores[q.zone] || 0) + v;
    zoneCounts[q.zone] = (zoneCounts[q.zone] || 0) + 1;
  });
  const finals = Object.keys(CFG.zones).map(z => ({
    z, name: CFG.zones[z],
    score: zoneCounts[z] ? Math.round(zoneScores[z] / zoneCounts[z]) : null
  })).filter(x => x.score !== null).sort((a, b) => b.score - a.score);
  const weakest = finals[finals.length - 1];
  const blunt = +(texts['blunt'] ?? 5) >= 7;
  let r = `═══ RAPPORT STRATEGY SESSION — __WEEK__ (__DATE__) ═══\\n\\nSCORES PAR ZONE\\n`;
  finals.forEach(f => r += `  ${f.name} : ${f.score}/10\\n`);
  r += `\\n🔴 ZONE LA PLUS FAIBLE : ${weakest.name.toUpperCase()} (${weakest.score}/10)\\n`;
  if (blunt && CFG.blunt_lines[weakest.z]) r += `\\nLa vérité en face : ${CFG.blunt_lines[weakest.z]}\\n`;
  if (texts['avoid']) r += `\\nCE QUE TU ÉVITES (tes mots) : ${texts['avoid']}\\n`;
  if (texts['focus']) r += `FOCUS (tes mots) : ${texts['focus']}\\n`;
  r += `\\nLES 3 MOUVEMENTS DE LA SEMAINE (par impact)\\n`;
  (CFG.moves[weakest.z] || []).forEach((m, i) => r += `${i + 1}. ${m}\\n`);
  r += `\\n─────\\nRe-réponds lundi prochain. La zone faible du rapport = le focus de ta semaine.`;
  const el = document.getElementById('report');
  el.textContent = r; el.style.display = 'block'; el.scrollIntoView({behavior: 'smooth'});
}
function copyReport() {
  const el = document.getElementById('report');
  if (el.textContent) navigator.clipboard.writeText(el.textContent);
}
</script></div></body></html>
"""


def render(cfg: dict, out_dir: Path) -> Path:
    date = cfg.get("date") or time.strftime("%Y-%m-%d")
    week = cfg.get("week") or "W?"
    html = (TEMPLATE.replace("__CFG__", json.dumps(cfg, ensure_ascii=False))
                    .replace("__WEEK__", week).replace("__DATE__", date))
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{date}_{week}_strategy_session.html"
    out.write_text(html, encoding="utf-8")
    return out


def validate(out: Path, cfg: dict) -> list[str]:
    """Antifragile : jamais de faux succès. Offline pur + intégrité structurelle."""
    html = out.read_text(encoding="utf-8")
    errs = []
    if re.search(r'(?:src|href)\s*=\s*["\']https?://', html):
        errs.append("lien externe détecté — la session doit être 100% offline")
    n_q = len(cfg["questions"])
    if f'"questions"' not in html or html.count('"id"') < n_q:
        errs.append(f"questions embarquées incomplètes (attendu {n_q})")
    for zone in cfg["zones"]:
        if zone not in json.dumps(cfg.get("moves", {})):
            errs.append(f"zone '{zone}' sans moves — le rapport serait vide si elle est la plus faible")
    return errs


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    cfg = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    out_dir = DEFAULT_STRATEGY_DIR
    out = render(cfg, out_dir)
    errs = validate(out, cfg)
    if errs:
        for e in errs:
            print(f"VALIDATION FAIL: {e}", file=sys.stderr)
        return 2
    print(f"OK: {out} ({out.stat().st_size} B, {len(cfg['questions'])} questions, offline valide)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

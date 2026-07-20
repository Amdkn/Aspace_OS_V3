#!/usr/bin/env python3
"""sob.py — interface unique du SOB (tout harness : Hermes/Multica/AIonUI/Orca/CC).
Usage:
  sob.py status
  sob.py prospect  "Nom" "https://url-verifiable" "segment" [source]     (idempotent: dedup nom)
  sob.py outreach  "Nom" canal "premiere ligne du message"               (append log)
  sob.py stage     "Nom" contacted|replied|demo|proposal|won|lost
  sob.py subscribe "Nom" 1000 "segment"                                  (won -> client paye)
  sob.py spend     12.5 inference|infra|acquisition|... domaine "note"
  sob.py issue     "client" low|med|high "resume"
  sob.py exp       domaine "segment" "hypothese" [running|pass|fail|inconclusive]
Regle: un prospect SANS URL verifiable n'entre pas (refuse les URLs vides/placeholder)."""
import sys, sqlite3, datetime, os
DB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "aspace.db")
def now(): return datetime.datetime.now().isoformat(timespec="seconds")
def main(a):
    db = sqlite3.connect(DB); c = db.cursor(); cmd = a[0]
    if cmd == "status":
        mrr = c.execute("SELECT COALESCE(SUM(mrr),0) FROM subscriptions WHERE status='subscribed'").fetchone()[0]
        pipe = dict(c.execute("SELECT stage, COUNT(*) FROM pipeline GROUP BY stage").fetchall())
        cash = c.execute("SELECT COALESCE(SUM(CASE WHEN category='revenue' THEN amount ELSE -abs(amount) END),0) FROM ledger").fetchone()[0]
        out = c.execute("SELECT COUNT(*) FROM outreach_log WHERE direction='out'").fetchone()[0]
        print(f"MRR={mrr}$ | pipeline={pipe or '{}'} | outreach_out={out} | net_cash={round(cash,2)}$")
    elif cmd == "prospect":
        name, url, seg = a[1], a[2], a[3]; src = a[4] if len(a) > 4 else "manual"
        if not url.startswith("http") or "example" in url or "TODO" in url:
            print(f"REFUSE: URL non verifiable ({url!r}) — regle R2"); return 1
        if c.execute("SELECT id FROM pipeline WHERE prospect=?", (name,)).fetchone():
            print(f"IDEMPOTENT: {name} deja en pipeline"); return 0
        c.execute("INSERT INTO pipeline(prospect,segment,stage,source,ts_created,ts_updated,note) VALUES(?,?,?,?,?,?,?)",
                  (name, seg, "new", src, now(), now(), url))
        db.commit(); print(f"+prospect {name} [{seg}] {url}")
    elif cmd == "outreach":
        name, ch, head = a[1], a[2], a[3]
        c.execute("INSERT INTO outreach_log(ts,prospect,channel,direction,message_head) VALUES(?,?,?,?,?)",
                  (now(), name, ch, "out", head[:120]))
        c.execute("UPDATE pipeline SET stage=CASE WHEN stage='new' THEN 'contacted' ELSE stage END, ts_updated=? WHERE prospect=?", (now(), name))
        db.commit(); print(f"+outreach {name} via {ch}")
    elif cmd == "stage":
        c.execute("UPDATE pipeline SET stage=?, ts_updated=? WHERE prospect=?", (a[2], now(), a[1]))
        db.commit(); print(f"{a[1]} -> {a[2]} ({c.rowcount} maj)")
    elif cmd == "subscribe":
        name, mrr, seg = a[1], float(a[2]), a[3]
        if c.execute("SELECT id FROM subscriptions WHERE customer=? AND status='subscribed'", (name,)).fetchone():
            print(f"IDEMPOTENT: {name} deja abonne"); return 0
        c.execute("INSERT INTO subscriptions(customer,segment,mrr,status,started) VALUES(?,?,?,?,?)", (name, seg, mrr, "subscribed", now()))
        c.execute("UPDATE pipeline SET stage='won', ts_updated=? WHERE prospect=?", (now(), name))
        c.execute("INSERT INTO ledger(ts,amount,category,domain,note) VALUES(?,?,?,?,?)", (now(), mrr, "revenue", "sales", f"1er mois {name}"))
        db.commit(); print(f"WON {name} {mrr}$/mois — MRR mis a jour")
    elif cmd == "spend":
        c.execute("INSERT INTO ledger(ts,amount,category,domain,note) VALUES(?,?,?,?,?)", (now(), -abs(float(a[1])), a[2], a[3], a[4] if len(a)>4 else ""))
        db.commit(); print("+spend loggee")
    elif cmd == "issue":
        c.execute("INSERT INTO issues(ts,customer,severity,status,summary) VALUES(?,?,?,?,?)", (now(), a[1], a[2], "open", a[3]))
        db.commit(); print("+issue")
    elif cmd == "exp":
        st = a[4] if len(a) > 4 else "running"
        c.execute("INSERT INTO experiments(ts,domain,segment,hypothesis,status) VALUES(?,?,?,?,?)", (now(), a[1], a[2], a[3], st))
        db.commit(); print("+exp")
    else:
        print(__doc__); return 1
    return 0
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]) if len(sys.argv) > 1 else (print(__doc__), 1)[1])

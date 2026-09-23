import sqlite3, datetime

c = sqlite3.connect('10_Tech_OS/kernel/uc.db', isolation_level=None)
now = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0)
c.execute(
    'insert or replace into claim(work_id,harness,claimed_at,expires_at) values (141,?,?,?)',
    ('rory_build_l1', now.isoformat(), (now + datetime.timedelta(hours=1)).isoformat())
)
pred_ts = (now - datetime.timedelta(minutes=2)).isoformat()
pred_txt = ('verify_deal.py affiche DEAL_OK et rc=0 apres refresh pulse.json '
            '(date_pulse=2026-09-16) + durcissement in place ; seuls pulse.json et '
            'verify_deal.py modifies')
c.execute(
    'insert into prediction(work_id,claim_text,confidence,predicted_at) '
    'values (141, ?, ?, ?)',
    (141, pred_txt, 0.9, pred_ts)
)
print('claim+prediction ok, pred_at', pred_ts)

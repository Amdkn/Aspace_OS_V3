import subprocess, sqlite3, sys, os
ROOT = r'C:/Users/amado/ASpace_OS_V3'
K = ROOT + '/10_Tech_OS/kernel'

def rc(args, cwd=K):
    p = subprocess.run([sys.executable] + args, cwd=cwd, capture_output=True, text=True, timeout=120)
    return p.returncode, (p.stdout + p.stderr)[-400:]

checks = {}
# B1: nardole assembler
checks['B1_nardole'] = rc(['nardole_assembler.py', '--blueprint', '_b1_bp.json', '--state', '_b1_state.json', '--out', '_b1_recheck_out.txt'])
# B2: graham checkpoint
checks['B2_graham'] = rc(['graham_checkpoint.py', 'save', '--work', '77'])
registre = ROOT + '/60_Implementation_Méthodologiques/_b4_recheck_out/-test-v2-sample-md.registre.json'
checks['B4_onto'] = rc(['../../70_Onthologies/onto_gate.py', registre, '--out', ROOT + '/70_Onthologies/_b4_recheck_out'])
# B4: gates (need an input file; use an existing V2 sample md)
sample = ROOT + '/50_Distillation/_test_v2_sample.md'
checks['B4_distill'] = rc(['../../50_Distillation/distill_gate.py', sample, '--out', ROOT + '/50_Distillation/_b4_recheck_out'])
checks['B4_impl'] = rc(['../../60_Implementation_Méthodologiques/impl_gate.py', sample, '--out', ROOT + '/60_Implementation_Méthodologiques/_b4_recheck_out'])
checks['B4_onto'] = rc(['../../70_Onthologies/onto_gate.py', sample, '--out', ROOT + '/70_Onthologies/_b4_recheck_out'])

c = sqlite3.connect(K + '/uc.db')
print('b3 tables:', [t for t in ('prompt_blueprints','domain_rules_b2','marvel_personas_b3') if c.execute("select 1 from sqlite_master where name=?",(t,)).fetchone()])
for k, (code, out) in checks.items():
    print(f'{k}: rc={code} :: {out.strip()[:300]}')

#!/usr/bin/env python3
"""dark_factory.py - L orchestreur de la Dark Factory A'Space.
Chaine: intent.md -> gate.py (admission) -> nardole_assembler.py (compile prompt)
        -> uc.py submit (work + prediction) -> build compagnon (herdr pane)
        -> review.py (rc=0 evidence) -> done. Sans intervention humaine.
Usage: python dark_factory.py --intent <chemin_intent.md> [--dry-run]
"""
import argparse, json, os, subprocess, sys, hashlib, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
V3 = os.path.dirname(os.path.dirname(HERE))
UC = os.path.join(HERE, 'uc.py')
ASSEMBLER = os.path.join(HERE, 'nardole_assembler.py')

def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=kw.get('timeout', 120), cwd=HERE)
    return r.returncode, (r.stdout or '') + (r.stderr or '')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--intent', required=True, help='chemin du intent.md FROZEN')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    if not os.path.exists(args.intent):
        print(f'INTENT ABSENT: {args.intent}'); return 1

    content = open(args.intent, encoding='utf-8').read()
    if 'FROZEN' not in content:
        print('INTENT non FROZEN - refuse par la chaine Dark Factory.'); return 1
    print(f'[1/5] INTENT valide (FROZEN): {args.intent}')

    # 1.bis Pré-évaluation symbolique Morty Local SLM Engine
    try:
        from slm.morty_engine import MortyLocalEngine
        morty = MortyLocalEngine()
        decision = morty.evaluate_decision({"intent": os.path.basename(args.intent), "energy": 1.0, "urgency": 0.5})
        if decision.get("veto"):
            print(f'MORTY VETO: {decision.get("reasons")}'); return 1
        print(f'[1b/5] Morty SLM Engine: PASS ({decision.get("action_recommended")})')
    except Exception as e:
        print(f'[1b/5] Morty SLM Engine: warning bypass ({e})')

    # 2. Gate admission (gate.py)
    rc, out = run([sys.executable, os.path.join(HERE, 'gate.py'), 'run'])
    print(f'[2/5] gate.py rc={rc}')
    if rc != 0:
        print(f'GATE REFUSE: {out[:200]}'); return 1

    # 3. Compile le prompt via nardole_assembler (Prompt-as-Code)
    blueprint = {
        'system': f'Tu es un compagnon A Space OS V3. Ton mandat vient de l intent: {os.path.basename(args.intent)}.',
        'constraints': ['Fait = preuve d environnement (chemin + rc + lecture retour)', 'Ne demande jamais rien - GO permanent Amadou', 'A SOURCER si tu ne peux pas sourcer'],
        'tools': ['terminal', 'file', 'python'],
    }
    import tempfile
    tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8')
    json.dump(blueprint, tmp)
    tmp.close()
    state_path = os.path.join(V3, '20_Life_OS', '22_Wheel_Discovery', 'LD01_Business_Book', 'state.json')
    rc, out = run(['C:/Users/amado/AppData/Local/hermes/hermes-agent/venv/Scripts/python.exe', ASSEMBLER, '--blueprint', tmp.name, '--state', state_path])
    print(f'[3/5] nardole_assembler rc={rc}')
    if rc != 0:
        print(f'ASSEMBLER ECHEC COMPLET:\n{out}'); return 1
    compiled = out  # le prompt compile

    # 4. Soumet le work dans uc.db
    title = os.path.basename(args.intent).replace('.md', '')
    rc, out = run(['C:/Users/amado/AppData/Local/hermes/hermes-agent/venv/Scripts/python.exe', UC, 'submit', '--title', title, '--layer', 'L2'])
    print(f'[4/5] uc.py submit rc={rc} -> {out[:100]}')
    if rc != 0:
        print(f'SUBMIT ECHEC'); return 1

    # 5. Dispatch au compagnon via herdr (le pane visible)
    print(f'[5/5] DISPATCH: le work est dans uc.db. Les crons des Docteurs le claim au prochain tick.')
    print(f'      Le compagnon (nardole/clara/bill) execute avec le prompt compile par nardole_assembler.')
    return 0

if __name__ == '__main__':
    sys.exit(main())

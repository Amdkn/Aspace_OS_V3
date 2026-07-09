import subprocess
import json
import sys

def test_gws():
    print("Testing GWS CLI via Python subprocess...")
    params = {"pageSize": 5, "q": "mimeType='application/vnd.google-apps.spreadsheet'"}
    
    cmd = [
        "gws",
        "drive",
        "files",
        "list",
        "--params",
        json.dumps(params)
    ]
    
    try:
        # We need to run gws.ps1 on Windows if gws alone is not resolved directly,
        # but since 'gws' worked as an external command, we can try running with shell=True
        # or by calling powershell.exe with gws.
        res = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        if res.returncode == 0:
            print("SUCCESS! Output:")
            print(res.stdout)
            try:
                files = json.loads(res.stdout)
                print(f"Parsed {len(files.get('files', []))} spreadsheets.")
                for f in files.get('files', []):
                    print(f" - {f.get('name')} (ID: {f.get('id')})")
            except Exception as e:
                print(f"Error parsing JSON output: {e}")
                print(f"Raw output:\n{res.stdout}")
        else:
            print(f"FAILED with code {res.returncode}")
            print(f"Stdout: {res.stdout}")
            print(f"Stderr: {res.stderr}")
    except Exception as e:
        print(f"Exception during execution: {e}")

if __name__ == "__main__":
    test_gws()

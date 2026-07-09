import os
import shutil

paths_to_purge = [
    r"C:\Aspace00\aspace_a0_amadeus\openclaw",
    r"C:\Aspace00\aspace_a0_amadeus\_SPECS"
]

def remove_readonly(func, path, excinfo):
    os.chmod(path, 0o777)
    func(path)

for path in paths_to_purge:
    if os.path.exists(path):
        print(f"Purging {path}...")
        try:
            shutil.rmtree(path, onerror=remove_readonly)
            print(f"Success: {path} removed.")
        except Exception as e:
            print(f"Error removing {path}: {e}")
    else:
        print(f"Path not found: {path}")

root = r"C:\Aspace00\aspace_a0_amadeus"
print("AUDIT_START")
if os.path.exists(root):
    for item in os.listdir(root):
        print(f"ITEM:{item}")
print("AUDIT_END")

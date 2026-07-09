import os
import shutil

path = r"C:\Aspace00\aspace_a0_amadeus\20_Life_OS\24_PARA_Enterprise\04_Archives_Data\A0_Memory\legacy"

def remove_readonly(func, path, excinfo):
    os.chmod(path, 0o777)
    func(path)

if os.path.exists(path):
    print(f"Purging {path}...")
    try:
        shutil.rmtree(path, onerror=remove_readonly)
        print("Success: Legacy archives fully purged.")
    except Exception as e:
        print(f"Error: {e}")
else:
    print("Path already removed or not found.")

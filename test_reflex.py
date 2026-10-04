import sys
sys.path.insert(0, ".")
import importlib

# Attempt to load jev_reflex
try:
    mod = importlib.import_module("10_Tech_OS.kernel.jev_reflex")
    print("jev_reflex loaded successfully")
except Exception as e:
    print(f"Error loading jev_reflex: {e}")

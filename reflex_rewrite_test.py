import sys
import importlib
sys.path.insert(0, ".")

try:
    mod = importlib.import_module("10_Tech_OS.kernel.inter_fabric")
    envelope = mod.InterFabricEnvelope
    print("InterFabricEnvelope imported correctly.")
except Exception as e:
    print(f"Error: {e}")

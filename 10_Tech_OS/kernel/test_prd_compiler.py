#!/usr/bin/env python3
import os
import sys
import unittest
import tempfile
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
COMPILER_PATH = os.path.join(HERE, "prd_compiler.py")

class TestPrdCompiler(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.tmp_dir.cleanup()

    def test_compilation(self):
        # Create a mock mandate file
        mandate_path = os.path.join(self.tmp_dir.name, "mandate.md")
        with open(mandate_path, 'w', encoding='utf-8') as f:
            f.write("""# Scope
Build an awesome feature.

# Dependencies
Must rely on the kernel.

# Acceptance
Should pass all tests.

# Evidence
Logs in stdout.

# Exclusive Files
kernel/test_feature.py
kernel/feature.py
""")

        cmd = [sys.executable, COMPILER_PATH, mandate_path]
        p = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(p.returncode, 0)
        output = p.stdout

        # Assert correct compilation output
        self.assertIn("# Bounded PRD", output)
        self.assertIn("## Scope\nBuild an awesome feature.", output)
        self.assertIn("## Owner\nPrimary Spec: Clara\nGatekeeper: Rick", output)
        self.assertIn("## Dependencies\nMust rely on the kernel.", output)
        self.assertIn("## Acceptance\nShould pass all tests.", output)
        self.assertIn("## Evidence\nLogs in stdout.", output)
        self.assertIn("## Exclusive Files\nkernel/test_feature.py\nkernel/feature.py", output)

    def test_missing_sections_default(self):
        # Create a mock mandate file with no sections
        mandate_path = os.path.join(self.tmp_dir.name, "mandate2.md")
        with open(mandate_path, 'w', encoding='utf-8') as f:
            f.write("Just some text without headers.")

        cmd = [sys.executable, COMPILER_PATH, mandate_path]
        p = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(p.returncode, 0)
        output = p.stdout

        # Assert correct compilation output
        self.assertIn("# Bounded PRD", output)
        self.assertIn("## Scope\nJust some text without headers.", output)
        self.assertIn("## Owner\nPrimary Spec: Clara\nGatekeeper: Rick", output)
        self.assertIn("## Dependencies\nNone explicitly defined.", output)
        self.assertIn("## Acceptance\nStandard acceptance criteria apply.", output)
        self.assertIn("## Evidence\nStandard evidence required.", output)
        self.assertIn("## Exclusive Files\nNone explicitly defined.", output)

if __name__ == "__main__":
    unittest.main()

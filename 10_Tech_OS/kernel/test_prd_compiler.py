import unittest
import os
import tempfile
import subprocess
from prd_compiler import compile_prd

class TestPRDCompiler(unittest.TestCase):
    def test_compile_prd_structure(self):
        mandate = "Implement bounded logic."
        prd = compile_prd(mandate)

        # Check required sections
        self.assertIn("## Scope", prd)
        self.assertIn("## Owner", prd)
        self.assertIn("## Dependencies", prd)
        self.assertIn("## Acceptance Criteria", prd)
        self.assertIn("## Evidence", prd)
        self.assertIn("## Exclusive Files", prd)

        # Check specific assignments
        self.assertIn("**Primary Spec:** Clara", prd)
        self.assertIn("**Mechanism Gatekeeper:** Rick", prd)

        # Check scope content
        self.assertIn("Implement bounded logic.", prd)

    def test_cli(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            mandate_file = os.path.join(tmpdir, "mandate.txt")
            out_file = os.path.join(tmpdir, "output.md")

            with open(mandate_file, 'w') as f:
                f.write("Compile fresh Linear mandate into bounded PRD.")

            env = os.environ.copy()
            script_path = os.path.join(os.path.dirname(__file__), "prd_compiler.py")

            result = subprocess.run(
                ["python3", script_path, "--mandate-file", mandate_file, "--out-file", out_file],
                env=env,
                capture_output=True,
                text=True
            )

            self.assertEqual(result.returncode, 0)
            self.assertTrue(os.path.exists(out_file))

            with open(out_file, 'r') as f:
                content = f.read()

            self.assertIn("Compile fresh Linear mandate into bounded PRD.", content)
            self.assertIn("**Primary Spec:** Clara", content)
            self.assertIn("**Mechanism Gatekeeper:** Rick", content)

if __name__ == "__main__":
    unittest.main()

import unittest
import os
import tempfile
import shutil
import subprocess

from prd_compiler import compile_prd

class TestPRDCompiler(unittest.TestCase):
    def test_compile_prd_with_sections(self):
        mandate = """
# Scope
This is the scope.

# Dependencies
Python, OS

# Acceptance
Passes all tests.

# Evidence
Logs are visible.

# Exclusive Files
test_file.py
"""
        prd = compile_prd(mandate, "TEST-123", "FORGE_TEST")

        self.assertIn("# Bounded PRD: TEST-123", prd)
        self.assertIn("Forge Group: FORGE_TEST", prd)
        self.assertIn("## Scope\nThis is the scope.", prd)
        self.assertIn("## Owner\n- Primary Spec: Clara\n- Mechanism Gatekeeper: Rick", prd)
        self.assertIn("## Dependencies\nPython, OS", prd)
        self.assertIn("## Acceptance\nPasses all tests.", prd)
        self.assertIn("## Evidence\nLogs are visible.", prd)
        self.assertIn("## Exclusive Files\ntest_file.py", prd)

    def test_compile_prd_empty_mandate(self):
        mandate = ""
        prd = compile_prd(mandate, "TEST-456", "FORGE_EMPTY")

        self.assertIn("# Bounded PRD: TEST-456", prd)
        self.assertIn("Forge Group: FORGE_EMPTY", prd)
        self.assertIn("## Scope\nNo scope provided.", prd)
        self.assertIn("## Owner\n- Primary Spec: Clara\n- Mechanism Gatekeeper: Rick", prd)
        self.assertIn("## Dependencies\nNone specified.", prd)
        self.assertIn("## Acceptance\nTests pass.", prd)
        self.assertIn("## Evidence\nLogs and successful test runs.", prd)
        self.assertIn("## Exclusive Files\nNone specified.", prd)

    def test_compile_prd_partial_sections(self):
        mandate = """
Just some random text.
# Scope
Defined scope.
"""
        prd = compile_prd(mandate, "TEST-789", "FORGE_PARTIAL")
        self.assertIn("## Scope\nDefined scope.", prd)
        self.assertIn("## Dependencies\nNone specified.", prd)

class TestPRDCompilerCLI(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.original_cwd = os.getcwd()
        # We need to run the CLI from the root so that `10_Tech_OS/PRD_Autonomy/...` is created locally.
        # But for the test, let's just test that the script runs successfully with a dummy file.
        self.test_mandate_path = os.path.join(self.temp_dir, "test_mandate.txt")
        with open(self.test_mandate_path, "w") as f:
            f.write("# Scope\nCLI test scope.")

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_cli_execution(self):
        env = os.environ.copy()
        script_path = os.path.join(self.original_cwd, "10_Tech_OS", "kernel", "prd_compiler.py")

        # Make sure PRD_Autonomy structure gets created in temp_dir instead of polluting the real repo
        os.chdir(self.temp_dir)
        try:
            result = subprocess.run([
                "python3", script_path,
                "--file", self.test_mandate_path,
                "--issue_id", "CLI-001",
                "--forge_group", "FORGE_CLI"
            ], capture_output=True, text=True, env=env)

            self.assertEqual(result.returncode, 0)

            out_file = os.path.join("10_Tech_OS", "PRD_Autonomy", "FORGE_CLI", "CLI-001.md")
            self.assertTrue(os.path.exists(out_file))

            with open(out_file, "r") as f:
                content = f.read()
                self.assertIn("## Scope\nCLI test scope.", content)
                self.assertIn("- Primary Spec: Clara", content)
        finally:
            os.chdir(self.original_cwd)

if __name__ == '__main__':
    unittest.main()

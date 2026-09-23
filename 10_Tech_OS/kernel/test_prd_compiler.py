#!/usr/bin/env python3
import os
import tempfile
import unittest
import shutil

from prd_compiler import parse_mandate, compile_prd

class TestPRDCompiler(unittest.TestCase):
    def test_parse_mandate_with_fields(self):
        mandate = """
Some initial text that should be ignored if possible.

Scope: Compile fresh Linear mandate into bounded PRD.
Dependencies: None
Acceptance: Output feeds Jules fleet.
Evidence: PRD file created.
Exclusive Files: 10_Tech_OS/kernel/prd_compiler.py
"""
        parsed = parse_mandate(mandate)
        self.assertEqual(parsed["Scope"], "Compile fresh Linear mandate into bounded PRD.")
        self.assertEqual(parsed["Dependencies"], "None")
        self.assertEqual(parsed["Acceptance"], "Output feeds Jules fleet.")
        self.assertEqual(parsed["Evidence"], "PRD file created.")
        self.assertEqual(parsed["Exclusive Files"], "10_Tech_OS/kernel/prd_compiler.py")

    def test_parse_mandate_missing_fields(self):
        mandate = """
Just some text without proper fields.
"""
        parsed = parse_mandate(mandate)
        self.assertEqual(parsed["Scope"], "TODO: Define Scope")
        self.assertEqual(parsed["Dependencies"], "TODO: Define Dependencies")

    def test_compile_prd_enforces_owner(self):
        mandate = """
Scope: Compile fresh Linear mandate into bounded PRD.
Owner: Somebody Else
Dependencies: None
Acceptance: Output feeds Jules fleet.
Evidence: PRD file created.
Exclusive Files: 10_Tech_OS/kernel/prd_compiler.py
"""
        prd_md = compile_prd(mandate, "FOR-4", "FORGE_F0")

        self.assertIn("# Bounded PRD: FOR-4 (FORGE_F0)", prd_md)
        self.assertIn("## Owner\nPrimary Spec: Clara\nGatekeeper: Rick", prd_md)
        self.assertNotIn("Somebody Else", prd_md)
        self.assertIn("## Scope\nCompile fresh Linear mandate into bounded PRD.", prd_md)

if __name__ == "__main__":
    unittest.main()

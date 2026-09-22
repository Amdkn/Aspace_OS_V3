#!/usr/bin/env python3
"""test_prd_compiler.py — Tests pour prd_compiler.py."""

import unittest
from pathlib import Path
import tempfile
import sys
import os

# Add kernel to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from prd_compiler import parse_mandate, generate_prd

class TestPrdCompiler(unittest.TestCase):
    def test_parse_mandate_headers(self):
        raw = """
## Scope
This is the scope.

## Dependencies
Dep1, Dep2

## Acceptance
- Test 1
- Test 2

## Evidence
Screenshot.png

## Exclusive Files
test.py
"""
        sections = parse_mandate(raw)
        self.assertEqual(sections["Scope"], "This is the scope.")
        self.assertEqual(sections["Dependencies"], "Dep1, Dep2")
        self.assertEqual(sections["Acceptance"], "- Test 1\n- Test 2")
        self.assertEqual(sections["Evidence"], "Screenshot.png")
        self.assertEqual(sections["Exclusive Files"], "test.py")

    def test_parse_mandate_inline(self):
        raw = """
**Scope:** Inline scope text.
**Dependencies:** no deps
"""
        sections = parse_mandate(raw)
        self.assertEqual(sections["Scope"], "Inline scope text.")
        self.assertEqual(sections["Dependencies"], "no deps")
        self.assertEqual(sections["Acceptance"], "")

    def test_parse_mandate_unstructured(self):
        raw = "Just a single block of text."
        sections = parse_mandate(raw)
        self.assertEqual(sections["Scope"], "Just a single block of text.")
        self.assertEqual(sections["Dependencies"], "")

    def test_generate_prd_owner(self):
        sections = {"Scope": "A scope"}
        prd = generate_prd("TEST-1", sections)
        self.assertIn("## Owner\nClara (Primary Spec) / Rick (Mechanism Gatekeeper)", prd)
        self.assertIn("## Scope\nA scope", prd)
        self.assertIn("## Dependencies\nNone specified.", prd)

if __name__ == '__main__':
    unittest.main()

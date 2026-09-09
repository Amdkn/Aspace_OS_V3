#!/usr/bin/env python3
"""
A'Space OS V3 — Engram Unit Test Suite
Suite de tests unitaires automatisée pour EngramPhraseBook et BethFilter.
"""

import sys
import unittest
from pathlib import Path

# Chargement dynamique sécurisé pour répertoires nommés avec des chiffres
sys.path.insert(0, str(Path(__file__).parent))

from engram_loader import EngramPhraseBook
from beth_filter import BethFilter


class TestEngramPhraseBook(unittest.TestCase):
    def setUp(self):
        self.phrasebook = EngramPhraseBook()

    def test_resolve_ld01_sob(self):
        tokens = ["Analyse", "du", "projet", "self", "operating", "business", "en", "cours"]
        match = self.phrasebook.resolve(tokens)
        self.assertIsNotNone(match)
        self.assertEqual(match["matched_key"], "LD01_SOB")
        self.assertEqual(match["dimension"], "7D")
        self.assertEqual(match["resolution_type"], "ONTOLOGY_POINTER")

    def test_resolve_13th_doctor(self):
        tokens = ["Appel", "du", "treizieme", "docteur", "kernel", "pour", "dispatch"]
        match = self.phrasebook.resolve(tokens)
        self.assertIsNotNone(match)
        self.assertEqual(match["matched_key"], "13TH_DOCTOR_KERNEL")
        self.assertEqual(match["dimension"], "5D")

    def test_resolve_no_match(self):
        tokens = ["Bonjour", "ceci", "est", "un", "message", "standard"]
        match = self.phrasebook.resolve(tokens)
        self.assertIsNone(match)


class TestBethFilter(unittest.TestCase):
    def setUp(self):
        self.filter = BethFilter()

    def test_evaluate_circuit_breaker_veto(self):
        intent = "Demande urgente os hyoide resilience suite surcharge queue"
        result = self.filter.evaluate_intent(intent)
        self.assertFalse(result["allowed"])
        self.assertTrue(result["veto"])
        self.assertEqual(result["matched_key"], "OS_HYOIDE_BUFFER")
        self.assertEqual(result["action"], "DISSIPATE_ASYNC_QUEUE")

    def test_evaluate_definition_of_done(self):
        intent = "Contrôle de la definition of done avant livraison"
        result = self.filter.evaluate_intent(intent)
        self.assertTrue(result["allowed"])
        self.assertFalse(result["veto"])
        self.assertEqual(result["matched_key"], "DOD_BINARY_GATE")
        self.assertIn("tsc_no_emit_0", result["required_rules"])

    def test_evaluate_standard_intent(self):
        intent = "Exécuter une tâche de routine sans invariant"
        result = self.filter.evaluate_intent(intent)
        self.assertTrue(result["allowed"])
        self.assertFalse(result["veto"])
        self.assertIsNone(result["matched_key"])


if __name__ == "__main__":
    unittest.main()

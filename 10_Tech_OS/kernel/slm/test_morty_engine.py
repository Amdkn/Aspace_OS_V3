#!/usr/bin/env python3
"""
test_morty_engine.py — Tests unitaires déterministes pour Morty Local Engine & Marin Extractor.
"""
import unittest
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from marin_dataset_extractor import extract_okf_concepts, extract_rdf_triplets, compile_marin_dataset
from morty_engine import MortyLocalEngine


class TestMortyLocalEngine(unittest.TestCase):

    def setUp(self):
        self.engine = MortyLocalEngine()

    def test_01_prediction_horizon(self):
        series = [10.0, 11.0, 12.0, 13.0, 14.0]
        res = self.engine.predict_horizon(series, horizon=14)
        self.assertEqual(res["horizon"], 14)
        self.assertEqual(len(res["predictions"]), 14)
        self.assertGreater(res["confidence"], 0.0)
        self.assertIn("backend", res)

    def test_02_decision_evaluation(self):
        # Contexte normal
        ctx_ok = {"intent": "build task", "energy": 0.8, "urgency": 0.5}
        eval_ok = self.engine.evaluate_decision(ctx_ok)
        self.assertTrue(eval_ok["allowed"])
        self.assertFalse(eval_ok["veto"])

        # Contexte surcharge
        ctx_burnout = {"intent": "urgent push", "energy": 0.1, "urgency": 0.9}
        eval_burnout = self.engine.evaluate_decision(ctx_burnout)
        self.assertFalse(eval_burnout["allowed"])
        self.assertTrue(eval_burnout["veto"])

    def test_03_marin_extractor(self):
        concepts = extract_okf_concepts()
        self.assertIsInstance(concepts, list)
        triplets = extract_rdf_triplets()
        self.assertIsInstance(triplets, list)


if __name__ == "__main__":
    unittest.main()

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

    def test_04_evaluate_decision_okf(self):
        # Contexte lié au canon (en supposant que 'engram' ou 'pyramide' sont dans OKF)
        ctx_canon = {"intent": "update engram index with pyramide levels", "energy": 0.9, "urgency": 0.5}
        eval_canon = self.engine.evaluate_decision(ctx_canon)
        self.assertIn("canonical_alignment_index", eval_canon)
        self.assertGreater(eval_canon["canonical_alignment_index"], 0.0)
        
        # Contexte hors canon
        ctx_hors_canon = {"intent": "do some random stuff completely unrelated", "energy": 0.9, "urgency": 0.5}
        eval_hors_canon = self.engine.evaluate_decision(ctx_hors_canon)
        self.assertEqual(eval_hors_canon["canonical_alignment_index"], 0.0)
        self.assertGreater(len(eval_hors_canon["missing_concepts"]), 0)
        self.assertIn("OUT_OF_CANON_INTENT", eval_hors_canon["violated_concepts"])

    def test_05_predict_horizon_onnx_fallback(self):
        # Setup engine with fake ONNX path
        fake_path = Path("fake_model.onnx")
        engine_fake_onnx = MortyLocalEngine(model_path=fake_path)
        
        series = [5.0, 6.0, 7.0]
        # Devrait fallback proprement sans crash
        res = engine_fake_onnx.predict_horizon(series, horizon=3)
        self.assertEqual(res["backend"], "cpu_deterministic_fallback")
        self.assertEqual(len(res["predictions"]), 3)


if __name__ == "__main__":
    unittest.main()

import json
import unittest
from copy import deepcopy
from pathlib import Path

from inter_fabric import (
    InterFabricInvariantError,
    translated_copy,
    validate_envelope,
    validate_translation,
)

HERE = Path(__file__).resolve().parent
EXAMPLE = HERE / "INTER_FABRIC_ENVELOPE_V1.example.json"


class TestInterFabricEnvelope(unittest.TestCase):
    def setUp(self):
        with EXAMPLE.open("r", encoding="utf-8") as handle:
            self.source = json.load(handle)

    def test_example_validates(self):
        validate_envelope(self.source)

    def test_translation_preserves_coordinates(self):
        target = translated_copy(
            self.source,
            "evidence:runtime-observation-001",
            "ObservationPacket",
        )
        self.assertEqual(
            target["mission"]["correlation_id"],
            self.source["mission"]["correlation_id"],
        )
        self.assertEqual(target["routing"]["return_to"], "github:#471")

    def test_authority_widening_fails_closed(self):
        target = deepcopy(self.source)
        target["authority"]["authority_scope"].append("write:machine")
        with self.assertRaises(InterFabricInvariantError):
            validate_translation(self.source, target)

    def test_unknown_coercion_is_rejected(self):
        target = deepcopy(self.source)
        target["truth"]["epistemic_state"] = "KNOWN"
        target["truth"]["freshness"] = "FRESH"
        with self.assertRaises(InterFabricInvariantError):
            validate_translation(self.source, target)

    def test_evidence_loss_is_rejected(self):
        target = deepcopy(self.source)
        target["truth"]["evidence_refs"] = []
        with self.assertRaises(InterFabricInvariantError):
            validate_translation(self.source, target)

    def test_return_to_loss_is_rejected(self):
        target = deepcopy(self.source)
        target["routing"]["return_to"] = "github:#333"
        with self.assertRaises(InterFabricInvariantError):
            validate_translation(self.source, target)


if __name__ == "__main__":
    unittest.main()

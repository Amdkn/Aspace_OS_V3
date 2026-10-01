import unittest

from validate_forge_contract import MARKER, SECTIONS, validate


def complete_body() -> str:
    parts = [MARKER]
    for section in SECTIONS:
        parts.append(f"## {section}\nEvidence for {section}.")
    return "\n\n".join(parts)


class ForgeContinuityContractTests(unittest.TestCase):
    def test_complete_contract_passes(self):
        self.assertEqual(validate(complete_body(), strict=True), [])

    def test_missing_marker_fails_when_strict(self):
        self.assertIn("missing marker", validate("## Mission / return-to\n#283", strict=True)[0])

    def test_empty_section_fails(self):
        body = complete_body().replace(
            "Evidence for Test / evidence.", "<!-- placeholder only -->"
        )
        self.assertIn("section has no evidence: Test / evidence", validate(body, strict=True))

    def test_unmarked_non_forge_pr_is_not_globally_blocked(self):
        self.assertEqual(validate("ordinary bounded product PR", strict=False), [])

    def test_contract_is_capability_based_not_sequential(self):
        body = complete_body()
        self.assertNotIn("Discovery (Bill)", SECTIONS)
        self.assertNotIn("Design / Compile (Clara)", SECTIONS)
        self.assertEqual(validate(body, strict=True), [])


if __name__ == "__main__":
    unittest.main()

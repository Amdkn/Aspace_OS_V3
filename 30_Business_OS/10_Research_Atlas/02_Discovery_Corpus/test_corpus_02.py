import os
import unittest
import json

CORPUS_DIR = "30_Business_OS/10_Research_Atlas/02_Discovery_Corpus/corpus_02_software_factory"

class TestCorpus02(unittest.TestCase):

    def test_01_all_nine_sources_present(self):
        expected_files = [
            "source_01_fable_wargames.md",
            "source_02_best_ai_coding_config.md",
            "source_03_dark_factory.md",
            "source_04_ai_sdlc_workshop.md",
            "source_05_ai_software_factories.md",
            "source_06_security_deterministic_gates.md",
            "source_07_gpt6_astra_remote_factory.md",
            "source_08_super_simple_factory.md",
            "source_09_github_swarm_factory.md",
        ]
        for fname in expected_files:
            fpath = os.path.join(CORPUS_DIR, fname)
            self.assertTrue(os.path.exists(fpath), f"Missing source file: {fname}")
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
                self.assertIn("## SourceClaim", content)
                self.assertIn("## Supporting evidence", content)
                self.assertIn("## Contradictions / limits", content)
                self.assertIn("## A'Space adaptation candidate", content)
                self.assertIn("## Anti-pattern / risk", content)
                self.assertIn("## Impacted holons", content)
                self.assertIn("## Candidate contract/ADR", content)
                self.assertIn("## Required test/canary", content)
                self.assertIn("## Confidence", content)
                self.assertIn("## Provenance refs", content)

    def test_02_fable_wargame_kit_zipped_source_exists(self):
        zip_path = "20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Wargames/Fable_Wargame_Kit/fable_wargame_kit_source.zip"
        self.assertTrue(os.path.exists(zip_path), "Fable wargame kit zip file missing!")

    def test_03_cross_source_synthesis_content(self):
        synth_path = os.path.join(CORPUS_DIR, "CORPUS_02_SYNTHESIS.md")
        self.assertTrue(os.path.exists(synth_path), "CORPUS_02_SYNTHESIS.md missing!")
        with open(synth_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Check at least 5 convergences
        self.assertIn("Convergence 1:", content)
        self.assertIn("Convergence 2:", content)
        self.assertIn("Convergence 3:", content)
        self.assertIn("Convergence 4:", content)
        self.assertIn("Convergence 5:", content)

        # Check at least 3 contradictions
        self.assertIn("Contradiction 1:", content)
        self.assertIn("Contradiction 2:", content)
        self.assertIn("Contradiction 3:", content)

        # Check Factory / Flow boundary
        self.assertIn("CLARA (S3 Design / Forge)", content)
        self.assertIn("RYAN (S3 Build / Industrialization)", content)
        self.assertIn("RIVER (S3 Flow / Operations)", content)

        # Check Anti-simplification rules
        self.assertIn("Ryan ≠ builder worker", content)
        self.assertIn("Yaz ≠ monitoring agent", content)
        self.assertIn("Graham ≠ memory database", content)
        self.assertIn("River ≠ workflow automation", content)

        # Check Lineage map
        self.assertIn("SourcePattern -> RuntimePrimitive -> HolonImpact -> CandidateCapability -> ValidationNeed", content)

if __name__ == "__main__":
    unittest.main()

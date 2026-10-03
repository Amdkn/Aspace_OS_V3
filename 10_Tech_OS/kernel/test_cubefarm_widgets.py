import unittest
from cubefarm_widgets import CubeFarmBrowserWidget, BrowserEvidenceState

class TestCubeFarmWidgets(unittest.TestCase):
    def test_render_and_append_evidence(self):
        widget = CubeFarmBrowserWidget("wid-123")
        widget.render_surface_state("sess-1", "chatgpt_web", "test_actor", True)

        res = widget.append_evidence("sess-1", {"action": "test", "result": "ok"})
        self.assertEqual(res["status"], "SUCCESS")
        self.assertEqual(res["evidence_count"], 1)

        tree = widget.get_display_tree("sess-1")
        self.assertIsNotNone(tree)
        self.assertEqual(tree["auth_indicator"], "GREEN")
        self.assertEqual(len(tree["timeline"]), 1)

    def test_append_evidence_no_session(self):
        widget = CubeFarmBrowserWidget("wid-123")
        res = widget.append_evidence("invalid-sess", {"action": "test"})
        self.assertEqual(res["status"], "FAILED")

if __name__ == "__main__":
    unittest.main()

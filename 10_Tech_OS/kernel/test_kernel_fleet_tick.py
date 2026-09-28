import unittest
from unittest.mock import patch
import kernel_fleet_tick as k

class TickTests(unittest.TestCase):
    def test_kernel_mapping(self):
        pole, prd = k.classify({"identifier":"KER-19","title":"x"})
        self.assertEqual((pole,prd),("K2_SYSTEM1_DECISION","KPRD-020"))

    def test_forge_mapping(self):
        pole, prd = k.classify({"identifier":"FOR-4","title":"[FPRD-001][F0] test"})
        self.assertEqual((pole,prd),("FORGE_F0","FPRD-001"))

    def test_life_mapping(self):
        pole, prd = k.classify({"identifier":"KER-28","title":"[LPRD-001][L0] test"})
        self.assertEqual((pole,prd),("LIFE_L0","LPRD-001"))

    def test_duplicate_detects_issue(self):
        active=[{"title":"ASPACE:X | KPRD-020 | KER-19","prompt":"","state":"IN_PROGRESS"}]
        self.assertTrue(k.duplicate(active,"KER-19"))
        self.assertFalse(k.duplicate(active,"KER-20"))

    def test_terminal_session_is_not_reusable(self):
        self.assertIsNone(k.reusable_session("KER-19"))

    def test_companion_lane_caps(self):
        self.assertEqual(k.MAX_ACTIVE,9)
        self.assertEqual(k.CORE_LIMITS["KERNEL"],3)
        self.assertEqual(k.CORE_LIMITS["LIFE"],3)
        self.assertEqual(k.CORE_LIMITS["BUSINESS"],3)

    def test_core_classifier(self):
        self.assertEqual(k.core_for("KERNEL_K0"),"KERNEL")
        self.assertEqual(k.core_for("LIFE_L0"),"LIFE")
        self.assertEqual(k.core_for("FORGE_F0"),"BUSINESS")

    def test_companion_routing(self):
        self.assertEqual(k.companion_for({"title":"implement runtime adapter","description":""},"KERNEL_K2"),"RYAN")
        self.assertEqual(k.companion_for({"title":"write ADR policy","description":""},"LIFE_L1"),"AMY")
        self.assertEqual(k.companion_for({"title":"artifact registry evidence","description":""},"FORGE_F4"),"BILL")

    def test_active_companion_session(self):
        xs=[
            {"id":"1","title":"ASPACE:KERNEL | RYAN | BUILD | KER-1"},
            {"id":"2","title":"ASPACE:KERNEL | RYAN | BUILD | KER-2"},
        ]
        self.assertEqual(k.active_companion_session(xs,"RYAN")["id"],"1")
        self.assertEqual(len(k.active_companion_sessions(xs,"RYAN")),2)
        self.assertIsNone(k.active_companion_session(xs,"YAZ"))

    def test_project_fallback_removes_prd_tag_gate(self):
        self.assertEqual(
            k.classify({"identifier":"SOH-999","title":"untagged life work","_project_name":"Tech OS — Life Core"}),
            ("LIFE_GENERAL","AUTO-SOH-999"),
        )
        self.assertEqual(
            k.classify({"identifier":"SOB-999","title":"untagged business work","_project_name":"Tech OS — Buzz Core"}),
            ("FORGE_GENERAL","AUTO-SOB-999"),
        )

    def test_canceled_blocker_does_not_freeze_descendant(self):
        issue={"identifier":"SOH-999","title":"work","_project_name":"Tech OS — Life Core","state":{"type":"backlog"}}
        with patch.object(k,"context",return_value={"relations":[{"relationship":"blockedBy","relatedIssue":{"identifier":"SOH-OLD"}}]}),              patch.object(k,"status_of",return_value="canceled"):
            self.assertTrue(k.is_ready(issue))

    def test_live_blocker_still_blocks(self):
        issue={"identifier":"SOH-999","title":"work","_project_name":"Tech OS — Life Core","state":{"type":"backlog"}}
        with patch.object(k,"context",return_value={"relations":[{"relationship":"blockedBy","relatedIssue":{"identifier":"SOH-LIVE"}}]}),              patch.object(k,"status_of",return_value="started"):
            self.assertFalse(k.is_ready(issue))

    def test_only_explicit_marker_opts_out(self):
        issue={"identifier":"SOH-999","title":"[BEDROCK] still valid work","_project_name":"Tech OS — Life Core","state":{"type":"backlog"}}
        with patch.object(k,"context",return_value={"relations":[]}):
            self.assertTrue(k.is_ready(issue))
        issue["title"]="[NO_AUTODISPATCH] deliberately manual"
        self.assertFalse(k.is_ready(issue))

if __name__=="__main__":
    unittest.main()

import unittest
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
        active=[{"title":"ASPACE:X | KPRD-020 | KER-19","prompt":"Work_id: 123","state":"IN_PROGRESS"}]
        self.assertTrue(k.duplicate(active,"KER-19"))
        self.assertTrue(k.duplicate(active,"KER-20","123"))
        self.assertFalse(k.duplicate(active,"KER-20","124"))

    def test_terminal_session_is_not_reusable(self):
        self.assertIsNone(k.reusable_session("KER-19"))

    def test_companion_lane_caps(self):
        self.assertEqual(k.MAX_ACTIVE,15)
        self.assertEqual(k.CORE_LIMITS["KERNEL"],5)
        self.assertEqual(k.CORE_LIMITS["LIFE"],5)
        self.assertEqual(k.CORE_LIMITS["BUSINESS"],5)

    def test_core_classifier(self):
        self.assertEqual(k.core_for("KERNEL_K0"),"KERNEL")
        self.assertEqual(k.core_for("LIFE_L0"),"LIFE")
        self.assertEqual(k.core_for("FORGE_F0"),"BUSINESS")

    def test_companion_routing(self):
        self.assertEqual(k.companion_for({"title":"implement runtime adapter","description":""},"KERNEL_K2"),"RYAN")
        self.assertEqual(k.companion_for({"title":"write ADR policy","description":""},"LIFE_L1"),"AMY")
        self.assertEqual(k.companion_for({"title":"artifact registry evidence","description":""},"FORGE_F4"),"BILL")

    def test_active_companion_session(self):
        xs=[{"id":"1","title":"ASPACE:KERNEL | RYAN | BUILD"}]
        self.assertEqual(k.active_companion_session(xs,"RYAN")["id"],"1")
        self.assertIsNone(k.active_companion_session(xs,"YAZ"))

if __name__=="__main__":
    unittest.main()

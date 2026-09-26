import unittest
from capacity_policy import can_allocate

class CapacityPolicyTests(unittest.TestCase):
    def setUp(self):
        self.policy = {
            "max_active": 9,
            "core_limits": {
                "KERNEL": 3,
                "LIFE": 3,
                "BUSINESS": 3
            },
            "core_reservations": {
                "KERNEL": 1,
                "LIFE": 1,
                "BUSINESS": 1
            }
        }

    def test_can_allocate_empty(self):
        # Empty allocation, requested core is KERNEL
        counts = {"KERNEL": 0, "LIFE": 0, "BUSINESS": 0}
        self.assertTrue(can_allocate(self.policy, counts, "KERNEL"))

    def test_bounded_concurrency(self):
        # Total active is 9, max is 9
        counts = {"KERNEL": 3, "LIFE": 3, "BUSINESS": 3}
        self.assertFalse(can_allocate(self.policy, counts, "KERNEL"))

    def test_budget_limits(self):
        # Budget for KERNEL reached, total is 3 (max 9)
        counts = {"KERNEL": 3, "LIFE": 0, "BUSINESS": 0}
        self.assertFalse(can_allocate(self.policy, counts, "KERNEL"))

        # But we can allocate for another core
        self.assertTrue(can_allocate(self.policy, counts, "LIFE"))

    def test_silent_capacity_theft_reservation(self):
        # We want to ensure that domains without any active units
        # reserve capacity and cannot be stolen by others.
        # Policy requires: max_active - current_total - 1 >= unmet_reservations

        # If LIFE and BUSINESS have 0 active, unmet is 1+1=2.
        # Max is 9. We are asking for KERNEL.
        # Max allowed for KERNEL without violating reservations:
        # current_total can go up to 9 - 1 (for current req) - 2 (unmet) = 6
        # Wait, if current KERNEL is 6, current_total=6.
        # 9 - 6 - 1 = 2 >= 2 -> True
        # If current KERNEL is 7, current_total=7.
        # 9 - 7 - 1 = 1 >= 2 -> False

        # However, KERNEL is also limited by core_limits (3).
        # Let's adjust policy dynamically to test just the theft logic.
        policy = {
            "max_active": 5,
            "core_limits": {"A": 5, "B": 5, "C": 5},
            "core_reservations": {"A": 1, "B": 1, "C": 1}
        }

        # All 0. Ask A.
        # unmet = 2 (for B, C). max=5. 5 - 0 - 1 = 4 >= 2 -> True
        counts = {"A": 0, "B": 0, "C": 0}
        self.assertTrue(can_allocate(policy, counts, "A"))

        # Ask A, but A already has 2. Total = 2.
        # unmet = 2. 5 - 2 - 1 = 2 >= 2 -> True
        counts = {"A": 2, "B": 0, "C": 0}
        self.assertTrue(can_allocate(policy, counts, "A"))

        # Ask A, A has 3. Total = 3.
        # unmet = 2. 5 - 3 - 1 = 1 >= 2 -> False
        counts = {"A": 3, "B": 0, "C": 0}
        self.assertFalse(can_allocate(policy, counts, "A"))

        # Now suppose B has 1. Ask A.
        # unmet = 1 (for C). A has 3, B has 1. Total = 4.
        # 5 - 4 - 1 = 0 >= 1 -> False
        counts = {"A": 3, "B": 1, "C": 0}
        self.assertFalse(can_allocate(policy, counts, "A"))

        # But if we ask C, total = 4. unmet (for A and B) = 0.
        # 5 - 4 - 1 = 0 >= 0 -> True
        self.assertTrue(can_allocate(policy, counts, "C"))

if __name__ == "__main__":
    unittest.main()

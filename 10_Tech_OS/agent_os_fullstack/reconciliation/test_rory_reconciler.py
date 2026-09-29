import unittest
from datetime import datetime, timezone, timedelta
from agent_os_fullstack.api.projection_gateway import ReconciliationClassification, ReconciliationDecision, SourceFingerprint, NestedSourceFingerprint
from agent_os_fullstack.reconciliation.rory_reconciler import classify_divergence

class TestRoryReconciler(unittest.TestCase):
    def test_consistent(self):
        now = datetime.now(timezone.utc).isoformat()
        local = {"updated_at": now, "status": "pending"}
        cloud = {"updated_at": now, "status": "pending"}
        receipt = classify_divergence(local, cloud, None, "1")
        self.assertEqual(receipt.classification, ReconciliationClassification.CONSISTENT)

    def test_local_newer(self):
        now = datetime.now(timezone.utc)
        past = (now - timedelta(minutes=5)).isoformat()
        local = {"updated_at": now.isoformat()}
        cloud = {"updated_at": past}
        receipt = classify_divergence(local, cloud, None, "1")
        self.assertEqual(receipt.classification, ReconciliationClassification.LOCAL_NEWER)
        self.assertEqual(receipt.decision, ReconciliationDecision.RETRY_SYNC)

    def test_cloud_newer(self):
        now = datetime.now(timezone.utc)
        future = (now + timedelta(minutes=5)).isoformat()
        local = {"updated_at": now.isoformat()}
        cloud = {"updated_at": future}
        receipt = classify_divergence(local, cloud, None, "1")
        self.assertEqual(receipt.classification, ReconciliationClassification.CLOUD_NEWER_BUT_NONAUTHORITATIVE)

    def test_stale_binding(self):
        now = datetime.now(timezone.utc).isoformat()
        local = {"updated_at": now, "status": "done"}
        cloud = {"updated_at": now, "status": "active"}
        receipt = classify_divergence(local, cloud, None, "1")
        self.assertEqual(receipt.classification, ReconciliationClassification.STALE_BINDING)
        self.assertEqual(receipt.decision, ReconciliationDecision.ACCEPT_LOCAL)

    def test_source_drift(self):
        fp = SourceFingerprint(parent_dirty=True)
        receipt = classify_divergence(None, None, fp, "1")
        self.assertEqual(receipt.classification, ReconciliationClassification.SOURCE_DRIFT)

if __name__ == '__main__':
    unittest.main()

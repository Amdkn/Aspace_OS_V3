import unittest
from agent_os_fullstack.sync.supabase_sync_adapter import SupabaseSyncAdapter

class TestSupabaseSyncAdapter(unittest.TestCase):
    def test_queue_and_flush(self):
        adapter = SupabaseSyncAdapter()
        event_id = adapter.queue_event("UPDATE", {"work_id": 1})

        self.assertEqual(len(adapter.outbox), 1)
        self.assertEqual(adapter.outbox[0]["event_id"], event_id)

        receipts = adapter.flush_outbox()
        self.assertEqual(len(receipts), 1)
        self.assertTrue(receipts[0].success)
        self.assertEqual(len(adapter.outbox), 0)

if __name__ == '__main__':
    unittest.main()

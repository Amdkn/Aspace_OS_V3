import unittest
import os
import shutil
from pathlib import Path
from harvester import ChannelHarvester

class TestChannelHarvester(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path("test_harvester_output")
        self.test_dir.mkdir(parents=True, exist_ok=True)
        self.mock_takeout_1 = self.test_dir / "Takeout1"
        self.mock_takeout_2 = self.test_dir / "Takeout2"
        self.mock_takeout_1.mkdir(exist_ok=True)
        self.mock_takeout_2.mkdir(exist_ok=True)

        # Snapshot 1
        with open(self.mock_takeout_1 / "watch-history.html", "w") as f:
            f.write('<div class="content-cell"><a href="https://www.youtube.com/watch?v=vid1">Video 1</a><br><a href="https://www.youtube.com/channel/chanA">Channel A</a><br>Jun 25, 2026, 11:34:00 AM EDT</div>\n')
            f.write('<div class="content-cell"><a href="https://www.youtube.com/watch?v=vid2">Video 2</a><br><a href="https://www.youtube.com/channel/chanA">Channel A</a><br>Jun 26, 2026, 11:34:00 AM EDT</div>\n')

        with open(self.mock_takeout_1 / "subscriptions.csv", "w") as f:
            f.write("chanA,https://youtube.com/channel/chanA,Channel A\n")

        # Snapshot 2 (overlaps with Snapshot 1 to test deduplication)
        with open(self.mock_takeout_2 / "watch-history.html", "w") as f:
            f.write('<div class="content-cell"><a href="https://www.youtube.com/watch?v=vid1">Video 1</a><br><a href="https://www.youtube.com/channel/chanA">Channel A</a><br>Jun 25, 2026, 11:34:00 AM EDT</div>\n')
            f.write('<div class="content-cell"><a href="https://www.youtube.com/watch?v=vid3">Video 3</a><br><a href="https://www.youtube.com/channel/chanB">Channel B</a><br>Jun 27, 2026, 11:34:00 AM EDT</div>\n')

        os.environ["MOCK_YTDLP"] = "1"

    def tearDown(self):
        shutil.rmtree(self.test_dir)
        if "MOCK_YTDLP" in os.environ:
            del os.environ["MOCK_YTDLP"]

    def test_harvester_pipeline(self):
        harvester = ChannelHarvester(out_dir=str(self.test_dir / "out"))

        # H0
        harvester.h0_immutable_inventory([str(self.mock_takeout_1), str(self.mock_takeout_2)])
        self.assertEqual(len(harvester.snapshots), 2)
        self.assertEqual(harvester.snapshots[0]["family"], "YouTube")

        # H1
        harvester.h1_canonical_graph()
        # vid1 should be deduplicated (appears in both takeouts)
        self.assertEqual(len(harvester.canonical_graph), 3)
        self.assertIn("vid1", harvester.canonical_graph)
        self.assertIn("vid2", harvester.canonical_graph)
        self.assertIn("vid3", harvester.canonical_graph)

        # Test sub parsing
        self.assertIn("chanA", harvester.subscriptions)
        self.assertNotIn("chanB", harvester.subscriptions)

        # H2
        harvester.h2_channel_recurrence()
        self.assertEqual(len(harvester.channel_recurrence), 2)

        chanA = harvester.channel_recurrence["chanA"]
        self.assertEqual(chanA.watched_count, 2)
        self.assertTrue(chanA.subscribed)
        self.assertEqual(chanA.return_frequency, 1)

        chanB = harvester.channel_recurrence["chanB"]
        self.assertEqual(chanB.watched_count, 1)
        self.assertFalse(chanB.subscribed)
        self.assertEqual(chanB.return_frequency, 0)

        # H3
        harvester.promoted_channels = ["chanA"]
        harvester.h3_research_expansion(harvester.promoted_channels)

        # Verify H3 outputs
        import json
        with open(self.test_dir / "out" / "h3_expansion.json", "r") as f:
            expansion = json.load(f)

        self.assertEqual(len(expansion), 1)
        self.assertEqual(expansion[0]["channel_id"], "chanA")
        self.assertEqual(expansion[0]["unseen_count"], 1) # from our mock
        self.assertEqual(len(expansion[0]["routed_to_watch_s1"]), 1)

        # H4 / Report
        report = harvester.generate_report()
        self.assertEqual(report["h1_canonical_videos"], 3)
        self.assertEqual(report["h4_future_monitoring_design"]["strategy"], "cron_monitor")

if __name__ == '__main__':
    unittest.main()

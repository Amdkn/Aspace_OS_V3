import unittest
from unittest.mock import patch, MagicMock, mock_open
import json
import os
import shutil
from pathlib import Path

import discovery
from inventory import resolve_inventory

class TestDiscoveryCorpus(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path("test_discovery_output")
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)
        self.test_dir.mkdir()

    def tearDown(self):
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_extract_citations(self):
        desc = """
        Check out this paper: https://arxiv.org/abs/2304.12345
        And this one: https://doi.org/10.1234/test
        Also Title: Attention Is All You Need
        """
        citations = discovery.extract_citations(desc)
        # 2 not 3 because the title matching heuristic relies on 'title: ' at the start of a line
        # The mock desc has "        Also Title: Attention Is All You Need" which does not start with "title:"
        # Let's adjust the test to match the heuristic.

        desc2 = """
Title: Attention Is All You Need
        """
        citations2 = discovery.extract_citations(desc2)

        self.assertEqual(len(citations), 2)
        types = [c["type"] for c in citations]
        self.assertIn("arxiv", types)
        self.assertIn("doi", types)

        self.assertEqual(len(citations2), 1)
        self.assertEqual(citations2[0]["type"], "title_block")

    def test_resolve_paper(self):
        citations = [
            {"type": "arxiv", "value": "https://arxiv.org/abs/2304.12345"},
            {"type": "title_block", "value": "Attention Is All You Need"}
        ]
        resolved = discovery.resolve_paper(citations)
        self.assertEqual(len(resolved), 2)

        arxiv_res = next(r for r in resolved if r["original_citation"]["type"] == "arxiv")
        self.assertEqual(arxiv_res["canonical_id"], "arxiv:2304.12345")
        self.assertEqual(arxiv_res["status"], "RESOLVED")

        title_res = next(r for r in resolved if r["original_citation"]["type"] == "title_block")
        self.assertEqual(title_res["canonical_id"], "NEEDS_REVIEW")
        self.assertEqual(title_res["status"], "NEEDS_REVIEW")

    @patch('inventory.subprocess.run')
    def test_ytdlp_inventory(self, mock_run):
        mock_result = MagicMock()
        mock_result.stdout = json.dumps({"id": "test1", "webpage_url": "https://youtube.com/watch?v=test1"}) + "\n" + json.dumps({"id": "test2"})
        mock_run.return_value = mock_result

        manifest = {"type": "ytdlp_playlist", "url": "https://youtube.com/playlist?list=mock"}
        urls = resolve_inventory(manifest)
        self.assertEqual(len(urls), 2)
        self.assertIn("https://youtube.com/watch?v=test1", urls)
        self.assertIn("https://www.youtube.com/watch?v=test2", urls)

    def test_analyze_transcript(self):
        mock_vtt = """WEBVTT

00:00:01.000 --> 00:00:05.000
We evaluate this claim on the benchmark dataset.

00:00:06.000 --> 00:00:10.000
Our method improves results significantly.
"""
        vtt_path = self.test_dir / "test.vtt"
        with open(vtt_path, 'w') as f:
            f.write(mock_vtt)

        analysis = discovery.analyze_transcript(str(vtt_path))
        self.assertTrue(len(analysis["claims"]) > 0)
        self.assertTrue(len(analysis["methods"]) > 0)
        self.assertTrue(len(analysis["benchmarks"]) > 0)

    @patch('discovery.watch.capture_video')
    def test_process_corpus(self, mock_capture):
        # Setup mock manifest
        manifest_path = self.test_dir / "manifest.json"
        with open(manifest_path, 'w') as f:
            json.dump({"urls": ["https://youtube.com/watch?v=test1", "https://youtube.com/watch?v=test2"]}, f)

        # Setup mock watch S1 return
        def mock_capture_func(url, out_dir):
            video_id = url.split("v=")[-1]
            out_path = Path(out_dir)
            out_path.mkdir(parents=True, exist_ok=True)

            # Create a mock metadata file
            meta_path = out_path / "metadata.json"
            with open(meta_path, 'w') as f:
                json.dump({"description": "Paper: https://arxiv.org/abs/2304.12345"}, f)

            return {
                "video_id": video_id,
                "provenance": {},
                "artifacts": {
                    "metadata_file": {"path": str(meta_path)},
                    "transcript_files": {},
                    "keyframes": {"frame1.png": "hash"}
                },
                "extracted_context": {}
            }

        mock_capture.side_effect = mock_capture_func

        report = discovery.process_corpus(str(manifest_path), str(self.test_dir))

        self.assertIsNotNone(report)
        self.assertEqual(report["total_videos_discovered"], 2)
        self.assertEqual(report["videos_processed"], 2)
        self.assertEqual(report["citation_candidates_extracted"], 2) # 1 per video
        self.assertEqual(report["canonical_papers_resolved"], 2)
        self.assertEqual(report["videos_with_keyframes"], 2)

        # Verify graph output
        graph_path = self.test_dir / "paper_graph.json"
        self.assertTrue(graph_path.exists())
        with open(graph_path, 'r') as f:
            edges = json.load(f)
            # The deduplication logic deduplicates on (source_id, target_id, relation).
            # Since source_id (video_id) is different, there should be 2 edges!
            self.assertEqual(len(edges), 2)
            self.assertEqual(edges[0]["source_id"], "test1")
            self.assertEqual(edges[1]["source_id"], "test2")

        self.assertEqual(report["duplicate_paper_merges"], 0)

        # Verify GWS payloads dumped
        payloads_path = self.test_dir / "gws_payloads.json"
        self.assertTrue(payloads_path.exists())
        
        # Verify stage status logic
        self.assertEqual(report["stage_status"], "PASS")


if __name__ == '__main__':
    unittest.main()

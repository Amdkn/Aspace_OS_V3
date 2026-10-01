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
        desc2 = "Title: Attention Is All You Need"
        citations2 = discovery.extract_citations(desc2)
        self.assertEqual(len(citations2), 1)
        self.assertEqual(citations2[0]["type"], "title_block")

    @patch('inventory.subprocess.run')
    def test_ytdlp_inventory(self, mock_run):
        mock_result = MagicMock()
        mock_result.stdout = json.dumps({"id": "test1", "webpage_url": "https://youtube.com/watch?v=test1"}) + "\n" + json.dumps({"id": "test2"})
        mock_run.return_value = mock_result
        manifest = {"type": "ytdlp_playlist", "url": "https://youtube.com/playlist?list=mock"}
        urls = resolve_inventory(manifest)
        self.assertEqual(len(urls), 2)

    def test_analyze_transcript(self):
        mock_vtt = "WEBVTT\n\n00:00:01.000 --> 00:00:05.000\nWe evaluate this claim on the benchmark dataset.\n"
        vtt_path = self.test_dir / "test.vtt"
        with open(vtt_path, 'w') as f:
            f.write(mock_vtt)
        analysis = discovery.analyze_transcript(str(vtt_path))
        self.assertTrue(len(analysis["claims"]) > 0)

    @patch('discovery.subprocess.run')
    @patch('discovery.urllib.request.urlopen')
    def test_stage_resume_and_checkpoint(self, mock_urlopen, mock_sub_run):
        # Initial run: should execute M1 (subprocess.run)
        mock_result = MagicMock()
        mock_result.stdout = json.dumps({"id": "vid1", "description": "test"})
        mock_sub_run.return_value = mock_result
        
        url = "https://youtube.com/watch?v=vid1"
        out_dir = self.test_dir / "vid1"
        out_dir.mkdir()
        
        discovery.process_video(url, str(out_dir))
        
        self.assertTrue((out_dir / "state.json").exists())
        with open(out_dir / "state.json", "r") as f:
            state = json.load(f)
            self.assertIn("M1", state["completed_stages"])
            self.assertIn("M7", state["completed_stages"])
            
        call_count_before = mock_sub_run.call_count
        
        # Second run: should skip subprocess entirely because stages are complete
        discovery.process_video(url, str(out_dir))
        
        call_count_after = mock_sub_run.call_count
        self.assertEqual(call_count_before, call_count_after)

    @patch('discovery.subprocess.run')
    def test_m1_m2_no_m6_side_effects(self, mock_sub_run):
        # We'll just run M1 and M2 explicitly to see if ffmpeg is ever called.
        mock_result = MagicMock()
        mock_result.stdout = json.dumps({"id": "vid2", "description": "some text"})
        mock_sub_run.return_value = mock_result
        
        out_dir = self.test_dir / "vid2"
        out_dir.mkdir()
        
        meta = discovery.run_m1_metadata("https://youtube.com/watch?v=vid2", str(out_dir))
        self.assertIsNotNone(meta)
        
        discovery.run_m2_citations(meta, str(out_dir))
        
        # Ensure yt-dlp was called with dump-json, NOT ffmpeg
        args = mock_sub_run.call_args[0][0]
        self.assertIn("--dump-json", args)
        self.assertNotIn("ffmpeg", args)


    @patch('discovery.urllib.request.urlopen')
    def test_provider_resolution(self, mock_urlopen):
        # Setup mock response
        mock_response = MagicMock()
        mock_response.status = 200
        mock_urlopen.return_value.__enter__.return_value = mock_response

        raw_citations = [
            {"type": "arxiv", "value": "https://arxiv.org/abs/2304.12345"},
            {"type": "doi", "value": "https://doi.org/10.1234/test"},
            {"type": "title_block", "value": "Attention Is All You Need"}
        ]
        
        resolved = discovery.run_m3_canonicalize(raw_citations, str(self.test_dir))
        self.assertEqual(len(resolved), 3)

        arxiv_res = next(r for r in resolved if r["original_citation"]["type"] == "arxiv")
        self.assertEqual(arxiv_res["canonical_id"], "arxiv:2304.12345")
        self.assertEqual(arxiv_res["status"], "RESOLVED")

        doi_res = next(r for r in resolved if r["original_citation"]["type"] == "doi")
        self.assertEqual(doi_res["canonical_id"], "doi:10.1234/test")
        self.assertEqual(doi_res["status"], "RESOLVED")

        title_res = next(r for r in resolved if r["original_citation"]["type"] == "title_block")
        self.assertEqual(title_res["canonical_id"], "NEEDS_REVIEW")
        self.assertEqual(title_res["status"], "NEEDS_REVIEW")

    @patch('discovery.process_video')
    def test_paper_graph_deduplication(self, mock_process_video):
        manifest_path = self.test_dir / "manifest.json"
        with open(manifest_path, 'w') as f:
            json.dump({"urls": ["url1", "url2"]}, f)

        # Mock two videos producing identical paper graph edges
        mock_process_video.side_effect = [
            {
                "video_id": "vid1",
                "extracted_context": {"citations": []},
                "artifacts": {},
                "paper_graph_edges": [
                    {"source_id": "vid1", "target_id": "arxiv:123", "relation": "cites_in_description"}
                ]
            },
            {
                "video_id": "vid2",
                "extracted_context": {"citations": []},
                "artifacts": {},
                "paper_graph_edges": [
                    {"source_id": "vid1", "target_id": "arxiv:123", "relation": "cites_in_description"}
                ]
            }
        ]

        report = discovery.process_corpus(str(manifest_path), str(self.test_dir))
        
        # Deduplication based on source, target, relation means there should be only 1 edge in unique_edges
        with open(self.test_dir / "paper_graph.json", 'r') as f:
            unique_edges = json.load(f)
        
        self.assertEqual(len(unique_edges), 1)
        self.assertEqual(report["duplicate_paper_merges"], 1)


if __name__ == '__main__':
    unittest.main()

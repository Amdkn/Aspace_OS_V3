import unittest
from unittest.mock import patch, MagicMock, mock_open
import json
import os
import shutil
from pathlib import Path

os.environ["CI"] = "true"

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

    def test_takeout_watch_history_inventory(self):
        dummy_html = """
        <div class="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1">
          <a href="https://www.youtube.com/watch?v=kY3O-tXk4wM">Video 1</a>
          <a href="https://www.youtube.com/watch?v=kY3O-tXk4wM">Video 1 Again</a>
          <a href="https://www.youtube.com/watch?v=abcdef12345&amp;t=5s">Video 2</a>
        </div>
        """
        html_path = self.test_dir / "dummy_watch_history.html"
        with open(html_path, "w") as f:
            f.write(dummy_html)

        manifest = {"type": "takeout_watch_history", "path": str(html_path)}
        urls = resolve_inventory(manifest)
        self.assertEqual(len(urls), 2)
        self.assertIn("https://www.youtube.com/watch?v=kY3O-tXk4wM", urls)
        self.assertIn("https://www.youtube.com/watch?v=abcdef12345", urls)

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
        # return empty JSON dict to avoid json.loads error in fetch_ss_edges
        mock_response.read.return_value = b'{}'
        mock_urlopen.return_value.__enter__.return_value = mock_response

        raw_citations = [
            {"type": "arxiv", "value": "https://arxiv.org/abs/2304.12345"},
            {"type": "doi", "value": "https://doi.org/10.1234/test"},
            {"type": "title_block", "value": "Attention Is All You Need"},
            {"type": "semanticscholar", "value": "https://www.semanticscholar.org/paper/Some-Title/a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"}
        ]

        resolved = discovery.run_m3_canonicalize(raw_citations, str(self.test_dir))
        self.assertEqual(len(resolved), 4)

        arxiv_res = next(r for r in resolved if r["original_citation"]["type"] == "arxiv")
        self.assertEqual(arxiv_res["canonical_id"], "arxiv:2304.12345")
        self.assertEqual(arxiv_res["status"], "RESOLVED")

        doi_res = next(r for r in resolved if r["original_citation"]["type"] == "doi")
        self.assertEqual(doi_res["canonical_id"], "doi:10.1234/test")
        self.assertEqual(doi_res["status"], "RESOLVED")

        ss_res = next(r for r in resolved if r["original_citation"]["type"] == "semanticscholar")
        self.assertEqual(ss_res["canonical_id"], "semanticscholar:a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2")
        self.assertEqual(ss_res["status"], "RESOLVED")

        title_res = next(r for r in resolved if r["original_citation"]["type"] == "title_block")
        self.assertEqual(title_res["canonical_id"], "NEEDS_REVIEW")
        self.assertEqual(title_res["status"], "NEEDS_REVIEW")

    @patch('discovery.urllib.request.urlopen')
    def test_bounded_expansion_references(self, mock_urlopen):
        # Mock responses for canonicalization and then for SS API references/citations
        # We simulate the first call to export.arxiv.org returning 200 OK
        # The next calls to semanticscholar references/citations should return specific JSON
        def side_effect(req, *args, **kwargs):
            mock_resp = MagicMock()
            mock_resp.status = 200

            url = req.full_url
            if "export.arxiv.org" in url:
                mock_resp.read.return_value = b''
            elif "references" in url:
                mock_resp.read.return_value = json.dumps({
                    "data": [
                        {"citedPaper": {"paperId": "ref1", "externalIds": {"ArXiv": "2305.00000"}}},
                        {"citedPaper": {"paperId": "ref2", "externalIds": {"DOI": "10.000/123"}}}
                    ]
                }).encode('utf-8')
            elif "citations" in url:
                mock_resp.read.return_value = json.dumps({
                    "data": [
                        {"citingPaper": {"paperId": "cit1", "externalIds": {}}}
                    ]
                }).encode('utf-8')
            else:
                mock_resp.read.return_value = b'{}'
            return mock_resp

        # We need mock_urlopen to act as a context manager and return the mock_resp
        mock_context = MagicMock()
        mock_context.__enter__ = lambda self: side_effect(mock_urlopen.call_args[0][0])
        mock_context.__exit__ = lambda self, *args: None

        mock_urlopen.side_effect = lambda req, **kwargs: mock_context

        raw_citations = [{"type": "arxiv", "value": "https://arxiv.org/abs/2304.12345"}]
        resolved = discovery.run_m3_canonicalize(raw_citations, str(self.test_dir))

        self.assertEqual(len(resolved), 1)
        arxiv_res = resolved[0]
        self.assertEqual(arxiv_res["status"], "RESOLVED")
        self.assertEqual(arxiv_res["references"], ["arxiv:2305.00000", "doi:10.000/123"])
        self.assertEqual(arxiv_res["cited_by"], ["semanticscholar:cit1"])

    def test_m7_evidence_paper_edges(self):
        # Verify run_m7_evidence generates the correct edges for references and cited_by
        resolved_papers = [
            {
                "original_citation": {"type": "arxiv", "value": "https://arxiv.org/abs/2304.12345"},
                "canonical_id": "arxiv:2304.12345",
                "status": "RESOLVED",
                "references": ["arxiv:2305.00000"],
                "cited_by": ["semanticscholar:cit1"]
            }
        ]
        evidence = discovery.run_m7_evidence(
            url="https://youtube.com/watch?v=vid1",
            video_id="vid1",
            metadata={"title": "Test Video"},
            resolved_papers=resolved_papers,
            transcripts={},
            analysis={},
            keyframes={},
            out_dir=str(self.test_dir)
        )

        edges = evidence["paper_graph_edges"]
        # 1. vid cites arxiv:2304.12345
        # 2. arxiv:2304.12345 references arxiv:2305.00000
        # 3. arxiv:2304.12345 cited_by semanticscholar:cit1
        self.assertEqual(len(edges), 3)

        cites_edge = next(e for e in edges if e["relation"] == "cites_in_description")
        self.assertEqual(cites_edge["source_id"], "vid1")
        self.assertEqual(cites_edge["target_id"], "arxiv:2304.12345")

        ref_edge = next(e for e in edges if e["relation"] == "references")
        self.assertEqual(ref_edge["source_id"], "arxiv:2304.12345")
        self.assertEqual(ref_edge["target_id"], "arxiv:2305.00000")

        cit_edge = next(e for e in edges if e["relation"] == "cited_by")
        self.assertEqual(cit_edge["source_id"], "arxiv:2304.12345")
        self.assertEqual(cit_edge["target_id"], "semanticscholar:cit1")

    @patch('discovery.run_m2_citations')
    @patch('discovery.run_m1_metadata')
    def test_through_m1(self, mock_m1, mock_m2):
        mock_m1.return_value = {"id": "vid1", "description": "test"}
        url = "https://youtube.com/watch?v=vid1"
        out_dir = self.test_dir / "vid1"
        out_dir.mkdir(parents=True, exist_ok=True)

        result = discovery.process_video(url, str(out_dir), through_stage="M1")

        self.assertEqual(result.get("status"), "PARTIAL")
        mock_m1.assert_called_once()
        mock_m2.assert_not_called()

    @patch('discovery.run_m4_transcripts')
    @patch('discovery.run_m3_canonicalize')
    @patch('discovery.run_m2_citations')
    @patch('discovery.run_m1_metadata')
    def test_through_m3(self, mock_m1, mock_m2, mock_m3, mock_m4):
        mock_m1.return_value = {"id": "vid1", "description": "test"}
        mock_m2.return_value = []
        mock_m3.return_value = []

        url = "https://youtube.com/watch?v=vid1"
        out_dir = self.test_dir / "vid1"
        out_dir.mkdir(parents=True, exist_ok=True)

        result = discovery.process_video(url, str(out_dir), through_stage="M3")

        self.assertEqual(result.get("status"), "PARTIAL")
        mock_m1.assert_called_once()
        mock_m2.assert_called_once()
        mock_m3.assert_called_once()
        mock_m4.assert_not_called()

    @patch('discovery.run_m4_transcripts')
    @patch('discovery.run_m3_canonicalize')
    @patch('discovery.run_m2_citations')
    @patch('discovery.run_m1_metadata')
    def test_resume_ceiling(self, mock_m1, mock_m2, mock_m3, mock_m4):
        mock_m1.return_value = {"id": "vid1", "description": "test"}
        mock_m2.return_value = []
        mock_m3.return_value = []

        url = "https://youtube.com/watch?v=vid1"
        out_dir = self.test_dir / "vid1"
        out_dir.mkdir(parents=True, exist_ok=True)

        # Run through M3
        discovery.process_video(url, str(out_dir), through_stage="M3")
        self.assertEqual(mock_m1.call_count, 1)
        self.assertEqual(mock_m3.call_count, 1)
        mock_m4.assert_not_called()

        # Now run through M4
        # Since state has M1-M3, they should not be called again
        mock_m4.return_value = {}
        discovery.process_video(url, str(out_dir), through_stage="M4")

        self.assertEqual(mock_m1.call_count, 1) # No new calls
        self.assertEqual(mock_m3.call_count, 1) # No new calls
        mock_m4.assert_called_once()

    def test_invalid_stage(self):
        url = "https://youtube.com/watch?v=vid1"
        out_dir = self.test_dir / "vid1"
        with self.assertRaises(ValueError):
            discovery.process_video(url, str(out_dir), through_stage="M8")

    @patch('discovery.process_video')
    def test_zero_partial_corpus(self, mock_process_video):
        manifest_path = self.test_dir / "manifest.json"
        with open(manifest_path, 'w') as f:
            json.dump({"urls": ["url1"], "through_stage": "M3"}, f)

        mock_process_video.return_value = {"status": "PARTIAL", "video_id": "vid1", "completed_stages": ["M1", "M2", "M3"]}

        report = discovery.process_corpus(str(manifest_path), str(self.test_dir))

        # A partial run shouldn't pass
        self.assertEqual(report["stage_status"], "PARTIAL_SUCCESS")

        # Test zero videos
        with open(manifest_path, 'w') as f:
            json.dump({"urls": []}, f)

        report_zero = discovery.process_corpus(str(manifest_path), str(self.test_dir))
        self.assertEqual(report_zero["stage_status"], "FAILED")


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

import importlib.util
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

MODULE_PATH = Path(__file__).with_name("rd_ingest.py")
spec = importlib.util.spec_from_file_location("rd_ingest", MODULE_PATH)
rd = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(rd)


class RDIngestTests(unittest.TestCase):
    def test_youtube_id_variants(self):
        self.assertEqual(
            rd.youtube_id("https://www.youtube.com/watch?v=abc123&t=4"),
            "abc123",
        )
        self.assertEqual(rd.youtube_id("https://youtu.be/xyz789"), "xyz789")
        self.assertEqual(
            rd.youtube_id("https://www.youtube.com/shorts/short1"),
            "short1",
        )

    def test_parse_vtt_removes_timing_tags_and_duplicates(self):
        raw = """WEBVTT

00:00:00.000 --> 00:00:02.000
Hello <c>world</c>

00:00:02.000 --> 00:00:04.000
Hello world

00:00:04.000 --> 00:00:06.000
Next line
"""
        self.assertEqual(rd.parse_vtt(raw), "Hello world\nNext line\n")

    def test_watch_override_is_reused(self):
        with tempfile.TemporaryDirectory() as td:
            skill = Path(td) / "watch"
            skill.mkdir()
            with patch.dict(os.environ, {"ASPACE_WATCH_SKILL": str(skill)}):
                self.assertEqual(rd.resolve_watch_skill(), skill)

    def test_packet_stops_at_capture_boundary(self):
        with tempfile.TemporaryDirectory() as td:
            transcript = Path(td) / "transcript.md"
            transcript.write_text("grounded transcript\n", encoding="utf-8")
            packet = rd.build_packet(
                "https://youtu.be/abc123",
                {
                    "source_type": "youtube",
                    "id": "abc123",
                    "title": "Demo",
                    "author": "Author",
                    "date": "20260928",
                    "url": "https://youtu.be/abc123",
                },
                "grounded transcript\n",
                "yt-dlp:vtt",
                rd.sha256_file(transcript),
                [],
                ["https://github.com/example/repo"],
                None,
                {"yt-dlp": "2026.07.04", "ffmpeg": "8.1.1"},
            )
            contract = packet["analysis_contract"]
            self.assertEqual(contract["state"], "CAPTURED_NOT_ANALYZED")
            self.assertEqual(contract["next_owner"], "Bill/DISCOVER")
            self.assertEqual(contract["provenance_review"], "Graham/REMEMBER")
            self.assertEqual(contract["design_return_to"], "Clara/DESIGN")
            self.assertEqual(
                packet["capture"]["code_refs"],
                ["https://github.com/example/repo"],
            )


if __name__ == "__main__":
    unittest.main()

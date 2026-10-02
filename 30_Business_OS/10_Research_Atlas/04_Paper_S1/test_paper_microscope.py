import unittest
from unittest.mock import patch, MagicMock
import json
import os
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paper_microscope

class TestPaperMicroscope(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path("test_paper_output")
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def tearDown(self):
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_extract_insights(self):
        text = "We propose a novel method for object detection. We show that it outperforms existing methods. We evaluate our approach on the COCO benchmark. The system is state-of-the-art."
        insights = paper_microscope.extract_insights(text)
        self.assertEqual(len(insights["methods"]), 1)
        self.assertIn("We propose a novel method for object detection", insights["methods"][0])
        self.assertEqual(len(insights["claims"]), 1)
        self.assertIn("We show that it outperforms existing methods", insights["claims"][0])
        self.assertEqual(len(insights["benchmarks"]), 2)
        self.assertIn("We evaluate our approach on the COCO benchmark", insights["benchmarks"][0])
        self.assertIn("The system is state-of-the-art", insights["benchmarks"][1])

    @patch('urllib.request.urlopen')
    def test_capture_paper_arxiv(self, mock_urlopen):
        mock_xml = b'''<?xml version="1.0" encoding="UTF-8"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry>
            <id>http://arxiv.org/abs/2305.10601</id>
            <published>2023-05-17T17:53:13Z</published>
            <title>Tree of Thoughts: Deliberate Problem Solving with Large Language Models</title>
            <summary>Language models are increasingly being deployed. We propose a new framework. We show better performance on a reasoning benchmark.</summary>
            <author><name>Shunyu Yao</name></author>
            <author><name>Dian Yu</name></author>
          </entry>
        </feed>
        '''

        mock_response = MagicMock()
        mock_response.read.return_value = mock_xml
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        evidence = paper_microscope.capture_paper("arxiv:2305.10601", str(self.test_dir))

        self.assertIsNotNone(evidence)
        self.assertEqual(evidence["canonical_id"], "arxiv:2305.10601")
        self.assertEqual(evidence["title"], "Tree of Thoughts: Deliberate Problem Solving with Large Language Models")
        self.assertEqual(evidence["provenance"]["agent"], "PAPER S1")
        self.assertEqual(evidence["provenance"]["routed_to"], "Graham/REMEMBER")

        # Verify bounded capture assertion
        self.assertEqual(evidence["graph_capture"]["status"], "BOUNDED")

        # Check extraction
        self.assertEqual(len(evidence["extracted_context"]["methods"]), 1)
        self.assertEqual(len(evidence["extracted_context"]["claims"]), 1)
        self.assertEqual(len(evidence["extracted_context"]["benchmarks"]), 1)

        # Check files
        packet_path = self.test_dir / "evidence_packet.json"
        metadata_path = self.test_dir / "metadata.json"
        self.assertTrue(packet_path.exists())
        self.assertTrue(metadata_path.exists())

        # Verify SHA-256 is present and valid
        self.assertIn("sha256", evidence["artifacts"]["metadata_file"])
        self.assertIsNotNone(evidence["artifacts"]["metadata_file"]["sha256"])

    @patch('urllib.request.urlopen')
    def test_capture_paper_unsupported(self, mock_urlopen):
        # Should proceed and generate a bounded packet even if source is unsupported
        evidence = paper_microscope.capture_paper("doi:10.1234/5678", str(self.test_dir))

        self.assertIsNotNone(evidence)
        self.assertEqual(evidence["canonical_id"], "doi:10.1234/5678")
        self.assertEqual(evidence["title"], "Unknown")
        self.assertEqual(evidence["graph_capture"]["status"], "BOUNDED")
        mock_urlopen.assert_not_called()

if __name__ == '__main__':
    unittest.main()

import importlib.util
import json
import re
import tempfile
import unittest
from pathlib import Path

P=Path(__file__).with_name("atlas_factory.py")
spec=importlib.util.spec_from_file_location("atlas_factory",P)
af=importlib.util.module_from_spec(spec);spec.loader.exec_module(af)

class FakeGWS:
    def __init__(self,schema):
        self.spreadsheet_id="fake-sheet"
        self.schema=schema
        self.tables={}
        self.mutations=0
    def metadata(self):
        return {"properties":{"title":self.schema["workbook_title"]},
                "sheets":[{"properties":{"title":x}} for x in self.tables]}
    def _tab(self,r):
        m=re.match(r"'([^']+)'!",r)
        if not m: raise AssertionError(r)
        return m.group(1)
    def read(self,r):
        return [list(x) for x in self.tables.get(self._tab(r),[])]
    def structural_update(self,requests):
        for req in requests:
            title=req["addSheet"]["properties"]["title"]
            self.tables.setdefault(title,[])
            self.mutations+=1
        return {}
    def values_update(self,r,values):
        tab=self._tab(r);rows=self.tables.setdefault(tab,[])
        m=re.search(r"![A-Z]+(\d+):",r)
        row=int(m.group(1)) if m else 1
        while len(rows)<row: rows.append([])
        rows[row-1]=list(values[0]);self.mutations+=1
        return {}
    def values_append(self,r,values):
        tab=self._tab(r);self.tables.setdefault(tab,[]).extend([list(x) for x in values]);self.mutations+=1
        return {}

class AtlasFactoryTests(unittest.TestCase):
    def test_m0_bootstrap_replay_is_idempotent(self):
        schema=af.load_schema();g=FakeGWS(schema)
        with tempfile.TemporaryDirectory() as td:
            first=af.stage_m0_bootstrap(g,Path(td))
            mutations_after_first=g.mutations
            second=af.stage_m0_bootstrap(g,Path(td))
            self.assertEqual(first["result"],"PASS")
            self.assertEqual(second["result"],"PASS")
            self.assertEqual(g.mutations,mutations_after_first)
            self.assertEqual(len(g.tables),13)
            self.assertEqual(len({x[0] for x in g.tables["00_Control"][1:]}),7)
            runs=g.tables["11_Runs"]
            self.assertEqual(len(runs),2) # header + one stable receipt
            self.assertEqual(runs[1][0],first["run_id"])
            self.assertEqual(runs[1][0],second["run_id"])

    def test_citation_miner_covers_direct_and_bibliographic_classes(self):
        text="""Paper: https://doi.org/10.1145/1234.5678
arXiv: 2609.12345
OpenReview https://openreview.net/forum?id=ABC_def-1
Project https://github.com/example/paper
Title: Who Is Behind the Harness? Fingerprinting LLMs through Agentic Behavior
Authors: Ada Alpha, Bob Beta and Cara Gamma
"""
        cs=af.mine_citations("video-1",text)
        kinds={x["candidate_kind"] for x in cs}
        self.assertTrue({"doi_url","arxiv_plain","openreview_url","provider_url","bibliographic_block"}.issubset(kinds))
        ids=[x["candidate_id"] for x in cs]
        self.assertEqual(ids,[x["candidate_id"] for x in af.mine_citations("video-1",text)])
        self.assertEqual(len(ids),len(set(ids)))

    def test_same_paper_two_videos_becomes_one_paper_two_edges(self):
        c1=af.candidate("v1","doi_plain","10.1145/1234.5678",url_or_id="10.1145/1234.5678")
        c2=af.candidate("v2","doi_url","https://doi.org/10.1145/1234.5678",url_or_id="10.1145/1234.5678")
        r=af.resolve_candidates([c1,c2])
        self.assertEqual(len(r["papers"]),1)
        self.assertEqual(len(r["edges"]),2)
        self.assertEqual(r["papers"][0]["paper_id"],"doi:10.1145/1234.5678")
        self.assertEqual({x["video_id"] for x in r["edges"]},{"v1","v2"})

    def test_ambiguous_bibliographic_candidate_goes_to_review(self):
        c=af.candidate("v1","bibliographic_block","Title: Some Paper\nAuthors: A, B",title="Some Paper",authors=["A","B"],confidence=.8)
        r=af.resolve_candidates([c])
        self.assertEqual(r["papers"],[])
        self.assertEqual(len(r["reviews"]),1)
        self.assertEqual(r["candidate_states"][c["candidate_id"]][0],"NEEDS_REVIEW")

if __name__=="__main__":
    unittest.main(verbosity=2)

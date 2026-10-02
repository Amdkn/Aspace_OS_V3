import argparse
import json
import os
import hashlib
from datetime import datetime, timezone
from pathlib import Path
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
import re

def compute_sha256(filepath):
    """Compute the SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception:
        return None

def setup_argparse():
    parser = argparse.ArgumentParser(description="PAPER S1 Deep Microscope")
    parser.add_argument("canonical_id", help="Canonical Paper ID (e.g., arxiv:2305.10601)")
    parser.add_argument("--out-dir", default="paper_output", help="Output directory")
    return parser

def fetch_paper_metadata_arxiv(arxiv_id):
    """
    Fetch metadata from arXiv API using urllib.
    """
    url = f"https://export.arxiv.org/api/query?id_list={arxiv_id}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'ASpaceOS/3.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = response.read()
            if not data:
                return {}

            root = ET.fromstring(data)
            # ArXiv API uses atom namespace
            ns = {'atom': 'http://www.w3.org/2005/Atom'}
            entry = root.find('atom:entry', ns)
            if entry is None:
                return {}

            title = entry.find('atom:title', ns)
            summary = entry.find('atom:summary', ns)
            published = entry.find('atom:published', ns)
            authors = [a.find('atom:name', ns).text for a in entry.findall('atom:author', ns) if a.find('atom:name', ns) is not None]

            return {
                "title": title.text.strip().replace('\n', ' ') if title is not None else "Unknown",
                "abstract": summary.text.strip() if summary is not None else "",
                "published_date": published.text if published is not None else "",
                "authors": authors
            }
    except Exception as e:
        print(f"[PAPER S1] ArXiv fetch failed for {arxiv_id}: {e}")
        return {}

def extract_insights(text):
    """
    Naively extract claims, methods, and benchmarks from abstract or text.
    Bounded deep capture: does not ingest the full graph, extraction remains evidence-backed.
    """
    insights = {
        "claims": [],
        "methods": [],
        "benchmarks": []
    }

    if not text:
        return insights

    sentences = re.split(r'(?<=[.!?]) +', text.replace('\n', ' '))
    for sentence in sentences:
        s_lower = sentence.lower()
        if "we show" in s_lower or "we demonstrate" in s_lower or "we prove" in s_lower or "result" in s_lower or "claim" in s_lower:
            insights["claims"].append(sentence.strip())
        if ("we propose" in s_lower or "method" in s_lower or "approach" in s_lower or "technique" in s_lower) and "existing methods" not in s_lower and "evaluate our approach" not in s_lower:
            insights["methods"].append(sentence.strip())
        if "benchmark" in s_lower or "dataset" in s_lower or "evaluate" in s_lower or "state-of-the-art" in s_lower or "sota" in s_lower:
            insights["benchmarks"].append(sentence.strip())

    return insights

def capture_paper(canonical_id, out_dir):
    print(f"-> Starting PAPER S1 capture for: {canonical_id}")
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    metadata = {}

    # 1. Fetch metadata
    if canonical_id.startswith("arxiv:"):
        arxiv_id = canonical_id.split("arxiv:")[1]
        print(f"-> Fetching ArXiv metadata for {arxiv_id}...")
        metadata = fetch_paper_metadata_arxiv(arxiv_id)
    else:
        print(f"-> Unsupported canonical source format: {canonical_id}. Only arxiv: is fully supported for automated deep capture currently.")
        # Proceed with empty metadata to generate packet structure

    # Write metadata artifact
    metadata_file = out_path / "metadata.json"
    with open(metadata_file, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    metadata_hash = compute_sha256(metadata_file)

    # 2. Extract Insights (from abstract for now - "full text when justified" logic can be expanded here)
    abstract = metadata.get("abstract", "")
    insights = extract_insights(abstract)

    # 3. Assemble Evidence Packet
    print("-> Assembling Evidence Packet...")

    evidence = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "canonical_id": canonical_id,
        "title": metadata.get("title", "Unknown"),
        "provenance": {
            "agent": "PAPER S1",
            "capability": "Bounded Deep Capture",
            "scope": "Microscope (Selected Source)",
            "routed_to": "Graham/REMEMBER"
        },
        "artifacts": {
            "metadata_file": {
                "path": str(metadata_file),
                "sha256": metadata_hash
            }
        },
        "extracted_context": {
            "claims": insights["claims"],
            "methods": insights["methods"],
            "benchmarks": insights["benchmarks"]
        },
        "graph_capture": {
            "status": "BOUNDED",
            "reason": "no eager full-text ingestion of the full graph"
        }
    }

    packet_file = out_path / "evidence_packet.json"
    with open(packet_file, "w", encoding="utf-8") as f:
        json.dump(evidence, f, indent=2, ensure_ascii=False)

    print(f"SUCCESS. Evidence packet written to: {packet_file}")
    return evidence

def main():
    parser = setup_argparse()
    args = parser.parse_args()
    capture_paper(args.canonical_id, args.out_dir)

if __name__ == "__main__":
    main()

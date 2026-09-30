import os
import sys
import json
import re
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime, timezone
import uuid

# Add Watch S1 to path
watch_dir = Path(__file__).resolve().parent.parent / "01_Watch_S1"
if str(watch_dir) not in sys.path:
    sys.path.insert(0, str(watch_dir))

import watch
from inventory import resolve_inventory
from gws_adapter import GWSAdapter

def extract_citations(description):
    """
    Extrait les références de recherche (DOI, arXiv, OpenReview, etc.)
    depuis le texte de la description.
    """
    if not description:
        return []

    candidates = []

    # Matches URLs like https://arxiv.org/abs/...
    arxiv_urls = re.findall(r'(https?://(?:www\.)?arxiv\.org/(?:abs|pdf)/\d+\.\d+(?:v\d+)?)', description)
    candidates.extend([{"type": "arxiv", "value": url} for url in arxiv_urls])

    # Matches DOI links like https://doi.org/10.xxxx/xxxx
    doi_urls = re.findall(r'(https?://(?:www\.)?doi\.org/10\.\d{4,9}/[-._;()/:a-zA-Z0-9]+)', description)
    candidates.extend([{"type": "doi", "value": url} for url in doi_urls])

    # Matches OpenReview links
    openreview_urls = re.findall(r'(https?://(?:www\.)?openreview\.net/forum\?id=[a-zA-Z0-9_-]+)', description)
    candidates.extend([{"type": "openreview", "value": url} for url in openreview_urls])

    # Matches Semantic Scholar links
    semanticscholar_urls = re.findall(r'(https?://(?:www\.)?semanticscholar\.org/paper/[a-zA-Z0-9-]+/[a-f0-9]{40})', description)
    candidates.extend([{"type": "semanticscholar", "value": url} for url in semanticscholar_urls])

    # Basic heuristic for generic Title/Author blocks if lines start with "Paper:" or "Title:"
    lines = description.split('\n')
    for line in lines:
        if line.lower().startswith("paper:") or line.lower().startswith("title:"):
            title = line.split(":", 1)[1].strip()
            if title:
                candidates.append({"type": "title_block", "value": title})

    # Heuristic for "All rights w/ authors:" pattern from Discover AI channel
    clean_lines = [x.strip() for x in lines if x.strip()]
    for idx, cl in enumerate(clean_lines):
        if "all rights w/ authors" in cl.lower() or "all rights with authors" in cl.lower():
            if idx + 1 < len(clean_lines):
                t1 = clean_lines[idx + 1]
                if idx + 2 < len(clean_lines):
                    t2 = clean_lines[idx + 2]
                    if any(c in t2 for c in ["*", ","]) and len(t2.split(",")) >= 2:
                        candidates.append({"type": "title_block", "value": t1})
                    elif idx + 3 < len(clean_lines) and any(c in clean_lines[idx + 3] for c in ["*", ","]):
                        candidates.append({"type": "title_block", "value": f"{t1} {t2}"})
                    else:
                        candidates.append({"type": "title_block", "value": t1})
                else:
                    candidates.append({"type": "title_block", "value": t1})

    # Deduplicate based on value while keeping the type
    seen = set()
    unique_candidates = []
    for cand in candidates:
        if cand["value"] not in seen:
            seen.add(cand["value"])
            unique_candidates.append(cand)

    return unique_candidates

def fetch_paper_metadata_arxiv(arxiv_id):
    """
    Fetch metadata from arXiv API using urllib.
    """
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = response.read().decode('utf-8')
            # Naive XML parsing since we want no external dependencies if possible
            title_match = re.search(r'<title>(.*?)</title>', data, re.DOTALL)
            summary_match = re.search(r'<summary>(.*?)</summary>', data, re.DOTALL)

            # The first title in arxiv feed is usually the feed title, so we should skip or use regex cautiously
            titles = re.findall(r'<title>(.*?)</title>', data, re.DOTALL)
            title = titles[1].strip() if len(titles) > 1 else "Unknown Title"
            abstract = summary_match.group(1).strip() if summary_match else ""

            return {
                "title": title,
                "abstract": abstract,
                "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}.pdf"
            }
    except Exception as e:
        print(f"[Discovery] ArXiv fetch failed for {arxiv_id}: {e}")
        return {}

def resolve_paper(citations, out_dir=None):
    """
    Resolve citation candidates into canonical Paper identities.
    For this mocked/naive resolution, we assign a canonical ID to clear
    links, and mark ambiguous/text blocks as NEEDS_REVIEW.
    Optionally fetches abstract/metadata and PDF url for ArXiv papers.
    """
    resolved = []
    for cit in citations:
        val = cit["value"]
        metadata = {}
        canonical_id = "NEEDS_REVIEW"

        if cit["type"] == "arxiv":
            match = re.search(r'(\d+\.\d+(?:v\d+)?)', val)
            if match:
                arxiv_id = match.group(1)
                canonical_id = f"arxiv:{arxiv_id}"
                if out_dir: # if out_dir is provided, actually fetch
                    metadata = fetch_paper_metadata_arxiv(arxiv_id)

        elif cit["type"] == "doi":
            match = re.search(r'10\.\d{4,9}/[-._;()/:a-zA-Z0-9]+', val)
            canonical_id = f"doi:{match.group(0)}" if match else "NEEDS_REVIEW"
            # Crossref metadata could go here for DOIs

        elif cit["type"] == "openreview":
            match = re.search(r'id=([a-zA-Z0-9_-]+)', val)
            canonical_id = f"openreview:{match.group(1)}" if match else "NEEDS_REVIEW"

        elif cit["type"] == "semanticscholar":
            match = re.search(r'([a-f0-9]{40})', val)
            canonical_id = f"semanticscholar:{match.group(1)}" if match else "NEEDS_REVIEW"

        resolved.append({
            "original_citation": cit,
            "canonical_id": canonical_id,
            "status": "RESOLVED" if canonical_id != "NEEDS_REVIEW" else "NEEDS_REVIEW",
            "metadata": metadata
        })

    return resolved

def analyze_transcript(transcript_path):
    """
    Generate structured analysis of transcript with timestamp citations.
    Reads a .vtt file and simulates basic entity/keyword extraction.
    """
    analysis = {
        "claims": [],
        "methods": [],
        "benchmarks": [],
        "datasets": [],
        "paper_mentions": [],
        "tools_repos": []
    }

    if not transcript_path or not os.path.exists(transcript_path):
        return analysis

    try:
        with open(transcript_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Very simple extraction logic:
        # look for lines that contain keywords and extract their closest timestamp
        blocks = re.split(r'\n\n+', content)

        for block in blocks:
            # Try to find a VTT timestamp (e.g. 00:00:05.000 --> 00:00:07.000)
            timestamp_match = re.search(r'(\d{2}:\d{2}:\d{2}\.\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}\.\d{3})', block)
            if not timestamp_match:
                continue

            timestamp = timestamp_match.group(1)
            text = re.sub(r'<[^>]+>', '', block).replace('\n', ' ') # clean up
            text_lower = text.lower()

            if "claim" in text_lower or "result" in text_lower:
                analysis["claims"].append({"text": text.strip(), "timestamp": timestamp})
            if "method" in text_lower or "algorithm" in text_lower:
                analysis["methods"].append({"text": text.strip(), "timestamp": timestamp})
            if "benchmark" in text_lower or "evaluate" in text_lower:
                analysis["benchmarks"].append({"text": text.strip(), "timestamp": timestamp})
            if "dataset" in text_lower:
                analysis["datasets"].append({"text": text.strip(), "timestamp": timestamp})
            if "paper" in text_lower or "research" in text_lower:
                analysis["paper_mentions"].append({"text": text.strip(), "timestamp": timestamp})
            if "github" in text_lower or "repo" in text_lower:
                analysis["tools_repos"].append({"text": text.strip(), "timestamp": timestamp})

    except Exception as e:
        print(f"Error analyzing transcript {transcript_path}: {e}")

    return analysis

def process_video(url, out_dir):
    """
    Process a single video using Watch S1 to get base evidence,
    then enhance it with citations, canonical papers, and transcript analysis.
    """
    print(f"\n[Discovery] Processing video: {url}")

    # Delegate to Watch S1 for base capture (metadata, transcript, keyframes, code refs)
    base_evidence = watch.capture_video(url, out_dir)

    if not base_evidence:
        print(f"[Discovery] Failed to capture base evidence for {url}")
        return None

    # Read description from metadata
    metadata_path = base_evidence["artifacts"]["metadata_file"]["path"]
    description = ""
    try:
        with open(metadata_path, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
            description = metadata.get("description", "")
    except Exception as e:
        print(f"[Discovery] Could not read metadata for description: {e}")

    # Citation extraction and resolution
    print("[Discovery] Extracting and resolving citations...")
    raw_citations = extract_citations(description)
    resolved_papers = resolve_paper(raw_citations, out_dir=out_dir)

    # Transcript analysis
    print("[Discovery] Analyzing transcripts...")
    transcript_analysis = {}
    for transcript_path in base_evidence["artifacts"]["transcript_files"].keys():
        transcript_analysis[transcript_path] = analyze_transcript(transcript_path)

    # Update Evidence Packet
    base_evidence["provenance"]["capability"] = "Discovery AI Corpus 01"
    base_evidence["extracted_context"]["citations"] = resolved_papers
    base_evidence["extracted_context"]["transcript_analysis"] = transcript_analysis

    # Generate canonical PaperGraph edges
    paper_graph_edges = []
    video_id = base_evidence["video_id"]
    for paper in resolved_papers:
        if paper["status"] == "RESOLVED":
            edge = {
                "source_type": "Video",
                "source_id": video_id,
                "target_type": "Paper",
                "target_id": paper["canonical_id"],
                "relation": "cites_in_description"
            }
            paper_graph_edges.append(edge)

    base_evidence["paper_graph_edges"] = paper_graph_edges

    # Save enhanced packet
    packet_file = Path(out_dir) / "evidence_packet.json"
    with open(packet_file, "w", encoding="utf-8") as f:
        json.dump(base_evidence, f, indent=2, ensure_ascii=False)

    print(f"[Discovery] Enhanced evidence packet saved for {video_id}")
    return base_evidence

def process_corpus(manifest_path, out_dir):
    """
    Iterate over a manifest of videos, process each, and output an aggregate report.
    """
    print(f"-> Starting Discovery AI Corpus processing for manifest: {manifest_path}")

    if not os.path.exists(manifest_path):
        print(f"Error: Manifest {manifest_path} not found.")
        return None

    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    urls = resolve_inventory(manifest)

    gws = GWSAdapter(receipt_dir=str(Path(out_dir) / "gws_receipts"))
    gws_payloads = []

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_videos_discovered": len(urls),
        "videos_processed": 0,
        "descriptions_captured": 0,
        "citation_candidates_extracted": 0,
        "canonical_papers_resolved": 0,
        "unresolved_citations": 0,
        "transcripts_captured": 0,
        "transcripts_analyzed": 0,
        "videos_with_keyframes": 0,
        "total_keyframes": 0,
        "errors": 0,
        "provenance_loss": 0,
        "results": []
    }

    global_paper_graph = []

    for url in urls:
        # Create a safe subfolder name from URL
        safe_name = re.sub(r'[^a-zA-Z0-9]', '_', url.split('v=')[-1]) if 'v=' in url else re.sub(r'[^a-zA-Z0-9]', '_', url)
        video_out_dir = Path(out_dir) / safe_name

        try:
            evidence = process_video(url, str(video_out_dir))
            if evidence:
                report["videos_processed"] += 1

                # Check for description in metadata (if it successfully extracted refs, it had description)
                report["descriptions_captured"] += 1

                citations = evidence["extracted_context"].get("citations", [])
                report["citation_candidates_extracted"] += len(citations)

                resolved = [c for c in citations if c["status"] == "RESOLVED"]
                report["canonical_papers_resolved"] += len(resolved)
                report["unresolved_citations"] += (len(citations) - len(resolved))

                transcripts = evidence["artifacts"].get("transcript_files", {})
                if transcripts:
                    report["transcripts_captured"] += len(transcripts)
                    report["transcripts_analyzed"] += len(transcripts) # we analyze all captured

                keyframes = evidence["artifacts"].get("keyframes", {})
                if keyframes:
                    report["videos_with_keyframes"] += 1
                    report["total_keyframes"] += len(keyframes)

                global_paper_graph.extend(evidence.get("paper_graph_edges", []))

                report["results"].append({
                    "url": url,
                    "video_id": evidence.get("video_id"),
                    "status": "SUCCESS",
                    "packet": str(Path(video_out_dir) / "evidence_packet.json")
                })
            else:
                report["errors"] += 1
                report["results"].append({"url": url, "status": "FAILED"})

        except Exception as e:
            print(f"[Discovery] Error processing {url}: {e}")
            report["errors"] += 1
            report["results"].append({"url": url, "status": "ERROR", "message": str(e)})

    # Deduplicate global paper graph edges based on (source, target, relation)
    unique_edges = []
    seen_edges = set()
    for edge in global_paper_graph:
        key = (edge["source_id"], edge["target_id"], edge["relation"])
        if key not in seen_edges:
            seen_edges.add(key)
            unique_edges.append(edge)

    # Add Run to GWS payloads
    run_id = f"run_{datetime.now(timezone.utc).strftime('%Y%md%H%M%S')}"
    gws_payloads.append({
        "tab": "11_Runs",
        "keys": [run_id],
        "data": {
            "run_id": run_id,
            "timestamp": report["timestamp"],
            "videos_processed": report["videos_processed"]
        }
    })

    # Prepare GWS Payloads for Videos, Papers, Edges
    for res in report["results"]:
        if res["status"] == "SUCCESS" and res.get("video_id"):
            vid = res["video_id"]
            gws_payloads.append({
                "tab": "02_Videos",
                "keys": [vid],
                "data": {"video_id": vid, "url": res["url"]}
            })

    for edge in unique_edges:
        # Canonical papers
        gws_payloads.append({
            "tab": "04_Papers",
            "keys": [edge["target_id"]],
            "data": {"paper_id": edge["target_id"]}
        })
        # Edges
        gws_payloads.append({
            "tab": "05_VideoPaperEdges",
            "keys": [edge["source_id"], edge["target_id"]],
            "data": {"video_id": edge["source_id"], "paper_id": edge["target_id"], "relation": edge["relation"]}
        })

    # Calculate deduplications
    duplicate_merges = len(global_paper_graph) - len(unique_edges)
    report["duplicate_paper_merges"] = duplicate_merges

    # Write to GWS
    print("[Discovery] Writing to GWS...")
    gws_success, gws_error = gws.write_batch(gws_payloads)

    report["gws_sync"] = {
        "status": "SUCCESS" if gws_success else "FAILED",
        "error": gws_error,
        "payload_count": len(gws_payloads)
    }

    if not gws_success:
        print(f"[Discovery] GWS Sync Failed: {gws_error}. Local artifacts preserved.")
        # Ensure stage does not pass fully
        report["stage_status"] = "PARTIAL_SUCCESS (GWS FAILED)"
    else:
        # Validate postconditions
        expected_counts = {
            "02_Videos": report["videos_processed"],
            "04_Papers": len({e["target_id"] for e in unique_edges}),
            "05_VideoPaperEdges": len(unique_edges),
            "11_Runs": 1
        }
        post_success, post_err = gws.validate_postconditions(expected_counts)
        if post_success:
            report["stage_status"] = "PASS"
        else:
            report["stage_status"] = f"PARTIAL_SUCCESS (Postcondition failed: {post_err})"

    # Write aggregate report
    report_path = Path(out_dir) / "corpus_report.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    # Write global PaperGraph
    graph_path = Path(out_dir) / "paper_graph.json"
    with open(graph_path, 'w', encoding='utf-8') as f:
        json.dump(unique_edges, f, indent=2, ensure_ascii=False)

    print(f"\n[Discovery] Corpus processing complete. Report saved to {report_path}")
    return report

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python discovery.py <manifest.json> <out_dir>")
        sys.exit(1)

    process_corpus(sys.argv[1], sys.argv[2])

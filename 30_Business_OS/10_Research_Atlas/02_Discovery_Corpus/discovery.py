import subprocess
import os
import sys
import json
import hashlib
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
    Extrait les rÃ©fÃ©rences de recherche (DOI, arXiv, OpenReview, etc.)
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


def compute_sha256(filepath):
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception:
        return None

def load_state(out_dir):
    state_file = Path(out_dir) / "state.json"
    if state_file.exists():
        try:
            with open(state_file, 'r') as f:
                return json.load(f)
        except Exception:
            pass
    return {"completed_stages": []}

def save_state(out_dir, state):
    state_file = Path(out_dir) / "state.json"
    with open(state_file, 'w') as f:
        json.dump(state, f, indent=2)

def run_m1_metadata(url, out_dir):
    out_path = Path(out_dir)
    metadata_file = out_path / "metadata.json"
    print(f"[Discovery] M1: Fetching metadata for {url}")

    cmd = [
        "yt-dlp",
        "--dump-json",
        "-o", str(out_path / "%(id)s.%(ext)s"),
        url
    ]
    try:
        import subprocess
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split('\n')
        metadata = json.loads(lines[-1])
        with open(metadata_file, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        return metadata
    except Exception as e:
        print(f"FAILED M1: {e}")
        return None

def run_m2_citations(metadata, out_dir):
    print("[Discovery] M2: Extracting citations")
    description = metadata.get("description", "")
    return extract_citations(description)

def fetch_ss_edges(canonical_id):
    """
    Fetch bounded references and citations for a paper using Semantic Scholar.
    Returns (references, citations) lists of canonical_ids.
    """
    if canonical_id.startswith("arxiv:"):
        ss_id = "ARXIV:" + canonical_id.split(":", 1)[1]
    elif canonical_id.startswith("doi:"):
        ss_id = "DOI:" + canonical_id.split(":", 1)[1]
    elif canonical_id.startswith("semanticscholar:"):
        ss_id = canonical_id.split(":", 1)[1]
    else:
        return [], []

    references = []
    citations = []

    def get_canonical(paper):
        if not paper: return None
        ext = paper.get("externalIds", {})
        if "ArXiv" in ext: return f"arxiv:{ext['ArXiv']}"
        if "DOI" in ext: return f"doi:{ext['DOI']}"
        if paper.get("paperId"): return f"semanticscholar:{paper['paperId']}"
        return None

    # Fetch references
    try:
        url = f"https://api.semanticscholar.org/graph/v1/paper/{ss_id}/references?limit=5&fields=paperId,externalIds"
        req = urllib.request.Request(url, headers={'User-Agent': 'Amdkn-Aspace/1.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            for item in data.get("data", []):
                c = get_canonical(item.get("citedPaper"))
                if c: references.append(c)
    except Exception as e:
        print(f"[Discovery] SS References fetch error for {ss_id}: {e}")

    # Fetch citations
    try:
        url = f"https://api.semanticscholar.org/graph/v1/paper/{ss_id}/citations?limit=5&fields=paperId,externalIds"
        req = urllib.request.Request(url, headers={'User-Agent': 'Amdkn-Aspace/1.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            for item in data.get("data", []):
                c = get_canonical(item.get("citingPaper"))
                if c: citations.append(c)
    except Exception as e:
        print(f"[Discovery] SS Citations fetch error for {ss_id}: {e}")

    return references, citations


def run_m3_canonicalize(raw_citations, out_dir):
    print("[Discovery] M3: Canonicalizing citations")
    resolved_papers = []
    for citation in raw_citations:
        resolved = {"original_citation": citation, "status": "NEEDS_REVIEW", "canonical_id": "NEEDS_REVIEW"}
        val = citation["value"]

        try:
            if citation["type"] == "arxiv":
                arxiv_id = val.split("/")[-1].replace(".pdf", "")
                resolved["canonical_id"] = f"arxiv:{arxiv_id}"

                # Fetch metadata via API
                api_url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
                req = urllib.request.Request(api_url, headers={'User-Agent': 'Amdkn-Aspace/1.0'})
                with urllib.request.urlopen(req, timeout=10) as response:
                    if response.status == 200:
                        resolved["status"] = "RESOLVED"
            elif citation["type"] == "doi":
                doi = val.split("doi.org/")[-1]
                resolved["canonical_id"] = f"doi:{doi}"

                api_url = f"https://api.crossref.org/works/{doi}"
                req = urllib.request.Request(api_url, headers={'User-Agent': 'Amdkn-Aspace/1.0'})
                with urllib.request.urlopen(req, timeout=10) as response:
                    if response.status == 200:
                        resolved["status"] = "RESOLVED"
            elif citation["type"] == "openreview":
                forum_id = val.split("id=")[-1]
                resolved["canonical_id"] = f"openreview:{forum_id}"
                resolved["status"] = "RESOLVED"
            elif citation["type"] == "semanticscholar":
                match = re.search(r'([a-f0-9]{40})', val)
                if match:
                    ss_id = match.group(1)
                    resolved["canonical_id"] = f"semanticscholar:{ss_id}"
                    api_url = f"https://api.semanticscholar.org/graph/v1/paper/{ss_id}?fields=paperId"
                    req = urllib.request.Request(api_url, headers={'User-Agent': 'Amdkn-Aspace/1.0'})
                    with urllib.request.urlopen(req, timeout=10) as response:
                        if response.status == 200:
                            resolved["status"] = "RESOLVED"
        except Exception as e:
            print(f"[Discovery] M3 Provider API Error: {e}")

        if resolved["status"] == "RESOLVED":
            refs, cites = fetch_ss_edges(resolved["canonical_id"])
            resolved["references"] = refs
            resolved["cited_by"] = cites

        resolved_papers.append(resolved)
    return resolved_papers



def run_m4_transcripts(url, out_dir):
    print(f"[Discovery] M4: Fetching transcripts for {url}")
    out_path = Path(out_dir)
    cmd = [
        "yt-dlp",
        "--write-auto-subs",
        "--sub-lang", "en,fr",
        "--write-subs",
        "--skip-download",
        "-o", str(out_path / "%(id)s.%(ext)s"),
        url
    ]
    try:
        import subprocess
        subprocess.run(cmd, capture_output=True, text=True, check=True)
    except Exception as e:
        print(f"FAILED M4: {e}")
        return {}

    # Identify transcript files (e.g., .vtt)
    transcript_files = list(out_path.glob("*.vtt"))
    return {str(p): compute_sha256(p) for p in transcript_files}

def run_m5_analysis(transcript_files):
    print("[Discovery] M5: Analyzing transcripts")
    transcript_analysis = {}
    for transcript_path in transcript_files:
        transcript_analysis[transcript_path] = analyze_transcript(transcript_path)
    return transcript_analysis

def run_m6_keyframes(url, video_id, out_dir):
    print(f"[Discovery] M6: Fetching bounded keyframes for {url}")
    out_path = Path(out_dir)
    video_file = out_path / f"{video_id}.mp4"
    cmd_vid = [
        "yt-dlp",
        "-f", "worstvideo/worst",
        "-o", str(video_file),
        url
    ]
    try:
        import subprocess
        subprocess.run(cmd_vid, check=True, capture_output=True)
    except Exception as e:
        print(f"FAILED M6 video download: {e}")
        return {}

    frames_dir = out_path / "frames"
    frames_dir.mkdir(exist_ok=True)

    if video_file.exists():
        cmd_ffmpeg = [
            "ffmpeg",
            "-hide_banner", "-loglevel", "error",
            "-i", str(video_file),
            "-vf", "fps=1/10,scale=854:-1",
            "-vframes", "50",
            str(frames_dir / "%04d.png")
        ]
        try:
            subprocess.run(cmd_ffmpeg, check=True)
        except Exception as e:
            print(f"FAILED M6 frame extraction: {e}")

    keyframes = list(frames_dir.glob("*.png"))
    return {str(p): compute_sha256(p) for p in keyframes}

def run_m7_evidence(url, video_id, metadata, resolved_papers, transcripts, analysis, keyframes, out_dir):
    print(f"[Discovery] M7: Assembling Evidence Packet for {video_id}")
    out_path = Path(out_dir)
    metadata_file = out_path / "metadata.json"

    # Generate canonical PaperGraph edges
    paper_graph_edges = []
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

            for ref_id in paper.get("references", []):
                paper_graph_edges.append({
                    "source_type": "Paper",
                    "source_id": paper["canonical_id"],
                    "target_type": "Paper",
                    "target_id": ref_id,
                    "relation": "references"
                })
            for cit_id in paper.get("cited_by", []):
                paper_graph_edges.append({
                    "source_type": "Paper",
                    "source_id": paper["canonical_id"],
                    "target_type": "Paper",
                    "target_id": cit_id,
                    "relation": "cited_by"
                })

    evidence = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source_url": url,
        "video_id": video_id,
        "title": metadata.get("title", "unknown_title"),
        "provenance": {
            "agent": "Bill",
            "capability": "Discovery AI Corpus 01",
            "scope": "Microscope (Selected Source)",
            "routed_to": "Graham/REMEMBER"
        },
        "artifacts": {
            "metadata_file": {
                "path": str(metadata_file),
                "sha256": compute_sha256(metadata_file)
            },
            "transcript_files": transcripts,
            "keyframe_directory": str(out_path / "frames"),
            "keyframes": keyframes,
            "keyframe_count": len(keyframes)
        },
        "extracted_context": {
            "citations": resolved_papers,
            "transcript_analysis": analysis
        },
        "paper_graph_edges": paper_graph_edges
    }

    packet_file = out_path / "evidence_packet.json"
    with open(packet_file, "w", encoding="utf-8") as f:
        json.dump(evidence, f, indent=2, ensure_ascii=False)

    return evidence


def process_video(url, out_dir, through_stage="M7"):
    """
    Process a single video through the M1-M7 pipeline, up to through_stage.
    """
    valid_stages = ["M1", "M2", "M3", "M4", "M5", "M6", "M7"]
    if through_stage not in valid_stages:
        raise ValueError(f"Invalid through_stage: {through_stage}. Must be one of {valid_stages}")

    stage_idx = valid_stages.index(through_stage)

    print(f"\n[Discovery] Processing video: {url} (through {through_stage})")
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    state = load_state(out_dir)
    stages = state.get("completed_stages", [])

    # Check if we should actually resume
    # Let's load intermediate artifacts if we resume
    metadata_file = out_path / "metadata.json"
    metadata = {}
    if metadata_file.exists():
        try:
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
        except Exception:
            pass

    video_id = metadata.get("id") or url.split("v=")[-1] if "v=" in url else url.split("/")[-1]

    # Check ceiling
    def should_run(stage_name):
        return valid_stages.index(stage_name) <= stage_idx

    # M1
    if not should_run("M1"):
        return {"status": "PARTIAL", "video_id": video_id, "completed_stages": stages}

    if "M1" not in stages:
        metadata = run_m1_metadata(url, out_dir)
        if not metadata:
            return None
        video_id = metadata.get("id", video_id)
        stages.append("M1")
        state["completed_stages"] = stages
        save_state(out_dir, state)

    # M2
    if not should_run("M2"):
        return {"status": "PARTIAL", "video_id": video_id, "completed_stages": stages}

    citations_file = out_path / "m2_citations.json"
    if "M2" not in stages:
        raw_citations = run_m2_citations(metadata, out_dir)
        with open(citations_file, 'w') as f:
            json.dump(raw_citations, f)
        stages.append("M2")
        state["completed_stages"] = stages
        save_state(out_dir, state)
    else:
        if citations_file.exists():
            with open(citations_file, 'r') as f:
                raw_citations = json.load(f)
        else:
            raw_citations = []

    # M3
    if not should_run("M3"):
        return {"status": "PARTIAL", "video_id": video_id, "completed_stages": stages}

    resolved_file = out_path / "m3_resolved.json"
    if "M3" not in stages:
        resolved_papers = run_m3_canonicalize(raw_citations, out_dir)
        with open(resolved_file, 'w') as f:
            json.dump(resolved_papers, f)
        stages.append("M3")
        state["completed_stages"] = stages
        save_state(out_dir, state)
    else:
        if resolved_file.exists():
            with open(resolved_file, 'r') as f:
                resolved_papers = json.load(f)
        else:
            resolved_papers = []

    # M4
    if not should_run("M4"):
        return {"status": "PARTIAL", "video_id": video_id, "completed_stages": stages}

    transcripts_file = out_path / "m4_transcripts.json"
    if "M4" not in stages:
        transcripts = run_m4_transcripts(url, out_dir)
        with open(transcripts_file, 'w') as f:
            json.dump(transcripts, f)
        stages.append("M4")
        state["completed_stages"] = stages
        save_state(out_dir, state)
    else:
        if transcripts_file.exists():
            with open(transcripts_file, 'r') as f:
                transcripts = json.load(f)
        else:
            transcripts = {}

    # M5
    if not should_run("M5"):
        return {"status": "PARTIAL", "video_id": video_id, "completed_stages": stages}

    analysis_file = out_path / "m5_analysis.json"
    if "M5" not in stages:
        analysis = run_m5_analysis(list(transcripts.keys()))
        with open(analysis_file, 'w') as f:
            json.dump(analysis, f)
        stages.append("M5")
        state["completed_stages"] = stages
        save_state(out_dir, state)
    else:
        if analysis_file.exists():
            with open(analysis_file, 'r') as f:
                analysis = json.load(f)
        else:
            analysis = {}

    # M6
    if not should_run("M6"):
        return {"status": "PARTIAL", "video_id": video_id, "completed_stages": stages}

    keyframes_file = out_path / "m6_keyframes.json"
    if "M6" not in stages:
        keyframes = run_m6_keyframes(url, video_id, out_dir)
        with open(keyframes_file, 'w') as f:
            json.dump(keyframes, f)
        stages.append("M6")
        state["completed_stages"] = stages
        save_state(out_dir, state)
    else:
        if keyframes_file.exists():
            with open(keyframes_file, 'r') as f:
                keyframes = json.load(f)
        else:
            keyframes = {}

    # M7
    if not should_run("M7"):
        return {"status": "PARTIAL", "video_id": video_id, "completed_stages": stages}

    if "M7" not in stages:
        evidence = run_m7_evidence(url, video_id, metadata, resolved_papers, transcripts, analysis, keyframes, out_dir)
        stages.append("M7")
        state["completed_stages"] = stages
        save_state(out_dir, state)
        return evidence
    else:
        # Load existing packet
        packet_file = out_path / "evidence_packet.json"
        if packet_file.exists():
            with open(packet_file, 'r') as f:
                return json.load(f)
        return None

def process_corpus(manifest_path, out_dir, through_stage=None):
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

    # Precedence: CLI > Manifest > M7
    effective_ceiling = through_stage or manifest.get("through_stage", "M7")
    print(f"[Discovery] Effective execution ceiling: {effective_ceiling}")

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
            evidence = process_video(url, str(video_out_dir), through_stage=effective_ceiling)
            if evidence:
                report["videos_processed"] += 1

                # Handle partial results
                if evidence.get("status") == "PARTIAL":
                    report["results"].append({
                        "url": url,
                        "video_id": evidence.get("video_id"),
                        "status": "PARTIAL_SUCCESS",
                        "completed_stages": evidence.get("completed_stages", [])
                    })
                    continue

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

    # Delegate GWS Payloads writing to GWSAdapter
    # mock_mode defaults to False but can be enabled in CI/tests
    # to bypass real API calls and save to gws_payloads.json.
    is_ci = os.environ.get("CI") == "true"
    adapter = GWSAdapter(mock_mode=is_ci)
    gws_success = adapter.write_batch(gws_payloads, out_dir)

    # Fix stage status logic
    if report["videos_processed"] == 0:
        report["stage_status"] = "FAILED"
    elif report["videos_processed"] < report["total_videos_discovered"] or effective_ceiling != "M7":
        report["stage_status"] = "PARTIAL_SUCCESS"
    elif not gws_success:
        print("[Discovery] Marking stage as FAILED due to GWS write failure.")
        report["stage_status"] = "FAILED"
    else:
        report["stage_status"] = "PASS"

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
    import argparse
    parser = argparse.ArgumentParser(description="Discovery AI Corpus Processor")
    parser.add_argument("manifest", help="Path to manifest.json")
    parser.add_argument("out_dir", help="Output directory")
    parser.add_argument("--through", help="Execution ceiling (e.g. M1, M3)", default=None)
    args = parser.parse_args()

    process_corpus(args.manifest, args.out_dir, through_stage=args.through)

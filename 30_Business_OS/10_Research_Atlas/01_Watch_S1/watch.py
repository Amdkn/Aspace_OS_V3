import argparse
import json
import os
import subprocess
import hashlib
from datetime import datetime, timezone
from pathlib import Path
import re

def setup_argparse():
    parser = argparse.ArgumentParser(description="Bill WATCH S1 Video Microscope")
    parser.add_argument("url", help="YouTube URL to process")
    parser.add_argument("--out-dir", default="watch_output", help="Output directory")
    return parser

def get_tool_version(tool):
    try:
        if tool == "yt-dlp":
            res = subprocess.run(["yt-dlp", "--version"], capture_output=True, text=True)
            return res.stdout.strip()
        elif tool == "ffmpeg":
            res = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)
            return res.stdout.split('\n')[0]
    except:
        pass
    return "UNKNOWN"

def extract_code_refs(description):
    """Extrait les references github/gitlab du texte de description."""
    if not description: return []
    # Updated regex to handle trailing punctuation
    urls = re.findall(r'(https?://(?:www\.)?(?:github|gitlab)\.com/[^\s\'"<>]+)', description)
    # Strip any trailing punctuation that might get caught
    cleaned = []
    for url in urls:
        while url and url[-1] in '.,;:!?)':
            url = url[:-1]
        if url:
            cleaned.append(url)
    return list(set(cleaned))

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

def capture_video(url, out_dir):
    print(f"-> Starting Bill WATCH S1 capture for: {url}")
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    # 1. Fetch metadata & transcript (using yt-dlp)
    print("-> Fetching metadata and transcript via yt-dlp...")
    metadata_file = out_path / "metadata.json"

    # We use yt-dlp to dump json, write auto subs, and skip video download initially.
    # But we actually also need the video for keyframes (ffmpeg).
    cmd = [
        "yt-dlp",
        "--dump-json",
        "--write-auto-subs",
        "--sub-lang", "en,fr",
        "--write-subs",
        "-o", str(out_path / "%(id)s.%(ext)s"),
        url
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        # Parse the last line as JSON, as yt-dlp might output other things before it.
        lines = result.stdout.strip().split('\n')
        metadata = json.loads(lines[-1])
    except Exception as e:
        print(f"FAILED to fetch metadata/transcript: {e}")
        return None

    with open(metadata_file, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    video_id = metadata.get("id", "unknown_id")
    title = metadata.get("title", "unknown_title")
    description = metadata.get("description", "")

    # Check what transcripts were downloaded
    transcript_files = list(out_path.glob(f"{video_id}*.vtt"))

    print(f"-> Extracting code references...")
    code_refs = extract_code_refs(description)

    # 2. Fetch video for keyframes (if needed, we just download worst video to be fast)
    video_file = out_path / f"{video_id}.mp4"
    print("-> Downloading low-res video for keyframe extraction...")
    cmd_vid = [
        "yt-dlp",
        "-f", "worstvideo[ext=mp4]+worstaudio[ext=m4a]/worst[ext=mp4]/worst",
        "-o", str(video_file),
        url
    ]
    try:
        subprocess.run(cmd_vid, check=True, capture_output=True)
    except Exception as e:
        print(f"FAILED to download video: {e}")
        # Proceed anyway, we just won't have keyframes

    # 3. Extract keyframes with ffmpeg (1 frame every 10s)
    frames_dir = out_path / "frames"
    frames_dir.mkdir(exist_ok=True)

    if video_file.exists():
        print("-> Extracting keyframes with ffmpeg (1 frame per 10s)...")
        cmd_ffmpeg = [
            "ffmpeg",
            "-hide_banner", "-loglevel", "error",
            "-i", str(video_file),
            "-vf", "fps=1/10,scale=854:-1",
            str(frames_dir / "%04d.png")
        ]
        try:
            subprocess.run(cmd_ffmpeg, check=True)
        except Exception as e:
            print(f"FAILED to extract frames: {e}")

    # 4. Generate Evidence Packet
    print("-> Assembling Evidence Packet...")

    # Compute hashes
    metadata_hash = compute_sha256(metadata_file)
    transcripts_with_hashes = {str(p): compute_sha256(p) for p in transcript_files}
    keyframes_with_hashes = {str(p): compute_sha256(p) for p in frames_dir.glob("*.png")}

    evidence = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source_url": url,
        "video_id": video_id,
        "title": title,
        "provenance": {
            "agent": "Bill",
            "capability": "WATCH S1",
            "scope": "Microscope (Selected Source)",
            "routed_to": "Graham/REMEMBER"
        },
        "artifacts": {
            "metadata_file": {
                "path": str(metadata_file),
                "sha256": metadata_hash
            },
            "transcript_files": transcripts_with_hashes,
            "keyframe_directory": str(frames_dir),
            "keyframes": keyframes_with_hashes,
            "keyframe_count": len(keyframes_with_hashes)
        },
        "extracted_context": {
            "code_references": code_refs
        },
        "environment": {
            "yt-dlp": get_tool_version("yt-dlp"),
            "ffmpeg": get_tool_version("ffmpeg")
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

    capture_video(args.url, args.out_dir)

if __name__ == "__main__":
    main()

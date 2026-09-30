#!/usr/bin/env python3
"""Discover AI Research Atlas continuous factory runtime (M0-M3).

Source contract: Clara PR #205 + ChatGPT Project source "Gates continus et factory unifiée".
This module keeps Google Sheets as an operational projection only. Raw descriptions and
receipts are local immutable artifacts; stable IDs make all Sheet writes replayable.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.parse
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ATLAS_ROOT = HERE.parent
REPO_ROOT = ATLAS_ROOT.parents[2]
SCHEMA_PATH = ATLAS_ROOT / "contracts" / "SPREADSHEET_SCHEMA.json"
INSTANCE_PATH = ATLAS_ROOT / "SPREADSHEET_INSTANCE.json"
CONTRACT_PATH = ATLAS_ROOT / "contracts" / "DISCOVER_AI_CONTRACTS.schema.json"

SCHEMA_VERSION = "aspace.discover-ai.spreadsheet.v1"
CHANNEL_ID = "UCfOvNb3xj28SNqPQ_JIbumg"
CHANNEL_HANDLE = "@code4AI"
CHANNEL_TITLE = "Discover AI"
CHANNEL_URL = "https://www.youtube.com/@code4AI/videos"

DEFAULT_ARTIFACT_ROOT = Path.home() / ".aspace" / "evidence" / "discover_ai"
DEFAULT_YTDLP = Path.home() / "bin" / "yt-dlp.exe"

CANDIDATE_KINDS = {
    "doi_url", "arxiv_url", "openreview_url", "provider_url",
    "doi_plain", "arxiv_plain", "plain_id", "bibliographic_block"
}


class FactoryError(RuntimeError):
    pass


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def canonical(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def stable_id(prefix: str, *parts: Any) -> str:
    return f"{prefix}-" + sha256_text(canonical(parts))[:24]


def col_letter(n: int) -> str:
    out = ""
    while n:
        n, rem = divmod(n - 1, 26)
        out = chr(65 + rem) + out
    return out


def parse_json_output(cp: subprocess.CompletedProcess[str], label: str) -> Any:
    if cp.returncode != 0:
        raise FactoryError(f"{label} failed rc={cp.returncode}: {(cp.stderr or cp.stdout)[-1500:]}")
    text = cp.stdout.strip()
    if not text:
        raise FactoryError(f"{label} returned empty stdout")
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise FactoryError(f"{label} returned non-JSON: {text[:500]}") from exc


def executable_argv(name: str) -> list[str]:
    found = shutil.which(name)
    if not found:
        raise FactoryError(f"executable not found: {name}")
    if os.name == "nt" and Path(found).suffix.lower() in {".cmd", ".bat"}:
        return [os.environ.get("COMSPEC") or r"C:\Windows\System32\cmd.exe", "/d", "/c", found]
    return [found]


class GWS:
    def __init__(self, spreadsheet_id: str, executable: str = "gws"):
        self.spreadsheet_id = spreadsheet_id
        self.base = executable_argv(executable)

    def run_json(self, args: list[str], *, body: Any | None = None, timeout: int = 30) -> Any:
        cmd = [*self.base, "sheets", *args]
        if body is not None:
            cmd += ["--json", canonical(body)]
        cp = subprocess.run(cmd, text=True, capture_output=True, timeout=timeout)
        return parse_json_output(cp, "gws " + " ".join(args[:3]))

    def metadata(self) -> dict[str, Any]:
        return self.run_json([
            "spreadsheets", "get",
            "--params", canonical({"spreadsheetId": self.spreadsheet_id, "includeGridData": False}),
            "--format", "json",
        ])

    def read(self, range_a1: str) -> list[list[Any]]:
        data = self.run_json([
            "+read", "--spreadsheet", self.spreadsheet_id,
            "--range", range_a1, "--format", "json",
        ])
        return data.get("values") or []

    def values_update(self, range_a1: str, values: list[list[Any]]) -> dict[str, Any]:
        return self.run_json([
            "spreadsheets", "values", "update",
            "--params", canonical({
                "spreadsheetId": self.spreadsheet_id,
                "range": range_a1,
                "valueInputOption": "RAW",
            }),
            "--format", "json",
        ], body={"majorDimension": "ROWS", "values": values})

    def values_append(self, range_a1: str, values: list[list[Any]]) -> dict[str, Any]:
        return self.run_json([
            "spreadsheets", "values", "append",
            "--params", canonical({
                "spreadsheetId": self.spreadsheet_id,
                "range": range_a1,
                "valueInputOption": "RAW",
                "insertDataOption": "INSERT_ROWS",
            }),
            "--format", "json",
        ], body={"majorDimension": "ROWS", "values": values})

    def structural_update(self, requests: list[dict[str, Any]]) -> dict[str, Any]:
        return self.run_json([
            "spreadsheets", "batchUpdate",
            "--params", canonical({"spreadsheetId": self.spreadsheet_id}),
            "--format", "json",
        ], body={"requests": requests})


def load_schema() -> dict[str, Any]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def load_instance() -> dict[str, Any]:
    return json.loads(INSTANCE_PATH.read_text(encoding="utf-8"))


def header_for(schema: dict[str, Any], tab: str) -> list[str]:
    for item in schema["tabs"]:
        if item["title"] == tab:
            return item["columns"]
    raise FactoryError(f"unknown tab: {tab}")


def read_table(gws: GWS, schema: dict[str, Any], tab: str) -> tuple[list[str], list[list[Any]]]:
    expected = header_for(schema, tab)
    rows = gws.read(f"'{tab}'!A1:{col_letter(len(expected))}")
    if not rows:
        return expected, []
    actual = [str(x) for x in rows[0]]
    if actual != expected:
        raise FactoryError(f"header mismatch {tab}: actual={actual!r} expected={expected!r}")
    return expected, rows[1:]


def row_dict(header: list[str], row: list[Any]) -> dict[str, Any]:
    padded = list(row) + [""] * max(0, len(header) - len(row))
    return dict(zip(header, padded[:len(header)]))


def row_values(header: list[str], data: dict[str, Any]) -> list[Any]:
    out = []
    for key in header:
        v = data.get(key, "")
        if isinstance(v, (list, dict)):
            v = canonical(v)
        elif v is None:
            v = ""
        out.append(v)
    return out


def upsert_projection(gws: GWS, schema: dict[str, Any], tab: str, data: dict[str, Any]) -> str:
    header, rows = read_table(gws, schema, tab)
    key_name = next(x["key"] for x in schema["tabs"] if x["title"] == tab)
    key = str(data[key_name])
    for idx, row in enumerate(rows, start=2):
        current = row_dict(header, row)
        if str(current.get(key_name, "")) == key:
            desired = row_values(header, data)
            if list(row) + [""] * max(0, len(header)-len(row)) != desired:
                gws.values_update(f"'{tab}'!A{idx}:{col_letter(len(header))}{idx}", [desired])
                return "UPDATED"
            return "UNCHANGED"
    gws.values_append(f"'{tab}'!A:{col_letter(len(header))}", [row_values(header, data)])
    return "APPENDED"


def append_unique(gws: GWS, schema: dict[str, Any], tab: str, data: dict[str, Any]) -> str:
    header, rows = read_table(gws, schema, tab)
    key_name = next(x["key"] for x in schema["tabs"] if x["title"] == tab)
    key = str(data[key_name])
    for row in rows:
        if str(row_dict(header, row).get(key_name, "")) == key:
            return "UNCHANGED"
    gws.values_append(f"'{tab}'!A:{col_letter(len(header))}", [row_values(header, data)])
    return "APPENDED"


def local_receipt(stage: str, input_obj: Any, output_ref: str, status: str = "PASS",
                  error_code: str | None = None, retry_of: str | None = None) -> dict[str, Any]:
    input_hash = "sha256:" + sha256_text(canonical(input_obj))
    run_id = stable_id("run", stage, input_hash)
    return {
        "run_id": run_id,
        "operation_id": stable_id("op", stage, input_hash),
        "stage": stage,
        "tool": "ryan-discover-ai-factory",
        "harness": "local-python",
        "model": "",
        "started_at": utc_now(),
        "finished_at": utc_now(),
        "status": status,
        "input_hash": input_hash,
        "output_ref": output_ref,
        "receipt_ref": output_ref,
        "error_code": error_code or "",
        "retry_of": retry_of or "",
    }


def persist_receipt(receipt: dict[str, Any], artifact_root: Path) -> Path:
    out = artifact_root / "receipts" / (receipt["run_id"] + ".json")
    out.parent.mkdir(parents=True, exist_ok=True)
    if not out.exists():
        out.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return out


def stage_m0_bootstrap(gws: GWS, artifact_root: Path) -> dict[str, Any]:
    schema = load_schema()
    meta = gws.metadata()
    title = (meta.get("properties") or {}).get("title")
    if title != schema["workbook_title"]:
        raise FactoryError(f"workbook title mismatch: {title!r}")
    existing_tabs = [(s.get("properties") or {}).get("title") for s in meta.get("sheets") or []]
    expected_tabs = [x["title"] for x in schema["tabs"]]
    duplicate_tabs = sorted({x for x in existing_tabs if existing_tabs.count(x) > 1})
    if duplicate_tabs:
        raise FactoryError(f"duplicate sheet titles: {duplicate_tabs}")

    added_tabs: list[str] = []
    missing = [x for x in expected_tabs if x not in existing_tabs]
    if missing:
        gws.structural_update([{"addSheet": {"properties": {"title": x}}} for x in missing])
        added_tabs.extend(missing)

    header_writes: list[str] = []
    for tab in schema["tabs"]:
        title = tab["title"]
        header = tab["columns"]
        rows = gws.read(f"'{title}'!A1:{col_letter(len(header))}1")
        if not rows:
            gws.values_update(f"'{title}'!A1:{col_letter(len(header))}1", [header])
            header_writes.append(title)
        elif [str(x) for x in rows[0]] != header:
            raise FactoryError(f"non-empty incompatible header in {title}")

    control = {
        "schema_version": SCHEMA_VERSION,
        "atlas_id": "DISCOVER-AI-RESEARCH-ATLAS",
        "corpus": "Discover AI",
        "authority": "operational_projection_not_ssot",
        "mutation_adapter": "gws CLI",
        "deep_indexer": "Antigravity",
        "build_owner": "Ryan",
    }
    control_states: dict[str, str] = {}
    chead, crows = read_table(gws, schema, "00_Control")
    current_control = {
        str(row_dict(chead, row).get("key", "")): row_dict(chead, row)
        for row in crows if row
    }
    for key, value in control.items():
        current = current_control.get(key)
        if current and str(current.get("value", "")) == value:
            control_states[key] = "UNCHANGED"
            continue
        control_states[key] = upsert_projection(gws, schema, "00_Control", {
            "key": key, "value": value, "updated_at": utc_now(),
            "run_id": "", "notes": "Ryan M0 idempotent bootstrap"
        })

    # Re-read all headers and count tabs after any mutation.
    post = gws.metadata()
    post_tabs = [(s.get("properties") or {}).get("title") for s in post.get("sheets") or []]
    header_ok = {}
    for tab in schema["tabs"]:
        rows = gws.read(f"'{tab['title']}'!A1:{col_letter(len(tab['columns']))}1")
        header_ok[tab["title"]] = bool(rows and [str(x) for x in rows[0]] == tab["columns"])

    summary = {
        "schema": "aspace.discover-ai.m0-evidence.v1",
        "spreadsheet_id": gws.spreadsheet_id,
        "expected_tabs": expected_tabs,
        "tab_count": len(post_tabs),
        "unique_tab_count": len(set(post_tabs)),
        "added_tabs": added_tabs,
        "header_writes": header_writes,
        "all_headers_match": all(header_ok.values()),
        "control_states": control_states,
        "result": "PASS" if post_tabs == expected_tabs and all(header_ok.values()) else "FAIL",
    }
    receipt = local_receipt("M0_SPREADSHEET_BOOTSTRAP", {
        "spreadsheet_id": gws.spreadsheet_id,
        "schema_sha256": sha256_bytes(SCHEMA_PATH.read_bytes()),
    }, "pending")
    rpath = persist_receipt(receipt, artifact_root)
    receipt["output_ref"] = str(rpath)
    receipt["receipt_ref"] = str(rpath)
    rpath.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    append_unique(gws, schema, "11_Runs", receipt)
    summary["run_id"] = receipt["run_id"]
    summary["receipt_ref"] = str(rpath)
    return summary


def ytdlp_argv(explicit: str | None = None) -> list[str]:
    if explicit:
        p = Path(explicit)
        if p.exists():
            return [str(p.resolve())]
    if DEFAULT_YTDLP.exists():
        return [str(DEFAULT_YTDLP.resolve())]
    return executable_argv("yt-dlp")


def ytdlp_json(args: list[str], explicit: str | None = None, timeout: int = 90) -> dict[str, Any]:
    cp = subprocess.run([*ytdlp_argv(explicit), *args], text=True, capture_output=True, timeout=timeout)
    return parse_json_output(cp, "yt-dlp")


def parse_upload_date(value: str | None) -> str:
    if not value or len(value) != 8:
        return ""
    try:
        return dt.datetime.strptime(value, "%Y%m%d").date().isoformat()
    except ValueError:
        return ""


def capture_description(video_id: str, description: str, artifact_root: Path) -> tuple[str, Path]:
    raw = description.encode("utf-8")
    digest = sha256_bytes(raw)
    path = artifact_root / "descriptions" / video_id / f"{digest}.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_bytes(raw)
    return digest, path


def stage_m1_inventory(gws: GWS, artifact_root: Path, *, limit: int = 5,
                       ytdlp: str | None = None) -> dict[str, Any]:
    schema = load_schema()
    flat = ytdlp_json([
        "--flat-playlist", "--playlist-end", str(limit),
        "--dump-single-json", CHANNEL_URL,
    ], ytdlp)
    actual_channel = flat.get("channel_id") or flat.get("id")
    if actual_channel != CHANNEL_ID:
        raise FactoryError(f"Discover AI channel identity mismatch: {actual_channel}")

    entries = flat.get("entries") or []
    channel_row = {
        "channel_id": CHANNEL_ID,
        "handle": CHANNEL_HANDLE,
        "title": flat.get("channel") or flat.get("uploader") or CHANNEL_TITLE,
        "uploads_playlist_id": "",
        "source_url": CHANNEL_URL,
        "inventory_state": "RUNNING",
        "last_inventory_at": utc_now(),
        "video_count_seen": 0,
        "source_run_id": "",
    }
    upsert_projection(gws, schema, "01_Channels", channel_row)

    videos: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    artifact_rows: list[dict[str, Any]] = []
    for entry in entries:
        vid = entry.get("id")
        if not vid:
            continue
        url = entry.get("url") or f"https://www.youtube.com/watch?v={vid}"
        if not str(url).startswith("http"):
            url = f"https://www.youtube.com/watch?v={vid}"
        try:
            detail = ytdlp_json(["--skip-download", "--no-playlist", "--dump-single-json", str(url)], ytdlp)
        except Exception as exc:
            skipped.append({"video_id": vid, "reason": str(exc)})
            continue
        description = detail.get("description") or ""
        digest, path = capture_description(vid, description, artifact_root)
        artifact_id = "sha256:" + digest
        artifact_row = {
            "artifact_id": artifact_id,
            "owner_type": "Video",
            "owner_id": vid,
            "artifact_type": "youtube_description",
            "uri": str(path),
            "sha256": digest,
            "mime_type": "text/plain; charset=utf-8",
            "size_bytes": len(description.encode("utf-8")),
            "capture_method": "yt-dlp",
            "captured_at": utc_now(),
            "source_run_id": "",
        }
        append_unique(gws, schema, "07_Artifacts", artifact_row)
        artifact_rows.append(artifact_row)
        video = {
            "video_id": vid,
            "channel_id": CHANNEL_ID,
            "published_at": parse_upload_date(detail.get("upload_date")),
            "title": detail.get("title") or entry.get("title") or "",
            "url": detail.get("webpage_url") or url,
            "description_hash": "sha256:" + digest,
            "description_artifact_ref": str(path),
            "description_state": "CAPTURED",
            "transcript_state": "NOT_CAPTURED",
            "keyframes_state": "NOT_CAPTURED",
            "citation_count": 0,
            "resolved_paper_count": 0,
            "deep_capture_state": "NOT_SELECTED",
            "first_seen_at": utc_now(),
            "last_seen_at": utc_now(),
            "source_run_id": "",
        }
        videos.append(video)

    receipt = local_receipt("M1_CHANNEL_INVENTORY", {
        "channel_id": CHANNEL_ID,
        "requested_limit": limit,
        "video_ids": [v["video_id"] for v in videos],
        "description_hashes": [v["description_hash"] for v in videos],
    }, "pending")
    rpath = persist_receipt(receipt, artifact_root)
    receipt["output_ref"] = str(rpath)
    receipt["receipt_ref"] = str(rpath)
    rpath.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    run_id = receipt["run_id"]
    for video in videos:
        video["source_run_id"] = run_id
        upsert_projection(gws, schema, "02_Videos", video)
    for art in artifact_rows:
        # Existing artifact IDs stay immutable; source_run_id is provenance on first append.
        art["source_run_id"] = run_id
    append_unique(gws, schema, "11_Runs", receipt)
    channel_row.update({
        "inventory_state": "PASS",
        "last_inventory_at": utc_now(),
        "video_count_seen": len(videos),
        "source_run_id": run_id,
    })
    upsert_projection(gws, schema, "01_Channels", channel_row)
    return {
        "schema": "aspace.discover-ai.m1-evidence.v1",
        "result": "PASS",
        "channel_id": CHANNEL_ID,
        "requested": len(entries),
        "captured": len(videos),
        "skipped": skipped,
        "video_ids": [v["video_id"] for v in videos],
        "run_id": run_id,
        "receipt_ref": str(rpath),
    }


DOI_URL_RE = re.compile(r"https?://(?:dx\.)?doi\.org/(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)", re.I)
DOI_PLAIN_RE = re.compile(r"\b(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)\b", re.I)
ARXIV_URL_RE = re.compile(r"https?://arxiv\.org/(?:abs|pdf)/([A-Za-z.-]+/\d{7}|\d{4}\.\d{4,5})(?:v\d+)?(?:\.pdf)?", re.I)
ARXIV_LABEL_RE = re.compile(r"\barXiv\s*:\s*([A-Za-z.-]+/\d{7}|\d{4}\.\d{4,5})(?:v\d+)?\b", re.I)
OPENREVIEW_RE = re.compile(r"https?://openreview\.net/(?:forum|pdf)\?id=([A-Za-z0-9_-]+)", re.I)
PROVIDER_URL_RE = re.compile(r"https?://(?:www\.)?(?:github\.com|aclanthology\.org|paperswithcode\.com|huggingface\.co/papers|openreview\.net)/(?:[^\s<>]+)", re.I)
TITLE_LINE_RE = re.compile(r"^(?:paper\s*)?(?:title\s*[:\-]|\d+[.)]\s*)(.{12,240})$", re.I)
AUTHORS_LINE_RE = re.compile(r"^(?:authors?\s*[:\-]|by\s+)(.{5,240})$", re.I)


def normalize_direct_id(mode: str, value: str) -> str:
    value = value.strip().rstrip(".,;)]}")
    if "doi" in mode:
        return value.lower()
    if "arxiv" in mode:
        return re.sub(r"v\d+$", "", value, flags=re.I).lower()
    return value


def candidate(video_id: str, kind: str, raw: str, *, url_or_id: str | None = None,
              title: str | None = None, authors: list[str] | None = None,
              confidence: float = 1.0, extraction_mode: str = "deterministic") -> dict[str, Any]:
    if kind not in CANDIDATE_KINDS:
        raise FactoryError(f"invalid candidate_kind: {kind}")
    normalized = normalize_direct_id(extraction_mode or kind, url_or_id) if url_or_id else None
    payload = {
        "candidate_kind": kind,
        "raw_text": raw.strip(),
        "normalized_title": title.strip() if title else None,
        "authors_raw": authors or [],
        "url_or_id": normalized,
        "extraction_mode": extraction_mode,
    }
    return {
        "candidate_id": stable_id("cand", video_id, payload),
        "video_id": video_id,
        **payload,
        "confidence": confidence,
    }


def mine_citations(video_id: str, description: str) -> list[dict[str, Any]]:
    found: dict[str, dict[str, Any]] = {}

    def add(c: dict[str, Any]) -> None:
        found[c["candidate_id"]] = c

    consumed_direct: set[str] = set()
    for m in DOI_URL_RE.finditer(description):
        doi = normalize_direct_id("doi_url", m.group(1))
        consumed_direct.add(doi)
        add(candidate(video_id, "doi_url", m.group(0), url_or_id=doi, extraction_mode="doi_url"))
    for m in ARXIV_URL_RE.finditer(description):
        aid = normalize_direct_id("arxiv_url", m.group(1))
        consumed_direct.add(aid)
        add(candidate(video_id, "arxiv_url", m.group(0), url_or_id=aid, extraction_mode="arxiv_url"))
    for m in OPENREVIEW_RE.finditer(description):
        oid = m.group(1)
        consumed_direct.add(oid.lower())
        add(candidate(video_id, "openreview_url", m.group(0), url_or_id=oid, extraction_mode="openreview_url"))
    for m in DOI_PLAIN_RE.finditer(description):
        doi = normalize_direct_id("doi_plain", m.group(1))
        if doi not in consumed_direct:
            add(candidate(video_id, "doi_plain", m.group(0), url_or_id=doi))
    for m in ARXIV_LABEL_RE.finditer(description):
        aid = normalize_direct_id("arxiv_plain", m.group(1))
        if aid not in consumed_direct:
            add(candidate(video_id, "arxiv_plain", m.group(0), url_or_id=aid))
    for m in PROVIDER_URL_RE.finditer(description):
        url = m.group(0).rstrip(".,;)]}")
        if "openreview.net" in url.lower() and "id=" in url.lower():
            continue
        add(candidate(video_id, "provider_url", url, url_or_id=url, confidence=0.9))

    lines = [x.strip() for x in description.splitlines()]
    for idx, line in enumerate(lines[:-1]):
        tm = TITLE_LINE_RE.match(line)
        am = AUTHORS_LINE_RE.match(lines[idx + 1])
        if tm and am:
            authors = [x.strip() for x in re.split(r",|\band\b", am.group(1)) if x.strip()]
            add(candidate(
                video_id, "bibliographic_block",
                line + "\n" + lines[idx + 1],
                title=tm.group(1), authors=authors,
                confidence=0.8, extraction_mode="deterministic_title_authors",
            ))
    return sorted(found.values(), key=lambda x: x["candidate_id"])


def citation_sheet_row(c: dict[str, Any], run_id: str) -> dict[str, Any]:
    return {
        "candidate_id": c["candidate_id"],
        "video_id": c["video_id"],
        "candidate_kind": c["candidate_kind"],
        "raw_text": c["raw_text"],
        "normalized_title": c.get("normalized_title") or "",
        "authors_raw": c.get("authors_raw") or [],
        "url_or_id": c.get("url_or_id") or "",
        "source_span": c["raw_text"][:500],
        "extraction_mode": c["extraction_mode"],
        "extract_confidence": c["confidence"],
        "resolver_state": "NEW",
        "review_reason": "",
        "source_run_id": run_id,
    }


def stage_m2_mine(gws: GWS, artifact_root: Path, *, video_ids: list[str] | None = None) -> dict[str, Any]:
    schema = load_schema()
    header, rows = read_table(gws, schema, "02_Videos")
    videos = [row_dict(header, r) for r in rows if r and str(r[0]).strip()]
    if video_ids:
        wanted = set(video_ids)
        videos = [v for v in videos if v.get("video_id") in wanted]
    all_candidates: list[dict[str, Any]] = []
    per_video: dict[str, int] = {}
    for v in videos:
        ref = str(v.get("description_artifact_ref") or "")
        if not ref or not Path(ref).exists():
            continue
        description = Path(ref).read_text(encoding="utf-8", errors="replace")
        cs = mine_citations(str(v["video_id"]), description)
        all_candidates.extend(cs)
        per_video[str(v["video_id"])] = len(cs)

    receipt = local_receipt("M2_CITATION_MINER", {
        "videos": sorted(per_video),
        "candidate_ids": [x["candidate_id"] for x in all_candidates],
    }, "pending")
    rpath = persist_receipt(receipt, artifact_root)
    receipt["output_ref"] = str(rpath)
    receipt["receipt_ref"] = str(rpath)
    rpath.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    run_id = receipt["run_id"]

    for c in all_candidates:
        upsert_projection(gws, schema, "03_CitationCandidates", citation_sheet_row(c, run_id))
    append_unique(gws, schema, "11_Runs", receipt)

    # Update citation_count in current video projection without destroying first_seen.
    for v in videos:
        vid = str(v.get("video_id") or "")
        if vid in per_video:
            v["citation_count"] = per_video[vid]
            v["last_seen_at"] = utc_now()
            upsert_projection(gws, schema, "02_Videos", v)

    return {
        "schema": "aspace.discover-ai.m2-evidence.v1",
        "result": "PASS",
        "videos_mined": len(per_video),
        "candidate_count": len(all_candidates),
        "kinds": sorted({x["candidate_kind"] for x in all_candidates}),
        "candidate_ids": [x["candidate_id"] for x in all_candidates],
        "run_id": run_id,
        "receipt_ref": str(rpath),
    }


def direct_paper_identity(c: dict[str, Any]) -> tuple[str, str, str] | None:
    kind = c["candidate_kind"]
    value = str(c.get("url_or_id") or "")
    if kind.startswith("doi"):
        return "doi", value.lower(), "doi:" + value.lower()
    if kind.startswith("arxiv"):
        value = re.sub(r"v\d+$", "", value, flags=re.I).lower()
        return "arxiv", value, "arxiv:" + value
    if kind == "openreview_url":
        return "openreview", value, "openreview:" + value
    return None


def resolve_candidates(candidates: list[dict[str, Any]]) -> dict[str, Any]:
    papers: dict[str, dict[str, Any]] = {}
    edges: dict[str, dict[str, Any]] = {}
    reviews: dict[str, dict[str, Any]] = {}
    candidate_states: dict[str, tuple[str, str]] = {}
    for c in candidates:
        identity = direct_paper_identity(c)
        if identity:
            id_type, canonical_id, paper_id = identity
            papers.setdefault(paper_id, {
                "paper_id": paper_id,
                "canonical_id_type": id_type,
                "canonical_id": canonical_id,
                "doi": canonical_id if id_type == "doi" else "",
                "arxiv_id": canonical_id if id_type == "arxiv" else "",
                "openreview_id": canonical_id if id_type == "openreview" else "",
                "title": c.get("normalized_title") or "",
                "year": "",
                "authors": c.get("authors_raw") or [],
                "abstract_hash": "",
                "abstract_artifact_ref": "",
                "resolver_provider": "direct_id",
                "resolver_confidence": 1.0,
                "review_state": "ACCEPTED",
                "deep_capture_state": "NOT_SELECTED",
                "first_seen_at": utc_now(),
                "last_seen_at": utc_now(),
                "source_run_id": "",
            })
            edge_id = stable_id("edge", c["video_id"], "CITES", paper_id, c["candidate_id"])
            edges[edge_id] = {
                "edge_id": edge_id,
                "video_id": c["video_id"],
                "paper_id": paper_id,
                "relation": "CITES",
                "candidate_id": c["candidate_id"],
                "resolution_confidence": 1.0,
                "provenance_ref": c["candidate_id"],
                "source_run_id": "",
            }
            candidate_states[c["candidate_id"]] = ("RESOLVED", "")
        else:
            review_id = stable_id("review", "CitationCandidate", c["candidate_id"])
            reviews[review_id] = {
                "review_id": review_id,
                "entity_type": "CitationCandidate",
                "entity_id": c["candidate_id"],
                "reason": "bibliographic/provider candidate requires converging resolver evidence",
                "priority": "normal",
                "evidence_refs": [c["candidate_id"]],
                "proposed_action": "resolve_with_bibliographic_provider",
                "owner_capability": "Bill/Graham",
                "state": "OPEN",
                "reviewed_by": "",
                "reviewed_at": "",
                "source_run_id": "",
            }
            candidate_states[c["candidate_id"]] = ("NEEDS_REVIEW", reviews[review_id]["reason"])
    return {
        "papers": list(papers.values()),
        "edges": list(edges.values()),
        "reviews": list(reviews.values()),
        "candidate_states": candidate_states,
    }


def stage_m3_resolve(gws: GWS, artifact_root: Path, *, candidate_ids: list[str] | None = None) -> dict[str, Any]:
    schema = load_schema()
    header, rows = read_table(gws, schema, "03_CitationCandidates")
    raw = [row_dict(header, r) for r in rows if r and str(r[0]).strip()]
    if candidate_ids:
        wanted = set(candidate_ids)
        raw = [x for x in raw if x.get("candidate_id") in wanted]
    candidates = []
    for r in raw:
        authors = r.get("authors_raw")
        if isinstance(authors, str):
            try:
                authors = json.loads(authors) if authors else []
            except json.JSONDecodeError:
                authors = [x.strip() for x in authors.split(",") if x.strip()]
        candidates.append({
            "candidate_id": r["candidate_id"],
            "video_id": r["video_id"],
            "candidate_kind": r["candidate_kind"],
            "raw_text": r.get("raw_text") or "",
            "normalized_title": r.get("normalized_title") or None,
            "authors_raw": authors or [],
            "url_or_id": r.get("url_or_id") or None,
            "extraction_mode": r.get("extraction_mode") or "",
            "confidence": float(r.get("extract_confidence") or 0),
        })
    resolved = resolve_candidates(candidates)
    receipt = local_receipt("M3_PAPER_RESOLVER", {
        "candidate_ids": sorted(x["candidate_id"] for x in candidates),
        "paper_ids": sorted(x["paper_id"] for x in resolved["papers"]),
        "edge_ids": sorted(x["edge_id"] for x in resolved["edges"]),
    }, "pending")
    rpath = persist_receipt(receipt, artifact_root)
    receipt["output_ref"] = str(rpath)
    receipt["receipt_ref"] = str(rpath)
    rpath.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    run_id = receipt["run_id"]

    for p in resolved["papers"]:
        p["source_run_id"] = run_id
        upsert_projection(gws, schema, "04_Papers", p)
    for e in resolved["edges"]:
        e["source_run_id"] = run_id
        append_unique(gws, schema, "05_VideoPaperEdges", e)
    for review in resolved["reviews"]:
        review["source_run_id"] = run_id
        upsert_projection(gws, schema, "10_ReviewQueue", review)

    # Update candidate states and video resolved counts.
    for r in raw:
        state, reason = resolved["candidate_states"].get(r["candidate_id"], ("NEW", ""))
        r["resolver_state"] = state
        r["review_reason"] = reason
        upsert_projection(gws, schema, "03_CitationCandidates", r)

    by_video: dict[str, int] = {}
    for e in resolved["edges"]:
        by_video[e["video_id"]] = by_video.get(e["video_id"], 0) + 1
    vhead, vrows = read_table(gws, schema, "02_Videos")
    for row in vrows:
        v = row_dict(vhead, row)
        vid = str(v.get("video_id") or "")
        if vid in by_video:
            v["resolved_paper_count"] = by_video[vid]
            v["last_seen_at"] = utc_now()
            upsert_projection(gws, schema, "02_Videos", v)

    append_unique(gws, schema, "11_Runs", receipt)
    return {
        "schema": "aspace.discover-ai.m3-evidence.v1",
        "result": "PASS",
        "candidate_count": len(candidates),
        "paper_count": len(resolved["papers"]),
        "edge_count": len(resolved["edges"]),
        "needs_review_count": len(resolved["reviews"]),
        "paper_ids": [x["paper_id"] for x in resolved["papers"]],
        "run_id": run_id,
        "receipt_ref": str(rpath),
    }


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser()
    p.add_argument("--spreadsheet-id", default=load_instance()["spreadsheet_id"])
    p.add_argument("--artifact-root", default=str(DEFAULT_ARTIFACT_ROOT))
    p.add_argument("--ytdlp")
    sub = p.add_subparsers(dest="stage", required=True)

    sub.add_parser("m0")

    p1 = sub.add_parser("m1")
    p1.add_argument("--limit", type=int, default=5)

    p2 = sub.add_parser("m2")
    p2.add_argument("--video-id", action="append", default=[])

    p3 = sub.add_parser("m3")
    p3.add_argument("--candidate-id", action="append", default=[])

    return p


def main() -> int:
    args = build_parser().parse_args()
    artifact_root = Path(args.artifact_root).expanduser().resolve()
    artifact_root.mkdir(parents=True, exist_ok=True)
    gws = GWS(args.spreadsheet_id)
    if args.stage == "m0":
        result = stage_m0_bootstrap(gws, artifact_root)
    elif args.stage == "m1":
        result = stage_m1_inventory(gws, artifact_root, limit=args.limit, ytdlp=args.ytdlp)
    elif args.stage == "m2":
        result = stage_m2_mine(gws, artifact_root, video_ids=args.video_id or None)
    elif args.stage == "m3":
        result = stage_m3_resolve(gws, artifact_root, candidate_ids=args.candidate_id or None)
    else:
        raise AssertionError(args.stage)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result.get("result") == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""A'Space universal IPBD capture hook.

Local-first invariant:
1. append every capture to a durable NDJSON outbox;
2. then attempt remote projection to Agent OS Backend;
3. failures never erase the local record;
4. replay is idempotent through dedupe_key.

No Supabase service-role key is stored or required locally.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


HOME = Path.home()
STATE_DIR = HOME / ".aspace" / "intent"
OUTBOX = STATE_DIR / "outbox.ndjson"
RECEIPTS = STATE_DIR / "receipts.ndjson"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def user_env(name: str) -> str | None:
    value = os.environ.get(name)
    if value:
        return value
    if os.name == "nt":
        try:
            import winreg  # type: ignore

            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as key:
                value, _ = winreg.QueryValueEx(key, name)
                return str(value) if value else None
        except OSError:
            pass
    return None


def append_jsonl(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    with path.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")
        fh.flush()
        os.fsync(fh.fileno())


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows: list[dict] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        try:
            rows.append(json.loads(raw))
        except json.JSONDecodeError:
            rows.append({"_corrupt_line": raw})
    return rows


def default_dedupe(args: argparse.Namespace) -> str:
    if args.source_event_id:
        seed = "|".join([
            args.source_type,
            args.source_ref or "",
            args.source_event_id,
        ])
        return "ipbd:" + hashlib.sha256(seed.encode("utf-8")).hexdigest()
    return "ipbd:" + str(uuid.uuid4())


def build_capture(args: argparse.Namespace) -> dict:
    text = args.text
    if text == "-":
        text = sys.stdin.read()
    text = text.strip()
    if not text:
        raise SystemExit("capture text is empty")

    metadata = json.loads(args.metadata_json) if args.metadata_json else {}
    framework_map = json.loads(args.framework_json) if args.framework_json else {}

    return {
        "outbox_id": str(uuid.uuid4()),
        "outbox_at": now_iso(),
        "kind": args.kind,
        "verbatim": text,
        "source_type": args.source_type,
        "dedupe_key": args.dedupe_key or default_dedupe(args),
        "source_ref": args.source_ref,
        "source_event_id": args.source_event_id,
        "actor": args.actor,
        "raw_payload": {},
        "core": args.core,
        "owner_role": args.owner,
        "framework_map": framework_map,
        "metadata": metadata,
    }


def synced_keys() -> set[str]:
    return {
        row.get("dedupe_key")
        for row in load_jsonl(RECEIPTS)
        if row.get("ok") is True and row.get("dedupe_key")
    }


def post_capture(row: dict) -> dict:
    url = user_env("ASPACE_CAPTURE_URL")
    token = user_env("ASPACE_CAPTURE_TOKEN")
    if not url or not token:
        return {
            "ok": False,
            "retryable": True,
            "error": "capture_endpoint_not_configured",
        }

    payload = {
        key: row.get(key)
        for key in (
            "kind", "verbatim", "source_type", "dedupe_key", "source_ref",
            "source_event_id", "actor", "raw_payload", "core", "owner_role",
            "framework_map", "metadata"
        )
    }
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = Request(
        url,
        data=body,
        method="POST",
        headers={
            "content-type": "application/json",
            "x-aspace-capture-token": token,
        },
    )
    try:
        with urlopen(req, timeout=15) as response:
            data = json.loads(response.read().decode("utf-8"))
            return {
                "ok": bool(data.get("ok")),
                "retryable": False,
                "intent_id": data.get("intent_id"),
                "http_status": response.status,
            }
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:1000]
        return {
            "ok": False,
            "retryable": exc.code >= 500,
            "http_status": exc.code,
            "error": detail,
        }
    except (URLError, TimeoutError, OSError) as exc:
        return {
            "ok": False,
            "retryable": True,
            "error": f"{type(exc).__name__}: {exc}",
        }


def record_receipt(row: dict, result: dict) -> None:
    append_jsonl(
        RECEIPTS,
        {
            "receipt_at": now_iso(),
            "outbox_id": row.get("outbox_id"),
            "dedupe_key": row.get("dedupe_key"),
            **result,
        },
    )


def sync_rows(*, only_dedupe: str | None = None) -> tuple[int, int]:
    done = synced_keys()
    ok_count = 0
    failed_count = 0
    for row in load_jsonl(OUTBOX):
        key = row.get("dedupe_key")
        if not key or key in done:
            continue
        if only_dedupe and key != only_dedupe:
            continue
        result = post_capture(row)
        record_receipt(row, result)
        if result.get("ok"):
            done.add(key)
            ok_count += 1
        else:
            failed_count += 1
    return ok_count, failed_count


def cmd_capture(args: argparse.Namespace) -> int:
    row = build_capture(args)
    append_jsonl(OUTBOX, row)
    print(json.dumps({
        "captured_local": True,
        "outbox_id": row["outbox_id"],
        "dedupe_key": row["dedupe_key"],
        "outbox": str(OUTBOX),
    }, ensure_ascii=False))

    if args.local_only:
        return 0

    ok, failed = sync_rows(only_dedupe=row["dedupe_key"])
    if ok:
        print(json.dumps({"projected_remote": True, "dedupe_key": row["dedupe_key"]}))
        return 0

    print(json.dumps({
        "projected_remote": False,
        "queued_for_retry": True,
        "failed_attempts": failed,
    }))
    return 0


def cmd_sync(_: argparse.Namespace) -> int:
    ok, failed = sync_rows()
    pending = sum(
        1 for row in load_jsonl(OUTBOX)
        if row.get("dedupe_key") not in synced_keys()
    )
    print(json.dumps({
        "synced_now": ok,
        "failed_now": failed,
        "pending": pending,
        "outbox": str(OUTBOX),
        "receipts": str(RECEIPTS),
    }))
    return 0 if failed == 0 else 2


def cmd_status(_: argparse.Namespace) -> int:
    outbox = load_jsonl(OUTBOX)
    receipts = load_jsonl(RECEIPTS)
    done = synced_keys()
    pending = [r for r in outbox if r.get("dedupe_key") not in done]
    print(json.dumps({
        "outbox_rows": len(outbox),
        "successful_receipts": len(done),
        "pending": len(pending),
        "endpoint_configured": bool(user_env("ASPACE_CAPTURE_URL")),
        "token_configured": bool(user_env("ASPACE_CAPTURE_TOKEN")),
    }))
    return 0


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="A'Space universal IPBD capture")
    sub = p.add_subparsers(dest="command", required=True)

    c = sub.add_parser("capture")
    c.add_argument("--kind", default="UNCLASSIFIED",
                   choices=["INTENTION","BESOIN","PROBLEMATIQUE","DESIR","MIXED","UNCLASSIFIED"])
    c.add_argument("--text", required=True, help="verbatim text, or - for stdin")
    c.add_argument("--source-type", default="manual")
    c.add_argument("--source-ref")
    c.add_argument("--source-event-id")
    c.add_argument("--dedupe-key")
    c.add_argument("--actor", default="A0-Amadeus")
    c.add_argument("--core", choices=["A0","KERNEL","LIFE","BUZZ"])
    c.add_argument("--owner")
    c.add_argument("--framework-json")
    c.add_argument("--metadata-json")
    c.add_argument("--local-only", action="store_true")
    c.set_defaults(func=cmd_capture)

    s = sub.add_parser("sync")
    s.set_defaults(func=cmd_sync)

    st = sub.add_parser("status")
    st.set_defaults(func=cmd_status)
    return p


def main() -> int:
    args = parser().parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())

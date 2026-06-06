#!/usr/bin/env python3
"""Repository Health Monitor — watches a repo and reports metrics."""
import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent
CONFIG_PATH = REPO_ROOT / "config.json"
REPORT_PATH = REPO_ROOT / "REPO_HEALTH_REPORT.md"
REPORT_TMP = REPO_ROOT / "REPO_HEALTH_REPORT.tmp.json"


def load_config():
    if CONFIG_PATH.exists():
        try:
            return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {
        "last_scan_path": None,
        "last_scan_timestamp": None,
        "last_known_file_count": None,
        "last_known_total_lines": None,
        "last_known_git_size_bytes": None,
        "last_known_working_size_bytes": None,
    }


def save_config(state):
    CONFIG_PATH.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def is_text_file(path: Path) -> bool:
    try:
        with path.open("rb") as f:
            chunk = f.read(4096)
            if b"\x00" in chunk:
                return False
            return True
    except Exception:
        return False


def count_lines_and_files(root: Path):
    total_lines = 0
    total_files = 0
    skip_dirnames = {".git", "node_modules", "__pycache__", ".venv", "venv"}
    binary_exts = {
        ".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf",
        ".zip", ".tar", ".gz", ".exe", ".dll", ".so", ".dylib",
        ".woff", ".woff2", ".ttf", ".ogg", ".mp3", ".mp4",
    }
    for dirpath, dirnames, filenames in os.walk(root):
        rel_parts = Path(dirpath).relative_to(root).parts
        if any(part in skip_dirnames for part in rel_parts):
            dirnames[:] = []
            continue
        for name in filenames:
            p = Path(dirpath) / name
            if not p.is_file():
                continue
            if p.suffix.lower() in binary_exts:
                continue
            if not is_text_file(p):
                continue
            total_files += 1
            try:
                with p.open("r", encoding="utf-8", errors="ignore") as f:
                    for _ in f:
                        total_lines += 1
            except Exception:
                continue
    return total_files, total_lines


def dir_size(path: Path) -> int:
    total = 0
    for dirpath, _, filenames in os.walk(path):
        for fname in filenames:
            fp = Path(dirpath) / fname
            try:
                total += fp.stat().st_size
            except OSError:
                pass
    return total


def form_delta(label, old, new):
    if old is None:
        return f"{label}: n/a (baseline established)"
    return f"{label}: {new - old:+}"


def run(report_path: Path | None = None, emit_json: bool = False):
    config = load_config()
    now = datetime.now(timezone.utc).isoformat()
    file_count, total_lines = count_lines_and_files(REPO_ROOT)
    git_dir = REPO_ROOT / ".git"
    git_size = dir_size(git_dir) if git_dir.exists() else 0
    working_size = dir_size(REPO_ROOT) - git_size

    churn = 0
    last_ts = config.get("last_scan_timestamp")
    if last_ts:
        try:
            last_dt = datetime.fromisoformat(last_ts)
            for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
                rel_parts = Path(dirpath).relative_to(REPO_ROOT).parts
                if ".git" in rel_parts or any(part in skip_dirnames for part in rel_parts):
                    dirnames[:] = []
                    continue
                for name in filenames:
                    p = Path(dirpath) / name
                    if not p.is_file():
                        continue
                    if p.suffix.lower() in binary_exts:
                        continue
                    if not is_text_file(p):
                        continue
                    try:
                        if datetime.fromtimestamp(p.stat().st_mtime, tz=timezone.utc) > last_dt:
                            churn += 1
                    except OSError:
                        pass
        except Exception:
            churn = 0

    payload = {
        "timestamp": now,
        "path": str(REPO_ROOT),
        "total_text_files": file_count,
        "total_lines": total_lines,
        "git_size_bytes": git_size,
        "working_size_bytes": working_size,
        "files_changed_since_last_scan": churn,
        "last_scan_timestamp": last_ts,
        "line_delta": total_lines - config["last_known_total_lines"] if config.get("last_known_total_lines") is not None else None,
        "git_size_delta": git_size - config["last_known_git_size_bytes"] if config.get("last_known_git_size_bytes") is not None else None,
        "working_size_delta": working_size - config["last_known_working_size_bytes"] if config.get("last_known_working_size_bytes") is not None else None,
    }

    state = {
        "last_scan_path": str(REPO_ROOT),
        "last_scan_timestamp": now,
        "last_known_file_count": file_count,
        "last_known_total_lines": total_lines,
        "last_known_git_size_bytes": git_size,
        "last_known_working_size_bytes": working_size,
    }
    save_config(state)

    if emit_json:
        print(json.dumps(payload, indent=2))
        return payload

    print(f"[HEALTH_SCAN] {now}")
    print(f"  Path            : {REPO_ROOT}")
    print(f"  Text files      : {file_count:,}")
    print(f"  Total lines     : {total_lines:,}")
    print(f"  .git size       : {git_size:,} bytes")
    print(f"  Working size    : {working_size:,} bytes")
    print(f"  Changed files   : {churn} since last scan")
    print(f"  Last scan       : {last_ts or 'N/A (first run)'}")
    if payload["line_delta"] is not None:
        print(f"  +Line delta     : {payload['line_delta']:+}")
    if payload["git_size_delta"] is not None:
        print(f"  +Git size delta : {payload['git_size_delta']:+}")
    if payload["working_size_delta"] is not None:
        print(f"  +Work size delta: {payload['working_size_delta']:+}")

    if report_path:
        report = REPORT_PATH.read_text(encoding="utf-8") if REPORT_PATH.exists() else ""
        body = "\n".join([
            "# REPO_HEALTH_REPORT",
            "",
            f"- Generated: {now}",
            f"- Path: {REPO_ROOT}",
            "",
            "```json",
            json.dumps(payload, indent=2),
            "```",
        ])
        if report != body:
            REPORT_PATH.write_text(body + "\n", encoding="utf-8")


binary_exts = set()
skip_dirnames = {".git"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="Emit JSON only")
    parser.add_argument("--report", action="store_true", help="Also write REPO_HEALTH_REPORT.md")
    args = parser.parse_args()
    payload = run(emit_json=True) if args.json else run(report_path=REPORT_PATH if args.report else None)


if __name__ == "__main__":
    main()

# ARCHITECTURE: Repository Health Monitor

## Goal
Automated monitor that watches a repository for changes and produces a health report.

## Scope
Watches the current working directory (cwd). Measures size, churn, and git state.

## Components

### 1. `config.json` — Baseline Store
Persists the last scan state so we can diff between runs.
Fields:
- `last_scan_path`: absolute path to the monitored repo
- `last_scan_timestamp`: ISO 8601
- `last_known_file_count`: int
- `last_known_total_lines`: int
- `last_known_git_size_bytes`: int
- `last_known_working_size_bytes`: int

### 2. `monitor.py` — Core Scanner
Python script, no external deps (stdlib only). Responsibilities:
- Load `config.json` if present; else initialize empty baseline
- Recursively count total lines in all text files (skip binary by extension/head-check)
- Count files modified since `last_scan_timestamp` (using `os.path.getmtime`)
- Measure `.git` directory size vs. working tree size (excluding `.git`)
- Write updated baseline back to `config.json`
- Print results as structured text to stdout

CLI contract:
```
python monitor.py [--json]
```
- Default: human-readable multiline output
- `--json`: emit JSON only (for piping to report generator)

### 3. `health_check.sh` — Entry Point
Bash wrapper that:
- Sets repo root (default: script's parent dir)
- Runs `python monitor.py --json`
- Writes output to `REPO_HEALTH_REPORT.md` with a timestamped header

Output artifact: `REPO_HEALTH_REPORT.md` containing:
- Title and generation timestamp
- The JSON health payload

## Data Flow
```
health_check.sh
  → monitor.py (stdout JSON)
    → REPO_HEALTH_REPORT.md (written by shell)
```

## Constraints
- No third-party Python packages
- Works on Windows (git-bash / MSYS shell) and Linux
- Idempotent: safe to run repeatedly; baseline updates in-place

## Future Extensions (out of scope for v1)
- Alert thresholds (warn if churn > N%)
- E-mail / Telegram push
- Time-series history in a log dir

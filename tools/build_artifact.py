#!/usr/bin/env python3
"""Derive the Claude Artifact preview file from index.html.

The published page and the artifact are the same document, but the artifact
host supplies its own <!doctype>/<html>/<head>/<body> skeleton. This strips the
wrapper and keeps <title>, <style> and the body content, so index.html stays
the single source of truth.

    python3 tools/build_artifact.py
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "index.html"
OUT = ROOT / "artifact.html"


def grab(pattern: str, html: str, what: str) -> str:
    match = re.search(pattern, html, re.S | re.I)
    if not match:
        sys.exit(f"build_artifact: no {what} found in {SRC.name}")
    return match.group(1).strip()


def main() -> None:
    html = SRC.read_text(encoding="utf-8")
    title = grab(r"<title>(.*?)</title>", html, "<title>")
    style = grab(r"<style>(.*?)</style>", html, "<style>")
    body = grab(r"<body[^>]*>(.*?)</body>", html, "<body>")

    OUT.write_text(
        f"<title>{title}</title>\n<style>\n{style}\n</style>\n\n{body}\n",
        encoding="utf-8",
    )
    print(f"build_artifact: wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()

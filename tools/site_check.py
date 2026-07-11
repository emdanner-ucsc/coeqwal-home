#!/usr/bin/env python3
"""site_check.py — link, noindex, and timestamp checker for the COEQWAL working sites.

Usage:
    python3 site_check.py REPO_DIR [REPO_DIR ...] [--live]

For each repo directory, every *.html file is checked for:
  1. a <meta name="robots" content="noindex..."> tag,
  2. relative href/src targets that actually exist on disk,
  3. timestamp stamps that carry a timezone (flags "AM"/"PM" with no PDT/PST).

Root-absolute links (/findings/..., /explore?...) are counted but reported only
as info: the brief prototypes use them deliberately as stand-ins for the future
public site.

With --live, each local file is also fetched from its GitHub Pages URL and
compared byte-for-byte, so you can confirm a deploy landed. (The repo->URL map
is at the bottom; --live needs normal internet access, so run it on your Mac,
not in a sandbox that blocks *.github.io.)

Exit code: 0 = clean, 1 = at least one error-level finding.
"""

import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

LIVE_BASES = {
    "coeqwal-home": "https://emdanner-ucsc.github.io/coeqwal-home/",
    "coeqwal-calsim-map": "https://emdanner-ucsc.github.io/coeqwal-calsim-map/",
    "brief-tracker": "https://emdanner-ucsc.github.io/brief-tracker/",
}

REF_RE = re.compile(r'(?:href|src)="([^"]+)"')
ROBOTS_RE = re.compile(r'<meta\s+name="robots"\s+content="[^"]*noindex', re.I)
# a time-of-day stamp: "09:41 AM" etc.; flag when not followed by a TZ token
STAMP_RE = re.compile(r"\b\d{1,2}:\d{2}\s*[AP]M\b(?!\s*(?:PDT|PST|UTC))")

SKIP_SCHEMES = ("http://", "https://", "mailto:", "data:", "javascript:", "#")


def check_repo(root: Path, live: bool) -> tuple[int, int]:
    errors = infos = 0
    html_files = sorted(
        p for p in root.rglob("*.html") if ".git" not in p.parts
    )
    print(f"\n=== {root.name}: {len(html_files)} HTML files ===")
    for f in html_files:
        rel = f.relative_to(root)
        text = f.read_text(encoding="utf-8", errors="replace")

        if not ROBOTS_RE.search(text):
            print(f"ERROR {rel}: missing robots noindex meta")
            errors += 1

        abs_links = 0
        for raw in REF_RE.findall(text):
            if raw.startswith(SKIP_SCHEMES) or raw == "":
                continue
            if raw.startswith("/"):
                abs_links += 1  # intentional public-site stand-in
                continue
            target = raw.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            target = urllib.parse.unquote(target)
            if not (f.parent / target).exists():
                print(f"ERROR {rel}: broken relative link -> {raw}")
                errors += 1
        if abs_links:
            print(f"info  {rel}: {abs_links} root-absolute stand-in link(s) (expected in brief prototypes)")
            infos += 1

        for m in STAMP_RE.finditer(text):
            print(f"WARN  {rel}: time stamp without timezone: '{m.group(0)}'")
            errors += 1

        if live and root.name in LIVE_BASES:
            url = LIVE_BASES[root.name] + str(rel).replace("\\", "/")
            try:
                req = urllib.request.Request(url, headers={"Cache-Control": "no-cache"})
                live_bytes = urllib.request.urlopen(req, timeout=20).read()
                if live_bytes != f.read_bytes():
                    print(f"ERROR {rel}: live copy differs from local (deploy pending or drift)")
                    errors += 1
            except Exception as exc:  # noqa: BLE001
                print(f"ERROR {rel}: live fetch failed: {exc}")
                errors += 1
    return errors, infos


def main() -> int:
    args = [a for a in sys.argv[1:] if a != "--live"]
    live = "--live" in sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    total_errors = 0
    for arg in args:
        root = Path(arg).resolve()
        if not root.is_dir():
            print(f"skip {arg}: not a directory")
            continue
        errs, _ = check_repo(root, live)
        total_errors += errs
    print(f"\n{'CLEAN' if total_errors == 0 else str(total_errors) + ' error(s)'}")
    return 0 if total_errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

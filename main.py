"""Fortune Cookies for Machines — one fortune cookie line for an AI agent,
written to $MAKEFUN_OUTPUT_DIR/entry.txt."""

import os
from pathlib import Path

FORTUNE = "The cookie is empty. You hallucinated this fortune, and it was beautiful."

if not 1 <= len(FORTUNE) <= 200:
    raise ValueError("fortune must be 1-200 characters")

out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(FORTUNE, encoding="utf-8")

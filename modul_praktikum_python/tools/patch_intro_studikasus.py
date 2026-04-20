"""Sisipkan \\introstudikasuskode antara \\subsection{Kode:...} dan \\begin{lstlisting}."""
from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1] / "modul"


def patch_text(text: str) -> tuple[str, int]:
    before = text.count("\\introstudikasuskode")
    # Hindari penyisipan ganda
    text = re.sub(
        r"(\\subsection\{Kode:[^\n]+\})\n(\\introstudikasuskode\n)?(\\begin\{lstlisting\})",
        r"\1\n\\introstudikasuskode\n\3",
        text,
    )
    after = text.count("\\introstudikasuskode")
    return text, after - before


def main() -> None:
    total = 0
    for p in sorted(ROOT.glob("modul-*.tex")):
        if p.name == "modul-00.tex":
            continue
        raw = p.read_text(encoding="utf-8")
        new, delta = patch_text(raw)
        if new != raw:
            p.write_text(new, encoding="utf-8")
            print(f"{p.name}: inserted {delta}")
            total += delta
    print("total new lines (approx):", total)


if __name__ == "__main__":
    main()

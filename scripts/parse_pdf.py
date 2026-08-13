#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pymupdf4llm"]
# ///

from argparse import ArgumentParser
from pathlib import Path

import pymupdf4llm


def parse_one(pdf: Path) -> Path:
    """Parse one PDF into Markdown at literature/corpus/<stem>.md.

    Images are not extracted. Returns the markdown path. Raises FileExistsError
    if the output file already exists.
    """
    pdf = pdf.resolve()
    if not pdf.is_file() or pdf.suffix.lower() != ".pdf":
        raise ValueError(f"input must be an existing PDF: {pdf}")

    repo_root = Path(__file__).resolve().parents[1]
    markdown_path = repo_root / "literature" / "corpus" / f"{pdf.stem}.md"

    if markdown_path.exists():
        raise FileExistsError(f"output already exists: {markdown_path}")

    markdown = pymupdf4llm.to_markdown(pdf, write_images=False)
    markdown_path.write_text(markdown)
    return markdown_path


def main() -> int:
    parser = ArgumentParser(
        description="Parse one PDF into Markdown with pymupdf4llm (no images)."
    )
    parser.add_argument("pdf", type=Path)
    args = parser.parse_args()

    try:
        markdown_path = parse_one(args.pdf)
    except (ValueError, FileExistsError) as e:
        parser.error(str(e))
    print(f"Parsed: {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

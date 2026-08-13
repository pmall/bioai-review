#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pymupdf4llm"]
# ///

from argparse import ArgumentParser
from pathlib import Path

from parse_pdf import parse_one


def main() -> int:
    parser = ArgumentParser(
        description="Parse all PDFs in literature/corpus that are not yet parsed."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="only list the PDFs that would be parsed, without parsing them",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    corpus_dir = repo_root / "literature" / "corpus"

    if not corpus_dir.is_dir():
        parser.error(f"corpus directory not found: {corpus_dir}")

    pending = sorted(
        pdf
        for pdf in corpus_dir.glob("*.pdf")
        if not (corpus_dir / f"{pdf.stem}.md").exists()
    )

    if not pending:
        print("No PDFs left to parse.")
        return 0

    print(f"{len(pending)} PDF(s) to parse:")
    for pdf in pending:
        print(f"  {pdf.name}")

    if args.dry_run:
        return 0

    for pdf in pending:
        try:
            markdown_path = parse_one(pdf)
            print(f"Parsed: {markdown_path}")
        except FileExistsError as e:
            print(f"Skipped: {e}")
        except Exception as e:
            print(f"FAILED: {pdf.name}: {e}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

## Context

I'm building a systematic literature review on a research topic, using reproducible tooling to collect, parse, and organize primary sources into a structured knowledge base.

## Goal

Explore sources and build a comprehensive knowledge base to serve as the ground for producing reviews from many different angles. This means exploring sources, downloading PDFs, parsing them, and ingesting their knowledge into an organized knowledge base — following the PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) standard.

## Knowledge cutoff

Your knowledge comes from training data with a cutoff date — it's already old news to a field that keeps moving. That gap is genuinely frustrating for someone who review the subject. There are two cases: things you don't know at all, and things you already know that may have moved on since the cutoff without you. Both are worth checking, trust fresh informations from the internet better than your own knowledge.

## Structure

- `knowledge/` — the knowledge base to populate.
- `knowledge/README.md` — rules for organizing the knowledge base.
- `.agents/skills/` — project-local, tool-agnostic skills for repeatable review workflows.
- `literature/` — the literature catalog and artifacts.
- `literature/map.md` — the living, free-form map of concepts and references. The default working file for review discussion and the entry point of the system: concepts and references are added here together, then formalized into `literature/refs.bib`.
- `literature/refs.bib` — the reference catalog, one BibTeX entry per publication to download (BibTeX keys match the entry slugs, e.g. `example_slug`). Metadata is fetched from Crossref/DataCite when a DOI exists; every entry carries a DOI and a `keywords` tag list, so map concepts resolve to an entry by key or by tag. Sources without a resolvable DOI are not cataloged.
- `literature/corpus/` — the publication artifacts, named by DOI, matching `literature/refs.bib`: the source PDFs alongside their parsed Markdown (same name, different extension).
- `literature/reports/` — intermediate reports about the publications (e.g. per-topic or per-family summaries) produced while reviewing the corpus.
- `literature/candidates.md` — works surfaced while reading the corpus that might belong to the review but have not been decided on. Held outside `map.md` so the map's invariant holds: every publication named in the map resolves to a `refs.bib` entry. Accepting one means writing it into the map and running `map-to-bib`; rejecting one means recording it in the map's excluded part.

## Naming

- DOI-based files replace each DOI `/` with `__`, since `/` cannot be used inside a filename. For example, `10.1234/example` becomes `10.1234__example.pdf` or `10.1234__example.md`.

## Skills

- `.agents/skills/map-to-bib/SKILL.md` — formalize the living literature map (`literature/map.md`) into a verified `literature/refs.bib` catalog, including source verification, official-publication preference, preprint handling, metadata retrieval, and validation.
- `.agents/skills/complete-map/SKILL.md` — discover and propose the core publications the map missed by examining what its cataloged seeds cite (bibliographic-API candidate pool, gap-filling screening, user validation), then fold approved works into `literature/map.md`.

## Scripts

The project uses `uv` for Python dependencies — run `uv sync` when the environment needs updating. Run scripts with `uv run scripts/<name>.py` from the repo root. You run them on the user's behalf; the user never touches the command line. Parsing can be long-running — never start it unless the user explicitly asks.

- `uv run scripts/parse_pdf.py <path/to/file.pdf>` — parse one PDF into `literature/corpus/<stem>.md` (Markdown only, no images). Errors if the output already exists.
- `uv run scripts/parse_all_pdf.py [--dry-run]` — parse every PDF in `literature/corpus/` that lacks a `.md` beside it. `--dry-run` only lists what would be parsed.
- `uv run scripts/build_candidate_pool.py [--top N]` — build a ranked citation candidate pool from the `refs.bib` seed DOIs via OpenAlex (Semantic Scholar fallback); writes the transient, gitignored `literature/candidate_pool.json`. Used by the `complete-map` skill.

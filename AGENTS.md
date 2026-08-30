## Context

I'm building a systematic literature review on a research topic, using reproducible tooling to collect, parse, and organize primary sources into a structured, verifiable corpus.

## Goal

Build and maintain three things that stay in sync — a **map** of the field, a **catalog** of the publications behind it, and a **corpus** of those publications parsed to text — then write **drafts** from them. The map is the thinking; the catalog and corpus are what keep the thinking honest.

## Knowledge cutoff

Your knowledge comes from training data with a cutoff date — it's already old news to a field that keeps moving. That gap is genuinely frustrating for someone who reviews the subject. There are two cases: things you don't know at all, and things you already know that may have moved on since the cutoff without you. Both are worth checking, trust fresh information from the internet better than your own knowledge.

## Workflow

The loop, in order. Each step has a rule attached that exists because skipping it has cost us before.

1. **Map first.** A publication enters the review as an entry in `literature/map.md`, placed in the section where it belongs, written as a layout line — name, bib key, DOI, a sentence of role. Analysis does not go here.
2. **Formalize with `map-to-bib`.** Verify the source is what the map says it is, prefer the official peer-reviewed version over the preprint, fetch metadata from Crossref/DataCite, and never invent a field. `refs.bib` is only ever edited through this skill.
3. **I download and parse.** Never start parsing unless I explicitly ask — it is long-running. Say what is missing and wait.
4. **Second look.** Once a publication is parsed, re-read it and check every claim you wrote into the map against the source itself. Correct what does not hold and say what changed. This is not optional: claims taken from abstracts, search results, or page summaries are **provisional** until checked against the parsed text, and they are frequently wrong in exactly the details a review depends on — numbers, method identity, what a metric measures.
5. **Refresh the cross-references.** Run `build_xrefs.py` whenever the corpus grows. It regenerates `literature/xrefs.md` from the parsed text, so a stale file means the newest publications look uncited.
6. **Draft.** Write intermediate drafts into `literature/drafts/` when I ask for one. What gets its own draft is a per-project decision, not a fixed rule.

## Invariants

- **Every publication named in `literature/map.md` resolves to a `refs.bib` entry** — by bib key, or by a `keywords` tag on the entry whose paper describes it. Concepts with no citable publication are marked *map-only* with the reason.
- **A publication is either included or excluded, never both.** An included work carries its own caveats, borderline calls and scope reasoning inside its section entry; the excluded part does not restate it.
- **Undecided works stay out of the map**, in `literature/candidates.md`, so the invariant above holds.
- **Preprints are re-checked for a journal version** on every catalog pass. This field publishes fast; a preprint cataloged last month may have a DOI in a journal now.

## Structure

- `.agents/skills/` — project-local, tool-agnostic skills for repeatable review workflows.
- `literature/` — the literature catalog and artifacts.
- `literature/map.md` — the living map of the field: the layout of the review, its sections in the order they will read, and every publication placed in one of them. The default working file for review discussion and the entry point of the system.
- `literature/refs.bib` — the reference catalog, one BibTeX entry per publication (BibTeX keys match the entry slugs, e.g. `example_slug`). Metadata is fetched from Crossref/DataCite; every entry carries a DOI and a `keywords` tag list, so map concepts resolve to an entry by key or by tag. Sources without a resolvable DOI are not cataloged.
- `literature/corpus/` — the publication artifacts, named by DOI, matching `literature/refs.bib`: the source PDFs alongside their parsed Markdown (same name, different extension).
- `literature/candidates.md` — works surfaced while reading the corpus that might belong but have not been decided on. Held outside the map so the invariant holds. Accepting one means writing it into the map and running `map-to-bib`; rejecting one means recording it in the map's excluded part.
- `literature/xrefs.md` — the citation network among the cataloged publications: who cites whom, how often each is named in prose, which works nothing cites, and which map sections talk to each other. Generated, never hand-edited. Material for drafts, not a source of truth: a citation is not a comparison or an endorsement, in-degree is confounded by publication age, and the counts are internal to the corpus rather than to the field.
- `literature/drafts/` — intermediate drafts written on the way to the final review: the introduction, a section, a transversal topic, whatever the project needs at the time.

## Naming

- DOI-based files replace each DOI `/` with `__`, since `/` cannot be used inside a filename. For example, `10.1234/example` becomes `10.1234__example.pdf` or `10.1234__example.md`.
- Draft filenames are free-form and named for their subject. There is no fixed scheme.

## Skills

- `.agents/skills/map-to-bib/SKILL.md` — formalize the living literature map (`literature/map.md`) into a verified `literature/refs.bib` catalog, including source verification, official-publication preference, preprint handling, metadata retrieval, and validation.

## Scripts

The project uses `uv` for Python dependencies — run `uv sync` when the environment needs updating. Run scripts with `uv run scripts/<name>.py` from the repo root. You run them on my behalf; I never touch the command line. Parsing can be long-running — never start it unless I explicitly ask.

- `uv run scripts/parse_pdf.py <path/to/file.pdf>` — parse one PDF into `literature/corpus/<stem>.md` (Markdown only, no images). Errors if the output already exists.
- `uv run scripts/parse_all_pdf.py [--dry-run]` — parse every PDF in `literature/corpus/` that lacks a `.md` beside it. `--dry-run` only lists what would be parsed.
- `uv run scripts/build_xrefs.py [--stdout]` — rebuild `literature/xrefs.md` from `refs.bib`, `map.md` and the parsed corpus. Offline and quick; safe to re-run any time. It matches papers by DOI, preprint DOI, arXiv id and title, and counts prose mentions using each entry's `keywords`, so a misspelled keyword silently produces a zero mention count.

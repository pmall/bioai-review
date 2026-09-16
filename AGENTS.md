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
3. **I download, you parse.** Getting the PDF is mine — I hand you the file or drop it in `literature/corpus/`. Parsing is yours: run it yourself as soon as a PDF lands, without asking. It is cheap (`pymupdf4llm`, seconds per paper). Say what is missing and wait only when the PDF itself is missing.
4. **Second look.** Once a publication is parsed, re-read it and check every claim you wrote into the map against the source itself. Correct what does not hold and say what changed. This is not optional: claims taken from abstracts, search results, or page summaries are **provisional** until checked against the parsed text, and they are frequently wrong in exactly the details a review depends on — numbers, method identity, what a metric measures.
5. **Refresh the cross-references.** Run `build_xrefs.py` whenever the corpus grows. It regenerates `literature/xrefs.md` from the parsed text, so a stale file means the newest publications look uncited.
6. **Draft.** Write intermediate drafts into `literature/drafts/` when I ask for one. What gets its own draft is a per-project decision, not a fixed rule.

## Invariants

- **Every publication named in `literature/map.md` resolves to a `refs.bib` entry** — by bib key, or by a `keywords` tag on the entry whose paper describes it. Concepts with no citable publication are marked *map-only* with the reason.
- **The map holds only what is in the review.** Undecided and excluded works live in `literature/candidates.md` with their reason, so the invariant above holds and no decision is re-litigated. An included work carries its own caveats, borderline calls and scope reasoning inside its section entry.
- **Excluded is not uncited.** A work excluded from the argument's structure stays in `refs.bib` and the corpus, and may still be quoted in the review — the catalog records what was obtained, the map records what is in scope.
- **Preprints are re-checked for a journal version** on every catalog pass. This field publishes fast; a preprint cataloged last month may have a DOI in a journal now.
- **Every map entry carries a tier** — `**backbone**`, `**meat**` or `**mention**`, placed after the DOI. See below.

## Tiers

Not every publication deserves the same weight. Each map entry carries one tier, written after its DOI as `· **backbone**`, so the intended writing weight is visible in the layout rather than rediscovered each time a section gets drafted.

The tier answers **how much of the review's argument rests on this work** — nothing else:

| Tier | Test | Consequence when drafting |
|---|---|---|
| **backbone** | Remove it and a beat of the review's argument, or a section's organizing fact, collapses | Analysed in full: mechanism, numbers, caveats, and what it is being contrasted with |
| **meat** | It supplies evidence a backbone claim rests on, but that claim survives if another work substitutes for it | Described and cited; its numbers may be quoted; no mechanism walkthrough |
| **mention** | It establishes that a category exists, or is a date on a timeline | One sentence. No numbers, no mechanism |

Rules that keep the tier honest:

- **Tier is not quality, novelty, or citation count.** A famous paper the argument does not lean on is a *mention*; an obscure one that anchors a section is *backbone*. Never derive a tier from `xrefs.md` — in-degree there is confounded by publication age and is corpus-internal.
- **Tier is per-claim, so state which claim.** A work is backbone *for something*. Where the tier is not self-evident from the entry, name the beat or organizing fact it carries — that is what makes the tier checkable, and what makes it re-derivable when the argument moves.
- **The tier is a property of the argument, not of the paper**, so it changes when the argument changes. Re-check tiers when a beat is rewritten or a section is reordered, not when a new paper arrives.
- **Every backbone entry names a distinct claim; the count per section is not a target.** A lineage or topic that spans more of the field legitimately anchors more of the review, and a section carrying many backbone entries is reporting that breadth rather than failing a quota. What makes a tier wrong is two backbone entries carrying the *same* claim, or a section with no backbone at all, which is a survey with no anchor.
- **Map-only concepts are tiered as well.** Having no publication does not make a concept argumentatively light; something the field cannot cite can still anchor a section.

## Structure

- `.agents/skills/` — project-local, tool-agnostic skills for repeatable review workflows.
- `literature/` — the literature catalog and artifacts.
- `literature/map.md` — the living map of the field: the layout of the review, its sections in the order they will read, and every publication placed in one of them. The default working file for review discussion and the entry point of the system.
- `literature/refs.bib` — the reference catalog, one BibTeX entry per publication (BibTeX keys match the entry slugs, e.g. `example_slug`). Metadata is fetched from Crossref/DataCite; every entry carries a DOI and a `keywords` tag list, so map concepts resolve to an entry by key or by tag. Sources without a resolvable DOI are not cataloged.
- `literature/corpus/` — the publication artifacts, named by DOI, matching `literature/refs.bib`: the source PDFs alongside their parsed Markdown (same name, different extension).
- `literature/candidates.md` — the decision log for everything outside the review: works surfaced while reading the corpus but not yet judged, and works retrieved, read and then judged out of scope, each with its reason. Held outside the map so the invariant holds. Accepting one means writing it into the map and running `map-to-bib`; rejecting one means moving it to the excluded part of the same file.
- `literature/xrefs.md` — the citation network among the cataloged publications: who cites whom, how often each is named in prose, which works nothing cites, and which map sections talk to each other. Generated, never hand-edited. Material for drafts, not a source of truth: a citation is not a comparison or an endorsement, in-degree is confounded by publication age, and the counts are internal to the corpus rather than to the field.
- `literature/drafts/` — intermediate drafts written on the way to the final review: the introduction, a section, a transversal topic, whatever the project needs at the time.

## Naming

- DOI-based files replace each DOI `/` with `__`, since `/` cannot be used inside a filename. For example, `10.1234/example` becomes `10.1234__example.pdf` or `10.1234__example.md`.
- Draft filenames are free-form and named for their subject. There is no fixed scheme.

## Skills

- `.agents/skills/map-to-bib/SKILL.md` — formalize the living literature map (`literature/map.md`) into a verified `literature/refs.bib` catalog, including source verification, official-publication preference, preprint handling, metadata retrieval, and validation.

## Scripts

The project uses `uv` for Python dependencies — run `uv sync` when the environment needs updating. Run scripts with `uv run scripts/<name>.py` from the repo root. You run all of them yourself, unprompted, including parsing; I never touch the command line.

- `uv run scripts/parse_pdf.py <path/to/file.pdf>` — parse one PDF into `literature/corpus/<stem>.md` (Markdown only, no images). Errors if the output already exists.
- `uv run scripts/parse_all_pdf.py [--dry-run]` — parse every PDF in `literature/corpus/` that lacks a `.md` beside it. `--dry-run` only lists what would be parsed.
- `uv run scripts/build_xrefs.py [--stdout]` — rebuild `literature/xrefs.md` from `refs.bib`, `map.md` and the parsed corpus. Offline and quick; safe to re-run any time. It matches papers by DOI, preprint DOI, arXiv id and title, and counts prose mentions using each entry's `keywords`, so a misspelled keyword silently produces a zero mention count.

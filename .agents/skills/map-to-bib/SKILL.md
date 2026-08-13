---
name: map-to-bib
description: Convert the living literature map into a verified BibTeX catalog, preferring official publications over preprints and preserving unresolved sources for review.
---

# Map To BibTeX

Use this skill when a project needs to convert `literature/map.md` into or update `literature/refs.bib`. This skill covers source analysis, publication verification, DOI selection, metadata retrieval, BibTeX generation, and validation. PDF downloading and PDF parsing are separate workflows and must not be performed here.

## Project Convention

The expected project layout is:

```text
literature/
├── map.md
├── refs.bib
└── corpus/
```

`literature/map.md` is the living discovery input: a free-form, project-specific map of concepts and references maintained together with the user. `literature/refs.bib` is the authoritative reference catalog. Keep the catalog machine-readable and git-compatible.

`literature/refs.bib` is a catalog of publications to download and parse. Every entry must have a resolvable DOI. Map concepts resolve to entries by BibTeX key or by a `keywords` tag: components, modules, and aliases without an independent publication become tags on the parent publication, not separate entries. Sources without a clear DOI are dismissed from the catalog and may re-enter when writing the knowledge base or the review.

## Workflow

### 1. Read And Inventory The Map

Read the complete `literature/map.md` before editing anything.

The map is informal and adapted to the review; there is no enforced schema. Use judgment to extract every named source (a concept can be a model, tool, platform, module, or lineage), along with its links, roles, and groupings. Expand grouped entries into separate records when they refer to separate papers or releases, for example:

- A project released in two major versions, each with its own paper
- A software framework and a companion evaluation tool published separately
- A model family published in two distinct papers

Distinguish among:

- A research publication
- A preprint
- A conference proceedings paper
- A software repository
- A commercial platform
- A component or module of another project

Do not assume that every name in the map has an independent publication. A component or module of a published project (for example a plugin bundled into a platform's release) is not a separate entry: it becomes a `keywords` tag on the parent publication.

### 2. Treat Map Links As Discovery Hints

Links in `literature/map.md` are starting points, not authoritative bibliographic metadata. Verify that each link actually corresponds to the named source.

The map may contain stale, incorrect, redirected, or mismatched links. If a link resolves to a different paper, do not preserve it as the source's publication link. Find the correct publication and record the discrepancy for the user or in a note.

### 3. Resolve The Best Available Publication

For each research source, search in this order:

1. Official publisher or journal page
2. Crossref DOI metadata
3. DataCite DOI metadata
4. Official conference proceedings
5. Preprint servers (for example arXiv or a field-specific server)
6. OpenReview
7. Author, laboratory, or project repository

Use current web sources and verify that the title, authors, and subject match the map entry. Do not rely only on a search-result title or an unverified repository description.

### 4. Publication Preference

Prefer the official peer-reviewed publication whenever one exists.

- Use the official publication DOI as the primary `doi` field.
- Use the official publisher or proceedings URL as the primary `url` field.
- If a preprint also matters, record it in `note`, an additional URL field if the chosen BibTeX style supports it, or a clearly labeled related entry.
- Use a preprint when no official publication can be found.
- Mark preprints explicitly as not yet peer-reviewed.
- Do not replace an official publication with a preprint merely because the preprint is easier to access.

The policy is about publication status, not DOI prefix. A preprint-server DOI is still a preprint DOI; a DOI alone does not establish peer review.

### 5. Never Invent Metadata

Never fabricate or infer a DOI, title, author list, venue, publication year, or publication status.

If metadata cannot be verified:

- Keep the entry with the verified name and source URL.
- Omit unknown fields rather than inserting placeholders such as `Unknown`.
- Add a `note` explaining what could not be verified.
- Mark the entry for manual review.

`refs.bib` holds only publications to download. Sources without a resolvable DOI — commercial platforms, no-DOI preprints, or project modules without an independent paper — are dismissed from the catalog. Record them for review (they may re-enter when writing the knowledge base or the review); when they are components of a published project, map the concept as a `keywords` tag on the parent entry instead.

### 6. Fetch Metadata

For DOI-bearing records, retrieve metadata from Crossref or DataCite. Capture, when available:

- Authors
- Exact publication title
- Publication year
- Journal or proceedings venue
- Volume, issue, and page range or article number
- DOI
- Official publication URL

For arXiv and other preprint, OpenReview, and proceedings-only records, retrieve the same fields from the source page or its authoritative API. Prefer the source's canonical version and preserve version information only when it is bibliographically relevant.

Check that fetched metadata matches the source's identity. A valid DOI that resolves to a different paper is not a valid DOI for the entry.

### 7. Generate `literature/refs.bib`

Use one stable BibTeX key per map source. Keys should be descriptive, lowercase, and stable across metadata updates, for example:

```text
example_project
example_release1
example_release2
example_component
```

Use standard, broadly compatible entry types:

- `@article` for journal publications
- `@inproceedings` for conference proceedings
- `@misc` for preprints, OpenReview, software, platforms, and unresolved non-publication records

Use fields appropriate to the source:

```bibtex
@article{example_paper,
  author = {Author, First and Author, Second},
  title = {A representative research publication},
  journal = {A Journal},
  year = {2026},
  volume = {12},
  pages = {123--134},
  doi = {10.1234/example},
  url = {https://doi.org/10.1234/example},
}
```

For preprints, include a clear status note:

```bibtex
@misc{example_preprint,
  author = {Author, First},
  title = {Example preprint},
  year = {2026},
  doi = {10.1234/preprint-example},
  url = {https://doi.org/10.1234/preprint-example},
  howpublished = {Preprint server},
  note = {Preprint; not yet peer-reviewed},
}
```

For arXiv records, include `eprint`, `archiveprefix = {arXiv}`, and the canonical abstract URL when available.

Give every entry a `keywords` field listing every map concept it covers, including components, modules, and aliases without an independent publication (for example `example_component`, `example_plugin`, `example_v2`). Use lowercase, hyphenated slugs derived from the map concept name. Map concepts resolve to an entry by key or by keyword.

Do not use a fabricated `author = {{Unknown}}`. If authors are unavailable, omit `author` and explain the limitation in `note`.

### 8. Validate The Catalog

Before finishing, validate all of the following:

- `literature/refs.bib` parses as valid BibTeX.
- Every entry has a resolvable DOI.
- Every source identified in `literature/map.md` has exactly one matching BibTeX key, unless it is explicitly a duplicate or parent-project component.
- Every valid map concept maps to an entry key or to a `keywords` tag on some entry.
- No component or module of a published project exists as a separate stub entry.
- Every BibTeX key is unique and stable.
- Every DOI resolves or is explicitly marked unresolved.
- Every DOI's resolved title matches the intended source.
- Official publications are primary when available.
- Preprints are clearly labeled.
- No source has an invented DOI or unsupported publication status.
- URLs point to the official publisher, proceedings, preprint, platform, or repository.
- No PDF files are downloaded or parsed as part of this skill.

Report unresolved or suspicious entries explicitly instead of silently accepting them.

## Updating Existing Catalogs

When rerunning the workflow:

1. Preserve existing stable BibTeX keys.
2. Re-check records whose publication status may have changed.
3. Replace a preprint with the official publication when one becomes available.
4. Keep the preprint DOI or URL in a note when it remains useful for provenance.
5. Maintain `keywords` when map concepts change or new components of a published project appear.
6. Avoid unrelated formatting churn in `literature/refs.bib`.
7. Review the diff and confirm that changes are limited to the catalog workflow.

## Completion Report

Report:

- Number of map sources processed
- Number of official publications
- Number of preprints
- Number of no-DOI/platform/module records
- Number of unresolved records
- Validation results
- Any corrected or mismatched map links

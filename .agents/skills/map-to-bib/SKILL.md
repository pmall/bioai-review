---
name: map-to-bib
description: Formalize the living literature map into a verified BibTeX catalog of downloadable publications.
---

# Map To BibTeX

Use this skill to convert `literature/map.md` into or update `literature/refs.bib`. PDF download and parsing are separate workflows, not part of this skill.

## Convention

`literature/map.md` is a free-form map of concepts and references (models, tools, platforms, modules, lineages). It is a superset of the catalog: concepts without a citable publication stay in the map.

`literature/refs.bib` is the catalog of publications to download and parse. Every entry has a resolvable DOI.

Every concept resolves to exactly one place:

- **Its own entry** — it has an independent, citable publication.
- **A `keywords` tag on an entry** — the paper describes it (a tool or component introduced there).
- **The map** — it has no citable publication (commercial platforms, no-DOI preprints, modules without a paper).

Works that might belong to the review but have not been decided on are not in the map and not in the catalog. They wait in `literature/candidates.md`. Do not catalog one until it has been accepted into the map.

`keywords` lists only what the paper itself describes. Keywords never cross-reference other publications; such references belong in the map.

## Workflow

### 1. Read the map

Read `literature/map.md` in full. Inventory every named source with its links and roles. Treat grouped names as separate records when they refer to separate papers (e.g. two versions of a project, each with its own paper).

### 2. Resolve each concept to its best publication

For concepts with a possible publication, search in this order:

1. Official publisher or journal page
2. Crossref DOI metadata
3. DataCite DOI metadata
4. Official conference proceedings
5. Preprint servers (e.g. arXiv or a field-specific server)
6. OpenReview
7. Author, laboratory, or project repository

Verify that title, authors, and subject match the map entry. Links and DOIs are discovery hints — if one resolves to a different paper, find the correct one and record the discrepancy.

Prefer the official peer-reviewed version. Use a preprint only when no official publication exists, and label it as not yet peer-reviewed.

### 3. Fetch and verify metadata

Retrieve from Crossref/DataCite or the source page: authors, title, year, venue, volume/issue/pages, DOI, and official URL. Confirm the retrieved metadata matches the source identity; a DOI that resolves to a different paper is not valid for this entry.

Only verified metadata enters the catalog. Omit unverifiable fields and explain the gap in a note — never invent fields, authors, or placeholders.

### 4. Generate `literature/refs.bib`

- One stable, lowercase, descriptive key per source.
- `@article` for journal papers, `@inproceedings` for proceedings, `@misc` for preprints and other records.
- Include `doi`, `url`, and a preprint status note; add `eprint`/`archiveprefix` for arXiv.
- Add `keywords` for the concepts the paper describes (lowercase, hyphenated slugs).
- Sources without a resolvable DOI stay in the map; they are not cataloged.

Example:

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
  keywords = {example_concept},
}

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

### 5. Validate

- `refs.bib` parses as valid BibTeX; keys are unique and stable.
- Every entry has a resolvable DOI and a `keywords` field.
- Every keyword is content of its own entry's paper.
- Every non-dismissed map concept maps to an entry key or keyword; dismissed concepts stay marked in the map.
- Official publications are primary; preprints are labeled.
- URLs point to official sources.
- Report unresolved or suspicious entries rather than accepting them silently.

## Updating an existing catalog

1. Preserve stable BibTeX keys.
2. **Re-check every cataloged preprint for a journal version, on every pass** — not only the entries being added. This field publishes fast enough that a preprint cataloged weeks ago may now have a journal DOI, and the catalog is supposed to prefer it.
   - Ask Crossref for the preprint DOI and look for an `is-preprint-of` relation.
   - The relation is not always populated, so also search Crossref by title filtered to `type:journal-article` and match the result against the entry.
   - arXiv DOIs (`10.48550/...`) are DataCite, not Crossref; a 404 there is expected and is not a finding.
   - When a journal version exists, switch the entry to it — new DOI, venue, volume, pages, and the published author list, which is often not the preprint's — and keep the preprint DOI in a `note` for provenance.
3. Maintain `keywords` as map concepts change.
4. Avoid unrelated formatting churn; review the diff.

## Completion report

Report: sources processed, official publications, preprints, dismissed map concepts, unresolved records, validation results, and any corrected or mismatched links. State the outcome of the preprint re-check explicitly, including when nothing had been published — a silent report is indistinguishable from a skipped step.

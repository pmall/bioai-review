---
name: complete-map
description: Discover and propose the core publications a literature map missed by examining what its cataloged seeds cite, then fold approved works into the map.
---

# Complete Map

Use this skill to find the handful of genuinely important publications the living literature map (`literature/map.md`) is missing, by examining the reference lists of the cataloged corpus. The skill ends at the map: cataloging (`map-to-bib`), downloading, and parsing are separate workflows.

## Convention

The map is the heart of the review: every concept in it is something the review discusses. This skill exists only to **fill genuine gaps** — catch core works the field clearly relies on but the map overlooked. It is **not** snowballing: additions must be works the review will actually talk about, not merely cited.

Each concept still resolves to exactly one place per the map convention:

- **Its own entry** — it has an independent, citable publication.
- **A `keywords` tag on an entry** — the paper describes it.
- **The map** — it has no citable publication.

## When to use

- Once, after `literature/map.md` and `literature/refs.bib` describe a parsed corpus.
- Second passes are rare: if genuinely needed, rerun from scratch against the updated map/`refs.bib` — nothing is persisted between passes.

## Workflow

### 1. Build the candidate pool

Run the candidate script from the repo root:

```
uv run scripts/build_candidate_pool.py
```

It reads every DOI in `literature/refs.bib`, fetches each seed's reference list from a bibliographic database (OpenAlex, Semantic Scholar fallback), unions and dedupes them, drops seeds and self-citations, and ranks candidates by **co-citation frequency** (how many seeds cite them), then recency.

Output: `literature/candidate_pool.json` (transient, gitignored) plus a printed top-N report. No persistent screening ledger exists — the pool is regenerated any time.

### 2. Screen by the field's criteria

Filter the pool against the review's scope and its date rule (e.g. "post-2025 unless a fundamental lineage anchor"). Propose a candidate only when it is genuinely at the heart of the review:

- a **canonical lineage anchor** the map is missing (a foundational method or an active lineage's ancestor), or
- a **map concept that gained a publication** — an item already in the map as "dismissed" or "no publication" that now has a citable paper, or
- a **major frontier or competing work** cited by multiple seeds as a baseline.

Reject everything else by default: single-citation methods, adjacent works, reviews, datasets, and infrastructure/background works (databases, tooling, benchmarks the review merely mentions). Such infrastructure is not map material; it is deferred to a separate post-review citation pass.

### 3. Propose and validate

Present each candidate with:

- title, year, venue
- resolvable DOI (verified via Crossref/DataCite if not already in the pool)
- co-citation count and the citing seed DOIs
- the map section/concept it would fill
- a one-line rationale tied to the criteria above

The user approves or rejects each proposal. **No publication enters the map without user validation.** Also flag any stale map annotations you noticed (e.g. a concept marked "no publication" that now has one).

### 4. Fold approved works into the map

For each approved work:

- add the concept to the relevant section of `literature/map.md` with its role and official link
- correct stale annotations found during screening (re-promote concepts previously marked "dismissed" or "no publication")
- leave rejected works out — nothing is recorded, they simply are not added

**Stop here.** The catalog, downloads, and parsing are handled by their own workflows (`map-to-bib` for `refs.bib`; manual download and `scripts/parse_pdf.py` for artifacts).

## Rules

- Candidates come from bibliographic APIs, never from parsed-PDF text.
- One-shot, add-only-if-at-the-heart, reject-by-default.
- Pre-date-rule works enter only as lineage anchors, consistent with the map's active-lineage philosophy.
- Infrastructure/background works are not map material.
- No persistent rejection ledger; the pool JSON is transient.
- Never mutate `refs.bib`; never download or parse PDFs.

## Completion report

Report: pool size, candidates proposed, approved/rejected with reasons, map sections updated, stale annotations corrected, and any discrepancies found (e.g. links resolving to different papers).

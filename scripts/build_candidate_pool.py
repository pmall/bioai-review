#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx", "bibtexparser"]
# ///

"""Build a ranked citation candidate pool from the seed DOIs in refs.bib.

For every seed DOI, fetch the paper's reference list from a bibliographic
database (OpenAlex, with Semantic Scholar as fallback), then union, dedupe,
drop seeds/self-citations, and rank candidates by co-citation frequency.

Emits:
  --json   literature/candidate_pool.json  (full machine-readable pool)
  stdout  a readable top-N report (default N=25)

No persistent screening ledger is written; the pool is regenerated any time.
"""

from argparse import ArgumentParser
from collections import Counter, defaultdict
from pathlib import Path
import json
import time

import httpx
import bibtexparser

USER_AGENT = "bioai-review (mailto:review@example.com)"
MAX_OPENALEX_BATCH = 50
MAX_S2_BATCH = 100


def seed_dois(refs_bib: Path) -> list[str]:
    with refs_bib.open() as fh:
        db = bibtexparser.load(fh)
    dois = []
    for entry in db.entries:
        if entry.get("doi"):
            dois.append(entry["doi"].strip().lower())
    return sorted(set(dois))


def openalex_references(client: httpx.Client, seed_doi: str) -> list[str] | None:
    """Return OpenAlex work IDs referenced by seed_doi, or None on failure."""
    url = f"https://api.openalex.org/works/doi:{seed_doi}"
    r = client.get(
        url,
        headers={"User-Agent": USER_AGENT},
        params={"select": "id,referenced_works"},
    )
    if r.status_code != 200:
        return None
    data = r.json()
    return data.get("referenced_works") or []


def openalex_works(client: httpx.Client, openalex_ids: list[str]) -> list[dict]:
    """Fetch work metadata for a batch of OpenAlex IDs."""
    out: list[dict] = []
    for i in range(0, len(openalex_ids), MAX_OPENALEX_BATCH):
        chunk = openalex_ids[i : i + MAX_OPENALEX_BATCH]
        url = "https://api.openalex.org/works"
        r = client.get(
            url,
            headers={"User-Agent": USER_AGENT},
            params={"filter": "openalex_id:" + "|".join(chunk), "per-page": 50},
        )
        if r.status_code == 200:
            out.extend(r.json().get("results", []))
        time.sleep(0.1)
    return out


def s2_references(client: httpx.Client, seed_doi: str) -> list[dict]:
    """Return Semantic Scholar references for seed_doi (fields of interest)."""
    url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{seed_doi}/references"
    r = client.get(
        url,
        params={"fields": "externalIds,title,year,venue,abstract", "limit": 1000},
    )
    if r.status_code != 200:
        return []
    return r.json().get("data") or []


def normalize_doi(doi: str) -> str:
    return doi.strip().lower().removeprefix("https://doi.org/").removeprefix("http://doi.org/")


def openalex_to_candidate(w: dict) -> dict:
    doi = normalize_doi(w.get("doi") or "")
    title = (w.get("title") or "").strip()
    year = w.get("publication_year")
    venue = None
    pl = w.get("primary_location") or {}
    src = pl.get("source") or {}
    venue = src.get("display_name")
    abstract = ""
    inv = w.get("abstract_inverted_index")
    if inv:
        pos = []
        for word, idxs in inv.items():
            for idx in idxs:
                pos.append((idx, word))
        abstract = " ".join(w for _, w in sorted(pos))
    return {
        "doi": doi,
        "title": title,
        "year": year,
        "venue": venue,
        "abstract": abstract,
        "cited_by": [],
    }


def build_pool(seed_dois: list[str], client: httpx.Client) -> list[dict]:
    candidates: dict[str, dict] = {}
    cited_by: defaultdict[str, list[str]] = defaultdict(list)
    seed_set = set(seed_dois)

    for seed_doi in seed_dois:
        try:
            refs = openalex_references(client, seed_doi)
        except httpx.HTTPError:
            refs = None

        if refs:
            works = openalex_works(client, refs)
            for w in works:
                cand = openalex_to_candidate(w)
                if not cand["doi"]:
                    continue
                cited_by[cand["doi"]].append(seed_doi)
                if cand["doi"] not in candidates:
                    candidates[cand["doi"]] = cand
        else:
            # Fallback: Semantic Scholar
            try:
                s2_refs = s2_references(client, seed_doi)
            except httpx.HTTPError:
                s2_refs = []
            for item in s2_refs:
                ref = item.get("citedPaper") or {}
                doi = normalize_doi((ref.get("externalIds") or {}).get("DOI", ""))
                if not doi:
                    continue
                title = ref.get("title") or ""
                cand = {
                    "doi": doi,
                    "title": title,
                    "year": ref.get("year"),
                    "venue": ref.get("venue"),
                    "abstract": ref.get("abstract") or "",
                    "cited_by": [],
                }
                cited_by[doi].append(seed_doi)

        time.sleep(0.2)

    for doi in list(candidates):
        if doi in seed_set:
            del candidates[doi]
    for doi, seeds in cited_by.items():
        if doi in seed_set:
            continue
        cand = candidates.setdefault(
            doi,
            {
                "doi": doi,
                "title": None,
                "year": None,
                "venue": None,
                "abstract": "",
                "cited_by": [],
            },
        )
        cand["cited_by"] = sorted(set(cand.get("cited_by", []) + seeds))

    pool = list(candidates.values())
    for cand in pool:
        cand["co_citations"] = len(cand["cited_by"])
    pool.sort(
        key=lambda c: (
            -c["co_citations"],
            -(c["year"] or 0),
            (c["title"] or "").lower(),
        )
    )
    return pool


def main() -> int:
    parser = ArgumentParser(
        description=(
            "Build a ranked citation candidate pool from refs.bib seed DOIs "
            "using OpenAlex (Semantic Scholar fallback)."
        )
    )
    parser.add_argument(
        "--refs", type=Path, default=None,
        help="path to refs.bib (default: literature/refs.bib)",
    )
    parser.add_argument(
        "--json", type=Path, default=None,
        help="write the full pool as JSON (default: literature/candidate_pool.json)",
    )
    parser.add_argument(
        "--top", type=int, default=25,
        help="number of top candidates to print (default: 25)",
    )
    parser.add_argument(
        "--all", action="store_true",
        help="print every candidate instead of only the top N",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    refs = args.refs or repo_root / "literature" / "refs.bib"
    if not refs.is_file():
        parser.error(f"refs.bib not found: {refs}")

    print(f"Seed DOIs: {refs}")
    dois = seed_dois(refs)
    print(f"  {len(dois)} seed entries")

    with httpx.Client(timeout=30) as client:
        pool = build_pool(dois, client)

    print(f"Candidate pool: {len(pool)} unique candidates")

    out = args.json or repo_root / "literature" / "candidate_pool.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(pool, indent=2))
    print(f"Pool written: {out}")

    shown = pool if args.all else pool[: args.top]
    print(f"\nTop {len(shown)} candidates:")
    for i, cand in enumerate(shown, 1):
        by = ", ".join(cand["cited_by"][:3])
        more = f" (+{len(cand['cited_by'])-3})" if len(cand["cited_by"]) > 3 else ""
        year = cand["year"] or "?"
        venue = cand["venue"] or ""
        title = cand["title"] or "(no title)"
        print(f"{i:3}. [{cand['co_citations']}x] ({year}) {title}")
        print(f"     doi: {cand['doi']}")
        print(f"     venue: {venue} | cited by: {by}{more}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

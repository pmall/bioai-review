# Candidates — check before adding

Works surfaced while reading the corpus that **might** belong to the review, held
here so they are neither lost nor silently adopted.

**Nothing here is part of the review.** None of it is in `literature/refs.bib` or
`literature/corpus/`, and no claim in `literature/map.md` depends on any of it.
This file exists precisely so the map's invariant holds: every publication named
in the map resolves to a `refs.bib` entry, so undecided works must live outside it.

Each entry below is **DOI-verified** — the identifier resolves and its metadata
matches the description — but **the paper has not been read**. Everything stated
is from the citing paper or the abstract, not from the source itself.

**To accept one:** read it, write it into its section in `literature/map.md`,
then run the `map-to-bib` skill. Delete it from this file.
**To reject one:** move it to Part V of the map (*examined and excluded*) with a
stated reason, so the decision is recorded rather than re-litigated later.

---

## mBER

- **DOI:** `10.1101/2025.09.26.678877` (bioRxiv, 28 Sep 2025)
- **Title:** *mBER: controllable de novo antibody design with million-scale experimental screening*
- **Authors:** Swanson, E., Nichols, M., Ravichandran, S. & Ogden, P.
- **Would go in:** §6 — inversion as a portable technique, as a sixth Level-2 system.
- **Why it might belong:** Germinal names it as the one open-source peer doing the
  same thing — *"mBER, like Germinal, leverages backpropagation-based
  hallucination with partial structural conditioning for nanobody design"*. If
  that holds, it is another independent group inverting a predictor, which is the
  evidence §6's portability argument rests on.
- **Why to check first:** the "million-scale experimental screening" in the title
  is the opposite of the low-*n* testing that Beat 3 makes the review's spine. It
  may turn out to be a screening paper with a design front-end rather than a
  design paper, which would change where — or whether — it belongs.
- **Surfaced from:** Germinal (`germinal`), discussion section, ref 50.

## ipSAE

- **DOI:** `10.1101/2025.02.10.637595` (bioRxiv, 14 Feb 2025)
- **Title:** *Rēs ipSAE loquuntur: what's wrong with AlphaFold's ipTM score and how to fix it*
- **Author:** Dunbrack, R. L.
- **Would go in:** Part IV — benchmarking, validity and evaluation infrastructure.
- **Why it might belong:** ipTM is half of the canonical Level-1 success criterion
  quoted in Beat 4 (AlphaProteo's *"interchain AF2 pAE < 10 … pLDDT > 80"*) and is
  used as a filter across §2–§7. A paper arguing the metric is broken would join
  the other known-limits findings Part IV already carries — PoseBusters'
  incompleteness, FoldBench's common-intersection problem, Boltz-2's temporal leakage.
- **Why to check first:** it is a metric critique, not a model or a benchmark
  suite. Confirm it belongs in the review at all rather than in a report footnote.
- **Surfaced from:** Germinal (`germinal`), ref 64.

## Overath et al. — binder-design meta-analysis

- **DOI:** `10.1101/2025.08.14.670059` (bioRxiv, 14 Aug 2025)
- **Title:** *Predicting experimental success in de novo binder design: a meta-analysis of 3,766 experimentally characterised binders*
- **Would go in:** Part IV, and it would be cited from Beat 3.
- **Why it might belong:** the only source seen so far that pools hit rates across
  labs. Beat 3's experimental-budget table is assembled from each system's own
  self-reported campaign, and the intro's second caveat admits those numbers are
  not comparable. A cross-lab meta-analysis is the one thing that could put a
  floor under that table — and BoltzProt-1's screening-hit / confirmed-binder
  distinction says such a normalization is exactly what the field lacks.
- **Why to check first:** its scope (3,766 binders) may predate or exclude the
  2026 systems this review centres on, in which case it characterises the previous
  generation rather than this one.
- **Surfaced from:** Germinal (`germinal`), ref 65.

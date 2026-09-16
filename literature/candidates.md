# Candidates and exclusions — the decision log

Everything the review considered and did not take. `literature/map.md` holds what
is in; this file holds what is out, and why, so no decision is re-litigated.

**Nothing here is part of the review.** No section of the map is built on any of
it, and nothing here is drafted. Two states:

- **Undecided** — surfaced while reading the corpus, not yet judged. Not in
  `refs.bib` and not in `corpus/`.
- **Excluded** — retrieved, parsed and then judged out of scope. These *stay* in
  `refs.bib` and `corpus/`: the catalog records what was obtained, the map records
  what is in scope. An excluded work can still be quoted in the review — the
  exclusion is from the argument's structure, not from the bibliography.

Undecided entries are **DOI-verified** — the identifier resolves and its metadata
matches the description — but **the paper has not been read**. Everything stated in
that part is from the citing paper or the abstract, not from the source itself.
Excluded entries have been read.

**To accept an undecided work:** read it, write it into its section in
`literature/map.md`, then run the `map-to-bib` skill. Delete it from this file.
**To reject one:** move it down to *Excluded* with a stated reason.

---

# UNDECIDED

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

## Protein Hunter

- **DOI:** `10.1101/2025.10.10.681530` (bioRxiv, 10 Oct 2025)
- **Title:** *Protein Hunter: exploiting structure hallucination within diffusion for protein design*
- **Authors:** Cho, Y., Rangel, G., Bhardwaj, G. & Ovchinnikov, S.
- **Would go in:** §6 — inversion as a portable technique.
- **Why it might belong:** RFOptimization benchmarks against it directly as "an
  independently developed cycling-based method", and it is the only external
  baseline in that comparison. Same senior author as BoltzDesign1, which matters
  for §6's independence bookkeeping — it would be a third point in one research
  programme, not a new group.
- **Why to check first:** whether it is Level 2 at all. RFO describes it as
  cycling-based and "confined to the confidence landscape of a single model",
  which would put it closer to RFO's cycling branch than to a gradient method.
- **Surfaced from:** RFOptimization (`rfoptimization`), ref 13.

## HalluDesign

- **DOI:** `10.1101/2025.11.08.686881` (bioRxiv, 9 Nov 2025)
- **Title:** *HalluDesign: Protein Optimization and de novo Design via Iterative Structure Hallucination and Sequence Design*
- **Authors:** Fang, M., Wang, C., Shi, J., Lian, F., et al. (Cao, L.)
- **Would go in:** §6 — inversion as a portable technique.
- **Why it might belong:** RFO groups it with BoltzDesign1 and Protein Hunter as
  predictor-guided optimization extended to all-atom models, and it is an
  independent group (Longxing Cao's), which is the kind of evidence §6's
  portability claim is built on. The title also pairs *optimization* with *de novo
  design*, the same two-mode framing that made §7 read as a platform.
- **Why to check first:** whether "hallucination" here means a gradient loop or an
  iterative predict-then-redesign cycle — the same ambiguity as Protein Hunter.
- **Surfaced from:** RFOptimization (`rfoptimization`), ref 12.

## AfCycDesign

- **DOI:** `10.1038/s41467-025-59940-7` (Nature Communications **16**, 4730, 2025)
- **Title:** *Cyclic peptide structure prediction and design using AlphaFold2*
- **Authors:** Rettie, S. A., Campbell, K. V., Bera, A. K., et al. (DiMaio, Ovchinnikov, Bhardwaj)
  Preprint: `10.1101/2023.02.25.529956` (bioRxiv, 26 Feb 2023).
- **Would go in:** §2 — as the critic RFpeptides filters on, or Part IV as an instrument.
- **Why it might belong:** RFpeptides is filtered by refolding with AfCycDesign, so
  the map currently describes that filter generically ("a cyclic-encoding
  AlphaFold2 variant") to avoid naming an uncataloged publication. It is also the
  cyclic-peptide analogue of the AF2-as-filter pattern §2–§5 run on, and the paper
  RFpeptides' own hallucination lineage starts from.
- **Why to check first:** it is a 2023 preprint / 2025 journal paper about
  *prediction and monomer design*, not binder design, so the scope rule does not
  obviously admit it. Decide whether a critic used by an included system earns its
  own entry, belongs in Part IV with the other instruments, or stays out with the
  filter described generically as it is now.
- **Surfaced from:** RFpeptides (`rfpeptides`), ref 11.

---

# EXCLUDED

Retrieved, parsed, and judged out of scope. Recorded rather than deleted: an
exclusion with a stated reason is part of the review's method, and keeping them
prevents re-litigating the same decision later. All remain in `refs.bib` and
`literature/corpus/`.

**Scope rule applied:** in scope = generates a **protein or peptide binder
conditioned on a target**, or predicts the structure such a system designs against.
Out of scope = a different modality (small molecules), or sequence generation with
no target conditioning.

* **DrugFlow** — `drugflow` · `10.48550/arXiv.2508.17815` · and **FLOWR** —
  `flowr` · `10.1038/s43588-026-00998-8` — *excluded: wrong modality.* Both are
  pocket-conditioned **small-molecule** generators, producing 3D atom types,
  coordinates and bond topology for a ligand. Structure-based drug design rather
  than binder design; the overlap is the flow-matching machinery, not the
  problem. Both are quoted in Beat 1 for their discrete/continuous hybrid
  schemes — the evidence for the differentiability asymmetry.
* **ProtFlow** — `protflow` · `10.64898/2026.02.14.705870` — *excluded: not
  binder design.* Rectified flow matching in sequence space for general protein
  engineering; learns the global semantic distribution of protein space. The
  words "binder" and "binding" do not appear anywhere in the paper, and there is
  no target conditioning.
* **moPPIt** — `moppit` · `10.1101/2024.07.31.606098` — *excluded: no lineage.* A
  genetic algorithm iterating a pool from the PepMLM peptide language model,
  scored by BindEvaluator (an ESM-2 binding-site predictor) plus perplexity. No
  diffusion, no flow matching, no structure input at all; AlphaFold2-Multimer
  appears only as retrospective validation. Target-conditioned, so it passes the
  scope rule, but it shares no machinery with anything else here and is cited by
  no other corpus paper.
  *Recorded error, do not reintroduce:* an earlier version of this map described
  moPPIt as discrete flow matching. That was wrong.
* **SaProt** — `saprot` · `10.1101/2023.10.01.560349` — *excluded: neither half of
  the review.* A structure-aware protein language model (Foldseek 3Di alphabet,
  441 tokens) with no folding head and no generative binder capability. It
  neither predicts 3D structure nor designs binders, and belongs to no lineage
  tracked here. Cited by one corpus paper.

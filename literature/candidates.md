# Candidates and exclusions — the decision log

Everything the review considered and did not take. `literature/map.md` holds
what is in; this file holds what is out, and why, so no decision is
re-litigated.

**Nothing here is part of the review.** No section of the map is built on any of
it, and nothing here is drafted. Two states:

- **Undecided** — surfaced while reading the corpus, not yet judged. Not in
  `refs.bib` and not in `corpus/`.
- **Excluded** — retrieved, parsed and then judged out of scope. These _stay_ in
  `refs.bib` and `corpus/`: the catalog records what was obtained, the map
  records what is in scope. An excluded work can still be quoted in the review —
  the exclusion is from the argument's structure, not from the bibliography.

Undecided entries are **DOI-verified** — the identifier resolves and its
metadata matches the description — but **the paper has not been read**.
Everything stated in that part is from the citing paper or the abstract, not
from the source itself. Excluded entries have been read.

**To accept an undecided work:** read it, write it into its section in
`literature/map.md`, then run the `map-to-bib` skill. Delete it from this file.
**To reject one:** move it down to _Excluded_ with a stated reason.

______________________________________________________________________

# UNDECIDED

_Empty — nothing is currently awaiting a decision._

# EXCLUDED

Judged out, with the reason stated. Recorded rather than deleted: an exclusion
with a stated reason is part of the review's method, and keeping them prevents
re-litigating the same decision later.

Two grounds for exclusion, and they differ in what is left behind:

- **Out of scope** — retrieved, parsed, then judged out. These remain in
  `refs.bib` and `literature/corpus/`, and may still be quoted. _Scope rule
  applied:_ in scope = generates a **protein or peptide binder conditioned on a
  target**, or predicts the structure such a system designs against. Out of
  scope = a different modality (small molecules), or sequence generation with no
  target conditioning.
- **Below the threshold** — in scope, but carrying no claim the review leans on.
  Judged out on the abstract and on how the corpus itself cites them, without
  being retrieved, so these are **not** in `refs.bib` or `literature/corpus/`
  and are not quotable. The review is not obliged to re-cite what a work it
  cites already cites; a reader who wants the comparison has the citing paper.

* **DrugFlow** — `drugflow` · `10.48550/arXiv.2508.17815` · and **FLOWR** —
  `flowr` · `10.1038/s43588-026-00998-8` — _excluded: wrong modality._ Both are
  pocket-conditioned **small-molecule** generators, producing 3D atom types,
  coordinates and bond topology for a ligand. Structure-based drug design rather
  than binder design; the overlap is the flow-matching machinery, not the
  problem. Both are quoted in the scope beat for their discrete/continuous
  hybrid schemes — the evidence for the differentiability asymmetry.
* **BoltzMol-1** — `boltzmol1` · `10.64898/2026.07.04.736485` — _excluded: wrong
  modality._ Small-molecule hit discovery over an optimized Boltz-2, API-only
  with no weights. It **screens catalogue compounds** rather than generating
  binders, so it fails the scope rule twice over — the same exclusion that keeps
  DrugFlow and FLOWR out. Its one pull toward the map is that it is a second
  closed Boltz model, but §3's open→closed fork is established by BoltzProt-1
  alone. In `refs.bib` and the corpus, and quotable.
* **ProtFlow** — `protflow` · `10.64898/2026.02.14.705870` — _excluded: not
  binder design._ Rectified flow matching in sequence space for general protein
  engineering; learns the global semantic distribution of protein space. The
  words "binder" and "binding" do not appear anywhere in the paper, and there is
  no target conditioning.
* **moPPIt** — `moppit` · `10.1101/2024.07.31.606098` — _excluded: no lineage._
  A genetic algorithm iterating a pool from the PepMLM peptide language model,
  scored by BindEvaluator (an ESM-2 binding-site predictor) plus perplexity. No
  diffusion, no flow matching, no structure input at all; AlphaFold2-Multimer
  appears only as retrospective validation. Target-conditioned, so it passes the
  scope rule, but it shares no machinery with anything else here and is cited by
  no other corpus paper. _Recorded error, do not reintroduce:_ an earlier
  version of this map described moPPIt as discrete flow matching. That was
  wrong.
* **SaProt** — `saprot` · `10.1101/2023.10.01.560349` — _excluded: neither half
  of the review._ A structure-aware protein language model (Foldseek 3Di
  alphabet, 441 tokens) with no folding head and no generative binder
  capability. It neither predicts 3D structure nor designs binders, and belongs
  to no lineage tracked here. Cited by one corpus paper.

## Below the threshold

- **Protein Hunter** — `10.1101/2025.10.10.681530` (bioRxiv, 10 Oct 2025; Cho,
  Rangel, Bhardwaj & Ovchinnikov) · and **HalluDesign** —
  `10.1101/2025.11.08.686881` (bioRxiv, 9 Nov 2025; Fang et al., Cao lab). Both
  were considered for §6 and both are **cycling, not gradient** — Protein Hunter
  hallucinates from an all-X sequence and improves it through _"iterative
  sequence re-design and structure re-prediction"_, HalluDesign is _"fine-tune
  free, forward-pass only"_. Neither backpropagates into the design variable, so
  neither can join the Level-2 roster without blurring the axis §6–§8 escalate
  along; and as cycling methods they would enter §6 at a weight the section does
  not have room for beside BindCraft, BoltzDesign1 and Germinal. Protein
  Hunter's one remaining claim was that it is RFOptimization's only external
  baseline (7.50% three-model consensus pass against RFO's 12.08%; ~178 GPU-min
  per filter-passing design against RFO's ~26 and BindCraft's ~34 GPU-h). That
  comparison is RFOptimization's own and is cited there; §2 and §6 carry the
  lineage's optimizer completely without it. _What their existence does
  establish, and the map does not need them to say:_ cycling-based hallucination
  is an independently developed family rather than an RFO idiosyncrasy —
  HalluDesign is the Cao lab's, independent of Ovchinnikov's.

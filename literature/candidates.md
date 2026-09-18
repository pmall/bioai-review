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

_Surfaced 18 Sep 2026 from Anthropic's inference-optimization release
(`anthropics/uplifting-biomolecular-modeling`), whose kit table is a third
party's list of the open models the field actually runs. The predictive half of
that list is already covered by the map; of the design-side models it names,
only Caliby is still open._

## Caliby

- **DOI:** `10.1101/2025.09.30.679633` (bioRxiv, 2 Oct 2025)
- **Title:** *Ensemble-conditioned protein sequence design with Caliby*
- **Authors:** Shuai, R. W., Lu, T., Bhatti, S., Kouba, P. & Huang, P.-S.
- **Would go in:** §2, as a **mention** under ProteinMPNN beside LigandMPNN.
  Nothing larger.
- **Why it might belong:** ProteinMPNN is the sequence stage the whole Level-1
  pipeline borrows, and the map presents it with no current challenger. Caliby
  is a Potts-model designer conditioned on an *ensemble* of backbone conformers
  rather than one, and claims to beat ProteinMPNN on AF2 self-consistency while
  scaling better across conformers. Its SolubleCaliby variant reports making
  binder backbones designable that SolubleMPNN judged undesignable, which is the
  only part touching the review's subject directly.
- **Why to check first:** sequence design with no target conditioning is out of
  scope by the rule below; it enters, if at all, only as a qualifier on
  ProteinMPNN's standing. Its binder evidence is a designability metric on
  Protpardelle-1c backbones, not binders tested against a target, and
  Protpardelle is not in the map.
- **Surfaced from:** the `caliby` kit (task: *sequence design*).

**Also on that list and deliberately not entered here:** `ef2inv` is the
ESMFold2 binder-design campaign already in §8; `esm_if1` is inverse folding that
ProteinMPNN's entry already covers; `mosaic` (with `joltz`) was a _map-only_
line in §6 and is now excluded below.

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

* **ProtDBench** — `protdbench` · `10.48550/arXiv.2605.04118` — _excluded: not a
  third party, and its head-to-head is in-silico only._ ICML 2026 (PMLR 306); a
  standardized, throughput-aware evaluation framework for binder design, with
  fixed targets, hotspots, filters and success criteria. Considered for Table B
  alongside the Overath meta-analysis and fails on both counts the map would
  have needed. _Not a third party:_ every author is ByteDance Seed or ex-Seed,
  corresponding author Wenzhi Xiao, who is also corresponding author on PXMeter,
  Protenix and PXDesign (§7) — and its verifier study concludes that Protenix
  and Protenix-Mini enrich best, then adopts Protenix-Mini as ProtDBench's own
  structural-consistency verifier. _Not a Table B row, and no help to the ones
  there:_ the seven-method comparison (RFdiffusion-3, BoltzGen, Protpardelle-1c,
  ODesign, PXDesign, BindCraft, BoltzDesign1) is scored entirely in silico —
  AF2-IG-Easy filter pass rate, successful backbones per 24 h on one A100,
  Foldseek cluster diversity, Protenix-Mini recapitulation. No assay, no
  designs-tested denominator, no hit definition, which is the same exclusion
  that keeps RFOptimization (§6) out of the table. Re-scoring seven systems'
  computed output does not make their wet-lab campaigns comparable, so Table B's
  claim stands unchanged. In `refs.bib` and the corpus, and quotable — two
  things in it bear on the map and are cited from here rather than given an
  entry: **(a)** the retrospective on RFdiffusion's released wet-lab outcomes
  (Appendix B.5, Table 10) — six targets, 139 confirmed binders against 432
  non-binders, already AF2-IG-prefiltered, AF2-IG precision 0.252 / recall
  0.754, Protenix-Mini precision 0.479 / recall 0.420 — which is a cross-lab
  discrimination measurement on someone else's designs; and **(b)** the finding
  that verifiers recover largely distinct subsets of true binders under
  identical filtering, with recall collapsing as more of them are required to
  agree, which is PXDesign's filter-ensembling result (§7) extended to seven
  verifiers and checked against wet-lab labels. _Also worth not re-deriving:_ it
  excludes Latent-X, AlphaProteo, Chai-2 and SeedProteo from the head-to-head
  outright, for shipping no code or weights.

* **Gauss-Seidel projection** — `gauss_seidel_projection` ·
  `10.48550/arXiv.2510.08946` — _excluded: nothing in the review uses it._ ICLR
  2026; a differentiable projection mapping provisional diffusion coordinates
  onto the nearest physically valid configuration, enforcing validity as a
  strict constraint rather than a bias, with a 2-step model reported at the
  accuracy of 200-step baselines. A real and peer-reviewed result, from a group
  with no other presence in the corpus and adopted by no system here. Held a
  **mention** whose only job was to be the fourth option in a physical-validity
  thread that has since been cut as too low-level for a field review. In
  `refs.bib` and the corpus, and quotable.

* **ColabFold** — `colabfold` · `10.1038/s41592-022-01488-1` — _excluded: a
  tool, carrying no claim the review leans on._ MMseqs2 homology search in front
  of unmodified AF2 / AlphaFold-Multimer weights, plus the ColabFoldDB
  environmental database and the Colab notebooks. Held a **meat** entry in the
  instruments unit on two jobs, and neither survived the tier test: the
  off-distribution claim it was credited with naming in 2022 is stated
  independently by AlphaFold2's own paper, BindCraft, mBER and ESMFold2, so
  ColabFold contributes a date; and its provenance fact is a table footnote
  rather than an entry. That footnote is kept under Table A — the AF2 cells and
  Table B's AF2 filters are ColabFold runs. In `refs.bib` and the corpus, and
  quotable.

* **DrugFlow** — `drugflow` · `10.48550/arXiv.2508.17815` · and **FLOWR** —
  `flowr` · `10.1038/s43588-026-00998-8` — _excluded: wrong modality._ Both are
  pocket-conditioned **small-molecule** generators, producing 3D atom types,
  coordinates and bond topology for a ligand. Structure-based drug design rather
  than binder design; the overlap is the flow-matching machinery, not the
  problem. Both are quoted in the scope beat for their discrete/continuous
  hybrid schemes — the evidence for the differentiability asymmetry.

* **OpenBind, first release** — `openbind` · `10.64898/2026.08.27.747600` —
  _excluded: wrong modality._ An open experimental structure-affinity dataset
  and benchmark: 925 crystallographic binding events from 699 compounds against
  enteroviral 2A protease, affinities for 601, from one antiviral campaign.
  Protein-**ligand** throughout; it generates no binder, and its one model
  result is fine-tuning OpenFold3-p2 on that target's 79 fragment-bound
  structures. Same exclusion as DrugFlow, FLOWR and BoltzMol-1. _Named here
  because the name misleads:_ Anthropic's release presents it among folding
  models, but its kit is `openfold3_ob0` — OpenFold3 0.5.0 on the **OpenBind-0
  checkpoint** — so the model is OpenFold3 and OpenBind is the data initiative
  behind its weights. _Not a Table A row, and the near miss is worth recording:_
  it runs a genuine third-party head-to-head of six co-folders here —
  AlphaFold3, Boltz-1, Boltz-2, OpenFold3-p2, Protenix-v1, RoseTTAFold3 — on one
  shared precomputed MSA with stated cutoffs, which is exactly the provenance
  Table A asks for, and Protenix-v1 leads at both Top-25 and Top-1. It still
  does not earn the row: **one target**, on the target class §3–§8 do not design
  for, and the authors say the ordering may not generalise. A protein-ligand row
  needs a multi-target benchmark. In `refs.bib` and the corpus, and quotable.

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

* **Genie 3** — `genie3` · `10.64898/2026.05.01.722168` — _excluded: no lineage
  in the review, and its dispute is not the review's._ An SE(3)-equivariant
  all-atom backbone diffusion model (AlQuraishi lab), target-conditioned and so
  in scope by the rule, reporting the most successful designs on 7 of 10 of
  AlphaProteo's binder problems at a fixed 200-structure budget against
  BindCraft, RFdiffusion, BoltzGen and Proteina-Complexa, and holding that lead
  normalized by GPU-hours. _Why it is out:_ the review is organized as predictor
  lineages followed to the design systems built on them, and Genie descends from
  none of the six. Admitting it on its benchmark result alone would make the
  review a scoreboard between generation and hallucination — the log of disputes
  `GOAL.md` rules out — and the coupling levels are an ordering of the material,
  not a claim that tighter coupling wins, so there is no beat here for it to
  overturn. _Reopen when:_ the Adaptyv Nipah competition is written up as
  material in its own right; §6's joltz/mosaic line is the map's only Nipah
  entry today, and it is in-silico only. Genie 3 is the wet-lab side of the same
  competition — 1 binder in 8 designs at KD ≈ 92 nM — and reports RFdiffusion
  3/60, BindCraft 1/100 and BoltzGen 2/288 there too. _How far that goes:_ the
  assay is shared, the method attribution is not. Those three rates are scraped
  from the competition site's self-reported method tags, which the paper says
  may be missing and may reflect the entrants' choices rather than the models'.
  So it is a common assay, not the controlled cross-method comparison the corpus
  lacks. That is a different job from a section entry and needs no decision now.
  Retrieved, parsed and in `refs.bib`, so quotable meanwhile; two numbers in it
  bear on the conclusion without an entry — the in-silico oracles' precision
  ceiling (maximum 12%, and no binder found at all for H3, TGFβ and TIE2) for
  the fifth gap, and the Nipah rates above, carrying that caveat. _Provisional
  claim corrected on reading:_ the Genie 3 / BindCraft design overlap is
  reported qualitatively in a figure, not as the \<10% this file previously
  recorded. _Preprint; re-check for a journal version._

* **joltz / mosaic** — _no publication, no DOI; not cataloguable_ — _excluded:
  its only claim on the review is a leaderboard score._ `joltz` ports Boltz-1/2
  to JAX and makes them differentiable; `mosaic` (Escalante Bio) optimizes
  against them — the Boltz counterpart to ColabDesign. Held a _map-only_ mention
  in §6 until Sep 2026. _Why it is out:_ what put it there was the top
  **in-silico** score in Adaptyv's Nipah binder competition (Jan 2026),
  descending a Boltz-2 loss directly with no inverse-folding stage, and a
  leaderboard result with no wet-lab outcome is not weight the review should
  spend a line on. _What removing it cost, recorded so it is not rediscovered:_
  it was the second group inverting Boltz, independent of BoltzDesign1's, and
  §6's step 4 portability count went from seven groups to six when it left. The
  architecture half of that claim is untouched — it rests on BoltzDesign1,
  PXDesign-h (§7) and ESMFold2 (§8), none of them affected. _Reopen when:_ the
  Adaptyv Nipah competition is written up, where it is the in-silico entrant
  beside Genie 3's wet-lab one. Cannot enter `refs.bib` in any case, so it comes
  back as a map-only line or not at all.

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

- **Proteina-Complexa** — `10.48550/arXiv.2603.27950` (arXiv, 30 Mar 2026; ICLR
  2026 oral; Didi et al., NVIDIA). Atomistic binder design by partially latent
  flow matching, extending La-Proteina, with inference-time search over the
  generative prior. Out for the same reason as Genie 3 above: it descends from
  no predictor lineage the review follows, and §5 covers the formalism through
  FrameFlow already. Its wet-lab weight was never its own — the million-design
  campaign behind it is Manifold Bio's, and mBER (§6) carries that group with a
  published paper. Not retrieved, so not quotable; Genie 3's benchmark of it is
  cited from there if the number is ever wanted.

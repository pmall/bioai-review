# Literature Map

> The living entry point of the review, ordered exactly as the final review will
> read, so there is no second organization to reconcile. The conventions it obeys
> — tiers, the map ↔ catalog invariant, *map-only*, what may and may not go inside
> an entry — are defined once in `AGENTS.md` and not restated here. What follows is
> specific to this review.
>
> **This file is the review minus its prose** — every publication, every fact and
> every claim, structured in reading order. Instructions addressed to whoever
> writes that prose live in `literature/writing-plan.md`, not here.
>
> **One unit per draft.** After the transversal block, the file is a flat sequence
> of the review's units in the order they render — the introduction, the metrics
> primer, the nine sections, the instruments, the two tables, the conclusion. Each
> heading below is one draft unit in `literature/writing-plan.md`, so there is no
> second organization to reconcile there either. The transversal block that opens
> the file is the only thing never drafted on its own: the section order, the two
> threads, and the rosters that span units.
>
> **Everything the review left out is in `literature/candidates.md`** — undecided
> works and examined-and-excluded ones, each with its reason. None of it is drafted,
> so none of it is here. A work excluded from the argument may still be *quoted* in
> it, and carries its bib key inline like any other citation.
>
> **Coupling levels — the review's spine,** argued in Beat 4 and the axis §6–§8
> escalate along:
> **Level 0** — the generator *is* a repurposed predictor (inherited weights). An
> attribute of an entry, not a section; marked *(inherits …)*.
> **Level 1** — generate, then filter with a critic, no gradient. Two regimes:
> *confidence-as-critic*, the field's default, against *trained-critic* (§3).
> **Level 2** — backpropagate the predictor's loss into the design variable. Two
> regimes as well, and the distinction is the design variable, not the gradient:
> *continuous relaxation*, where the sequence is a simplex the optimizer descends
> (BindCraft, Germinal, BoltzDesign1, PXDesign-h, ESMFold2), against *discrete
> gradient-guided search*, where it stays one-hot and the gradient only proposes
> and ranks point mutations (RFOptimization, whose stated reason is that a
> continuous representation is an attack surface the optimizer will exploit).
>
> **Scope.** In scope = generates a **protein or peptide binder conditioned on a
> target**, or predicts the structure such a system designs against. Out of scope
> = a different modality (small molecules), or sequence generation with no target
> conditioning. The field moves fast — explosive in 2026 — so references dated
> before 2025 are generally out of scope, except where they belong to an active
> lineage whose full history is kept for understanding (ESM, RoseTTAFold).

---

# Transversal — what belongs to no single unit

Material that runs across the units below and is drafted in none of them. Where it
surfaces in the prose is `writing-plan.md`'s business; what it says is here.

## Section order and progression

Per-lineage organization. Each section pairs a predictor with the design systems
built on it, so a reader meets an architecture once and then follows it to its
conclusion.

**Two axes, used in sequence.** §1–5 are predominantly Level 1, so within that
block the ordering principle is the **generative formalism**: diffusion first,
then flow matching as its successor, then the models that do not say. §6–8 then
escalate by **degree of integration**: first the Level-2 loop as a bare
technique, portable and composable (§6); then a platform that composes both
couplings into one product (§7); then the case where language model, folding head
and design loop are not composed at all but are one model (§8). §9 steps outside
the argument entirely.

| # | Section | Covers | Organizing fact |
|---|---|---|---|
| 1 | **AlphaFold, and the open co-folding cluster** | AlphaFold2, AlphaFold3; OpenFold/OpenFold3; OpenDDE | prediction only; everything later is defined relative to it |
| 2 | **RoseTTAFold → RFdiffusion** | RF1, RFAA, RF3/AtomWorks; RFdiffusion 1/2/3; RFantibody, RFpeptides; ProteinMPNN/LigandMPNN; RFOptimization | diffusion; the first prediction→generation turn; introduces inverse folding — and the only lineage still shipping predictors *and* generators |
| 3 | **Boltz** | Boltz-1, Boltz-2, BoltzGen, BoltzProt-1/BoltzPPI, BoltzMol-1 | diffusion, stated outright — and the lineage that opened, then closed |
| 4 | **Chai** | Chai-1, Chai-2 | Chai-1 is a diffusion co-folder; Chai-2's *generator* is undisclosed |
| 5 | **Flow matching** | FrameFlow, PPIFlow, OriginFlow, AtomFlow, D-Flow | the successor formalism — FrameFlow *"adapt[s] FrameDiff … to the flow-matching generative modeling paradigm"* |
| 6 | **Inversion as a portable technique** | BindCraft, BoltzDesign1, Germinal, mBER | Level 2 as a bare method — four groups, three predictors, one technique |
| 7 | **Protenix** | Protenix-v1, Protenix-v2, PXDesign-d and PXDesign-h | the first pipeline to *compose* both couplings into one platform |
| 8 | **ESM** | ESM-2/ESMFold, ESM-3, ESMC/ESMFold2 and its binder campaign | Level 2, fully integrated — the analytical climax |
| 9 | **The closed frontier** | AlphaProteo, Latent-X 1/2; IsoDDE, Chai-3, SeedFold | benchmarked but unexplainable — a coda, not a step in the argument |

**Level-2 roster, spread across §2 and §6–8 by lineage.** Seven systems, six
groups, five predictor families: BindCraft (AlphaFold2, §6), BoltzDesign1 (Boltz,
§6), Germinal (AlphaFold2 + antibody LM, §6), mBER (AlphaFold-Multimer, §6),
PXDesign-h (Protenix, §7), ESMFold2 campaign (ESMC/ESMFold2, §8), RFOptimization
(RF3, §2). Any claim about Level 2 being general rather than an AF2 quirk rests on
this spread — and on the *groups*, since mBER adds no predictor family. RFO is the
one that also breaks the *continuous-relaxation* assumption the other six share.
**The spread is narrower than the count:** the three AlphaFold-family systems —
BindCraft, Germinal and mBER — all run on ColabDesign (§6), so seven systems are
five implementations.

## The two threads

Two arguments run across the sections rather than living in one. Both are planted
early and paid off late, and neither gets a section of its own.

### MSA emancipation

Planted in Beat 2 (coevolution as the founding bet),
first attacked as a *cost* rather than a dependency by ColabFold (the
instruments), turned in Beat 4 (an MSA is a database lookup on a sequence that
does not exist yet, so a Level-2 loop must run single-sequence), paid off in §8.
Touches §1, §4 (Chai-1's protein-LM track), §6 (BindCraft off-distribution) and §8.

### Cyclic peptides and macrocycles

*Not a modality section — the modality is
the vehicle, and the payload is that this is the one place where the review's
open-versus-closed argument is settled by measurement rather than asserted.*
Where it appears:

| Section | Entry | What the thread takes from it |
|---|---|---|
| §2 | AfCycDesign | where the thread starts — the cyclic encoding, and the critic RFpeptides is filtered by |
| §2 | RFpeptides | the open method, and the corpus's low-water mark for designs tested per target |
| §9 | Latent-X1 | the closed method that re-synthesized RFpeptides' own best binders and measured them in its own assays |
| §9 | Latent-X2 | macrocycles claimed competitive with trillion-scale mRNA display — Beat 3's budget collapse at its most extreme |
| Tables | — | the head-to-head itself, stated in full under Table B |
| §6 | RFOptimization | cyclic peptides as one of its four optimization settings, seeded from RFpeptides |
| §5 | D-Flow | mirror-image D-peptides — the modality's exotic edge, and a *mention*, not a pillar |

Beat 5 argues the frontier publishes benchmarks and withholds mechanisms; this is
the one place where a withholding system did the more disciplined experiment. The
thread is promised in Beat 1, where macrocycles are already named in scope, and
lands under Table B rather than §9 — evidence about measurement, not a point
scored for Latent Labs.

## Non-disclosure

**Non-disclosure covers four of the strongest results** — Chai-2, AlphaProteo,
Latent-X and IsoDDE. Lineages are not fragmented by disclosure status, so Chai-2
stays in §4 and Boltz's closed models stay in §3, each with a pointer to §9.

---

# The introduction

What the introduction establishes, in five beats. A reader who stops here should
already hold the field's anatomy, its coupling taxonomy and its limits; the nine
sections are the lineages in detail.

## Beat 1 — Scope: proteins and peptides, not small molecules

This review covers one problem. **Given a target protein, and usually a chosen
site on it, design a new protein or peptide that binds there.** Antibodies,
nanobodies, VHHs, scFvs, minibinders and macrocyclic peptides are all the same
problem here, because to every model in the review they are the same object: a
chain of amino acids, judged by how it folds against the target.

Small molecules are the other half of binder discovery, and they are out of
scope. The reason is not that their papers live elsewhere. It is that a sequence
is a far easier thing to search than a molecule, in two specific ways, and the
second of them is what most of this review is about.

**Binding degrades gently along a sequence.** Change one atom of a small molecule
and its potency can collapse — the activity-cliff problem — so a small-molecule
generator has to land exactly right rather than merely close. Boltz-2, whose
affinity module is aimed at small molecules, describes the difficulty as
*"distinguishing subtle differences in binding affinity among closely related
analogues"*. Protein binders are far more forgiving between neighbouring
sequences, and that tolerance is the only reason the field's standard move —
generate many candidates, keep the ones a predictor likes — works at all.

**A sequence can be differentiated; a molecule cannot.** This is the deeper
reason, and it is the mechanism Beat 4 is built on. A protein sequence relaxes
cleanly into a continuous object: a probability distribution over the 20 amino
acids at each of *L* positions. Every point in that space is still a valid input
to a structure predictor, so a design loop can hand the predictor a blurred
sequence, read how wrong the resulting structure is, and step downhill. That is
what BindCraft does through AlphaFold2, on an *L*×20 gradient over amino-acid
choices; what Germinal does over antibody CDR logits; and what the ESMFold2 binder
campaign does through a protein language model and a folding head at once. A
molecule is a variable-size graph with hard valence rules, and almost nothing
between two molecules is itself a molecule, so small-molecule generators have to
build discrete machinery — Markov bridges over atom and bond types (`drugflow`),
a mixed continuous-and-categorical scheme (`flowr`) — exactly where proteins need
none. Whether a gradient loop is reachable for small molecules at all is open, and
this review does not settle it; the asymmetry is real, and it is why the two
halves of binder discovery are not one field.

## Beat 2 — The founding bet, and how a co-folder is built

Design needed prediction first, and prediction was solved on a single wager:
**that coevolution between two positions in a multiple sequence alignment is a
usable proxy for the two residues being close in space.** AlphaFold2 cashed it —
median 0.96 Å backbone accuracy on CASP14, against 2.8 Å for the next best method
— and AlphaFold3 generalized it from single chains to arbitrary complexes of
proteins, nucleic acids, ligands and ions.

**Every co-folder in this review is two stages, and they do different jobs.** This
is the anatomy the rest of the review reads through, because almost every
disagreement between systems is a disagreement about one of the two.

**Stage 1 — the trunk. Sequences in, pairwise reasoning out.** What comes out is
principally a **distogram**: for each pair of residues, a probability distribution
over how far apart they are. The contact map *is* the trunk's output, so this is
where the coevolution bet is cashed, and the stage is differentiable throughout.
The variation here is what feeds it, and the divide runs the length of the review:

- **An MSA**, retrieved by searching sequence databases at inference time —
  evolutionary depth looked up on demand. AlphaFold2 and AlphaFold3, RoseTTAFold,
  Boltz, Protenix.
- **A protein language model**, which has the same statistics in its weights, so a
  single sequence is enough. ESM-2 with ESMFold, then ESMC with ESMFold2 (§8).

The divide is not a wall — Chai-1 (§4) carries both tracks and runs on either —
but which of the two a model is built around is the thread this review follows
longest, and what it settles is not accuracy so much as how tightly a generator
can later couple to it (Beat 4).

**Stage 2 — the structure stage. Pairwise reasoning in, atomic coordinates out.**
The variation here is the generative formalism, and what it decides is how many
forward passes one sample costs:

- **A single regression pass — AlphaFold2.** The structure module with IPA,
  trained end to end; AF2's own ablation table lists *"no end-to-end structure
  gradients"* as a measurable cost. Gradients traverse the entire network.
- **Diffusion — AlphaFold3, and everything built in its image.** Coordinates are
  sampled along a long stochastic denoising trajectory. FrameFlow, the paper that
  recast this problem as flow matching, puts the cost at *"∼1000 model forward
  passes ... to produce high-quality samples"*.
- **Flow matching — §5.** An ODE rather than an SDE, with *"straighter sampling
  trajectories"*, so far fewer steps buy the same sample: FrameFlow reports 2×
  designability at 5× fewer sampling steps.

That is the machine. Its limit is where Beat 3 starts: a predictor tells you what
a *given* sequence folds into. It does not tell you which sequence to try.

## Beat 3 — Prediction and generation are the same machinery

**What separates them is only which sequences you hold fixed.** Give a co-folder
every chain in the complex and it predicts a structure. Leave one chain blank —
usually the short binder you are trying to invent — and ask the same model for a
chain that folds against the rest, and the same machine is a generator. BoltzGen
says so outright: *"a single all-atom diffusion model capable of performing both
structure prediction and protein design"*. RFdiffusion reached the same place from
the other direction, by fine-tuning RoseTTAFold — a predictor — into a generator
of backbones. The two halves of this review are one technology used two ways.

**Why the predictor alone was not enough.** A predictor answers a question you
must already have asked: how does *this* sequence fold against the target? It
cannot tell you which sequence to try, and there are vastly more candidates than
anyone can test — twenty choices at every position of a chain tens of residues
long. The established way around that was to let a library do the searching:
immunize an animal, or screen 10¹² or more random sequences by display and keep
whatever sticks. This works, and it is still how most binders are found. Its limit
is not scale but aim. RFantibody states it plainly: *"no method currently exists
to design novel, epitope-specific antibodies entirely in silico. Instead, antibody
discovery currently relies on immunization, random library screening or the
isolation of antibodies directly from patients"*. A library returns binders to
whichever part of the target happens to be accessible or immunogenic; it cannot be
aimed at the site you care about.

**What generation bought is measured in one number: how many designs you have to
physically make before one of them binds.** That collapse is the review's
quantitative spine.

| Era | Designs tested per target | Source |
|---|---|---|
| Screening-based, and early computational design | *"thousands to millions of designs to reliably identify hits"* | Chai-2's characterisation of prior work |
| Current generative + filtering | 16–30 (Protenix-v2), ≤20 (Chai-2), ≤20 (RFpeptides), 30–100 (Latent-X), 43–101 (Germinal), 84 (ESMFold2) | each system's own campaign |

The hit rates in the same papers sharpen it: 16% for Chai-2 on de novo
antibodies, up to 48% and 16–88% on GPCRs for Protenix-v2's VHH-Fc designs, 70%
for ESMFold2's minibinders. **The measure of progress in this field is how few
designs you must make to get a binder**, and the nine sections are, read one way,
a history of that number falling.

Those percentages do not all count the same event. BoltzProt-1 separates
*screening hits* from *confirmed binders* and notes that screening hits are
*"what prior binder design model literature typically reports as binders"*; its
own confirmed-binder rate is 8.0%, where the looser definition would give a much
larger number.

**And the campaign that did not choose its targets.** Every number above comes from
a campaign whose targets and epitopes were selected by the people reporting it. mBER
(§6) is the corpus's one exception: 1,153,241 VHH designs against 436 human
cell-surface proteins, hotspots drawn at random from exposed surface residues, 145
targets screened all-against-all by phage display. Its per-design on-design hit rate
is **0.4% median** (range 0.02–8%, library-wide 0.5% then 0.7%) — two orders of
magnitude below Chai-2's 16% or ESMFold2's 70%, at the same coupling level and on
the same predictor as Germinal. The headline *"45% of targets"* is not a hit rate at
all; it is the fraction of screened targets with a statistically significant excess
of on-design hits.
The spread *inside* this one campaign is the finding. TFRC returns 0.4% (10/2,317)
overall but 7.5% (6/80) at its best hotspot, and the most favourable epitopes reach
38% (8/21) under strict ipTM filtering — back inside the range everyone else
reports. So target and epitope selection alone move a hit rate across the full width
of the literature's spread, which is what the introduction's second caveat asserts
and this is the evidence for. Its hits are also phage-display enrichments, i.e.
BoltzProt-1's *screening hits* rather than confirmed binders, with no affinity
quantification.

**The generative machinery was borrowed from image generation, and the field said
so.** RFdiffusion introduces the technique as *"denoising diffusion probabilistic
models (DDPMs), a powerful class of machine learning models recently demonstrated
to generate new photorealistic images in response to text"*. The parallel is the
field's own and it earns its place twice: it orients any reader who has met Stable
Diffusion, and it explains the formalism shift in §5, because image generation
made the same diffusion → flow-matching move for the same reasons of speed and
simplicity.

The analogy breaks exactly where this field becomes interesting: **image
generation has no AlphaFold.** Nothing scores whether a generated image is
*correct*, so image models are judged by human preference and cannot close a loop
on their own objective. Protein design can, because it has a predictor to grade
against — and how tightly that loop is closed is Beat 4. The borrowed machinery
was the easy half; the critic is the part with no counterpart in the source field.

## Beat 4 — How tightly the generator is coupled to its critic

Every system in this review pairs something that proposes sequences with something
that judges them. What separates them is how tightly the two are bound, and that
is the axis §6–§8 escalate along. The levels themselves are defined in this file's
header; what follows is what each one costs and what it buys.

| Route | What is optimized | Where the critic sits | Corpus examples |
|---|---|---|---|
| **Level 0** — the generator *is* a predictor | the model's own sampling | inside the model | BoltzGen (§3); RFdiffusion 1/2, fine-tuned from RF1 (§2) — Beat 3's identity |
| **Level 1** — backbone, then inverse folding, then a predictor judges | nothing is optimized; designs are sampled and filtered | after the fact | RFdiffusion → ProteinMPNN → AF2 (§2); RFpeptides, BoltzGen, PXDesign-d, Protenix-v2 design |
| **Level 2, continuous** — descend a relaxed sequence | an *L*×20 simplex, annealed to one-hot | inside the loss | BindCraft, Germinal, BoltzDesign1 (§6); PXDesign-h (§7); ESMFold2 (§8) |
| **Level 2, discrete** — gradients only rank point mutations | a sequence that stays one-hot throughout | inside the loss | RFOptimization (§2, §6) |

Level 1 is still the field's default, and it is the origin of the standard success
criterion — AlphaProteo's *"interchain AF2 pAE < 10, binder-aligned binder RMSD <
1 Å, pLDDT > 80"* — which is also the first place a reader meets these units.

**Why MSA emancipation was the precondition for Level 2.** This is the
introduction's one genuinely non-obvious claim. **An MSA is a database lookup on a
sequence that does not exist yet.** It is neither differentiable nor even defined
for a binder still being invented, so any Level-2 loop has to run its predictor
single-sequence on the designed chain. That is why BindCraft, hallucinating
through AlphaFold2, operates the model in exactly the regime AF2's own paper
documents as its weakest — and why ESMC/ESMFold2, which is natively
single-sequence, can backpropagate through a 6-billion-parameter language model
without ever leaving distribution. MSA emancipation is not an accuracy story; it
sets the ceiling on how tightly a generator can couple to its critic.

**Where the gradient attaches is the mechanical half of the same claim**, and Beat
2's anatomy decides it. AlphaFold2 is differentiable end to end, so BindCraft
backpropagates through the whole network. AF3-class models replaced the structure
module with diffusion and broke that — not because diffusion is undifferentiable,
but because unrolling a thousand denoising steps to get a gradient is impossible.
Nothing here is undifferentiable in principle; the trajectory is simply too long.
The corpus holds three answers to that one architectural fact:

- **Attach to the trunk.** BoltzDesign1 stop-gradients the diffusion module and
  optimizes the Pairformer's distogram directly, on the grounds that it
  *"represents the probability distribution of atomic distances that the diffusion
  model later samples from"* — optimize the distribution, not a sampled structure.
- **Attach to the trunk and the confidence heads.** RFOptimization applies the
  same stop-gradient and adds iPAE, pLDDT and iPTM, because the confidence path
  back to the input stays differentiable when the coordinate path does not.
- **Shorten the trajectory until it can be crossed.** Protenix's **two-step ODE
  sampler** is short enough to traverse, so PXDesign-h backpropagates through the
  whole model, which it says permits *"end-to-end backpropagation of gradients
  from all confidence metrics, rather than being limited to contact loss derived
  from Pairformer outputs"* — naming BoltzDesign1 as the limitation it beats. This
  is what §5's formalism shift bought beyond sampling speed: flow matching is what
  made the structure stage short enough to reopen to a design gradient.

The two axes are orthogonal: BoltzDesign1 and RFOptimization attach in the same
place and differ in the design variable; BindCraft and PXDesign-h share the design
variable and differ in the attachment point.

**And the filter, not the generator, is where the hit rate lives.** Level 1 says
"filter", and the field long read that as the predictor's own confidence head.
Three systems say otherwise, which is why Level 1 splits into two regimes in the
header. BoltzPPI (§3) replaces BoltzGen's confidence metrics with a critic trained
to answer "will this bind", and roughly doubles the confirmed-binder rate with the
generator untouched. PXDesign (§7) finds that Protenix and AF2-IG filters retain
*different* true positives. RFOptimization (§2, §6) treats agreement with a single
predictor as the failure mode itself, mixing three predictor families across the
loop and holding one of them out as an independent check — and it is the one that
moves the response out of the filter and into the optimizer.

## Beat 5 — The closed frontier

The limit of what a literature review can establish. The strongest claimed results
increasingly come from systems that publish benchmarks and withhold mechanisms —
AlphaProteo, Latent-X, Chai-2's generator, and IsoDDE, which has no publication at
all and is visible only as the top point on a competitor's scaling curve.

**The sharpest version of this is not IsoDDE — it is Boltz.** The lineage enters
the review as the open answer to AlphaFold3's closed weights and exits with its own
frontier closed: Boltz-1, Boltz-2 and BoltzGen stay MIT, while BoltzProt-1 and
BoltzMol-1 ship API-only with no weights. It is the one lineage where the review
holds the before *and* the after, both with papers.

The symmetry that gives §9 its force: **AlphaFold3 is a Google DeepMind *and
Isomorphic Labs* paper**, so the review opens on the published half of that
organisation's work and closes on the half that stopped publishing.

## Two caveats the introduction plants

1. **The numbers are not as comparable as they look** — different benchmarks,
   cutoffs and target sets, each with a documented defect, gathered under the
   instruments and Tables A and B.
2. **Wet-lab hit rates are self-reported and target-dependent.** Every campaign
   chose its own targets, and the papers that disclose most about their methods are
   not the ones reporting the highest numbers — itself a finding, and Beat 5's
   justification.

---

# The metrics primer

First of the three benchmarking units — with the instruments and the two tables,
which render at the close. It renders here instead because §1–§9 quote pAE, pLDDT,
ipTM and PB-valid from the start, and a reader meeting those units for the first
time in a closing part has been reading numbers on trust. Only its presentation
moves; it belongs with the instruments.

**The problem it solves.** Beat 4 quotes the canonical success criterion before
anything has said what pAE or pLDDT are, and every section afterwards reports
numbers in these units. One place defines them, and this is it. Not in the intro:
a definitions block dropped into Beat 2 or Beat 4 would stall an argument.

**Do not write it as a glossary.** An alphabetical list of metrics is dead weight
the reader skips. Organize it around the one distinction that does analytical work
in this review — **the two families of metric, and which family the design half
actually runs on**:

1. **Ground-truth metrics** — the prediction is compared against a solved
   structure. This family answers *was it right*, requires an experimental
   answer to exist, and is therefore available only for prediction benchmarking
   (Table A below).
2. **Confidence metrics** — the model's own estimate of how much to trust itself.
   No ground truth needed. This family answers *does the model believe it*.

**The point the primer exists to make:** every Level-1 system in this review
filters on family 2. A designed binder has no solved structure by definition, so
the critic can only ever be a self-estimate — the generator is graded by the
predictor's opinion of its own output. That is what makes four findings in the
benchmarking units matter rather than being technicalities: PoseBusters'
incompleteness, AlphaFold-Multimer's ipTM being the metric everyone inherited (§1),
the two measurements of what that self-estimate is worth, reconciled just below,
and BoltzProt-1's BoltzPPI (§3) replacing a confidence head with a critic trained
against experimental outcomes — the first departure from family 2 in the corpus.
The primer is those two families and that consequence; individual metrics appear
only as far as they support it.

**The two measurements, and the distinction they force.** The corpus tests family 2
twice and the results look contradictory until the question is split. Overath (the
instruments) finds precision running 0.1 to 1.0 across targets for the best score
available, and Germinal finds its nonbinders clearing the ipSAE threshold alongside
its binders. mBER (§6) finds the opposite at larger scale: across 1.15M designs, hit
rates climb with ipTM while off-design rates stay flat. Both hold, because they
answer different questions. At population scale a confidence score **enriches**; on
any individual design it does not **discriminate**. Enrichment is what a library
campaign needs, discrimination is what low-*n* testing needs — so the same metric is
validated in §6 and inadequate under Table B, and Beat 3's collapsing budget is
exactly the move from the regime where enrichment suffices into the one where it
does not.

---

# §1 — AlphaFold, and the open co-folding cluster

Prediction only. The forward problem — sequence / chemical input → 3D structural
state — and the reference every later section is defined against.

*Why it opens:* AlphaFold is the elephant in the room — everything later
reproduces it, reacts to it, or replaces its evolutionary input, so the review
cannot begin anywhere else without the reader waiting for it. **OpenFold3 and
OpenDDE join it here** rather than getting their own sections: open co-folding
models in the AF3 mould with no design descendant to follow.

* **AlphaFold2** — `alphafold2` · `10.1038/s41586-021-03819-2` · **backbone** — single-chain and
  multimer predictor that established modern deep-learning structural biology;
  the MSA-as-coevolution bet every later model inherits or reacts against.
  *Also serves as:* the differentiable objective in BindCraft and Germinal (§6)
  and the standard post-hoc filter across §2–5 and §7.
* **AlphaFold-Multimer** — `alphafold_multimer` · `10.1101/2021.10.04.463034` · **backbone** —
  AF2 retrained on complexes, and the complex predictor the review actually runs
  on: §6 does not invert AlphaFold2, it inverts this. Kept despite the pre-2025
  rule under the active-lineage exception.
  *Also where ipTM comes from*, which makes it the unit half the review's numbers
  are denominated in — load-bearing for §2–§7 and the benchmarking units, not
  only §6.
  *Never peer-reviewed:* the field's most-used complex predictor has no journal
  version — a disclosure gap of a different kind from §9's.
* **AlphaFold3** — `alphafold3` · `10.1038/s41586-024-07487-w` · **backbone** — all-atom
  diffusion predictor for protein / nucleic-acid / small-molecule / ion
  complexes. Closed weights — the stated motivating gap behind Boltz-1, Protenix
  and OpenFold3, and the origin of the openness thread that closes in §9.
* **OpenDDE** — `opendde` · `10.48550/arXiv.2607.03787` · **meat** — Apache-2.0 all-atom
  co-folding foundation model with atomic latent reasoning; reports IsoDDE-level
  accuracy, a cross-model scaling law, and the corpus's most complete third-party
  antibody-antigen head-to-head. Design is roadmap only — explicitly *"not a
  complete drug-discovery system"*. [GitHub](https://github.com/aurekaresearch/OpenDDE)
* **OpenFold → OpenFold3** — AlQuraishi Lab's open reimplementations; OpenFold
  reproduces AlphaFold2 and supplies the distillation set Boltz-1 trains on,
  OpenFold3-preview targets bitwise AF3 reproduction.
  [GitHub](https://github.com/aqlaboratory/openfold-3)
  *(map-only — code releases, no paper or DOI; third-party benchmark numbers
  exist, run as a baseline by Protenix-v2 and OpenDDE.)* · **mention**

# §2 — RoseTTAFold → RFdiffusion

The Baker Lab / IPD line, kept whole: the structure predictors, the generative
models fine-tuned from them, the sequence-design stage the whole field borrowed,
and — newest — the optimizer that refines their output. Level 0 in its purest
form for RFdiffusion 1/2 and their modality arms: one architecture serving
prediction or generation depending on what it is fine-tuned for.

*Why it is second:* the RoseTTAFold lineage explored every aspect of the problem,
and that makes it the best teacher in the review. A reader who has been through it
once has met prediction, the generative turn, inverse folding, antibodies,
macrocycles and gradient optimization — the whole pipeline, in one architecture
family, before any other lineage asks them to hold a partial view. It is also the
one architecture developed independently of AlphaFold, so placing it second
establishes early that this field has two origins rather than one.

**Section-defining fact:** the lineage is the only one in the review that is whole
at both ends. Its *early* predictors have left the conversation — nothing published
since 2024 benchmarks against RF1 or RFAA, and the recent co-folding papers do not
mention them — while as *generators* they remain the reference the whole field
cites. But the predictor track did not stop: **RF3 (2025) is current**, benchmarks
directly against AF3, Boltz-2 and Chai-1, and is what RFOptimization takes its
gradients from. So §2 is not a lineage that turned generative and abandoned
prediction; it is the one lineage still shipping both, from one framework.
*The two tracks' names collide:* **RF3** (RoseTTAFold3) is the predictor,
**RFdiffusion3** (RFD3) the generator. Siblings built on the same AtomWorks
framework, not two versions of one model. Both diffuse — RF3 denoises coordinates
for a **known** sequence, RFD3 invents a backbone with the sequence **unknown**,
which is why RFD3 is followed by ProteinMPNN and RF3 is not.

**With RFOptimization, this lineage covers every stage of the problem** —
predict, generate, inverse-fold, optimize, filter — and it is the only one that
does. It is not a platform in §7's sense: RFO is a refinement stage rather than a
second generation arm, and it is deliberately assembled from three lineages
(RF3 + Boltz + AF3) rather than one, so §7 keeps the
*first-to-compose-both-couplings* claim on dates and on kind.

* **RoseTTAFold (RF1)** — `rosettafold` · `10.1126/science.abj8754` · **backbone** — three-track
  (1D/2D/3D) network developed independently of AF2; complex prediction emerged
  untrained from two-segment cropping. The architecture the family fine-tunes from.
  *Carries:* §2's organizing fact — the one architecture in the review not derived
  from AlphaFold, which is what makes the lineage a second origin rather than a fork.
  *Intermediate steps, map-only:* RoseTTAFoldNA and RoseTTAFold2 (preprints; RF2
  is RFAA's base network). · **mention** — though RF2 is the network RFpeptides
  adds cyclic encoding to, so the cyclic thread names it.
* **RoseTTAFold All-Atom (RFAA)** — `rosettafold_all_atom` ·
  `10.1126/science.adl2528` · **meat** — all-atom generalization published two months
  *before* AF3 and independently of it; encodes chirality as architectural input
  features rather than as a loss or post-hoc penalty. No diffusion module.
* **RoseTTAFold3 (RF3)** — `rosettafold3` · `10.1101/2025.08.14.670328` · **backbone**
  — the lineage's current all-atom predictor, AF3-class with a diffusion structure
  stage, trained on **AtomWorks**, the IPD's data framework for building structure
  models, which RFdiffusion3 is also built on. BSD, with weights. Benchmarks
  between closed AF3 and open Boltz in
  almost every category; on antibody-antigen, DockQ > 0.23 for 33% of cases against
  44% (AF3), 28% (Chai-1) and 22% (Boltz-2).
  *Carries:* two things nothing else in §2 does. It is the **predictor
  RFOptimization inverts** (§6), so the corpus's only discrete Level-2 system runs
  on a model the review can now cite. And it turns RFAA's chirality choice into a
  measured argument — stereochemistry as a *learned* feature (signed angles at each
  chiral centre, plus inverted-chirality training augmentation) beating
  **inference-time guidance**, which the paper argues *"may shift the network
  outside the training distribution"*. Directly answers Boltz-1x's steering
  (the instruments), and reaches the cyclic thread through mixed L/D peptides.
* **RFdiffusion** — `rfdiffusion` · `10.1038/s41586-023-06415-8` · **backbone** *(inherits RF1)*
  — SE(3)-equivariant frame diffusion; established modern generative backbone
  design. Filtered by AF2 pAE / "in silico success".
  *Carries:* Beat 3's borrowed-from-image-generation passage, and step 2 of §6's
  arc — it is the paper that beat hallucination and sent Level 2 quiet.
  [GitHub](https://github.com/RosettaCommons/RFdiffusion)
* **RFdiffusion2** — `rfdiffusion2` · `10.1038/s41592-025-02975-x` · **mention** *(inherits RF1)*
  — atom-level enzyme active-site scaffolding from functional-group positions,
  sequence-agnostic.
* **RFdiffusion3** — `rfdiffusion3` · `10.1101/2025.09.18.676967` · **meat** —
  transformer-based all-atom diffusion across proteins, DNA, RNA and ligands;
  adopts AF3's non-equivariant diffusion approach.
  *Not Level 0:* unlike RFdiffusion 1/2 it is not fine-tuned from a RoseTTAFold
  predictor — it is a new architecture trained from scratch on the PDB plus AF2
  distillation structures, built on **AtomWorks**, the lineage's data framework.
  RF3 appears in RFD3's pipeline only as a refolding oracle, beside AF3.
* **RFantibody** — `rfantibody` · `10.1038/s41586-025-09721-5` · **backbone** *(inherits RFdiffusion)*
  — the lineage's antibody arm: a fine-tuned RFdiffusion designing VHHs, scFvs and
  full antibodies against chosen epitopes.
  *Why it matters to the argument:* it pairs design with **yeast-display library
  screening**, and says the screen is still necessary. That makes it the honest
  baseline Beat 3's collapsing-budget table is measured against, and the paper
  §3, §4 and §6 cite when claiming they no longer need library selection.
  *Collision:* Beat 3 quotes its statement of the epitope gap (*"no method
  currently exists to design novel, epitope-specific antibodies entirely in
  silico"*); what this entry owns is the concession that the screen remains.
* **RFpeptides** — `rfpeptides` · `10.1038/s41589-025-01929-w` · **backbone** *(inherits RFdiffusion)*
  — the lineage's macrocycle arm: RFdiffusion and RF2 extended with a **cyclic
  relative positional encoding** so the generated chain closes head-to-tail;
  sequences from ProteinMPNN, filtered by refolding with AfCycDesign and by Rosetta
  interface metrics. Level 1.
  * **AfCycDesign** — `afcycdesign` · `10.1038/s41467-025-59940-7` · **mention** —
    the critic above: AlphaFold2 given a cyclic offset on its relative positional
    encoding so the chain reads as closed, and the lineage this arm starts from.
    Also hallucinates macrocycles de novo and designs binders from them, so the
    cyclic thread begins here rather than at RFpeptides.
  *Carries:* the low end of Beat 3's budget — binders against all four targets
  from fewer than 20 synthesized designs each, with crystal structures on three —
  and the cyclic thread's open method, against Latent-X1's undisclosed one (§9).
  [code](https://github.com/RosettaCommons/RFdiffusion)
* **RFOptimization (RFO)** — `rfoptimization` · `10.64898/2026.09.04.749184` · **meat** —
  training-free refinement of existing designs, seeded from RFdiffusion and
  RFpeptides outputs. *Level 2; reviewed in full in §6.* Listed here because it is
  the stage that completes this lineage's stack.
* **ProteinMPNN** — `proteinmpnn` · `10.1126/science.add2187` · **backbone** · and
  **LigandMPNN** — `ligandmpnn` · `10.1038/s41592-025-02626-1` · **meat** — autoregressive
  message-passing networks generating sequences for a fixed backbone (and ligand
  / nucleic-acid environment, for LigandMPNN). The standard inverse-folding stage
  between backbone generation and structural validation, introduced here because
  §3–7 all rely on it. [GitHub](https://github.com/dauparas/ProteinMPNN)
  *Adoption is field-wide, not lineage-bound* — used across nine distinct labs and
  both coupling levels, so it is shared machinery rather than a Baker-lab
  component.
  *Adoption, not necessity* — AlphaDesign (§6) substitutes an autoregressive
  diffusion model of its own and benchmarks it as comparable, the corpus's one
  alternative.

# §3 — Boltz

Diffusion, stated outright: BoltzGen is *"a single all-atom diffusion model
capable of performing both structure prediction and protein design"* — Level 0
in its cleanest published form. The section also carries two things the rest of
the review needs: the **trained-critic** refinement to Level 1, and the
**open→closed fork** that Beat 5 and §9 turn on.

*Why it precedes Chai:* BoltzGen states its mechanism plainly and shows the
Level-0 identity in its purest form — one diffusion model doing prediction *and*
design — and the two refinements below are the ones Beat 4 and §9 need.

**The fork** (stated in Beat 5, evidenced here): Boltz-1, Boltz-2 and BoltzGen
remain MIT with weights released; BoltzProt-1 and BoltzMol-1 are API-only and
commercial, yet still publish papers and wet-lab numbers. That is what makes this
a better §9 exhibit than IsoDDE — the review holds the before and the after with
publications on both sides, where IsoDDE has only an after.

* **Boltz-1** — `boltz1` · `10.1101/2024.11.19.624167` · **backbone** — first fully open (MIT)
  AF3-class co-folder; Boltz-1x adds Feynman-Kac inference-time steering for
  physical validity. Source of this project's only independent cross-model
  physical-validity measurements. [GitHub](https://github.com/jwohlwend/boltz)
* **Boltz-2** — `boltz2` · `10.1101/2025.06.14.659707` · **meat** — adds a binding-affinity
  module (approaching FEP accuracy at >1000× lower cost), MD-ensemble
  conditioning, and the most complete conditioning system in the corpus (method,
  multimeric templates, contacts/pockets, each with optional hard steering).
  *Caveat:* benchmark numbers carry a temporal-leakage caveat flagged
  independently by ESMC, Protenix-v1 and Protenix-v2.
* **BoltzGen** — `boltzgen` · `10.1101/2025.11.20.689494` · **backbone** *(inherits Boltz)* —
  unified generative design across proteins, peptides, nanobodies, antibodies and
  small molecules, filtered by refolding with Boltz-2. Level 1,
  confidence-as-critic — the baseline BoltzProt-1 then beats by changing only the
  critic.
* **BoltzProt-1** — `boltzprot1` · `10.64898/2026.06.23.733997` · **backbone** *(inherits BoltzGen)*
  — a refined BoltzGen ranked by **BoltzPPI**, a critic trained to answer "will
  this bind" rather than a confidence head reused as one. Changing only the filter
  sharply raises the hit rate — the map's cleanest evidence that the critic, not
  the generator, is where hit rate lives. *Level 1 still, but the trained-critic
  regime.* API-only: the closed half of the fork above. It also splits *screening
  hits* from *confirmed binders*, a definition problem Beat 3 and Table B inherit.
  * **BoltzPPI** — the critic itself, no separate publication.
    *(resolves to the `boltzppi` keyword on `boltzprot1`.)* · **backbone** — it is
    the trained-critic half of Beat 4, and the reason BoltzProt-1 is backbone.
* **BoltzMol-1** — `boltzmol1` · `10.64898/2026.07.04.736485` · **mention** — small-molecule hit
  discovery over an optimized Boltz-2. API-only, no weights.
  *Out of scope by modality* — it screens catalogue compounds rather than
  generating binders, the same exclusion that keeps DrugFlow and FLOWR out.
  **Kept here rather than there** because it is a Boltz model first, and the fork
  above needs both closed models in one place. It contributes nothing else.
* **BoltzDesign1** — `boltzdesign1` · `10.1101/2025.04.06.647261` · **meat** — inverts the
  Boltz predictor for binder design. *Level 2; reviewed in full in §6*, where the
  portability argument needs it next to BindCraft.

# §4 — Chai

Diffusion co-folding, then the strongest antibody-design result in the corpus
from a generator whose mechanism is never stated.

* **Chai-1** — `chai1` · `10.1101/2024.10.10.615955` · **meat** — AF3-derivative adding a
  protein-LM track alongside the MSA track (either usable alone) and
  experimentally-grounded constraint features (pocket, contact, docking). The
  partial-MSA-emancipation hinge that §8 completes.
  [GitHub](https://github.com/chaidiscovery/chai-lab)
* **Chai-2** — `chai2` · `10.1101/2025.07.05.663018` · **backbone** *(inherits Chai-1, via a
  "Chai-1d" design prototype)* — zero-shot antibody design; ~16% wet-lab hit rate
  in 24-well-plate assays across 52 unbiased targets.
  *Disclosure note:* the paper describes only the *folding* submodule (Chai-2f,
  *"a similar architecture as Chai-1"*); the generative mechanism is never
  stated. Reported here, with a pointer to §9.
* **Chai-3 (2026)** — high-throughput commercial 3D foundation model.
  [platform](https://lab.chaidiscovery.com/) *(map-only — no publication;
  discussed in §9.)* · **mention**

# §5 — Flow matching

Presented in these papers as the successor to diffusion rather than an
alternative — FrameFlow explicitly recasts FrameDiff as SE(3) flow matching and
reports 2× designability at 5× fewer sampling steps. All five generate protein or
peptide binders conditioned on a target; flow-matching papers that generate small
molecules or unconditioned sequences are excluded (`candidates.md`).

*Why it comes after the diffusion sections, not before:* flow matching only reads
as a successor once the reader has seen diffusion doing real work, and FrameFlow
is literally FrameDiff reformulated, so the section opens by re-deriving something
familiar rather than introducing a parallel formalism cold.

* **FrameFlow** — `frameflow` · `10.48550/arXiv.2310.05297` · **backbone** — recasts FrameDiff as
  SE(3) flow matching; methodological ancestor of the rest of this section.
* **PPIFlow** — `ppiflow` · `10.64898/2026.01.19.700484` · **mention** — SE(3) flow matching
  with in-silico maturation for picomolar/nanomolar binders and single-domain
  antibodies.
* **OriginFlow** — `originflow` · `10.1101/2025.04.29.651154` · **mention** — combined SDE and
  flow-matching framework; reports 90% wet-lab hit rates across PD-L1, RBD, VEGF.
* **AtomFlow** — `atomflow` · `10.48550/arXiv.2409.12080` · **mention** — atomic flow matching
  on unified biotokens; generates ligand-binding pockets from 2D molecular graphs
  without bound conformers.
* **D-Flow** — `dflow` · `10.1109/JBHI.2026.3683934` · **mention** — full-atom flow matching for
  bioorthogonal D-peptide binders.
  *Borderline on modality, included deliberately:* mirror-image peptides are an
  exotic chemistry unlike anything else here, but the paper is target-conditioned
  binder design, so the scope rule keeps it.

**This is not a lineage.** Only FrameFlow has traction as the methodological
ancestor; the other four are cited by nothing else in the corpus, so what §5
holds is a set of parallel isolated efforts responding to one problem.
*What redeems it is Beat 4's step-count argument:* flow matching's ODE formulation
shortens the structure stage enough for PXDesign-h to backpropagate through it end
to end, so the formalism shift has a consequence beyond sampling cost — it is what
reopened the whole network to a design gradient.

# §6 — Inversion as a portable technique

**Level 2, isolated.** Gradients flow through a structure predictor into the
design variable. Not a lineage — a *method*, shown here to be portable across
predictor families and research groups, met as a bare part before §7 builds it
into a product and §8 dissolves it into a single model.

*Why it comes before §7 and §8:* a pipeline is a composition of techniques and the
reader should meet the part before the assembly. §8 is the limit case with nothing
left to compose, which is why it ends the argument rather than §9.

The arc to carry into the section:

1. *Tried early.* Constrained **hallucination** — optimizing a sequence through
   RoseTTAFold until it predicts the target fold — was the Baker lab's approach
   before RFdiffusion.
2. *Abandoned.* RFdiffusion's own paper reports beating it: *"RFdiffusion
   significantly outperforms Hallucination (with RF) at unconditional monomer
   generation"* (z = 9.5, P = 1.6 × 10⁻⁹). Diffusion won, and Level 2 went quiet.
   *Whose verdict:* the Baker lab's, on its own predecessor — AlphaDesign below is
   the contemporaneous group that did not accept it.
3. *Revived.* It returns on predictors strong enough to be run single-sequence
   without falling off-distribution — the precondition argued in Beat 4.
4. *Portable.* Counting the systems housed in §2, §7 and §8, it now runs on five
   predictor families across six groups — the roster counted in the transversal
   block. mBER is the case that separates the two counts: a sixth group on a
   predictor family already present, so it strengthens the claim about *groups*
   and leaves the claim about *architectures* where it was. *Where the claim
   thins:* on the AlphaFold family the portability is one codebase —
   ColabDesign, below.
5. *Conceded.* RFOptimization closes the arc: the Baker lab returns to the
   technique it abandoned in step 2, on its own AF3-class predictor, and reports
   beating BindCraft on cost per filter-passing design.

* **AlphaDesign** — `alphadesign` · `10.1038/s44320-025-00119-z` · **mention** —
  hallucination through AlphaFold2, searched by an evolutionary algorithm rather
  than descended by a gradient, so Level 1 and not part of this section's roster.
  The independent group that hallucinated from 2021 and never abandoned it, with
  in vivo hits — the date step 2 is qualified against.
* **ColabDesign** — `colabdesign` · `10.5281/zenodo.13309080` · **mention** — the framework
  for running AlphaFold backwards: input preparation, losses over the model's outputs, and
  gradients from those losses to the sequence, in a continuous and a discrete regime. Three
  of this section's systems are built on it — BindCraft, Germinal and mBER, with
  OpenGerminal inheriting it through Germinal — as is AfCycDesign (§2), where the cyclic
  offset lives. No paper; a versioned software release, cited as a repository by the work
  that depends on it.
  *What the dependence covers:* not just an AF2 wrapper. mBER runs ColabDesign's
  `design_3stage` protocol and reports its losses and hyperparameters *"largely inherited
  from ColabDesign and BindCraft"*; Germinal takes both the loss set and the gradient
  scaling, *"as originally done by ColabDesign"*; BindCraft the backpropagation itself.
  So step 4's portability holds across *groups* and across *predictors*, but on the
  AlphaFold family it is one implementation being retargeted. BoltzDesign1,
  RFOptimization and the ESMFold2 campaign are the instances that left it, and they are
  what the claim about architectures actually rests on.
* **BindCraft** — `bindcraft` · `10.1038/s41586-025-09429-6` · **backbone** — backpropagates
  through AF2-multimer weights to produce an *L*×20 error gradient over
  amino-acid choices, annealed in four stages from continuous logits to one-hot.
  Target flexibility retained; no separate scaffolding step.
  *Carries:* Beat 1's differentiability asymmetry (the *L*×20 gradient is the
  worked example) and Beat 4's off-distribution claim — it is the canonical
  Level-2 system the other four are read against.
  *Predictor:* AlphaFold2 (§1), run single-sequence for the designed chain —
  off-distribution for AF2, which the annealing and 5-model ensembling appear to
  compensate for.
  *Attachment (Beat 2's anatomy):* the whole network. AF2 has no diffusion stage,
  so this is the only Level-2 system that never has to choose where to attach.
* **BoltzDesign1** — `boltzdesign1` · `10.1101/2025.04.06.647261` · **meat** — the same
  inversion moved from AlphaFold2 to the Boltz all-atom predictor (§3).
  *Attachment:* stop-gradient on the diffusion module, optimizing the Pairformer
  distogram — the first system in the corpus to hit the AF3-class wall and answer
  it by retreating to the trunk. Beat 4 quotes it.
  *Relation that matters:* it shares senior authors with BindCraft, so the two are
  one research programme porting one method, not two independent data points. The
  independence of the technique rests on Germinal, mBER, PXDesign-h and ESMFold2.
* **Germinal** — `germinal` · `10.1038/s41587-026-03187-0` · **backbone** — gradient-based
  hallucination through AlphaFold-Multimer for epitope-targeted antibody CDRs.
  *Essentially BindCraft for antibodies*, and the paper's own framing; the group
  is independent of BindCraft's, which is what §6's portability claim rests on.
  *Distinct in the way that matters:* the only Level-2 system putting a **sequence
  prior inside the loss**, merging the predictor's gradient with an antibody
  language model's — where §8 reaches the same place with one model, not two.
  *The claim is narrow, and mBER below is the near neighbour that tests it:* mBER
  also carries a PLM prior through every optimization step, but as a fixed logit
  bias from one ESM2 forward pass, with no gradient through the language model.
  Germinal merges two live gradients; mBER biases one. Stated because the two
  otherwise read as the same move.
  * **OpenGerminal** — `opengerminal` · `10.64898/2026.06.25.734527` · **mention** — Apache-2.0
    reimplementation on an open stack; the counter-movement to §3's closure.
* **mBER** — `mber` · `10.1101/2025.09.26.678877` · **meat** — Manifold Bio's
  open-source (MIT) VHH designer, concurrent with and independent of Germinal, which
  both papers state. Same technique and same predictor as BindCraft — ColabDesign
  backpropagation through AlphaFold-Multimer — so it adds a *group* to this
  section's count, not a predictor family.
  *Its own answer to Beat 4's off-distribution problem:* **structural templates**,
  where BindCraft uses annealing and 5-model ensembling. With a binder template, a
  truncated target and the ESM2 prior above, AlphaFold-Multimer produces confident
  docked folds **with no MSA at all** — the MSA-emancipation thread's most explicit
  statement outside §8.
  *Carries:* Beat 3's counterweight, which is why it is here — see there. Also the
  enrichment half of the metrics primer's conclusion: across 1.15M designs with
  paired outcomes, hit rates climb with ipTM while off-design rates stay flat.
* **RFOptimization** — `rfoptimization` · `10.64898/2026.09.04.749184` · **meat** —
  gradient-guided mutation through RF3, interleaved at even odds with a cycling
  move (Boltz prediction → ProteinMPNN/LigandMPNN inverse folding), under
  Metropolis-style acceptance with temperature annealing (the paper notes it
  carries no proposal-density ratio, so it is not Hastings-corrected). *Home section §2*
  (Baker lab / IPD); reviewed here because it changes the category three ways:
  *(i) Discrete, not continuous* — the second Level-2 regime in the header, and the
  only instance of it. *Attachment:* trunk plus confidence heads, diffusion
  stop-gradiented, as BoltzDesign1 does — the two differ in the design variable,
  not the attachment point.
  *(ii) Refinement, not generation* — it moves borderline RFdiffusion / RFpeptides
  outputs across the filter rather than designing from scratch. A new *stage*, not
  a competing generator.
  *(iii) Deliberately cross-lineage* — gradients from RF3, cycling through Boltz,
  final filter by AF3, as an anti-overfitting measure with AF3 held out so it can
  serve as an independent check; the ablations say the two-branch protocol beats
  either branch alone under a three-model consensus. *In silico only — no wet-lab
  validation.*
  *Code status:* no code-availability statement and no findable repository, but
  the Supplementary Methods document "the RFO repository", a public CLI and
  "public software behavior" at parameter level — a real software release
  described without an address.

# §7 — Protenix

The first full assembly. One lineage ships the predictor, a Level-1 diffusion arm
and a Level-2 hallucination arm as a single platform — the couplings of §1–6 stop
being alternatives and become two modes of one product, chosen per target. It is
also where §6's technique gets benchmarked from the outside.

* **Protenix-v1** — `protenix_v1` · `10.64898/2026.02.05.703733` · **meat** — ByteDance
  Seed's open all-atom model matching AF3 under matched cutoff/scale/inference
  budget; adds RNA MSAs and protein templates. Contributes the
  common-intersection critique of FoldBench (the instruments).
  [GitHub](https://github.com/bytedance/Protenix)
  *Predecessor, map-only:* the 2024/2025 *Protenix — advancing structure
  prediction through a comprehensive AlphaFold3 reproduction* technical report
  (v0.2.0/v0.5.0), cited as ref 19 by Protenix-v1; not cataloged, not in corpus.
  · **mention**
* **Protenix-v2** — `protenix_v2` · `10.64898/2026.04.10.717613` · **meat** — both halves in
  one paper, which is why the lineage reads as a platform rather than a model.
  *Prediction:* antibody-antigen gains over v1, plus the finding that the
  PoseBusters criterion is itself incomplete (the instruments). *Design (Level 1,
  inherits Protenix):* target-conditioned generation across miniproteins, VHH and
  Fv, with epitope-specific and site-agnostic modes.
* **PXDesign** — `pxdesign` · `10.1101/2025.08.15.670450` · **backbone** — the platform that
  composes both couplings, and the reason this section sits where it does:
  * **PXDesign-d** — diffusion arm, Level 1 *(inherits Protenix)*.
  * **PXDesign-h** — hallucination arm, **Level 2**, backpropagating through
    Protenix. Benchmarked head-to-head against exactly BindCraft and BoltzDesign1
    — evidence the field treats §6 as one category.
    *Attachment:* end-to-end through the two-step flow, which it argues beats being
    *"limited to contact loss derived from Pairformer outputs"* — a direct answer
    to BoltzDesign1, and the corpus's clearest instance of the field arguing about
    where a Level-2 gradient should attach. Beat 4 plants it.
  * *Also contributes the filter-ensembling finding:* Protenix and AF2-IG filters
    retain **different** true positives with limited overlap — the other half of
    Beat 4's critic-quality argument, alongside BoltzPPI.

# §8 — ESM

The analytical climax: the only entry where language model, folding head and
design loop are one system.

* **ESM-2 & ESMFold** — `esm2` · `10.1126/science.ade2574` · **meat** — founding
  single-sequence predictor; structure emerges from masked-LM scaling alone, no
  MSA or templates at inference. Enabled the ESM Metagenomic Atlas (>617M
  predicted structures; the Atlas itself is a database, out of scope).
* **ESM-3** — `esm3` · `10.1126/science.ads0018` · **mention** — multimodal promptable PLM
  tokenizing sequence, structure and function in parallel tracks. A lineage step,
  reviewed as such rather than as a competitor on folding accuracy.
* **ESMC & ESMFold2** — `esmc` · `10.64898/2026.06.03.729735` · **backbone** — Biohub /
  EvolutionaryScale's ~2.8B-sequence LM plus a folding head on its frozen
  representations. **Full MSA emancipation:** single-sequence antibody-antigen
  accuracy exceeding AF3-with-MSA, with a detachable MSA encoder kept only as a
  rescue path for high-perplexity sequences.
  *Covers:* ESMFold2 and ESMFold2-Fast (modules of this release, no separate paper).
  * **ESMFold2 binder design campaign** — **Level 2**, and the tightest coupling
    in the review: gradients pass through the language model as well as the
    folding head, so there is nothing left to compose. Single-sequence is its
    native regime, so unlike §6's systems it pays no off-distribution penalty —
    the point the MSA throughline has been building toward since §1, and what
    makes §8 the climax rather than ESMC's folding accuracy.
    *(module of the ESMC release — no separate publication.)* · **backbone**

# §9 — The closed frontier

A coda, not a step in the argument. Systems that publish benchmarks and withhold
mechanisms — placed last because they cannot be analysed the way §1–8 analyse
everything else. **Two tiers, and they are not the same problem.**

**Tier 1 — published, results disclosed, mechanism withheld.**

* **AlphaProteo** — `alphaproteo` · `10.48550/arXiv.2409.08022` · **backbone** — DeepMind
  generative engine plus a multi-stage filter for picomolar/nanomolar binders.
  Describes its generator only as *"a generative model trained on structure and
  sequence data from the PDB and a distillation set of AlphaFold predictions"*.
  Defines in-silico success as *"interchain AF2 pAE < 10, binder-aligned binder
  RMSD < 1 Å, pLDDT > 80"* — the canonical statement of the Level-1 criterion,
  quoted in Beat 4.
* **Latent-X1** — `latentx1` · `10.48550/arXiv.2507.19375` · **backbone** · and **Latent-X2** —
  `latentx2` · `10.48550/arXiv.2512.20263` · **meat** — Latent Labs' atom-level binder design
  platform: macrocycles and minibinders (X1), then drug-like low-immunogenicity
  antibodies validated in human panels (X2). Reports >90% wet-lab hit rates on
  macrocycles — the corpus's highest, and self-reported. Filters on ipTM/pAE and
  self-consistency; architecture credited only as *"our proprietary
  architecture"*. The one design lineage in this map with no predictor parent in
  §1–8.
  *The one tier-1 entry that can be checked against an open method:* Latent-X1
  benchmarks itself against **RFpeptides** (§2) on macrocycles and re-synthesized
  its published best binders to measure them in its own assays — the corpus's only
  third-party wet-lab head-to-head between design methods. Stated in full under
  Table B, where its limits belong.
* **Back-references:** **Chai-2**'s generator (§4) and **BoltzProt-1 /
  BoltzMol-1** (§3) belong to this tier and are reviewed in their own lineages.
  Boltz is the tier's most informative case because the same lab's earlier models
  are open and in the corpus — the comparison the other entries do not permit.

**Tier 2 — no publication at all, known only through other people's benchmarks.**

* **IsoDDE** (Isomorphic Labs) — the frontier reference at the top of OpenDDE's
  scaling curve, and the purest case of the tier: everything the review can say
  about it was measured by a competitor, which OpenDDE itself states as a limit on
  what can be concluded. *(map-only — private, no publication.)* · **backbone**
  — it is the review's only fully unpublished system, and Beat 5's Tier 2 rests
  on it.
* **Chai-3** and **SeedFold** — a commercial web platform and a point on
  OpenDDE's scaling curve respectively. *(map-only.)* · **mention**

For all of Tier 2, every number this review can cite was measured by a
competitor. Beat 5's symmetry lands here: Isomorphic authors are core
contributors on the AlphaFold3 paper, so the review opens on the published half of
that organisation's work and closes on the half that stopped publishing.

---

# The instruments

Not models, but the instruments every number in §1–§9 is denominated in. Written
once, referred to from any section.

* **ColabFold** — `colabfold` · `10.1038/s41592-022-01488-1` · **meat** — the apparatus
  rather than a scorer: AlphaFold2 and AlphaFold-Multimer weights untouched, with the
  HMMer/HHblits homology search replaced by a hosted MMseqs2 server over UniRef100,
  PDB70 templates and a new environmental set (ColabFoldDB), delivered as a Colab
  notebook and a `colabfold_batch` CLI. 40–60× faster search, ~5× end to end, ~90× in
  batch — a 1,762-protein proteome in 48 h on one GPU. Accuracy holds: mean TM 0.887
  against AF2's 0.888 across CASP14, 0.826 against 0.79 on the free-modeling subset, and
  parity with AlphaFold-Multimer on ClusPro.
  *Carries:* the AF2 numbers elsewhere in the review are ColabFold numbers. Chai-1 and
  Chai-2 name the version they ran, and ESMC builds every evaluation MSA with it — so
  Table A's AF2 column and Table B's AF2/AF-M filters rest on ColabFoldDB MSAs rather
  than the BFD/MGnify pipeline AF2 shipped with. The Overath meta-analysis goes further:
  one ColabFold MSA per target, *"reused across ColabFold, AF3, and Boltz-1"*, so the
  design half's only cross-lab instrument reports all three of its predictors on
  ColabFold's alignments.
  *Where it meets the design half:* it exposes AF2's internals, and reports that
  *"designed proteins without known homologs"* are the case extra recycling rescues —
  Beat 4's off-distribution problem, named in 2022 and answered with a knob. The
  corpus turns that knob in both directions: recycling to 12 lifts CASP14 targets with
  little MSA information, while the Overath pipeline cuts recycles from ten to three
  to afford its scale. A parameter the papers set differently, on numbers the review
  compares.
  *Also drives RoseTTAFold* (§2), far behind AF2 there: TM 0.754 against 0.888 over CASP14.
* **PoseBusters** — `posebusters` · `10.1039/D3SC04185A` · **meat** — 18-check
  physical/chemical validity suite (RDKit) plus a benchmark set; source of the
  "PB-valid" metric reported by AF3, Chai-1, Boltz-1 and Protenix. Its own
  finding — that deep-learning docking did not beat classical tools on physical
  plausibility or generalization to novel sequences — concerns ligand docking, so
  it is a ligand-side instrument doing protein-side duty here.
  *Known limit:* Protenix-v2 shows the criterion is incomplete — structures pass
  while exhibiting twisted amides and distorted aromatics.
  *(PoseBusters V2 — a benchmark-set revision, not a separate publication; map-only.)* · **mention**
* **FoldBench** — `foldbench` · `10.1038/s41467-025-67127-3` · **backbone** — peer-reviewed
  all-atom prediction benchmark spanning monomers, protein-protein,
  antibody-antigen, protein-ligand and protein-nucleic interfaces; the shared
  evaluation set behind the AF3 / Protenix / Boltz / ESMFold2 / OpenDDE comparisons.
  *Carries:* Table A's benchmark column, and therefore the Table A / Table B
  asymmetry — the benchmarking units' strongest finding and Beat 5's main
  empirical support exist only because prediction has a shared instrument and
  design has none.
  *Known limit:* Protenix-v1 shows its published aggregates do not enforce a
  common intersection of successfully-evaluated targets, so coverage differences
  alone can flip model rankings.
* **Overath binder meta-analysis** — `overath_meta` · `10.1101/2025.08.14.670059` ·
  **meat** — the design half's only cross-lab instrument, and the only one here
  measuring a *filter* rather than a prediction: 3,766 designs against 15 targets,
  pooled from six published studies and re-scored under one pipeline (the paper
  counts these per target, as 15 campaigns). AF3 `ipSAE_min` beats every other
  score, at 1.4× the average precision of the AF2 initial-guess iPAE RFdiffusion
  filters on.
  * **ipSAE** — `ipsae` · `10.1101/2025.02.10.637595` · **mention** — the metric
    that wins above, restricting the interface score to high-confidence residue
    pairs; its own paper benchmarks PPI prediction, not design.
  *Carries:* the metrics primer's payoff, and the sharper half of it. Precision runs
  0.1 to 1.0 across targets at the max-F1 threshold for the best score available,
  and Germinal (§6) reports the same failure from the other side, its nonbinders
  clearing the ipSAE threshold alongside its binders.
  *mBER (§6) measures the same thing at larger scale and points the other way;* the
  primer is where the two are reconciled.
  *Known limit:* previous-generation miniproteins, antibodies excluded — the
  generation before the one this review centres on. Leaves Table B's missing
  benchmark column as it is.

* **PXMeter** — `pxmeter` · `10.1101/2025.07.17.664878` · **meat** — open evaluation toolkit
  and artifact-filtered dataset; basis of the PXM benchmark family. v1.1.0 extends
  PoseBusters with sp2-planarity, amide-planarity and sp3-non-planarity checks.
  [GitHub](https://github.com/bytedance/PXMeter)
* **Gauss-Seidel projection** — `gauss_seidel_projection` ·
  `10.48550/arXiv.2510.08946` · **mention** (ICLR 2026) — a differentiable projection mapping
  provisional diffusion coordinates to the nearest physically valid
  configuration, exploiting constraint sparsity; integrates into existing
  predictors for end-to-end fine-tuning. Enforces validity as a *strict
  constraint* rather than a bias, which the paper argues inference-time steering
  (Boltz-1x) cannot guarantee. Two denoising steps suffice.
  *A fifth distinct response to the inherited physical-validity problem, alongside
  re-ranking, steering, learned chirality features (RFAA, then RF3) and fixing the
  metric (PXMeter).*
  *The corpus now measures two of these against each other:* RF3 (§2) reports 88%
  of ligand chiral centres correct without inference-time guidance against 84%
  (AF3) and 76% (Boltz-2), and argues steering *"may shift the network outside the
  training distribution"* — a direct answer to Boltz-1x, and the one place the
  steering-versus-learned-feature question is settled by numbers rather than
  asserted.

**The third caveat this part owns:** Boltz-2's benchmark numbers carry a
temporal-leakage caveat flagged independently by ESMC, Protenix-v1 and
Protenix-v2. With FoldBench's common-intersection problem and PoseBusters'
incompleteness, these are the three documented defects behind the intro's first
caveat — one per prediction instrument, which is the point. The Overath
meta-analysis carries a fourth, of a different kind: its own, stated in its own
discussion, and about the design half rather than the prediction half.

---

# Tables A and B — planned, not yet filled

Two tables close the review, gathering the numbers spread across §1–§9 so a
reader sees the whole field at once. **Numbers are deliberately not entered here**
— the map does not carry per-paper figures; they are gathered from the corpus when
the tables are written.

**The risk they carry.** Everything else in the benchmarking units argues these
numbers are *not* comparable, and a tidy side-by-side table reads as a
leaderboard — the exact misreading they exist to prevent. The tables therefore
make their own construction visible: **the provenance columns are not
decoration, they are the point**, and a cell without a stated benchmark, cutoff
and measurer has no entry.

## Table A — structure prediction accuracy

*Rows:* the predictors of §1, §3, §4, §7, §8 — AlphaFold2/3, AlphaFold-Multimer,
OpenDDE, OpenFold3, Boltz-1/2, Chai-1, Protenix-v1/v2, ESMFold/ESMFold2, plus the
RoseTTAFold pair from §2 as the historical baseline.
*Columns:* model · benchmark and version · training cutoff · target class ·
metric · **who measured it**.

*Target class is the axis that matters,* not a single aggregate — split at minimum
into monomer, protein-protein, **antibody-antigen**, protein-ligand,
protein-nucleic. Antibody-antigen carries the most weight: most systems in §3–§8
design antibodies or nanobodies, so that is the accuracy their critics actually
run on, and a model leading on monomers while trailing there is a weak critic for
this review's purposes. Only a split table shows it.

*The "who measured it" column earns its place* because the corpus contains genuine
third-party measurement — OpenDDE's antibody-antigen head-to-head, Protenix-v2's
baseline runs of OpenFold3 and others. Make self-reported and independently-run
numbers visually distinguishable: that distinction is Beat 5 arriving early.

## Table B — quality of generated binders

*Rows:* the design systems — RFdiffusion, RFantibody, RFpeptides, BoltzGen,
BoltzProt-1, PXDesign-d/h, Protenix-v2 design, Chai-2, the flow-matching five,
BindCraft, BoltzDesign1, Germinal, mBER, the ESMFold2 campaign, AlphaProteo,
Latent-X1/X2. *RFOptimization cannot be one:* in-silico success rates only, so no
designs-tested denominator and no hit definition. It sits beneath the table
instead — the corpus's first system to claim a design advance on refolding
statistics alone.
*Columns:* system · coupling level · target class and count · **designs tested per
target** · **hit definition** · assay · hit rate · affinity reached · targets
self-chosen?

**Sorted by designs-tested, not hit rate.** Beat 3's thesis is that the measure of
progress is how few designs you must make to get a binder, so the denominator is
the argument; sorting by hit rate silently converts the table into the leaderboard.

**The hit-definition column is mandatory, and is why this table is hard.**
BoltzProt-1 (§3) separates *screening hits* from *confirmed binders* and states
that screening hits are *"what prior binder design model literature typically
reports as binders"*. Its own percentages are confirmed-binder rates; most others
quoted in this map are on the looser definition. Without the column the table
compares two different events and calls it progress.

**The one documented exception.** Latent-X1 (§9)
designed macrocycles against RFpeptides' own targets and epitopes, re-synthesized
RFpeptides' published best binders, and measured them in its own assays alongside
its own designs — the corpus's only third-party wet-lab comparison of two design
methods. Two limits keep it honest: only the *binders* were re-measured, while the
hit rates it contrasts with are RFpeptides' own literature-reported ones, so that
half is not a matched-assay comparison; and it covers one pair of methods on one
modality. It runs in the awkward direction for Beat 5: the mechanism-withholding
system did the more disciplined experiment.

**What the pair says together, and why they stay adjacent.** Table A has a
benchmark column that can be filled — FoldBench, PXM and PoseBusters are shared
instruments run across models. Table B has none, because **there is no shared
benchmark for binder design at all**; every campaign chose its own targets, assays
and hit definition. The prediction half of this field is measured, the design half
self-reported, and two adjacent tables demonstrate that as no paragraph can. That
asymmetry is the benchmarking units' finding and Beat 5's strongest empirical
support.

---

# The conclusion

**Deliberately empty, and recorded so the gap is visible.** §9 is a coda and
Beat 5 sets up an ending, but what the review concludes follows from the units
above rather than preceding them, so it is settled once they exist. What it has
to land, all of it already argued above and none of it resolved: the open-
versus-closed question Beat 5 opens and §9 leaves standing; the two threads,
which are paid off in §8 and under Table B but not closed; and Beat 3's designs-
tested number, whose trajectory is the review's spine and has no shared
instrument to measure it against.

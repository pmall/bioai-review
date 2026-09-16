# Literature Map

> The living entry point of the review, ordered exactly as the final review will
> read, so there is no second organization to reconcile. The conventions it obeys
> — tiers, the map ↔ catalog invariant, *map-only*, what may and may not go inside
> an entry — are defined once in `AGENTS.md` and not restated here. What follows is
> specific to this review.
>
> **This file is the review minus its prose** — every publication and every claim
> the review makes, structured in reading order. Instructions addressed to whoever
> writes that prose live in `literature/writing-plan.md`, not here.
>
> **Claims here, evidence in the corpus.** The map states *what the review asserts*;
> `literature/corpus/` holds what proves it. "Changing only the filter roughly
> doubles the confirmed-binder rate" is a claim and belongs in an entry; the figure,
> the cutoff, the assay and the caveat that travels with them are read out of the
> parsed text at writing time. The consequence is the test the writing plan states:
> a section draft that could have been written from the map alone has failed.
> The failure in the other direction is an entry that records only a work's *role*
> — where it sits, what it is contrasted with — and never says what it claims.
>
> **Entry schema.** Every entry opens with name · bib key · DOI · tier, then one
> or two sentences of what the work is. Anything further uses this vocabulary and
> no other, so that a missing line is visible rather than merely absent:
>
> | Line | Holds | Required on |
> |---|---|---|
> | *Carries:* | the claim the tier rests on, named so the tier is checkable | **backbone**, **meat** |
> | *Against:* | what the work is contrasted with — the comparison the prose is built around | **backbone** |
> | *Caveat:* | the limit that travels with the claim wherever it is cited | where one exists |
> | *Collision:* | material this entry does **not** own, and where it is owned | where two units could both claim it |
> | *Level:* / *Attachment:* | the two coordinates of Beat 4's taxonomy | design systems only |
>
> A **mention** carries none of these: a mention is one sentence, and if it needs a
> *Carries* line it is not a mention.
>
> **One unit per draft.** After the layout block, the file is a flat sequence
> of the review's units in the order they render — the introduction, the metrics
> primer, the nine sections, the gaps unit, the instruments, the two tables, the
> conclusion. Each heading below is one draft unit in `literature/writing-plan.md`, so there is no
> second organization to reconcile there either. The layout block that opens the
> file is the only thing never drafted on its own: the section order, and the rule
> that lineages are not split by disclosure status.
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

# The layout

Two ordering decisions that belong to no single unit. Where either surfaces in the
prose is `writing-plan.md`'s business; what they say is here.

## Section order

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
| 3 | **Boltz** | Boltz-1, Boltz-2, BoltzGen, BoltzProt-1/BoltzPPI, BoltzDesign1 | diffusion, stated outright — and the lineage that opened, then closed |
| 4 | **Chai** | Chai-1, Chai-2 | Chai-1 is a diffusion co-folder; Chai-2's *generator* is undisclosed |
| 5 | **Flow matching** | FrameFlow, PPIFlow, OriginFlow, AtomFlow, D-Flow | the successor formalism — FrameFlow *"adapt[s] FrameDiff … to the flow-matching generative modeling paradigm"* |
| 6 | **Inversion as a portable technique** | BindCraft, BoltzDesign1, Germinal, mBER | Level 2 as a bare method — four groups, three predictors, one technique |
| 7 | **Protenix** | Protenix-v1, Protenix-v2, PXDesign-d and PXDesign-h | the first pipeline to *compose* both couplings into one platform |
| 8 | **ESM** | ESM-2/ESMFold, ESM-3, ESMC/ESMFold2 and its binder campaign | Level 2, fully integrated — the analytical climax |
| 9 | **The closed frontier** | AlphaProteo, Latent-X 1/2; IsoDDE, Chai-3, SeedFold | benchmarked but unexplainable — a coda, not a step in the argument |

## Non-disclosure

Chai-2 (§4), AlphaProteo (§9), Latent-X (§9) and IsoDDE (§9). Lineages are not
fragmented by disclosure status, so Chai-2 stays in §4 and Boltz's closed models
stay in §3, each with a pointer to §9.

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
between two molecules is itself a molecule, so small-molecule generators build
discrete machinery exactly where proteins need none (`drugflow`, `flowr` — both
excluded by modality, cited here for the contrast). Whether a gradient loop is reachable for small molecules at all is open, and
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

**And the one campaign that did not choose its targets.** Every number above comes
from a campaign whose targets and epitopes its own authors selected. mBER (§6) is the
exception — a million-scale VHH campaign against hundreds of human cell-surface
proteins, hotspots drawn at random — and its median per-design hit rate lands two
orders of magnitude below the headline numbers, at the same coupling level and on the
same predictor as Germinal. The spread *inside* that single campaign is the finding:
its best epitopes come back up into the range everyone else reports. **Target and
epitope selection alone move a hit rate across the full width of the literature's
spread**, which is what the introduction's second caveat rests on. Its hits are
phage-display enrichments — BoltzProt-1's *screening hits*, not confirmed binders.

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
2's anatomy decides it. AlphaFold2 is differentiable end to end, so a design loop can
backpropagate through the whole network. AF3-class models replaced the structure
module with diffusion and broke that — not because diffusion is undifferentiable, but
because unrolling a thousand denoising steps to get a gradient is impossible. The
corpus holds three answers to that one architectural fact, and they are the substance
of §6; the introduction's business is that the question exists and that Beat 2's
architecture is what raises it.

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
frontier closed: Boltz-1, Boltz-2 and BoltzGen stay MIT, while BoltzProt-1 ships
API-only with no weights. It is the one lineage where the review holds the before
*and* the after, both with papers.

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
twice and the results look opposed until the question is split. Overath (the
instruments) and Germinal both find confidence scores failing on individual designs —
nonbinders clearing the threshold alongside binders. mBER (§6) finds them working at
million-design scale, hit rates climbing with ipTM. Both hold: at population scale a
confidence score **enriches**; on any individual design it does not **discriminate**.
That is the primer's sharpest consequence, because **Beat 3's collapsing budget is
precisely the move out of the regime where enrichment suffices and into the one where
it does not.** A field testing twenty designs per target needs the property its
metrics have not been shown to have.

---

# §1 — AlphaFold, and the open co-folding cluster

Prediction only. The forward problem — sequence / chemical input → 3D structural
state — and the reference every later section is defined against.

*Why it opens:* AlphaFold is the elephant in the room — everything later
reproduces it, reacts to it, or replaces its evolutionary input, so the review
cannot begin anywhere else without the reader waiting for it. **OpenFold3 and
OpenDDE join it here** rather than getting their own sections: open co-folding
models in the AF3 mould with no design descendant to follow.

* **AlphaFold2** — `alphafold2` · `10.1038/s41586-021-03819-2` · **backbone** —
  single-chain predictor at experimental accuracy, and the model that cashed the
  MSA-as-coevolution bet.
  *Carries:* three facts the review is built on. Beat 2's **Stage-1 anatomy** —
  trunk, distogram, coevolution wager — is AF2's design, and every co-folder in §3,
  §4, §7 and §9 is a variation on it. Beat 2's **single regression pass** is the
  structure stage everything after it replaced. And because the whole network is
  differentiable, it is the **only predictor a design loop can invert without
  choosing an attachment point** — the fact §6 is built on and the reason BindCraft
  exists. It is also the standard post-hoc filter across §2–§5 and §7: the review's
  first model and its most-used critic.
  *Against:* the CASP14 field it displaced — which is why the coevolution bet is
  treated as settled rather than argued, and why every later contrast in the review
  is drawn with AF2 rather than with anything before it.
  *Caveat:* it is weakest run single-sequence, which its own paper documents — the
  regime §6 then operates it in.
  *Collision:* Beat 2 owns the CASP14 margin and the statement of the bet; this
  entry owns the three consequences above.
* **AlphaFold-Multimer** — `alphafold_multimer` · `10.1101/2021.10.04.463034` · **backbone** —
  AF2 retrained on complexes, and the complex predictor the review actually runs on:
  §6 does not invert AlphaFold2, it inverts this. Kept despite the pre-2025 rule
  under the active-lineage exception.
  *Carries:* **ipTM**, the unit half the review's numbers are denominated in —
  load-bearing for §2–§7 and for both benchmarking units, not only §6. Every "the
  field's standard filter" claim resolves to a metric this paper defined.
  *Against:* AF2 itself. It is the evidence that complex prediction needed its own
  training rather than following from single-chain accuracy — which is what makes
  the binder problem a distinct problem and not a corollary of folding.
  *Caveat:* never peer-reviewed. The field's most-used complex predictor has no
  journal version — a disclosure gap of a different kind from §9's.
* **AlphaFold3** — `alphafold3` · `10.1038/s41586-024-07487-w` · **backbone** — the
  generalization from single chains to arbitrary complexes of proteins, nucleic
  acids, ligands and ions, and the architecture the open lineages reproduce.
  *Carries:* the review's second structural fact — replacing AF2's structure module
  with **diffusion** broke end-to-end differentiability, and the three answers to
  that one decision (attach to the trunk, attach to the confidence heads, shorten
  the trajectory) are what §2, §6 and §7 disagree about. It also carries the
  openness thread's opening: closed weights are the stated motivating gap behind
  Boltz-1, Protenix and OpenFold3, so §3 and §7 exist as answers to this paper.
  *Against:* AF2, on both counts — more modalities, at the cost of the property
  §6 depends on. The review's central trade, stated by the same lab in two papers.
  *Caveat:* its physical-validity behaviour is the problem the instruments' four
  responses answer, and "PB-valid" enters the literature here.
* **OpenDDE** — `opendde` · `10.48550/arXiv.2607.03787` · **meat** — Apache-2.0
  all-atom co-folding model with no design descendant.
  *Carries:* what it *measured*, not what it is. It runs the corpus's most complete
  third-party antibody-antigen head-to-head, which Table A's "who measured it"
  column rests on, and its scaling curve is the only public evidence about IsoDDE (§9).
  *Caveat:* explicitly *"not a complete drug-discovery system"* — design is roadmap
  only, so it belongs to the prediction half throughout.
  [GitHub](https://github.com/aurekaresearch/OpenDDE)
* **OpenFold → OpenFold3** — AlQuraishi Lab's open reimplementations: OpenFold
  reproduces AlphaFold2 and supplies the distillation set Boltz-1 trains on,
  OpenFold3-preview targets bitwise AF3 reproduction.
  *(map-only — code releases, no paper or DOI.)* · **mention**
  [GitHub](https://github.com/aqlaboratory/openfold-3)

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

**AtomWorks** — the IPD's data framework — is what RF3 and RFdiffusion3 are both
built on, and that is its whole role here: one line, never a passage.

**With RFOptimization, this lineage covers every stage of the problem** —
predict, generate, inverse-fold, optimize, filter — and it is the only one that
does. It is not a platform in §7's sense: RFO is a refinement stage rather than a
second generation arm, and it is deliberately assembled from three lineages
(RF3 + Boltz + AF3) rather than one, so §7 keeps the
*first-to-compose-both-couplings* claim on dates and on kind.

* **RoseTTAFold (RF1)** — `rosettafold` · `10.1126/science.abj8754` · **backbone** —
  three-track (1D/2D/3D) network developed independently of AF2; complex prediction
  emerged untrained from two-segment cropping.
  *Carries:* §2's organizing fact — the one architecture in the review not derived
  from AlphaFold, which is what makes this lineage a second origin rather than a
  fork. It is also the network RFdiffusion is fine-tuned from, so Beat 3's identity
  claim has its historical proof here.
  *Against:* AF2, contemporaneously and on the same problem — the comparison that
  establishes there were two independent routes to the same result, and the reason
  the review has two lineage origins to place rather than one.
  *Caveat:* as a *predictor* it has left the conversation; nothing published since
  2024 benchmarks against it. Its standing in the review is as an ancestor.
  *Intermediate steps, map-only:* RoseTTAFoldNA and RoseTTAFold2 (preprints; RF2 is
  RFAA's base network, and the network RFpeptides adds cyclic encoding to). · **mention**
* **RoseTTAFold All-Atom (RFAA)** — `rosettafold_all_atom` ·
  `10.1126/science.adl2528` · **mention** — all-atom generalization published two
  months *before* AF3 and independently of it: the date that makes the two origins
  a fact rather than a framing.
* **RoseTTAFold3 (RF3)** — `rosettafold3` · `10.1101/2025.08.14.670328` · **meat**
  — the lineage's current all-atom predictor, AF3-class with a diffusion structure
  stage, BSD with weights, benchmarked directly against AF3, Boltz-2 and Chai-1.
  *Carries:* the evidence for the section-defining fact — this lineage never stopped
  shipping predictors — and it is the model RFOptimization takes its gradients from,
  so the corpus's only discrete Level-2 system runs on something the review can cite.
  *Collision:* its chirality result belongs to the physical-validity thread and is
  stated once with the instruments, not here.
* **RFdiffusion** — `rfdiffusion` · `10.1038/s41586-023-06415-8` · **backbone** *(inherits RF1)*
  — the generative turn itself, and the most-cited design model in the corpus.
  SE(3)-equivariant frame diffusion, fine-tuned from a predictor, filtered by AF2 pAE.
  *Carries:* three beats. **Beat 3's identity claim** in its cleanest historical
  form — a predictor fine-tuned into a generator, with nothing else changed.
  **Beat 4's Level 1**, the pipeline this paper established (backbone, then
  ProteinMPNN, then AF2 judges) which every section from §3 to §7 either runs or
  argues with. And **step 2 of §6's arc**: its verdict on hallucination, which sent
  Level 2 quiet for two years.
  *Against:* hallucination through RoseTTAFold — the Baker lab's own predecessor,
  beaten on the Baker lab's own benchmark. That is the comparison §6 later reopens,
  and it is why §6 can be written as a return rather than an arrival.
  *Caveat:* its "in silico success" criterion is a confidence-metric filter, so the
  designs-tested numbers attached to it are subject to the metrics primer's
  discrimination problem.
  [GitHub](https://github.com/RosettaCommons/RFdiffusion)
* **RFdiffusion2** — `rfdiffusion2` · `10.1038/s41592-025-02975-x` · **mention** *(inherits RF1)*
  — atom-level enzyme active-site scaffolding from functional-group positions,
  sequence-agnostic.
* **RFdiffusion3** — `rfdiffusion3` · `10.1101/2025.09.18.676967` · **meat** —
  transformer-based all-atom diffusion, adopting AF3's non-equivariant approach.
  *Carries:* the lineage's own break with Level 0 — unlike RFdiffusion 1/2 it is not
  fine-tuned from a predictor but trained from scratch, so the identity Beat 3 rests
  on is weakest in the lineage that established it.
  *Collision:* AtomWorks is named once above; this entry does not re-explain it.
* **RFantibody** — `rfantibody` · `10.1038/s41586-025-09721-5` · **backbone** *(inherits RFdiffusion)*
  — the lineage's antibody arm: a fine-tuned RFdiffusion designing VHHs, scFvs and
  full antibodies against chosen epitopes.
  *Carries:* the concession that **the screen remains**. It pairs design with
  yeast-display library screening and says so, which makes it the honest baseline
  Beat 3's collapsing-budget table is measured against — and the paper §3, §4 and §6
  cite when claiming they no longer need library selection.
  *Against:* immunization and random library screening, which it states cannot be
  aimed at a chosen epitope. That framing is what the whole design half inherits.
  *Collision:* Beat 3 quotes its statement of the epitope gap; this entry owns the
  concession, not the gap.
* **RFpeptides** — `rfpeptides` · `10.1038/s41589-025-01929-w` · **backbone** *(inherits RFdiffusion)*
  — the lineage's macrocycle arm: RFdiffusion and RF2 extended with a **cyclic
  relative positional encoding** so the generated chain closes head-to-tail;
  sequences from ProteinMPNN, filtered by refolding with AfCycDesign and by Rosetta
  interface metrics. *Level 1.*
  *Carries:* the low end of Beat 3's budget — binders against every target from
  fewer than twenty synthesized designs each, with crystal structures — and the
  cyclic thread's **open** method.
  *Against:* Latent-X1 (§9), which designed against these targets and epitopes and
  re-synthesized these binders to measure in its own assays. The corpus's only
  third-party wet-lab comparison of two design methods runs through this entry.
  *Collision:* that head-to-head is argued under Table B, where its limits belong.
  * **AfCycDesign** — `afcycdesign` · `10.1038/s41467-025-59940-7` · **mention** —
    AlphaFold2 given a cyclic offset so the chain reads as closed; the critic above,
    and where the cyclic thread starts.
* **RFOptimization (RFO)** — `rfoptimization` · `10.64898/2026.09.04.749184` · **meat** —
  training-free refinement of existing designs. *Level 2; reviewed in §6.* Listed
  here because it completes this lineage's stack — predict, generate, inverse-fold,
  optimize, filter, all from one group.
* **ProteinMPNN** — `proteinmpnn` · `10.1126/science.add2187` · **backbone** —
  autoregressive message-passing network that writes a sequence for a fixed
  backbone. **The review's one piece of universally shared machinery**: §2–§7 all
  run it, across nine labs and both coupling levels.
  *Carries:* the middle stage of Beat 4's Level 1. A diffusion model generates
  geometry, not sequence — two separate problems — and this paper is why the second
  one stopped being the bottleneck. Every "generate, then filter" pipeline in the
  review has this step in it, usually unremarked, and §6 exists precisely because
  Level 2 removes it.
  *Against:* AlphaDesign (§6), which substitutes a diffusion model of its own and
  benchmarks it as comparable — the corpus's one alternative, and the evidence that
  the field's dependence is adoption rather than necessity.
  *Caveat:* its own paper notes that sequence recovery, the metric it is scored on,
  may not track whether the sequence folds.
  [GitHub](https://github.com/dauparas/ProteinMPNN)
  * **LigandMPNN** — `ligandmpnn` · `10.1038/s41592-025-02626-1` · **meat** — the
    same network conditioned on ligand and nucleic-acid context.
    *Carries:* the all-atom extension of the inverse-folding stage — the variant
    RFOptimization's cycling move runs alongside ProteinMPNN.

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
remain MIT with weights released; **BoltzProt-1 is API-only and commercial**, yet
still publishes a paper and wet-lab numbers. That is what makes this lineage a better
§9 exhibit than IsoDDE — the review holds the before and the after with publications
on both sides, where IsoDDE has only an after. *(BoltzMol-1, the lineage's other
closed model, is excluded by modality and logged in `candidates.md`; the fork is
established by BoltzProt-1 alone and does not need it.)*

* **Boltz-1** — `boltz1` · `10.1101/2024.11.19.624167` · **backbone** — the first
  fully open (MIT) AF3-class co-folder, and the paper that made AF3's architecture
  something the rest of the field could build on.
  *Carries:* the openness thread's opening. §6's BoltzDesign1, §3's own BoltzGen and
  a good part of the design literature exist because these weights were
  downloadable — and the thread it opens is the one Beat 5 closes on this same
  lineage. **Boltz-1x** adds Feynman-Kac inference-time steering, the corpus's first
  answer to the physical-validity problem.
  *Against:* AlphaFold3, which it reproduces and releases. The comparison is not
  about accuracy; it is about what a downloadable model makes possible downstream,
  and §3, §6 and §7 are the evidence.
  *Collision:* the steering-versus-learned-features argument is settled once with
  the instruments, not here.
  [GitHub](https://github.com/jwohlwend/boltz)
* **Boltz-2** — `boltz2` · `10.1101/2025.06.14.659707` · **meat** — adds a
  binding-affinity module and the corpus's most complete conditioning system; the
  refolding oracle BoltzGen and BoltzProt-1 filter with, which is its role here.
  *Carries:* the corpus's only affinity prediction — and its scope. The module is
  protein-ligand, and its own paper states it does not handle multimeric binding
  partners, which is why the gaps unit can say no system here predicts
  protein-protein affinity.
  *Caveat:* its benchmark numbers carry a temporal-leakage caveat flagged
  independently by ESMC, Protenix-v1 and Protenix-v2 — stated with the instruments.
* **BoltzGen** — `boltzgen` · `10.1101/2025.11.20.689494` · **backbone** *(inherits Boltz)* —
  unified generative design across proteins, peptides, nanobodies, antibodies and
  small molecules, filtered by refolding with Boltz-2. *Level 1,
  confidence-as-critic.*
  *Carries:* Beat 3's identity claim in its published form. RFdiffusion demonstrated
  it historically by fine-tuning; BoltzGen states it as a design principle — *"a
  single all-atom diffusion model capable of performing both structure prediction
  and protein design"* — and is the cleanest Level 0 in the corpus.
  *Against:* BoltzProt-1 below, which beats it by changing only the critic. The two
  are the same generator, which is what makes the comparison worth the section.
* **BoltzProt-1** — `boltzprot1` · `10.64898/2026.06.23.733997` · **backbone** *(inherits BoltzGen)*
  — a refined BoltzGen ranked by **BoltzPPI**, a critic trained to answer "will this
  bind" rather than a confidence head reused as one. *Level 1, trained-critic
  regime.*
  *Carries:* two beats at once. It is the **trained-critic** half of Beat 4 —
  changing only the filter roughly doubles the confirmed-binder rate with the
  generator untouched, the corpus's cleanest evidence that hit rate lives in the
  critic. And it is the first departure from the metrics primer's family 2, a critic
  trained against experimental outcomes rather than a confidence head reused as one.
  It also splits *screening hits* from *confirmed binders*, the definition problem
  Beat 3 and Table B inherit.
  *Against:* BoltzGen, its own unmodified generator — the only controlled comparison
  of a filter in the corpus, and the reason the claim is not confounded.
  *Caveat:* API-only, no weights — the closed half of the fork above, so the result
  cannot be independently reproduced.
  *(BoltzPPI is the critic itself, no separate publication — resolves to the
  `boltzppi` keyword on this entry.)*
* **BoltzDesign1** — `boltzdesign1` · `10.1101/2025.04.06.647261` · **meat** — inverts
  the Boltz predictor for binder design. *Level 2; reviewed in full in §6*, where
  the portability argument needs it next to BindCraft.

# §4 — Chai

Diffusion co-folding, then the strongest antibody-design result in the corpus
from a generator whose mechanism is never stated.

* **Chai-1** — `chai1` · `10.1101/2024.10.10.615955` · **meat** — AF3-derivative
  carrying **both** of Beat 2's Stage-1 inputs: an MSA track and a protein-LM track,
  either usable alone. Also adds experimentally-grounded constraint features
  (pocket, contact, docking).
  *Carries:* the qualifier Beat 2 needs — the MSA/PLM divide is a switch here, not a
  commitment, which is why the review can say the divide is not a wall. The hinge §8
  completes by removing the MSA entirely.
  [GitHub](https://github.com/chaidiscovery/chai-lab)
* **Chai-2** — `chai2` · `10.1101/2025.07.05.663018` · **backbone** *(inherits Chai-1, via a
  "Chai-1d" design prototype)* — zero-shot antibody design at roughly one hit in six,
  on twenty or fewer designs per target, across dozens of targets.
  *Carries:* the low end of Beat 3's collapsing budget, and the characterisation the
  table's top row quotes — that prior work needed *"thousands to millions of designs
  to reliably identify hits"*. It is the result the field measures antibody design
  against.
  *Against:* library screening, explicitly and by the number. The paper's framing —
  zero-shot, no affinity maturation, small plate assays — is the sharpest statement
  in the corpus that the screen has been removed, and it is exactly the claim
  RFantibody (§2) declines to make.
  *Caveat, and the section's finding:* the paper describes only the *folding*
  submodule (Chai-2f, *"a similar architecture as Chai-1"*). **The generative
  mechanism is never stated.** The strongest antibody result in the corpus is the
  one the review can say least about — §9's argument arriving early, inside a
  lineage rather than in the coda.
* **Chai-3 (2026)** — high-throughput commercial 3D foundation model.
  *(map-only — no publication; discussed in §9.)* · **mention**
  [platform](https://lab.chaidiscovery.com/)

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

* **FrameFlow** — `frameflow` · `10.48550/arXiv.2310.05297` · **backbone** — recasts
  FrameDiff as SE(3) flow matching; the methodological ancestor of the rest of this
  section.
  *Carries:* the section's whole argument, and Beat 4's step-count premise. It is the
  paper that puts diffusion's cost on the record — *"∼1000 model forward passes"* —
  and reports the ODE formulation buying better designability at a fraction of the
  steps. Beat 4 then draws the consequence: a trajectory short enough to cross is a
  trajectory a design gradient can cross.
  *Against:* FrameDiff, which it is a reformulation of — the same model, the same
  problem, one formalism swapped. That is why §5 can open by re-deriving something
  familiar instead of introducing a parallel formalism cold.
  *Caveat:* its numbers are unconditional monomer designability, not
  target-conditioned binder design, so the step-count claim transfers to §7 but the
  quality claim does not.
* **PPIFlow** — `ppiflow` · `10.64898/2026.01.19.700484` · **mention** — SE(3) flow
  matching with in-silico maturation, for binders and single-domain antibodies.
* **OriginFlow** — `originflow` · `10.1101/2025.04.29.651154` · **mention** — combines
  an SDE with flow matching. *Its self-reported hit rate is among the corpus's
  highest and belongs in Table B, not in the prose.*
* **AtomFlow** — `atomflow` · `10.48550/arXiv.2409.12080` · **mention** — atomic flow
  matching over unified biotokens, for ligand-binding pockets.
* **D-Flow** — `dflow` · `10.1109/JBHI.2026.3683934` · **mention** — full-atom flow
  matching for D-peptide binders; borderline on modality, kept by the scope rule.

**This is not a lineage.** Only FrameFlow has traction; the other four are cited by
nothing else in the corpus, and `xrefs.md` shows them pointing at §2 rather than at
each other — five independent responses to one problem, not a succession.

**It is a section nonetheless, and that is settled.** §1–§5 are ordered by generative
formalism — diffusion, then its successor, then the models that do not say — so
folding flow matching into §2–§4 would remove the middle term of the review's own
ordering axis and leave §4's "does not say" with nothing to sit after. A reader of
this field also arrives expecting the formalism covered. It is therefore the review's
**shortest** section: one argument, one paper analysed, four named in support.

**The section's claim.** Flow matching's ODE formulation shortens the structure
stage enough for PXDesign-h (§7) to backpropagate through a whole AF3-class model,
which BoltzDesign1 could not do through diffusion. The formalism shift matters here
because it **reopened the network to a design gradient** — not because it made
sampling cheaper. The other four papers are the evidence that the move was general
rather than one group's preference.

# §6 — Inversion as a portable technique

**Level 2, isolated.** Gradients flow through a structure predictor into the
design variable. Not a lineage — a *method*, shown here to be portable across
predictor families and research groups, met as a bare part before §7 builds it
into a product and §8 dissolves it into a single model.

*Why it comes before §7 and §8:* a pipeline is a composition of techniques and the
reader should meet the part before the assembly. §8 is the limit case with nothing
left to compose, which is why it ends the argument rather than §9.

**The section owns two things, and they are orthogonal.** Every Level-2 system
differs from every other on exactly two coordinates, which is why the entries below
all carry both and why no other section needs them:

1. **The design variable** — a relaxed *L*×20 simplex annealed to one-hot
   (*continuous*: BindCraft, BoltzDesign1, Germinal, mBER, PXDesign-h, ESMFold2),
   against a sequence that stays one-hot while the gradient only proposes and ranks
   mutations (*discrete*: RFOptimization alone).
2. **The attachment point** — where in the predictor the gradient is taken. Beat 4
   states why the question exists; here is the answer, and it is the clearest case in
   the review of the field arguing with itself about a mechanism.
   - **Attach to the trunk.** BoltzDesign1 stop-gradients the diffusion module and
     optimizes the Pairformer's distogram directly, because it *"represents the
     probability distribution of atomic distances that the diffusion model later
     samples from"* — optimize the distribution, not a sampled structure.
   - **Attach to the trunk and the confidence heads.** RFOptimization applies the same
     stop-gradient and adds iPAE, pLDDT and iPTM, because the confidence path back to
     the input stays differentiable when the coordinate path does not.
   - **Shorten the trajectory until it can be crossed.** Protenix's two-step ODE
     sampler is short enough to traverse, so PXDesign-h (§7) backpropagates through
     the whole model, which it says permits *"end-to-end backpropagation of gradients
     from all confidence metrics, rather than being limited to contact loss derived
     from Pairformer outputs"* — naming BoltzDesign1 as the limitation it beats.
   - **Or never face the question.** AlphaFold2 has no diffusion stage, so BindCraft,
     Germinal and mBER take the whole network and never choose.

**The two coordinates are independent, and that is the section's analytical payoff.**
BoltzDesign1 and RFOptimization attach in the same place and differ in the design
variable; BindCraft and PXDesign-h share the design variable and differ in the
attachment point. Any system in the review can be located on both axes, which is what
makes §6 a category rather than a list — and PXDesign benchmarking itself against
exactly BindCraft and BoltzDesign1 (§7) is the field agreeing that it is one.

*This is also what §5's formalism shift bought beyond sampling speed:* flow matching
is what made the structure stage short enough to reopen to a design gradient.

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
   predictor families across six groups.
   *The claim has to be stated carefully, and this is the only place it is stated.*
   On the AlphaFold family the portability is one codebase being retargeted —
   BindCraft, Germinal and mBER all run ColabDesign — so those three add *groups*,
   not architectures. What the claim about **architectures** actually rests on is
   the three systems that left that codebase: BoltzDesign1 here, PXDesign-h (§7)
   and the ESMFold2 campaign (§8).
5. *Conceded.* RFOptimization closes the arc: the Baker lab returns to the
   technique it abandoned in step 2, on its own AF3-class predictor, and reports
   beating BindCraft on cost per filter-passing design.

* **AlphaDesign** — `alphadesign` · `10.1038/s44320-025-00119-z` · **mention** —
  hallucination through AlphaFold2 searched by an evolutionary algorithm, not a
  gradient, so Level 1 rather than part of this roster. The date step 2 is qualified
  against: an independent group that never abandoned the technique.
* **ColabDesign** — `colabdesign` · `10.5281/zenodo.13309080` · **mention** — the
  framework for running AlphaFold backwards, and the shared substrate under
  BindCraft, Germinal, mBER and AfCycDesign (§2). Named because step 4's claim
  depends on knowing it is there. *(No paper; a versioned software release.)*
* **BindCraft** — `bindcraft` · `10.1038/s41586-025-09429-6` · **backbone** —
  backpropagates through AF2-multimer weights to produce an *L*×20 error gradient
  over amino-acid choices, annealed in four stages from continuous logits to
  one-hot. Target flexibility retained; no separate scaffolding step.
  *Level:* 2, continuous. *Attachment:* the whole network.
  *Carries:* Beat 1's differentiability asymmetry, of which the *L*×20 gradient is
  the worked example, and Beat 4's off-distribution claim. It is the canonical
  Level-2 system the other four in this section are read against, and the one
  PXDesign-h (§7) benchmarks itself on.
  *Against:* Level-1 generate-and-filter, which it replaces outright — no backbone
  generator, no inverse-folding stage, no separate critic. That is the clearest
  statement in the corpus of what Level 2 removes.
  *Caveat:* it runs AF2 single-sequence on the designed chain, off-distribution for
  that model, which the annealing and 5-model ensembling appear to compensate for.
  Its own paper adds a second: the ipTM it ranks on predicts *whether* a design
  binds but does not track *how tightly* — the filters-predict-binding-not-affinity
  gap the gaps unit states.
* **BoltzDesign1** — `boltzdesign1` · `10.1101/2025.04.06.647261` · **meat** — the same
  inversion moved from AlphaFold2 to the Boltz all-atom predictor (§3).
  *Level:* 2, continuous. *Attachment:* the trunk.
  *Carries:* the first answer to the AF3-class wall — the first system in the corpus
  to hit it and retreat to the trunk, which is why the other two answers above are
  framed as replies to this one.
  *Caveat:* it shares senior authors with BindCraft, so the two are one research
  programme porting one method, not two independent data points. The independence of
  the technique rests on Germinal, mBER, PXDesign-h and ESMFold2.
* **Germinal** — `germinal` · `10.1038/s41587-026-03187-0` · **backbone** —
  gradient-based hallucination through AlphaFold-Multimer for epitope-targeted
  antibody CDRs. *Essentially BindCraft for antibodies*, and the paper's own framing.
  *Level:* 2, continuous. *Attachment:* the whole network.
  *Carries:* §6's portability claim at the level of *groups* — the group is
  independent of BindCraft's, which both papers state. And the section's one
  mechanical novelty: it is the only Level-2 system putting a **sequence prior inside
  the loss**, merging the predictor's gradient with an antibody language model's,
  where §8 reaches the same place with one model rather than two.
  *Against:* BindCraft, which it adapts, and §8, which dissolves the two-model
  arrangement it needs. Germinal is the strongest form of the composed answer, and
  §8 is why the review does not end on it.
  *Caveat:* two, both its own. Its nonbinders clear the ipSAE threshold alongside its
  binders — the discrimination failure the metrics primer reconciles. And it states
  that how far design success depends on the quality of the antigen model remains an
  open question, which is the gaps unit's structure-availability entry.
  *(mBER below also carries a PLM prior, but as a fixed logit bias rather than a live
  gradient — a distinction worth a clause, not a passage.)*
  * **OpenGerminal** — `opengerminal` · `10.64898/2026.06.25.734527` · **mention** —
    Apache-2.0 reimplementation on an open stack.
* **mBER** — `mber` · `10.1101/2025.09.26.678877` · **meat** — Manifold Bio's
  open-source VHH designer: the same technique and predictor as BindCraft, so it adds
  a group rather than an architecture.
  *Level:* 2, continuous. *Attachment:* the whole network.
  *Carries:* scale, not method. At million-design scale against hundreds of targets
  with hotspots drawn at random, it is the corpus's only campaign that did not choose
  its own targets — the control for every hit rate in Table B, and the evidence behind
  the introduction's second caveat. It also carries the enrichment half of the metrics
  primer's reconciliation. *Method note, one clause:* it answers the off-distribution
  problem with structural templates where BindCraft uses annealing, and gets confident
  docked folds from AlphaFold-Multimer with no MSA at all.
  *Collision:* Beat 3 owns the unchosen-targets argument; this entry does not restate it.
  *Caveat:* its hits are phage-display enrichments — BoltzProt-1's *screening hits*,
  not confirmed binders, with no affinity quantification.
* **RFOptimization** — `rfoptimization` · `10.64898/2026.09.04.749184` · **meat** —
  gradient-guided mutation through RF3, refining existing designs rather than
  generating them. *Home section §2.*
  *Level:* 2, **discrete** — the only instance in the corpus. The sequence stays
  one-hot and the gradient only proposes and ranks mutations, on the stated grounds
  that a continuous relaxation is an attack surface the optimizer will exploit.
  *Attachment:* trunk plus confidence heads — the same place as BoltzDesign1, so the
  two isolate the design variable cleanly.
  *Carries:* the header's second Level-2 regime, and the close of §6's arc — the
  Baker lab returning to what it abandoned in step 2. Its cross-lineage construction
  (gradients from RF3, cycling through Boltz, AF3 held out as an independent check)
  treats agreement with a single predictor as the failure mode, and is the only
  system moving that response into the optimizer rather than the filter.
  *Caveat:* **in silico only.** No wet-lab validation, no designs-tested denominator,
  no Table B row. That is the ceiling on how far the review leans on it.

# §7 — Protenix

The first full assembly. One lineage ships the predictor, a Level-1 diffusion arm
and a Level-2 hallucination arm as a single platform — the couplings of §1–6 stop
being alternatives and become two modes of one product, chosen per target. It is
also where §6's technique gets benchmarked from the outside.

* **Protenix-v1** — `protenix_v1` · `10.64898/2026.02.05.703733` · **meat** — ByteDance
  Seed's open all-atom model matching AF3 under matched cutoff, scale and inference
  budget — the second answer to AF3's closed weights, after Boltz-1.
  *Carries:* the common-intersection critique of FoldBench, stated with the
  instruments; and the matched-conditions framing that makes "matches AF3" a
  checkable claim rather than a leaderboard position.
  [GitHub](https://github.com/bytedance/Protenix)
* **Protenix-v2** — `protenix_v2` · `10.64898/2026.04.10.717613` · **meat** — both halves
  in one paper, which is why the lineage reads as a platform rather than a model.
  *Prediction:* antibody-antigen gains over v1, plus the finding that the PoseBusters
  criterion is itself incomplete (the instruments). *Design:* target-conditioned
  generation across miniproteins, VHH and Fv, with epitope-specific and site-agnostic
  modes. *Level:* 1 *(inherits Protenix)*.
* **PXDesign** — `pxdesign` · `10.1101/2025.08.15.670450` · **backbone** — the section's
  reason for existing: the first system to ship **both couplings as two modes of one
  product**, chosen per target rather than argued over.
  * **PXDesign-d** — diffusion arm. *Level:* 1 *(inherits Protenix)*.
  * **PXDesign-h** — hallucination arm. *Level:* 2, continuous. *Attachment:*
    end-to-end through the two-step flow — the third answer, argued in §6.
  *Carries:* the composition claim — everything §1–§6 presented as competing answers
  appears here as configuration — and the **filter-ensembling finding**: Protenix and
  AF2-IG filters retain *different* true positives with limited overlap, the other
  half of Beat 4's critic-quality argument alongside BoltzPPI.
  *Against:* BindCraft and BoltzDesign1, benchmarked head-to-head. That is the
  evidence §6 is a real category rather than the review's own grouping, and it is the
  corpus's clearest instance of the field arguing about where a Level-2 gradient
  should attach.
  *Caveat:* the head-to-head is run by the system being promoted, so it belongs in
  Table B's self-reported column like every other in-house comparison.

# §8 — ESM

**The analytical climax, and the section that closes the review's longest thread.**
Two things land here at once: the MSA/PLM divide opened in Beat 2 and followed
since §1 resolves in favour of the language model, and the coupling axis reaches
its limit case — language model, folding head and design loop are one system, with
nothing left to compose.

*Why it comes last in the argument:* §6 met Level 2 as a portable technique, §7 as
one mode of a platform. Here it is not a technique applied to a predictor at all.
The escalation has nowhere further to go, which is why §9 is a coda rather than a
tenth step.

* **ESM-2 & ESMFold** — `esm2` · `10.1126/science.ade2574` · **backbone** — the
  founding single-sequence predictor: structure emerges from masked-LM scaling alone,
  with no MSA and no templates at inference. Enabled the ESM Metagenomic Atlas (a
  database, out of scope).
  *Carries:* the other half of Beat 2's Stage-1 divide. AlphaFold2 established that
  evolutionary depth is *retrieved* at inference; this paper established that it can
  live in the weights instead — and Beat 4's precondition for Level 2 depends on that
  alternative existing.
  *Against:* AlphaFold2 with an MSA, which it did not match. That is the point: the
  trade was accuracy for independence, and §8 exists because ESMC later closed the
  gap rather than because this paper won.
  *Caveat:* the gap it traded away is real and was the standing objection to
  single-sequence prediction for three years; the review should state it rather than
  read the lineage backwards from its conclusion.
* **ESM-3** — `esm3` · `10.1126/science.ads0018` · **mention** — multimodal promptable
  PLM over sequence, structure and function. A lineage step.
* **ESMC & ESMFold2** — `esmc` · `10.64898/2026.06.03.729735` · **backbone** — Biohub /
  EvolutionaryScale's ~2.8B-sequence LM plus a folding head on its frozen
  representations. *Covers ESMFold2 and ESMFold2-Fast — modules of this release, no
  separate paper.*
  *Carries:* the resolution of Beat 2's divide — single-sequence antibody-antigen
  accuracy **exceeding AF3-with-MSA**, with the MSA encoder detachable and kept only
  as a rescue path for high-perplexity sequences. The retrieval step is no longer the
  price of accuracy, which is what licenses the campaign below.
  *Against:* AF3 with an MSA, on antibody-antigen — the target class §3–§8 actually
  design for, which is why the comparison settles the thread rather than scoring a
  point.
  *Caveat:* it flags the temporal-leakage problem in Boltz-2's numbers, so its own
  comparisons should be read under the instruments' first caveat like everyone's.
  * **ESMFold2 binder design campaign** — **backbone**. *Level:* 2, continuous.
    *Attachment:* the language model **and** the folding head — the tightest coupling
    in the corpus, with nothing left to compose.
    *Carries:* the claim that the penalty is gone. Every §6 system inverts a
    predictor outside the regime it was trained in; BindCraft runs AF2
    single-sequence and compensates with annealing and ensembling. Single-sequence
    **is** ESMFold2's native regime, so the off-distribution problem Beat 4 opens
    does not arise. MSA emancipation was never an accuracy story — it set the ceiling
    on coupling, and this is the ceiling.
    *Against:* §6's composed systems, and Germinal in particular: the same sequence
    prior, reached with one model instead of two.
    *Caveat:* self-chosen targets and a self-reported hit rate, the corpus's highest
    outside §9. Table B's provenance columns apply here as everywhere.
    *(module of the ESMC release — no separate publication.)*

# §9 — The closed frontier

A coda, not a step in the argument. Systems that publish benchmarks and withhold
mechanisms — placed last because they cannot be analysed the way §1–8 analyse
everything else. **Two tiers, and they are not the same problem.**

**Tier 1 — published, results disclosed, mechanism withheld.**

* **AlphaProteo** — `alphaproteo` · `10.48550/arXiv.2409.08022` · **meat** — DeepMind
  generative engine plus a multi-stage filter for picomolar/nanomolar binders.
  Describes its generator only as *"a generative model trained on structure and
  sequence data from the PDB and a distillation set of AlphaFold predictions"*.
  *Carries:* the canonical statement of the Level-1 success criterion — *"interchain
  AF2 pAE < 10, binder-aligned binder RMSD < 1 Å, pLDDT > 80"* — quoted in Beat 4,
  and the first place a reader meets those units.
  *Caveat:* the criterion is the field's rather than this paper's; what is proprietary
  is the generator, and the filter it publishes is the part everyone already ran.
* **Latent-X1** — `latentx1` · `10.48550/arXiv.2507.19375` · **backbone** · and
  **Latent-X2** — `latentx2` · `10.48550/arXiv.2512.20263` · **meat** — Latent Labs'
  atom-level binder design platform: macrocycles and minibinders (X1), then
  drug-like low-immunogenicity antibodies (X2). Architecture credited only as *"our
  proprietary architecture"*; filters on ipTM/pAE and self-consistency. The one
  design lineage in this map with no predictor parent in §1–§8.
  *Carries:* §9's one checkable result, and the awkward direction Beat 5 has to
  absorb. Latent-X1 designed macrocycles against **RFpeptides'** own targets and
  epitopes, re-synthesized RFpeptides' published best binders, and measured them in
  its own assays — the corpus's only third-party wet-lab comparison of two design
  methods. The mechanism-withholding system did the more disciplined experiment.
  *Against:* RFpeptides (§2), which is why the entry exists here rather than as a
  line in Table B — and against the rest of §9, since it is the only tier-1 system
  that can be checked against an open method at all.
  *Caveat:* two, and they are what keep the comparison honest. Only the *binders*
  were re-measured, while the hit rates it contrasts with are RFpeptides'
  literature-reported ones, so that half is not a matched-assay comparison; and it
  covers one pair of methods on one modality. Its own headline rates are
  self-reported and the corpus's highest.
  *Collision:* the head-to-head is argued in full under Table B, where its limits
  belong. **Latent-X2 carries the gaps unit's developability entry**, not this one.
* **Back-references:** **Chai-2**'s generator (§4) and **BoltzProt-1** (§3) belong to
  this tier and are reviewed in their own lineages. Boltz is the
  tier's most informative case, because the same lab's earlier models are open and in
  the corpus — the comparison the other entries do not permit.

**Tier 2 — no publication at all, known only through other people's benchmarks.**

* **IsoDDE** (Isomorphic Labs) — the frontier reference at the top of OpenDDE's
  scaling curve. Everything the review can say about it was measured by a competitor,
  which OpenDDE itself states as a limit on what can be concluded.
  *(map-only — private, no publication.)* · **mention**
* **Chai-3** and **SeedFold** — a commercial web platform and a point on
  OpenDDE's scaling curve respectively. *(map-only.)* · **mention**

For all of Tier 2, every number this review can cite was measured by a
competitor. Beat 5's symmetry lands here: Isomorphic authors are core
contributors on the AlphaFold3 paper, so the review opens on the published half of
that organisation's work and closes on the half that stopped publishing.

---

# What the field has not shown

A short unit, placed after §9 because every item in it is a question §1–§9 raise and
none of them answer. **Each entry is a limit the corpus states about itself** — no
gap is asserted here that a paper in `refs.bib` does not name, and each points at the
entry where the evidence sits.

**1. Binding is not the endpoint, and almost nothing here optimizes past it.**
Every system in §1–§8 generates, filters and reports on *binding*. Latent-X2 (§9)
states the problem directly: campaigns fail *"not because they lack binding, but
because binding alone is insufficient when clinical success demands developability
and low immunogenicity"*, and it reports developability profiles and what it claims
is the first low-immunogenicity demonstration for an AI-generated antibody.
*The awkward part, and the reason this is a unit rather than a caveat:* the one
system in the review that optimizes past binding is a closed one. Beat 5's
uncomfortable direction, arriving a second time.

**2. No system here predicts protein-protein binding affinity.** The filters are
binary. BindCraft (§6) says so of its own: AF2 ipTM is a strong predictor of
*whether* a design binds and does not track *how tightly*. The corpus's one affinity
module is Boltz-2's (§3), which is protein-ligand and whose own paper states it does
not handle multimeric binding partners. So the field designs binders it cannot rank
by strength, and affinity appears in Table B only as an outcome measured in a wet lab
after the fact.

**3. Design success against targets with no experimental structure is untested.**
Germinal (§6) names it: how far design success depends on the quality of the antigen
model *"remains an open question"*. Every campaign in Table B designed against solved
or confidently predicted structures. What the methods do on the targets that most
need them is not in the corpus.

**4. There is no shared benchmark for binder design, and one third-party wet-lab
comparison exists in the whole corpus.** Both facts are established elsewhere — the
first under Tables A and B, the second in §2's RFpeptides entry and §9's Latent-X1
entry. This unit does not re-argue them; it collects them as what they are, the
measurement gap the review's caveats keep running into.

*What this unit is not.* Not a wish list, not a speculation about what comes next,
and not a place for limitations already attached to an entry. A gap enters here only
when a publication in the catalog states it and no section owns it.

---

# The instruments

Not models, but the instruments every number in §1–§9 is denominated in. Written
once, referred to from any section.

* **ColabFold** — `colabfold` · `10.1038/s41592-022-01488-1` · **meat** — apparatus,
  not a scorer: AF2 and AlphaFold-Multimer weights untouched, with the homology search
  replaced by a hosted MMseqs2 pipeline over its own environmental database. Orders of
  magnitude faster, at unchanged accuracy.
  *One claim, and it is the reason the entry exists:* **the AF2 numbers elsewhere in
  this review are ColabFold numbers.** Chai names the version it ran, ESMC builds every
  evaluation MSA with it, and the Overath meta-analysis reuses one ColabFold MSA per
  target across all three of its predictors. Table A's AF2 column and Table B's AF2
  filters therefore rest on ColabFoldDB alignments, not the pipeline AF2 shipped with —
  a provenance fact the tables must state and the prose need not dwell on.
  *One consequence for the design half:* it names *"designed proteins without known
  homologs"* as the case extra recycling rescues — Beat 4's off-distribution problem,
  identified in 2022 — and the corpus sets that knob differently paper to paper.
* **PoseBusters** — `posebusters` · `10.1039/D3SC04185A` · **meat** — physical and
  chemical validity checks plus a benchmark set; source of the "PB-valid" metric
  reported by AF3, Chai-1, Boltz-1 and Protenix.
  *Carries:* the unit the physical-validity thread is denominated in, and its own
  finding that deep-learning docking did not beat classical tools on physical
  plausibility or generalization to novel sequences.
  *Caveat:* two. It is a **ligand-side** instrument doing protein-side duty here; and
  Protenix-v2 shows the criterion is incomplete — structures pass while exhibiting
  twisted amides and distorted aromatics.
  *(PoseBusters V2 is a benchmark-set revision, not a separate publication; map-only.)* · **mention**
* **FoldBench** — `foldbench` · `10.1038/s41467-025-67127-3` · **backbone** —
  peer-reviewed all-atom prediction benchmark spanning monomers, protein-protein,
  antibody-antigen, protein-ligand and protein-nucleic interfaces; the shared
  evaluation set behind the AF3 / Protenix / Boltz / ESMFold2 / OpenDDE comparisons.
  *Carries:* Table A's benchmark column, and therefore the Table A / Table B
  asymmetry — the benchmarking units' strongest finding, and Beat 5's main empirical
  support, exist only because prediction has a shared instrument and design has none.
  *Against:* the design half's nothing. Its value to this review is as much what its
  absence proves on the other side as what it measures on this one.
  *Caveat:* Protenix-v1 shows its published aggregates do not enforce a common
  intersection of successfully-evaluated targets, so coverage differences alone can
  flip model rankings.
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
  *Carries:* the metrics primer's payoff. Precision for the best available score
  runs across nearly the full range from target to target, and Germinal (§6) reports
  the same failure from the other side. mBER (§6) measures the same thing at larger
  scale and points the other way; the primer is where the two are reconciled.
  *Against:* the AF2 initial-guess iPAE that RFdiffusion filters on, which AF3
  `ipSAE_min` beats — the only head-to-head of *filters* in the corpus, as opposed to
  head-to-heads of generators.
  *Caveat:* previous-generation miniproteins, antibodies excluded — the generation
  before the one this review centres on. It does not fill Table B's missing benchmark
  column.

* **PXMeter** — `pxmeter` · `10.1101/2025.07.17.664878` · **meat** — open evaluation toolkit
  and artifact-filtered dataset; basis of the PXM benchmark family. v1.1.0 extends
  PoseBusters with sp2-planarity, amide-planarity and sp3-non-planarity checks.
  [GitHub](https://github.com/bytedance/PXMeter)
* **Gauss-Seidel projection** — `gauss_seidel_projection` ·
  `10.48550/arXiv.2510.08946` · **mention** — a differentiable projection onto the
  nearest physically valid configuration, enforcing validity as a strict constraint
  rather than a bias.

**The physical-validity thread, stated once here and nowhere else.** AF3-class
models inherited a problem their predecessors did not have: diffused coordinates can
be chemically impossible. The corpus holds four responses — inference-time
**steering** (Boltz-1x, §3), **learned** stereochemistry features (RFAA then RF3,
§2), **strict projection** (above), and **fixing the metric** (PoseBusters' limit,
then PXMeter). Only one pair has been measured against the other: RF3 reports more
ligand chiral centres correct than AF3 or Boltz-2 without guidance, and argues
steering *"may shift the network outside the training distribution"*. That is the
thread's one settled question; the rest is four groups asserting different answers,
and the section says so rather than adjudicating.

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
Beat 5 sets up an ending, but what the review concludes follows from the units above
rather than preceding them, so it is settled once they exist. What it has to land,
all of it already argued above and none of it resolved: the open-versus-closed
question Beat 5 opens and §9 leaves standing; the two threads, which are paid off in
§8 and under Table B but not closed; Beat 3's designs-tested number, whose trajectory
is the review's spine and has no shared instrument to measure it against; and the
four gaps, which are where the conclusion has its material if it wants any.

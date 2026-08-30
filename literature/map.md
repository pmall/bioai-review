# Literature Map

> The living entry point of the review. One layout, used everywhere: the map is
> ordered exactly as the final review will read, so there is no second
> organization to reconcile. Concepts and references are added here first, then
> formalized into `literature/refs.bib` through the `map-to-bib` skill.
>
> **This file is a layout, not a review.** Every publication in the corpus is
> named here, placed in exactly one home section, and given one line of role.
> The analysis lives in `literature/drafts/` — one report per section, written
> separately. Resist growing entries here; if a finding needs a paragraph, it
> belongs in that section's report.
>
> **Five parts.** I — the intro narrative plan. II — the section order and why
> it is that order. III — the nine sections and the publications in each.
> IV — benchmarking and validity infrastructure, transversal to all nine.
> V — publications examined and deliberately excluded, with the reason recorded.
>
> **Every publication named in this file is in `refs.bib`.** Works that might
> belong but have not been decided on are held out of the map entirely, in
> `literature/candidates.md`.
>
> **Coupling levels** — the review's spine, defined in Beat 4 and in
> `drafts/structure_prediction_family_overview.md` §1.1:
> **Level 0** the generator *is* a repurposed predictor (inherited weights);
> **Level 1** generate, then filter with a critic (no gradient);
> **Level 2** backpropagate the predictor's loss into the design variable.
> Level 0 is an attribute of an entry, not a section — marked *(inherits …)*.
>
> **Map ↔ catalog invariant.** Every concept resolves to exactly one place: its
> own `refs.bib` entry, a `keywords` tag on the paper that describes it, or the
> map alone. Entries with a publication carry their **bib key** and **DOI**
> inline so the mapping is checkable mechanically in both directions. Concepts
> with no publication are marked *map-only* with the reason.
>
> **Scope.** In scope = generates a **protein or peptide binder conditioned on a
> target**, or predicts the structure such a system designs against. Out of
> scope = a different modality (small molecules), or sequence generation with no
> target conditioning. The field moves fast — explosive in 2026 — so references
> dated before 2025 are generally out of scope, except where they belong to an
> active lineage whose full history is kept for understanding (ESM, RoseTTAFold).

---

# PART I — PLAN: INTRODUCTION NARRATIVE

The intro's job is to make the nine sections feel inevitable rather than
enumerated. Five beats, each ending where the next begins.

### Beat 1 — Scope: protein and peptide binders

State the modality up front: this is a review of designing **proteins and
peptides that bind a chosen target**, not of small-molecule drug design.
Antibodies, nanobodies, VHH, scFvs, minibinders and macrocyclic peptides are in;
DrugFlow and FLOWR generate small molecules and are recorded as out of scope in
Part V; BoltzMol-1 screens them and is out of scope for the same reason, but is
kept in §3 with the rest of the Boltz lineage.

Two reasons, both better than "that is where the papers are":

- **Small molecules are brittle in a way sequences are not.** Potency can
  collapse on a single-atom change — the activity-cliff problem — so a generator
  must land in exactly the right place rather than a good neighbourhood. Boltz-2
  frames its affinity work around *"distinguishing subtle differences in binding
  affinity among closely related analogues"*, precisely the regime where small
  perturbations are not small. A protein binder's affinity degrades far more
  gracefully across nearby sequences, which is what makes generate-and-filter
  workable at all.
- **Sequences are differentiable; molecular graphs are not.** The deeper reason,
  and what connects Beat 1 to Beat 4. A protein sequence relaxes cleanly into a
  continuous distribution over 20 amino acids per position — every point in that
  simplex is a valid input, so a Level-2 loop can backpropagate straight through
  it (BindCraft's *L*×20 gradient; ESMFold2's continuous amino-acid
  distributions; Germinal's CDR logits). A molecule is a variable-size graph with
  hard valence constraints, and most continuous relaxations of it are not
  molecules. The corpus shows the field working around this rather than solving
  it: **DrugFlow** pairs continuous flow matching for coordinates with **discrete
  Markov bridges** for atom and bond types; **FLOWR** uses a *"mixed continuous
  and categorical"* scheme for the same reason. Separate discrete machinery is
  needed exactly where proteins need none. Whether a Level-2 loop is achievable
  for small molecules is an open question this review does not settle — but the
  asymmetry is real, and it justifies the scope.

### Beat 2 — The founding bet, and the problem that got solved

Structure prediction was the prerequisite, and it was solved on a single wager:
**coevolution in a multiple sequence alignment is a usable proxy for spatial
contact.** AlphaFold2 cashed it — median 0.96 Å backbone accuracy on CASP14
against 2.8 Å for the next best method — and AlphaFold3 generalized it to
arbitrary complexes. Plant the MSA thread here; it pays off in Beat 4.

Close on the limitation that matters: a predictor tells you what a *given*
sequence folds into. It does not tell you which sequence to try.

### Beat 3 — Why prediction was not enough: the experimental budget

The honest motivation for generative design is not the size of sequence space in
the abstract — it is that **you cannot screen your way to a binder**. Make the
collapsing experimental budget the review's quantitative spine:

| Era | Designs tested per target | Source |
|---|---|---|
| Screening-based, and early computational design | *"thousands to millions of designs to reliably identify hits"* | Chai-2's characterisation of prior work |
| Current generative + filtering | 16–30 (Protenix-v2), ≤20 (Chai-2), 30–100 (Latent-X), 43–101 (Germinal), 84 (ESMFold2) | each system's own campaign |

**Read the hit rates below with BoltzProt-1's distinction in hand** (§3): it separates *screening hits* from *confirmed binders*, and reports that screening hits are *"what prior binder design model literature typically reports as binders"*. Its own confirmed-binder rate is 8.0% where the screening-hit framing would give a much larger number. The percentages quoted across this review are not all measuring the same event.

Hit rates reported in the same papers — 16% (Chai-2, de novo antibodies), up to
48% and 16–88% on GPCRs
(Protenix-v2 VHH-Fc), >90% (Latent-X macrocycles), 70% (ESMFold2 minibinders) —
make the point sharper than any statement about combinatorics. **The measure of
progress in this field is how few designs you must make to get a binder.**
The nine sections are, read one way, a history of that number falling.

**Worth one sentence: the machinery was borrowed from image generation, and the
field said so.** RFdiffusion's paper introduces the technique as *"denoising
diffusion probabilistic models (DDPMs), a powerful class of machine learning
models recently demonstrated to generate new photorealistic images in response to
text"*. The parallel is the field's own, not a populariser's, and it earns its
place twice: it orients any reader who has met Stable Diffusion, and it explains
the formalism shift in §5 — image generation made the same diffusion →
flow-matching move, for the same reasons of sampling speed and simplicity.

Then turn it, because the analogy breaks exactly where this field gets
interesting: **image generation has no AlphaFold.** There is no differentiable
oracle scoring whether a generated image is *correct*, so image models are judged
by human preference and cannot close a loop on their own objective. Protein
design can, and that is Beat 4. The borrowed machinery is the easy half; the
critic is the part with no counterpart in the source field.

### Beat 4 — Closing the loop, and why MSA emancipation was the precondition

Generators need a critic, and the critic is a structure predictor. That gives the
review its spine — the three coupling levels defined in this map's header:

- **Level 0** the generator *is* a repurposed predictor;
- **Level 1** generate, then filter — still the field's default, and the origin
  of the standard success criterion (AlphaProteo: *"interchain AF2 pAE < 10,
  binder-aligned binder RMSD < 1 Å, pLDDT > 80"*);
- **Level 2** backpropagate the predictor's loss into the sequence being designed.

Here the MSA thread pays off, and it is the intro's one genuinely non-obvious
claim: **an MSA is a database lookup on a sequence that does not exist yet.** It
is neither differentiable nor defined for a binder being invented, so a Level-2
loop must run its predictor single-sequence on the designed chain. That is why
BindCraft, hallucinating through AlphaFold2, operates the model in exactly the
regime AF2's own paper documents as its weakest, and why ESMC/ESMFold2 —
natively single-sequence — can backpropagate through a 6B-parameter language
model without leaving distribution. **MSA emancipation is not an accuracy story;
it sets the ceiling on how tightly a generator can couple to its critic.**

Close with the arc recorded in §6: Level 2 is the *oldest* idea here, tried as
constrained hallucination, beaten by RFdiffusion, and now returning because the
predictors finally support it — across five systems and four predictor families.

**A second refinement to plant, or §3 will surprise the reader.** Level 1 says
"filter", and the field long read that as *the predictor's own confidence head*.
BoltzPPI breaks that equation: a critic trained specifically to answer "will this
bind", replacing BoltzGen's confidence metrics, lifts the confirmed-binder hit
rate from 3.3% to 8.0% with the generator untouched. So Level 1 has two regimes —
*confidence-as-critic* and *trained-critic* — and the evidence says the filter,
not the generator, is where the hit rate lives. PXDesign's finding that Protenix
and AF2-IG filters retain *different* true positives points the same way.

### Beat 5 — The closed frontier

End on the limit of what a literature review can establish. The strongest claimed
results increasingly come from systems that publish benchmarks and withhold
mechanisms — AlphaProteo, Latent-X, Chai-2's generator, and IsoDDE, which has no
publication at all and is visible only as the top point on a competitor's scaling
curve.

**The sharpest version of this is not IsoDDE — it is Boltz.** The Boltz lineage
enters the review as the open answer to AlphaFold3's closed weights, and exits it
with its own frontier closed: Boltz-1, Boltz-2 and BoltzGen stay MIT, while
BoltzProt-1 and BoltzMol-1 ship API-only with no weights. It is the one lineage
where the review holds the before *and* the after, both with papers. Note also
the symmetry that gives §9 its force: **AlphaFold3 is a Google DeepMind *and
Isomorphic Labs* paper**, so the review opens on the published half of that
organisation's work and closes on the half that stopped publishing.

### Two caveats the intro must plant, or the reader will over-read the tables

1. **The numbers are not as comparable as they look.** Different benchmarks,
   cutoffs and target sets; FoldBench's published aggregates do not enforce a
   common intersection of evaluated targets, and Boltz-2's have a
   temporal-leakage caveat flagged independently by three teams. Point at Part IV
   rather than relitigating it in each section.
2. **Wet-lab hit rates are self-reported and target-dependent.** Every campaign
   chose its own targets, and the papers that disclose most about their methods
   are not the ones reporting the highest numbers — itself a finding, and Beat
   5's justification.

---

# PART II — PLAN: SECTION ORDER AND PROGRESSION

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
the argument entirely. Stating this up front stops the order looking inconsistent
halfway through.

| # | Section | Covers | Organizing fact |
|---|---|---|---|
| 1 | **AlphaFold, and the open co-folding cluster** | AlphaFold2, AlphaFold3; OpenFold/OpenFold3; OpenDDE | prediction only; everything later is defined relative to it |
| 2 | **RoseTTAFold → RFdiffusion** | RF1, RFAA; RFdiffusion 1/2/3; ProteinMPNN/LigandMPNN | diffusion; the first prediction→generation turn; introduces inverse folding |
| 3 | **Boltz** | Boltz-1, Boltz-2, BoltzGen, BoltzProt-1/BoltzPPI, BoltzMol-1 | diffusion, stated outright — and the lineage that opened, then closed |
| 4 | **Chai** | Chai-1, Chai-2 | Chai-1 is a diffusion co-folder; Chai-2's *generator* is undisclosed |
| 5 | **Flow matching** | FrameFlow, PPIFlow, OriginFlow, AtomFlow, D-Flow | the successor formalism — FrameFlow *"adapt[s] FrameDiff … to the flow-matching generative modeling paradigm"* |
| 6 | **Inversion as a portable technique** | BindCraft, BoltzDesign1, Germinal | Level 2 as a bare method — three groups, three predictors, one technique |
| 7 | **Protenix** | Protenix-v1, Protenix-v2, PXDesign-d and PXDesign-h | the first pipeline to *compose* both couplings into one platform |
| 8 | **ESM** | ESM-2/ESMFold, ESM-3, ESMC/ESMFold2 and its binder campaign | Level 2, fully integrated — the analytical climax |
| 9 | **The closed frontier** | AlphaProteo, Latent-X 1/2; IsoDDE, Chai-3, SeedFold | benchmarked but unexplainable — a coda, not a step in the argument |

**Why this order.**

- **1 first** because everything else reproduces AlphaFold, reacts to it, or
  replaces its evolutionary input. OpenFold3 and OpenDDE join it rather than
  getting their own sections: open co-folding models in the AF3 mould with no
  design descendant to follow.
- **2 second** — the one architecture developed independently of AlphaFold, the
  first to make the generative turn, and the source of the inverse-folding stage
  every later section relies on.
- **3 and 4** keep the diffusion block together while each lineage stays whole.
  Boltz precedes Chai because BoltzGen states its mechanism plainly and
  demonstrates the Level-0 identity in its purest form — one diffusion model
  doing prediction *and* design — and because §3 now also carries the two
  refinements §9 and Beat 4 need: the trained-critic result (BoltzPPI) and the
  open→closed fork.
- **5 after the diffusion sections, not before.** Flow matching only reads as a
  successor if the reader has already seen diffusion doing real work in §2–4.
  FrameFlow is literally FrameDiff reformulated, so the section can open by
  re-deriving something familiar rather than introducing a parallel formalism cold.
- **6, 7, 8 escalate integration, and the technique comes before the pipelines
  that compose it.** §6 introduces inversion on its own terms — three groups
  inverting three different predictors, no product around it — because a pipeline
  is a composition of techniques, and the reader should meet the part before the
  assembly. §7 is then the first full assembly: one lineage shipping a predictor,
  a Level-1 diffusion arm and a Level-2 hallucination arm as a single platform,
  with PXDesign-h measuring itself against the §6 systems. §8 is the limit case, where
  there is nothing left to compose: language model, folding head and design loop
  are one model. It ends the *argument* as the conclusion the MSA throughline has
  been building toward since §1.
- **9 last, deliberately outside the argument.** These systems publish benchmarks
  but not mechanisms, so they cannot be analysed the way §1–8 analyse everything
  else; placing them earlier would interrupt an argument they cannot contribute
  to. Last, they work as a coda — here is the frontier, here is what it claims,
  and here is precisely how little can be said about it.

**One ordering exception.** Part IV's metrics primer is *organized* with
the instruments but *renders* before §1 in the final review — sections 1–9 quote
pAE, pLDDT, ipTM and PB-valid from the start, and a reader who meets those units
for the first time in a closing part has been reading numbers on trust. Keep the
primer's single home in Part IV; move only its presentation.

**Level-2 roster, spread across §6–8 by lineage.** Five systems, four groups,
four predictor families: BindCraft (AlphaFold2, §6), BoltzDesign1 (Boltz, §6),
Germinal (AlphaFold2 + antibody LM, §6), PXDesign-h (Protenix, §7), ESMFold2
campaign (ESMC/ESMFold2, §8). Any claim about Level 2 being general rather than
an AF2 quirk rests on this spread.

**Non-disclosure covers four of the strongest results** — Chai-2, AlphaProteo,
Latent-X and IsoDDE. Lineages are not fragmented by disclosure status, so Chai-2
stays in §4 and Boltz's closed models stay in §3, each with a pointer to §9.

---

# PART III — THE SECTIONS

## §1 — AlphaFold, and the open co-folding cluster

Prediction only. The forward problem — sequence / chemical input → 3D structural
state — and the reference every later section is defined against.
Reviewed in `drafts/structure_prediction_family_overview.md`.

* **AlphaFold2** — `alphafold2` · `10.1038/s41586-021-03819-2` — single-chain and
  multimer predictor that established modern deep-learning structural biology;
  the MSA-as-coevolution bet every later model inherits or reacts against.
  *Also serves as:* the differentiable objective in BindCraft and Germinal (§6)
  and the standard post-hoc filter across §2–5 and §7.
* **AlphaFold-Multimer** — `alphafold_multimer` · `10.1101/2021.10.04.463034` —
  AF2 retrained on complexes; the complex predictor the rest of the review
  actually uses. **Kept despite the pre-2025 rule, under the active-lineage
  exception, because §6 does not invert AlphaFold2 — it inverts this.** BindCraft
  and Germinal both backpropagate through AF-M, and Germinal calls it AF-M
  throughout; without this entry the predictor at the centre of the Level-2
  section would be absent from the catalog. Mentioned by 13 corpus papers.
  **It is also where ipTM comes from** — *"we call this metric Interface pTM, or
  ipTM"*, with model confidence defined as 0.8·ipTM + 0.2·pTM. The canonical
  Level-1 success criterion quoted in Beat 4 is denominated in a metric this paper
  introduced, which makes the entry load-bearing for §2–§7 and Part IV, not just §6.
  *Never peer-reviewed* — still a 2021 bioRxiv preprint, checked August 2026.
  Worth one sentence in §9's terms: the most-used complex predictor in the field
  never got a journal version.
* **AlphaFold3** — `alphafold3` · `10.1038/s41586-024-07487-w` — all-atom
  diffusion predictor for protein / nucleic-acid / small-molecule / ion
  complexes. Closed weights — the stated motivating gap behind Boltz-1, Protenix
  and OpenFold3, and the origin of the openness thread that closes in §9.
* **OpenDDE** — `opendde` · `10.48550/arXiv.2607.03787` — Apache-2.0 all-atom
  co-folding foundation model with atomic latent reasoning; reports IsoDDE-level
  accuracy, a cross-model scaling law, and the corpus's most complete third-party
  antibody-antigen head-to-head. Design is roadmap only — explicitly *"not a
  complete drug-discovery system"*. [GitHub](https://github.com/aurekaresearch/OpenDDE)
* **OpenFold → OpenFold3** — AlQuraishi Lab's open reimplementations; OpenFold
  reproduces AlphaFold2 and supplies the distillation set Boltz-1 trains on,
  OpenFold3-preview targets bitwise AF3 reproduction.
  [GitHub](https://github.com/aqlaboratory/openfold-3)
  *(map-only — code releases, no paper or DOI; third-party benchmark numbers
  exist, run as a baseline by Protenix-v2 and OpenDDE.)*

## §2 — RoseTTAFold → RFdiffusion

The Baker Lab / IPD line, kept whole: two structure predictors, the three
generative models fine-tuned from them, and the sequence-design stage the whole
field borrowed. Level 0 in its purest form — one architecture serving prediction
or generation depending on what it is fine-tuned for.
Reviewed in `drafts/rfdiffusion_family_summary.md` and
`drafts/proteinmpnn_ligandmpnn_summary.md`.

**Section-defining fact:** as *predictors* these have left the conversation.
Mentions per co-folding paper run AlphaFold3 25, Chai-1 11, then Boltz-1,
Boltz-2, Protenix-v1, Protenix-v2, OpenDDE and ESMC/ESMFold2 all **zero**.
Nothing published since 2024 benchmarks against them. As *generators* they remain
the reference the whole field cites.

* **RoseTTAFold (RF1)** — `rosettafold` · `10.1126/science.abj8754` — three-track
  (1D/2D/3D) network developed independently of AF2; complex prediction emerged
  untrained from two-segment cropping. The architecture the family fine-tunes from.
  *Intermediate steps, map-only:* RoseTTAFoldNA and RoseTTAFold2 (preprints; RF2
  is RFAA's base network).
* **RoseTTAFold All-Atom (RFAA)** — `rosettafold_all_atom` ·
  `10.1126/science.adl2528` — all-atom generalization published two months
  *before* AF3 and independently of it; encodes chirality as architectural input
  features rather than as a loss or post-hoc penalty. No diffusion module.
* **RFdiffusion** — `rfdiffusion` · `10.1038/s41586-023-06415-8` *(inherits RF1)*
  — SE(3)-equivariant frame diffusion; established modern generative backbone
  design. Filtered by AF2 pAE / "in silico success".
  [GitHub](https://github.com/RosettaCommons/RFdiffusion)
* **RFdiffusion2** — `rfdiffusion2` · `10.1038/s41592-025-02975-x` *(inherits RF1)*
  — atom-level enzyme active-site scaffolding from functional-group positions,
  sequence-agnostic.
* **RFdiffusion3** — `rfdiffusion3` · `10.1101/2025.09.18.676967` *(inherits RF1)*
  — transformer-based all-atom diffusion across proteins, DNA, RNA and ligands;
  inherits AF3's non-equivariant diffusion approach.
* **RFantibody** — `rfantibody` · `10.1038/s41586-025-09721-5` (*Nature* **649**,
  183–193; online 5 Nov 2025, issue 1 Jan 2026; preprint
  `10.1101/2024.03.14.585103`) *(inherits RFdiffusion)*
  — the lineage's antibody arm: a fine-tuned RFdiffusion designing VHHs, scFvs and
  full antibodies against user-specified epitopes, with cryo-EM confirming the
  designed CDR poses at atomic accuracy.
  *Why it matters to the argument:* it pairs design with **yeast-display library
  screening**, and says why in its own words — the screen is *"currently necessary
  due to the quite low design success rate"*. That is the honest baseline Beat 3's
  collapsing-budget table is measured against: §3, §4 and §6 report binders from
  tens of designs, and this is the paper they cite when claiming they no longer
  need library selection or directed evolution.
  Cited by seven corpus papers — Chai-2, Germinal, BoltzProt-1, BoltzGen,
  Protenix-v2, OpenGerminal, PPIFlow.
* **ProteinMPNN** — `proteinmpnn` · `10.1126/science.add2187` · and
  **LigandMPNN** — `ligandmpnn` · `10.1038/s41592-025-02626-1` — autoregressive
  message-passing networks generating sequences for a fixed backbone (and ligand
  / nucleic-acid environment, for LigandMPNN). The standard inverse-folding stage
  between backbone generation and structural validation, introduced here because
  §3–7 all rely on it. [GitHub](https://github.com/dauparas/ProteinMPNN)
  *Adoption is field-wide, not lineage-bound* — corpus papers referencing it:
  RFdiffusion3 (27), BoltzGen (14), RFdiffusion (10), RFdiffusion2 (6), RFAA (5),
  Latent-X1 (5), PXDesign (5), BindCraft (5), PPIFlow (4), AtomFlow (3),
  AlphaProteo (3), FrameFlow (2), D-Flow (2), OriginFlow (2), SaProt (2). Nine
  distinct labs, both coupling levels.

## §3 — Boltz

Diffusion, stated outright: BoltzGen is *"a single all-atom diffusion model
capable of performing both structure prediction and protein design"* — Level 0
in its cleanest published form. The section also carries two things the rest of
the review needs: the **trained-critic** refinement to Level 1, and the
**open→closed fork** that Beat 5 and §9 turn on.

**The fork.** Boltz enters the review as the open answer to AlphaFold3's closed
weights and exits it with its own frontier closed. Boltz-1, Boltz-2 and BoltzGen
remain MIT with weights released; BoltzProt-1 and BoltzMol-1 are API-only, no
weights, commercially distributed (from $0.025/prediction, partner integrations
at Benchling, Tamarind, Phylo and others). Both closed models still publish
papers and wet-lab numbers. This is the only lineage where the review holds the
before and the after with publications on both sides — which makes it a better
§9 exhibit than IsoDDE, where only the after exists.

* **Boltz-1** — `boltz1` · `10.1101/2024.11.19.624167` — first fully open (MIT)
  AF3-class co-folder; Boltz-1x adds Feynman-Kac inference-time steering for
  physical validity. Source of this project's only independent cross-model
  physical-validity measurements. [GitHub](https://github.com/jwohlwend/boltz)
* **Boltz-2** — `boltz2` · `10.1101/2025.06.14.659707` — adds a binding-affinity
  module (approaching FEP accuracy at >1000× lower cost), MD-ensemble
  conditioning, and the most complete conditioning system in the corpus (method,
  multimeric templates, contacts/pockets, each with optional hard steering).
  *Caveat:* benchmark numbers carry a temporal-leakage caveat flagged
  independently by ESMC, Protenix-v1 and Protenix-v2.
* **BoltzGen** — `boltzgen` · `10.1101/2025.11.20.689494` *(inherits Boltz)* —
  unified generative design across proteins, peptides, nanobodies, antibodies and
  small molecules; filters 10,000-design pools by refolding with Boltz-2
  (RMSD < 2.5 Å) plus a composite interaction score. Level 1,
  confidence-as-critic — the baseline BoltzProt-1 then beats by changing only the
  critic.
* **BoltzProt-1** — `boltzprot1` · `10.64898/2026.06.23.733997` *(inherits BoltzGen)* — refined
  BoltzGen generator ranked by **BoltzPPI**, a protein-protein interaction
  predictor built on Boltz-2 and trained to answer "will this bind" directly.
  Swapping the filter alone takes the confirmed-binder hit rate from **3.3% to
  8.0%** across 10 novel targets; 58% of designs pass all developability criteria
  simultaneously vs 40% for BoltzGen, 25% for clinical-stage IgG and 21% for
  clinical-stage VHH controls. On a second panel of 10 prior-literature targets it
  gets screening hits on **7/10, against the 6/10 Chai-2 reported** — the one
  direct §3-vs-§4 comparison in the map.
  *Still Level 1 — no gradient — but the critic is no longer the predictor's own
  confidence head.* API-only, no weights.
  **Definitional contribution, and it belongs in Beat 3.** The paper separates
  *screening hits* from *confirmed binders*, and says plainly that screening hits
  are *"what prior binder design model literature typically reports as binders"*.
  The 3.3→8.0% figures are confirmed-binder rates. Every hit rate quoted elsewhere
  in this map is on the looser definition, which makes cross-paper comparison
  worse than caveat 2 of the intro currently admits.
  * **BoltzPPI** — the trained critic itself; introduced inside the BoltzProt-1
    paper, no separate publication. *(resolves to the `boltzppi` keyword on
    `boltzprot1`.)*
* **BoltzMol-1** — `boltzmol1` · `10.64898/2026.07.04.736485` — small-molecule hit-discovery
  pipeline over an optimized Boltz-2, with an ADMET triage layer (logS, logD,
  Caco-2 permeability); functional actives or binders on **6/10 targets** on
  experimental budgets of **28–96 compounds per target**. API-only, no weights.
  *Out of scope by modality* — small-molecule virtual screening, ranking
  commercial catalogue compounds rather than generating binders, so the same
  exclusion that puts DrugFlow and FLOWR in Part V. **Kept here rather than
  there** because it is a Boltz model first: the open→closed fork is the section's
  argument and needs both closed models in one place. It contributes nothing to
  the review beyond that.
* **BoltzDesign1** — `boltzdesign1` · `10.1101/2025.04.06.647261` — inverts the
  Boltz predictor for binder design. *Level 2; reviewed in full in §6*, where the
  portability argument needs it next to BindCraft.

## §4 — Chai

Diffusion co-folding, then the strongest antibody-design result in the corpus
from a generator whose mechanism is never stated.

* **Chai-1** — `chai1` · `10.1101/2024.10.10.615955` — AF3-derivative adding a
  protein-LM track alongside the MSA track (either usable alone) and
  experimentally-grounded constraint features (pocket, contact, docking). The
  partial-MSA-emancipation hinge that §8 completes.
  [GitHub](https://github.com/chaidiscovery/chai-lab)
* **Chai-2** — `chai2` · `10.1101/2025.07.05.663018` *(inherits Chai-1, via a
  "Chai-1d" design prototype)* — zero-shot antibody design; ~16% wet-lab hit rate
  in 24-well-plate assays across 52 unbiased targets.
  *Disclosure note:* the paper describes only the *folding* submodule (Chai-2f,
  *"a similar architecture as Chai-1"*); the generative mechanism is never
  stated. Reported here, with a pointer to §9.
* **Chai-3 (2026)** — high-throughput commercial 3D foundation model.
  [platform](https://lab.chaidiscovery.com/) *(map-only — no publication;
  discussed in §9.)*

## §5 — Flow matching

Presented in these papers as the successor to diffusion rather than an
alternative — FrameFlow explicitly recasts FrameDiff as SE(3) flow matching and
reports 2× designability at 5× fewer sampling steps. All five generate protein or
peptide binders conditioned on a target; flow-matching papers that generate small
molecules or unconditioned sequences are in Part V.

* **FrameFlow** — `frameflow` · `10.48550/arXiv.2310.05297` — recasts FrameDiff as
  SE(3) flow matching; methodological ancestor of the rest of this section.
* **PPIFlow** — `ppiflow` · `10.64898/2026.01.19.700484` — SE(3) flow matching
  with in-silico maturation for picomolar/nanomolar binders and single-domain
  antibodies.
* **OriginFlow** — `originflow` · `10.1101/2025.04.29.651154` — combined SDE and
  flow-matching framework; reports 90% wet-lab hit rates across PD-L1, RBD, VEGF.
* **AtomFlow** — `atomflow` · `10.48550/arXiv.2409.12080` — atomic flow matching
  on unified biotokens; generates ligand-binding pockets from 2D molecular graphs
  without bound conformers.
* **D-Flow** — `dflow` · `10.1109/JBHI.2026.3683934` — full-atom flow matching on
  SE(3) frames and torus manifolds for bioorthogonal D-peptide binders.
  *Borderline on modality, and included deliberately:* D-peptides are mirror-image
  peptides built from D-amino acids, an exotic chemistry unlike anything else in
  this map. But the paper is explicitly *"conditioned on receptor binding"* for
  *"de novo D-peptide design"*, so the scope rule makes it binder design and it
  stays. Revisit only if the review decides to bound the modality more tightly
  than the rule does.

**Known weakness of this section, to budget for.** PPIFlow, OriginFlow, AtomFlow
and D-Flow are each cited by zero other papers in this corpus; only FrameFlow, at
3, has traction as the methodological ancestor. It will read as a survey of
parallel isolated efforts rather than a lineage. One combined report, not one per
model.

## §6 — Inversion as a portable technique

**Level 2, isolated.** Gradients flow through a structure predictor into the
design variable. Not a lineage — a *method*, shown here to be portable across
predictor families and research groups. It comes before §7 and §8 deliberately: a
pipeline is a composition of techniques, so the reader should meet inversion as a
bare part, on three different predictors and from three different groups, before
meeting it built into a product (§7) or dissolved into a single model (§8).
The arc to carry into the section:

1. *Tried early.* Constrained **hallucination** — optimizing a sequence through
   RoseTTAFold until it predicts the target fold — was the Baker lab's approach
   before RFdiffusion.
2. *Abandoned.* RFdiffusion's own paper reports beating it: *"RFdiffusion
   significantly outperforms Hallucination (with RF) at unconditional monomer
   generation"* (z = 9.5, P = 1.6 × 10⁻⁹). Diffusion won, and Level 2 went quiet.
3. *Revived.* It returns on predictors strong enough to be run single-sequence
   without falling off-distribution — the precondition argued in Beat 4 and in
   `drafts/structure_prediction_family_overview.md` §1.2.
4. *Portable.* Counting the two Level-2 systems housed in §7 and §8, five systems
   from four groups now invert four different predictor families.

Do not present Level 2 as simply the newest thing; it is the oldest idea in the
review, returning under conditions that did not previously hold.

* **BindCraft** — `bindcraft` · `10.1038/s41586-025-09429-6` — backpropagates
  through AF2-multimer weights to produce an *L*×20 error gradient over
  amino-acid choices, annealed in four stages from continuous logits to one-hot.
  Target flexibility retained; no separate scaffolding step.
  *Predictor:* AlphaFold2 (§1), run single-sequence for the designed chain —
  off-distribution for AF2, which the annealing and 5-model ensembling appear to
  compensate for.
* **BoltzDesign1** — `boltzdesign1` · `10.1101/2025.04.06.647261` — the same
  inversion moved from AlphaFold2 to the Boltz all-atom predictor (§3).
  *Lineage:* Cho, Pacesa, Zhang, **Correia** and **Ovchinnikov** — the last two
  are also BindCraft's senior authors, so these two entries are one research
  programme porting one method, not two independent data points. The independence
  of the technique rests on Germinal, PXDesign-h and ESMFold2, not on this pair.
  *(In the corpus, not yet reviewed in depth. Cited by six corpus papers:
  PXDesign, RFdiffusion3, Latent-X1, Boltz-2, BoltzGen, ESMC.)*
* **Germinal** — `germinal` · `10.1038/s41587-026-03187-0` (*Nature Biotechnology*,
  23 Jun 2026; preprint `10.1101/2025.09.19.677421`) — gradient-based
  hallucination through AlphaFold-Multimer (AF-M) via ColabDesign, designing
  epitope-targeted CDRs onto a user-specified framework, in nanobody and scFv
  formats. Four diverse targets, nanomolar affinities, **43–101 designs tested
  per antigen**.
  *Essentially BindCraft for antibodies*, and the paper's own framing — it opens
  by crediting BindCraft with inverting AF-M *"to achieve high experimental
  success rates for de novo miniproteins"*. Same predictor, same inversion,
  specialized to the CDR problem, independent group (Mille-Fragoso, Hie, Gao —
  Stanford / Arc Institute).
  **Mechanistically distinct in the way that matters:** the only Level-2 system
  that puts a *sequence prior inside the loss*. AF-M and IgLM gradients are
  merged each iteration — default a weighted sum, ∇Germinal = ∇AFM + λ∇IgLM, with
  MGDA and weighted PCGrad as alternatives. ESMC gets the same effect by having
  the LM and folding head be one model; Germinal bolts a separate LM onto the
  gradient. Position it against §8 on exactly that point.
  *Also worth carrying into the report:* three-phase optimization (logits →
  softmax → **semigreedy** discrete updates), so like BindCraft and unlike ESMFold2
  it is multi-stage; **AbMPNN** (antibody-fine-tuned MPNN) redesigns CDR residues
  not contacting the antigen, a lineage variant of §2's inverse-folding stage;
  and the input antigen structures come from **AlphaFold3**, validated to
  Cα-RMSD < 1 Å against experimental structures.
  *Number to handle carefully:* the widely-quoted **4–22% success rate** is from
  the September 2025 **preprint abstract**. It does not appear in the *Nature
  Biotechnology* text, which reports design counts and per-target results instead.
  Cite the preprint explicitly if the range is used at all.
  *Best-connected recent addition:* cited by six corpus papers — PPIFlow,
  Protenix-v1, Protenix-v2, BoltzGen, ESMC, Latent-X2.
  * **OpenGerminal** — `opengerminal` · `10.64898/2026.06.25.734527` — Apache-2.0 reimplementation
    replacing PyRosetta with OpenMM/FreeSASA/FASPR and IgLM with AbLang1, at
    ≥1.5× per-trajectory cost. The counter-movement to §3's closure, and worth one
    sentence for that contrast alone.
    *Read its numbers carefully — the abstract and the body disagree.* The
    headline 33.7% vs 18.6% (PD-L1) and 24.6% vs 8.0% (IL-3) are **cofolding
    entry** rates; §3.3 gives the **pass** rates as 18.4% vs 10.9% and 5.2% vs
    4.0%, a much smaller gap. Computational only — two VHH targets, no wet lab.

## §7 — Protenix

The first full assembly. One lineage ships the predictor, a Level-1 diffusion
arm and a Level-2 hallucination arm as a single platform — the couplings of §1–6
stop being alternatives and become two modes of one product, chosen per target.
It is also the section where §6's technique gets benchmarked from the outside:
PXDesign-h measures itself against exactly BindCraft and BoltzDesign1.

* **Protenix-v1** — `protenix_v1` · `10.64898/2026.02.05.703733` — ByteDance
  Seed's open all-atom model matching AF3 under matched cutoff/scale/inference
  budget; adds RNA MSAs and protein templates. Contributes the
  common-intersection critique of FoldBench (Part IV).
  [GitHub](https://github.com/bytedance/Protenix)
  *Predecessor, map-only:* the 2024/2025 *Protenix — advancing structure
  prediction through a comprehensive AlphaFold3 reproduction* technical report
  (v0.2.0/v0.5.0), cited as ref 19 by Protenix-v1; not cataloged, not in corpus.
* **Protenix-v2** — `protenix_v2` · `10.64898/2026.04.10.717613` — both halves in
  one paper. *Prediction:* 9–13 point antibody-antigen gains over v1, 5-seed
  performance exceeding v1 at 1000 seeds, and the finding that the PoseBusters
  criterion is itself incomplete. *Design (Level 1, inherits Protenix):*
  target-conditioned generation with epitope-specific or site-agnostic modes
  across miniproteins, VHH and Fv; per-CDR length control; 100% target-level
  success in novelty-controlled VHH-Fc campaigns, GPCR hit rates 16–88%.
* **PXDesign** — `pxdesign` · `10.1101/2025.08.15.670450` — the platform that
  composes both couplings, and the reason this section sits where it does:
  * **PXDesign-d** — diffusion arm, Level 1 *(inherits Protenix)*.
  * **PXDesign-h** — hallucination arm, **Level 2**, backpropagating through
    Protenix. Benchmarked head-to-head against exactly BindCraft and BoltzDesign1
    — evidence the field treats §6 as one category.
  * *Also contributes the filter-ensembling finding:* Protenix and AF2-IG filters
    retain **different** true positives with limited overlap — the other half of
    Beat 4's critic-quality argument, alongside BoltzPPI.

## §8 — ESM

The analytical climax: the only entry where language model, folding head and
design loop are one system, and the conclusion the MSA throughline has been
building toward since §1.

* **ESM-2 & ESMFold** — `esm2` · `10.1126/science.ade2574` — founding
  single-sequence predictor; structure emerges from masked-LM scaling alone, no
  MSA or templates at inference. Enabled the ESM Metagenomic Atlas (>617M
  predicted structures; the Atlas itself is a database, out of scope).
* **ESM-3** — `esm3` · `10.1126/science.ads0018` — multimodal promptable PLM
  tokenizing sequence, structure and function in parallel tracks. A lineage step,
  reviewed as such rather than as a competitor on folding accuracy.
* **ESMC & ESMFold2** — `esmc` · `10.64898/2026.06.03.729735` — Biohub /
  EvolutionaryScale's ~2.8B-sequence LM plus a folding head on its frozen
  representations. **Full MSA emancipation:** single-sequence antibody-antigen
  accuracy exceeding AF3-with-MSA, with a detachable MSA encoder kept only as a
  rescue path for high-perplexity sequences.
  *Covers:* ESMFold2 and ESMFold2-Fast (modules of this release, no separate paper).
  * **ESMFold2 binder design campaign** — **Level 2**, and the tightest coupling
    in the review: *"represents sequences as continuous distributions over amino
    acid probabilities and optimizes by backpropagation through ESMC and
    ESMFold2"* — gradients pass through the 6B language model as well as the
    folding head, and a **single-stage** optimization suffices, where BindCraft
    needs four annealing stages. Minibinders and scFvs against five
    oncology/immunology targets, BLI-validated, hit rates rising with compute.
    Single-sequence is its native regime, so there is no off-distribution penalty
    to compensate for. *(module of the ESMC release — no separate publication.)*

## §9 — The closed frontier

A coda, not a step in the argument. Systems that publish benchmarks and withhold
mechanisms — placed last because they cannot be analysed the way §1–8 analyse
everything else. **Two tiers, and they are not the same problem.**

**Tier 1 — published, results disclosed, mechanism withheld.**

* **AlphaProteo** — `alphaproteo` · `10.48550/arXiv.2409.08022` — DeepMind
  generative engine plus a multi-stage filter for picomolar/nanomolar binders.
  Describes its generator only as *"a generative model trained on structure and
  sequence data from the PDB and a distillation set of AlphaFold predictions"*.
  Defines in-silico success as *"interchain AF2 pAE < 10, binder-aligned binder
  RMSD < 1 Å, pLDDT > 80"* — the canonical statement of the Level-1 criterion,
  quoted in Beat 4.
* **Latent-X1** — `latentx1` · `10.48550/arXiv.2507.19375` · and **Latent-X2** —
  `latentx2` · `10.48550/arXiv.2512.20263` — Latent Labs' atom-level binder design
  platform: macrocycles and minibinders (X1), then drug-like low-immunogenicity
  antibodies validated in human panels (X2). Filters on ipTM/pAE and
  self-consistency; architecture credited only as *"our proprietary
  architecture"*. The one design lineage in this map with no predictor parent in
  §1–8.
* **Back-references:** **Chai-2**'s generator (§4) and **BoltzProt-1 /
  BoltzMol-1** (§3) belong to this tier and are reviewed in their own lineages.
  Boltz is the tier's most informative case because the same lab's earlier models
  are open and in the corpus — the comparison the other entries do not permit.

**Tier 2 — no publication at all, known only through other people's benchmarks.**

* **IsoDDE** (Isomorphic Labs) — the frontier reference at the top of OpenDDE's
  scaling curve; credited with gains in protein-ligand generalisation,
  antibody-antigen interfaces, pocket identification and affinity estimation.
  OpenDDE states the limit plainly: *"we do not have access to its full training
  recipe, data mixture, inference procedure, post-training strategy, or
  engineering optimizations … we cannot yet determine which differences arise
  from model architecture, data processing, scaling, distillation, or
  inference-time procedures."* *(map-only — private, no publication.)*
* **Chai-3** and **SeedFold** — a commercial web platform and a point on
  OpenDDE's scaling curve respectively. *(map-only.)*

For all of Tier 2, every number this review can cite was measured by a
competitor. Close on the symmetry: **AlphaFold3 is a Google DeepMind *and
Isomorphic Labs* paper** — Isomorphic authors are listed as core contributors —
so the review opens on the published half of that organisation's work and closes
on the half that stopped publishing.

---

# PART IV — BENCHMARKING, VALIDITY & EVALUATION INFRASTRUCTURE

Not models, but the instruments every number in Part III is denominated in.
Transversal: written once, cited from any section. One combined report.
Three blocks: the metrics primer, the instruments themselves, then the two
summary tables that gather what they measured.

## The metrics primer — read first, filed here

**The problem it solves.** Beat 4 quotes the canonical success criterion —
*"interchain AF2 pAE < 10, binder-aligned binder RMSD < 1 Å, pLDDT > 80"* — before
anything has said what pAE or pLDDT are. Every section afterwards then reports
numbers in these units. The review needs one place that defines them, and it must
be read early even though it is organized here with the other instruments (see
Part II). Do not put it in the intro: the intro is building an argument, and a
definitions block dropped into Beat 2 or Beat 4 would stall it.

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
predictor's opinion of its own output. That is what makes three findings in this
part matter rather than being technicalities: PoseBusters' incompleteness,
AlphaFold-Multimer's ipTM being the metric everyone inherited (§1), and
BoltzProt-1's BoltzPPI (§3) replacing a confidence head with a critic trained
against experimental outcomes — the first departure from family 2 in the corpus.
State the families and that consequence; list individual metrics only as needed
to support it.

## The instruments

* **PoseBusters** — `posebusters` · `10.1039/D3SC04185A` — 18-check
  physical/chemical validity suite (RDKit) plus a benchmark set; source of the
  "PB-valid" metric reported by AF3, Chai-1, Boltz-1 and Protenix. Its own
  finding — that deep-learning docking did not beat classical tools on physical
  plausibility or generalization to novel sequences — concerns ligand docking, so
  it is a ligand-side instrument doing protein-side duty here.
  *Known limit:* Protenix-v2 shows the criterion is incomplete — structures pass
  while exhibiting twisted amides and distorted aromatics.
  *(PoseBusters V2 — a benchmark-set revision, not a separate publication; map-only.)*
* **FoldBench** — `foldbench` · `10.1038/s41467-025-67127-3` — peer-reviewed
  all-atom prediction benchmark spanning monomers, protein-protein,
  antibody-antigen, protein-ligand and protein-nucleic interfaces; the shared
  evaluation set behind the AF3 / Protenix / Boltz / ESMFold2 / OpenDDE comparisons.
  *Known limit:* Protenix-v1 shows its published aggregates do not enforce a
  common intersection of successfully-evaluated targets, so coverage differences
  alone can flip model rankings.
* **PXMeter** — `pxmeter` · `10.1101/2025.07.17.664878` — open evaluation toolkit
  and artifact-filtered dataset; basis of the PXM benchmark family. v1.1.0 extends
  PoseBusters with sp2-planarity, amide-planarity and sp3-non-planarity checks.
  [GitHub](https://github.com/bytedance/PXMeter)
* **Gauss-Seidel projection** — `gauss_seidel_projection` ·
  `10.48550/arXiv.2510.08946` (ICLR 2026) — a differentiable projection mapping
  provisional diffusion coordinates to the nearest physically valid
  configuration, exploiting constraint sparsity; integrates into existing
  predictors for end-to-end fine-tuning. Enforces validity as a *strict
  constraint* rather than a bias, which the paper argues inference-time steering
  (Boltz-1x) cannot guarantee. Two denoising steps suffice.
  *A fifth distinct response to the inherited physical-validity problem, alongside
  re-ranking, steering, architectural chirality features (RFAA) and fixing the
  metric (PXMeter).*

**The third caveat this part owns:** Boltz-2's benchmark numbers carry a
temporal-leakage caveat flagged independently by ESMC, Protenix-v1 and
Protenix-v2. Together with FoldBench's common-intersection problem and
PoseBusters' incompleteness, this is why Beat 3's tables must be read as
self-reported rather than head-to-head.

## The two summary tables — to be filled once the section reports exist

Two tables closing this part, gathering the numbers scattered across Part III so a
reader can see the whole field at once. **Numbers are deliberately not entered
yet** — they should be transcribed from the per-section reports, once written, so
each cell has a report behind it rather than being re-extracted from papers here.

**The risk to design against.** Everything else in this part argues these numbers
are *not* comparable. A tidy side-by-side table is read as a leaderboard, which is
the exact misreading Part IV and the intro's two caveats exist to prevent. So the
tables must make their own construction visible: **the provenance columns are not
decoration, they are the point.** A cell without a stated benchmark, cutoff and
measurer does not go in.

### Table A — structure prediction accuracy

*Rows:* the predictors of §1, §3, §4, §7, §8 — AlphaFold2/3, AlphaFold-Multimer,
OpenDDE, OpenFold3, Boltz-1/2, Chai-1, Protenix-v1/v2, ESMFold/ESMFold2, and the
RoseTTAFold pair from §2 for the historical baseline.

*Columns:* model · benchmark and version · training cutoff · target class ·
metric · **who measured it**.

*Target class is the axis that matters,* not a single aggregate score. Split at
minimum into monomer, protein-protein, **antibody-antigen**, protein-ligand,
protein-nucleic. Antibody-antigen carries the most weight of the five: most
systems in §3–§8 design antibodies or nanobodies, so antibody-antigen prediction
accuracy is the accuracy their critics actually run on. A model that leads on
monomers and trails on antibody-antigen is a weak critic for this review's
purposes, and only a split table shows that.

*The "who measured it" column earns its place here* because the corpus contains
genuine third-party measurement — OpenDDE's antibody-antigen head-to-head and
Protenix-v2's baseline runs of OpenFold3 and others. Self-reported and
independently-run numbers should be visually distinguishable, since that
distinction is Beat 5's whole argument arriving early.

### Table B — quality of generated binders

*Rows:* the design systems — RFdiffusion, RFantibody, BoltzGen, BoltzProt-1,
PXDesign-d/h, Protenix-v2 design, Chai-2, the flow-matching five, BindCraft,
BoltzDesign1, Germinal, the ESMFold2 campaign, AlphaProteo, Latent-X1/X2.

*Columns:* system · coupling level · target class and count · **designs tested per
target** · **hit definition** · assay · hit rate · affinity reached · targets
self-chosen?

**Sort by designs-tested, not by hit rate.** Beat 3's thesis is that the measure
of progress is how few designs you must make to get a binder, so the denominator
is the argument and the hit rate is secondary. Sorting by hit rate would silently
convert the table into the leaderboard we are trying not to publish.

**The hit-definition column is mandatory and is the reason this table is hard.**
BoltzProt-1 (§3) separates *screening hits* from *confirmed binders* and states
that screening hits are *"what prior binder design model literature typically
reports as binders"*. Its own two numbers, 3.3% and 8.0%, are confirmed-binder
rates. Percentages elsewhere in this map are on the looser definition. Without
that column the table would compare two different events and call it progress.

**What the pair says when placed together, and the reason to keep them adjacent:**
Table A has a benchmark column that can be filled — FoldBench, PXM, PoseBusters
are shared instruments run across models. Table B has no such column, because
**there is no shared benchmark for binder design at all**; every campaign chose its
own targets, assays and hit definition. The prediction half of this field is
measured, the design half is self-reported, and setting the two tables side by
side demonstrates that in a way no paragraph does. That asymmetry is the finding —
it should be stated in the text between them, and it is the strongest empirical
support Beat 5 has.

---

# PART V — EXAMINED AND EXCLUDED

**A publication is either included or excluded, never both.** Everything below is
excluded and appears nowhere in Parts I–IV; anything included carries its own
caveats, borderline calls and scope reasoning inside its section entry, and is not
restated here.

Sources retrieved, parsed into `literature/corpus/`, and then judged out of
scope. Recorded rather than deleted: an exclusion with a stated reason is part of
the review's method, and keeping them prevents re-litigating the same decision
later. All remain in `refs.bib` — the catalog tracks what was
obtained, the map tracks what is in scope.

**Scope rule applied:** in scope = generates a **protein or peptide binder
conditioned on a target**. Out of scope = a different modality (small molecules),
or sequence generation with no target conditioning.

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

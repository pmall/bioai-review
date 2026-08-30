# Literature Map

> This is the living, free-form entry point of the review. Maintain it together:
> concepts and their references, as loose and project-specific as the field needs.
> Default working file for review discussion.
>
> **Organization.** Five sections, in the order the final review will read:
> (1) structure prediction models; (2) the RoseTTAFold → RFdiffusion lineage,
> kept whole because its predictors and generators are the same architecture,
> and carrying ProteinMPNN/LigandMPNN so the sequence-design stage is introduced
> early; (3) other generative systems that use a predictor only as a filter;
> (4) the systems that backpropagate through the predictor; (5) benchmarking and
> validity infrastructure. A publication may appear in more than one section —
> many are both a predictor and a design engine — and is written in full where it
> is primarily reviewed, with a back-reference elsewhere.
>
> **Coupling levels** (see `literature/reports/structure_prediction_family_overview.md` §1.1):
> **Level 0** the generator *is* a repurposed predictor (inherited weights);
> **Level 1** generate, then filter with a predictor's confidence (no gradient);
> **Level 2** backpropagate the predictor's loss into the design variable.
> Level 0 is an attribute of an entry, not a section: every Level-0 system also
> filters, so inherited generators are grouped under Level 1 and marked *(inherits …)*.
>
> **Map ↔ catalog invariant.** Every concept resolves to exactly one place: its own
> `refs.bib` entry (it has a citable publication), a `keywords` tag on the paper that
> describes it, or the map alone (no citable publication). Entries with a publication
> carry their **bib key** and **DOI** inline so the mapping can be checked
> mechanically in both directions. Concepts with no publication are marked
> *map-only* with the reason. `refs.bib` is only edited through the `map-to-bib` skill.
>
> Scope: this field (AI-assisted drug discovery) moves very fast — explosive in
> 2026. References dated before 2025 are generally out of scope, except when they
> belong to an active lineage, whose full history is kept for complete
> understanding (e.g. the ESM family: ESM2/ESMFold → ESM3 → ESMC).

## **SECTION 1: STRUCTURE PREDICTION MODELS**

Predictive architectures solving the forward problem: sequence / chemical input → 3D structural state. Reviewed in `literature/reports/structure_prediction_family_overview.md`.

### **1.1 All-atom multi-entity co-folding**

* **AlphaFold2** — `alphafold2` · `10.1038/s41586-021-03819-2`
  * *Role:* Single-chain and multimer predictor that established modern deep-learning structural biology; the MSA-as-coevolution bet every later model inherits or reacts against.
  * *Links:* [Nature](https://doi.org/10.1038/s41586-021-03819-2) | [GitHub](https://github.com/google-deepmind/alphafold)
  * *Also used as:* the differentiable objective inside BindCraft (§4) and the standard post-hoc filter across §3.
  * *Map-only relative:* AlphaFold-Multimer (2021 preprint; pre-2025, kept as context).
* **AlphaFold3** — `alphafold3` · `10.1038/s41586-024-07487-w`
  * *Role:* All-atom diffusion predictor for protein / nucleic-acid / small-molecule / ion complexes. Closed weights — the stated motivating gap behind Boltz-1, Protenix and OpenFold3.
  * *Links:* [Nature](https://doi.org/10.1038/s41586-024-07487-w) | [GitHub](https://github.com/google-deepmind/alphafold3)
* **Boltz-1** — `boltz1` · `10.1101/2024.11.19.624167`
  * *Role:* First fully open (MIT) AF3-class co-folder; Boltz-1x adds Feynman-Kac inference-time steering for physical validity. Source of this project's only independent cross-model physical-validity measurements.
  * *Links:* [bioRxiv](https://doi.org/10.1101/2024.11.19.624167) | [GitHub](https://github.com/jwohlwend/boltz)
* **Boltz-2** — `boltz2` · `10.1101/2025.06.14.659707`
  * *Role:* Adds a binding-affinity module (approaching FEP accuracy at >1000× lower cost), MD-ensemble conditioning, and the most complete conditioning system in the corpus (method, multimeric templates, contacts/pockets, each with optional hard steering).
  * *Link:* [bioRxiv](https://doi.org/10.1101/2025.06.14.659707)
  * *Caveat:* benchmark numbers carry a temporal-leakage caveat flagged independently by ESMC, Protenix-v1 and Protenix-v2.
* **Protenix-v1** — `protenix_v1` · `10.64898/2026.02.05.703733`
  * *Role:* ByteDance Seed's open all-atom model matching AF3 under matched cutoff/scale/inference budget; adds RNA MSAs and protein templates; contributes the common-intersection critique of FoldBench (§3).
  * *Links:* [bioRxiv](https://doi.org/10.64898/2026.02.05.703733) | [GitHub](https://github.com/bytedance/Protenix)
  * *Predecessor, map-only:* the 2024/2025 *Protenix — advancing structure prediction through a comprehensive AlphaFold3 reproduction* technical report, describing Protenix v0.2.0/v0.5.0. Cited as ref 19 by Protenix-v1; not cataloged, not in the corpus.
* **Protenix-v2** — `protenix_v2` · `10.64898/2026.04.10.717613`
  * *Role:* Prediction half — 9–13 point antibody-antigen gains over v1, 5-seed performance exceeding v1 at 1000 seeds, and the finding that the PoseBusters criterion is itself incomplete (extended in PXMeter v1.1.0). Design half in §3.1.
  * *Link:* [bioRxiv](https://doi.org/10.64898/2026.04.10.717613)
* **Chai-1** — `chai1` · `10.1101/2024.10.10.615955`
  * *Role:* AF3-derivative adding a protein-LM track alongside the MSA track (either usable alone) and experimentally-grounded constraint features (pocket, contact, docking). The partial-MSA-emancipation hinge.
  * *Links:* [bioRxiv](https://doi.org/10.1101/2024.10.10.615955) | [GitHub](https://github.com/chaidiscovery/chai-lab)
* **OpenDDE** — `opendde` · `10.48550/arXiv.2607.03787`
  * *Role:* Apache-2.0 all-atom co-folding foundation model with atomic latent reasoning; reports IsoDDE-level accuracy, a cross-model scaling law, and the corpus's most complete third-party antibody-antigen head-to-head. Design is roadmap only — explicitly *"not a complete drug-discovery system"*.
  * *Links:* [arXiv](https://arxiv.org/abs/2607.03787) | [GitHub](https://github.com/aurekaresearch/OpenDDE)
* **OpenFold lineage (OpenFold → OpenFold3)**
  * *Role:* AlQuraishi Lab's open reimplementations — OpenFold reproduces AlphaFold2 (and supplies the distillation set Boltz-1 trains on); OpenFold3-preview targets bitwise AF3 reproduction.
  * *Links:* [OpenFold3 GitHub](https://github.com/aqlaboratory/openfold-3) | [OpenFold GitHub](https://github.com/aqlaboratory/openfold)
  * *(map-only — code releases, no paper or DOI. Third-party benchmark numbers exist: run as a baseline by Protenix-v2 and OpenDDE.)*
* **IsoDDE (Isomorphic Labs, 2025/2026)**
  * *Role:* Private frontier drug-design engine. Appears in this project only as a reference level on OpenDDE's scaling curve — the sole quantitative handle available.
  * *Link:* [Isomorphic Labs](https://www.isomorphiclabs.com/)
  * *(map-only — private, no publication; too heavy to ignore.)*
* **Chai-3 (2026)** and **SeedFold**
  * *Role:* Chai-3 — high-throughput commercial 3D foundation model. SeedFold — appears only as a point on OpenDDE's scaling curve.
  * *Link:* [Chai Discovery platform](https://lab.chaidiscovery.com/)
  * *(map-only — no publication, no DOI.)*

### **1.2 Language-model structure predictors**

* **ESM-2 & ESMFold** — `esm2` · `10.1126/science.ade2574`
  * *Role:* Founding single-sequence predictor — structure emerges from masked-LM scaling alone, no MSA or templates at inference. Enabled the ESM Metagenomic Atlas (>617M predicted structures; the Atlas itself is a database, out of scope).
  * *Link:* [Science](https://doi.org/10.1126/science.ade2574)
* **ESMC & ESMFold2** — `esmc` · `10.64898/2026.06.03.729735`
  * *Role:* Biohub/EvolutionaryScale's ~2.8B-sequence LM plus a folding head on its frozen representations. Full MSA emancipation: single-sequence antibody-antigen accuracy exceeding AF3-with-MSA, with a detachable MSA encoder kept only as a rescue path for high-perplexity sequences. Also the Level-2 design engine in §4.
  * *Links:* [bioRxiv](https://doi.org/10.64898/2026.06.03.729735) | [Biohub release](https://biohub.org/news/world-model-of-protein-biology/)
  * *Covers:* ESMFold2 and ESMFold2-Fast (modules of this release, no separate paper).

### **1.3 Protein language models without a folding head**

* **ESM-3** — `esm3` · `10.1126/science.ads0018`
  * *Role:* Multimodal promptable PLM tokenizing sequence, structure and function in parallel tracks. Reviewed inside the ESM section of the final review (§7 of the plan below) as a lineage step, not as a competitor on folding accuracy.
  * *Link:* [Science](https://doi.org/10.1126/science.ads0018)

## **SECTION 2: THE ROSETTAFOLD → RFDIFFUSION LINEAGE**

The Baker Lab / IPD line, kept whole: two structure predictors and the four generative models fine-tuned from them, plus the sequence-design stage the whole field borrowed. Reviewed together in `literature/reports/rfdiffusion_family_summary.md` and `literature/reports/proteinmpnn_ligandmpnn_summary.md`.

Grouped this way for two reasons. **The architecture is the lineage** — RFdiffusion is a fine-tuned RoseTTAFold, RFdiffusionAA a fine-tuned RFAA — so parent and descendant belong together; this is Level 0 coupling in its purest form, one architecture serving prediction or generation depending on what it is fine-tuned for. And **as predictors these have left the conversation**: mentions per co-folding paper run AlphaFold3 25, Chai-1 11, then Boltz-1, Boltz-2, Protenix-v1, Protenix-v2, OpenDDE and ESMC/ESMFold2 all **zero**. Nothing published since 2024 benchmarks against them.

### **2.1 The predictors it grew from**

* **RoseTTAFold (RF1)** — `rosettatfold` · `10.1126/science.abj8754`
  * *Role:* Three-track (1D/2D/3D) network developed independently of AF2; complex prediction emerged untrained from two-segment cropping. The architecture the whole RFdiffusion family is fine-tuned from.
  * *Link:* [Science](https://doi.org/10.1126/science.abj8754)
  * *Intermediate steps, map-only:* RoseTTAFoldNA and RoseTTAFold2 (preprints; RF2 is RFAA's base network).
* **RoseTTAFold All-Atom (RFAA)** — `rosettatfold_all_atom` · `10.1126/science.adl2528`
  * *Role:* All-atom generalization published two months *before* AF3 and independently of it; encodes chirality as architectural input features rather than as a loss or a post-hoc penalty. No diffusion module in the predictor.
  * *Link:* [Science](https://doi.org/10.1126/science.adl2528)

### **2.2 The generative models**

* **RFdiffusion** — `rfdiffusion` · `10.1038/s41586-023-06415-8` *(inherits RoseTTAFold)*
  * *Role:* SE(3)-equivariant frame diffusion; established modern generative backbone design. Filtered by AF2 pAE/"in silico success".
  * *Links:* [Nature](https://doi.org/10.1038/s41586-023-06415-8) | [GitHub](https://github.com/RosettaCommons/RFdiffusion)
  * *Reviewed in* `literature/reports/rfdiffusion_family_summary.md`.
* **RFdiffusion2** — `rfdiffusion2` · `10.1038/s41592-025-02975-x` *(inherits RoseTTAFold)*
  * *Role:* Atom-level enzyme active-site scaffolding from functional-group positions, sequence-agnostic.
  * *Link:* [Nature Methods](https://doi.org/10.1038/s41592-025-02975-x)
* **RFdiffusion3** — `rfdiffusion3` · `10.1101/2025.09.18.676967` *(inherits RoseTTAFold)*
  * *Role:* Transformer-based all-atom diffusion across proteins, DNA, RNA and ligands; inherits AF3's non-equivariant diffusion approach.
  * *Links:* [bioRxiv](https://doi.org/10.1101/2025.09.18.676967) | [IPD announcement](https://www.ipd.uw.edu/2025/12/rfdiffusion3-now-available/)

### **2.3 Sequence design and inverse folding — introduced here, used everywhere**

* **ProteinMPNN** — `proteinmpnn` · `10.1126/science.add2187` · and **LigandMPNN** — `ligandmpnn` · `10.1038/s41592-025-02626-1`
  * *Role:* Autoregressive message-passing networks generating sequences for a fixed backbone (and ligand / nucleic-acid environment, for LigandMPNN). The standard inverse-folding stage between backbone generation and structural validation.
  * *Links:* [Science (ProteinMPNN)](https://doi.org/10.1126/science.add2187) | [Nature Methods (LigandMPNN)](https://doi.org/10.1038/s41592-025-02626-1) | [GitHub](https://github.com/dauparas/ProteinMPNN)
  * *Reviewed in* `literature/reports/proteinmpnn_ligandmpnn_summary.md`.
  * *Lineage:* Baker Lab, same origin as RoseTTAFold (§2.1) and the RFdiffusion family (§2.2) — but adoption is field-wide, not lineage-bound. Corpus papers referencing it: RFdiffusion3 (27 mentions), BoltzGen (14), RFdiffusion (10), RFdiffusion2 (6), RFAA (5), Latent-X1 (5), PXDesign (5), BindCraft (5), PPIFlow (4), AtomFlow (3), AlphaProteo (3), FrameFlow (2), D-Flow (2), OriginFlow (2), SaProt (2). Nine distinct labs, both coupling levels.

## **SECTION 3: OTHER BINDER GENERATION SYSTEMS — ALL LEVEL 1**

Generative systems solving the inverse problem: target → novel binder. Everything outside the RoseTTAFold lineage of §2 that uses a predictor **only as a post-hoc critic** — generate first, then predict the complex and filter on confidence (ipTM, pAE, pLDDT, or refolding RMSD). The predictor never sees a gradient; systems that do get one are in §4.

Subsections run by *generative mechanism*, in the order the review will present them: diffusion first (continuing directly from §2's RFdiffusion), then flow matching, then the outliers. Entries marked *(inherits …)* are also Level 0 — the generator's weights descend from a predictor in §1.

Sequence design for most systems here is ProteinMPNN/LigandMPNN, introduced in §2 with the lineage that produced it.

### **3.1 Diffusion**

All four descend from a co-folding predictor in §1, so they are Level 0 as well as Level 1 — the diffusion module is the predictor's own, repurposed for generation.

* **BoltzGen** — `boltzgen` · `10.1101/2025.11.20.689494` *(inherits Boltz)*
  * *Role:* Unified generative design across proteins, peptides, nanobodies, antibodies and small molecules. Filters 10,000-design pools by refolding with Boltz-2 (RMSD < 2.5 Å) plus a composite interaction score.
  * *Links:* [bioRxiv](https://doi.org/10.1101/2025.11.20.689494) | [GitHub](https://github.com/jwohlwend/boltz)
* **PXDesign (PXDesign-d)** — `pxdesign` · `10.1101/2025.08.15.670450` *(inherits Protenix)*
  * *Role:* Diffusion arm of the PXDesign platform, plus a systematic study of confidence-based filtering. Finds Protenix and AF2-IG filters retain *different* true positives with limited overlap — an argument for ensembling critics.
  * *Links:* [bioRxiv](https://doi.org/10.1101/2025.08.15.670450) | [GitHub](https://github.com/bytedance/Protenix)
* **Protenix-v2 (design half)** — `protenix_v2` · `10.64898/2026.04.10.717613` *(inherits Protenix)*
  * *Role:* Target-conditioned generation with epitope-specific or site-agnostic modes across miniproteins, VHH and Fv; per-CDR length control and scaffold specification. 100% target-level success in novelty-controlled VHH-Fc campaigns; GPCR hit rates 16–88%. Prediction half in §1.1.
* **Chai-2** — `chai2` · `10.1101/2025.07.05.663018` *(inherits Chai-1, via a "Chai-1d" design prototype)*
  * *Role:* Zero-shot antibody design; ~16% wet-lab hit rate in 24-well-plate assays across 52 unbiased targets.
  * *Link:* [bioRxiv](https://doi.org/10.1101/2025.07.05.663018)

### **3.2 Flow matching**

Presented in these papers as the successor to diffusion rather than an alternative to it — FrameFlow explicitly recasts the earlier FrameDiff model as SE(3) flow matching and reports 2× designability at 5× fewer sampling steps. All five here generate **protein or peptide binders conditioned on a target** — the scope of this review. Flow-matching papers that generate small molecules, or sequences with no target conditioning, are recorded in §6 instead. None of these five has had its dedicated report yet.

* **FrameFlow** — `frameflow` · `10.48550/arXiv.2310.05297`
  * *Role:* Recasts FrameDiff as SE(3) flow matching — 2× designability at 5× fewer sampling steps. Methodological ancestor of much of this subsection.
  * *Link:* [arXiv](https://arxiv.org/abs/2310.05297)
* **PPIFlow** — `ppiflow` · `10.64898/2026.01.19.700484`
  * *Role:* SE(3) flow matching with in-silico maturation for picomolar/nanomolar binders and single-domain antibodies.
  * *Link:* [bioRxiv](https://doi.org/10.64898/2026.01.19.700484)
* **OriginFlow** — `originflow` · `10.1101/2025.04.29.651154`
  * *Role:* Combined SDE and flow-matching framework for functional binder design; reports 90% wet-lab hit rates across PD-L1, RBD and VEGF.
  * *Link:* [bioRxiv](https://doi.org/10.1101/2025.04.29.651154)
* **AtomFlow** — `atomflow` · `10.48550/arXiv.2409.12080`
  * *Role:* Atomic flow matching on unified biotokens; generates ligand-binding pockets directly from 2D molecular graphs, without bound conformers.
  * *Link:* [arXiv](https://arxiv.org/abs/2409.12080)
* **D-Flow** — `dflow` · `10.1109/JBHI.2026.3683934`
  * *Role:* Full-atom flow matching on SE(3) frames and torus manifolds for bioorthogonal D-peptide binders.
  * *Link:* [IEEE JBHI](https://doi.org/10.1109/JBHI.2026.3683934) (preprint: [arXiv](https://arxiv.org/abs/2411.10618))

### **3.3 Architecture not disclosed**

Two of the strongest published wet-lab results in this map come from systems whose generative mechanism is not described. Recorded as its own category rather than guessed at.

* **AlphaProteo** — `alphaproteo` · `10.48550/arXiv.2409.08022`
  * *Role:* DeepMind generative engine plus a multi-stage filter for picomolar/nanomolar binders. Defines in-silico success as *"interchain AF2 pAE < 10, binder-aligned binder RMSD < 1 Å, pLDDT > 80"* — the canonical statement of the Level-1 criterion.
  * *Links:* [arXiv](https://arxiv.org/abs/2409.08022) | [DeepMind blog](https://deepmind.google/discover/blog/alphaproteo-generates-novel-proteins-for-biological-research/)
* **Latent-X1** — `latentx1` · `10.48550/arXiv.2507.19375` · and **Latent-X2** — `latentx2` · `10.48550/arXiv.2512.20263`
  * *Role:* Latent Labs' atom-level binder design platform — macrocycles and minibinders (X1), then drug-like low-immunogenicity antibodies validated in human panels (X2). Filters on ipTM/pAE and self-consistency.
  * *Links:* [Latent-X1 arXiv](https://arxiv.org/abs/2507.19375) | [Latent-X2 arXiv](https://arxiv.org/abs/2512.20263)
  * *Note:* the one design lineage in this map with no predictor parent in §1.

## **SECTION 4: LEVEL 2 — THE BACKPROPAGATION LOOP**


Gradients flow through a structure predictor into the design variable. The smallest group in this map — four systems — and, on the evidence, a deliberate cohort: PXDesign benchmarks itself head-to-head against exactly BindCraft and BoltzDesign, so the field treats these as one category.

**The arc to carry into the review: tried early, abandoned for diffusion, revived once predictors got good enough — and now portable across predictor families.**

1. *Tried early.* Constrained *hallucination* — optimizing a sequence through RoseTTAFold until it predicts the target fold — was the Baker lab's approach before RFdiffusion.
2. *Abandoned.* RFdiffusion's own paper reports beating it: *"RFdiffusion significantly outperforms Hallucination (with RF) at unconditional monomer generation"* (z = 9.5, P = 1.6 × 10⁻⁹). Diffusion won, and Level 2 went quiet.
3. *Revived.* It returns on predictors strong enough to be run single-sequence without falling off-distribution — the precondition argued in `structure_prediction_family_overview.md` §1.2.
4. *Portable.* Correia and Ovchinnikov have now demonstrated the same inversion on AlphaFold2 (BindCraft) and on Boltz (BoltzDesign1), while ByteDance did it on Protenix and Biohub on ESMFold2 — four systems, three groups, four different predictor families. Evidence the method is general rather than an AF2 quirk.

Do not present Level 2 as simply the newest thing; it is the oldest idea in the section, returning under conditions that did not previously hold.

* **BindCraft** — `bindcraft` · `10.1038/s41586-025-09429-6`
  * *Role:* Backpropagates through AF2-multimer weights to produce an *L*×20 error gradient over amino-acid choices, annealed in four stages from continuous logits to one-hot. Target flexibility retained; no separate scaffolding step.
  * *Link:* [Nature](https://doi.org/10.1038/s41586-025-09429-6)
  * *Predictor:* AlphaFold2 (§1.1), run single-sequence for the designed chain — off-distribution for AF2, which the multi-stage annealing and 5-model ensembling appear to compensate for.
* **ESMFold2 binder design campaign** — covered by `esmc` · `10.64898/2026.06.03.729735`
  * *Role:* *"Represents sequences as continuous distributions over amino acid probabilities and optimizes by backpropagation through ESMC and ESMFold2"* — gradients pass through the 6B language model as well as the folding head, and a **single-stage** optimization suffices. Minibinders and scFvs against five oncology/immunology targets; BLI-validated hit rates rising with compute.
  * *Predictor:* ESMC/ESMFold2 (§1.2) — single-sequence is its native regime, so no off-distribution penalty.
  * *(module of the ESMC release — no separate publication.)*
* **PXDesign-h** — covered by `pxdesign` · `10.1101/2025.08.15.670450`
  * *Role:* The hallucination-based arm of PXDesign, built on the Protenix predictor. Its diffusion arm (PXDesign-d) is Level 1, in §3.1.
  * *Predictor:* Protenix (§1.1).
* **BoltzDesign1** — `boltzdesign1` · `10.1101/2025.04.06.647261`
  * *Role:* Inverts the Boltz all-atom predictor for generalized binder design — the same inversion idea as BindCraft, moved from AlphaFold2 to Boltz.
  * *Link:* [bioRxiv](https://doi.org/10.1101/2025.04.06.647261)
  * *Predictor:* Boltz-1/2 (§1.1).
  * *Lineage:* Cho, Pacesa, Zhang, **Correia** and **Ovchinnikov** — the last two are also BindCraft's senior authors, so two of the four Level-2 systems come from one group porting the approach across predictors. Worth treating as one research programme, not two independent data points.
  * *(In the corpus, not yet reviewed in depth. Cited by six other corpus papers: PXDesign, RFdiffusion3, Latent-X1, Boltz-2, BoltzGen, ESMC.)*

## **SECTION 5: BENCHMARKING, VALIDITY & EVALUATION INFRASTRUCTURE**

Test suites, benchmark sets and constraint modules used to evaluate and repair predicted or generated structures. Not models — but the numbers every claim in Sections 1 and 2 is denominated in.

* **PoseBusters** — `posebusters` · `10.1039/D3SC04185A`
  * *Role:* 18-check physical/chemical validity suite (RDKit) plus a benchmark set; source of the "PB-valid" metric reported by AF3, Chai-1, Boltz-1 and Protenix. Its own finding — that deep-learning docking did not beat classical tools on physical plausibility or generalization to novel sequences — concerns ligand docking, so it is a ligand-side instrument doing protein-side duty here.
  * *Links:* [Chemical Science](https://doi.org/10.1039/D3SC04185A) | [GitHub](https://github.com/maabuu/posebusters)
  * *Known limit:* Protenix-v2 shows the criterion is incomplete — structures pass it while still exhibiting twisted amides and distorted aromatics.
  * *(PoseBusters V2 — a benchmark-set revision, not a separate publication; map-only.)*
* **FoldBench** — `foldbench` · `10.1038/s41467-025-67127-3`
  * *Role:* Peer-reviewed all-atom prediction benchmark spanning monomers, protein-protein, antibody-antigen, protein-ligand and protein-nucleic interfaces; the shared evaluation set behind the AF3 / Protenix / Boltz / ESMFold2 / OpenDDE comparisons.
  * *Link:* [Nature Communications](https://doi.org/10.1038/s41467-025-67127-3)
  * *Known limit:* Protenix-v1 shows its published aggregates do not enforce a common intersection of successfully-evaluated targets, so coverage differences alone can flip model rankings.
* **PXMeter** — `pxmeter` · `10.1101/2025.07.17.664878`
  * *Role:* Open evaluation toolkit and artifact-filtered dataset; basis of the PXM benchmark family. v1.1.0 extends PoseBusters with sp2-planarity, amide-planarity and sp3-non-planarity checks.
  * *Links:* [bioRxiv](https://doi.org/10.1101/2025.07.17.664878) | [GitHub](https://github.com/bytedance/PXMeter)
* **Gauss-Seidel projection** — `gauss_seidel_projection` · `10.48550/arXiv.2510.08946`
  * *Role:* A differentiable projection mapping provisional diffusion coordinates to the nearest physically valid configuration, via a Gauss-Seidel scheme exploiting constraint sparsity; integrates into existing predictors for end-to-end fine-tuning. Enforces validity as a *strict constraint* rather than a bias, which the paper argues inference-time steering (Boltz-1x) cannot guarantee. Two denoising steps suffice.
  * *Link:* [arXiv](https://arxiv.org/abs/2510.08946) (ICLR 2026)
  * *Note:* a fifth distinct response to the inherited physical-validity problem, alongside re-ranking, steering, architectural chirality features and fixing the metric.

## **SECTION 6: EXAMINED AND EXCLUDED**

Sources retrieved, parsed into `literature/corpus/`, and then judged out of scope. Recorded here rather than deleted, per PRISMA: an exclusion with a stated reason is part of the review's method, and keeping them prevents re-litigating the same decision later. All remain in `refs.bib` — the catalog tracks what was obtained, the map tracks what is in scope.

**Scope rule applied:** in scope = generates a **protein or peptide binder conditioned on a target**. Out of scope = generates a different modality (small molecules), or generates sequences with no target conditioning.

* **moPPIt** — `moppit` · `10.1101/2024.07.31.606098`
  * *Excluded:* method is an outlier with no lineage in this review — a genetic algorithm iterating a pool from the PepMLM peptide language model, scored by BindEvaluator (an ESM-2 binding-site predictor) plus perplexity. No diffusion, no flow matching, no structure input at all; AlphaFold2-Multimer appears only as retrospective validation. Target-conditioned, so it passes the scope rule, but it shares no machinery with anything else here and is cited by no other paper in the corpus.
  * *Note:* an earlier version of this map described moPPIt as discrete flow matching. That was wrong — worth recording so the error is not reintroduced.
  * *Link:* [bioRxiv](https://doi.org/10.1101/2024.07.31.606098)
* **DrugFlow** — `drugflow` · `10.48550/arXiv.2508.17815` · and **FLOWR** — `flowr` · `10.1038/s43588-026-00998-8`
  * *Excluded:* wrong modality. Both are pocket-conditioned **small-molecule** generators, producing 3D atom types, coordinates and bond topology for a ligand. Structure-based drug design rather than binder design; the overlap with this review is the flow-matching machinery, not the problem.
  * *Links:* [DrugFlow arXiv](https://arxiv.org/abs/2508.17815) | [FLOWR Nature Comp. Sci.](https://doi.org/10.1038/s43588-026-00998-8)
* **ProtFlow** — `protflow` · `10.64898/2026.02.14.705870`
  * *Excluded:* not binder design. Rectified flow matching in sequence space for general protein engineering — antimicrobial peptides and functional sequence generation, learning the global semantic distribution of protein space. The words "binder" and "binding" do not appear anywhere in the paper, and there is no target conditioning.
  * *Link:* [bioRxiv](https://doi.org/10.64898/2026.02.14.705870)

* **SaProt** — `saprot` · `10.1101/2023.10.01.560349`
  * *Excluded:* a structure-aware protein language model (Foldseek 3Di alphabet, 441 tokens) with no folding head and no generative binder capability. It neither predicts 3D structure nor designs binders, so it sits outside both halves of this review, and it belongs to no lineage tracked here. Cited by one other corpus paper.
  * *Link:* [bioRxiv](https://doi.org/10.1101/2023.10.01.560349)

**Borderline, currently kept in §3.2:** **D-Flow** (`dflow`) designs *D*-peptides — mirror-image peptides built from D-amino acids, an exotic chemistry — but it is explicitly *"conditioned on receptor binding"* for *"de novo D-peptide design"*, so by the scope rule above it is binder design and stays. Flag it if you want the modality out too.


---

## **PLAN: INTRODUCTION NARRATIVE**

The intro's job is to make the nine sections feel inevitable rather than enumerated. Five beats, each ending where the next begins.

### **Beat 1 — Scope: protein and peptide binders**

State the modality up front: this is a review of designing **proteins and peptides that bind a chosen target**, not of small-molecule drug design. Antibodies, nanobodies, VHH, scFvs, minibinders and macrocyclic peptides are in; of everything catalogued here only DrugFlow and FLOWR generate small molecules, and both are recorded as out of scope in §6.

Two reasons to give, and they are better than "that is where the papers are".

- **Small molecules are brittle in a way sequences are not.** Potency can collapse on a single-atom change — the activity-cliff problem — so a generator must land in exactly the right place rather than a good neighbourhood. The corpus states the difficulty from the evaluation side: Boltz-2 frames its affinity work around *"distinguishing subtle differences in binding affinity among closely related analogues"*, which is precisely the regime where small perturbations are not small. A protein binder's affinity degrades far more gracefully across nearby sequences, which is what makes iterative generate-and-filter workable at all.
- **Sequences are differentiable; molecular graphs are not.** This is the deeper reason, and it is what connects Beat 1 to Beat 4. A protein sequence relaxes cleanly into a continuous distribution over 20 amino acids per position — every point in that simplex is a valid input, so a Level-2 loop can backpropagate straight through it (BindCraft's *L*×20 gradient; ESMFold2's continuous amino-acid distributions). A molecule is a variable-size graph with hard valence and bonding constraints, and most continuous relaxations of it are simply not molecules. The corpus shows the field working around this rather than solving it: **DrugFlow** pairs continuous flow matching for coordinates with **discrete Markov bridges** for atom and bond types; **FLOWR** uses a *"mixed continuous and categorical"* scheme for the same reason. Separate discrete machinery is needed exactly where proteins need none. Whether a Level-2 loop is achievable for small molecules is an open question this review does not try to settle — but the asymmetry is real, and it justifies the scope.

### **Beat 2 — The founding bet, and the problem that got solved**

Structure prediction was the prerequisite, and it was solved on the back of a single wager: **coevolution in a multiple sequence alignment is a usable proxy for spatial contact.** AlphaFold2 cashed it — median 0.96 Å backbone accuracy on CASP14 against 2.8 Å for the next best method — and AlphaFold3 generalised it to arbitrary complexes. This is where the MSA thread starts; it must be planted here because it pays off in Beat 4.

Close the beat on the limitation that matters: a predictor tells you what a *given* sequence folds into. It does not tell you which sequence to try.

### **Beat 3 — Why prediction was not enough: the experimental budget**

The honest motivation for generative design is not the size of sequence space in the abstract — it is that **you cannot screen your way to a binder**. Anchor it in the papers' own framing, and make the collapsing experimental budget the review's quantitative spine:

| Era | Designs tested per target | Source |
|---|---|---|
| Screening-based, and early computational design | *"thousands to millions of designs to reliably identify hits"* | Chai-2's characterisation of prior work |
| Current generative + filtering | 16–30 (Protenix-v2), ≤20 (Chai-2), 30–100 (Latent-X), 84 (ESMFold2) | each system's own campaign |

Hit rates now reported in the same papers — 16% (Chai-2, de novo antibodies), up to 48% and 16–88% on GPCRs (Protenix-v2 VHH-Fc), >90% (Latent-X macrocycles), 70% (ESMFold2 minibinders) — make the point sharper than any statement about combinatorics. **The measure of progress in this field is how few designs you must make to get a binder.** Sections 2–9 are, read one way, a history of that number falling.

**Worth one sentence here: the machinery was borrowed from image generation, and the field said so.** RFdiffusion's paper introduces the technique as *"denoising diffusion probabilistic models (DDPMs), a powerful class of machine learning models recently demonstrated to generate new photorealistic images in response to text"*, trained to denoise *"data (for instance, images or text)"*. So the parallel is the field's own, not a populariser's, and it earns its place twice over: it orients any reader who has met Stable Diffusion, and it explains the formalism shift in section 5 — image generation made the same diffusion → flow-matching move, for the same reasons of sampling speed and simplicity.

Then turn it, because the analogy breaks exactly where this field gets interesting: **image generation has no AlphaFold.** There is no differentiable oracle that scores whether a generated image is *correct*, so image models are judged by human preference and cannot close a loop on their own objective. Protein design can, and that is the entire subject of Beat 4. The borrowed machinery is the easy half; the critic is the part with no counterpart in the source field.

### **Beat 4 — Closing the loop, and why MSA emancipation was the precondition**

Generators need a critic, and the critic is a structure predictor. That gives the review its spine — the coupling levels defined in the header of this map:

- **Level 0** the generator *is* a repurposed predictor;
- **Level 1** generate, then filter on the predictor's confidence — still the field's default, and the origin of the standard success criterion (AlphaProteo: *"interchain AF2 pAE < 10, binder-aligned binder RMSD < 1 Å, pLDDT > 80"*);
- **Level 2** backpropagate the predictor's loss into the sequence being designed.

Here the MSA thread from Beat 2 pays off, and it is the intro's one genuinely non-obvious claim: **an MSA is a database lookup on a sequence that does not exist yet.** It is neither differentiable nor defined for a binder being invented, so a Level-2 loop must run its predictor single-sequence on the designed chain. That is why BindCraft, hallucinating through AlphaFold2, operates the model in exactly the regime AF2's own paper documents as its weakest, and why ESMC/ESMFold2 — natively single-sequence — can backpropagate through a 6B-parameter language model without leaving distribution. **MSA emancipation is not an accuracy story; it sets the ceiling on how tightly a generator can couple to its critic.**

Close with the arc recorded in §4 of this map: Level 2 is the *oldest* idea here, tried as constrained hallucination, beaten by RFdiffusion, and now returning because the predictors finally support it — and portable across four predictor families.

### **Beat 5 — The closed frontier**

End on the limit of what a literature review can establish. The strongest claimed results increasingly come from systems that publish benchmarks and withhold mechanisms — AlphaProteo, Latent-X, Chai-2's generator, and IsoDDE, which has no publication at all and is visible only as the top point on a competitor's scaling curve. Note the symmetry that gives section 9 its force: **AlphaFold3 is a Google DeepMind *and Isomorphic Labs* paper**, so the review opens on the published half of that organisation's work and closes on the half that stopped publishing.

### **Two caveats the intro must plant, or the reader will over-read the tables**

1. **The numbers are not as comparable as they look.** Different benchmarks, different cutoffs, different target sets; FoldBench's published aggregates do not enforce a common intersection of evaluated targets, and Boltz-2's have a temporal-leakage caveat flagged independently by three teams. Point at the transversal benchmarking report rather than relitigating it in each section.
2. **Wet-lab hit rates are self-reported and target-dependent.** Every campaign chose its own targets, and the papers that disclose most about their methods are not the ones reporting the highest numbers — which is itself a finding, and Beat 5's justification.

---

## **PLAN: SECTION ORDER FOR THE FINAL REVIEW**

Per-lineage organization. Each section pairs a predictor with the design systems built on it, so a reader meets an architecture once and then follows it to its conclusion.

**Two axes, used in sequence.** Sections 2–6 are all Level 1 (predictor as filter), so within that block the ordering principle is the **generative formalism**: diffusion first, then flow matching as its successor, then the models that do not say. Sections 7–9 then escalate by **coupling depth** to Level 2. Stating this up front stops the order looking inconsistent halfway through.

| # | Section | Covers | Organizing fact |
|---|---|---|---|
| 1 | **AlphaFold, and the open co-folding cluster** | AlphaFold2, AlphaFold3; OpenFold/OpenFold3; OpenDDE | prediction only; everything later is defined relative to it |
| 2 | **RoseTTAFold → RFdiffusion** | RF1, RFAA; RFdiffusion 1/2/3; ProteinMPNN/LigandMPNN | diffusion; the first prediction→generation turn; introduces inverse folding |
| 3 | **Boltz** | Boltz-1, Boltz-2, BoltzGen | diffusion, stated outright: BoltzGen is *"a single all-atom diffusion model capable of performing both structure prediction and protein design"* |
| 4 | **Chai** | Chai-1, Chai-2 | Chai-1 is a diffusion co-folder; Chai-2's *generator* is undisclosed (see note) |
| 5 | **Flow matching** | FrameFlow, PPIFlow, OriginFlow, AtomFlow, D-Flow | the successor formalism — FrameFlow *"adapt[s] FrameDiff, a state-of-the-art diffusion model, to the flow-matching generative modeling paradigm"* |
| 6 | **Protenix** | Protenix-v1, Protenix-v2, PXDesign-d and PXDesign-h | first to ship *both* couplings — the bridge to Level 2 |
| 7 | **BindCraft and BoltzDesign1** | inversion as a portable technique | Level 2, one group, two different predictors |
| 8 | **ESM** | ESM-2/ESMFold, ESM-3, ESMC/ESMFold2 and its binder campaign | Level 2, fully integrated — the analytical climax |
| 9 | **The closed frontier** | AlphaProteo, Latent-X 1/2; IsoDDE, Chai-3, SeedFold | benchmarked but unexplainable — a coda, not a step in the argument |

**Why this order.**

- **1 first** because everything else reproduces AlphaFold, reacts to it, or replaces its evolutionary input. OpenFold3 and OpenDDE join it rather than getting their own sections: open co-folding models in the AF3 mould, with no design descendant to follow.
- **2 second** — the one architecture developed independently of AlphaFold, the first to make the generative turn, and the source of the inverse-folding stage every later section relies on.
- **3 and 4** keep the diffusion block together while each lineage stays whole. Boltz precedes Chai because BoltzGen states its mechanism plainly and demonstrates the Level-0 identity in its purest form — one diffusion model doing prediction *and* design.
- **5 after the diffusion sections, not before.** Flow matching only reads as a successor if the reader has already seen diffusion doing real work in sections 2–4. FrameFlow is literally FrameDiff reformulated, so the section can open by re-deriving something familiar rather than introducing a parallel formalism cold.
- **6, 7, 8 escalate coupling.** Protenix is the hinge: PXDesign-d inherits, PXDesign-h backpropagates. BindCraft and BoltzDesign1 then show the inversion is portable across predictor families (same group, AlphaFold2 and Boltz). ESM ends the *argument* as the only entry where language model, folding head and design loop are one system, and as the conclusion the MSA throughline has been building toward since section 1.
- **9 last, deliberately outside the argument.** These systems publish benchmarks but not mechanisms, so they cannot be analysed the way sections 1–8 analyse everything else — placing them earlier would interrupt an argument they cannot contribute to. Last, they work as a coda: here is the frontier, here is what it claims, and here is precisely how little can be said about it. It also closes a loop. **AlphaFold3 is a Google DeepMind *and Isomorphic Labs* paper** — Isomorphic authors are listed as core contributors — so the review opens on the published half of that organisation's work and closes on the half that stopped publishing.

**Section 9 has two tiers, and they are not the same problem.**

- *Published, results disclosed, mechanism withheld.* **AlphaProteo** describes only *"a generative model trained on structure and sequence data from the PDB and a distillation set of AlphaFold predictions"*. **Latent-X** credits *"our proprietary architecture"*. Both report strong wet-lab numbers that can be quoted but not attributed to any design choice.
- *No publication at all, known only through other people's benchmarks.* **IsoDDE** (Isomorphic Labs) is the frontier reference on OpenDDE's scaling curve, sitting at the top of it — credited with gains in protein-ligand generalisation, antibody-antigen interfaces, pocket identification and affinity estimation. OpenDDE states the limit plainly: *"we do not have access to its full training recipe, data mixture, inference procedure, post-training strategy, or engineering optimizations ... we cannot yet determine which differences arise from model architecture, data processing, scaling, distillation, or inference-time procedures."* **Chai-3** is a commercial web platform; **SeedFold** appears only as a point on the same curve. For all three, every number this review can cite was measured by a competitor.

**Note carried into section 4.** Chai-2's paper describes only its *folding* submodule (Chai-2f, *"a similar architecture as Chai-1"*); the generative mechanism is never stated. Non-disclosure therefore covers four of the strongest results here — Chai-2, AlphaProteo, Latent-X and IsoDDE. Chai-2 nonetheless stays in the Chai section: lineages are not fragmented by disclosure status, and the fact is reported there with a pointer to section 9.

**Transversal reference reports**, written once and cited from any section rather than placed in the sequence:

- **Structure prediction: lineages, critics and the road to design** — `literature/reports/structure_prediction_family_overview.md`. Already written; supplies the coupling-level framework (Level 0/1/2) and the MSA-emancipation throughline that every section refers to.
- **Benchmarking and physical validity** — PoseBusters, FoldBench, PXMeter, Gauss-Seidel projection (§5 of this map): the instruments every number is denominated in, plus their known limits — FoldBench's common-intersection problem, PoseBusters' incompleteness, and Boltz-2's temporal leakage flagged by three independent teams.

**Open question for the plan.** Section 5 is the weakest as a *story*: PPIFlow, OriginFlow, AtomFlow and D-Flow are each cited by zero other papers in this corpus (only FrameFlow, at 3, has traction as the methodological ancestor), so it will read as a survey of parallel isolated efforts rather than a lineage. Budget it as one combined report, not one per model.

# Literature Map

> This is the living, free-form entry point of the review. Maintain it together:
> concepts and their references, as loose and project-specific as the field needs.
> Default working file for review discussion.
>
> Concepts are named things under discussion — models, tools, platforms, modules,
> lineages. They are not keywords. When this map is formalized into
> `literature/refs.bib` (via the `map-to-bib` skill), each concept is resolved by
> judgment: to a publication entry, to a `keywords` tag on a parent publication,
> or to dismissal (no resolvable DOI). `refs.bib` is only edited through that skill.
>
> Scope: this field (AI-assisted drug discovery) moves very fast — explosive in
> 2026. References dated before 2025 are generally out of scope, except when they
> belong to an active lineage, whose full history is kept for complete
> understanding (e.g. the ESM family: ESM2/ESMFold → ESM3 → ESMC).

## **SECTION 1: BIOMOLECULAR STRUCTURE PREDICTION MODELS**

Predictive architectures that solve the forward problem: \\text{Sequence / Chemical Input} \\rightarrow \\text{3D Structural State}.

### **1.1 All-Atom Multi-Entity Co-Folding Foundations**

* **AlphaFold 3 (2024 \- Foundation Predictor Anchor)**
  * *Role:* All-atom 3D coordinate diffusion predictor for protein, nucleic acid, small-molecule, and ion interactions.
  * *Links:* [Nature Article](https://www.nature.com/articles/s41586-024-07487-w) | [Google DeepMind GitHub](https://github.com/google-deepmind/alphafold3)
* **Protenix-v1 & Protenix-v2 (2025/2026)**
  * *Role:* Open-source (Apache-2.0) all-atom foundation model featuring custom CUDA kernels, local ColabFold search integration, and antibody–antigen interface optimization.
  * *Link:* [ByteDance Protenix GitHub](https://github.com/bytedance/Protenix)
  * *Also covers:* PXDesign (de novo binder design engine) and PXMeter (evaluation toolkit) — modules of the Protenix project.
* **Boltz-1 & Boltz-2 (2024–2026)**
  * *Role:* Boltz-1 provides open-source all-atom co-folding; Boltz-2 incorporates thermodynamic binding affinity estimation (\\log\_{10}(\\text{IC}\_{50}) in \\mu\\text{M}).
  * *Links:* [PMC Article (Boltz-1)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11601547/) | [MIT Jameel Clinic GitHub](https://github.com/jwohlwend/boltz)
  * *Also covers:* BoltzGen (generative design engine on the Boltz foundation) — module of the Boltz project.
* **Chai Predictive Lineage (Chai-1 & Chai-3)**
  * **Chai-1 (2024):** Multi-modal structure prediction model supporting single-sequence inputs, SMILES strings, and protein glycosylations. [bioRxiv Preprint](https://www.biorxiv.org/content/10.1101/2024.10.10.615955v1) | [GitHub](https://github.com/chaidiscovery/chai-lab)
  * **Chai-3 (2026):** High-throughput 3D foundation model expanding predictive accuracy across large macromolecular assemblies. [Chai Discovery Web Platform](https://lab.chaidiscovery.com/) *(dismissed — commercial platform, no preprint/DOI; covered as a `chai-3` tag on Chai-1)*
* **AlphaFold 2 / AlphaFold-Multimer (Historical Lineage Anchor)**
  * *Role:* Single-chain and multimer structure predictor that established modern deep learning structural biology.
  * *Links:* [Nature Article](https://www.nature.com/articles/s41586-021-03819-2) | [DeepMind AlphaFold GitHub](https://github.com/google-deepmind/alphafold)
  * *OpenFold lineage:* see dedicated bullet below (OpenFold → OpenFold3); OpenFold is kept as the `openfold` keyword on this entry.
* **OpenFold lineage (OpenFold → OpenFold3)**
  * *Role:* AQ Laboratory's open-source reimplementations of the AlphaFold models. OpenFold (2022/2024) reproduces AlphaFold2 (kept as an `openfold` keyword on the AlphaFold 2 entry). OpenFold3 (The OpenFold3 Team, *OpenFold3-preview* v0.4.1, 2025) is a fully open-source, all-atom model based on AlphaFold3.
  * *Links:* [OpenFold3 GitHub](https://github.com/aqlaboratory/openfold-3) | [OpenFold GitHub](https://github.com/aqlaboratory/openfold)
  * *Note:* OpenFold3 is a 2025 code release with no paper/DOI, so it cannot enter `refs.bib`; it stays in the map (cited as a benchmark baseline in the ESMC paper, ref 38) for the knowledge base. The map is a superset of `refs.bib`.

### **1.2 Protein Language Models & Sequence Predictors**

* **ESMC (CZ Biohub \- 2026\)**
  * *Role:* Metagenomic sequence foundation model (6B parameters) forming the core sequence engine for Biohub's protein world model.
  * *Links:* [Biohub World Model Release](https://biohub.org/news/world-model-of-protein-biology/) | [Biohub ESM Repository](https://github.com/Biohub/esm)
  * *Also covers:* ESMFold2 (structure predictor and binder design engine) — module of the ESMC release.
* **ESM-2 & ESMFold (2023, Science)**
  * *Role:* Foundational ESM language-model scaling (ESM-2, 650M–15B params) and the single-sequence structure predictor (ESMFold); enabled the ESM Metagenomic Atlas (>617M predicted structures). Links the ESM-1 lineage to ESM-3.
  * *Link:* [Science Article](https://www.science.org/doi/10.1126/science.ade2574)
* **ESM-3 (EvolutionaryScale \- 2024\)**
  * *Role:* Multimodal promptable protein language model tokenizing sequence, 3D structure, and functional annotations into parallel tracks.
  * *Link:* [EvolutionaryScale Site](https://www.evolutionaryscale.ai/)
* **SaProt (2024/2025)**
  * *Role:* Structure-aware PLM using Foldseek 3Di structural alphabets (441 tokens) to process sequence and spatial constraints concurrently.
  * *Links:* [bioRxiv Preprint](https://www.biorxiv.org/content/10.1101/2023.10.01.560349v1) | [Westlake SaProt GitHub](https://github.com/westlake-repl/SaProt)

## **SECTION 2: DE NOVO BINDER GENERATION SYSTEMS & WORKFLOWS**

Generative systems that solve the inverse problem: \\text{Target Surface} \\rightarrow \\text{Novel Binder}.

### **2.1 Flow-Matching Generative Architectures**

Generative frameworks operating over continuous vector fields and Ordinary Differential Equations (ODEs) on SE(3) manifolds and discrete state spaces.

* **RFdiffusion2 (2024/2025)**
  * *Focus:* Active Site / Enzyme Scaffolding.
  * *Role:* Continuous SE(3) flow-matching model enabling sequence-agnostic, atom-level active site scaffolding (theozymes) directly from functional group positions.
  * *Links:* [bioRxiv Preprint (Enzymes 2025\)](https://www.biorxiv.org/content/10.1101/2025.04.09.648075v1) | [bioRxiv Preprint (Metallohydrolases 2024\)](https://www.biorxiv.org/content/10.1101/2024.11.13.623507)
* **PPIFlow (2026)**
  * *Focus:* Protein-Protein Interactions & VHH Design.
  * *Role:* SE(3) flow matching coupled with in silico maturation for direct generation of picomolar and nanomolar protein binders and single-domain antibodies.
  * *Link:* [ResearchGate / bioRxiv](https://www.researchgate.net/publication/400111229_High-Affinity_Protein_Binder_Design_via_Flow_Matching_and_In_Silico_Maturation)
* **IgFlow-LM (2025/2026)**
  * *Focus:* Antibody Sequence-Structure Co-Design.
  * *Role:* Multimodal conditional flow matching framework integrating antibody language models (IgBert) with SE(3) flow matching for joint backbone and latent sequence generation.
  * *Link:* [OpenReview PDF](https://openreview.net/pdf?id=cf01412a650fdfae28e931a168bc1c1d25079915) *(dismissed — OpenReview-only preprint, no DOI)*
* **ATOMFLOW (2025/2026)**
  * *Focus:* Ligand-Binding Protein Design.
  * *Role:* Atomic flow-matching model on unified biotokens, generating target-binding protein pockets directly from 2D molecular graphs without bound conformer structures.
  * *Link:* [OpenReview PDF](https://openreview.net/pdf?id=8cb7a8d548b9d4600e22a321d7b96f527dbcad39)
* **OriginFlow (2025)**
  * *Focus:* General Backbone & Binder Scaffolding.
  * *Role:* Combined SDE and flow matching framework for functional binder design, achieving 90% wet-lab hit rates across PD-L1, RBD, and VEGF targets.
  * *Link:* [bioRxiv Preprint](https://www.biorxiv.org/content/10.1101/2025.04.29.651154v1)
* **D-Flow (2024/2025)**
  * *Focus:* Therapeutic Peptides & D-Peptides.
  * *Role:* Full-atom flow matching on SE(3) frames and high-dimensional torus manifolds for bioorthogonal D-peptide binder discovery.
  * *Link:* [arXiv Paper](https://arxiv.org/abs/2411.10618)
* **moPPIt (2024/2025)**
  * *Focus:* Peptide Binders.
  * *Role:* Discrete flow matching for one-shot, de novo generation of motif-specific peptide binders.
  * *Link:* [bioRxiv Preprint](https://www.biorxiv.org/content/10.1101/2024.07.31.606098v2)
* **FrameFlow (2024/2025)**
  * *Focus:* Backbone Frame Generation.
  * *Role:* Recasts FrameDiff into an SE(3) flow matching framework, delivering 2\\times higher designability with 5\\times fewer sampling steps.
  * *Link:* [arXiv Preprint](https://arxiv.org/abs/2310.01234)
* **DrugFlow, FLOWR, & SemlaFlow (2024–2026)**
  * *Focus:* Small-Molecule Ligand Design.
  * *Role:* Flow matching models for pocket-conditioned ligand generation, generating 3D atom types, coordinates, and bond topologies directly.
  * *Links:* [DrugFlow bioRxiv](https://www.biorxiv.org/content/10.64898/2026.06.28.734975v1) | [SemlaFlow / FLOWR Paper](https://www.biorxiv.org/content/10.1101/2025.10.20.683377)
  * SemlaFlow *(dismissed — AISTATS proceedings without DOI)*.
* **ProtFlow (2026)**
  * *Focus:* Sequence Space Generation.
  * *Role:* Rectified flow-matching model capturing global protein semantic distributions for antimicrobial peptide and functional sequence generation.
  * *Link:* [bioRxiv Preprint](https://www.biorxiv.org/content/10.64898/2026.02.14.705870v1)

### **2.2 Generative Diffusion Engines & Multimodal Design Platforms**

* **RFdiffusion3 (2025/2026)**
  * *Role:* Modular, transformer-based all-atom diffusion foundation engine for target-conditioned generation across proteins, DNA, RNA, and small-molecule ligands.
  * *Links:* [IPD Release Announcement](https://www.ipd.uw.edu/2025/12/rfdiffusion3-now-available/) | [RosettaCommons GitHub](https://github.com/RosettaCommons/RFdiffusion)
* **Chai Generative Lineage (Latent-X & Chai-2)**
  * **Latent-X1 & Latent-X2 (2025/2026):** All-atom binder design platforms generating low-immunogenicity antibodies, macrocycles, and minibinders. [arXiv Link](https://arxiv.org/abs/2512.20263)
  * **Chai-2 (2025/2026):** Multimodal zero-shot antibody design system achieving a 16% wet-lab hit rate in 24-well plate assays across 52 unbiased targets. [ResearchGate Link](https://www.researchgate.net/publication/393457212_Zero-shot_antibody_design_in_a_24-well_plate)
* **PXDesign (2025)**
  * *Role:* Open-source de novo protein binder design platform built directly on top of the Protenix all-atom predictor. *(module — covered by the Protenix entries)*
  * *Link:* [ByteDance Protenix GitHub](https://github.com/bytedance/Protenix)
* **BoltzGen (2025/2026)**
  * *Role:* Unified generative design engine built on the Boltz foundation targeting proteins, peptides, nanobodies, antibodies, and small molecules. *(module — covered by the Boltz entries)*
  * *Link:* [MIT Jameel Clinic GitHub](https://github.com/jwohlwend/boltz)
* **AlphaProteo (2024/2025)**
  * *Role:* Google DeepMind's generative diffusion engine and multi-stage filtering pipeline for picomolar/nanomolar binder design.
  * *Link:* [DeepMind Technical Blog](https://deepmind.google/discover/blog/alphaproteo-generates-novel-proteins-for-biological-research/)
* **RFdiffusion (Historical Lineage Anchor)**
  * *Role:* \\text{SE}(3)-equivariant frame diffusion model that established modern generative protein backbone design.
  * *Links:* [Nature Article](https://www.nature.com/articles/s41586-023-06415-8) | [RosettaCommons GitHub](https://github.com/RosettaCommons/RFdiffusion)

### **2.3 Dual-Role Systems (Predictor \+ Binder Design Engine)**

* **ESMFold2 (CZ Biohub \- 2026\)**
  * *Role:* Dual structure predictor and binder design engine built on ESMC 6B; predicts complex interfaces and generates novel therapeutic candidates. *(module — covered by the ESMC entry)*
  * *Links:* [Biohub Release](https://biohub.org/news/world-model-of-protein-biology/) | [Biohub ESM Repository](https://github.com/Biohub/esm)

### **2.4 Sequence Optimization & Inverse Folding Submodules**

* **ProteinMPNN & LigandMPNN (2022–2024)**
  * *Role:* Autoregressive message-passing networks assigned to generate optimal amino acid sequences given fixed backbones and ligand environments. *(LigandMPNN covered as a `ligandmpnn` tag on the ProteinMPNN entry)*
  * *Links:* [Science Article](https://www.science.org/doi/10.1126/science.add2187) | [ProteinMPNN GitHub](https://github.com/dauparas/ProteinMPNN)

## **SECTION 3: AUXILIARY STEERING, FILTERING, & EVALUATION INFRASTRUCTURE**

Biophysical constraints, energy modules, and benchmark suites used to refine and evaluate generated candidates.

* **ProteinGS (2025)**
  * *Role:* Differentiable Gauss-Seidel projection module enforcing stereochemical constraints directly into generative diffusion/flow trajectories.
  * *Link:* [arXiv Preprint](https://arxiv.org/abs/2410.03456) *(dismissed — seed link mismatched; could not be resolved reliably to a clear DOI)*
* **PoseBusters & PoseBusters V2 (2023/2025)**
  * *Role:* Automated 18-check physical and chemical validity testing suite for evaluating generated ligand poses. *(PoseBusters V2 covered as a `posebusters-v2` tag on the PoseBusters entry)*
  * *Links:* [Chemical Science Article](https://pubs.rsc.org/en/content/articlelanding/2024/sc/d3sc04185a) | [PoseBusters GitHub](https://github.com/michellab/PoseBusters)
* **PXMeter (2025)**
  * *Role:* Open-source evaluation toolkit and artifact-filtered dataset for benchmarking multi-entity complex predictors and binder design outputs. *(module — covered by the Protenix entries)*
  * *Link:* [ByteDance Protenix GitHub](https://github.com/bytedance/Protenix)

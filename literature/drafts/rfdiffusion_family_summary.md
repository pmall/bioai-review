# The RoseTTAFold → RFdiffusion Lineage: RF1, RFAA, RFD1, RFdiffusion-AA, RFD2, RFD3

Source paper for RFD3 details: *De novo Design of All-atom Biomolecular Interactions with RFdiffusion3*, Butcher, Krishna, Mitra et al., bioRxiv 2025.09.18.676967v2 (Baker Lab / Institute for Protein Design, UW). Preprint, not peer-reviewed.

This document consolidates the whole Baker Lab / IPD line in one place: the two structure predictors it grew out of (Part I) and the four generative models built on them (Part II), plus the reasoning and clarifications worked out in discussion.

Sequence design throughout is ProteinMPNN / LigandMPNN — same lab, reviewed in `literature/drafts/proteinmpnn_ligandmpnn_summary.md`. Worth stating once here because it is presented early and then relied on by every later report: MPNN is *not* a Baker-lab-only component. Corpus papers referencing it span nine labs and both coupling levels — RFdiffusion3 (27 mentions), BoltzGen (14), RFdiffusion (10), RFdiffusion2 (6), RFAA (5), Latent-X1 (5), PXDesign (5), BindCraft (5), PPIFlow (4), AtomFlow (3), AlphaProteo (3), FrameFlow (2), D-Flow (2), OriginFlow (2).

---

## Part I — Where this lineage comes from: RoseTTAFold → RoseTTAFold All-Atom

*Moved here from `structure_prediction_family_overview.md`, where these two were previously reviewed as predictors. The reason is that the architecture **is** the lineage — RFdiffusion is a fine-tuned RoseTTAFold and RFdiffusionAA a fine-tuned RFAA — so the parent belongs with its descendants. The predictor report keeps three cross-cutting findings in short form and points here for the rest.*

*One empirical note that justifies the move: as a predictor, this lineage has left the conversation. Mentions in each co-folding paper run AlphaFold3 25, Chai-1 11, then Boltz-1, Boltz-2, Protenix-v1, Protenix-v2, OpenDDE and ESMC/ESMFold2 all **zero**. Nothing published since 2024 benchmarks against it. Its living relevance is entirely as the origin of what follows in Part II.*

**RoseTTAFold (RF1, Baek et al., *Science* 2021, `10.1126/science.abj8754`).** Built in the window when AF2's CASP14 performance was public but its method was not — the paper explicitly frames the work as exploring combinations of the five ideas DeepMind had presented at CASP14, "in the absence of a published method." The two papers appeared online the same day, 15 July 2021. Core architecture: a **three-track network** in which 1D (sequence/MSA), 2D (residue-pair distance/orientation), and 3D (coordinate) representations update *simultaneously*, with information exchanged between all three tracks at every layer — vs. AF2's more sequential Evoformer→structure-module pipeline, where 3D reasoning begins after 1D/2D processing is essentially complete. The paper's own evidence that the third track matters is direct: the three-track model clearly beats its own two-track variant (which itself beat trRosetta, the next-best CASP14 method) on CASP14 targets, with identical training data.

- **Two output modes, honestly compared:** (1) *pyRosetta mode* — network-predicted distance/orientation distributions drive Rosetta all-atom modeling; (2) *end-to-end mode* — a final SE(3)-equivariant layer directly outputs backbone coordinates. The end-to-end version is measurably worse, and the paper says why: GPU memory limits forced training on discontinuous two-segment crops totaling 260 residues, and side chains are ignored until the relaxation stage. Inference is cheap either way (~10 min end-to-end on a single RTX 2080 for <400 residues, after ~1.5 h of MSA/template search) — pointedly contrasted in-paper with DeepMind's CASP14 configuration of "several GPUs for days" per prediction.
- **Blind results:** #1 among all CAMEO servers over its first 69 medium/hard targets (May–June 2021); on CASP14 retroactively, it outperformed every participating group except AF2 itself — including Zhang-server, BAKER-ROSETTASERVER, and the BAKER human group (then the world #2). MSA-depth dependence is reported as *lower* than trRosetta's, "as in the case of AlphaFold2" — an early second data point for the MSA-threshold effect in §2.
- **Complex prediction as an untrained bonus — the lineage-defining finding:** because two-segment crops taught the network to handle chain breaks, feeding it two or more sequences with paired MSAs makes it predict complexes directly — "flexible backbone docking almost by construction," since chains fold *in the context of each other*. Achieved with zero complex training data (monomer-only training), with accuracy tracking paired-MSA depth — cross-chain coevolution doing real work. This observation is the seed of everything the lineage later became, including its generative turn.
- **An honest negative result worth keeping:** iteratively feeding predictions back as templates and subsampling MSAs generates ensembles that *contain* higher-accuracy models — but the confidence predictor "was not able to consistently identify" them. Sampling helps; ranking doesn't.
- **Demonstrated utility beyond benchmarks:** four previously unsolved molecular-replacement crystal structures solved from RF1 models (trRosetta models failed on all four); a cryo-EM domain fit (p101 GBD in PI3Kγ, 3.0 Å Cα-RMSD over the core β-sheets) where the top template hit had HHsearch E-value 40; predicted models for all human GPCRs of unknown structure, in both active and inactive states; 693 disease-relevant domains with >1/3 at lDDT >0.8, from which functional hypotheses were derived (TANGO2's Ntn-hydrolase fold, ADAM33's lipocalin-like prodomain, CERS1's six-helix active-site crevice).
- **Fully open from day one** — Robetta server, source, and weights on GitHub. This is the access posture AF2 set and AF3 abandoned; the Baker lineage never needed a reproduction effort because it never closed.

The intermediate steps between RF1 and RFAA — RoseTTAFoldNA (nucleic acids; residue alphabet widened to 28: 20 amino acids + 8 bases) and RoseTTAFold2 (RF2; faster and more accurate, template-integrated) — are preprints not cataloged in this corpus; RFAA's paper uses RF2 as its base network.

**RoseTTAFold All-Atom (RFAA, Krishna et al., *Science* 2024, `10.1126/science.adl2528`).** Get the chronology right, as a previous draft of this doc did not: RFAA was published online **7 March 2024 — two months *before* AF3 (8 May 2024)**. It is not "the lineage's answer to AF3"; the two are concurrent, independent generalizations of the 2021 generation to all-atom multi-entity modeling. (Also correcting the earlier draft: RFAA is in *Science*, not *Nature*.) Architecture — the three-track idea pushed to atomic resolution, with **no diffusion module anywhere in the predictor**:

- **Dual-granularity representation instead of AF3's unified tokenization:** biopolymers stay residue-level (inherited from RF2); everything else — small molecules, covalent modifications, unnatural amino acids — enters as an **atom-bond graph**: element tokens (46 types) on the 1D track, bond orders (single/double/triple/aromatic) on the 2D track, chirality on the 3D track. Atom tokens carry no relative-position encoding; permutation invariance is delegated to attention itself.
- **Chirality as input features, not losses — the direct architectural opposite of AF3's approach:** because the 1D/2D tracks are reflection-invariant, (R)/(S) centers are encoded on the 3D track as the sign of angles around each center, with the gradient of the deviation from ideal geometry fed as a feature into every subsequent block. Where AF3 has no chirality mechanism in its denoiser (hence its self-reported 4.4% PoseBusters violation rate, patched downstream by ranking penalties in AF3/Protenix or inference-time steering in Boltz), RFAA builds it in. Caveat stated plainly: **the paper reports no PoseBusters-style physical-validity pass rate at all**, so the two design philosophies cannot be compared on that axis from these papers alone — architecturally distinct, metrically unverified.
- **A "gas" that includes free atoms:** the system starts as "a disconnected gas of amino acid residues, nucleic acid bases, and freely moving atoms" — heavy atoms update by predicted translation only (no rigid frame), unlike residues' rotation+translation frames. The all-atom extension of AF2's FAPE loss gives every atom its own local frame defined by its bonded neighbors, with atom-pair terms upweighted.
- **Atomization, a training trick with a clear rationale:** random stretches of 3–5 contiguous residues are fed as bare atoms (sequence/template features deleted; an alanine becomes five heavy-atom tokens plus an "atom-to-residue" bond token). This forces the physics of protein-internal and protein-ligand atomic interactions to be learned jointly rather than as separate problems. Training data: 121,800 protein–small-molecule, 112,546 protein–metal, and 12,689 covalently-modified structures (30% sequence-ID clustered), plus organic small-molecule crystals from the Cambridge Structural Database, plus protein/nucleic examples carried over from RF2/RFNA training; crops of 256 tokens, 375 at fine-tuning.
- **One model, all modalities, stated as a philosophy:** "a single model trained on all available data over all modalities would have the greatest ability to generalize and be more accessible than a series of models specialized for specific problems." Same choice as Chai-1, which likewise trains one model on one cutoff. It is *not* a three-paper consensus, as an earlier draft had it: AF3 trains two models (a 2019 cutoff for PoseBusters, 2021 for everything else, to avoid the appearance of leakage) and Protenix-v1 also ships two checkpoints, split by benchmark-alignment vs. deployment (`structure_prediction_family_overview.md` §4) — so this is a two-against-two split on a live design question, not a settled one.
- **Fully open (code and weights on GitHub) and the only all-atom co-folder in this doc that neither reproduces AF3 nor was motivated by its closure** — Boltz-1, Protenix, and OpenFold3-preview all exist because AF3 closed; RFAA predates AF3's release. (A provisional patent was nevertheless filed — openness with an IP reservation.)

**Claims vs. evidence:**

- **Protein-ligand, blind (CAMEO ligand-docking server):** 43% of targets predicted with high confidence (PAE-interaction <10), and 77% of *those* land <2 Å ligand RMSD — the paper's usable interface is confidence gating, not raw accuracy. Against the CAMEO AutoDock Vina server on shared targets: 32% vs. 8% success (<2 Å), while doing the harder end-to-end task (Vina's server homology-models the protein first; the paper concedes an expert-driven Vina pipeline would do considerably better). Against DiffDock on post-cutoff PDB entries: **42% vs. 38%** — with RFAA folding the protein from sequence while DiffDock receives the bound crystal structure. That 42% (RMSD computed with the PoseBusters suite) is the number Chai-1's paper cites for RFAA — note it is RFAA's self-reported benchmark, not an independent re-run, and it lands RFAA far behind the ~76–77% the AF3-class models report on PoseBusters V1 (`structure_prediction_family_overview.md` §2, §6).
- **Where physics-based methods still win:** given both the bound protein structure and the pocket residues, AutoDock Vina beats RFAA 52% vs. 42% — the paper states this boundary plainly. Most common RFAA failure mode: ligand placed in the correct pocket but the wrong orientation.
- **Generalization, disaggregated the way this project values:** on 5,421 post-cutoff complexes, success is 35% for proteins with training overlap vs. 24% for proteins with none (BLAST E >1); 19% vs. 14% for ligands with Tanimoto <0.5 similarity to anything in training. Real but shallow degradation — the same genre of honest disaggregation as Protenix's common/non-common ligand split.
- **Evidence the model learned physical chemistry, not just geometry:** prediction accuracy correlates with Rosetta-computed interaction energies of the native complex (50/25/22% success for ΔG <−30 / −30–0 / >0 REU over 940+ cases), and on PoseBusters compounds RFAA's confidence assigns a worse PAE to the true binder's most-Tanimoto-similar decoy in 75.1% of cases — a discrimination signal, not merely a fitting one.
- **Ligand context improves the *protein* prediction:** where both RFAA and RF2 are confident, RFAA's protein structure is the more accurate one — capturing domain movements, subtle backbone shifts, and rotamer flips that accommodate the ligand, which protein-only RF2 misses. The modalities are coupled in training, and the coupling pays off on the core task.
- **Covalent modifications — a capability no other paper in this doc claims:** 46% of 931 recent covalent modifications predicted <2.5 Å RMSD (60% high-confidence, 63% of those accurate; 27.5% accurate even with zero sequence overlap to training). Median RMSD 0.99 Å for covalently bound cofactors, 2.8 Å for covalent drugs, 3.2 Å for glycans up to seven monosaccharides — verified against experimental density, not just internal metrics. The paper notes no prior deep-learning tool models covalent modification at all.
- **Multicomponent assemblies in one forward pass:** a DNA polymerase (7U7W) with DNA + nucleotide + Mg²⁺ predicted despite no protein+small-molecule+nucleic-acid higher-order assemblies in training — honestly flagged as likely synthesis from related binary complexes in the training set, not de novo prediction.
- **No accuracy sacrifice on the core protein task:** median GDT 85 vs. AF2's 86 on monomers; protein–nucleic-acid accuracy comparable to RFNA (median all-atom LDDT 0.74 vs. 0.78). The all-atom generalization cost about one GDT point.
- **Self-disclosed limitation, from the discussion itself:** consistently accurate protein–small-molecule prediction "on par with the accuracy ... on protein systems alone" will require more training data and/or architectural improvements — the authors place ligand co-folding as unfinished, which the large gap to the AF3-class PoseBusters numbers independently confirms.

---

## Part II — the generative turn

### The core problem this whole lineage is solving

Deep learning protein design methods generate **3D structure**, not sequence. In every version of this family, the pipeline is always two steps:
1. A diffusion model generates **3D coordinates** (backbone, and in later versions, side chains and non-protein atoms).
2. A **separate, independently trained inverse-folding model** (ProteinMPNN, or LigandMPNN when non-protein atoms are present) takes the fixed 3D backbone and designs a full amino acid sequence for it from scratch, autoregressively (position by position). This is not "filling gaps" in a partial sequence — it receives no sequence at all and generates the whole thing conditioned purely on 3D shape (and on target/ligand atoms, for LigandMPNN).
3. AF3 (or Chai, an open-source AF3 reproduction) is typically used afterward as an in silico validation step: does the designed sequence actually refold back into the intended structure?

The single technical limitation that each successive model chips away at: **a residue-frame representation cannot natively express atomic-level design goals** (specific hydrogen bonds, exact catalytic geometry, burial of individual atoms). RFD1 has no atomic variables at all. RFD-AA and RFD2 patch in atomic detail as exceptions. RFD3 removes the frame representation entirely and makes atoms the only unit, for both the generated protein and (optionally) the target itself.

---

### RFdiffusion (RFD1)

**What it generates:** Protein backbones only. No side chains, no non-protein atoms.

**Representation:** Each residue = one **rigid-body frame**: a 3D position (Cα) + a 3D orientation (like a small tripod pointing in a direction). Backbone atoms (N, Cα, C, O) are not learned outputs — they're reconstructed afterward from fixed, known peptide bond geometry, since this geometry is essentially identical across all proteins.

**Target representation:** If there is a target (e.g., binder design against another protein), it is represented **identically to the generated protein — residue-level frames.** Same resolution on both sides. The target is completely frozen; only the new chain's frames are diffused.

**Target types supported:** Only proteins (or no target — unconditional generation), because RFD1 has no data type capable of representing non-protein atoms.

**Typical use cases:** Protein monomers, symmetric assemblies, protein-binding proteins (binder design), motif scaffolding, unconditional generation.

**Unconditional generation, specifically:** Not just a novelty — it's also a validation step (does the model produce diverse, plausible folds with realistic sequence composition at all, before trusting it on harder conditioned tasks?). No design utility on its own.

**Core limitation:** No side-chain atoms exist as variables anywhere in the model, so it structurally cannot represent atomic-level goals — no hydrogen bond specification, no catalytic geometry, no small-molecule pockets.

---

### RFdiffusion-AA ("all-atom", RFD-AA)

**What it adds over RFD1:** The ability to condition generation on a **small-molecule target**.

**Target representation:** Full explicit atoms — every atom of the ligand with real 3D coordinates and real element/chemistry identity (which atom is O, N, etc.). This is necessary because a small molecule has no residue structure to compress into a frame — there's no analogous "backbone."

**Generated protein representation:** Unchanged from RFD1 — still residue-frame-based. This is the key limitation: the *protein side* did not gain atomic resolution, only the target did.

**Fixed or moving:** The ligand's conformation is a **rigid, frozen input**, supplied once by the user (typically its known bioactive/crystallographic pose) and never repositioned during generation. Only the protein frames around it are diffused.

**Typical use cases / motivation for small-molecule targets in general:** Sensors and diagnostics (protein changes conformation/signal on binding a target molecule), sequestering agents, enzyme pocket design (holding a substrate for catalysis), light-harvesting proteins (holding a chromophore in a precise geometry).

**Core limitation:** Because the protein remains frame-only, there's no way to specify precise atomic contacts (which side-chain atom touches which ligand atom, hydrogen bond donor/acceptor identity, etc.) — you get a pocket shape, not fine atomic control. Also, requiring a rigid pre-specified ligand conformation is a problem for molecules with multiple plausible conformers, since a wrong guess means the pocket is built around the wrong shape.

---

### RFdiffusion2 (RFD2)

**What it adds over RFD1 / RFD-AA:** The ability to pin a **small, hand-picked subset of atoms** — from either the generated protein or the target — at exact fixed coordinates, injected directly into the noise cloud the network refines.

**Important clarification on what gets pinned:** These pinned atoms are *not* specifically "the target" — they can be:
- Atoms belonging to the **protein being generated** (e.g., the exact coordinates of a catalytic histidine's side-chain nitrogen, specified in advance).
- Atoms belonging to a **ligand/target** (e.g., a specific contact atom the ligand must be near).

Everything else in the system — the bulk of the generated protein, and any protein target — remains plain residue frames, exactly as in RFD1. RFD2's innovation is a general mechanism ("essentially a new data type," per the RFD3 paper) for injecting atomic precision *wherever* it's needed, not a redesign of how targets are represented.

**Fixed or moving:** The flagged special atoms are **frozen exact coordinates** — not diffused, not movable. The network builds a plausible scaffold around them.

**Typical use cases:** Enzyme active-site scaffolding (this is the headline capability — precisely arranging catalytic residues around a reaction transition state without hard-coding their sequence position), more precise motif scaffolding, and coarse-grained extras like specifying solvent exposure/burial of ligands.

**Documented limitation (from RFD3 paper):** Active sites spanning more than 4 separate, non-contiguous "residue islands" were difficult for RFD2 to scaffold successfully. Also, because only a small, manually chosen subset of atoms is ever explicit, RFD2 cannot do *general* atom-level conditioning (e.g., broadly flagging hydrogen-bond donor/acceptor status or burial across many atoms) — only for the handful of atoms specifically pinned by the user.

---

### RFdiffusion3 (RFD3) — the paper reviewed in this project

**What it adds over all previous versions:** Removes the frame representation entirely. **Every atom — of the protein being designed and of the target (ligand/DNA) — is diffused in one shared atomic coordinate cloud.** No more "coarse frames + patched-in exceptions": atoms are the only unit, everywhere.

#### Representation details

- Every residue = **14 atom slots**: 4 backbone atoms (N, Cα, C, O) + 10 side-chain atoms. The number 10 is sized to tryptophan, the largest canonical amino acid's side chain atom count.
- **How smaller residues fill the slots:** unused side-chain positions are not spread into fictional geometry — they collapse onto a single repeated point, placed **on the Cβ atom** (or Cα for glycine, which has no Cβ). So for a small residue like alanine, most of the 14 "atoms" are literally stacked at one coordinate, not distributed into a nonexistent radical.
- **Exception:** serine's terminal oxygen and cysteine's sulfur are kept as distinct labeled virtual atoms (rather than both collapsing identically) so the network can distinguish these two otherwise-similar small residues.
- **At training time**, ground-truth amino acid identity is known, so the model is explicitly told which slots to collapse and where.
- **At inference/generation time**, sequence identity is *not* yet known (that's decided afterward by MPNN) — so the network doesn't know in advance whether a position will end up alanine or tryptophan. In practice, the network has learned from training data that local structural context (packing density, curvature, proximity to a binding partner) correlates with small vs. large side chains, so its raw output naturally tends to place the 14 points either tightly collapsed (implying a small residue fits) or spread into a larger shape (implying room/need for a bigger side chain) — this spread is an implicit, geometric signal about likely residue type, not junk.
- **After MPNN assigns a real amino acid identity** to each position, only the atoms that actually exist for that amino acid are kept in the final structure; whatever extra raw coordinates don't correspond to a real atom of the assigned residue are discarded — they were scaffolding used during generation, not atoms carried forward into the final design.
- *Open item, not confirmed from the main text*: the exact tokenization scheme for DNA nucleotides (how many atom slots per base, whether there's Cβ-style padding) is not detailed in the main text — likely lives in the Supplemental Methods, not yet reviewed.

#### Target representation — the genuinely novel part

Unlike prior versions, **RFD3 does not have a single fixed rule for whether the target is frozen.** The determining factor is whether the target's real-world 3D shape is already known and stable, or whether it's flexible/uncertain in the bound state:

- **Protein targets** (e.g., PD-L1, InsulinR, IL-7Rα, Tie2, IL-2Rα in the binder benchmarks): typically **kept fixed**. These are stable, experimentally known folded structures whose shape doesn't meaningfully change depending on binding partner in these benchmark cases — freezing them loses no real information.
- **DNA targets:** the design *input* is a desired DNA **sequence**, not a structure — DNA is flexible and can adopt different shapes (bending, groove geometry) depending on what's bound to it, so there often isn't a single correct pre-existing structure to hand in. RFD3 is trained to **jointly predict the protein structure and the DNA conformation together**, rather than requiring a pre-guessed DNA shape.
- **Small-molecule targets:** many have multiple rotatable bonds / plausible conformations. RFD-AA required guessing the bioactive conformation up front. RFD3 can **jointly sample the ligand's conformation** along with the protein, removing that guess.
- Motifs/functional atoms can still be supplied as **fixed exact coordinates** when the user wants to lock them in (this mode still exists, inherited conceptually from RFD2's pinning mechanism, but now expressed natively in the atomic representation rather than as a bolted-on exception).

**Important scope boundary (discussed explicitly):** RFD3 diffuses conformations of ligands/DNA whose chemical identity is already specified — it does not invent novel small-molecule chemotypes (new atoms, new bonding) from scratch. It is a protein-(+known-ligand-pose) generator, not a de novo molecule-generation model. For workflows like "fix a peptide binder's structural hotspots, then generate a *novel small molecule* scaffold to recreate those interactions" (pharmacophore-based scaffold hopping / peptidomimetic design), RFD3 is not the right tool — that requires a different class of model built specifically to generate small-molecule atoms and bonds conditioned on a target pocket (e.g., pocket-conditioned molecule-generation diffusion models such as DiffSBDD, Pocket2Mol, TargetDiff — noted here as general field context to verify independently, not as something confirmed or endorsed in the RFD3 paper). RFD3's fixed-atom mechanism *does* directly apply, however, to fixing known functional atoms and scaffolding a **new protein/peptide** around them — that's exactly the enzyme motif-scaffolding workflow the paper demonstrates.

#### Why diffusing side chains matters, even though MPNN mostly reads the backbone

Forcing the network to also place plausible side-chain atoms during training shapes the *backbone itself* to be better primed for the intended contacts (hydrogen bonds, ligand grip), even though MPNN's downstream sequence design mostly reads final backbone geometry rather than literally inheriting side-chain positions. The paper checks this indirectly (Fig. S9a–d): MPNN-redesigned sequences tend to recapitulate many of the same interactions the diffused side chains implied.

#### Architecture

- Transformer-based **U-Net**: (i) downsampling module encoding atomic- and residue-level features including the partially noised structure, (ii) sparse transformer processing token-wise information, (iii) upsampling module modulating atomic features with token-wise features to predict coordinate updates. Inspired by AF3's diffusion module.
- **Sparse attention**: atoms/residues attend to each other only if geometrically close in the noised structure — focuses compute on local interactions, reduces overfitting.
- **Cross-attention pooling** between atom-level and token-level representations (up-pooling and down-pooling), inspired by Pagnoni et al. — lets the token-level transformer focus on specific atoms within each token; token features are read out via cross-attention by token splitting.
- **Pairformer shrunk from AF3's 48 layers to 2** — since design conditioning information is much lighter-weight to process than a full amino acid sequence (as AF3 requires for structure prediction).
- **No triangle multiplicative/attention updates** (present in AF3 and prior RFdiffusion architectures) — omitted for efficiency.
- **Classifier-free guidance** (borrowed from image diffusion) — at each denoising step, a weighted average of a conditioned and unconditioned forward pass improves adherence to complex conditioning sets.
- **168M trainable parameters** vs. ~350M for AF3.
- **~10x speed improvement** over RFD2 for typical protein length ranges.

#### Training

- All Protein Data Bank (PDB) complexes: protein-protein, protein-small molecule, protein-DNA interfaces, plus motif scaffolding examples, plus high-quality AF2 distillation structures (Hsu et al.).
- PDB entries used through December 2024.
- Hierarchical procedure: pretrain on a mix of AF2 predictions + PDB structures, then fine-tune with a larger fraction of DNA and protein-protein interface examples, to prevent overfitting given the range of task types.
- Training examples generated by noising native structures to varying extents and predicting backbone/side-chain positions given a subset of applicable conditioning info (hydrogen bonds, binding partners, functional motifs annotated per structure).

#### New conditioning capabilities enabled (native, not bolted on)

- Hydrogen bond donor/acceptor status per atom — raises the fraction of designed interactions from 26.67% → 32.67% (conditioned) → 36.67% (+classifier-free guidance) for small-molecule binder design; similar trend for DNA base H-bonds (11% → 11.3% → 12.5%).
- Solvent-accessible surface area (burial) labels per atom.
- Center-of-mass placement of the generated protein relative to the target/motif.
- Symmetric noise initialization for generating symmetric assemblies.
- Atom-level "hotspots" for binder design (vs. residue-level hotspots in RFD1/prior tools) — more precise control over the desired interaction epitope.

#### In silico benchmark results (self-defined AF3-confidence-based success criteria, cutoffs from the group's own earlier work)

- **Unconditional generation:** 41 distinct structural clusters out of 96 generations (length 100–250, TM-score cutoff 0.5); sequence composition similar to ProteinMPNN's distribution but biased toward alanine vs. native sequences (hypothesized: sample distribution biased toward compact globular folds). 98% of designs (length 100–200) have ≥1 of 8 MPNN-generated sequences predicted by AF3 to fold within 1.5 Å RMSD.
- **Protein-binding proteins:** benchmarked against RFD1 on 5 therapeutic targets (PD-L1, InsulinR, IL-7Rα, Tie2, IL-2Rα), 400 designs per method per target. RFD3 outperforms RFD1 on 4/5 targets (all backbones considered); finds far more unique successful solution clusters per target (8.2 vs 1.4 average, TM-score 0.6 clustering); also samples more diverse docking poses.
- **Protein-DNA interactions:** tested on 3 DNA sequences held out from training. 8.67% pass rate for monomeric designs, 6.67% for dimeric designs (<5Å DNA-aligned RMSD, protein Cα RMSD after DNA-phosphate alignment, trimming terminal loops). When the RFD3-generated interface is fixed during LigandMPNN sequence design: 6.5% (monomeric) / 5.5% (dimeric). Removing DNA structure pre-specification slightly reduces monomeric refolding success but increases DNA conformational diversity; for dimeric generation it can improve refolding success in some cases.
- **Small-molecule binders:** benchmarked on 4 diverse molecules (from RFD2's paper) against RFD-AA with rigid ligands — RFD3 significantly outperforms in all four cases. Same trend holds when jointly generating ligand coordinates with a buried RASA (relative accessible surface area) label + classifier-free guidance. RFD3 designs are also more diverse, more novel vs. the training set, and have lower (better) Rosetta ΔΔG binding energies.
- **Enzyme design (AME benchmark, 41 active sites from PDB, measured via Chai/AF3):** RFD3 outperforms RFD2 on 37/41 cases (90%). On the harder subset with >4 non-contiguous residue islands (n=12): 15% vs 4% pass rate for RFD3 vs RFD2. Symmetric (C2) active site subsetting: with symmetric noise initialization, RFD3 successfully scaffolds the active site geometry across both subunits in all tested cases, including a 7-residue-island case.

#### Wet-lab experimental validation (the weakest-evidenced part of the paper)

- **DNA binders:** two-stage protocol — (1) sample designs directly conditioned on an AF3 prediction of a randomly generated target DNA sequence, (2) for well-predicted designs, fix the DNA-contacting motif and resample the rest of the backbone to optimize. 5 synthetic designs tested via yeast surface display + flow cytometry; **1 of 5 bound**, EC50 = 5.89 ± 2.15 µM. No crystal/cryo-EM structural confirmation of the actual binding pose was reported.
- **Enzyme design:** esterase reaction (Cys-His-Asp catalytic triad hydrolyzing 4-methylumbelliferyl phenyl acetate), minimal motif defined from a native cysteine hydrolase (Ulp-1) crystal structure. 190 designs screened; **35 multi-turnover hits**; best design Kcat/Km = 3557, stated to exceed prior *designed* enzymes for the same reaction (no natural-enzyme baseline given for scale comparison).
- Cross-check: tested whether MPNN-designed interactions recapitulate the residue positions/charge properties implied by RFD3's input side chains — found that MPNN "recapitulates many" of the designed interactions (Fig. S9a-d) — and that fixing these interaction residues while redesigning the rest doesn't significantly hurt refolding metrics.

---

### Standing criticisms of the RFD3 paper (earned, not exhaustive)

- **Wet-lab sample sizes are small and largely unconfirmed structurally.** 5 DNA-binder designs (1 hit) and 190 enzyme designs screened — no crystallography/cryo-EM confirming that successful binders/enzymes actually adopt the predicted structure; DNA binding is measured only by affinity (flow cytometry), not structural fidelity.
- **Success metrics are self-referee'd.** Nearly all in silico benchmarks use AF3-predicted-structure-agreement cutoffs defined in the group's own earlier papers — a reasonable field-standard proxy, but a proxy stacked on a proxy, not independent validation.
- **All comparisons are intra-family** (RFD1, RFD2, RFD-AA) — no benchmarking against other groups' atomic/diffusion-based design methods, limiting conclusions about RFD3's standing relative to the field as a whole.
- **Some reported gains rest on small N** — e.g., the >4-residue-island enzyme subset is n=12 (15% vs 4% ≈ 2/12 vs 0.5/12).
- **No natural-enzyme baseline given for the Kcat/Km = 3557 result** — the comparison is only to prior *designed* enzymes for the same reaction, so it's hard to judge how far this still lags biological catalysts.
- **Preprint status** — not yet peer-reviewed as of the reviewed version (posted November 19, 2025).

---

### Summary table

| | RFD1 | RFD-AA | RFD2 | RFD3 |
|---|---|---|---|---|
| Generated protein representation | Residue frames | Residue frames | Residue frames + a few pinned atoms | Full atoms (14/residue) |
| Target representation | Frames (if protein target) | Full rigid atoms (small molecule) | Frames, or frames + pinned atoms | Full atoms; frozen or jointly generated depending on molecule type |
| Target types | Protein / none | Small molecule | Protein / small molecule, with pinned functional atoms | Protein, small molecule, DNA |
| Can target move during generation? | No | No (rigid) | No (pinned atoms are frozen) | Sometimes — yes for DNA/ligand conformation, typically no for protein targets |
| Native atomic conditioning (H-bonds, burial, etc.) | No | No | Only for manually pinned atoms | Yes, generally, for any atom |
| Params | — (RoseTTAFold-derived) | — | RoseTTAFold-derived, heavier | 168M |
| Speed vs RFD2 | — | — | baseline | ~10x faster |
| Headline use case | Binder design, monomers, assemblies | Small-molecule pocket design (rigid ligand) | Enzyme active-site scaffolding | Unified: binders, DNA binders, small-molecule binders (flexible ligand), enzymes |

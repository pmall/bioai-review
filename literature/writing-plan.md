# Writing plan and method

> How the review gets written: what the draft units are, how big each one is,
> what shape a section takes, and in what order they are drafted.
>
> `literature/map.md` holds the content: every publication, every fact, every
> claim, structured in reading order — the review minus its prose. This file holds
> everything addressed to whoever writes that prose: sizes, drafting order, section
> shape, and the placement directives below. Neither restates the other. **No
> instruction to the writer belongs in the map.**

## Target

**8,000 words of main text**, 49 references — the standard scale for a journal
review at this reference count (Nature Reviews, Briefings in Bioinformatics, Annual
Review). Not an exhaustive survey.

**Tables A and B are display items**, not main text, and do not count against the
budget in any of those venues. Only the paragraph between them does.

---

## Weight — the rule that governs every other rule here

A review is read for its **proportions** before it is read for its sentences. A
reader who knows this field arrives with a rough map of what matters in it, and the
fastest way to lose them is to spend three paragraphs on a preprint they have not
heard of and one clause on AlphaFold. The tier system exists to prevent exactly
that, and this section is where it becomes an instruction to the writer.

**Tier determines treatment. It is not a hint.**

| Tier | Treatment in the prose | Test the draft must pass |
|---|---|---|
| **backbone** | A passage of its own: mechanism, the numbers that matter, the caveat, and what it is contrasted with | A reader could explain what this system does and why it mattered, from the review alone |
| **meat** | Named in a sentence or two while a backbone claim is being made; its numbers may be quoted | Removing it weakens a claim's evidence; it does not leave a hole in the narrative |
| **mention** | A clause, or a parenthetical. No mechanism, no numbers in the prose — numbers go to Table A or B | It can be read past without loss |

**Twenty publications carry the review.** They are the backbone set, and they are
the ones a reader should come away able to name:

| Section | Gets a passage |
|---|---|
| §1 | AlphaFold2 · AlphaFold-Multimer · AlphaFold3 |
| §2 | RoseTTAFold · RFdiffusion · RFantibody · RFpeptides · ProteinMPNN |
| §3 | Boltz-1 · BoltzGen · BoltzProt-1 |
| §4 | Chai-2 |
| §5 | FrameFlow |
| §6 | BindCraft · Germinal |
| §7 | PXDesign |
| §8 | ESM-2/ESMFold · ESMC/ESMFold2 · the ESMFold2 binder campaign |
| §9 | Latent-X1 |
| Instruments | FoldBench |

Everything else in `map.md` — roughly thirty further works — appears in support of
a claim or not at all. **That is not a demotion**; the invariant that every named
publication resolves to a catalog entry is about the catalog's honesty, not about
the prose owing each one a turn.

**Three failure modes, in the order they actually happen.**

1. **The recency inversion.** Recent preprints have long, specific, quotable
   entries because they were read most recently and argue with each other in detail.
   Mastodonts have short entries because their content is assumed. A draft written
   by following entry length will invert the field's weight. *Check:* if a 2026
   preprint gets more prose than AlphaFold2, RFdiffusion or ProteinMPNN, the draft
   is wrong regardless of how interesting the preprint is.
2. **The interesting-detail trap.** A small paper with an unusual result is more
   fun to write about than a foundational one whose result everybody knows. Interest
   is not weight. A finding earns prose in proportion to what rests on it, and
   `map.md` states what rests on each entry under *Carries*.
3. **Cataloguing under the guise of completeness.** Listing five flow-matching
   papers because the corpus holds five. §5's own entry says what to do instead:
   one argument, four examples named in support.

**Where the map over-supplies, cut rather than expand.** Some entries carry more
material than their tier warrants, because the underlying paper is recent and
detailed. The map records what is true; this file decides what is written. When the
two disagree, tier wins.

## Draft units

Fifteen drafts. `map.md` carries one heading per draft, in render order, so
this table is a lookup rather than a second slicing of the material. The map's
layout block is the one heading with no draft. The three benchmarking units
are three drafts rather than one because they have different sources, timing and
positions in the final text. Excluded works are not a draft unit — they are a
record in `candidates.md`, not a part of the review.

| # | Draft | File | Source |
|---|---|---|---|
| 1 | Introduction | `drafts/00-intro.md` | The introduction |
| 2 | Metrics primer | `drafts/01-metrics-primer.md` | The metrics primer — renders before §1 |
| 3 | §1 AlphaFold and the open co-folding cluster | `drafts/02-alphafold.md` | §1 |
| 4 | §2 RoseTTAFold → RFdiffusion | `drafts/03-rosettafold.md` | §2 |
| 5 | §3 Boltz | `drafts/04-boltz.md` | §3 |
| 6 | §4 Chai | `drafts/05-chai.md` | §4 |
| 7 | §5 Flow matching | `drafts/06-flow-matching.md` | §5 |
| 8 | §6 Inversion as a portable technique | `drafts/07-inversion.md` | §6 |
| 9 | §7 Protenix | `drafts/08-protenix.md` | §7 |
| 10 | §8 ESM | `drafts/09-esm.md` | §8 |
| 11 | §9 The closed frontier | `drafts/10-closed-frontier.md` | §9 |
| 12 | What the field has not shown | `drafts/11-gaps.md` | The gaps unit — four stated limits, written after §1–§9 |
| 13 | Instruments | `drafts/12-instruments.md` | The instruments |
| 14 | Tables A and B | `drafts/13-tables.md` | Tables A and B — written after §1–§9 |
| 15 | Conclusion | `drafts/14-conclusion.md` | The conclusion — a stub; the map records the gap, not the answer |

**The layout block does not become a draft.** It turns into two things: a
short roadmap paragraph closing the introduction, and the seam sentences between
sections — the block supplies the two-axis logic, and each section's own
*Why here* line supplies the seam into it.

**The conclusion is written last, from the finished parts.** §9 is a coda and Beat 5
sets up an ending, but nothing in the map states what the review concludes —
deliberately, and the stub there says so. What it concludes follows from the other
fourteen drafts, so it is decided when they exist rather than planned in advance.

**The gaps unit has a hard rule and it is the map's, not this file's:** a gap enters
only when a publication in the catalog states it. The unit is four items long for
that reason, and it is not the place to speculate about what comes next. It is
drafted after §1–§9 because three of its four items are limits those sections
establish and one is Tables A and B's.

## Size budget

**These shares are the weight rule made countable, not a quota to hit.** They exist
so that a section's length can be checked against what the section carries, before
anyone has written a word. The absolute counts are indicative; the **column that
matters is the backbone count**, because that is what the share is derived from.

*Shares are re-derived when the argument moves, never when a paper arrives.*

| Draft | Backbones | Share | @ 8,000 | Why that weight |
|---|---|---|---|---|
| Introduction | — | 15% | 1,200 | five beats, carrying the two frames the whole review reads through: the co-folder anatomy (Beat 2) and the coupling taxonomy (Beat 4) |
| Metrics primer | — | 4% | 320 | two families of metric, one consequence; tight by design |
| §1 AlphaFold | 3 | 10% | 800 | the three papers everything else is defined against, and the MSA bet the review's longest thread starts from |
| §2 RoseTTAFold | 5 | 12.5% | 1,000 | the most backbones of any section — the second origin, the generative turn, the antibody and macrocycle arms, and ProteinMPNN for the whole review |
| §3 Boltz | 3 | 9.5% | 760 | the open AF3-class model, the cleanest Level 0, and the trained-critic result |
| §4 Chai | 1 | 4.5% | 360 | the corpus's strongest antibody result from an undisclosed generator — short, and that is the finding |
| §5 Flow matching | 1 | 3% | 240 | one argument with four examples, not five papers taking turns; its weight sits in Beat 4's step-count passage |
| §6 Inversion | 2 | 8% | 640 | the five-step arc plus BindCraft and Germinal; the other four systems are evidence, not subjects |
| §7 Protenix | 1 | 6.5% | 520 | the platform argument plus the filter-ensembling finding |
| §8 ESM | 3 | 9% | 720 | the climax: the MSA throughline lands and the coupling axis ends |
| §9 Closed frontier | 1 | 4.5% | 360 | coda, restrained on purpose — restraint is the argument |
| Gaps | — | 4% | 320 | four stated limits, each pointing at the entry that evidences it; no speculation |
| Instruments | 1 | 5% | 400 | four instruments; three prediction-side defects plus Overath's own, stated once |
| Table commentary | — | 3% | 240 | display items; only the asymmetry argument is main text |
| Conclusion | — | 4% | 320 | written from the finished parts |
| **Total** | **21** | 100% | **8,000** | |

**The check this table exists for:** §1 outweighs §6, §7 and §9; §2 outweighs
everything. If a draft comes back the other way round, the recency inversion has
happened and the fix is to cut the recent material, not to argue for it.

*If the introduction overruns when drafted,* the co-folder anatomy moves to the
metrics primer, which already renders before §1 and is already built to teach one
distinction before the reader needs it. That trade is the relief valve; cutting the
anatomy is not.

§1–§9 come to about two thirds of the review, which is right for a review whose
argument is the section order.

## What a section is

A section is a block of argument. It is **not** a list of publications with
commentary on each. Publications appear inside the prose, supporting claims; they
are not headings and they do not each get a turn.

**Its backbones are its subjects; everything else is evidence.** A section with
three backbones has three things to explain properly and a supporting cast. Prose
spent on the cast is prose taken from the subjects — that is the trade, and it is
always the wrong way round when a *mention* has a sentence to itself.

**Read the entry schema before drafting a section.** `map.md`'s header defines it:
each entry's *Carries* line is the claim that must survive into the prose, *Against*
is the comparison the passage should be built around, *Caveat* travels with the claim
wherever it is cited, and *Collision* says what this section must not restate. A
backbone passage that states what a system *is* without stating what it is
**against** has described a paper instead of making an argument.

Every section makes the same four moves, in this order. This is what keeps nine
independently drafted sections reading as one review:

1. **The claim.** What this lineage or technique contributed, stated as a
   proposition. Not a preview of what the section will cover.
2. **The mechanism.** What these models actually do — told once for the whole
   section, from the parsed corpus, rather than restarted for each paper.
3. **The evidence.** Benchmarks and wet-lab campaigns, with the caveat that
   applies to them.
4. **The handoff.** Where the section sits on the coupling spine, and the seam
   into the next section.

**A section draft that could have been written from the map alone has failed.**
The map's own header says what it refuses to hold: *"Method internals, benchmark
numbers, per-paper caveats and quotes are read out of the corpus at writing
time."* That material is exactly what a section draft is made of, and it comes
from `literature/corpus/`, not from the map entry.

**Collisions are already assigned by the map.** Each draft opens with three lines —
owns / references / must not restate — copied from the map, not reinvented. The
standing assignments: ipTM and pAE definitions to the primer, ProteinMPNN to §2,
AtomWorks to §2 in one line, the trained-critic result to §3, BoltzDesign1's analysis
to §6, the groups-versus-architectures qualification to §6's step 4, mBER's
unchosen-targets argument to Beat 3, the physical-validity thread and all benchmark
caveats to the instruments, and the disclosure argument to §9.

## Using xrefs

`literature/xrefs.md` is not a sizing instrument. Its own header says in-degree
is confounded by publication age, so §6, §7 and §9 score low for being recent,
not for being minor. Three uses that hold:

- **It tells you the shape a section must take.** §2 has 34 citations internal
  to itself: a genuine lineage, written chronologically. §5 has 4 internal edges
  but 14 pointing at §2 — those five flow-matching papers are descendants of
  RFdiffusion, not of each other. §5 therefore cannot be written as a lineage;
  it is five independent responses to one problem, organized by what they do
  differently. The map suspected this; xrefs establishes it.
- **It gives the drafting order.** §7 cites §3 nine times and §4 six times, so
  §3 and §4 must exist first. Worked through the between-sections matrix, map
  order already is dependency order.
- **Prose-mention counts point at the passages to read.** BoltzProt-1 names
  BoltzGen 57 times — that is §3's central comparison. OpenGerminal names
  Germinal 45 times — §6's. Latent-X1 names RFdiffusion 50 times — what §9
  measures itself against. Those counts say where to start reading in the
  corpus. A high count means the papers argue with each other; it never means
  agreement or benchmarking, which only reading the passage settles.

Regenerate with `uv run scripts/build_xrefs.py` before a drafting pass, so the
shape and order above are computed from the current corpus.

## Drafting order

1. **Metrics primer** — before §1, which quotes pAE and ipTM immediately.
2. **§1 → §9 in map order** — already dependency order, per the matrix above.
   **Budget the time by backbone count:** §2 carries five and is the longest to
   draft, §1, §3 and §8 three each, and §4, §5, §7 and §9 one apiece.
3. **Introduction** — after §1–§9, when the numbers it promises are known to
   be real and the beats can point at sections that exist.
4. **Instruments, then Tables A and B** — the tables gather the sections' numbers
   and cannot precede it.
5. **The gaps unit**, which needs §1–§9 and both tables to exist first.
6. **Conclusion.**

## Assembly

Two passes, neither of which rewrites a section.

**The nine sections.** They group as the map's layout block describes: §1–5
ordered by generative formalism, §6–8 by degree of integration, §9 outside the
argument. Assembling them means writing the two block seams and smoothing the
handoffs — not re-editing section bodies.

**The review.** Front matter (introduction, then the metrics primer), the nine
sections, the gaps unit, the instruments and tables, the conclusion. Scope is argued
in Beat 1; the exclusion log stays in `candidates.md` and is never drafted.

## Placement directives

Decisions about *where* material lands and *how* it must be handled, so the map
stays content.

| Directive | Why |
|---|---|
| The metrics primer renders before §1, though it belongs with the instruments | §§1–9 quote pAE, pLDDT, ipTM and PB-valid from the start |
| The primer is written around the two families of metric, never as an alphabetical glossary | a metric list is dead weight the reader skips; the families do the analytical work |
| The Latent-X1 / RFpeptides head-to-head lands under Table B, not §9 | so it reads as evidence about measurement, not a point scored for Latent Labs |
| The map's layout block never becomes text | it turns into the intro's roadmap paragraph and the seams between sections |
| The gaps unit admits only limits a cataloged publication states | otherwise it becomes a wish list, which is the genre's standard filler |
| Developability and immunogenicity are the gaps unit's, not §9's | Latent-X2 is the evidence but the point is about the field, not about Latent Labs |
| §2 opens by separating RF3 (predictor) from RFdiffusion3 (generator) | the names collide; the lineage's two tracks are unreadable otherwise |
| AtomWorks gets one line, never a passage | it is training infrastructure, not a model or an instrument; its role is that RF3 and RFdiffusion3 both come out of it |
| Level 2 is introduced as the *oldest* idea in the review, not the newest | the §6 arc depends on the reader knowing it was tried and abandoned first |
| Table B is sorted by designs-tested, never by hit rate | the denominator is Beat 3's argument; hit-rate order makes it a leaderboard |
| Table B's hit-definition column is mandatory | BoltzProt-1's screening-hit / confirmed-binder split means the percentages measure different events |
| No cell enters Table A or B without a stated benchmark, cutoff and measurer | the provenance columns are the defence against a leaderboard reading |
| Benchmark caveats are stated once with the instruments and pointed at, never relitigated per section | three documented defects, one per prediction instrument, plus Overath's own on the design side |
| The physical-validity thread is stated once with the instruments | four groups assert four answers and only one pair has been measured against the other; per-section retelling implies more agreement than exists |

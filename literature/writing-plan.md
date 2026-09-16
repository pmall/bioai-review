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

**8,000 words of main text**, 49 references. That is the standard scale for a
journal review at this reference count — Nature Reviews, Briefings in
Bioinformatics, Annual Review. Not an exhaustive survey.

**Tables A and B are display items**, not main text, and do not count against the
budget in any of those venues. Only the paragraph between them does.

*Consequence, stated up front:* at this scale roughly 12–15 publications get
individual treatment. The rest are cited in support of a claim, sometimes in a
clause. That is correct for the genre — a review argues and cites, it does not
enumerate. Every publication in the corpus still earns its place by supporting
something; not every one gets a sentence of its own.

## Draft units

Fourteen drafts. `map.md` now carries one heading per draft, in render order, so
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
| 12 | Instruments | `drafts/11-instruments.md` | The instruments |
| 13 | Tables A and B | `drafts/12-tables.md` | Tables A and B — written after §1–§9 |
| 14 | Conclusion | `drafts/13-conclusion.md` | The conclusion — a stub; the map records the gap, not the answer |

**The layout block does not become a draft.** It turns into two things: a
short roadmap paragraph closing the introduction, and the seam sentences between
sections — the block supplies the two-axis logic, and each section's own
*Why here* line supplies the seam into it.

**The conclusion is written last, from the finished parts.** §9 is a coda and
Beat 5 sets up an ending, but nothing in the map states what the review
concludes — deliberately, and the stub there says so. What it concludes follows
from the other thirteen drafts, so it is decided when they exist rather than
planned in advance.

## Size budget

**Provisional, and expected to move.** Shares are re-derived whenever the argument
changes — the introduction grew when Beat 2 took on the co-folder anatomy and Beat
4 the generation taxonomy, and §2 grew when RF3 entered. The multiplier is the only
thing to change if the *target* moves; the shares change when the content does.
Both columns are given so switching venue is one substitution.

| Draft | Share | @ 8,000 | @ 12,000 | Why that size |
|---|---|---|---|---|
| Introduction | 15% | 1,200 | 1,800 | five beats, and it now carries the two conceptual frames the whole review reads through: the co-folder anatomy (Beat 2) and the prediction/generation taxonomy (Beat 4) |
| Metrics primer | 4.5% | 350 | 550 | two families of metric, one consequence; tight by design |
| §1 AlphaFold | 7.5% | 600 | 900 | two predictors explained properly, plus the MSA bet everything rests on |
| §2 RoseTTAFold | 11.5% | 900 | 1,400 | six backbone entries, both tracks (RF1/RFAA/RF3 and RFdiffusion 1/2/3), and it owns MPNN for the whole review |
| §3 Boltz | 10% | 800 | 1,200 | five models; owns the trained-critic result and the open→closed fork |
| §4 Chai | 5% | 400 | 600 | two papers, one with no disclosed mechanism — short, and that is the finding |
| §5 Flow matching | 4.5% | 350 | 550 | one comparative block; most of its argumentative weight now sits in Beat 4's step-count passage, not in the five papers |
| §6 Inversion | 8% | 650 | 1,000 | the five-beat arc plus four systems |
| §7 Protenix | 7% | 550 | 850 | the platform argument plus the filter-ensembling finding |
| §8 ESM | 8% | 650 | 1,000 | the climax; the MSA throughline lands here |
| §9 Closed frontier | 5% | 400 | 600 | coda, restrained on purpose |
| Instruments | 5.5% | 450 | 650 | four instruments, three caveats |
| Table commentary | 3% | 250 | 350 | the tables are display items; only the asymmetry argument is main text |
| Conclusion | 5% | 400 | 600 | currently unplanned |
| **Total** | 100% | **8,000** | **12,150** | |

*If the introduction still overruns when drafted,* the co-folder anatomy moves to
the metrics primer — which already renders before §1 and is already built to teach
one distinction before the reader needs it. That trade is the relief valve; cutting
the anatomy is not.

§1–§9 come to 5,400 at the 8,000 target — about two thirds of the review,
which is right for a review whose argument is the section order.

## What a section is

A section is a block of argument. It is **not** a list of publications with
commentary on each. Publications appear inside the prose, supporting claims;
they are not headings and they do not each get a turn.

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

**Collisions are already assigned by the map.** Each draft opens with three
lines — owns / references / must not restate — copied from the map, not
reinvented. The standing assignments: ipTM and pAE definitions to the primer,
MPNN to §2, the trained-critic result to §3, BoltzDesign1's analysis to §6,
benchmark caveats to the instruments, the disclosure argument to §9.

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
3. **Introduction** — after §1–§9, when the numbers it promises are known to
   be real and the beats can point at sections that exist.
4. **Instruments, then Tables A and B** — the tables gather the sections' numbers
   and cannot precede it.
5. **Scope and exclusions**, then **Conclusion**.

## Assembly

Two passes, neither of which rewrites a section.

**The nine sections.** They group as the map's layout block describes: §1–5
ordered by generative formalism, §6–8 by degree of integration, §9 outside the
argument. Assembling them means writing the two block seams and smoothing the
handoffs — not re-editing section bodies.

**The review.** Front matter (introduction, then the metrics primer), the nine
sections, the instruments and tables, the conclusion. Scope is argued in Beat 1;
the
exclusion log stays in `candidates.md` and is never drafted.

## Placement directives

Decisions about *where* material lands and *how* it must be handled. They were
previously embedded in `map.md`; they live here so the map stays content.

| Directive | Why |
|---|---|
| The metrics primer renders before §1, though it belongs with the instruments | §§1–9 quote pAE, pLDDT, ipTM and PB-valid from the start |
| The primer is written around the two families of metric, never as an alphabetical glossary | a metric list is dead weight the reader skips; the families do the analytical work |
| The Latent-X1 / RFpeptides head-to-head lands under Table B, not §9 | so it reads as evidence about measurement, not a point scored for Latent Labs |
| The map's layout block never becomes text | it turns into the intro's roadmap paragraph and the seams between sections |
| §2 opens by separating RF3 (predictor) from RFdiffusion3 (generator) | the names collide; the lineage's two tracks are unreadable otherwise |
| AtomWorks gets one line, never a passage | it is training infrastructure, not a model or an instrument; its role is that RF3 and RFdiffusion3 both come out of it |
| Level 2 is introduced as the *oldest* idea in the review, not the newest | the §6 arc depends on the reader knowing it was tried and abandoned first |
| Table B is sorted by designs-tested, never by hit rate | the denominator is Beat 3's argument; hit-rate order makes it a leaderboard |
| Table B's hit-definition column is mandatory | BoltzProt-1's screening-hit / confirmed-binder split means the percentages measure different events |
| No cell enters Table A or B without a stated benchmark, cutoff and measurer | the provenance columns are the defence against a leaderboard reading |
| Benchmark caveats are stated once with the instruments and pointed at, never relitigated per section | three documented defects, one per instrument |

## Open decisions

- **§5's length.** One backbone, no meat, four mentions — the only section with
  that shape. Either it compresses to a few paragraphs hung on FrameFlow, or the
  formalism thread folds into §2–4 and §5 stops being a section. Beat 4's
  step-count argument is the strongest case for keeping it: flow matching's ODE
  formulation is what makes the structure stage short enough to backpropagate
  through, which is what PXDesign-h exploits.
- **§2's budget.** Five backbone entries, the most of any section, each carrying a
  different claim. It is the longest section to draft and should be scheduled as
  such.
- **§3's tiers have not been re-derived** since the section last changed shape.
  Four backbone entries may well be right — Boltz spans the open→closed fork and
  the trained-critic result — but the per-claim justification is not written down
  the way §2's is. Settle it when §3 is drafted.

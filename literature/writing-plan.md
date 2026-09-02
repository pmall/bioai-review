# Writing plan and method

> How the review gets written: what the draft units are, how big each one is,
> what shape a section takes, and in what order they are drafted.
>
> `literature/map.md` is the layout — what goes where. This file is the method —
> how it gets turned into prose. Neither restates the other. Sizes and drafting
> order live here so the map stays a layout.

## Target

**8,000 words of main text**, 46 references. That is the standard scale for a
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

Fifteen drafts. Part I is one narrative and is not sliced. Part II never becomes
text. Part IV splits into three because its blocks have different sources,
different timing, and different positions in the final text.

| # | Draft | File | Source |
|---|---|---|---|
| 1 | Introduction | `drafts/00-intro.md` | Part I, five beats |
| 2 | Metrics primer | `drafts/01-metrics-primer.md` | Part IV, block 1 — renders before §1 |
| 3 | §1 AlphaFold and the open co-folding cluster | `drafts/02-alphafold.md` | Part III §1 |
| 4 | §2 RoseTTAFold → RFdiffusion | `drafts/03-rosettafold.md` | Part III §2 |
| 5 | §3 Boltz | `drafts/04-boltz.md` | Part III §3 |
| 6 | §4 Chai | `drafts/05-chai.md` | Part III §4 |
| 7 | §5 Flow matching | `drafts/06-flow-matching.md` | Part III §5 |
| 8 | §6 Inversion as a portable technique | `drafts/07-inversion.md` | Part III §6 |
| 9 | §7 Protenix | `drafts/08-protenix.md` | Part III §7 |
| 10 | §8 ESM | `drafts/09-esm.md` | Part III §8 |
| 11 | §9 The closed frontier | `drafts/10-closed-frontier.md` | Part III §9 |
| 12 | Instruments | `drafts/11-instruments.md` | Part IV, block 2 |
| 13 | Tables A and B | `drafts/12-tables.md` | Part IV, block 3 — written after Part III |
| 14 | Scope and exclusions | `drafts/13-excluded.md` | Part V |
| 15 | Conclusion | `drafts/14-conclusion.md` | **not yet in the map** |

**Part II does not become a draft.** It turns into two things: a short roadmap
paragraph closing the introduction, and the seam sentences between sections,
both written at assembly time from Part II's "why this order" bullets.

**The conclusion is written last, from the finished parts.** §9 is a coda and
Beat 5 sets up an ending, but nothing in the map states what the review
concludes — deliberately. What it concludes follows from the other fourteen
drafts, so it is decided when they exist rather than planned in advance.

## Size budget

Shares are fixed; the multiplier is the only thing to change if the target moves.
Both columns are given so switching venue is one substitution.

| Draft | Share | @ 8,000 | @ 12,000 | Why that size |
|---|---|---|---|---|
| Introduction | 12.5% | 1,000 | 1,500 | five beats, the collapsing-budget table, two caveats |
| Metrics primer | 4.5% | 350 | 550 | two families of metric, one consequence; tight by design |
| §1 AlphaFold | 7.5% | 600 | 900 | two predictors explained properly, plus the MSA bet everything rests on |
| §2 RoseTTAFold | 10% | 800 | 1,200 | largest roster, a real lineage, and it owns MPNN for the whole review |
| §3 Boltz | 10% | 800 | 1,200 | five models; owns the trained-critic result and the open→closed fork |
| §4 Chai | 5% | 400 | 600 | two papers, one with no disclosed mechanism — short, and that is the finding |
| §5 Flow matching | 6.5% | 500 | 800 | five papers written as one comparative block |
| §6 Inversion | 8% | 650 | 1,000 | the four-beat arc plus three systems |
| §7 Protenix | 7% | 550 | 850 | the platform argument plus the filter-ensembling finding |
| §8 ESM | 8% | 650 | 1,000 | the climax; the MSA throughline lands here |
| §9 Closed frontier | 5.5% | 450 | 650 | coda, restrained on purpose |
| Instruments | 6% | 500 | 750 | four instruments, three caveats |
| Table commentary | 3.5% | 300 | 450 | the tables are display items; only the asymmetry argument is main text |
| Scope and exclusions | 2.5% | 200 | 300 | five papers, one reason each |
| Conclusion | 5% | 400 | 600 | currently unplanned |
| **Total** | 100% | **8,150** | **12,350** | |

Part III comes to 5,400 at the 8,000 target — about two thirds of the review,
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
benchmark caveats to Part IV, the disclosure argument to §9.

## Using xrefs

`literature/xrefs.md` is not a sizing instrument. Its own header says in-degree
is confounded by publication age, so §6, §7 and §9 score low for being recent,
not for being minor. Three uses that hold:

- **It tells you the shape a section must take.** §2 has 22 citations internal
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
3. **Introduction** — after Part III, when the numbers it promises are known to
   be real and the beats can point at sections that exist.
4. **Instruments, then Tables A and B** — the tables gather Part III's numbers
   and cannot precede it.
5. **Scope and exclusions**, then **Conclusion**.

## Assembly

Two passes, neither of which rewrites a section.

**Part III.** The nine sections group as Part II describes: §1–5 ordered by
generative formalism, §6–8 by degree of integration, §9 outside the argument.
Assembling Part III means writing the two block seams and smoothing the
handoffs — not re-editing section bodies.

**The review.** Front matter (introduction, then the metrics primer), Part III,
the instruments and tables, the conclusion. Scope and exclusions goes to an
appendix or folds into the introduction's scope beat — decide at assembly.

## Open items

- Whether Part V ships as an appendix or folds into the introduction.
- The three files currently in `drafts/` predate this plan and are organized
  predictor-side vs design-side, which is not the map's organization. They are
  not inputs to any draft above.

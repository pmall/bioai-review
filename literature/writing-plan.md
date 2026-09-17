# Writing plan and method

> How the review gets written: what the draft units are, how big each one is,
> what shape a section takes, and in what order they are drafted.
>
> `literature/map.md` holds the content: every publication, every fact, every
> claim, structured in reading order — the review minus its prose. This file
> holds everything addressed to whoever writes that prose: sizes, drafting
> order, section shape, and the placement directives below. Neither restates the
> other. **No instruction to the writer belongs in the map.**

## Target

**A review of 49 references, not an exhaustive survey.** There is no word count,
here or anywhere. A draft is as long as what it carries requires; the relative
weights below are the only size constraint, and a section is too long when it
spends prose on material its tier does not warrant, never because it passed a
count.

**Tables A and B are display items**, not main text. Only the paragraph between
them is prose.

______________________________________________________________________

## Weight — the rule that governs every other rule here

A review is read for its **proportions** before it is read for its sentences. A
reader who knows this field arrives with a rough map of what matters in it, and
the fastest way to lose them is to spend three paragraphs on a preprint they
have not heard of and one clause on AlphaFold. The tier system exists to prevent
exactly that, and this section is where it becomes an instruction to the writer.

**Tier determines treatment. It is not a hint.**

| Tier         | Treatment in the prose                                                                               | Test the draft must pass                                                                |
| ------------ | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **backbone** | A passage of its own: mechanism, the numbers that matter, the caveat, and what it is contrasted with | A reader could explain what this system does and why it mattered, from the review alone |
| **meat**     | Named in a sentence or two while a backbone claim is being made; its numbers may be quoted           | Removing it weakens a claim's evidence; it does not leave a hole in the narrative       |
| **mention**  | A clause, or a parenthetical. No mechanism, no numbers in the prose — numbers go to Table A or B     | It can be read past without loss                                                        |

**Twenty publications carry the review.** They are the backbone set, and they
are the ones a reader should come away able to name:

| Section     | Gets a passage                                                    |
| ----------- | ----------------------------------------------------------------- |
| §1          | AlphaFold2 · AlphaFold-Multimer · AlphaFold3                      |
| §2          | RoseTTAFold · RFdiffusion · RFantibody · RFpeptides · ProteinMPNN |
| §3          | Boltz-1 · BoltzGen · BoltzProt-1                                  |
| §4          | Chai-2                                                            |
| §5          | FrameFlow                                                         |
| §6          | BindCraft · Germinal                                              |
| §7          | PXDesign                                                          |
| §8          | ESM-2/ESMFold · ESMC/ESMFold2 · the ESMFold2 binder campaign      |
| §9          | Latent-X1                                                         |
| Instruments | FoldBench                                                         |

Everything else in `map.md` — roughly thirty further works — appears in support
of a claim or not at all. **That is not a demotion**; the invariant that every
named publication resolves to a catalog entry is about the catalog's honesty,
not about the prose owing each one a turn.

**Three failure modes, in the order they actually happen.**

1. **The recency inversion.** Recent preprints have long, specific, quotable
   entries because they were read most recently and argue with each other in
   detail. Mastodonts have short entries because their content is assumed. A
   draft written by following entry length will invert the field's weight.
   _Check:_ if a 2026 preprint gets more prose than AlphaFold2, RFdiffusion or
   ProteinMPNN, the draft is wrong regardless of how interesting the preprint
   is.
1. **The interesting-detail trap.** A small paper with an unusual result is more
   fun to write about than a foundational one whose result everybody knows.
   Interest is not weight. A finding earns prose in proportion to what rests on
   it, and `map.md` states what rests on each entry under _Carries_.
1. **Cataloguing under the guise of completeness.** Listing five flow-matching
   papers because the corpus holds five. §5's own entry says what to do instead:
   one argument, four examples named in support.

**Where the map over-supplies, cut rather than expand.** Some entries carry more
material than their tier warrants, because the underlying paper is recent and
detailed. The map records what is true; this file decides what is written. When
the two disagree, tier wins.

## Draft units

Two layers: **drafts**, one per map heading, and the **parts** they collapse
into. A draft is written from one heading and the corpus behind it; a part is
the merge, and merging writes seams and one voice, never a rewrite of a draft.
The introduction and *From prediction to design* are written a beat at a time,
because the beats have different sources and merging is where they are made to
read as one. The map's layout block is the one heading with no draft. The three
benchmarking units are three drafts rather than one because they have different
sources, timing and positions in the final text. Excluded works are not a draft
unit — they are a record in `candidates.md`, not a part of the review.

| #   | Draft                                        | File                           | Source                                                           |
| --- | -------------------------------------------- | ------------------------------ | ---------------------------------------------------------------- |
| 1   | Scope                                        | `drafts/00-scope.md`           | The scope beat                                                   |
| 2   | The disclosure limit                         | `drafts/01-frontier.md`        | The disclosure beat                                              |
| 3   | Metrics primer                               | `drafts/02-metrics-primer.md`  | The metrics primer                                               |
| 4   | The founding bet                             | `drafts/03-anatomy.md`         | The anatomy beat                                                 |
| 5   | Prediction and generation are one machine    | `drafts/04-identity.md`        | The identity beat                                                |
| 6   | Generator–critic coupling                    | `drafts/05-coupling.md`        | The coupling beat                                                |
| 7   | §1 AlphaFold and the open co-folding cluster | `drafts/06-alphafold.md`       | §1                                                               |
| 8   | §2 RoseTTAFold → RFdiffusion                 | `drafts/07-rosettafold.md`     | §2                                                               |
| 9   | §3 Boltz                                     | `drafts/08-boltz.md`           | §3                                                               |
| 10  | §4 Chai                                      | `drafts/09-chai.md`            | §4                                                               |
| 11  | §5 Flow matching                             | `drafts/10-flow-matching.md`   | §5                                                               |
| 12  | §6 Inversion as a portable technique         | `drafts/11-inversion.md`       | §6                                                               |
| 13  | §7 Protenix                                  | `drafts/12-protenix.md`        | §7                                                               |
| 14  | §8 ESM                                       | `drafts/13-esm.md`             | §8                                                               |
| 15  | §9 The closed frontier                       | `drafts/14-closed-frontier.md` | §9                                                               |
| 16  | What the field has not shown                 | `drafts/15-gaps.md`            | The gaps unit — four stated limits, written after §1–§9          |
| 17  | Instruments                                  | `drafts/16-instruments.md`     | The instruments                                                  |
| 18  | Tables A and B                               | `drafts/17-tables.md`          | Tables A and B — written after §1–§9                             |
| 19  | Conclusion                                   | `drafts/18-conclusion.md`      | The conclusion — a stub; the map records the gap, not the answer |

The parts they collapse into:

| Part                      | File                                   | Merges                                                |
| ------------------------- | -------------------------------------- | ----------------------------------------------------- |
| Introduction              | `drafts/parts/intro.md`                | drafts 1–2, plus the layout block's roadmap paragraph |
| From prediction to design | `drafts/parts/prediction-to-design.md` | drafts 4–6                                            |
| The nine sections         | `drafts/parts/sections.md`             | drafts 7–15                                           |

Drafts 3 and 16–19 stand on their own; the metrics primer renders between the
two front-matter parts, and the rest close the review.

**The layout block does not become a draft.** It turns into two things: a short
roadmap paragraph closing the introduction, and the seam sentences between
sections — the block supplies the two-axis logic, and each section's own _Why
here_ line supplies the seam into it.

**The conclusion is written last, from the finished parts.** §9 is a coda and
the disclosure beat sets up an ending, but nothing in the map states what the
review concludes — deliberately, and the stub there says so. What it concludes
follows from the other drafts, so it is decided when they exist rather than
planned in advance.

**The gaps unit has a hard rule and it is the map's, not this file's:** a gap
enters only when a publication in the catalog states it. The unit is four items
long for that reason, and it is not the place to speculate about what comes
next. It is drafted after §1–§9 because three of its four items are limits those
sections establish and one is Tables A and B's.

## Relative weight

**How much of the review each draft should occupy relative to its neighbours — a
proportion, never a target to hit.** The **column that matters is the backbone
count**, because that is what the share is derived from.

_Weights are re-derived when the argument moves, never when a paper arrives._

| Draft                     | Backbones | Share | Why that weight                                                                                                                                    |
| ------------------------- | --------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Introduction              | —         | 5%    | the problem, the scope argument, the disclosure limit, the roadmap                                                                                 |
| Metrics primer            | —         | 4%    | two families of metric, one consequence; tight by design                                                                                           |
| From prediction to design | —         | 7.5%  | the two frames the whole review reads through — the co-folder anatomy and the coupling taxonomy — plus the designs-tested spine                    |
| §1 AlphaFold              | 3         | 10%   | the three papers everything else is defined against, and the MSA bet the review's longest thread starts from                                       |
| §2 RoseTTAFold            | 5         | 12.5% | the most backbones of any section — the second origin, the generative turn, the antibody and macrocycle arms, and ProteinMPNN for the whole review |
| §3 Boltz                  | 3         | 9.5%  | the open AF3-class model, the cleanest Level 0, and the trained-critic result                                                                      |
| §4 Chai                   | 1         | 4.5%  | the corpus's strongest antibody result from an undisclosed generator — short, and that is the finding                                              |
| §5 Flow matching          | 1         | 3%    | one argument with four examples, not five papers taking turns; its weight sits in the coupling beat's step-count passage                           |
| §6 Inversion              | 2         | 8%    | the five-step arc plus BindCraft and Germinal; the other four systems are evidence, not subjects                                                   |
| §7 Protenix               | 1         | 6.5%  | the platform argument plus the filter-ensembling finding                                                                                           |
| §8 ESM                    | 3         | 9%    | the climax: the MSA throughline lands and the coupling axis ends                                                                                   |
| §9 Closed frontier        | 1         | 4.5%  | coda, restrained on purpose — restraint is the argument                                                                                            |
| Gaps                      | —         | 4%    | four stated limits, each pointing at the entry that evidences it; no speculation                                                                   |
| Instruments               | 1         | 5%    | four instruments; three prediction-side defects plus Overath's own, stated once                                                                    |
| Table commentary          | —         | 3%    | display items; only the asymmetry argument is main text                                                                                            |
| Conclusion                | —         | 4%    | written from the finished parts                                                                                                                    |
| **Total**                 | **21**    | 100%  |                                                                                                                                                    |

**The check this table exists for:** §1 outweighs §6, §7 and §9; §2 outweighs
everything. If a draft comes back the other way round, the recency inversion has
happened and the fix is to cut the recent material, not to argue for it.

§1–§9 come to about two thirds of the review, which is right for a review whose
argument is the section order.

## What a section is

A section is a block of argument. It is **not** a list of publications with
commentary on each. Publications appear inside the prose, supporting claims;
they are not headings and they do not each get a turn.

**Its backbones are its subjects; everything else is evidence.** A section with
three backbones has three things to explain properly and a supporting cast.
Prose spent on the cast is prose taken from the subjects — that is the trade,
and it is always the wrong way round when a _mention_ has a sentence to itself.

**Read the entry schema before drafting a section.** `map.md`'s header defines
it: each entry's _Carries_ line is the claim that must survive into the prose,
_Against_ is the comparison the passage should be built around, _Caveat_ travels
with the claim wherever it is cited, and _Collision_ says what this section must
not restate. A backbone passage that states what a system _is_ without stating
what it is **against** has described a paper instead of making an argument.

Every section makes the same four moves, in this order. This is what keeps nine
independently drafted sections reading as one review:

1. **The claim.** What this lineage or technique contributed, stated as a
   proposition. Not a preview of what the section will cover.
1. **The mechanism.** What these models actually do — told once for the whole
   section, from the parsed corpus, rather than restarted for each paper.
1. **The evidence.** Benchmarks and wet-lab campaigns, with the caveat that
   applies to them.
1. **The handoff.** Where the section sits on the coupling spine, and the seam
   into the next section.

**A section draft that could have been written from the map alone has failed.**
The map's own header says what it refuses to hold: _"Method internals, benchmark
numbers, per-paper caveats and quotes are read out of the corpus at writing
time."_ That material is exactly what a section draft is made of, and it comes
from `literature/corpus/`, not from the map entry.

**Collisions are already assigned by the map.** Each draft opens with three
lines — owns / references / must not restate — copied from the map, not
reinvented. The standing assignments: ipTM and pAE definitions to the primer,
ProteinMPNN to §2, AtomWorks to §2 in one line, the trained-critic result to §3,
BoltzDesign1's analysis to §6, the groups-versus-architectures qualification to
§6's step 4, mBER's unchosen-targets argument to the identity beat, the
physical-validity thread and all benchmark caveats to the instruments, and the
disclosure argument to §9.

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
1. **§1 → §9 in map order** — already dependency order, per the matrix above.
   **Budget the time by backbone count:** §2 carries five and is the longest to
   draft, §1, §3 and §8 three each, and §4, §5, §7 and §9 one apiece.
1. **The five beats** — after §1–§9, when the numbers they promise are known to
   be real and they can point at sections that exist.
1. **Instruments, then Tables A and B** — the tables gather the sections'
   numbers and cannot precede it.
1. **The gaps unit**, which needs §1–§9 and both tables to exist first.
1. **Conclusion.**

## Assembly

Drafts merge into parts, parts into the review. No pass rewrites a draft.

**The nine sections.** They group as the map's layout block describes: §1–5
ordered by generative formalism, §6–8 by degree of integration, §9 outside the
argument. Assembling them means writing the two block seams and smoothing the
handoffs — not re-editing section bodies.

**The review.** Front matter (introduction, the metrics primer, then *From
prediction to design*), the nine sections, the gaps unit, the instruments and
tables, the conclusion. Scope is argued in the scope beat; the exclusion log
stays in `candidates.md` and is never drafted.

## Placement directives

Decisions about _where_ material lands and _how_ it must be handled, so the map
stays content.

| Directive                                                                                                                   | Why                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| The metrics primer renders between the introduction and *From prediction to design*, though it belongs with the instruments | the coupling beat and §§1–9 quote pAE, pLDDT, ipTM and PB-valid from the start                                                                  |
| The primer is written around the two families of metric, never as an alphabetical glossary                                  | a metric list is dead weight the reader skips; the families do the analytical work                                                              |
| The Latent-X1 / RFpeptides head-to-head lands under Table B, not §9                                                         | so it reads as evidence about measurement, not a point scored for Latent Labs                                                                   |
| The map's layout block never becomes text                                                                                   | it turns into the intro's roadmap paragraph and the seams between sections                                                                      |
| The gaps unit admits only limits a cataloged publication states                                                             | otherwise it becomes a wish list, which is the genre's standard filler                                                                          |
| Developability and immunogenicity are the gaps unit's, not §9's                                                             | Latent-X2 is the evidence but the point is about the field, not about Latent Labs                                                               |
| §2 opens by separating RF3 (predictor) from RFdiffusion3 (generator)                                                        | the names collide; the lineage's two tracks are unreadable otherwise                                                                            |
| AtomWorks gets one line, never a passage                                                                                    | it is training infrastructure, not a model or an instrument; its role is that RF3 and RFdiffusion3 both come out of it                          |
| Level 2 is introduced as the _oldest_ idea in the review, not the newest                                                    | the §6 arc depends on the reader knowing it was tried and abandoned first                                                                       |
| Table B is sorted by designs-tested, never by hit rate                                                                      | the denominator is the identity beat's argument; hit-rate order makes it a leaderboard                                                          |
| Table B's hit-definition column is mandatory                                                                                | BoltzProt-1's screening-hit / confirmed-binder split means the percentages measure different events                                             |
| No cell enters Table A or B without a stated benchmark, cutoff and measurer                                                 | the provenance columns are the defence against a leaderboard reading                                                                            |
| Benchmark caveats are stated once with the instruments and pointed at, never relitigated per section                        | three documented defects, one per prediction instrument, plus Overath's own on the design side                                                  |
| The physical-validity thread is stated once with the instruments                                                            | four groups assert four answers and only one pair has been measured against the other; per-section retelling implies more agreement than exists |

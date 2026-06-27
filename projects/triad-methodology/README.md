---
title: Triad — Multi-Model Analysis Methodology
tags: [portfolio, ai-infra, methodology, flagship]
status: draft
created: 2026-06-26
---

# The Triad

> A method for routing one problem through several models in distinct roles — built to surface where they *disagree*, not to manufacture a consensus answer.

## The problem it solves

The intuitive failure mode of AI analysis is a wrong answer. The dangerous one is a *confident, convergent* answer where every model agrees — because they all inherited the same blind spot from the same framing. When three models concur, it feels like strong evidence. It usually isn't: convergence is weaker evidence than it feels, and shared blind spots, not disagreement, are the real risk.

The Triad is built specifically to resist that. Its goal is the opposite of consensus tooling: keep the perspectives apart long enough to see what one of them caught that the others missed.

## The roles

Each model runs in a deliberate role, not as a redundant voter:

- **Framer** — drafts the initial concept document fast. Sets the problem up but doesn't get the last word.
- **Divergent critic** — critiques the *concept only*, with no access to the raw artifacts. This restriction is the key design choice (below).
- **Deep analyzer** — works at the artifact level with full repository/file access, grounding or refuting the concept against what's actually there.
- **Synthesizer** — reconciles the three, explicitly *crediting where they diverged* and naming the dimension all of them may have missed.

## The one design choice that makes it work

The critic sees the concept, not the artifacts — on purpose. If it saw the same raw material the framer did, it would anchor on the same details and produce agreement dressed up as a second opinion. Starving it of the artifacts forces a genuinely independent vantage. The disagreement it produces is *signal*, not noise, precisely because it wasn't looking at the same evidence.

The dispatch across these stages is automated by an orchestrator script, so the method is a repeatable pipeline rather than a manual ritual.

## The honest limitation (and the fix in progress)

The Triad has a known weakness I haven't fully closed: if the *framer's* initial framing misses a dimension, all three roles can converge on an incomplete answer — the framer defines the box everyone else reasons inside. The disagreement machinery doesn't help if the disagreement is all happening within a shared, wrong frame.

The fix I'm building is a **Stage 0 cold-framing** step: an independent framing pass before the main framer's, so the problem gets defined from two unrelated starting points and a missed dimension has a second chance to surface. Documenting the limitation is part of the method — a methodology that only advertises its strengths is one I wouldn't trust.

## What it has actually produced

- **Validated a business thesis under pressure.** The Law AERP vertical thesis was run through the Triad across six-plus rounds before committing to it — the divergent critic's job was specifically to attack the framing, not flatter it.
- **Surfaced a real research tension.** Two models scoring the same output diverged systematically — one on *craft*, one on *novelty* — which exposed that "quality" in automated analysis isn't a single scalar. The Triad didn't resolve it; it made the tension visible, which is the point.

## What this demonstrates

- I can **orchestrate multiple models as a system** with differentiated roles, not just prompt them in parallel.
- I design **against the failure mode that actually bites** — confident convergence — rather than the one that's easy to picture.
- I hold a methodology to the same standard I'd hold a system: state its limits, build the fix, document both.

---

*Applied in: [Hermes Agent Platform — Case Study] · used to validate [Law AERP].*

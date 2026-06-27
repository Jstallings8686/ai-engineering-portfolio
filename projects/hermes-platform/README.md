---
title: Hermes Agent Platform — Case Study
tags: [portfolio, ai-infra, agents, flagship]
status: draft
created: 2026-06-26
---

# Hermes Agent Platform

> A local, multi-model agent system with persistent identity, durable memory, and a self-directed background process that analyzes its own knowledge base while I'm not watching.

## Why it exists

Off-the-shelf agents forget everything between sessions, depend on a cloud endpoint, and do exactly what you tell them and nothing more. I wanted an agent platform that runs locally, holds state across sessions, coordinates multiple models by role, and does useful work autonomously — not a chatbot, an operating layer. Hermes is that platform. Most of the engineering below is about the unglamorous parts that make autonomy trustworthy: memory that's honest, selection that can't get stuck, and state you can actually inspect.

## Centerpiece: the Dreaming Agent

The Dreaming Agent is an autonomous cognitive cycle that runs every 90 minutes on a cron schedule. Each cycle it selects an under-examined note from the knowledge vault, analyzes it, and writes the result to durable memory. It's an original system, not a configuration — and its history is the clearest example of how I build.

The first version used a multi-factor scorer to pick which note to analyze. It kept locking onto the same handful of notes. The instinct most people have is to tune the scoring weights. I did the opposite: I **replaced the scorer with a deliberately dumb picker** — an eligibility gate followed by "least-recently-dreamed, random tiebreak." That made lock-on *structurally impossible* rather than statistically unlikely. Verification across a ~196-note vault (~117 never analyzed at audit time) confirmed it now spreads correctly. The lesson I keep applying: a structural fix beats tuning a heuristic, because it removes the failure mode instead of making it rarer.

Two more decisions from the same refactor are worth naming because they're the kind of thing that separates a demo from a system:

- **Honest async state via lagged reconciliation.** The agent's "journal written" flag was optimistic — it claimed success before the write was confirmed. Rather than try to verify an in-flight write, I had each cycle reconcile the *previous* cycle's output. State became truthful without fragile real-time checks.
- **Observability as a primitive.** I'd repeatedly found components that were built but never confirmed to actually fire — a failure mode I now actively guard against. So per-cycle counters (eligible notes, skipped-unchanged) are emitted as a first-class part of the agent, making its behavior inspectable without a debugger dive.

## Identity and memory architecture

Hermes agents persist across sessions through a layered design I built: a `SOUL.md` carrying instance-wide persona and behavioral stance, a `MEMORY.md` for project-specific facts and decision history, and a `USER.md` briefing the agent on who it's working for. Session continuity runs through a local SQLite store — and a hard-won detail: continuation has to be explicit (a `--continue` flag), or the agent silently spins up a blank slate and ignores everything it knew. Memory you *think* you have but don't is worse than no memory; making continuity explicit was the fix.

## Orchestration and tooling

- **Multi-model by role (the Triad).** A fast framer drafts, a divergent critic operates on the concept only, and a deep analyzer works with full repo access — synthesized so that *disagreement* is preserved rather than averaged away. (Documented separately as its own methodology piece.)
- **Planner/executor split.** Hermes plans architecture; a coding agent (OpenCode) runs the build-and-verify loop directly in the repo. A discipline that came out of this: catching collateral damage when an agent-dispatched refactor deletes still-needed code, before it ships.
- **MCP sidecars for zero-hallucination tools.** Migrating from static text-file "skills" to Model Context Protocol sidecars decouples tool execution from the model — JSON schemas hand off to native Python/Bash, so a tool either runs correctly or fails loudly, instead of the model hallucinating a result.

## Operating it like infrastructure

The platform runs as an ecosystem of scheduled jobs — roughly eight cron pipelines spanning data collection, analysis, consolidation, and delivery — plus an agent-to-agent bridge for cross-process coordination. *(The bridge coordinates with a second operator's agent; the documentable artifact here is the protocol design, not the coordination content.)* I authored eight original agent skills — spanning multi-model analysis, source-verification gating, platform-specific scraping, Windows RAM recovery, and an agent-to-agent messaging protocol; the number that matters isn't the total installed, it's how many I wrote and why.

## A finding worth keeping

When I had two models score the same analysis for quality, they diverged systematically: one rated on *craft* (does it follow a sound template), the other on *novelty* (does it say something non-obvious). That's not noise — it surfaced a real question about what "quality" even means for automated analysis, and it's an open methodological tension I'm still resolving. I mention it because noticing it is the work; pretending automated quality is a solved scalar would be the easy, wrong move.

## Honest constraints

A few functions from the pre-refactor design are now orphaned and flagged for a cleanup pass — I know they're there; they're scheduled, not forgotten. The platform is single-operator and runs on the sovereign lab's hardware, so it inherits that lab's awake-host constraint. These are tracked, not hidden.

## What this demonstrates

- I design **autonomous systems**, not agent configs — with the boring guarantees (honest state, inspectable behavior, non-degenerate selection) that make autonomy safe to leave running.
- I reach for **structural fixes over heuristic tuning**, and I can articulate why.
- I treat **"built but not verified" as a real failure mode** and engineer observability to catch it.
- I can **orchestrate multiple models by role** and preserve their disagreement instead of collapsing it.

---

*Related: [Triad — methodology] · [Sovereign Inference Lab — Case Study] (the hardware this runs on).*

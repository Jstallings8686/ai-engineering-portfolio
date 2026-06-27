# AI Engineering Portfolio

**Johnnie Stallings** | Network Engineer → AI Systems Builder

This portfolio documents applied AI infrastructure engineering — local-first, privacy-conscious systems built on constrained consumer hardware. Each project below is a working system with documented architecture, failure modes, and honest constraints.

## Projects

### [Sovereign Inference Lab](./projects/sovereign-inference-lab/)
Production-grade LLM agents fully offline on a single 4 GB consumer GPU. Brain + Head split architecture, KV-cache budgeting, boundary enforcement through continuous audit.
- [Case Study](./projects/sovereign-inference-lab/README.md)

### [Hermes Agent Platform](./projects/hermes-platform/)
A local, multi-model agent system with persistent identity, durable memory, and an autonomous Dreaming Agent that analyzes its own knowledge base on a schedule. Original system design with honest-state verification, structural fixes over heuristic tuning, and role-based model orchestration.
- [Case Study](./projects/hermes-platform/README.md)

### [Triad — Multi-Model Analysis Methodology](./projects/triad-methodology/)
A method for routing problems through multiple models in distinct roles — built to surface where they disagree rather than manufacture consensus. Divergent critic, deep analyzer, framer, and synthesizer roles with a Stage 0 cold-framing fix for shared blind spots.
- [Case Study](./projects/triad-methodology/README.md)

### [Repository Health Monitor](./projects/repo-health-monitor/)
Automated change detection and reporting system — zero external dependencies, cross-platform (Windows + Linux), persistent baseline tracking.
- [Project Docs](./projects/repo-health-monitor/)

## Engineering Themes

| Theme | Evidence |
|-------|----------|
| Systems that run on the hardware you have, not the hardware you wish you had | Sovereign Inference Lab — 4 GB VRAM budget, KV-cache control |
| Structural fixes over heuristic tuning | Dreaming Agent — replaced scorer with dumb picker to make lock-on structurally impossible |
| Honest state and observability | Lagged reconciliation, per-cycle counters, inspectable agent behavior |
| Security as continuous defense | Upstream dependency regression caught during routine config audit |
| Multi-model orchestration | Triad methodology — preserving divergence across model roles |
| Knowing what not to build | Deferred features listed explicitly in every project |

## Resume

[View Full Resume](./RESUME.md) — Applied AI Engineer, local & on-prem LLM systems.

---

*Last updated: June 2026*

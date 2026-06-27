---
title: Resume — Johnathan Stallings
tags: [career, resume]
status: draft
created: 2026-06-26
---

# Johnathan Stallings

**Applied AI Engineer — Local & On-Prem LLM Systems**

Los Angeles, CA · Jastallings76@gmail.com · github.com/Jstallings8686 · linkedin.com/in/johnathan-stallings-65ab64229
Open to on-site roles in the LA area · open to relocation under the right conditions

---

## Summary

Self-directed AI engineer who builds local, offline-first LLM systems end-to-end — from raw idea to a working product a real user could run. Specialized in sovereign / on-premises AI: capable agents running on constrained consumer hardware with no cloud dependency and no data leaving the building. Comfortable across the full stack of the problem — inference optimization, multi-agent orchestration, autonomous pipelines, and shipping the result as something a non-technical customer can actually use. Currently building and piloting a vertical AI product for legal practices.

---

## Technical Skills

**AI / LLM:** local inference (Ollama, llama.cpp), multi-model orchestration, agent frameworks, quantization & VRAM/KV-cache optimization, MCP tool integration, RAG, prompt and context engineering
**Languages & tooling:** Python, Bash, Rust (proxy/perf work), Git, SQLite, Streamlit
**Systems & infra:** Linux (Kali), Windows host administration, cron pipeline orchestration, role-based auth, encrypted backup, networking, distributed/cross-machine serving
**Practice:** controlled experimentation, observability instrumentation, deterministic safety gating, spec-driven development

---

## Projects

*Detailed case studies: github.com/Jstallings8686*

### Sovereign Inference Lab — local, offline LLM infrastructure
Designed and built a fully offline AI environment running production-grade, tool-using agents on a single 4 GB consumer GPU. Split-role architecture (dedicated inference host + lightweight orchestration client) over a private LAN, with the entire system operable air-gapped — no cloud, no external endpoint in the path.
- Diagnosed and fixed a KV-cache overflow from uncapped context windows; established VRAM-budgeting discipline (defensive context ceilings, per-model schemas) that kept agents stable on constrained hardware.
- Caught and removed an upstream dependency that silently introduced external data-egress, preserving the fully-local guarantee — security vigilance against my own toolchain.

### Hermes Agent Platform — autonomous multi-agent system
Built a local agent platform with persistent identity/memory and a self-directed background process that analyzes its own knowledge base on a 90-minute cycle.
- Replaced a brittle multi-factor selection scorer with a structurally simple design (eligibility gate + least-recently-used picker), eliminating a lock-on failure mode by construction rather than tuning.
- Engineered honest asynchronous state (lagged reconciliation) and per-cycle observability after repeatedly finding components that were built but never verified to fire.
- Authored 8 original agent skills spanning research, devops, and communication (multi-model analysis, source-verification gating, platform scraping, Windows RAM recovery, agent-to-agent messaging); integrated vector storage (Chroma) as durable memory.

### Triad — multi-model analysis methodology
Designed a repeatable pipeline that routes one problem through multiple models in differentiated roles (framer, concept-only critic, artifact-level analyzer, synthesizer) to surface disagreement rather than manufacture consensus — built specifically to resist convergence bias and shared blind spots. Documented its known limitations and the in-progress fix.

### Law AERP — vertical AI product for legal practices *(in pilot)*
Built a private, on-prem AI system for law firms that turns messy intake documents into a source-cited, attorney-ready matter packet locally. Includes five deterministic legal-safety gates (e.g., conflict-check enforced before matter open), role-based access, encrypted backup, and auditable packet export. Currently structuring a paid pilot offering.

---

## Education

**Santa Monica College** — Computer Science coursework, transfer track toward UCLA (Apr 2019 – Sep 2020)
**Santa Monica High School** — graduate

**Certifications (in progress):** CompTIA Security+ (SY0-701) · CompTIA Network+

---

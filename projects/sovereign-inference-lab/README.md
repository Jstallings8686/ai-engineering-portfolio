---
title: Sovereign Inference Lab — Engineering Case Study
tags: [portfolio, ai-infra, sovereign-ai, engineering]
status: draft
created: 2026-06-26
---

# Sovereign Inference Lab

> Production-grade LLM agents running fully offline on a single 4 GB consumer GPU — so that sensitive work never has to touch a cloud server.

## Why it exists

Plenty of work can't be sent to a hosted AI API — privileged, regulated, or confidential material that legally or contractually has to stay in-house. The default industry answer is "trust our cloud," which isn't an answer for anyone whose whole constraint is that the data can't leave.

So I built the alternative as a working system: capable agentic AI that runs entirely on hardware the operator controls, with nothing sensitive ever leaving the machine. The lab is the proof that offline, sovereign AI isn't a slogan — it runs, it's fast enough to be useful, and the boundary is verifiable by hand.

## The demonstration that matters

Disconnect the internet. The agents keep working.

Inference, tool-calling, file manipulation, and memory all run on local hardware over a private LAN — no external endpoint is anywhere in the path. The system has no dependency on a cloud provider being up, a subscription being current, or data being allowed to leave. The guarantee isn't a policy you have to trust; it's a property you can watch hold when you pull the cable.

(There's a portable variant too — a self-contained agent workspace on an encrypted USB drive with portable Python/Node runtimes — for the fully air-gapped, single-device case.)

## Architecture: Brain and Head

Two machines, split by role, so neither bottlenecks the other:

- **The Brain** — a Windows 11 host carrying the RTX 3050 (4 GB VRAM). It runs the inference server on the local network and does nothing but tensor processing. All GPU work lands here.
- **The Head** — a Kali Linux machine running the agent frameworks, orchestration, and filesystem work. Its local inference service is disabled by design, so 100% of model execution routes to the Brain.

The split is the point. The constrained GPU never competes with the orchestration layer for resources, and the Head stays a lightweight control plane. The working knowledge base stays identical across both machines via a Git-based sync — no cloud sync app in the loop, consistent with the offline posture.

## Engineering inside a 4 GB budget

This is where the real work is. 4 GB of VRAM is an unforgiving constraint, and most of the lab's engineering is about respecting it precisely instead of hoping it works.

The instructive failure: an uncapped context window (133K tokens on a Gemma variant) forced the runtime to pre-allocate an enormous KV cache, overflowing the GPU. The symptom wasn't a clean crash — it was silent CPU offloading and an agent that quietly lost the ability to call tools or hold state. The kind of bug that looks like "the model got dumber" until you find the real cause.

The fix was a discipline, not a patch: treat VRAM as a hard budget and cap context defensively to a fixed, conservative ceiling, with custom model schemas per model. Model selection follows the same logic — the daily-driver agent runs Hermes-3-Llama-3.2-3B specifically because at ~2 GB it fits *with* a 64K context and still generates clean JSON tool arguments. Heavier reasoning is routed off-box through a separate interface rather than forced onto a GPU that can't hold it. Knowing what *not* to run locally is part of the optimization.

## Enforcing the boundary, not just claiming it

An offline guarantee is only as good as your willingness to audit it. During a routine update, a merged upstream dependency silently introduced a default web-search integration that pointed agent traffic at an external server. Nothing in the UI announced it. I caught it during a config audit, traced it, and removed the untrusted integration to restore the fully-local state.

It's a small story with a large point: the boundary is something I actively defend against regressions — including ones introduced by my own toolchain — rather than a claim made once and never rechecked.

## A debugging note

While extending a compression proxy to shrink command payloads, I inadvertently compressed the agent's *outgoing* JSON tool-call responses too — which broke tool execution entirely ("the agent's hands stopped working"). The fix was scope, not cleverness: strip compression specifically off the tool-call path and keep those payloads pure. A small bug, but the right instinct — when an optimization breaks something, narrow its blast radius instead of tuning around the symptom.

## What it doesn't do (yet)

Honest constraints: the GPU sleeps when idle, so always-on messaging currently depends on the host being awake (roadmap: a small VPS gateway over a WireGuard tunnel with Wake-on-LAN, to keep the GPU off until needed). The stack is still bare-metal rather than containerized (roadmap: Docker Compose with NVIDIA passthrough once it's a stable multi-service deployment). These are deliberate sequencing choices, not gaps I'm unaware of.

## What this demonstrates

- I can run real, tool-using AI agents **fully offline on constrained consumer hardware** — the hard version of the problem, not the cloud-budget version.
- I design **around** hardware limits (VRAM budgeting, KV-cache control, role-split architecture) instead of pretending they aren't there.
- I treat a security boundary as something to **audit and defend continuously**, including against my own dependencies.
- The whole thing is **verifiable by inspection** — the core property of sovereign infrastructure is that you don't have to take my word for it.

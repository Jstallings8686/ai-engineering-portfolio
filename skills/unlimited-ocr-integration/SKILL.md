---
name: unlimited-ocr-integration
description: >
  Chain Unlimited-OCR → ZeroLeak → MemPalace to turn a scanned document into
  structured, searchable data — locally. Use when a user drops a scanned PDF or
  image that needs text extraction and structuring, and ZeroLeak alone can't read
  the input format. Do not use on documents that are already digital text.
tags: [ocr, document-processing, local-ai]
version: 1.1.0
author: Johnathan Stallings
---

# Unlimited-OCR Integration

> Extracts text from a scanned PDF or image, structures it, and indexes it for
> search — with a confidence gate that stops the chain before bad OCR can poison
> downstream structuring or durable memory.

## When to use this skill

- **Use when:** the user drops a scanned PDF or image of a document.
- **Use when:** ZeroLeak alone can't handle the input format (it needs text, the input is pixels).
- **Do NOT use when:** the document is already digital/selectable text — skip OCR and send it straight to ZeroLeak.

## How it works

A three-stage pipeline with a gate after each stage that can fail. The pipeline
**halts on a failed gate** and returns a structured failure — it never passes
low-trust data forward.

1. **OCR** — run Unlimited-OCR (3.3B, ~2 GB VRAM) on the input file.
   - **Gate 1 — OCR confidence:** if mean confidence `< 0.7`, **halt.** Do not
     call ZeroLeak. Return the raw OCR text + the score so a human can decide.
     (Low-confidence OCR fed into structuring produces confident nonsense — the
     worst kind, because it looks valid.)

2. **Structure** — feed the OCR text to ZeroLeak.
   - **Gate 2 — valid output:** if ZeroLeak doesn't return parseable JSON, **halt.**
     Return the OCR text + the structuring error. Nothing gets indexed.

3. **Index** — write the structured result to MemPalace.
   - **Gate 3 — confirmed write:** do not assume the index succeeded — *confirm* it
     (read back / check the returned id). If confirmation fails, **halt** and report
     unindexed. An unconfirmed write that's reported as success silently corrupts
     durable memory, which then pollutes every future retrieval. (Same lesson as the
     Dreaming Agent's `journal_written`: confirmed, never assumed.)

Only after all three gates pass does the skill report success.

## Inputs and outputs

- **Expects:** a file path to a scanned PDF or image.
- **Produces (success):** `{ status: "ok", data: <structured JSON>, mempalace_id: <id> }`
- **Produces (failure):** `{ status: "blocked", stage: <ocr|structure|index>, reason: <text>, ocr_text: <raw>, ocr_confidence: <score> }`
  — the caller can always tell success from failure, and nothing partial is left indexed.

## Gates and guardrails

| Gate | Between | Condition to pass | On fail |
|------|---------|-------------------|---------|
| 1 | OCR → ZeroLeak | mean confidence ≥ 0.7 | halt, return raw text + score |
| 2 | ZeroLeak → MemPalace | output parses as valid JSON | halt, return text + error |
| 3 | MemPalace → done | write confirmed (id read back) | halt, report unindexed |

No stage proceeds on an unverified prior stage. Partial failures never leave a
corrupted entry in durable memory.

## Verification

Smoke test the *whole chain*, including the unhappy path:

- [ ] A clean scan runs end-to-end and returns `status: "ok"` with a confirmed `mempalace_id`.
- [ ] A deliberately blurry/low-quality scan trips Gate 1 and returns `status: "blocked", stage: "ocr"` — and nothing is indexed.
- [ ] A malformed-structuring case trips Gate 2 — and nothing is indexed.
- [ ] Re-querying MemPalace returns the indexed document for the success case only.

## Pitfalls

- **Putting the confidence check in "verification" instead of as a gate** → it runs
  *after* the chain, too late to stop bad data propagating. Gate placement (between
  steps) is the point.
- **Reporting success on an unconfirmed MemPalace write** → silent durable-memory
  corruption. Always read back.
- **Returning only the success shape** → the caller can't distinguish "done" from
  "silently failed." Always return the structured failure object too.

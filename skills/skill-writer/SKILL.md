---
name: skill-writer
description: >
  Create clean, well-structured agent skills from a repeatable template. Use when
  you're starting a new skill from scratch, reviewing an existing skill for missing
  sections, or reformatting rough notes into a publishable SKILL.md.
tags: [skills, markdown, documentation, templates]
version: 1.0.0
author: Johnathan Stallings
---

# Skill Writer

> A reusable format for writing agent skills that are consistent, scannable, and
> easy for an agent to load and act on.

## When to use this skill

- Use when: starting a new skill from scratch and need a structure to fill
- Use when: reviewing an existing skill that feels incomplete or hard to follow
- Use when: converting rough notes or a terminal transcript into a proper skill
- Do NOT use when: you need to write a one-off script or document that won't be
  loaded as a skill by an agent

## How it works

1. Copy the frontmatter block below and fill in the metadata fields (name,
   description, tags, version, author).
2. Copy the section headings that are relevant — you don't need all of them.
   The only requirement is valid YAML frontmatter.
3. Write each section in plain markdown, prioritizing:
   - Concrete trigger conditions ("Use when X happens")
   - Numbered steps the agent follows in order
   - Copy-pasteable commands where applicable
4. Run the verification checklist before publishing.
5. Save as `skills/<skill-name>/SKILL.md`.

### Frontmatter template

```yaml
---
name: skill-name-here
description: >
  [WHAT it does in one clause] + [WHEN to use it]. The "Use when…" half is the
  trigger — it's what an agent reads to decide whether to load this skill, so make
  the conditions concrete and specific.
tags: [domain, action, subject]
version: 1.0.0
author: Johnathan Stallings
---
```

### Section template

```markdown
## When to use this skill
- Use when: [specific condition]
- Use when: [another concrete trigger]
- Do NOT use when: [look-alike case]

## How it works
1. [First step]
2. [Next step]
3. [Decision point: if X, do this; if Y, do that]

## Inputs and outputs
- **Expects:** [what must be true / what context is needed]
- **Produces:** [the concrete artifact or result]

## Gates and guardrails  (delete if not needed)
- [Hard rule that must hold]

## Verification
- [ ] [Observable check that proves it worked]
- [ ] [Edge case that's easy to get wrong]

## Pitfalls
- [Specific mistake], because [why it happens] → [what to do instead]

**Bad vs. good:**
Bad:  description: "Helps with documents."
Good: description: "Extract structured fields from invoices/receipts. Use when a
       user drops a financial document and wants the data as JSON/CSV."
```

## Inputs and outputs

- **Expects:** A Markdown editor, a rough idea of what the skill should do, and
  the agent skill directory available at `~/.hermes/skills/`.
- **Produces:** A valid `SKILL.md` file ready for the skill directory.

## Verification

- [ ] YAML frontmatter parses correctly with all required fields (name, description,
      tags, version, author)
- [ ] "Bad vs. good" examples are included if the skill has a common miswrite risk
- [ ] Steps are copy-pasteable where they're commands
- [ ] Trigger conditions are concrete enough that an agent can self-select

## Pitfalls

- Loading a skill with invalid YAML frontmatter — the frontmatter must have `---`
  on lines by themselves.
- Writing a description without a trigger condition — "Helps with documents" tells
  neither the user nor the agent when to use it.
- Padding optional sections (Gates, Inputs/Outputs) when they have nothing to say.
  Delete them instead.

**Bad vs. good:**

```
Bad:  description: "Helps with documents."
Good: description: "Extract structured fields from invoices/receipts. Use when a
       user drops a financial document and wants the data as JSON/CSV."
```

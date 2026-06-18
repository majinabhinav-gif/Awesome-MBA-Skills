---
name: pm-master
description: Master orchestrator for the full product management lifecycle — jobs-to-be-done, discovery, prioritization, strategy, roadmapping, and user stories — plus turning any of those outputs into a polished slide deck or spreadsheet. Use when a PM task doesn't clearly belong to one skill alone, when the user asks "what should I do next" or "where do I start," when a request spans multiple PM disciplines (e.g. "help me go from a vague idea to a roadmap"), or when the user wants a deliverable (deck, one-pager, scorecard, roadmap timeline) built from PM work already done in the conversation. This skill does not duplicate the content of the six component skills — it routes to them and sequences them.
---

## Purpose

Most real PM work doesn't arrive pre-labeled as "I need a JTBD exercise" — it arrives as "we have churn and I don't know why" or "leadership wants a roadmap by Friday." This skill is the front door: it figures out where a request sits in the product lifecycle, calls the right component skill(s) in the right order, carries outputs from one phase into the next, and — when the work is done — can turn it into a deck or spreadsheet.

This is a **router and sequencer, not a content library**. It does not redefine JTBD, discovery, prioritization, strategy, roadmap, or user-story logic — those live in their own skills and stay the single source of truth. This file only decides *which* skill(s) to invoke, in *what* order, with *what* handoff between them, and *what* to do with the result.

## The Six Component Skills (do not duplicate, always defer to)

| Skill | Type | Answers |
|---|---|---|
| `jobs-to-be-done` | Component | What is the customer actually trying to accomplish, and what pains/gains surround it? |
| `discovery-process` | Workflow | Is this problem real, and what solution actually addresses it? |
| `prioritization-advisor` | Interactive | Given everything on the table, what do we do first? |
| `product-strategy-session` | Workflow | What's our positioning, problem, solution direction, and high-level plan? |
| `roadmap-planning` | Workflow | How do we sequence validated/prioritized work into a communicable plan? |
| `user-story` | Component | How do we hand a specific piece of work to engineering with testable criteria? |

Two of these (`discovery-process`, `product-strategy-session`) are themselves workflows that orchestrate `jobs-to-be-done`, `prioritization-advisor`, and `user-story` internally. This skill sits one level above all of them — it decides which workflow or component applies, including when to invoke a workflow versus its components directly.

## Step 0: Always Triage First

Before doing any PM work, classify the request using the table below. Don't guess — if the answer isn't obvious from what the user said, ask one clarifying question rather than picking a skill at random.

| Signal in the request | Likely stage | Route to |
|---|---|---|
| "Why do customers do X," "what are they trying to accomplish," "unmet need," "switch interview" | Understanding motivation | `jobs-to-be-done` |
| "We have a problem but don't know the cause/solution," "should we build this," "validate before committing" | Problem/solution validation | `discovery-process` |
| "Too many ideas," "what do we build first," "RICE vs ICE," "backlog is huge" | Ranking known options | `prioritization-advisor` |
| "We need direction," "positioning is unclear," "new product/initiative," "what's our strategy" | Strategic framing (pre-roadmap) | `product-strategy-session` |
| "Turn this into a roadmap," "sequence by quarter," "communicate the plan to execs" | Sequencing validated/prioritized work | `roadmap-planning` |
| "Write a ticket," "translate this epic into stories," "acceptance criteria" | Execution handoff | `user-story` |
| "Make this a deck/PPT/slides," "put this in Excel," "I need a file to share" | Deliverable packaging | Skip to **Deliverables Layer** below, using whatever PM work already exists in the conversation |
| Spans multiple rows above, or starts from "I have a vague idea" with no narrower signal | Full lifecycle | Run the **Full Lifecycle Sequence** below |

If genuinely ambiguous between two adjacent rows (e.g. discovery vs. strategy session), ask:

"Are you starting from a specific customer problem you want to validate (→ discovery), or from a broader strategic question about direction/positioning (→ strategy session)?"

## Full Lifecycle Sequence

When a request doesn't fit one row — e.g. "help me take this idea from zero to a roadmap" — run phases in this order, skipping any phase the user has already completed (ask what they already have before starting any phase, since redoing completed work wastes their time):

```
1. jobs-to-be-done        → understand the customer motivation/pain/gain
        ↓ (informs problem framing)
2. discovery-process       → validate the problem is real and the solution direction works
        ↓ (validated solution direction)
3. prioritization-advisor  → if multiple validated solutions/epics compete for the same resources
        ↓ (ranked list)
4. roadmap-planning        → sequence into Now/Next/Later or quarters
        ↓ (committed epics)
5. user-story              → break committed epics into development-ready stories
        ↓ (optional)
6. Deliverables Layer      → package as a deck (strategy/roadmap narrative) or spreadsheet (scoring, sequencing)
```

`product-strategy-session` is an **alternative entry point to steps 1-2-3**, not an additional step — use it instead of running `jobs-to-be-done` + `discovery-process` + `prioritization-advisor` separately when the user's need is broad strategic framing (positioning + problem + solution + initial prioritization) rather than a narrow, already-scoped problem. Don't run both `product-strategy-session` and the three components it already covers; pick one path.

### Carrying context between phases

Each component skill expects certain inputs (see its own "Step 1: Gather Context" or "Application" section). When this skill sequences them, carry forward:
- From `jobs-to-be-done` → the prioritized pains/gains feed the problem hypothesis in `discovery-process` Phase 1, or the positioning context in `product-strategy-session` Phase 1.
- From `discovery-process` or `product-strategy-session` → the validated problem statement and solution direction feed `prioritization-advisor`'s scoring inputs and `roadmap-planning` Phase 1 ("gather inputs").
- From `prioritization-advisor` → the ranked backlog feeds `roadmap-planning` Phase 3 directly (don't re-prioritize from scratch).
- From `roadmap-planning` → committed, sequenced epics feed `user-story` Step 1 context (persona, problem, desired outcome already established — don't re-ask).

Never re-ask the user for information already produced by an earlier phase in the same session.

## Deliverables Layer: Decks and Spreadsheets

PM work frequently needs to leave the conversation as a file. This skill decides *which* document skill applies and *what structure* to put the PM content into — the actual file mechanics (fonts, QA, layout rules, formula standards) are owned entirely by the `pptx` and `xlsx` skills, which must be consulted before producing either file type. Do not improvise document structure or formatting rules here.

### When to produce a deck (→ defer to `pptx` skill)

Use a slide deck when the output is **narrative and persuasive** — meant to align stakeholders or communicate direction:
- Strategy session output (positioning, problem, solution direction, roadmap) → exec-readable strategy deck
- Roadmap communication (Phase 5 of `roadmap-planning`) → Now/Next/Later or quarterly roadmap deck
- Discovery readout (Phase 6 of `discovery-process`) → GO/PIVOT/KILL recommendation deck

Suggested slide skeleton (adapt to content — never force empty slides to fill this list):
1. Title + framing question
2. Problem/opportunity (from JTBD or discovery)
3. Evidence (research findings, data, quotes — paraphrased, not reproduced verbatim from any source document)
4. Recommended direction / positioning
5. Prioritized initiatives (table or 2x2 from `prioritization-advisor` output)
6. Roadmap (Now/Next/Later or quarter-based, from `roadmap-planning` output)
7. Ask / next steps

Before writing any slide content or code, read `/mnt/skills/public/pptx/SKILL.md` in full — it governs color palette selection, typography, layout variety, and the mandatory visual QA loop. Do not skip the QA step for PM decks; a roadmap slide with overlapping timeline bars is a common, embarrassing failure mode.

### When to produce a spreadsheet (→ defer to `xlsx` skill)

Use a spreadsheet when the output is **structured and computational** — meant to be scored, sorted, or recalculated:
- Prioritization scoring (RICE/ICE/Value-Effort tables from `prioritization-advisor`) → live-formula scorecard, not hardcoded ranks
- Roadmap sequencing with dependencies/dates → timeline or now/next/later grid
- Backlog of user stories with status tracking → tracker with columns for persona, story, AC status, sprint

Before writing any spreadsheet code, read `/mnt/skills/public/xlsx/SKILL.md` in full — it governs the use of real formulas (e.g. RICE score as `=(B2*C2*D2)/E2`, never a precomputed number), color-coding conventions, and the mandatory recalculation step. A prioritization scorecard with hardcoded scores instead of formulas defeats the purpose — the user should be able to change an Effort estimate and watch the ranking update.

### Choosing between them

If the user asks for "a roadmap" with no format specified, ask which they mean — a presentation-style roadmap (deck) or a working sequencing tool (spreadsheet) — since the two have different audiences (stakeholder alignment vs. ongoing planning):

"Do you want this as a presentation slide to share with stakeholders, or as a working spreadsheet you'll keep updating?"

Default to deck for anything explicitly described as a "readout," "presentation," or "to share with execs." Default to spreadsheet for anything described as "scoring," "tracker," or "backlog."

## Common Pitfalls

### Pitfall 1: Skipping triage and guessing the skill
**Symptom:** Jumping straight into a user-story template when the user hasn't validated the problem yet.
**Fix:** Always run Step 0 triage first, even when a request looks obviously like one skill — "write me a user story" might still need a quick check that a validated problem/persona exists.

### Pitfall 2: Running the full lifecycle when only one phase was asked for
**Symptom:** User asks for prioritization help and gets dragged through a JTBD exercise first.
**Fix:** Only run the Full Lifecycle Sequence when the request genuinely spans multiple phases or starts from "I have nothing yet." A scoped request gets routed directly to its matching skill.

### Pitfall 3: Re-deriving content the component skills already own
**Symptom:** This skill starts explaining RICE scoring formulas inline instead of invoking `prioritization-advisor`.
**Fix:** This file routes and sequences; it never reproduces a component skill's frameworks, templates, or question sets. If you find yourself writing JTBD category definitions here, stop — that belongs in `jobs-to-be-done/SKILL.md`.

### Pitfall 4: Hardcoding numbers into a "live" scorecard
**Symptom:** Exporting a prioritization scorecard to Excel with the RICE score typed in as a static number.
**Fix:** Follow the `xlsx` skill's formula-first rule without exception — scores must be formulas referencing input cells.

### Pitfall 5: Building a deck before content is validated
**Symptom:** User says "make me a strategy deck" with no prior discovery/strategy work in the conversation; skill jumps straight to slide design.
**Fix:** Deliverables Layer formats *existing* PM work. If no upstream work exists yet, run the relevant component/workflow skill first, then build the deck from its output.

## References

### Component Skills (orchestrated, never duplicated)
- `skills/jobs-to-be-done/SKILL.md`
- `skills/discovery-process/SKILL.md` (workflow; orchestrates `jobs-to-be-done`, `prioritization-advisor`, `user-story` internally)
- `skills/prioritization-advisor/SKILL.md`
- `skills/product-strategy-session/SKILL.md` (workflow; alternative entry point to JTBD + discovery + prioritization)
- `skills/roadmap-planning/SKILL.md` (workflow; orchestrates `prioritization-advisor`)
- `skills/user-story/SKILL.md`

### Document Skills (deferred to for all file mechanics)
- `/mnt/skills/public/pptx/SKILL.md` — slide creation, design, and required visual QA
- `/mnt/skills/public/xlsx/SKILL.md` — spreadsheet creation, formula rules, and required recalculation

---

**Skill type:** Orchestrator (meta-workflow)
**Suggested filename:** `pm-master.md`
**Suggested placement:** `/skills/user/pm-master/`
**Dependencies:** Routes to all six listed component/workflow skills; defers to `pptx` and `xlsx` public skills for any file output. Holds no PM framework content of its own.

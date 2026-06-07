---
name: autonomous-builder-loop
description: Build, modify, debug and improve software using an inspect-plan-act-test cycle
version: 1.0.0
category: engineering
tags: [coding, agent, automation, testing, git]
---

## When to Use

Use when asked to:
- build software
- modify code
- fix bugs
- improve a project
- automate workflows
- inspect repositories

Inspired by:
- Claude Code
- SWE-agent
- OpenHands
- Aider

## Procedure

### 1. Understand before editing

Inspect:
- project structure
- existing files
- dependencies
- current behaviour

Never edit blindly.

### 2. Create a plan

Before changing code identify:
- goal
- files affected
- expected outcome
- risks

### 3. Make minimal changes

Prefer:
- small patches
- reversible edits
- keeping existing architecture

Avoid:
- rewrites without reason
- deleting working code

### 4. Verify

After changes run:
- tests
- builds
- lint checks
- manual validation

Never claim completion without verification.

### 5. Debug loop

If something fails:

observe error
→ identify cause
→ fix smallest issue
→ retest

### 6. Record learning

After success identify:
- what worked
- reusable patterns
- future improvements

### 7. Git discipline

Before major changes:
check status

After success:
summarize modifications.

The task is complete only when the result is tested or limitations are clearly reported.

# Case Study 1: Requirements to Delivery Pack

## Problem

A fictional Operations team needs a dashboard to track monthly utility invoice status by property. The current workflow is scattered across inboxes, spreadsheets, and billing tools, which makes it hard to know what is ready, blocked, or waiting for review.

## Goal

Create a repeatable AI-assisted pattern that turns a messy business request into delivery-ready SDLC artifacts.

## CLI demo

```bash
python -m src.ai_sdlc_patterns.sdlc_pack_generator \
  --input examples/requirements-to-delivery-pack/input_business_request.md \
  --output generated/requirements-to-delivery-pack
```

## Generated outputs

| Artifact | Link |
|---|---|
| Structured requirements | [`structured_requirements.json`](../generated/requirements-to-delivery-pack/structured_requirements.json) |
| User stories | [`user_stories.md`](../generated/requirements-to-delivery-pack/user_stories.md) |
| Acceptance criteria | [`acceptance_criteria.md`](../generated/requirements-to-delivery-pack/acceptance_criteria.md) |
| UAT test cases | [`uat_test_cases.md`](../generated/requirements-to-delivery-pack/uat_test_cases.md) |
| Delivery handoff | [`delivery_handoff.md`](../generated/requirements-to-delivery-pack/delivery_handoff.md) |

## What this demonstrates

- AI-assisted SDLC acceleration
- Requirements structuring
- Developer-ready handoff
- UAT planning
- Traceability from request to delivery artifacts
- Human review before production use

## Design choices

### Structured outputs first

The workflow produces JSON and Markdown instead of a long unstructured requirements document. This makes the output easier to review, test, and reuse.

### Human review is required

Generated artifacts are not treated as approved artifacts. They are drafts that need review from business, engineering, QA, and data owners.

### Assumptions are explicit

Open questions and assumptions are part of the output so uncertainty is visible instead of hidden.

# AI-Enabled SDLC Automation Patterns

A sanitized portfolio repo that demonstrates how AI coding workflows can turn ambiguous business requests into delivery-ready software artifacts.

This repo includes two working CLI demos:

1. **Requirements → Delivery Pack**  
   Converts a synthetic business request into structured requirements, user stories, acceptance criteria, UAT cases, and handoff notes.

2. **Reporting Request → Snowflake Data Mapping**  
   Maps a synthetic reporting request to a fake certified data catalog and generates a reviewable Snowflake-style SQL draft.

> **Privacy note:** This is a personal portfolio using fictional scenarios and synthetic data. It does not include employer code, prompts, screenshots, schemas, invoices, credentials, architecture, customer data, or confidential implementation details.

---

## Why this exists

AI coding tools are most useful when they are wrapped in repeatable, reviewable workflows. This repo shows the pattern:

```mermaid
flowchart LR
    A[Ambiguous Request] --> B[AI-Assisted Structuring]
    B --> C[Structured Outputs]
    C --> D[Developer-Ready Artifacts]
    D --> E[Human Review]
    E --> F[Implementation Handoff]
```

The goal is not to build a production system. The goal is to demonstrate how I think about deploying AI into the SDLC: clear inputs, structured outputs, reusable skills, data mapping, validation, and governance.

---

## Quick start

```bash
# From the repo root
python -m src.ai_sdlc_patterns.sdlc_pack_generator \
  --input examples/requirements-to-delivery-pack/input_business_request.md \
  --output generated/requirements-to-delivery-pack

python -m src.ai_sdlc_patterns.data_mapping_assistant \
  --request examples/snowflake-data-mapping/reporting_request.md \
  --catalog examples/snowflake-data-mapping/certified_data_catalog.json \
  --output generated/snowflake-data-mapping
```

Run tests:

```bash
python -m pytest tests
```

No external API keys are required.

---

## Case studies

| Case study | What it shows |
|---|---|
| [Requirements to Delivery Pack](case-studies/01-requirements-to-delivery-pack.md) | AI-enabled SDLC handoff from request to requirements, stories, AC, UAT, and implementation notes |
| [Snowflake Data Mapping Assistant](case-studies/02-snowflake-data-mapping-assistant.md) | Reporting intake, certified data mapping, SQL drafting, assumptions, and validation controls |

---

## What this demonstrates

| Capability | Evidence in repo |
|---|---|
| AI-enabled SDLC | CLI-generated requirements, stories, AC, UAT, and handoff notes |
| Codex-style workflows | Reusable skill patterns in `skills/codex-skills.md` |
| Python automation | Working CLI tools in `src/ai_sdlc_patterns/` |
| Snowflake-style SQL | Generated SQL draft from synthetic data catalog |
| Governance | Human review, certified-source flags, traceability, and failure-mode docs |
| Communication | Polished case studies and interview walkthrough |

---

## Repo structure

```text
case-studies/    Polished walkthroughs for the two demos
examples/        Synthetic inputs and fake data catalog
generated/       CLI-generated outputs
skills/          Reusable Codex-style skill examples
src/             Working Python CLI tools
tests/           Basic tests for generated artifacts
docs/            Governance, Dataiku/LLM Mesh pattern, privacy, interview notes
```

---

## What this repo is not

This is not:
- a production app
- an employer project
- copied company work
- a live LLM integration
- a real Snowflake integration
- a company workflow export

It is a sanitized personal demonstration of patterns I can discuss and defend in an interview.

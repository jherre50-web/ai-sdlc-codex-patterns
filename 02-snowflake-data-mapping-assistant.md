# Case Study 2: Snowflake Data Mapping Assistant

## Problem

A fictional Finance team wants a monthly utility invoice readiness report. The request includes invoice status, meter usage, total charges, review owner, and missing data reasons.

The challenge is not just writing SQL. The challenge is mapping business fields to the right certified data sources and making assumptions visible before engineering work begins.

## Goal

Create a reusable pattern for turning reporting requests into:
- data mappings
- source-of-truth notes
- Snowflake-style SQL drafts
- validation rules
- human review checkpoints

## CLI demo

```bash
python -m src.ai_sdlc_patterns.data_mapping_assistant \
  --request examples/snowflake-data-mapping/reporting_request.md \
  --catalog examples/snowflake-data-mapping/certified_data_catalog.json \
  --output generated/snowflake-data-mapping
```

## Generated outputs

| Artifact | Link |
|---|---|
| Data mapping JSON | [`data_mapping.json`](../generated/snowflake-data-mapping/data_mapping.json) |
| Snowflake-style SQL draft | [`sample_snowflake_sql.sql`](../generated/snowflake-data-mapping/sample_snowflake_sql.sql) |
| Assumptions and validation | [`assumptions_and_validation.md`](../generated/snowflake-data-mapping/assumptions_and_validation.md) |

## What this demonstrates

- Snowflake-style SQL thinking
- Data discovery and mapping
- Certified data-layer preference
- Reporting intake acceleration
- Reviewable generated artifacts
- Governance around non-certified sources

## Design choices

### Certified data sources are preferred

The mapping flags whether each source is certified. Non-certified sources are allowed only with explicit review.

### SQL is a draft, not production code

The SQL is intentionally reviewable. It favors clarity over cleverness.

### Validation is part of the handoff

The workflow includes row-count, join, null, blocked-status, and freshness checks before release.

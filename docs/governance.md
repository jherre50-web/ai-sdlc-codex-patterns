# Governance and Human Review

AI-generated SDLC artifacts should accelerate teams without removing accountability.

## Required review points

| Artifact | Reviewer |
|---|---|
| Requirements | Business owner |
| Data mappings | Data owner |
| SQL drafts | Engineer or analytics engineer |
| UAT cases | QA or business tester |
| Delivery handoff | Product / delivery owner |

## Controls

- Prefer certified data sources.
- Flag assumptions and open questions.
- Preserve traceability from request to artifact.
- Route uncertain or high-impact outputs to human review.
- Do not automate downstream financial or operational actions without approval.

## Failure modes

- Hallucinated data sources
- Incorrect report grain
- Missing edge cases
- Unreviewed SQL
- Ambiguous ownership
- Over-automation beyond confidence level

"""Generate a delivery pack from a synthetic business request.

This is intentionally deterministic. In an enterprise environment, the
`extract_requirements` function could be replaced with a governed LLM call
through an approved provider, Dataiku LLM Mesh, or another internal AI service.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def extract_requirements(request_text: str) -> dict:
    """Create structured requirements for the synthetic demo request."""
    return {
        "initiative": "Utility Invoice Status Dashboard",
        "problem": "Operations lacks a centralized way to track monthly utility invoice status by property.",
        "users": ["Operations Analyst", "Finance Reviewer", "Accounting Partner"],
        "goals": [
            "Reduce manual invoice tracking",
            "Improve visibility into blocked invoices",
            "Support downstream billing readiness",
            "Preserve traceability from source record to dashboard output",
        ],
        "functional_requirements": [
            {"id": "FR-001", "text": "Display invoice status by property and billing month."},
            {"id": "FR-002", "text": "Flag invoices requiring human review."},
            {"id": "FR-003", "text": "Display standardized missing data reasons."},
            {"id": "FR-004", "text": "Allow export of invoice status for Finance and Accounting."},
        ],
        "non_functional_requirements": [
            {"id": "NFR-001", "text": "Use certified data sources where available."},
            {"id": "NFR-002", "text": "Maintain traceability between source data and dashboard output."},
        ],
        "open_questions": [
            "What refresh cadence is required?",
            "What confidence threshold should route records to review?",
            "Which export format does Finance require?",
        ],
        "source_request_preview": request_text[:300],
    }


def render_user_stories(requirements: dict) -> str:
    return """# User Stories

## Story 1: View invoice status by property

As an Operations Analyst, I want to view invoice status by property and month so that I can identify which invoices are received, blocked, pending, or approved.

## Story 2: Review blocked invoices

As an Operations Analyst, I want to see missing data reasons so that I can resolve blocked invoices quickly.

## Story 3: Export approved invoice status

As a Finance Reviewer, I want to export approved invoice statuses so that I can support downstream finance and accounting workflows.

## Story 4: Preserve source traceability

As an Accounting Partner, I want each record to include a source reference so that invoice status can be audited back to the originating system.
"""


def render_acceptance_criteria(requirements: dict) -> str:
    return """# Acceptance Criteria

## Invoice status view

- Given I select a billing month, when the dashboard loads, then I can see invoice status grouped by property.
- Given an invoice is blocked, when I view the invoice row, then I can see the missing data reason.
- Given an invoice requires human review, when I view the record, then it is clearly marked as review required.

## Export

- Given I filter to approved invoices, when I select export, then the export includes property, billing month, vendor, invoice number, status, and source reference.
- Given no records match the filters, when I select export, then the system displays an empty-state message.

## Traceability

- Given an invoice appears in the dashboard, when I open the details, then I can see the source reference.
- Given a record has no source reference, when the data refreshes, then it is routed for review.
"""


def render_uat_cases(requirements: dict) -> str:
    return """# UAT Test Cases

| ID | Scenario | Expected Result |
|---|---|---|
| UAT-001 | Filter dashboard by billing month | Only records for selected month display |
| UAT-002 | View blocked invoice | Missing data reason is visible |
| UAT-003 | Export approved invoices | Export includes required fields |
| UAT-004 | Review source traceability | Source reference is visible for each record |
| UAT-005 | Missing source reference | Record is routed to review |
"""


def render_delivery_handoff(requirements: dict) -> str:
    return """# Delivery Handoff

## First release scope

- Invoice status by property and month
- Standardized missing data reasons
- Export for Finance and Accounting
- Source reference visibility
- Review routing for records missing required data

## Excluded from first release

- Automatic downstream billing submission
- Complex approval routing
- Predictive delay modeling

## Risks

- Conflicting invoice status across source systems
- Missing source references
- Users treating dashboard output as final accounting approval
- Incomplete review ownership

## Human review checkpoints

- Business owner reviews requirements
- Data owner reviews mappings
- Engineering reviews implementation approach
- QA reviews UAT cases
"""


def generate_delivery_pack(input_path: Path, output_dir: Path) -> list[Path]:
    request_text = input_path.read_text(encoding="utf-8")
    requirements = extract_requirements(request_text)
    output_dir.mkdir(parents=True, exist_ok=True)

    files = {
        "structured_requirements.json": json.dumps(requirements, indent=2),
        "user_stories.md": render_user_stories(requirements),
        "acceptance_criteria.md": render_acceptance_criteria(requirements),
        "uat_test_cases.md": render_uat_cases(requirements),
        "delivery_handoff.md": render_delivery_handoff(requirements),
    }

    written = []
    for name, content in files.items():
        path = output_dir / name
        path.write_text(content.rstrip() + "\n", encoding="utf-8")
        written.append(path)

    return written


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a synthetic SDLC delivery pack.")
    parser.add_argument("--input", required=True, type=Path, help="Path to the business request markdown file.")
    parser.add_argument("--output", required=True, type=Path, help="Directory for generated artifacts.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    written = generate_delivery_pack(args.input, args.output)
    for path in written:
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()

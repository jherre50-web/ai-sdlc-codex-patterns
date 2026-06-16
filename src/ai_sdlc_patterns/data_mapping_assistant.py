"""Generate a synthetic data mapping and Snowflake-style SQL draft.

This script does not connect to Snowflake. It uses a fake certified data catalog
and deterministic mapping rules for portfolio demonstration.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


FIELD_TO_SOURCE = {
    "Property ID": ("analytics.dim_property", "property_id"),
    "Property name": ("analytics.dim_property", "property_name"),
    "Billing month": ("analytics.fact_utility_invoice", "billing_month"),
    "Vendor name": ("analytics.dim_vendor", "vendor_name"),
    "Invoice number": ("analytics.fact_utility_invoice", "invoice_number"),
    "Invoice status": ("analytics.fact_utility_invoice", "invoice_status"),
    "Missing data reason": ("analytics.fact_utility_invoice", "missing_data_reason_code"),
    "Meter usage kWh": ("analytics.fact_meter_usage", "usage_kwh"),
    "Total invoice amount": ("analytics.fact_utility_invoice", "total_amount"),
    "Review owner": ("analytics.invoice_review_status", "review_owner"),
    "Last updated timestamp": ("analytics.fact_utility_invoice", "last_updated_ts"),
}


def load_catalog(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def is_certified(catalog: dict, table_name: str) -> bool:
    for table in catalog.get("tables", []):
        if table["name"] == table_name:
            return bool(table["certified"])
    return False


def build_mapping(catalog: dict) -> dict:
    mappings = []
    for business_field, (table, column) in FIELD_TO_SOURCE.items():
        certified = is_certified(catalog, table)
        mappings.append(
            {
                "business_field": business_field,
                "source_table": table,
                "source_column": column,
                "certified_source": certified,
                "requires_review": not certified,
            }
        )

    return {
        "report": "Monthly Utility Invoice Readiness Report",
        "grain": "property_id + billing_month + invoice_id",
        "mappings": mappings,
        "review_required": any(item["requires_review"] for item in mappings),
        "review_notes": [
            "Confirm report grain before implementation.",
            "Review non-certified sources with the data owner.",
            "Validate join row counts and null rates before release.",
        ],
    }


def render_sql() -> str:
    return """-- Synthetic Snowflake-style SQL draft for portfolio demonstration only.

WITH invoice_base AS (
    SELECT
        invoice_id,
        property_id,
        vendor_id,
        billing_month,
        invoice_number,
        invoice_status,
        missing_data_reason_code,
        total_amount,
        last_updated_ts
    FROM analytics.fact_utility_invoice
),

meter_usage AS (
    SELECT
        property_id,
        billing_month,
        SUM(usage_kwh) AS total_usage_kwh
    FROM analytics.fact_meter_usage
    GROUP BY property_id, billing_month
)

SELECT
    p.property_id,
    p.property_name,
    i.billing_month,
    v.vendor_name,
    i.invoice_number,
    i.invoice_status,
    i.missing_data_reason_code,
    m.total_usage_kwh,
    i.total_amount,
    r.review_owner,
    i.last_updated_ts,
    DATEDIFF('day', i.last_updated_ts, CURRENT_TIMESTAMP()) AS days_since_update,
    CASE
        WHEN i.invoice_status = 'BLOCKED' THEN TRUE
        WHEN i.missing_data_reason_code IS NOT NULL THEN TRUE
        WHEN DATEDIFF('day', i.last_updated_ts, CURRENT_TIMESTAMP()) > 7 THEN TRUE
        ELSE FALSE
    END AS requires_attention
FROM invoice_base i
LEFT JOIN analytics.dim_property p
    ON i.property_id = p.property_id
LEFT JOIN analytics.dim_vendor v
    ON i.vendor_id = v.vendor_id
LEFT JOIN meter_usage m
    ON i.property_id = m.property_id
    AND i.billing_month = m.billing_month
LEFT JOIN analytics.invoice_review_status r
    ON i.invoice_id = r.invoice_id
WHERE p.active_flag = TRUE;
"""


def render_validation_notes() -> str:
    return """# Assumptions and Validation

## Assumptions

- `fact_utility_invoice` is the source of truth for invoice status.
- Meter usage should be aggregated to property and billing month.
- `invoice_review_status` is not certified and requires data owner review.
- Active properties only are included in first release.

## Validation checks

- Confirm invoice row counts before and after joins.
- Validate that blocked invoices have missing data reasons.
- Check null rates for required fields.
- Confirm review owner coverage for records requiring review.
- Reconcile total invoice amount by month against source system totals.

## Human review required when

- A non-certified source is used.
- SQL affects finance or billing workflows.
- Join logic changes row counts unexpectedly.
- Required fields have high null rates.
"""


def generate_mapping_outputs(request_path: Path, catalog_path: Path, output_dir: Path) -> list[Path]:
    _ = request_path.read_text(encoding="utf-8")  # Kept to show the requested input is part of the workflow.
    catalog = load_catalog(catalog_path)
    mapping = build_mapping(catalog)
    output_dir.mkdir(parents=True, exist_ok=True)

    outputs = {
        "data_mapping.json": json.dumps(mapping, indent=2),
        "sample_snowflake_sql.sql": render_sql(),
        "assumptions_and_validation.md": render_validation_notes(),
    }

    written = []
    for name, content in outputs.items():
        path = output_dir / name
        path.write_text(content.rstrip() + "\n", encoding="utf-8")
        written.append(path)
    return written


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a synthetic Snowflake-style data mapping package.")
    parser.add_argument("--request", required=True, type=Path, help="Path to the reporting request markdown file.")
    parser.add_argument("--catalog", required=True, type=Path, help="Path to the fake certified data catalog JSON.")
    parser.add_argument("--output", required=True, type=Path, help="Directory for generated artifacts.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    written = generate_mapping_outputs(args.request, args.catalog, args.output)
    for path in written:
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()

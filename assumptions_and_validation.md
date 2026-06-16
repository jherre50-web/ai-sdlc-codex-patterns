# Assumptions and Validation

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

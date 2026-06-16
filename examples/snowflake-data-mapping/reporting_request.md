# Synthetic Reporting Request

Finance needs a monthly utility invoice readiness report.

## Requested fields

- Property ID
- Property name
- Billing month
- Vendor name
- Invoice number
- Invoice status
- Missing data reason
- Meter usage kWh
- Total invoice amount
- Review owner
- Last updated timestamp

## Business questions

1. Which properties have invoices ready for review?
2. Which invoices are blocked and why?
3. What is the total invoice amount by property and month?
4. Which invoices have not been updated in the last 7 days?

## Constraints

- Use certified data sources where available
- Preserve record traceability
- Flag assumptions
- Do not automate downstream billing decisions from this report alone

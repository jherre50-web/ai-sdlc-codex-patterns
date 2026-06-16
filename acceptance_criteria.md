# Acceptance Criteria

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

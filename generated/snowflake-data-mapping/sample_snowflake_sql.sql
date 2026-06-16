-- Synthetic Snowflake-style SQL draft for portfolio demonstration only.

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

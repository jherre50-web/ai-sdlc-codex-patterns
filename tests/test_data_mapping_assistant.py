from pathlib import Path
import json

from src.ai_sdlc_patterns.data_mapping_assistant import generate_mapping_outputs


def test_generate_mapping_outputs(tmp_path: Path):
    request_path = tmp_path / "request.md"
    request_path.write_text("Finance needs monthly invoice readiness.", encoding="utf-8")

    catalog_path = tmp_path / "catalog.json"
    catalog_path.write_text(
        json.dumps({
            "tables": [
                {"name": "analytics.dim_property", "certified": True},
                {"name": "analytics.fact_utility_invoice", "certified": True},
                {"name": "analytics.fact_meter_usage", "certified": True},
                {"name": "analytics.dim_vendor", "certified": True},
                {"name": "analytics.invoice_review_status", "certified": False},
            ]
        }),
        encoding="utf-8",
    )

    written = generate_mapping_outputs(request_path, catalog_path, tmp_path / "out")

    assert len(written) == 3
    mapping = json.loads((tmp_path / "out" / "data_mapping.json").read_text())
    assert mapping["report"] == "Monthly Utility Invoice Readiness Report"
    assert mapping["review_required"] is True
    assert "DATEDIFF" in (tmp_path / "out" / "sample_snowflake_sql.sql").read_text()

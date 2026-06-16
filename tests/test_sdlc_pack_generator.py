from pathlib import Path
import json

from src.ai_sdlc_patterns.sdlc_pack_generator import generate_delivery_pack


def test_generate_delivery_pack(tmp_path: Path):
    input_path = tmp_path / "request.md"
    input_path.write_text("Operations needs invoice status visibility by property.", encoding="utf-8")

    written = generate_delivery_pack(input_path, tmp_path / "out")

    assert len(written) == 5
    requirements = json.loads((tmp_path / "out" / "structured_requirements.json").read_text())
    assert requirements["initiative"] == "Utility Invoice Status Dashboard"
    assert any(item["id"] == "FR-001" for item in requirements["functional_requirements"])
    assert (tmp_path / "out" / "user_stories.md").exists()
    assert "Human review" in (tmp_path / "out" / "delivery_handoff.md").read_text()

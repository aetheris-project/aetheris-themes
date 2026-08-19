"""Unit tests for the theme validator."""

import json
from pathlib import Path

from tools.validate import (
    ALLOWED_ACCENTS,
    REQUIRED_CSS_TOKENS,
    _contrast_ratio,
    validate_css,
    validate_json,
)

ROOT = Path(__file__).resolve().parent.parent
THEMES = ROOT / "themes"
TEMPLATES = ROOT / "templates"


def test_standard_themes_are_valid():
    for path in THEMES.glob("*.json"):
        errors: list = []
        warnings: list = []
        assert validate_json(path, errors, warnings), f"{path}: {errors}"
        assert not errors


def test_aurora_uses_registered_custom_accent():
    assert "violet" in ALLOWED_ACCENTS
    path = THEMES / "aurora.json"
    errors: list = []
    warnings: list = []
    assert validate_json(path, errors, warnings)


def test_template_is_valid():
    errors: list = []
    warnings: list = []
    assert validate_json(TEMPLATES / "theme.template.json", errors, warnings)


def test_missing_top_level_key_fails(tmp_path):
    payload = json.loads((THEMES / "emerald.json").read_text(encoding="utf-8"))
    del payload["modules"]
    bad = tmp_path / "bad.json"
    bad.write_text(json.dumps(payload), encoding="utf-8")
    errors: list = []
    warnings: list = []
    assert not validate_json(bad, errors, warnings)
    assert any("modules" in error for error in errors)


def test_unknown_accent_fails(tmp_path):
    payload = json.loads((THEMES / "emerald.json").read_text(encoding="utf-8"))
    payload["theme"]["accent"] = "hotpink"
    bad = tmp_path / "accent.json"
    bad.write_text(json.dumps(payload), encoding="utf-8")
    errors: list = []
    warnings: list = []
    assert not validate_json(bad, errors, warnings)
    assert any("accent" in error for error in errors)


def test_template_css_has_all_tokens():
    css_path = TEMPLATES / "theme.template.css"
    css = css_path.read_text(encoding="utf-8")
    present = {match for match in REQUIRED_CSS_TOKENS if f"{match}:" in css}
    assert present == REQUIRED_CSS_TOKENS


def test_contrast_ratio():
    black = (0, 0, 0)
    white = (255, 255, 255)
    assert _contrast_ratio(white, black) > 20
    assert _contrast_ratio(black, black) == 1.0


def test_validate_css_missing_token(tmp_path):
    css = ":root { --aetheris-bg: 9 9 11; }"
    bad = tmp_path / "bad.css"
    bad.write_text(css, encoding="utf-8")
    errors: list = []
    warnings: list = []
    assert not validate_css(bad, errors, warnings)
    assert errors

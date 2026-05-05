"""Verify requirements.txt files are parseable and minimally well-formed.

Catches accidents like the previous backend/requirements.txt, which had
duplicated frontend deps interleaved with commented-out lines.
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _parse_requirements(path: str) -> list[str]:
    """Return the package names declared in ``path`` (one per line, ignoring
    comments and blank lines)."""

    pkgs: list[str] = []
    with open(path) as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            # Strip env markers, version specifiers, and extras
            name = re.split(r"[\s<>=!~;\[]", line, maxsplit=1)[0].lower()
            if name:
                pkgs.append(name)
    return pkgs


def test_backend_requirements_parses():
    pkgs = _parse_requirements(os.path.join(ROOT, "backend", "requirements.txt"))
    assert "fastapi" in pkgs
    assert "uvicorn" in pkgs
    assert "openai" in pkgs


def test_frontend_requirements_parses():
    pkgs = _parse_requirements(os.path.join(ROOT, "frontend", "requirements.txt"))
    assert "kivy" in pkgs
    assert "pvporcupine" in pkgs
    assert "pyaudio" in pkgs


def test_backend_requirements_has_no_frontend_only_deps():
    """Regression guard: kivy/pvporcupine should never appear in the
    backend file again."""
    pkgs = _parse_requirements(os.path.join(ROOT, "backend", "requirements.txt"))
    for forbidden in ("kivy", "kivymd", "pvporcupine", "pyaudio"):
        assert forbidden not in pkgs, f"{forbidden} leaked back into backend/requirements.txt"


def test_no_duplicate_packages():
    for sub in ("backend", "frontend"):
        path = os.path.join(ROOT, sub, "requirements.txt")
        pkgs = _parse_requirements(path)
        assert len(pkgs) == len(set(pkgs)), f"duplicates in {sub}/requirements.txt: {pkgs}"

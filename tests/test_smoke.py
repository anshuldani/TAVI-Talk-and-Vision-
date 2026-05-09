"""Import smoke tests — fail fast on syntax errors or top-level import-time bugs.

These do not exercise the model APIs (Whisper, BLIP, Mistral, Groq) — those
require keys and network. They only verify the backend modules parse and
import cleanly with the runtime deps installed.
"""

import importlib

import pytest


@pytest.mark.parametrize("module_name", ["app", "audio", "video", "processing"])
def test_backend_module_imports(module_name):
    importlib.import_module(module_name)


def test_fastapi_app_exposes_endpoints():
    from app import app

    routes = {r.path for r in app.routes}
    assert "/process_audio/" in routes
    assert "/process_video/" in routes
    assert "/download_audio/{audio_filename}" in routes


def test_fastapi_endpoint_methods():
    from app import app

    method_map: dict = {r.path: r.methods for r in app.routes if hasattr(r, "methods")}
    assert "POST" in method_map.get("/process_video/", set())
    assert "POST" in method_map.get("/process_audio/", set())
    assert "GET" in method_map.get("/download_audio/{audio_filename}", set())


def test_global_text_summary_is_dict():
    from audio import GLOBAL_TEXT_SUMMARY

    assert isinstance(GLOBAL_TEXT_SUMMARY, dict)
    assert "latest" in GLOBAL_TEXT_SUMMARY

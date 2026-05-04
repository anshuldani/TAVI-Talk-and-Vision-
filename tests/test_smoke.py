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

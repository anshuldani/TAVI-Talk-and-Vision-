# Changelog

All notable changes to TAVI are tracked here. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); the project does
not yet tag releases.

## Unreleased

### Added
- `Makefile` with `setup`, `run-backend`, `run-frontend`, `test`, `lint` targets
- `frontend/requirements.txt` so the Kivy app installs independently of backend deps
- `tests/` scaffold with backend import smoke tests
- `.gitignore` covering venvs, temp uploads, local model weights, and env files

### Changed
- README rewritten end-to-end: real hook, "why this is hard" section,
  accurate ASCII pipeline diagram, stack table, quickstart, results, and
  team credits
- Backend uses `asyncio.get_running_loop()` instead of the deprecated
  `get_event_loop()` inside async handlers

### Fixed
- Frontend file handles closed after multipart upload (previously leaked on
  error paths)
- Mistral OCR response now correctly extracts markdown from the
  `pages` field rather than the top-level response
- Whisper STT uses `transcriptions` API for English, not `translations`
  (translations was force-translating English audio through itself)
- `processing.py` and `audio.py` had dead `requests` imports that
  masked which module was actually issuing HTTP calls

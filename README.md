# TAVI — Talk and Vision Assistant

Winner, Google Hack4Access 2024 (hosted by Google, Code Your Dreams, and Deaf Kids Code). TAVI is a multimodal AI assistant for visually impaired users: say the wake word, ask what's around you, and get a spoken scene description back — no screen required.

---

## The problem

Visually impaired users navigating unfamiliar environments can't glance at something to understand it. Existing screen readers don't help with the physical world. TAVI fills that gap: it's always listening, and when you ask, it captures what the camera sees, reads any text in frame, and speaks a coherent summary back — no touch input, no display, no sighted help needed.

---

## Why this is hard

A single TAVI response chains five systems in sequence: Porcupine wake word detection (local), PyAudio recording, Whisper API (STT), GPT-4o-mini intent routing, then either a direct Groq LLaMA reply or the full video branch — BLIP captioning (local model), Mistral OCR (API), Groq summarization (API), and pyttsx3 TTS (local). Each step can fail silently.

The hard constraint is that the user has no screen. They're standing somewhere waiting in silence. A 15-second hang or a misrouted intent isn't a UX inconvenience — it's disorienting. Every failure path needs an audio fallback, and the intent classifier has to be right without a confirmation step.

The threading model is also non-trivial. Kivy's event loop, PyAudio's stream callbacks, and OpenCV's frame capture all want to run on the main thread. Wake word detection runs in a background daemon thread; any UI update from that thread crashes the app without a traceback. All Kivy mutations route through `Clock.schedule_once`.

---

## Stack

| Layer | Technology |
|---|---|
| Frontend | Python, Kivy (PyQt-style cross-platform UI) |
| Backend | Python, FastAPI |
| Wake word | Porcupine (`pvporcupine`) — keyword: "Jarvis" |
| Speech-to-text | OpenAI Whisper API |
| Intent routing | GPT-4o-mini |
| Image captioning | BLIP (`Salesforce/blip-image-captioning-base`, local) |
| OCR | Mistral OCR API |
| LLM summarization | Groq — LLaMA 3.3 70B Versatile |
| Text-to-speech | pyttsx3 (local, offline) |
| Video processing | OpenCV |

---

## Architecture

```
[background thread]                    [main thread]
Porcupine wake word detection
          │
          ▼ wake word detected
    PyAudio recording (5s)
          │
          ▼
   POST /process_audio/  ──────────────► FastAPI backend
                                               │
                                         Whisper STT
                                               │
                                         GPT-4o-mini intent routing
                                               │
                              ┌────────────────┴────────────────┐
                              ▼                                  ▼
                          Record                          General / Fallback
                              │                                  │
                    OpenCV frame extraction            Groq LLaMA direct reply
                    BLIP caption (local, per frame)            │
                    Mistral OCR (API, per frame)                ▼
                    Groq LLaMA summarization             pyttsx3 TTS
                              │                                  │
                              ▼                                  ▼
                        pyttsx3 TTS                     spoken response
                              │
                              ▼
                    spoken scene description
```

The **backend** (`backend/app.py`) is a FastAPI server with two endpoints:
- `POST /process_audio/` — STT + intent routing + LLM response
- `POST /process_video/` — frame extraction + BLIP + OCR + summarization

The **frontend** (`frontend/main.py`) is a Kivy app that owns wake word detection, audio recording, video capture, and the chat-style UI. It calls the backend for all model inference.

---

## Quickstart

**Prerequisites:** Python 3.10+, a webcam, a microphone, and API keys for OpenAI, Porcupine, Mistral, and Groq.

```bash
git clone https://github.com/anshuldani/TAVI-Talk-and-Vision-
cd TAVI-Talk-and-Vision-
pip install -r backend/requirements.txt
```

Create `.env` in the project root:

```env
OPENAI_API_KEY=sk-...
PORCUPINE_ACCESS_KEY=...
MISTRAL_API_KEY=...
GROQ_API_KEY=...
BACKEND_URL=http://localhost:8000
```

Start the backend:

```bash
cd backend
uvicorn app:app --reload --port 8000
```

Start the frontend (separate terminal):

```bash
cd frontend
python main.py
```

Say **"Jarvis"** to wake TAVI. Then speak your request. Saying "look around" or "what do you see" triggers the full video pipeline with a spoken scene description.

---

## Results

- **Winner, Google Hack4Access 2024** — judged on accessibility impact, technical innovation, and real-world usability across teams from Code Your Dreams and Deaf Kids Code partner programs.
- End-to-end latency for a General intent response: ~3–5 seconds.
- End-to-end latency for a Record (video + scene description) response: ~8–12 seconds on a standard network connection.

---

## What's next

- Replace pyttsx3 with a higher-quality local TTS model to reduce robotic output
- Stream Groq responses as audio chunks instead of waiting for the full summary
- Add GPS integration for turn-by-turn navigation overlay in scene descriptions
- Multilingual support via Whisper's built-in language detection

---

## Team

Built at Google Hack4Access 2024. AI/ML pipeline integration, FastAPI backend, and Kivy frontend by Anshul Dani.


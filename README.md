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

## 📦 Tech Stack

- **Programming:** Python
- **Frontend:** Kivy
- **Backend:** FastAPI
- **AI Models:** 
  - OpenAI Whisper (speech-to-text)
  - Hugging Face BLIP (image captioning)
  - ChatGroq LLM (summarization & intent reasoning)
  - OCR for text recognition
  - pyttsx3 (text-to-speech)
- **Wake Word Detection:** Porcupine
- **UI/UX:** Figma, Framer prototypes

---

## 🏆 Achievements

- Developed as part of a **Hackathon-winning project** for Accessibility.
- Recognized for **impact on accessibility, innovation, and real-world usability**.

---

## 👥 Team

TAVI was developed by a collaborative team of engineers, designers, and researchers during a hackathon, with contributions in:
- AI/ML Model Integration
- Frontend & Backend Development
- UX Research & UI Design
- Accessibility Testing

---

## 🔮 Future Improvements

- Integration with **navigation systems (GPS)**.
- Support for **wearable devices**.
- Improved **real-time streaming efficiency**.
- Expanded **multilingual voice support**.


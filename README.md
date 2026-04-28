# TAVI — Talk and Vision Assistant

Winner, Google Hack4Access 2024 (hosted by Google, Code Your Dreams, and Deaf Kids Code). TAVI is a multimodal AI assistant for visually impaired users: say the wake word, ask what's around you, and get a spoken scene description back — no screen required.

---

## The problem

Visually impaired users navigating unfamiliar environments can't glance at something to understand it. Existing screen readers don't help with the physical world. TAVI fills that gap: it's always listening, and when you ask, it captures what the camera sees, reads any text in frame, and speaks a coherent summary back — no touch input, no display, no sighted help needed.

---

## ✨ Key Features

### 🎙 Continuous Voice Interaction
- Wake-word detection via **Porcupine** (`"Hello Assistant"` / `"I am done Assistant"`).
- **Whisper API** transcribes user speech to text.
- GPT-based **intent classification** (Record, General, Fallback, or TAVI-specific).

### 📷 Multimodal Video & Audio Processing
- **Record Mode**:
  - Captures video frames.
  - **Image captioning** using Hugging Face’s **BLIP model**.
  - **OCR** for text extraction.
  - **Summarization** with ChatGroq LLM.
  - **Text-to-speech output** via `pyttsx3`.
- Non-record intents: Direct GPT-based audio response without video capture.

### 📱 Accessible Chat-Style UI
- Built using **Kivy**.
- Displays:
  - User queries (transcribed text).
  - Assistant responses.
  - Media previews (video/audio).
- Continuous interaction loop (auto-reactivates microphone after each turn).

---

## 🛠 Technical Architecture

### Backend
- **FastAPI** server with endpoints:
  - `/process_audio/`
  - `/process_video/`
- Handles transcription, intent detection, and multimodal workflows.

### Frontend
- **Kivy application** in `frontend/`:
  - Wake-word detection.
  - Audio capture & UI rendering.
  - Chat-style interface for accessibility.

### Workflow
1. **Audio Input** → Whisper transcription → GPT intent detection.
2. **Intent: Record** → Capture video → BLIP captions + OCR → LLM summary → pyttsx3 voice output.
3. **Intent: General** → Direct GPT-based spoken response.


### Configurations
- `.env` file stores API keys and configs:
  - Hugging Face
  - OpenAI
  - Groq / Mistral
  - Porcupine
  - Backend URL

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


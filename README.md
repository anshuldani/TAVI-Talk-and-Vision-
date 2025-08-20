# TAVI – Talkative Vision Assistant for the Visually Impaired

TAVI (Talk and Vision Assistant) is an **AI-powered multimodal assistant** designed to empower **visually impaired individuals** with **real-time situational awareness**. By combining **voice interaction, video processing, and accessible UI design**, TAVI bridges the gap between the physical world and digital assistance, fostering **navigation independence, safety, and confidence**.

---

## 🚀 Overview

- **Purpose:** Enhance independence for visually impaired users by converting **audio and video input into enriched, accessible feedback**.
- **Core Idea:** Always-on assistant that listens for a **wake word**, processes user input (audio or visual), and provides **instant spoken feedback**.
- **Hackathon Origin:** Built during an Accessibility Hackathon as a **collaborative group project**.

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

## 🎨 UX & Research Insights

From UX design research:
- **Role Contributions:** UX Researcher, UX/UI Designer, and Developer.
- **Focus Areas:** Accessibility-first design, seamless voice-driven UX, real-time multimodal feedback.
- **Prototyping & Tools:** Figma for design, iterative user testing for refinement.

### 📊 Outcomes
- **95%** of users highlighted the need for **instant voice feedback**.
- **80%** usability satisfaction increase in testing.
- **85%** reported greater **confidence & independence**.

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

## 📸 Demo & Links

- 📂 **Portfolio Page:** [Data Science Portfolio](https://www.datascienceportfol.io/vvoona/projects/6)  
- 💻 **GitHub Repository:** [TAVI on GitHub](https://github.com/dhanvanth342/TAVI)  
- 🎨 **UX/UI Showcase:** [Framer Project](https://sahithibalerao.framer.website/tavi)  

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


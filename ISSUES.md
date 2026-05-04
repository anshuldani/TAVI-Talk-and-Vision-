# Follow-up tickets

Open these manually when ready — each is real backlog, not made-up scope.

## 1. README claims local BLIP, code uses HF InferenceClient

The README's stack table and "why this is hard" section say "BLIP captioning
(local model)". `backend/video.py` actually calls `huggingface_hub.InferenceClient`
with `provider="hf-inference"` — it's an API call, not a local model. The
local-model code is commented out as a fallback.

Either:
- restore the local fallback path (faster, offline, no `HF_API_KEY` required), or
- update the README to reflect that BLIP runs on HF Inference and document
  the latency/cost tradeoff honestly.

## 2. `processing.py` is ~unused but still loaded

`backend/processing.py` is imported nowhere outside `app.py` (and may not even
be imported there after the recent cleanup). Audit and either wire it into the
pipeline properly or delete it.

## 3. Replace `pyttsx3` with a higher-quality TTS

Already listed in `What's next` in the README. Concretely: pyttsx3 is initialized
in both `audio.py` and `video.py`, and on macOS it uses NSSpeechSynthesizer's
default voice which is robotic. Candidates: ElevenLabs API, OpenAI's
`tts-1`, or Coqui TTS for fully local. Pick one based on whether
"offline-capable" stays a goal (the original Hack4Access pitch said yes).

## 4. Stream Groq responses to TTS instead of buffering full summary

End-to-end Record-intent latency is ~8–12s. Most of that is waiting for the
Groq summarization to finish before TTS begins. Streaming chunks into pyttsx3
(or a streaming-capable TTS) would cut perceived latency by several seconds —
the user starts hearing the response immediately.

## 5. Add request-level timeout + audible failure on stuck pipelines

The README explicitly calls out that a 15-second silent hang is disorienting
for a no-screen user. The backend currently has no timeouts on the OpenAI,
Mistral, or Groq calls. Add `httpx.Timeout(15.0)` on each client and emit an
audible "I lost track, try again" via the TTS path on failure.

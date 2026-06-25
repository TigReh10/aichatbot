# aichatbot

A warm, empathetic **companion chatbot** for people who feel lonely or isolated.
Its personality lives in [`SYSTEM_PROMPT.md`](SYSTEM_PROMPT.md); the chat program
is [`chat.py`](chat.py), powered by a local model through [Ollama](https://ollama.com).

## Talk to it (free, runs on your own laptop)

1. **Install Ollama** — https://ollama.com/download (you've done this).
2. **Download a model** (one time, a few GB):
   ```bash
   ollama pull llama3.2
   ```
3. **Run the chatbot:**
   ```bash
   python chat.py
   ```
   Type a message, press Enter, and the bot replies. Type `quit` to exit.

No extra Python packages are needed — `chat.py` uses only the standard library
and talks to Ollama running on your computer.

## Customizing

- **Change its personality:** edit [`SYSTEM_PROMPT.md`](SYSTEM_PROMPT.md).
- **Use a different model:** `OLLAMA_MODEL=llama3.1 python chat.py`
  (any model you've pulled with `ollama pull`).

## Note

This bot is a supportive, friendly presence — not a therapist, doctor, or a
replacement for real human relationships. If you're in crisis, please reach out
to someone you trust or a local helpline.

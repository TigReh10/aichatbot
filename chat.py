"""Talk to your companion chatbot in the terminal, powered by a local Ollama model.

Setup (one time):
  1. Install Ollama:        https://ollama.com/download
  2. Pull a model:          ollama pull llama3.2

Run it:
  python chat.py

The bot's personality is read from SYSTEM_PROMPT.md in this same folder.
No extra Python packages are needed — this uses only the standard library.

Optional environment variables:
  OLLAMA_MODEL   which model to use (default: llama3.2)
  OLLAMA_URL     Ollama chat endpoint (default: http://localhost:11434/api/chat)
"""
from __future__ import annotations

import json
import os
import sys
import urllib.request
import urllib.error

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/chat")
MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2")
HERE = os.path.dirname(os.path.abspath(__file__))
PROMPT_FILE = os.path.join(HERE, "SYSTEM_PROMPT.md")


def load_system_prompt() -> str:
    try:
        with open(PROMPT_FILE, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"[!] Could not find {PROMPT_FILE}.")
        print("    Make sure SYSTEM_PROMPT.md is in the same folder as chat.py.")
        sys.exit(1)


def ask(messages: list[dict]) -> str:
    payload = json.dumps({"model": MODEL, "messages": messages, "stream": False}).encode("utf-8")
    req = urllib.request.Request(
        OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data["message"]["content"].strip()
    except urllib.error.URLError:
        print("\n[!] Couldn't reach Ollama. Make sure it's running and the model is pulled:")
        print("      ollama serve            (if it isn't already running)")
        print(f"      ollama pull {MODEL}\n")
        sys.exit(1)


def main() -> None:
    system_prompt = load_system_prompt()
    messages = [{"role": "system", "content": system_prompt}]

    print(f"\nCompanion chatbot is ready (model: {MODEL}).")
    print("Type your message and press Enter. Type 'quit' or 'exit' to leave.\n")

    while True:
        try:
            user = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nTake care of yourself. \u2764\n")
            break
        if user.lower() in {"quit", "exit", "bye"}:
            print("Take care of yourself. \u2764\n")
            break
        if not user:
            continue
        messages.append({"role": "user", "content": user})
        reply = ask(messages)
        messages.append({"role": "assistant", "content": reply})
        print(f"\nCompanion: {reply}\n")


if __name__ == "__main__":
    main()

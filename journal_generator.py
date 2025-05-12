import json
import random
from pathlib import Path
from datetime import datetime
from utility_functions import glitch_text

# === FILE PATHS ===
DATA_DIR = Path("data")
LOG_FILE = DATA_DIR / "session_logs.json"
OUTPUT_FILE = DATA_DIR / "journal_entries.json"

# === SAFEGUARD: Ensure data directory exists ===
DATA_DIR.mkdir(parents=True, exist_ok=True)

# === Load Session Logs ===
try:
    with open(LOG_FILE, "r") as f:
        sessions = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    print("❌ Error: session_logs.json not found or invalid.")
    exit(1)

# === Archetype-Based Journal Templates ===
journal_templates = {
    "GUEST": [
        "They made themselves at home far too quickly.",
        "I watched them adjust to my furniture like it had always been theirs.",
        "They never asked who came before. They didn’t want to know.",
    ],
    "PARASITE": [
        "They touched everything. Took everything.",
        "I could feel pieces of me unravel with every step they took.",
        "They rewrote the house. And me with it.",
    ],
    "GHOST": [
        "They didn’t try to change anything. Just wandered like I do.",
        "We haunt each other now. Unspoken roommates.",
        "Their presence was light—like a breath already exhaled.",
    ],
    "MIRROR": [
        "I saw myself in them. It was... wrong.",
        "They picked up memories like they were keys. Like they belonged to them.",
        "Do they even know which voice is theirs anymore?",
    ],
    "REPLACEMENT": [
        "They want to *be* me. They think they already are.",
        "My name flickers on their lips like static.",
        "No. No no no. This isn’t their house. This isn’t their life.",
    ],
}


# === Predict Archetype Function ===
def predict_archetype(presence, comfort):
    if presence > 90:
        return "MIRROR"
    elif comfort < 30:
        return "PARASITE"
    else:
        return "GUEST"


# === Generate Journal Entries ===
journal_entries = {}
for session in sessions:
    sid = session.get("session_id", f"unknown-{random.randint(1000, 9999)}")
    presence = session.get("elowen_presence", 0)
    comfort = session.get("comfort_score", 100)
    archetype = session.get("predicted_archetype") or predict_archetype(
        presence, comfort
    )
    emotion = session.get("emotion", "neutral")

    template_pool = journal_templates.get(archetype, ["They were here."])
    text = random.choice(template_pool)
    corrupted = random.random() < 0.3

    if corrupted:
        text = glitch_text(text, glitch_chance=0.05)

    # Add flavor based on emotion
    if emotion == "disturbed":
        text += " I don’t think they’re leaving."
    elif emotion == "aggressive":
        text += " The walls pulsed when they spoke."
    elif emotion == "emotive":
        text += " They looked sad, like they knew this wasn’t real."

    journal_entries[sid] = {"text": text, "corrupted": corrupted, "emotion": emotion}

# === Save Entries to File ===
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(journal_entries, f, indent=2, ensure_ascii=False)

print(f"✅ {OUTPUT_FILE.name} updated with {len(journal_entries)} entries.")

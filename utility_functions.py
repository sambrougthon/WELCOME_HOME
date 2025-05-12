# utility_functions.py

from pathlib import Path
import json
import os
import random

# === FILE PATHS ===
DATA_DIR = Path("data")
LOOP_FILE = DATA_DIR / "loop_counter.json"


# === INIT & READ/WRITE LOOP FILE ===
def init_loop_file():
    if not LOOP_FILE.exists():
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(LOOP_FILE, "w") as f:
            json.dump({"count": 1, "offenses": 0, "rebooted": False}, f)


def read_loop_file():
    init_loop_file()
    try:
        with open(LOOP_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"count": 1, "offenses": 0, "rebooted": False}


def write_loop_file(data):
    with open(LOOP_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


# === LOOP TRACKING ===
def get_loop_count():
    data = read_loop_file()
    data["count"] += 1
    write_loop_file(data)
    return data["count"]


def get_offense_count():
    return read_loop_file().get("offenses", 0)


def log_offense():
    data = read_loop_file()
    data["offenses"] = data.get("offenses", 0) + 1
    write_loop_file(data)


def reset_session():
    write_loop_file({"count": 1, "offenses": 0, "rebooted": True})


def was_rebooted():
    return read_loop_file().get("rebooted", False)


# === ENDING CHECK ===
def check_true_ending():
    try:
        meta = read_loop_file()
        return (
            meta.get("offenses", 0) == 0
            and not meta.get("rebooted", False)
            and meta.get("count", 0) >= 6
        )
    except Exception:
        return False


# === UI TEXT GLITCHER ===
def glitch_text(text, glitch_chance=0.1):
    return "".join(
        (
            random.choice(["#", "@", "!", "%", "*", "?"])
            if random.random() < glitch_chance
            else c
        )
        for c in text
    )

# interaction_logger.py
import json
import os
import random
from datetime import datetime
from pathlib import Path
import streamlit as st
from text_utils import clean_text

SESSION_LOG_FILE = Path("data/session_logs.json")


def build_interaction(query, response, loop_count):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    session_id = st.session_state.get("session_id")

    # Ensure session_id is always set
    if not session_id:
        session_id = f"auto-{random.randint(1000, 9999)}"
        st.session_state["session_id"] = session_id

    interaction = {
        "timestamp": timestamp,
        "query": clean_text(query),
        "response": clean_text(response),
        "loop_count": loop_count,  # Ensure this always logs
        "session_id": session_id,
        "memory_fragments": random.randint(5, 40),
        "corruption_level": min(loop_count * 0.15, 0.95),
    }

    os.makedirs(SESSION_LOG_FILE.parent, exist_ok=True)
    try:
        with open(SESSION_LOG_FILE, "r", encoding="utf-8") as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    logs.append(interaction)
    with open(SESSION_LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)

    # Increment session loop count if needed
    if "loop_count" not in st.session_state:
        st.session_state.loop_count = loop_count + 1

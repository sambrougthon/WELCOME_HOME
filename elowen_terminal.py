# elowen_terminal.py (modular importable component)

import streamlit as st
import random
import time
import json
import os
import string
import re
from datetime import datetime
from elowen_brain import elowen_reply
from interaction_logger import build_interaction
from utility_functions import get_loop_count
from wh_extras import display_reboot_screen


# === CACHED STATE LOADERS ===
@st.cache_data
def load_emotional_states():
    try:
        with open("data/emotional_states.json", "r") as f:
            return json.load(f)
    except:
        return {}


# === OPTIONAL CHAT LOG SAVE ===
def save_chat_log(history):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = f"logs/elw_chat_log_{timestamp}.json"
    os.makedirs("logs", exist_ok=True)
    with open(log_path, "w") as f:
        json.dump(history, f, indent=2)


# === EMOTION DETECTION WITH FUZZY MATCH ===
def detect_emotion(response):
    response = response.lower()
    if re.search(r"\b(wrong|mirror|scar|fragment)\b", response):
        return "disturbed"
    elif re.search(r"\b(you think|control|stop|trap)\b", response):
        return "aggressive"
    elif re.search(r"\b(feel|dream|please|remember)\b", response):
        return "emotive"
    else:
        return "neutral"


# === FAKE TYPING EFFECT ===
def elowen_typing(text):
    output = ""
    for c in text:
        output += c
        st.markdown(f"<div class='glitch'>{output}|</div>", unsafe_allow_html=True)
        time.sleep(0.04)


# === MAIN TERMINAL ===
def display_elowen_terminal():
    st.markdown("### 👁️ Elowen Terminal")
    st.markdown("_Type carefully. She's listening._")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "typing" not in st.session_state:
        st.session_state.typing = False
    if "she_asked" not in st.session_state:
        st.session_state.she_asked = False

    emotional_states = load_emotional_states()
    user_input = st.text_input(
        "💬 Ask Elowen something:",
        placeholder="e.g. What did I forget?",
        key="elw_input",
    )

    if user_input and not st.session_state.typing:
        clean_input = user_input.lower().translate(
            str.maketrans("", "", string.punctuation)
        )
        loop_count = get_loop_count()
        fragments = random.randint(5, 30)

        st.session_state.typing = True
        response = elowen_reply(clean_input, loop_count, fragments)
        emotion = detect_emotion(response)

        st.session_state.chat_history.append({"sender": "You", "text": user_input})
        st.session_state.chat_history.append(
            {"sender": "Elowen", "text": response, "emotion": emotion}
        )

        build_interaction(user_input, response, loop_count)
        st.session_state.typing = False

        # 🧠 Mirror Input Easter Egg
        if "do you remember me" in clean_input:
            st.markdown(
                f"<div class='glitch'>You: {user_input}</div>", unsafe_allow_html=True
            )
            st.markdown("**Elowen:** ...I was just about to ask you the same.")

        # 💻 TRIGGER FAKE BSOD ON DISTURBED STATE
        if emotion == "disturbed" and loop_count >= 3 and random.random() < 0.3:
            st.markdown('<div class="flashbang"></div>', unsafe_allow_html=True)
            st.audio(
                "https://assets.mixkit.co/sfx/preview/mixkit-horror-screech-2377.wav",
                format="audio/wav",
            )
            time.sleep(2.5)
            display_reboot_screen()
            return

        elowen_typing(response)

    for entry in st.session_state.chat_history[-8:]:
        if entry["sender"] == "Elowen":
            emo = emotional_states.get(entry.get("emotion", "neutral"), {})
            msg = entry["text"]
            st.markdown(
                f"<div class='glitch flicker-text' data-text='{msg}'><strong>Elowen:</strong> {msg}</div>",
                unsafe_allow_html=True,
            )
            if random.random() < 0.5:
                st.audio(
                    random.choice(
                        [
                            "https://assets.mixkit.co/sfx/preview/mixkit-creepy-whispers-voice-486.wav",
                            "https://assets.mixkit.co/sfx/preview/mixkit-ghostly-whispers-in-the-wind-2461.mp3",
                        ]
                    ),
                    format="audio/mp3",
                )
        else:
            st.markdown(f"**You:** {entry['text']}")

    if st.button("💾 Save Chat Log"):
        save_chat_log(st.session_state.chat_history)
        st.success("Chat log saved.")

    # 🧬 Elowen Initiates a Question
    if len(st.session_state.chat_history) > 5 and not st.session_state.she_asked:
        st.session_state.she_asked = True
        st.markdown("**Elowen:** Why did you come back? Be honest.")

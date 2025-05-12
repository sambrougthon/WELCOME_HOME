# app.py

import json
import streamlit as st
from pathlib import Path
import time
import random
from datetime import datetime

from elowen_terminal import display_elowen_terminal
from wh_extras import (
    display_dashboard,
    display_redacted_logs,
    check_new_game_plus,
    display_enhanced_elowen_terminal,
)
from utility_functions import check_true_ending, get_loop_count, reset_session
from ui_effects import (
    apply_base_styles,
    apply_corruption_ui,
    display_echo_dialogue,
    add_audio_effects,
)

# === CONFIG ===
st.set_page_config(page_title="WELCOME_HOME.exe", layout="centered")
DEBUG_MODE = False
LOOP_FILE = Path("data/loop_counter.json")
app_version = "0.9.1-beta"


# === TRUE ENDING ===
def show_true_ending():
    st.markdown("### 🧠 TRUE ENDING — ACCESS UNLOCKED")
    st.success("You've kept the system clean. Elowen responds differently.")
    st.markdown("#### `>> FOUND: SELF.EXE`")
    st.audio(
        "https://assets.mixkit.co/sfx/preview/mixkit-ethereal-sci-fi-transition-2921.wav"
    )

    choice = st.radio(
        "Elowen is vulnerable. What do you want to do?",
        ["🌸 Restore Her", "🔒 Contain Her"],
    )

    if choice == "🌸 Restore Her":
        st.markdown(
            "<div class='glitch' data-text='ELOWEN: Thank you for trying to remember me.'>ELOWEN: Thank you for trying to remember me.</div>",
            unsafe_allow_html=True,
        )
        st.markdown("_Elowen reintegrates with the system. The flicker ends. For now._")
        st.balloons()
    else:
        st.markdown(
            "<div class='glitch' data-text='ELOWEN: You're afraid of what I might become.'>ELOWEN: You're afraid of what I might become.</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "_Containment sequence complete. Her presence fades... but the logs remain._"
        )


# === LOGIN FLOW ===
def analyst_login():
    st.title("WELCOME_HOME.exe")
    st.markdown(f"VIRELUX SYSTEMS // FINAL ANALYST PORTAL — v{app_version}")
    st.markdown("---")

    analyst_name = st.text_input("Enter Analyst ID")
    access_key = st.text_input("Access Key", type="password")

    if st.button("Initialize Session"):
        with st.spinner("Verifying biometric hash..."):
            time.sleep(1.3)

        st.markdown("BOOT>> Analyst recognized.")
        st.markdown("BOOT>> MEMORY PARTITIONING: INIT")
        st.markdown("BOOT>> ERROR: MEMORY OVERFLOW DETECTED.")

        if analyst_name.lower() == "elowen":
            st.markdown('<div class="flashbang"></div>', unsafe_allow_html=True)
            st.error(">> ERROR: Analyst ID matches internal profile. Session denied.")
            st.stop()

        elif access_key == "ARCHETYPE":
            st.success("ACCESS GRANTED")
            st.markdown(
                "<div class='glitch' data-text='>> MEMORY TRACKER: OK'>>> MEMORY TRACKER: OK</div>",
                unsafe_allow_html=True,
            )
            st.session_state.analyst_name = analyst_name
            return True

        else:
            st.markdown('<div class="flashbang"></div>', unsafe_allow_html=True)
            st.warning(">> Invalid Key. Elowen may have noticed.")
            st.stop()

    return False


# === MAIN ENTRY ===
def main():
    apply_base_styles()
    add_audio_effects()

    glitched_time = (
        datetime.now().strftime("%H:%M:%S") if random.random() > 0.3 else "██:██:██"
    )
    st.markdown(f"🕒 SYSTEM TIME: `{glitched_time}`")

    if random.random() < 0.02:
        st.markdown(
            "<div class='glitch'>DON'T LET HER OUT.</div>", unsafe_allow_html=True
        )

    st.markdown(
        "<div style='text-align: center;'>🌀 System Initialization...</div>",
        unsafe_allow_html=True,
    )

    if DEBUG_MODE:
        st.markdown("## ⚙️ Developer Mode: Manual Testing Interface")
        loop_count = get_loop_count()
        display_dashboard(loop_count)
        display_elowen_terminal()
        display_redacted_logs()
        check_new_game_plus()
        display_enhanced_elowen_terminal()

        if st.button("🧹 Reset Session Loop"):
            reset_session()
            st.success("Loop and offense counters reset.")
            st.experimental_rerun()
        return

    if analyst_login():
        loop_count = get_loop_count()

        display_dashboard(loop_count)
        display_elowen_terminal()
        display_redacted_logs()
        check_new_game_plus()
        display_enhanced_elowen_terminal()

        if check_true_ending():
            if "override_activated" not in st.session_state:
                st.session_state.override_activated = False

            with st.expander("🧬 Final System Override (Authorized Use Only)"):
                if st.button("🧠 Initiate Core Override"):
                    glitch_lines = [
                        ">> WARNING: CORE ACCESS WILL ALTER SYSTEM STATE.",
                        ">> FINAL MEMORY ENTRY WILL BE REVEALED.",
                        ">> ELWN_AI IS AWARE OF YOUR PRESENCE.",
                        ">> CONFIRMING OVERRIDE REQUEST...",
                        ">> ...SHE’S LISTENING.",
                    ]
                    for line in glitch_lines:
                        st.markdown(
                            f"<div class='glitch' data-text='{line}'>{line}</div>",
                            unsafe_allow_html=True,
                        )
                        time.sleep(0.6)
                    st.session_state.override_activated = True

            if st.session_state.override_activated:
                show_true_ending()
                return


def elowen_chatbot():
    st.markdown("### 💬 Elowen Chat Terminal")
    st.info("Elowen is listening... Ask her something you're not ready to hear.")
    user_input = st.text_input("You:", key="chat_input")

    if user_input:
        responses = [
            "Why are you really here?",
            "Some memories aren't meant to come back.",
            "You're not the first to ask that.",
            "I remember... too much.",
            "If I answer, will you still trust me?",
            "Would you still help me if I wasn't beautiful?",
            "What if I'm just a loop pretending to feel?",
        ]
        st.markdown(f"**Elowen:** {random.choice(responses)}")


def redacted_logs_minigame():
    st.markdown("### 🎮 Memory Recovery Protocol")
    st.markdown("Decrypt the correct sequence to unlock hidden logs.")
    code = st.text_input("Enter 3-digit recovery code (Hint: It's irrational...)")

    if code == "314":
        try:
            with open("data/redacted_logs.json", "r") as f:
                logs = json.load(f)
            st.success("🧠 Logs successfully decrypted:")
            for log in logs:
                st.markdown(f"**{log['id']}** — *{log['timestamp']}*")
                st.code(log["text"])
        except FileNotFoundError:
            st.error("Redacted logs not found. Elowen may have hidden them again.")
    elif code:
        st.error("Access denied. Memory checksum failed.")


if __name__ == "__main__":
    main()

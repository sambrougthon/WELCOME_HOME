# wh_extras.py — Support Modules for WELCOME_HOME

import streamlit as st
import pandas as pd
import json
import time
import random
from datetime import datetime
from pathlib import Path

from interaction_logger import build_interaction
from elowen_brain import elowen_reply
from utility_functions import get_loop_count, check_true_ending
from ui_effects import apply_corruption_ui, display_echo_dialogue


# === DASHBOARD ===
def display_dashboard(loop_count):
    st.markdown("## 📊 Analyst Dashboard")
    st.markdown(f"### 🧠 Loop Count: {loop_count}")

    try:
        with open("data/session_logs.json", "r") as f:
            session_data = json.load(f)
        df = pd.DataFrame(session_data)

        df["status"] = df.apply(
            lambda row: (
                "⚠️ CORRUPTED" if row.get("corruption_level", 0) > 0.75 else "🟢 OK"
            ),
            axis=1,
        )

        st.markdown("### 🗂️ Recent Sessions")
        st.dataframe(df.tail(10), use_container_width=True)

        st.markdown("#### 🔍 Log Status Overview:")
        corrupted = df[df["status"] == "⚠️ CORRUPTED"]
        if not corrupted.empty:
            for _, row in corrupted.iterrows():
                st.code(
                    f"> Session {row.get('session_id', 'unknown')} flagged: "
                    f"Loop={row.get('loop_count', '❓')} | "
                    f"Corruption={row.get('corruption_level', 0):.2f}"
                )
        else:
            st.success("No corrupted logs detected. But that could change.")

    except FileNotFoundError:
        st.warning("No session logs found.")


# === REDACTED LOGS ===
def display_redacted_logs():
    st.markdown("### 🔐 Redacted Logs")
    try:
        with open("data/redacted_logs.json", "r") as f:
            logs = json.load(f)
        for log in logs:
            display_text = log["text"] if not log.get("locked") else "🔒 LOCKED"
            st.markdown(f"**[{log['id']}]** — {log['timestamp']}")
            st.markdown(
                f"<div class='glitch' data-text='{display_text}'>{display_text}</div>",
                unsafe_allow_html=True,
            )
            st.markdown("---")
    except FileNotFoundError:
        st.warning("No redacted logs found.")


# === NEW_GAME+ CHECK ===
def check_new_game_plus():
    st.markdown("### 🧬 NEW_GAME+ Protocol")
    st.markdown("_Loop integrity check initiated..._")
    try:
        with open("data/loop_counter.json", "r") as f:
            data = json.load(f)
        if data.get("count", 0) >= 8 and data.get("offenses", 0) == 0:
            st.success("✅ Eligible for NEW_GAME+ mode.")
            st.markdown("**Elowen is watching. Be careful what you trigger.**")
        else:
            st.info("Not yet eligible. Loop deeper.")
    except Exception as e:
        st.warning(f"Loop data unavailable: {e}")


# === ENHANCED TERMINAL ===
def display_enhanced_elowen_terminal():
    st.markdown("### 👁️ Enhanced Terminal Interface")
    st.markdown(
        "<div class='glitch' data-text='Welcome back, Observer.'>Welcome back, Observer.</div>",
        unsafe_allow_html=True,
    )
    st.markdown("_Her presence feels stronger this time..._")


# === REBOOT SCREEN ===
def display_reboot_screen():
    st.markdown("## 🔁 SYSTEM REBOOTING...")
    st.markdown("Please wait while memory systems are restructured.")
    progress = st.progress(0)
    reboot_text = [
        ">>> Terminating corrupted thread...",
        ">>> Recovering last known memory...",
        ">>> Memory signature unstable...",
        ">>> Integrating foreign fragment...",
        ">>> WARNING: Residual consciousness detected.",
    ]
    for i in range(100):
        if i in [15, 35, 55, 75, 95]:
            st.markdown(
                f"<div class='glitch'>{random.choice(reboot_text)}</div>",
                unsafe_allow_html=True,
            )
        time.sleep(0.02)
        progress.progress(i + 1)
    st.success("Memory integrity partially restored. Proceed with caution.")

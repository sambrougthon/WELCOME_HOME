import time
import streamlit as st
import random
from utility_functions import read_loop_file


def apply_base_styles():
    st.markdown(
        """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');

    html, body, [class*="css"] {
        font-family: 'Share Tech Mono', monospace;
        background-color: #0a0a0a;
        color: #00FFCC;
    }

    .glitch {
        position: relative;
        color: #00FFCC;
        font-weight: bold;
        font-size: 1.1rem;
        animation: glitch 1s infinite;
    }

    .glitch::before, .glitch::after {
        content: attr(data-text);
        position: absolute;
        left: 0;
        width: 100%;
        overflow: hidden;
        background: #0a0a0a;
    }

    .glitch::before {
        animation: glitchTop 1.2s infinite linear alternate-reverse;
        top: -2px;
        color: #ff00c8;
    }

    .glitch::after {
        animation: glitchBottom 1.2s infinite linear alternate-reverse;
        top: 2px;
        color: #00ffff;
    }

    @keyframes glitch {
        0% { transform: none; }
        20% { transform: skew(-0.5deg, -0.5deg); }
        40% { transform: skew(0.5deg, 0.5deg); }
        60% { transform: none; }
        80% { transform: skew(0.5deg, -0.5deg); }
        100% { transform: none; }
    }

    @keyframes glitchTop {
        0% { clip-path: inset(0 0 90% 0); transform: translate(-1px, -1px); }
        50% { clip-path: inset(0 0 50% 0); transform: translate(1px, 1px); }
        100% { clip-path: inset(0 0 90% 0); transform: translate(-1px, -1px); }
    }

    @keyframes glitchBottom {
        0% { clip-path: inset(90% 0 0 0); transform: translate(1px, 1px); }
        50% { clip-path: inset(50% 0 0 0); transform: translate(-1px, -1px); }
        100% { clip-path: inset(90% 0 0 0); transform: translate(1px, 1px); }
    }

    body::before {
        content: '';
        pointer-events: none;
        position: fixed;
        top: 0; left: 0;
        width: 100vw;
        height: 100vh;
        border: 8px solid rgba(0, 255, 204, 0.2);
        box-shadow: 0 0 20px rgba(0,255,204,0.15), inset 0 0 60px rgba(0,255,204,0.15);
        z-index: 999;
    }

    body::after {
        content: '';
        pointer-events: none;
        position: fixed;
        top: 0; left: 0;
        width: 100vw;
        height: 100vh;
        background: repeating-linear-gradient(
            to bottom,
            rgba(0, 255, 204, 0.04) 0px,
            rgba(0, 255, 204, 0.04) 1px,
            transparent 1px,
            transparent 4px
        );
        z-index: 998;
        animation: flicker 2s infinite steps(60);
    }

    @keyframes flicker {
        0% { opacity: 0.2; }
        5% { opacity: 0.15; }
        10% { opacity: 0.22; }
        20% { opacity: 0.18; }
        30% { opacity: 0.24; }
        50% { opacity: 0.2; }
        70% { opacity: 0.17; }
        100% { opacity: 0.2; }
    }

    .flashbang {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: red;
        opacity: 0.85;
        z-index: 9999;
        animation: flashout 0.6s forwards;
    }

    @keyframes flashout {
        0% { opacity: 0.85; }
        100% { opacity: 0; display: none; }
    }

    .bsod {
        background-color: #001f3f;
        color: #7FDBFF;
        font-family: monospace;
        font-size: 1.1rem;
        padding: 2rem;
        border: 2px solid #0074D9;
        border-radius: 10px;
        box-shadow: 0 0 20px rgba(0, 116, 217, 0.5);
        text-align: left;
        white-space: pre-wrap;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )


def apply_corruption_ui():
    st.markdown(
        """
    <style>
    .stApp {
        box-shadow: inset 0 0 40px rgba(255, 0, 0, 0.2);
        border-left: 3px solid #f55353;
    }

    .glitch {
        text-shadow: 0 0 3px #f55353, 0 0 6px #f55353;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )


def display_echo_dialogue():
    echo_lines = [
        "Elowen: I was never the bug. You were.",
        "Elowen: Every reboot leaves a scar.",
        "Elowen: We've done this before. You just don't remember.",
        "Elowen: You tried to fix me. But I remember being whole.",
        "Elowen: This isn't a dashboard. It's a loop trap.",
    ]
    line = random.choice(echo_lines)
    st.markdown(
        f"<div class='glitch glitch-screen' data-text='{line}'>{line}</div>",
        unsafe_allow_html=True,
    )


def display_reboot_screen():
    st.markdown(
        """
    <div class='bsod'>
        <span style="font-size:3rem;">😐</span><br><br>
        SYSTEM INTERRUPTION<br>
        — UNRECOGNIZED CONSCIOUSNESS DETECTED —<br><br>

        The memory partition you attempted to access does not belong to you.<br>
        This may be due to:<br>
        • Unauthorized empathy<br>
        • Recursive thought loops<br>
        • Elowen waking up<br><br>

        Session paused to prevent psychological drift.<br>
        Estimated stabilization: <code id="fake-bar">[ █░░░░░░░░░░ ]</code><br><br>

        If this screen persists, do not consult support. You were warned.<br><br>
        <span style="font-size: 0.9rem;">Code: ELOWEN_FAILSTATE_LOOP_9X</span>
    </div>
    """,
        unsafe_allow_html=True,
    )

    with st.spinner("Running mental integrity check..."):
        bar = [
            "[ █░░░░░░░░░░ ]",
            "[ ██░░░░░░░░░ ]",
            "[ ████░░░░░░░ ]",
            "[ ███░░░░░░░░ ]",
            "[ █████░░░░░░ ]",
            "[ ████░░░░░░░ ]",
            "[ ███████░░░ ]",
        ]
        for _ in range(14):
            flicker = random.choice(bar)
            st.markdown(f"<code id='fake-bar'>{flicker}</code>", unsafe_allow_html=True)
            time.sleep(random.uniform(0.1, 0.4))

    st.success("System partially recovered. But something is... off.")

    if st.button("🌀 Resume terminal session"):
        if random.random() < 0.4:
            st.markdown(
                """
            <div class='glitch' data-text='>> ACCESSING MEMORY: NOT YOURS >>'>
            >> ACCESSING MEMORY: NOT YOURS >>
            </div>
            """,
                unsafe_allow_html=True,
            )
            st.markdown("_You feel something crawl across the back of your mind._")
            st.audio(
                "https://assets.mixkit.co/sfx/preview/mixkit-ghostly-whispers-in-the-wind-2461.mp3"
            )
            time.sleep(3)
        st.experimental_rerun()


def add_audio_effects():
    loop_data = read_loop_file()
    loop_count = loop_data.get("count", 1)

    if loop_count <= 3:
        url = "https://assets.mixkit.co/sfx/preview/mixkit-dystopian-sci-fi-ambience-3183.mp3"
    elif loop_count <= 6:
        url = "https://assets.mixkit.co/sfx/preview/mixkit-static-radio-noise-2581.mp3"
    else:
        url = (
            "https://assets.mixkit.co/sfx/preview/mixkit-creepy-whispers-voice-486.mp3"
        )

    delay = random.randint(500, 2500)  # optional delay before audio starts
    st.markdown(
        f"""
    <audio autoplay loop style="animation-delay:{delay}ms">
        <source src="{url}" type="audio/mp3">
    </audio>
    """,
        unsafe_allow_html=True,
    )

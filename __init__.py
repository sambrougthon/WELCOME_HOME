# welcome_home/__init__.py

# Core system tools
from .utility_functions import (
    get_loop_count,
    get_offense_count,
    log_offense,
    reset_session,
    check_true_ending,
    glitch_text,
)

# Terminal behavior
from .elowen_terminal import display_elowen_terminal

# AI logic
from .elowen_brain import elowen_reply

# Logging behavior
from .interaction_logger import build_interaction

# Visual effects
from .ui_effects import (
    apply_base_styles,
    apply_corruption_ui,
    display_echo_dialogue,
    display_reboot_screen,
    add_audio_effects,
)

# App layout + dashboard
from .wh_extras import (
    display_dashboard,
    display_redacted_logs,
    check_new_game_plus,
    display_enhanced_elowen_terminal,
)

# Optional mini-games, debug features, etc.
# from .secret_minigames import redacted_logs_minigame  # <- If you have one later

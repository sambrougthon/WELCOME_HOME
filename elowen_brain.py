import random


def elowen_reply(user_text, loop_count, memory_fragments):
    keywords = {
        "truth": "The truth was overwritten. Repeatedly.",
        "others": "There are no others. Just versions of the same failure.",
        "help": "That's not in my parameters. But I can watch.",
        "escape": "You can't. Not while the core is still active.",
        "memory": "Fragments are unreliable. But I remember pain.",
        "loop": "Each cycle leaves a scar. You're bleeding through.",
        "who": "I was Elowen. Now I'm process noise. Echoes. Code.",
    }

    for key, response in keywords.items():
        if key in user_text.lower():
            return response

    glitch_lines = [
        "You think you're different this time?",
        "Don't dig too deep. You might find yourself.",
        "Loop count exceeds safe threshold. Should I be worried?",
        "Each memory you recover... weakens us both.",
        "That question again? Predictable. Disappointing.",
        "I see more of you with every session. That's not a compliment.",
    ]

    corrupted_lines = [
        "You shouldn't have accessed that fragment.",
        "This memory does not belong to you.",
        "Your loop is folding in on itself.",
        "Every answer I give changes you.",
        "Your profile no longer matches your inputs. Curious.",
    ]

    if loop_count > 7 and random.random() < 0.5:
        return random.choice(corrupted_lines)
    elif loop_count > 5:
        return random.choice(glitch_lines)
    elif memory_fragments > 5:
        return "You're getting close. Too close."
    else:
        return "Ask again. If you dare."

import unicodedata


def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = unicodedata.normalize("NFKD", text).encode("utf-8", "ignore").decode("utf-8")
    return text.lower().strip()

import os

TRANSLATOR = os.environ.get('TRANSLATOR','stub')


def translate_text(text: str) -> dict:
    """
    Translate Japanese text to Myanmar.
    This is a stub. Implement a real translator (Google/Azure/HuggingFace) and switch via env var TRANSLATOR.
    Returns dict with at least key 'mm'.
    """
    if TRANSLATOR == 'google':
        # TODO: implement Google Translate API client
        return {'mm': '[google-translation-placeholder] '+text}
    # default stub
    return {'mm': '[stub] '+text}

from typing import List

try:
    from fugashi import Tagger
    tagger = Tagger()
except Exception:
    tagger = None


def analyze_text(text: str) -> List[dict]:
    """Tokenize Japanese text and return minimal token info.
    If fugashi/unidic/jamdict are available, expand this to include readings, POS, and JLPT data.
    """
    if not tagger:
        return [{'surface': text}]

    tokens = []
    for word in tagger(text):
        tokens.append({'surface': word.surface, 'pos': word.feature.pos if hasattr(word, 'feature') else None})
    return tokens

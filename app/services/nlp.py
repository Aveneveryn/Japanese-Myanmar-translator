from typing import List, Dict

# fugashi tokenization
try:
    from fugashi import Tagger
    tagger = Tagger()
except Exception:
    tagger = None

# jamdict dictionary lookup (optional)
try:
    from jamdict import Jamdict
    jam = Jamdict()
except Exception:
    jam = None


def analyze_text(text: str) -> List[Dict]:
    """
    Tokenize Japanese text and return token info.
    Each token contains: surface, base_form, reading, pos, meanings (if jamdict works).
    """
    if not tagger:
        return [{'surface': text}]

    tokens = []
    for node in tagger(text):
        surface = node.surface
        # attempt to extract features (works with unidic)
        feats = getattr(node, 'feature', None)
        pos = None
        base = None
        reading = None
        try:
            # Many unidic builds expose lemma/base and reading via features
            if feats:
                pos = getattr(feats, 'pos1', None) or getattr(feats, 'pos', None)
                base = getattr(feats, 'lemma', None) or getattr(feats, 'base_form', None)
                reading = getattr(feats, 'reading', None)
        except Exception:
            pos = None

        # jamdict lookup by base form (best-effort)
        meanings = []
        if jam and base:
            try:
                entries = jam.lookup(base)
                for lex in entries.all_lexemes():
                    for sense in lex.senses:
                        for g in sense.glosses:
                            meanings.append(g.text)
            except Exception:
                meanings = []

        tokens.append({
            'surface': surface,
            'base_form': base,
            'reading': reading,
            'pos': pos,
            'meanings': meanings
        })

    return tokens

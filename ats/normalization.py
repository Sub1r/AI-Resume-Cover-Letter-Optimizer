import re
from ats.constants import SYNONYM_MAP

# ============================================================
# TEXT NORMALIZATION
# ============================================================

def normalize_text(text: str) -> str:

    if not text:
        return ""

    text = text.lower()

    text = normalize_unicode(text)

    text = normalize_separators(text)

    text = apply_synonyms(text)

    text = collapse_whitespace(text)

    return text

def normalize_unicode(text: str) -> str:

    return (
        text.replace("–", "-")
            .replace("—", "-")
            .replace("’", "'")
            .replace("“", '"')
            .replace("”", '"')
    )

def normalize_separators(text: str) -> str:

    text = re.sub(r"[_\-]+", " ", text)

    text = re.sub(
        r"[^\w\s./+#]",
        " ",
        text
    )

    return text

def apply_synonyms(text: str) -> str:

    for old, new in SYNONYM_MAP.items():

        pattern = rf"\b{re.escape(old)}\b"

        text = re.sub(pattern, new, text)

    return text

def collapse_whitespace(text: str) -> str:

    return re.sub(
        r"\s+",
        " ",
        text
    ).strip()
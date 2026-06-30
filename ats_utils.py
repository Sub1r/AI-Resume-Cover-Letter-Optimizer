import re


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_keywords(text):
    common_words = {
        "the", "and", "or", "to", "of", "in", "for", "with", "a", "an",
        "is", "are", "on", "as", "by", "be", "this", "that", "from",
        "we", "you", "our", "your", "will", "can", "should", "must",
        "candidate", "role", "job", "work", "team", "company"
    }

    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    keywords = []

    for word in words:
        if len(word) > 3 and word not in common_words:
            keywords.append(word)

    return set(keywords)


def calculate_match_score(resume_text, job_description):
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_description)

    if not job_keywords:
        return 0, []

    matched_keywords = resume_keywords.intersection(job_keywords)

    score = int((len(matched_keywords) / len(job_keywords)) * 100)

    return score, sorted(list(matched_keywords))
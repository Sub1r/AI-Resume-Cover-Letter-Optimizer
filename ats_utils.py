import re
from collections import Counter


COMMON_WORDS = {
    "the", "and", "or", "to", "of", "in", "for", "with", "a", "an",
    "is", "are", "on", "as", "by", "be", "this", "that", "from",
    "we", "you", "our", "your", "will", "can", "should", "must",
    "candidate", "role", "job", "work", "team", "company", "looking",
    "required", "preferred", "skills", "experience", "ability"
}


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_keywords(text):
    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    keywords = []

    for word in words:
        if len(word) > 3 and word not in COMMON_WORDS:
            keywords.append(word)

    return keywords


def calculate_match_score(resume_text, job_description):
    resume_keywords = set(extract_keywords(resume_text))
    job_keyword_list = extract_keywords(job_description)

    if not job_keyword_list:
        return 0, [], []

    job_keyword_counts = Counter(job_keyword_list)
    important_job_keywords = set(job_keyword_counts.keys())

    matched_keywords = resume_keywords.intersection(important_job_keywords)
    missing_keywords = important_job_keywords.difference(resume_keywords)

    score = int((len(matched_keywords) / len(important_job_keywords)) * 100)

    return (
        score,
        sorted(list(matched_keywords)),
        sorted(list(missing_keywords))
    )
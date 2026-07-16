import re
from dataclasses import dataclass, field
from typing import Set

# ============================================================
# CONFIGURATION
# ============================================================

SCORE_WEIGHTS = {
    "skills": 45,
    "experience": 20,
    "projects": 10,
    "education": 5,
    "certifications": 5,
    "soft_skills": 10,
    "formatting": 5,
}

SYNONYM_MAP = {

    # Cloud
    "amazon web services": "aws",
    "amazon aws": "aws",

    # DevOps
    "continuous integration": "ci/cd",
    "continuous deployment": "ci/cd",
    "continuous delivery": "ci/cd",

    "github-actions": "github actions",

    # Programming
    "javascript": "javascript",
    "js": "javascript",

    "typescript": "typescript",
    "ts": "typescript",

    # AI
    "large language models": "llm",

    # Databases
    "postgres": "postgresql",

    # Common formatting
    "ci cd": "ci/cd",
}

SECTION_HEADERS = {

    "requirements": "required",

    "required qualifications": "required",

    "qualifications": "required",

    "skills": "required",

    "preferred": "preferred",

    "preferred qualifications": "preferred",

    "nice to have": "preferred",

    "responsibilities": "responsibilities",

    "what you'll do": "responsibilities",

    "what you will do": "responsibilities",

    "duties": "responsibilities",

    "job responsibilities": "responsibilities",

}

RESUME_SECTION_HEADERS = {

    "skills": "skills",
    "technical skills": "skills",
    "technologies": "skills",
    "tech stack": "skills",

    "projects": "projects",

    "experience": "experience",
    "professional experience": "experience",
    "work experience": "experience",

    "education": "education",

    "certifications": "certifications",

}

CONNECTOR_WORDS = {
    "experience",
    "knowledge",
    "proficiency",
    "familiarity",
    "required",
    "preferred",
    "working",
    "hands-on",
    "ability",
    "understanding",
    "plus",
    "with",
    "using",
}

# ============================================================
# DATA CLASSES
# ============================================================

@dataclass
class SkillMatch:
    matched: set[str] = field(default_factory=set)
    missing: set[str] = field(default_factory=set)
    score: float = 0.0

@dataclass
class ATSResult:
    ats_score: int = 0

    matched_skills: list[str] = field(default_factory=list)
    missing_skills: list[str] = field(default_factory=list)
    section_scores: dict[str, int] = field(default_factory=dict)

@dataclass
class JobDescription:
    required_skills: set[str] = field(default_factory=set)
    preferred_skills: set[str] = field(default_factory=set)
    responsibilities: set[str] = field(default_factory=set)

@dataclass
class Resume:
    skills: set[str] = field(default_factory=set)
    sections: dict[str, str] = field(default_factory=dict)

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

# ============================================================
# EXTRACTION
# ============================================================

def normalize_delimiters(text: str) -> str:
    """
    Convert all common separators into commas.
    """

    separators = [
        ";",
        "|",
        "/",
    ]

    for sep in separators:
        text = text.replace(sep, ",")

    text = re.sub(r"\band\b", ",", text)
    text = re.sub(r"\bor\b", ",", text)

    return text

def clean_item(item: str) -> str:

    item = normalize_text(item)

    words = []

    for word in item.split():

        if word in CONNECTOR_WORDS:
            continue

        words.append(word)

    return " ".join(words)

def extract_items_from_line(line: str) -> set[str]:
    """
    Extract individual skills from one JD line.
    """

    line = normalize_text(line)

    line = normalize_delimiters(line)

    parts = line.split(",")

    results = set()

    for part in parts:

        cleaned = clean_item(part)

        if len(cleaned) < 2:
            continue

        results.add(cleaned)

    return results

def parse_resume(resume_text: str) -> Resume:
    """
    Parse resume into structured data.
    Placeholder implementation.
    """

    resume = Resume()

    resume.sections["raw"] = normalize_text(resume_text)

    return resume

def parse_job_description(job_description: str) -> JobDescription:
    """
    Parse job description into structured data.
    Placeholder implementation.
    """

    jd = JobDescription()

    jd.required_skills = extract_items_from_line(job_description)

    return jd


# ============================================================
# MATCHING
# ============================================================

def match_skills(resume_skills, required_skills):

    matched = resume_skills & required_skills
    missing = required_skills - resume_skills

    return SkillMatch(
        matched=matched,
        missing=missing,
        score=0.0
    )


# ============================================================
# SCORING
# ============================================================

def score_skills(skill_match: SkillMatch):

    if not skill_match.matched and not skill_match.missing:
        return 0

    total = len(skill_match.matched) + len(skill_match.missing)

    return round(
        len(skill_match.matched) / total
        * SCORE_WEIGHTS["skills"]
    )


def calculate_final_score(section_scores):

    return min(sum(section_scores.values()), 100)


# ============================================================
# MAIN PUBLIC FUNCTION
# ============================================================

def analyze_resume(resume_text: str, job_description: str):
    """
    Main ATS analysis pipeline.
    """

    resume = parse_resume(resume_text)

    job = parse_job_description(job_description)

    skill_match = match_skills(
        resume.skills,
        job.required_skills,
    )

    section_scores = {
        "skills": score_skills(skill_match)
    }

    result = ATSResult()

    result.ats_score = calculate_final_score(section_scores)

    result.matched_skills = sorted(skill_match.matched)

    result.missing_skills = sorted(skill_match.missing)

    result.section_scores = section_scores

    return result

def calculate_match_score(resume_text: str, job_description: str):
    """
    Backward-compatible wrapper.

    Keeps the old API working while the new ATS engine
    is being developed.
    """

    result = analyze_resume(resume_text, job_description)

    return (
        result.ats_score,
        result.matched_skills,
        result.missing_skills,
    )
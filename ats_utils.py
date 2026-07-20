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

    "required skills": "required",

    "technical skills": "required",

    "mandatory skills": "required",

    "essential skills": "required",

    "qualifications": "required",

    "skills": "required",

    "preferred": "preferred",

    "preferred skills": "preferred",

    "preferred qualifications": "preferred",
    
    "desired skills": "preferred",

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

CATEGORY_LABELS = {
    "languages",
    "language",
    "frameworks",
    "framework",
    "libraries",
    "library",
    "tools",
    "tool",
    "developer tools",
    "cloud",
    "database",
    "databases",
    "technologies",
    "technology",
    "platforms",
    "platform",
    "operating systems",
    "operating system",
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
class CategoryMatch:
    category: str
    matched: set[str] = field(default_factory=set)
    missing: set[str] = field(default_factory=set)
    score: float = 0.0

@dataclass
class ATSResult:
    ats_score: int = 0

    matched_skills: list[str] = field(default_factory=list)
    missing_skills: list[str] = field(default_factory=list)
    section_scores: dict[str, int] = field(default_factory=dict)
    category_matches: dict[str, CategoryMatch] = field(default_factory=dict)

@dataclass
class JobDescription:
    required_skills: set[str] = field(default_factory=set)
    preferred_skills: set[str] = field(default_factory=set)

    required_skill_categories: dict[str, set[str]] = field(default_factory=dict)
    preferred_skill_categories: dict[str, set[str]] = field(default_factory=dict)

    responsibilities: set[str] = field(default_factory=set)

@dataclass
class Resume:
    skills: set[str] = field(default_factory=set)
    skill_categories: dict[str, set[str]] = field(default_factory=dict)
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
    "•",
    "·",
]

    for sep in separators:
        text = text.replace(sep, ",")

    text = re.sub(r"\band\b", ",", text)
    text = re.sub(r"\bor\b", ",", text)

    return text

def clean_item(item: str) -> str:

    item = item.strip()

    # Remove common bullet characters
    item = re.sub(r"^[•\-\*]+\s*", "", item)

    item = normalize_text(item)

    words = []

    for word in item.split():

        if word in CONNECTOR_WORDS:
            continue

        words.append(word)

    cleaned = " ".join(words)

    if cleaned in CATEGORY_LABELS:
        return ""

    return cleaned

def tokenize_line(line: str) -> list[str]:
    """
    Split a line into raw tokens using the supported delimiters.

    This function does NOT clean or normalize the tokens.
    It only separates them.
    """

    normalized = normalize_delimiters(line)

    return [
        token.strip()
        for token in normalized.split(",")
        if token.strip()
    ]

def extract_items_from_line(line: str) -> set[str]:
    """
    Extract individual skills from one JD line.
    """

    parts = tokenize_line(line)

    results = set()

    for part in parts:

        cleaned = clean_item(part)

        if len(cleaned) < 2:
            continue

        results.add(cleaned)

    return results

def detect_section_header(
    line: str,
    section_headers: dict[str, str],
) -> str | None:
    """
    Detect whether a line is a known section header.

    Returns the normalized section name (e.g. "skills",
    "required", "preferred") or None.
    """

    normalized = normalize_text(line)

    # Remove common markdown prefixes
    normalized = normalized.lstrip("#").strip()

    # Remove trailing colon
    normalized = normalized.rstrip(":").strip()

    return section_headers.get(normalized)

def extract_skill_categories(line: str) -> dict[str, set[str]]:
    """
    Extract categorized skills from a resume line.

    Example:
        Languages: Python, Java
        Frameworks: FastAPI, Django
    """

    results: dict[str, set[str]] = {}

    if ":" not in line:
        return results

    category_text, skills_text = line.split(":", 1)

    category = normalize_text(category_text)

    if category not in CATEGORY_LABELS:
        return results

    skills = extract_items_from_line(skills_text)

    if skills:
        results[category] = skills

    return results

def parse_resume(resume_text: str) -> Resume:
    """
    Parse a resume into structured sections.

    Currently extracts skills while preserving the
    architecture for future section parsing.
    """

    resume = Resume()

    current_section = None
    current_skill_category = None

    for raw_line in resume_text.splitlines():

        line = raw_line.strip()

        if not line:
            continue

        current_section_name = detect_section_header(
    line,
    RESUME_SECTION_HEADERS,
)

        if current_section_name:
            current_section = current_section_name

            # Reset the current skill category whenever we enter
            # a new resume section.
            current_skill_category = None

            continue

        if (
            current_section == "skills"
            and normalize_text(line) in CATEGORY_LABELS
        ):
            current_skill_category = normalize_text(line)
            continue

        if current_section == "skills":

            items = extract_items_from_line(line)

            # Always maintain the flat skill set
            resume.skills.update(items)

            # Support the existing "Category: skill1, skill2" format
            categorized = extract_skill_categories(line)

            for category, skills in categorized.items():
                resume.skill_categories.setdefault(category, set()).update(skills)

            # Support multi-line category layouts
            if current_skill_category and items:
                resume.skill_categories.setdefault(
                    current_skill_category,
                    set()
                ).update(items)

                resume.sections.setdefault(current_section or "raw", "")
                resume.sections[current_section or "raw"] += line + "\n"

    return resume

def parse_job_description(job_description: str) -> JobDescription:
    """
    Parse a job description into structured sections.

    The parser reads the document line by line, detects section
    headers, and extracts information into a structured
    JobDescription object.
    """

    jd = JobDescription()

    current_section = None
    current_skill_category = None

    for raw_line in job_description.splitlines():

        line = raw_line.strip()

        if not line:
            continue

        current_section_name = detect_section_header(
    line,
    SECTION_HEADERS,
)

        if current_section_name:
            current_section = current_section_name

            # Reset the current skill category whenever we
            # enter a new JD section.
            current_skill_category = None

            continue

        if (
            current_section in {"required", "preferred"}
            and normalize_text(line) in CATEGORY_LABELS
        ):
            current_skill_category = normalize_text(line)
            continue

        items = extract_items_from_line(line)

        if not items:
            continue

        if current_section == "required":

            # Maintain backward compatibility
            jd.required_skills.update(items)

            # Support inline categories (e.g. "Languages: Python, Java")
            categorized = extract_skill_categories(line)

            for category, skills in categorized.items():
                jd.required_skill_categories.setdefault(
                    category,
                    set()
                ).update(skills)

            # Support multi-line categories
            if current_skill_category and items:
                jd.required_skill_categories.setdefault(
                    current_skill_category,
                    set()
                ).update(items)

        elif current_section == "preferred":

            # Maintain backward compatibility
            jd.preferred_skills.update(items)

            # Support inline categories
            categorized = extract_skill_categories(line)

            for category, skills in categorized.items():
                jd.preferred_skill_categories.setdefault(
                    category,
                    set()
                ).update(skills)

            # Support multi-line categories
            if current_skill_category and items:
                jd.preferred_skill_categories.setdefault(
                    current_skill_category,
                    set()
                ).update(items)

        elif current_section == "responsibilities":
            jd.responsibilities.update(items)

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

def match_skill_categories(
    resume_categories: dict[str, set[str]],
    job_categories: dict[str, set[str]],
) -> dict[str, CategoryMatch]:
    """
    Match resume skills against job skills by category.
    """

    matches: dict[str, CategoryMatch] = {}

    for category, required_skills in job_categories.items():

        candidate_skills = resume_categories.get(category, set())

        matched = candidate_skills & required_skills
        missing = required_skills - candidate_skills

        if required_skills:
            score = (len(matched) / len(required_skills)) * 100
        else:
            score = 100.0

        matches[category] = CategoryMatch(
            category=category,
            matched=matched,
            missing=missing,
            score=round(score, 1),
        )

    return matches


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
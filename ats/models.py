from dataclasses import dataclass, field

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
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from ats_utils import (
    parse_resume,
    parse_job_description,
    match_skills,
)

resume_text = """
John Smith

Technical Skills

Languages:
Python, Java

Frameworks:
FastAPI, Django

Cloud:
AWS, Azure

Databases:
PostgreSQL, MySQL

Developer Tools:
Docker, Git
"""

jd_text = """
Required Skills

Languages:
Python

Frameworks:
FastAPI

Cloud:
AWS

Databases:
PostgreSQL

Developer Tools:
Docker
Git
"""

resume = parse_resume(resume_text)
job = parse_job_description(jd_text)

match = match_skills(
    resume.skills,
    job.required_skills
)

print("Matched:")
print(match.matched)

print()

print("Missing:")
print(match.missing)

print()

print("Score:")
print(match.score)
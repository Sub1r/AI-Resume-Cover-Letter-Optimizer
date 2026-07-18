import sys
from pathlib import Path

# Add the project root to Python's module search path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from ats_utils import parse_job_description

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

job = parse_job_description(jd_text)

print("===== JOB DESCRIPTION =====")
print(jd_text)
print("===========================")
print()

print("Job Object:")
print(job)

print()

print("Required Skills:")
print(job.required_skills)

print()

print("Preferred Skills:")
print(job.preferred_skills)

print()

print("Responsibilities:")
print(job.responsibilities)
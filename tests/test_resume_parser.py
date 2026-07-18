import sys
from pathlib import Path

# Add the project root to Python's module search path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from ats_utils import parse_resume

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

resume = parse_resume(resume_text)

print("Resume Skills:")
print(resume.skills)

print()

print("Skill Categories:")
print(resume.skill_categories)
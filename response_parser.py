def parse_ai_response(ai_response):
    sections = {
        "Match Score": "",
        "Strong Matches": "",
        "Missing Skills or Keywords": "",
        "Resume Improvement Suggestions": "",
        "Tailored Cover Letter": "",
        "Interview Preparation Questions": ""
    }

    current_section = None

    for line in ai_response.splitlines():
        cleaned_line = line.strip().replace("#", "").strip()

        if cleaned_line in sections:
            current_section = cleaned_line
        elif current_section:
            sections[current_section] += line + "\n"

    return sections
import streamlit as st
from prompts import build_resume_analysis_prompt
from ai_client import get_ai_response
from ats_utils import calculate_match_score
from file_handler import extract_text_from_file
from response_parser import parse_ai_response
from ui_components import display_analysis_dashboard

st.set_page_config(
    page_title="AI Resume & Cover Letter Optimizer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume & Cover Letter Optimizer")

st.write(
    "Analyze your resume against a job description and generate practical improvement suggestions, "
    "a tailored cover letter, and interview preparation questions."
)

with st.sidebar:
    st.header("How to use")
    st.write("1. Paste your resume.")
    st.write("2. Paste the job description.")
    st.write("3. Click Analyze.")
    st.write("4. Review the AI-generated suggestions.")

    st.divider()

    st.header("Project Info")
    st.write("Model: Llama 3.2 3B via Ollama")
    st.write("Built with: Python + Streamlit")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Your Resume")

    uploaded_resume = st.file_uploader(
        "Upload your resume",
        type=["txt", "pdf", "docx"]
    )

    if uploaded_resume is not None:
        resume_text = extract_text_from_file(uploaded_resume)

        if resume_text.strip():
            st.success("Resume uploaded and text extracted successfully!")
        else:
            st.error("Could not extract text from this file. Try another file or paste the resume manually.")
            resume_text = ""
    else:
        resume_text = st.text_area(
            "Or paste your resume here",
            height=350,
            placeholder="Example: Education, skills, experience, projects..."
        )

with col2:
    st.subheader("Job Description")
    job_description = st.text_area(
        "Paste the job description here",
        height=350,
        placeholder="Example: Responsibilities, required skills, qualifications..."
    )

analyze_button = st.button("🔍 Analyze Resume", type="primary")

if analyze_button:
    if not resume_text.strip() or not job_description.strip():
        st.warning("Please paste both your resume and the job description.")
    else:
        ats_score, matched_keywords, missing_keywords = calculate_match_score(
            resume_text,
            job_description
        )

        prompt = build_resume_analysis_prompt(
            resume_text,
            job_description
        )

        with st.spinner("Analyzing your resume..."):
            ai_response = get_ai_response(prompt)
            sections = parse_ai_response(ai_response)

        display_analysis_dashboard(
            ats_score,
            matched_keywords,
            sections,
            ai_response
        )
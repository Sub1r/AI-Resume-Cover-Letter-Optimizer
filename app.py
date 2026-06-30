import streamlit as st
from prompts import build_resume_analysis_prompt
from ai_client import get_ai_response
from ats_utils import calculate_match_score

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
    resume_text = st.text_area(
        "Paste your resume here",
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
        ats_score, matched_keywords = calculate_match_score(
            resume_text,
            job_description
        )

        prompt = build_resume_analysis_prompt(
            resume_text,
            job_description
        )

        with st.spinner("Analyzing your resume..."):
            ai_response = get_ai_response(prompt)

        st.divider()

        st.subheader("🎯 ATS Keyword Match Score")
        st.progress(ats_score / 100)
        st.write(f"**Score:** {ats_score}/100")

        if matched_keywords:
            st.write("**Matched Keywords:**")
            st.write(", ".join(matched_keywords[:30]))
        else:
            st.write("No strong keyword matches found.")

        st.subheader("📊 AI Resume Analysis")
        st.markdown(ai_response)

        st.download_button(
            label="⬇️ Download Analysis",
            data=ai_response,
            file_name="resume_analysis.txt",
            mime="text/plain"
        )
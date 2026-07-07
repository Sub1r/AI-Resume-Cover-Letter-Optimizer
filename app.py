import streamlit as st
from prompts import build_resume_analysis_prompt
from ai_client import get_ai_response
from ats_utils import calculate_match_score
from file_handler import extract_text_from_file
from response_parser import parse_ai_response
from ui_components import display_analysis_dashboard
from styles import apply_custom_styles

st.set_page_config(
    page_title="AI Resume & Cover Letter Optimizer",
    page_icon="📄",
    layout="wide"
)
apply_custom_styles()

st.markdown(
    """
    <div class="hero-card">
        <h1><span class="gradient-text">AI Resume</span> & Cover Letter Optimizer</h1>
        <p class="hero-subtitle">
        Upload your resume, compare it with a job description, get an ATS keyword score,
        discover missing skills, and generate a tailored cover letter using local AI.
        </p>
        <div class="pill-row">
            <span class="pill">⚡ Local AI with Ollama</span>
            <span class="pill">🎯 ATS Keyword Score</span>
            <span class="pill">📄 PDF / DOCX / TXT Upload</span>
            <span class="pill">💌 Cover Letter Generator</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.header("How to use")
    st.write("1. Upload or paste your resume.")
    st.write("2. Paste the job description.")
    st.write("3. Click Analyze with Local AI.")
    st.write("4. Review your ATS score, missing skills, cover letter, and interview questions.")

    st.divider()

    st.header("Project Info")
    st.write("Model: Llama 3.2 3B via Ollama")
    st.write("Built with: Python + Streamlit")

st.markdown("### Start Your Resume Analysis")

input_col1, input_col2 = st.columns(2)

with input_col1:
    with st.container(border=True):
        st.markdown(
            """
            <div class="card-title">📄 Resume</div>
            <div class="card-subtitle">
            Upload your resume or paste the text manually.
            Supported formats: TXT, PDF, DOCX.
            </div>
            """,
            unsafe_allow_html=True
        )

        uploaded_resume = st.file_uploader(
            "Upload resume file",
            type=["txt", "pdf", "docx"]
        )

        if uploaded_resume is not None:
            resume_text = extract_text_from_file(uploaded_resume)

            if resume_text.strip():
                st.success("Resume uploaded and text extracted successfully!")
            else:
                st.error(
                    "Could not extract text from this file. "
                    "Try another file or paste the resume manually."
                )
                resume_text = ""
        else:
            resume_text = st.text_area(
                "Or paste your resume here",
                height=330,
                placeholder="Example: Education, skills, experience, projects..."
            )

with input_col2:
    with st.container(border=True):
        st.markdown(
            """
            <div class="card-title">💼 Job Description</div>
            <div class="card-subtitle">
            Paste the job description you want to compare your resume against.
            </div>
            """,
            unsafe_allow_html=True
        )

        job_description = st.text_area(
            "Paste the job description here",
            height=415,
            placeholder="Example: Responsibilities, required skills, qualifications..."
        )

button_col1, button_col2, button_col3 = st.columns([1, 1, 1])

with button_col2:
    analyze_button = st.button("✨ Analyze with Local AI", type="primary", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">ATS Score</div>
            <div class="feature-text">Measure keyword alignment with the job description.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🔍</div>
            <div class="feature-title">Missing Skills</div>
            <div class="feature-text">Find important terms your resume may be missing.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">💡</div>
            <div class="feature-title">AI Suggestions</div>
            <div class="feature-text">Get practical improvement recommendations.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">💌</div>
            <div class="feature-title">Cover Letter</div>
            <div class="feature-text">Generate a tailored application letter.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🎤</div>
            <div class="feature-title">Interview Prep</div>
            <div class="feature-text">Prepare with likely interview questions.</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

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
            try:
                ai_response = get_ai_response(prompt)
                sections = parse_ai_response(ai_response)

            except Exception:
                st.error(
                    "❌ Unable to connect to Ollama.\n\n"
                    "Please make sure:\n"
                    "- Ollama is running\n"
                    "- The Llama 3.2 model is installed\n"
                    "- The Ollama server is accessible"
                )
                st.stop()

        display_analysis_dashboard(
            ats_score,
            matched_keywords,
            missing_keywords,
            sections,
            ai_response
        )
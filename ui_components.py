import streamlit as st
from report_generator import generate_pdf_report


def display_tags(items, limit=15):
    """
    Display keywords as visual badges.
    """
    if not items:
        return "No keywords found."

    visible = items[:limit]
    tags = " ".join(f"`{item}`" for item in visible)

    if len(items) > limit:
        tags += f" ... (+{len(items) - limit} more)"

    return tags

def display_section(title, content, icon="📌", expanded=True):
    """
    Display a reusable analysis section.
    """
    with st.expander(f"{icon} {title}", expanded=expanded):
        st.markdown(content if content else "No information available.")


def display_analysis_dashboard(
    ats_score,
    matched_keywords,
    missing_keywords,
    sections,
    ai_response
):
    st.divider()

    st.subheader("📊 Resume Analysis Dashboard")

    st.success(
        "Resume analysis completed successfully! Review your personalized insights below."
    )

    # ==========================
    # Score + Keyword Overview
    # ==========================

    score_col, keyword_col = st.columns(2)

    with score_col:
        with st.container(border=True):

            st.metric(
                label="Keyword Match Score",
                value=f"{ats_score}/100"
            )

            progress_value = max(0.0, min(ats_score / 100, 1.0))
            st.progress(progress_value)

            with st.expander("ℹ️ What is ATS and what does this score mean?"):
                st.markdown("""
### What is an ATS?

An **Applicant Tracking System (ATS)** is software used by many employers to organize and search job applications. It often scans resumes for relevant skills, keywords, and job-related information before a recruiter reviews them.

### How is this score calculated?

This application compares the **skills, technologies, and keywords** in your resume with those found in the job description.

A higher score generally means your resume contains more of the terms that appear in the job posting.

### Important

This is an **estimated keyword match score**, not an official ATS score.

Different companies use different ATS software, and many also evaluate factors such as formatting, work experience, education, achievements, and overall resume quality.
""")

    with keyword_col:
        with st.container(border=True):

            st.write("### ✅ Matching Skills & Keywords")
            st.markdown(display_tags(matched_keywords))

            st.write("### ⚠️ Missing Skills & Keywords")
            st.markdown(display_tags(missing_keywords))

    st.divider()

    # ==========================
    # Detailed Analysis
    # ==========================

    display_section(
        "Overall Match Summary",
        sections.get("Match Score"),
        "📋",
        True
    )

    display_section(
        "Strong Matches",
        sections.get("Strong Matches"),
        "✅",
        True
    )

    display_section(
        "Missing Skills & Keywords",
        sections.get("Missing Skills or Keywords"),
        "⚠️",
        True
    )

    display_section(
        "Resume Improvement Suggestions",
        sections.get("Resume Improvement Suggestions"),
        "💡",
        True
    )

    display_section(
        "Tailored Cover Letter",
        sections.get("Tailored Cover Letter"),
        "💌",
        False
    )

    display_section(
        "Interview Preparation Questions",
        sections.get("Interview Preparation Questions"),
        "🎤",
        False
    )

    st.divider()

    # ==========================
    # PDF Report
    # ==========================

    pdf_report = generate_pdf_report(
        title="AI Resume & Cover Letter Optimizer",
        content=ai_response
    )

    with st.container(border=True):

        st.write("### 📄 Export Your Report")

        st.download_button(
            label="Download Professional PDF Report",
            data=pdf_report,
            file_name="resume_analysis_report.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    st.divider()

    st.caption(
        "Built with ❤️ using Python, Streamlit, and Ollama (llama3.2:3b)"
    )
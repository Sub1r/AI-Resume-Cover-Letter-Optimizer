import streamlit as st
from report_generator import generate_pdf_report


def display_tags(items):
    """
    Display keywords as visual badges.
    """
    if not items:
        return "No keywords found."

    return " ".join(f"`{item}`" for item in items[:15])


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
        "Resume analysis completed successfully! Review your improvement suggestions below."
    )

    # ==========================
    # ATS Score + Keyword Cards
    # ==========================

    score_col, keyword_col = st.columns(2)

    with score_col:
        with st.container(border=True):
            st.metric(
                label="ATS Keyword Match Score",
                value=f"{ats_score}/100"
            )
            st.progress(ats_score / 100)

    with keyword_col:
        with st.container(border=True):
            st.write("### ✅ Matched Keywords")
            st.markdown(display_tags(matched_keywords))

            st.write("### ⚠️ Missing Keywords")
            st.markdown(display_tags(missing_keywords))

    st.divider()

    # ==========================
    # Analysis Sections
    # ==========================

    display_section(
        "Match Score",
        sections.get("Match Score"),
        "📊",
        True
    )

    display_section(
        "Strong Matches",
        sections.get("Strong Matches"),
        "✅",
        True
    )

    display_section(
        "Missing Skills or Keywords",
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
            mime="application/pdf"
        )

    st.divider()

    st.caption(
        "Built with ❤️ using Python, Streamlit, and Ollama (llama3.2:3b)"
    )
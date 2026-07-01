import streamlit as st


def display_analysis_dashboard(
    ats_score,
    matched_keywords,
    missing_keywords,
    sections,
    ai_response
):
    st.divider()

    st.subheader("📊 Resume Analysis Dashboard")

    score_col, keyword_col = st.columns(2)

    with score_col:
        st.metric(
            label="ATS Keyword Match Score",
            value=f"{ats_score}/100"
        )
        st.progress(ats_score / 100)

    with keyword_col:
        st.write("**Top Matched Keywords**")

        if matched_keywords:
            st.write(", ".join(matched_keywords[:30]))
        else:
            st.write("No strong keyword matches found.")

        st.write("**Top Missing Keywords**")

        if missing_keywords:
            st.write(", ".join(missing_keywords[:30]))
        else:
            st.write("No major missing keywords found.")

    st.divider()

    with st.expander("📊 Match Score", expanded=True):
        st.markdown(sections["Match Score"])

    with st.expander("✅ Strong Matches", expanded=True):
        st.markdown(sections["Strong Matches"])

    with st.expander("⚠️ Missing Skills or Keywords", expanded=True):
        st.markdown(sections["Missing Skills or Keywords"])

    with st.expander("💡 Resume Improvement Suggestions", expanded=True):
        st.markdown(sections["Resume Improvement Suggestions"])

    with st.expander("💌 Tailored Cover Letter", expanded=False):
        st.markdown(sections["Tailored Cover Letter"])

    with st.expander("🎤 Interview Preparation Questions", expanded=False):
        st.markdown(sections["Interview Preparation Questions"])

    st.download_button(
        label="⬇️ Download Full Analysis",
        data=ai_response,
        file_name="resume_analysis.txt",
        mime="text/plain"
    )
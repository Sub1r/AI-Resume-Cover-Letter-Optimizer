import streamlit as st


def apply_custom_styles():
    st.markdown(
        """
        <style>
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(37, 99, 235, 0.22), transparent 35%),
                radial-gradient(circle at top right, rgba(168, 85, 247, 0.18), transparent 35%),
                linear-gradient(135deg, #020617 0%, #0f172a 55%, #111827 100%);
            color: #f8fafc;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1400px;
        }

        h1 {
            font-size: 3.4rem !important;
            line-height: 1.1 !important;
            font-weight: 900 !important;
            letter-spacing: -0.04em;
        }

        .gradient-text {
            background: linear-gradient(90deg, #60a5fa, #a78bfa, #f472b6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-card {
            padding: 2rem;
            border-radius: 24px;
            background: rgba(15, 23, 42, 0.72);
            border: 1px solid rgba(148, 163, 184, 0.18);
            box-shadow: 0 24px 80px rgba(0, 0, 0, 0.35);
            margin-bottom: 2rem;
        }

        .hero-subtitle {
            font-size: 1.1rem;
            color: #cbd5e1;
            max-width: 850px;
            margin-top: 0.8rem;
        }

        .pill-row {
            display: flex;
            gap: 0.7rem;
            flex-wrap: wrap;
            margin-top: 1.2rem;
        }

        .pill {
            padding: 0.45rem 0.8rem;
            border-radius: 999px;
            background: rgba(99, 102, 241, 0.16);
            border: 1px solid rgba(129, 140, 248, 0.35);
            color: #dbeafe;
            font-size: 0.9rem;
        }

        .input-card {
            padding: 1.4rem;
            border-radius: 22px;
            background: rgba(15, 23, 42, 0.74);
            border: 1px solid rgba(148, 163, 184, 0.20);
            box-shadow: 0 18px 60px rgba(0, 0, 0, 0.25);
            min-height: 560px;
        }

        .card-title {
            font-size: 1.45rem;
            font-weight: 800;
            margin-bottom: 0.25rem;
            color: #f8fafc;
        }

        .card-subtitle {
            color: #94a3b8;
            margin-bottom: 1rem;
        }

        .stTextArea textarea {
            background: rgba(30, 41, 59, 0.9) !important;
            color: #f8fafc !important;
            border: 1px solid rgba(148, 163, 184, 0.25) !important;
            border-radius: 16px !important;
        }

        .stFileUploader {
            background: rgba(30, 41, 59, 0.72);
            padding: 1rem;
            border-radius: 16px;
            border: 1px dashed rgba(148, 163, 184, 0.35);
        }

        .stButton button {
            background: linear-gradient(90deg, #2563eb, #7c3aed, #ec4899) !important;
            color: white !important;
            border: none !important;
            border-radius: 16px !important;
            padding: 0.85rem 1.8rem !important;
            font-weight: 800 !important;
            font-size: 1rem !important;
            box-shadow: 0 12px 35px rgba(124, 58, 237, 0.35);
        }

        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0 18px 45px rgba(236, 72, 153, 0.35);
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 1rem;
            margin-top: 1.5rem;
            margin-bottom: 2rem;
        }

        .feature-card {
            padding: 1rem;
            border-radius: 18px;
            background: rgba(15, 23, 42, 0.72);
            border: 1px solid rgba(148, 163, 184, 0.18);
        }

        .feature-icon {
            font-size: 1.6rem;
        }

        .feature-title {
            font-weight: 800;
            margin-top: 0.5rem;
        }

        .feature-text {
            color: #94a3b8;
            font-size: 0.9rem;
        }

        div[data-testid="stMetric"] {
            background: rgba(15, 23, 42, 0.75);
            padding: 1rem;
            border-radius: 18px;
            border: 1px solid rgba(148, 163, 184, 0.20);
        }

        .stExpander {
            background: rgba(15, 23, 42, 0.70) !important;
            border-radius: 16px !important;
            border: 1px solid rgba(148, 163, 184, 0.20) !important;
        }

        section[data-testid="stSidebar"] {
            background: rgba(2, 6, 23, 0.92);
            border-right: 1px solid rgba(148, 163, 184, 0.15);
        }
        </style>
        """,
        unsafe_allow_html=True
    )
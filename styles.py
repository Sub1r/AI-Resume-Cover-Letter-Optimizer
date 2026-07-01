import streamlit as st


def apply_custom_styles():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #0f172a 0%, #111827 45%, #020617 100%);
            color: #f8fafc;
        }

        h1 {
            font-size: 3rem !important;
            font-weight: 800 !important;
            background: linear-gradient(90deg, #60a5fa, #a78bfa, #f472b6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        h2, h3 {
            color: #f8fafc !important;
        }

        .hero-subtitle {
            font-size: 1.1rem;
            color: #cbd5e1;
            max-width: 900px;
            margin-bottom: 2rem;
        }

        .stTextArea textarea {
            background-color: #1e293b !important;
            color: #f8fafc !important;
            border: 1px solid #334155 !important;
            border-radius: 14px !important;
        }

        .stFileUploader {
            background-color: #1e293b;
            padding: 1rem;
            border-radius: 14px;
            border: 1px solid #334155;
        }

        .stButton button {
            background: linear-gradient(90deg, #2563eb, #7c3aed) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 0.75rem 1.5rem !important;
            font-weight: 700 !important;
        }

        .stButton button:hover {
            transform: scale(1.02);
            box-shadow: 0 0 20px rgba(124, 58, 237, 0.45);
        }

        div[data-testid="stMetric"] {
            background-color: #1e293b;
            padding: 1rem;
            border-radius: 16px;
            border: 1px solid #334155;
        }

        .stExpander {
            background-color: #111827 !important;
            border-radius: 14px !important;
            border: 1px solid #334155 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
# AI Resume & Cover Letter Optimizer

An AI-powered resume analysis and optimization tool that helps improve resumes by analyzing job alignment, identifying missing keywords, providing AI-generated recommendations, and generating structured feedback reports.

Built with a local Large Language Model (LLM) using Ollama, this project focuses on privacy-friendly AI processing, resume intelligence, and practical career assistance.

---

## Overview

The **AI Resume & Cover Letter Optimizer** is a Streamlit-based AI application that analyzes resumes against job requirements and provides actionable improvement suggestions.

The application combines:

* Resume document extraction
* ATS keyword matching
* AI-powered analysis using Ollama
* Structured response parsing
* Interactive dashboard visualization
* Automated PDF report generation

The project demonstrates how modern AI applications can combine document processing, prompt engineering, and local LLM inference into a complete end-to-end workflow.

---

# Features

## Resume Processing

* Supports multiple resume formats:

  * PDF
  * DOCX
  * TXT

* Extracts resume content automatically for analysis.

## AI-Powered Analysis

* Uses Ollama with Llama 3.2 3B for local AI inference.
* Generates resume improvement suggestions.
* Identifies strengths and weaknesses.
* Provides structured career-focused feedback.

## ATS Optimization

* Calculates resume keyword matching score.
* Identifies matched keywords.
* Detects missing keywords.
* Helps improve resume compatibility with Applicant Tracking Systems (ATS).

## Dashboard & Reporting

* Interactive Streamlit dashboard.
* Visual ATS score representation.
* Organized analysis sections.
* Generates downloadable PDF reports.

## Reliability Features

* Defensive error handling across modules.
* Handles invalid files gracefully.
* Handles AI connection failures.
* Protects against incomplete AI responses.

---

# Tech Stack

## Programming Language

* Python

## AI / Machine Learning

* Ollama
* Llama 3.2 3B Large Language Model

## Framework

* Streamlit

## Document Processing

* PDF parsing
* DOCX extraction
* Text file processing

## Report Generation

* ReportLab

## Other Libraries

* Python standard libraries
* Custom prompt engineering pipeline

---

# Screenshots

Screenshots will be added soon.

Planned screenshots:

* Application home page
* Resume analysis dashboard
* Generated PDF report
* Demo workflow GIF

Future assets:

```
assets/
├── home.png
├── dashboard.png
├── pdf-report.png
└── demo.gif
```

---

# Project Structure

```
AI-Resume-Cover-Letter-Optimizer/

├── app.py                  # Main Streamlit application
├── ai_client.py            # Ollama AI communication layer
├── ats_utils.py             # ATS scoring and keyword analysis
├── file_handler.py          # Resume file extraction utilities
├── prompts.py               # AI prompt construction
├── report_generator.py      # PDF report generation
├── response_parser.py       # AI response processing
├── styles.py                # UI styling
├── ui_components.py         # Dashboard components
├── requirements.txt
├── test_pdf.py
├── .gitignore
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/Sub1r/AI-Resume-Cover-Letter-Optimizer.git
```

Navigate into the project:

```bash
cd AI-Resume-Cover-Letter-Optimizer
```

---

## 2. Install Dependencies

Install required Python packages:

```bash
pip install -r requirements.txt
```

---

# Ollama Setup

This project uses Ollama to run the AI model locally.

## Install Ollama

Download and install Ollama:

https://ollama.com

## Download Required Model

Pull the Llama 3.2 3B model:

```bash
ollama pull llama3.2:3b
```

## Start Ollama Server

Run:

```bash
ollama serve
```

The application will communicate with Ollama through its local API.

---

# Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# How It Works

The application follows this workflow:

```
Resume Upload
       |
       v
Document Extraction
       |
       v
ATS Keyword Analysis
       |
       v
Prompt Engineering Layer
       |
       v
Local LLM (Ollama)
       |
       v
AI Response Parsing
       |
       v
Dashboard Visualization
       |
       v
PDF Report Generation
```

---

# Architecture Overview

The project follows a modular architecture:

### Application Layer

`app.py`

Handles:

* User interaction
* Application workflow
* Error handling

### AI Layer

`ai_client.py`

Handles:

* Communication with Ollama
* AI response generation

### Processing Layer

Includes:

* `file_handler.py`
* `ats_utils.py`
* `response_parser.py`

Responsible for:

* File extraction
* Resume analysis
* Response processing

### Presentation Layer

Includes:

* `ui_components.py`
* `styles.py`

Responsible for:

* Dashboard layout
* User interface components

### Reporting Layer

`report_generator.py`

Handles:

* PDF report creation
* Export functionality

---

# Implemented Features

✅ Resume parsing (PDF, DOCX, TXT)

✅ Local AI analysis using Ollama

✅ ATS keyword matching score

✅ Missing keyword detection

✅ AI recommendation generation

✅ Structured AI response parsing

✅ Streamlit dashboard interface

✅ PDF report generation

✅ Modular project architecture

✅ Error handling and validation

---

# Future Improvements

Planned improvements:

* Add job description upload support
* Improve ATS scoring using semantic similarity models
* Add resume version comparison
* Add cover letter generation workflow
* Add authentication system
* Add cloud deployment option
* Add automated testing pipeline
* Add application screenshots and demo GIF

---

# Author

**Subir Mandi**

GitHub:
https://github.com/Sub1r

---

# License

This project is licensed under the MIT License.

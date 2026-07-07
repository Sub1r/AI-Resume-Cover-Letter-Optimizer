from report_generator import generate_pdf_report

generate_pdf_report(
    output_path="test_report.pdf",
    title="Resume Analysis",
    content="""
This is a test PDF.

Generated successfully!

Congratulations!
Your PDF generator is working.
"""
)

print("PDF created successfully!")
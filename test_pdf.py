from report_generator import generate_pdf_report

pdf_bytes = generate_pdf_report(
    title="Resume Analysis",
    content="""
This is a test PDF.

Generated successfully!

Congratulations!
Your PDF generator is working.
"""
)

with open("test_report.pdf", "wb") as file:
    file.write(pdf_bytes)

print("PDF created successfully!")
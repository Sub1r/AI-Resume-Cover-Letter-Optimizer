from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(output_path, title, content):
    """
    Generate a simple PDF report.

    Parameters
    ----------
    output_path : str
        The path where the PDF will be saved.

    title : str
        The title displayed at the top of the PDF.

    content : str
        The main body text of the report.
    """

    document = SimpleDocTemplate(output_path)
    styles = getSampleStyleSheet()

    elements = [
        Paragraph(title, styles["Heading1"]),
        Paragraph(content.replace("\n", "<br/>"), styles["BodyText"])
    ]

    document.build(elements)
from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate


def generate_pdf_report(title, content):
    """
    Generate a PDF report and return it as bytes.

    Parameters
    ----------
    title : str
        The title displayed at the top of the PDF.

    content : str
        The main body text of the report.

    Returns
    -------
    bytes
        The generated PDF as a byte string.
    """

    # Defensive check to prevent errors if content is not a string
    content = content if isinstance(content, str) else ""

    buffer = BytesIO()
    document = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    elements = [
        Paragraph(title, styles["Heading1"]),
        Paragraph(content.replace("\n", "<br/>"), styles["BodyText"])
    ]

    document.build(elements)

    buffer.seek(0)
    return buffer.getvalue()
from reportlab.pdfgen import canvas

def generate_pdf():

    c = canvas.Canvas(
        "outputs/reports/report.pdf"
    )

    c.drawString(
        100,
        800,
        "Recommendation Report"
    )

    c.drawString(
        100,
        770,
        "Project Executed Successfully"
    )

    c.save()
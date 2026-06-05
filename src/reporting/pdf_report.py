from pathlib import Path
import pandas as pd

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
    recommendations,
    metrics
):

    Path(
        "outputs/reports"
    ).mkdir(
        parents=True,
        exist_ok=True
    )

    pdf_path = (
        "outputs/reports/project_report.pdf"
    )

    products = pd.read_csv(
        "data/raw/products.csv"
    )

    users = pd.read_csv(
        "data/raw/users.csv"
    )

    interactions = pd.read_csv(
        "data/raw/interactions.csv"
    )

    doc = SimpleDocTemplate(
        pdf_path
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI E-Commerce Recommendation Platform",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "Project Summary",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            "Advanced recommendation system using synthetic e-commerce data, preprocessing pipelines, collaborative filtering, content-based recommendations, and evaluation metrics.",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "Dataset Statistics",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            f"Products: {len(products)}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Users: {len(users)}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Interactions: {len(interactions)}",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "Recommendation Results",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            str(recommendations),
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "Evaluation Metrics",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            f"Precision@10: {metrics['precision']}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Recall@10: {metrics['recall']}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"NDCG@10: {metrics['ndcg']}",
            styles["BodyText"]
        )
    )

    content.append(PageBreak())

    content.append(
        Paragraph(
            "Generated Charts",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            "See outputs/screenshots folder for generated visual analytics.",
            styles["BodyText"]
        )
    )

    doc.build(content)

    print(
        "[PDF] project_report.pdf generated"
    )
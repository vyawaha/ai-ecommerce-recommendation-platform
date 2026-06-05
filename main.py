from src.generators.dataset_generator import (
    generate_products
)

from src.generators.synthetic_user_generator import (
    generate_users,
    generate_interactions
)

from src.preprocessing.cleaner import (
    run_cleaning
)

from src.preprocessing.splitter import (
    create_splits
)

from src.preprocessing.feature_store import (
    build_feature_store
)

from src.recommenders.hybrid_engine import (
    hybrid_recommendation
)

from src.evaluation.evaluator import (
    evaluate
)

from src.visualization.charts import (
    generate_all_charts
)

from src.visualization.heatmaps import (
    generate_interaction_heatmap
)

from src.visualization.screenshots import (
    verify_outputs
)

from src.reporting.pdf_report import (
    generate_pdf_report
)


def main():

    print("=" * 60)
    print("AI E-Commerce Recommendation Platform")
    print("=" * 60)

    print("\nGenerating Products...")
    generate_products()

    print("\nGenerating Users...")
    generate_users()

    print("\nGenerating Interactions...")
    generate_interactions()

    print("\nCleaning Data...")
    run_cleaning()

    print("\nCreating Train/Test Splits...")
    create_splits()

    print("\nBuilding Feature Store...")
    build_feature_store()

    print("\nGenerating Recommendations...\n")

    recommendations = hybrid_recommendation(
        user_id=1,
        seed_product=1,
        top_n=10
    )

    print("Recommended Products:")
    print(recommendations)

    metrics = evaluate(
        user_id=1,
        recommendations=recommendations,
        k=10
    )

    print("\nEvaluation Metrics")
    print(f"Precision@10 : {metrics['precision']}")
    print(f"Recall@10    : {metrics['recall']}")
    print(f"NDCG@10      : {metrics['ndcg']}")

    print("\nGenerating Charts...")

    generate_all_charts()

    generate_interaction_heatmap()

    verify_outputs()

    print("\nGenerating PDF Report...")

    generate_pdf_report(
        recommendations,
        metrics
    )

    print("\nPipeline Complete")


if __name__ == "__main__":
    main()
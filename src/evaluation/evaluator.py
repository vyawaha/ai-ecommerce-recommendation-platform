import pandas as pd

from src.evaluation.precision import (
    precision_at_k
)

from src.evaluation.recall import (
    recall_at_k
)

from src.evaluation.ndcg import (
    ndcg_at_k
)

def evaluate(
    user_id,
    recommendations,
    k=10
):

    interactions = pd.read_csv(
        "data/cleaned/interactions_clean.csv"
    )

    relevant_items = (
        interactions[
            interactions["user_id"] == user_id
        ]["product_id"]
        .unique()
        .tolist()
    )

    precision = precision_at_k(
        recommendations,
        relevant_items,
        k
    )

    recall = recall_at_k(
        recommendations,
        relevant_items,
        k
    )

    ndcg = ndcg_at_k(
        recommendations,
        relevant_items,
        k
    )

    return {
        "precision": round(
            precision,
            4
        ),
        "recall": round(
            recall,
            4
        ),
        "ndcg": round(
            ndcg,
            4
        )
    }

import pandas as pd

def recommend_for_user(user_id, top_n=10):

    interactions = pd.read_csv(
        "data/cleaned/interactions_clean.csv"
    )

    user_products = set(
        interactions[
            interactions["user_id"] == user_id
        ]["product_id"]
    )

    other_users = interactions[
        interactions["product_id"].isin(
            user_products
        )
    ]["user_id"].unique()

    recommendations = interactions[
        interactions["user_id"].isin(
            other_users
        )
    ]

    recommendations = recommendations[
        ~recommendations["product_id"].isin(
            user_products
        )
    ]

    top_products = (
        recommendations["product_id"]
        .value_counts()
        .head(top_n)
        .index
        .tolist()
    )

    return top_products

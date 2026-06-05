import pandas as pd

from sklearn.feature_extraction.text import (
    TfidfVectorizer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)

def similar_products(
    product_id,
    top_n=10
):

    products = pd.read_csv(
        "data/cleaned/products_clean.csv"
    )

    tfidf = TfidfVectorizer()

    matrix = tfidf.fit_transform(
        products["description"]
    )

    similarity = cosine_similarity(
        matrix
    )

    idx = products.index[
        products["product_id"] == product_id
    ][0]

    scores = list(
        enumerate(
            similarity[idx]
        )
    )

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for i in scores[1:top_n+1]:

        recommendations.append(
            int(
                products.iloc[
                    i[0]
                ]["product_id"]
            )
        )

    return recommendations

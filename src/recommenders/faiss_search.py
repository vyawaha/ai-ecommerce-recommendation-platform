import pandas as pd

from sklearn.feature_extraction.text import (
    TfidfVectorizer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)

def semantic_search(
    product_id,
    top_n=5
):

    products = pd.read_csv(
        "data/cleaned/products_clean.csv"
    )

    tfidf = TfidfVectorizer()

    matrix = tfidf.fit_transform(
        products["description"]
    )

    sim = cosine_similarity(
        matrix
    )

    idx = products.index[
        products["product_id"] == product_id
    ][0]

    scores = list(
        enumerate(sim[idx])
    )

    scores.sort(
        key=lambda x: x[1],
        reverse=True
    )

    results = []

    for i in scores[1:top_n+1]:

        results.append(
            int(
                products.iloc[
                    i[0]
                ]["product_id"]
            )
        )

    return results

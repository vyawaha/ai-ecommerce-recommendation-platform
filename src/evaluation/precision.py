def precision_at_k(recommended, relevant, k=10):

    recommended = recommended[:k]

    hits = len(
        set(recommended).intersection(
            set(relevant)
        )
    )

    return hits / k if k > 0 else 0
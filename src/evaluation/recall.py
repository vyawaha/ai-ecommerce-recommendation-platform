def recall_at_k(recommended, relevant, k=10):

    recommended = recommended[:k]

    hits = len(
        set(recommended).intersection(
            set(relevant)
        )
    )

    return (
        hits / len(relevant)
        if len(relevant) > 0
        else 0
    )

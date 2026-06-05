import math

def dcg(scores):

    total = 0

    for i, score in enumerate(scores):

        total += (
            score /
            math.log2(i + 2)
        )

    return total

def ndcg_at_k(
    recommended,
    relevant,
    k=10
):

    recommended = recommended[:k]

    gains = []

    for item in recommended:

        gains.append(
            1 if item in relevant else 0
        )

    ideal = sorted(
        gains,
        reverse=True
    )

    actual_dcg = dcg(gains)

    ideal_dcg = dcg(ideal)

    if ideal_dcg == 0:
        return 0

    return actual_dcg / ideal_dcg

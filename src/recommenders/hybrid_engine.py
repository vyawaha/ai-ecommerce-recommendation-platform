from src.recommenders.collaborative_filtering import (
    recommend_for_user
)

from src.recommenders.content_based import (
    similar_products
)

def hybrid_recommendation(
    user_id,
    seed_product,
    top_n=10
):

    collaborative = recommend_for_user(
        user_id,
        top_n
    )

    content = similar_products(
        seed_product,
        top_n
    )

    combined = []

    for item in collaborative:
        combined.append(item)

    for item in content:

        if item not in combined:
            combined.append(item)

    return combined[:top_n]

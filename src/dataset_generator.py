import pandas as pd
import random

def generate():

    categories = [
        "Electronics",
        "Fashion",
        "Books",
        "Sports",
        "Home"
    ]

    products = []

    for i in range(1,101):

        products.append([
            i,
            f"Product_{i}",
            random.choice(categories),
            random.randint(100,5000)
        ])

    pd.DataFrame(
        products,
        columns=[
            "id",
            "name",
            "category",
            "price"
        ]
    ).to_csv(
        "data/products.csv",
        index=False
    )

generate()
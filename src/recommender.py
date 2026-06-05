import pandas as pd

def recommend():

    products = pd.read_csv(
        "data/products.csv"
    )

    return products.sort_values(
        by="price",
        ascending=False
    ).head(10)
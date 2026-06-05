import pandas as pd
import matplotlib.pyplot as plt

def top_products():

    products = pd.read_csv(
        "data/products.csv"
    )

    top = products.nlargest(
        10,
        "price"
    )

    plt.figure(
        figsize=(10,5)
    )

    plt.bar(
        top["name"],
        top["price"]
    )

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        "images/top_products.png"
    )

    plt.close()
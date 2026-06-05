import pandas as pd
import matplotlib.pyplot as plt

def generate_charts():

    products = pd.read_csv(
        "data/products.csv"
    )

    products["category"].value_counts().plot(
        kind="bar"
    )

    plt.savefig(
        "images/category_distribution.png"
    )

    plt.close()
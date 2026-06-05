import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

OUTPUT_DIR = "outputs/screenshots"

def generate_popularity_chart():

    Path(OUTPUT_DIR).mkdir(
        parents=True,
        exist_ok=True
    )

    interactions = pd.read_csv(
        "data/cleaned/interactions_clean.csv"
    )

    popularity = (
        interactions["product_id"]
        .value_counts()
        .head(10)
    )

    plt.figure(figsize=(10, 5))

    popularity.plot(kind="bar")

    plt.title(
        "Top 10 Popular Products"
    )

    plt.xlabel("Product ID")
    plt.ylabel("Interactions")

    plt.tight_layout()

    plt.savefig(
        f"{OUTPUT_DIR}/popularity_chart.png"
    )

    plt.close()

    print(
        "[CHART] popularity_chart.png generated"
    )


def generate_user_activity_chart():

    interactions = pd.read_csv(
        "data/cleaned/interactions_clean.csv"
    )

    activity = (
        interactions["user_id"]
        .value_counts()
        .head(10)
    )

    plt.figure(figsize=(10, 5))

    activity.plot(kind="bar")

    plt.title(
        "Top Active Users"
    )

    plt.xlabel("User ID")
    plt.ylabel("Interactions")

    plt.tight_layout()

    plt.savefig(
        f"{OUTPUT_DIR}/user_activity.png"
    )

    plt.close()

    print(
        "[CHART] user_activity.png generated"
    )


def generate_all_charts():

    generate_popularity_chart()
    generate_user_activity_chart()


if __name__ == "__main__":
    generate_all_charts()

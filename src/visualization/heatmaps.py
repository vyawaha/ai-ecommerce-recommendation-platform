import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

OUTPUT_DIR = "outputs/screenshots"

def generate_interaction_heatmap():

    interactions = pd.read_csv(
        "data/cleaned/interactions_clean.csv"
    )

    sample = interactions.head(300)

    matrix = pd.crosstab(
        sample["user_id"],
        sample["product_id"]
    )

    plt.figure(figsize=(10, 8))

    sns.heatmap(
        matrix,
        cmap="viridis"
    )

    plt.title(
        "User Product Interaction Heatmap"
    )

    plt.tight_layout()

    plt.savefig(
        f"{OUTPUT_DIR}/interaction_heatmap.png"
    )

    plt.close()

    print(
        "[HEATMAP] interaction_heatmap.png generated"
    )


if __name__ == "__main__":
    generate_interaction_heatmap()

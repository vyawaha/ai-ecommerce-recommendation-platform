import pandas as pd
from pathlib import Path

CLEAN_DIR = "data/cleaned"
PROCESSED_DIR = "data/processed"

def build_user_features():

    interactions = pd.read_csv(
        f"{CLEAN_DIR}/interactions_clean.csv"
    )

    user_features = (
        interactions
        .groupby("user_id")
        .agg(
            total_events=("event","count")
        )
        .reset_index()
    )

    user_features.to_parquet(
        f"{PROCESSED_DIR}/user_features.parquet",
        index=False
    )

    print(
        f"[FEATURES] Users: {len(user_features)}"
    )

def build_item_features():

    interactions = pd.read_csv(
        f"{CLEAN_DIR}/interactions_clean.csv"
    )

    item_features = (
        interactions
        .groupby("product_id")
        .agg(
            popularity=("event","count")
        )
        .reset_index()
    )

    item_features.to_parquet(
        f"{PROCESSED_DIR}/item_features.parquet",
        index=False
    )

    print(
        f"[FEATURES] Products: {len(item_features)}"
    )

def build_feature_store():

    Path(PROCESSED_DIR).mkdir(
        parents=True,
        exist_ok=True
    )

    build_user_features()
    build_item_features()

if __name__ == "__main__":
    build_feature_store()

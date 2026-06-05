import pandas as pd
from pathlib import Path

RAW_DIR = "data/raw"
CLEAN_DIR = "data/cleaned"

def clean_products():

    df = pd.read_csv(f"{RAW_DIR}/products.csv")

    df = df.drop_duplicates()

    df = df.fillna({
        "brand": "Unknown",
        "description": "No Description"
    })

    Path(CLEAN_DIR).mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        f"{CLEAN_DIR}/products_clean.csv",
        index=False
    )

    print(
        f"[CLEANED] Products: {len(df)} rows"
    )

def clean_users():

    df = pd.read_csv(f"{RAW_DIR}/users.csv")

    df = df.drop_duplicates()

    df.to_csv(
        f"{CLEAN_DIR}/users_clean.csv",
        index=False
    )

    print(
        f"[CLEANED] Users: {len(df)} rows"
    )

def clean_interactions():

    df = pd.read_csv(
        f"{RAW_DIR}/interactions.csv"
    )

    df = df.drop_duplicates()

    df.to_csv(
        f"{CLEAN_DIR}/interactions_clean.csv",
        index=False
    )

    print(
        f"[CLEANED] Interactions: {len(df)} rows"
    )

def run_cleaning():

    clean_products()
    clean_users()
    clean_interactions()

if __name__ == "__main__":
    run_cleaning()

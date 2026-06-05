import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path

CLEAN_DIR = "data/cleaned"
PROCESSED_DIR = "data/processed"

def create_splits():

    Path(PROCESSED_DIR).mkdir(
        parents=True,
        exist_ok=True
    )

    df = pd.read_csv(
        f"{CLEAN_DIR}/interactions_clean.csv"
    )

    train_df, temp_df = train_test_split(
        df,
        test_size=0.30,
        random_state=42
    )

    val_df, test_df = train_test_split(
        temp_df,
        test_size=0.50,
        random_state=42
    )

    train_df.to_parquet(
        f"{PROCESSED_DIR}/train.parquet",
        index=False
    )

    val_df.to_parquet(
        f"{PROCESSED_DIR}/validation.parquet",
        index=False
    )

    test_df.to_parquet(
        f"{PROCESSED_DIR}/test.parquet",
        index=False
    )

    print(
        f"[TRAIN] {len(train_df)} rows"
    )

    print(
        f"[VALIDATION] {len(val_df)} rows"
    )

    print(
        f"[TEST] {len(test_df)} rows"
    )

if __name__ == "__main__":
    create_splits()

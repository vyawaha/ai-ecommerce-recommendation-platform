import pandas as pd
import random
from datetime import datetime
from datetime import timedelta
from pathlib import Path

EVENTS = [
    "view",
    "cart",
    "purchase"
]


def generate_users(
    num_users=500,
    output_file="data/raw/users.csv"
):

    Path("data/raw").mkdir(
        parents=True,
        exist_ok=True
    )

    users = []

    for uid in range(1, num_users + 1):

        users.append([
            uid,
            random.randint(18, 60),
            random.choice(
                ["Male", "Female"]
            ),
            random.choice(
                [
                    "Mumbai",
                    "Pune",
                    "Delhi",
                    "Bangalore",
                    "Hyderabad"
                ]
            )
        ])

    columns = [
        "user_id",
        "age",
        "gender",
        "city"
    ]

    df = pd.DataFrame(
        users,
        columns=columns
    )

    df.to_csv(
        output_file,
        index=False
    )

    print(
        f"[SUCCESS] Generated {num_users} users"
    )

    return df


def generate_interactions(
    num_users=500,
    num_products=1000,
    interactions_per_user=20,
    output_file="data/raw/interactions.csv"
):

    interactions = []

    start_date = datetime.now() - timedelta(
        days=180
    )

    for uid in range(
        1,
        num_users + 1
    ):

        for _ in range(
            interactions_per_user
        ):

            product_id = random.randint(
                1,
                num_products
            )

            event = random.choices(
                EVENTS,
                weights=[60, 25, 15]
            )[0]

            timestamp = (
                start_date +
                timedelta(
                    days=random.randint(
                        0,
                        180
                    )
                )
            )

            interactions.append([
                uid,
                product_id,
                event,
                timestamp
            ])

    columns = [
        "user_id",
        "product_id",
        "event",
        "timestamp"
    ]

    df = pd.DataFrame(
        interactions,
        columns=columns
    )

    df.to_csv(
        output_file,
        index=False
    )

    print(
        "[SUCCESS] Generated interactions"
    )

    return df


if __name__ == "__main__":

    generate_users()

    generate_interactions()
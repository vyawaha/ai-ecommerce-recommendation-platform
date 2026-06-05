import pandas as pd
import random
from pathlib import Path

PRODUCT_CATEGORIES = {
    "Electronics": [
        "Laptop",
        "Smartphone",
        "Monitor",
        "Keyboard",
        "Mouse",
        "Headphones",
        "Tablet",
        "Smartwatch"
    ],
    "Fashion": [
        "Shirt",
        "Jeans",
        "Jacket",
        "Sneakers",
        "T-Shirt",
        "Watch",
        "Hoodie"
    ],
    "Books": [
        "Python Guide",
        "Data Science",
        "Machine Learning",
        "Algorithms",
        "Operating Systems",
        "DBMS"
    ],
    "Sports": [
        "Football",
        "Cricket Bat",
        "Basketball",
        "Tennis Racket",
        "Gym Gloves",
        "Yoga Mat"
    ],
    "Home": [
        "Chair",
        "Table",
        "Lamp",
        "Sofa",
        "Mixer",
        "Vacuum Cleaner"
    ]
}

BRANDS = [
    "TechPro",
    "Nova",
    "Elite",
    "Prime",
    "Ultra",
    "Max",
    "Vision",
    "SmartLife"
]


def generate_products(
    num_products=1000,
    output_file="data/raw/products.csv"
):

    Path("data/raw").mkdir(
        parents=True,
        exist_ok=True
    )

    products = []

    for pid in range(1, num_products + 1):

        category = random.choice(
            list(PRODUCT_CATEGORIES.keys())
        )

        base_name = random.choice(
            PRODUCT_CATEGORIES[category]
        )

        brand = random.choice(
            BRANDS
        )

        price = round(
            random.uniform(100, 50000),
            2
        )

        rating = round(
            random.uniform(3.0, 5.0),
            1
        )

        stock = random.randint(
            10,
            500
        )

        title = f"{brand} {base_name}"

        description = (
            f"{title} in category "
            f"{category} with rating "
            f"{rating}"
        )

        products.append([
            pid,
            title,
            category,
            brand,
            price,
            rating,
            stock,
            description
        ])

    columns = [
        "product_id",
        "title",
        "category",
        "brand",
        "price",
        "rating",
        "stock",
        "description"
    ]

    df = pd.DataFrame(
        products,
        columns=columns
    )

    df.to_csv(
        output_file,
        index=False
    )

    print(
        f"[SUCCESS] Generated {num_products} products"
    )

    return df


if __name__ == "__main__":
    generate_products()
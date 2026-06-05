from pathlib import Path

def verify_outputs():

    screenshot_dir = Path(
        "outputs/screenshots"
    )

    print(
        "\nGenerated Screenshot Files:\n"
    )

    for file in screenshot_dir.glob("*"):

        print(file.name)


if __name__ == "__main__":
    verify_outputs()

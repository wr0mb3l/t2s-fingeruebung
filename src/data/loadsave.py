#!/usr/bin/env python
"""Loads and saves XML files containing IsoSpace data, tokens and tags.
"""

from pathlib import Path
import os


def load(path: Path):
    """Loads Content of given File to string.

    Args:
        path (Path): Path to file.

    Raises:
        FileNotFoundError: File was not found or is empty.

    Returns:
        str: Content.
    """

    content = ""
    with open(Path(Path(__file__).parent.resolve(), path), "r") as f:
        if (content := f.read()) != "":
            return content
        raise FileNotFoundError()


def save(path: Path, data: str):
    """Saves given data in file.

    Args:
        path (Path): Path to file, starting in src/data.
        data (str): Data to save.
    """
    full_path = Path(Path(__file__).parent.resolve(), path)
    # Create dirs if necessary
    os.makedirs(str(full_path.parent))

    with open(full_path, "w") as f:
        f.write(data)


def main():
    """Short usage example.
    """
    print("loadsave.py\n" + __doc__ + "\n")

    content = ""
    try:
        content = load("training-data/Traning/RFC/Bicycles.xml")
        print(content)
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    main()

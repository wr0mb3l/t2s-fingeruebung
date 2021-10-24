#!/usr/bin/env python
"""Loads and saves XML files containing IsoSpace data, tokens and tags.
"""

from pathlib import Path


def fromXML(path: Path,):
    """Loads a given XML files contents and returns string.

    Args:
        path (str): Path to XML file starting in src/data.
    """

    content = ""
    with open(Path(Path(__file__).parent.resolve(), path), "r") as f:
        if (content := f.read()) != "":
            return content
        raise FileNotFoundError()


def main():
    """Short usage example.
    """
    print("loadsave.py\n"+__doc__ + "\n")

    content = ""
    try:
        content = fromXML("training-data/Traning/RFC/Bicycles.xml")
        print(content)
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()


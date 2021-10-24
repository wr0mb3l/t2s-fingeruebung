#!/usr/bin/env python
"""Text2Scene Pratkikum WiSe 21-22 Fingerübung.

Reads IsoSpace XML-Data from Files, tokenizes and tags read data using Spacy.
Generated Data can then be saved in XML again.
"""

import data.loadsave
import data.parser


def main():
    """Quick usage example.
    """
    print("main.py\n"+__doc__)
    
    # Load XML content from file
    content = ""
    try:
        content = data.loadsave.load("training-data/Traning/RFC/Bicycles.xml")
        # data.loadsave.save("json/Bicycles.json", data.parser.XMLtoJSON(content))
    except FileNotFoundError as e:
        print(e)

    # Add Language Analysis    


if __name__ == "__main__":
    main()


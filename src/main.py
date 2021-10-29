#!/usr/bin/env python
"""Text2Scene Pratkikum WiSe 21-22 Fingerübung.

Reads IsoSpace XML-Data from Files, tokenizes and tags read data using Spacy.
Generated Data can then be saved in XML again.
"""

import data.loadsave
import data.parser
import nlp.analyzer
import stats.stats


def main():
    """Quick usage example.
    """
    print("main.py\n"+__doc__)

    path = "RFC/Bicycles"
    
    # Load XML content from file and convert to dictionary
    content = ""
    try:
        content = data.parser.xml_to_dict(
            data.loadsave.load("training-data/Traning/" + path + ".xml")
        )["spaceevaltaskv1.2"]
    except FileNotFoundError as e:
        print(e)

    # Add Language Analysis
    try:
        content["tags"]["token"] = nlp.analyzer.analyze(content["text"])
    except Exception as e:
        print(e)

    # Save as JSON
    data.loadsave.save("json/" + path + ".json", data.parser.dict_to_json(content))

    # Load from JSON
    content = data.parser.json_to_dict(data.loadsave.load("json/" + path + ".json"))

    # Print some stats
    print(stats.stats.qslink_types(content["tags"]["qslink"]))


if __name__ == "__main__":
    main()


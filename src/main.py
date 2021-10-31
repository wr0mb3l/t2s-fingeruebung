#!/usr/bin/env python
"""Text2Scene Pratkikum WiSe 21-22 Fingerübung.

Reads IsoSpace XML-Data from Files, tokenizes and tags read data using Spacy.
Collected Data can then be saved in JSON.
Includes some crude analysis tools and a visualizer to show a network graph of the XML contents.
"""

import data.loadsave
import data.parser
import nlp.analyzer
import eval.stats
import eval.visualizer
import matplotlib.pyplot as plt
from pathlib import Path


def printable_dict(dic: dict):
    result = ""
    for k in dic.keys():
        result += k + ":  " + str(dic[k]) + "\n"
    return result


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
    print("PoS counts:\n" + printable_dict(eval.stats.pos_count(content["tags"])))
    print("\n\nIsoSpace tag counts:\n" + printable_dict(eval.stats.iso_space_count(content["tags"])))
    print("\n\nQsLink Type counts:\n" + printable_dict(eval.stats.qs_link_types(content["tags"])))
    print("\n\nQsLink preposition counts:")
    link_prep_count = eval.stats.link_prepositions_count(content["tags"])
    print("Qslink Triggers:\n" + printable_dict(link_prep_count["qslink"]))
    print("OLink Triggers:\n" + printable_dict(link_prep_count["olink"]))
    print("\n\n5 most common motion verbs:\n" + printable_dict(eval.stats.most_common_motion_verbs(content["tags"])))

    eval.visualizer.show_network_graph(content["tags"])

    plt.tight_layout()
    plt.axis("off")
    plt.savefig(Path(Path(__file__).parent.resolve(), "data/json/" + path + ".png"), dpi=400)


if __name__ == "__main__":
    main()


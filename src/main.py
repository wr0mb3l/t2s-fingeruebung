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
import argparse

parser = argparse.ArgumentParser(description='Analyze some preprocessed IsoSpace XML files.')
parser.add_argument('files', metavar='file', type=str, nargs='*',
                    help='a file to process')
parser.add_argument('--graph', action='store', type=str, help='a file to visualize')
args = parser.parse_args()


def printable_dict(dic: dict):
    result = ""
    for k in dic.keys():
        result += k + ":  " + str(dic[k]) + "\n"
    return result


def main():
    """Answers questions given to students.
    """
    print("main.py\n" + __doc__)

    contents = []

    for path in args.files + ([] if args.graph is None else [args.graph]):
        content = {}
        try:
            # Load from JSON
            content = data.parser.json_to_dict(data.loadsave.load("json/" + path[:-3] + "json"))
        except FileNotFoundError as e:
            pass

        if path[-4:] != ".xml":
            print("Not an xml file")
            continue

        # Load XML content from file and convert to dictionary
        try:
            content = data.parser.xml_to_dict(
                data.loadsave.load("training-data/Traning/" + path)
            )["spaceevaltaskv1.2"]
        except FileNotFoundError as e:
            print(e)

        # Add Language Analysis
        try:
            content["tags"]["token"] = nlp.analyzer.analyze(content["text"])
        except Exception as e:
            print(e)

        contents.append(content)

        # Save as JSON
        data.loadsave.save("json/" + path[:-3] + "json", data.parser.dict_to_json(content))

        if args.graph == path:
            eval.visualizer.show_network_graph(content["tags"])

            plt.axis("off")
            plt.savefig(Path(Path(__file__).parent.resolve(), "data/json/" + path[:-3] + "png"), dpi=400)
            plt.clf()


    # Print some stats
    print("PoS counts:\n" + printable_dict(eval.stats.pos_count(contents)))
    print("\n\nIsoSpace tag counts:\n" + printable_dict(eval.stats.iso_space_count(contents)))
    print("\n\nQsLink Type counts:\n" + printable_dict(eval.stats.qs_link_types(contents)))
    print("\n\nQsLink preposition counts:")
    link_prep_count = eval.stats.link_prepositions_count(contents)
    print("Qslink Triggers:\n" + printable_dict(link_prep_count["qslink"]))
    print("OLink Triggers:\n" + printable_dict(link_prep_count["olink"]))
    print("\n\n5 most common motion verbs:\n" + printable_dict(eval.stats.most_common_motion_verbs(contents)))

    # Create Picture with bar chart for sentence lengths
    sentence_lengths = eval.stats.sentence_lengths(contents)
    plt.bar(sentence_lengths.keys(), sentence_lengths.values())
    plt.savefig(Path(Path(__file__).parent.resolve(), "sentence-lengths.png"), dpi=400)
    plt.clf()


if __name__ == "__main__":
    main()

#!/usr/bin/env python
"""Analyzer Tool for preprocessed JSON files containing Token and IsoSpace data.
"""


def pos_count(tokens: dict):
    stats = {}
    for token in tokens:
        if token["pos"] in stats.keys():
            stats[token["pos"]] += 1
            continue
        stats[token["pos"]] = 1
    return stats


def isospace_count(tags: dict):
    stats = {}
    for name in tags.keys():
        if not name == "token":
            stats[name] = len(tags[name]) if type(tags[name]) == list else 1
    return stats


def qslink_types(links: dict):
    stats = {}
    for link in links:
        if link["reltype"] in stats.keys():
            stats[link["reltype"]] += 1
            continue
        stats[link["reltype"]] = 1
    return stats


def main():
    """Quick usage example.
    """
    print("stats.py\n"+__doc__)


if __name__ == "__main__":
    main()

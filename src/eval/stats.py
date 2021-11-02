#!/usr/bin/env python
"""Analyzer Tool for preprocessed Dictionaries containing Token and IsoSpace data.
"""


def pos_count(contents: list):
    """Counts Part of Speech tags in tokens.

    Args:
        contents (list): List of contents containing Tags.
    Returns:
        dict: PoS as keys and counts as values.
    """

    stats = {}
    for content in contents:
        for token in content["tags"]["token"]:
            if token["pos"] in stats.keys():
                stats[token["pos"]] += 1
                continue
            stats[token["pos"]] = 1
    return stats


def iso_space_count(contents: list):
    """Counts Iso Space tags in tokens.

    Args:
        contents (list): List of contents containing Tags.
    Returns:
        dict: Iso Space tags as keys and counts as values.
    """

    stats = {}
    for content in contents:
        tags = content["tags"]
        for name in tags.keys():
            if not name == "token":
                if name in stats.keys():
                    stats[name] += len(tags[name]) if type(tags[name]) == list else 1
                    continue
                stats[name] = len(tags[name]) if type(tags[name]) == list else 1
    return stats


def qs_link_types(contents: list):
    """Counts QS-Link types.

    Args:
        contents (list): List of contents containing Tags.
    Returns:
        dict: QS-Link types as keys and counts as values.
    """

    stats = {}
    for content in contents:
        tags = content["tags"]
        for link in tags["qslink"]:
            if link["reltype"] in stats.keys():
                stats[link["reltype"]] += 1
                continue
            stats[link["reltype"]] = 1
    return stats


def sentence_lengths(contents: list):
    """Counts sentence lengths from list of tokens.

    Args:
        contents (list): List of contents containing Tags.
    Returns:
        dict: Dictionary with Sentence length as keys and counts as values.
    """

    stats = {}
    for content in contents:
        length = 1
        # Used to ignore first sentence (length = 0)
        first = True
        tags = content["tags"]
        for token in tags["token"]:
            length += 1
            if token["sentence"] and not first:
                # Add to dict
                if length in stats.keys():
                    stats[length] += 1
                    length = 1
                    continue
                stats[length] = 1
                # Reset length
                length = 1
            first = False
        # Add last sentence length
        if length in stats.keys():
            stats[length] += 1
        stats[length] = 1

    return stats


def link_prepositions_count(contents: list):
    """Counts Prepositions that triggered QS/O-Links.

    Args:
        contents (list): List of contents containing Tags.
    Returns:
        dict: Contains dictionaries with 2 keys, "qslink" and "olink, both containing more info.
    """
    stats = {"qslink": {}, "olink": {}}
    for content in contents:
        tags = content["tags"]
        for name in stats.keys():
            for e in tags[name]:
                prepositions = [x["text"] for x in tags["spatial_signal"] if x["id"] == e["trigger"]]
                if not prepositions:
                    continue
                prep = prepositions[0]
                if prep in stats[name].keys():
                    stats[name][prep] += 1
                    continue
                stats[name][prep] = 1

    return stats


def most_common_motion_verbs(contents: list):
    """Returns 5 most common motion verbs.

    Args:
        contents (list): List of contents containing Tags.
    Returns:
        dict: Contains the most-used verbs as keys and their counts as values.
    """
    count = {}
    for content in contents:
        tags = content["tags"]
        # Count all motion verbs.
        for verb in tags["motion"]:
            if verb["text"] in count.keys():
                count[verb["text"]] += 1
                continue
            count[verb["text"]] = 1

    verbs = list(count.keys())

    # Comparator function.
    def appearances(v):
        return count[v]

    verbs.sort(key=appearances)
    return {i: count[i] for i in verbs[:5]}


def main():
    """Quick usage example.
    """
    print("stats.py\n" + __doc__)


if __name__ == "__main__":
    main()

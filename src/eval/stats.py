#!/usr/bin/env python
"""Analyzer Tool for preprocessed Dictionaries containing Token and IsoSpace data.
"""


def pos_count(tags: dict):
    """Counts Part of Speech tags in tokens.

    Args:
        tags (dict): Tags containing Tokens.
    Returns:
        dict: PoS as keys and counts as values.
    """

    stats = {}
    for token in tags["token"]:
        if token["pos"] in stats.keys():
            stats[token["pos"]] += 1
            continue
        stats[token["pos"]] = 1
    return stats


def iso_space_count(tags: dict):
    """Counts Iso Space tags in tokens.

    Args:
        tags (dict): Tags.
    Returns:
        dict: Iso Space tags as keys and counts as values.
    """

    stats = {}
    for name in tags.keys():
        if not name == "token":
            stats[name] = len(tags[name]) if type(tags[name]) == list else 1
    return stats


def qs_link_types(tags: dict):
    """Counts QS-Link types.

    Args:
        tags (dict): Tags containing QS-Links.
    Returns:
        dict: QS-Link types as keys and counts as values.
    """

    stats = {}
    for link in tags["qslink"]:
        if link["reltype"] in stats.keys():
            stats[link["reltype"]] += 1
            continue
        stats[link["reltype"]] = 1
    return stats


def sentence_lengths(tags: dict):
    """Counts sentence lengths from list of tokens.

    Args:
        tags (dict): Tags containing tokens with sentence start markers.
    Returns:
        dict: Dictionary with Sentence length as keys and counts as values.
    """

    stats = {}
    length = 1
    # Used to ignore first sentence (length = 0)
    first = True
    for token in tags["tokens"]:
        # Ignore punctuation for sentence length
        length += 0 if token["text"] in [".", ",", ";", ":"] else 1
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


def link_prepositions_count(tags: dict):
    """Counts Prepositions that triggered QS/O-Links.

    Args:
        tags (dict): Tags containing information.
    Returns:
        dict: Contains dictionaries with 2 keys, "qslink" and "olink, both containing more info.
    """
    stats = {"qslink": {}, "olink": {}}
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


def most_common_motion_verbs(tags: dict):
    """Returns 5 most common motion verbs.

    Args:
        tags (dict): Tags containing motion-verbs.
    Returns:
        dict: Contains the most-used verbs as keys and their counts as values.
    """
    count = {}
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

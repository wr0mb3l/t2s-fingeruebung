#!/usr/bin/env python
"""Part of Speech Tagger and Tokenizer using Spacy.
"""

import spacy

__nlp = spacy.load("en_core_web_sm")


def analyze(content: str):
    doc = __nlp(content)
    result = []
    id = 0
    for token in doc:
        result.append({"id": id,
                      "start": token.i,
                      "end": token.i + len(token.text),
                      "text": token.text,
                      "pos": token.pos_,
                      "sentence": token.is_sent_start
                      })
        id += 1
    return result


def main():
    """Quick usage example.
    """
    print("pos.py\n" + __doc__)

    print(analyze("Apple is looking at buying U.K. startup for $1 billion"))


if __name__ == "__main__":
    main()

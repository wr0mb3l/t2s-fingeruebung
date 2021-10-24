#!/usr/bin/env python
"""Parser between XML containing ISOSpace and JSON.
"""

import json
import xmltodict


def xml_to_dict(xml_str: str):
    dic = xmltodict.parse(xml_str)
    return dic


def xml_to_json(xml_str: str):
    return json.dumps(xml_to_dict(xml_str))


def main():
    """Quick usage example.
    """
    print("parser.py\n" + __doc__)
    xml_data = """
        <student>
            <id>DEL</id>
            <name> Jack </name>
            <email>jack@example.com</email>
            <semseter>8</semseter>
            <class>CSE</class>
            <cgpa> 7.5</cgpa>
        </student>
    """
    print(xml_to_json(xml_data))


if __name__ == "__main__":
    main()

#!/usr/bin/env python
"""Parser between XML containing ISOSpace and JSON.
"""
import collections

import json
import xmltodict


def xml_to_dict(xml_str: str):
    def postprocessor(path, key, value):
        try:
            return key.lower(), int(value)
        except (ValueError, TypeError):
            return key.lower(), value
    return xmltodict.parse(xml_str, attr_prefix="", dict_constructor=dict, postprocessor=postprocessor)


def xml_to_json(xml_str: str):
    return json.dumps(xml_to_dict(xml_str))


def json_to_dict(json_str: str):
    return json.loads(json_str)


def dict_to_json(dic: dict):
    return json.dumps(dic)


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

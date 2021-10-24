#!/usr/bin/env python
"""Parser between XML containing ISOSpace and JSON.
"""
import collections

import json
import xmltodict


def postprocessor(path, key, value):
    """Postprocessor used for XML to Dictionary conversion.

    Converts Boolean and Numeric values from str and makes all keys lowercase.


    """
    try:
        # Boolean Values
        if value == "TRUE":
            return key.lower(), True
        elif value == "FALSE":
            return key.lower(), False
        # Convert numeric values from str
        return key.lower(), int(value)
    except (ValueError, TypeError):
        return key.lower(), value


def xml_to_dict(xml_str: str):
    """Converts XML string to python Dictionary. Applies Postprocessor.

    Args:
        xml_str (str): XML String to convert.

    Returns:
        dict: Dictionary containing all XML contents.
    """
    return xmltodict.parse(xml_str, attr_prefix="", dict_constructor=dict, postprocessor=postprocessor)


def dict_to_json(dic: dict):
    """Converts Python Dictionary JSON string.

    Args:
        dic (dict): Dictionary to convert.

    Returns:
        str: JSON String.
    """
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
    print(dic := xml_to_dict(xml_data))
    print(dict_to_json(dic))


if __name__ == "__main__":
    main()

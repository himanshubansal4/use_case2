import json
import os.path

file_name = os.path.dirname(__file__) + "/../data.json"


def read_data():
    """
    :return: json file in dictionary consisting of city and state
    """
    f = open(file_name)
    query_set = json.load(f)
    return query_set


def get_suggestions(inp_val):
    """
    :param inp_val: the pattern for martching city
    :return: list of city matching with the pattern
    """
    data = read_data()
    return list(filter(lambda x: inp_val.lower() in x["name"].lower(), data))


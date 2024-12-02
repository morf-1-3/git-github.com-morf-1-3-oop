import os
import json

PATH = os.path.abspath(__file__ + "/..")
PATH_JSON = PATH + "/filebd.json"

def load_data():
    try:
        with open(PATH_JSON, "r") as file:
            result = json.load(file)
            return result
    except FileNotFoundError:
        result = dict()
        return result
import os
import json

PATH = os.path.abspath(__file__ + "/..")
PATH_JSON = PATH + "/filebd.json"

def save_data(obj):
    with open(PATH_JSON, "w") as file:
        json.dump(obj, file,indent=0)
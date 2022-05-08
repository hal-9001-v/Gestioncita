import os
import random
import json

file_path = os.path.dirname(__file__) + "\\Json\\"

test_path = file_path + "text.json"


def write_file(file, values):
    file = open(file, "w")
    file.write(json.dumps(values))
    file.close()


val = {"Jiji": "pinguino", "Caquitas": [{"Caquita 1": "Hola"},{"Caquita 2": "Hola"} ]}

write_file(test_path, val)

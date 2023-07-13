import random
import os
import json


def read_from_file(file_name):
    if not os.path.exists(file_name):
        return []

    with open(file_name, 'r') as file:
        return json.load(file)


def write_to_file(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file)


def generate_pin():
    return str(random.randint(1000, 9999))

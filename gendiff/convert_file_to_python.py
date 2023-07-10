import json
import yaml


def convert(file_path):
    if file_path.endswith('.json'):
        with open(file_path, 'r') as file:
            file = dict(json.load(file))
    if file_path.endswith('.yaml') or file_path.endswith('.yml'):
        with open(file_path, 'r') as file:
            file = yaml.load(file, Loader=yaml.SafeLoader)
    return file

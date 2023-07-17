import json
import yaml
import sys


def convert_to_dict(file_path):
    if file_path.lower().endswith('.json'):
        with open(file_path, 'r') as file:
            file = dict(json.load(file))
    elif file_path.lower().endswith(('.yaml', '.yml')):
        with open(file_path, 'r') as file:
            file = yaml.load(file, Loader=yaml.SafeLoader)

    try:
        return file
    except UnboundLocalError:
        print(
            f'{file_path} has the wrong extension. '
            f'Possible file extensions: yml, yaml, json'
        )
        sys.exit()

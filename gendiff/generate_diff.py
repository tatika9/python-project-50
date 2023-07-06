import json


def lower_bool(text):
    if type(text) == bool:
        return str(text).lower()
    return text


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as file1:
        file1 = dict(json.load(file1))
    with open(file_path2, 'r') as file2:
        file2 = dict(json.load(file2))
    all_keys = set(file1.keys()) | set(file2.keys())
    result = []
    for key in sorted(all_keys):
        if file1.get(key) == file2.get(key):
            result.append(f'    {key}: {lower_bool(file1.get(key))}')
            continue
        if key not in file1:
            result.append(f'  + {key}: {lower_bool(file2.get(key))}')
            continue
        if key not in file2:
            result.append(f'  - {key}: {lower_bool(file1.get(key))}')
            continue
        result.append(f'  - {key}: {lower_bool(file1.get(key))}')
        result.append(f'  + {key}: {lower_bool(file2.get(key))}')
    result = '{\n' + '\n'.join(result) + '\n}'
    return result

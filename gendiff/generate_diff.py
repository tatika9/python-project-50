from gendiff.convert_file_to_python import convert


def lower_bool(text):
    if type(text) == bool:
        return str(text).lower()
    if text is None:
        return 'null'
    return text


def generate_diff(file_path1, file_path2):
    dict1 = convert(file_path1)
    dict2 = convert(file_path2)

    all_keys = set(dict1.keys()) | set(dict2.keys())
    result = []
    for key in sorted(all_keys):
        if dict1.get(key) == dict2.get(key):
            result.append(f'    {key}: {lower_bool(dict1.get(key))}')
            continue
        if key not in dict1:
            result.append(f'  + {key}: {lower_bool(dict2.get(key))}')
            continue
        if key not in dict2:
            result.append(f'  - {key}: {lower_bool(dict1.get(key))}')
            continue
        result.append(f'  - {key}: {lower_bool(dict1.get(key))}')
        result.append(f'  + {key}: {lower_bool(dict2.get(key))}')
    return '{\n' + '\n'.join(result) + '\n}'

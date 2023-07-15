from gendiff.conversion import convert_to_dict
from gendiff.diff_parser import get_diff
from gendiff.formatters.format import get_format


def generate_diff(file_path1, file_path2, format='stylish'):
    dict1 = convert_to_dict(file_path1)
    dict2 = convert_to_dict(file_path2)
    diff = get_diff(dict1, dict2)

    return get_format(diff, format)

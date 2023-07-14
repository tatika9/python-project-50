from gendiff.convert_file_to_python import convert
from gendiff.parser_diff import get_diff
from gendiff.format import get_format


def generate_diff(file_path1, file_path2, format='stylish'):
    dict1 = convert(file_path1)
    dict2 = convert(file_path2)
    diff = get_diff(dict1, dict2)

    return get_format(diff, format)

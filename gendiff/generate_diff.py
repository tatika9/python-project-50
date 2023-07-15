from gendiff.convert_file_to_python import convert
from gendiff.parser_diff import get_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import get_json


def get_format(diff, format):
    if format == 'stylish':
        return stylish(diff)
    if format == 'plain':
        return plain(diff)
    if format == 'json':
        return get_json(diff)


def generate_diff(file_path1, file_path2, format='stylish'):
    dict1 = convert(file_path1)
    dict2 = convert(file_path2)
    diff = get_diff(dict1, dict2)

    return get_format(diff, format)
